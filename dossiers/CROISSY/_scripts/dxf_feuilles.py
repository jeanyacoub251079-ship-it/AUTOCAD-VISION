#!/usr/bin/env python3
"""
CROISSY-FLORA — Découpage du DXF indice C en feuilles et mesure des emprises.
CARNAC v2.6 — verrou V13.

Chaque vue est dessinée à l'échelle réelle (unité = cm, $INSUNITS = 5) et posée
sur une grille de feuilles de 50 m x 35 m. Ce script isole chaque feuille,
identifie son titre et mesure l'emprise réelle des murs.
"""
import collections, os
import ezdxf
from ezdxf import bbox

DXF = "google_drive/208_FLORA_Plans_DCE_IndC.dxf"
OUT = "dossiers/CROISSY/_rendus/dxf_feuilles.txt"
CW, CH = 5000.0, 3500.0     # pas de la grille de feuilles, en cm

doc = ezdxf.readfile(DXF)
msp = doc.modelspace()

def cell(x, y):
    return (int(x // CW), int(y // CH))

# --- regroupement des entités par feuille
sheets = collections.defaultdict(list)
for e in msp:
    try:
        if e.dxftype() in ("TEXT", "MTEXT"):
            p = e.dxf.insert
        elif e.dxftype() == "DIMENSION":
            p = e.dxf.text_midpoint
        else:
            b = bbox.extents([e], fast=True)
            if not b.has_data:
                continue
            p = b.center
        sheets[cell(p.x, p.y)].append(e)
    except Exception:
        continue

lines = []
def out(s=""):
    lines.append(str(s)); print(s)

out("=" * 100)
out("DÉCOUPAGE EN FEUILLES — DXF 208_FLORA_Plans_DCE_IndC.dxf")
out("Grille de feuilles : 50 m x 35 m (5 000 x 3 500 cm) — unités du fichier : cm")
out("=" * 100)
hdr = f"{'Feuille':<10} {'Titre relevé':<34} {'Murs X':>9} {'Murs Y':>9} {'ΔX (m)':>8} {'ΔY (m)':>8} {'n':>6}"
out(hdr)
out("-" * 100)

rows = []
for (cx, cy), ents in sorted(sheets.items()):
    titles = []
    for e in ents:
        if e.dxftype() == "TEXT":
            t = " ".join(e.dxf.text.split())
            if t and len(t) > 2:
                titles.append((e.dxf.insert.y, e.dxf.layer, t))
        elif e.dxftype() == "MTEXT":
            t = " ".join(e.plain_text().split())
            if t and len(t) > 2:
                titles.append((e.dxf.insert.y, e.dxf.layer, t))
    # titre = le texte le plus haut de la feuille, hors cotes de détail
    titles.sort(key=lambda z: -z[0])
    titre = ""
    for _, lay, t in titles:
        if lay.startswith("077") or "FLORA" in t.upper() or "RDC" in t.upper() or "R+1" in t.upper():
            titre = t; break
    if not titre and titles:
        titre = titles[0][2]

    walls = [e for e in ents if e.dxf.layer in ("010_mur", "Murs porteurs selon geometre projet")]
    if walls:
        try:
            b = bbox.extents(walls, fast=True)
            dx = (b.extmax.x - b.extmin.x) / 100.0
            dy = (b.extmax.y - b.extmin.y) / 100.0
            wx, wy = b.extmin.x, b.extmin.y
        except Exception:
            dx = dy = float("nan"); wx = wy = 0
    else:
        dx = dy = float("nan"); wx = wy = 0

    out(f"{str((cx,cy)):<10} {titre[:34]:<34} {wx:>9.0f} {wy:>9.0f} {dx:>8.2f} {dy:>8.2f} {len(ents):>6}")
    rows.append(((cx, cy), titre, dx, dy, len(ents)))

out("")
out("=" * 100)
out("AXES STRUCTURELS (calque 090_repères-axes) PAR FEUILLE")
out("=" * 100)
for (cx, cy), ents in sorted(sheets.items()):
    axes = [e for e in ents if e.dxf.layer == "090_repères-axes"]
    if not axes:
        continue
    xs, ys = set(), set()
    for e in axes:
        try:
            b = bbox.extents([e], fast=True)
        except Exception:
            continue
        if not b.has_data: continue
        # un axe vertical : ΔX faible ; un axe horizontal : ΔY faible
        if (b.extmax.x - b.extmin.x) < 5:
            xs.add(round(b.extmin.x, 0))
        elif (b.extmax.y - b.extmin.y) < 5:
            ys.add(round(b.extmin.y, 0))
    out(f"Feuille {str((cx,cy)):<10} : {len(axes):>3} entités | X = {sorted(xs)} | Y = {sorted(ys)}")

out("")
out("=" * 100)
out("COTES D'ENSEMBLE — valeurs > 300 cm")
out("=" * 100)
dims = []
for e in msp:
    if e.dxftype() != "DIMENSION":
        continue
    try:
        v = e.get_measurement()
    except Exception:
        continue
    if v and v > 300:
        p = e.dxf.text_midpoint
        dims.append((v, cell(p.x, p.y), p.x, p.y))
for v, c, x, y in sorted(dims, reverse=True)[:40]:
    out(f"  {v:>9.2f} cm  ({v/100:>6.2f} m)   feuille {str(c):<10} en ({x:>7.0f},{y:>7.0f})")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"\n[journal : {OUT}]")
