#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type ASSEMBLAGE — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D RDC (report, jamais redessin). Note B-50 Ind. A.
A2 10 M16 R1 · A5 platines P1 · A4 M12 Stab1 (NON CHIFFRÉ).
A1 déjà FOND · A3 déjà METAL (D-36) · A6 déjà MACON.
Sabots charpente : efforts B-44, type non catalogué (DOC-09) — non inventé.
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
BASE = os.path.join(PLANS, "FLORA_B60_ASSEMBLAGE_EXE_IndA")
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
log("B-60 — PLANS D'EXÉCUTION — type ASSEMBLAGE — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-50 A · A4 DOC-09 · sabots non catalogués · feu hors lot)")
log("=" * 78)

titre("[0] ENTRÉES")
log("  Note amont : B-50 Ind. A — A1/A2/A5 OK · A3 CLOSE D-36 · A4 NON CALCULABLE · A6 → MACON")
log("  Positions  : B-20 Ind. B — millimètre, aucune position inventée")
log("  Vue        : B-32 Ind. D RDC")
log("  Déjà livré : A1 (FOND) · A3 D-36 (METAL) · A6 coussins (MACON)")
log("  Hors type  : type de sabot charpente (DOC-09) — non inventé")

titre("[1] CLAUSES")
log("  D-34 : f_k=1,5 MPa · f_vk0=0,15 MPa · essais hors mission — PLAN ET NOTE.")
log("  D-26 : AUCUNE vérif. sismique. D-28 : AUCUN joint de dilatation.")
log("  D-29 : aucun effort horizontal aux platines P1 (maçonnerie seule).")
log("  A4 : AUCUNE capacité écrite (DOC-09 exclue). R-50-3 OUVERTE.")
log("  A1 : 3 conditions (équerre, c_nom 50, cadres HA8) — déjà FOND. R-50-1 CLOSE.")
log("  A3 : sans D-36, R3 NE PAS POSER. R-50-2 CLOSE (METAL).")
log("  Protection au feu : ADEQUATE A PREVOIR (hors lot GO) — NON dimensionnee.")
log("  Galva ISO 1461 70 um (B-50 §10).")

# A2 — 5 rangées × 2, entraxe 700 mm, sur R1 B-20
R1X0, R1Y, R1X1 = 8547.5, 5488.7, 8969.8
A2_ROWS = [8618.5, 8688.5, 8758.5, 8828.5, 8898.5]  # e3 ~ 71 cm ≥ 11,2
# A5
P1 = [("P1-N", 9540.5, 4904.4), ("P1-S", 9540.5, 4778.4)]
# A4 Stab1 files
STAB = [
    ("Stab1-NW", 9175.5, 5534.2, 9175.5, 6296.7),
    ("Stab1-NE", 9349.4, 5534.2, 9349.4, 6296.7),
    ("Stab1-SW", 9175.5, 4509.9, 9175.5, 5189.1),
    ("Stab1-SE", 9349.4, 4509.9, 9349.4, 5189.1),
]
P2 = (9535.0, 5929.2)

titre("[2] IMPLANTATION (report B-20 / B-50, cm DXF)")
log("  A2  R1  10 M16 8.8 / face  5 rangées e=700 mm  e2=90 mm  taux 0,691  bois gouverne")
log("  A5  P1-N/S  platine 200x200x15  4 M16 8.8 constructif  sigma 0,118")
log("  A4  Stab1  2 M12 / file  F<=5,8 kN  NON CHIFFRÉ (DOC-09)  R-50-3")
log("  A1  P2/SF1  6 HA12 équerre l_bd 166  — déjà FOND")
log("  A3  R3  D-36  — déjà METAL")
log("  A6  8 appuis  — déjà MACON")
log("  Sabots DF/PN : V=5,11 / 14,89 kN — type NON catalogué, non inventé")

doc = ezdxf.readfile(SRC)
n_del, n_blk = purge_unused_blocks(doc)
log("  purge blocs : −%d → %d restants" % (n_del, n_blk))

for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9

LAYERS = (
    ("ASSEMBLAGE-AXES", 1), ("ASSEMBLAGE-BOULONS", 1), ("ASSEMBLAGE-PLATINES", 6),
    ("ASSEMBLAGE-SCELLEMENTS", 4), ("ASSEMBLAGE-ANCRAGES", 3), ("ASSEMBLAGE-EXISTANT", 8),
    ("ASSEMBLAGE-DETAILS", 4), ("ASSEMBLAGE-NOMENCLATURE", 7),
    ("ASSEMBLAGE-HABILLAGE-TEXTE", 7), ("ASSEMBLAGE-CARTOUCHE", 7), ("ASSEMBLAGE-HYP", 6),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="ASSEMBLAGE-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer, hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.0, layer="ASSEMBLAGE-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + max(40, len(t) * ht * 0.5), ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


# Axes
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "ASSEMBLAGE-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "ASSEMBLAGE-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "ASSEMBLAGE-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "ASSEMBLAGE-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "ASSEMBLAGE-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "ASSEMBLAGE-AXES")

# R1 report (hôte A2)
msp.add_line((R1X0, R1Y), (R1X1, R1Y), dxfattribs={"layer": "ASSEMBLAGE-EXISTANT"})
txt((R1X0 + R1X1) / 2.0 - 80, R1Y + 22.0, "R1  2x UPE 200  moisage  |  A2  10 M16 8.8 / face", 11.5, "ASSEMBLAGE-EXISTANT")

# A2 boulons : 5 × 2 cercles Ø16 mm = 1,6 cm
for x in A2_ROWS:
    for dy in (-4.5, 4.5):
        msp.add_circle((x, R1Y + dy), 0.8, dxfattribs={"layer": "ASSEMBLAGE-BOULONS"})
leader(7920.0, R1Y + 8.0, R1X0, R1Y,
       "A2  10 M16 8.8 / face  e=700 mm  e2=90  taux 0,691  BOIS gouverne (11,2 kN)",
       11.5, "ASSEMBLAGE-BOULONS")

# A5 platines 200×200 mm = 20 cm
for ref, xc, yc in P1:
    rect(xc - 10.0, yc - 10.0, xc + 10.0, yc + 10.0, "ASSEMBLAGE-PLATINES", hatch_col=6)
    for dx, dy in [(-6, -6), (6, -6), (-6, 6), (6, 6)]:
        msp.add_circle((xc + dx, yc + dy), 0.8, dxfattribs={"layer": "ASSEMBLAGE-PLATINES"})
    leader(9645.0, yc + 8.0, xc + 10.0, yc,
           "%s  A5  platine 200x200x15  4 M16 8.8 constructif" % ref,
           11.5, "ASSEMBLAGE-PLATINES")

# A4 Stab1 — 2 M12 par file, entraxe 10 cm ( ≥ 100 mm), au milieu de chaque file
for ref, x0, y0, x1, y1 in STAB:
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": "ASSEMBLAGE-EXISTANT"})
    ym = (y0 + y1) / 2.0
    msp.add_circle((x0, ym - 5.0), 0.6, dxfattribs={"layer": "ASSEMBLAGE-SCELLEMENTS"})
    msp.add_circle((x0, ym + 5.0), 0.6, dxfattribs={"layer": "ASSEMBLAGE-SCELLEMENTS"})
txt(9188.0, 6100.0, "A4  Stab1  2 M12 / file  F<=5,8 kN  NON CHIFFRE (DOC-09)  R-50-3", 11.0, "ASSEMBLAGE-HYP")

# A1 report
rect(P2[0] - 12.5, P2[1] - 7.5, P2[0] + 12.5, P2[1] + 7.5, "ASSEMBLAGE-ANCRAGES", hatch_col=3)
leader(9645.0, 5988.0, P2[0] + 12.5, P2[1],
       "A1  6 HA12 equerre  l_bd 166  |  deja FOND  |  3 conditions", 11.5, "ASSEMBLAGE-ANCRAGES")

# A3 / A6 reports
txt(7920.0, 4688.0, "A3  R3 : remplissage D-36 deja METAL. Sans beton : NE PAS POSER (tau 1,40).", 11.5)
txt(7920.0, 4660.0, "A6  8 appuis maconnerie : deja MACON (coussins D-37). R-50-5 CLOSE.", 11.5)
txt(7920.0, 4632.0, "Sabots DF/PN (B-44) : V=14,89 / 5,11 kN. Type NON catalogué (DOC-09) — non invente.", 11.5)
txt(7920.0, 4604.0, "Harnais de serrage INTERDIT sur bois sec (B-45). Rondelles larges obligatoires.", 11.5)

# --- PANNEAU DROIT ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "ASSEMBLAGE-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "ASSEMBLAGE-AXES")
txt(rx0 + 20.0, 6462.0,
    "B-60 Ind. A  |  ASSEMBLAGE EXE  |  A1-A6  |  NE PAS EXECUTER SANS EXE COTE ET VISA",
    13.0, "ASSEMBLAGE-AXES")

# 1. Détail A2
txt(rx0 + 25.0, 6378.0, "1. A2 — MOISAGE R1  —  10 M16 8.8 / face  —  cotes mm  —  ech. 1/10", 13.0, "ASSEMBLAGE-DETAILS")
K = 2.0
cx, cy = rx0 + 280.0, 6120.0
# bois 200 x 150
rect(cx, cy - 7.5 * K, cx + 20 * K, cy + 7.5 * K, "ASSEMBLAGE-EXISTANT", hatch_col=8)
# UPE gauches / droits schématiques
rect(cx - 8 * K, cy - 10 * K, cx, cy + 10 * K, "ASSEMBLAGE-BOULONS")
rect(cx + 20 * K, cy - 10 * K, cx + 28 * K, cy + 10 * K, "ASSEMBLAGE-BOULONS")
# 2 boulons
msp.add_circle((cx + 10 * K, cy - 4.5 * K), 1.6, dxfattribs={"layer": "ASSEMBLAGE-BOULONS"})
msp.add_circle((cx + 10 * K, cy + 4.5 * K), 1.6, dxfattribs={"layer": "ASSEMBLAGE-BOULONS"})
txt(cx + 32 * K, cy + 28, "2 x UPE 200  +  bois 200 x 150", 11.0, "ASSEMBLAGE-BOULONS")
txt(cx + 32 * K, cy + 8, "10 M16 8.8 / face  =  5 rangées x 2", 11.0)
txt(cx + 32 * K, cy - 12, "e1 = 700 mm  >>  112   |  e2 = 90 mm  >  64", 11.0)
txt(cx + 32 * K, cy - 32, "F_v,Rd bois 11,19 kN  |  acier 120,6 kN  —  BOIS gouverne", 11.0)
txt(cx + 32 * K, cy - 52, "Capacite 111,9 kN  /  V_Ed 77,4  =  0,691", 11.0)
txt(cx + 32 * K, cy - 72, "Maintien R-45-2 ASSURE par le meme boulonnage.", 11.0)
txt(cx + 4 * K, cy - 14 * K, "150 mm", 11.0, "ASSEMBLAGE-COTATION" if False else "ASSEMBLAGE-DETAILS")

# 2. Tableau
txt(rx0 + 25.0, 5855.0, "2. SIX ASSEMBLAGES  —  report B-50  —  rien recalcule", 13.0, "ASSEMBLAGE-DETAILS")
rect(rx0 + 18.0, 5488.0, rx1 - 18.0, 5840.0, "ASSEMBLAGE-DETAILS")
tab = [
    "A1  6 HA12 P2/SF1     l_bd 166 <= 200   OK sous 3 cond.   deja FOND   R-50-1 CLOSE",
    "A2  10 M16 8.8 / face V_Ed 77,4 kN      taux 0,691        CE PLAN     bois gouverne",
    "A3  R3 torsion        tau 1,40          D-36 OBLIGATOIRE  deja METAL  R-50-2 CLOSE",
    "A4  Stab1 2 M12/file  F<=5,8 kN         NON CHIFFRE       CE PLAN     R-50-3 OUVERTE",
    "A5  platine 200x200   4 M16 constructif sigma 0,118       CE PLAN     R-50-4 ouverte",
    "A6  8 appuis macon.   23 a 77 kN        deja MACON        D-37        R-50-5 CLOSE",
    "Sabots DF/PN : efforts B-44. Type NON catalogué (DOC-09) — aucune fiche inventee.",
]
for k, line in enumerate(tab):
    txt(rx0 + 28.0, 5810.0 - k * 42.0, line, 10.8, "ASSEMBLAGE-DETAILS")

# 3. Clauses
rect(rx0 + 18.0, 5088.0, rx1 - 18.0, 5460.0, "ASSEMBLAGE-AXES")
d34 = [
    "D-34 — MAÇONNERIE (mot pour mot, plan ET note) : f_k = 1,5 MPa · f_vk0 = 0,15 MPa.",
    "Essais hors mission. Si non concluants : reprise d'étude chiffrée.",
    "D-26 : AUCUNE vérif. sismique.  D-28 : AUCUN joint (platines d'about à 20 mm du nu).",
    "D-29 : aucun effort horizontal aux platines P1. 4 M16 = minimum constructif (R-50-4).",
    "A4 : 2 M12, e>=100, bords >=150, resine p>=80, JAMAIS en alveole. Butée hourdis.",
    "Capacité A4 NON écrite. Essai d'arrachement 1 file / 4 avant généralisation.",
]
for k, line in enumerate(d34):
    txt(rx0 + 32.0, 5428.0 - k * 50.0, line, 11.0,
        "ASSEMBLAGE-AXES" if k == 0 else "ASSEMBLAGE-HABILLAGE-TEXTE")

# 4. Nomenclature
txt(rx0 + 25.0, 5045.0, "3. NOMENCLATURE GRAPHIQUE (façonnage -> B-62)", 13.0, "ASSEMBLAGE-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 5030.0, "ASSEMBLAGE-NOMENCLATURE")
nom_l = [
    "Boulon M16 8.8 + ecrou + 2 rondelles LARGES   20 u   moisage R1 (10 / face)",
    "Tige M16 8.8 scellement chimique               8 u   pied P1 (4 / poteau)",
    "Tige M12 scellement chimique                   8 u   Stab1 (2 / file) — A4 NON chiffre",
    "Platine 200 x 200 x 15 S275                    2 u   pied P1-N / P1-S",
    "Hors nomencl. : A1 (FOND) · D-36 (METAL) · coussins (MACON) · sabots DF (DOC-09).",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 28.0, 4990.0 - k * 90.0, line, 11.2, "ASSEMBLAGE-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "ASSEMBLAGE-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "ASSEMBLAGE-AXES")
txt(rx0 + 25.0, 4412.0, "B-60 ASSEMBLAGE EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D · amont B-50 A", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "ASSEMBLAGE-AXES")
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
    if lay.startswith("ASSEMBLAGE-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
nass = sum(n for l, n in cnt.items() if l.startswith("ASSEMBLAGE-"))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  ASSEMBLAGE-* = %d  ·  calque 0 ajouts = %d  ·  manquants : %s" % (
    nass, cnt.get("0", 0), manquants or "aucun"))

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
    "CROISSY-FLORA — B-60 Ind. A — ASSEMBLAGE EXE — A1 à A6\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D · B-50 A)",
    fontsize=11.0, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "ASSEMBLAGE", "indice": "A", "mode": "PARTIEL-DECLARE",
    "A2_boulons": 20, "A5_platines": 2, "A4_chiffre": False,
    "R50_3": "ouverte",
    "purge": n_del, "blocs": n_blk, "audit": len(audit.errors),
    "n_ASSEMBLAGE": nass, "calques_manquants": manquants,
    "octets": os.path.getsize(chemin),
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_assemblage.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_assemblage.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("Journal : %s" % os.path.join(OUT, "b60_assemblage.txt"))
