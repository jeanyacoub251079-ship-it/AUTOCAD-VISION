"""Moteur de calcul structurel local (§2.4.6).

Flux pour une option générée :
1. Construction du modèle global (poteaux, poutres, voiles, niveaux) — les
   dalles sont converties en charges uniformes réparties sur les barres de
   leur contour (répartition tributaire uniforme : somme de charge exactement
   conservée, approximation documentée).
2. Cas de charges unitaires G, Q, S, W, E ; combinaisons ELU/ELS EC0 + AN FR
   appliquées comme facteurs de combinaison.
3. Analyse : PyNite (éléments finis 3D, unités kN-m) si disponible, sinon
   modèle analytique de repli (poutres bi-articulées, majorant) — le deux
   chemins produisent la même structure de résultats.
4. Les vérifications EC2/EC8 sont dans engine.py.

Hypothèses assumées (repris dans le rapport) :
- dalles bi-articulées par panneau (majorant) ;
- poutres continues aux nœuds mais sans redistribution plastique ;
- encastrement parfait en base (tassements vus au module fondations) ;
- second ordre poteaux par raideur nominale (fluage ignoré) ;
- séisme/vent statique équivalent.
"""
from __future__ import annotations

import math
from typing import Any

from ..logging_setup import get_logger
from . import codes

log = get_logger("structai.calc")

try:
    from Pynite import FEModel3D  # PyNiteFEA  (unités kN, m)
    HAS_PY_NITE = True
except Exception:
    try:
        from Pynite import FEModel3D  # type: ignore  # noqa: F811
        HAS_PY_NITE = True
    except Exception:
        FEModel3D = None
        HAS_PY_NITE = False

EPS = 1e-6
CASES = ("G", "Q", "S", "W", "E")


# ---------------------------------------------------------------------------
# Géométrie
# ---------------------------------------------------------------------------

def _intersect(p1, p2, p3, p4):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if abs(d) < EPS:
        return None
    t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / d
    u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / d
    if -0.02 <= t <= 1.02 and -0.02 <= u <= 1.02:
        return (round(x1 + t * (x2 - x1), 4), round(y1 + t * (y2 - y1), 4))
    return None


def _poly_bbox(poly):
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    return min(xs), min(ys), max(xs), max(ys)


def _poly_area(poly) -> float:
    n = len(poly)
    a = 0.0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0


def _near(a, b, tol=0.05) -> bool:
    return abs(a[0] - b[0]) < tol and abs(a[1] - b[1]) < tol


def _live_load(proj: dict) -> float:
    usage = str(proj.get("usage", "habitation"))
    base = codes.LIVE_LOADS.get(usage, codes.LIVE_LOADS["habitation"])
    return float(proj.get("q_exploitation_kpa", base["q"]))


class Model:
    """Modèle global multi-étages (barres + charges par cas)."""

    def __init__(self, option: dict, proj: dict, gen_settings: dict | None = None):
        st = option.get("structure", {})
        self.proj = proj or {}
        self.gen = gen_settings or {}
        self.niveaux = int(self.proj.get("niveaux", 1) or 1)
        self.h_etage = float(self.proj.get("hauteur_etage", 2.8) or 2.8)
        self.classe_beton = str((option.get("meta") or {}).get("classe_beton", "C25/30"))
        self.members: dict[str, dict] = {}
        self.nodes: dict[tuple, dict] = {}
        self.panels: list[dict] = []
        self.surface_par_niveau: dict[int, float] = {}
        self.seis_mass: dict[int, float] = {}
        self.lateral: dict[int, dict[str, float]] = {}
        self.warnings: list[str] = []
        self._build(st)

    # -- construction --------------------------------------------------------
    def _node(self, x, y, z) -> tuple:
        key = (round(x, 4), round(y, 4), round(z, 3))
        if key not in self.nodes:
            self.nodes[key] = {}
        return key

    def _add_member(self, mid: str, n1, n2, b: float, h: float, mtype: str,
                    concrete: str, extra: dict | None = None):
        self.members[mid] = {"n1": n1, "n2": n2, "b": b, "h": h, "type": mtype,
                             "concrete": concrete,
                             "loads": {c: (0.0, 0.0) for c in CASES}}
        if extra:
            self.members[mid].update(extra)

    def _split_points(self, a, b, all_lines) -> list:
        pts = [a, b]
        for (c, d) in all_lines:
            p = _intersect(a, b, c, d)
            if p and p not in (a, b):
                pts.append(p)
        dx, dy = b[0] - a[0], b[1] - a[1]
        L2 = dx * dx + dy * dy
        uniq = []
        for p in sorted(pts, key=lambda q: ((q[0] - a[0]) * dx + (q[1] - a[1]) * dy) / max(L2, EPS)):
            if not uniq or math.dist(uniq[-1], p) > 0.02:
                uniq.append(p)
        return uniq

    def _build(self, st: dict):
        cols = st.get("poteaux", []) or []
        beams = st.get("poutres", []) or []
        walls = st.get("voiles", []) or []
        slabs = st.get("dalles", []) or []
        beam_lines = [(tuple(b["debut"]), tuple(b["fin"])) for b in beams]
        wall_lines = [(tuple(w["debut"]), tuple(w["fin"])) for w in walls]
        all_lines = beam_lines + wall_lines

        # --- barres horizontales par niveau : poutres + voiles (chaînage) ---
        for level in range(1, self.niveaux + 1):
            z = level * self.h_etage
            for bm in beams:
                if int(bm.get("niveau", level)) != level:
                    continue
                b, h = bm["section"]
                a, c = tuple(bm["debut"]), tuple(bm["fin"])
                pts = self._split_points(a, c, all_lines)
                for i in range(len(pts) - 1):
                    if math.dist(pts[i], pts[i + 1]) < 0.02:
                        continue
                    mid = f"{bm['id']}@{level}#{i}"
                    n1 = self._node(*pts[i], z)
                    n2 = self._node(*pts[i + 1], z)
                    self._add_member(mid, n1, n2, b, h, "poutre",
                                     _cls(bm.get("materiau")) or self.classe_beton,
                                     {"id": bm["id"], "niveau": level})
            for w in walls:
                lv = w.get("niveaux") or [0, self.niveaux - 1]
                if not (min(lv) + 1 <= level <= max(lv) + 1):
                    continue
                a, c = tuple(w["debut"]), tuple(w["fin"])
                pts = self._split_points(a, c, all_lines)
                t = float(w.get("epaisseur", 0.20))
                for i in range(len(pts) - 1):
                    if math.dist(pts[i], pts[i + 1]) < 0.02:
                        continue
                    mid = f"{w['id']}@{level}#{i}"
                    n1 = self._node(*pts[i], z)
                    n2 = self._node(*pts[i + 1], z)
                    Lseg = math.dist(pts[i], pts[i + 1])
                    self._add_member(mid, n1, n2, t, max(Lseg, 0.5), "voile-h",
                                     _cls(w.get("materiau")) or self.classe_beton,
                                     {"id": w["id"], "niveau": level})
        # --- poteaux ---
        for c_ in cols:
            x, y = c_["position"]
            lv = c_.get("niveaux") or [0, self.niveaux - 1]
            z0, z1 = min(lv) * self.h_etage, (max(lv) + 1) * self.h_etage
            b, h = c_.get("section", [0.30, 0.30])
            n0 = self._node(x, y, z0)
            n1 = self._node(x, y, z1)
            mid = f"{c_['id']}#col"
            self._add_member(mid, n0, n1, b, h, "poteau",
                             _cls(c_.get("materiau")) or self.classe_beton,
                             {"id": c_["id"], "z0": z0, "z1": z1, "niveaux": lv})
        # --- charges des dalles sur les barres de contour ---
        self._assign_slab_loads(slabs, beams, walls)

    def _panel_boundary_members(self, bbox, level):
        x0, y0, x1, y1 = bbox
        out = []
        for mid, m in self.members.items():
            if m["type"] not in ("poutre", "voile-h") or m.get("niveau") != level:
                continue
            mx = (m["n1"][0] + m["n2"][0]) / 2
            my = (m["n1"][1] + m["n2"][1]) / 2
            if x0 - 0.4 <= mx <= x1 + 0.4 and y0 - 0.4 <= my <= y1 + 0.4:
                out.append(mid)
        return out

    def _assign_slab_loads(self, slabs, beams, walls):
        for sl in slabs:
            poly = sl.get("polygone") or []
            if len(poly) < 3:
                continue
            area = _poly_area(poly)
            if area <= 0.1:
                continue
            bbox = _poly_bbox(poly)
            level = int(sl.get("niveau", 1))
            t = float(sl.get("epaisseur", 0.20))
            roof = bool(sl.get("toiture", level >= self.niveaux))
            g_surf = t * codes.GAMMA_CONCRETE + (1.2 if roof else
                     codes.FINISHES_KPA + codes.PARTITIONS_KPA + codes.CEILING_KPA)
            q_live = _live_load(self.proj) * (1.0 if not roof else float(self.proj.get("q_exploitation_comble_kpa", 0.5)))
            sk = 0.0
            psi0_s = 0.0
            if roof:
                sk, _ = codes.snow_load_sk(str(self.proj.get("zone_neige", "A2")),
                                           float(self.proj.get("altitude", 50) or 50))
                sk *= codes.SNOW_MU_FLAT
                psi0_s = float(codes.SNOW_ZONES.get(str(self.proj.get("zone_neige", "A2")),
                                                    codes.SNOW_ZONES["A2"])["psi0"])
            members = self._panel_boundary_members(bbox, level)
            perim = sum(math.dist(m["n1"][:2], m["n2"][:2]) for m in map(self.members.get, members))
            perim = max(perim, 0.5)
            wG = g_surf * area / perim
            wQ = q_live * area / perim
            wS = sk * area / perim if roof else 0.0
            for mid in members:
                mm = self.members[mid]
                for case, w in (("G", wG), ("Q", wQ), ("S", wS)):
                    a, b = mm["loads"][case]
                    mm["loads"][case] = (a + w, b + w)
            self.panels.append({"id": sl.get("id"), "niveau": level, "bbox": bbox,
                                "aire": area, "epaisseur": t, "toiture": roof,
                                "g_surf": g_surf, "q_live": q_live, "sk": sk,
                                "sens": sl.get("sens_portee", "court")})
            self.surface_par_niveau[level] = self.surface_par_niveau.get(level, 0.0) + area
        # poids propre barres
        for mid, m in self.members.items():
            if m["type"] == "poteau":
                w = m["b"] * m["h"] * codes.GAMMA_CONCRETE
                z = m["z1"] - m["z0"]
                m["self_w"] = (w * z, w * z)   # total en kN
            elif m["type"] == "poutre":
                t_dalle = max((p["epaisseur"] for p in self.panels if p["niveau"] == m.get("niveau")),
                              default=0.2)
                h_web = max(m["h"] - t_dalle, 0.08)
                w = m["b"] * h_web * codes.GAMMA_CONCRETE
                m["loads"]["G"] = (m["loads"]["G"][0] + w, m["loads"]["G"][1] + w)
            elif m["type"] == "voile-h":
                t_dalle = max((p["epaisseur"] for p in self.panels if p["niveau"] == m.get("niveau")),
                              default=0.2)
                w = m["b"] * max(m["h"] - t_dalle, 0.0) * codes.GAMMA_CONCRETE * 0.0  # poids du voile vu au §vertical
        self.psi0_s = max((p.get("sk", 0.0) and _psi0s(self.proj)) or 0.0 for p in self.panels) \
            if any(p.get("sk", 0) for p in self.panels) else 0.0

        # --- séisme / vent par niveau ---
        W = {}
        for level, surf in self.surface_par_niveau.items():
            g = sum(p["g_surf"] for p in self.panels if p["niveau"] == level) / max(
                sum(1 for p in self.panels if p["niveau"] == level), 1)
            W[level] = g * surf  # kN
        psi2 = codes.LIVE_LOADS.get(str(self.proj.get("usage", "habitation")),
                                    codes.LIVE_LOADS["habitation"])["psi2"]
        self.W_seis = {lvl: w * (1.0 + psi2) for lvl, w in W.items()}  # poids sismique W = G + ψ2Q (kN)
        zone = int(self.proj.get("zone_sismique", 2) or 2)
        qb = codes.wind_reference_pressure(int(self.proj.get("zone_vent", 2) or 2))["qb_kpa"]
        emprise = self.proj.get("emprise") or {}
        largeur = float(emprise.get("largeur", 12.5) or 12.5)
        self.qb = qb
        self.largeur = largeur
        Fb = 0.0
        if zone >= 2:
            ag = codes.SEISME_AGR.get(zone, 0.7) * codes.IMPORTANCE_GAMMA_I.get(
                str(self.proj.get("categorie_importance", "II")), 1.0)
            soil = codes.SOIL_TYPES.get(str(self.proj.get("classe_sol", "A")), codes.SOIL_TYPES["A"])
            qy = float(self.proj.get("q_comportement", 3.0) or 3.0)
            dc = str(self.proj.get("classe_ductilite", "DCM"))
            system = str(self.proj.get("systeme_sismique", "portique"))
            T1 = codes.estimate_fundamental_period(self.niveaux, system)
            spec = codes.seismic_spectral_acceleration(T1, ag, soil, 1.0, qy, dc)
            Wtot = sum(self.W_seis.values())
            Fb = spec["Sd_m_s2"] / codes.G_ACC * Wtot
            s = sum(w * lvl * self.h_etage for lvl, w in self.W_seis.items()) or 1.0
            for level, w in self.W_seis.items():
                self.lateral.setdefault(level, {})["E"] = Fb * w * (level * self.h_etage) / s
            self.Vb = Fb
        else:
            self.Vb = 0.0
        for level in range(1, self.niveaux + 1):
            Fw = qb * largeur * self.h_etage * 1.0  # kN/niveau (cpe−cpi≈1.0, simplifié)
            self.lateral.setdefault(level, {})["W"] = Fw
            self.lateral[level].setdefault("E", 0.0)

    # ------------------------------------------------------------------
    # Combinaisons
    # ------------------------------------------------------------------
    def combination_cases(self) -> list[dict]:
        has_snow = any(abs(m["loads"]["S"][0]) > EPS for m in self.members.values())
        psi0_s = float(codes.SNOW_ZONES.get(str(self.proj.get("zone_neige", "A2")),
                                            codes.SNOW_ZONES["A2"])["psi0"])
        gU, gQ = codes.GAMMA_G_INFAVORABLE, codes.GAMMA_Q
        out = [
            {"id": "ELU-1", "type": "ELU", "expression": "1.35G + 1.5Q",
             "f": {"G": gU, "Q": gQ, "S": 0.0, "W": 0.0, "E": 0.0}},
            {"id": "ELS-car", "type": "ELS", "expression": "G + Q",
             "f": {"G": 1.0, "Q": 1.0, "S": 0.0, "W": 0.0, "E": 0.0}},
            {"id": "ELS-qp", "type": "ELS", "expression": "G + ψ2·Q",
             "f": {"G": 1.0, "Q": _psi2(self.proj), "S": 0.0, "W": 0.0, "E": 0.0}},
        ]
        if has_snow:
            out.insert(1, {"id": "ELU-2", "type": "ELU", "expression": "1.35G + 1.5S",
                           "f": {"G": gU, "Q": 0.0, "S": gQ, "W": 0.0, "E": 0.0}})
            if psi0_s > 0:
                out.insert(2, {"id": "ELU-2b", "type": "ELU", "expression": "1.35G + 1.5Q + 1.5ψ0S·S",
                               "f": {"G": gU, "Q": gQ, "S": gQ * psi0_s, "W": 0.0, "E": 0.0}})
        out.append({"id": "ELU-3", "type": "ELU", "expression": "1.35G + 1.5Q + 1.5ψ0W·W",
                    "f": {"G": gU, "Q": gQ, "S": 0.0, "W": gQ * 0.5, "E": 0.0}})
        out.append({"id": "ELS-car-W", "type": "ELS", "expression": "G + W",
                    "f": {"G": 1.0, "Q": 0.0, "S": 0.0, "W": 1.0, "E": 0.0}})
        out.append({"id": "ELU-acc-E", "type": "ELU-acc", "expression": "G + ψ2Q + E",
                    "f": {"G": 1.0, "Q": _psi2(self.proj), "S": 0.0, "W": 0.0, "E": 1.0}})
        if _favorable(self.proj):
            out.append({"id": "ELU-acc-E2", "type": "ELU-acc", "expression": "0.8G + E",
                        "f": {"G": 0.8, "Q": 0.0, "S": 0.0, "W": 0.0, "E": 1.0}})
        return out

    # ------------------------------------------------------------------
    # Solveurs
    # ------------------------------------------------------------------
    def solve(self, verbose: bool = False) -> dict:
        combos = self.combination_cases()
        use_fe = HAS_PY_NITE and len(self.members) <= 600
        if use_fe:
            try:
                res = self._solve_fe(combos, verbose=verbose)
                res["methode"] = "elements_finis_pinite"
                res["combos"] = combos
                return res
            except Exception as exc:
                log.warning("Échec FE (%s) — repli analytique.", exc)
                self.warnings.append(f"Analyse FE indisponible ({exc}) — modèle analytique de repli.")
        res = self._solve_analytic(combos)
        res["methode"] = "analytique_repli"
        res["combos"] = combos
        return res

    # -- FE PyNite ---------------------------------------------------------
    def _solve_fe(self, combos, verbose=False) -> dict:
        model = FEModel3D()
        for cname in {m["concrete"] for m in self.members.values()} | {self.classe_beton}:
            p = codes.concrete_props(cname)
            model.add_material(f"BE{cname}", E=p["Ecm"] * 1e3,  # MPa->kN/m²
                               G=11e6, nu=0.2, rho=codes.GAMMA_CONCRETE)
        for mid, m in self.members.items():
            model.add_section(f"SEC{mid}", A=m["b"] * m["h"],
                              Iy=m["h"] * m["b"] ** 3 / 12.0,
                              Iz=m["b"] * m["h"] ** 3 / 12.0,
                              J=max(0.1 * m["b"] * m["h"] ** 3, 1e-6))
        node_names = {nk: f"N{i}" for i, nk in enumerate(self.nodes)}
        for nk, nm in node_names.items():
            model.add_node(nm, nk[0], nk[1], nk[2])
        for nk in self.nodes:
            if abs(nk[2]) <= EPS:
                model.def_support(node_names[nk], True, True, True, True, True, True)
        for mid, m in self.members.items():
            model.add_member(mid, node_names[m["n1"]], node_names[m["n2"]],
                             f"BE{m['concrete']}", f"SEC{mid}")
        # charges unitaires par cas
        for mid, m in self.members.items():
            if m["type"] == "poteau":
                wtot, _ = m.get("self_w", (0.0, 0.0))
                if wtot:
                    Lz = max(m["z1"] - m["z0"], EPS)
                    w = wtot / Lz
                    model.add_member_dist_load(mid, "Fz", -w, -w, case="G")
                continue
            for case in ("G", "Q", "S"):
                w1, w2 = m["loads"][case]
                if abs(w1) + abs(w2) > EPS:
                    model.add_member_dist_load(mid, "Fz", -w1, -w2, case=case)
        # charges latérales nodales (réparties sur les nœuds du plancher)
        per_level_nodes: dict[int, list] = {}
        for nk, nm in node_names.items():
            if nk[2] > EPS:
                per_level_nodes.setdefault(int(round(nk[2] / self.h_etage)), []).append(nm)
        for level, loads in self.lateral.items():
            nodes = per_level_nodes.get(level) or []
            if not nodes:
                continue
            for case, F in loads.items():
                if not F:
                    continue
                f = F / len(nodes)
                for nm in nodes:
                    model.add_node_load(nm, "FX", -f, case=case)
        for c in combos:
            model.add_load_combo(c["id"], dict(c["f"]))
        model.analyze(check_stability=False, log=verbose)

        results: dict[str, Any] = {"members": {}, "reactions": {}, "displacements": {},
                                   "warnings": list(self.warnings)}
        for mid, m in self.members.items():
            mem = model.members[mid]
            slot = {"M": 0.0, "V": 0.0, "N": 0.0, "d": 0.0, "M_combo": "", "combos": {}}
            for c in combos:
                cid = c["id"]
                try:
                    My = max(abs(mem.max_moment("My", cid)), abs(mem.min_moment("My", cid)))
                    Mz = max(abs(mem.max_moment("Mz", cid)), abs(mem.min_moment("Mz", cid)))
                    Vy = max(abs(mem.max_shear("Fy", cid)), abs(mem.min_shear("Fy", cid)))
                    Vz = max(abs(mem.max_shear("Fz", cid)), abs(mem.min_shear("Fz", cid)))
                    Nn = max(abs(mem.max_axial(cid)), abs(mem.min_axial(cid)))
                    dz = max(abs(mem.max_deflection("dz", cid)), abs(mem.min_deflection("dz", cid)))
                except Exception:
                    continue
                vals = {"M_kNm": round(max(My, Mz), 2), "V_kN": round(max(Vy, Vz), 2),
                        "N_kN": round(Nn, 2), "d_mm": round(dz * 1000.0, 3)}
                slot["combos"][cid] = vals
                if vals["M_kNm"] >= slot["M"]:
                    slot.update({"M": vals["M_kNm"], "V": max(slot["V"], vals["V_kN"]),
                                 "N": max(slot["N"], vals["N_kN"]), "d": vals["d_mm"],
                                 "M_combo": cid})
            results["members"][mid] = slot
        for nk, nm in node_names.items():
            node = model.nodes[nm]
            rslot = {"R": 0.0, "R_combo": "", "combos": {}, "MX": 0.0}
            for c in combos:
                cid = c["id"]
                try:
                    rz = abs(node.RxnFZ.get(cid, 0.0) or 0.0)
                    rx = abs(node.RxnMY.get(cid, 0.0) or 0.0) if hasattr(node, "RxnMY") else 0.0
                except Exception:
                    rz = rx = 0.0
                rslot["combos"][cid] = {"Rz_kN": round(rz, 1), "Mx_kNm": round(rx, 1)}
                if c["type"] == "ELU" and rz > rslot["R"]:
                    rslot["R"] = round(rz, 1)
                    rslot["R_combo"] = cid
            if nk[2] <= EPS:
                results["reactions"][nk] = rslot
        # déplacements latéraux par niveau et par combo
        disp = {}
        for c in combos:
            cid = c["id"]
            if cid not in ("ELU-3", "ELU-acc-E", "ELU-acc-E2"):
                continue
            for nk, nm in node_names.items():
                if nk[2] <= EPS:
                    continue
                u = abs(model.nodes[nm].DX.get(cid, 0.0) or 0.0)
                level = int(round(nk[2] / self.h_etage))
                disp[level] = max(disp.get(level, 0.0), u)
        results["displacements"]["levels_mm"] = {lvl: round(u * 1000.0, 2) for lvl, u in disp.items()}
        return results

    # -- Analytique (repli) -----------------------------------------------
    def _solve_analytic(self, combos) -> dict:
        results = {"members": {}, "reactions": {}, "displacements": {"levels_mm": {}},
                   "warnings": list(self.warnings)}
        base_react: dict[tuple, dict[str, float]] = {}
        for mid, m in self.members.items():
            if m["type"] == "poteau":
                continue
            L = max(math.dist(m["n1"][:2], m["n2"][:2]), 0.05)
            slot = {"M": 0.0, "V": 0.0, "N": 0.0, "d": 0.0, "M_combo": "", "combos": {}}
            for c in combos:
                f = c["f"]
                wG = (m["loads"]["G"][0] + m["loads"]["G"][1]) / 2 * f["G"]
                wQ = (m["loads"]["Q"][0] + m["loads"]["Q"][1]) / 2 * f["Q"]
                wS = (m["loads"]["S"][0] + m["loads"]["S"][1]) / 2 * f["S"]
                w = wG + wQ + wS
                M = w * L * L / 8.0
                V = w * L / 2.0
                E = codes.concrete_props(m["concrete"])["Ecm"] * 1e3
                Izz = m["b"] * m["h"] ** 3 / 12.0
                d = 5 * w * L ** 4 / (384 * E * max(Izz, 1e-9))
                vals = {"M_kNm": round(M, 2), "V_kN": round(V, 2), "N_kN": 0.0,
                        "d_mm": round(d * 1000.0, 3)}
                slot["combos"][c["id"]] = vals
                if M >= slot["M"]:
                    slot.update({"M": vals["M_kNm"], "V": max(slot["V"], V), "d": vals["d_mm"],
                                 "M_combo": c["id"]})
                for nk in (m["n1"], m["n2"]):
                    br = base_react.setdefault(nk, {})
                    br[c["id"]] = br.get(c["id"], 0.0) + V
            results["members"][mid] = slot
        for nk, combos_r in base_react.items():
            rslot = {"R": 0.0, "R_combo": "", "combos": {}, "MX": 0.0}
            for cid, val in combos_r.items():
                rslot["combos"][cid] = {"Rz_kN": round(val, 1), "Mx_kNm": 0.0}
            elu = [v for cid, v in rslot["combos"].items() if any(
                c["id"] == cid and c["type"] == "ELU" for c in combos)]
            if elu:
                rslot["R"] = round(max(elu), 1)
                rslot["R_combo"] = "ELU"
            results["reactions"][nk] = rslot
        # poteaux : effort normal cumulé descendant par axe de poteau
        col_lines: dict[tuple, list[tuple]] = {}
        for mid, m in self.members.items():
            if m["type"] == "poteau":
                col_lines.setdefault((round(m["n2"][0], 3), round(m["n2"][1], 3)), []).append(mid)
        for xy, mids in col_lines.items():
            mids_sorted = sorted(mids, key=lambda mm: self.members[mm]["z0"])
            N_above: dict[str, float] = {}
            for mid in mids_sorted:
                m = self.members[mid]
                slot = {"M": 0.0, "V": 0.0, "N": 0.0, "d": 0.0, "M_combo": "", "combos": {}}
                for c in combos:
                    cid = c["id"]
                    N = N_above.get(cid, 0.0)
                    # somme des tranchants des barres aboutissant au nœud haut
                    for other, om in self.members.items():
                        if om["type"] == "poteau":
                            continue
                        if abs(om["n1"][2] - m["z1"]) > 0.01 and abs(om["n2"][2] - m["z1"]) > 0.01:
                            continue
                        if not (_near(om["n1"][:2], xy) or _near(om["n2"][:2], xy)):
                            continue
                        rr = results["members"].get(other, {}).get("combos", {}).get(cid, {})
                        N += rr.get("V_kN", 0.0)
                    wtot, _ = m.get("self_w", (0.0, 0.0))
                    N += wtot * c["f"]["G"]
                    N_above[cid] = N
                    # effort tranchant d'étage approx réparti sur les poteaux du noyau
                    lat = sum(self.lateral.get(int(round(m["z1"] / self.h_etage)), {}).values())
                    V_et = lat * c["f"]["E"] if c["type"] == "ELU-acc" else (
                        lat * c["f"]["W"] if cid == "ELU-3" else 0.0)
                    V_et = V_et / max(len(col_lines), 1)
                    M_pied = V_et * self.h_etage / 2.0
                    slot["combos"][cid] = {"M_kNm": round(M_pied, 2), "V_kN": round(V_et, 2),
                                           "N_kN": round(N, 1), "d_mm": 0.0}
                    if N >= slot["N"]:
                        slot.update({"N": round(N, 1), "M": round(M_pied, 2), "V": round(V_et, 2),
                                     "M_combo": cid})
                results["members"][mid] = slot
        # dérives : portique + voiles, modèle cisaillement par niveau
        cum: dict[int, float] = {}
        u = 0.0
        k_tot = 0.0
        for mid, m in self.members.items():
            if m["type"] == "poteau":
                E = codes.concrete_props(m["concrete"])["Ecd"] * 1e3
                Icol = min(m["b"] * m["h"] ** 3, m["h"] * m["b"] ** 3) / 12.0
                k_tot += 12.0 * E * Icol / self.h_etage ** 3
        for level in range(1, self.niveaux + 1):
            V = sum(sum(self.lateral.get(l, {}).values()) for l in range(level, self.niveaux + 1))
            du = V / max(k_tot, 1e6)
            u += du
            cum[level] = round(u * 1000.0, 2)
        results["displacements"]["levels_mm"] = cum
        return results

    def story_drift(self, disp_levels: dict | None = None) -> tuple[float, str]:
        disp = disp_levels or {}
        max_drift = 0.0
        worst = ""
        prev = 0.0
        for level in range(1, self.niveaux + 1):
            u = disp.get(level, disp.get(str(level), prev))
            drift = abs(u - prev) / (self.h_etage * 1000.0)
            if drift > max_drift:
                max_drift, worst = drift, f"niveau {level}"
            prev = u
        return max_drift, worst


def _cls(materiau) -> str:
    if not materiau:
        return ""
    s = str(materiau).replace("beton_", "")
    return s if "/" in s else ""


def _psi2(proj) -> float:
    usage = str(proj.get("usage", "habitation"))
    return float(codes.LIVE_LOADS.get(usage, codes.LIVE_LOADS["habitation"])["psi2"])


def _psi0s(proj) -> float:
    return float(codes.SNOW_ZONES.get(str(proj.get("zone_neige", "A2")),
                                     codes.SNOW_ZONES["A2"])["psi0"])


def _favorable(proj) -> bool:
    return int(proj.get("zone_sismique", 2) or 2) >= 3
