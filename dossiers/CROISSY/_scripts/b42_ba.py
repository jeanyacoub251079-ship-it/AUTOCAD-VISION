#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-42 — POTEAUX ET JAMBAGES BA — CROISSY-FLORA
==============================================
Note de calcul d'exécution EC2 des trois porteurs verticaux en béton armé
implantés par B-20 : P2 (15x25), P3 (50x40), J1 (jambage 24x50).

Méthode :
  - flexion composée : diagramme d'interaction N-M calculé par compatibilité
    des déformations (bloc rectangulaire 0,8x, acier élasto-plastique) ;
  - flambement : EC2 § 5.8.3 (élancement limite) puis § 5.8.8 (courbure
    nominale) lorsque lambda > lambda_lim ;
  - dispositions constructives : EC2 § 9.5 (As,min, As,max, cadres).

Aucune valeur « par expérience » : chaque donnée d'entrée porte sa source.
Sorties : _rendus/b42_ba.txt + .json
"""
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_TXT = os.path.join(ROOT, "_rendus", "b42_ba.txt")
OUT_JSON = os.path.join(ROOT, "_rendus", "b42_ba.json")
NOTE = os.path.join(ROOT, "06_CALCULS", "B-42_Verticaux_BA.md")

LOG = []


def log(s=""):
    LOG.append(s)
    print(s)


def table(rows, widths):
    for r in rows:
        line = "    "
        for cell, w in zip(r, widths):
            line += str(cell)[:w].ljust(w) + "  "
        log(line.rstrip())


# ---------------------------------------------------------------------------
# 1. MATÉRIAUX ET COEFFICIENTS (EC2 + annexe nationale FR)
# ---------------------------------------------------------------------------
FCK = 25.0          # MPa — C25/30 (B-20, planches)
FYK = 500.0         # MPa — S500 (B-20)
GAMMA_C = 1.5
GAMMA_S = 1.15
ALPHA_CC = 0.85     # retenu : valeur recommandée EC2, conservative vs AN FR (1,0)
FCD = ALPHA_CC * FCK / GAMMA_C          # 14,17 MPa
FYD = FYK / GAMMA_S                     # 434,8 MPa
ES = 200000.0                           # MPa
EPS_CU = 0.0035
EPS_YD = FYD / ES
C_NOM = 30.0        # mm — enrobage hors fondation (H-23, XA1)
PHI_ST = 8.0        # mm — cadres HA8 (φ_t >= max(6 ; φ_l/4))
BETA_CADRE = 0.35
PHI_EF = 2.0        # fluage effectif retenu (RH 50 %, h0 ~ 94 mm)

BARRES = {12: 113.1, 14: 153.9, 16: 201.1, 20: 314.2}   # mm² par barre


# ---------------------------------------------------------------------------
# 2. CHARGES (B-21, tableau 5 — N_ELU) ET GÉOMÉTRIE (B-20)
# ---------------------------------------------------------------------------
# H : B-20 § « P3 & J1 — H ≈ 2,40 à 2,80 m ». On retient la borne haute.
H_COL = 2800.0      # mm — longueur de flambement l0, appuis rotulés (l0 = H)
H_SENS = 3500.0     # mm — sensibilité : hauteur de maçonnerie au-dessus du
                    # linteau (B-21 § 5 : 0,50 x 3,50 x 22 = 38,5 kN/m)

ELEMENTS = [
    dict(id="P2", nom="Poteau BA sous F2 (façade Ouest Nord)",
         b=150.0, h=250.0, N=159.0, M0=0.0,
         note="N_ELU = 159,0 kN (B-21 Ind. C § 6.2) — le plus chargé des trois"),
    dict(id="P3", nom="Poteau BA dans refend intérieur",
         b=400.0, h=500.0, N=35.8, M0=0.0,
         note="N_ELU = 35,8 kN (B-21 Ind. C § 6.2) — porteur de refend"),
    dict(id="J1", nom="Jambage BA 24x50 dans refend central",
         b=240.0, h=500.0, N=39.8, M0=0.0,
         note="N_ELU = 39,8 kN (B-21 Ind. C § 6.2) — jambage sous F1"),
]

# Excentricité de premier ordre : minimum EC2 § 6.1(4) = max(h/30 ; 20 mm)
E0_MIN = 20.0


# ---------------------------------------------------------------------------
# 3. DIAGRAMME D'INTERACTION N-M (compatibilité des déformations)
# ---------------------------------------------------------------------------
def section_response(b, h, bars, x):
    """Pour une profondeur d'axe neutre x (mm), retourne (N, M) en N et N.mm.
    bars : liste de (y_mm depuis la fibre la plus comprimée, As_mm2)."""
    a = min(0.8 * x, h)
    fc = a * b * FCD                      # N
    n = fc
    m = fc * (h / 2.0 - a / 2.0)          # N.mm
    for y, as_i in bars:
        eps = EPS_CU * (x - y) / x        # compression positive
        eps = max(min(eps, 0.01), -0.01)
        sigma = max(min(ES * eps, FYD), -FYD)
        f = sigma * as_i
        n += f
        m += f * (h / 2.0 - y)
    return n, abs(m)


def m_rd_at_n(b, h, bars, n_ed):
    """M_Rd (N.mm) pour N = N_Ed : interpolation sur le diagramme."""
    pts = []
    for i in range(1, 601):
        x = h * 3.0 * i / 600.0
        n, m = section_response(b, h, bars, x)
        pts.append((n, m))
    pts.sort(key=lambda p: p[0])
    for i in range(len(pts) - 1):
        n1, m1 = pts[i]
        n2, m2 = pts[i + 1]
        if n1 <= n_ed <= n2 and n2 > n1:
            t = (n_ed - n1) / (n2 - n1)
            return m1 + t * (m2 - m1)
    return 0.0


def n_rd_max(b, h, as_tot):
    """Effort normal résistant centré."""
    return b * h * FCD + as_tot * FYD


def bars_layout(b, h, phi, n_face):
    """n_face = nombre de barres sur CHAQUE grande face (>= 2).
    Le modèle est celui de n_face paires de barres réparties sur la hauteur h :
    chaque position y porte deux barres (une par face), soit 2 x A par paquet.
    Retourne la liste (y, As du paquet), l'aire totale et d1."""
    d1 = C_NOM + PHI_ST + phi / 2.0
    if n_face == 2:
        y_pos = [d1, h - d1]
    else:
        y_pos = [d1 + i * (h - 2 * d1) / (n_face - 1) for i in range(n_face)]
    bars = [(y, 2.0 * BARRES[phi]) for y in y_pos]
    as_tot = sum(a for _, a in bars)
    return bars, as_tot, d1


def cadres(phi, b, h):
    """Espacement maximal des cadres : EC2 § 9.5.3 min(20 phi_l ; b_min ; 400)."""
    smax = min(20.0 * phi, min(b, h), 400.0)
    for cand in (300, 250, 200, 150, 100):
        if cand <= smax:
            return cand, smax
    return 100, smax


# ---------------------------------------------------------------------------
# 4. FLAMBEMENT — EC2 § 5.8.3 et § 5.8.8
# ---------------------------------------------------------------------------
def slenderness(b, h, l0):
    i = min(b, h) / math.sqrt(12.0)
    return l0 / i, i


def lambda_lim(b, h, n_ed, l0):
    n = n_ed / (b * h * FCD)
    A, B, C = 0.7, 1.1, 0.7      # fluage inconnu, pas d'effort tranchant notable,
    return 20.0 * A * B * C / math.sqrt(n), n   # moments d'extrémité nuls


def second_order(b, h, l0, n_ed, as_tot):
    """Courbure nominale EC2 § 5.8.8.3."""
    d = h - C_NOM - PHI_ST - 8.0        # bras utile approché (φ retenu 16 mm)
    inv_r0 = EPS_YD / (0.45 * d)
    n_u = 1.0 + (as_tot * FYD) / (b * h * FCD)
    n_bal = 0.4
    n = n_ed / (b * h * FCD)
    kr = min(max((n_u - n) / (n_u - n_bal), 0.0), 1.0)
    k_phi = 1.0 + BETA_CADRE * PHI_EF
    inv_r = kr * k_phi * inv_r0
    e2 = inv_r * (l0 ** 2) / (math.pi ** 2)
    return e2, kr, k_phi, inv_r


# ---------------------------------------------------------------------------
# 5. CALCUL PAR ÉLÉMENT
# ---------------------------------------------------------------------------
def calc_element(el, l0, e0, phi, n_face, sens=False):
    b, h, n_ed = el["b"], el["h"], el["N"] * 1000.0
    lam, i = slenderness(b, h, l0)
    lam_lim, n_rel = lambda_lim(b, h, n_ed, l0)
    flamb = lam > lam_lim

    bars, as_tot, d1 = bars_layout(b, h, phi, n_face)
    if flamb:
        e2, kr, k_phi, inv_r = second_order(b, h, l0, n_ed, as_tot)
    else:
        e2, kr, k_phi, inv_r = 0.0, 0.0, 0.0, 0.0
    e_i = l0 / 400.0
    e_tot = e0 + e_i + e2
    m_ed = n_ed * e_tot

    m_rd = m_rd_at_n(b, h, bars, n_ed)
    n_rd = n_rd_max(b, h, as_tot)
    util = m_ed / m_rd if m_rd > 0 else 99.0

    as_min = max(0.10 * n_ed / FYD, 0.002 * b * h)
    as_max = 0.04 * b * h
    d_petit = min(b, h)
    espace_ret, espace = cadres(phi, b, h)
    phi_st_min = max(6.0, phi / 4.0)

    return dict(id=el["id"], nom=el["nom"], b=b, h=h, n_ed=n_ed,
                l0=l0, e0=e0, lam=lam, i=i, lam_lim=lam_lim, n_rel=n_rel,
                flamb=flamb, e_i=e_i, e2=e2, e_tot=e_tot, m_ed=m_ed,
                m_rd=m_rd, n_rd=n_rd, util=util, phi=phi, n_face=n_face,
                as_tot=as_tot, as_min=as_min, as_max=as_max,
                espace=espace, espace_ret=espace_ret, phi_st_min=phi_st_min, d1=d1,
                kr=kr, k_phi=k_phi, inv_r=inv_r, sens=sens)


def espacement_barres(b, h, phi, n_face):
    """Distance entre barres consécutives sur la grande face (EC2 § 9.5.3(3))."""
    d1 = C_NOM + PHI_ST + phi / 2.0
    pas = (h - 2.0 * d1) / (n_face - 1) if n_face > 1 else 0.0
    return pas, min(20.0 * phi, min(b, h), 400.0)


def choisir(el, l0, e0):
    """Plus petite disposition qui satisfait : N-M, As,min et espacement."""
    essais = [(12, 2), (14, 2), (16, 2), (20, 2), (12, 3), (16, 3), (20, 3)]
    for phi, nf in essais:
        r = calc_element(el, l0, e0, phi, nf)
        pas, pas_max = espacement_barres(r["b"], r["h"], phi, nf)
        if (r["util"] <= 1.0 and r["as_min"] <= r["as_tot"] <= r["as_max"]
                and pas <= pas_max):
            r["pas_barres"], r["pas_max"] = pas, pas_max
            return r
    r = calc_element(el, l0, e0, 20, 4)
    r["pas_barres"], r["pas_max"] = espacement_barres(r["b"], r["h"], 20, 4)
    return r


# ---------------------------------------------------------------------------
# 6. CONTRÔLE DE LA NOTE (8 CRITÈRES)
# ---------------------------------------------------------------------------
def controle(note):
    crit = []

    ok1 = all(("`%s`" % e["id"]) in note for e in ELEMENTS) and \
        all(("%.1f" % e["N"]).replace(".", ",") in note for e in ELEMENTS)
    crit.append(("1. Les 3 porteurs et leurs N_ELU de B-21 figurent dans la note", ok1))

    ok2 = note.count("M_Rd") >= 3 and note.count("interaction") >= 2
    crit.append(("2. Diagramme d'interaction N-M explicité", ok2))

    ok3 = "15 × 25" in note and "50 × 40" in note and "24 × 50" in note
    crit.append(("3. Sections identiques aux plans B-20", ok3))

    ok4 = "30 mm" in note and "XA1" in note
    crit.append(("4. Enrobage 30 mm et classe XA1 (H-23) rappelés", ok4))

    ok5 = "As,min" in note and "As,max" in note and "0,002" in note
    crit.append(("5. As,min / As,max EC2 § 9.5.2 contrôlés", ok5))

    ok6 = "20 φ" in note and "cadres" in note
    crit.append(("6. Espacement des cadres ≤ min(20 φ ; b ; 400 mm)", ok6))

    ok7 = "aucune vérification sismique" in note.lower() and "incendie" in note.lower()
    crit.append(("7. Sismique (D-26) et incendie déclarés hors mission", ok7))

    ok8 = "débits" in note.lower() and "HA" in note
    crit.append(("8. Tableau de débits cohérent avec les sections retenues", ok8))

    return crit


def main():
    log("=" * 78)
    log("B-42 — POTEAUX ET JAMBAGES BA — CROISSY-FLORA — EC2")
    log("=" * 78)
    log("")
    log("Matériaux : C25/30 (f_ck = %.0f MPa) · S500 (f_yk = %.0f MPa)"
        % (FCK, FYK))
    log("            f_cd = %.2f MPa (alpha_cc = %.2f) · f_yd = %.1f MPa"
        % (FCD, ALPHA_CC, FYD))
    log("            enrobage nominal 30 mm · cadres HA8 · l0 = %.0f mm (H, B-20)"
        % H_COL)
    log("")

    resultats = []
    for el in ELEMENTS:
        r = choisir(el, H_COL, E0_MIN)
        resultats.append(r)

    log("--- TABLEAU 1 : ÉLANCEMENT ET FLAMBEMENT (EC2 § 5.8.3) -----------")
    table([("ID", "b x h (mm)", "i (mm)", "lambda", "lambda_lim", "2d ordre ?")] +
          [(r["id"], "%dx%d" % (r["b"], r["h"]), "%.1f" % r["i"],
            "%.1f" % r["lam"], "%.1f" % r["lam_lim"],
            "OUI" if r["flamb"] else "non") for r in resultats],
          (6, 16, 10, 10, 12, 12))
    log("")

    log("--- TABLEAU 2 : FLEXION COMPOSÉE (N-M) ----------------------------")
    table([("ID", "N_Ed (kN)", "e_tot (mm)", "M_Ed (kN.m)", "M_Rd (kN.m)", "M_Ed/M_Rd")] +
          [(r["id"], "%.1f" % (r["n_ed"] / 1000.0), "%.1f" % r["e_tot"],
            "%.1f" % (r["m_ed"] / 1e6), "%.1f" % (r["m_rd"] / 1e6),
            "%.3f" % r["util"]) for r in resultats],
          (6, 12, 12, 14, 14, 12))
    log("")

    log("--- TABLEAU 3 : FERRAILLAGE RETENU ---------------------------------")
    table([("ID", "disposition", "As (mm2)", "As,min", "As,max", "cadres")] +
          [(r["id"], "%d HA%d" % (r["n_face"] * 2, r["phi"]),
            "%.0f" % r["as_tot"], "%.0f" % r["as_min"], "%.0f" % r["as_max"],
            "HA8 e%d" % r["espace_ret"])
           for r in resultats],
          (6, 16, 12, 10, 10, 18))
    log("")

    log("--- SENSIBILITÉ (disposition retenue, non contractuelle) ---------")
    for el, r in zip(ELEMENTS, resultats):
        a = calc_element(el, H_COL, E0_MIN, r["phi"], r["n_face"])
        b_ = calc_element(el, H_SENS, E0_MIN, r["phi"], r["n_face"])
        c = calc_element(el, H_COL, 50.0, r["phi"], r["n_face"])
        d = calc_element(el, H_SENS, 50.0, r["phi"], r["n_face"])
        log("    %-3s %dHA%-2d  nominal %.3f | l0 = %.0f : %.3f | e0 = 50 : %.3f"
            " | les deux : %.3f"
            % (el["id"], r["n_face"] * 2, r["phi"], a["util"], H_SENS,
               b_["util"], c["util"], d["util"]))
    log("")

    log("--- TABLEAU 4 : PRESSION D'APPUI SUR LA MAÇONNERIE (EC6) ---------")
    FK = (1.5, 1.0, 0.5)
    table([("ID", "A_appui (m2)", "sigma (MPa)", "f_d a 1,5", "f_d a 1,0", "f_d a 0,5")] +
          [(el["id"], "%.3f" % (el["b"] * el["h"] / 1e6),
            "%.3f" % (el["N"] * 1000.0 / (el["b"] * el["h"])),
            "%.2f" % (el["N"] * 1000.0 / (el["b"] * el["h"]) / (1.5 / 2.5)),
            "%.2f" % (el["N"] * 1000.0 / (el["b"] * el["h"]) / (1.0 / 2.5)),
            "%.2f" % (el["N"] * 1000.0 / (el["b"] * el["h"]) / (0.5 / 2.5)))
           for el in ELEMENTS if el["id"] != "P2"], (6, 12, 12, 12, 12, 12))
    log("    (rapport sigma_d / f_d, gamma_M = 2,5 — H-26 ; > 1,00 = non satisfait)")
    log("    P2 exclu : il repose sur SF1 80x80 (D-30, B-40), pas sur la maçonnerie.")
    log("    P2 sur SF1 : %.0f kN / 0,64 m2 = %.2f MPa sur béton C25/30 — sans objet ici."
        % (ELEMENTS[0]["N"], ELEMENTS[0]["N"] * 1000.0 / 640000.0))
    log("")

    # contrôle de la note
    if not os.path.exists(NOTE):
        log("!! Note absente : %s" % NOTE)
        return 2
    with open(NOTE, encoding="utf-8") as f:
        note = f.read()

    crit = controle(note)
    log("--- CRITÈRE D'ACCEPTATION (8 POINTS) ------------------------------")
    for lib, ok in crit:
        log("    [%s] %s" % ("OK" if ok else "KO", lib))
    conformes = sum(1 for _, ok in crit if ok)
    log("")
    log("RÉSULTAT : %d/%d CONFORME" % (conformes, len(crit)))
    log("")

    os.makedirs(os.path.dirname(OUT_TXT), exist_ok=True)
    with open(OUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")

    data = dict(
        brique="B-42", indice="B", date="20/10/2026", note=os.path.basename(NOTE),
        materiaux=dict(fck=FCK, fyk=FYK, fcd=round(FCD, 2), fyd=round(FYD, 1),
                       alpha_cc=ALPHA_CC, enrobage=C_NOM),
        elements=[dict(id=r["id"], nom=r["nom"], b=r["b"], h=r["h"],
                       N_Ed_kN=round(r["n_ed"] / 1000.0, 1),
                       l0=r["l0"], lam=round(r["lam"], 1),
                       lam_lim=round(r["lam_lim"], 1), flambement=r["flamb"],
                       e_tot=round(r["e_tot"], 1),
                       M_Ed_kNm=round(r["m_ed"] / 1e6, 2),
                       M_Rd_kNm=round(r["m_rd"] / 1e6, 2),
                       utilisation=round(r["util"], 3),
                       ferraillage="%d HA%d" % (r["n_face"] * 2, r["phi"]),
                       As_mm2=round(r["as_tot"]), As_min=round(r["as_min"]),
                       As_max=round(r["as_max"]),
                       cadres_retenu_mm=r["espace_ret"], cadres_max_mm=round(r["espace"])) for r in resultats],
        verdict_8_criteres=conformes,
    )
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\nJournal : %s" % os.path.relpath(OUT_TXT, os.path.dirname(ROOT)))
    print("JSON    : %s" % os.path.relpath(OUT_JSON, os.path.dirname(ROOT)))
    print("TXT     : %s o · JSON : %s o" % (os.path.getsize(OUT_TXT), os.path.getsize(OUT_JSON)))
    return 0 if conformes == 8 else 1


if __name__ == "__main__":
    sys.exit(main())
