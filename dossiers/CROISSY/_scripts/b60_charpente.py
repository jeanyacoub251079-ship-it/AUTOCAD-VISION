#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type CHARPENTE — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D R+1 (report, jamais redessin). Note B-44 Ind. A.
Pannes PN1/2/3, demi-fermes DF1/2, contrefiches CF — positions B-20.
E-07 NON CHARGÉ. PA-03 reste ouvert (B-43). Existant E-04/05/06 hors calcul.
Assemblages → B-60 ASSEMBLAGE. Purge blocs non référencés (viewer JS).
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
SRC = os.path.join(ROOT, "_plans", "FLORA_R1_VUE-NETTOYEE_IndD.dxf")
PLANS = os.path.join(ROOT, "_plans")
OUT = os.path.join(ROOT, "_rendus")
BASE = os.path.join(PLANS, "FLORA_B60_CHARPENTE_EXE_IndA")
LIGNES = []
DY = -3726.0  # B-20 : R+1_PROJ − RDC_PROJ


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
log("B-60 — PLANS D'EXÉCUTION — type CHARPENTE — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-44 A · H-29 · PA-03 ouvert · existant hors calcul)")
log("=" * 78)

titre("[0] ENTRÉES")
log("  Note amont : B-44 Ind. A — neufs OK : PN 0,830 · DF-arb 0,626 · DF-ent 0,108 · CF 0,940")
log("  Positions  : B-20 Ind. B planche 3 — millimètre, DY=-3726 cm, aucune position inventée")
log("  Vue        : B-32 Ind. D R+1")
log("  Hors type  : assemblages (sabots, ancrages) → B-60 ASSEMBLAGE")
log("  Hors type  : E-04/05/06 existant (B-24) · E-07 non chargé · ZN1/ZN2 aucun calcul")

titre("[1] CLAUSES")
log("  D-34 : f_k=1,5 MPa · f_vk0=0,15 MPa · essais hors mission — PLAN ET NOTE.")
log("  D-26 : AUCUNE vérif. sismique. D-28 : AUCUN joint de dilatation.")
log("  D-38 : B-41 / B-48 SANS OBJET.")
log("  C24 spécification d'approvisionnement. Classe de service 2 (MAT-08).")
log("  E-07 NON CHARGÉ — demi-fermes désolidarisées. PA-03 reste ouvert (B-43).")
log("  Contreventement de toiture : ABSENT au D2 — pannes ≠ diaphragme. Non inventé.")
log("  Protection au feu : ADEQUATE A PREVOIR (hors lot GO) — NON dimensionnee.")

# Positions B-20 planche 3, déjà en Y R+1
PANNES = [
    ("PN1", 8856.0, 4961.7 + DY, 8856.0, 5881.7 + DY, 12.0, "75x200 C24", "3,20 m", "Aile Est  e=1,60  w 0,830"),
    ("PN2", 9002.5, 5535.6 + DY, 9537.1, 5535.6 + DY, 12.0, "75x200 C24", "3,20 m", "Hall Nord  w 0,830"),
    ("PN3", 9002.5, 5271.3 + DY, 9537.1, 5271.3 + DY, 12.0, "75x200 C24", "3,20 m", "Hall Sud   w 0,830"),
]
DF = [
    ("DF1", 8567.5, 5566.6 + DY, 8952.5, 5566.6 + DY, 14.0, "arb 100x200 + ent 75x200", "3,20 m", "Est N  File A-C  arb 0,626"),
    ("DF2", 8567.5, 5276.8 + DY, 8952.5, 5276.8 + DY, 14.0, "arb 100x200 + ent 75x200", "3,20 m", "Est S  File A-C  arb 0,626"),
]
CF = ("CF", 9537.1, 5139.2 + DY, 9537.1, 5667.7 + DY, 16.0, "75x225 C24", "2,62 m", "Ouest  APRES purge E-05  0,940")
ZN = [
    ("ZN1", 9005.0, 5685.0 + DY, 9525.0, 6295.0 + DY, "Nord — relevé avant taille"),
    ("ZN2", 9005.0, 4480.0 + DY, 9525.0, 5120.0 + DY, "Sud  — relevé avant taille"),
]

titre("[2] IMPLANTATION (report B-20 R+1, cm DXF)")
log("  %-6s %8s %8s %8s %8s %-24s %-8s" % ("RÉP", "X0", "Y0", "X1", "Y1", "SECTION", "L"))
for r in PANNES + DF + [CF]:
    log("  %-6s %8.1f %8.1f %8.1f %8.1f %-24s %-8s" % (r[0], r[1], r[2], r[3], r[4], r[6], r[7]))
log("  ZN1/ZN2 : nuages D-19 — AUCUN CALCUL. E-07 non chargé. Rien n'est recalculé.")

doc = ezdxf.readfile(SRC)
n_del, n_blk = purge_unused_blocks(doc)
log("  purge blocs : −%d → %d restants" % (n_del, n_blk))

for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9

LAYERS = (
    ("CHARPENTE-AXES", 1), ("CHARPENTE-PANNES", 3), ("CHARPENTE-FERMES", 1),
    ("CHARPENTE-CONTREFICHES", 4), ("CHARPENTE-EXISTANT", 8), ("CHARPENTE-HYP", 6),
    ("CHARPENTE-COTATION", 8), ("CHARPENTE-DETAILS", 4), ("CHARPENTE-NOMENCLATURE", 7),
    ("CHARPENTE-HABILLAGE-TEXTE", 7), ("CHARPENTE-CARTOUCHE", 7),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="CHARPENTE-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="CHARPENTE-CARTOUCHE", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.0, layer="CHARPENTE-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + max(40, len(t) * ht * 0.5), ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


def bande(x0, y0, x1, y1, w_cm, layer, hatch=1, double=False):
    dx, dy = x1 - x0, y1 - y0
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx, ny = -dy / L * (w_cm / 2.0), dx / L * (w_cm / 2.0)
    pts = [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)]
    msp.add_lwpolyline(pts + [pts[0]], dxfattribs={"layer": layer})
    hh = msp.add_hatch(color=hatch, dxfattribs={"layer": layer})
    hh.paths.add_polyline_path(pts, is_closed=True)
    if double:
        for sgn in (-0.22, 0.22):
            msp.add_line((x0 + nx * 2 * sgn, y0 + ny * 2 * sgn),
                         (x1 + nx * 2 * sgn, y1 + ny * 2 * sgn),
                         dxfattribs={"layer": layer})
    else:
        msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})


def cloud(x0, y0, x1, y1, step=32.0):
    pts = []
    x = x0
    while x < x1:
        pts.append((x, y0)); x += step
    y = y0
    while y < y1:
        pts.append((x1, y)); y += step
    x = x1
    while x > x0:
        pts.append((x, y1)); x -= step
    y = y1
    while y > y0:
        pts.append((x0, y)); y -= step
    pts.append((x0, y0))
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        mx, my = 0.5 * (ax + bx), 0.5 * (ay + by)
        dx, dy = bx - ax, by - ay
        L = (dx * dx + dy * dy) ** 0.5 or 1.0
        nx, ny = -dy / L * 8.0, dx / L * 8.0
        msp.add_arc((mx + nx, my + ny), 0.55 * L, 0, 360,
                    dxfattribs={"layer": "CHARPENTE-HYP"})


# Axes — mêmes files que RDC, Y translaté
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 620.0), (xv, 2620.0), dxfattribs={"layer": "CHARPENTE-AXES"})
    msp.add_circle((xv, 2650.0), 24.0, dxfattribs={"layer": "CHARPENTE-AXES"})
    txt(xv - 8.0, 2642.0, code, 18.0, "CHARPENTE-AXES")
for code, y_rdc in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    yv = y_rdc + DY
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "CHARPENTE-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "CHARPENTE-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "CHARPENTE-AXES")

# Pannes
for ref, x0, y0, x1, y1, w, sec, L, note in PANNES:
    bande(x0, y0, x1, y1, w, "CHARPENTE-PANNES", hatch=3, double=False)
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    if ref == "PN1":
        txt(x0 + 16.0, my - 8.0, "PN1  75x200 C24  L=3,20 m", 11.5, "CHARPENTE-PANNES")
    else:
        txt(mx - 70.0, my + 14.0, "%s  75x200 C24  L=3,20" % ref, 11.5, "CHARPENTE-PANNES")

# Demi-fermes
for ref, x0, y0, x1, y1, w, sec, L, note in DF:
    bande(x0, y0, x1, y1, w, "CHARPENTE-FERMES", hatch=1, double=True)
    leader(7920.0, y0 + 10.0, x0, y0,
           "%s  arb 100x200 + ent 75x200  L=3,20 m  |  desolidarisee E-07" % ref,
           11.5, "CHARPENTE-FERMES")

# Contrefiches sur ferme tradi existante (report B-20, pas de diagonale inventée)
ref, x0, y0, x1, y1, w, sec, L, note = CF
bande(x0, y0, x1, y1, w, "CHARPENTE-CONTREFICHES", hatch=4, double=True)
leader(9645.0, (y0 + y1) / 2.0, x0 + 8.0, (y0 + y1) / 2.0,
       "CF  75x225 C24  L=2,62 m  |  APRES purge E-05  |  0,940",
       11.5, "CHARPENTE-CONTREFICHES")
txt(9548.0, y0 - 28.0, "E-05 ferme tradi : EXISTANT — B-24, hors calcul", 11.0, "CHARPENTE-EXISTANT")

# Nuages ZN
for nom, x0, y0, x1, y1, lab in ZN:
    cloud(x0, y0, x1, y1)
    txt(x0 + 40.0, (y0 + y1) / 2.0, "%s  ZONE NON RELEVEE  |  %s  |  D-19" % (nom, lab),
        12.0, "CHARPENTE-HYP")

txt(7920.0, 980.0, "E-04 potelets : SUPPRIMES par DF1/DF2. Ordre : 1. pose DF  2. reprise pannes  3. depose potelets.", 11.5)
txt(7920.0, 952.0, "E-06 pannes existantes : B-24, non calculees. Les 3 neuves S'AJOUTENT.", 11.5)
txt(7920.0, 924.0, "E-07 plancher haut : NON CHARGE. PA-03 reste ouvert (B-43). Vide de desolidarisation.", 11.5)
txt(7920.0, 896.0, "Contreventement toiture : ABSENT au D2. Pannes ≠ diaphragme. Non invente.", 11.5)
txt(7920.0, 868.0, "Sabots / ancrages / boulons CF : B-60 ASSEMBLAGE (B-50). Feu : hors lot GO.", 11.5)

# --- PANNEAU DROIT ---
rx0, rx1 = 10260.0, 12020.0
ry0, ry1 = 560.0, 2700.0
rect(rx0, ry0, rx1, ry1, "CHARPENTE-CARTOUCHE")
rect(rx0, 2605.0, rx1, 2700.0, "CHARPENTE-AXES")
txt(rx0 + 20.0, 2642.0,
    "B-60 Ind. A  |  CHARPENTE EXE  |  R+1  |  NE PAS EXECUTER SANS EXE COTE ET VISA",
    13.0, "CHARPENTE-AXES")

# 1. Coupe DF
txt(rx0 + 25.0, 2558.0, "1. DEMI-FERME TYPE — cotes mm — ech. 1/20 — C24 — desolidarisee", 13.0, "CHARPENTE-DETAILS")
K = 0.55  # 1 m = 55 u  → L=3,20 m → 176 u ; h=1,70 → 93.5
cx, cy = rx0 + 220.0, 2280.0
# entrait
msp.add_lwpolyline([(cx, cy), (cx + 3.20 * 100 * K, cy)], dxfattribs={"layer": "CHARPENTE-FERMES"})
# arbalétrier
msp.add_lwpolyline([(cx, cy), (cx + 3.20 * 100 * K, cy + 1.70 * 100 * K)],
                   dxfattribs={"layer": "CHARPENTE-FERMES"})
# vide E-07
msp.add_lwpolyline([(cx, cy - 18.0), (cx + 3.20 * 100 * K, cy - 18.0)],
                   dxfattribs={"layer": "CHARPENTE-EXISTANT"})
txt(cx + 20, cy - 36, "E-07  —  VIDE de desolidarisation  —  NON CHARGE", 11.0, "CHARPENTE-EXISTANT")
txt(cx + 20, cy + 8, "entrait 75x200 C24  N=14,0 kN  taux 0,108", 11.0, "CHARPENTE-FERMES")
txt(cx + 40, cy + 70, "arbaletrier 100x200 C24  N=31,7 kN  taux 0,626", 11.0, "CHARPENTE-FERMES")
txt(cx + 3.20 * 100 * K + 12, cy - 8, "File C", 11.0, "CHARPENTE-AXES")
txt(cx - 50, cy - 8, "File A", 11.0, "CHARPENTE-AXES")
msp.add_line((cx, cy - 50), (cx + 3.20 * 100 * K, cy - 50), dxfattribs={"layer": "CHARPENTE-COTATION"})
txt(cx + 70, cy - 66, "L = 3 200 mm", 11.0, "CHARPENTE-COTATION")
txt(cx + 3.20 * 100 * K + 12, cy + 40, "h = 1 700 mm  alpha=28 deg", 11.0, "CHARPENTE-COTATION")
txt(cx, cy + 110, "Appuis : murs Files A et C  V=14,89 kN  —  sabots -> ASSEMBLAGE", 11.0)

# 2. Tableau
txt(rx0 + 25.0, 2140.0, "2. BOIS NEUFS  —  report B-44 / B-20  —  rien recalcule", 13.0, "CHARPENTE-DETAILS")
rect(rx0 + 18.0, 1860.0, rx1 - 18.0, 2125.0, "CHARPENTE-DETAILS")
tab = [
    "PN1/2/3  75 x 200 C24  L=3,20 m  e=1,60 m  w_fin 0,830 (L/300)  k_crit=1,00 SANS maintien",
    "DF-arb   100 x 200 C24  L=3,62 m  N=31,72 kN  flamb. 0,626  (lambda_rel 2,13)",
    "DF-ent   75 x 200 C24  L=3,20 m  N=14,00 kN  traction 0,108",
    "CF       75 x 225 C24  L=2,62 m  N=44,03 kN  flamb. 0,940  — APRES purge E-05",
    "Classe C24 = specification. Service 2 (MAT-08). k_mod=0,80  k_def=0,80  gamma_M=1,30.",
    "H-29 G_toiture=0,95 kN/m2. Pas de soulevement net (G gouverne). Ancrages -> ASSEMBLAGE.",
]
for k, line in enumerate(tab):
    txt(rx0 + 28.0, 2095.0 - k * 38.0, line, 11.0, "CHARPENTE-DETAILS")

# 3. Clauses
rect(rx0 + 18.0, 1488.0, rx1 - 18.0, 1835.0, "CHARPENTE-AXES")
d34 = [
    "D-34 — MAÇONNERIE (mot pour mot, plan ET note) : f_k = 1,5 MPa · f_vk0 = 0,15 MPa.",
    "Essais hors mission. Si non concluants : reprise d'étude chiffrée.",
    "D-26 : AUCUNE vérif. sismique.  D-28 : AUCUN joint de dilatation.  D-38 : pas de pieu / prédalle.",
    "E-07 NON CHARGE. PA-03 reste OUVERT (B-43). Ne pas clore.",
    "Contreventement toiture ABSENT au D2 — non inventé. ZN1/ZN2 : relevé avant taille (D-19).",
    "Feu : ADEQUATE A PREVOIR (hors lot GO). Termites : D1 § 01.2.1.9.2 déjà prescrit.",
]
for k, line in enumerate(d34):
    txt(rx0 + 32.0, 1800.0 - k * 48.0, line, 11.0,
        "CHARPENTE-AXES" if k == 0 else "CHARPENTE-HABILLAGE-TEXTE")

# 4. Nomenclature + phasage
txt(rx0 + 25.0, 1445.0, "3. NOMENCLATURE GRAPHIQUE (assemblages -> B-62 / ASSEMBLAGE)", 12.5, "CHARPENTE-NOMENCLATURE")
rect(rx0 + 18.0, 980.0, rx1 - 18.0, 1430.0, "CHARPENTE-NOMENCLATURE")
nom_l = [
    "PN1/PN2/PN3  x3  75 x 200 C24  L=3200  entraxe 1600  |  flèche gouverne 0,830",
    "DF1/DF2  x2  arb 100 x 200 + ent 75 x 200 C24  L_horiz=3200  |  desolidarisees",
    "CF  x2  75 x 225 C24  L=2620  |  sur E-05  |  APRES purge (B-23 P-2)",
    "Hors nomencl. : E-04 supprimes · E-05/06 B-24 · E-07 non charge · ZN1/ZN2 D-19.",
    "PHASAGE E-04 : 1. pose DF1/DF2  2. reprise pannes  3. depose potelets. Inverse INTERDIT.",
    "PHASAGE E-05 : 1. purge bois mort  2. traitement  3. pose CF. Inverse INTERDIT.",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 28.0, 1395.0 - k * 62.0, line, 11.2, "CHARPENTE-NOMENCLATURE")

rect(rx0, 560.0, rx1, 700.0, "CHARPENTE-CARTOUCHE")
txt(rx0 + 25.0, 670.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "CHARPENTE-AXES")
txt(rx0 + 25.0, 638.0, "B-60 CHARPENTE EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D R+1 · amont B-44 A", 12.0)
txt(rx0 + 25.0, 604.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "CHARPENTE-AXES")
txt(rx0 + 25.0, 574.0, "Protection au feu : ADEQUATE A PREVOIR (hors lot GO)  ·  CARNAC v3.0  ·  cotes mm  ·  DXF cm", 11.0)

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
    if lay.startswith("CHARPENTE-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
nch = sum(n for l, n in cnt.items() if l.startswith("CHARPENTE-"))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  CHARPENTE-* = %d  ·  calque 0 ajouts = %d  ·  manquants : %s" % (
    nch, cnt.get("0", 0), manquants or "aucun"))

fig = plt.figure(figsize=(16.54, 11.69))
ax = fig.add_axes([0.015, 0.02, 0.97, 0.90])
cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
Frontend(RenderContext(doc2), MatplotlibBackend(ax), config=cfg).draw_layout(
    doc2.modelspace(), finalize=False)
ax.set_xlim(7900.0, 12100.0)
ax.set_ylim(430.0, 2760.0)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
ax.set_title(
    "CROISSY-FLORA — B-60 Ind. A — CHARPENTE EXE — R+1  PN / DF / CF\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D R+1 · C24)",
    fontsize=11.0, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "CHARPENTE", "indice": "A", "mode": "PARTIEL-DECLARE",
    "pannes": 3, "demi_fermes": 2, "contrefiches": 1,
    "E07_charge": False, "PA03": "ouvert",
    "purge": n_del, "blocs": n_blk, "audit": len(audit.errors),
    "n_CHARPENTE": nch, "calques_manquants": manquants,
    "octets": os.path.getsize(chemin),
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_charpente.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_charpente.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("Journal : %s" % os.path.join(OUT, "b60_charpente.txt"))
