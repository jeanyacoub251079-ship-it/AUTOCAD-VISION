"""
PL-05 — DÉTAILS D'ASSEMBLAGE ACIER / BÉTON ARMÉ.

Deux planches A3 paysage :

  PL-05/1 — reprises en sous-œuvre (échelles 1/12 et 1/14)
    A. appui d'un profilé S355 sur un jambage BA (D2 / D4 / D6) ;
    B. appui d'un profilé S355 sur un sommier BA en pied de mur conservé ;
    C. about de profilé encastré dans la maçonnerie meulière (D1) ;
    D. jonction de deux profilés sur poteau BA (D3 / D5).

  PL-05/2 — extension (E-02 rectifié)
    E. appui de la poutre-acrotère sur le voile BA de rive neuf ;
    F. appui de la poutre de rive sur l'about en console de la poutre
       perpendiculaire (poteau à 1,30 m, console 0,70 m) ;
    G. appui glissant de la dalle sur la façade existante ;
    H. jonction du voile de rive neuf au pignon existant.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "00_SOURCES"))

import plan_engine as E       # noqa: E402
import detail_lib as D        # noqa: E402

OUT = os.path.join(HERE, "plans")

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-05/1 — ASSEMBLAGES RSO ACIER / BA",
    "sous_titre": "Appuis de profilés S355 sur jambages et sommiers BA",
    "repere": "PL-05/1",
    "phase": "Tâche 4 — détails d'exécution",
    "indice": "Indice B — révision E-02 — 12/11/2026",
    "echelle": "Échelles : 1/12 et 1/14",
    "date": "S355 — C25/30",
}

CARTOUCHE2 = dict(CARTOUCHE)
CARTOUCHE2.update({
    "titre": "PL-05/2 — ASSEMBLAGES BA — EXTENSION E-02",
    "sous_titre": "Extension E-02 rectifiée — voile neuf, console et appui glissant",
    "repere": "PL-05/2",
    "echelle": "Échelles : 1/20, 1/30 et 1/40",
    "date": "C25/30 — B500B",
})


# ---------------------------------------------------------------------------
# A — appui d'un profilé S355 sur un jambage BA (1/10)
# ---------------------------------------------------------------------------

def detail_A() -> E.Scene:
    """Profilé posé sur un jambage BA 25 x 50, platine + tiges d'ancrage."""
    sc = E.Scene()

    # jambage BA 25 (largeur) x 50 (hauteur visible)
    D.beton_rect(sc, 0, -50.0, 50.0, 50.0, sp=1.4)
    # sommier / semelle de répartition
    sc.rect(0, 0, 50.0, 3.0, "STR_COTATIONS_TEXTES", 0.25)

    # platine 300 x 250 x 20
    sc.rect(-3.0, 3.0, 56.0, 2.0, "STR_ACIER_PROFILS", 0.45,
            hatch="ANSI31", angle=45.0, spacing=0.9)
    # mortier de calage
    sc.rect(-3.0, 2.0, 56.0, 1.0, "STR_COTATIONS_TEXTES", 0.20)

    # profilé IPE 270 en silhouette (âme vue de face) posé sur la platine
    prof = E.section_pts("IPE 270", 10.0, 5.0)
    sc.poly(prof, "STR_ACIER_PROFILS", 0.45, closed=True)
    sc.hatch_poly(prof, "STR_ACIER_PROFILS", 45.0, 0.8)

    # tiges d'ancrage M16 + écrous
    for x in (5.0, 45.0):
        sc.line(x, 5.0, x, -14.0, "STR_ACIER_PROFILS", 0.35)
        sc.line(x - 1.2, -12.0, x + 1.2, -12.0, "STR_ACIER_PROFILS", 0.30)
        sc.line(x - 1.2, -14.0, x + 1.2, -14.0, "STR_ACIER_PROFILS", 0.30)
        sc.line(x, -14.0, x + 4.0, -20.0, "STR_ACIER_PROFILS", 0.30)

    # cotes
    D.cote_h(sc, 0, 50.0, -34.0, "25")
    D.cote_h(sc, -3.0, 53.0, 14.0, "30")
    D.cote_v(sc, 0, 3.0, -10.0, "3")
    D.cote_v(sc, 3.0, 5.0, -18.0, "2")

    # annotations
    sc.leader("Profilé S355 (IPE 270)\nsoudé sur platine", 56, 30, 22.0,
              22.0, fontsize=2.0)
    sc.leader("Platine 300 x 250 x 20\n4 tiges M16", 56, 8, 53.0, 4.0,
              fontsize=2.0)
    sc.leader("Mortier M50 — ép. 10 à 30", 56, -8, 53.0, 2.5,
              fontsize=1.9)
    sc.leader("Jambage BA\n25 x 50 C25/30", 56, -22, 46.0, -26.0,
              fontsize=2.0)
    sc.leader("Clavetage Ø 16", 56, -42, 44.0, -40.0, fontsize=2.0)
    return sc


# ---------------------------------------------------------------------------
# B — appui sur sommier BA en pied de mur conservé (1/10)
# ---------------------------------------------------------------------------

def detail_B() -> E.Scene:
    """Sommier BA coulé sous un mur conservé ; linteau métallique au-dessus."""
    sc = E.Scene()

    # mur conservé au-dessus
    sc.rect(0, 55.0, 47.0, 30.0, "STR_EXISTANT", 0.35,
            hatch="ANSI31", angle=45.0, spacing=1.8)
    # sommier BA 25 x 25
    D.beton_rect(sc, 0, 30.0, 47.0, 25.0, sp=1.4)
    # amorce de la maçonnerie sous le sommier (déposée)
    sc.rect(0, 0, 47.0, 30.0, "STR_DEMOLITION", 0.25,
            hatch="ANSI31", angle=-45.0, spacing=3.0)

    # armatures du sommier : 4 HA 12 + étriers
    for y in (33.0, 34.6):
        sc.line(-6.0, y, 53.0, y, "STR_FERRAILLAGE", 0.32)
    for y in (50.0, 51.6):
        sc.line(-6.0, y, 53.0, y, "STR_FERRAILLAGE", 0.32)
    for x in (-4.0, 12.0, 28.0, 44.0, 51.0):
        D.etrier(sc, x - 3.0, 32.0, 45.0, 21.0, lw=0.22, retour=3.0)

    # platine + profilé sous le sommier (reprise vers les appuis)
    sc.rect(0, 27.0, 47.0, 3.0, "STR_ACIER_PROFILS", 0.45,
            hatch="ANSI31", angle=45.0, spacing=0.9)

    D.cote_h(sc, 0, 47.0, 22.0, "ep. mur")
    D.cote_v(sc, 30.0, 55.0, -10.0, "25")
    sc.leader("Mur conservé", 56, 78, 40.0, 74.0, fontsize=2.0)
    sc.leader("Sommier BA 25 x 25\n4 HA 12 + HA 8 e = 150", 56, 46,
              46.0, 44.0, fontsize=2.0)
    sc.leader("Maçonnerie déposée\n(reprise sur étai)", 56, 12, 30.0,
              16.0, fontsize=2.0)
    sc.leader("Platine 470 x 250 x 20", 56, 28, 42.0, 28.5, fontsize=2.0)
    return sc


# ---------------------------------------------------------------------------
# C — about de profilé encastré dans la meulière (1/10)
# ---------------------------------------------------------------------------

def detail_C() -> E.Scene:
    """About de profilé dans une réservation de la meulière, calé au mortier."""
    sc = E.Scene()

    # mur meulière
    sc.rect(-34.0, 0, 34.0, 74.0, "STR_EXISTANT", 0.40,
            hatch="ANSI31", angle=45.0, spacing=2.4)
    # réservation
    sc.rect(0, 20.0, 26.0, 27.0, "STR_COTATIONS_TEXTES", 0.22)
    # profilé entrant dans la réservation (silhouette en bout)
    prof = E.section_pts("IPE 180", -46.0, 22.0)
    sc.poly(prof, "STR_ACIER_PROFILS", 0.45, closed=True)
    sc.hatch_poly(prof, "STR_ACIER_PROFILS", 45.0, 0.8)
    # plaque d'about + calage au mortier
    sc.rect(24.0, 21.0, 2.0, 25.0, "STR_ACIER_PROFILS", 0.40)
    sc.rect(0.0, 21.0, 24.0, 25.0, "STR_COTATIONS_TEXTES", 0.15)

    D.cote_h(sc, 0, 26.0, 14.0, "26")
    D.cote_v(sc, 20.0, 47.0, -52.0, "27")
    sc.leader("Meulière existante\nf_d 1,0 à 1,5 MPa", 34, 70, 30.0, 66.0,
              fontsize=1.9)
    sc.leader("Réservation 26 x 27", 34, 46, 20.0, 38.0, fontsize=1.9)
    sc.leader("IPE 180 — about enrobé\nmortier NHL 3,5", 34, 14, 12.0,
              22.0, fontsize=1.9)
    sc.leader("Plaque d'about\n200 x 250 x 10", 34, -6, 25.0, 30.0,
              fontsize=1.9)
    return sc


# ---------------------------------------------------------------------------
# D — jonction de deux profilés sur poteau BA (1/10)
# ---------------------------------------------------------------------------

def detail_D() -> E.Scene:
    """Deux profilés aboutissant sur un poteau BA, platines boulonnées."""
    sc = E.Scene()

    # poteau BA 25 x 40 (coupe)
    D.beton_rect(sc, 0, -46.0, 40.0, 46.0, sp=1.4)
    for x in (6.0, 34.0):
        sc.line(x, -42.0, x, -2.0, "STR_FERRAILLAGE", 0.30)
    for y in (-38.0, -24.0):
        D.etrier(sc, 6.0, y, 28.0, 12.0, lw=0.22, retour=3.0)

    # platine de tête
    sc.rect(-2.0, 0, 44.0, 2.5, "STR_ACIER_PROFILS", 0.45,
            hatch="ANSI31", angle=45.0, spacing=0.9)
    # deux profilés en vue longitudinale posés sur la platine
    for x0 in (-30.0, 40.0):
        prof = E.section_pts("IPE 180", x0, 2.5)
        sc.poly(prof, "STR_ACIER_PROFILS", 0.40, closed=True)
    # boulons M20
    for x in (6.0, 34.0):
        sc.circle(x, 1.2, 1.1, "STR_ACIER_PROFILS", 0.30)
    # goussets
    for (ax, bx) in ((6.0, 2.0), (34.0, 38.0)):
        sc.line(ax, 2.5, bx, 12.0, "STR_ACIER_PROFILS", 0.35)

    D.cote_h(sc, 0, 40.0, 46.0, "40")
    D.cote_v(sc, -46.0, 0.0, -16.0, "40")
    sc.leader("Poteau BA 25 x 40\n6 HA 12 + HA 8 e = 200", -34, -32, 2.0,
              -26.0, fontsize=1.9)
    sc.leader("Platine 400 x 250 x 20", 20, 56, 40.0, 2.0, fontsize=1.9)
    sc.leader("Boulons M20 8.8", -32, 26, 6.0, 1.2, fontsize=1.9)
    sc.leader("IPE 180 aboutés", -32, -12, -14.0, 8.0, fontsize=1.9)
    return sc


# ---------------------------------------------------------------------------
# E — appui simple de la poutre-acrotère sur le voile de rive neuf
# ---------------------------------------------------------------------------

def detail_E() -> E.Scene:
    """Appui simple de la poutre de rive sur le voile BA neuf et sa semelle."""
    sc = E.Scene()
    D.beton_rect(sc, -22.5, -75.0, 65.0, 30.0, sp=1.4)
    D.beton_rect(sc, 0.0, -45.0, 20.0, 45.0, sp=1.4)
    sc.rect(0.0, 0.0, 20.0, 2.0, "STR_ACIER_PROFILS", 0.35,
            hatch="ANSI31", angle=45.0, spacing=1.0)
    D.beton_rect(sc, -5.0, 2.0, 30.0, 67.0, sp=1.4)
    for x in (-1.0, 6.0, 14.0, 21.0):
        D.point_barre(sc, x, 6.0, 1.4)
    D.etrier(sc, -2.0, 5.0, 24.0, 61.0, lw=0.30, retour=4.0)
    for x in (4.0, 16.0):
        sc.line(x, -42.0, x, -2.0, "STR_FERRAILLAGE", 0.32)

    D.cote_h(sc, -5.0, 25.0, 78.0, "30", fs=3.0)
    D.cote_v(sc, 2.0, 69.0, 34.0, "67", fs=3.0)
    D.cote_h(sc, 0.0, 20.0, -51.0, "20", fs=3.0)
    D.cote_h(sc, -22.5, 42.5, -87.0, "65", fs=3.0)
    D.cote_v(sc, -75.0, -45.0, 52.0, "30", fs=3.0)

    sc.leader("Poutre de rive 30 x 67", 42.0, 61.0, 23.0, 52.0, fontsize=2.0)
    sc.leader("4 HA 14; HA 8 e = 300", 42.0, 55.0, 23.0, 49.0, fontsize=1.9)
    sc.leader("Appui articulé — à valider BET", 42.0, 15.0, 19.0, 1.0, fontsize=1.8)
    sc.text("Voile BA neuf 20 cm", 31.0, -13.0, 2.1, align="left")
    sc.text("4 HA 12/face", 31.0, -19.0, 2.0, align="left")
    sc.text("HA 8 e = 250", 31.0, -25.0, 1.9, align="left")
    sc.leader("Semelle filante 65 x 30", 49.0, -67.0, 35.0, -59.0, fontsize=1.9)
    sc.leader("Arase NGF 39,02", 49.0, -72.0, 35.0, -59.0, fontsize=1.8)
    return sc

def detail_F() -> E.Scene:
    """Plan de principe poteau / poutre perpendiculaire / console de rive."""
    sc = E.Scene()
    sc.rect(-12.0, -12.0, 12.0, 50.0, "STR_EXISTANT", 0.35,
            hatch="ANSI31", angle=45.0, spacing=2.0)
    sc.rect(0.0, 0.0, 200.0, 25.0, "STR_COFFRAGE_BA", 0.50,
            hatch="ANSI31", angle=45.0, spacing=2.0)
    sc.rect(117.5, 0.0, 25.0, 25.0, "STR_COFFRAGE_BA", 0.50,
            hatch="ANSI37", angle=0.0, spacing=1.4)
    sc.rect(170.0, -5.0, 30.0, 35.0, "STR_COFFRAGE_BA", 0.60,
            hatch="ANSI31", angle=0.0, spacing=1.4)

    D.cote_h(sc, 0.0, 130.0, -22.0, "1,30 m", fs=3.0)
    D.cote_h(sc, 130.0, 200.0, -22.0, "0,70 m", fs=3.0)
    D.cote_h(sc, 0.0, 200.0, -42.0, "2,00 m", fs=3.0)
    sc.leader("Poutre perpendiculaire 25 x 67", 35.0, 60.0, 82.0, 22.0, fontsize=1.9)
    sc.leader("Poteau 25 x 25; axe 1,30 m", 40.0, -62.0, 130.0, 12.5, fontsize=1.9)
    sc.leader("Rive 30 x 67 sur console", 172.0, 47.0, 185.0, 12.0, fontsize=1.8)
    sc.text("PLAN DE PRINCIPE — cotes en cm", 100.0, 80.0, 2.1, align="center")
    return sc

def detail_G() -> E.Scene:
    """Appui glissant de la dalle sur la façade — sans ancrage dans le mur."""
    sc = E.Scene()
    sc.rect(-28.0, -35.0, 28.0, 85.0, "STR_EXISTANT", 0.40,
            hatch="ANSI31", angle=45.0, spacing=2.2)
    sc.rect(-6.0, -2.0, 12.0, 2.0, "STR_ACIER_PROFILS", 0.35,
            hatch="ANSI31", angle=45.0, spacing=1.0)
    sc.rect(0.0, 0.0, 170.0, 20.0, "STR_COFFRAGE_BA", 0.50, fill=True)
    D.beton_rect(sc, 170.0, -67.0, 30.0, 67.0, sp=1.4)
    sc.line(6.0, 4.0, 166.0, 4.0, "STR_FERRAILLAGE", 0.35)
    sc.line(6.0, 6.2, 166.0, 6.2, "STR_FERRAILLAGE", 0.35)

    D.cote_h(sc, 0.0, 170.0, 42.0, "1,70 m", fs=3.0)
    D.cote_h(sc, 170.0, 200.0, 42.0, "30", fs=3.0)
    D.cote_h(sc, 0.0, 200.0, 58.0, "2,00 m", fs=3.0)
    D.cote_v(sc, 0.0, 20.0, -40.0, "20", fs=3.0, side="right")
    D.cote_v(sc, -67.0, 0.0, 214.0, "67", fs=3.0)

    sc.leader("Appui glissant + PTFE", 8.0, 77.0, 1.0, 0.0, fontsize=1.9)
    sc.leader("Sans ancrage", 8.0, 72.0, 1.0, 0.0, fontsize=1.8)
    sc.text("Dalle BA 20 cm", 65.0, 31.0, 2.1, align="center")
    sc.text("4 HA 10 — sens portée", 65.0, 25.0, 2.0, align="center")
    sc.leader("Rive 30 x 67", 176.0, -74.0, 184.0, -7.0, fontsize=1.8)
    sc.text("Joint vertical 20 mm", 46.0, -46.0, 2.0, align="left")
    sc.text("Interface à coordonner — DOC-02 §5.5", 46.0, -52.0, 1.8, align="left")
    return sc

def detail_H() -> E.Scene:
    """Clavetage du voile de rive neuf au mur pignon existant."""
    sc = E.Scene()
    sc.rect(-30.0, 0.0, 30.0, 90.0, "STR_EXISTANT", 0.40,
            hatch="ANSI31", angle=45.0, spacing=2.2)
    D.beton_rect(sc, 0.0, 0.0, 20.0, 90.0, sp=1.3)
    for y in (14.0, 34.0, 54.0, 74.0):
        sc.line(-18.0, y, 18.0, y, "STR_FERRAILLAGE", 0.35)
        sc.line(-16.0, y, -12.0, y + 6.0, "STR_FERRAILLAGE", 0.30)
        D.point_barre(sc, -12.0, y, 1.2)
    for x in (4.0, 16.0):
        sc.line(x, 2.0, x, 88.0, "STR_FERRAILLAGE", 0.30)

    D.cote_h(sc, 0.0, 20.0, -8.0, "20", fs=2.8)
    sc.leader("Pignon existant", -18.0, 82.0, -20.0, 74.0, fontsize=1.8)
    sc.text("Voile BA neuf 20 cm", 10.0, 112.0, 1.9, align="center")
    sc.text("4 HA 12 / face", 10.0, 106.0, 1.9, align="center")
    sc.text("HA 8 e = 250", 10.0, 100.0, 1.9, align="center")
    sc.text("HA 12 traversants", -17.0, -14.0, 1.9, align="left")
    sc.text("e = 500; scellement sain", -17.0, -20.0, 1.8, align="left")
    return sc

def placer(pb, sc, x, y, w, h, scale):
    pb.k = 10.0 / scale
    x0, y0, x1, y1 = pb.bbox(sc)
    cw, ch = (x1 - x0) * pb.k, (y1 - y0) * pb.k
    pb.set_origin(x + (w - cw) / 2.0 - x0 * pb.k,
                  y + (h - ch) / 2.0 - y0 * pb.k)
    pb.render(sc)


def tableau_assembleages(pb, x, y, rows, titre):
    pb.tableau(x, y, titre, ["Rep.", "Assemblage", "Disposition", "Reprise"],
               rows, [14, 70, 62, 44], size=2.2, hrow=5.8, hline=4.6)
    return y - 5.8 - 4.6 * len(rows)


def page1(pb):
    scA, scB, scC, scD = detail_A(), detail_B(), detail_C(), detail_D()

    # Abaisser les cadres pour réserver une zone de titre distincte en tête.
    # Les scènes A–C passent au 1/12 afin que toutes les annotations restent
    # dans leurs cadres ; le détail D reste au 1/14.
    pb.frame(14, 152, 96, 110)
    placer(pb, scA, 14, 152, 96, 110, 12.0)
    pb.vtitle(14, 265, "A — APPUI SUR JAMBAGE BA — 1/12")

    pb.frame(118, 152, 96, 110)
    placer(pb, scB, 118, 152, 96, 110, 12.0)
    pb.vtitle(118, 265, "B — SOMMIER SOUS MUR — 1/12")

    pb.frame(222, 152, 96, 110)
    placer(pb, scC, 222, 152, 96, 110, 12.0)
    pb.vtitle(222, 265, "C — ENCASTREMENT MEULIÈRE — 1/12")

    pb.frame(326, 152, 80, 110)
    placer(pb, scD, 326, 152, 80, 110, 14.0)
    pb.vtitle(326, 265, "D — JONCTION SUR POTEAU — 1/14")

    tableau_assembleages(pb, 14, 146, [
        ("A", "Profilé / jambage BA", "Platine + 4 tiges M16", "M 44 kN·m"),
        ("B", "Profilé / sommier BA", "Platine 470 x 250 x 20", "V 87 kN"),
        ("C", "Profilé / meulière", "Réservation 32 x 27", "V 47 kN"),
        ("D", "Profilé / poteau BA", "Platine + 4 M20 8.8", "M 156 kN·m"),
    ], "TABLEAU DES ASSEMBLAGES — PL-05/1")

    pb.note_block(14, 108, "DISPOSITIONS CONSTRUCTIVES", [
        "1. Platines et goussets soudés en atelier ; soudure d'atelier contrôlée 100 %.",
        "2. Mortier de calage sans retrait classe M50, épaisseur 10 à 30 mm.",
        "3. Tiges d'ancrage : perçage Ø 18, résine chimique, profondeur 15 cm mini.",
        "4. Clavetage dans la meulière : scellement à la résine après dépoussiérage et humidification.",
        "5. Toutes les platines en contact avec la maçonnerie reçoivent une protection anticorrosion.",
        "6. Reprise provisoire sur étais métalliques avant dépose de toute maçonnerie porteuse.",
    ], width=250)

    pb.note_block(272, 108, "TOLÉRANCES", [
        "1. Implantation ± 10 mm.",
        "2. Niveau d'assise ± 5 mm.",
        "3. Verticalité du poteau : H/500.",
        "4. Serrage boulons au couple prescrit.",
    ], width=130)


def page2(pb):
    scE, scF, scG, scH = detail_E(), detail_F(), detail_G(), detail_H()

    pb.frame(14, 143, 96, 104)
    placer(pb, scE, 14, 143, 96, 104, 20.0)
    pb.vtitle(14, 250, "E — APPUI SUR VOILE DE RIVE NEUF — 1/20")

    pb.frame(118, 143, 96, 104)
    placer(pb, scF, 118, 143, 96, 104, 30.0)
    pb.vtitle(118, 250, "F — APPUI SUR CONSOLE 0,70 m — 1/30")

    pb.frame(222, 143, 96, 104)
    placer(pb, scG, 222, 143, 96, 104, 40.0)
    pb.vtitle(222, 250, "G — APPUI GLISSANT DALLE / FAÇADE — 1/40")

    pb.frame(326, 143, 80, 104)
    placer(pb, scH, 326, 143, 80, 104, 20.0)
    pb.vtitle(326, 250, "H — CLAVETAGE AU PIGNON — 1/20")

    tableau_assembleages(pb, 14, 136, [
        ("E", "Poutre 8,03 / voile neuf", "Appui simple articulé*", "V_Ed 69,9 kN"),
        ("F", "Poutre 8,03 / console", "Poutre 25 x 67 ; 0,70 m", "R poteau 69,9 kN"),
        ("G", "Dalle / façade", "Appui glissant, sans scellement", "4 HA 10 ; M 4,6 kN·m"),
        ("H", "Voile neuf / pignon", "HA 12 traversants e = 500", "4 HA 12/face"),
    ], "TABLEAU DES ASSEMBLAGES — PL-05/2")

    pb.note_block(14, 100, "NOTES DE MISE EN ŒUVRE — E-02 RECTIFIÉ", [
        "1. Poutre-acrotère de rive 30 x 67, portée 8,03 m : 4 HA 14, étriers HA 8 e = 300.",
        "2. Appui droit sur voile BA neuf 20 cm, semelle filante 65 x 30 à NGF 39,02.",
        "3. À gauche, appui sur l'about de la poutre perpendiculaire 25 x 67 ; poteau à 1,30 m, console 0,70 m.",
        "4. Poteau 25 x 25 : 6 HA 8 ; puits n° 1 Ø 1,35 m. Puits n° 2 sous voile : Ø 1,75 m.",
        "5. Dalle BA 20 cm, portée de 1,70 m, 4 HA 10 ; appui glissant sur façade (sans ancrage).",
        "6. Joint vertical 20 mm : coordination obligatoire entre appui glissant, étanchéité et menuiserie.",
        "7. *Dimensions / nature de l'appareil d'appui du voile à valider avant exécution par le BET et le fournisseur.",
    ], width=330)

    pb.note_block(356, 100, "PHASAGE", [
        "1. Étaiement.",
        "2. Fondation / voile neuf.",
        "3. Poutre et poteau.",
        "4. Dalle / appuis.",
        "5. Contrôles BET.",
        "6. Dépose étais.",
    ], width=48)

def main():
    os.makedirs(OUT, exist_ok=True)
    scs = [detail_A(), detail_B(), detail_C(), detail_D(), detail_E(),
           detail_F(), detail_G(), detail_H()]

    # ---------------- DXF -------------------------------------------------
    dxf = E.DxfBackend("PL-05")
    placements = [
        (0.0, 0.0), (130.0, 0.0), (260.0, 0.0), (390.0, 0.0),
        (0.0, -260.0), (180.0, -260.0), (470.0, -260.0), (770.0, -260.0),
    ]
    for sc, (ox, oy) in zip(scs, placements):
        t = E.Scene()
        for it in sc.items:
            t.items.append(_shift(it, ox, oy))
        dxf.render(t)
    p_dxf = dxf.save(os.path.join(OUT, "PL-05_Assemblages_Acier_BA.dxf"))

    # ---------------- PDF (2 pages) ---------------------------------------
    pb = E.PdfBackend("PL-05", CARTOUCHE)
    pb.new_page()
    pb.titre("PL-05/1 — ASSEMBLAGES ACIER / BA — REPRISES EN SOUS-ŒUVRE",
             "Appuis de profilés S355 sur jambages et sommiers BA, "
             "encastrement en meulière, jonction sur poteau — échelles 1/12 et 1/14")
    page1(pb)

    pb.add_page(CARTOUCHE2)
    pb.titre("PL-05/2 — ASSEMBLAGES BA — EXTENSION E-02 RECTIFIÉE",
             "Appui sur voile neuf, console portée par le poteau et appui glissant de la dalle")
    page2(pb)

    p_pdf = os.path.join(OUT, "PL-05_Assemblages_Acier_BA.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


def _shift(it, ox, oy):
    k = it[0]
    if k == "line":
        _, p1, p2, *r = it
        return ("line", (p1[0] + ox, p1[1] + oy),
                (p2[0] + ox, p2[1] + oy), *r)
    if k == "rect":
        _, (x, y), (w, h), *r = it
        return ("rect", (x + ox, y + oy), (w, h), *r)
    if k == "poly":
        _, pts, *r = it
        return ("poly", [(a + ox, b + oy) for (a, b) in pts], *r)
    if k == "circle":
        _, (cx, cy), rad, *r = it
        return ("circle", (cx + ox, cy + oy), rad, *r)
    if k == "arc":
        _, (cx, cy), rad, a1, a2, *r = it
        return ("arc", (cx + ox, cy + oy), rad, a1, a2, *r)
    if k == "text":
        _, s, (x, y), *r = it
        return ("text", s, (x + ox, y + oy), *r)
    if k == "arrow":
        _, pts, layer = it
        return ("arrow", [(a + ox, b + oy) for (a, b) in pts], layer)
    if k == "hatchpoly":
        _, pts, *r = it
        return ("hatchpoly", [(a + ox, b + oy) for (a, b) in pts], *r)
    if k == "dim_h":
        _, x1, x2, y, *r = it
        return ("dim_h", x1 + ox, x2 + ox, y + oy, *r)
    if k == "dim_v":
        _, y1, y2, x, *r = it
        return ("dim_v", y1 + oy, y2 + oy, x + ox, *r)
    return it


if __name__ == "__main__":
    main()
