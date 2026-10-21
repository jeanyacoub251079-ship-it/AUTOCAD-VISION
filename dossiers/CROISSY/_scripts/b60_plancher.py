#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PLANS D'EXÉCUTION — type PLANCHER — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Fond B-32 Ind. D (report, jamais redessin). Note B-43 Ind. B.
Zone D : dallage BA 13 cm ST25C, joints de RETRAIT 4,50 m, désolidarisation 20 mm.
D-35 recharge 15 cm sur 100 %. D-28 AUCUN joint de dilatation.
Zones A/B = existant (pas un coffrage neuf). Zone C = E-07 / PA-03 hors planche.
Purge des blocs DXF non référencés (viewer JS) — géométrie B-32 inchangée.
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
BASE = os.path.join(PLANS, "FLORA_B60_PLANCHER_EXE_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


def purge_unused_blocks(doc):
    """Retire les blocs ACAD non référencés (454 → ~11). Géométrie modelspace inchangée."""
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
log("B-60 — PLANS D'EXÉCUTION — type PLANCHER — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (B-43 B · D-35 · D-19 non levé · STR-03 absent)")
log("=" * 78)

titre("[0] ENTRÉES — ÉTAPE 1")
log("  Note amont     : B-43 Ind. B — dallage CONFORME, solives A 0,619, zone B → B-45, E-07 impossible")
log("  Vue nettoyée   : B-32 Ind. D  — %s (%d o)" % (SRC, os.path.getsize(SRC)))
log("  Calage         : B-30")
log("  Cloisons/isol. : 0 — D-25")
log("  Dalle BA 20 cm : ÉCARTÉE (décision ferme)")
log("  Hors type      : FOND (livré) · VERT (livré) · METAL · MACON · LINTEAU · CHARPENTE")

titre("[1] HYPOTHÈSES ET CLAUSES OPPOSABLES")
log("  D-28 : AUCUN JOINT DE DILATATION. Joints de RETRAIT ≠ dilatation (NF DTU 13.3).")
log("  D-35 : recharge 15 cm sur le DALLAGE à 100 %, jamais sur planchers A et B.")
log("  D-09 : dallage coulé À MÊME les semelles, désolidarisé, JAMAIS sur leur débord.")
log("  D-26 : AUCUNE VÉRIFICATION SISMIQUE.")
log("  c_nom = 30 mm (H-23) — le dallage n'est PAS une fondation (50 mm).")
log("  Termites : PRESCRITES D1 § 01.2.1.9.2 — sous dallage, avec polyane et géotextile.")
log("  E-07 / PA-03 / R-43-1 : plancher haut NON sondé — hors cette planche.")
log("  Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO).")
log("  H-06 : emprise 111,15 m² = B-43 / B-21 — NON remesurée.")

titre("[2] ZONES (B-43 — rien recalculé)")
log("  D  dallage BA 13 cm ST25C   111,15 m²   p_ELU 14,21 kN/m²   portance 2,9 %   EXE ce plan")
log("  A  solives 8×18 e500 C18    existant    flexion 0,619        EXISTANT — pas un coffrage neuf")
log("  B  IPE 160 e720 + IPE 330   existant    7,28 kN/m            RENVOI B-45 / B-60 METAL")
log("  C  plancher haut            E-07        incalculable         PA-03 — hors planche (R+1)")

titre("[3] DALLAGE — DISPOSITIONS D'EXÉCUTION")
log("  Épaisseur     : 130 mm C25/30")
log("  Treillis      : ST25C Ø7 e150 = 257 mm²/m ≥ As,min 122  — PARTIE HAUTE, 40 mm sous nu sup.")
log("  Joints retrait: sciés e ≤ 4 500 mm, profondeur 43 mm (1/3 h), < 24 h, treillis NON coupé")
log("  Panneaux      : ≥ 6, ≤ 20,25 m²")
log("  Désolid.      : polystyrène 20 mm + mastic — périmètre ET P2/P3/J1/SF1/murs")
log("  Film          : polyane 200 µm remonté 100 mm")
log("  Fond de forme : GNT 40 cm")
log("  Recharge      : 150 mm sur 100 % (D-35)")
log("  Compactage    : INTERDIT sur débord de semelle")

doc = ezdxf.readfile(SRC)
n_del, n_blk = purge_unused_blocks(doc)
log("  purge blocs non référencés : −%d  → %d blocs restants (géométrie B-32 inchangée)" % (n_del, n_blk))

for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
    if lname in doc.layers:
        doc.layers.get(lname).color = 8 if lname == "010_mur" else 9

LAYERS = (
    ("PLANCHER-AXES", 1), ("PLANCHER-DALLAGE", 8), ("PLANCHER-JOINTS", 6),
    ("PLANCHER-DESOLID", 30), ("PLANCHER-ACIER", 3), ("PLANCHER-COTATION", 8),
    ("PLANCHER-EXISTANT", 8), ("PLANCHER-DETAILS", 4),
    ("PLANCHER-NOMENCLATURE", 7), ("PLANCHER-HABILLAGE-TEXTE", 7),
    ("PLANCHER-CARTOUCHE", 7), ("PLANCHER-HYP", 6),
)
for nom, coul in LAYERS:
    if nom not in doc.layers:
        doc.layers.add(nom, color=coul)
msp = doc.modelspace()


def txt(x, y, t, ht=12.0, layer="PLANCHER-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def rect(x0, y0, x1, y1, layer="PLANCHER-DALLAGE", hatch_col=None):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})
    if hatch_col is not None:
        hh = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        hh.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def leader(tx, ty, px, py, t, ht=12.5, layer="PLANCHER-HABILLAGE-TEXTE"):
    msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + len(t) * ht * 0.55, ty - 3.0)],
                       dxfattribs={"layer": layer})
    txt(tx, ty, t, ht=ht, layer=layer)


def cote_h(x1, x2, y, texte, layer="PLANCHER-COTATION"):
    msp.add_line((x1, y), (x2, y), dxfattribs={"layer": layer})
    for x in (x1, x2):
        msp.add_line((x, y - 8), (x, y + 8), dxfattribs={"layer": layer})
    txt((x1 + x2) / 2.0 - len(texte) * 3.5, y + 6, texte, 11.0, layer)


def cote_v(y1, y2, x, texte, layer="PLANCHER-COTATION"):
    msp.add_line((x, y1), (x, y2), dxfattribs={"layer": layer})
    for y in (y1, y2):
        msp.add_line((x - 8, y), (x + 8, y), dxfattribs={"layer": layer})
    txt(x + 10, (y1 + y2) / 2.0 - 5, texte, 11.0, layer)


# --- GAUCHE : implantation sur B-32 ---
for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
    msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "PLANCHER-AXES"})
    msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "PLANCHER-AXES"})
    txt(xv - 8.0, 6484.0, code, 18.0, "PLANCHER-AXES")
for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
    msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "PLANCHER-AXES"})
    msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "PLANCHER-AXES"})
    txt(8380.0, yv - 8.0, code, 18.0, "PLANCHER-AXES")

# Emprise dallage : intérieur des murs B-32 (report, pas un nouveau contour).
# Surface contractuelle 111,15 m² (B-43) — NON remesurée (H-06).
D0, D1 = 8575.0, 9505.0
E0, E1 = 4485.0, 6275.0
hh = msp.add_hatch(color=8, dxfattribs={"layer": "PLANCHER-DALLAGE"})
hh.set_pattern_fill("ANSI31", scale=12.0)
hh.paths.add_polyline_path([(D0, E0), (D1, E0), (D1, E1), (D0, E1)], is_closed=True)
msp.add_lwpolyline([(D0, E0), (D1, E0), (D1, E1), (D0, E1), (D0, E0)],
                   dxfattribs={"layer": "PLANCHER-DALLAGE"})

# Joints de RETRAIT e ≤ 4,50 m (450 cm DXF)
joint_x = [D0 + 450.0, D0 + 900.0]          # 9025, 9475
joint_y = [E0 + 450.0, E0 + 900.0, E0 + 1350.0, E0 + 1800.0]
for xj in joint_x:
    if D0 < xj < D1:
        msp.add_line((xj, E0), (xj, E1), dxfattribs={"layer": "PLANCHER-JOINTS"})
        txt(xj + 6, E1 - 40, "JR e<=4500", 10.0, "PLANCHER-JOINTS")
for yj in joint_y:
    if E0 < yj < E1:
        msp.add_line((D0, yj), (D1, yj), dxfattribs={"layer": "PLANCHER-JOINTS"})

txt(8600.0, 6200.0, "ZONE D — DALLAGE BA 130 mm C25/30 + ST25C  (emprise 111,15 m2 B-43, non remesuree)",
    13.0, "PLANCHER-DALLAGE")
txt(8600.0, 6170.0, "Joints de RETRAIT scies e<=4500 mm  |  profondeur 43 mm  |  treillis CONTINU  |  D-28 : PAS de dilatation",
    11.5, "PLANCHER-JOINTS")
txt(8600.0, 6140.0, "Recharge 150 mm sur 100 % (D-35)  |  polyane 200 um  |  GNT 40 cm  |  termites D1 § 01.2.1.9.2",
    11.5, "PLANCHER-DALLAGE")

# Désolidarisation autour P2 / P3 / J1
p2x, p2y = 9535.0, 5929.2
p3x, p3y = 9408.6, 5489.1
j1x, j1y = 8977.5, 5452.1
for cx, cy, dx, dy, lab in [
    (p2x, p2y, 14.5, 9.5, "desolid. 20 mm P2/SF1"),
    (p3x, p3y, 27.0, 22.0, "desolid. 20 mm P3"),
    (j1x, j1y, 14.0, 27.0, "desolid. 20 mm J1"),
]:
    msp.add_lwpolyline(
        [(cx - dx, cy - dy), (cx + dx, cy - dy), (cx + dx, cy + dy), (cx - dx, cy + dy), (cx - dx, cy - dy)],
        dxfattribs={"layer": "PLANCHER-DESOLID"})
leader(9645.0, cy + 20.0, cx + dx, cy, lab, 11.5, "PLANCHER-DESOLID")

# Périmètre désolidarisation (offset 2 cm à l'intérieur du contour)
off = 2.0
msp.add_lwpolyline(
    [(D0 + off, E0 + off), (D1 - off, E0 + off), (D1 - off, E1 - off), (D0 + off, E1 - off), (D0 + off, E0 + off)],
    dxfattribs={"layer": "PLANCHER-DESOLID"})
txt(8600.0, 4510.0, "Desolidarisation perimetrique polystyrene 20 mm + mastic (toute hauteur du dallage)",
    11.0, "PLANCHER-DESOLID")

# Zones A / B — EXISTANT, pas un coffrage neuf
txt(7960.0, 5750.0, "ZONE A (Est) : solives 8x18 e500 C18 EXISTANTES", 12.0, "PLANCHER-EXISTANT")
txt(7960.0, 5720.0, "flexion 0,619  |  PAS un ouvrage neuf GO  |  D3 p.10", 11.0, "PLANCHER-EXISTANT")
txt(7960.0, 5688.0, "ZONE B (Ouest) : IPE 160 e720 + IPE 330 EXISTANTS", 12.0, "PLANCHER-EXISTANT")
txt(7960.0, 5658.0, "7,28 kN/m  |  RENVOI B-45 / B-60 METAL  |  D3 p.11-12", 11.0, "PLANCHER-EXISTANT")
txt(7960.0, 4688.0, "ZONE C : plancher haut E-07 NON SONDE — PA-03 / R-43-1 — hors cette planche (vue R+1).", 11.5, "PLANCHER-HYP")
txt(7960.0, 4660.0, "Dalle BA 20 cm ECARTEE. Dallage = 13 cm. Un plan = un type (FOND/VERT deja livrés).", 11.5)

# --- DROITE ---
rx0, rx1 = 10260.0, 12020.0
rect(rx0, 4340.0, rx1, 6520.0, "PLANCHER-CARTOUCHE")
rect(rx0, 6425.0, rx1, 6520.0, "PLANCHER-AXES")
txt(rx0 + 20.0, 6462.0,
    "B-60 Ind. A  |  PLANCHER EXE  |  DALLAGE SUR RDC BAS  |  NE PAS EXECUTER SANS EXE COTE ET VISA",
    14.0, "PLANCHER-AXES")

K = 2.0
txt(rx0 + 25.0, 6375.0,
    "1. COUPE DU COMPLEXE — ech. 1/10  —  cotes mm  —  D-09 / D-35 / DTU 13.3",
    13.0, "PLANCHER-DETAILS")

# Coupe complexe (unités DXF = cm ; K agrandit)
cx, cy = rx0 + 220.0, 5480.0
# fond de forme 400 mm = 40 cm * K
h_ff, h_da, h_re, h_rv = 40.0 * K, 13.0 * K, 15.0 * K, 2.0 * K
w = 90.0 * K
y = cy
rect(cx, y, cx + w, y + h_ff, "PLANCHER-DETAILS")  # GNT
txt(cx + w + 24, y + h_ff * 0.35, "GNT 400 mm (D2 f.03)", 12.0)
y += h_ff
msp.add_line((cx, y + 1), (cx + w, y + 1), dxfattribs={"layer": "PLANCHER-ACIER"})
txt(cx + w + 24, y + 6, "Polyane 200 um + termites D1 § 01.2.1.9.2", 11.5)
y += 4.0
rect(cx, y, cx + w, y + h_da, "PLANCHER-DALLAGE", hatch_col=8)
ty = y + h_da - 4.0 * K
msp.add_line((cx + 4, ty), (cx + w - 4, ty), dxfattribs={"layer": "PLANCHER-ACIER"})
for i in range(8):
    msp.add_line((cx + 8 + i * 10, ty - 3), (cx + 14 + i * 10, ty + 3), dxfattribs={"layer": "PLANCHER-ACIER"})
txt(cx + w + 24, y + h_da * 0.45, "Dallage 130 mm C25/30 + ST25C partie haute", 12.0)
txt(cx + w + 24, y + 4, "c_nom 30 mm  |  257 >= 122 mm2/m", 11.0)
y += h_da
rect(cx, y, cx + w, y + h_re, "PLANCHER-HYP")
txt(cx + w + 24, y + h_re * 0.35, "Recharge 150 mm — 100 % (D-35)", 12.0)
y += h_re
rect(cx, y, cx + w, y + h_rv, "PLANCHER-EXISTANT")
txt(cx + w + 24, y + 1, "Revetement 20 mm (hors lot GO)", 11.0)
cote_v(cy, cy + h_ff, cx - 18, "400")
cote_v(cy + h_ff + 2, cy + h_ff + 2 + h_da, cx - 18, "130")
cote_v(cy + h_ff + 2 + h_da, cy + h_ff + 2 + h_da + h_re, cx - 18, "150")
txt(cx - 8, cy - 22, "0,000 RELATIF (PB RDC — D-21)  |  arase inf. dallage = nu sup. fond de forme", 11.0, "PLANCHER-AXES")

# Joint + désolid
txt(rx0 + 25.0, 5320.0, "2. JOINT DE RETRAIT SCIE + DESOLIDARISATION  —  cotes mm", 13.0, "PLANCHER-DETAILS")
jx, jy = rx0 + 220.0, 5055.0
rect(jx, jy, jx + 160, jy + 26, "PLANCHER-DALLAGE")
msp.add_lwpolyline([(jx + 80, jy + 26), (jx + 74, jy + 17), (jx + 86, jy + 17), (jx + 80, jy + 26)],
                   dxfattribs={"layer": "PLANCHER-JOINTS"})
msp.add_line((jx + 8, jy + 18), (jx + 152, jy + 18), dxfattribs={"layer": "PLANCHER-ACIER"})
txt(jx + 180, jy + 18, "Saignee 43 mm (1/3 h)  |  e <= 4500 mm  |  ouverture < 24 h  |  treillis NON coupe", 11.0, "PLANCHER-JOINTS")
txt(jx + 180, jy + 0, "D-28 : ceci N'EST PAS un joint de dilatation. Aucun joint de dilatation dans le batiment.", 11.0)

# désolid semelle
sx, sy = rx0 + 220.0, 4900.0
rect(sx, sy, sx + 70, sy + 20, "PLANCHER-DETAILS")          # semelle
rect(sx + 78, sy + 8, sx + 200, sy + 34, "PLANCHER-DALLAGE")  # dallage
msp.add_line((sx + 76, sy + 8), (sx + 76, sy + 34), dxfattribs={"layer": "PLANCHER-DESOLID"})
txt(sx + 220, sy + 22, "Polystyrene 20 mm toute hauteur + mastic  |  treillis arrete a 20 mm du joint", 11.0, "PLANCHER-DESOLID")
txt(sx + 220, sy + 4, "Semelle/poteau : dallage A MEME, JAMAIS sur le debord (D-09). Compactage interdit.", 11.0)

rect(rx0 + 18.0, 4648.0, rx1 - 18.0, 4868.0, "PLANCHER-AXES")
notes = [
    "OPPOSABLE : D-09 · D-28 · D-35 · D-26 · termites D1 § 01.2.1.9.2 · c_nom 30 mm · ST25C partie haute.",
    "Portance 14,2 kPa / 490 kPa = 2,9 % — NON gouvernante. Gouverne = retrait + desolidarisation.",
    "Trémies : STR-03 absent — treillis CONTINU ; toute trémie future encadrée 2 HA8 + chapeaux (B-34).",
    "Zone A existante (0,619) · Zone B → B-45 · Zone C E-07 PA-03 HORS PLANCHE. Dalle 20 cm ECARTEE.",
]
for k, line in enumerate(notes):
    txt(rx0 + 32.0, 4838.0 - k * 42.0, line, 11.0,
        "PLANCHER-AXES" if k == 0 else "PLANCHER-HABILLAGE-TEXTE")

txt(rx0 + 25.0, 4610.0, "3. NOMENCLATURE GRAPHIQUE (faconnage -> B-62)", 13.0, "PLANCHER-NOMENCLATURE")
rect(rx0 + 18.0, 4488.0, rx1 - 18.0, 4598.0, "PLANCHER-NOMENCLATURE")
nom_l = [
    "Dallage  130 mm C25/30  111,15 m2  |  ST25C Ø7 e150  257 mm2/m  |  joints scies e<=4500  |  desolid. 20 mm",
    "GNT 400 mm  |  polyane 200 um  |  recharge 150 mm (D-35)  |  termites CCTP  |  A/B existant hors nomencl. neuve",
]
for k, line in enumerate(nom_l):
    txt(rx0 + 32.0, 4568.0 - k * 40.0, line, 11.2, "PLANCHER-NOMENCLATURE")

rect(rx0, 4340.0, rx1, 4475.0, "PLANCHER-CARTOUCHE")
txt(rx0 + 25.0, 4445.0, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 16.0, "PLANCHER-AXES")
txt(rx0 + 25.0, 4412.0, "B-60 PLANCHER EXE  ·  Ind. A · 21/10/2026 · PARTIEL-DECLARE · fond B-32 D · amont B-43 B", 12.0)
txt(rx0 + 25.0, 4378.0, "NE PAS EXECUTER SANS EXE COTE ET VISA", 18.0, "PLANCHER-AXES")
txt(rx0 + 25.0, 4352.0, "Protection au feu : ADEQUATE A PREVOIR (hors lot GO)  ·  CARNAC v3.0  ·  cotes mm  ·  DXF cm", 11.0)

chemin = BASE + ".dxf"
doc.saveas(chemin)
audit = doc.audit()
log("")
log("  écrit : %s (%d o) — audit %d erreur(s) — blocs %d" % (
    chemin, os.path.getsize(chemin), len(audit.errors), len(list(doc.blocks))))

doc2 = ezdxf.readfile(chemin)
cnt = Counter()
for e in doc2.modelspace():
    cnt[e.dxf.layer] += 1
titre("[4] TEST DE RELECTURE DXF (V13)")
log("  calque                          n")
for lay, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
    if lay.startswith("PLANCHER-") or lay == "0":
        log("  %-28s %6d" % (lay, n))
npl = sum(n for l, n in cnt.items() if l.startswith("PLANCHER-"))
manquants = [l for l, _ in LAYERS if l not in doc2.layers]
log("  PLANCHER-* total = %d  ·  calque 0 ajouts = %d  ·  blocs = %d" % (
    npl, cnt.get("0", 0), len(list(doc2.blocks))))
log("  calques attendus : %d  · manquants : %s" % (len(LAYERS), manquants or "aucun"))

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
    "CROISSY-FLORA — B-60 Ind. A — PLANCHER EXE — DALLAGE IMPLANTÉ SUR RDC BAS\n"
    "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond B-32 Ind. D · joints de RETRAIT ≠ dilatation)",
    fontsize=11.0, fontweight="bold", pad=8,
)
fig.savefig(BASE + ".png", dpi=180, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

res = {
    "type": "PLANCHER", "indice": "A", "mode": "PARTIEL-DECLARE",
    "dallage_mm": 130, "treillis": "ST25C", "joints_mm": 4500,
    "D28": "aucun joint de dilatation", "D35": "recharge 150 mm 100%",
    "emprise_m2": 111.15, "purge_blocs": n_del, "blocs_restants": n_blk,
    "audit": len(audit.errors), "n_PLANCHER": npl,
    "calques_manquants": manquants,
    "octets": os.path.getsize(chemin),
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b60_plancher.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b60_plancher.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b60_plancher.txt"),
                             os.path.getsize(os.path.join(OUT, "b60_plancher.txt"))))
