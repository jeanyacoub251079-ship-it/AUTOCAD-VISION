#!/usr/bin/env python3
"""B-20 — Plans de principe Conception GO (INTERNE-GO)
Fond B-32, ouvrages neufs et renforts implantés, repères uniques, légende, filigrane.
Génère DXF + PNG + PDF.
"""
import ezdxf
from ezdxf.math import Vec2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrow
from matplotlib.lines import Line2D
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))
B32 = "/home/user/AUTOCAD-VISION/affaires/JYCROISSY/03_PHASE_1_SOCLE/B-32_Vue_Nettoyee/SOCLE-GEOS_VUE-NETTOYEE_V1.dxf"

# ---- Lecture du fond B-32 ----
doc = ezdxf.readfile(B32)
msp = doc.modelspace()

# Collecte des entités B-32 (pour le fond)
entities_b32 = list(msp)
print(f"Entités B-32 lues : {len(entities_b32)}")

# ---- Création du DXF de principe ----
principe = ezdxf.new("R2010")
principe.units = 6  # mètres
p_msp = principe.modelspace()

# Filigrane
filigrane = p_msp.add_text("PRINCIPE — NE PAS EXÉCUTER — Indice P1", height=0.5)
filigrane.dxf.insert = (1, 1, 0)
filigrane.dxf.rotation = 0

# Légende
legend_texts = [
    "LÉGENDE — PLAN DE PRINCIPE B-20",
    "P = Poteau neuf BA",
    "Pt = Poutre métallique",
    "SI = Semelle isolée",
    "SF = Semelle filante",
    "Lt = Linteau neuf BA",
    "Dg = Dallage neuf",
    "R = Renfort de l'existant",
    "Fond : B-32 Vue Nettoyée",
]
y_leg = 15.0
for i, txt in enumerate(legend_texts):
    t = p_msp.add_text(txt, height=0.35)
    t.dxf.insert = (-0.5, y_leg - i * 0.6, 0)

# ---- Copie du fond B-32 (existant en gris) ----
for e in entities_b32:
    try:
        new_e = e.dxftype()
        if new_e == 'LINE':
            p_msp.add_line(e.dxf.start, e.dxf.end)
        elif new_e == 'CIRCLE':
            p_msp.add_circle(e.dxf.center, e.dxf.radius)
        elif new_e == 'ARC':
            p_msp.add_arc(e.dxf.center, e.dxf.radius, e.dxf.start_angle, e.dxf.end_angle)
        elif new_e == 'LWPOLYLINE':
            pts = [Vec2(p[0], p[1]) for p in e.get_points()]
            p_msp.add_lwpolyline(pts, close=e.closed)
        elif new_e == 'TEXT':
            t = p_msp.add_text(e.dxf.text, height=e.dxf.height)
            t.dxf.insert = e.dxf.insert
        elif new_e == 'INSERT':
            p_msp.add_blockref(e.dxf.name, e.dxf.insert, e.dxf.xscale, e.dxf.yscale)
    except Exception as ex:
        pass

# ---- Ouvrages neufs et renforts (couleurs) ----
# Poteaux neufs (rouge)
poteaux = [
    ("P1", (9.0, 0.0)),
    ("P2", (9.0, 6.0)),
    ("P3", (9.0, 18.0)),
]
for name, (x, y) in poteaux:
    p_msp.add_lwpolyline([Vec2(x-0.15, y-0.15), Vec2(x+0.15, y-0.15), Vec2(x+0.15, y+0.15), Vec2(x-0.15, y+0.15)], close=True)
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x+0.3, y+0.3)

# Poutres métalliques (orange)
poutres = [
    ("Pt1", (9.0, 0.0), (9.0, 6.0)),
    ("Pt2", (9.0, 6.0), (9.0, 18.0)),
]
for name, (x1, y1), (x2, y2) in poutres:
    p_msp.add_line(Vec2(x1, y1), Vec2(x2, y2))
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x1+0.3, y1-0.5)

# Semelle isolée (vert)
semelles = [
    ("SI1", (9.0, 0.0)),
    ("SI2", (9.0, 6.0)),
    ("SI3", (9.0, 18.0)),
]
for name, (x, y) in semelles:
    p_msp.add_lwpolyline([Vec2(x-0.5, y-0.5), Vec2(x+0.5, y-0.5), Vec2(x+0.5, y+0.5), Vec2(x-0.5, y+0.5)], close=True)
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x-0.8, y-0.8)

# Semelle filante (vert clair)
p_msp.add_line(Vec2(0.0, 0.0), Vec2(18.0, 0.0))
p_msp.add_text("SF1", height=0.3).dxf.insert = Vec2(0.0, -0.8)

# Linteaux (jaune)
linteaux = [
    ("Lt1", (0.0, 0.0), (3.0, 0.0)),
    ("Lt2", (15.0, 18.0), (18.0, 18.0)),
]
for name, (x1, y1), (x2, y2) in linteaux:
    p_msp.add_line(Vec2(x1, y1), Vec2(x2, y2))
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x1+0.3, y1+0.3)

# Dallage (bleu)
p_msp.add_lwpolyline([Vec2(0.0, 0.0), Vec2(18.0, 0.0), Vec2(18.0, 12.0), Vec2(0.0, 12.0)], close=True)
p_msp.add_text("Dg1", height=0.4).dxf.insert = Vec2(9.0, 6.0)

# Renforts (magenta)
renforts = [
    ("R1", (9.0, 3.0), "Moisage"),
    ("R2", (0.0, 0.0), "Sommier répartition"),
    ("R3", (9.0, 6.0), "Entretoise"),
    ("R4", (9.0, 18.0), "Contrefiche"),
]
for name, (x, y), desc in renforts:
    p_msp.add_circle(Vec2(x, y), 0.2)
    p_msp.add_text(f"{name} {desc}", height=0.25).dxf.insert = Vec2(x+0.4, y+0.4)

# Axes (gris foncé)
axes = [
    ("A", (0.0, -0.5), (0.0, 13.0)),
    ("B", (9.0, -0.5), (9.0, 13.0)),
    ("C", (18.0, -0.5), (18.0, 13.0)),
    ("1", (-0.5, 0.0), (20.0, 0.0)),
    ("2", (-0.5, 9.0), (20.0, 9.0)),
    ("3", (-0.5, 18.0), (20.0, 18.0)),
]
for name, (x1, y1), (x2, y2) in axes:
    p_msp.add_line(Vec2(x1, y1), Vec2(x2, y2))
    p_msp.add_text(name, height=0.4).dxf.insert = Vec2(x1, y1-0.4)

# Sauvegarde DXF
dxf_path = os.path.join(OUT, "B-20_Plan_Principe_P1.dxf")
principe.saveas(dxf_path)
print(f"DXF sauvegardé : {dxf_path}")

# ---- PNG via matplotlib ----
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
fig.patch.set_facecolor('white')

# Fond B-32 (existant en gris)
for e in entities_b32:
    try:
        if e.dxftype() == 'LINE':
            ax.plot([e.dxf.start.x, e.dxf.end.x], [e.dxf.start.y, e.dxf.end.y],
                    color='lightgray', linewidth=0.5, zorder=1)
        elif e.dxftype() == 'CIRCLE':
            ax.add_patch(Circle((e.dxf.center.x, e.dxf.center.y), e.dxf.radius,
                                fill=False, color='lightgray', linewidth=0.5, zorder=1))
        elif e.dxftype() == 'LWPOLYLINE':
            pts = e.get_points()
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            ax.plot(xs, ys, color='lightgray', linewidth=0.5, zorder=1)
    except Exception:
        pass

# Poteaux (rouge)
for name, (x, y) in poteaux:
    ax.add_patch(Rectangle((x-0.15, y-0.15), 0.3, 0.3, fill=False, edgecolor='red', linewidth=1.5, zorder=5))
    ax.text(x+0.3, y+0.3, name, fontsize=8, color='red', zorder=6)

# Poutres (orange)
for name, (x1, y1), (x2, y2) in poutres:
    ax.plot([x1, x2], [y1, y2], color='orange', linewidth=2, zorder=5)
    ax.text(x1+0.3, y1-0.5, name, fontsize=8, color='darkorange', zorder=6)

# Semelle isolée (vert)
for name, (x, y) in semelles:
    ax.add_patch(Rectangle((x-0.5, y-0.5), 1.0, 1.0, fill=False, edgecolor='green', linewidth=1.5, zorder=5))
    ax.text(x-0.8, y-0.8, name, fontsize=8, color='green', zorder=6)

# Semelle filante (vert clair)
ax.plot([0, 18], [0, 0], color='limegreen', linewidth=2, zorder=5)
ax.text(0, -0.8, "SF1", fontsize=8, color='limegreen', zorder=6)

# Linteaux (jaune)
for name, (x1, y1), (x2, y2) in linteaux:
    ax.plot([x1, x2], [y1, y2], color='gold', linewidth=2, zorder=5)
    ax.text(x1+0.3, y1+0.3, name, fontsize=8, color='darkgoldenrod', zorder=6)

# Dallage (bleu)
ax.add_patch(Rectangle((0, 0), 18, 12, fill=False, edgecolor='blue', linewidth=1.5, linestyle='--', zorder=5))
ax.text(9, 6, "Dg1", fontsize=10, color='blue', zorder=6)

# Renforts (magenta)
for name, (x, y), desc in renforts:
    ax.add_patch(Circle((x, y), 0.2, fill=False, edgecolor='magenta', linewidth=1.5, zorder=5))
    ax.text(x+0.4, y+0.4, f"{name} {desc}", fontsize=7, color='magenta', zorder=6)

# Axes
for name, (x1, y1), (x2, y2) in axes:
    ax.plot([x1, x2], [y1, y2], color='dimgray', linewidth=0.5, linestyle=':', zorder=2)
    ax.text(x1, y1-0.4, name, fontsize=10, color='dimgray', zorder=6)

# Filigrane
ax.text(0.5, 0.02, "PRINCIPE — NE PAS EXÉCUTER — Indice P1", transform=ax.transAxes,
        fontsize=14, color='red', alpha=0.5, ha='center', va='bottom', zorder=10)

# Légende
legend_elems = [
    plt.Line2D([0], [0], color='red', lw=2, label='Poteau neuf BA (P)'),
    plt.Line2D([0], [0], color='orange', lw=2, label='Poutre métallique (Pt)'),
    plt.Line2D([0], [0], color='green', lw=2, label='Semelle isolée (SI)'),
    plt.Line2D([0], [0], color='limegreen', lw=2, label='Semelle filante (SF)'),
    plt.Line2D([0], [0], color='gold', lw=2, label='Linteau neuf BA (Lt)'),
    plt.Line2D([0], [0], color='blue', lw=2, linestyle='--', label='Dallage neuf (Dg)'),
    plt.Line2D([0], [0], color='magenta', lw=2, label="Renfort (R)"),
    plt.Line2D([0], [0], color='lightgray', lw=0.5, label='Fond B-32 (existant)'),
]
ax.legend(handles=legend_elems, loc='upper left', fontsize=7, framealpha=0.9)

ax.set_aspect('equal')
ax.set_title("B-20 — Plan de principe Conception GO — Indice P1", fontsize=12)
ax.set_xlabel("X (m, RSU)")
ax.set_ylabel("Y (m, RSU)")
ax.grid(True, alpha=0.3)

png_path = os.path.join(OUT, "B-20_Plan_Principe_P1.png")
fig.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"PNG sauvegardé : {png_path}")

# ---- PDF ----
pdf_path = os.path.join(OUT, "B-20_Plan_Principe_P1.pdf")
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
fig.patch.set_facecolor('white')

for e in entities_b32:
    try:
        if e.dxftype() == 'LINE':
            ax.plot([e.dxf.start.x, e.dxf.end.x], [e.dxf.start.y, e.dxf.end.y],
                    color='lightgray', linewidth=0.5, zorder=1)
        elif e.dxftype() == 'CIRCLE':
            ax.add_patch(Circle((e.dxf.center.x, e.dxf.center.y), e.dxf.radius,
                                fill=False, color='lightgray', linewidth=0.5, zorder=1))
    except Exception:
        pass

for name, (x, y) in poteaux:
    ax.add_patch(Rectangle((x-0.15, y-0.15), 0.3, 0.3, fill=False, edgecolor='red', linewidth=1.5, zorder=5))
    ax.text(x+0.3, y+0.3, name, fontsize=8, color='red', zorder=6)
for name, (x1, y1), (x2, y2) in poutres:
    ax.plot([x1, x2], [y1, y2], color='orange', linewidth=2, zorder=5)
    ax.text(x1+0.3, y1-0.5, name, fontsize=8, color='darkorange', zorder=6)
for name, (x, y) in semelles:
    ax.add_patch(Rectangle((x-0.5, y-0.5), 1.0, 1.0, fill=False, edgecolor='green', linewidth=1.5, zorder=5))
    ax.text(x-0.8, y-0.8, name, fontsize=8, color='green', zorder=6)
ax.plot([0, 18], [0, 0], color='limegreen', linewidth=2, zorder=5)
ax.text(0, -0.8, "SF1", fontsize=8, color='limegreen', zorder=6)
for name, (x1, y1), (x2, y2) in linteaux:
    ax.plot([x1, x2], [y1, y2], color='gold', linewidth=2, zorder=5)
    ax.text(x1+0.3, y1+0.3, name, fontsize=8, color='darkgoldenrod', zorder=6)
ax.add_patch(Rectangle((0, 0), 18, 12, fill=False, edgecolor='blue', linewidth=1.5, linestyle='--', zorder=5))
ax.text(9, 6, "Dg1", fontsize=10, color='blue', zorder=6)
for name, (x, y), desc in renforts:
    ax.add_patch(Circle((x, y), 0.2, fill=False, edgecolor='magenta', linewidth=1.5, zorder=5))
    ax.text(x+0.4, y+0.4, f"{name} {desc}", fontsize=7, color='magenta', zorder=6)
for name, (x1, y1), (x2, y2) in axes:
    ax.plot([x1, x2], [y1, y2], color='dimgray', linewidth=0.5, linestyle=':', zorder=2)
    ax.text(x1, y1-0.4, name, fontsize=10, color='dimgray', zorder=6)
ax.text(0.5, 0.02, "PRINCIPE — NE PAS EXÉCUTER — Indice P1", transform=ax.transAxes,
        fontsize=14, color='red', alpha=0.5, ha='center', va='bottom', zorder=10)
legend_elems = [
    plt.Line2D([0], [0], color='red', lw=2, label='Poteau neuf BA (P)'),
    plt.Line2D([0], [0], color='orange', lw=2, label='Poutre métallique (Pt)'),
    plt.Line2D([0], [0], color='green', lw=2, label='Semelle isolée (SI)'),
    plt.Line2D([0], [0], color='limegreen', lw=2, label='Semelle filante (SF)'),
    plt.Line2D([0], [0], color='gold', lw=2, label='Linteau neuf BA (Lt)'),
    plt.Line2D([0], [0], color='blue', lw=2, linestyle='--', label='Dallage neuf (Dg)'),
    plt.Line2D([0], [0], color='magenta', lw=2, label="Renfort (R)"),
    plt.Line2D([0], [0], color='lightgray', lw=0.5, label='Fond B-32 (existant)'),
]
ax.legend(handles=legend_elems, loc='upper left', fontsize=7, framealpha=0.9)
ax.set_aspect('equal')
ax.set_title("B-20 — Plan de principe Conception GO — Indice P1", fontsize=12)
ax.set_xlabel("X (m, RSU)")
ax.set_ylabel("Y (m, RSU)")
ax.grid(True, alpha=0.3)
fig.savefig(pdf_path, dpi=150, bbox_inches='tight', format='pdf')
plt.close()
print(f"PDF sauvegardé : {pdf_path}")

print("\n=== B-20 Plans de principe générés ===")
print(f"DXF: {dxf_path}")
print(f"PNG: {png_path}")
print(f"PDF: {pdf_path}")
