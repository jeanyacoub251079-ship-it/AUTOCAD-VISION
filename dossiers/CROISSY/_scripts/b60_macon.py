#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type MACON — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D (report, jamais redessin). Note B-46 Ind. A + D-37.
Coussins w_b ≥ 300 mm sous R1, F2, F3 — PAS des linteaux.
R-46-1 / R-46-2 CLOSE (D-37). D-34 mot pour mot.
Profilés = report B-20 (exécution acier → B-60 METAL).
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
BASE = os.path.join(PLANS, "FLORA_B60_MACON_EXE_IndA")
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
log("B-60 — PLANS D'EXÉCUTION — type MACON — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-46 A · D-37 · D-34 · MAT-09..12 bloquants)")
log("=" * 78)

titre("[0] ENTRÉES")
log("  Note amont : B-46 Ind. A — 5 appuis OK, R1/F2/F3 → coussin w_b >= 300 mm")
log("  Décision   : D-37 (21/10) — coussin prescrit, R-46-1 / R-46-2 CLOSE")
log("  Positions  : B-20 Ind. B — millimètre, aucune position inventée")
log("  Vue        : B-32 Ind. D")
log("  Hors type  : F1/R3 (LINTEAU livré) · remplissage D-36 (METAL) · chaînages MAT-12 non relevés")

titre("[1] CLAUSES")
log("  D-34 : f_k=1,5 MPa · f_vk0=0,15 MPa · essais hors mission — PLAN ET NOTE.")
log("  D-37 : on prescrit le coussin w_b >= 300 mm sous R1 / F2 / F3.")
log("  Ce n'est PAS un linteau. D-26 : AUCUNE vérif. sismique. D-28 : AUCUN joint de dilatation.")
log("  Sommier centré en épaisseur (e <= t/4). Lit de mortier complet.")
log("  Compactage / injection / tirants : hors type (spécialiste).")
log("  Protection au feu : ADEQUATE A PREVOIR (hors lot GO).")
log("  MAT-09..12 bloquants : aucune maçonnerie NEUVE dimensionnée.")

titre("[2] COUSSINS (report B-20, w_b élargi à 300 mm)")
# x0,y0,x1,y1 déjà B-20 sommier ; on élargit w_b (X) à 30 cm vers l'intérieur de la travée
COUSSINS = [
    ("C-F2-O", 8647.4, 4926.0, 8677.4, 4961.5, "F2 Ouest", "62,4 kN", "S1 → 300 mm"),
    ("C-F2-E", 8942.5, 4927.0, 8972.5, 4962.6, "F2 Est", "62,4 kN", "S1 → 300 mm"),
    ("C-F3-O", 8547.5, 5293.8, 8577.5, 5329.5, "F3 Ouest", "61,6 kN", "S1 → 300 mm"),
    ("C-F3-E", 8942.5, 5293.8, 8972.5, 5329.5, "F3 Est", "61,6 kN", "S1 → 300 mm"),
    ("C-R1-O", 8547.5, 5464.6, 8577.5, 5513.7, "R1 Ouest", "77,4 kN", "S2 → 300 mm"),
    ("C-R1-E", 8942.5, 5464.1, 8972.5, 5518.1, "R1 Est", "77,4 kN", "S2 → 300 mm"),
]
log("  %-8s %-12s %-8s %s" % ("RÉP", "SOUS", "V_Ed", "GEOM"))
for r in COUSSINS:
    log("  %-8s %-12s %-8s %s" % (r[0], r[5], r[6], r[7]))
log("  N_Rdc (w_b=300, a1=0) >= 84 kN > 77,4  — verdict inconditionnel (B-46 §4).")

BEAMS = [
    ("F2", 8647.4, 4954.1, 8972.5, 4954.1, "HEB 200  L=2,85 m  → B-60 METAL"),
    ("F3", 8547.5, 5311.6, 8972.5, 5311.6, "HEB 160  L=3,85 m  → B-60 METAL"),
    ("R1", 8547.5, 5488.7, 8969.8, 5488.7, "2x UPE 200  L=3,85 m  → B-60 METAL"),
]

doc = ezdxf.readfile(SRC)
n_del, n_blk = purge_unused_blocks(doc)
log("  purge blocs : −%d → %d restants" % (n_del, n_blk))

for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9

LAYERS = (
    ("MACON-AXES", 1), ("MACON-COUSSIN", 3), ("MACON-PROFILES", 8),
    ("MACON-COTATION", 8), ("MACON-DETAILS", 4), ("MACON-NOMENCLATURE", 7),
    ("MACON-HABILLAGE-TEXTE", 7), ("MACON-CARTOUCHE", 7), ("MACON-HYP", 6),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="MACON-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="MACON-COUSSIN", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.0, layer="MACON-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + max(40, len(t) * ht * 0.5), ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "MACON-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "MACON-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "MACON-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "MACON-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "MACON-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "MACON-AXES")

# Profilés = report B-20 (hôte des coussins), exécution acier = METAL
for ref, x0, y0, x1, y1, lab in BEAMS:
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": "MACON-PROFILES"})
    txt((x0 + x1) / 2.0 - 80, y0 + 18.0, "%s  %s" % (ref, lab), 11.5, "MACON-PROFILES")

# Coussins
for rid, x0, y0, x1, y1, sous, ved, geom in COUSSINS:
    rect(x0, y0, x1, y1, "MACON-COUSSIN", hatch_col=3)
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    if "Ouest" in sous:
        leader(7960.0, my + 8.0, x0, my,
               "%s  w_b=300 mm  V_Ed %s  |  %s" % (rid, ved, sous), 11.5, "MACON-COUSSIN")
    else:
        leader(9645.0, my + 8.0, x1, my,
               "%s  w_b=300 mm  |  %s  |  C25/30 h=200" % (rid, sous), 11.5, "MACON-COUSSIN")

txt(7960.0, 4688.0, "F1 / R3 : LINTEAU (livre) — S1 200 mm suffisent, PAS de coussin D-37.", 11.5)
txt(7960.0, 4660.0, "R2-N/S / F4 : OK sans coussin (B-46). Chaînages : MAT-12 non releve — aucune maille inventee.", 11.5)
txt(7960.0, 4632.0, "Profilés F2/F3/R1 : report B-20. Execution acier + remplissage D-36 = B-60 METAL.", 11.5)

# --- DROITE ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "MACON-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "MACON-AXES")
txt(rx0 + 20.0, 6462.0,
    "B-60 Ind. A  |  MACON EXE  |  COUSSINS D-37 sous R1/F2/F3  |  NE PAS EXECUTER SANS EXE COTE ET VISA",
    13.5, "MACON-AXES")

txt(rx0 + 25.0, 6378.0, "1. COUSSIN TYPE — w_b = 300 mm  —  cotes mm  —  C25/30  —  ech. 1/10", 13.0, "MACON-DETAILS")
K = 2.5
cx, cy = rx0 + 420.0, 6050.0
# mur
rect(cx - 25 * K, cy - 40 * K, cx + 25 * K, cy + 40 * K, "MACON-HYP")
# coussin 300 x 200 vu en plan (w_b selon X du dessin de détail = horizontal)
rect(cx - 15 * K, cy - 20 * K, cx + 15 * K, cy + 20 * K, "MACON-COUSSIN", hatch_col=3)
# profilé
msp.add_lwpolyline([(cx - 8, cy - 55 * K), (cx - 8, cy + 55 * K),
                    (cx + 8, cy + 55 * K), (cx + 8, cy - 55 * K), (cx - 8, cy - 55 * K)],
                   dxfattribs={"layer": "MACON-PROFILES"})
txt(cx - 15 * K, cy + 48 * K, "Profilé (F2/F3/R1) — B-60 METAL", 11.0, "MACON-PROFILES")
txt(cx + 28 * K, cy + 10, "w_b = 300 mm MINI (D-37)", 12.5, "MACON-COUSSIN")
txt(cx + 28 * K, cy - 12, "h = 200 mm  C25/30  |  4 HA8 constructive", 11.0)
txt(cx + 28 * K, cy - 34, "Centre en epaisseur  e <= t/4  |  mortier complet", 11.0)
txt(cx + 28 * K, cy - 56, "N_Rdc (a1=0) >= 84 kN  >  V_Ed max 77,4 kN (R1)", 11.0)
# cote w_b
msp.add_line((cx - 15 * K, cy - 24 * K), (cx + 15 * K, cy - 24 * K), dxfattribs={"layer": "MACON-COTATION"})
txt(cx - 20, cy - 28 * K, "300 mm", 11.0, "MACON-COTATION")

txt(rx0 + 25.0, 5755.0, "2. LES 6 APPUIS  —  verdict inconditionnel des que w_b = 300 mm", 13.0, "MACON-DETAILS")
rect(rx0 + 18.0, 5488.0, rx1 - 18.0, 5740.0, "MACON-DETAILS")
tab = [
    "R1   2 appuis  V_Ed 77,4 kN  sommier S2 elargi  300 x ~500 x 200  |  a1* etait 0,24 m",
    "F2   2 appuis  V_Ed 62,4 kN  sommier S1 elargi  300 x ~400 x 200  |  a1* etait 0,30 m",
    "F3   2 appuis  V_Ed 61,6 kN  sommier S1 elargi  300 x ~400 x 200  |  a1* etait 0,20 m",
    "R-46-1 CLOSE (a1) · R-46-2 CLOSE (groupe unites) — D-37. Plus de dependence a a1 ni a beta.",
]
for k, line in enumerate(tab):
    txt(rx0 + 32.0, 5708.0 - k * 48.0, line, 11.2, "MACON-DETAILS")

rect(rx0 + 18.0, 5088.0, rx1 - 18.0, 5460.0, "MACON-AXES")
d34 = [
    "D-34 — MAÇONNERIE (mot pour mot, plan ET note) : f_k = 1,5 MPa · f_vk0 = 0,15 MPa.",
    "Essais hors mission. Si non concluants : reprise d'étude chiffrée.",
    "D-37 : coussin w_b >= 300 mm sous R1, F2, F3. PAS un linteau. D-26 : AUCUNE vérif. sismique.",
    "D-28 : AUCUN joint de dilatation.  D-36 (remplissage UPE R3) : B-60 METAL, pas ce plan.",
    "Aucune maçonnerie neuve dimensionnée (MAT-09..12 bloquants). Chaînages : orientation seule.",
    "Feu : ADEQUATE A PREVOIR (hors lot GO).",
]
for k, line in enumerate(d34):
    txt(rx0 + 32.0, 5428.0 - k * 50.0, line, 11.0,
        "MACON-AXES" if k == 0 else "MACON-HABILLAGE-TEXTE")

txt(rx0 + 25.0, 5045.0, "3. NOMENCLATURE GRAPHIQUE (faconnage -> B-62)", 13.0, "MACON-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 5030.0, "MACON-NOMENCLATURE")
nom_l = [
    "C-R1-O / C-R1-E   coussin BA  300 x 500 x 200  C25/30  x2  |  sous R1  |  4 HA8",
    "C-F2-O / C-F2-E   coussin BA  300 x 400 x 200  C25/30  x2  |  sous F2  |  4 HA8",
    "C-F3-O / C-F3-E   coussin BA  300 x 400 x 200  C25/30  x2  |  sous F3  |  4 HA8",
    "TOTAL  6 coussins.  w_b = 300 mm MINI  —  ne pas reduire.  Mortier complet.  e <= t/4.",
    "Hors nomencl. : F1/R3 (LINTEAU) · R2/F4 (OK sans coussin) · profilés (METAL) · D-36 (METAL).",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 32.0, 4995.0 - k * 90.0, line, 11.5, "MACON-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "MACON-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "MACON-AXES")
txt(rx0 + 25.0, 4412.0, "B-60 MACON EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D · amont B-46 A / D-37", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "MACON-AXES")
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
    if lay.startswith("MACON-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
nmac = sum(n for l, n in cnt.items() if l.startswith("MACON-"))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  MACON-* = %d  ·  calque 0 ajouts = %d  ·  manquants : %s" % (
    nmac, cnt.get("0", 0), manquants or "aucun"))

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
    "CROISSY-FLORA — B-60 Ind. A — MACON EXE — COUSSINS D-37 (R1 / F2 / F3)\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D · w_b ≥ 300 mm)",
    fontsize=11.0, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "MACON", "indice": "A", "mode": "PARTIEL-DECLARE",
    "coussins": 6, "w_b_mm": 300, "D37": True,
    "purge": n_del, "blocs": n_blk, "audit": len(audit.errors),
    "n_MACON": nmac, "calques_manquants": manquants,
    "octets": os.path.getsize(chemin),
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_macon.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_macon.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("Journal : %s" % os.path.join(OUT, "b60_macon.txt"))
