#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type METAL — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D (report, jamais redessin). Note B-45 Ind. A + D-36.
Profilés F2/F3/F4/R1/R2/P1/Stab1 implantés (positions B-20, millimètre).
Remplissage C25/30 des UPE 200 de R3 (D-36) — condition de pose.
F1a/b/c = LINTEAU (livré). Coussins D-37 = MACON (livré).
Assemblages (boulons, platines, scellements) → B-60 ASSEMBLAGE.
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
BASE = os.path.join(PLANS, "FLORA_B60_METAL_EXE_IndA")
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
log("B-60 — PLANS D'EXÉCUTION — type METAL — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-45 A · D-36 · assemblages → ASSEMBLAGE · feu hors lot)")
log("=" * 78)

titre("[0] ENTRÉES")
log("  Note amont : B-45 Ind. A — 11 barres classe 1, toutes conformes ELU/ELS")
log("  Décision   : D-36 (21/10) — remplissage C25/30 des UPE 200 de R3 ACCEPTÉ")
log("  Positions  : B-20 Ind. B — millimètre, aucune position inventée")
log("  Vue        : B-32 Ind. D")
log("  Hors type  : F1a/b/c (LINTEAU livré) · coussins D-37 (MACON livré)")
log("  Hors type  : boulons/platines/scellements (B-50 → B-60 ASSEMBLAGE)")

titre("[1] CLAUSES")
log("  D-36 : remplissage C25/30 entre les ailes des UPE 200 de R3, toute la longueur.")
log("         Sans ce remplissage, R3-N/S NON CONFORME (B-50 A3, tau=1,40) — NE PAS POSER.")
log("  D-34 : f_k=1,5 MPa · f_vk0=0,15 MPa · essais hors mission — PLAN ET NOTE.")
log("  D-26 : AUCUNE vérif. sismique. D-28 : AUCUN joint de dilatation.")
log("  D-37 : coussins R1/F2/F3 = MACON (livré), PAS ce plan.")
log("  S275 contractuel (MAT-05f, D2 p. 1). Galva ISO 1461 70 um (B-45 §10).")
log("  F3 : AUCUNE CHARGE AJOUTEE (R-45-1, fleche 0,971 de L/300).")
log("  Protection au feu : ADEQUATE A PREVOIR (hors lot GO) — NON dimensionnee.")

# Positions B-20 Ind. B (cm DXF). Largeurs = B-20 (report).
# ref, x0, y0, x1, y1, w_cm, profil, L, note
POUTRES = [
    ("F2",   8647.4, 4954.1, 8972.5, 4954.1, 20.0, "HEB 200",  "2,85 m", "V_Ed 62,4  M 0,252  w 0,237"),
    ("F3",   8547.5, 5311.6, 8972.5, 5311.6, 16.0, "HEB 160",  "3,85 m", "V_Ed 61,6  M 0,609  w 0,971  R-45-1"),
    ("F4",   8875.0, 4458.6, 8875.0, 4946.6, 15.0, "IPE 200",  "4,88 m", "V_Ed 11,5  M 0,231  w 0,306"),
    ("R1",   8547.5, 5488.7, 8969.8, 5488.7, 26.0, "2x UPE 200","3,85 m", "V_Ed 77,4  M 0,605  LT 0,880  R-45-2"),
    ("R2-N", 8570.5, 5709.1, 8952.5, 5709.1, 16.0, "HEB 160",  "3,82 m", "V_Ed 46,2  M 0,453  w 0,835"),
    ("R2-S", 8570.5, 5133.1, 8952.5, 5133.1, 16.0, "HEB 160",  "3,82 m", "V_Ed 35,9  M 0,352  w 0,650"),
]
# R3 : déjà LINTEAU ; report + calque remplissage D-36
R3 = [
    ("R3-N", 8570.5, 5584.2, 8570.5, 5834.1, 10.0, "UPE 200+B", "1,55 m", "D-36  Mt 1,85  flech. 0,291"),
    ("R3-S", 8570.5, 5007.9, 8570.5, 5258.0, 10.0, "UPE 200+B", "1,55 m", "D-36  Mt 1,85  flech. 0,291"),
]
P1 = [
    ("P1-N", 9540.5, 4904.4, 14.0, "SHS 140x140x6,3", "N_Ed 100,3 kN  flamb. 0,123"),
    ("P1-S", 9540.5, 4778.4, 14.0, "SHS 140x140x6,3", "N_Ed 100,3 kN  flamb. 0,123"),
]
STAB = [
    ("Stab1-NW", 9175.5, 5534.2, 9175.5, 6296.7),
    ("Stab1-NE", 9349.4, 5534.2, 9349.4, 6296.7),
    ("Stab1-SW", 9175.5, 4509.9, 9175.5, 5189.1),
    ("Stab1-SE", 9349.4, 4509.9, 9349.4, 5189.1),
]

titre("[2] IMPLANTATION (report B-20, cm DXF)")
log("  %-8s %8s %8s %8s %8s %-14s %-8s" % ("RÉP", "X0", "Y0", "X1", "Y1", "PROF", "L"))
for r in POUTRES + R3:
    log("  %-8s %8.1f %8.1f %8.1f %8.1f %-14s %-8s" % (r[0], r[1], r[2], r[3], r[4], r[6], r[7]))
for r in P1:
    log("  %-8s %8.1f %8.1f %8s %8s %-14s %s" % (r[0], r[1], r[2], "—", "—", r[4], r[5]))
log("  Stab1 : 4 files IPE 120  F<=5,8 kN/file  — scellement A4 NON calculable (DOC-09) → ASSEMBLAGE")
log("  Nuance S275. Rien n'est recalcule. F1a/b/c = LINTEAU.")

doc = ezdxf.readfile(SRC)
n_del, n_blk = purge_unused_blocks(doc)
log("  purge blocs : −%d → %d restants" % (n_del, n_blk))

for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9

LAYERS = (
    ("METAL-AXES", 1), ("METAL-PROFILES", 1), ("METAL-POTEAUX", 6),
    ("METAL-STAB", 4), ("METAL-REMPLISSAGE", 3), ("METAL-EXISTANT", 8),
    ("METAL-COTATION", 8), ("METAL-DETAILS", 4), ("METAL-NOMENCLATURE", 7),
    ("METAL-HABILLAGE-TEXTE", 7), ("METAL-CARTOUCHE", 7), ("METAL-HYP", 6),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="METAL-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="METAL-PROFILES", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.0, layer="METAL-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + max(40, len(t) * ht * 0.5), ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


def bande(x0, y0, x1, y1, w_cm, layer="METAL-PROFILES", hatch=1, double=False):
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


# Axes
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "METAL-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "METAL-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "METAL-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "METAL-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "METAL-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "METAL-AXES")

# Poutres neuves
for ref, x0, y0, x1, y1, w, prof, L, note in POUTRES:
    bande(x0, y0, x1, y1, w, "METAL-PROFILES", hatch=1, double=(ref == "R1"))
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    if ref == "F4":
        leader(7960.0, 4520.0, x0 - 8.0, (y0 + y1) / 2.0,
               "F4  IPE 200  L=4,88 m  S275  |  V_Ed 11,5 kN", 11.5, "METAL-PROFILES")
    elif ref in ("F2", "R2-S"):
        leader(7960.0, my - 6.0, x0, my,
               "%s  %s  L=%s  S275  |  %s" % (ref, prof, L, note.split("  ")[0]),
               11.5, "METAL-PROFILES")
    else:
        txt(mx - 90.0, my + 14.0, "%s  %s  L=%s  S275" % (ref, prof, L), 11.5, "METAL-PROFILES")

# R3 : report + hatch remplissage (D-36)
for ref, x0, y0, x1, y1, w, prof, L, note in R3:
    bande(x0, y0, x1, y1, w, "METAL-REMPLISSAGE", hatch=3, double=False)
    my = (y0 + y1) / 2.0
    leader(7960.0, my + 4.0, x0, my,
           "%s  UPE 200 + C25/30  L=%s  |  D-36 OBLIGATOIRE" % (ref, L),
           11.5, "METAL-REMPLISSAGE")

# P1
for ref, xc, yc, cote, prof, note in P1:
    hw = cote / 2.0
    rect(xc - hw, yc - hw, xc + hw, yc + hw, "METAL-POTEAUX", hatch_col=6)
    leader(9645.0, yc + 10.0, xc + hw, yc,
           "%s  SHS 140x6,3" % ref, 11.5, "METAL-POTEAUX")

# Stab1
for ref, x0, y0, x1, y1 in STAB:
    bande(x0, y0, x1, y1, 6.4, "METAL-STAB", hatch=4, double=False)
txt(9185.0, 6100.0, "Stab1  IPE 120  4 files  F<=5,8 kN  |  A4 DOC-09 -> ASSEMBLAGE", 11.0, "METAL-STAB")

# Hors type
txt(7960.0, 4688.0, "F1a/b/c : LINTEAU (livre) — 2x HEA 200. Hors type METAL.", 11.5)
txt(7960.0, 4660.0, "Coussins C-R1 / C-F2 / C-F3 : MACON (livre, D-37). Appuis sur S1/S2 elargis.", 11.5)
txt(7960.0, 4632.0, "Boulons R1 (10 M16) · platines · scellements Stab1 : B-60 ASSEMBLAGE (B-50).", 11.5)
txt(7960.0, 4604.0, "F3 : AUCUNE CHARGE AJOUTEE (R-45-1). IPE 330 existant : hors calcul (B-24).", 11.5)

# --- PANNEAU DROIT ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "METAL-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "METAL-AXES")
txt(rx0 + 20.0, 6462.0,
    "B-60 Ind. A  |  METAL EXE  |  PROFILES + D-36  |  NE PAS EXECUTER SANS EXE COTE ET VISA",
    13.0, "METAL-AXES")

# 1. Détail D-36
txt(rx0 + 25.0, 6378.0, "1. D-36 — REMPLISSAGE UPE 200 de R3  —  cotes mm  —  ech. 1/5", 13.0, "METAL-DETAILS")
K = 2.2
cx, cy = rx0 + 280.0, 6120.0
# UPE schématique : âme + 2 ailes, remplissage
# âme
rect(cx, cy - 20 * K, cx + 1.3 * K, cy + 20 * K, "METAL-PROFILES", hatch_col=1)
# aile inf
rect(cx, cy - 20 * K, cx + 16 * K, cy - 20 * K + 2.3 * K, "METAL-PROFILES", hatch_col=1)
# aile sup
rect(cx, cy + 20 * K - 2.3 * K, cx + 16 * K, cy + 20 * K, "METAL-PROFILES", hatch_col=1)
# béton
rect(cx + 1.3 * K, cy - 20 * K + 2.3 * K, cx + 16 * K, cy + 20 * K - 2.3 * K,
     "METAL-REMPLISSAGE", hatch_col=3)
txt(cx + 20 * K, cy + 28, "UPE 200  h=200  b=80  tw=6,5  tf=11,5", 11.0, "METAL-PROFILES")
txt(cx + 20 * K, cy + 6, "C25/30 entre ailes, TOUTE la longueur (1,55 m)", 11.0, "METAL-REMPLISSAGE")
txt(cx + 20 * K, cy - 16, "I_T ~ 10^7 mm4  (ouverte : 9,6e4)  — torsion close", 11.0)
txt(cx + 20 * K, cy - 38, "SANS ce beton : R3 NON CONFORME (tau 1,40) — NE PAS POSER", 11.0, "METAL-AXES")
txt(cx + 20 * K, cy - 60, "Forages de remplissage en semelle sup. Diam./entraxe -> B-62.", 10.5)
txt(cx + 20 * K, cy - 82, "Controle reception : beton affleurant, sans vide. R-50-2 CLOSE.", 10.5)
msp.add_line((cx, cy - 24 * K), (cx + 16 * K, cy - 24 * K), dxfattribs={"layer": "METAL-COTATION"})
txt(cx + 4 * K, cy - 28 * K, "80 mm", 11.0, "METAL-COTATION")
msp.add_line((cx - 8 * K, cy - 20 * K), (cx - 8 * K, cy + 20 * K), dxfattribs={"layer": "METAL-COTATION"})
txt(cx - 28 * K, cy - 4, "200 mm", 11.0, "METAL-COTATION")

# 2. Tableau barres
txt(rx0 + 25.0, 5855.0, "2. BARRES IMPLANTEES  —  report B-45 / B-20  —  rien recalcule", 13.0, "METAL-DETAILS")
rect(rx0 + 18.0, 5488.0, rx1 - 18.0, 5840.0, "METAL-DETAILS")
tab = [
    "F2    HEB 200     L=2,85 m  V_Ed 62,4 kN  ratio M 0,252  w 0,237   appui MACON (coussin)",
    "F3    HEB 160     L=3,85 m  V_Ed 61,6 kN  ratio M 0,609  w 0,971   R-45-1 AUCUNE CHARGE +",
    "F4    IPE 200     L=4,88 m  V_Ed 11,5 kN  ratio M 0,231  w 0,306   sous toiture basse",
    "R1    2x UPE 200  L=3,85 m  V_Ed 77,4 kN  LT 0,880  w 0,927        moisage — boulons ASSEMBLAGE",
    "R2-N  HEB 160     L=3,82 m  V_Ed 46,2 kN  ratio M 0,453  w 0,835   refend Nord",
    "R2-S  HEB 160     L=3,82 m  V_Ed 35,9 kN  ratio M 0,352  w 0,650   refend Sud",
    "P1    SHS 140x6,3 N_Ed 100,3 kN  flamb. 0,123  platine 200x200 sur SF1 (FOND)",
]
for k, line in enumerate(tab):
    txt(rx0 + 28.0, 5810.0 - k * 42.0, line, 10.8, "METAL-DETAILS")

# 3. Clauses
rect(rx0 + 18.0, 5088.0, rx1 - 18.0, 5460.0, "METAL-AXES")
d34 = [
    "D-36 — REMPLISSAGE C25/30 des UPE 200 de R3 : ACCEPTÉ. Condition de pose.",
    "D-34 — MAÇONNERIE (mot pour mot, plan ET note) : f_k = 1,5 MPa · f_vk0 = 0,15 MPa.",
    "Essais hors mission. Si non concluants : reprise d'étude chiffrée.",
    "D-26 : AUCUNE vérif. sismique.  D-28 : AUCUN joint de dilatation.",
    "D-37 (coussins) : MACON, pas ce plan.  F1a/b/c : LINTEAU, pas ce plan.",
    "S275 (MAT-05f). Galva ISO 1461 70 um. Feu : ADEQUATE A PREVOIR (hors lot GO).",
]
for k, line in enumerate(d34):
    txt(rx0 + 32.0, 5428.0 - k * 50.0, line, 11.0,
        "METAL-AXES" if k == 0 else "METAL-HABILLAGE-TEXTE")

# 4. Nomenclature
txt(rx0 + 25.0, 5045.0, "3. NOMENCLATURE GRAPHIQUE (faconnage / boulons -> B-62 / ASSEMBLAGE)", 12.5, "METAL-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 5030.0, "METAL-NOMENCLATURE")
nom_l = [
    "F2 x1 HEB 200 S275 L=2850   |  F3 x1 HEB 160 S275 L=3850   |  F4 x1 IPE 200 S275 L=4880",
    "R1 x2 UPE 200 S275 L=3850 moisage   |  R2-N/S x2 HEB 160 S275 L=3820",
    "R3-N/S x2 UPE 200 S275 L=1550 + C25/30 (D-36)   |  P1-N/S x2 SHS 140x140x6,3",
    "Stab1 x4 files IPE 120  pas 2500  F<=5,8 kN   |  scellement A4 NON chiffre (DOC-09)",
    "Hors nomencl. : F1 (LINTEAU) · coussins (MACON) · 10 M16 / platines (ASSEMBLAGE).",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 28.0, 4990.0 - k * 90.0, line, 11.2, "METAL-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "METAL-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "METAL-AXES")
txt(rx0 + 25.0, 4412.0, "B-60 METAL EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D · amont B-45 A / D-36", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "METAL-AXES")
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
    if lay.startswith("METAL-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
nmet = sum(n for l, n in cnt.items() if l.startswith("METAL-"))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  METAL-* = %d  ·  calque 0 ajouts = %d  ·  manquants : %s" % (
    nmet, cnt.get("0", 0), manquants or "aucun"))

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
    "CROISSY-FLORA — B-60 Ind. A — METAL EXE — PROFILÉS + D-36 (R3)\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D · S275)",
    fontsize=11.0, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "METAL", "indice": "A", "mode": "PARTIEL-DECLARE",
    "poutres": 6, "poteaux": 2, "stab": 4, "r3_d36": 2,
    "D36": True,
    "purge": n_del, "blocs": n_blk, "audit": len(audit.errors),
    "n_METAL": nmet, "calques_manquants": manquants,
    "octets": os.path.getsize(chemin),
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_metal.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_metal.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("Journal : %s" % os.path.join(OUT, "b60_metal.txt"))
