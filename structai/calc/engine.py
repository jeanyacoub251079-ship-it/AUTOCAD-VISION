"""Orchestration des vérifications pour une option (§2.3 étape 5, §4.6).

Produit le JSON « resultats_calcul » complet : hypothèses, charges,
combinaisons, vérifications par élément, dimensionnement des armatures,
synthèse, conformité par Eurocode, indicateurs et quantitatifs.
"""
from __future__ import annotations

import math
from typing import Any

from ..logging_setup import get_logger
from . import codes
from .model import Model, _poly_area, _poly_bbox
from .sections import (effort_tranchant, fissuration, fleche, flexion,
                       ancrage, poteau as poteau_check)

log = get_logger("structai.engine")

BAR_MASS_KG_M2 = {6: 0.222, 8: 0.395, 10: 0.617, 12: 0.888, 14: 1.208,
                  16: 1.578, 20: 2.466, 25: 3.854, 32: 6.313}


def _parse_bars(notat: str) -> tuple[int, int]:
    try:
        n = int(notat.split("HA")[0])
        d = int(notat.split("HA")[1])
        return n, d
    except Exception:
        return 0, 0


def _cadres_kg_m(notation: str) -> float:
    try:
        part = notation.split(" ")[0]
        d = int(part.split("HA")[1])
        e = float(notation.split("e=")[1])
    except Exception:
        return 2 * BAR_MASS_KG_M2[8] / 0.25
    return 2 * BAR_MASS_KG_M2.get(d, 0.395) / max(e / 1000.0, 0.05)


def _esp(notation: str) -> float:
    try:
        return float(notation.split("e=")[1])
    except Exception:
        return 250.0


def analyze_option(option: dict, proj: dict, gen: dict | None = None) -> dict:
    gen = gen or {}
    st = option.get("structure", {})
    model = Model(option, proj, gen)
    res = model.solve()
    members = res.get("members", {})
    reactions = res.get("reactions", {})
    combos = res["combos"]

    verifs: list[dict] = []
    armatures: dict[str, Any] = {}
    warnings: list[str] = list(res.get("warnings", []))
    q_steel = {"long": 0.0, "trans": 0.0}
    q_beton = {"poteaux": 0.0, "poutres": 0.0, "dalles": 0.0,
               "voiles": 0.0, "fondations": 0.0}
    q_coff = {"poteaux": 0.0, "poutres": 0.0, "dalles": 0.0,
              "voiles": 0.0, "fondations": 0.0}

    if res.get("methode") == "analytique_repli":
        warnings.append("Modèle analytique de repli : moments/flèches bi-articulés "
                        "(majorants aux travées extrêmes, minorés en continuité).")

    classe_expo = str(proj.get("classe_exposition", "XC1"))
    panels = model.panels
    slab_t = max((p["epaisseur"] for p in panels), default=0.20)
    psi2 = _psi2(proj)

    # -------------------------------------------------------------- poutres
    groups: dict[str, list[str]] = {}
    for mid, m in model.members.items():
        if m["type"] in ("poutre", "voile-h"):
            groups.setdefault((m["type"], m["id"]), []).append(mid)
    for (kind, pid), mids in groups.items():
        M, V, combo_M = 0.0, 0.0, "ELU-1"
        for mid in mids:
            r = members.get(mid, {})
            if r.get("M", 0) > M:
                M, combo_M = r["M"], r.get("M_combo", "ELU-1")
            V = max(V, r.get("V", 0.0))
        m0 = model.members[mids[0]]
        b, h = m0["b"], m0["h"]
        L = sum(max(math.dist(model.members[mm]["n1"][:2], model.members[mm]["n2"][:2]), 0.05)
                for mm in mids)
        cover = codes.design_cover(classe_expo, "poutre")
        f = flexion(b, h, cover, M, m0["concrete"])
        v = effort_tranchant(b, h, cover, V, f["As_need_cm2"], m0["concrete"])
        wG = _mean_load(model, mids, "G")
        wQ = _mean_load(model, mids, "Q")
        wS = _mean_load(model, mids, "S")
        fl = fleche(max(L / max(len(mids), 1), 0.5), wG + psi2 * wQ, wG + wQ + wS,
                    h, b, m0["concrete"])
        Mqp = max((members.get(mm, {}).get("combos", {}).get("ELS-qp", {}).get("M_kNm", 0.0)
                   for mm in mids), default=0.0)
        fx = fissuration(b, h, cover, Mqp, max(f["As_need_cm2"], 1.0),
                         concrete=m0["concrete"])
        tlabel = "poutre" if kind == "poutre" else "chainage_voile"
        verifs += [
            {"element": pid, "type": tlabel, "verification": "flexion", "combinaison": combo_M,
             "sollicitation_kNm": M, "resistance_kNm": round(M / max(f["taux_travail"], 1e-6), 1) if f["taux_travail"] > 0 else None,
             "taux_travail": f["taux_travail"], "statut": f["statut"],
             "detail": {"mu": f["mu"], "As_need_cm2": f["As_need_cm2"],
                        "barres": f["longitudinel"]["barres"], "regime": f.get("regime")}},
            {"element": pid, "type": tlabel, "verification": "effort_tranchant", "combinaison": combo_M,
             "sollicitation_kN": round(V, 1), "resistance_kN": v.get("VRd_c_kN"),
             "taux_travail": v["taux_travail"], "statut": v["statut"],
             "detail": {"cadres": v.get("cadres")}},
            {"element": pid, "type": tlabel, "verification": "fleche", "combinaison": "ELS",
             "valeur_mm": fl["fleche_totale_mm"], "limite_mm": fl["limite_mm"],
             "taux_travail": fl["taux_travail"], "statut": fl["statut"]},
            {"element": pid, "type": tlabel, "verification": "fissuration", "combinaison": "ELS-qp",
             "valeur_mm": fx["wk_mm"], "limite_mm": fx["wk_lim_mm"],
             "taux_travail": fx["taux_travail"], "statut": fx["statut"]},
        ]
        armatures[pid] = {"section_longitudinale_cm2": f["As_need_cm2"],
                          "barres": f["longitudinel"]["barres"],
                          "section_reelle_cm2": f["longitudinel"]["section_reelle_cm2"],
                          "cadres": v.get("cadres", "HA8 e=250"),
                          "espacement_cm": round(_esp(v.get("cadres", "HA8 e=250")) / 10.0, 1),
                          "enrobage_mm": cover}
        n_long, d_long = _parse_bars(f["longitudinel"]["barres"])
        lb = ancrage(concrete=m0["concrete"])["lb_mm"] / 1000.0
        q_steel["long"] += n_long * BAR_MASS_KG_M2.get(d_long, 1.578) * (L + 2 * 0.4 * lb)
        q_steel["trans"] += _cadres_kg_m(v.get("cadres", "HA8 e=250")) * L
        q_beton["poutres" if kind == "poutre" else "voiles"] += \
            b * (h if kind != "poutre" else max(h - slab_t, 0.08)) * L
        q_coff["poutres"] += (2 * max(h - slab_t, 0.05) + b) * L if kind == "poutre" else 0.0

    # -------------------------------------------------------------- dalles
    for p in panels:
        x0, y0, x1, y1 = p["bbox"]
        dx, dy = x1 - x0, y1 - y0
        L0 = max(min(dx, dy) - 0.3, 0.5)
        t = p["epaisseur"]
        g_self = p["g_surf"]
        q_live = p["q_live"]
        sk = p["sk"]
        best_M, best_combo = 0.0, "ELU-1"
        best_V = 0.0
        for c in combos:
            if c["type"] in ("ELS", "ELU-acc"):
                continue
            fct = c["f"]
            gd = fct["G"] * g_self + fct["Q"] * q_live + fct["S"] * sk
            M = gd * L0 * L0 / 8.0
            if M > best_M:
                best_M, best_combo = M, c["id"]
                best_V = gd * L0 / 2.0
        cover = codes.design_cover(classe_expo, "dalle")
        f = flexion(1.0, t, cover, best_M, model.classe_beton)
        v = effort_tranchant(1.0, t, cover, best_V, f["As_need_cm2"], model.classe_beton)
        qp_g = g_self + psi2 * q_live
        ch_g = g_self + q_live + sk
        fl = fleche(L0, qp_g, ch_g, t, 1.0, model.classe_beton)
        verifs.append({"element": p["id"], "type": "dalle", "verification": "flexion",
                       "combinaison": best_combo, "sollicitation_kNm": f["M_Ed_kNm"],
                       "taux_travail": f["taux_travail"], "statut": f["statut"],
                       "detail": {"portee_calc_m": round(L0, 2), "barres": f["longitudinel"]["barres"],
                                  "toiture": p["toiture"]}})
        verifs.append({"element": p["id"], "type": "dalle", "verification": "fleche",
                       "combinaison": "ELS", "valeur_mm": fl["fleche_totale_mm"],
                       "limite_mm": fl["limite_mm"], "taux_travail": fl["taux_travail"],
                       "statut": fl["statut"]})
        verifs.append({"element": p["id"], "type": "dalle", "verification": "effort_tranchant",
                       "combinaison": best_combo, "sollicitation_kN": round(best_V, 1),
                       "resistance_kN": v["VRd_c_kN"], "taux_travail": v["taux_travail"],
                       "statut": v["statut"]})
        Mqp_dalle = (1.0 * g_self + psi2 * q_live) * L0 * L0 / 8.0
        fx = fissuration(1.0, t, cover, Mqp_dalle, max(f["As_need_cm2"], 1.0), concrete=model.classe_beton)
        verifs.append({"element": p["id"], "type": "dalle", "verification": "fissuration",
                       "combinaison": "ELS-qp", "valeur_mm": fx["wk_mm"], "limite_mm": fx["wk_lim_mm"],
                       "taux_travail": fx["taux_travail"], "statut": fx["statut"]})
        armatures[p["id"]] = {"section_longitudinale_cm2_m": f["As_need_cm2"],
                              "barres": f["longitudinel"]["barres"],
                              "espacement_cm": 20.0,
                              "enrobage_mm": cover,
                              "note": "dalle armée dans le sens court, bi-articulée (majorant)"}
        area = p["aire"]
        q_steel["long"] += f["As_need_cm2"] * 0.785 * (area / max(min(dx, dy), 1e-6))
        q_steel["trans"] += 4.0 * area
        q_beton["dalles"] += area * t
        q_coff["dalles"] += area

    # -------------------------------------------------------------- poteaux
    col_groups: dict[str, list[str]] = {}
    for mid, m in model.members.items():
        if m["type"] == "poteau":
            col_groups.setdefault(m["id"], []).append(mid)
    for cid, mids in col_groups.items():
        N = M = 0.0
        combo_N = "ELU-1"
        for mid in mids:
            r = members.get(mid, {})
            for cidc, vals in r.get("combos", {}).items():
                if vals.get("N_kN", 0) > N:
                    N, combo_N = vals["N_kN"], cidc
                M = max(M, vals.get("M_kNm", 0.0))
        m0 = model.members[mids[0]]
        b, h = m0["b"], m0["h"]
        Lf = max((model.members[mid]["z1"] - model.members[mid]["z0"]) for mid in mids)
        pc = poteau_check(b, h, Lf, N, M, m0["concrete"], classe_expo)
        verifs.append({"element": cid, "type": "poteau",
                       "verification": "compression_composee_flambement",
                       "combinaison": combo_N, "sollicitation_kN": round(N, 1),
                       "resistance_kN": pc["Nu_Rd_kN"], "taux_travail": pc["taux_travail"],
                       "statut": pc["statut"],
                       "detail": {"elancement": pc["elancement"], "M_tot_kNm": pc["M_tot_kNm"],
                                  "interaction": pc["interaction"]}})
        armatures[cid] = {"section_longitudinale_cm2": pc["As_min_cm2"],
                          "barres": pc["longitudinel"]["barres"],
                          "section_reelle_cm2": pc["longitudinel"]["section_reelle_cm2"],
                          "cadres": pc["cadres"],
                          "enrobage_mm": pc["enrobage_mm"]}
        n_long, d_long = _parse_bars(pc["longitudinel"]["barres"])
        q_steel["long"] += n_long * BAR_MASS_KG_M2.get(d_long, 1.578) * Lf * len(mids)
        q_steel["trans"] += _cadres_kg_m(pc["cadres"]) * Lf * len(mids)
        q_beton["poteaux"] += b * h * Lf
        q_coff["poteaux"] += 2 * (b + h) * Lf

    # -------------------------------------------------------------- voiles (vertical)
    wall_by_id: dict[str, list[dict]] = {}
    for w in st.get("voiles", []):
        wall_by_id.setdefault(w["id"], []).append(w)
    Vb = getattr(model, "Vb", 0.0)
    cap_sism_tot = 0.0
    for wid, segs in wall_by_id.items():
        t = float(segs[0].get("epaisseur", 0.20))
        Lw = sum(math.dist(tuple(w["debut"]), tuple(w["fin"])) for w in segs)
        Hw = model.niveaux * model.h_etage
        Nw = 0.0
        for nk, rr in reactions.items():
            if abs(nk[2]) < 1e-6 and _near_line((nk[0], nk[1]), tuple(segs[0]["debut"]),
                                                tuple(segs[0]["fin"]), 0.4):
                Nw += rr.get("R", 0.0)
        M0 = sum(Vb_f * l * model.h_etage
                 for l, Vb_f in {lvl: model.lateral.get(lvl, {}).get("E", 0.0)
                                 for lvl in range(1, model.niveaux + 1)}.items())
        fc28 = 0.65 * codes.concrete_props(model.classe_beton)["fck_cube"]
        cap_sism = 0.15 * fc28 * 1e3 * t * Lw  # kN : 0.15·fc28(MPa)=MPa→kPa × aire m²
        cap_sism_tot += cap_sism
        pc = poteau_check(t, max(Lw, 0.5), Hw, Nw, M0, model.classe_beton, classe_expo)
        verifs.append({"element": wid, "type": "voile", "verification": "flexion_composee_pied",
                       "combinaison": "ELU-acc-E", "sollicitation_kN": round(Nw, 1),
                       "resistance_kN": pc["Nu_Rd_kN"], "taux_travail": pc["taux_travail"],
                       "statut": pc["statut"],
                       "detail": {"M_renversement_kNm": round(M0, 1), "capacite_cisaillement_kN": round(cap_sism, 0)}})
        armatures[wid] = {"armaturage_min_cm2_m": round(2 * 0.002 * t * 1000, 1),
                          "barres": "treillis HA10 e=150 x2 parements (DCM)",
                          "enrobage_mm": codes.design_cover(classe_expo, "voile")}
        q_steel["long"] += 0.004 * (t * Lw * Hw) * codes.GAMMA_STEEL * 1000.0
        q_beton["voiles"] += t * Lw * Hw
        q_coff["voiles"] += 2 * Lw * Hw

    # -------------------------------------------------------------- séisme global / dérive
    ec8_statut = "conforme"
    zone_s = int(proj.get("zone_sismique", 2) or 2)
    drift, where = model.story_drift(res.get("displacements", {}).get("levels_mm", {}))
    fc28_g = 0.65 * codes.concrete_props(model.classe_beton)["fck_cube"]
    cap_frame = 0.0
    for mid, m in model.members.items():
        if m["type"] == "poteau":
            # contribution des abouts de poutre/poteau (portique dissipatif) — ordre de grandeur
            cap_frame += 0.12 * fc28_g * 1e3 * m["b"] * 0.9 * m["h"] / max(model.niveaux, 1)
    cap_resist_tot = cap_sism_tot + cap_frame
    if zone_s >= 2:
        if Vb > cap_resist_tot:
            ec8_statut = "non_conforme"
            warnings.append(f"Contreventement sismique insuffisant : Vb={Vb:.0f} kN > "
                            f"capacité ≈ {cap_resist_tot:.0f} kN (voiles+portiques).")
        lim = 0.005
        verifs.append({"element": "global", "type": "structure",
                       "verification": "deplacement_etage_ec8", "combinaison": "ELU-acc-E",
                       "valeur_mm": round(drift * model.h_etage * 1000, 2),
                       "limite_mm": round(lim * model.h_etage * 1000, 2),
                       "taux_travail": round(drift / lim, 3),
                       "statut": "conforme" if drift <= lim else "non_conforme",
                       "detail": {"etage_critique": where}})
        verifs.append({"element": "global", "type": "structure",
                       "verification": "effort_tranchant_base_sismique", "combinaison": "ELU-acc-E",
                       "sollicitation_kN": round(Vb, 1),
                       "resistance_kN": round(cap_resist_tot, 1),
                       "taux_travail": round(Vb / max(cap_resist_tot, 1e-9), 3) if cap_resist_tot else 9.9,
                       "statut": ec8_statut})
        for rule in _constructive_rules(st, proj):
            verifs.append({"element": rule["element"], "type": "regle_ec8",
                           "verification": f"ec8_{rule['code']}", "combinaison": "—",
                           "statut": rule["statut"], "detail": {"regle": rule["regle"]}})
            if rule["statut"] != "conforme":
                ec8_statut = "non_conforme"

    # -------------------------------------------------------------- fondations
    qsol = float(proj.get("qsol_kpa", gen.get("qsol_kpa", 250.0)) or 250.0)
    for fo in st.get("fondations", []):
        pid = fo.get("poteau")
        dims = fo.get("dimensions", [1.5, 1.5, 0.4])
        B = float(dims[0]); Lb = float(dims[1])
        hF = float(dims[2]) if len(dims) > 2 else 0.4
        N_car = N_elu = N_qp = 0.0
        pos = None
        for cm in st.get("poteaux", []):
            if cm["id"] == pid:
                pos = cm["position"]
                break
        if pos is None:
            warnings.append(f"Fondation {fo['id']} : poteau {pid} introuvable.")
            continue
        for nk, rr in reactions.items():
            if abs(nk[2]) > 1e-6:
                continue
            if abs(nk[0] - pos[0]) > 0.45 or abs(nk[1] - pos[1]) > 0.45:
                continue
            N_elu = max(N_elu, rr.get("R", 0.0))
            for ccid, vv in rr.get("combos", {}).items():
                if ccid == "ELS-car":
                    N_car = max(N_car, vv.get("Rz_kN", 0.0))
                elif ccid == "ELS-qp":
                    N_qp = max(N_qp, vv.get("Rz_kN", 0.0))
        area = max(B * Lb, 1e-9)
        q_sol = (N_car + B * Lb * 1.0 * 22.0) / area
        stat = "conforme" if q_sol <= qsol else "non_conforme"
        verifs.append({"element": fo["id"], "type": "semelle", "verification": "capacite_portante_sol",
                       "combinaison": "ELS-car", "sollicitation_kPa": round(q_sol, 1),
                       "resistance_kPa": qsol, "taux_travail": round(q_sol / qsol, 3),
                       "statut": stat,
                       "detail": {"N_car_kN": round(N_car, 1), "surface_m2": round(area, 2)}})
        c1 = max((Lb - 0.30) / 2, 0.05)
        qnet = max(N_elu - 1.35 * B * Lb * hF * 25, 0.0) / area
        M_f = qnet * c1 * c1 / 2.0
        fF = flexion(1.0, max(hF, 0.3), float(codes.FONDATION_COVER), M_f, "C25/30")
        armatures[fo["id"]] = {"section_longitudinale_cm2_m": fF["As_need_cm2"],
                               "barres": fF["longitudinel"]["barres"],
                               "enrobage_mm": codes.FONDATION_COVER,
                               "note": "ferraillage bas de semelle, débit croisé"}
        q_beton["fondations"] += B * Lb * hF
        q_coff["fondations"] += 2 * (B + Lb) * hF
        q_steel["long"] += fF["As_need_cm2"] * 0.785 * (B + Lb)

    # -------------------------------------------------------------- assemblage
    statuts = [v["statut"] for v in verifs]
    ok_elements = all(s == "conforme" for s in statuts)
    ec8_val = (ec8_statut if zone_s >= 2 else "non_requis")
    conformite = {
        "ec0": "conforme",
        "ec1": "conforme",
        "ec2": "conforme" if ok_elements else "non_conforme",
        "ec8": ec8_val,
        "an_fr": "conforme" if ok_elements and ec8_val in ("conforme", "non_requis") else "non_conforme",
    }
    taux_max = max((v.get("taux_travail", 0.0) or 0.0 for v in verifs), default=0.0)
    fleche_max = max((v.get("valeur_mm", 0.0) or 0.0 for v in verifs if v["verification"] == "fleche"),
                     default=0.0)
    critical = max(verifs, key=lambda v: v.get("taux_travail", 0.0) or 0.0, default=None)
    synthese = {
        "taux_travail_max": round(taux_max, 3),
        "element_critique": (critical or {}).get("element"),
        "verification_critique": (critical or {}).get("verification"),
        "marge_pct": round((1 - taux_max) * 100, 1) if taux_max < 9 else -1,
    }
    indicateurs = {
        "taux_travail_max": round(taux_max, 3),
        "fleche_max_mm": round(fleche_max, 1),
        "deplacement_etage_max_mm": round(drift * model.h_etage * 1000, 1),
        "volume_beton_m3": round(sum(q_beton.values()), 1),
        "masse_acier_kg": round(q_steel["long"] + q_steel["trans"], 0),
        "surface_coffrage_m2": round(sum(q_coff.values()), 1),
        "nombre_poteaux": len(st.get("poteaux", [])),
        "nombre_poutres": len(st.get("poutres", [])),
        "nombre_voiles": len(st.get("voiles", [])),
        "nombre_semelles": len([f for f in st.get("fondations", []) if f.get("type") != "radier"]),
    }
    charges = build_charges_json(proj, model)
    g_ref = max((p["g_surf"] for p in panels), default=6.0)
    hypotheses = {
        "materiaux": {
            "beton": {"classe": model.classe_beton,
                      **{k: round(v, 2) for k, v in codes.concrete_props(model.classe_beton).items()},
                      "fcd": round(codes.concrete_props(model.classe_beton)["fcd"], 2),
                      "gamma_c": 1.5, "alpha_cc": 0.85},
            "acier": {"classe": "B500B", "fyk": 500,
                      "fyd": round(codes.steel_props()["fyd"], 1), "gamma_s": 1.15},
        },
        "duree_utilisation": proj.get("duree_utilisation", 50),
        "classe_exposition": classe_expo,
        "categorie_importance": proj.get("categorie_importance", "II"),
        "modeles": {
            "analyse": res.get("methode"),
            "repartition_dalle": "tributaire uniforme par panneau (somme conservée)",
            "second_ordre": "raideur nominale, fluage négligé (poteaux)",
            "seisme": "statique équivalent, λ=1, W=G+ψ2·Q",
            "vent": "qb toiture, statique équivalent (terrain II, cs·cd=1)",
            "semelles": "qsol paramétrable, excentricité non vérifiée hors séisme",
        },
        "note": ("Résultats de conception préliminaire — vérification par l'ingénieur requise. "
                 "Valeurs normatives par défaut indicatives, éditables dans les paramètres."),
    }
    resultats = {
        "option_id": option.get("id"),
        "hypotheses": hypotheses,
        "charges": charges,
        "combinaisons": [
            {"id": c["id"], "type": c["type"], "expression": c["expression"],
             "valeur": round(c["f"]["G"] * g_ref + c["f"]["Q"] * charges["reference_surcharge_kpa"]
                             + c["f"]["S"] * charges["neige"]["sk"] * codes.SNOW_MU_FLAT, 2)}
            for c in combos],
        "verifications": verifs,
        "dimensionnement_armatures": armatures,
        "synthese": synthese,
        "avertissements": warnings,
        "indicateurs": indicateurs,
        "quantitatifs": {"beton_m3": {k: round(v, 2) for k, v in q_beton.items()},
                        "acier_kg": {k: round(v, 1) for k, v in q_steel.items()},
                        "coffrage_m2": {k: round(v, 1) for k, v in q_coff.items()}},
        "modele": {"n_members": len(model.members), "n_nodes": len(model.nodes),
                   "methode": res.get("methode")},
    }
    from ..util import jsonable
    return jsonable({"conformite": conformite, "resultats": resultats, "synthese": synthese,
                     "indicateurs": indicateurs, "quantitatifs": resultats["quantitatifs"],
                     "verifs_count": len(verifs), "warnings": warnings})


# ---------------------------------------------------------------------------
def _mean_load(model: Model, mids: list[str], case: str) -> float:
    tot = 0.0
    for mid in mids:
        m = model.members[mid]
        a, b = m["loads"][case]
        L = max(math.dist(m["n1"][:2], m["n2"][:2]), 0.05)
        tot += (a + b) / 2 * L
    n = len(mids) or 1
    Lm = sum(max(math.dist(model.members[mid]["n1"][:2], model.members[mid]["n2"][:2]), 0.05)
             for mid in mids) / n
    return tot / max(Lm * n, 1e-9)


def _psi2(proj) -> float:
    usage = str(proj.get("usage", "habitation"))
    return float(codes.LIVE_LOADS.get(usage, codes.LIVE_LOADS["habitation"])["psi2"])


def _near_line(p, a, b, tol=0.45) -> bool:
    (x, y), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 < 1e-9:
        return math.hypot(x - ax, y - ay) < tol
    t = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / L2))
    px, py = ax + t * dx, ay + t * dy
    return math.hypot(x - px, y - py) < tol


def _constructive_rules(st, proj) -> list[dict]:
    out = []
    q = float(proj.get("q_comportement", 3.0) or 3.0)
    system = str(proj.get("systeme_sismique", "portique"))
    allowed = max(d["q"] for d in codes.BEHAVIOR_FACTORS.get(
        system, codes.BEHAVIOR_FACTORS["portique"]).values())
    out.append({"element": "comportement", "code": "5.2.2.2",
                "statut": "conforme" if q <= allowed + 1e-9 else "non_conforme",
                "regle": f"q retenu ({q}) ≤ q max du système {system} ({allowed})"})
    has_wall = bool(st.get("voiles"))
    if int(proj.get("zone_sismique", 2) or 2) >= 3 and not has_wall and q > 3.0:
        out.append({"element": "contreventement", "code": "4.3.1",
                    "statut": "non_conforme",
                    "regle": "zone ≥3 : voiles requis pour q>3 (portiques seuls limités à q=3 DCM)"})
    for c in st.get("poteaux", []):
        b, h = c.get("section", [0.3, 0.3])
        out.append({"element": c["id"], "code": "5.4.1.2(3)",
                    "statut": "conforme" if min(b, h) >= 0.25 else "non_conforme",
                    "regle": "dimension minimale poteau ≥ 250 mm (DCM)"})
    for bm in st.get("poutres", []):
        b, h = bm.get("section", [0.3, 0.5])
        out.append({"element": bm["id"], "code": "5.4.2.1(2)",
                    "statut": "conforme" if (b >= 0.20 and h / max(b, 1e-9) <= 3.0) else "non_conforme",
                    "regle": "largeur poutre ≥ 200 mm ; h/b ≤ 3"})
    for w in st.get("voiles", []):
        out.append({"element": w["id"], "code": "5.4.1",
                    "statut": "conforme" if float(w.get("epaisseur", 0.2)) >= 0.16 else "non_conforme",
                    "regle": "épaisseur voile ≥ 160 mm (pratique FR, DCM)"})
    return out


def build_charges_json(proj: dict, model: Model) -> dict:
    usage = str(proj.get("usage", "habitation"))
    live = codes.LIVE_LOADS.get(usage, codes.LIVE_LOADS["habitation"])
    zone_neige = str(proj.get("zone_neige", "A2"))
    alt = float(proj.get("altitude", 50) or 50)
    sk, sk_note = codes.snow_load_sk(zone_neige, alt)
    wind = codes.wind_reference_pressure(int(proj.get("zone_vent", 2) or 2))
    zone_s = int(proj.get("zone_sismique", 2) or 2)
    agr = codes.SEISME_AGR.get(zone_s, 0.7)
    gI = codes.IMPORTANCE_GAMMA_I.get(str(proj.get("categorie_importance", "II")), 1.0)
    t_slab = max((p["epaisseur"] for p in getattr(model, "panels", [])), default=0.2)
    poids_propre = round(t_slab * codes.GAMMA_CONCRETE, 2)
    return {
        "permanentes": {"poids_propre": "auto (dalle + poutres + poteaux + voiles)",
                        "beton_gamma": codes.GAMMA_CONCRETE,
                        "revetements": codes.FINISHES_KPA, "cloisons": codes.PARTITIONS_KPA,
                        "plafonds": codes.CEILING_KPA},
        "exploitation": {usage: live["q"], "libelle": live["libelle"],
                         "psi0": live["psi0"], "psi1": live["psi1"], "psi2": live["psi2"]},
        "neige": {"zone": zone_neige, "sk": round(sk, 2), "mu": codes.SNOW_MU_FLAT,
                  "psi0": float(codes.SNOW_ZONES.get(zone_neige, codes.SNOW_ZONES["A2"])["psi0"]),
                  "note": sk_note},
        "vent": {"zone": int(proj.get("zone_vent", 2) or 2), "vb0_ms": wind["vb0_ms"],
                 "qb_kpa": wind["qb_kpa"],
                 "note": "qb0 NA ; qp(z) simplifié = qb0 (terrain II, cs·cd=1, h<15 m)"},
        "seisme": {"zone": zone_s, "agr_ms2": agr, "gammaI": gI, "ag_ms2": round(agr * gI, 3),
                   "classe_sol": str(proj.get("classe_sol", "A")),
                   "q": float(proj.get("q_comportement", 3.0) or 3.0),
                   "T1_estime_s": round(codes.estimate_fundamental_period(
                       int(proj.get("niveaux", 1) or 1),
                       str(proj.get("systeme_sismique", "portique"))), 2)},
        "reference_surcharge_kpa": round(live["q"], 2),
        "poids_propre_surcharge_kpa": round(poids_propre + codes.FINISHES_KPA +
                                            codes.PARTITIONS_KPA + codes.CEILING_KPA, 2),
    }
