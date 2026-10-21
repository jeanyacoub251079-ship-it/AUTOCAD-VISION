#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type FOND — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D (report, jamais redessin). Implantation B-40 Ind. F.
Attentes A1 (B-50) : 6 HA12, l_bd 166 mm, 3 conditions R-50-1.
ENC v3 (12 alinéas) intégrale. Titre PLS (D-11). Cotes en mm.
Aucun cloison, aucune isolation. D-19 maintenus. D-23 porté (non corrigé).
"""
import json
import os
from collections import Counter

import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_plans", "FLORA_RDC_VUE-NETTOYEE_IndD.dxf")
PLANS = os.path.join(ROOT, "_plans")
OUT = os.path.join(ROOT, "_rendus")
BASE = os.path.join(PLANS, "FLORA_B60_FOND_EXE_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


def add_cloud(msp, x0, y0, x1, y1, layer="FOND-HYP-D19", step=22.0):
    pts = []
    x, y = x0, y0
    while x < x1:
        pts.append((x, y0))
        x += step
    while y < y1:
        pts.append((x1, y))
        y += step
    while x > x0:
        pts.append((x, y1))
        x -= step
    while y > y0:
        pts.append((x0, y))
        y -= step
    pts.append((x0, y0))
    msp.add_lwpolyline(pts, dxfattribs={"layer": layer})


titre("=" * 78)
log("B-60 — PLANS D'EXÉCUTION — type FOND — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13) — PLS (D-11)")
log("Mode : PARTIEL-DÉCLARÉ (B-40 F · nuages D-19 · ENC v3)")
log("=" * 78)

titre("[0] ENTRÉES — ÉTAPE 1")
log("  Note amont     : B-40 Ind. F  — SF1 80×80×25, type 60×60×30, ENC v3")
log("  Vue nettoyée   : B-32 Ind. D  — %s (%d o)" % (SRC, os.path.getsize(SRC)))
log("  Calage         : B-30 (résidu médian 21,0 mm) — D-23 translation rigide R+1/RDC")
log("  Attentes       : B-50 A1 — 6 HA12, l_bd 166 ≤ 200 mm, 3 conditions R-50-1")
log("  Poteau         : B-42 B — P2 15×25, 6 HA12, N_Ed 159,0 kN")
log("  Cartouche      : modèle FLORA (annexe A) — unités mm sur cotes, DXF cm (B-32)")
log("  Cloisons/isol. : 0 — D-25 / V9")
log("  B-34 / B-33    : non livrées — STR-03 NON BLOQUANTE ; B-33 est aval (phase 6)")

titre("[1] HYPOTHÈSES ET CLAUSES OPPOSABLES")
log("  D-09 / D-12 : ARASE −1,00 m / TN MINIMUM — jamais une cote fixe, jamais de remontée.")
log("  D-11 : titre PLS = plan de fondations.")
log("  D-14 : semelle ≥ 60×60. D-30 : SF1 = 80×80×25.")
log("  D-06 : c_nom = 50 mm en fondation.")
log("  D-16 : hors nappe — venue d'eau = point d'arrêt.")
log("  D-15 : tassements hors mission GO.")
log("  D-19 : nuages Z-P1N, Z-P1S, Z-P3, Z-J1 MAINTEUS.")
log("  D-23 : écart R+1/RDC 10,1 cm porté comme DONNÉE, non corrigé.")
log("  D-26 : AUCUNE VÉRIFICATION SISMIQUE. D-28 : AUCUN JOINT DE DILATATION.")
log("  D-34 : f_k = 1,5 MPa — essais hors mission.")
log("  Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée.")

titre("[2] IMPLANTATION (report B-40, aucune position inventée)")
IMP = [
    ("SF1", "95,35", "59,29", "80×80×25 BA", "CERTAIN — D-30 / B-40 F"),
    ("Z-P1N", "95,41", "49,04", "vérif. moellons ou 60×60", "NUAGE D-19"),
    ("Z-P1S", "95,41", "47,78", "vérif. moellons ou 60×60", "NUAGE D-19"),
    ("Z-P3", "94,09", "54,89", "appui P3 50×40 + GB", "NUAGE D-19"),
    ("Z-J1", "89,78", "54,52", "appui J1 24×50 + GB", "NUAGE D-19"),
    ("BÊCHE", "86,67→89,53", "46,77", "ép. 20 cm, L=2,85 m", "EXI-07c"),
    ("RSO-PASS", "87,70→93,50", "63,3→64,3", "passes ≤ 1,00 m C16/20", "EXI-07e"),
]
log("  %-10s %14s %14s %-28s %s" % ("REPÈRE", "X m", "Y m", "OUVRAGE", "STATUT"))
for r in IMP:
    log("  %-10s %14s %14s %-28s %s" % r)

titre("[3] SF1 — FERRAILLAGE D'EXÉCUTION (B-40 + B-50 A1)")
log("  Semelle        : 800 × 800 × 250 mm  C25/30  (D-30)")
log("  c_nom          : 50 mm sur 4 faces (D-06) — NON AJUSTABLE")
log("  Lit inférieur  : HA8 e150  2 directions  (A_s = 335 mm²/m ≥ A_s,min 323)")
log("  Nb barres SF1  : 6 HA8 par direction (B-40 §2.3)")
log("  Cadres         : HA8 e150 jusqu'au lit inférieur (R-50-1 condition 3)")
log("  Attentes P2    : 6 HA12, équerre en pied, l_bd = 166 mm ≤ 200 mm (B-50 A1)")
log("  Si équerre ôtée: l_bd = 237 mm > 200 mm — NON CONFORME (R-50-1)")
log("  Gros béton     : C16/20 SOUS la semelle si existant plus profond (D-09)")
log("  Propreté       : 50 mm")
log("  N_ELS / N_ELU  : 130,5 / 182,9 kN  σ = 0,204 / 0,286 MPa")
log("  Poinçonnement  : v_Ed 0,279 ≤ v_Rd,c 0,392 MPa (0,71)")

titre("[4] NOMENCLATURE GRAPHIQUE (détail B-62)")
NOM = [
    ("SF1", "Semelle isolée BA", "800×800×250", "1", "C25/30"),
    ("SF-T", "Semelle type (si fouille)", "600×600×300 mini", "selon D-19", "C25/30"),
    ("HA8", "Lit inf. croisé + cadres", "HA8 e150", "6+6 / SF1", "S500B"),
    ("HA12", "Attentes P2 dans SF1", "HA12 équerre", "6", "S500B, l_bd 166"),
    ("GB", "Gros béton rattrapage", "C16/20", "selon fouille", "sous semelle"),
    ("BP", "Béton de propreté", "50 mm", "sous SF1", "—"),
    ("BÊCHE", "Réhausse dallage SE", "200 mm × 2,85 m", "1", "C25/30"),
    ("RSO", "Passerelle château", "passes ≤ 1000 mm", "1 zone", "C16/20"),
]
log("  %-8s %-28s %-18s %-14s %s" % ("RÉP", "DÉSIGNATION", "SECTION", "QTÉ", "MATÉRIAU"))
for n in NOM:
    log("  %-8s %-28s %-18s %-14s %s" % n)

# ============================================================== DXF
doc = ezdxf.readfile(SRC)
for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9
LAYERS = (
    ("FOND-AXES", 1), ("FOND-COFFRAGE", 5), ("FOND-ACIER-INF", 3),
    ("FOND-ACIER-SUP", 4), ("FOND-COTATION", 8), ("FOND-HYP-D19", 6),
    ("FOND-GROS-BETON", 30), ("FOND-DETAILS", 4), ("FOND-NOMENCLATURE", 7),
    ("FOND-HABILLAGE-TEXTE", 7), ("FOND-CARTOUCHE", 7),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="FOND-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="FOND-COFFRAGE", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.5, layer="FOND-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + len(t) * ht * 0.62, ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


def cote_h(x1, x2, y, texte, layer="FOND-COTATION"):
    msp.add_line((x1, y), (x2, y), dxfattribs={"layer": layer})
    for x in (x1, x2):
        msp.add_line((x, y - 8), (x, y + 8), dxfattribs={"layer": layer})
    txt((x1 + x2) / 2.0 - len(texte) * 3.5, y + 6, texte, 11.0, layer)


def cote_v(y1, y2, x, texte, layer="FOND-COTATION"):
    msp.add_line((x, y1), (x, y2), dxfattribs={"layer": layer})
    for y in (y1, y2):
        msp.add_line((x - 8, y), (x + 8, y), dxfattribs={"layer": layer})
    txt(x + 10, (y1 + y2) / 2.0 - 5, texte, 11.0, layer)


# --- GAUCHE : implantation sur B-32 ---
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "FOND-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "FOND-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "FOND-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "FOND-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "FOND-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "FOND-AXES")

p2x, p2y = 9535.0, 5929.2
rect(p2x - 45.0, p2y - 45.0, p2x + 45.0, p2y + 45.0, "FOND-GROS-BETON")
rect(p2x - 40.0, p2y - 40.0, p2x + 40.0, p2y + 40.0, "FOND-COFFRAGE", hatch_col=5)
rect(9522.5, 5921.7, 9547.6, 5936.7, "FOND-ACIER-INF", hatch_col=3)
leader(9645.0, 5955.0, p2x + 40.0, p2y + 8.0, "SF1 : 800x800x250 mm BA (D-30, sous P2)", 13.0, "FOND-COFFRAGE")
txt(9645.0, 5932.0, "X=95,35 / Y=59,29 m | HA8 e150 + 6 HA12 A1 | GB D-09 | N_ELS 130,5 kN", 11.0)

for xc, yc, lx, ly_t, lab in [
    (9540.5, 4904.4, 9645.0, 4925.0, "Z-P1N (D-19) : verif. moellons ou SF 600x600"),
    (9540.5, 4778.4, 9645.0, 4785.0, "Z-P1S (D-19) : verif. moellons ou SF 600x600"),
    (9408.6, 5489.1, 9645.0, 5555.0, "Z-P3 (D-19) : pied P3 50x40 + GB D-09"),
    (8977.5, 5452.1, 7960.0, 5555.0, "Z-J1 (D-19) : pied J1 24x50 + GB D-09"),
]:
    rect(xc - 30.0, yc - 30.0, xc + 30.0, yc + 30.0, "FOND-HYP-D19")
    add_cloud(msp, xc - 42.0, yc - 42.0, xc + 42.0, yc + 42.0, "FOND-HYP-D19", 22.0)
    leader(lx, ly_t, xc + (32.0 if lx > xc else -32.0), yc, lab, 12.2, "FOND-HYP-D19")

rect(8667.4, 4666.6, 8952.5, 4686.5, "FOND-COFFRAGE", hatch_col=5)
leader(7960.0, 4685.0, 8667.4, 4676.5, "Beche BA ep.200 mm (L=2850 mm — EXI-07c)", 12.2, "FOND-COFFRAGE")
add_cloud(msp, 8750.0, 6320.0, 9380.0, 6450.0, "FOND-GROS-BETON", 28.0)
txt(8775.0, 6392.0, "RSO Passerelle : passes alternees <= 1000 mm gros beton C16/20 (EXI-07e)", 11.8, "FOND-GROS-BETON")

# --- DROITE : détails EXE ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "FOND-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "FOND-AXES")
txt(rx0 + 20.0, 6462.0,
    "PLS (D-11) — B-60 Ind. A  |  FOND EXE  |  NE PAS EXECUTER SANS EXE COTE ET VISA  (PARTIEL-DECLARE)",
    15.5, "FOND-AXES")

K = 2.5
txt(rx0 + 25.0, 6365.0,
    "1. SEMELLES TYPES — PLAN FERRAILLE (HA8 e150, 2 lits croises, c_nom = 50 mm) — cotes en mm",
    13.5)
for Bm, cx_s, titre_s, amax_s in [
    (0.60, rx0 + 240.0, "TYPE 600x600", "D-14 minimum — A <= 14 m2"),
    (0.70, rx0 + 780.0, "TYPE 700x700", "A <= 19 m2"),
    (0.80, rx0 + 1360.0, "SF1 800x800 (D-30)", "sous P2 — N_ELS = 130,5 kN"),
]:
    cy_s = 6135.0
    c = Bm * 100.0 * K / 2.0
    p = 0.125 * 100.0 * K
    rect(cx_s - c - 5 * K, cy_s - c - 5 * K, cx_s + c + 5 * K, cy_s + c + 5 * K, "FOND-GROS-BETON")
    rect(cx_s - c, cy_s - c, cx_s + c, cy_s + c, "FOND-COFFRAGE")
    rect(cx_s - p, cy_s - p * 0.6, cx_s + p, cy_s + p * 0.6, "FOND-COFFRAGE")
    mg = 5.0 * K
    nbar = 6 if Bm >= 0.80 else (5 if Bm >= 0.70 else 4)
    for j in range(nbar):
        yj = cy_s - c + mg + j * (2 * (c - mg) / (nbar - 1))
        xj = cx_s - c + mg + j * (2 * (c - mg) / (nbar - 1))
        msp.add_line((cx_s - c + mg, yj), (cx_s + c - mg, yj), dxfattribs={"layer": "FOND-ACIER-INF"})
        msp.add_line((xj, cy_s - c + mg), (xj, cy_s + c - mg), dxfattribs={"layer": "FOND-ACIER-INF"})
    msp.add_line((cx_s - c - 30, cy_s), (cx_s + c + 30, cy_s), dxfattribs={"layer": "FOND-AXES"})
    msp.add_line((cx_s, cy_s - c - 30), (cx_s, cy_s + c + 30), dxfattribs={"layer": "FOND-AXES"})
    cote_h(cx_s - c, cx_s + c, cy_s - c - 28, "%d mm" % round(Bm * 1000))
    cote_v(cy_s - c, cy_s + c, cx_s + c + 24, "%d" % round(Bm * 1000))
    txt(cx_s - c, cy_s + c + 60, titre_s, 13.0, "FOND-COFFRAGE")
    txt(cx_s - c, cy_s + c + 38, amax_s, 10.8)

# Coupe A-A EXE avec A1
txt(rx0 + 25.0, 5855.0,
    "2. COUPE A-A — SF1 800x800x250 + ATTENTES 6 HA12 (B-50 A1) + GROS BETON D-09  — ech. 1/20",
    13.5, "FOND-DETAILS")
ccx, ccy = rx0 + 380.0, 5545.0
cw, ch = 80.0 * K, 25.0 * K
rect(ccx - cw / 2 - 20, ccy - 75.0, ccx + cw / 2 + 20, ccy - 12.5, "FOND-GROS-BETON")
rect(ccx - cw / 2 - 12.5, ccy - 12.5, ccx + cw / 2 + 12.5, ccy, "FOND-COFFRAGE")
rect(ccx - cw / 2, ccy, ccx + cw / 2, ccy + ch, "FOND-COFFRAGE")
pw = 25.0 * K / 2.0
msp.add_lwpolyline([(ccx - pw, ccy + ch), (ccx - pw, ccy + ch + 140),
                    (ccx + pw, ccy + ch + 140), (ccx + pw, ccy + ch)],
                   dxfattribs={"layer": "FOND-COFFRAGE"})
msp.add_line((ccx - cw / 2 + 12.5, ccy + 13.5), (ccx + cw / 2 - 12.5, ccy + 13.5),
             dxfattribs={"layer": "FOND-ACIER-INF"})
for j in range(6):
    xj = ccx - cw / 2 + 16 + j * (cw - 32) / 5.0
    msp.add_circle((xj, ccy + 18.0), 3.5, dxfattribs={"layer": "FOND-ACIER-INF"})
# attentes HA12 avec équerre (hook)
for s in (-1, 1):
    xh = ccx + s * (pw - 10)
    msp.add_line((xh, ccy + 18), (xh, ccy + ch + 95), dxfattribs={"layer": "FOND-ACIER-SUP"})
    msp.add_line((xh, ccy + 18), (xh - s * 16, ccy + 18), dxfattribs={"layer": "FOND-ACIER-SUP"})  # équerre
# cadres jusqu'au lit
for k in range(3):
    yk = ccy + 18 + k * 18
    msp.add_lwpolyline([(ccx - pw + 4, yk), (ccx + pw - 4, yk),
                        (ccx + pw - 4, yk + 8), (ccx - pw + 4, yk + 8), (ccx - pw + 4, yk)],
                       dxfattribs={"layer": "FOND-ACIER-SUP"})

cote_h(ccx - cw / 2, ccx + cw / 2, ccy - 98.0, "800 mm (D-30)")
cote_v(ccy, ccy + ch, ccx + cw / 2 + 28.0, "h=250 mm")
txt(ccx + cw / 2 + 140.0, ccy + ch + 95.0, "0,000 RELATIF (PB RDC — D-21) / TN", 12.0, "FOND-AXES")
txt(ccx + cw / 2 + 140.0, ccy + ch + 55.0, "6 HA12 EQUERRE — l_bd 166 mm <= 200 mm (B-50 A1)", 11.5, "FOND-ACIER-SUP")
txt(ccx + cw / 2 + 140.0, ccy + ch + 32.0, "R-50-1 : equerre + c_nom 50 mm 4 faces + cadres HA8 e150 au lit", 11.2, "FOND-ACIER-SUP")
txt(ccx + cw / 2 + 140.0, ccy + 22.0, "2 lits HA8 e150 (335 mm2/m) — c_nom = 50 mm — S500B", 11.5, "FOND-ACIER-INF")
txt(ccx + cw / 2 + 140.0, ccy - 8.0, "Arase inf. -1,00 m / TN MINIMUM (D-08/D-12) + proprete 50 mm", 11.5, "FOND-COFFRAGE")
txt(ccx + cw / 2 + 140.0, ccy - 50.0, "GROS BETON C16/20 SOUS semelle si existant plus profond (D-09)", 11.5, "FOND-GROS-BETON")
txt(ccx + cw / 2 + 140.0, ccy - 72.0, "JAMAIS de remontee. Approfondissement seulement (D-12).", 11.5, "FOND-GROS-BETON")

# ENC + nomenclature
rect(rx0 + 18.0, 4760.0, rx1 - 18.0, 5360.0, "FOND-AXES")
enc = [
    "ENC v3 — PRESCRIPTION FONDATIONS — A REPORTER INTEGRALEMENT (D-09 / D-11) :",
    "1. Arase inf. -1,00 m / TN MINIMUM — jamais cote fixe, jamais remontee (D-12).",
    "2. Encastrement 0,50 m dans alluvions. 3. Semelles >= 600x600 mm. q_ELS<=0,30 q_ELU<=0,49 MPa.",
    "4-7. Verifier niveau existant en fouille. Si plus profond : GB C16/20 SOUS semelle. Jamais remonter.",
    "8. Hors nappe (D-16) : venue d'eau = POINT D'ARRET. 9. Tassements HORS MISSION (D-15).",
    "10. Reception contradictoire fond de fouille avant coulage. 11. C25/30 · C16/20 · S500B · c_nom 50 mm.",
    "12. Un plan portant la seule cote -1,00 m est INCOMPLET par omission.",
    "D-23 : ecart R+1/RDC 10,1 cm (enveloppe) / 22 cm (median) = DONNEE, non corrige.",
    "R-50-1 : sans equerre, l_bd=237>200 — A1 NON CONFORME. Les 3 conditions sont OPPOSABLES.",
]
for k, line in enumerate(enc):
    txt(rx0 + 32.0, 5328.0 - k * 58.0, line, 11.0,
        "FOND-AXES" if k == 0 else "FOND-HABILLAGE-TEXTE")

# nomenclature graphique
txt(rx0 + 25.0, 4705.0, "3. NOMENCLATURE GRAPHIQUE (faconnage -> B-62)", 13.0, "FOND-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 4695.0, "FOND-NOMENCLATURE")
nom_l = [
    "SF1  800x800x250 C25/30  ×1   |  HA8 e150  6+6  S500B  |  6 HA12 equerre  l_bd 166 mm",
    "TYPE 600x600x300 mini (D-14) si fouille D-19  |  GB C16/20 sous semelle  |  proprete 50 mm",
    "BECHE 200 mm × 2850 mm C25/30  |  RSO passerelle passes <= 1000 mm C16/20",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 32.0, 4665.0 - k * 48.0, line, 11.5, "FOND-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "FOND-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "FOND-AXES")
txt(rx0 + 25.0, 4412.0, "PLS (D-11) — B-60 FOND EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "FOND-AXES")
txt(rx0 + 25.0, 4352.0, "Protection au feu : ADEQUATE A PREVOIR (hors lot GO)  ·  CARNAC v3.0  ·  cotes mm  ·  DXF cm", 11.0)

chemin = BASE + ".dxf"
doc.saveas(chemin)
audit = doc.audit()
log("")
log("  écrit : %s (%d o) — audit %d erreur(s)" % (chemin, os.path.getsize(chemin), len(audit.errors)))

# V13 — relecture réelle
doc2 = ezdxf.readfile(chemin)
cnt = Counter()
for e in doc2.modelspace():
    cnt[e.dxf.layer] += 1
titre("[5] TEST DE RELECTURE DXF (V13 / annexe O §6)")
log("  calque                          n")
for lay, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
    if lay.startswith("FOND-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
n0 = cnt.get("0", 0)
nfond = sum(n for l, n in cnt.items() if l.startswith("FOND-"))
log("  FOND-* total = %d  ·  calque 0 (fond B-32 inclus) = %d" % (nfond, n0))
log("  Les entités FOND-* ne sont PAS sur 0. Fond B-32 conserve ses calques source.")
attendus = [l for l, _ in LAYERS]
manquants = [l for l in attendus if l not in doc2.layers]
log("  calques FOND attendus : %d  · manquants : %s" % (len(attendus), manquants or "aucun"))

fig = plt.figure(figsize=(16.54, 11.69))
ax = fig.add_axes([0.015, 0.02, 0.97, 0.90])
cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
Frontend(RenderContext(doc2), MatplotlibBackend(ax), config=cfg).draw_layout(
    doc2.modelspace(), finalize=False)
ax.set_xlim(7940.0, 12060.0)
ax.set_ylim(4290.0, 6560.0)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
ax.set_title(
    "CROISSY-FLORA — PLS (D-11) / B-60 Ind. A — FONDATIONS EXE COTÉES\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D : cloisons et isolation supprimées)",
    fontsize=11.5, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "FOND", "indice": "A", "mode": "PARTIEL-DECLARE",
    "SF1_mm": [800, 800, 250], "c_nom_mm": 50,
    "A1_HA12": 6, "l_bd_mm": 166, "R50_1": True,
    "audit": len(audit.errors), "n_FOND": nfond,
    "calques_manquants": manquants,
    "D19": ["Z-P1N", "Z-P1S", "Z-P3", "Z-J1"],
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_fond.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_fond.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b60_fond.txt"),
                             os.path.getsize(os.path.join(OUT, "b60_fond.txt"))))
