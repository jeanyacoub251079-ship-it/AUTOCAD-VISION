#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-49 — LINTEAUX ET SEUILS — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13) — EC3 §6.2 / EC6 §8.1.6 / triangle de charge.

Sorties : _rendus/b49_linteaux.txt / .json + _plans/FLORA_B49_LINTEAUX_IndA.{dxf,png,pdf}

Périmètre :
  - 5 linteaux MÉTALLIQUES NEUFS (F1a/b/c, R3-N/S) — type linteau métallique.
  - Linteaux bois existants E-08 : COURT-CIRCUITÉS par R3 (B-20) — non calculés.
  - Linteau bois Ouest sous P1 : SOULAGÉ par P1, pas un linteau de notre lot.
  - Seuils BA : SANS OBJET (aucune prescription D1/D2/D4).
Aucun scellement calculé (B-50). Aucune protection incendie dimensionnée.
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_rendus")
PLANS = os.path.join(ROOT, "_plans")
BASE = os.path.join(PLANS, "FLORA_B49_LINTEAUX_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


# ============================================================== DONNÉES
FY = 275.0            # S275 — MAT-05f
GM0 = 1.0
E = 210000.0          # MPa
GAMMA = 22.0          # kN/m3 — moellons (B-21)
T_MUR = 0.50          # m
H_MUR = 3.50          # m — hauteur de maçonnerie au-dessus (B-21 §5)
G_PLAN = 4.71         # kN/m² — plancher B (B-21 C)
Q_PLAN = 2.50         # kN/m² — D-32
BANDE = 1.00          # m — bande tributaire F1 (B-21)
FD = 1.5 / 2.5        # 0,60 MPa — H-25 / D-34

# HEA 200 (B-45) — 2 profilés
WPL_HEA = 429.5       # cm3
A_HEA = 53.8          # cm2
IY_HEA = 3692.0       # cm4
M_RD_F1 = 2 * WPL_HEA * 1e3 * FY / GM0 / 1e6          # 236.2 kN.m
V_RD_F1 = 573.2                                        # kN — B-45 (2 × Av)

# UPE 200 (B-45)
WPL_UPE = 224.0
IY_UPE = 1910.0
M_RD_R3 = WPL_UPE * 1e3 * FY / GM0 / 1e6              # 61.6 kN.m
P_R3 = 46.2           # kN — réaction R2-N ELU (B-21 §5)
L_BAIE = 1.55         # m
L_PROF_R3 = 2.50      # m — profilé livré

# Enveloppe B-45 (charge mur pleine hauteur — conservatrice)
P_ELU_ENV = 71.4      # kN/m
P_ELS_ENV = 52.6
L_CALC_F1 = 1.25      # m — B-45


def triangle(L):
    """Triangle isocèle 60° (pratique FR / DTU 20.1) — h = L × √3/2."""
    h = L * math.sqrt(3.0) / 2.0
    form = h <= H_MUR
    Wk = 0.5 * L * min(h, H_MUR) * T_MUR * GAMMA     # kN
    return h, form, Wk


# ============================================================== EN-TÊTE
titre("=" * 78)
log("B-49 — LINTEAUX ET SEUILS — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13) — EC3 §6.2 / EC6 §8.1.6 / triangle 60°")
log("Type : LINTEAU MÉTALLIQUE (5 neufs). Seuils BA : SANS OBJET.")
log("Mode : PARTIEL-DÉCLARÉ (SEC-01 non dimensionnée — hors lot GO).")
log("=" * 78)

titre("[0] HYPOTHÈSES ET CLAUSES OPPOSABLES")
log("  D-34 : f_k = 1,5 MPa HYPOTHÈSE — essais hors mission, reprise chiffrée.")
log("  D-26 : AUCUNE VÉRIFICATION SISMIQUE (zone 1).")
log("  D-28 : AUCUN JOINT DE DILATATION.")
log("  D-09 : ARASE −1,00 M / TN MINIMUM — ÉGALISATION GROS BÉTON SI ÉCART.")
log("  D-36 : remplissage béton C25/30 des UPE 200 de R3 — ACCEPTÉ.")
log("  D-37 : coussin w_b ≥ 300 mm sous R1, F2, F3 — ACCEPTÉ (B-46, pas un linteau).")
log("  Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée.")

titre("[1] INVENTAIRE — PREUVE D'ÉPUISEMENT (V14)")
INV = [
    ("L1", "F1a", "2×HEA 200", "1,00", "refend central File D", "NEUF — D2 f.01"),
    ("L2", "F1b", "2×HEA 200", "0,90", "mur Nord hall File 4", "NEUF — D2 f.01"),
    ("L3", "F1c", "2×HEA 200", "0,85", "mur Sud hall File 3", "NEUF — D2 f.01"),
    ("L4", "R3-N", "UPE 200+béton", "1,55", "façade Est baie N", "NEUF — D2 f.01 · D-36"),
    ("L5", "R3-S", "UPE 200+béton", "1,55", "façade Est baie S", "NEUF — D2 f.01 · D-36"),
    ("E-08", "2 linteaux bois", "existant déformé", "1,55", "façade Est Désordre 1", "COURT-CIRCUITÉ par R3"),
    ("—", "linteau bois Ouest", "23×15 existant", "2,52", "façade Ouest Sud", "SOULAGÉ par P1 — hors lot"),
    ("—", "seuils BA", "—", "—", "—", "SANS OBJET — 0 prescription"),
]
log("  %-6s %-18s %-16s %-6s %-24s %s" % ("RÉF", "OUVRAGE", "SECTION", "L m", "EMPLACEMENT", "STATUT"))
for r in INV:
    log("  %-6s %-18s %-16s %-6s %-24s %s" % r)
log("")
log("  Épuisement : D1 § 01.2.1 (aucun seuil BA, aucun linteau BA prescrit) ·")
log("  D2 f.01 (F1 2×HEA 200, R3 UPE 200, P1 sous linteau bois) · D3 p.5 (Désordre 1,")
log("  2 linteaux non porteurs façade Est) · D3 p.16 (linteau bois Ouest 23×15) ·")
log("  D4 p.23-25 (GEO-05 baies, aucun seuil structurel) · B-20 §4-5 · B-21 §5 ·")
log("  B-23 désordre 1 · B-24 E-08 · B-45 §4 et §9 · B-46 Z2/Z4 · B-50 A3/A6.")
log("  Aucun linteau BA. Aucun seuil BA. Aucun linteau maçonnerie neuf.")

# ============================================================== F1 triangle
titre("[2] F1a/b/c — LINTEAUX COURTS : TRIANGLE DE CHARGE (60°)")
log("  Formule : h_Δ = L × √3/2  (triangle isocèle 60°, pratique FR / DTU 20.1)")
log("  W_k = ½ · L · h_Δ · t · γ   si h_Δ ≤ H_mur = 3,50 m  (triangle formé)")
log("  Plancher : p_ELU = 1,35×4,71 + 1,5×2,50 = 10,11 kN/m sur bande 1,00 m")
log("  M_Ed = W_ELU·L/6 + p_plan·L²/8   (triangle + uniforme, appuis simples)")
log("  Enveloppe B-45 : p_ELU = 71,4 kN/m sur L_calc = 1,25 m (mur pleine hauteur)")
log("")
log("  %-6s %-6s %-8s %-8s %-8s %-8s %-8s %-8s %s"
    % ("RÉF", "L m", "h_Δ m", "W_k kN", "M_Δ", "M_env", "taux_Δ", "taux_env", "VERDICT"))

f1_res = []
for nom, L in (("F1a", 1.00), ("F1b", 0.90), ("F1c", 0.85)):
    h, form, Wk = triangle(L)
    W_ELU = 1.35 * Wk
    p_plan = 1.35 * G_PLAN * BANDE + 1.5 * Q_PLAN * BANDE
    M_tri = W_ELU * L / 6.0 + p_plan * L ** 2 / 8.0
    V_tri = W_ELU / 2.0 + p_plan * L / 2.0
    M_env = P_ELU_ENV * L_CALC_F1 ** 2 / 8.0
    V_env = P_ELU_ENV * L_CALC_F1 / 2.0
    t_tri = M_tri / M_RD_F1
    t_env = M_env / M_RD_F1
    f1_res.append({
        "ref": nom, "L": L, "h_tri": round(h, 3), "forme": form,
        "Wk": round(Wk, 2), "M_tri": round(M_tri, 2), "V_tri": round(V_tri, 2),
        "M_env": round(M_env, 2), "taux_tri": round(t_tri, 4),
        "taux_env": round(t_env, 3),
    })
    log("  %-6s %-6.2f %-8.3f %-8.2f %-8.2f %-8.1f %-8.4f %-8.3f %s"
        % (nom, L, h, Wk, M_tri, M_env, t_tri, t_env, "OK"))

log("")
log("  M_Rd (2×HEA 200) = %.1f kN·m · V_Rd = %.1f kN" % (M_RD_F1, V_RD_F1))
log("  Triangle FORMÉ pour les 3 (h_Δ ≤ 3,50 m) : la maçonnerie au-dessus du")
log("  triangle va aux jambages, pas au linteau. B-21 mettait 38,5 kN/m de mur")
log("  (pleine hauteur) : c'est l'enveloppe conservatrice déjà vérifiée en B-45")
log("  (taux 0,059). B-49 n'y touche pas : il ajoute la méthode du triangle,")
log("  qui est la bonne pour un linteau court, et confirme que F1 n'est pas le sujet.")
log("  Appui : sommier S2 20×50×20, w_b = 200 mm ≥ 90 mm (EC6 §8.1.6) — B-46 Z2 OK.")

# ============================================================== R3
titre("[3] R3-N / R3-S — LINTEAUX SOUS CHARGE PONCTUELLE (B-45 §9, D-36)")
M_R3 = P_R3 * L_BAIE / 4.0
V_R3 = P_R3 / 2.0
w_R3 = P_R3 * 1e3 * (L_BAIE * 1000.0) ** 3 / (48.0 * E * IY_UPE * 1e4)
log("  P_Ed = %.1f kN à mi-portée (réaction R2-N, B-21 §5)" % P_R3)
log("  L_baie = %.2f m · profilé livré %.2f m" % (L_BAIE, L_PROF_R3))
log("  M_Ed = P·L/4 = %.2f kN·m  /  M_Rd = %.1f kN·m  →  taux %.3f"
    % (M_R3, M_RD_R3, M_R3 / M_RD_R3))
log("  V_Ed = P/2 = %.1f kN  →  taux cisaillement (B-45) 0,051" % V_R3)
log("  Flèche = %.1f mm  /  L/250 = %.1f mm  →  %.3f"
    % (w_R3, L_BAIE * 1000.0 / 250.0, w_R3 / (L_BAIE * 1000.0 / 250.0)))
log("  Torsion : D-36 — remplissage C25/30 entre ailes → section FERMÉE,")
log("  I_T ~ 10^7 mm⁴, torsion hors critère (R-50-2 CLOSE, B-50 A3).")
log("  Appui : 2 × S1 20×40×20 par linteau, w_b = 200 ≥ 90 mm — B-46 Z2 OK")
log("  (R3 admissible même en a1 = 0 et β = 1). Coussin D-37 NON requis sur R3.")

# ============================================================== existant
titre("[4] E-08 ET LINTEAU OUEST — PAS DE CALCUL, PAS DE RELEVÉ DE BOIS")
log("  Façade Est, Désordre 1 (D3 p.5) : 2 linteaux bois déformés, NON PORTEURS.")
log("  B-20 §5 : R3-N/S + 4×S1 COURT-CIRCUITENT totalement ces linteaux.")
log("  Les sommiers S1 tombent sur les ABOUTS DE MUR, hors emprise des bois.")
log("  → R-46-4 CLOSE : aucun sommier n'est censé reposer sur un linteau bois.")
log("  Contrôle d'implantation = B-60 (cotation), pas un sondage de bois.")
log("")
log("  Façade Ouest Sud : linteau bois 23×15 (D3 p.16), L = 2,52 m entre P1-N/S.")
log("  D2 f.01 : P1 « en renfort du linteau bois existant » — le bois RESTE,")
log("  P1 le soulage. Aucune intervention sur le bois n'est prescrite (CCTP,")
log("  D2, D4). Pas de relevé, pas de réserve bois (règle du 20/10).")
log("  P1 est un POTEAU (B-45, B-42) — pas un linteau.")

titre("[5] SEUILS BA — SANS OBJET")
log("  D1 : aucun seuil BA au CCTP GO. D2 f.01-04 : aucun seuil coté.")
log("  D4 p.23-25 (GEO-05) : nomenclatures de baies, pas de seuil structurel.")
log("  Le dallage (B-43) est désolidarisé 20 mm — pas un seuil.")
log("  Verdict : SANS OBJET. Réactivable si un seuil porteur est prescrit.")

titre("[6] LONGUEURS D'APPUI ET CONTRAINTES (renvoi B-46, pas un nouveau calcul)")
log("  F1a/b/c : S2, N_Rdc (β=1) = 60 kN ≥ V_Ed enveloppe 44,6 kN — OK (B-46).")
log("  R3-N/S  : S1, N_Rdc (β=1) = 48 kN ≥ V_Ed 23,1 kN — OK (B-46).")
log("  Mini EC6 §8.1.6 = 90 mm : w_b = 200 mm — OK.")
log("  Coussin D-37 (w_b ≥ 300 mm) : R1, F2, F3 — CE NE SONT PAS DES LINTEAUX.")
log("  Aucun scellement calculé ici (B-50).")

titre("[7] AUTO-CONTRÔLE DÉCLARÉ — LINTEAU PAR LINTEAU")
AC = [
    ("F1a", "triangle 60° + enveloppe B-45", "OK 0,010 / 0,059", "S2, B-46 OK"),
    ("F1b", "idem, L=0,90 m", "OK", "S2, B-46 OK"),
    ("F1c", "idem, L=0,85 m", "OK", "S2, B-46 OK"),
    ("R3-N", "ponctuel 46,2 kN + D-36", "OK 0,291 flexion", "S1, B-46 OK, torsion close"),
    ("R3-S", "idem R3-N", "OK", "S1, B-46 OK"),
    ("E-08", "court-circuité par R3", "HORS CALCUL", "R-46-4 close"),
    ("Seuils", "0 prescription", "SANS OBJET", "—"),
]
for z, c, v, p in AC:
    log("  %-8s %-36s %-22s %s" % (z, c, v, p))
log("")
log("  Points DE PRINCIPE : triangle appliqué aux linteaux courts ; enveloppe")
log("  B-45 non réduite ; aucun bois calculé ; aucun scellement ; pas de feu.")
log("  Points À LEVER : aucun sur les 5 linteaux neufs. Implantation S1 hors")
log("  bois = B-60 (cotation), pas une réserve de calcul.")

res = {
    "mode": "PARTIEL-DÉCLARÉ",
    "type": "linteau métallique",
    "seuils": "SANS OBJET",
    "f1": f1_res,
    "r3": {"P": P_R3, "M": round(M_R3, 2), "taux": round(M_R3 / M_RD_R3, 3),
           "w_mm": round(w_R3, 2)},
    "e08": "court-circuité",
    "ecarts": 0,
}

# ============================================================== PLANCHE
import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

doc = ezdxf.new("R2018", setup=True)
msp = doc.modelspace()
for nom, coul in (("LINTEAU-AXES", 1), ("LINTEAU-COFFRAGE", 5), ("LINTEAU-ACIER", 3),
                  ("LINTEAU-HABILLAGE-TEXTE", 7), ("LINTEAU-CARTOUCHE", 7)):
    doc.layers.add(nom, color=coul)


def txt(x, y, t, ht=2.4, layer="LINTEAU-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))


def rect(x0, y0, x1, y1, layer="LINTEAU-COFFRAGE"):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})


def ligne(x0, y0, x1, y1, layer="LINTEAU-COFFRAGE"):
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})


rect(8, 8, 412, 289, "LINTEAU-CARTOUCHE")
txt(14, 279, "CROISSY-FLORA — B-49 — LINTEAUX MÉTALLIQUES", 3.8, "LINTEAU-AXES")
txt(14, 272.5, "Indice A — 21/10/2026 — Mode PARTIEL-DÉCLARÉ — 5 linteaux neufs, seuils SANS OBJET", 2.4, "LINTEAU-AXES")
txt(14, 267, "Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée.", 2.3)

# --- D1 triangle F1
txt(14, 257, "1. F1a/b/c — LINTEAU COURT : TRIANGLE 60° (EC3 + DTU 20.1)", 2.5, "LINTEAU-AXES")
x0, y0 = 26, 208
rect(x0, y0, x0 + 40, y0 + 6, "LINTEAU-ACIER")          # linteau
ligne(x0, y0 + 6, x0 + 20, y0 + 40, "LINTEAU-AXES")     # triangle
ligne(x0 + 40, y0 + 6, x0 + 20, y0 + 40, "LINTEAU-AXES")
ligne(x0, y0 + 6, x0 + 40, y0 + 6, "LINTEAU-AXES")
rect(x0 - 8, y0 + 6, x0, y0 + 44, "LINTEAU-COFFRAGE")   # jambage
rect(x0 + 40, y0 + 6, x0 + 48, y0 + 44, "LINTEAU-COFFRAGE")
txt(x0 + 50, y0 + 36, "2 × HEA 200 — L_libre 0,85 à 1,00 m", 2.0, "LINTEAU-AXES")
txt(x0 + 50, y0 + 31, "h_Δ = 0,74 à 0,87 m  <<  H_mur 3,50 m", 2.0)
txt(x0 + 50, y0 + 26, "W_k = 3,4 à 4,8 kN (mur) + plancher 10,1 kN/m", 2.0)
txt(x0 + 50, y0 + 21, "M_Δ ≤ 2,3 kN·m  /  M_Rd 236 kN·m  →  0,010", 2.0, "LINTEAU-AXES")
txt(x0 + 50, y0 + 16, "Enveloppe B-45 (mur plein) : taux 0,059 — OK", 2.0, "LINTEAU-AXES")
txt(x0 + 50, y0 + 11, "Sommier S2 20×50×20 — w_b 200 ≥ 90 mm", 2.0)
txt(x0 + 50, y0 + 6, "Section CONTRACTUELLE (D2 f.01) — ne pas réduire", 2.0)

# --- D2 R3
txt(14, 196, "2. R3-N/S — UPE 200 REMPLI (D-36) SOUS CHARGE PONCTUELLE R2", 2.5, "LINTEAU-AXES")
xc, yc = 26, 152
ligne(xc, yc, xc + 50, yc, "LINTEAU-ACIER")
ligne(xc, yc + 8, xc + 50, yc + 8, "LINTEAU-ACIER")
ligne(xc, yc, xc, yc + 8, "LINTEAU-ACIER")
ligne(xc + 50, yc, xc + 50, yc + 8, "LINTEAU-ACIER")
for k in range(1, 8):
    ligne(xc + k * 6.2, yc + 1, xc + k * 6.2, yc + 7, "LINTEAU-COFFRAGE")
ligne(xc + 25, yc + 8, xc + 25, yc + 28, "LINTEAU-AXES")
txt(xc + 27, yc + 22, "R2  46,2 kN", 2.0, "LINTEAU-AXES")
rect(xc - 6, yc - 4, xc + 4, yc, "LINTEAU-COFFRAGE")
rect(xc + 46, yc - 4, xc + 56, yc, "LINTEAU-COFFRAGE")
txt(xc + 58, yc + 18, "M_Ed = 17,9 kN·m  /  61,6  →  0,291", 2.0, "LINTEAU-AXES")
txt(xc + 58, yc + 13, "Remplissage C25/30 — torsion CLOSE (D-36)", 2.0, "LINTEAU-AXES")
txt(xc + 58, yc + 8, "2 × S1 20×40×20 — abouts de mur, hors bois", 2.0)
txt(xc + 58, yc + 3, "Ancien linteau bois : COURT-CIRCUITÉ", 2.0, "LINTEAU-AXES")
txt(xc, yc - 10, "UPE 200 + béton (hachures) — L_baie 1,55 m", 1.9)

# --- tableau
txt(14, 132, "3. LES 5 LINTEAUX NEUFS — CONTRÔLE", 2.5, "LINTEAU-AXES")
rect(14, 78, 250, 126, "LINTEAU-CARTOUCHE")
cols = (16, 40, 78, 118, 158, 200)
for c, t in zip(cols, ("RÉF", "SECTION", "L m", "M_Ed / M_Rd", "APPUI", "VERDICT")):
    txt(c, 120, t, 1.9, "LINTEAU-AXES")
lignes_t = [
    ("F1a", "2×HEA 200", "1,00", "0,010 / 0,059", "S2 200 mm", "OK"),
    ("F1b", "2×HEA 200", "0,90", "0,010 / 0,059", "S2 200 mm", "OK"),
    ("F1c", "2×HEA 200", "0,85", "0,010 / 0,059", "S2 200 mm", "OK"),
    ("R3-N", "UPE 200+B", "1,55", "0,291", "S1 200 mm", "OK + D-36"),
    ("R3-S", "UPE 200+B", "1,55", "0,291", "S1 200 mm", "OK + D-36"),
]
for k, l in enumerate(lignes_t):
    y = 113 - k * 6.5
    for c, v in zip(cols, l):
        txt(c, y, v, 1.85)

# --- existant / seuils
txt(255, 257, "4. EXISTANT ET SEUILS — HORS CALCUL", 2.5, "LINTEAU-AXES")
rect(255, 189, 405, 250, "LINTEAU-CARTOUCHE")
txt(258, 243, "E-08 (Désordre 1, façade Est)", 2.0, "LINTEAU-AXES")
txt(258, 238, "2 linteaux bois déformés, NON PORTEURS.", 1.95)
txt(258, 233.5, "R3 + 4×S1 les court-circuitent (B-20).", 1.95)
txt(258, 229, "S1 sur ABOUTS DE MUR, hors bois.", 1.95)
txt(258, 224.5, "→ R-46-4 CLOSE. Pas de relevé bois.", 2.0, "LINTEAU-AXES")
txt(258, 218, "Linteau Ouest 23×15 : soulagé par P1.", 1.95)
txt(258, 213.5, "Le bois RESTE. Aucune intervention bois", 1.95)
txt(258, 209, "prescrite (CCTP, D2, D4).", 1.95)
txt(258, 203, "Seuils BA : SANS OBJET.", 2.0, "LINTEAU-AXES")
txt(258, 198.5, "0 prescription D1 / D2 / D4 p.23-25.", 1.95)

# --- D-34 box
rect(255, 128, 405, 178, "LINTEAU-CARTOUCHE")
txt(258, 171, "CLAUSE D-34 — MAJUSCULES (OPPOSABLE)", 2.0, "LINTEAU-AXES")
clause = [
    "NOS ÉTUDES SONT RÉALISÉES AVEC f_k = 1,5 MPa.",
    "ESSAIS HORS MISSION, À CHARGE DU MOA.",
    "ESSAIS NON CONCLUANTS => REPRISE CHIFFRÉE.",
    "D-36 : UPE 200 DE R3 REMPLI C25/30.",
    "D-37 : COUSSIN w_b ≥ 300 mm SOUS R1, F2, F3",
    "(PAS DES LINTEAUX — B-46 / B-60).",
]
for k, t in enumerate(clause):
    txt(258, 165 - k * 5.2, t, 1.9, "LINTEAU-AXES")

# --- notes
n0 = 14
txt(n0, 70, "NOTES OPPOSABLES", 2.4, "LINTEAU-AXES")
notes = [
    "1. F1 : triangle 60° (méthode linteau court) + enveloppe B-45 0,059 — les deux OK.",
    "2. R3 : flexion 0,291 · torsion CLOSE par D-36 (remplissage C25/30).",
    "3. E-08 court-circuité — AUCUN calcul de bois, AUCUN relevé (non prescrit).",
    "4. Seuils BA : SANS OBJET. Coussin D-37 = R1/F2/F3, pas les linteaux.",
    "5. AUCUN JOINT DE DILATATION (D-28). D-09 : ARASE −1,00 M / TN MINI.",
    "6. Aucun scellement calculé (B-50). Protection incendie NON dimensionnée.",
]
for k, t in enumerate(notes):
    col, row = (0, k) if k < 3 else (1, k - 3)
    txt(n0 + col * 200, 64 - row * 5.0, t, 1.85)

rect(14, 10, 405, 42, "LINTEAU-CARTOUCHE")
txt(18, 34, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 3.2, "LINTEAU-AXES")
txt(18, 27, "B-49 — LINTEAUX ET SEUILS  ·  Indice A · 21/10/2026 · PARTIEL-DÉCLARÉ · DXF mm", 2.1)
txt(18, 21, "EC3 §6.2 · EC6 §8.1.6 · triangle 60° · CARNAC v3.0", 2.1)
txt(18, 13, "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 4.0, "LINTEAU-AXES")

chemin = BASE + ".dxf"
doc.saveas(chemin)
audit = doc.audit()
log("")
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

with open(os.path.join(OUT, "b49_linteaux.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b49_linteaux.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)

log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b49_linteaux.txt"),
                             os.path.getsize(os.path.join(OUT, "b49_linteaux.txt"))))
log("JSON    : %s (%d o)" % (os.path.join(OUT, "b49_linteaux.json"),
                             os.path.getsize(os.path.join(OUT, "b49_linteaux.json"))))
