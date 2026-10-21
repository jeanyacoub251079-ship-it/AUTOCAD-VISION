#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-60 — PASSE PRÉSENTATION Ind. B — CROISSY-FLORA — 21/10/2026
Mêmes chiffres, mêmes réserves. Fond blanc, existant gris, ouvrages en couleur.
Implantation obligatoire. Codes CARNAC hors dessin.
CARNAC v3.0.1 addendum A1 / LIV-06.
"""
from __future__ import annotations

import json
import os
from collections import Counter

import ezdxf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, Circle, FancyArrowPatch
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANS = os.path.join(ROOT, "_plans")
OUT = os.path.join(ROOT, "_rendus")
os.makedirs(PLANS, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

# --- couleurs (style BET lisible) ---
GRIS = "#B0B0B0"
GRIS_F = "#7A7A7A"
NOIR = "#1A1A1A"
ORANGE = "#E07A2F"   # BA / semelles
BLEU = "#2F6DB5"     # acier
VERT = "#2E8B57"     # BA verticaux / sommiers
MARRON = "#8B5A2B"   # bois
ROUGE = "#C0392B"    # linteaux / alerte
VIOLET = "#6C3483"   # assemblages
HACH_D19 = "#F4D03F"

AX_X = {"A": 85.55, "B": 86.55, "C": 88.75, "D": 89.78, "E": 95.35}
AX_Y = {"1": 44.60, "2": 49.54, "3": 52.14, "4": 54.89, "5": 59.05, "6": 63.12}
OUTER = (85.47, 44.38, 95.55, 63.20)  # xmin ymin xmax ymax

LOG = []


def log(t=""):
    LOG.append(t)
    print(t)


def m(cm):
    return cm / 100.0


# ---------- géométrie (report B-20, cm → m) ----------
FRANGEMENTS = [
    ("F1a", 8977.4, 5320.2, 8977.4, 5464.1, 0.28, "2×HEA 200", "1,00 m"),
    ("F1b", 9279.8, 5489.2, 9427.5, 5489.2, 0.28, "2×HEA 200", "0,90 m"),
    ("F1c", 9407.5, 5214.0, 9532.5, 5214.0, 0.28, "2×HEA 200", "0,85 m"),
    ("F2", 8647.4, 4954.1, 8972.5, 4954.1, 0.20, "HEB 200", "2,85 m"),
    ("F3", 8547.5, 5311.6, 8972.5, 5311.6, 0.16, "HEB 160", "3,85 m"),
    ("F4", 8875.0, 4458.6, 8875.0, 4946.6, 0.15, "IPE 200", "4,88 m"),
]
RENFORTS = [
    ("R1", 8547.5, 5488.7, 8969.8, 5488.7, 0.26, "2×UPE 200", "3,85 m"),
    ("R2-N", 8570.5, 5709.1, 8952.5, 5709.1, 0.16, "HEB 160", "3,82 m"),
    ("R2-S", 8570.5, 5133.1, 8952.5, 5133.1, 0.16, "HEB 160", "3,82 m"),
    ("R3-N", 8570.5, 5584.2, 8570.5, 5834.1, 0.14, "UPE 200+B", "1,55 m"),
    ("R3-S", 8570.5, 5007.9, 8570.5, 5258.0, 0.14, "UPE 200+B", "1,55 m"),
]
P1 = [("P1-N", 9540.5, 4904.4, 0.14, "SHS 140×140×6,3"),
      ("P1-S", 9540.5, 4778.4, 0.14, "SHS 140×140×6,3")]
P_BA = [
    ("P2", 9522.5, 5921.7, 9547.6, 5936.7, "150×250", "6 HA12"),
    ("P3", 9389.7, 5464.1, 9427.5, 5514.1, "400×500", "6 HA12"),
    ("J1", 8952.5, 5440.1, 9002.5, 5464.1, "240×500", "6 HA12"),
]
SF1 = (95.35, 59.29, 0.80)  # xc, yc, B
D19 = [
    ("Z-P1N", 95.41, 49.04),
    ("Z-P1S", 95.41, 47.78),
    ("Z-P3", 94.09, 54.89),
    ("Z-J1", 89.78, 54.52),
]
BECHE = (86.67, 46.77, 89.53, 46.97)
RSO = (87.70, 63.30, 93.50, 64.30)
COUSSINS = [
    ("C-F2-O", 8647.4, 4926.0, 8677.4, 4961.5),
    ("C-F2-E", 8942.5, 4927.0, 8972.5, 4962.6),
    ("C-F3-O", 8547.5, 5293.8, 8577.5, 5329.5),
    ("C-F3-E", 8942.5, 5293.8, 8972.5, 5329.5),
    ("C-R1-O", 8547.5, 5464.6, 8577.5, 5513.7),
    ("C-R1-E", 8942.5, 5464.1, 8972.5, 5518.1),
]
PANNES = [
    ("PN1", 8856.0, 4961.7, 8856.0, 5881.7, 0.12, "75×200 C24"),
    ("PN2", 9002.5, 5535.6, 9537.1, 5535.6, 0.12, "75×200 C24"),
    ("PN3", 9002.5, 5271.3, 9537.1, 5271.3, 0.12, "75×200 C24"),
]
DF = [
    ("DF1", 8567.5, 5566.6, 8952.5, 5566.6, 0.14, "arb. 100×200"),
    ("DF2", 8567.5, 5276.8, 8952.5, 5276.8, 0.14, "arb. 100×200"),
]
CF = ("CF", 9537.1, 5139.2, 9537.1, 5667.7, 0.16, "75×225 C24")
ZN = [("ZN1", 90.05, 56.85, 95.25, 62.95), ("ZN2", 90.05, 44.80, 95.25, 51.20)]
STAB = [
    ("Stab1-NW", 9175.5, 5534.2, 9175.5, 6296.7),
    ("Stab1-NE", 9349.4, 5534.2, 9349.4, 6296.7),
    ("Stab1-SW", 9175.5, 4509.9, 9175.5, 5189.1),
    ("Stab1-SE", 9349.4, 4509.9, 9349.4, 5189.1),
]


# ---------- primitives matplotlib ----------
def stroke():
    return [pe.withStroke(linewidth=2.4, foreground="white")]


def draw_building(ax, show_axes=True):
    x0, y0, x1, y1 = OUTER
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False,
                           ec=GRIS_F, lw=1.4, zorder=1))
    # murs internes
    for x in (AX_X["B"], AX_X["C"], AX_X["D"]):
        ax.plot([x, x], [y0, y1], color=GRIS, lw=0.7, zorder=1)
    for y in (AX_Y["2"], AX_Y["3"], AX_Y["4"], AX_Y["5"]):
        ax.plot([x0, x1], [y, y], color=GRIS, lw=0.7, zorder=1)
    if show_axes:
        for k, x in AX_X.items():
            ax.plot(x, y1 + 0.35, "o", ms=10, mfc="white", mec=GRIS_F, zorder=3)
            ax.text(x, y1 + 0.35, k, ha="center", va="center", fontsize=8,
                    color=GRIS_F, fontweight="bold", zorder=4)
        for k, y in AX_Y.items():
            ax.plot(x0 - 0.40, y, "o", ms=10, mfc="white", mec=GRIS_F, zorder=3)
            ax.text(x0 - 0.40, y, k, ha="center", va="center", fontsize=8,
                    color=GRIS_F, fontweight="bold", zorder=4)
    ax.text((x0 + x1) / 2, y0 - 0.55, "EXISTANT  —  trait gris  ·  NEUF  —  couleur",
            ha="center", fontsize=7.5, color=GRIS_F, style="italic")


def beam(ax, x1, y1, x2, y2, w, color, label=None, z=4):
    x1, y1, x2, y2 = m(x1), m(y1), m(x2), m(y2)
    dx, dy = x2 - x1, y2 - y1
    L = (dx * dx + dy * dy) ** 0.5 or 1e-6
    nx, ny = -dy / L * w / 2, dx / L * w / 2
    pts = [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)]
    ax.add_patch(Polygon(pts, closed=True, fc=color, ec=color, alpha=0.85, lw=0.4, zorder=z))
    if label:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.18, label, ha="center", va="bottom",
                fontsize=7.5, color=color, fontweight="bold", zorder=z + 1,
                path_effects=stroke())


def rect_m(ax, x0, y0, x1, y1, color, label=None, alpha=0.85):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=color, ec=color,
                           alpha=alpha, lw=0.6, zorder=4))
    if label:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, label, ha="center", va="center",
                fontsize=7.5, color="white", fontweight="bold", zorder=5)


def dim_h(ax, x1, x2, y, txt):
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    ax.text((x1 + x2) / 2, y + 0.08, txt, ha="center", va="bottom", fontsize=7, color=NOIR)


def dim_v(ax, y1, y2, x, txt):
    ax.annotate("", xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    ax.text(x + 0.10, (y1 + y2) / 2, txt, ha="left", va="center", fontsize=7, color=NOIR)


def title_block(fig, ligne1, ligne2, ligne3):
    fig.text(0.015, 0.975, ligne1, fontsize=11, fontweight="bold", va="top", color=NOIR)
    fig.text(0.015, 0.948, ligne2, fontsize=10, va="top", color=NOIR)
    fig.text(0.015, 0.924, ligne3, fontsize=8.5, va="top", color=GRIS_F)
    fig.text(0.985, 0.975, "NE PAS EXÉCUTER SANS VISA", fontsize=9,
             ha="right", va="top", color=ROUGE, fontweight="bold")
    fig.text(0.985, 0.948, "Protection au feu adéquate à prévoir (hors lot GO)",
             fontsize=7.5, ha="right", va="top", color=GRIS_F)


def watermark(ax, text="NE PAS EXÉCUTER SANS VISA"):
    ax.text(0.50, 0.50, text, transform=ax.transAxes, fontsize=22,
            color=ROUGE, alpha=0.07, ha="center", va="center", rotation=28,
            fontweight="bold", zorder=0)


def nom_table(ax, rows, title="Nomenclature"):
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.text(0.02, 0.96, title, fontsize=9, fontweight="bold", va="top", color=NOIR)
    y = 0.88
    for line in rows:
        ax.text(0.02, y, line, fontsize=7.4, va="top", family="DejaVu Sans", color=NOIR)
        y -= 0.075
        if y < 0.04:
            break


def new_fig():
    fig = plt.figure(figsize=(16.54, 11.69), facecolor="white")  # A3 paysage
    ax = fig.add_axes([0.03, 0.06, 0.62, 0.84])
    ax.set_aspect("equal")
    ax.set_xlim(OUTER[0] - 1.3, OUTER[2] + 1.6)
    ax.set_ylim(OUTER[1] - 1.1, OUTER[3] + 1.0)
    ax.axis("off")
    ax.set_facecolor("white")
    axc = fig.add_axes([0.67, 0.42, 0.31, 0.48])
    axc.set_facecolor("white")
    axn = fig.add_axes([0.67, 0.06, 0.31, 0.33])
    axn.set_facecolor("#FAFAFA")
    return fig, ax, axc, axn


def save(fig, base):
    png = base + ".png"
    pdf = base + ".pdf"
    fig.savefig(png, dpi=160, facecolor="white")
    fig.savefig(pdf, facecolor="white")
    plt.close(fig)
    return png, pdf


# ---------- DXF léger ----------
def dxf_new(prefix):
    doc = ezdxf.new("R2013")
    doc.units = 4  # mm — on travaille en cm*10 = mm? On reste en m * 1000 = mm
    msp = doc.modelspace()
    layers = [
        (f"{prefix}-EXISTANT", 8), (f"{prefix}-OUVRAGE", 5),
        (f"{prefix}-ACIER", 1), (f"{prefix}-COTATION", 3),
        (f"{prefix}-TEXTE", 7), (f"{prefix}-CARTOUCHE", 7),
        (f"{prefix}-DETAILS", 4), (f"{prefix}-NOMENCLATURE", 7),
        (f"{prefix}-AXES", 8),
    ]
    for n, c in layers:
        if n not in doc.layers:
            doc.layers.add(n, color=c)
    return doc, msp


def dxf_rect(msp, x0, y0, x1, y1, layer):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})


def dxf_txt(msp, x, y, t, h=180, layer="FOND-TEXTE"):
    e = msp.add_text(t, height=h, dxfattribs={"layer": layer})
    e.set_placement((x, y))


def dxf_building(msp, prefix):
    x0, y0, x1, y1 = [v * 1000 for v in OUTER]  # mm
    dxf_rect(msp, x0, y0, x1, y1, f"{prefix}-EXISTANT")
    for x in AX_X.values():
        msp.add_line((x * 1000, y0), (x * 1000, y1), dxfattribs={"layer": f"{prefix}-AXES"})
    for y in AX_Y.values():
        msp.add_line((x0, y * 1000), (x1, y * 1000), dxfattribs={"layer": f"{prefix}-AXES"})


def dxf_save(doc, base, prefix):
    path = base + ".dxf"
    doc.saveas(path)
    audit = doc.audit()
    doc2 = ezdxf.readfile(path)
    cnt = Counter(e.dxf.layer for e in doc2.modelspace())
    n0 = cnt.get("0", 0)
    npre = sum(n for l, n in cnt.items() if l.startswith(prefix))
    return path, len(audit.errors), n0, npre, dict(cnt)


# ===================== PLANCHES =====================
def plan_fond():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  FONDATIONS (RDC BAS)  —  Ind. B  —  21/10/2026",
                "C25/30 · S500B · arase inf. −1,00 m / TN mini  ·  c_nom 50 mm  ·  PARTIEL-DÉCLARÉ")
    draw_building(ax)
    watermark(ax)
    xc, yc, B = SF1
    rect_m(ax, xc - B / 2 - 0.05, yc - B / 2 - 0.05, xc + B / 2 + 0.05, yc + B / 2 + 0.05,
           "#D4A017", alpha=0.35)  # GB
    rect_m(ax, xc - B / 2, yc - B / 2, xc + B / 2, yc + B / 2, ORANGE, "SF1")
    rect_m(ax, 95.225, 59.217, 95.476, 59.367, VERT, "P2")
    dim_h(ax, xc - B / 2, xc + B / 2, yc - B / 2 - 0.35, "800 mm")
    for name, x, y in D19:
        ax.add_patch(Circle((x, y), 0.38, fc="none", ec=HACH_D19, lw=1.4, ls="--", zorder=3))
        ax.text(x + 0.45, y, name, fontsize=7, color="#9A7D0A", fontweight="bold")
    rect_m(ax, BECHE[0], BECHE[1], BECHE[2], BECHE[3], ORANGE, alpha=0.7)
    ax.text((BECHE[0] + BECHE[2]) / 2, BECHE[1] - 0.25, "Bêche 200 mm", ha="center",
            fontsize=7, color=ORANGE, fontweight="bold")
    ax.add_patch(Rectangle((RSO[0], RSO[1]), RSO[2] - RSO[0], RSO[3] - RSO[1],
                           fc="none", ec=ORANGE, lw=1.2, ls="--", zorder=3))
    ax.text((RSO[0] + RSO[2]) / 2, (RSO[1] + RSO[3]) / 2, "RSO passerelle\npasses ≤ 1,00 m",
            ha="center", va="center", fontsize=7, color=ORANGE)

    # coupe
    axc.set_xlim(-0.3, 2.4)
    axc.set_ylim(-1.35, 1.15)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("Coupe A-A  —  SF1  800×800×250  ·  1/20", fontsize=9, loc="left", pad=2)
    # GB
    axc.add_patch(Rectangle((-0.15, -1.05), 1.10, 0.30, fc="#E8C96A", ec="#9A7D0A", lw=0.8))
    axc.text(0.40, -0.90, "gros béton C16/20\nsi existant plus profond", ha="center", fontsize=6.5, color="#6B4F00")
    # propreté
    axc.add_patch(Rectangle((-0.05, -0.75), 0.90, 0.05, fc="#CCCCCC", ec=GRIS_F, lw=0.5))
    # semelle
    axc.add_patch(Rectangle((0.00, -0.70), 0.80, 0.25, fc="#F3D1B0", ec=ORANGE, lw=1.2))
    axc.add_patch(Rectangle((0.00, -0.70), 0.80, 0.25, fill=False, ec=ORANGE, lw=1.2,
                            hatch="///"))
    # poteau
    axc.add_patch(Rectangle((0.275, -0.45), 0.25, 1.10, fc="#C5E1C5", ec=VERT, lw=1.1))
    # aciers lit inf
    for i in range(6):
        axc.plot(0.08 + i * 0.13, -0.58, "o", ms=4, color=ROUGE, zorder=5)
    # attentes équerre
    for s in (0.30, 0.50):
        axc.plot([s, s], [-0.58, 0.55], color=ROUGE, lw=1.4, zorder=5)
        axc.plot([s, s + 0.10], [-0.58, -0.58], color=ROUGE, lw=1.4, zorder=5)
    axc.annotate("", xy=(0.00, -0.78), xytext=(0.80, -0.78),
                 arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    axc.text(0.40, -0.82, "800 mm", ha="center", fontsize=7)
    axc.annotate("", xy=(0.92, -0.70), xytext=(0.92, -0.45),
                 arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    axc.text(0.96, -0.57, "250", fontsize=7)
    axc.text(1.05, 0.20, "P2  150×250\n6 HA12 équerre\nl_bd = 166 mm", fontsize=7.5, color=VERT)
    axc.text(1.05, -0.20, "HA8 e150  2 nappes\nc_nom = 50 mm  4 faces", fontsize=7.5, color=ROUGE)
    axc.text(1.05, -1.15, "Arase inf.  −1,00 m / TN  MINIMUM\nJamais de remontée.", fontsize=7, color=NOIR)
    axc.axhline(-1.00, color=GRIS_F, ls=":", lw=0.6)
    axc.text(-0.28, -1.00, "−1,00", fontsize=6.5, color=GRIS_F, va="center")

    nom_table(axn, [
        "Rep.     Ouvrage                         Qté",
        "SF1      Semelle 800×800×250 C25/30        1",
        "HA8      Lit inf. e150  6+6                1 nappe",
        "HA12     Attentes P2 équerre               6",
        "GB       C16/20 sous semelle         selon fouille",
        "BP       Propreté 50 mm                    1",
        "Bêche    200 mm × 2,85 m                   1",
        "RSO      Passes ≤ 1,00 m C16/20         1 zone",
        "Type     600×600×300 si fouille      selon constat",
        "",
        "Fouille : réception contradictoire avant coulage.",
        "Nuages jaunes = reconnaissance en fouille (ouverte).",
    ], "Nomenclature  —  façonnage → B-62")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  coupe 1/20  ·  cotes mm  ·  niveaux m  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_FOND_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("FOND")
    dxf_building(msp, "FOND")
    dxf_rect(msp, (xc - 0.4) * 1000, (yc - 0.4) * 1000, (xc + 0.4) * 1000, (yc + 0.4) * 1000, "FOND-OUVRAGE")
    dxf_txt(msp, xc * 1000, (yc + 0.55) * 1000, "SF1 800x800x250", 120, "FOND-TEXTE")
    dxf_txt(msp, OUTER[0] * 1000, (OUTER[3] + 0.8) * 1000,
            "FLORA FOND EXE Ind.B — NE PAS EXECUTER SANS VISA", 200, "FOND-CARTOUCHE")
    return dxf_save(doc, base, "FOND")


def plan_vert():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  POTEAUX ET JAMBAGES BA  —  Ind. B  —  21/10/2026",
                "C25/30 · S500B · c_nom 30 mm  ·  6 HA12 partout  ·  H = 2,80 m (à relever)")
    draw_building(ax)
    watermark(ax)
    for name, x0, y0, x1, y1, sec, fer in P_BA:
        rect_m(ax, m(x0), m(y0), m(x1), m(y1), VERT, name)
        ax.text(m((x0 + x1) / 2), m(y1) + 0.22, sec, ha="center", fontsize=6.5, color=VERT)
    # nuages P3 J1
    ax.add_patch(Circle((94.09, 54.89), 0.45, fc="none", ec=HACH_D19, lw=1.3, ls="--"))
    ax.add_patch(Circle((89.78, 54.52), 0.45, fc="none", ec=HACH_D19, lw=1.3, ls="--"))

    axc.set_xlim(-0.15, 1.6)
    axc.set_ylim(-0.15, 3.15)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("Coupe type P2  150×250  ·  1/20", fontsize=9, loc="left")
    axc.add_patch(Rectangle((0.10, 0.00), 0.25, 2.80, fc="#C5E1C5", ec=VERT, lw=1.2, hatch="///"))
    for i, x in enumerate((0.14, 0.22, 0.31)):
        axc.plot([x, x], [0.05, 2.75], color=ROUGE, lw=1.3)
    for y in (0.15, 0.30, 0.45, 0.90, 1.35, 1.80, 2.25, 2.55, 2.70):
        axc.add_patch(Rectangle((0.12, y), 0.21, 0.04, fill=False, ec=ROUGE, lw=0.7))
    axc.annotate("", xy=(0.10, -0.08), xytext=(0.35, -0.08),
                 arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    axc.text(0.225, -0.12, "150", ha="center", fontsize=7)
    axc.annotate("", xy=(0.42, 0.00), xytext=(0.42, 2.80),
                 arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    axc.text(0.46, 1.40, "2 800 mm\n(à relever)", fontsize=7)
    axc.text(0.70, 2.20, "6 HA12\nHA8 e150\nc_nom 30 mm", fontsize=8, color=ROUGE)
    axc.text(0.70, 1.40, "N_Ed = 159,0 kN\nM_Ed / M_Rd = 0,305\nλ = 64,7  →  2ᵉ ordre", fontsize=7.5)
    axc.text(0.70, 0.50, "P3  400×500   0,013\nJ1  240×500   0,015\n(min. réglementaire)", fontsize=7.5, color=GRIS_F)

    nom_table(axn, [
        "Rep.   Section mm     Acier        N_Ed     Taux",
        "P2     150 × 250      6 HA12     159,0 kN   0,305",
        "P3     400 × 500      6 HA12      35,8 kN   0,013",
        "J1     240 × 500      6 HA12      39,8 kN   0,015",
        "Cadres HA8 e150 (P2) / e200 (P3, J1)",
        "",
        "6 HA12 imposé par l'espacement max., pas par As,min.",
        "Appui J1 sur maçonnerie : 0,332 MPa (f_k = 1,5 MPa).",
        "H = 2 800 mm = hypothèse — relevé avant façonnage.",
    ], "Nomenclature  —  façonnage → B-62")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  coupe 1/20  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_VERT_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("VERT")
    dxf_building(msp, "VERT")
    for name, x0, y0, x1, y1, sec, fer in P_BA:
        dxf_rect(msp, x0 * 10, y0 * 10, x1 * 10, y1 * 10, "VERT-OUVRAGE")
        dxf_txt(msp, x0 * 10, y1 * 10 + 80, name, 120, "VERT-TEXTE")
    return dxf_save(doc, base, "VERT")


def plan_plancher():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  DALLAGE RDC BAS  —  Ind. B  —  21/10/2026",
                "C25/30  130 mm  ·  ST25C  ·  111,15 m²  ·  joints de retrait e ≤ 4,50 m")
    draw_building(ax)
    watermark(ax)
    x0, y0, x1, y1 = OUTER
    inset = 0.08
    ax.add_patch(Rectangle((x0 + inset, y0 + inset), (x1 - x0) - 2 * inset, (y1 - y0) - 2 * inset,
                           fc="#F5CBA7", ec=ORANGE, alpha=0.45, lw=1.0, zorder=2, hatch="...."))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2, "ZONE D  —  DALLAGE BA  130 mm\n111,15 m²   ST25C  Ø7 e150",
            ha="center", va="center", fontsize=10, color=ORANGE, fontweight="bold", zorder=3)
    # joints retrait ~ 4.5 m
    xs = list(ax.transData.inverted().transform((0, 0)))  # dummy
    jx = x0 + 4.5
    while jx < x1 - 0.3:
        ax.plot([jx, jx], [y0 + 0.15, y1 - 0.15], color=ROUGE, ls="--", lw=0.8, zorder=3, alpha=0.7)
        jx += 4.5
    jy = y0 + 4.5
    while jy < y1 - 0.3:
        ax.plot([x0 + 0.15, x1 - 0.15], [jy, jy], color=ROUGE, ls="--", lw=0.8, zorder=3, alpha=0.7)
        jy += 4.5
    ax.text(x1 - 0.15, y1 - 0.4, "joints sciés  e ≤ 4,50 m\n(retrait, pas dilatation)",
            ha="right", fontsize=7, color=ROUGE)
    ax.text(x0 + 0.2, y0 + 0.25, "désolidarisation périphérique 20 mm", fontsize=7, color=GRIS_F)

    axc.set_xlim(-0.2, 2.6)
    axc.set_ylim(-0.85, 0.55)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("Coupe type dallage  ·  1/10", fontsize=9, loc="left")
    axc.add_patch(Rectangle((-0.05, -0.70), 2.2, 0.40, fc="#C8B48A", ec="#8D6E3B", lw=0.6))
    axc.text(1.05, -0.50, "fond de forme  400 mm", ha="center", fontsize=7, color="#6B4F00")
    axc.add_patch(Rectangle((-0.05, -0.30), 2.2, 0.15, fc="#A07840", ec="#6B4F00", lw=0.6))
    axc.text(1.05, -0.225, "recharge 150 mm  (100 % emprise)", ha="center", fontsize=7)
    axc.add_patch(Rectangle((-0.05, -0.15), 2.2, 0.13, fc="#F3D1B0", ec=ORANGE, lw=1.1, hatch="///"))
    axc.plot([-0.02, 2.12], [-0.085, -0.085], color=ROUGE, lw=1.5)
    axc.text(1.05, -0.02, "dallage 130 mm  +  ST25C", ha="center", fontsize=8, color=ORANGE, fontweight="bold")
    axc.add_patch(Rectangle((-0.05, -0.15), 0.02, 0.13, fc="#333333", ec="none"))
    axc.text(-0.02, 0.05, "20 mm", fontsize=6.5, rotation=90, va="bottom")
    axc.text(0.15, 0.22, "p_ELU = 14,21 kN/m²   ·   portance sol 2,9 %   ·   désolidarisé des semelles",
             fontsize=7)

    nom_table(axn, [
        "Rep.     Ouvrage                              Qté",
        "Dallage  BA 130 mm C25/30  111,15 m²            1",
        "ST25C    Ø7 e150  257 mm²/m  2 nappes           1",
        "Joints   sciés e ≤ 4 500 mm              selon plan",
        "Bandes   polystyrène 20 mm  périphérie          1",
        "Recharge 150 mm sous dallage              100 %",
        "",
        "Zone A solives 8×18 : EXISTANT — hors ce plan.",
        "Zone B IPE 160/330 : EXISTANT — voir métal.",
        "Plancher haut E-07 : non sondé — non chargé.",
    ], "Nomenclature")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  coupe 1/10  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_PLANCHER_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("PLANCHER")
    dxf_building(msp, "PLANCHER")
    dxf_rect(msp, (x0 + 0.08) * 1000, (y0 + 0.08) * 1000, (x1 - 0.08) * 1000, (y1 - 0.08) * 1000, "PLANCHER-OUVRAGE")
    dxf_txt(msp, 88.5 * 1000, 54 * 1000, "DALLAGE 130 mm  111,15 m2  ST25C", 180, "PLANCHER-TEXTE")
    return dxf_save(doc, base, "PLANCHER")


def plan_metal():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  STRUCTURE MÉTALLIQUE  —  Ind. B  —  21/10/2026",
                "S275  ·  F3 : aucune charge ajoutée (flèche 0,971 × L/300)")
    draw_building(ax)
    watermark(ax)
    for rec in FRANGEMENTS:
        if rec[0].startswith("F1"):
            continue  # linteaux
        beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], BLEU, rec[0])
    for rec in RENFORTS:
        if rec[0].startswith("R3"):
            continue
        beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], BLEU, rec[0])
    for name, xc, yc, cote, prof in P1:
        rect_m(ax, m(xc) - 0.18, m(yc) - 0.18, m(xc) + 0.18, m(yc) + 0.18, VIOLET, None)
        ax.text(m(xc) + 0.35, m(yc), name, fontsize=8, color=VIOLET, fontweight="bold",
                va="center", path_effects=stroke())
    for name, x1, y1, x2, y2 in STAB:
        ax.plot([m(x1), m(x2)], [m(y1), m(y2)], color="#5DADE2", lw=1.6, ls=":", zorder=3)
    ax.text(92.6, 58.8, "Stab1 IPE 120", fontsize=7, color="#5DADE2")

    axc.set_axis_off()
    axc.set_xlim(0, 1)
    axc.set_ylim(0, 1)
    axc.text(0.02, 0.96, "Profilés  —  S275  —  classe 1", fontsize=9, fontweight="bold", va="top")
    lines = [
        "F2   HEB 200    L=2,85 m   M 0,252   w 0,237",
        "F3   HEB 160    L=3,85 m   M 0,609   w 0,971  ←",
        "F4   IPE 200    L=4,88 m   M 0,231   w 0,306",
        "R1   2×UPE 200  L=3,85 m   LT 0,880  w 0,927",
        "R2   HEB 160    L=3,82 m   ×2",
        "P1   SHS 140×6,3  N_Ed 100,3 kN  flamb. 0,123",
        "Stab1  IPE 120   4 files   5,8 kN / file",
        "",
        "F3 : 12,5 mm pour 12,8 mm admis.",
        "Toute charge ajoutée (y c. C4) = non conforme.",
        "IPE 330 existant : hors calcul.",
        "R3 / F1 : voir LINTEAU.  Coussins : MACON.",
    ]
    y = 0.88
    for L in lines:
        axc.text(0.02, y, L, fontsize=7.4, va="top", family="DejaVu Sans",
                 color=ROUGE if "←" in L else NOIR)
        y -= 0.07

    nom_table(axn, [
        "Rep.    Profil              L (mm)   Qté",
        "F2      HEB 200              2 850     1",
        "F3      HEB 160              3 850     1",
        "F4      IPE 200              4 880     1",
        "R1      UPE 200              3 850     2",
        "R2-N/S  HEB 160              3 820     2",
        "P1-N/S  SHS 140×140×6,3      3 000     2",
        "Stab1   IPE 120            selon relevé  4",
        "Remplissage UPE R3 : C25/30 (METAL / LINTEAU).",
    ], "Nomenclature")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_METAL_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("METAL")
    dxf_building(msp, "METAL")
    for rec in FRANGEMENTS + RENFORTS:
        msp.add_line((rec[1] * 10, rec[2] * 10), (rec[3] * 10, rec[4] * 10),
                     dxfattribs={"layer": "METAL-OUVRAGE"})
    return dxf_save(doc, base, "METAL")


def plan_linteau():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  LINTEAUX  —  Ind. B  —  21/10/2026",
                "S275  ·  F1 = 2×HEA 200  ·  R3 = UPE 200 rempli C25/30")
    draw_building(ax)
    watermark(ax)
    for rec in FRANGEMENTS:
        if rec[0].startswith("F1"):
            beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], ROUGE, rec[0])
    for rec in RENFORTS:
        if rec[0].startswith("R3"):
            beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], ROUGE, rec[0])
    # sommiers S1 R3
    for x0, y0, x1, y1, lab in [
        (8547.5, 5798.6, 8567.5, 5834.1, "S1"),
        (8547.5, 5584.2, 8567.5, 5619.7, "S1"),
        (8547.5, 5222.5, 8567.5, 5258.0, "S1"),
        (8547.5, 5007.9, 8567.5, 5043.7, "S1"),
    ]:
        rect_m(ax, m(x0), m(y0), m(x1), m(y1), VERT, None, alpha=0.9)

    axc.set_xlim(-0.2, 2.4)
    axc.set_ylim(-0.4, 1.3)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("Coupe R3  —  UPE 200 + béton  ·  1/10", fontsize=9, loc="left")
    # UPE schématique
    axc.plot([0.05, 0.05, 0.25, 0.25], [0.90, 0.10, 0.10, 0.90], color=BLEU, lw=2.2)
    axc.plot([0.05, 0.28], [0.90, 0.90], color=BLEU, lw=2.2)
    axc.plot([0.05, 0.28], [0.10, 0.10], color=BLEU, lw=2.2)
    axc.add_patch(Rectangle((0.06, 0.12), 0.16, 0.76, fc="#F3D1B0", ec=ORANGE, lw=0.6, hatch="///"))
    axc.text(0.40, 0.55, "UPE 200\nrempli C25/30\n(sans béton : τ = 1,40)", fontsize=8, color=NOIR)
    axc.text(0.40, 0.15, "L = 1,55 m  ·  2 appuis S1\nE-08 bois court-circuité", fontsize=7.5, color=GRIS_F)

    nom_table(axn, [
        "Rep.    Profil           L        Appuis",
        "F1a     2×HEA 200      1,00 m    S2 + J1",
        "F1b     2×HEA 200      0,90 m    S2 + P3",
        "F1c     2×HEA 200      0,85 m    2×S2",
        "R3-N    UPE 200 + B    1,55 m    2×S1",
        "R3-S    UPE 200 + B    1,55 m    2×S1",
        "",
        "Seuils BA : SANS OBJET.",
        "Linteaux bois existants : hors lot (non prescrit).",
        "S1 sur abouts de mur, hors bois.",
    ], "Nomenclature")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  coupe 1/10  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_LINTEAU_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("LINTEAU")
    dxf_building(msp, "LINTEAU")
    return dxf_save(doc, base, "LINTEAU")


def plan_macon():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  COUSSINS D'APPUI  —  Ind. B  —  21/10/2026",
                "C25/30  ·  w_b = 300 mm mini  ·  6 appuis sous R1 / F2 / F3")
    draw_building(ax)
    watermark(ax)
    for rec in FRANGEMENTS:
        if rec[0] in ("F2", "F3"):
            beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], GRIS, rec[0])
    beam(ax, 8547.5, 5488.7, 8969.8, 5488.7, 0.26, GRIS, "R1")
    for name, x0, y0, x1, y1 in COUSSINS:
        rect_m(ax, m(x0), m(y0), m(x1), m(y1), VERT, None)
        ax.text(m((x0 + x1) / 2), m((y0 + y1) / 2), name.replace("C-", ""),
                ha="center", va="center", fontsize=6, color="white", fontweight="bold", zorder=6)

    axc.set_xlim(-0.15, 1.8)
    axc.set_ylim(-0.25, 1.05)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("Coussin type  ·  1/10", fontsize=9, loc="left")
    axc.add_patch(Rectangle((0.05, 0.05), 0.30, 0.20, fc="#C5E1C5", ec=VERT, lw=1.2, hatch="///"))
    axc.add_patch(Rectangle((0.08, 0.25), 0.16, 0.12, fc=BLEU, ec=BLEU, lw=0.8, alpha=0.8))
    axc.annotate("", xy=(0.05, -0.05), xytext=(0.35, -0.05),
                 arrowprops=dict(arrowstyle="<->", color=NOIR, lw=0.7))
    axc.text(0.20, -0.10, "w_b = 300 mm MINI", ha="center", fontsize=8, fontweight="bold")
    axc.text(0.50, 0.45, "h = 200 mm  C25/30\n4 HA8\nmortier complet\ne ≤ t/4 du nu de mur", fontsize=8)

    nom_table(axn, [
        "Rep.      Sous     V_Ed     Section",
        "C-R1-O/E  R1      77,4 kN   300×500×200",
        "C-F2-O/E  F2      62,4 kN   300×400×200",
        "C-F3-O/E  F3      61,6 kN   300×400×200",
        "TOTAL  6 coussins.  Ne pas réduire w_b.",
        "",
        "F1 / R3 : S1 200 mm suffisent — pas de coussin.",
        "R2 / F4 : OK sans coussin.",
        "Ce ne sont PAS des linteaux.",
    ], "Nomenclature")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  détail 1/10  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_MACON_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("MACON")
    dxf_building(msp, "MACON")
    return dxf_save(doc, base, "MACON")


def plan_charpente():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  CHARPENTE BOIS NEUVE  —  Ind. B  —  21/10/2026",
                "C24  ·  service 2  ·  demi-fermes désolidarisées du plancher  ·  E-07 non chargé")
    draw_building(ax)
    watermark(ax)
    for rec in PANNES:
        beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], MARRON, rec[0])
    for rec in DF:
        beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5], MARRON, rec[0])
    beam(ax, CF[1], CF[2], CF[3], CF[4], CF[5], MARRON, "CF")
    for name, x0, y0, x1, y1 in ZN:
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=ROUGE, alpha=0.12,
                               ec=ROUGE, lw=1.0, ls="--", hatch="xxx", zorder=2))
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, name + "\nNON RELEVÉE\n— hors calcul",
                ha="center", va="center", fontsize=8, color=ROUGE, fontweight="bold", zorder=3)

    axc.set_xlim(-0.3, 3.8)
    axc.set_ylim(-0.3, 2.2)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("Demi-ferme  ·  schéma  ·  C24", fontsize=9, loc="left")
    axc.plot([0.1, 3.3], [0.15, 0.15], color=MARRON, lw=3.2)  # entrait
    axc.plot([0.1, 3.3], [0.15, 1.85], color=MARRON, lw=3.2)  # arb
    axc.text(1.6, 0.00, "entrait  75×200   taux 0,108", ha="center", fontsize=7, color=MARRON)
    axc.text(1.9, 1.15, "arbalétrier  100×200   0,626", fontsize=7, color=MARRON, rotation=28)
    axc.text(0.1, 1.95, "Appuis murs Files A et C  —  pas le plancher", fontsize=7.5, color=GRIS_F)

    nom_table(axn, [
        "Rep.   Section          L       Taux max",
        "PN1/2/3  75×200 C24    3,20 m    0,830  (flèche)",
        "DF-arb   100×200 C24   3,62 m    0,626",
        "DF-ent   75×200 C24    3,20 m    0,108",
        "CF       75×225 C24    2,62 m    0,940  (flambement)",
        "",
        "Contreventement de toiture : absent au D2 — non inventé.",
        "Sabots : non catalogués — non inventés.",
        "ZN1 / ZN2 : relevé avant toute taille.",
    ], "Nomenclature")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_CHARPENTE_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("CHARPENTE")
    dxf_building(msp, "CHARPENTE")
    return dxf_save(doc, base, "CHARPENTE")


def plan_assemblage():
    fig, ax, axc, axn = new_fig()
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "PLAN D'EXÉCUTION  —  ASSEMBLAGES  —  Ind. B  —  21/10/2026",
                "A1 ancrage  ·  A2 moisage  ·  A5 platine  ·  A4 non chiffré")
    draw_building(ax)
    watermark(ax)
    # repères
    ax.plot(95.35, 59.29, "s", ms=10, color=VIOLET)
    ax.text(95.55, 59.29, "A1  P2 / SF1", fontsize=8, color=VIOLET, fontweight="bold")
    ax.plot(87.6, 54.89, "s", ms=10, color=VIOLET)
    ax.text(87.8, 55.15, "A2  R1  10 M16", fontsize=8, color=VIOLET, fontweight="bold")
    ax.plot(95.40, 49.04, "s", ms=10, color=VIOLET)
    ax.text(94.1, 49.2, "A5  P1", fontsize=8, color=VIOLET, fontweight="bold")
    ax.plot(92.6, 58.0, "s", ms=10, color=ROUGE)
    ax.text(92.8, 58.2, "A4  Stab1  NON CHIFFRÉ", fontsize=8, color=ROUGE, fontweight="bold")

    axc.set_xlim(-0.2, 2.6)
    axc.set_ylim(-0.3, 1.6)
    axc.set_aspect("equal")
    axc.axis("off")
    axc.set_title("A2  —  moisage R1  ·  10 M16 8.8  ·  1/10", fontsize=9, loc="left")
    axc.add_patch(Rectangle((0.15, 0.25), 0.08, 0.70, fc=MARRON, ec=MARRON, lw=0.8))
    axc.add_patch(Rectangle((0.05, 0.20), 0.08, 0.80, fc=BLEU, ec=BLEU, lw=0.8, alpha=0.85))
    axc.add_patch(Rectangle((0.25, 0.20), 0.08, 0.80, fc=BLEU, ec=BLEU, lw=0.8, alpha=0.85))
    for y in (0.35, 0.50, 0.65, 0.80, 0.95):
        axc.plot([0.05, 0.33], [y, y], color=NOIR, lw=1.1)
    axc.text(0.50, 0.70, "2×UPE 200  +  bois 15×20\n10 M16 cl. 8.8 / face\ntaux 0,69  —  le bois gouverne",
             fontsize=8)

    nom_table(axn, [
        "Rep.  Assemblage                         Verdict",
        "A1    6 HA12 dans SF1  l_bd 166 mm         OK",
        "A2    10 M16 8.8  moisage R1              OK 0,69",
        "A3    torsion UPE R3           CLOSE (béton D-36)",
        "A4    scellement Stab1 M12          NON CHIFFRÉ",
        "A5    platine P1 200×200                 OK 0,12",
        "A6    appuis maçonnerie  →  coussins MACON",
        "",
        "Sabots DF / PN : non catalogués — non inventés.",
        "A4 : 8 tiges non commandables tant que fiche absente.",
    ], "Nomenclature  —  NE PAS COMMANDER SANS VISA")
    fig.text(0.03, 0.02, "Échelle plan ~1/100  ·  Ind. B remplace Ind. A (présentation, aucun chiffre modifié)",
             fontsize=7, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_ASSEMBLAGE_EXE_IndB")
    save(fig, base)
    doc, msp = dxf_new("ASSEMBLAGE")
    dxf_building(msp, "ASSEMBLAGE")
    return dxf_save(doc, base, "ASSEMBLAGE")


def plan_ensemble():
    """Vue de lecture — tous les neufs sur RDC. PAS un EXE fusionné."""
    fig = plt.figure(figsize=(16.54, 11.69), facecolor="white")
    ax = fig.add_axes([0.04, 0.07, 0.92, 0.84])
    ax.set_aspect("equal")
    ax.set_xlim(OUTER[0] - 1.2, OUTER[2] + 1.4)
    ax.set_ylim(OUTER[1] - 1.0, OUTER[3] + 1.0)
    ax.axis("off")
    title_block(fig,
                "EHPAD LA ROSERAIE  —  PAVILLON FLORA  —  CROISSY-SUR-SEINE",
                "VUE D'ENSEMBLE DE LECTURE  —  OUVRAGES NEUFS SUR RDC  —  Ind. B",
                "LECTURE — NE PAS EXÉCUTER   ·   un type = un plan EXE (FOND, VERT, PLANCHER, LINTEAU, MACON, METAL)")
    draw_building(ax, show_axes=True)
    ax.text(0.50, 0.50, "LECTURE — NE PAS EXÉCUTER", transform=ax.transAxes,
            fontsize=26, color=ROUGE, alpha=0.08, ha="center", va="center", rotation=25,
            fontweight="bold", zorder=0)
    # dallage léger
    x0, y0, x1, y1 = OUTER
    ax.add_patch(Rectangle((x0 + 0.08, y0 + 0.08), x1 - x0 - 0.16, y1 - y0 - 0.16,
                           fc="#F5CBA7", alpha=0.18, ec="none", zorder=1))
    for rec in FRANGEMENTS:
        beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5],
             ROUGE if rec[0].startswith("F1") else BLEU, rec[0])
    for rec in RENFORTS:
        beam(ax, rec[1], rec[2], rec[3], rec[4], rec[5],
             ROUGE if rec[0].startswith("R3") else BLEU, rec[0])
    for name, x0b, y0b, x1b, y1b, sec, fer in P_BA:
        rect_m(ax, m(x0b), m(y0b), m(x1b), m(y1b), VERT, name)
    for name, xc, yc, cote, prof in P1:
        rect_m(ax, m(xc) - 0.18, m(yc) - 0.18, m(xc) + 0.18, m(yc) + 0.18, VIOLET, None)
        ax.text(m(xc) + 0.35, m(yc), name, fontsize=8, color=VIOLET, fontweight="bold",
                va="center", path_effects=stroke())
    xc, yc, B = SF1
    rect_m(ax, xc - B / 2, yc - B / 2, xc + B / 2, yc + B / 2, ORANGE, "SF1")
    for name, x0c, y0c, x1c, y1c in COUSSINS:
        rect_m(ax, m(x0c), m(y0c), m(x1c), m(y1c), VERT, None, alpha=0.7)
    fig.text(0.04, 0.02,
             "Légende : orange = fondations  ·  vert = BA / coussins  ·  bleu = profilés  ·  rouge = linteaux  ·  violet = P1  ·  saumon = dallage.  Charpente : plan CHARPENTE (R+1).",
             fontsize=7.5, color=GRIS_F)
    base = os.path.join(PLANS, "FLORA_B60_ENSEMBLE_LECTURE_IndB")
    save(fig, base)
    doc, msp = dxf_new("ENSEMBLE")
    dxf_building(msp, "ENSEMBLE")
    dxf_txt(msp, OUTER[0] * 1000, (OUTER[3] + 0.9) * 1000,
            "LECTURE — NE PAS EXECUTER — ensemble RDC Ind.B", 200, "ENSEMBLE-CARTOUCHE")
    return dxf_save(doc, base, "ENSEMBLE")


def main():
    log("B-60 PRÉSENTATION Ind. B — CROISSY-FLORA")
    log("Mêmes chiffres. Fond blanc. Implantation obligatoire.")
    results = {}
    for name, fn in [
        ("FOND", plan_fond),
        ("VERT", plan_vert),
        ("PLANCHER", plan_plancher),
        ("METAL", plan_metal),
        ("LINTEAU", plan_linteau),
        ("MACON", plan_macon),
        ("CHARPENTE", plan_charpente),
        ("ASSEMBLAGE", plan_assemblage),
        ("ENSEMBLE", plan_ensemble),
    ]:
        path, nerr, n0, npre, cnt = fn()
        results[name] = {"dxf": path, "audit": nerr, "layer0": n0, "n": npre}
        log("  %-12s  audit=%d  calque0=%d  entités préfixe=%d" % (name, nerr, n0, npre))
    jp = os.path.join(OUT, "b60_presentation.json")
    with open(jp, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "b60_presentation.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log("Journal : %s" % jp)


if __name__ == "__main__":
    main()
