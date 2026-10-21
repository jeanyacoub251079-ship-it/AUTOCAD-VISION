# -*- coding: utf-8 -*-
"""B-43 — PLANCHERS, PLANCHER HAUT ET DALLAGE — CROISSY-FLORA — Indice B.
Régime OUTILLÉ (V13). Toutes les valeurs numériques de la note sortent d'ici.
Entrées : B-21 Ind. C (§ 3 et § 6), D3 p. 10-12 (constitutions), D-35, D-31, D-32.
Sorties : _rendus/b43_planchers.txt / .json + _plans/FLORA_B43_DALLAGE_IndB.{dxf,png,pdf}
"""
import json
import math
import os

import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_TXT = os.path.join(ROOT, "_rendus", "b43_planchers.txt")
OUT_JSON = os.path.join(ROOT, "_rendus", "b43_planchers.json")
BASE = os.path.join(ROOT, "_plans", "FLORA_B43_DALLAGE_IndB")

LOG = []


def log(m=""):
    print(m)
    LOG.append(m)


def titre(m):
    log("")
    log(m)
    log("-" * 78)


def table(rows, widths):
    for r in rows:
        log("  " + "".join(str(c).ljust(w)[:w] for c, w in zip(r, widths)))


# ----------------------------------------------------------------- ENTRÉES
# Plancher A — D3 p. 10 (EXI-01a/b/e) + B-21 Ind. C § 3.5
A_B, A_H, A_E, A_L = 80.0, 180.0, 0.50, 2770.0     # mm, mm, m, mm
A_G, A_Q = 1.80, 2.50                              # kN/m²
E0_MEAN, E0_05 = 9000.0, 6000.0                    # MPa — C18
FM_K, FV_K, FC90_K = 18.0, 2.0, 2.2                # MPa — C18 (EN 338)
RHO_K = 320.0                                      # kg/m³
K_MOD, K_DEF, GAMMA_M = 0.80, 0.60, 1.30
KC90 = 1.25
L_APPUI = 100.0                                    # mm — longueur d'appui

# Plancher B — D3 p. 11-12 + B-21 Ind. C § 3.2
B_G, B_Q, B_E = 4.71, 2.50, 0.72                   # kN/m², kN/m², m

# Dallage — B-21 Ind. C § 3.6 + D-35
D_G, D_Q = 7.75, 2.50
D_EMPRISE = 111.15
D_H = 130.0                                        # mm — dallage BA (B-20)
D_C_NOM = 30.0                                     # mm — XC1/XC2, non en fondation
Q_ELS_ADM, Q_ELU_ADM = 300.0, 490.0                # kPa
FCTM, FYK = 2.56, 500.0
FOND_FORME = 400.0                                 # mm — D2 f. 03

# EC0 — coefficients partiels / psi (cat. B)
PSI1, PSI2 = 0.50, 0.30

# Vérification existante D3 (reprise, pour mémoire)
D3_FLE_SOLIVE = 7.7
D3_FLE_POUTRE = 72.8
D3_REACTION_IPE330 = 6.9                           # t


def main():
    os.makedirs(os.path.join(ROOT, "_rendus"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "_plans"), exist_ok=True)
    res = {}

    log("=" * 90)
    log("B-43 — PLANCHERS, PLANCHER HAUT ET DALLAGE — CROISSY-FLORA — INDICE A")
    log("CARNAC v3.0 — régime OUTILLÉ (V13) — EC2 / EC5 / NF DTU 13.3")
    log("=" * 90)

    # ---------------------------------------------------------- [1] DDC
    titre("[1] DESCENTE DE CHARGES D'EXÉCUTION — PAR ZONE (distincte de B-21)")
    log("  Coefficient psi : psi_1 = %.1f · psi_2 = %.1f (EC0 tableau A1.1, cat. B)"
        % (PSI1, PSI2))
    zones = [
        ("A — solives bois 8x18 @ 0,50", A_G, A_Q, "B-21 § 3.5 / D3 p. 10"),
        ("B — mixte IPE 160 @ 0,72 + hourdis", B_G, B_Q, "B-21 § 3.2 / D3 p. 11-12"),
        ("D — dallage rechargé (D-35)", D_G, D_Q, "B-21 § 3.6 / D-35"),
    ]
    rows = [("ZONE", "g (kN/m2)", "q (kN/m2)", "ELS car.", "ELS freq.", "ELS q-p", "ELU")]
    for nom, g, q, src in zones:
        rows.append(("" if not nom else nom[:36], "%.2f" % g, "%.2f" % q,
                     "%.2f" % (g + q), "%.2f" % (g + PSI1 * q),
                     "%.2f" % (g + PSI2 * q), "%.2f" % (1.35 * g + 1.5 * q)))
    table(rows, (40, 11, 11, 10, 11, 11, 8))
    log("")
    log("  Plancher haut d'étage (E-07) : AUCUNE charge établie — nature du support inconnue.")
    res["zones"] = {n.split(" —")[0]: {"g": g, "q": q,
                                      "els": round(g + q, 2),
                                      "elu": round(1.35 * g + 1.5 * q, 2)}
                    for n, g, q, _ in zones}

    # ------------------------------------------------- [2] ZONE A — SOLIVES
    titre("[2] ZONE A — SOLIVE BOIS 8x18 @ 0,50 m, PORTÉE 2,77 m — EC5")
    p_elu = (1.35 * A_G + 1.5 * A_Q) * A_E
    p_els = (A_G + A_Q) * A_E
    L = A_L / 1000.0
    M = p_elu * L ** 2 / 8.0
    V = p_elu * L / 2.0
    W = A_B * A_H ** 2 / 6.0
    I = A_B * A_H ** 3 / 12.0
    fm_d = K_MOD * FM_K / GAMMA_M
    fv_d = K_MOD * FV_K / GAMMA_M
    fc90_d = K_MOD * FC90_K / GAMMA_M
    sigma_m = M * 1e6 / W
    tau = 1.5 * V * 1e3 / (A_B * A_H)
    r_flex = sigma_m / fm_d
    r_shear = tau / fv_d
    sig_c90 = V * 1e3 / (A_B * L_APPUI)
    r_c90 = sig_c90 / (KC90 * fc90_d)

    # flèches — EC5 §7.2 / §7.4
    pG, pQ = A_G * A_E, A_Q * A_E
    def w(p):
        return 5.0 * p * (A_L ** 4) / (384.0 * E0_MEAN * I)
    w_inst_tot = w(pG + pQ)
    w_inst_G, w_inst_Q = w(pG), w(pQ)
    w_fin = w_inst_G * (1 + K_DEF) + w_inst_Q * (1 + PSI2 * K_DEF)
    lim_inst, lim_fin = A_L / 300.0, A_L / 250.0

    log("  p_ELU = (1,35 x %.2f + 1,50 x %.2f) x %.2f = %.2f kN/m"
        % (A_G, A_Q, A_E, p_elu))
    log("  M_Ed = %.2f kN.m · V_Ed = %.2f kN" % (M, V))
    log("  W = b h2/6 = %.0f mm3 · I = b h3/12 = %.3e mm4" % (W, I))
    log("  f_m,d = %.2f x %.0f / %.1f = %.2f MPa · f_v,d = %.2f MPa"
        % (K_MOD, FM_K, GAMMA_M, fm_d, fv_d))
    log("  f_c,90,d = %.2f x 2.2 / 1.3 = %.2f MPa · k_c,90 = 1.25 (appui 100 mm)"
        % (K_MOD, fc90_d))
    rows = [("VÉRIFICATION", "ED", "RD", "RATIO", "VERDICT"),
            ("Flexion EC5 6.1.6", "%.2f MPa" % sigma_m, "%.2f MPa" % fm_d,
             "%.3f" % r_flex, "OK" if r_flex <= 1 else "NON"),
            ("Cisaillement EC5 6.1.7", "%.3f MPa" % tau, "%.2f MPa" % fv_d,
             "%.3f" % r_shear, "OK" if r_shear <= 1 else "NON"),
            ("Compression appui EC5 6.1.5", "%.3f MPa" % sig_c90,
             "%.2f MPa" % (KC90 * fc90_d), "%.3f" % r_c90, "OK" if r_c90 <= 1 else "NON"),
            ("Flèche instantanée EC5 7.2", "%.1f mm" % w_inst_tot,
             "%.1f mm (L/300)" % lim_inst,
             "%.3f" % (w_inst_tot / lim_inst), "OK" if w_inst_tot <= lim_inst else "NON"),
            ("Flèche finale EC5 7.2", "%.1f mm" % w_fin,
             "%.1f mm (L/250)" % lim_fin,
             "%.3f" % (w_fin / lim_fin), "OK" if w_fin <= lim_fin else "NON")]
    table(rows, (34, 12, 18, 9, 9))
    log("  Flèche finale = %.2f x (1 + %.1f) + %.2f x (1 + %.1f x %.1f) = %.1f mm"
        % (w_inst_G, K_DEF, w_inst_Q, PSI2, K_DEF, w_fin))
    log("  A_s : sans objet — section pleine bois, pas d'armature (EC5 §6.1).")
    log("  Déversement : solives maintenues en compression par le parquet continu")
    log("  → EC5 6.3.3 non déclenché (maintien latéral continu, k_crit = 1).")
    log("  Réaction par solive : R_Ed = %.2f kN · par ml d'appui : %.2f kN/m"
        % (V, V / (A_E * 1000.0 / 1000.0)))

    res["zoneA"] = dict(p_elu=round(p_elu, 2), M=round(M, 2), V=round(V, 2),
                        sigma_m=round(sigma_m, 2), fm_d=round(fm_d, 2),
                        r_flex=round(r_flex, 3), tau=round(tau, 3),
                        fv_d=round(fv_d, 2), r_shear=round(r_shear, 3),
                        sig_c90=round(sig_c90, 3), r_c90=round(r_c90, 3),
                        w_inst=round(w_inst_tot, 2), w_fin=round(w_fin, 2),
                        lim_inst=round(lim_inst, 2), lim_fin=round(lim_fin, 2))

    # --------------------------------------------- [3] ZONE A — POUTRE 20x15
    titre("[3] ZONE A — POUTRE 20x15 (b = 200, h = 150) — RÉACTIONS, PUIS RENVOI B-45")
    p_poutre = p_elu * (A_L / 1000.0) / 2.0     # bande apportée par les solives
    log("  Charge linéaire apportée par les solives : %.2f x %.2f / 2 = %.2f kN/m"
        % (p_elu, L, p_poutre))
    log("  Réaction d'about (portée 4,34 m) : %.2f kN par appui" % (p_poutre * 4.34 / 2.0))
    log("  Flèche constatée D3 p. 10-13 : %.1f mm pour %.1f mm admis (L/417)."
        % (D3_FLE_POUTRE, 4340.0 / 417.0))
    log("  → La poutre EXISTANTE est hors limites : son renfort par moisage (R1) est")
    log("    dimensionné en B-45, pas ici. B-43 fournit la charge et la réaction.")
    res["zoneA_poutre"] = dict(p=round(p_poutre, 2),
                               R=round(p_poutre * 4.34 / 2.0, 2),
                               fleche_d3=D3_FLE_POUTRE)

    # ------------------------------------------------------- [4] ZONE B
    titre("[4] ZONE B — PLANCHER MIXTE EXISTANT (IPE 160 @ 0,72 + hourdis) — RENVOI B-45")
    p_b = (1.35 * B_G + 1.5 * B_Q) * B_E
    log("  p_ELU par solive = (1,35 x %.2f + 1,50 x %.2f) x %.2f = %.2f kN/m"
        % (B_G, B_Q, B_E, p_b))
    log("  Charge surfacique ELU = %.2f kN/m2 · ELS = %.2f kN/m2"
        % (1.35 * B_G + 1.5 * B_Q, B_G + B_Q))
    log("  Hourdis briques 7 cm + chape 10 cm : éléments de maçonnerie existants,")
    log("    ni BA ni bois — EC2 et EC5 ne s'y appliquent pas.")
    log("  IPE 160 et IPE 330 : vérification de section en B-45 (EC3).")
    log("  Diagnostic D3 p. 12 : flèche IPE 160 OK, IPE 330 OK, déversement IPE 160")
    log("    instable → entretoises Stab1 retenues par B-20. Réaction IPE 330 : %.1f t."
        % D3_REACTION_IPE330)
    log("  → B-43 ne dimensionne pas cette zone : il en fixe la charge et la réaction.")
    res["zoneB"] = dict(p_solive=round(p_b, 2),
                        p_elu=round(1.35 * B_G + 1.5 * B_Q, 2),
                        p_els=round(B_G + B_Q, 2),
                        reaction_ipe330_t=D3_REACTION_IPE330)

    # ------------------------------------------------------- [5] ZONE C
    titre("[5] ZONE C — PLANCHER HAUT D'ÉTAGE (E-07) — AUCUN CALCUL POSSIBLE")
    log("  D3 p. 4 et p. 10 : « plancher haut non sondé » (cage centrale).")
    log("  Ni nature, ni épaisseur, ni portée ne sont établies → aucune formule.")
    log("  V15 : la chaîne toiture → potelets → plancher haut → murs est ROMPUE ici.")
    log("  → Réserve R-43-1 · point d'arrêt PA-03 · aucun chiffre produit.")
    res["zoneC"] = dict(calcul=False, reserve="R-43-1", pa="PA-03")

    # ------------------------------------------------------- [6] DALLAGE
    titre("[6] ZONE D — DALLAGE SUR TERRE-PLEIN, 100 % DE L'EMPRISE (D-35)")
    p_els_d = D_G + D_Q
    p_elu_d = 1.35 * D_G + 1.5 * D_Q
    sig_els, sig_elu = p_els_d, p_elu_d              # kN/m2 = kPa
    N_tot = p_elu_d * D_EMPRISE
    log("  g = %.2f · q = %.2f → p_ELS = %.2f · p_ELU = %.2f kN/m2"
        % (D_G, D_Q, p_els_d, p_elu_d))
    log("  Emprise rechargée : %.2f m2 → N_ELU total = %.0f kN" % (D_EMPRISE, N_tot))
    rows = [("CRITÈRE", "VALEUR", "ADMISSIBLE", "TAUX", "VERDICT"),
            ("Portance ELS", "%.1f kPa" % sig_els, "%.0f kPa" % Q_ELS_ADM,
             "%.1f %%" % (100 * sig_els / Q_ELS_ADM), "OK"),
            ("Portance ELU", "%.1f kPa" % sig_elu, "%.0f kPa" % Q_ELU_ADM,
             "%.1f %%" % (100 * sig_elu / Q_ELU_ADM), "OK")]
    table(rows, (22, 12, 14, 9, 9))
    log("  → la portance n'est pas le critère : le sol est sollicité à moins de 3 %.")
    log("")
    log("  Flexion : sous charge répartie, un dallage continu sur fond de forme suit")
    log("  son support — le moment de flexion tend vers zéro. Les moments réels")
    log("  proviennent des tassements différentiels (HORS MISSION, D-15) et des")
    log("  charges concentrées (aucune dans le programme actuel).")
    log("  → l'épaisseur est gouvernée par les dispositions constructives, pas par M_Ed.")
    d_util = D_H - D_C_NOM - 8.0
    as_min1 = 0.26 * FCTM / FYK * 1000.0 * d_util
    as_min2 = 0.0013 * 1000.0 * d_util
    as_min = max(as_min1, as_min2)
    st25c = 257.0                                     # mm2/m — ST25C Ø7 e150
    log("  A_s,min EC2 9.3.1.1 = max(0,26 x %.2f / %.0f x b d ; 0,0013 b d) = %.0f mm2/m"
        % (FCTM, FYK, as_min))
    log("  Treillis retenu : ST25C (Ø7 e150) = %.0f mm2/m → %.2f x A_s,min"
        % (st25c, st25c / as_min))
    log("  Fissuration EC2 7.3 : w_k <= 0,30 mm (XC1/XC2). Règles indirectes :")
    log("    espacement des fils 150 mm <= 300 mm et Ø 7 mm <= 16 mm → satisfait sans calcul.")
    res["dallage"] = dict(g=D_G, q=D_Q, p_els=round(p_els_d, 2), p_elu=round(p_elu_d, 2),
                          emprise=D_EMPRISE, N_elu=round(N_tot, 0),
                          taux_els=round(100 * sig_els / Q_ELS_ADM, 1),
                          taux_elu=round(100 * sig_elu / Q_ELU_ADM, 1),
                          h=D_H, d=round(d_util, 0), as_min=round(as_min, 0),
                          treillis="ST25C", as_treillis=st25c,
                          ratio_treillis=round(st25c / as_min, 2))

    # joints et panneaux — NF DTU 13.3 / NF P11-213
    log("")
    log("  JOINTS DE RETRAIT — NF DTU 13.3 (dallage) / NF P11-213 :")
    log("    - joints sciés sur 1/3 de l'épaisseur (%.0f mm) dès que le béton porte," % (D_H / 3))
    log("      au plus tard 24 h après coulage, avant toute circulation ;")
    log("    - espacement maximal retenu : 4,50 m dans les deux sens ;")
    log("    - surface maximale d'un panneau : 4,50 x 4,50 = 20,25 m2 ;")
    n_panneaux = math.ceil(D_EMPRISE / 20.25)
    log("    - emprise %.2f m2 → au moins %d panneaux." % (D_EMPRISE, n_panneaux))
    log("    - joints de retrait ≠ joints de dilatation : D-28 interdit les seconds,")
    log("      pas les premiers. Un dallage de 111 m2 sans joint de retrait fissure.")
    res["dallage"]["joints"] = dict(espacement=4.5, profondeur=round(D_H / 3, 0),
                                    panneau_max=20.25, n_panneaux=n_panneaux)

    # désolidarisation
    log("")
    log("  DÉSOLIDARISATION — au droit de CHAQUE semelle, poteau, mur et ouvrage")
    log("  existant (D-09, D-35) : polystyrène 20 mm + mastic souple en surface,")
    log("  sur toute la hauteur du dallage, + film polyane remonté.")
    log("  Consigne de coulage : dallage coulé À MÊME les semelles, jamais compacté")
    log("  sur leur débord ; vibration à 200 mm du joint minimum.")
    res["dallage"]["desolidarisation"] = "polystyrene 20 mm + mastic, perimetre et au droit de chaque appui"

    # --------------------------------------------------- [7] APPUIS → B-50
    titre("[7] EFFORTS AUX APPUIS TRANSMIS À B-50 (assemblages) ET B-46 (existant)")
    R_solive = V
    R_ml = R_solive / (A_E * 1000.0) * 1000.0     # kN par mètre d'appui
    rows = [("APPUI", "OUVRAGE", "EFFORT", "UNITÉ", "DESTINATAIRE"),
            ("Solives A", "mur / poutre 20x15", "%.2f" % R_solive, "kN/solive", "B-50 · B-46"),
            ("Ligne A", "appui continu", "%.2f" % R_ml, "kN/m", "B-46"),
            ("Poutre 20x15", "about", "%.2f" % (p_poutre * 4.34 / 2.0), "kN", "B-45 · B-50"),
            ("IPE 160 (B)", "charge linéaire", "%.2f" % p_b, "kN/m", "B-45"),
            ("IPE 330 (B)", "appui central", "%.1f" % (D3_REACTION_IPE330 * 9.81), "kN (D3)", "B-46"),
            ("Dallage", "sol support", "%.1f" % sig_elu, "kPa (ELU)", "B-40")]
    table(rows, (16, 22, 12, 26, 18))
    res["appuis"] = dict(solive=round(R_solive, 2), ligne=round(R_ml, 2),
                         poutre=round(p_poutre * 4.34 / 2.0, 2),
                         ipe160=round(p_b, 2),
                         ipe330=round(D3_REACTION_IPE330 * 9.81, 1),
                         dallage=round(sig_elu, 1))

    # ------------------------------------------------------------ PLANCHE
    dessiner(res)

    with open(OUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    res["journal_octets"] = os.path.getsize(OUT_TXT)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    log("")
    log("Journal : %s (%d o)" % (OUT_TXT, os.path.getsize(OUT_TXT)))
    log("JSON    : %s (%d o)" % (OUT_JSON, os.path.getsize(OUT_JSON)))
    return 0


# ------------------------------------------------------------------ PLAN
def dessiner(res):
    doc = ezdxf.new("R2018", setup=True)
    msp = doc.modelspace()
    for nom, coul in (("PLANCHER-AXES", 1), ("PLANCHER-COFFRAGE", 5),
                      ("PLANCHER-ACIER-INF", 3), ("PLANCHER-ACIER-SUP", 4),
                      ("PLANCHER-HABILLAGE-TEXTE", 7), ("PLANCHER-COTATION", 8),
                      ("PLANCHER-JOINTS", 6), ("PLANCHER-DESOLID", 30),
                      ("PLANCHER-CARTOUCHE", 7)):
        doc.layers.add(nom, color=coul)

    def txt(x, y, t, ht=2.4, layer="PLANCHER-HABILLAGE-TEXTE"):
        e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
        e.set_placement((x, y))
        return e

    def rect(x0, y0, x1, y1, layer="PLANCHER-COFFRAGE"):
        msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                           dxfattribs={"layer": layer})

    def ligne(x0, y0, x1, y1, layer="PLANCHER-COFFRAGE"):
        msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})

    def rap(px, py, tx, ty, t, ht=2.2, layer="PLANCHER-HABILLAGE-TEXTE"):
        msp.add_lwpolyline([(px, py), (tx - 4, ty), (tx, ty)], dxfattribs={"layer": layer})
        txt(tx + 1.5, ty + 0.8, t, ht, layer)

    S = 1 / 5.0                      # mm réel -> mm papier (échelle 1:5)

    # cadre A3 paysage
    rect(8, 8, 412, 289, "PLANCHER-CARTOUCHE")
    txt(14, 279, "CROISSY-FLORA — B-43 — DALLAGE : FERRAILLAGE, JOINTS DE RETRAIT, DÉSOLIDARISATION", 4.0, "PLANCHER-AXES")
    txt(14, 272, "Indice B — 20/10/2026 — NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 2.8, "PLANCHER-AXES")
    txt(14, 266.5, "AUCUN JOINT DE DILATATION (D-28) — LES JOINTS DE RETRAIT NE SONT PAS DES JOINTS DE DILATATION",
        2.6, "PLANCHER-JOINTS")
    txt(14, 261.5, "D-09 : DALLAGE COULÉ À MÊME LES SEMELLES, DÉSOLIDARISÉ — JAMAIS SUR LEUR DÉBORD",
        2.6, "PLANCHER-DESOLID")

    # ---------------------------------------------------- DÉTAIL 1 : coupe
    txt(14, 254, "1. COUPE DU COMPLEXE — 1:5", 3.0, "PLANCHER-AXES")
    x1, y1 = 24.0, 138.0
    w = 300 * S                      # 60
    gnt, dal, rev = 400 * S, D_H * S, 20 * S
    rect(x1, y1, x1 + w, y1 + gnt, "PLANCHER-COFFRAGE")
    for k in range(1, 8):            # hachures GNT
        yk = y1 + k * gnt / 8.0
        ligne(x1, yk, x1 + w, yk, "PLANCHER-COTATION")
    y_dal = y1 + gnt
    rect(x1, y_dal, x1 + w, y_dal + dal, "PLANCHER-COFFRAGE")
    ligne(x1, y_dal + 1.5, x1 + w, y_dal + 1.5, "PLANCHER-DESOLID")
    y_tr = y_dal + 40 * S
    ligne(x1, y_tr, x1 + w, y_tr, "PLANCHER-ACIER-INF")
    for k in range(9):
        xk = x1 + 4 + k * 6.5
        ligne(xk, y_tr - 1.2, xk + 1.2, y_tr + 1.2, "PLANCHER-ACIER-INF")
    y_rev = y_dal + dal
    rect(x1, y_rev, x1 + w, y_rev + rev, "PLANCHER-COFFRAGE")
    for k in range(1, 6):
        ligne(x1 + k * w / 6.0, y_rev, x1 + k * w / 6.0, y_rev + rev, "PLANCHER-COTATION")
    rap(x1 + w - 2, y_rev + rev - 1, 100, 250, "Revêtement de sol 2 cm (hors lot GO)")
    rap(x1 + w - 2, y_dal + dal / 2, 100, y_dal + dal / 2 + 2, "Dallage BA C25/30 — ép. 13 cm")
    rap(x1 + w - 2, y_tr, 100, y_tr - 3, "Treillis ST25C (Ø7 e150) — 257 mm²/m", 2.2, "PLANCHER-ACIER-INF")
    rap(x1 + w - 2, y_dal + 1.5, 100, y_dal - 5, "Film polyane 200 µm remonté sur 10 cm", 2.2, "PLANCHER-DESOLID")
    rap(x1 + w - 2, y1 + gnt / 2, 100, y1 + gnt / 2, "Fond de forme GNT 40 cm (D2 f. 03)")

    # ---------------------------------------------------- DÉTAIL 2 : joint
    txt(14, 128, "2. JOINT DE RETRAIT SCIÉ — 1:5", 3.0, "PLANCHER-AXES")
    x2, y2 = 24.0, 97.0
    rect(x2, y2, x2 + w, y2 + dal, "PLANCHER-COFFRAGE")
    ligne(x2 + w / 2, y2 + dal, x2 + w / 2 + 4, y2 + dal - D_H / 3 * S, "PLANCHER-JOINTS")
    ligne(x2 + w / 2 + 4, y2 + dal - D_H / 3 * S, x2 + w / 2 + 8, y2 + dal, "PLANCHER-JOINTS")
    ligne(x2, y2 + 7, x2 + w, y2 + 7, "PLANCHER-ACIER-INF")
    rap(x2 + w / 2 + 4, y2 + dal - D_H / 3 * S, 100, 118,
        "Saignée 43 mm (1/3 de l'épaisseur), ouverte à la règle", 2.2, "PLANCHER-JOINTS")
    rap(x2 + w - 2, y2 + 7, 100, 106,
        "Treillis continu : aucune armature coupée", 2.2, "PLANCHER-ACIER-INF")
    rap(x2 + w - 2, y2 + dal - 2, 100, 112,
        "Espacement 4,50 m max — panneau ≤ 20,25 m²")
    txt(100, 99, "Joint de retrait ≠ joint de dilatation (D-28 : aucun)", 2.2, "PLANCHER-AXES")

    # ----------------------------------------- DÉTAIL 3 : désolidarisation
    txt(14, 88, "3. DÉSOLIDARISATION AU DROIT D'UNE SEMELLE OU D'UN MUR — SCHÉMA DE PRINCIPE, SANS ÉCHELLE", 2.7, "PLANCHER-AXES")
    x3, y3 = 24.0, 50.0
    rect(x3, y3, x3 + 60 * S, y3 + 25 * S, "PLANCHER-COFFRAGE")          # semelle
    rect(x3 + 10 * S, y3 + 25 * S, x3 + 50 * S, y3 + 60 * S, "PLANCHER-COFFRAGE")  # fût
    rect(x3 + 60 * S, y3, x3 + 80 * S, y3 + 60 * S, "PLANCHER-DESOLID")  # polystyrène
    rect(x3 + 80 * S, y3 + 12 * S, x3 + 200 * S, y3 + 38 * S, "PLANCHER-COFFRAGE")  # dallage
    ligne(x3 + 80 * S, y3 + 20 * S, x3 + 200 * S, y3 + 20 * S, "PLANCHER-ACIER-INF")
    rap(x3 + 14, y3 + 22 * S, 105, 82, "Polystyrène 20 mm sur toute la hauteur du dallage", 2.2, "PLANCHER-DESOLID")
    rap(x3 + 16, y3 + 38 * S, 105, 76, "Mastic souple en surface")
    rap(x3 + 34, y3 + 20 * S, 105, 70, "Treillis arrêté à 20 mm du joint", 2.2, "PLANCHER-ACIER-INF")
    rap(x3 + 6, y3 + 30 * S, 105, 64, "Semelle et poteau (B-40) — neuf ou existant")
    txt(108, 52, "Compactage interdit sur le débord de semelle (D-09).", 1.9)

    # --------------------------------------------- DÉTAIL 4 : recouvrement
    txt(14, 42, "4. RECOUVREMENT DU TREILLIS — SCHÉMA DE PRINCIPE, SANS ÉCHELLE", 2.7, "PLANCHER-AXES")
    x4, y4 = 24.0, 25.0
    ligne(x4, y4 + 4, x4 + 150 * S + 20, y4 + 4, "PLANCHER-ACIER-INF")
    ligne(x4 + 120 * S, y4 + 8, x4 + 250 * S, y4 + 8, "PLANCHER-ACIER-INF")
    txt(x4 + 118 * S, y4 + 9, "Recouvrement : 2 mailles + 50 mm (300 mm mini)", 2.1, "PLANCHER-ACIER-INF")

    # ----------------------------------------------------------- NOTES
    nx0, ny0, nx1, ny1 = 205, 100, 405, 190
    rect(nx0, ny0, nx1, ny1, "PLANCHER-CARTOUCHE")
    notes = [
        ("NOTES OPPOSABLES", 3.0, "PLANCHER-AXES"),
        ("1. Dallage BA C25/30 ép. 13 cm sur fond de forme GNT 40 cm (D2 f. 03).", 2.3, None),
        ("2. Treillis ST25C (Ø7 e150) = 257 mm²/m ≥ A_s,min = 122 mm²/m (EC2 9.3.1.1).", 2.3, None),
        ("3. Enrobage 30 mm (XC1/XC2) — le dallage n'est PAS en fondation (50 mm).", 2.3, None),
        ("4. Joints de retrait sciés tous les 4,50 m max, 43 mm de profondeur, sous 24 h.", 2.3, None),
        ("5. Désolidarisation périmétrique et au droit de chaque semelle, poteau et mur.", 2.3, None),
        ("6. AUCUN joint de dilatation (D-28) — les joints de retrait ne le sont pas.", 2.3, None),
        ("7. Charge : g 7,75 · q 2,50 → p_ELU 14,21 kN/m² sur 111,15 m² (D-35).", 2.3, None),
        ("8. Portance sol : 14,2 kPa à l'ELU = 2,9 % de 490 kPa — non gouvernante.", 2.3, None),
        ("9. Protection anti-termites PRESCRITE au CCTP (D1 01.2.1.9.2) — classe à justifier.", 2.3, None),
        ("10. Protection au feu adéquate à prévoir (hors lot GO).", 2.3, None),
    ]
    for k, (t, h, lay) in enumerate(notes):
        txt(nx0 + 4, ny1 - 8 - k * 6.4, t, h, lay or "PLANCHER-HABILLAGE-TEXTE")

    # ------------------------------------------------------- CARTOUCHE
    cx0, cy0, cx1, cy1 = 180, 10, 405, 62
    rect(cx0, cy0, cx1, cy1, "PLANCHER-CARTOUCHE")
    txt(cx0 + 4, cy1 - 10, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 3.4, "PLANCHER-AXES")
    txt(cx0 + 4, cy1 - 18, "B-43 — PLANCHERS, PLANCHER HAUT & DALLAGE — DALLAGE : PRINCIPES", 2.7)
    txt(cx0 + 4, cy1 - 25, "Brique B-43 · Indice B · 20/10/2026 · Mode PARTIEL-DÉCLARÉ · Unités DXF : mm", 2.2)
    txt(cx0 + 4, cy1 - 32, "Détails 1 et 2 au 1:5 · schémas 3 et 4 sans échelle · CARNAC v3.0 · EC2 / NF DTU 13.3", 2.2)
    txt(cx0 + 4, cy1 - 42, "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 4.2, "PLANCHER-AXES")

    chemin = BASE + ".dxf"
    doc.saveas(chemin)
    audit = doc.audit()
    log("  écrit : %s (%d o) — audit %d erreur(s)"
        % (chemin, os.path.getsize(chemin), len(audit.errors)))

    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(msp, finalize=False)
    ax.set_xlim(0, 420)
    ax.set_ylim(0, 297)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    fig.savefig(BASE + ".png", dpi=200, facecolor="white")
    fig.savefig(BASE + ".pdf", facecolor="white")
    plt.close(fig)
    log("  rendus : %s.png / .pdf" % BASE)


if __name__ == "__main__":
    raise SystemExit(main())
