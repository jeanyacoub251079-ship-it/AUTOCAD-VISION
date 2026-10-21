#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type LINTEAU — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D (report, jamais redessin). Note B-49 Ind. A.
5 linteaux neufs : F1a/b/c (2×HEA 200) · R3-N/S (UPE 200 + D-36).
S1 de R3 sur ABOUTS DE MUR, hors bois (R-46-4). E-08 court-circuité.
Seuils BA SANS OBJET. D-37 (R1/F2/F3) = type MACON, pas ce plan.
Purge blocs non référencés (viewer JS).
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
BASE = os.path.join(PLANS, "FLORA_B60_LINTEAU_EXE_IndA")
LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


def purge_unused_blocks(doc):
    ref = set()

    def walk(layout):
        for e in layout:
            if e.dxftype() == "INSERT":
                n = e.dxf.name
                ref.add(n)
                if n in doc.blocks:
                    walk(doc.blocks.get(n))

    walk(doc.modelspace())
    keep = set(ref)
    for b in doc.blocks:
        n = b.name
        if n.startswith("*Model") or n.startswith("*Paper") or n.startswith("_"):
            keep.add(n)
    deleted = 0
    for n in list(b.name for b in doc.blocks):
        if n in keep:
            continue
        try:
            doc.blocks.delete_block(n, safe=False)
            deleted += 1
        except Exception:
            pass
    return deleted, len(list(doc.blocks))


titre("=" * 78)
log("B-60 — PLANS D'EXÉCUTION — type LINTEAU — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-49 A · D-34 · SEC-01 hors lot)")
log("=" * 78)

titre("[0] ENTRÉES")
log("  Note amont   : B-49 Ind. A — 5 linteaux neufs OK · seuils SO · E-08 hors calcul")
log("  Positions    : B-20 Ind. B — report, millimètre, aucune position inventée")
log("  Vue          : B-32 Ind. D")
log("  Hors type    : F2/F3/R1 (METAL/MACON, D-37) · P1 (METAL) · FOND/VERT/PLANCHER livrés")

titre("[1] CLAUSES")
log("  D-34 : f_k=1,5 MPa · f_vk0=0,15 MPa · essais hors mission — SUR LE PLAN ET LA NOTE.")
log("  D-36 : remplissage C25/30 des UPE 200 de R3 ACCEPTÉ — porté ici, détail METAL.")
log("  D-26 : AUCUNE VÉRIFICATION SISMIQUE. D-28 : AUCUN JOINT DE DILATATION.")
log("  D-37 : coussins R1/F2/F3 — PAS des linteaux → B-60 MACON.")
log("  E-08 : COURT-CIRCUITÉ. Aucun relevé de bois. S1 hors emprise bois.")
log("  Seuils BA : SANS OBJET.")
log("  Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO).")

titre("[2] IMPLANTATION (B-20, cm DXF)")
LINTEAUX = [
    ("F1a", 8977.4, 5320.2, 8977.4, 5464.1, 14.0, "2xHEA200", "1,00 m", "File D · S2+J1"),
    ("F1b", 9279.8, 5489.2, 9427.5, 5489.2, 14.0, "2xHEA200", "0,90 m", "File 4 · S2+P3"),
    ("F1c", 9407.5, 5214.0, 9532.5, 5214.0, 14.0, "2xHEA200", "0,85 m", "File 3 · 2xS2"),
    ("R3-N", 8570.5, 5584.2, 8570.5, 5834.1, 10.0, "UPE200+B", "1,55 m", "Est Nord · 2xS1"),
    ("R3-S", 8570.5, 5007.9, 8570.5, 5258.0, 10.0, "UPE200+B", "1,55 m", "Est Sud · 2xS1"),
]
log("  %-6s %8s %8s %8s %8s %-10s %-8s %s" % ("RÉP", "X0", "Y0", "X1", "Y1", "PROF", "L", "APPUI"))
for ref, x0, y0, x1, y1, demi, prof, L, appui in LINTEAUX:
    log("  %-6s %8.1f %8.1f %8.1f %8.1f %-10s %-8s %s" % (ref, x0, y0, x1, y1, prof, L, appui))

S1_R3 = [
    (8547.5, 5798.6, 8567.5, 5834.1, "S1 R3-N N"),
    (8547.5, 5584.2, 8567.5, 5619.7, "S1 R3-N S"),
    (8547.5, 5222.5, 8567.5, 5258.0, "S1 R3-S N"),
    (8547.5, 5007.9, 8567.5, 5043.7, "S1 R3-S S"),
]
S2_F1 = [
    (8952.5, 5320.2, 9002.5, 5340.2, "S2 F1a S"),
    (9279.8, 5464.1, 9299.8, 5514.1, "S2 F1b O"),
    (9407.5, 5189.1, 9427.5, 5239.1, "S2 F1c O"),
    (9512.5, 5189.1, 9532.5, 5239.1, "S2 F1c E"),
]

doc = ezdxf.readfile(SRC)
n_del, n_blk = purge_unused_blocks(doc)
log("  purge blocs : −%d → %d restants" % (n_del, n_blk))

for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9

LAYERS = (
    ("LINTEAU-AXES", 1), ("LINTEAU-PROFILES", 1), ("LINTEAU-SOMMIER", 3),
    ("LINTEAU-EXISTANT", 8), ("LINTEAU-COTATION", 8), ("LINTEAU-DETAILS", 4),
    ("LINTEAU-NOMENCLATURE", 7), ("LINTEAU-HABILLAGE-TEXTE", 7),
    ("LINTEAU-CARTOUCHE", 7), ("LINTEAU-HYP", 6),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="LINTEAU-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="LINTEAU-SOMMIER", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.0, layer="LINTEAU-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + max(40, len(t) * ht * 0.5), ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


def bande(x0, y0, x1, y1, demi, layer="LINTEAU-PROFILES", hatch=1):
    """Bande centrée sur le segment, largeur 2*demi (cm)."""
    dx, dy = x1 - x0, y1 - y0
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx, ny = -dy / L * demi, dx / L * demi
    pts = [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)]
    msp.add_lwpolyline(pts + [pts[0]], dxfattribs={"layer": layer})
    hh = msp.add_hatch(color=hatch, dxfattribs={"layer": layer})
    hh.paths.add_polyline_path(pts, is_closed=True)


# Axes
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "LINTEAU-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "LINTEAU-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "LINTEAU-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "LINTEAU-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "LINTEAU-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "LINTEAU-AXES")

# Sommiers d'abord (sous l'acier)
for x0, y0, x1, y1, lab in S1_R3:
    rect(x0, y0, x1, y1, "LINTEAU-SOMMIER", hatch_col=3)
for x0, y0, x1, y1, lab in S2_F1:
    rect(x0, y0, x1, y1, "LINTEAU-SOMMIER", hatch_col=3)

# Linteaux
for ref, x0, y0, x1, y1, demi, prof, L, appui in LINTEAUX:
    bande(x0, y0, x1, y1, demi, "LINTEAU-PROFILES", hatch=1)
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    if ref.startswith("R3"):
        leader(7960.0, my + 15.0, x0 - 8.0, my,
               "%s : UPE 200 + C25/30 (D-36)  L=%s  |  2xS1 ABOUTS, hors bois" % (ref, L),
               12.0, "LINTEAU-PROFILES")
    else:
        tx = 9645.0 if mx > 9100 else 7960.0
        leader(tx, my + 18.0, x1 if mx > 9100 else x0, my,
               "%s : 2x HEA 200  L=%s  |  %s  |  taux 0,059 env." % (ref, L, appui),
               12.0, "LINTEAU-PROFILES")

# E-08 court-circuité — même baies que R3, décalé, EXISTANT
for y0, y1, lab in [(5584.2, 5834.1, "E-08 N COURT-CIRCUITE (bois RESTE, hors calcul)"),
                    (5007.9, 5258.0, "E-08 S COURT-CIRCUITE (bois RESTE, hors calcul)")]:
    msp.add_lwpolyline([(8595.0, y0), (8595.0, y1)], dxfattribs={"layer": "LINTEAU-EXISTANT"})
    txt(8602.0, (y0 + y1) / 2.0, lab, 10.5, "LINTEAU-EXISTANT")

leader(9645.0, 5810.0, 8567.5, 5816.0,
       "S1 200x400x200 : ABOUTS DE MUR — hors emprise bois (R-46-4 CLOSE)", 12.0, "LINTEAU-SOMMIER")
leader(9645.0, 5360.0, 9002.5, 5330.0,
       "S2 200x500x200 sous F1 — w_b 200 mm >= 90 mm (EC6 8.1.6)", 12.0, "LINTEAU-SOMMIER")

txt(7960.0, 4688.0, "F2 / F3 / R1 : PAS des linteaux — B-60 METAL / MACON (coussins D-37).", 11.5)
txt(7960.0, 4660.0, "Seuils BA : SANS OBJET. Linteau Ouest 23x15 : soulage par P1 (METAL), bois RESTE.", 11.5)
txt(7960.0, 4632.0, "Aucun scellement nouveau (B-50). Section F1 CONTRACTUELLE — ne pas reduire.", 11.5)

# --- DROITE ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "LINTEAU-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "LINTEAU-AXES")
txt(rx0 + 20.0, 6462.0,
    "B-60 Ind. A  |  LINTEAU EXE  |  F1a/b/c + R3-N/S IMPLANTES  |  NE PAS EXECUTER SANS EXE COTE ET VISA",
    13.5, "LINTEAU-AXES")

K = 2.5
txt(rx0 + 25.0, 6378.0, "1. SECTIONS — cotes mm  —  S275  —  ne pas reduire F1 (D2 f.01)", 13.0, "LINTEAU-DETAILS")

# 2 x HEA 200
hx, hy = rx0 + 280.0, 6120.0
bw, bh = 20.0 * K / 2, 19.0 * K / 2
for s in (-1, 1):
    cx = hx + s * (bw + 2)
    rect(cx - bw, hy - bh, cx + bw, hy + bh, "LINTEAU-PROFILES")
    # âme + semelles schématiques
    msp.add_line((cx, hy - bh + 3), (cx, hy + bh - 3), dxfattribs={"layer": "LINTEAU-PROFILES"})
txt(hx - 70, hy + bh + 40, "F1a/b/c  :  2 x HEA 200  S275", 12.5, "LINTEAU-PROFILES")
txt(hx - 70, hy + bh + 20, "h=190  b=200  |  M_Rd 236 kN.m  |  taux env. 0,059", 11.0)
txt(hx - 70, hy - bh - 28, "Appui S2 200x500x200  |  triangle 60 deg OK 0,010", 11.0)

# UPE 200 + béton
ux, uy = rx0 + 1100.0, 6120.0
uw, uh = 8.0 * K / 2, 20.0 * K / 2
rect(ux - uw - 4, uy - uh, ux + uw + 8, uy + uh, "LINTEAU-HYP", hatch_col=8)  # béton
rect(ux - uw, uy - uh, ux + uw, uy + uh, "LINTEAU-PROFILES")
txt(ux - 40, uy + uh + 40, "R3-N/S  :  UPE 200 + remplissage C25/30 (D-36)", 12.5, "LINTEAU-PROFILES")
txt(ux - 40, uy + uh + 20, "L_baie 1550 mm  |  M_Ed 17,9 / 61,6 = 0,291  |  torsion CLOSE", 11.0)
txt(ux - 40, uy - uh - 28, "Detail de coulage du remplissage -> B-60 METAL", 11.0, "LINTEAU-HYP")

# Cotation S1 hors bois
txt(rx0 + 25.0, 5860.0, "2. COTATION S1 HORS BOIS  —  R-46-4  —  cotes mm", 13.0, "LINTEAU-DETAILS")
cx, cy = rx0 + 380.0, 5600.0
# mur
rect(cx - 40, cy - 90, cx + 40, cy + 90, "LINTEAU-EXISTANT")
# bois E-08 (existant, non porteur)
msp.add_lwpolyline([(cx + 50, cy - 70), (cx + 50, cy + 70)], dxfattribs={"layer": "LINTEAU-EXISTANT"})
txt(cx + 58, cy + 40, "E-08 bois (RESTE, hors calcul)", 10.5, "LINTEAU-EXISTANT")
# R3 UPE
rect(cx - 8, cy - 78, cx + 8, cy + 78, "LINTEAU-PROFILES", hatch_col=1)
# S1 abouts
rect(cx - 30, cy + 78, cx + 10, cy + 118, "LINTEAU-SOMMIER", hatch_col=3)
rect(cx - 30, cy - 118, cx + 10, cy - 78, "LINTEAU-SOMMIER", hatch_col=3)
txt(cx + 180, cy + 90, "S1 200 x 400 x 200 mm  —  ABOUT de mur", 12.0, "LINTEAU-SOMMIER")
txt(cx + 180, cy + 68, "Hors emprise du linteau bois. Aucun sommier sur E-08.", 11.0)
txt(cx + 180, cy + 20, "R3  UPE 200  L_baie = 1550 mm  (profilé livré 2500 mm)", 11.5, "LINTEAU-PROFILES")
txt(cx + 180, cy - 10, "Remplissage C25/30 entre ailes  —  D-36  —  R-50-2 CLOSE", 11.0)
txt(cx + 180, cy - 70, "2 x S1 par linteau. w_b = 200 mm. Coussin D-37 NON requis sur R3.", 11.0)

# D-34
rect(rx0 + 18.0, 5008.0, rx1 - 18.0, 5368.0, "LINTEAU-AXES")
d34 = [
    "D-34 — MAÇONNERIE (mot pour mot, plan ET note) : f_k = 1,5 MPa · f_vk0 = 0,15 MPa.",
    "Essais hors mission. Si non concluants : reprise d'étude chiffrée.",
    "D-36 : UPE 200 de R3 REMPLI C25/30.  D-26 : AUCUNE vérif. sismique.  D-28 : AUCUN joint de dilatation.",
    "D-37 (coussins R1/F2/F3) : PAS des linteaux — B-60 MACON.  Feu : ADEQUATE A PREVOIR (hors lot GO).",
    "E-08 : court-circuité. Aucun relevé de bois (non prescrit). Seuils BA : SANS OBJET.",
]
for k, line in enumerate(d34):
    txt(rx0 + 32.0, 5335.0 - k * 58.0, line, 11.0,
        "LINTEAU-AXES" if k == 0 else "LINTEAU-HABILLAGE-TEXTE")

txt(rx0 + 25.0, 4965.0, "3. NOMENCLATURE GRAPHIQUE (faconnage -> B-62)", 13.0, "LINTEAU-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 4950.0, "LINTEAU-NOMENCLATURE")
nom_l = [
    "F1a  2xHEA 200  L=1000  x1  |  S2 200x500x200  |  File D  |  taux 0,010 / 0,059",
    "F1b  2xHEA 200  L= 900  x1  |  S2 + P3         |  File 4  |  taux 0,008 / 0,059",
    "F1c  2xHEA 200  L= 850  x1  |  2x S2           |  File 3  |  taux 0,007 / 0,059",
    "R3-N UPE 200 + C25/30  L_baie=1550  x1  |  2x S1 ABOUTS  |  0,291  |  D-36",
    "R3-S UPE 200 + C25/30  L_baie=1550  x1  |  2x S1 ABOUTS  |  0,291  |  D-36",
    "S1 x4 (R3)  200x400x200 C25/30  |  S2 x4 (F1)  200x500x200 C25/30  |  S275 profilés",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 32.0, 4918.0 - k * 62.0, line, 11.2, "LINTEAU-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "LINTEAU-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "LINTEAU-AXES")
txt(rx0 + 25.0, 4412.0, "B-60 LINTEAU EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D · amont B-49 A", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "LINTEAU-AXES")
txt(rx0 + 25.0, 4352.0, "Protection au feu : ADEQUATE A PREVOIR (hors lot GO)  ·  CARNAC v3.0  ·  cotes mm  ·  DXF cm", 11.0)

chemin = BASE + ".dxf"
doc.saveas(chemin)
audit = doc.audit()
log("")
log("  écrit : %s (%d o) — audit %d — blocs %d" % (
    chemin, os.path.getsize(chemin), len(audit.errors), len(list(doc.blocks))))

doc2 = ezdxf.readfile(chemin)
cnt = Counter(e.dxf.layer for e in doc2.modelspace())
titre("[3] V13")
for lay, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
    if lay.startswith("LINTEAU-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
nlin = sum(n for l, n in cnt.items() if l.startswith("LINTEAU-"))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  LINTEAU-* = %d  ·  calque 0 ajouts = %d  ·  manquants : %s" % (
    nlin, cnt.get("0", 0), manquants or "aucun"))

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
    "CROISSY-FLORA — B-60 Ind. A — LINTEAUX EXE COTÉS (F1a/b/c · R3-N/S)\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D · S1 hors bois)",
    fontsize=11.0, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "LINTEAU", "indice": "A", "mode": "PARTIEL-DECLARE",
    "neufs": ["F1a", "F1b", "F1c", "R3-N", "R3-S"],
    "seuils": "SANS OBJET", "E08": "court-circuite",
    "purge": n_del, "blocs": n_blk, "audit": len(audit.errors),
    "n_LINTEAU": nlin, "calques_manquants": manquants,
    "octets": os.path.getsize(chemin),
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_linteau.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_linteau.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("Journal : %s" % os.path.join(OUT, "b60_linteau.txt"))
