#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type VERT — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D (report, jamais redessin). Porteurs B-42 Ind. B.
P2 150×250 / P3 400×500 / J1 240×500 — 6 HA12 partout.
c_nom 30 mm (H-23, hors fondation). H = 2800 mm HYPOTHÈSE (R-42-1 ouverte).
D-19 maintenus sur P3 et J1. D-34 mot pour mot. Aucune fusion de type.
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
BASE = os.path.join(PLANS, "FLORA_B60_VERT_EXE_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


def add_cloud(msp, x0, y0, x1, y1, layer="VERT-HYP-D19", step=22.0):
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
log("B-60 — PLANS D'EXÉCUTION — type VERT — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-42 B · nuages D-19 · H hypothèse B-20 · D-34)")
log("=" * 78)

titre("[0] ENTRÉES — ÉTAPE 1")
log("  Note amont     : B-42 Ind. B — P2 / P3 / J1, 6 HA12, 8/8 CONFORME")
log("  Vue nettoyée   : B-32 Ind. D  — %s (%d o)" % (SRC, os.path.getsize(SRC)))
log("  Calage         : B-30 (résidu médian 21,0 mm)")
log("  Ancrage pied   : B-50 A1 / B-60 FOND — 6 HA12 équerre, l_bd 166 mm (P2/SF1)")
log("  Cartouche      : modèle FLORA — cotes mm, DXF cm (B-32)")
log("  Cloisons/isol. : 0 — D-25 / V9")
log("  Hors type      : R1/R2/R3 (METAL/MACON) · F2/F3 (METAL) · P1-N/S (METAL)")
log("  B-34 / B-33    : non livrées — STR-03 NON BLOQUANTE")

titre("[1] HYPOTHÈSES ET CLAUSES OPPOSABLES")
log("  H-23 / D-06 : c_nom = 30 mm hors fondation (XA1). 50 mm = FOND seulement.")
log("  H = 2 800 mm = BORNE HAUTE B-20 — HYPOTHÈSE, pas un relevé (R-42-1 OUVERTE).")
log("  D-19 : nuages Z-P3 et Z-J1 MAINTEUS (pieds sur maçonnerie).")
log("  D-26 : AUCUNE VÉRIFICATION SISMIQUE.")
log("  D-34 : f_k = 1,5 MPa, f_vk0 = 0,15 MPa ; essais hors mission ;")
log("         reprise chiffrée si non concluants — SUR LE PLAN ET LA NOTE.")
log("  D-28 : AUCUN JOINT DE DILATATION.")
log("  Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée.")
log("  R-42-2 : excentricité F2/P2 → B-50 (appareil d'appui) — non tranchée ici.")
log("  R-42-3 : pression J1 0,332 MPa → B-46 + D-34 — non tranchée ici.")

titre("[2] IMPLANTATION (report B-40 / B-42, aucune position inventée)")
IMP = [
    ("P2", "95,35", "59,29", "150×250 mm BA", "CERTAIN — sur SF1 / B-60 FOND"),
    ("P3", "94,09", "54,89", "400×500 mm BA", "NUAGE D-19 — pied maçonnerie"),
    ("J1", "89,78", "54,52", "240×500 mm BA", "NUAGE D-19 — pied maçonnerie"),
]
log("  %-8s %10s %10s %-18s %s" % ("RÉP", "X m", "Y m", "SECTION", "STATUT"))
for r in IMP:
    log("  %-8s %10s %10s %-18s %s" % r)

titre("[3] FERRAILLAGE D'EXÉCUTION (B-42 B — rien recalculé)")
log("  P2  150×250  N_Ed 159,0 kN  M_Ed/M_Rd 0,305  6 HA12  cadres HA8 e150")
log("  P3  400×500  N_Ed  35,8 kN  M_Ed/M_Rd 0,013  6 HA12  cadres HA8 e200")
log("  J1  240×500  N_Ed  39,8 kN  M_Ed/M_Rd 0,015  6 HA12  cadres HA8 e200")
log("  c_nom 30 mm  C25/30  S500B")
log("  6 HA12 imposé par l'espacement max, pas par la résistance.")
log("  P2 : 3 barres / face 250 mm (2 barres → 166 > 150 mm — interdit).")
log("  Ancrage pied P2 : B-60 FOND / B-50 A1 (équerre, l_bd 166 mm).")
log("  H = 2800 mm HYPOTHÈSE — débits indicatifs seulement (B-62).")

titre("[4] NOMENCLATURE GRAPHIQUE (façonnage → B-62)")
NOM = [
    ("P2", "Poteau BA sous F2", "150×250", "1", "C25/30 · 6 HA12 · HA8 e150"),
    ("P3", "Poteau BA refend", "400×500", "1", "C25/30 · 6 HA12 · HA8 e200"),
    ("J1", "Jambage BA refend", "240×500", "1", "C25/30 · 6 HA12 · HA8 e200"),
    ("HA12", "Longitudinal", "HA12", "18", "S500B — 6 / fût"),
    ("HA8", "Cadres", "HA8", "P2 e150 · P3/J1 e200", "S500B"),
]
log("  %-8s %-22s %-10s %-22s %s" % ("RÉP", "DÉSIGNATION", "SECTION", "QTÉ", "MATÉRIAU"))
for n in NOM:
    log("  %-8s %-22s %-10s %-22s %s" % n)

doc = ezdxf.readfile(SRC)
for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9
LAYERS = (
    ("VERT-AXES", 1), ("VERT-COFFRAGE", 5), ("VERT-ACIER-LONG", 3),
    ("VERT-ACIER-TRANS", 4), ("VERT-COTATION", 8), ("VERT-HYP-D19", 6),
    ("VERT-DETAILS", 4), ("VERT-NOMENCLATURE", 7),
    ("VERT-HABILLAGE-TEXTE", 7), ("VERT-CARTOUCHE", 7),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="VERT-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="VERT-COFFRAGE", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.5, layer="VERT-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + len(t) * ht * 0.62, ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


def cote_h(x1, x2, y, texte, layer="VERT-COTATION"):
    msp.add_line((x1, y), (x2, y), dxfattribs={"layer": layer})
    for x in (x1, x2):
        msp.add_line((x, y - 8), (x, y + 8), dxfattribs={"layer": layer})
    txt((x1 + x2) / 2.0 - len(texte) * 3.5, y + 6, texte, 11.0, layer)


def cote_v(y1, y2, x, texte, layer="VERT-COTATION"):
    msp.add_line((x, y1), (x, y2), dxfattribs={"layer": layer})
    for y in (y1, y2):
        msp.add_line((x - 8, y), (x + 8, y), dxfattribs={"layer": layer})
    txt(x + 10, (y1 + y2) / 2.0 - 5, texte, 11.0, layer)


# --- GAUCHE : implantation sur B-32 ---
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "VERT-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "VERT-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "VERT-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "VERT-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "VERT-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "VERT-AXES")

# P2 150×250 — orientation B-60 FOND : 250 mm selon X, 150 mm selon Y
p2x, p2y = 9535.0, 5929.2
rect(p2x - 12.5, p2y - 7.5, p2x + 12.5, p2y + 7.5, "VERT-COFFRAGE", hatch_col=5)
leader(9645.0, 5988.0, p2x + 12.5, p2y + 4.0,
       "P2 : 150x250 mm BA  |  6 HA12 + HA8 e150  |  CERTAIN (sur SF1)", 13.0, "VERT-COFFRAGE")
txt(9645.0, 5962.0, "X=95,35 / Y=59,29 m  |  N_Ed 159,0 kN  |  c_nom 30 mm  |  ancrage A1 -> B-60 FOND", 11.0)

# P3 400×500
p3x, p3y = 9408.6, 5489.1
rect(p3x - 25.0, p3y - 20.0, p3x + 25.0, p3y + 20.0, "VERT-COFFRAGE", hatch_col=5)
add_cloud(msp, p3x - 42.0, p3y - 42.0, p3x + 42.0, p3y + 42.0, "VERT-HYP-D19", 22.0)
leader(9645.0, 5555.0, p3x + 25.0, p3y,
       "P3 : 400x500 mm BA  |  6 HA12 + HA8 e200  |  D-19 pied maconnerie", 12.5, "VERT-HYP-D19")
txt(9645.0, 5530.0, "X=94,09 / Y=54,89 m  |  N_Ed 35,8 kN  |  c_nom 30 mm", 11.0, "VERT-HYP-D19")

# J1 240×500 — 240 mm selon X (ep. refend axe D), 500 mm selon Y
j1x, j1y = 8977.5, 5452.1
rect(j1x - 12.0, j1y - 25.0, j1x + 12.0, j1y + 25.0, "VERT-COFFRAGE", hatch_col=5)
add_cloud(msp, j1x - 42.0, j1y - 42.0, j1x + 42.0, j1y + 42.0, "VERT-HYP-D19", 22.0)
leader(7960.0, 5555.0, j1x - 12.0, j1y,
       "J1 : 240x500 mm BA  |  6 HA12 + HA8 e200  |  D-19 pied maconnerie", 12.5, "VERT-HYP-D19")
txt(7960.0, 5528.0, "X=89,78 / Y=54,52 m  |  N_Ed 39,8 kN  |  D-34 f_k=1,5 MPa", 11.0, "VERT-HYP-D19")

txt(7960.0, 4688.0, "P1-N / P1-S = poteaux ACIER (B-45) — hors type VERT. R1/R2/R3/F2/F3 = METAL/MACON.", 11.5)
txt(7960.0, 4662.0, "Dallage, linteaux, charpente : B-60 types suivants. Un plan = un type.", 11.5)

# --- DROITE : détails EXE ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "VERT-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "VERT-AXES")
txt(rx0 + 20.0, 6462.0,
    "B-60 Ind. A  |  VERT EXE  |  P2 / P3 / J1  |  NE PAS EXECUTER SANS EXE COTE ET VISA  (PARTIEL-DECLARE)",
    14.5, "VERT-AXES")

K = 2.2
txt(rx0 + 25.0, 6378.0,
    "1. SECTIONS COFFRAGE + FERRAILLAGE  —  6 HA12 S500B  —  c_nom = 30 mm  —  cotes en mm",
    13.0)

# --- 3 sections ---
def section_ba(cx, cy, b_mm, h_mm, titre_s, cadres, n_long=6):
    """b = largeur (X), h = hauteur (Y) en mm. Échelle K (DXF cm)."""
    bw = (b_mm / 10.0) * K / 2.0
    hh = (h_mm / 10.0) * K / 2.0
    rect(cx - bw, cy - hh, cx + bw, cy + hh, "VERT-COFFRAGE")
    # cadre
    m = 3.0 * K
    msp.add_lwpolyline(
        [(cx - bw + m, cy - hh + m), (cx + bw - m, cy - hh + m),
         (cx + bw - m, cy + hh - m), (cx - bw + m, cy + hh - m),
         (cx - bw + m, cy - hh + m)],
        dxfattribs={"layer": "VERT-ACIER-TRANS"})
    # 6 HA12 : 3 sur chaque face longue
    if h_mm >= b_mm:
        # face longue = h (Y) → 3 barres à gauche, 3 à droite
        ys = [cy - hh + m + 4, cy, cy + hh - m - 4]
        for yb in ys:
            msp.add_circle((cx - bw + m + 4, yb), 3.2, dxfattribs={"layer": "VERT-ACIER-LONG"})
            msp.add_circle((cx + bw - m - 4, yb), 3.2, dxfattribs={"layer": "VERT-ACIER-LONG"})
    else:
        xs = [cx - bw + m + 4, cx, cx + bw - m - 4]
        for xb in xs:
            msp.add_circle((xb, cy - hh + m + 4), 3.2, dxfattribs={"layer": "VERT-ACIER-LONG"})
            msp.add_circle((xb, cy + hh - m - 4), 3.2, dxfattribs={"layer": "VERT-ACIER-LONG"})
    cote_h(cx - bw, cx + bw, cy - hh - 28, "%d mm" % b_mm)
    cote_v(cy - hh, cy + hh, cx + bw + 22, "%d" % h_mm)
    txt(cx - bw, cy + hh + 52, titre_s, 12.5, "VERT-COFFRAGE")
    txt(cx - bw, cy + hh + 32, "6 HA12 + %s  |  c_nom 30 mm" % cadres, 10.5)


section_ba(rx0 + 280.0, 6155.0, 250, 150, "P2  250 x 150", "HA8 e150")
section_ba(rx0 + 820.0, 6155.0, 500, 400, "P3  500 x 400", "HA8 e200")
section_ba(rx0 + 1420.0, 6155.0, 500, 240, "J1  500 x 240", "HA8 e200")

# --- Coupe P2 ---
txt(rx0 + 25.0, 5895.0,
    "2. COUPE P2 — fût 150x250 x H=2800 mm (HYPOTHESE B-20 / R-42-1)  —  ech. 1/20  —  cotes mm",
    13.0, "VERT-DETAILS")
ccx, ccy = rx0 + 280.0, 5200.0
pw, ph = 12.5 * K, 7.5 * K   # 250×150 mm at K, drawn as elevation of 150-face
Hdx = 280.0 * K / 4.0       # 2800 mm / 4 to fit (schematic 1/20-ish compressed)
# fût
rect(ccx - pw, ccy, ccx + pw, ccy + Hdx, "VERT-COFFRAGE")
# semelle ghost (renvoi FOND, pas redessin FOND)
rect(ccx - 40 * K / 2, ccy - 25 * K / 4, ccx + 40 * K / 2, ccy, "VERT-DETAILS")
# HA12
for s in (-1, 0, 1):
    xh = ccx + s * (pw - 6)
    msp.add_line((xh, ccy + 8), (xh, ccy + Hdx - 8), dxfattribs={"layer": "VERT-ACIER-LONG"})
# cadres
for k in range(5):
    yk = ccy + 12 + k * (Hdx - 24) / 4.0
    msp.add_lwpolyline(
        [(ccx - pw + 4, yk), (ccx + pw - 4, yk),
         (ccx + pw - 4, yk + 6), (ccx - pw + 4, yk + 6), (ccx - pw + 4, yk)],
        dxfattribs={"layer": "VERT-ACIER-TRANS"})
cote_v(ccy, ccy + Hdx, ccx + pw + 28, "H=2800 mm HYP.")
cote_h(ccx - pw, ccx + pw, ccy - 42, "150 mm")
txt(ccx + pw + 140.0, ccy + Hdx + 20.0, "0,000 RELATIF (PB RDC — D-21)", 12.0, "VERT-AXES")
txt(ccx + pw + 140.0, ccy + Hdx - 20.0, "6 HA12  |  cadres HA8 e150 jusqu'au lit", 11.5, "VERT-ACIER-LONG")
txt(ccx + pw + 140.0, ccy + Hdx - 48.0, "c_nom = 30 mm (H-23 XA1) — PAS 50 mm", 11.5)
txt(ccx + pw + 140.0, ccy + 40.0, "Ancrage pied : 6 HA12 EQUERRE l_bd 166 mm", 11.5, "VERT-ACIER-LONG")
txt(ccx + pw + 140.0, ccy + 14.0, "-> B-60 FOND / B-50 A1  (R-50-1 CLOSE)", 11.5)
txt(ccx + pw + 140.0, ccy - 18.0, "SF1 800x800x250 — voir B-60 FOND (pas ce plan)", 11.2, "VERT-DETAILS")
txt(ccx + pw + 140.0, ccy - 48.0, "H = 2800 mm = borne haute B-20. R-42-1 OUVERTE (releve).", 11.2)

# D-34
rect(rx0 + 18.0, 4765.0, rx1 - 18.0, 5088.0, "VERT-AXES")
d34 = [
    "D-34 — MAÇONNERIE (mot pour mot, plan ET note) :",
    "f_k = 1,5 MPa  ·  f_vk0 = 0,15 MPa. Essais hors mission.",
    "Si non concluants : reprise d'étude chiffrée. J1 : sigma_d = 0,332 MPa (0,55 à f_k=1,5 ; défaut si f_k < 0,83).",
    "Dé de répartition sous J1 : option B-46, pas une initiative de ce plan. R-42-3 OUVERTE.",
    "D-19 : pieds P3 et J1 = nuages (vérif. soubassement à l'ouverture des fouilles). P2 CERTAIN sur SF1.",
    "D-26 : AUCUNE vérification sismique.  D-28 : AUCUN joint de dilatation.",
    "R-42-1 : H non relevée.  R-42-2 : excentricité F2/P2 → B-50.  Feu : ADEQUATE A PREVOIR (hors lot GO).",
]
for k, line in enumerate(d34):
    txt(rx0 + 32.0, 5058.0 - k * 40.0, line, 11.0,
        "VERT-AXES" if k == 0 else "VERT-HABILLAGE-TEXTE")

txt(rx0 + 25.0, 4728.0, "3. NOMENCLATURE GRAPHIQUE (faconnage -> B-62)", 13.0, "VERT-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 4715.0, "VERT-NOMENCLATURE")
nom_l = [
    "P2  150x250 C25/30  x1  |  6 HA12 S500B  |  cadres HA8 e150  |  N_Ed 159,0 kN  |  CERTAIN",
    "P3  400x500 C25/30  x1  |  6 HA12 S500B  |  cadres HA8 e200  |  N_Ed  35,8 kN  |  D-19",
    "J1  240x500 C25/30  x1  |  6 HA12 S500B  |  cadres HA8 e200  |  N_Ed  39,8 kN  |  D-19 / D-34",
    "H = 2800 mm HYPOTHESE B-20 — debits indicatifs (B-62). P1-N/S, R1/R2/R3, F2/F3 : hors type.",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 32.0, 4688.0 - k * 42.0, line, 11.2, "VERT-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "VERT-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "VERT-AXES")
txt(rx0 + 25.0, 4412.0, "B-60 VERT EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D · amont B-42 B", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "VERT-AXES")
txt(rx0 + 25.0, 4352.0, "Protection au feu : ADEQUATE A PREVOIR (hors lot GO)  ·  CARNAC v3.0  ·  cotes mm  ·  DXF cm", 11.0)

chemin = BASE + ".dxf"
doc.saveas(chemin)
audit = doc.audit()
log("")
log("  écrit : %s (%d o) — audit %d erreur(s)" % (chemin, os.path.getsize(chemin), len(audit.errors)))

doc2 = ezdxf.readfile(chemin)
cnt = Counter()
for e in doc2.modelspace():
    cnt[e.dxf.layer] += 1
titre("[5] TEST DE RELECTURE DXF (V13 / annexe O §6)")
log("  calque                          n")
for lay, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
    if lay.startswith("VERT-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
n0 = cnt.get("0", 0)
nvert = sum(n for l, n in cnt.items() if l.startswith("VERT-"))
log("  VERT-* total = %d  ·  calque 0 (ajouts) = %d" % (nvert, n0))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  calques VERT attendus : %d  · manquants : %s" % (len(LAYERS), manquants or "aucun"))

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
    "CROISSY-FLORA — B-60 Ind. A — VERTICAUX BA EXE COTÉS (P2 / P3 / J1)\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D : cloisons et isolation supprimées)",
    fontsize=11.5, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "VERT", "indice": "A", "mode": "PARTIEL-DECLARE",
    "porteurs": ["P2", "P3", "J1"],
    "ferraillage": "6 HA12",
    "c_nom_mm": 30,
    "H_mm_hypothese": 2800,
    "R42_1": "OUVERTE",
    "D19": ["Z-P3", "Z-J1"],
    "audit": len(audit.errors),
    "n_VERT": nvert,
    "calques_manquants": manquants,
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_vert.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_vert.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b60_vert.txt"),
                             os.path.getsize(os.path.join(OUT, "b60_vert.txt"))))
