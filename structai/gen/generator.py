"""Génération d'options de conception structurelle (§2.3-4a, §3.8, §4.5).

Exploration systématique et déterministe d'un espace de conception paramétré
(grille de poteaux, portées, épaisseurs de dalle, systèmes de contreventement,
fondations), filtrage par règles simples, calcul complet (moteur Lot 3) des
meilleurs candidats, conservation des seules options conformes, classement
selon critère paramétrable — seed fixée pour la reproductibilité.

Les pistes « IA créative » (Lot 2/4b) sont injectées comme paramètres
admissibles supplémentaires et passent par le MÊME pipeline de validation :
aucune proposition IA n'est retenue sans calcul conforme.
"""
from __future__ import annotations

import math
import random
from typing import Any

from ..calc.engine import analyze_option
from ..logging_setup import get_logger
from ..util import now_iso

log = get_logger("structai.gen")


# ---------------------------------------------------------------------------
# Géométrie de base depuis l'interprétation validée
# ---------------------------------------------------------------------------

def emprise_from_interpretation(interp: dict, parsed: dict | None, unit_to_m: float) -> dict:
    bat = (interp or {}).get("batiment", {}) or {}
    em = bat.get("emprise") or {}
    if em.get("largeur") and em.get("profondeur"):
        return {"x0": 0.0, "y0": 0.0, "x1": float(em["largeur"]), "y1": float(em["profondeur"])}
    if parsed:
        b = parsed.get("emprise", {})
        k = parsed.get("unit_to_m", unit_to_m)
        (x0, y0), (x1, y1) = b.get("min", [0, 0]), b.get("max", [12.5, 9.0])
        return {"x0": x0 * k, "y0": y0 * k, "x1": x1 * k, "y1": y1 * k}
    return {"x0": 0.0, "y0": 0.0, "x1": 12.5, "y1": 9.0}


def _wall_candidates(interp: dict) -> list[dict]:
    out = []
    for w in (interp or {}).get("murs_porteurs", []) or []:
        a, b = tuple(w.get("debut", (0, 0))), tuple(w.get("fin", (0, 0)))
        L = math.dist(a, b)
        if L < 1.5:
            continue
        out.append({"debut": list(a), "fin": list(b),
                    "epaisseur": float(w.get("epaisseur", 0.20) or 0.20),
                    "materiau": w.get("materiau_presume", "beton_armé")})
    return out


# ---------------------------------------------------------------------------
# Construction d'une option depuis un jeu de paramètres
# ---------------------------------------------------------------------------

def build_option(params: dict, interp: dict, proj: dict, emprise: dict) -> dict:
    W = emprise["x1"] - emprise["x0"]
    D = emprise["y1"] - emprise["y0"]
    nx = max(2, int(round(W / params["portee_x"])) + 1)
    ny = max(2, int(round(D / params["portee_y"])) + 1)
    xs = [emprise["x0"] + i * W / (nx - 1) for i in range(nx)]
    ys = [emprise["y0"] + j * D / (ny - 1) for j in range(ny)]
    niveaux = int(proj.get("niveaux", 1) or 1)
    system = params["systeme"]
    t_dalle = params["dalle"]
    sec = list(params["poteau"])
    b_p, h_p = params["poutre"]
    concret = params["beton"]
    walls_in = _wall_candidates(interp) if system != "portique" else []
    wall_lines = [tuple(w["debut"]) + tuple(w["fin"]) for w in walls_in]

    def on_wall(x, y, tol=0.4):
        for w in walls_in:
            if _near_seg((x, y), tuple(w["debut"]), tuple(w["fin"]), tol):
                return True
        return False

    cols = []
    n = 1
    col_at: dict[tuple, str] = {}
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if system != "portique" and on_wall(x, y) and (i in (0, nx - 1) or j in (0, ny - 1)):
                continue  # remplacé par le voile
            cid = f"P{n}"; n += 1
            cols.append({"id": cid, "position": [round(x, 3), round(y, 3)],
                         "section": sec, "materiau": f"beton_{concret}",
                         "niveaux": [0, niveaux - 1]})
            col_at[(round(x, 4), round(y, 4))] = cid
    beams = []
    bcount = 1
    for level in range(1, niveaux + 1):
        for j in range(ny):
            for i in range(nx - 1):
                a, b = (xs[i], ys[j]), (xs[i + 1], ys[j])
                beams.append({"id": f"B{bcount}", "debut": [round(a[0], 3), round(a[1], 3)],
                              "fin": [round(b[0], 3), round(b[1], 3)],
                              "section": [b_p, h_p], "materiau": f"beton_{concret}",
                              "niveau": level}); bcount += 1
        for i in range(nx):
            for j in range(ny - 1):
                a, b = (xs[i], ys[j]), (xs[i], ys[j + 1])
                beams.append({"id": f"B{bcount}", "debut": [round(a[0], 3), round(a[1], 3)],
                              "fin": [round(b[0], 3), round(b[1], 3)],
                              "section": [b_p, h_p], "materiau": f"beton_{concret}",
                              "niveau": level}); bcount += 1
    dalles = []
    dcount = 1
    for level in range(1, niveaux + 1):
        roof = level == niveaux
        for i in range(nx - 1):
            for j in range(ny - 1):
                poly = [[xs[i], ys[j]], [xs[i + 1], ys[j]], [xs[i + 1], ys[j + 1]], [xs[i], ys[j + 1]]]
                dalles.append({"id": f"D{dcount}", "polygone": poly, "epaisseur": t_dalle,
                               "materiau": f"beton_{concret}", "niveau": level,
                               "toiture": roof, "sens_portee": "court"})
                dcount += 1
    voiles = []
    for k, w in enumerate(walls_in):
        voiles.append({"id": f"V{k + 1}", "debut": [round(w["debut"][0], 3), round(w["debut"][1], 3)],
                       "fin": [round(w["fin"][0], 3), round(w["fin"][1], 3)],
                       "epaisseur": max(w["epaisseur"], 0.16),
                       "niveaux": [0, niveaux - 1], "role": "contreventement",
                       "materiau": f"beton_{concret}"})
    fondations = []
    ftype = params["fondation"]
    N_floor = 2.5 * t_dalle * 25 * (W * D) / max(len(cols) or 1, 1)  # ordre de grandeur kN
    dim = 1.6
    for c in cols:
        fondations.append({"id": f"F{c['id'][1:]}", "type": ftype, "poteau": c["id"],
                           "dimensions": [dim, dim, 0.5], "materiau": f"beton_{concret}"})
    if ftype == "radier":
        fondations = [{"id": "FRAD", "type": "radier", "poteau": None,
                       "dimensions": [round(W + 0.6, 2), round(D + 0.6, 2), 0.35],
                       "materiau": f"beton_{concret}"}]
    desc = (f"Trame {nx}×{ny} poteaux, portées {xs[1]-xs[0]:.2f}×{ys[1]-ys[0]:.2f} m, "
            f"dalles pleines {t_dalle*100:.0f} cm, "
            + ("voiles de façade en contreventement." if voiles else
               "portiques en contreventement."))
    option = {
        "id": "OPT-TEMP",
        "date_generation": now_iso(),
        "methode": "algorithme_local",
        "seed": params.get("seed"),
        "description_courte": desc,
        "structure": {"poteaux": cols, "poutres": beams, "dalles": dalles,
                      "voiles": voiles, "fondations": fondations},
        "meta": {"classe_beton": concret, "params": {k: v for k, v in params.items() if k != "seed"},
                 "emprise": emprise},
    }
    return option


def _near_seg(p, a, b, tol=0.35):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 < 1e-9:
        return math.hypot(px - ax, py - ay) < tol
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy)) < tol


# ---------------------------------------------------------------------------
# Espace de conception + filtrage par règles simples
# ---------------------------------------------------------------------------

def design_space(proj: dict, gen: dict, emprise: dict) -> list[dict]:
    W = emprise["x1"] - emprise["x0"]
    D = emprise["y1"] - emprise["y0"]
    pmin = float(gen.get("portee_min_m", 3.2))
    pmax = float(gen.get("portee_max_m", 6.5))
    portees = [p for p in (3.6, 4.0, 4.2, 4.5, 4.8, 5.0, 5.4, 6.0) if pmin <= p <= pmax]
    epaisseurs = [e for e in gen.get("epaisseurs_dalle_m", [0.16, 0.18, 0.20, 0.22, 0.25])]
    zone = int(proj.get("zone_sismique", 2) or 2)
    has_walls = bool((proj.get("_interpretation") or {}).get("murs_porteurs"))
    systemes = ["portique"]
    if zone >= 3 or has_walls:
        systemes.append("double_systeme")
    if has_walls and zone >= 2:
        systemes.append("voiles")
    fonda = ["semelle_isolee"]
    qsol = float(proj.get("qsol_kpa", 250.0) or 250.0)
    if qsol < 150:
        fonda = ["radier", "semelle_isolee"]
    if not has_walls:
        fonda.append("filant")
    betons = ["C25/30"] if zone < 4 else ["C25/30", "C30/37"]
    out: list[dict] = []
    for px in portees:
        for py in portees:
            for t in epaisseurs:
                for sysx in systemes:
                    for f in fonda:
                        for bt in betons:
                            for psec in ([0.30, 0.30], [0.25, 0.30]):
                                out.append({
                                    "portee_x": px, "portee_y": py, "dalle": t,
                                    "systeme": sysx, "fondation": f, "beton": bt,
                                    "poteau": psec, "poutre": [0.30, max(0.45, min(0.60, px * 0.12))],
                                })
    # Filtrage par règles simples (§4a)
    def ok(p):
        if max(p["portee_x"], p["portee_y"]) / (p["dalle"] * 1000) > 30:  # L/h > 30 dalle
            return False
        if min(p["poteau"]) < 0.25 and zone >= 3:
            return False
        if p["systeme"] == "voiles" and not has_walls:
            return False
        if W / p["portee_x"] + D / p["portee_y"] > 26:  # trop d'éléments → hors budget calcul
            return False
        return True
    filtered = [p for p in out if ok(p)]
    return filtered or out[:80]


# ---------------------------------------------------------------------------
# Génération complète
# ---------------------------------------------------------------------------

def generate_options(interpretation: dict, proj: dict, gen: dict,
                     ai_variants: list[dict] | None = None,
                     progress=None, cancel=None, parsed: dict | None = None) -> dict:
    seed = int(proj.get("seed") or 123456)
    rng = random.Random(seed)
    unit_to_m = (parsed or {}).get("unit_to_m", 0.001)
    emprise = emprise_from_interpretation(interpretation, parsed, unit_to_m)
    proj = dict(proj)
    proj["_interpretation"] = interpretation
    W = emprise["x1"] - emprise["x0"]
    D = emprise["y1"] - emprise["y0"]
    if not proj.get("emprise"):
        proj["emprise"] = {"largeur": round(W, 2), "profondeur": round(D, 2)}

    space = design_space(proj, gen, emprise)
    rng.shuffle(space)
    if ai_variants:
        for v in ai_variants:
            p = _ai_variant_to_params(v, gen, proj)
            if p:
                space.insert(0, p)
    max_calc = int(gen.get("max_options_calculees", 40))
    n_target = int(proj.get("nb_options", gen.get("nb_options", 5)))

    log_fn = progress or (lambda stage, msg, pct: None)
    log_fn("space", f"Espace de conception : {len(space)} combinaisons paramétriques", 5)
    options_ok: list[dict] = []
    seen_sig: set[tuple] = set()
    evaluated = 0
    for i, params in enumerate(space):
        if cancel and cancel():
            break
        if evaluated >= max_calc and len(options_ok) >= n_target:
            break
        if evaluated >= max_calc:
            break
        params = dict(params)
        params["seed"] = seed
        sig = (params["portee_x"], params["portee_y"], params["dalle"], params["systeme"],
               params["fondation"], params["beton"], tuple(params["poteau"]))
        if sig in seen_sig:
            continue
        seen_sig.add(sig)
        try:
            option = build_option(params, interpretation, proj, emprise)
        except Exception as exc:
            log.debug("build_option skip: %s", exc)
            continue
        if len(option["structure"]["poteaux"]) < 2 and params["systeme"] != "voiles":
            continue
        evaluated += 1
        try:
            an = analyze_option(option, proj, gen)
        except Exception as exc:
            log.debug("option non calculable: %s", exc)
            log_fn("calc", f"Option {evaluated}/{max_calc} — erreur de calcul ignorée", 
                   int(5 + 85 * evaluated / max_calc))
            continue
        conf = an["conformite"]
        allconf = all(v in ("conforme", "non_requis") for v in conf.values())
        option["conformite"] = conf
        option["indicateurs"] = an["indicateurs"]
        option["resultats_calcul"] = an["resultats"]
        option["synthese"] = an["synthese"]
        option["methode"] = ("algorithme_local + ia_creative" if params.get("from_ai")
                             else "algorithme_local")
        if allconf:
            options_ok.append(option)
        log_fn("calc", f"Option {evaluated}/{max_calc} — "
               f"{'CONFORME' if allconf else 'non conforme'} (taux max "
               f"{an['synthese']['taux_travail_max']})",
               int(5 + 85 * evaluated / max_calc))
    # Classement
    crit = str(proj.get("critere_classement", gen.get("critereme_classement",
                                                     "simplicite_mise_en_oeuvre")))
    key_fn = _rank_key(crit)
    options_ok.sort(key=lambda o: key_fn(o) if o.get("resultats_calcul") else (9e9,))
    presented = options_ok[: max(n_target, 3)]
    for k, o in enumerate(presented):
        o["id"] = f"OPT-{k + 1:03d}"
        o["rank"] = k + 1
    index = {
        "projet_id": proj.get("id"),
        "date_generation": now_iso(),
        "nombre_options_generees": len(space),
        "nombre_options_calculees": evaluated,
        "nombre_options_conformes": len(options_ok),
        "nombre_options_presentees": len(presented),
        "criteres_classement": [crit, "masse_acier", "taux_travail_max"],
        "seed": seed,
        "options_presentees": [o["id"] for o in presented],
    }
    log_fn("done", f"{len(presented)} options conformes présentées sur {len(options_ok)}", 100)
    return {"options": presented, "index": index,
            "diagnostic": _diagnostic(len(space), evaluated, len(options_ok), proj) if len(presented) < 3 else ""}


def _rank_key(crit: str):
    def ind(o, name, default=9e9):
        return float(o.get("indicateurs", {}).get(name, default))
    if crit == "masse_acier":
        return lambda o: (ind(o, "masse_acier_kg"), ind(o, "taux_travail_max"))
    if crit == "volume_beton":
        return lambda o: (ind(o, "volume_beton_m3"), ind(o, "taux_travail_max"))
    if crit == "performance_sismique":
        return lambda o: (ind(o, "deplacement_etage_max_mm", 0.0), ind(o, "taux_travail_max"))
    if crit == "marge_structurelle":
        return lambda o: (ind(o, "taux_travail_max"), ind(o, "masse_acier_kg"))
    # simplicité de mise en œuvre : peu d'éléments, sections normalisées
    return lambda o: (ind(o, "nombre_poteaux", 0) + ind(o, "nombre_poutres", 0),
                      ind(o, "masse_acier_kg"), ind(o, "taux_travail_max"))


def _ai_variant_to_params(v: dict, gen: dict, proj: dict) -> dict | None:
    """Traduit une proposition IA (abstraite) en paramètres de generation."""
    try:
        portee = float(v.get("portee", v.get("trame", 4.5)))
        portee = min(max(portee, 3.0), 7.5)
        dalle = float(v.get("dalle", v.get("epaisseur_dalle", 0.20)))
        if dalle < 0.14 or dalle > 0.32:
            return None
        sysx = str(v.get("systeme", "double_systeme"))
        if sysx not in ("portique", "voiles", "double_systeme"):
            sysx = "double_systeme"
        return {"portee_x": portee, "portee_y": portee, "dalle": dalle,
                "systeme": sysx, "fondation": v.get("fondation", "semelle_isolee"),
                "beton": v.get("beton", "C25/30"), "poteau": [0.30, 0.30],
                "poutre": [0.30, 0.50], "from_ai": True}
    except Exception:
        return None


def _diagnostic(n_space: int, n_eval: int, n_ok: int, proj: dict) -> str:
    if n_space == 0:
        return ("Aucune combinaison paramétrique possible : vérifier l'emprise "
                "du bâtiment dans l'interprétation.")
    if n_ok == 0:
        return ("Aucune option conforme. Pistes : augmenter le nombre d'options "
                "calculées, assouplir les portées max, vérifier les zones "
                "sismique/neige et qsol, ou épaissir les dalles "
                "(paramètres → génération).")
    return (f"Seulement {n_ok} option(s) conforme(s) sur {n_eval} calculée(s) — "
            "contraintes probablement sévères (zone sismique, sol).")
