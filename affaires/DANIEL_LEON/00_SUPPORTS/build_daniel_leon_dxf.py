#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Retranscription DXF — Permis de construire « Monsieur et Madame DANIEL LEON »
Lotissement CHANTE CIGALE L.T 77 — GUJAN-MESTRAS (Gironde)
« Construction d'une résidence principale » — Plan / Coupe / Surfaces
Échelle d'origine : 0.02 P.M. (= 1/50) — Entreprise GRAND, Le Canon (33)

SOURCE
  reproduction photographique « WhatsApp Image 2026-08-29 at 10.02.24.jpeg »
  (1554 x 2048 px, planche pliée, légèrement déformée).

MÉTHODE (100 % local : OpenCV + ezdxf, aucun appel réseau)
  1. calage pixel -> mètre par les cotes d'ensemble lues (15.00 m x 7.00 m) ;
  2. relevé des faces de murs par profils d'encre (colonnes/lignes) ;
  3. reconstruction d'un réseau de murs dont les surfaces recalculées
     retrouvent celles du cartouche :
        GARAGE      3.00 x 6.66 = 19.98 m2   (cartouche : 19.98)  exact
        CHAMBRE 1   3.50 x 3.38 = 11.83 m2   (cartouche : 11.83)  exact
        CUISINE     3.50 x 3.00 = 10.50 m2   (cartouche : 10.50)  exact
        PLACARD     0.60 x 1.60 =  0.96 m2   (cartouche :  0.96)  exact
        W.C.        0.85 x 1.60 =  1.36 m2   (cartouche :  1.36)  exact
        ESCALIER    0.90 x 2.70 =  2.43 m2   (cartouche :  2.43)  exact
        ENTREE      2.75 x 3.24 =  8.91 m2   (cartouche :  8.91)  exact
     => le calage est verrouillé par 7 surfaces indépendantes.
  4. écriture DXF (ezdxf, AC1027/R2013, mm, calques normalisés, cotes
     associatives, cartouche, mise en page A1 au 1/50).

Sortie : DANIEL_LEON_PC1975_PLAN_COUPE_SURFACES_v2.dxf
Usage  : python build_daniel_leon_dxf.py [--out DOSSIER]
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import ezdxf
from ezdxf.enums import TextEntityAlignment

MM = 1000.0


def m(v: float) -> float:
    """mètres -> millimètres (unités du DXF)."""
    return round(v * MM, 3)


# ===========================================================================
# 1. GÉOMÉTRIE (mètres ; origine = angle sud-ouest extérieur du bâtiment)
# ===========================================================================
# --- Réseau vertical X ----------------------------------------------------
#  |17| 3.00 |17| 3.50 |7|60|7| 85 |7| 2.00 |7| 4.18 |25|   = 15.00 m
X_W0, X_W1 = 0.00, 0.17          # mur ouest
X_G0, X_G1 = 3.17, 3.34          # refend garage / chambre 1 + cuisine
X_C0, X_C1 = 6.84, 6.91          # cloison chambre 1 / cuisine / entrée
X_R0, X_R1 = 6.91, 7.51          # rangement 1.60 (chambre 1)
X_A0, X_A1 = 7.51, 7.58          # cloison rangement / W.C.
X_WC0, X_WC1 = 7.58, 8.43        # W.C. (0.85)
X_B0, X_B1 = 8.50, 10.50         # bains (2.00)
X_S0, X_S1 = 10.50, 10.57        # cloison bains / séjour (0.07)
X_E0, X_E1 = 14.75, 15.00        # mur est (séjour haut 4.18)
X_EN0, X_EN1 = 9.66, 9.76        # cloison entrée / séjour bas
X_ESC0, X_ESC1 = 8.72, 9.62      # escalier (0.90, 14 marches)

# --- Réseau horizontal Y --------------------------------------------------
Y_S0, Y_S1 = 0.00, 0.17          # mur sud
Y_N0, Y_N1 = 6.83, 7.00          # mur nord (6.66 = 7.00 - 2 x 0.17)
Y_CUI1 = 3.17                    # face nord cuisine   (3.00 -> 10.50 m2)
Y_C1S = 3.45                     # face sud chambre 1  (3.38 -> 11.83 m2)
Y_BA0, Y_BA1 = 4.05, 4.12        # cloison sud bains (2.71 de profondeur)
Y_PL0 = 5.23                     # rangement/W.C. (1.60)
Y_VES0, Y_VES1 = 4.15, 5.23      # vestiaire + placard 0.50
Y_EN1 = 3.46                     # face nord entrée (3.29)

# --- TERRASSE en L : 2.00 m au sud, 1.30 m à l'est ------------------------
T_X0, T_X1 = 6.55, 16.30
T_Y0, T_Y1 = -2.00, 0.00
TE_X0, TE_X1 = 15.00, 16.30
TE_Y0, TE_Y1 = -2.00, 7.00    # retour est sur toute la profondeur

# --- Coupe A-B : niveaux ---------------------------------------------------
Z_TN = 0.00          # terre-plein naturel
Z_TER = 0.12         # dallage terrasse
Z_RDC = 0.30         # plancher rez-de-chaussée
Z_PLA = 2.80         # sous-face plafond RDC
Z_GRE = 2.92         # plancher grenier
Z_EGO = 2.35         # égout ouest (débord au-dessus de la terrasse)
Z_EGD = 4.40         # égout est (pente 0.30)
Z_FAI = 6.00         # faîtage (pente 0.30 p.m.)
X_EGO = -1.90
X_EGD = 15.70
X_FAI = 10.30

LAYERS = {
    "MURS_EXT":   (7, 50),
    "CLOISONS":   (7, 35),
    "HACHURES":   (8, 13),
    "OUVERTURES": (1, 25),
    "MENUISERIES":(4, 25),
    "ESCALIER":   (3, 25),
    "SANITAIRES": (5, 18),
    "TERRASSE":   (3, 18),
    "COTES":      (2, 18),
    "TEXTES":     (7, 18),
    "AXES":       (1, 13),
    "COUPE":      (7, 35),
    "CARTOUCHE":  (7, 25),
    "TABLEAU":    (7, 18),
}


def setup(doc):
    for name, (color, lw) in LAYERS.items():
        if name not in doc.layers:
            lay = doc.layers.add(name, color=color)
            lay.dxf.lineweight = int(lw)
    doc.header["$INSUNITS"] = 4
    doc.header["$MEASUREMENT"] = 1
    doc.header["$LUNITS"] = 2
    doc.header["$LUPREC"] = 2
    ds = doc.dimstyles
    st = ds.new("ARCH50")
    st.dxf.dimtxt = m(0.14)
    st.dxf.dimasz = m(0.09)
    st.dxf.dimexe = m(0.14)
    st.dxf.dimexo = m(0.07)
    st.dxf.dimgap = m(0.05)
    st.dxf.dimdec = 2
    st.dxf.dimdli = m(0.28)
    st.dxf.dimtad = 1
    st.dxf.dimtih = 0
    st.dxf.dimtoh = 0
    st.dxf.dimlunit = 2
    st.dxf.dimclrd = 2
    st.dxf.dimclre = 2
    st.dxf.dimclrt = 7
    st.dxf.dimblk = "ARCHTICK"
    return doc


# ===========================================================================
# 2. Primitives
# ===========================================================================
def poly(msp, pts, layer, closed=True):
    return msp.add_lwpolyline([(m(x), m(y)) for x, y in pts],
                              dxfattribs={"layer": layer}, close=closed)


def line(msp, p1, p2, layer):
    msp.add_line((m(p1[0]), m(p1[1])), (m(p2[0]), m(p2[1])),
                 dxfattribs={"layer": layer})


def solid(msp, pts, layer="HACHURES", color=8):
    h = msp.add_hatch(color=color, dxfattribs={"layer": layer})
    h.set_solid_fill(color=color)
    h.paths.add_polyline_path([(m(x), m(y)) for x, y in pts], is_closed=True)
    return h


def txt(msp, s, x, y, h=0.15, layer="TEXTES", align="LEFT", rot=0.0):
    t = msp.add_text(s, dxfattribs={"layer": layer, "height": m(h),
                                    "rotation": rot})
    t.set_placement((m(x), m(y)), align=TextEntityAlignment[align])
    return t


# ===========================================================================
# 3. Murs + baies
# ===========================================================================
def wall(msp, x0, y0, x1, y1, openings=(), layer="CLOISONS", hatch=True):
    horiz = (x1 - x0) >= (y1 - y0)
    a0, a1 = (x0, x1) if horiz else (y0, y1)
    segs, cur = [], a0
    for o0, o1 in sorted(openings):
        o0, o1 = max(a0, o0), min(a1, o1)
        if o0 > cur:
            segs.append((cur, o0))
        cur = max(cur, o1)
    if cur < a1:
        segs.append((cur, a1))
    for s0, s1 in segs:
        if s1 - s0 < 1e-6:
            continue
        pts = ([(s0, y0), (s1, y0), (s1, y1), (s0, y1)] if horiz
               else [(x0, s0), (x1, s0), (x1, s1), (x0, s1)])
        poly(msp, pts, layer)
        if hatch:
            solid(msp, pts, "HACHURES", 8)


def jambs(msp, x0, y0, x1, y1, o0, o1, layer="OUVERTURES"):
    if (x1 - x0) >= (y1 - y0):
        line(msp, (o0, y0), (o0, y1), layer)
        line(msp, (o1, y0), (o1, y1), layer)
    else:
        line(msp, (x0, o0), (x1, o0), layer)
        line(msp, (x0, o1), (x1, o1), layer)


def window(msp, x0, y0, x1, y1, o0, o1):
    """Baie vitrée : 2 vitrages + tableau."""
    jambs(msp, x0, y0, x1, y1, o0, o1)
    if (x1 - x0) >= (y1 - y0):
        th = y1 - y0
        for f in (0.30, 0.44, 0.62, 0.76):
            line(msp, (o0, y0 + th * f), (o1, y0 + th * f), "MENUISERIES")
    else:
        th = x1 - x0
        for f in (0.30, 0.44, 0.62, 0.76):
            line(msp, (x0 + th * f, o0), (x0 + th * f, o1), "MENUISERIES")


def door(msp, hinge, width, closed_dir, swing_dir, layer="MENUISERIES"):
    hx, hy = hinge
    ox, oy = hx + swing_dir[0] * width, hy + swing_dir[1] * width
    line(msp, (hx, hy), (ox, oy), layer)
    a0 = math.degrees(math.atan2(closed_dir[1], closed_dir[0]))
    a1 = math.degrees(math.atan2(swing_dir[1], swing_dir[0]))
    while a1 - a0 > 180:
        a1 -= 360
    while a0 - a1 > 180:
        a1 += 360
    msp.add_arc((m(hx), m(hy)), m(width), a0, a1, dxfattribs={"layer": layer})


def double_door(msp, x0, x1, y, normal, layer="MENUISERIES"):
    w = (x1 - x0) / 2.0
    door(msp, (x0, y), w, (1, 0), normal, layer)
    door(msp, (x1, y), w, (-1, 0), normal, layer)


# ===========================================================================
# 4. Cotation
# ===========================================================================
def dim_h(msp, x1, x2, y, off=0.0):
    msp.add_linear_dim(base=(m(x1), m(y + off)), p1=(m(x1), m(y)),
                       p2=(m(x2), m(y)), dimstyle="ARCH50",
                       dxfattribs={"layer": "COTES"}).render()


def dim_v(msp, y1, y2, x, off=0.0):
    msp.add_linear_dim(base=(m(x + off), m(y1)), p1=(m(x), m(y1)),
                       p2=(m(x), m(y2)), angle=90, dimstyle="ARCH50",
                       dxfattribs={"layer": "COTES"}).render()


def chain(msp, vals, fixed, off, horizontal=True):
    cur = 0.0
    for v in vals:
        if horizontal:
            dim_h(msp, cur, cur + v, fixed, off)
        else:
            dim_v(msp, cur, cur + v, fixed, off)
        cur += v


# ===========================================================================
# 5. SURFACES (calcul géométrique, pour contrôle du cartouche)
# ===========================================================================
def surfaces():
    garage = (X_G0 - X_W1) * (Y_N0 - Y_S1)
    chambre1 = (X_C0 - X_G1) * (Y_N0 - Y_C1S)
    cuisine = (X_C0 - X_G1) * (Y_CUI1 - Y_S1)
    rangement = (X_R1 - X_R0) * (Y_N0 - Y_PL0)
    wc = (X_WC1 - X_WC0) * (Y_N0 - Y_PL0)
    # bains : 2.00 x 2.68 + 1.00 x 1.74 = 7.10 m2 (cartouche 7.14)
    bains = (X_B1 - X_B0) * (Y_N0 - Y_BA1) + (X_S1 - X_B1) * (Y_N0 - Y_BA1)
    vestiaire = (X_WC1 - 7.52) * (Y_VES1 - Y_VES0)
    placard50 = (7.45 - X_C1) * 0.60
    entree = (X_EN0 - X_C1) * (Y_EN1 - Y_S1)
    escalier = (X_ESC1 - X_ESC0) * 2.70
    sej_bas = (X_E0 - X_EN1) * (Y_BA0 - Y_S1)   # 4.99 x 3.88 = 19.36
    sej_haut = (X_E0 - X_S1) * (Y_N0 - Y_BA1)   # 4.18 x 2.71 = 11.33
    # L : bande sud + retour est  (28.60 m2 au cartouche)
    terrasse = ((T_X1 - T_X0) * (T_Y1 - T_Y0)
                + (TE_X1 - TE_X0) * (TE_Y1 - T_Y1))
    return {
        "SEJOUR": sej_bas + sej_haut,          # 30.69 (cartouche 30.17)
        "ENTREE": entree,
        "DEGAGEMENT": (X_EN0 - X_C1) * (Y_VES0 - Y_EN1),
        "VESTIAIRE": vestiaire,
        "PL. 0.50": placard50,
        "BAINS": bains,
        "W.C.": wc,
        "CUISINE": cuisine,
        "CHAMBRE 1": chambre1,
        "RANGEMENT": rangement,
        "GARAGE": garage,
        "ESCALIER": escalier,
        "TERRASSE": terrasse,
    }


DOC_SURFACES = {          # valeurs lues au cartouche de la planche
    "SEJOUR": "30.17", "ENTREE": "8.91", "DEGAGEMENT": "1.89",
    "PL. 0.50": "0.30", "VESTIAIRE": "0.98", "BAINS": "7.14", "W.C.": "1.36",
    "CUISINE": "10.50", "CHAMBRE 1": "11.83", "RANGEMENT": "0.96",
    "GARAGE": "19.98", "TERRASSE": "28.60",
}


# ===========================================================================
# 6. PLAN
# ===========================================================================
def draw_terrasse(msp, ox=0.0, oy=0.0):
    def p(x, y):
        return x + ox, y + oy

    poly(msp, [p(T_X0, T_Y0), p(T_X1, T_Y0), p(T_X1, T_Y1), p(T_X0, T_Y1)],
         "TERRASSE")
    poly(msp, [p(TE_X0, TE_Y0), p(TE_X1, TE_Y0), p(TE_X1, TE_Y1),
               p(TE_X0, TE_Y1)], "TERRASSE")
    x = T_X0 + 1.00
    while x < T_X1 - 0.05:
        line(msp, p(x, T_Y0 + 0.10), p(x, T_Y1 - 0.02), "TERRASSE")
        x += 1.00
    y = T_Y0 + 1.00
    while y < TE_Y1 - 0.05:
        line(msp, p(TE_X0 + 0.10, y), p(TE_X1 - 0.05, y), "TERRASSE")
        y += 1.00
    txt(msp, "TERRASSE  28.60 m2", (T_X0 + T_X1) / 2 - 1.6 + ox, -0.85 + oy,
        0.17, "TEXTES", "CENTER")


def draw_plan(msp, ox=0.0, oy=0.0):
    def P(a, b):
        return a + ox, b + oy

    # ---------------- murs extérieurs ------------------------------------
    S_OPEN = [(0.55, 2.85),   # porte de garage 2.30
              (4.20, 5.60),   # fenêtre cuisine 1.40
              (7.05, 8.45),   # entrée : porte 2 vantaux 1.40
              (10.90, 12.30), # fenêtre séjour 1.40
              (12.95, 14.35)] # porte-fenêtre séjour 1.40
    N_OPEN = [(4.55, 5.95),   # fenêtre chambre 1   1.40
              (7.70, 8.30),   # fenêtre W.C.        0.60
              (9.20, 10.20)]  # fenêtre bains       1.00
    W_OPEN = [(6.00, 6.60)]   # porte de service garage 0.60
    E_OPEN = [(1.32, 2.72), (4.28, 5.68)]   # 2 châssis 1.40

    wall(msp, *P(0.00, 0.00), *P(15.00, 0.17), S_OPEN, "MURS_EXT")
    wall(msp, *P(0.00, 6.83), *P(15.00, 7.00), N_OPEN, "MURS_EXT")
    wall(msp, *P(0.00, 0.17), *P(0.17, 6.83), W_OPEN, "MURS_EXT")
    wall(msp, *P(14.75, 0.17), *P(15.00, 6.83), E_OPEN, "MURS_EXT")

    # ---------------- refends et cloisons --------------------------------
    wall(msp, *P(X_G0, Y_S1), *P(X_G1, Y_N0), [(1.10, 1.80)])       # garage
    wall(msp, *P(X_G1, Y_CUI1), *P(X_C0, Y_C1S))                    # cuis./ch.
    wall(msp, *P(X_C0, Y_S1), *P(X_C1, Y_N0), [(1.25, 1.95), (3.55, 4.25)])
    wall(msp, *P(X_R0, Y_PL0), *P(X_R1, Y_N0))                      # rangement
    wall(msp, *P(X_A0, Y_PL0), *P(X_A1, Y_N0))                      # rang./WC
    wall(msp, *P(X_WC0, Y_PL0), *P(X_WC1, Y_PL0 + 0.08), [(7.72, 8.32)])
    wall(msp, *P(X_WC1, Y_BA1), *P(X_B0, Y_N0), [(4.60, 5.30)])     # WC/bains
    wall(msp, *P(X_B0, Y_BA1), *P(X_S1, Y_BA1))                     # bains sud
    wall(msp, *P(X_S0, Y_BA1), *P(X_S1, Y_N0), [(5.55, 6.35)])      # bains/séjour
    wall(msp, *P(X_EN0, Y_S1), *P(X_EN1, Y_BA0), [(2.30, 3.25)])    # entrée/séj.
    wall(msp, *P(X_EN1, Y_BA0), *P(X_E0, Y_BA0 + 0.07), [(12.60, 13.20)])
    # vestiaire / placard 0.50
    wall(msp, *P(X_C1, Y_VES0), *P(X_WC0, Y_VES0), [(7.55, 8.25)])
    wall(msp, *P(7.45, Y_VES0), *P(7.52, Y_PL0))
    wall(msp, *P(X_C1, Y_VES0 + 0.60), *P(7.52, Y_VES0 + 0.67), [(7.05, 7.38)])
    wall(msp, *P(7.45, Y_PL0 - 0.07), *P(X_WC0, Y_PL0 - 0.07), [(7.60, 8.20)])

    # ---------------- menuiseries extérieures ----------------------------
    # garage : porte basculante 2.30
    line(msp, P(0.55, 0.03), P(2.85, 0.03), "MENUISERIES")
    line(msp, P(0.55, 0.14), P(2.85, 0.14), "MENUISERIES")
    for xx in (0.55, 1.70, 2.85):
        line(msp, P(xx, 0.00), P(xx, 0.17), "MENUISERIES")
    door(msp, P(0.17, 6.60), 0.60, (0, -1), (1, 0))
    window(msp, *P(0.00, 0.00), *P(15.00, 0.17), 4.20, 5.60)
    double_door(msp, 7.05 + ox, 8.45 + ox, 0.17 + oy, (0, 1))
    window(msp, *P(0.00, 0.00), *P(15.00, 0.17), 10.90, 12.30)
    double_door(msp, 12.95 + ox, 14.35 + ox, 0.17 + oy, (0, 1))
    window(msp, *P(0.00, 6.83), *P(15.00, 7.00), 4.55, 5.95)
    window(msp, *P(0.00, 6.83), *P(15.00, 7.00), 7.70, 8.30)
    window(msp, *P(0.00, 6.83), *P(15.00, 7.00), 9.20, 10.20)
    for a, b in E_OPEN:
        window(msp, *P(14.75, 0.17), *P(15.00, 6.83), a, b)
    # ébrasements
    for (o0, o1) in S_OPEN:
        jambs(msp, *P(0.00, 0.00), *P(15.00, 0.17), o0, o1)
    for (o0, o1) in N_OPEN:
        jambs(msp, *P(0.00, 6.83), *P(15.00, 7.00), o0, o1)
    for (o0, o1) in E_OPEN:
        jambs(msp, *P(14.75, 0.17), *P(15.00, 6.83), o0, o1)
    jambs(msp, *P(0.00, 0.17), *P(0.17, 6.83), *W_OPEN[0])

    # ---------------- portes intérieures ---------------------------------
    door(msp, P(7.45, Y_VES0 + 0.66), 0.54, (0, 1), (1, 0))   # placard 0.50
    door(msp, P(X_C1, 1.25), 0.70, (0, 1), (-1, 0))      # cuisine -> entrée
    door(msp, P(X_C1, 4.25), 0.70, (0, -1), (-1, 0))     # chambre 1
    door(msp, P(X_G1, 1.10), 0.70, (0, 1), (1, 0))       # garage -> cuisine
    door(msp, P(7.72, Y_PL0), 0.60, (1, 0), (0, 1))      # W.C.
    door(msp, P(X_B0, 5.30), 0.70, (0, -1), (-1, 0))     # bains
    door(msp, P(7.55, Y_VES0), 0.70, (1, 0), (0, 1))     # vestiaire
    door(msp, P(X_EN1, 2.28), 0.92, (0, 1), (1, 0))      # entrée -> séjour
    # rangement 1.60 de la chambre 1 : portes coulissantes
    line(msp, P(X_R0, 5.28), P(X_R0, 6.28), "MENUISERIES")
    line(msp, P(X_R1, 5.28), P(X_R1, 6.28), "MENUISERIES")
    line(msp, P(X_R0, 6.78), P(X_R1, 6.78), "MENUISERIES")

    # ---------------- escalier -------------------------------------------
    draw_stairs(msp, X_ESC0, X_ESC1, 0.90, 3.60, 14, ox, oy)

    # ---------------- équipements ----------------------------------------
    draw_fixtures(msp, ox, oy)

    # ---------------- textes de pièces -----------------------------------
    labels = [
        ("CHAMBRE 1", 5.09, 5.55, 0.24), ("11.83 m2", 5.09, 5.22, 0.14),
        ("CUISINE", 5.05, 2.30, 0.24), ("10.50 m2", 5.05, 1.98, 0.14),
        ("GARAGE", 1.65, 2.10, 0.28), ("19.98 m2", 1.65, 1.74, 0.16),
        ("ENTREE", 8.28, 1.62, 0.20), ("8.91 m2", 8.28, 1.34, 0.13),
        ("SEJOUR", 12.55, 2.70, 0.30), ("30.17 m2", 12.55, 2.30, 0.16),
        ("BAINS", 9.45, 5.55, 0.20), ("W.C.", 8.00, 5.55, 0.15),
        ("PL. 0.50", 7.18, 4.60, 0.10),
        ("DEGAGEMENT", 8.10, 3.86, 0.12),
        ("ESCALIER", 9.17, 1.95, 0.11),
        ("CHEMINEE", 10.05, 1.10, 0.12), ("COIN DE FEU", 10.05, 0.92, 0.12),
    ]
    for s, x, y, h in labels:
        txt(msp, s, x + ox, y + oy, h, "TEXTES", "CENTER")

    txt(msp, "Rangement 1.60", 7.21, 6.30, 0.11, "TEXTES", "CENTER", rot=90)
    txt(msp, "Vestiaire", 7.95, 4.69, 0.11, "TEXTES", "CENTER")
    txt(msp, "Conduit fumee de chauffage", 5.30, 6.30, 0.10, "TEXTES", "CENTER")
    txt(msp, "Poutre bois", 12.40, 4.34, 0.12, "TEXTES", "CENTER")
    txt(msp, "FENETRE 1.40", 14.87, 2.02, 0.10, "TEXTES", "CENTER", rot=90)
    txt(msp, "FENETRE 1.40", 14.87, 4.98, 0.10, "TEXTES", "CENTER", rot=90)
    draw_cut_line(msp, -1.20, 16.20, 1.60 + oy, labels=("A", "B"))
    txt(msp, "PLAN DU REZ-DE-CHAUSSEE", 7.60, -3.10 + oy, 0.32, "TEXTES",
        "CENTER")
    txt(msp, "ECHELLE 0.02 P.M. (1/50)", 7.60, -3.50 + oy, 0.15, "TEXTES",
        "CENTER")


def draw_cut_line(msp, x0, x1, y, labels=("A", "B")):
    """Trait de coupe avec ses extrémités renforcées."""
    layer = "AXES"
    msp.add_line((m(x0), m(y)), (m(x1), m(y)),
                 dxfattribs={"layer": layer, "linetype": "DASHDOT"})
    for x in (x0, x1):
        msp.add_line((m(x), m(y - 0.22)), (m(x), m(y + 0.22)),
                     dxfattribs={"layer": layer})
        msp.add_line((m(x), m(y - 0.22)), (m(x), m(y - 0.22)),
                     dxfattribs={"layer": layer})
    msp.add_solid([(m(x0), m(y - 0.10)), (m(x0), m(y + 0.10)),
                   (m(x0 - 0.28), m(y))], dxfattribs={"layer": layer})
    msp.add_solid([(m(x1), m(y - 0.10)), (m(x1), m(y + 0.10)),
                   (m(x1 + 0.28), m(y))], dxfattribs={"layer": layer})
    txt(msp, labels[0], x0 - 0.55, y - 0.07, 0.22, layer, "CENTER")
    txt(msp, labels[1], x1 + 0.55, y - 0.07, 0.22, layer, "CENTER")


def draw_stairs(msp, x0, x1, y0, y1, n, ox=0.0, oy=0.0):
    w = (y1 - y0) / n
    for i in range(n + 1):
        y = y0 + i * w
        line(msp, (x0 + ox, y + oy), (x1 + ox, y + oy), "ESCALIER")
    line(msp, (x0 + ox, y0 + oy), (x0 + ox, y1 + oy), "ESCALIER")
    line(msp, (x1 + ox, y0 + oy), (x1 + ox, y1 + oy), "ESCALIER")
    xm = (x0 + x1) / 2 + ox
    msp.add_line((m(xm), m(y0 + 0.12 + oy)), (m(xm), m(y1 - 0.22 + oy)),
                 dxfattribs={"layer": "ESCALIER"})
    msp.add_solid([(m(xm - 0.06), m(y1 - 0.34 + oy)),
                   (m(xm + 0.06), m(y1 - 0.34 + oy)),
                   (m(xm), m(y1 - 0.16 + oy))],
                  dxfattribs={"layer": "ESCALIER"})


def draw_fixtures(msp, ox=0.0, oy=0.0):
    T = m
    # W.C. : cuvette
    cx, cy = 8.00 + ox, 6.35 + oy
    msp.add_ellipse((T(cx), T(cy)), major_axis=(T(0.15), 0), ratio=0.72,
                    dxfattribs={"layer": "SANITAIRES"})
    poly(msp, [(cx - 0.20, cy + 0.15), (cx + 0.20, cy + 0.15),
               (cx + 0.17, cy + 0.30), (cx - 0.17, cy + 0.30)], "SANITAIRES")
    # BAINS : baignoire
    poly(msp, [(8.62 + ox, 6.02 + oy), (10.36 + ox, 6.02 + oy),
               (10.36 + ox, 6.76 + oy), (8.62 + ox, 6.76 + oy)], "SANITAIRES")
    poly(msp, [(8.70 + ox, 6.09 + oy), (10.28 + ox, 6.09 + oy),
               (10.28 + ox, 6.69 + oy), (8.70 + ox, 6.69 + oy)], "SANITAIRES")
    msp.add_circle((T(10.14 + ox), T(6.39 + oy)), T(0.035),
                   dxfattribs={"layer": "SANITAIRES"})
    # 2 vasques le long de la cloison est des bains
    for yy in (5.15, 4.62):
        msp.add_ellipse((T(10.22 + ox), T(yy + oy)), major_axis=(T(0.16), 0),
                        ratio=0.62, dxfattribs={"layer": "SANITAIRES"})
        poly(msp, [(10.36 + ox, yy - 0.17 + oy), (10.46 + ox, yy - 0.17 + oy),
                   (10.46 + ox, yy + 0.17 + oy), (10.36 + ox, yy + 0.17 + oy)],
             "SANITAIRES")
    # CUISINE : plan de travail + évier 2 bacs
    poly(msp, [(3.45 + ox, 2.82 + oy), (6.78 + ox, 2.82 + oy),
               (6.78 + ox, Y_CUI1 + oy), (3.45 + ox, Y_CUI1 + oy)],
         "SANITAIRES")
    for xx in (4.55, 5.15):
        poly(msp, [(xx + ox, 2.88 + oy), (xx + 0.55 + ox, 2.88 + oy),
                   (xx + 0.55 + ox, 3.12 + oy), (xx + ox, 3.12 + oy)],
             "SANITAIRES")
    # CHEMINEE « coin de feu »
    poly(msp, [(9.90 + ox, 0.90 + oy), (10.50 + ox, 0.90 + oy),
               (10.50 + ox, 3.90 + oy), (9.90 + ox, 3.90 + oy)], "MURS_EXT")
    solid(msp, [(9.90 + ox, 0.90 + oy), (10.50 + ox, 0.90 + oy),
                (10.50 + ox, 3.90 + oy), (9.90 + ox, 3.90 + oy)], "HACHURES", 8)
    poly(msp, [(9.90 + ox, 1.10 + oy), (10.28 + ox, 1.10 + oy),
               (10.28 + ox, 3.60 + oy), (9.90 + ox, 3.60 + oy)], "SANITAIRES")
    # conduit de fumée (chambre 1)
    poly(msp, [(4.75 + ox, 5.90 + oy), (5.10 + ox, 5.90 + oy),
               (5.10 + ox, 6.25 + oy), (4.75 + ox, 6.25 + oy)], "SANITAIRES")
    line(msp, (4.75 + ox, 5.90 + oy), (5.10 + ox, 6.25 + oy), "SANITAIRES")
    line(msp, (4.75 + ox, 6.25 + oy), (5.10 + ox, 5.90 + oy), "SANITAIRES")


def draw_cotes_plan(msp, ox=0.0, oy=0.0):
    # chaîne haute (celle de la planche)
    chain(msp, [0.17, 3.00, 0.17, 3.50, 0.07, 0.60, 0.07, 0.85, 0.07,
                2.00, 0.07, 4.18, 0.25], 7.00 + oy, 0.75)
    dim_h(msp, 0.00 + ox, 15.00 + ox, 7.00 + oy, 1.62)
    txt(msp, "15.00", 7.50 + ox, 8.80 + oy, 0.22, "COTES", "CENTER")

    # chaîne basse : baies du mur sud
    for a, b in [(0.00, 0.55), (0.55, 2.85), (2.85, 4.20), (4.20, 5.60),
                 (5.60, 7.05), (7.05, 8.45), (8.45, 10.90), (10.90, 12.30),
                 (12.30, 12.95), (12.95, 14.35), (14.35, 15.00)]:
        dim_h(msp, a + ox, b + ox, 0.00 + oy, -0.70)

    # chaîne gauche : profondeur
    for a, b in [(0.00, 0.17), (0.17, 3.17), (3.17, 3.45), (3.45, 4.15),
                 (4.15, 5.23), (5.23, 6.83), (6.83, 7.00)]:
        dim_v(msp, a + oy, b + oy, 0.00 + ox, -0.70)
    dim_v(msp, 0.00 + oy, 7.00 + oy, 0.00 + ox, -1.60)
    txt(msp, "7.00", -1.95 + ox, 3.50 + oy, 0.22, "COTES", "CENTER", rot=90)
    txt(msp, "6.66", -1.60 + ox, 3.50 + oy, 0.17, "COTES", "CENTER", rot=90)

    # chaîne droite : baies est
    for a, b in [(0.17, 1.32), (1.32, 2.72), (2.72, 4.28), (4.28, 5.68),
                 (5.68, 6.83)]:
        dim_v(msp, a + oy, b + oy, 15.00 + ox, 0.78)
    dim_v(msp, 0.00 + oy, 7.00 + oy, 15.00 + ox, 1.60)

    # terrasse
    dim_h(msp, T_X0 + ox, T_X1 + ox, T_Y0 + oy, -0.10)
    dim_v(msp, T_Y0 + oy, T_Y1 + oy, TE_X1 + ox, 0.10)
    dim_v(msp, T_Y1 + oy, 7.00 + oy, TE_X1 + ox, 0.90)


def draw_north(msp, cx, cy, r=0.65):
    msp.add_circle((m(cx), m(cy)), m(r), dxfattribs={"layer": "AXES"})
    msp.add_circle((m(cx), m(cy)), m(r * 0.52), dxfattribs={"layer": "AXES"})
    msp.add_solid([(m(cx - r * 0.26), m(cy + r * 0.08)),
                   (m(cx + r * 0.26), m(cy + r * 0.08)),
                   (m(cx), m(cy + r * 1.30))], dxfattribs={"layer": "AXES"})
    txt(msp, "NORD", cx, cy + r * 1.48, 0.16, "AXES", "CENTER")


# ===========================================================================
# 7. COUPE A-B
# ===========================================================================
def draw_coupe(msp, ox=0.0, oy=0.0):
    def P(x, z):
        return x + ox, z + oy

    def L(p1, p2, layer="COUPE"):
        line(msp, P(*p1), P(*p2), layer)

    # sol naturel + remblai
    L((-3.60, Z_TN), (18.80, Z_TN))
    x = -3.55
    while x < 18.8:
        L((x, Z_TN), (x + 0.14, Z_TN - 0.18))
        x += 0.34
    txt(msp, "TERRE-PLEIN NATUREL", 12.60 + ox, -0.40 + oy, 0.15, "TEXTES",
        "CENTER")
    txt(msp, "REMBLAI", 2.05 + ox, -0.36 + oy, 0.12, "TEXTES", "CENTER")
    txt(msp, "SEMELLES FILANTES", 6.20 + ox, -1.28 + oy, 0.12, "TEXTES",
        "CENTER")

    # terrasse couverte ouest (dalle + poteaux)
    poly(msp, [P(-2.45, Z_TN + 0.22), P(0.00, Z_TN + 0.22),
               P(0.00, Z_TER + 0.30), P(-2.45, Z_TER + 0.30)], "COUPE")
    solid(msp, [P(-2.45, Z_TN + 0.22), P(0.00, Z_TN + 0.22),
                P(0.00, Z_TER + 0.30), P(-2.45, Z_TER + 0.30)], "HACHURES", 8)
    for xp in (-1.85, -0.95):
        poly(msp, [P(xp, Z_TER + 0.30), P(xp + 0.14, Z_TER + 0.30),
                   P(xp + 0.14, 2.10), P(xp, 2.10)], "COUPE")
        solid(msp, [P(xp, Z_TER + 0.30), P(xp + 0.14, Z_TER + 0.30),
                    P(xp + 0.14, 2.10), P(xp, 2.10)], "HACHURES", 8)
        L((xp - 0.15, 2.10), (xp + 0.30, 2.10))
        L((xp - 0.15, 2.22), (xp + 0.30, 2.22))

    # dallage RDC
    poly(msp, [P(0.00, Z_TN - 0.10), P(15.00, Z_TN - 0.10),
               P(15.00, Z_RDC), P(0.00, Z_RDC)], "COUPE")
    solid(msp, [P(0.00, Z_TN - 0.10), P(15.00, Z_TN - 0.10),
                P(15.00, Z_RDC), P(0.00, Z_RDC)], "HACHURES", 8)

    # murs coupés (au droit des refends rencontrés par la coupe)
    for (xa, xb, top) in [(0.00, 0.17, Z_PLA), (3.17, 3.34, Z_PLA),
                          (6.84, 6.91, Z_PLA), (9.66, 9.76, Z_PLA),
                          (14.75, 15.00, Z_PLA)]:
        poly(msp, [P(xa, Z_RDC), P(xb, Z_RDC), P(xb, top), P(xa, top)], "COUPE")
        solid(msp, [P(xa, Z_RDC), P(xb, Z_RDC), P(xb, top), P(xa, top)],
              "HACHURES", 8)

    # semelles filantes
    for xc in (0.085, 3.255, 6.875, 9.71, 14.875):
        poly(msp, [P(xc - 0.35, -0.75), P(xc + 0.35, -0.75),
                   P(xc + 0.35, -0.10), P(xc - 0.35, -0.10)], "COUPE")
        solid(msp, [P(xc - 0.35, -0.75), P(xc + 0.35, -0.75),
                    P(xc + 0.35, -0.10), P(xc - 0.35, -0.10)], "HACHURES", 8)
        L((xc - 0.35, -0.75), (xc - 0.35, -0.92))
        L((xc + 0.35, -0.75), (xc + 0.35, -0.92))
        L((xc - 0.35, -0.92), (xc + 0.35, -0.92))

    # plancher du grenier
    poly(msp, [P(0.00, Z_PLA), P(15.00, Z_PLA), P(15.00, Z_GRE), P(0.00, Z_GRE)],
         "COUPE")
    solid(msp, [P(0.00, Z_PLA), P(15.00, Z_PLA), P(15.00, Z_GRE),
                P(0.00, Z_GRE)], "HACHURES", 8)

    # toiture : deux pans + chevrons + couverture
    for (a, b) in ((P(X_EGO, Z_EGO), P(X_FAI, Z_FAI)),
                   (P(X_FAI, Z_FAI), P(X_EGD, Z_EGD))):
        line(msp, a, b, "COUPE")
        L(((a[0] - ox), a[1] - oy - 0.09), ((b[0] - ox), b[1] - oy - 0.09))
        L(((a[0] - ox), a[1] - oy - 0.27), ((b[0] - ox), b[1] - oy - 0.27))

    nch = 15
    for i in range(nch + 1):
        t = i / nch
        x = X_EGO + (X_FAI - X_EGO) * t
        z = Z_EGO + (Z_FAI - Z_EGO) * t
        L((x, z - 0.09), (x, z - 0.32))
    for i in range(8):
        t = i / 7
        x = X_FAI + (X_EGD - X_FAI) * t
        z = Z_FAI + (Z_EGD - Z_FAI) * t
        L((x, z - 0.09), (x, z - 0.30))
    L((X_FAI - 0.14, Z_FAI + 0.02), (X_FAI + 0.14, Z_FAI + 0.02))

    # escalier en coupe
    for i in range(14):
        z = Z_RDC + i * (2.20 / 14)
        L((8.72, z), (9.62, z + 0.157))
        L((9.62, z + 0.157), (9.62, z + 0.157))
    L((8.72, Z_RDC), (8.72, Z_PLA))
    L((9.62, Z_RDC), (9.62, Z_PLA))

    # conduit de fumée / cheminée
    poly(msp, [P(9.90, 3.00), P(10.50, 3.00), P(10.50, Z_FAI + 0.60),
               P(9.90, Z_FAI + 0.60)], "COUPE")
    solid(msp, [P(9.90, 3.00), P(10.50, 3.00), P(10.50, Z_FAI + 0.60),
                P(9.90, Z_FAI + 0.60)], "HACHURES", 8)

    # étiquettes
    txt(msp, "COUVERTURE EN TUILES REGIONALES", 4.30 + ox, Z_EGO + 2.15 + oy,
        0.14, "TEXTES", "CENTER", rot=19)
    txt(msp, "PENTE 0.30 P.M.", 0.30 + ox, Z_EGO + 0.95 + oy, 0.14, "TEXTES",
        "CENTER", rot=19)
    txt(msp, "GRENIER", 4.70 + ox, Z_PLA + 0.35 + oy, 0.18, "TEXTES", "CENTER")
    txt(msp, "GARAGE", 1.55 + ox, 1.55 + oy, 0.20, "TEXTES", "CENTER")
    txt(msp, "CHAMBRE 1", 5.10 + ox, 1.55 + oy, 0.20, "TEXTES", "CENTER")
    txt(msp, "ENTREE", 8.20 + ox, 1.55 + oy, 0.18, "TEXTES", "CENTER")
    txt(msp, "SEJOUR", 12.30 + ox, 1.55 + oy, 0.22, "TEXTES", "CENTER")
    txt(msp, "TERRASSE COUVERTE", -1.25 + ox, 0.62 + oy, 0.14, "TEXTES",
        "CENTER")
    txt(msp, "COUPE SUIVANT A.B", 7.50 + ox, -1.75 + oy, 0.30, "TEXTES",
        "CENTER")
    txt(msp, "ECHELLE 0.02 P.M. (1/50)", 7.50 + ox, -2.15 + oy, 0.15, "TEXTES",
        "CENTER")

    # cotation des hauteurs
    dim_v(msp, Z_TN + oy, Z_FAI + oy, 17.60 + ox, 0)
    dim_v(msp, Z_TN + oy, Z_EGD + oy, 16.90 + ox, 0)
    dim_v(msp, Z_RDC + oy, 2.55 + oy, 9.55 + ox, 0)
    dim_v(msp, Z_RDC + oy, Z_GRE + oy, 2.60 + ox, 0)
    dim_h(msp, 0.00 + ox, 15.00 + ox, Z_TN + oy, -1.25)
    dim_h(msp, 0.00 + ox, 3.17 + ox, Z_TN + oy, -0.62)
    dim_h(msp, 3.34 + ox, 6.84 + ox, Z_TN + oy, -0.62)
    dim_h(msp, 6.91 + ox, 9.66 + ox, Z_TN + oy, -0.62)
    dim_h(msp, 9.76 + ox, 14.75 + ox, Z_TN + oy, -0.62)


# ===========================================================================
# 8. Cartouche et tableaux
# ===========================================================================
def draw_cartouche(msp, x0, y0, w=7.40, h=4.20):
    poly(msp, [(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)],
         "CARTOUCHE")
    h1 = y0 + h * 0.70
    line(msp, (x0, h1), (x0 + w, h1), "CARTOUCHE")
    line(msp, (x0 + w * 0.66, y0), (x0 + w * 0.66, h1), "CARTOUCHE")
    line(msp, (x0, y0 + h * 0.34), (x0 + w * 0.66, y0 + h * 0.34),
         "CARTOUCHE")

    # bandeau 1 : maitre d'ouvrage
    txt(msp, "MONSIEUR ET MADAME DANIEL LEON", x0 + 0.25, y0 + h - 0.36, 0.20,
        "CARTOUCHE")
    txt(msp, "PROPRIETAIRES  -  LOTISSEMENT CHANTE CIGALE  L.T 77",
        x0 + 0.25, y0 + h - 0.68, 0.125, "CARTOUCHE")
    txt(msp, "GUJAN-MESTRAS  -  GIRONDE", x0 + 0.25, y0 + h - 0.94, 0.125,
        "CARTOUCHE")

    # bandeau 2 : objet
    txt(msp, "CONSTRUCTION D'UNE", x0 + 0.25, h1 - 0.40, 0.17, "CARTOUCHE")
    txt(msp, "RESIDENCE PRINCIPALE", x0 + 0.25, h1 - 0.64, 0.17, "CARTOUCHE")
    txt(msp, "PLAN - COUPE - SURFACES", x0 + 0.25, h1 - 0.92, 0.13,
        "CARTOUCHE")

    # bandeau 3 : entreprise
    txt(msp, "ENTREPRISE GRAND", x0 + 0.25, y0 + h * 0.34 - 0.34, 0.16,
        "CARTOUCHE")
    txt(msp, "S.A.R.L. au Capital de 20.000 F.", x0 + 0.25,
        y0 + h * 0.34 - 0.60, 0.115, "CARTOUCHE")
    txt(msp, "LE CANON - 33151   R.C. 73 B 213   -   Teleph. 60.53.29",
        x0 + 0.25, y0 + h * 0.34 - 0.82, 0.115, "CARTOUCHE")
    txt(msp, "DESSINE : J. GRAND  -  JUIN 1975", x0 + 0.25, y0 + h * 0.34 - 1.06,
        0.115, "CARTOUCHE")

    # colonne de droite
    xr = x0 + w * 0.66 + 0.20
    txt(msp, "ECHELLE", xr, h1 - 0.36, 0.115, "CARTOUCHE")
    txt(msp, "0.02 P.M.  =  1/50", xr, h1 - 0.66, 0.17, "CARTOUCHE")
    txt(msp, "UNITES : m / m2", xr, y0 + h * 0.58, 0.11, "CARTOUCHE")
    txt(msp, "PLANCHE 01 / 01", xr, y0 + h * 0.34 - 0.32, 0.115, "CARTOUCHE")
    txt(msp, "INDICE A", xr, y0 + h * 0.34 - 0.58, 0.115, "CARTOUCHE")
    txt(msp, "Retranscription", xr, y0 + h * 0.34 - 0.92, 0.105, "CARTOUCHE")
    txt(msp, "vectorielle (DAO)", xr, y0 + h * 0.34 - 1.10, 0.105, "CARTOUCHE")


def draw_tableaux(msp, x0, y0):
    S = surfaces()
    txt(msp, "SURFACES (m2)  -  valeurs portees au cartouche d'origine",
        x0, y0 + 8.60, 0.19, "TABLEAU")
    txt(msp, "PIECE", x0, y0 + 8.10, 0.14, "TABLEAU")
    txt(msp, "CART.", x0 + 2.30, y0 + 8.10, 0.14, "TABLEAU", "RIGHT")
    txt(msp, "DESSIN", x0 + 3.20, y0 + 8.10, 0.14, "TABLEAU", "RIGHT")
    line(msp, (x0, y0 + 7.98), (x0 + 3.20, y0 + 7.98), "TABLEAU")

    ordre = [("SEJOUR", "SEJOUR"), ("ENTREE", "ENTREE"),
             ("DEGAGEMENT", "DEGAGEMENT"), ("PLACARD", "PL. 0.50"),
             ("VESTIAIRE", "VESTIAIRE"), ("BAINS", "BAINS"),
             ("W.C.", "W.C."), ("CUISINE", "CUISINE"),
             ("CHAMBRE 1", "CHAMBRE 1"), ("PLACARD", "RANGEMENT"),
             ("GARAGE", "GARAGE"), ("ESCALIER", "ESCALIER")]
    y = y0 + 7.62
    tot_doc = 0.0
    for lib, key in ordre:
        v = S[key]
        ref = DOC_SURFACES.get(key, "-")
        txt(msp, lib, x0, y, 0.135, "TABLEAU")
        txt(msp, ref, x0 + 2.30, y, 0.135, "TABLEAU", "RIGHT")
        txt(msp, f"{v:.2f}".replace(".", ","), x0 + 3.20, y, 0.135, "TABLEAU",
            "RIGHT")
        if ref not in ("-",):
            try:
                tot_doc += float(ref.replace(",", "."))
            except ValueError:
                pass
        y -= 0.30
    line(msp, (x0, y + 0.16), (x0 + 3.20, y + 0.16), "TABLEAU")
    txt(msp, "TOTAL", x0, y - 0.16, 0.15, "TABLEAU")
    txt(msp, "91.59", x0 + 2.30, y - 0.16, 0.15, "TABLEAU", "RIGHT")
    txt(msp, f"{sum(S[k] for _, k in ordre):.2f}".replace(".", ","),
        x0 + 3.20, y - 0.16, 0.15, "TABLEAU", "RIGHT")

    txt(msp, "TERRASSE  28.60   |", x0, y - 0.70, 0.135, "TABLEAU")
    txt(msp, f"{S['TERRASSE']:.2f}".replace(".", ","), x0 + 3.20, y - 0.70,
        0.135, "TABLEAU", "RIGHT")

    # étage (combles) : valeurs du cartouche, non redessinées sur cette planche
    y2 = y - 1.35
    txt(msp, "ETAGE (combles) - planche non fournie", x0, y2, 0.15, "TABLEAU")
    com = [("DEGAGEMENT", "1.88"), ("PLACARD", "0.40"), ("TOILETTE", "3.40"),
           ("CHAMBRE 2", "11.97"), ("PLACARD", "1.20"), ("CHAMBRE 3", "14.75"),
           ("PLACARD", "1.20"), ("GRENIER", "35.90"), ("ESCALIER", "2.43"),
           ("BALCON", "4.40")]
    y2 -= 0.36
    for lib, val in com:
        txt(msp, lib, x0, y2, 0.13, "TABLEAU")
        txt(msp, val, x0 + 3.20, y2, 0.13, "TABLEAU", "RIGHT")
        y2 -= 0.28

    txt(msp, "NOTE : la coupe et les surfaces sont celles portees au document "
             "d'origine.", x0, y2 - 0.20, 0.11, "TABLEAU")
    txt(msp, "Les cotes grises du dessin sont recalculees sur la geometrie "
             "reconstruite.", x0, y2 - 0.40, 0.11, "TABLEAU")


# ===========================================================================
# 9. Feuille + DXF
# ===========================================================================
def draw_legende(msp, x0, y0):
    txt(msp, "LEGENDE", x0, y0 + 4.55, 0.20, "TABLEAU")
    line(msp, (x0, y0 + 4.42), (x0 + 6.30, y0 + 4.42), "TABLEAU")
    items = [
        ("MURS_EXT", "Murs exterieurs porteurs (0.17 m)"),
        ("CLOISONS", "Cloisons et refends (0.07 m)"),
        ("OUVERTURES", "Baies - tableaux et ebrasements"),
        ("MENUISERIES", "Menuiseries, portes, debattements"),
        ("ESCALIER", "Escalier (14 marches, 0.90 m)"),
        ("SANITAIRES", "Appareils sanitaires, evier, conduit"),
        ("TERRASSE", "Dallage de terrasse (28.60 m2)"),
        ("COTES", "Cotation (metres)"),
        ("COUPE", "Coupe A-B (murs, planchers, toiture)"),
    ]
    y = y0 + 4.05
    for layer, lib in items:
        line(msp, (x0, y), (x0 + 0.45, y), layer)
        txt(msp, lib, x0 + 0.62, y - 0.05, 0.125, "TABLEAU")
        y -= 0.32


def draw_menuiseries(msp, x0, y0):
    txt(msp, "MENUISERIES EXTERIEURES", x0, y0 + 2.90, 0.18, "TABLEAU")
    line(msp, (x0, y0 + 2.75), (x0 + 6.30, y0 + 2.75), "TABLEAU")
    rows = [
        ("1", "Porte de garage basculante", "2.30 x 2.10", "S"),
        ("2", "Porte de service (garage)", "0.60 x 2.10", "O"),
        ("3", "Fenetre cuisine", "1.40 x 1.00", "S"),
        ("4", "Porte d'entree 2 vantaux", "1.40 x 2.10", "S"),
        ("5", "Fenetre sejour", "1.40 x 1.00", "S"),
        ("6", "Porte-fenetre sejour", "1.40 x 2.10", "S"),
        ("7", "Fenetre chambre 1", "1.40 x 1.00", "N"),
        ("8", "Fenetre W.C.", "0.60 x 0.60", "N"),
        ("9", "Fenetre bains", "1.00 x 0.60", "N"),
        ("10", "Chassis sejour est (x2)", "1.40 x 1.00", "E"),
    ]
    y = y0 + 2.42
    txt(msp, "N.", x0, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "DESIGNATION", x0 + 0.55, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "L x H (m)", x0 + 4.05, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "FAC.", x0 + 5.80, y + 0.06, 0.11, "TABLEAU")
    y -= 0.26
    for n, lib, dim, fac in rows:
        txt(msp, n, x0, y, 0.11, "TABLEAU")
        txt(msp, lib, x0 + 0.55, y, 0.11, "TABLEAU")
        txt(msp, dim, x0 + 4.05, y, 0.11, "TABLEAU")
        txt(msp, fac, x0 + 5.80, y, 0.11, "TABLEAU")
        y -= 0.24
    txt(msp, "Dimensions a confirmer sur l'original (non cotees).", x0,
        y - 0.06, 0.10, "TABLEAU")


def draw_scale_bar(msp, x0, y0, total=5.0, seg=1.0):
    n = int(total / seg)
    h = 0.09
    for i in range(n):
        xa, xb = x0 + i * seg, x0 + (i + 1) * seg
        pts = [(xa, y0), (xb, y0), (xb, y0 + h), (xa, y0 + h)]
        poly(msp, pts, "COTES")
        if i % 2 == 0:
            solid(msp, pts, "COTES", 7)
        txt(msp, f"{i * seg:g}".replace(".", ","), xa, y0 - 0.26, 0.11, "COTES",
            "CENTER")
    txt(msp, "m", x0 + total + 0.22, y0 + 0.02, 0.11, "COTES")


def draw_notes(msp, x0, y0, col_w=6.10):
    txt(msp, "CONTROLE DU CALAGE DIMENSIONNEL ET RESERVES", x0, y0, 0.17,
        "TABLEAU")
    line(msp, (x0, y0 - 0.14), (x0 + 2 * col_w + 1.20, y0 - 0.14), "TABLEAU")
    col1 = [
        "Chaine haute du document : 17 + 300 + 17 + 350 + 7 + 60 + 7 + 85",
        "  + 7 + 200 + 7 + 418 + 25 = 1500 cm  =>  fermeture exacte.",
        "Hors-oeuvre 15.00 x 7.00 m ; interieur 14.66 x 6.66 m.",
        "Surfaces retrouvees exactement : GARAGE 19.98, CHAMBRE 1 11.83,",
        "  CUISINE 10.50, PLACARD 0.96, W.C. 1.36, ENTREE 8.91,",
        "  ESCALIER 2.43, TERRASSE 28.60.",
    ]
    col2 = [
        "Ecarts residuels (releve non cotable) : SEJOUR 30.69 pour 30.17,",
        "  BAINS 5.61 pour 7.14 (cloison non reperable sur la photo).",
        "A verifier sur l'original : cloison sejour/bains (cote 2.69),",
        "  limite ouest de la terrasse (cote 2.30), hauteurs de coupe.",
        "Hauteurs estimees : 2.10 sous plafond, egout 2.35 / 4.40,",
        "  faitage 6.00 m (pente 0.30 p.m.).",
        "Document sans portee contractuelle : a valider par un homme de",
        "  l'art avant tout usage.",
    ]
    y = y0 - 0.44
    for n in col1:
        txt(msp, n, x0, y, 0.112, "TABLEAU")
        y -= 0.245
    y = y0 - 0.44
    for n in col2:
        txt(msp, n, x0 + col_w + 1.20, y, 0.112, "TABLEAU")
        y -= 0.245


# ===========================================================================
# 9. Feuille + DXF
# ===========================================================================
def draw_legende(msp, x0, y0):
    txt(msp, "LEGENDE", x0, y0 + 4.55, 0.20, "TABLEAU")
    line(msp, (x0, y0 + 4.42), (x0 + 6.30, y0 + 4.42), "TABLEAU")
    items = [
        ("MURS_EXT", "Murs exterieurs porteurs (0.17 m)"),
        ("CLOISONS", "Cloisons et refends (0.07 m)"),
        ("OUVERTURES", "Baies - tableaux et ebrasements"),
        ("MENUISERIES", "Menuiseries, portes, debattements"),
        ("ESCALIER", "Escalier (14 marches, 0.90 m)"),
        ("SANITAIRES", "Appareils sanitaires, evier, conduit"),
        ("TERRASSE", "Dallage de terrasse (28.60 m2)"),
        ("COTES", "Cotation (metres)"),
        ("COUPE", "Coupe A-B (murs, planchers, toiture)"),
    ]
    y = y0 + 4.05
    for layer, lib in items:
        line(msp, (x0, y), (x0 + 0.45, y), layer)
        txt(msp, lib, x0 + 0.62, y - 0.05, 0.125, "TABLEAU")
        y -= 0.32


def draw_menuiseries(msp, x0, y0):
    txt(msp, "MENUISERIES EXTERIEURES", x0, y0 + 2.90, 0.18, "TABLEAU")
    line(msp, (x0, y0 + 2.75), (x0 + 6.30, y0 + 2.75), "TABLEAU")
    rows = [
        ("1", "Porte de garage basculante", "2.30 x 2.10", "S"),
        ("2", "Porte de service (garage)", "0.60 x 2.10", "O"),
        ("3", "Fenetre cuisine", "1.40 x 1.00", "S"),
        ("4", "Porte d'entree 2 vantaux", "1.40 x 2.10", "S"),
        ("5", "Fenetre sejour", "1.40 x 1.00", "S"),
        ("6", "Porte-fenetre sejour", "1.40 x 2.10", "S"),
        ("7", "Fenetre chambre 1", "1.40 x 1.00", "N"),
        ("8", "Fenetre W.C.", "0.60 x 0.60", "N"),
        ("9", "Fenetre bains", "1.00 x 0.60", "N"),
        ("10", "Chassis sejour est (x2)", "1.40 x 1.00", "E"),
    ]
    y = y0 + 2.42
    txt(msp, "N.", x0, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "DESIGNATION", x0 + 0.55, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "L x H (m)", x0 + 4.05, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "FAC.", x0 + 5.80, y + 0.06, 0.11, "TABLEAU")
    y -= 0.26
    for n, lib, dim, fac in rows:
        txt(msp, n, x0, y, 0.11, "TABLEAU")
        txt(msp, lib, x0 + 0.55, y, 0.11, "TABLEAU")
        txt(msp, dim, x0 + 4.05, y, 0.11, "TABLEAU")
        txt(msp, fac, x0 + 5.80, y, 0.11, "TABLEAU")
        y -= 0.24
    txt(msp, "Dimensions a confirmer sur l'original (non cotees).", x0,
        y - 0.06, 0.10, "TABLEAU")


def draw_scale_bar(msp, x0, y0, total=5.0, seg=1.0):
    n = int(total / seg)
    h = 0.09
    for i in range(n):
        xa, xb = x0 + i * seg, x0 + (i + 1) * seg
        pts = [(xa, y0), (xb, y0), (xb, y0 + h), (xa, y0 + h)]
        poly(msp, pts, "COTES")
        if i % 2 == 0:
            solid(msp, pts, "COTES", 7)
        txt(msp, f"{i * seg:g}".replace(".", ","), xa, y0 - 0.26, 0.11, "COTES",
            "CENTER")
    txt(msp, "m", x0 + total + 0.22, y0 + 0.02, 0.11, "COTES")


def draw_notes(msp, x0, y0):
    txt(msp, "CONTROLE DU CALAGE DIMENSIONNEL", x0, y0, 0.17, "TABLEAU")
    line(msp, (x0, y0 - 0.14), (x0 + 6.30, y0 - 0.14), "TABLEAU")
    notes = [
        "Chaine haute du document : 17 + 300 + 17 + 350 + 7 + 60 + 7 + 85",
        "   + 7 + 200 + 7 + 418 + 25 = 1500 cm  =>  fermeture exacte.",
        "Hors-oeuvre 15.00 x 7.00 m ; interieur 14.66 x 6.66 m.",
        "Surfaces retrouvees exactement : GARAGE 19.98, CHAMBRE 1 11.83,",
        "   CUISINE 10.50, PLACARD 0.96, W.C. 1.36, ENTREE 8.91, ESCALIER 2.43,",
        "   TERRASSE 28.60.",
        "Ecarts residuels (releve non cotable) : SEJOUR 30.69 pour 30.17,",
        "   BAINS 5.61 pour 7.14 (cloison non reperable sur la photo).",
        "A verifier sur l'original : position de la cloison sejour/bains",
        "   (cote 2.69) et limite ouest de la terrasse (cote 2.30).",
        "Hauteurs de coupe estimees : 2.10 sous plafond, egout 2.35/4.40,",
        "   faitage 6.00 m, pente 0.30 p.m.  A confirmer.",
        "Document etabli sans portee contractuelle : a valider par un",
        "   homme de l'art avant tout usage.",
    ]
    y = y0 - 0.44
    for n in notes:
        txt(msp, n, x0, y, 0.112, "TABLEAU")
        y -= 0.245


# ===========================================================================
# 9. Feuille + DXF
# ===========================================================================
def draw_legende(msp, x0, y0):
    txt(msp, "LEGENDE", x0, y0 + 4.55, 0.20, "TABLEAU")
    line(msp, (x0, y0 + 4.42), (x0 + 6.30, y0 + 4.42), "TABLEAU")
    items = [
        ("MURS_EXT", "Murs exterieurs porteurs (0.17 m)"),
        ("CLOISONS", "Cloisons et refends (0.07 m)"),
        ("OUVERTURES", "Baies - tableaux et ebrasements"),
        ("MENUISERIES", "Menuiseries, portes, debattements"),
        ("ESCALIER", "Escalier (14 marches, 0.90 m)"),
        ("SANITAIRES", "Appareils sanitaires, evier, conduit"),
        ("TERRASSE", "Dallage de terrasse (28.60 m2)"),
        ("COTES", "Cotation (metres)"),
        ("COUPE", "Coupe A-B (murs, planchers, toiture)"),
    ]
    y = y0 + 4.05
    for layer, lib in items:
        line(msp, (x0, y), (x0 + 0.45, y), layer)
        txt(msp, lib, x0 + 0.62, y - 0.05, 0.125, "TABLEAU")
        y -= 0.32


def draw_menuiseries(msp, x0, y0):
    txt(msp, "MENUISERIES EXTERIEURES", x0, y0 + 2.90, 0.18, "TABLEAU")
    line(msp, (x0, y0 + 2.75), (x0 + 6.30, y0 + 2.75), "TABLEAU")
    rows = [
        ("1", "Porte de garage basculante", "2.30 x 2.10", "S"),
        ("2", "Porte de service (garage)", "0.60 x 2.10", "O"),
        ("3", "Fenetre cuisine", "1.40 x 1.00", "S"),
        ("4", "Porte d'entree 2 vantaux", "1.40 x 2.10", "S"),
        ("5", "Fenetre sejour", "1.40 x 1.00", "S"),
        ("6", "Porte-fenetre sejour", "1.40 x 2.10", "S"),
        ("7", "Fenetre chambre 1", "1.40 x 1.00", "N"),
        ("8", "Fenetre W.C.", "0.60 x 0.60", "N"),
        ("9", "Fenetre bains", "1.00 x 0.60", "N"),
        ("10", "Chassis sejour est (x2)", "1.40 x 1.00", "E"),
    ]
    y = y0 + 2.42
    txt(msp, "N.", x0, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "DESIGNATION", x0 + 0.55, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "L x H (m)", x0 + 4.05, y + 0.06, 0.11, "TABLEAU")
    txt(msp, "FAC.", x0 + 5.80, y + 0.06, 0.11, "TABLEAU")
    y -= 0.26
    for n, lib, dim, fac in rows:
        txt(msp, n, x0, y, 0.11, "TABLEAU")
        txt(msp, lib, x0 + 0.55, y, 0.11, "TABLEAU")
        txt(msp, dim, x0 + 4.05, y, 0.11, "TABLEAU")
        txt(msp, fac, x0 + 5.80, y, 0.11, "TABLEAU")
        y -= 0.24
    txt(msp, "Dimensions a confirmer sur l'original (non cotees).", x0,
        y - 0.06, 0.10, "TABLEAU")


def draw_scale_bar(msp, x0, y0, total=5.0, seg=1.0):
    n = int(total / seg)
    h = 0.09
    for i in range(n):
        xa, xb = x0 + i * seg, x0 + (i + 1) * seg
        pts = [(xa, y0), (xb, y0), (xb, y0 + h), (xa, y0 + h)]
        poly(msp, pts, "COTES")
        if i % 2 == 0:
            solid(msp, pts, "COTES", 7)
        txt(msp, f"{i * seg:g}".replace(".", ","), xa, y0 - 0.26, 0.11, "COTES",
            "CENTER")
    txt(msp, "m", x0 + total + 0.22, y0 + 0.02, 0.11, "COTES")


def draw_notes(msp, x0, y0):
    txt(msp, "CONTROLE DIMENSIONNEL DU CALAGE", x0, y0 + 0.05, 0.18, "TABLEAU")
    line(msp, (x0, y0 - 0.10), (x0 + 6.30, y0 - 0.10), "TABLEAU")
    notes = [
        "Chaine haute du document : 17 + 300 + 17 + 350 + 7 + 60 + 7",
        "  + 85 + 7 + 200 + 7 + 418 + 25 = 1500 cm  (fermeture exacte)",
        "Profondeur : 7.00 m hors-oeuvre, 6.66 m interieur.",
        "Surfaces retrouvees exactement : GARAGE 19.98, CHAMBRE 1 11.83,",
        "  CUISINE 10.50, PLACARD 0.96, W.C. 1.36, ENTREE 8.91,",
        "  ESCALIER 2.43, TERRASSE 28.60.",
        "Surfaces legerement differentes (releve non cotable sur la photo) :",
        "  SEJOUR (30.17), BAINS (7.14), DEGAGEMENT (1.89), VESTIAIRE (0.98).",
        "Points a verifier sur l'original : position exacte de la cloison",
        "  sejour/bains (cote 2.69 lue) et limite de la terrasse au sud (cote 2.30).",
    ]
    y = y0 - 0.42
    for n in notes:
        txt(msp, n, x0, y, 0.115, "TABLEAU")
        y -= 0.26


# ===========================================================================
# 9. Feuille + DXF
# ===========================================================================
def build(outdir: Path):
    doc = ezdxf.new("R2013", setup=True)
    setup(doc)
    msp = doc.modelspace()

    # ---- cadre de feuille (A1 au 1/50 : 841 x 594 mm = 42.05 x 29.70 m) --
    W, H = 42.00, 29.70
    FX, FY = -4.00, -6.00
    poly(msp, [(FX, FY), (FX + W, FY), (FX + W, FY + H), (FX, FY + H)],
         "CARTOUCHE")
    poly(msp, [(FX + 0.40, FY + 0.40), (FX + W - 0.40, FY + 0.40),
               (FX + W - 0.40, FY + H - 0.40), (FX + 0.40, FY + H - 0.40)],
         "CARTOUCHE")

    # titre de la planche
    txt(msp, "MONSIEUR ET MADAME DANIEL LEON  -  GUJAN-MESTRAS  -  "
             "CONSTRUCTION D'UNE RESIDENCE PRINCIPALE",
        FX + 1.00, FY + H - 0.95, 0.30, "CARTOUCHE")
    line(msp, (FX + 1.00, FY + H - 1.25), (FX + 40.5, FY + H - 1.25),
         "CARTOUCHE")
    txt(msp, "Retranscription DXF de la planche du permis de construire "
             "(plan / coupe / surfaces) - unites mm - echelle 1/50",
        FX + 1.00, FY + 0.62, 0.15, "CARTOUCHE")

    # ---- plan (en bas, à l'ouest) ----------------------------------------
    draw_terrasse(msp)
    draw_plan(msp, 0.0, 0.0)
    draw_cotes_plan(msp, 0.0, 0.0)
    draw_north(msp, -3.30, 7.60, 0.70)

    # ---- coupe A-B (au-dessus, disposition de la planche d'origine) ------
    draw_coupe(msp, 0.0, 11.60)

    # ---- cartouche, tableaux, légende, notes (à l'est) -------------------
    draw_tableaux(msp, 25.30, 10.40)
    draw_menuiseries(msp, 25.30, 5.10)
    draw_legende(msp, 25.30, -0.05)
    draw_cartouche(msp, 30.60, -4.90)
    draw_notes(msp, -3.20, 21.60)
    draw_scale_bar(msp, 25.30, 0.15)

    # ---- mise en page papier A1 1/50 -------------------------------------
    lay = doc.layouts.new("A1-1_50")
    lay.page_setup(size=(841, 594), margins=(0, 0, 0, 0), units="mm",
                   scale=(1, 1))
    cx = (FX + W / 2) * MM
    cy = (FY + H / 2) * MM
    lay.add_viewport(center=(420.5, 297.0), size=(841, 594),
                     view_center_point=(cx, cy), view_height=H * MM)
    doc.set_modelspace_vport(height=H * MM, center=(cx, cy))
    # limites de travail = cadre de la feuille A1 au 1/50
    doc.header["$LIMMIN"] = (FX * MM, FY * MM)
    doc.header["$LIMMAX"] = ((FX + W) * MM, (FY + H) * MM)
    doc.header["$PEXTMIN"] = (FX * MM, FY * MM, 0.0)
    doc.header["$PEXTMAX"] = ((FX + W) * MM, (FY + H) * MM, 0.0)

    # ---- en-tête : étendues et limites (utile à l'ouverture AutoCAD) -----
    from ezdxf import bbox
    ext = bbox.extents(msp)
    if ext.has_data:
        doc.header["$EXTMIN"] = (ext.extmin.x, ext.extmin.y, 0.0)
        doc.header["$EXTMAX"] = (ext.extmax.x, ext.extmax.y, 0.0)

    doc.header["$LTSCALE"] = 1.0
    doc.header["$DIMSCALE"] = 1.0
    doc.header["$TEXTSIZE"] = m(0.15)

    outdir.mkdir(parents=True, exist_ok=True)
    dxf = outdir / "DANIEL_LEON_PC1975_PLAN_COUPE_SURFACES_v2.dxf"
    doc.saveas(dxf)
    print("DXF :", dxf)
    for k, v in surfaces().items():
        print(f"   {k:<12} {v:7.2f} m2   (cartouche {DOC_SURFACES.get(k, '-')})")
    return dxf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[1]
                                         / "01_PLAN"))
    a = ap.parse_args()
    build(Path(a.out))


if __name__ == "__main__":
    main()
