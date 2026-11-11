"""
Petite bibliothèque de détails d'armatures et d'assemblages.

Complète `plan_engine` pour les planches de détail (PL-04 et PL-05) où les
cotes sont posées **en centimètres modèle** avec des décalages adaptés aux
échelles 1/10 et 1/20 (à 1/10, 1 cm modèle = 1 mm papier).
"""
from __future__ import annotations

import math

import plan_engine as E


# ---------------------------------------------------------------------------
# Cotation lisible aux grandes échelles
# ---------------------------------------------------------------------------

def cote_h(sc, x1, x2, y, label, fs=2.2, ext=2.5, layer=None):
    """Cote horizontale : ligne + traits + texte au-dessus (décalage 1,0 cm)."""
    layer = layer or E.CALQUE_AXES
    sc.line(x1, y, x2, y, layer, 0.18)
    for x in (x1, x2):
        sc.line(x, y - ext * 0.45, x, y + ext * 0.45, layer, 0.25)
        sc.line(x - 0.8, y - 0.8, x + 0.8, y + 0.8, layer, 0.25)
    sc.text(label, (x1 + x2) / 2.0, y + 1.2, fs, layer, "center")


def cote_v(sc, y1, y2, x, label, fs=2.2, ext=2.5, layer=None, side="left"):
    """Cote verticale : texte posé horizontalement à côté de la ligne."""
    layer = layer or E.CALQUE_AXES
    sc.line(x, y1, x, y2, layer, 0.18)
    for y in (y1, y2):
        sc.line(x - ext * 0.45, y, x + ext * 0.45, y, layer, 0.25)
        sc.line(x - 0.8, y - 0.8, x + 0.8, y + 0.8, layer, 0.25)
    dx = -1.0 if side == "left" else 1.0
    sc.text(label, x + dx, (y1 + y2) / 2.0 - 0.7, fs, layer,
            "right" if side == "left" else "left")


def bulle(sc, x, y, txt, r=4.0, fs=2.2, layer=None):
    """Pastille de repère cerclée."""
    layer = layer or E.CALQUE_AXES
    sc.circle(x, y, r, layer, 0.25)
    sc.line(x - r, y, x + r, y, layer, 0.13)
    sc.text(txt, x, y - 0.8, fs, layer, "center", bold=True)


# ---------------------------------------------------------------------------
# Barres et façonnage
# ---------------------------------------------------------------------------

def barre(sc, pts, label=None, lw=0.35, layer="STR_FERRAILLAGE",
          hook_start=None, hook_end=None, crochet=8.0, fs=2.0,
          label_dy=0.9, label_align="left"):
    """Trace une barre (polyligne) avec crochets optionnels à ses extrémités.

    `hook_start` / `hook_end` : angle en degrés du retour de crochet.
    """
    sc.poly(pts, layer, lw, closed=False)
    if hook_start is not None:
        (x0, y0), (x1, y1) = pts[0], pts[1]
        a = math.radians(hook_start)
        sc.line(x0, y0, x0 - crochet * math.cos(a),
                y0 - crochet * math.sin(a), layer, lw)
    if hook_end is not None:
        (x0, y0), (x1, y1) = pts[-1], pts[-2]
        a = math.radians(hook_end)
        sc.line(x0, y0, x0 - crochet * math.cos(a),
                y0 - crochet * math.sin(a), layer, lw)
    if label:
        sc.text(label, pts[0][0], pts[0][1] + label_dy, fs, layer,
                label_align)


def etrier(sc, x, y, w, h, lw=0.30, layer="STR_FERRAILLAGE",
           retour=6.0, angle=135.0):
    """Cadre/étrier rectangulaire avec deux retours d'angle."""
    sc.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], layer, lw,
            closed=True)
    a = math.radians(angle)
    sc.line(x + w - retour, y + h, x + w - retour + retour * math.cos(a),
            y + h - abs(retour * math.sin(a)), layer, lw)
    sc.line(x + retour, y, x + retour - retour * math.cos(a),
            y + abs(retour * math.sin(a)), layer, lw)


def point_barre(sc, cx, cy, d, layer="STR_FERRAILLAGE"):
    """Section d'une barre : cercle plein (hachuré)."""
    sc.dia(cx, cy, d, layer, 0.22)
    sc.circle(cx, cy, d * 0.30, layer, 0.13)


# ---------------------------------------------------------------------------
# Béton : contour + hachure béton armé
# ---------------------------------------------------------------------------

def beton(sc, pts, hatch=True, lw=0.45, sp=0.9):
    sc.poly(pts, "STR_COFFRAGE_BA", lw, closed=True)
    if hatch:
        sc.hatch_poly(pts, "STR_COFFRAGE_BA", 45.0, sp)


def beton_rect(sc, x, y, w, h, hatch=True, lw=0.45, sp=0.9):
    sc.rect(x, y, w, h, "STR_COFFRAGE_BA", lw, hatch="ANSI31" if hatch else
            None, angle=45.0, spacing=sp)


# ---------------------------------------------------------------------------
# Lignes de rupture / coupes partielles
# ---------------------------------------------------------------------------

def ligne_rupture(sc, x, y1, y2, amp=2.2, n=7, layer=None):
    """Ligne de rupture en zigzag vertical en x."""
    layer = layer or E.CALQUE_AXES
    pts = []
    for i in range(n + 1):
        yy = y1 + (y2 - y1) * i / n
        pts.append((x + (amp if i % 2 else -amp), yy))
    sc.poly(pts, layer, 0.18, closed=False)


def cotation_axe(sc, x, y1, y2, txt, layer=None):
    """Ligne d'axe avec bulle en haut."""
    layer = layer or E.CALQUE_AXES
    sc.line(x, y1, x, y2, layer, 0.13)
    sc.circle(x, y2, 4.0, layer, 0.25)
    return x
