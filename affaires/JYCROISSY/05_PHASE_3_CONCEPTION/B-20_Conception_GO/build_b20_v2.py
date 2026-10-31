#!/usr/bin/env python3
"""B-20 V2 — Plans de principe Conception GO (INTERNE-GO) — Fond PROJET (B-32 V3).
CARNAC v3.0 — ouvrages neufs et renforts implantés sur la zone PROJET de Flora.

V2 (2026-10-31) — Refait sur B-32 V3 (plan d'exécution = PROJET seul).
Trame positionnée sur la zone PROJET (X > 115,64 m) au lieu de la zone EXISTANT.
"""
import ezdxf
from ezdxf.math import Vec2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.lines import Line2D
import os, json

ROOT = "/home/user/AUTOCAD-VISION"
OUT = f"{ROOT}/affaires/JYCROISSY/05_PHASE_3_CONCEPTION/B-20_Conception_GO"
B32 = f"{ROOT}/affaires/JYCROISSY/03_PHASE_1_SOCLE/B-32_Vue_Nettoyee/SOCLE-GEOS_VUE-NETTOYEE_V3.dxf"

# ---- Lecture du fond B-32 V3 (zone PROJET) ----
doc = ezdxf.readfile(B32)
msp = doc.modelspace()
entities_b32 = list(msp)
print(f"Entités B-32 V3 lues : {len(entities_b32)}")

# ---- Extents du bâtiment PROJET (depuis le bloc Murs porteurs) ----
# Bloc « Murs porteurs selon geometre projet » à (179.86, 41.44)
# Enveloppante bâtiment : X[145.70, 156.98] Y[40.86, 60.22] (déduite du bloc)
BLD_X_MIN = 145.70
BLD_X_MAX = 156.98
BLD_Y_MIN = 40.86
BLD_Y_MAX = 60.22
BLD_W = BLD_X_MAX - BLD_X_MIN  # 11.28 m
BLD_D = BLD_Y_MAX - BLD_Y_MIN  # 19.36 m

# Trame structurelle sur zone PROJET
AX_X = [BLD_X_MIN, (BLD_X_MIN + BLD_X_MAX) / 2, BLD_X_MAX]  # A, B, C
AX_Y = [BLD_Y_MIN, (BLD_Y_MIN + BLD_Y_MAX) / 2, BLD_Y_MAX]  # 1, 2, 3

# ---- Création du DXF de principe ----
principe = ezdxf.new("R2010")
principe.units = 6
p_msp = principe.modelspace()

# Filigrane
filigrane = p_msp.add_text("PRINCIPE — NE PAS EXÉCUTER — Indice P1", height=0.5)
filigrane.dxf.insert = (BLD_X_MIN - 20, 5, 0)

# Légende
legend_texts = [
    "LÉGENDE — PLAN DE PRINCIPE B-20 V2",
    "P = Poteau neuf BA",
    "Pt = Poutre métallique",
    "SI = Semelle isolée",
    "SF = Semelle filante",
    "Lt = Linteau neuf BA",
    "Dg = Dallage neuf",
    "R = Renfort de l'existant",
    "Fond : B-32 V3 (PROJET — plan d'exécution)",
]
y_leg = BLD_Y_MAX + 5
for i, txt in enumerate(legend_texts):
    t = p_msp.add_text(txt, height=0.35)
    t.dxf.insert = (BLD_X_MIN - 20, y_leg - i * 0.6, 0)

# ---- Copie du fond B-32 V3 (PROJET en gris) ----
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
        elif new_e == 'MTEXT':
            t = p_msp.add_mtext(e.text, height=e.dxf.char_height if hasattr(e.dxf, 'char_height') else 0.3)
            t.dxf.insert = e.dxf.insert
        elif new_e == 'INSERT':
            p_msp.add_blockref(e.dxf.name, e.dxf.insert, e.dxf.xscale, e.dxf.yscale)
    except Exception:
        pass

# ---- Ouvrages neufs et renforts (positionnés sur zone PROJET) ----

# Poteaux neufs (rouge) — axe B
poteaux = [
    ("P1", (AX_X[1], AX_Y[0])),
    ("P2", (AX_X[1], AX_Y[1])),
    ("P3", (AX_X[1], AX_Y[2])),
]
for name, (x, y) in poteaux:
    p_msp.add_lwpolyline([Vec2(x-0.15, y-0.15), Vec2(x+0.15, y-0.15),
                          Vec2(x+0.15, y+0.15), Vec2(x-0.15, y+0.15)], close=True)
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x+0.3, y+0.3)

# Poutres métalliques (orange) — axe B
poutres = [
    ("Pt1", (AX_X[1], AX_Y[0]), (AX_X[1], AX_Y[1])),
    ("Pt2", (AX_X[1], AX_Y[1]), (AX_X[1], AX_Y[2])),
]
for name, (x1, y1), (x2, y2) in poutres:
    p_msp.add_line(Vec2(x1, y1), Vec2(x2, y2))
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x1+0.3, y1-0.5)

# Semelle isolée (vert)
semelles = [
    ("SI1", (AX_X[1], AX_Y[0])),
    ("SI2", (AX_X[1], AX_Y[1])),
    ("SI3", (AX_X[1], AX_Y[2])),
]
for name, (x, y) in semelles:
    p_msp.add_lwpolyline([Vec2(x-0.5, y-0.5), Vec2(x+0.5, y-0.5),
                          Vec2(x+0.5, y+0.5), Vec2(x-0.5, y+0.5)], close=True)
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x-0.8, y-0.8)

# Semelle filante (vert clair) — axe A (façade)
p_msp.add_line(Vec2(AX_X[0], AX_Y[0]), Vec2(AX_X[2], AX_Y[0]))
p_msp.add_text("SF1", height=0.3).dxf.insert = Vec2(AX_X[0], AX_Y[0]-0.8)

# Linteaux (jaune)
linteaux = [
    ("Lt1", (AX_X[0], AX_Y[0]), (AX_X[0]+3.0, AX_Y[0])),
    ("Lt2", (AX_X[2]-3.0, AX_Y[2]), (AX_X[2], AX_Y[2])),
]
for name, (x1, y1), (x2, y2) in linteaux:
    p_msp.add_line(Vec2(x1, y1), Vec2(x2, y2))
    p_msp.add_text(name, height=0.3).dxf.insert = Vec2(x1+0.3, y1+0.3)

# Dallage (bleu)
p_msp.add_lwpolyline([Vec2(AX_X[0], AX_Y[0]), Vec2(AX_X[2], AX_Y[0]),
                      Vec2(AX_X[2], AX_Y[1]), Vec2(AX_X[0], AX_Y[1])], close=True)
p_msp.add_text("Dg1", height=0.4).dxf.insert = Vec2((AX_X[0]+AX_X[2])/2, (AX_Y[0]+AX_Y[1])/2)

# Renforts (magenta)
renforts = [
    ("R1", (AX_X[1], AX_Y[0]+2.84), "Moisage"),
    ("R2", (AX_X[0], AX_Y[0]), "Sommier répartition"),
    ("R3", (AX_X[1], AX_Y[1]), "Entretoise"),
    ("R4", (AX_X[1], AX_Y[2]), "Contrefiche"),
]
for name, (x, y), desc in renforts:
    p_msp.add_circle(Vec2(x, y), 0.2)
    p_msp.add_text(f"{name} {desc}", height=0.25).dxf.insert = Vec2(x+0.4, y+0.4)

# Axes (gris foncé)
axes = [
    ("A", (AX_X[0], AX_Y[0]-0.5), (AX_X[0], AX_Y[2]+0.5)),
    ("B", (AX_X[1], AX_Y[0]-0.5), (AX_X[1], AX_Y[2]+0.5)),
    ("C", (AX_X[2], AX_Y[0]-0.5), (AX_X[2], AX_Y[2]+0.5)),
    ("1", (AX_X[0]-0.5, AX_Y[0]), (AX_X[2]+0.5, AX_Y[0])),
    ("2", (AX_X[0]-0.5, AX_Y[1]), (AX_X[2]+0.5, AX_Y[1])),
    ("3", (AX_X[0]-0.5, AX_Y[2]), (AX_X[2]+0.5, AX_Y[2])),
]
for name, (x1, y1), (x2, y2) in axes:
    p_msp.add_line(Vec2(x1, y1), Vec2(x2, y2))
    p_msp.add_text(name, height=0.4).dxf.insert = Vec2(x1, y1-0.4)

# Sauvegarde DXF
dxf_path = os.path.join(OUT, "B-20_Plan_Principe_P1_V2.dxf")
principe.saveas(dxf_path)
print(f"DXF sauvegardé : {dxf_path}")

# ---- PNG via matplotlib ----
fig, ax = plt.subplots(1, 1, figsize=(20, 16))
fig.patch.set_facecolor('white')

# Fond B-32 V3 (PROJET en gris)
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
            ax.plot([p[0] for p in pts], [p[1] for p in pts],
                    color='lightgray', linewidth=0.5, zorder=1)
        elif e.dxftype() in ('TEXT', 'MTEXT'):
            txt = e.dxf.text if e.dxftype() == 'TEXT' else e.text
            ax.text(e.dxf.insert.x, e.dxf.insert.y, str(txt), fontsize=2, color='gray', zorder=1)
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
ax.plot([AX_X[0], AX_X[2]], [AX_Y[0], AX_Y[0]], color='limegreen', linewidth=2, zorder=5)
ax.text(AX_X[0], AX_Y[0]-0.8, "SF1", fontsize=8, color='limegreen', zorder=6)

# Linteaux (jaune)
for name, (x1, y1), (x2, y2) in linteaux:
    ax.plot([x1, x2], [y1, y2], color='gold', linewidth=2, zorder=5)
    ax.text(x1+0.3, y1+0.3, name, fontsize=8, color='darkgoldenrod', zorder=6)

# Dallage (bleu)
ax.add_patch(Rectangle((AX_X[0], AX_Y[0]), AX_X[2]-AX_X[0], AX_Y[1]-AX_Y[0],
              fill=False, edgecolor='blue', linewidth=1.5, linestyle='--', zorder=5))
ax.text((AX_X[0]+AX_X[2])/2, (AX_Y[0]+AX_Y[1])/2, "Dg1", fontsize=10, color='blue', zorder=6)

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
    plt.Line2D([0], [0], color='lightgray', lw=0.5, label='Fond B-32 V3 (PROJET)'),
]
ax.legend(handles=legend_elems, loc='upper left', fontsize=7, framealpha=0.9)

ax.set_aspect('equal')
ax.set_title(f"B-20 V2 — Plan de principe Conception GO — Indice P1\n"
             f"Fond : B-32 V3 (PROJET) — Trame sur zone PROJET (X > 115,64 m)", fontsize=11)
ax.set_xlabel("X (m, RSU)")
ax.set_ylabel("Y (m, RSU)")
ax.grid(True, alpha=0.3)

png_path = os.path.join(OUT, "B-20_Plan_Principe_P1_V2.png")
fig.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"PNG sauvegardé : {png_path}")

# ---- PDF ----
pdf_path = os.path.join(OUT, "B-20_Plan_Principe_P1_V2.pdf")
fig, ax = plt.subplots(1, 1, figsize=(20, 16))
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
for name, (x, y) in semelles:
    ax.add_patch(Rectangle((x-0.5, y-0.5), 1.0, 1.0, fill=False, edgecolor='green', linewidth=1.5, zorder=5))
ax.plot([AX_X[0], AX_X[2]], [AX_Y[0], AX_Y[0]], color='limegreen', linewidth=2, zorder=5)
for name, (x1, y1), (x2, y2) in linteaux:
    ax.plot([x1, x2], [y1, y2], color='gold', linewidth=2, zorder=5)
ax.add_patch(Rectangle((AX_X[0], AX_Y[0]), AX_X[2]-AX_X[0], AX_Y[1]-AX_Y[0],
              fill=False, edgecolor='blue', linewidth=1.5, linestyle='--', zorder=5))
for name, (x, y), desc in renforts:
    ax.add_patch(Circle((x, y), 0.2, fill=False, edgecolor='magenta', linewidth=1.5, zorder=5))
for name, (x1, y1), (x2, y2) in axes:
    ax.plot([x1, x2], [y1, y2], color='dimgray', linewidth=0.5, linestyle=':', zorder=2)
ax.text(0.5, 0.02, "PRINCIPE — NE PAS EXÉCUTER — Indice P1", transform=ax.transAxes,
        fontsize=14, color='red', alpha=0.5, ha='center', va='bottom', zorder=10)
ax.set_aspect('equal')
ax.set_title("B-20 V2 — Plan de principe Conception GO — Indice P1", fontsize=11)
ax.set_xlabel("X (m, RSU)")
ax.set_ylabel("Y (m, RSU)")
ax.grid(True, alpha=0.3)
fig.savefig(pdf_path, dpi=150, bbox_inches='tight', format='pdf')
plt.close()
print(f"PDF sauvegardé : {pdf_path}")

# ---- Journal V2 ----
with open(os.path.join(OUT, "journal_B20_V2.md"), "w", encoding="utf-8") as f:
    f.write("# Journal B-20 V2 — Conception structure GO — Fond PROJET (B-32 V3)\n\n")
    f.write("**Date** : 2026-10-31  \n**Mode** : INTERNE-GO  \n**Script** : `build_b20_v2.py`  \n\n")
    f.write("## Correction fondamentale\n\n")
    f.write("B-20 V1 était positionné sur la zone EXISTANT (X=0-18). Refait sur B-32 V3 (PROJET seul).\n")
    f.write("La trame et les renforts sont maintenant implantés sur la zone PROJECT (X > 115,64 m).\n\n")
    f.write("## Trame structurelle (zone PROJET)\n\n")
    f.write(f"- Bâtiment : X[{BLD_X_MIN:.2f}, {BLD_X_MAX:.2f}] Y[{BLD_Y_MIN:.2f}, {BLD_Y_MAX:.2f}] — {BLD_W:.2f} m × {BLD_D:.2f} m\n")
    f.write(f"- Axes A/B/C (sens 1) : X = {AX_X[0]:.2f}, {AX_X[1]:.2f}, {AX_X[2]:.2f} m\n")
    f.write(f"- Axes 1/2/3 (sens 2) : Y = {AX_Y[0]:.2f}, {AX_Y[1]:.2f}, {AX_Y[2]:.2f} m\n\n")
    f.write("## Ouvrages neufs implantés (zone PROJET)\n\n")
    for name, (x, y) in poteaux:
        f.write(f"- {name} : ({x:.2f}, {y:.2f})\n")
    for name, (x1, y1), (x2, y2) in poutres:
        f.write(f"- {name} : ({x1:.2f}, {y1:.2f}) → ({x2:.2f}, {y2:.2f})\n")
    for name, (x, y) in semelles:
        f.write(f"- {name} : ({x:.2f}, {y:.2f})\n")
    f.write(f"- SF1 : ({AX_X[0]:.2f}, {AX_Y[0]:.2f}) → ({AX_X[2]:.2f}, {AX_Y[0]:.2f})\n")
    for name, (x1, y1), (x2, y2) in linteaux:
        f.write(f"- {name} : ({x1:.2f}, {y1:.2f}) → ({x2:.2f}, {y2:.2f})\n")
    f.write(f"- Dg1 : dallage RDC ({AX_X[0]:.2f}, {AX_Y[0]:.2f}) à ({AX_X[2]:.2f}, {AX_Y[1]:.2f})\n\n")
    f.write("## Renforts de l'existant\n\n")
    for name, (x, y), desc in renforts:
        f.write(f"- {name} ({desc}) : ({x:.2f}, {y:.2f})\n")
    f.write("\n## Livrables\n\n")
    f.write(f"- DXF : B-20_Plan_Principe_P1_V2.dxf\n")
    f.write(f"- PNG : B-20_Plan_Principe_P1_V2.png\n")
    f.write(f"- PDF : B-20_Plan_Principe_P1_V2.pdf\n")
    f.write(f"- Journal : journal_B20_V2.md\n\n")
    f.write("## Contrôles\n\n")
    f.write("- Fond : B-32 V3 (PROJET seul, 30 entités)\n")
    f.write("- Aucun élément en zone EXISTANT ou MILIEU\n")
    f.write("- Filigrane « PRINCIPE — NE PAS EXÉCUTER — Indice P1 » appliqué\n")

print("\n=== B-20 V2 Plans de principe générés ===")
print(f"DXF: {dxf_path}")
print(f"PNG: {png_path}")
print(f"PDF: {pdf_path}")
