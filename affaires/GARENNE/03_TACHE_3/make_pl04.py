"""
PL-04 — PLAN DE FERRAILLAGE ET DÉTAILS.

Une planche A3 paysage, quatre cadres :

  A. coupe de la poutre-acrotère 30 x 67 : 4 HA 14, étriers HA 8 e = 300 ;
  B. plan d'appui de la poutre de rive sur la console (poteau à 1,30 m,
     console 0,70 m) ;
  C. poteau BA 25 x 25, 6 HA 8, au-dessus du puits n° 1 Ø 1,35 m ;
  D. dalle BA 20 cm, portée de 1,70 m entre façade et poutre de rive ;
  D. tableau récapitulatif des aciers + nomenclature des façonnages.

Toutes les cotes en centimètres modèle ; à 1/20, 1 cm = 0,5 mm papier.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "00_SOURCES"))

import plan_engine as E       # noqa: E402
import detail_lib as D        # noqa: E402

OUT = os.path.join(HERE, "plans")
RES = json.load(open(os.path.join(HERE, "..", "02_TACHE_2",
                                  "calculs_resultats.json")))

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-04 — FERRAILLAGE ET DÉTAILS",
    "sous_titre": "E-02 rectifié — poutre 4 HA 14, poteau à 1,30 m, "
                  "console 0,70 m et dalle 1,70 m",
    "repere": "PL-04",
    "phase": "Tâche 4 — détails d'exécution",
    "indice": "Indice B — révision E-02 — 12/11/2026",
    "echelle": "Échelles : 1/10, 1/20 et 1/40",
    "date": "C25/30 — B500B",
}


# ---------------------------------------------------------------------------
# Cadre A — coupe transversale de la poutre-acrotère 30 x 67 (1/10)
# ---------------------------------------------------------------------------

def cadre_poutre() -> E.Scene:
    """Coupe en travée de la poutre 30 x 67 — armatures retenues E-02."""
    sc = E.Scene()
    b, h, enrob = 30.0, 67.0, 3.0

    D.beton_rect(sc, 0, 0, b, h, sp=1.1)
    # 4 HA 14 en nappe basse, une file (As = 6,16 cm²).
    for x in (5.0, 11.7, 18.3, 25.0):
        D.point_barre(sc, x, 4.2, 1.4)
    D.etrier(sc, enrob, enrob, b - 2 * enrob, h - 2 * enrob,
             lw=0.35, retour=5.0)

    D.cote_h(sc, 0, b, -9.0, "30")
    D.cote_v(sc, 0, h, -8.0, "67")
    D.cote_v(sc, 0, enrob, -16.0, "3")

    sc.leader("4 HA 14 — nappe basse\nAs = 6,16 cm² > 5,41 requis",
              36, 14, 18.0, 4.2, fontsize=1.95)
    sc.leader("Étriers HA 8 — e = 300 mm\n(calcul DOC-03)",
              36, 48, 27.0, 36.0, fontsize=1.95)
    sc.leader("Enrobage nominal 30 mm", -24, 7, 3.0, 8.0, fontsize=1.85)
    return sc

def cadre_poutre_appui() -> E.Scene:
    """Plan schématique de l'appui sur la console de la poutre perpendiculaire."""
    sc = E.Scene()

    # Nu de façade existante, puis poutre perpendiculaire jusqu'à la rive.
    sc.rect(-12.0, -12.0, 12.0, 50.0, "STR_EXISTANT", 0.35,
            hatch="ANSI31", angle=45.0, spacing=2.0)
    sc.rect(0.0, 0.0, 200.0, 25.0, "STR_COFFRAGE_BA", 0.50,
            hatch="ANSI31", angle=45.0, spacing=2.0)

    # Poteau sous la poutre perpendiculaire, axe à 1,30 m du nu de façade.
    sc.rect(117.5, 0.0, 25.0, 25.0, "STR_COFFRAGE_BA", 0.50,
            hatch="ANSI37", angle=0.0, spacing=1.4)
    # Poutre-acrotère de rive (vue en plan) portée par l'about de la console.
    sc.rect(170.0, -2.5, 30.0, 30.0, "STR_COFFRAGE_BA", 0.60,
            hatch="ANSI31", angle=0.0, spacing=1.4)

    D.cote_h(sc, 0.0, 130.0, -22.0, "1,30 m")
    D.cote_h(sc, 130.0, 200.0, -22.0, "0,70 m")
    D.cote_h(sc, 0.0, 200.0, -40.0, "2,00 m")

    sc.leader("Poutre perpendiculaire BA 25 x 67", 48, 62,
              82.0, 23.0, fontsize=1.9)
    sc.leader("Poteau BA 25 x 25\naxe à 1,30 m de façade", 52, -50,
              130.0, 12.5, fontsize=1.9)
    sc.leader("Poutre-acrotère 30 x 67\nappui à l'about de la console",
              208, 48, 185.0, 13.0, fontsize=1.9)
    sc.text("PLAN DE PRINCIPE — cotes en cm", 100.0, 83.0, 1.8,
            align="center")
    return sc

def cadre_poteau() -> E.Scene:
    """Coupe schématique du poteau et du puits n° 1 (Ø 1,35 m)."""
    sc = E.Scene()
    D.beton_rect(sc, -55.0, -244.0, 135.0, 244.0, sp=1.6)
    D.beton_rect(sc, 0.0, 0.0, 25.0, 44.0, sp=1.1)
    for x in (3.5, 12.5, 21.5):
        sc.line(x, -10.0, x, 42.0, "STR_FERRAILLAGE", 0.35)
    for y in (4.0, 24.0, 40.0):
        D.etrier(sc, 3.0, y, 19.0, 3.0, lw=0.25, retour=2.0)
    D.ligne_rupture(sc, 12.5, 48.0, 65.0, amp=2.5)

    D.cote_h(sc, -55.0, 80.0, -258.0, "Ø 1,35 m")
    D.cote_v(sc, -244.0, 0.0, 90.0, "2,40 m")
    D.cote_h(sc, 0.0, 25.0, 57.0, "25")
    sc.text("Poteau BA 25 x 25", 35.0, 38.0, 2.4, align="left")
    sc.text("6 HA 8 — e = 200", 35.0, 32.0, 2.2, align="left")
    sc.text("Puits n° 1 — Ø 1,35 m", 12.5, -92.0, 2.8,
            align="center")
    sc.text("Gros béton C16/20", 12.5, -99.0, 2.6, align="center")
    sc.text("Profondeur calcul : 2,40 m", 12.5, -224.0, 2.2,
            align="center")
    return sc

def cadre_dalle() -> E.Scene:
    """Coupe transversale de la dalle, de son appui glissant à la poutre de rive."""
    sc = E.Scene()
    ep = 20.0
    x_voie, x_ber, x_ext = 0.0, 170.0, 200.0

    # Façade existante et appui glissant, sans scellement dans la maçonnerie.
    sc.rect(-28.0, -42.0, 28.0, 86.0, "STR_EXISTANT", 0.35,
            hatch="ANSI31", angle=45.0, spacing=2.2)
    sc.rect(-6.0, -2.0, 12.0, 2.0, "STR_ACIER_PROFILS", 0.35,
            hatch="ANSI31", angle=45.0, spacing=1.0)
    sc.rect(0.0, 0.0, x_ber, ep, "STR_COFFRAGE_BA", 0.50, fill=True)
    # Poutre-acrotère de rive 30 x 67, entre x=1,70 et 2,00 m.
    D.beton_rect(sc, x_ber, -67.0, 30.0, 67.0, sp=1.5)
    # Armatures longitudinales de la dalle (schéma en coupe).
    sc.line(4.0, 4.0, x_ber - 4.0, 4.0, "STR_FERRAILLAGE", 0.35)
    sc.line(4.0, 6.2, x_ber - 4.0, 6.2, "STR_FERRAILLAGE", 0.35)

    D.cote_h(sc, x_voie, x_ber, ep + 22.0, "1,70 m")
    D.cote_h(sc, x_ber, x_ext, ep + 22.0, "30")
    D.cote_h(sc, x_voie, x_ext, ep + 38.0, "2,00 m")
    D.cote_v(sc, 0.0, ep, -39.0, "20")
    D.cote_v(sc, -67.0, 0.0, 211.0, "67")

    sc.leader("Dalle BA 20 cm — 4 HA 10\nsens de portée",
              42, -26, 85.0, 5.0, fontsize=2.4)
    sc.leader("Appui glissant façade\nplatine + PTFE, sans ancrage",
              -18, 55, 0.0, 0.0, fontsize=2.0)
    sc.leader("Poutre-acrotère BA 30 x 67\nnu intérieur à 1,70 m",
              218, 36, 183.0, -4.0, fontsize=1.8)
    sc.text("Interface façade / joint de 20 mm : voir PL-05 et DOC-02 §5.5",
            84.0, -41.0, 1.75, align="center")
    return sc

def tableau_aciers(pb, x, y):
    rows = [
        ("PB1", "4 HA 14", "8,03 m*", "4 filants", "6,16", "Poutre-acrotère 30 x 67"),
        ("PB2", "HA 8", "e = 300", "étriers", "—", "Poutre-acrotère 8,03 m"),
        ("PP1", "2 HA 12", "selon ancrage", "2 filants", "2,26", "Poutre perpendiculaire 25 x 67"),
        ("PP2", "HA 8", "e = 300", "étriers", "—", "Poutre perpendiculaire"),
        ("C1", "6 HA 8", "selon hauteur", "6 verticaux", "3,02", "Poteau BA 25 x 25"),
        ("D1", "4 HA 10", "sens de portée", "filants", "3,14", "Dalle BA ép. 20 cm"),
        ("V1", "4 HA 12", "H = 5,28 m*", "par face", "4,52/face", "Voile neuf ép. 20 cm"),
        ("V2", "HA 8", "e = 250", "répartition", "—", "Voile neuf — 2 faces"),
    ]
    pb.tableau(x, y, "NOMENCLATURE — ARMATURES RETENUES (B500B)", [
        "Rep.", "Désignation", "Pas / longueur", "Disposition", "As (cm²)", "Emploi"],
        rows, [13, 23, 24, 22, 20, 70], size=2.05, hrow=5.4, hline=4.3)
    pb.note_block(x, y - 5.4 - 4.3 * len(rows) - 2, "RÉSERVES DE FAÇONNAGE", [
        "* Longueurs indicatives : ancrages, recouvrements et façonnages à vérifier",
        "  sur plans de ferraillage avant commande. Pas de substitution sans BET.",
    ], width=175)
    return y - 5.4 - 4.3 * len(rows)

def tableau_contraintes(pb, x, y):
    rows = [
        ("M_Ed", "140,3 kN·m", "M_Rd > M_Ed"),
        ("V_Ed", "69,9 kN", "V_Rd,c = 81,3 kN"),
        ("As requis", "5,41 cm²", "4 HA 14 = 6,16 cm²"),
        ("Étriers", "HA 8 e = 300", "DOC-03 §3.3"),
        ("Flèche LT", "22,48 mm", "L/357 ; cf. 20 mm"),
    ]
    pb.tableau(x, y, "VÉRIFICATIONS EC2 — POUTRE (DOC-03)", ["Grandeur", "Valeur",
                "Critère / disposition"], rows, [29, 36, 57], size=2.05,
               hrow=5.4, hline=4.2)
    return y - 5.4 - 4.2 * len(rows)

def placer(pb, sc, x, y, w, h, scale, marge=4.0):
    """Centre la scène dans le cadre (x, y, w, h) à l'échelle donnée."""
    pb.k = 10.0 / scale
    x0, y0, x1, y1 = pb.bbox(sc)
    cw = (x1 - x0) * pb.k
    ch = (y1 - y0) * pb.k
    ox = x + (w - cw) / 2.0 - x0 * pb.k
    oy = y + (h - ch) / 2.0 - y0 * pb.k
    pb.set_origin(ox, oy)
    pb.render(sc)
    return cw, ch


CARTOUCHE2 = dict(CARTOUCHE)
CARTOUCHE2["repere"] = "PL-04/2"
CARTOUCHE2["titre"] = "PL-04/2 — DALLE, POTEAU, DÉTAILS"
CARTOUCHE2["sous_titre"] = "Poteau sur puits, dalle portée sur 1,70 m et façonnages indicatifs"
CARTOUCHE2["echelle"] = "Échelles : 1/20 et 1/25"


def placer(pb, sc, x, y, w, h, scale):
    """Centre la scène dans le cadre (x, y, w, h) à l'échelle donnée."""
    pb.k = 10.0 / scale
    x0, y0, x1, y1 = pb.bbox(sc)
    cw, ch = (x1 - x0) * pb.k, (y1 - y0) * pb.k
    pb.set_origin(x + (w - cw) / 2.0 - x0 * pb.k,
                  y + (h - ch) / 2.0 - y0 * pb.k)
    pb.render(sc)
    return cw, ch


def cadre_ancrage() -> E.Scene:
    """Détail indicatif de recouvrement et ancrage pour HA 14 (40 Ø)."""
    sc = E.Scene()

    D.etrier(sc, 0, 0, 24.0, 61.0, lw=0.40, retour=8.0)
    D.cote_h(sc, 0, 24.0, -8.0, "24")
    D.cote_v(sc, 0, 61.0, -8.0, "61")
    sc.leader("Étrier HA 8 — 24 x 61\nretours d'angle selon façonnage",
              34, 66, 24.0, 58.0, fontsize=1.9)

    # Recouvrement effectif de 56 cm = 40 Ø pour des barres HA 14.
    y = 120.0
    D.barre(sc, [(0.0, y), (100.0, y)], "HA 14", lw=0.45)
    D.barre(sc, [(44.0, y + 9.0), (144.0, y + 9.0)], "HA 14", lw=0.45)
    sc.line(44.0, y - 4.0, 44.0, y + 13.0, "STR_COTATIONS_TEXTES", 0.18)
    sc.line(100.0, y - 4.0, 100.0, y + 13.0, "STR_COTATIONS_TEXTES", 0.18)
    D.cote_h(sc, 44.0, 100.0, y - 9.0, "40 Ø = 56 cm")
    sc.leader("Recouvrement HA 14\n40 Ø minimum — à valider par BET",
              42, y + 34.0, 78.0, y + 9.0, fontsize=1.9)

    y2 = 62.0
    D.barre(sc, [(0.0, y2), (56.0, y2), (56.0, y2 - 16.0)], "HA 14",
            lw=0.45)
    D.cote_h(sc, 0.0, 56.0, y2 - 28.0, "40 Ø = 56 cm")
    sc.leader("Ancrage droit dans l'appui\nlongueur indicative 40 Ø",
              68, y2 + 12.0, 44.0, y2 + 2.0, fontsize=1.9)
    return sc

def schema_principe() -> E.Scene:
    """Élévation de principe : étriers HA 8 e = 300 mm sur la poutre."""
    sc = E.Scene()
    L, h = 803.0, 67.0
    sc.rect(0, 0, L, h, "STR_COFFRAGE_BA", 0.45, fill=True)
    # Appuis schématiques aux deux extrémités.
    for x in (0.0, L - 20.0):
        sc.rect(x - 20.0 if x else -20.0, -18.0, 20.0, 18.0,
                "STR_COFFRAGE_BA", 0.35, hatch="ANSI31", spacing=1.6)
    x = 15.0
    while x < L - 5.0:
        sc.line(x, 3.0, x, h - 3.0, "STR_FERRAILLAGE", 0.25)
        x += 30.0
    sc.line(0.0, 4.2, L, 4.2, "STR_FERRAILLAGE", 0.40)
    sc.text("HA 8 — e = 300 mm (espacement nominal)", L / 2.0, h + 15.0,
            2.2, align="center")
    sc.text("Vérifier les zones d'ancrage et les dispositions locales au droit des appuis",
            L / 2.0, -28.0, 2.0, align="center")
    return sc

def page1(pb):
    scA, scB, scS = cadre_poutre(), cadre_poutre_appui(), schema_principe()

    pb.frame(14, 158, 152, 104)
    placer(pb, scA, 14, 158, 152, 104, 10.0)
    pb.vtitle(14, 264.5, "A — POUTRE-ACROTÈRE 30 x 67 — 1/10")

    pb.frame(176, 158, 152, 104)
    placer(pb, scB, 176, 158, 152, 104, 20.0)
    pb.vtitle(176, 264.5, "B — APPUI SUR CONSOLE — PLAN DE PRINCIPE 1/20")

    pb.frame(14, 74, 300, 74)
    placer(pb, scS, 14, 74, 300, 74, 40.0)
    pb.vtitle(14, 150.5, "C — ÉLÉVATION : ÉTRIERS HA 8 e = 300 mm — PRINCIPE")

    pb.note_block(322, 144, "GÉOMÉTRIE ET ARMATURES E-02", [
        "1. Poutre-acrotère de rive 30 x 67, portée 8,03 m, isostatique.",
        "2. Armatures principales calculées : 4 HA 14 (As = 6,16 cm²).",
        "3. Étriers HA 8 e = 300 mm ; dispositions d'appui à confirmer au ferraillage.",
        "4. Appui gauche sur l'about de la poutre perpendiculaire 25 x 67.",
        "5. Poteau BA 25 x 25 à 1,30 m du nu de façade ; console = 0,70 m.",
        "6. Appui droit sur le voile de rive BA neuf (voir PL-05/2).",
        "7. Contre-flèche de coffrage : 20 mm ; flèche LT = 22,48 mm.",
    ], width=70)

def page2(pb):
    scC, scP, scG = cadre_poteau(), cadre_dalle(), cadre_ancrage()

    pb.frame(14, 132, 80, 144)
    placer(pb, scC, 14, 132, 80, 144, 25.0)
    pb.vtitle(14, 281, "D — POTEAU / PUITS N° 1 — 1/25")

    pb.frame(102, 132, 176, 122)
    placer(pb, scP, 102, 132, 176, 122, 20.0)
    pb.vtitle(102, 281, "E — DALLE 20 cm ET APPUI FAÇADE — 1/20")

    pb.frame(286, 132, 118, 144)
    placer(pb, scG, 286, 132, 118, 144, 20.0)
    pb.vtitle(286, 281, "F — FAÇONNAGE HA 14 — 1/20")

    tableau_aciers(pb, 14, 126)
    tableau_contraintes(pb, 190, 126)
    pb.note_block(322, 126, "FONDATIONS / VOILE", [
        "1. Puits n° 1 sous poteau : Ø 1,35 m, gros béton C16/20.",
        "2. Puits n° 2 sous voile : Ø 1,75 m ; profondeur de calcul 2,40 m.",
        "3. Arase des fondations : NGF 39,02 (DOC-03 §4.3).",
        "4. Voile de rive neuf : 20 cm, 4 HA 12 par face, HA 8 e = 250.",
        "5. Semelle filante neuve sous voile : 65 x 30 cm.",
        "6. Appui de la dalle sur façade : glissant, sans scellement ; joint 20 mm à coordonner.",
    ], width=82)

    pb.note_block(190, 83, "MISE EN ŒUVRE", [
        "1. Aciers B500B ; ancrages / recouvrements à valider selon plans définitifs.",
        "2. Enrobages selon exposition et plans de coffrage.",
        "3. Contre-flèche 20 mm sur la poutre-acrotère de 8,03 m.",
        "4. Pas de substitution de diamètre sans accord du BET.",
    ], width=114)

    pb.note_block(322, 83, "CONTRÔLES", [
        "1. Contrôle du ferraillage avant chaque bétonnage.",
        "2. Vérification des appuis / niveaux avant pose de la poutre.",
        "3. Réception du fond de fouille par le BET.",
        "4. PV béton C25/30 et acier B500B.",
    ], width=82)

def cadre_elevation_poutre() -> E.Scene:
    """Élévation indicative de la poutre de 8,03 m avec étriers e=300."""
    sc = E.Scene()
    L, h = 803.0, 67.0
    sc.rect(0, 0, L, h, "STR_COFFRAGE_BA", 0.40)
    sc.rect(-25.0, -40.0, 25.0, 40.0, "STR_EXISTANT", 0.35)
    sc.rect(L, -40.0, 25.0, 40.0, "STR_COFFRAGE_BA", 0.40)
    x = 15.0
    while x < L - 5.0:
        sc.line(x, 4.0, x, h - 4.0, "STR_FERRAILLAGE", 0.22)
        x += 30.0
    sc.line(-22.0, 4.2, L + 22.0, 4.2, "STR_FERRAILLAGE", 0.45)
    sc.line(-22.0, 6.2, L + 22.0, 6.2, "STR_FERRAILLAGE", 0.45)
    D.cote_h(sc, 0, L, -30.0, "8,03 m")
    D.cote_v(sc, 0, h, -46.0, "67")
    D.bulle(sc, 40.0, h * 0.55, "HA 8", r=9.0, fs=2.3)
    sc.text("e = 300 mm", L / 2.0, h + 14.0, 2.2, align="center")
    return sc

def main():
    os.makedirs(OUT, exist_ok=True)
    scA, scB = cadre_poutre(), cadre_poutre_appui()
    scC, scP = cadre_poteau(), cadre_dalle()
    scE = schema_principe()

    # ---------------- DXF (un seul fichier, 2 files) ----------------------
    dxf = E.DxfBackend("PL-04")
    scG = cadre_ancrage()
    for sc, (ox, oy) in ((scA, (0, 0)), (scB, (150, 0)),
                         (scE, (0, -230)), (scP, (1000, -230)),
                         (scC, (1400, -230)), (scG, (1600, -230))):
        t = E.Scene()
        for it in sc.items:
            t.items.append(_shift(it, ox, oy))
        dxf.render(t)
    p_dxf = dxf.save(os.path.join(OUT, "PL-04_Ferraillage_Details.dxf"))

    # ---------------- PDF (2 pages) ---------------------------------------
    pb = E.PdfBackend("PL-04", CARTOUCHE)
    pb.new_page()
    pb.titre("PL-04/1 — FERRAILLAGE DE LA POUTRE-ACROTÈRE",
             "Coupe de ferraillage, plan d'appui sur console et élévation "
             "schématique — béton C25/30, acier B500B")
    page1(pb)
    pb.add_page(CARTOUCHE2)
    pb.titre("PL-04/2 — FERRAILLAGE : POTEAU, DALLE ET FAÇONNAGE",
             "Poteau BA 25 x 25 sur puits, dalle terrasse 20 cm et "
             "façonnage indicatif des armatures")
    page2(pb)

    p_pdf = os.path.join(OUT, "PL-04_Ferraillage_Details.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


def _shift(it, ox, oy):
    k = it[0]
    if k == "line":
        _, p1, p2, *r = it
        return ("line", (p1[0] + ox, p1[1] + oy), (p2[0] + ox, p2[1] + oy),
                *r)
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
