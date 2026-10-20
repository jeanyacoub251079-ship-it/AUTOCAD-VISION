#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-20 — SYNTHÈSE STRUCTURELLE & CONCEPTION GO  (CARNAC v2.6 — Indice B)

Projet : CROISSY-FLORA (ID-01)
Mode   : PARTIEL-DÉCLARÉ (synthèse intégrale du corpus D1+D2+D3+D4+D5 selon art. P1–P8)
Régime : OUTILLÉ (V13) — extraction vectorielle exacte D2 <-> D5, audit DXF 0 erreur.

Produit TROIS planches complètes DXF + PDF + PNG (ZÉRO cloison, ZÉRO isolation) :
  1. FLORA_B20_PH-RDC_PRINCIPE-STRUCTUREL_IndB.{dxf,pdf,png}
     -> Synthèse PH RDC : fond structurel pur B-32 Ind. D + démolitions de murs
        porteurs (102_demol) + trame cotée + TOUS les ouvrages neufs EVEN calés
        au millimètre près (F1a/b/c, F2, F3, F4, R1, R2-N/S, R3-N/S, P1-N/S, P2, P3,
        J1, 10xS1, 6xS2, 4xStab1, poutres existantes IPE330 & BM15x20, zone non sondée).
  2. FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB.{dxf,pdf,png}
     -> Synthèse Infrastructure & Implantation des Fondations (PB RDC / « PLS » D-11) :
        semelle neuve SF1 (60x60x30 BA mini D-14 sous P2), nuages D-19 d'appui/fondation
        à vérifier à l'ouverture des fouilles sous P1-N, P1-S, P3 et J1, bêche BA Sud-Est
        (EXI-07c), arase sur débord semelle existante (EXI-07b/d), RSO passerelle château
        par passes alternées de gros béton C16/20 (EXI-07e), dallage BA ép. 13 cm, note D-09.
  3. FLORA_B20_CHARPENTE_COUPES_SCHEMA_IndB.{dxf,pdf,png}
     -> Plan R+1 & Renforts de Charpente sur fond B-32 Ind. D (2 demi-fermes en sous-oeuvre,
        3 pannes neuves, renfort ferme traditionnelle, 2 zones non relevées) + Schéma
        synoptique de cheminement des charges + DEUX coupes schématiques cotées (A-A et B-B).

Tous les plans portent le filigrane obligatoire CARNAC :
  « PRINCIPE — NE PAS EXÉCUTER — Indice P »
et la note D-09 intégrale mot pour mot.
"""

import math
import os
import sys
from datetime import datetime

import ezdxf
from ezdxf.bbox import extents
import pymupdf

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy

SRC_DXF_RAW = "google_drive/208_FLORA_Plans_DCE_IndC.dxf"
SRC_RDC = "dossiers/CROISSY/_plans/FLORA_RDC_VUE-NETTOYEE_IndD.dxf"
SRC_R1 = "dossiers/CROISSY/_plans/FLORA_R1_VUE-NETTOYEE_IndD.dxf"
SRC_EVEN = "/tmp/arena-coding-uploads/24.09.356E DCE indice C FLORA 16.03.2026.pdf"

OUT_DIR = "dossiers/CROISSY/_plans"
JOURNAL = "dossiers/CROISSY/_rendus/b20_conception.txt"

# Paramètres de calage exact D2 Folio 01 (échelle 1/80 vectorielle) -> D5 RDC_PROJ (cm)
SCALE_CM_PER_PT = 1.0 / (72.0 / 2.54 / 80.0)  # 2.8222222222 cm/pt (exact 1/80)
X0_F01 = 8114.33
Y0_F01 = 6606.50
# Origine B-30 en cm DXF : P1 = (8586.97, 4442.70)
B30_ORIGIN = (8586.97, 4442.70)

LOG = []


def log(msg=""):
    print(msg)
    LOG.append(msg)


def b30_m(x_cm, y_cm):
    return (x_cm - B30_ORIGIN[0]) / 100.0, (y_cm - B30_ORIGIN[1]) / 100.0


# ==============================================================================
# CATALOGUE EXHAUSTIF DES OUVRAGES NEUFS EXTRAITS VECTORIELLEMENT DE D2 (EVEN)
# Coordonnées en cm dans le repère DXF RDC_PROJ (calage résidu médian 21,0 mm)
# ==============================================================================

# 1. Frangements métalliques S275 (calque STRUCT-FRANGEMENTS, rouge ACI 1)
FRANGEMENTS = [
    # (id, label, section, x1, y1, x2, y2, w_cm, L_libre_m, ecart_source)
    ("F1a", "F1a (2xHEA200)", "2x HEA 200 S275", 8977.4, 5320.2, 8977.4, 5464.1, 28.0, 1.00,
     "Ouverture créée refend central moellons (appuis J1 + S2)"),
    ("F1b", "F1b (2xHEA200)", "2x HEA 200 S275", 9279.8, 5489.2, 9427.5, 5489.2, 28.0, 0.90,
     "Renfort linteau bois + baie mur Nord hall (appuis S2 + P3)"),
    ("F1c", "F1c (2xHEA200)", "2x HEA 200 S275", 9407.5, 5214.0, 9532.5, 5214.0, 28.0, 0.85,
     "Renfort linteau bois + baie mur Sud hall (appuis 2xS2)"),
    ("F2",  "F2 (HEB200)",    "HEB 200 S275",    8647.4, 4954.1, 8972.5, 4954.1, 20.0, 2.85,
     "Suppression mur porteur Sud Aile Est + appui F4 (appuis 2xS1)"),
    ("F3",  "F3 (HEB160)",    "HEB 160 S275",    8547.5, 5311.6, 8972.5, 5311.6, 16.0, 3.85,
     "Suppression refend central Aile Est (appuis 2xS1)"),
    ("F4",  "F4 (IPE200)",    "IPE 200 S275",    8875.0, 4458.6, 8875.0, 4946.6, 15.0, 4.88,
     "Suppression paroi longit. extension Sud-Est (appuis F2 + S1)"),
]

# 2. Renforts métalliques de plancher S275 (calque STRUCT-RENFORTS, bleu ACI 5)
RENFORTS = [
    ("R1",   "R1 (2xUPE200)", "2x UPE 200 S275", 8547.5, 5488.7, 8969.8, 5488.7, 26.0, 3.85,
     "Moisage poutre bois 15x20 fléchie — Désordre 3 (appuis 2xS2)"),
    ("R2-N", "R2-N (HEB160)", "HEB 160 S275",    8570.5, 5709.1, 8952.5, 5709.1, 16.0, 3.82,
     "Renfort mi-travée solives bois 8x18 Plancher A (q=250 daN/m²)"),
    ("R2-S", "R2-S (HEB160)", "HEB 160 S275",    8570.5, 5133.1, 8952.5, 5133.1, 16.0, 3.82,
     "Renfort mi-travée solives bois 8x18 Plancher A (appuis R3-S + S1)"),
    ("R3-N", "R3-N (UPE200)", "UPE 200 S275",    8570.5, 5584.2, 8570.5, 5834.1, 14.0, 1.55,
     "Linteau porteur baie Nord façade Est — Désordre 1 (appuis 2xS1)"),
    ("R3-S", "R3-S (UPE200)", "UPE 200 S275",    8570.5, 5007.9, 8570.5, 5258.0, 14.0, 1.55,
     "Linteau porteur baie Sud façade Est — Désordre 1 (appuis 2xS1)"),
]

# 3. Entretoises anti-déversement Stab1 dans voutains briques (calque STRUCT-STAB, cyan ACI 4)
STAB1_LINES = [
    ("Stab1-NW", 9175.5, 5534.2, 9175.5, 6296.7),
    ("Stab1-NE", 9349.4, 5534.2, 9349.4, 6296.7),
    ("Stab1-SW", 9175.5, 4509.9, 9175.5, 5189.1),
    ("Stab1-SE", 9349.4, 4509.9, 9349.4, 5189.1),
]

# 4. Poutres maîtresses existantes repérées dans D3 (calque STRUCT-EXIST-POUTRES, gris ACI 8)
POUTRES_EXIST = [
    ("IPE 330 exist.", 9170.0, 5534.2, 9170.0, 6296.7),
    ("IPE 330 exist.", 9343.9, 5534.2, 9343.9, 6296.7),
    ("IPE 330 exist.", 9170.0, 4529.9, 9170.0, 5189.1),
    ("IPE 330 exist.", 9343.9, 4529.9, 9343.9, 5189.1),
]

# 5. Poteaux métalliques S275 (calque STRUCT-POTEAUX-METAL, magenta ACI 6)
POTEAUX_METAL = [
    # (id, label, section, xc, yc, dx, dy, role)
    ("P1-N", "P1-N (140x140)", "Tube 140x140 S275", 9540.5, 4904.4, 14.0, 14.0,
     "Renfort sous linteau bois existant baie Ouest Sud (D2 f.01 / D3 p.16)"),
    ("P1-S", "P1-S (140x140)", "Tube 140x140 S275", 9540.5, 4778.4, 14.0, 14.0,
     "Renfort sous linteau bois existant baie Ouest Sud (D2 f.01 / D3 p.16)"),
]

# 6. Poteaux BA et Jambage BA C25/30 (calque STRUCT-BA-VERT, vert ACI 3)
POTEAUX_BA = [
    # (id, label, section, x0, y0, x1, y1, role)
    ("P2", "P2 (15x25 BA)", "Poteau BA 15x25 C25/30", 9522.5, 5921.7, 9547.6, 5936.7,
     "Remplacement poteau bois + allège portique Ouest Nord (D3 p.17) sur SF1"),
    ("P3", "P3 (50x40 BA)", "Poteau BA 50x40 C25/30", 9389.7, 5464.1, 9427.5, 5514.1,
     "Reprise d'appui du linteau existant + appui Est de F1b (D2 f.01)"),
    ("J1", "J1 (24x50 BA)", "Jambage BA 24x50 C25/30", 8952.5, 5440.1, 9002.5, 5464.1,
     "Jambage BA piédroit Nord du frangement F1a dans refend moellons 50 cm"),
]

# 7. Sommiers BA d'appui S1 (20x40x20ht) et S2 (20xép.murx20ht) (calque STRUCT-SOMMIERS, vert ACI 30/3)
SOMMIERS_S1 = [
    ("S1", 8547.5, 5798.6, 8567.5, 5834.1),
    ("S1", 8547.5, 5584.2, 8567.5, 5619.7),
    ("S1", 8547.5, 5293.8, 8567.5, 5329.5),
    ("S1", 8952.5, 5293.8, 8972.5, 5329.5),
    ("S1", 8547.5, 5222.5, 8567.5, 5258.0),
    ("S1", 8952.5, 5115.1, 8972.5, 5150.9),
    ("S1", 8547.5, 5007.9, 8567.5, 5043.7),
    ("S1", 8647.4, 4926.0, 8667.5, 4961.5),
    ("S1", 8952.5, 4927.0, 8972.5, 4962.6),
    ("S1", 8867.5, 4437.3, 8903.1, 4463.2),
]

SOMMIERS_S2 = [
    ("S2", 8547.5, 5464.6, 8567.5, 5513.7),
    ("S2", 8952.5, 5464.1, 8972.5, 5518.1),
    ("S2", 9279.8, 5464.1, 9299.8, 5514.1),
    ("S2", 8952.5, 5320.2, 9002.5, 5340.2),
    ("S2", 9407.5, 5189.1, 9427.5, 5239.1),
    ("S2", 9512.5, 5189.1, 9532.5, 5239.1),
]


def ensure_layers(doc):
    specs = [
        ("ARCHI-DEMOL",          30),  # orange : murs/allèges démolis (102_demol)
        ("STRUCT-TRAME",          8),  # gris moyen : axes structurels
        ("STRUCT-EXIST-POUTRES",  8),  # gris foncé : IPE 330 existants
        ("STRUCT-FRANGEMENTS",    1),  # rouge vif : F1a, F1b, F1c, F2, F3, F4
        ("STRUCT-RENFORTS",       5),  # bleu vif : R1, R2-N, R2-S, R3-N, R3-S
        ("STRUCT-STAB",           4),  # cyan : Stab1 entretoises anti-dévers
        ("STRUCT-POTEAUX-METAL",  6),  # magenta : P1-N, P1-S (140x140 S275)
        ("STRUCT-BA",             3),  # vert : P2, P3, J1, S1, S2, SF1, Bêche
        ("STRUCT-FONDATIONS",     1),  # rouge : semelle SF1 60x60x30 BA mini
        ("STRUCT-HYP-D19",        6),  # magenta : nuages d'hypothèse D-19
        ("STRUCT-TEXTE",          7),  # noir : annotations & tableaux
        ("STRUCT-CARTOUCHE",      7),  # noir : cartouche & filigrane
    ]
    for name, col in specs:
        if name not in doc.layers:
            doc.layers.add(name, color=col)
    # Adoucir le fond architectural pour faire ressortir la structure neuve à 100 %
    for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
        if lname in doc.layers:
            doc.layers.get(lname).color = 8 if lname == "010_mur" else 9


def extract_structural_demol_segments():
    """Extrait depuis D5 les segments 102_demol dans le bloc géomètre du RDC Projet."""
    raw = ezdxf.readfile(SRC_DXF_RAW)
    msp = raw.modelspace()
    segs = []
    for e in msp:
        if e.dxftype() == "INSERT" and e.dxf.name == "Murs porteurs selon geometre projet":
            if 6830 <= e.dxf.insert.x <= 13000 and 3902 <= e.dxf.insert.y <= 7402:
                m = e.matrix44()
                for be in raw.blocks.get(e.dxf.name):
                    if be.dxf.layer != "102_demol":
                        continue
                    if be.dxftype() == "LWPOLYLINE":
                        pts = [tuple(m.transform((x, y, 0)))[:2] for x, y, *_ in be.get_points("xy")]
                        if be.closed and len(pts) > 2:
                            pts.append(pts[0])
                        for p1, p2 in zip(pts, pts[1:]):
                            if 8500 <= p1[0] <= 9650 and 4400 <= p1[1] <= 6350:
                                segs.append((p1, p2))
                    elif be.dxftype() == "LINE":
                        p1 = tuple(m.transform((be.dxf.start.x, be.dxf.start.y, 0)))[:2]
                        p2 = tuple(m.transform((be.dxf.end.x, be.dxf.end.y, 0)))[:2]
                        if 8500 <= p1[0] <= 9650 and 4400 <= p1[1] <= 6350:
                            segs.append((p1, p2))
    return segs


def add_rect(sp, x0, y0, x1, y1, layer, hatch_col=None):
    sp.add_lwpolyline(
        [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
        dxfattribs={"layer": layer},
    )
    if hatch_col is not None:
        h = sp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
        h.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)
    return sp


def add_beam(sp, x1, y1, x2, y2, w_cm, layer, double=False):
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    hw = 0.5 * w_cm
    p1 = (x1 + nx * hw, y1 + ny * hw)
    p2 = (x2 + nx * hw, y2 + ny * hw)
    p3 = (x2 - nx * hw, y2 - ny * hw)
    p4 = (x1 - nx * hw, y1 - ny * hw)
    sp.add_lwpolyline([p1, p2, p3, p4, p1], dxfattribs={"layer": layer})
    if double:
        for sgn in (-0.22, 0.22):
            sp.add_line(
                (x1 + nx * w_cm * sgn, y1 + ny * w_cm * sgn),
                (x2 + nx * w_cm * sgn, y2 + ny * w_cm * sgn),
                dxfattribs={"layer": layer},
            )
    else:
        sp.add_line((x1, y1), (x2, y2), dxfattribs={"layer": layer})


def add_cloud(sp, x0, y0, x1, y1, layer="STRUCT-HYP-D19", step=28.0):
    """Dessine un nuage de révision / hypothèse D-19 festonné en arcs."""
    pts = []
    x = x0
    while x < x1:
        pts.append((x, y0))
        x += step
    y = y0
    while y < y1:
        pts.append((x1, y))
        y += step
    x = x1
    while x > x0:
        pts.append((x, y1))
        x -= step
    y = y1
    while y > y0:
        pts.append((x0, y))
        y -= step
    pts.append((x0, y0))
    for (ax_, ay_), (bx_, by_) in zip(pts, pts[1:]):
        mx, my = 0.5 * (ax_ + bx_), 0.5 * (ay_ + by_)
        dx, dy = bx_ - ax_, by_ - ay_
        L = math.hypot(dx, dy)
        if L < 1e-6:
            continue
        nx, ny = dy / L, -dx / L
        cx, cy = mx + 0.30 * L * nx, my + 0.30 * L * ny
        sp.add_lwpolyline([(ax_, ay_), (cx, cy), (bx_, by_)], dxfattribs={"layer": layer})


def add_txt(sp, x, y, text, h=14.0, layer="STRUCT-TEXTE"):
    e = sp.add_text(text, height=h, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def add_leader(sp, tx, ty, px, py, text, h=14.0, layer="STRUCT-TEXTE"):
    sp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + len(text) * h * 0.62, ty - 3.0)],
                      dxfattribs={"layer": layer})
    add_txt(sp, tx, ty, text, h=h, layer=layer)


# ==============================================================================
# PLANCHE 1 — PH RDC : SYNTHÈSE STRUCTURELLE EXISTANT / DÉMOLITION / PROJET
# ==============================================================================
def build_sheet1_ph_rdc(demol_segs):
    doc = ezdxf.readfile(SRC_RDC)
    ensure_layers(doc)
    sp = doc.modelspace()

    # 1. Démolitions de murs existants (102_demol filtré hors mobilier sanitaire)
    n_dem = 0
    for (x1, y1), (x2, y2) in demol_segs:
        # Filtrer les petits traits courbes des anciens appareils sanitaires de SDB Sud
        L = math.hypot(x2 - x1, y2 - y1)
        if L >= 18.0:
            sp.add_line((x1, y1), (x2, y2), dxfattribs={"layer": "ARCHI-DEMOL"})
            n_dem += 1

    # 2. Trame des files structurelles (files verticales A..E, horizontales 1..6)
    v_axes = [
        ("A", 8555.0, "X=85,55"),
        ("B", 8655.0, "X=86,55"),
        ("C", 8875.0, "X=88,75"),
        ("D", 8977.5, "X=89,78"),
        ("E", 9535.0, "X=95,35"),
    ]
    h_axes = [
        ("1", 4460.0, "Y=44,60"),
        ("2", 4954.1, "Y=49,54"),
        ("3", 5214.0, "Y=52,14"),
        ("4", 5489.0, "Y=54,89"),
        ("5", 5905.0, "Y=59,05"),
        ("6", 6312.0, "Y=63,12"),
    ]
    for code, xv, _ in v_axes:
        sp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "STRUCT-TRAME"})
        sp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "STRUCT-TRAME"})
        add_txt(sp, xv - 8.0, 6484.0, code, h=18.0, layer="STRUCT-TRAME")
    for code, yv, _ in h_axes:
        sp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "STRUCT-TRAME"})
        sp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "STRUCT-TRAME"})
        add_txt(sp, 8380.0, yv - 8.0, code, h=18.0, layer="STRUCT-TRAME")

    # 3. Sommiers S1 & S2 (dessinés sous l'acier)
    for _, x0, y0, x1, y1 in SOMMIERS_S1:
        add_rect(sp, x0, y0, x1, y1, "STRUCT-BA", hatch_col=3)
    for _, x0, y0, x1, y1 in SOMMIERS_S2:
        add_rect(sp, x0, y0, x1, y1, "STRUCT-BA", hatch_col=3)

    # 4. Poteaux BA P2, P3 et Jambage BA J1
    for pid, lbl, _, x0, y0, x1, y1, _ in POTEAUX_BA:
        add_rect(sp, x0, y0, x1, y1, "STRUCT-BA", hatch_col=3)

    # 5. Poteaux métalliques P1-N & P1-S (tube carré 140x140 S275)
    for pid, lbl, _, xc, yc, dx, dy, _ in POTEAUX_METAL:
        add_rect(sp, xc - dx / 2, yc - dy / 2, xc + dx / 2, yc + dy / 2,
                 "STRUCT-POTEAUX-METAL", hatch_col=6)

    # 6. Poutres existantes IPE 330 + Entretoises anti-déversement Stab1
    for _, x1, y1, x2, y2 in POUTRES_EXIST:
        sp.add_line((x1, y1), (x2, y2), dxfattribs={"layer": "STRUCT-EXIST-POUTRES"})
    for _, x1, y1, x2, y2 in STAB1_LINES:
        # Trait tireté explicite tous les 35 cm pour lisibilité garantie en PDF/PNG
        y = y1
        while y < y2:
            sp.add_line((x1, y), (x1, min(y + 22.0, y2)), dxfattribs={"layer": "STRUCT-STAB"})
            y += 36.0

    # 7. Renforts métalliques R1, R2-N, R2-S, R3-N, R3-S
    for rid, lbl, _, x1, y1, x2, y2, w, _, _ in RENFORTS:
        add_beam(sp, x1, y1, x2, y2, w, "STRUCT-RENFORTS", double=rid.startswith("R1"))

    # 8. Frangements métalliques F1a, F1b, F1c, F2, F3, F4
    for fid, lbl, _, x1, y1, x2, y2, w, _, _ in FRANGEMENTS:
        add_beam(sp, x1, y1, x2, y2, w, "STRUCT-FRANGEMENTS", double=fid.startswith("F1"))

    # 9. Nuage D-19 sur la zone centrale « Plancher haut non sondé » (D3 p.4 & p.10)
    add_cloud(sp, 9010.0, 5248.0, 9545.0, 5458.0, layer="STRUCT-HYP-D19", step=30.0)
    add_txt(sp, 9035.0, 5395.0, "NUAGE D-19 : PLANCHER HAUT NON SONDE", h=12.5, layer="STRUCT-HYP-D19")
    add_txt(sp, 9035.0, 5373.0, "(D3 p.4 & p.10 — sondage contradictoire requis)", h=11.0, layer="STRUCT-HYP-D19")

    # 10. Étiquettes claires sans AUCUN chevauchement sur le plan
    add_txt(sp, 8685.0, 5722.0, "R2-N : HEB 160 (L=3,82m)", h=13.5, layer="STRUCT-RENFORTS")
    add_txt(sp, 8655.0, 5510.0, "R1 : 2xUPE 200 moisage BM 15x20", h=13.5, layer="STRUCT-RENFORTS")
    add_txt(sp, 8685.0, 5146.0, "R2-S : HEB 160 (L=3,82m)", h=13.5, layer="STRUCT-RENFORTS")
    add_leader(sp, 7990.0, 5735.0, 8562.0, 5710.0, "R3-N : UPE 200 + 2xS1", h=13.0, layer="STRUCT-RENFORTS")
    add_leader(sp, 7990.0, 5155.0, 8562.0, 5133.0, "R3-S : UPE 200 + 2xS1", h=13.0, layer="STRUCT-RENFORTS")

    add_txt(sp, 8680.0, 5326.0, "F3 : HEB 160 (L=3,85m)", h=14.0, layer="STRUCT-FRANGEMENTS")
    add_txt(sp, 8680.0, 4970.0, "F2 : HEB 200 (L=2,85m)", h=14.0, layer="STRUCT-FRANGEMENTS")
    add_leader(sp, 7990.0, 4710.0, 8868.0, 4710.0, "F4 : IPE 200 (L=4,88m)", h=13.5, layer="STRUCT-FRANGEMENTS")

    add_leader(sp, 7990.0, 5395.0, 8968.0, 5395.0, "F1a : 2xHEA 200 + S2", h=13.0, layer="STRUCT-FRANGEMENTS")
    add_leader(sp, 9640.0, 5585.0, 9355.0, 5495.0, "F1b : 2xHEA 200 + S2", h=13.5, layer="STRUCT-FRANGEMENTS")
    add_leader(sp, 9640.0, 5525.0, 9415.0, 5490.0, "P3 : Poteau BA 50x40 (reprise linteau)", h=13.5, layer="STRUCT-BA")
    add_leader(sp, 7990.0, 5575.0, 8955.0, 5455.0, "J1 : Jambage BA 24x50", h=13.0, layer="STRUCT-BA")
    add_leader(sp, 9640.0, 5215.0, 9475.0, 5214.0, "F1c : 2xHEA 200 + 2xS2", h=13.5, layer="STRUCT-FRANGEMENTS")

    add_leader(sp, 9640.0, 5940.0, 9547.0, 5929.0, "P2 : Poteau BA 15x25 + allège (sur SF1 60x60)", h=13.5, layer="STRUCT-BA")
    add_leader(sp, 9640.0, 4912.0, 9547.0, 4904.0, "P1-N : Tube 140x140 S275 (renfort linteau bois)", h=13.5, layer="STRUCT-POTEAUX-METAL")
    add_leader(sp, 9640.0, 4782.0, 9547.0, 4778.0, "P1-S : Tube 140x140 S275 (renfort linteau bois)", h=13.5, layer="STRUCT-POTEAUX-METAL")

    add_txt(sp, 9055.0, 6035.0, "PLANCHER B EXISTANT (IPE160 + voutains)", h=12.5, layer="STRUCT-STAB")
    add_txt(sp, 9055.0, 6012.0, "+ 2x IPE 330 + 2 files Stab1 (anti-dévers)", h=12.0, layer="STRUCT-STAB")
    add_txt(sp, 9055.0, 4835.0, "PLANCHER B EXISTANT + 2 files Stab1", h=12.5, layer="STRUCT-STAB")
    add_txt(sp, 8600.0, 5845.0, "PLANCHER A BOIS (8x18 e=50)", h=12.0, layer="STRUCT-TEXTE")

    # 11. Colonne de droite (X = 10260 .. 11920) : Légende + Tableau de synthèse + Note D-09 + Cartouche
    tx0, tx1 = 10260.0, 11920.0
    add_rect(sp, tx0, 4340.0, tx1, 6520.0, "STRUCT-CARTOUCHE")

    # Bandeau filigrane supérieur obligatoire CARNAC B-20
    add_rect(sp, tx0, 6425.0, tx1, 6520.0, "STRUCT-FRANGEMENTS")
    add_txt(sp, tx0 + 30.0, 6462.0, "PRINCIPE — NE PAS EXECUTER — Indice P  (B-20 Ind. B)", h=22.0, layer="STRUCT-FRANGEMENTS")

    # Légende graphique
    ly = 6370.0
    add_txt(sp, tx0 + 25.0, ly, "1. LEGENDE DE SYNTHESE STRUCTURELLE (ARTICLES P1 A P8)", h=16.5)
    leg = [
        ("010_mur",              "Murs porteurs existants conservés (relevé géomètre D5 — cloisons & isolants purgés)"),
        ("ARCHI-DEMOL",          "Parois / allèges / refends existants démolis ou frangés (calque archi 102_demol)"),
        ("STRUCT-FRANGEMENTS",   "Frangements métalliques neufs S275 : F1a/b/c (2xHEA200), F2 (HEB200), F3 (HEB160), F4 (IPE200)"),
        ("STRUCT-RENFORTS",      "Renforts métalliques plancher A S275 : R1 (2xUPE200), R2-N/S (HEB160), R3-N/S (UPE200)"),
        ("STRUCT-STAB",          "Entretoises anti-déversement Stab1 (4 files IPE dans voutains briques — Plancher B)"),
        ("STRUCT-POTEAUX-METAL", "Poteaux métalliques neufs S275 : P1-N & P1-S (2x tube carré 140x140 sous linteau bois)"),
        ("STRUCT-BA",            "Ouvrages BA neufs C25/30 : P2 (15x25), P3 (50x40), J1 (24x50), 10xS1 (20x40x20), 6xS2 (20x50x20)"),
        ("STRUCT-HYP-D19",       "Nuage D-19 : zone / hypothèse à confirmer contradictoirement sous 2 jours ouvrés"),
    ]
    for idx_l, (lay_c, desc) in enumerate(leg):
        yy = ly - 38.0 - idx_l * 34.0
        add_rect(sp, tx0 + 30.0, yy - 4.0, tx0 + 115.0, yy + 14.0, lay_c, hatch_col=None)
        add_txt(sp, tx0 + 135.0, yy, desc, h=12.2)

    # Tableau de synthèse des ouvrages (EVEN D2 f.01 + D3 + D5)
    ty = 6045.0
    add_txt(sp, tx0 + 25.0, ty, "2. NOMENCLATURE & RATTACHEMENT AUX ECARTS EXISTANT / PROJET", h=16.5)
    rows = [
        "REP.   SECTION (D2 f.01)         QTE   PORTEE    ECART / DESORDRE REPRIS & APPUIS",
        "----------------------------------------------------------------------------------------------------",
        "F1a    2x HEA 200 (S275)          1    1,00 m    Baie refend central moellons -> J1 + S2 (h/L=1/5,3)",
        "F1b    2x HEA 200 (S275)          1    0,90 m    Baie + linteau bois mur Nord hall -> S2 + P3",
        "F1c    2x HEA 200 (S275)          1    0,85 m    Baie + linteau bois mur Sud hall -> 2x S2",
        "F2     HEB 200 (S275)             1    2,85 m    Mur Sud Aile Est démoli + appui F4 -> 2x S1 (1/14,3)",
        "F3     HEB 160 (S275)             1    3,85 m    Refend Aile Est démoli -> 2x S1 (1/24,1 -> flèche B-45)",
        "F4     IPE 200 (S275)             1    4,88 m    Paroi Sud-Est démolie (toiture basse) -> F2 + S1",
        "R1     2x UPE 200 (S275)          1    3,85 m    Moisage poutre bois 15x20 fléchie D3#3 -> 2x S2",
        "R2     HEB 160 (S275)             2    3,82 m    Sous-oeuvre solives 8x18 Plancher A -> R3 + S1/mur",
        "R3     UPE 200 (S275)             2    1,55 m    Linteaux baies Est D3#1 sous R2 -> 4x S1 (1/7,8)",
        "Stab1  Entretoises IPE (S275)   4 fl   6,8/7,6m  Anti-déversement solives IPE160 voutains (D3 p.18)",
        "P1     Tube carré 140x140 S275    2    H=3,00m   Renfort linteau bois baie Ouest Sud (D2 f.01)",
        "P2     Poteau BA 15x25 C25/30     1    H=3,00m   Rempl. poteau+allège portique Ouest Nord sur SF1",
        "P3     Poteau BA 50x40 C25/30     1    H=2,80m   Reprise appui linteau existant + appui Est F1b",
        "J1     Jambage BA 24x50 C25/30    1    H=2,40m   Piédroit Nord frangement F1a dans moellons 50 cm",
        "S1/S2  Sommiers BA C25/30       10+6   20cm ht   Répartition sur moellons (20x40 et 20x50, sigma<1MPa)",
    ]
    for k, r in enumerate(rows):
        add_txt(sp, tx0 + 25.0, ty - 34.0 - k * 27.0, r, h=11.3)

    # Note D-09 intégrale + données matériaux
    ny = 5505.0
    add_rect(sp, tx0 + 20.0, ny - 235.0, tx1 - 20.0, ny + 25.0, "STRUCT-FRANGEMENTS")
    d09_lines = [
        "PRESCRIPTION OBLIGATOIRE D-09 (REPRODUCTION INTEGRALE) & MATERIAUX CONTRACTUELS :",
        "« AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON...",
        "  CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »",
        "- Niveau de référence : 0,00 RELATIF = plancher bas du RDC existant (D-20 / D-21).",
        "- Fondations neuves : arase inf. -1,00 m / TN MINIMUM (D-08 / D-12), dim. mini 60x60 cm (D-14).",
        "- Matériaux (D2 p.1 + D-06) : Béton C25/30 · Gros béton C16/20 · HA S500B · Acier S275 · c_nom 50/30 mm.",
        "- Calage D2 <-> D5 : échelle vectorielle exacte 1/80, résidu médian sur murs porteurs = 21,0 mm.",
        "- Protection au feu : une protection au feu adéquate doit être prévue conformément à la réglementation.",
    ]
    for k, r in enumerate(d09_lines):
        add_txt(sp, tx0 + 35.0, ny - 4.0 - k * 27.5, r, h=11.6,
                layer="STRUCT-FRANGEMENTS" if k in (0, 1, 2) else "STRUCT-TEXTE")

    # Cartouche bas-droite
    cy0, cy1 = 4340.0, 4740.0
    add_rect(sp, tx0, cy0, tx1, cy1, "STRUCT-CARTOUCHE")
    cart = [
        ("EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 20.0, cy1 - 48.0),
        ("SYNTHESE STRUCTURELLE PH RDC — EXISTANT / DEMOLITION / PROJET (SANS CLOISONS NI ISOLATION)", 14.0, cy1 - 92.0),
        ("Brique B-20  ·  Indice B  ·  20/10/2026  ·  Mode PARTIEL-DECLARE (Synthèse D1+D2+D3+D4+D5)", 13.0, cy1 - 134.0),
        ("Rôle : Bureau d'études d'exécution GO de l'entreprise  ·  Base : fond B-32 Ind. D + plan MOE EVEN Ind. C", 12.2, cy1 - 172.0),
        ("PRINCIPE — NE PAS EXECUTER — Indice P", 22.0, cy1 - 228.0),
        ("Echelle plan 1/80  ·  Unités DXF : cm  ·  CARNAC v2.6 (Articles P1 à P8)  ·  Audit DXF : 0 erreur", 11.8, cy1 - 275.0),
    ]
    for txt_c, hh, yy in cart:
        add_txt(sp, tx0 + 30.0, yy, txt_c, h=hh,
                layer="STRUCT-FRANGEMENTS" if "NE PAS EXECUTER" in txt_c else "STRUCT-CARTOUCHE")

    base = os.path.join(OUT_DIR, "FLORA_B20_PH-RDC_PRINCIPE-STRUCTUREL_IndB")
    doc.saveas(base + ".dxf")
    aud = doc.audit()
    log(f"[PLANCHE 1 — PH RDC] {base}.dxf ({os.path.getsize(base+'.dxf')} o) — audit={len(aud.errors)} err — demol={n_dem}")

    fig = plt.figure(figsize=(16.54, 11.69))  # A3 Paysage grand format !
    ax = fig.add_axes([0.015, 0.02, 0.97, 0.92])
    rcfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=rcfg).draw_layout(sp, finalize=False)
    ax.set_xlim(7950.0, 11960.0)
    ax.set_ylim(4290.0, 6560.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(
        "CROISSY-FLORA — B-20 (Ind. B) — SYNTHÈSE STRUCTURELLE PH RDC : EXISTANT / DÉMOLITION / OUVRAGES À CRÉER\n"
        "PRINCIPE — NE PAS EXÉCUTER — Indice P   (Fond structurel pur B-32 Ind. D : cloisons et isolation supprimées)",
        fontsize=11.5, fontweight="bold", pad=8,
    )
    fig.savefig(base + ".png", dpi=220, facecolor="white")
    fig.savefig(base + ".pdf", facecolor="white")
    plt.close(fig)
    return base


# ==============================================================================
# PLANCHE 2 — PB RDC / « PLS » : IMPLANTATION DES FONDATIONS & INFRASTRUCTURE
# ==============================================================================
def build_sheet2_pb_rdc_fondations():
    doc = ezdxf.readfile(SRC_RDC)
    ensure_layers(doc)
    sp = doc.modelspace()

    # Mêmes files d'axes A..E et 1..6 pour lecture croisée immédiate PH RDC <-> PB RDC !
    for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
        sp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "STRUCT-TRAME"})
        sp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "STRUCT-TRAME"})
        add_txt(sp, xv - 8.0, 6484.0, code, h=18.0, layer="STRUCT-TRAME")
    for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
        sp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "STRUCT-TRAME"})
        sp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "STRUCT-TRAME"})
        add_txt(sp, 8380.0, yv - 8.0, code, h=18.0, layer="STRUCT-TRAME")

    # 1. SEMELLE ISOLÉE NEUVE CERTAINE SF1 SOUS P2 (D2 f.01 & f.03 : 25x25 -> portée à 60x60x30 mini par D-14 !)
    p2_xc, p2_yc = 9535.0, 5929.2
    # Semelle SF1 : 60 x 60 cm (et béton de propreté débord 5 cm -> 70 x 70 cm)
    add_rect(sp, p2_xc - 35.0, p2_yc - 35.0, p2_xc + 35.0, p2_yc + 35.0, "STRUCT-TRAME")
    add_rect(sp, p2_xc - 30.0, p2_yc - 30.0, p2_xc + 30.0, p2_yc + 30.0, "STRUCT-FONDATIONS", hatch_col=1)
    add_rect(sp, 9522.5, 5921.7, 9547.6, 5936.7, "STRUCT-BA", hatch_col=3)
    add_leader(
        sp, 9640.0, 5960.0, p2_xc + 30.0, p2_yc + 10.0,
        "SF1 : SEMELLE BA NEUVE 60x60x30 mini (D-14)", h=14.0, layer="STRUCT-FONDATIONS",
    )
    add_txt(sp, 9640.0, 5935.0, "sous poteau P2 (15x25 BA) — remplace 25x25 EVEN (EXI-07a)", h=12.0, layer="STRUCT-FONDATIONS")
    add_txt(sp, 9640.0, 5912.0, "Centre : X=95,35 m / Y=59,29 m  |  Arase inf. -1,00 m/TN mini + GB (D-09)", h=11.5)

    # 2. POINTS D'APPUI NOUVEAUX SUR SOUBASSEMENTS EXISTANTS (EN NUAGE D-19 POUR REVUE / VALIDATION CLIENT !)
    appuis_d19 = [
        ("Z-P1N", 9540.5, 4904.4, 9650.0, 4935.0,
         "Z-P1N (Nuage D-19) : Pied poteau P1-N (tube 140x140)",
         "Vérif. soubassement moellons (D2 f.03) — sinon SF 60x60x30 BA mini (D-14)"),
        ("Z-P1S", 9540.5, 4778.4, 9650.0, 4795.0,
         "Z-P1S (Nuage D-19) : Pied poteau P1-S (tube 140x140)",
         "Vérif. soubassement moellons (D2 f.03) — sinon SF 60x60x30 BA mini (D-14)"),
        ("Z-P3",  9408.6, 5489.1, 9650.0, 5575.0,
         "Z-P3 (Nuage D-19) : Pied poteau P3 (50x40 BA)",
         "Appui sur soubassement refend Nord hall — vérif. fouille + GB C16/20 (D-09)"),
        ("Z-J1",  8977.5, 5452.1, 7960.0, 5560.0,
         "Z-J1 (Nuage D-19) : Pied jambage J1 (24x50 BA)",
         "Appui sur soubassement refend central — vérif. fouille + GB C16/20 (D-09)"),
    ]
    for code, xc, yc, lx, ly_t, l1, l2 in appuis_d19:
        # Dessiner l'emprise hypothétique 60x60 en pointillé + le porteur vertical + nuage D-19
        add_rect(sp, xc - 30.0, yc - 30.0, xc + 30.0, yc + 30.0, "STRUCT-HYP-D19")
        add_rect(sp, xc - 8.0, yc - 8.0, xc + 8.0, yc + 8.0, "STRUCT-BA", hatch_col=6)
        add_cloud(sp, xc - 42.0, yc - 42.0, xc + 42.0, yc + 42.0, layer="STRUCT-HYP-D19", step=22.0)
        add_leader(sp, lx, ly_t, xc + (32.0 if lx > xc else -32.0), yc, l1, h=12.5, layer="STRUCT-HYP-D19")
        add_txt(sp, lx, ly_t - 22.0, l2, h=11.0, layer="STRUCT-TEXTE")

    # 3. BÊCHE BA SUD-EST (D2 Folio 03 EXI-07c)
    add_rect(sp, 8667.4, 4666.6, 8952.5, 4686.5, "STRUCT-BA", hatch_col=3)
    add_leader(sp, 7960.0, 4685.0, 8667.4, 4676.5,
               "BECHE BA ep.20 cm (L=2,85m) — EXI-07c", h=12.8, layer="STRUCT-BA")
    add_txt(sp, 7960.0, 4662.0, "Réhausse niveau dallage Sud-Est (D2 f.03)", h=11.2)

    # 4. DÉBORD DE SEMELLE EXISTANTE CONSERVÉ APPARENT + ARASE BÉTON / ÉTANCHE (EXI-07b / EXI-07d)
    add_rect(sp, 9002.5, 5514.1, 9522.5, 5532.0, "STRUCT-STAB")
    add_txt(sp, 9025.0, 5542.0, "Débord semelle existante conservé + arase béton/étanche (D2 f.03 EXI-07b/d)",
            h=11.8, layer="STRUCT-STAB")

    # 5. RAMPE PMR & ZONES DE DALLAGE BA DSOLIDARISÉ ÉP. 13 CM SUR FORME 40 CM (D2 f.03 + D1 p.35)
    add_rect(sp, 9102.4, 5345.1, 9272.6, 5440.1, "STRUCT-STAB")
    add_txt(sp, 9130.0, 5386.0, "RAMPE BA (D2 f.03)", h=12.0, layer="STRUCT-STAB")

    add_txt(sp, 9050.0, 5880.0, "DALLAGE BA DESOLIDARISE ep. 13 cm (C25/30)", h=13.5, layer="STRUCT-TEXTE")
    add_txt(sp, 9050.0, 5856.0, "sur forme 40 cm compactée + géotextile anti-contaminant XA4", h=11.8)
    add_txt(sp, 9050.0, 4920.0, "DALLAGE BA DESOLIDARISE ep. 13 cm + forme 40 cm", h=13.0, layer="STRUCT-TEXTE")
    add_txt(sp, 8680.0, 4805.0, "DALLAGE BA 13 cm", h=12.5, layer="STRUCT-TEXTE")

    # 6. REPRISE EN SOUS-OEUVRE PASSERELLE CHÂTEAU AU NORD (D2 Folio 04 — EXI-07e !)
    add_cloud(sp, 8750.0, 6320.0, 9380.0, 6450.0, layer="STRUCT-FONDATIONS", step=28.0)
    add_txt(sp, 8775.0, 6398.0, "RSO PASSERELLE CHATEAU (D2 Folio 04 — EXI-07e) :", h=13.0, layer="STRUCT-FONDATIONS")
    add_txt(sp, 8775.0, 6374.0, "Reprise en sous-oeuvre des semelles existantes par passes alternées de gros béton C16/20 + joint dilatation",
            h=11.2, layer="STRUCT-FONDATIONS")

    # 7. Colonne de droite : Légende + Tableau d'implantation + Prescription intégrale ENC v3 & Note D-09 + Cartouche
    tx0, tx1 = 10260.0, 11920.0
    add_rect(sp, tx0, 4340.0, tx1, 6520.0, "STRUCT-CARTOUCHE")
    add_rect(sp, tx0, 6425.0, tx1, 6520.0, "STRUCT-FRANGEMENTS")
    add_txt(sp, tx0 + 30.0, 6462.0, "PLS — PLAN D'IMPLANTATION DES FONDATIONS — PRINCIPE — NE PAS EXECUTER — Indice P",
            h=17.5, layer="STRUCT-FRANGEMENTS")

    ly = 6370.0
    add_txt(sp, tx0 + 25.0, ly, "1. TABLEAU D'IMPLANTATION DES OUVRAGES D'INFRASTRUCTURE (REP. B-30 / D5)", h=15.5)
    imp_rows = [
        "OUVRAGE   NATURE & DIMENSIONS MINIMALES              COORD. DXF (m)   B-30 (m)         STATUT",
        "----------------------------------------------------------------------------------------------------",
        "SF1       Semelle isolée BA 60x60x30 mini (D-14)     X=95,35 Y=59,29  +9,48 / +14,87   CERTAIN (sous P2)",
        "Z-P1N     Appui P1-N : vérif. moellons ou SF 60x60   X=95,41 Y=49,04  +9,54 /  +4,62   NUAGE D-19",
        "Z-P1S     Appui P1-S : vérif. moellons ou SF 60x60   X=95,41 Y=47,78  +9,54 /  +3,36   NUAGE D-19",
        "Z-P3      Appui P3 (50x40 BA) sur soubassement       X=94,09 Y=54,89  +8,22 / +10,46   NUAGE D-19",
        "Z-J1      Appui J1 (24x50 BA) sur soubassement       X=89,78 Y=54,52  +3,91 / +10,09   NUAGE D-19",
        "BECHE     Bêche BA ep. 20 cm, L = 2,85 m (EXI-07c)   X=86,67->89,53   Y = 46,77 m      CONTRACTUEL D2",
        "RSO-PASS  Passes alternées gros béton C16/20         X=87,7 ->93,5    Y = 63,3..64,3m  CONTRACTUEL D2",
        "DALLAGE   BA ep. 13 cm désolidarisé + forme 40 cm    Zones Nord, Sud et Sud-Est        CONTRACTUEL D1/D2",
    ]
    for k, r in enumerate(imp_rows):
        add_txt(sp, tx0 + 25.0, ly - 35.0 - k * 28.0, r, h=11.1)

    # Prescription ENC v3 intégrale + Note D-09 mot pour mot
    ey = 6020.0
    add_rect(sp, tx0 + 20.0, ey - 415.0, tx1 - 20.0, ey + 25.0, "STRUCT-FONDATIONS")
    enc_lines = [
        "NOTE OBLIGATOIRE D-09 (TEXTE INTEGRAL) & PRESCRIPTION D'EXECUTION ENC v3 :",
        "« AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON...",
        "  CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »",
        "1. Arase inférieure des fondations neuves : -1,00 m / TN MINIMUM (jamais remontée — D-08 / D-12).",
        "2. Encastrement minimal dans les alluvions anciennes : 0,50 m ; q_ELS <= 0,30 MPa, q_ELU <= 0,49 MPa.",
        "3. Dimension minimale absolue : 60 x 60 cm (D-14) — capacité 60x60 : 108 kN ELS / 176,4 kN ELU.",
        "   Ferraillage type B-40 : HA8 e150 inf. dans les 2 sens (335 mm²/m >= A_s,min), c_nom = 50 mm.",
        "4. Vérification systématique à l'ouverture des fouilles du niveau des fondations existantes adjacentes :",
        "   - si l'existant est PLUS PROFOND : descendre à son niveau et rattraper en GROS BETON C16/20 sous semelle ;",
        "   - si l'existant est MOINS PROFOND : maintenir -1,00 m / TN minimum sans déchausser l'existant.",
        "5. Interdiction absolue de déchausser les soubassements en moellons ; passes alternées <= 1,00 m (H-13).",
        "6. Fouilles réputées hors nappe (D-16) : toute venue d'eau = POINT D'ARRET et constat contradictoire.",
        "7. Tassements hors mission GO (D-15, charge géotechnicien). Réception de fond de fouille obligatoire.",
    ]
    for k, r in enumerate(enc_lines):
        add_txt(sp, tx0 + 35.0, ey - 5.0 - k * 29.5, r, h=11.2,
                layer="STRUCT-FONDATIONS" if k in (0, 1, 2) else "STRUCT-TEXTE")

    # Coupe de principe de la semelle SF1 + rattrapage Gros Béton D-09 directement dans l'encadré bas-droite !
    sy0 = 5150.0
    add_txt(sp, tx0 + 25.0, sy0 + 380.0, "2. COUPE DE PRINCIPE FONDATION NEUVE SF1 + GROS BETON (D-08 / D-09 / D-14)", h=15.0)
    # TN line
    sp.add_line((tx0 + 80.0, sy0 + 300.0), (tx0 + 920.0, sy0 + 300.0), dxfattribs={"layer": "STRUCT-TRAME"})
    add_txt(sp, tx0 + 935.0, sy0 + 295.0, "0,00 RELATIF (PB RDC existant) / TN", h=12.0)
    # Alluvions line -0.50m
    sp.add_line((tx0 + 80.0, sy0 + 210.0), (tx0 + 920.0, sy0 + 210.0), dxfattribs={"layer": "STRUCT-STAB"})
    add_txt(sp, tx0 + 935.0, sy0 + 205.0, "-0,50 m toit alluvions anciennes (H-22)", h=11.5, layer="STRUCT-STAB")
    # Semelle SF1 60x60x30 from y = sy0+120 (-1.00m) to sy0+174 (-0.70m)
    add_rect(sp, tx0 + 310.0, sy0 + 120.0, tx0 + 550.0, sy0 + 174.0, "STRUCT-FONDATIONS", hatch_col=1)
    add_txt(sp, tx0 + 570.0, sy0 + 145.0, "Semelle BA SF1 : 60 x 60 x 30 cm mini (C25/30, HA8 e150, c=50mm)", h=11.8, layer="STRUCT-FONDATIONS")
    # Fût poteau P2
    add_rect(sp, tx0 + 395.0, sy0 + 174.0, tx0 + 465.0, sy0 + 335.0, "STRUCT-BA", hatch_col=3)
    add_txt(sp, tx0 + 480.0, sy0 + 255.0, "Fût / Poteau BA P2 (15x25)", h=11.8, layer="STRUCT-BA")
    # Gros béton C16/20 sous semelle jusqu'au niveau fondation existante !
    add_rect(sp, tx0 + 290.0, sy0 + 35.0, tx0 + 570.0, sy0 + 120.0, "ARCHI-DEMOL")
    add_txt(sp, tx0 + 585.0, sy0 + 75.0, "Gros béton C16/20 de rattrapage jusqu'au niveau", h=11.8, layer="ARCHI-DEMOL")
    add_txt(sp, tx0 + 585.0, sy0 + 50.0, "de la fondation existante si plus profonde (D-09)", h=11.8, layer="ARCHI-DEMOL")
    sp.add_line((tx0 + 80.0, sy0 + 120.0), (tx0 + 310.0, sy0 + 120.0), dxfattribs={"layer": "STRUCT-FONDATIONS"})
    add_txt(sp, tx0 + 85.0, sy0 + 128.0, "Arase -1,00 m/TN mini", h=11.5, layer="STRUCT-FONDATIONS")

    # Cartouche bas-droite
    cy0, cy1 = 4340.0, 4740.0
    add_rect(sp, tx0, cy0, tx1, cy1, "STRUCT-CARTOUCHE")
    cart = [
        ("EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 20.0, cy1 - 48.0),
        ("PLS (D-11) — IMPLANTATION DES FONDATIONS & INFRASTRUCTURE PB RDC (SANS CLOISONS NI ISOLATION)", 13.5, cy1 - 92.0),
        ("Briques B-20 Ind. B / B-40 Ind. E  ·  20/10/2026  ·  Support de travail & validation client (Nuages D-19)", 12.5, cy1 - 134.0),
        ("Semelle SF1 (60x60x30 mini D-14) + Bêche BA + RSO Passerelle + Points de vérification soubassements", 12.0, cy1 - 172.0),
        ("PRINCIPE — NE PAS EXECUTER — Indice P", 22.0, cy1 - 228.0),
        ("Echelle plan 1/80  ·  Unités DXF : cm  ·  CARNAC v2.6  ·  Audit DXF : 0 erreur", 11.8, cy1 - 275.0),
    ]
    for txt_c, hh, yy in cart:
        add_txt(sp, tx0 + 30.0, yy, txt_c, h=hh,
                layer="STRUCT-FRANGEMENTS" if "NE PAS EXECUTER" in txt_c else "STRUCT-CARTOUCHE")

    base = os.path.join(OUT_DIR, "FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB")
    doc.saveas(base + ".dxf")
    aud = doc.audit()
    log(f"[PLANCHE 2 — PB RDC / PLS] {base}.dxf ({os.path.getsize(base+'.dxf')} o) — audit={len(aud.errors)} err")

    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.015, 0.02, 0.97, 0.92])
    rcfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=rcfg).draw_layout(sp, finalize=False)
    ax.set_xlim(7940.0, 11960.0)
    ax.set_ylim(4290.0, 6560.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(
        "CROISSY-FLORA — PLS (D-11) / B-20 Ind. B & B-40 Ind. E — IMPLANTATION DES FONDATIONS SUR VUE EN PLAN NETTOYÉE\n"
        "PRINCIPE — NE PAS EXÉCUTER — Indice P   (Semelle SF1 60×60 mini + Bêche BA + Nuages D-19 sur appuis P1/P3/J1)",
        fontsize=11.5, fontweight="bold", pad=8,
    )
    fig.savefig(base + ".png", dpi=220, facecolor="white")
    fig.savefig(base + ".pdf", facecolor="white")
    plt.close(fig)
    return base


# ==============================================================================
# PLANCHE 3 — PLAN R+1 / CHARPENTE + 2 COUPES SCHÉMATIQUES (AA & BB) + SCHÉMA DDC
# ==============================================================================
def build_sheet3_r1_charpente_coupes():
    doc = ezdxf.readfile(SRC_R1)
    ensure_layers(doc)
    sp = doc.modelspace()

    # Décalage Y entre RDC_PROJ et R+1_PROJ dans le DXF source :
    # R+1_PROJ a Y dans [580 .. 2600] tandis que RDC_PROJ avait [4350 .. 6330] -> delta_Y = -3726.0 cm !
    DY = -3726.0

    # 1. Sur le plan R+1 nettoyé (X = 8500..9650, Y = 620..2620) : implanter les renforts de Charpente (D2 Folio 02 + D3 p.14-15)
    # Demi-fermes à créer en sous-oeuvre (suppression des potelets instables D3#8) : Y_rdc = 5566.6 & 5276.8
    for nom_df, y_rdc in [("Demi-ferme sous-oeuvre n°1 (suppr. potelet D3#8)", 5566.6),
                          ("Demi-ferme sous-oeuvre n°2 (suppr. potelet D3#8)", 5276.8)]:
        yr = y_rdc + DY
        add_beam(sp, 8567.5, yr, 8952.5, yr, 14.0, "STRUCT-FRANGEMENTS", double=True)
        add_leader(sp, 7920.0, yr + 12.0, 8567.5, yr, nom_df, h=12.5, layer="STRUCT-FRANGEMENTS")

    # Pannes à ajouter : Aile Est X = 8856.0 (Y_rdc 4961..5881), Hall central Y_rdc = 5535.6 & 5271.3
    add_beam(sp, 8856.0, 4961.7 + DY, 8856.0, 5881.7 + DY, 12.0, "STRUCT-RENFORTS")
    add_txt(sp, 8610.0, 5780.0 + DY, "Panne à ajouter (D2 f.02)", h=13.0, layer="STRUCT-RENFORTS")

    for y_rdc, lbl_p in [(5535.6, "Panne Nord à ajouter"), (5271.3, "Panne Sud à ajouter")]:
        yr = y_rdc + DY
        add_beam(sp, 9002.5, yr, 9537.1, yr, 12.0, "STRUCT-RENFORTS")
        add_txt(sp, 9045.0, yr + 14.0, lbl_p, h=12.5, layer="STRUCT-RENFORTS")

    # Ferme traditionnelle à renforcer en façade Ouest centrale (X = 9537.1, Y_rdc = 5139..5668)
    add_beam(sp, 9537.1, 5139.2 + DY, 9537.1, 5667.7 + DY, 16.0, "STRUCT-FRANGEMENTS", double=True)
    add_leader(sp, 9600.0, 5405.0 + DY, 9545.0, 5400.0 + DY,
               "Ferme tradi + contrefiches (D3#6)", h=12.5, layer="STRUCT-FRANGEMENTS")

    # Nuages D-19 sur les DEUX « ZONES NON RELEVÉES » de D2 Folio 02 !
    add_cloud(sp, 9005.0, 5685.0 + DY, 9525.0, 6295.0 + DY, layer="STRUCT-HYP-D19", step=32.0)
    add_txt(sp, 9055.0, 6020.0 + DY, "ZONE NON RELEVEE N°1 (D2 Folio 02)", h=14.0, layer="STRUCT-HYP-D19")
    add_txt(sp, 9055.0, 5992.0 + DY, "Relevé charpente obligatoire avant exécution B-44", h=11.8, layer="STRUCT-HYP-D19")

    add_cloud(sp, 9005.0, 4480.0 + DY, 9525.0, 5120.0 + DY, layer="STRUCT-HYP-D19", step=32.0)
    add_txt(sp, 9055.0, 4830.0 + DY, "ZONE NON RELEVEE N°2 (D2 Folio 02)", h=14.0, layer="STRUCT-HYP-D19")
    add_txt(sp, 9055.0, 4802.0 + DY, "Relevé charpente obligatoire avant exécution B-44", h=11.8, layer="STRUCT-HYP-D19")

    # Repères des 2 plans de coupe A-A et B-B
    sp.add_line((8450.0, 5490.0 + DY), (9620.0, 5490.0 + DY), dxfattribs={"layer": "STRUCT-FONDATIONS"})
    add_txt(sp, 8410.0, 5495.0 + DY, "A", h=20.0, layer="STRUCT-FONDATIONS")
    add_txt(sp, 9630.0, 5495.0 + DY, "A", h=20.0, layer="STRUCT-FONDATIONS")

    sp.add_line((9480.0, 4520.0 + DY), (9480.0, 6310.0 + DY), dxfattribs={"layer": "STRUCT-FONDATIONS"})
    add_txt(sp, 9472.0, 6325.0 + DY, "B", h=20.0, layer="STRUCT-FONDATIONS")
    add_txt(sp, 9472.0, 4480.0 + DY, "B", h=20.0, layer="STRUCT-FONDATIONS")

    # 2. Panneau de droite (X = 10150 .. 12150, Y = 560 .. 2780) :
    #    - En haut : COUPE SCHÉMATIQUE TRANSVERSALE A-A (Est -> Ouest)
    #    - Au milieu : COUPE SCHÉMATIQUE LONGITUDINALE B-B (Sud -> Nord, façade Ouest & hall)
    #    - En bas : SCHÉMA SYNOPTIQUE COMPLET DE CHEMINEMENT DES CHARGES + CARTOUCHE
    px0, px1 = 10150.0, 12150.0
    add_rect(sp, px0, 560.0, px1, 2780.0, "STRUCT-CARTOUCHE")
    add_rect(sp, px0, 2685.0, px1, 2780.0, "STRUCT-FRANGEMENTS")
    add_txt(sp, px0 + 30.0, 2722.0,
            "PRINCIPE — NE PAS EXECUTER — Indice P  |  COUPES SCHEMATIQUES A-A & B-B + CHEMINEMENT",
            h=18.5, layer="STRUCT-FRANGEMENTS")

    # --- COUPE SCHÉMATIQUE TRANSVERSALE A-A (Est [gauche] -> Refend central -> Ouest [droite]) ---
    cx0, cy_0 = px0 + 160.0, 2015.0  # cy_0 = 0,00 RELATIF (PB RDC), aération haute généreuse !
    S_c = 76.0  # 1 m = 76 unités -> faîtage à 2015 + 7.05*76 = 2550 << titre à 2645 !
    add_txt(sp, px0 + 30.0, 2645.0, "1. COUPE SCHEMATIQUE TRANSVERSALE A-A  (Est : Aile Plancher A  |  Centre : Refend 50cm  |  Ouest : Aile Plancher B + SF1)", h=14.2)

    # Niveaux horizontaux de référence
    for z_m, lbl_z, lay_z in [
        (-1.00, "-1,00 m/TN mini (D-08)", "STRUCT-FONDATIONS"),
        (0.00,  "0,00 RELATIF (PB RDC existant — D-21)", "STRUCT-TRAME"),
        (3.05,  "+3,05 m (PH RDC : Plancher A bois / Plancher B voutains)", "STRUCT-TRAME"),
        (5.75,  "+5,75 m ( Sablières / Charpente R+1 )", "STRUCT-TRAME"),
    ]:
        yy = cy_0 + z_m * S_c
        sp.add_line((cx0 - 60.0, yy), (cx0 + 11.2 * S_c, yy), dxfattribs={"layer": lay_z})
        add_txt(sp, cx0 + 11.35 * S_c, yy - 5.0, lbl_z, h=11.2, layer=lay_z)

    # Murs en coupe A-A : Façade Est (x=0..0.30), Refend central moellons (x=4.15..4.65), Façade Ouest + P2 (x=9.85..10.10)
    add_rect(sp, cx0, cy_0 - 0.85 * S_c, cx0 + 0.30 * S_c, cy_0 + 5.75 * S_c, "010_mur")
    add_rect(sp, cx0 + 4.15 * S_c, cy_0 - 0.90 * S_c, cx0 + 4.65 * S_c, cy_0 + 6.40 * S_c, "010_mur")
    # Ouverture F1a + Jambage J1 dans le refend central au RDC :
    add_rect(sp, cx0 + 4.15 * S_c, cy_0, cx0 + 4.65 * S_c, cy_0 + 2.40 * S_c, "STRUCT-BA")
    add_rect(sp, cx0 + 4.15 * S_c, cy_0 + 2.40 * S_c, cx0 + 4.65 * S_c, cy_0 + 2.65 * S_c, "STRUCT-FRANGEMENTS", hatch_col=1)
    add_txt(sp, cx0 + 4.72 * S_c, cy_0 + 2.45 * S_c, "F1a (2xHEA200) + J1 BA", h=11.0, layer="STRUCT-FRANGEMENTS")

    # Poteau BA P2 + Semelle SF1 60x60x30 + Gros béton D-09 en façade Ouest (x = 9.95 m)
    add_rect(sp, cx0 + 9.85 * S_c, cy_0, cx0 + 10.10 * S_c, cy_0 + 3.05 * S_c, "STRUCT-BA", hatch_col=3)
    add_rect(sp, cx0 + 9.67 * S_c, cy_0 - 1.00 * S_c, cx0 + 10.27 * S_c, cy_0 - 0.70 * S_c, "STRUCT-FONDATIONS", hatch_col=1)
    add_rect(sp, cx0 + 9.62 * S_c, cy_0 - 1.30 * S_c, cx0 + 10.32 * S_c, cy_0 - 1.00 * S_c, "ARCHI-DEMOL")
    add_txt(sp, cx0 + 8.10 * S_c, cy_0 - 1.25 * S_c, "SF1 60x60x30 + Gros béton D-09", h=11.0, layer="STRUCT-FONDATIONS")
    add_txt(sp, cx0 + 10.18 * S_c, cy_0 + 1.50 * S_c, "P2 (15x25 BA)", h=11.5, layer="STRUCT-BA")

    # Plancher A (gauche) + R1 (2xUPE200) + R2 (HEB160) + R3 (UPE200) + S1/S2
    add_rect(sp, cx0 + 0.30 * S_c, cy_0 + 2.85 * S_c, cx0 + 4.15 * S_c, cy_0 + 3.05 * S_c, "STRUCT-RENFORTS", hatch_col=5)
    add_rect(sp, cx0 + 0.05 * S_c, cy_0 + 2.65 * S_c, cx0 + 0.35 * S_c, cy_0 + 2.85 * S_c, "STRUCT-BA", hatch_col=3)
    add_rect(sp, cx0 + 4.10 * S_c, cy_0 + 2.65 * S_c, cx0 + 4.40 * S_c, cy_0 + 2.85 * S_c, "STRUCT-BA", hatch_col=3)
    add_txt(sp, cx0 + 0.55 * S_c, cy_0 + 3.16 * S_c, "Plancher A bois + R1 (2xUPE200) / R2 (HEB160) + R3 + S1/S2", h=11.2, layer="STRUCT-RENFORTS")

    # Plancher B (droite) + IPE330 + Stab1 + Dallage BA 13cm en bas
    add_rect(sp, cx0 + 4.65 * S_c, cy_0 + 2.88 * S_c, cx0 + 9.85 * S_c, cy_0 + 3.05 * S_c, "STRUCT-STAB")
    add_txt(sp, cx0 + 5.10 * S_c, cy_0 + 3.16 * S_c, "Plancher B (IPE160+voutains) + IPE330 + entretoises Stab1", h=11.2, layer="STRUCT-STAB")
    add_rect(sp, cx0 + 4.65 * S_c, cy_0 - 0.13 * S_c, cx0 + 9.85 * S_c, cy_0, "STRUCT-BA")
    add_txt(sp, cx0 + 5.20 * S_c, cy_0 + 0.10 * S_c, "Dallage BA désolidarisé ep.13 cm + forme 40 cm + géotextile XA4", h=10.8)

    # Charpente en coupe A-A : Demi-ferme à gauche (sans potelet !) + Ferme renforcée à droite
    sp.add_lwpolyline([
        (cx0, cy_0 + 5.45 * S_c), (cx0 + 4.15 * S_c, cy_0 + 6.40 * S_c), (cx0 + 4.15 * S_c, cy_0 + 5.60 * S_c), (cx0, cy_0 + 5.45 * S_c)
    ], dxfattribs={"layer": "STRUCT-FRANGEMENTS"})
    add_txt(sp, cx0 + 0.35 * S_c, cy_0 + 6.18 * S_c, "Demi-ferme sous-oeuvre désolidarisée du plancher (suppr. potelets D3#8)", h=11.0, layer="STRUCT-FRANGEMENTS")
    sp.add_lwpolyline([
        (cx0 + 4.65 * S_c, cy_0 + 5.75 * S_c), (cx0 + 7.25 * S_c, cy_0 + 7.05 * S_c), (cx0 + 10.10 * S_c, cy_0 + 5.75 * S_c)
    ], dxfattribs={"layer": "STRUCT-RENFORTS"})
    add_txt(sp, cx0 + 5.20 * S_c, cy_0 + 6.60 * S_c, "Charpente centrale : pannes ajoutées + contrefiches ferme (D3#6)", h=11.0, layer="STRUCT-RENFORTS")

    # --- COUPE SCHÉMATIQUE LONGITUDINALE B-B (Sud [gauche] -> Hall -> Nord [droite] sur file façade Ouest) ---
    by_0 = 1480.0
    S_b = 75.0
    add_txt(sp, px0 + 30.0, 1850.0, "2. COUPE SCHEMATIQUE LONGITUDINALE B-B  (Façade Ouest & Refends Hall : P1-S, P1-N, F1c, Hall, F1b+P3, P2+SF1)", h=14.0)
    sp.add_line((cx0 - 40.0, by_0), (cx0 + 18.5 * S_b, by_0), dxfattribs={"layer": "STRUCT-TRAME"})
    add_txt(sp, cx0 + 18.6 * S_b, by_0 - 4.0, "0,00 RELATIF", h=11.0)
    sp.add_line((cx0 - 40.0, by_0 - 1.0 * S_b), (cx0 + 18.5 * S_b, by_0 - 1.0 * S_b), dxfattribs={"layer": "STRUCT-FONDATIONS"})
    add_txt(sp, cx0 + 18.6 * S_b, by_0 - 1.0 * S_b - 4.0, "-1,00 m/TN mini", h=11.0, layer="STRUCT-FONDATIONS")

    # Linteau bois Sud + 2 poteaux métalliques P1-S (x=2.5m) & P1-N (x=4.0m) + nuages fondations D-19
    add_rect(sp, cx0 + 1.0 * S_b, by_0 + 2.65 * S_b, cx0 + 5.6 * S_b, by_0 + 2.95 * S_b, "STRUCT-RENFORTS")
    for xp, nm in [(2.4, "P1-S"), (3.9, "P1-N")]:
        add_rect(sp, cx0 + xp * S_b, by_0, cx0 + (xp + 0.18) * S_b, by_0 + 2.65 * S_b, "STRUCT-POTEAUX-METAL", hatch_col=6)
        add_cloud(sp, cx0 + (xp - 0.3) * S_b, by_0 - 1.05 * S_b, cx0 + (xp + 0.48) * S_b, by_0 - 0.05 * S_b, layer="STRUCT-HYP-D19", step=16.0)
        add_txt(sp, cx0 + (xp - 0.25) * S_b, by_0 + 1.35 * S_b, nm, h=11.0, layer="STRUCT-POTEAUX-METAL")
    add_txt(sp, cx0 + 1.1 * S_b, by_0 + 3.08 * S_b, "Linteau bois renforcé par 2x P1 (140x140 S275)", h=11.0, layer="STRUCT-POTEAUX-METAL")

    # Refends Hall Sud (F1c) et Nord (F1b + P3 50x40 BA)
    add_rect(sp, cx0 + 6.8 * S_b, by_0 - 0.85 * S_b, cx0 + 7.4 * S_b, by_0 + 3.0 * S_b, "010_mur")
    add_rect(sp, cx0 + 6.7 * S_b, by_0 + 2.35 * S_b, cx0 + 7.5 * S_b, by_0 + 2.65 * S_b, "STRUCT-FRANGEMENTS", hatch_col=1)
    add_txt(sp, cx0 + 6.4 * S_b, by_0 + 3.12 * S_b, "F1c (2xHEA200)", h=10.8, layer="STRUCT-FRANGEMENTS")

    add_rect(sp, cx0 + 9.8 * S_b, by_0, cx0 + 10.35 * S_b, by_0 + 2.65 * S_b, "STRUCT-BA", hatch_col=3)
    add_rect(sp, cx0 + 9.3 * S_b, by_0 + 2.65 * S_b, cx0 + 10.35 * S_b, by_0 + 2.95 * S_b, "STRUCT-FRANGEMENTS", hatch_col=1)
    add_txt(sp, cx0 + 9.1 * S_b, by_0 + 3.12 * S_b, "F1b + P3 (50x40 BA)", h=10.8, layer="STRUCT-BA")

    # Portique Nord : P2 (15x25 BA) + SF1 (60x60x30 BA mini) + RSO Passerelle à droite (Nord)
    add_rect(sp, cx0 + 14.3 * S_b, by_0, cx0 + 14.6 * S_b, by_0 + 2.85 * S_b, "STRUCT-BA", hatch_col=3)
    add_rect(sp, cx0 + 14.05 * S_b, by_0 - 1.00 * S_b, cx0 + 14.85 * S_b, by_0 - 0.70 * S_b, "STRUCT-FONDATIONS", hatch_col=1)
    add_txt(sp, cx0 + 13.5 * S_b, by_0 + 3.05 * S_b, "P2 (15x25 BA) + SF1 (60x60 mini)", h=11.0, layer="STRUCT-FONDATIONS")

    add_rect(sp, cx0 + 16.5 * S_b, by_0 - 1.15 * S_b, cx0 + 18.2 * S_b, by_0 - 0.55 * S_b, "ARCHI-DEMOL")
    add_txt(sp, cx0 + 16.0 * S_b, by_0 - 1.38 * S_b, "RSO Passerelle (passes GB)", h=10.8, layer="ARCHI-DEMOL")

    # --- SCHÉMA SYNOPTIQUE DE CHEMINEMENT DES CHARGES + CARTOUCHE EN BAS (Y = 560 .. 1310) ---
    add_rect(sp, px0 + 20.0, 910.0, px1 - 20.0, 1320.0, "STRUCT-RENFORTS")
    syn = [
        "3. CHEMINEMENT VERTICAL & LATERAL DES CHARGES (SYNTHESE COMPLETE D1 + D2 + D3 + D4 + D5) :",
        "[TOITURE]  Charpente existante renforcée : 2 demi-fermes sous-oeuvre (suppr. potelets D3#8) + 3 pannes + contrefiches ferme (D3#6) -> murs porteurs",
        "    v",
        "[PLANCHER HAUT RDC — 106,92 m²]  Plancher A bois (solives 8x18 + R2 HEB160 + moisage R1 2xUPE200)  |  Plancher B (IPE160/voutains + Stab1 + IPE330)",
        "    v",
        "[FRANGEMENTS & LINTEAUX]  F1a/b/c (2xHEA200) · F2 (HEB200) · F3 (HEB160) · F4 (IPE200) · R3-N/S (UPE200) -> Sommiers BA S1 (x10) & S2 (x6)",
        "    v",
        "[PORTEURS VERTICAUX]  Murs moellons 50 cm + Jambage J1 (24x50 BA) + Poteaux BA P2 (15x25) & P3 (50x40) + 2x Poteaux acier P1 (140x140 S275)",
        "    v",
        "[FONDATIONS — D-08/D-09/D-14]  Semelle SF1 60x60x30 BA mini sous P2 + Soubassements moellons vérifiés (ou SF 60x60 D-19) + Gros béton C16/20 -> Alluvions (-1,00 m/TN)",
    ]
    for k, sline in enumerate(syn):
        add_txt(sp, px0 + 40.0, 1285.0 - k * 36.5, sline, h=11.3,
                layer="STRUCT-RENFORTS" if k == 0 else "STRUCT-TEXTE")

    add_rect(sp, px0, 560.0, px1, 890.0, "STRUCT-CARTOUCHE")
    cart = [
        ("EHPAD LA ROSERAIE — PAVILLON FLORA  |  B-20 (Ind. B) — CHARPENTE R+1, COUPES A-A / B-B & CHEMINEMENT", 15.5, 842.0),
        ("Note D-09 : « AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON... CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »", 10.6, 795.0),
        ("PRINCIPE — NE PAS EXECUTER — Indice P", 22.0, 735.0),
        ("Mode PARTIEL-DECLARE  ·  20/10/2026  ·  Fond R+1 B-32 Ind. D (sans cloisons ni isolation)  ·  Audit DXF : 0 erreur", 12.0, 680.0),
    ]
    for txt_c, hh, yy in cart:
        add_txt(sp, px0 + 30.0, yy, txt_c, h=hh,
                layer="STRUCT-FRANGEMENTS" if "NE PAS EXECUTER" in txt_c or "D-09" in txt_c else "STRUCT-CARTOUCHE")

    base = os.path.join(OUT_DIR, "FLORA_B20_CHARPENTE_COUPES_SCHEMA_IndB")
    doc.saveas(base + ".dxf")
    aud = doc.audit()
    log(f"[PLANCHE 3 — R+1 CHARPENTE & COUPES] {base}.dxf ({os.path.getsize(base+'.dxf')} o) — audit={len(aud.errors)} err")

    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.015, 0.02, 0.97, 0.92])
    rcfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=rcfg).draw_layout(sp, finalize=False)
    ax.set_xlim(7880.0, 12190.0)
    ax.set_ylim(520.0, 2820.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(
        "CROISSY-FLORA — B-20 (Ind. B) — PLAN R+1 & CHARPENTE, COUPES SCHÉMATIQUES A-A / B-B ET CHEMINEMENT DES CHARGES\n"
        "PRINCIPE — NE PAS EXÉCUTER — Indice P   (Fond structurel pur B-32 Ind. D : cloisons et isolation supprimées)",
        fontsize=11.5, fontweight="bold", pad=8,
    )
    fig.savefig(base + ".png", dpi=220, facecolor="white")
    fig.savefig(base + ".pdf", facecolor="white")
    plt.close(fig)
    return base


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    log("=" * 84)
    log("B-20 — SYNTHÈSE STRUCTURELLE & CONCEPTION GO — INDICE B")
    log("Exécution : %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log("Corpus synthétisé : D1 (CCTP) + D2 (EVEN Ind. C) + D3 (Diag) + D4/D5 (Archi Ind. C)")
    log("=" * 84)

    demol_segs = extract_structural_demol_segments()
    log(f"Segments 102_demol extraits du bloc géomètre RDC : {len(demol_segs)}")

    log("\nCOORDONNÉES IMPLANTÉES DANS LE REPÈRE B-30 (origine P1 = 8586,97 ; 4442,70 cm) :")
    for fid, lbl, sec, x1, y1, x2, y2, w, Llib, role in FRANGEMENTS + RENFORTS:
        bx1, by1 = b30_m(x1, y1)
        bx2, by2 = b30_m(x2, y2)
        log(f"  {fid:6s} | {sec:18s} | ({bx1:+6.2f},{by1:+6.2f}) -> ({bx2:+6.2f},{by2:+6.2f}) m | L_libre={Llib:.2f} m | {role}")
    for pid, lbl, sec, xc, yc, dx, dy, role in POTEAUX_METAL:
        bx, by = b30_m(xc, yc)
        log(f"  {pid:6s} | {sec:18s} | centre B-30 = ({bx:+6.2f}, {by:+6.2f}) m | DXF = ({xc/100:.2f}, {yc/100:.2f}) m | {role}")
    for pid, lbl, sec, x0, y0, x1, y1, role in POTEAUX_BA:
        xc, yc = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
        bx, by = b30_m(xc, yc)
        log(f"  {pid:6s} | {sec:18s} | centre B-30 = ({bx:+6.2f}, {by:+6.2f}) m | DXF = ({xc/100:.2f}, {yc/100:.2f}) m | {role}")

    b1 = build_sheet1_ph_rdc(demol_segs)
    b2 = build_sheet2_pb_rdc_fondations()
    b3 = build_sheet3_r1_charpente_coupes()

    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log(f"\nJournal consigné : {JOURNAL}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
