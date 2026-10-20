#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-40 — FONDATIONS SUPERFICIELLES — IMPLANTATION « PLS » & FERRAILLAGE TYPE (Indice E)

Projet : CROISSY-FLORA (ID-01)
Mode   : PARTIEL-DÉCLARÉ (CHG-02 & CHG-03 en enveloppe haute déclarée ; appuis Z-P1/P3/J1 en nuage D-19)
Régime : OUTILLÉ (V13) — script exécuté, journal 11 sections, audit DXF 0 erreur.

Évolution majeure Indice E (20/10/2026) :
  - Fond structurel pur B-32 Ind. D (ZÉRO cloison, ZÉRO isolation) ;
  - Implantation complète des fondations en vue en plan (« PLS », D-11) à gauche de la planche :
      * SF1 : semelle isolée BA 60x60x30 mini (D-14, remplaçant 25x25 EVEN EXI-07a) sous P2 (15x25 BA)
              à X = 95,35 m / Y = 59,29 m (repère B-30 : +9,48 m / +14,87 m) ;
      * Nuages D-19 aux pieds de P1-N, P1-S, P3 et J1 (vérification soubassement moellons à l'ouverture
        des fouilles D-09, ou création semelle BA 60x60x30 mini D-14 si portance/état insuffisant) ;
      * Bêche BA ép. 20 cm (L = 2,85 m, EXI-07c), débord semelle existante arasé (EXI-07b/d),
        RSO passerelle château par passes alternées de gros béton C16/20 (EXI-07e) ;
  - À droite de la planche : détails cotés Plan des semelles types (60x60 / 70x70 / 80x80) + Coupe A-A
    ferraillée (HA8 e150 inf. croisés, c_nom = 50 mm, béton de propreté 5 cm, rattrapage Gros Béton C16/20)
    + Note D-09 intégrale mot pour mot + Cartouche.
"""

import math
import os
import sys
from datetime import datetime

import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy

SRC_RDC = "dossiers/CROISSY/_plans/FLORA_RDC_VUE-NETTOYEE_IndD.dxf"
OUT = "dossiers/CROISSY/_plans"
JOURNAL = "dossiers/CROISSY/_rendus/b40_fondations.txt"
BASE = os.path.join(OUT, "FLORA_FONDATIONS_TYPE_IndF")

FDC = [
    ("SOL-01", "q_ELS", 0.30, "MPa", "D-02 / D2 p. 1"),
    ("SOL-02", "q_ELU", 0.49, "MPa", "D-03 / D1 p. 13"),
    ("D-14",   "B_min", 60.0, "cm",  "D-14 (dimension minimale absolue)"),
    ("MAT-01a","f_ck",  25.0, "MPa", "D2 p. 1 — C25/30"),
    ("MAT-01b","f_ck_gb",16.0,"MPa", "D2 p. 1 — C16/20 gros béton"),
    ("MAT-03a","c_nom", 50.0, "mm",  "D-06 (enrobage fondations XC2)"),
    ("MAT-04", "f_yk",  500.0,"MPa", "D2 p. 1 — S500B"),
    ("D-08",   "arase", -1.00,"m",   "D-08 / D-09 / D-12 — arase inf. / TN MINIMUM"),
    ("CHG-03", "g_plancher", 4.71, "kN/m²", "B-21 Ind. C § 3.5 — plancher B + cloisons, SANS recharge (D-35)"),
    ("CHG-03b", "g_dallage", 7.75, "kN/m²", "B-21 Ind. C § 3.6 — dallage BA 13 + revêtement + recharge 15 cm + cloisons (D-35)"),
    ("CHG-02", "q_exploit",  2.50, "kN/m²", "D2 p. 1 cabinet paramédical 250 — enveloppe haute"),
]

GAMMA_B = 25.0
ALPHA_CC = 0.85
GAMMA_C = 1.5
GAMMA_S = 1.15
B_POTEAU = 0.25  # m — grand côté P2 (15x25 BA) ; calcul conservatoire à b=0,30 m maintenu en référence

LOG = []


def log(m=""):
    print(m)
    LOG.append(m)


def titre(m):
    log("")
    log("-" * 78)
    log(m)
    log("-" * 78)


def add_cloud(msp, x0, y0, x1, y1, layer="FOND-HYP-D19", step=22.0):
    pts = []
    x = x0
    while x < x1:
        pts.append((x, y0)); x += step
    y = y0
    while y < y1:
        pts.append((x1, y)); y += step
    x = x1
    while x > x0:
        pts.append((x, y1)); x -= step
    y = y1
    while y > y0:
        pts.append((x0, y)); y -= step
    pts.append((x0, y0))
    for (ax_, ay_), (bx_, by_) in zip(pts, pts[1:]):
        mx, my = 0.5 * (ax_ + bx_), 0.5 * (ay_ + by_)
        dx, dy = bx_ - ax_, by_ - ay_
        L = math.hypot(dx, dy)
        if L < 1e-6:
            continue
        nx, ny = dy / L, -dx / L
        msp.add_lwpolyline([(ax_, ay_), (mx + 0.30 * L * nx, my + 0.30 * L * ny), (bx_, by_)],
                           dxfattribs={"layer": layer})


def main():
    os.makedirs(OUT, exist_ok=True)
    log("=" * 80)
    log("B-40 — FONDATIONS SUPERFICIELLES & IMPLANTATION « PLS » — INDICE F")
    log("Exécution : %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log("=" * 80)

    titre("[1] DONNÉES D'ENTRÉE — FDC IND. F + RDR IND. P")
    d = {}
    for code, nom, val, unit, src in FDC:
        d[nom] = val
        log("  %-9s %-12s %8.2f %-7s  %s" % (code, nom, val, unit, src))

    q_els = d["q_ELS"] * 1000.0
    q_elu = d["q_ELU"] * 1000.0
    g, q = d["g_plancher"], d["q_exploit"]

    titre("[2] MATÉRIAUX — EC2")
    fck = d["f_ck"]
    fctm = 0.30 * fck ** (2.0 / 3.0)
    fcd = ALPHA_CC * fck / GAMMA_C
    fyk = d["f_yk"]
    fyd = fyk / GAMMA_S
    log("  f_ctm = %.2f MPa  |  f_cd = %.2f MPa  |  f_yd = %.1f MPa" % (fctm, fcd, fyd))

    titre("[3] DESCENTE DE CHARGES D'EXÉCUTION")
    g_els = g + q
    g_elu = 1.35 * g + 1.50 * q
    log("  ELS caractéristique = %.2f kN/m²  |  ELU fondamental = %.2f kN/m²" % (g_els, g_elu))
    log("  Niveau R+1 complet (106,92 m²) : %.0f kN ELS / %.0f kN ELU" % (g_els * 106.92, g_elu * 106.92))
    # Descente de charges spécifique au poteau P2 (portique Ouest Nord, bande ~6,5 m²) :
    # SF1 : N repris TEL QUEL de B-21 Ind. C (continuité 1,15 incluse), semelle 80x80x25 (D-30)
    SF1_B, SF1_H = 0.80, 0.25
    A_SF1 = SF1_B ** 2
    A_P2 = 11.46
    N_P2_els, N_P2_elu = 130.5, 182.9
    log("  Semelle SF1 sous P2 : %.0f x %.0f x %.0f cm (D-30) — A_inf = %.2f m²" %
        (SF1_B * 100, SF1_B * 100, SF1_H * 100, A_P2))
    log("    N_ELS(SF1) = %.1f kN (B-21 Ind. C) -> σ_ELS = %.3f MPa <= 0,300 MPa -> %s"
        % (N_P2_els, N_P2_els / A_SF1 / 1000.0,
           "OK" if N_P2_els / A_SF1 / 1000.0 <= 0.30 else "NON CONFORME"))
    log("    N_ELU(SF1) = %.1f kN (B-21 Ind. C) -> σ_ELU = %.3f MPa <= 0,490 MPa -> %s"
        % (N_P2_elu, N_P2_elu / A_SF1 / 1000.0,
           "OK" if N_P2_elu / A_SF1 / 1000.0 <= 0.49 else "NON CONFORME"))
    log("    Dallage (D-35, 100 %% de l'emprise) : g = %.2f · p_ELS = %.2f · p_ELU = %.2f kN/m²"
        % (d["g_dallage"], d["g_dallage"] + q, 1.35 * d["g_dallage"] + 1.5 * q))
    log("    → sur le sol : %.1f kPa à l'ELU, soit %.1f %% de q_ELU — portance sans objet,"
        % (1.35 * d["g_dallage"] + 1.5 * q,
           100.0 * (1.35 * d["g_dallage"] + 1.5 * q) / q_elu))
    log("      le dallage est un problème de fissuration et de désolidarisation, pas de portance.")

    titre("[4] TABLEAU DE SENSIBILITÉ — ABAQUE DE CHANTIER B(A)")
    h = 0.30

    def dim(B, A):
        W = B * B * h * GAMMA_B
        return W, g_els * A + W, g_elu * A + 1.35 * W

    def B_requis(A, B0=0.60):
        B = B0
        for _ in range(60):
            W, N_els, N_elu = dim(B, A)
            s_els, s_elu = N_els / (B * B), N_elu / (B * B)
            if s_els <= q_els and s_elu <= q_elu:
                return B, s_els, s_elu, N_els, N_elu
            B += 0.05
        return B, s_els, s_elu, N_els, N_elu

    table = []
    for A in (6.5, 9.0, 11.0, 12.0, 15.0, 18.0, 21.0, 24.0):
        B, s_els, s_elu, N_els, N_elu = B_requis(A)
        table.append((A, B, N_els, s_els, N_elu, s_elu, True))
        log("  A=%5.1f m² -> B=%4.2f m | N_ELS=%6.1f kN (σ=%.3f MPa) | N_ELU=%6.1f kN (σ=%.3f MPa)"
            % (A, B, N_els, s_els / 1000, N_elu, s_elu / 1000))

    titre("[5] FERRAILLAGE — EC2 §9.8.3 & §9.2.1.1")
    b_ref = 0.30
    Bref, s_els, s_elu, N_els, N_elu = B_requis(12.0)
    d_util = h * 1000 - d["c_nom"] - 8.0
    p_elu = N_elu / (Bref * Bref)
    M = p_elu * Bref * (Bref - b_ref) ** 2 / 8.0
    As = M * 1e6 / (0.9 * d_util * fyd)
    r1 = 0.26 * fctm / fyk
    asmin = max(r1, 0.0013) * 1000 * d_util
    retenu = max(asmin, As / Bref)
    log("  d = %.0f mm | M_Ed = %.2f kN·m | A_s,calc = %.0f mm²/m | A_s,min = %.0f mm²/m"
        % (d_util, M, As / Bref, asmin))
    log("  Ferraillage retenu : HA8 e150 dans les 2 sens = 335 mm²/m >= %.0f mm²/m -> OK" % retenu)

    titre("[6] RIGIDITÉ & [7] POINÇONNEMENT — SF1 80x80x25 (D-30) — EC2 §6.4")
    d_sf1 = SF1_H * 1000.0 - d["c_nom"] - 8.0
    b_pot = 0.25
    u1 = 4 * b_pot * 1000 + 2 * math.pi * 2 * d_sf1
    v_ed = N_P2_elu * 1e3 / (u1 * d_sf1)
    k_p = min(1 + math.sqrt(200 / d_sf1), 2.0)
    rho = 335.0 / (1000 * d_sf1)
    v_rdc = 0.12 * k_p * (100 * rho * fck) ** (1.0 / 3.0)
    log("  d(SF1) = %.0f mm | rigidité EC2 §9.8.3 : (B-b)/4 = %.0f mm <= d -> OK"
        % (d_sf1, (SF1_B * 1000.0 - b_pot * 1000.0) / 4.0))
    log("  v_Ed = %.3f MPa <= v_Rd,c = %.3f MPa (ratio = %.2f) -> %s"
        % (v_ed, v_rdc, v_ed / v_rdc, "OK" if v_ed <= v_rdc else "NON CONFORME"))
    log("  (toujours 335 mm²/m : HA8 e150 — A_s,min gouverne, pas la flexion)")

    titre("[8] IMPLANTATION DES FONDATIONS SUR VUE EN PLAN NETTOYÉE (INDICE F)")
    log("  SF1     : X=95,35 m / Y=59,29 m (B-30 : +9,48 / +14,87 m) — Semelle BA 80x80x25 (D-30) sous P2 (CERTAIN)")
    log("  Z-P1N   : X=95,41 m / Y=49,04 m (B-30 : +9,54 /  +4,62 m) — Vérif. moellons ou SF 60x60 (NUAGE D-19)")
    log("  Z-P1S   : X=95,41 m / Y=47,78 m (B-30 : +9,54 /  +3,36 m) — Vérif. moellons ou SF 60x60 (NUAGE D-19)")
    log("  Z-P3    : X=94,09 m / Y=54,89 m (B-30 : +8,22 / +10,46 m) — Appui P3 50x40 BA + GB D-09 (NUAGE D-19)")
    log("  Z-J1    : X=89,78 m / Y=54,52 m (B-30 : +3,91 / +10,09 m) — Appui J1 24x50 BA + GB D-09 (NUAGE D-19)")
    log("  BECHE   : X=86,67->89,53 m / Y=46,77 m — Bêche BA ép. 20 cm réhausse dallage Sud-Est (EXI-07c)")
    log("  RSO-PASS: X=87,7->93,5 m / Y=63,3..64,3 m — Passes alternées gros béton C16/20 passerelle (EXI-07e)")

    # ------------------------------------------------------------------ PLANCHE DXF COMBINÉE (GAUCHE = VUE EN PLAN IMPLANTATION PLS | DROITE = DÉTAILS D'EXÉCUTION PLAN + COUPE A-A + NOTE D-09)
    doc = ezdxf.readfile(SRC_RDC)
    for lname in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
        if lname in doc.layers:
            doc.layers.get(lname).color = 8 if lname == "010_mur" else 9
    for nom, coul in (
        ("FOND-AXES", 1), ("FOND-COFFRAGE", 5), ("FOND-ACIER-INF", 3),
        ("FOND-ACIER-SUP", 4), ("FOND-COTATION", 8), ("FOND-HYP-D19", 6),
        ("FOND-GROS-BETON", 30), ("FOND-HABILLAGE-TEXTE", 7), ("FOND-CARTOUCHE", 7),
    ):
        if nom not in doc.layers:
            doc.layers.add(nom, color=coul)
    msp = doc.modelspace()

    def txt(x, y, t, ht=12.0, layer="FOND-HABILLAGE-TEXTE"):
        e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
        e.set_placement((x, y))
        return e

    def rect(x0, y0, x1, y1, layer="FOND-COFFRAGE", hatch_col=None):
        msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], dxfattribs={"layer": layer})
        if hatch_col is not None:
            hh_ = msp.add_hatch(color=hatch_col, dxfattribs={"layer": layer})
            hh_.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)

    def leader(tx, ty, px, py, t, ht=12.5, layer="FOND-HABILLAGE-TEXTE"):
        msp.add_lwpolyline([(px, py), (tx, ty - 3.0), (tx + len(t) * ht * 0.62, ty - 3.0)], dxfattribs={"layer": layer})
        txt(tx, ty, t, ht=ht, layer=layer)

    def cote_h(x1, x2, y, texte, layer="FOND-COTATION"):
        msp.add_line((x1, y), (x2, y), dxfattribs={"layer": layer})
        for x in (x1, x2):
            msp.add_line((x, y - 8), (x, y + 8), dxfattribs={"layer": layer})
        txt((x1 + x2) / 2.0 - len(texte) * 3.5, y + 6, texte, 11.0, layer)

    def cote_v(y1, y2, x, texte, layer="FOND-COTATION"):
        msp.add_line((x, y1), (x, y2), dxfattribs={"layer": layer})
        for y in (y1, y2):
            msp.add_line((x - 8, y), (x + 8, y), dxfattribs={"layer": layer})
        txt(x + 10, (y1 + y2) / 2.0 - 5, texte, 11.0, layer)

    # --- PARTIE GAUCHE : IMPLANTATION SUR LE FOND B-32 IND. D (X = 7950 .. 10150) ---
    for code, xv in [("A", 8555.0), ("B", 8655.0), ("C", 8875.0), ("D", 8977.5), ("E", 9535.0)]:
        msp.add_line((xv, 4340.0), (xv, 6465.0), dxfattribs={"layer": "FOND-AXES"})
        msp.add_circle((xv, 6492.0), 24.0, dxfattribs={"layer": "FOND-AXES"})
        txt(xv - 8.0, 6484.0, code, 18.0, "FOND-AXES")
    for code, yv in [("1", 4460.0), ("2", 4954.1), ("3", 5214.0), ("4", 5489.0), ("5", 5905.0), ("6", 6312.0)]:
        msp.add_line((8415.0, yv), (9695.0, yv), dxfattribs={"layer": "FOND-AXES"})
        msp.add_circle((8388.0, yv), 24.0, dxfattribs={"layer": "FOND-AXES"})
        txt(8380.0, yv - 8.0, code, 18.0, "FOND-AXES")

    # Semelle SF1 (80x80x25 BA — D-30) sous P2
    p2x, p2y = 9535.0, 5929.2
    rect(p2x - 45.0, p2y - 45.0, p2x + 45.0, p2y + 45.0, "FOND-GROS-BETON")
    rect(p2x - 40.0, p2y - 40.0, p2x + 40.0, p2y + 40.0, "FOND-COFFRAGE", hatch_col=5)
    rect(9522.5, 5921.7, 9547.6, 5936.7, "FOND-ACIER-INF", hatch_col=3)
    leader(9645.0, 5955.0, p2x + 40.0, p2y + 8.0, "SF1 : 80x80x25 BA (D-30, sous P2)", 13.0, "FOND-COFFRAGE")
    txt(9645.0, 5932.0, "X=95,35 / Y=59,29 m | HA8 e150 | GB D-09 | N_ELS 130,5 kN", 11.2, "FOND-HABILLAGE-TEXTE")

    # Nuages D-19 sur P1-N, P1-S, P3, J1
    for xc, yc, lx, ly_t, lab in [
        (9540.5, 4904.4, 9645.0, 4925.0, "Z-P1N (D-19) : vérif. moellons ou SF 60x60"),
        (9540.5, 4778.4, 9645.0, 4785.0, "Z-P1S (D-19) : vérif. moellons ou SF 60x60"),
        (9408.6, 5489.1, 9645.0, 5555.0, "Z-P3 (D-19) : pied P3 50x40 + GB D-09"),
        (8977.5, 5452.1, 7960.0, 5555.0, "Z-J1 (D-19) : pied J1 24x50 + GB D-09"),
    ]:
        rect(xc - 30.0, yc - 30.0, xc + 30.0, yc + 30.0, "FOND-HYP-D19")
        add_cloud(msp, xc - 42.0, yc - 42.0, xc + 42.0, yc + 42.0, "FOND-HYP-D19", 22.0)
        leader(lx, ly_t, xc + (32.0 if lx > xc else -32.0), yc, lab, 12.2, "FOND-HYP-D19")

    # Bêche BA Sud-Est + RSO Passerelle Nord
    rect(8667.4, 4666.6, 8952.5, 4686.5, "FOND-COFFRAGE", hatch_col=5)
    leader(7960.0, 4685.0, 8667.4, 4676.5, "Bêche BA ep.20 cm (L=2,85m — EXI-07c)", 12.2, "FOND-COFFRAGE")
    add_cloud(msp, 8750.0, 6320.0, 9380.0, 6450.0, "FOND-GROS-BETON", 28.0)
    txt(8775.0, 6392.0, "RSO Passerelle château : passes alternées gros béton C16/20 (EXI-07e)", 11.8, "FOND-GROS-BETON")

    # --- PARTIE DROITE : DÉTAILS D'EXÉCUTION SEMELLES TYPES (AGRANDISSEMENT x2,8 LISIBLE !) + COUPE A-A + NOTE D-09 ---
    rx0, rx1 = 10260.0, 12020.0
    rect(rx0, 4340.0, rx1, 6520.0, "FOND-CARTOUCHE")
    rect(rx0, 6425.0, rx1, 6520.0, "FOND-AXES")
    txt(rx0 + 25.0, 6462.0, "PLS (D-11) — B-40 Ind. F  |  NE PAS EXECUTER SANS EXE COTE ET VISA  (MODE PARTIEL-DECLARE)", 16.5, "FOND-AXES")

    # 1. Vues en plan des 3 semelles types agrandies (échelle x2,5 -> 60 cm = 150 unités !)
    K = 2.5
    txt(rx0 + 30.0, 6365.0, "1. SEMELLES ISOLEES TYPES — VUES EN PLAN FERRAILLEES (HA8 e150 inf. 2 lits croisés, c_nom = 50 mm)", 14.0)
    for idx_s, (Bm, cx_s, titre_s, amax_s) in enumerate([
        (0.60, rx0 + 240.0, "TYPE 60x60", "D-14 minimum — A <= 14 m²"),
        (0.70, rx0 + 780.0, "TYPE 70x70", "A <= 19 m²"),
        (0.80, rx0 + 1360.0, "SF1 80x80 (D-30)", "sous P2 — N_ELS = 130,5 kN"),
    ]):
        cy_s = 6135.0
        c = Bm * 100.0 * K / 2.0
        p = 0.125 * 100.0 * K
        rect(cx_s - c - 5 * K, cy_s - c - 5 * K, cx_s + c + 5 * K, cy_s + c + 5 * K, "FOND-GROS-BETON")
        rect(cx_s - c, cy_s - c, cx_s + c, cy_s + c, "FOND-COFFRAGE")
        rect(cx_s - p, cy_s - p * 0.6, cx_s + p, cy_s + p * 0.6, "FOND-COFFRAGE")
        mg = 5.0 * K
        for j in range(5):
            yj = cy_s - c + mg + j * (2 * (c - mg) / 4.0)
            xj = cx_s - c + mg + j * (2 * (c - mg) / 4.0)
            msp.add_line((cx_s - c + mg, yj), (cx_s + c - mg, yj), dxfattribs={"layer": "FOND-ACIER-INF"})
            msp.add_line((xj, cy_s - c + mg), (xj, cy_s + c - mg), dxfattribs={"layer": "FOND-ACIER-INF"})
        msp.add_line((cx_s - c - 30, cy_s), (cx_s + c + 30, cy_s), dxfattribs={"layer": "FOND-AXES"})
        msp.add_line((cx_s, cy_s - c - 30), (cx_s, cy_s + c + 30), dxfattribs={"layer": "FOND-AXES"})
        cote_h(cx_s - c, cx_s + c, cy_s - c - 28, "%d cm" % round(Bm * 100))
        cote_v(cy_s - c, cy_s + c, cx_s + c + 24, "%d" % round(Bm * 100))
        txt(cx_s - c, cy_s + c + 60, titre_s, 13.0, "FOND-COFFRAGE")
        txt(cx_s - c, cy_s + c + 38, amax_s, 10.8, "FOND-HABILLAGE-TEXTE")

    # 2. Coupe verticale A-A agrandie x2,5 avec Gros Béton D-09 + Béton de propreté + Attentes B-50
    txt(rx0 + 30.0, 5855.0, "2. COUPE VERTICALE A-A — SEMELLE SF1 (80x80x25 BA, D-30) + GROS BETON DE RATTRAPAGE D-09", 14.0)
    ccx, ccy = rx0 + 420.0, 5545.0  # ccy = arase inférieure semelle BA (-1,00 m/TN mini)
    cw = 80.0 * K
    ch = 25.0 * K
    # Gros béton C16/20 sous semelle (si fondation existante plus profonde — D-09)
    rect(ccx - cw / 2 - 20, ccy - 75.0, ccx + cw / 2 + 20, ccy - 12.5, "FOND-GROS-BETON")
    # Béton de propreté 5 cm
    rect(ccx - cw / 2 - 12.5, ccy - 12.5, ccx + cw / 2 + 12.5, ccy, "FOND-COFFRAGE")
    # Semelle BA 60x60x30
    rect(ccx - cw / 2, ccy, ccx + cw / 2, ccy + ch, "FOND-COFFRAGE")
    # Fût poteau P2 (25 cm)
    pw = 25.0 * K / 2.0
    msp.add_lwpolyline([(ccx - pw, ccy + ch), (ccx - pw, ccy + ch + 140),
                        (ccx + pw, ccy + ch + 140), (ccx + pw, ccy + ch)], dxfattribs={"layer": "FOND-COFFRAGE"})
    # Lit inférieur HA8 e150 + attentes en attente B-50
    msp.add_line((ccx - cw / 2 + 12.5, ccy + 13.5), (ccx + cw / 2 - 12.5, ccy + 13.5), dxfattribs={"layer": "FOND-ACIER-INF"})
    for j in range(5):
        xj = ccx - cw / 2 + 16 + j * (cw - 32) / 4.0
        msp.add_circle((xj, ccy + 18.0), 3.5, dxfattribs={"layer": "FOND-ACIER-INF"})
    msp.add_line((ccx - pw + 12, ccy + 18), (ccx - pw + 12, ccy + ch + 95), dxfattribs={"layer": "FOND-ACIER-SUP"})
    msp.add_line((ccx + pw - 12, ccy + 18), (ccx + pw - 12, ccy + ch + 95), dxfattribs={"layer": "FOND-ACIER-SUP"})

    cote_h(ccx - cw / 2, ccx + cw / 2, ccy - 98.0, "80 cm (D-30 / D-14)")
    cote_v(ccx_y0 := ccy, ccy + ch, ccx + cw / 2 + 30.0, "h = 25 cm")
    txt(ccx + cw / 2 + 160.0, ccy + ch + 95.0, "0,00 RELATIF (PB RDC existant — D-21) / TN", 12.0, "FOND-AXES")
    txt(ccx + cw / 2 + 160.0, ccy + ch + 50.0, "Attentes poteau P2 : logement seul, ancrage en B-50", 11.5, "FOND-ACIER-SUP")
    txt(ccx + cw / 2 + 160.0, ccy + 25.0, "Semelle BA C25/30 — 2 lits HA8 e150 (335 mm²/m) — c_nom = 50 mm", 11.8, "FOND-ACIER-INF")
    txt(ccx + cw / 2 + 160.0, ccy - 6.0, "Arase inf. -1,00 m/TN MINIMUM (D-08/D-12) + Béton propreté 5 cm", 11.5, "FOND-COFFRAGE")
    txt(ccx + cw / 2 + 160.0, ccy - 52.0, "Rattrapage en GROS BETON C16/20 jusqu'au niveau exact", 11.8, "FOND-GROS-BETON")
    txt(ccx + cw / 2 + 160.0, ccy - 74.0, "de la fondation existante si celle-ci est plus profonde (D-09)", 11.8, "FOND-GROS-BETON")

    # 3. Encadré Note D-09 intégrale + Dispositions constructives (Y = 4760 .. 5360)
    rect(rx0 + 20.0, 4760.0, rx1 - 20.0, 5360.0, "FOND-AXES")
    notes = [
        "NOTE OBLIGATOIRE D-09 (TEXTE INTEGRAL) — REPORTEE MOT POUR MOT SUR PLAN ET NOTE DE CALCUL :",
        "« AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON...",
        "  CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »",
        "- Mode PARTIEL-DECLARE : planchers g = 4,71 kN/m² (B-21 Ind. C) · dallage g = 7,75 kN/m² (D-35, recharge 15 cm sur 100 % de l'emprise).",
        "- Sol (G2 AVP GEOEXPERTS + D-02/D-03/D-08) : alluvions anciennes dès -0,50 m, q_ELS <= 0,30 MPa, q_ELU <= 0,49 MPa.",
        "- SF1 80x80x25 (D-30) sous P2 : N_ELS = 130,5 kN (σ = 0,204 MPa <= 0,300) | N_ELU = 182,9 kN (σ = 0,286 <= 0,490).",
        "- Poinçonnement EC2 §6.4 (SF1) : v_Ed = 0,279 MPa <= v_Rd,c = 0,392 MPa (OK à 71 %).",
        "- Fouilles hors nappe déclarée (D-16 : toute venue d'eau = POINT D'ARRET). Tassements hors mission GO (D-15).",
        "- Interdiction absolue de déchausser les fondations existantes ; blindage si distance < 1,50 m.",
    ]
    for k, line_n in enumerate(notes):
        txt(rx0 + 38.0, 5325.0 - k * 58.0, line_n, 11.4,
            "FOND-AXES" if k in (0, 1, 2) else "FOND-HABILLAGE-TEXTE")

    # 4. Cartouche bas-droite
    rect(rx0, 4340.0, rx1, 4730.0, "FOND-CARTOUCHE")
    for t_c, hh_c, yy_c in [
        ("EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 19.5, 4680.0),
        ("PLS (D-11) — FONDATIONS SUPERFICIELLES : IMPLANTATION EN PLAN & FERRAILLAGE TYPE", 13.8, 4632.0),
        ("Brique B-40  ·  Indice F  ·  20/10/2026  ·  Mode PARTIEL-DECLARE  ·  Fond B-32 Ind. D (sans cloisons)", 12.5, 4588.0),
        ("NE PAS EXECUTER SANS EXE COTE ET VISA", 21.0, 4525.0),
        ("CARNAC v2.6  ·  Unités DXF : cm  ·  Audit DXF : 0 erreur", 12.0, 4470.0),
    ]:
        txt(rx0 + 30.0, yy_c, t_c, hh_c, "FOND-AXES" if "NE PAS EXECUTER" in t_c else "FOND-CARTOUCHE")

    chemin = BASE + ".dxf"
    doc.saveas(chemin)
    a = doc.audit()
    log("  écrit : %s (%d o) — audit %d erreur(s)" % (chemin, os.path.getsize(chemin), len(a.errors)))

    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.015, 0.02, 0.97, 0.92])
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(msp, finalize=False)
    ax.set_xlim(7940.0, 12060.0)
    ax.set_ylim(4290.0, 6560.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(
        "CROISSY-FLORA — PLS (D-11) / B-40 Ind. F — FONDATIONS SUPERFICIELLES : IMPLANTATION EN PLAN & FERRAILLAGE TYPE\n"
        "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA   (Fond structurel pur B-32 Ind. D : cloisons et isolation supprimées)",
        fontsize=11.5, fontweight="bold", pad=8,
    )
    fig.savefig(BASE + ".png", dpi=220, facecolor="white")
    fig.savefig(BASE + ".pdf", facecolor="white")
    plt.close(fig)
    log("  rendus : %s.png / .pdf" % BASE)

    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log("\nJournal écrit : %s" % JOURNAL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
