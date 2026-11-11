"""
PL-03 — Coupes et élévations de l'extension.

Deux cadres sur la planche A3 paysage :
  1. coupe verticale sur la terrasse (échelle 1/50) — altimétrie NGF des
     niveaux, plancher haut RDC 44,08, arase d'acrotère 44,75, fondations
     39,02, niveau du terrain 41,11 ;
  2. détail de l'appui de la poutre-acrotère sur le poteau BA 25 × 25 et sur
     le voile mitoyen (échelle 1/20).
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "00_SOURCES"))

import plan_engine as E          # noqa: E402
import niveaux_retenus as N      # noqa: E402

OUT = os.path.join(HERE, "plans")

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-03 — COUPES ET ÉLÉVATIONS DE L'EXTENSION",
    "sous_titre": "Coupe verticale sur la terrasse (1/50) et détail d'appui "
                  "de la poutre-acrotère (1/20)",
    "repere": "PL-03",
    "phase": "Tâche 3 — plans généraux",
    "indice": "Indice A — 11/11/2026",
    "date": "Échelle 1/50 et 1/20",
}

# ---------------------------------------------------------------------------
# Cadre 1 — coupe verticale (unités : cm, x = 0 au nu de façade)
# ---------------------------------------------------------------------------

X_FACADE = 0.0        # nu extérieur de la façade existante
EP_FAC = 49.0
P = 320.0             # profondeur de l'extension
Y_POT = 200.0         # axe du poteau, depuis le nu de façade
B_POUTRE = 30.0
H_POUTRE = 67.0

Z = 100.0             # facteur : 1 m NGF = 100 cm dans la scène


def z(ngf):
    """Altitude NGF (m) -> ordonnée scène (cm), sol RDC à 0."""
    return (ngf - N.NGF_SOL_RDC) * Z


def build_coupe() -> E.Scene:
    """Coupe A-A perpendiculaire à la façade, à mi-portée de la poutre.

    x = 0  : nu extérieur de la façade existante
    x = 200: axe du poteau BA et de la poutre-acrotère (2,00 m)
    x = 320: verrière frontale
    z      : altitude NGF ramenée au sol fini RDC (41,46 -> 0)
    """
    sc = E.Scene()

    y_ph = z(N.NGF_PH_RDC)
    y_pb = z(N.NGF_POUTRE_BAS)
    y_pt = z(N.NGF_POUTRE_HAUT)
    y_fond = z(N.NGF_FONDATION)
    y_ver = z(N.NGF_VERRIERE_HEAD)
    y_terr = z(N.NGF_TERRAIN)

    # ---- 1. Façade existante conservée (cave -> plancher haut RDC) ------
    sc.rect(-EP_FAC, y_fond, EP_FAC, y_ph - y_fond, "STR_EXISTANT", lw=0.35)
    for i in range(16):
        yy = y_fond + i * 32
        sc.line(-EP_FAC, yy, -EP_FAC + 26, yy + 32, "STR_EXISTANT", lw=0.13)
    # plancher haut du RDC existant (44,08)
    sc.rect(-EP_FAC, y_ph - 22, EP_FAC, 22, "STR_EXISTANT", lw=0.25)

    # ---- 2. Dalle de terrasse (20 cm) -----------------------------------
    sc.rect(0, y_ph, P, 20, "STR_COFFRAGE_BA", lw=0.50, fill=True)

    # ---- 3. Poutre-acrotère 30 x 67 --------------------------------------
    sc.rect(Y_POT - B_POUTRE / 2, y_pb, B_POUTRE, y_pt - y_pb,
            "STR_COFFRAGE_BA", lw=0.50, fill=True)
    # arase d'acrotère prolongée (garde-corps de la terrasse)
    sc.line(Y_POT - B_POUTRE / 2, y_pt, 0, y_pt, "STR_COTATIONS_TEXTES",
            lw=0.13)

    # ---- 4. Poteau BA 25 x 25 --------------------------------------------
    sc.rect(Y_POT - 12.5, 0, 25, y_pb, "STR_COFFRAGE_BA", lw=0.50, fill=True)

    # ---- 5. Puits n° 1 (sous le poteau) ----------------------------------
    sc.rect(Y_POT - 102.5, y_fond, 205, -y_fond, "STR_COFFRAGE_BA", lw=0.50)
    for i in range(-3, 4):
        sc.line(Y_POT + i * 34, y_fond + 8, Y_POT + i * 34 + 46, -8,
                "STR_COFFRAGE_BA", lw=0.13)
    sc.text("Puits n° 1 — Ø 2,05 m — gros béton C16/20", Y_POT, y_fond - 24,
            2.1, align="center")

    # ---- 6. Verrière frontale (hors mission) -----------------------------
    sc.line(P, 0, P, y_ver, "STR_COTATIONS_TEXTES", lw=0.30)
    sc.line(P - 60, y_ver, P + 60, y_ver, "STR_COTATIONS_TEXTES", lw=0.18)
    sc.leader("Verrière frontale (hors mission)\nreprise sur la dalle",
              P - 30, y_ver + 52, P, y_ver - 6, fontsize=2.1)

    # ---- 7. Sols et terrain ----------------------------------------------
    sc.line(-EP_FAC - 30, y_terr, P + 40, y_terr, "STR_EXISTANT", lw=0.25)
    sc.line(-EP_FAC, 0, P, 0, "STR_EXISTANT", lw=0.35)
    sc.text("Terrain NGF 41,11", P + 46, y_terr + 4, 2.0, align="left")

    # ---- 8. Annotations ---------------------------------------------------
    sc.leader("Poutre-acrotère BA 30 × 67\narase NGF 44,75",
              Y_POT + 62, y_pt + 44, Y_POT + B_POUTRE / 2, y_pt - 10,
              fontsize=2.15)
    sc.leader("Poteau BA 25 × 25\naxe à 2,00 m du nu de façade",
              Y_POT + 86, 110, Y_POT + 12.5, 150, fontsize=2.15)
    sc.leader("Dalle BA 20 cm — travée 2,00 m\npuis porte-à-faux 1,20 m",
              -46, y_ph + 132, -6, y_ph + 14, fontsize=2.15)

    # ---- 9. Cotation des niveaux NGF -------------------------------------
    xc = -86.0
    for ngf, lab in ((N.NGF_FONDATION, "39,02"),
                     (N.NGF_SOL_RDC, "41,46"),
                     (N.NGF_PH_RDC, "44,08"),
                     (N.NGF_ACROTERE, "44,75"),
                     (N.NGF_VERRIERE_HEAD, "45,90")):
        yy = z(ngf)
        sc.line(xc - 14, yy, -EP_FAC - 30, yy, "STR_COTATIONS_TEXTES",
                lw=0.13)
        sc.text(lab, xc - 18, yy - 3, 2.0, align="right")

    # ---- 10. Cotation horizontale ----------------------------------------
    sc.dim_h(0, Y_POT, y_pt + 62, "2,00 m")
    sc.dim_h(Y_POT, P, y_pt + 62, "1,20 m")
    sc.text("Niveaux en m NGF", xc - 18, z(N.NGF_VERRIERE_HEAD) + 22, 2.0,
            align="right")

    return sc


# ---------------------------------------------------------------------------
# Cadre 2 — détail d'appui (1/20)
# ---------------------------------------------------------------------------

def build_detail() -> E.Scene:
    """Appui de la poutre sur le poteau BA ; unités cm."""
    sc = E.Scene()

    # poteau 25 x 25
    sc.rect(0, 0, 25, 25, "STR_COFFRAGE_BA", lw=0.50, fill=True)
    # poutre 30 x 67 posée sur le poteau (léger débord de 2,5 cm de chaque côté)
    sc.rect(-2.5, 25, 30, 67, "STR_COFFRAGE_BA", lw=0.50, fill=True)
    # dalle de part et d'autre
    sc.line(-60, 92, -2.5, 92, "STR_COFFRAGE_BA", lw=0.50)
    sc.line(27.5, 92, 85, 92, "STR_COFFRAGE_BA", lw=0.50)
    sc.line(-60, 72, -2.5, 72, "STR_COFFRAGE_BA", lw=0.35)
    sc.line(27.5, 72, 85, 72, "STR_COFFRAGE_BA", lw=0.35)

    # platine d'appui + appareil d'appui
    sc.rect(-2.5, 23.0, 30, 2.0, "STR_ACIER_PROFILS", lw=0.50)
    sc.rect(-1.0, 21.0, 27, 2.0, "STR_COTATIONS_TEXTES", lw=0.25)

    # armatures du poteau : 6 HA 8
    for (bx, by) in ((-2.5, 1.6), (12.5, 1.0), (27.5, 1.6),
                     (-2.5, 23.4), (12.5, 21.4), (27.5, 23.4)):
        sc.circle(bx, by, 0.8, "STR_FERRAILLAGE", lw=0.35)

    # cadre HA 8 e = 200
    sc.line(-2.0, 1.5, 27.0, 1.5, "STR_FERRAILLAGE", lw=0.35)
    sc.line(27.0, 1.5, 27.0, 23.5, "STR_FERRAILLAGE", lw=0.35)
    sc.line(27.0, 23.5, -2.0, 23.5, "STR_FERRAILLAGE", lw=0.35)
    sc.line(-2.0, 23.5, -2.0, 1.5, "STR_FERRAILLAGE", lw=0.35)

    # 4 HA 20 en nappe basse de la poutre
    for i in range(4):
        sc.circle(2.0 + i * 8.4, 30.5, 1.0, "STR_FERRAILLAGE", lw=0.40)
    # étriers HA 8 e = 175
    sc.line(0.5, 28.0, 27.0, 28.0, "STR_FERRAILLAGE", lw=0.35)
    sc.line(27.0, 28.0, 27.0, 89.5, "STR_FERRAILLAGE", lw=0.35)
    sc.line(27.0, 89.5, 0.5, 89.5, "STR_FERRAILLAGE", lw=0.35)
    sc.line(0.5, 89.5, 0.5, 28.0, "STR_FERRAILLAGE", lw=0.35)

    # ---- annotations ------------------------------------------------------
    sc.leader("Poutre-acrotère BA 30 × 67\n4 HA 20 + étriers HA 8 e = 175",
              95, 78, 27.5, 70, fontsize=2.1)
    sc.leader("Platine d'appui 300 × 200 × 15\nmatée au mortier sans retrait",
              95, 40, 27.5, 24, fontsize=2.1)
    sc.leader("Poteau BA 25 × 25 — 6 HA 8\ncadres HA 8 e = 200",
              95, 8, 25, 8, fontsize=2.1)
    sc.leader("Dalle BA 20 cm", -68, 96, -30, 92, fontsize=2.0)
    sc.leader("Contre-flèche de coffrage 20 mm\n(à rattraper sur l'étaiement)",
              -68, 55, -2.5, 60, fontsize=2.0)

    # cotes
    sc.dim_h(0, 25, -14, "25")
    sc.dim_h(-2.5, 27.5, 108, "30")
    sc.dim_v(0, 25, -20, "25")
    sc.dim_v(25, 92, -20, "67")
    return sc


def main():
    os.makedirs(OUT, exist_ok=True)

    # ---------- DXF : les deux cadres côte à côte -------------------------
    sc1, sc2 = build_coupe(), build_detail()
    dxf = E.DxfBackend("PL-03")
    dxf.render(sc1)
    # translation du détail pour le poser à droite de la coupe
    sc2t = E.Scene()
    for it in sc2.items:
        if it[0] in ("line",):
            _, p1, p2, layer, lw = it
            sc2t.line(p1[0] + 620, p1[1], p2[0] + 620, p2[1], layer, lw)
        elif it[0] in ("rect",):
            _, (x, y), (w, h), layer, lw, fill, hatch, ang, sp = it
            sc2t.rect(x + 620, y, w, h, layer, lw, fill, hatch, ang, sp)
        elif it[0] == "circle":
            _, (cx, cy), r, layer, lw, fill, hatch = it
            sc2t.circle(cx + 620, cy, r, layer, lw, fill, hatch)
        elif it[0] == "text":
            _, s, (x, y), fs, layer, al, ang, b = it
            sc2t.text(s, x + 620, y, fs, layer, al, ang, b)
        elif it[0] == "dim_h":
            _, x1, x2, y, lab, fs, layer, tick = it
            sc2t.dim_h(x1 + 620, x2 + 620, y, lab, fs, layer, tick)
        elif it[0] == "dim_v":
            _, y1, y2, x, lab, fs, layer, tick = it
            sc2t.dim_v(y1, y2, x + 620, lab, fs, layer, tick)
    dxf.render(sc2t)
    p_dxf = dxf.save(os.path.join(OUT, "PL-03_Coupes_Elevations.dxf"))

    # ---------- PDF : deux cadres, deux échelles --------------------------
    pb = E.PdfBackend("PL-03", CARTOUCHE)
    pb.new_page()
    pb.titre("PL-03 — COUPES ET ÉLÉVATIONS DE L'EXTENSION",
             "Coupe verticale sur la terrasse (1/50) et détail d'appui de la "
             "poutre-acrotère (1/20)")

    # cadre 1 : coupe 1/50 — à gauche
    pb.place(sc1, 34.0, 92.0, scale=50.0)
    pb.render(sc1)
    c = pb._c
    c.setFont("Helvetica-Bold", 2.9)
    c.setFillColor(pb.Color(0, 0, 0))
    c.drawString(34, 258, "COUPE VERTICALE A-A SUR LA TERRASSE — 1/50")

    # cadre 2 : détail 1/20 — à droite
    pb.place(sc2, 232.0, 140.0, scale=20.0)
    pb.render(sc2)
    c.setFont("Helvetica-Bold", 2.9)
    c.drawString(232, 258, "DÉTAIL D'APPUI POUTRE / POTEAU — 1/20")

    # légende et notes
    pb.legende(232, 126, [
        ("STR_COFFRAGE_BA", "Béton armé coulé en place", "hatch"),
        ("STR_ACIER_PROFILS", "Platine / appareil d'appui S275", "line"),
        ("STR_FERRAILLAGE", "Armatures B500B", "line"),
        ("STR_EXISTANT", "Maçonnerie existante conservée", "line"),
    ])
    pb.note_block(24, 76, "NOTES", [
        "1. Niveaux en m NGF ; sol fini RDC = 41,46 (DOC-01 §5).",
        "2. La poutre-acrotère fait office d'acrotère : arase 44,75,",
        "   sous-face 44,08 (sous-face du plancher haut RDC).",
        "3. Poteau BA 25 × 25 à 2,00 m du nu de façade (arbitrage E-01).",
        "4. Contre-flèche de coffrage 20 mm sur la poutre-acrotère.",
        "5. Appui glissant sur le voile mitoyen (armatures en attente).",
        "6. Fondations descendues à NGF 39,02 (assise de l'existant).",
    ], width=180)

    p_pdf = os.path.join(OUT, "PL-03_Coupes_Elevations.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


if __name__ == "__main__":
    main()
