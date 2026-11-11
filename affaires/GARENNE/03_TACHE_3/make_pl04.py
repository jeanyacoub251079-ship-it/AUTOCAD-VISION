"""
PL-04 — PLAN DE FERRAILLAGE ET DÉTAILS.

Une planche A3 paysage, quatre cadres :

  A. coupe transversale de la poutre-acrotère 30 x 67 + coupe sur appui
     (1/20) : 4 HA 20 en nappe basse, 2 HA 12 de peau, étriers HA 8 e = 175,
     chapeaux sur appui, platine d'appui ;
  B. poteau BA 25 x 25 (1/20) : 6 HA 8 verticaux, cadres HA 8 e = 200,
     recouvrement et ancrage dans le puits ;
  C. dalle terrasse 20 cm (1/20) : 4 HA 10, nappe supérieure sur appui,
     console 1,20 m, ancrage dans la façade ;
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
    "sous_titre": "Poutre-acrotère, poteau BA et dalle terrasse — "
                  "coupes et façonnages",
    "repere": "PL-04",
    "phase": "Tâche 4 — détails d'exécution",
    "indice": "Indice A — 11/11/2026",
    "echelle": "Échelles : 1/20 et 1/10",
    "date": "C25/30 — B500B",
}


# ---------------------------------------------------------------------------
# Cadre A — coupe transversale de la poutre-acrotère 30 x 67 (1/10)
# ---------------------------------------------------------------------------

def cadre_poutre() -> E.Scene:
    """Coupe en travée, échelle 1/10 (1 cm modèle = 1 mm papier)."""
    sc = E.Scene()
    b, h = 30.0, 67.0
    enrob = 3.0

    # --- béton ------------------------------------------------------------
    D.beton_rect(sc, 0, 0, b, h, sp=1.1)

    # --- nappe basse 4 HA 20 (deux lits de 2) -----------------------------
    for i, dx in enumerate((7.0, 23.0)):
        D.point_barre(sc, dx, enrob + 1.0, 2.0)
    for i, dx in enumerate((7.0, 23.0)):
        D.point_barre(sc, dx, enrob + 3.4, 2.0)
    D.cote_h(sc, 7.0, 23.0, -5.5, "16")

    # --- nappe supérieure 2 HA 12 (chapeaux + montage) --------------------
    for dx in (7.0, 23.0):
        D.point_barre(sc, dx, h - enrob - 1.2, 1.2)

    # --- HA 12 de peau (2 x 2 faces) --------------------------------------
    for dy in (h / 2 - 8.0, h / 2 + 8.0):
        D.point_barre(sc, enrob + 0.6, dy, 1.2)
        D.point_barre(sc, b - enrob - 0.6, dy, 1.2)

    # --- étriers HA 8 e = 175 ---------------------------------------------
    D.etrier(sc, enrob, enrob, b - 2 * enrob, h - 2 * enrob, lw=0.35,
             retour=5.0)

    # --- cotes ------------------------------------------------------------
    D.cote_h(sc, 0, b, -12.0, "30")
    D.cote_v(sc, 0, h, -7.5, "67")
    D.cote_v(sc, 0, enrob, -15.0, "3")
    D.cote_v(sc, enrob, h - enrob, -15.0, "61")

    # --- repères / annotations -------------------------------------------
    sc.leader("4 HA 20 (2 lits de 2) — nappe basse\nAs = 12,57 cm² > 10,52 requis",
              36, 14, 24.0, 6.0, fontsize=1.95)
    sc.leader("2 HA 12 de montage en chapeau", 36, 66, 24.0,
              h - enrob - 1.2, fontsize=1.95)
    sc.leader("4 HA 12 de peau (1 par face et par lit)", 36, 40, 30.0,
              h / 2 + 8, fontsize=1.95)
    sc.leader("Étriers HA 8 e = 175 mm\n(retours 10 Ø)", -26, 60, 3.0, 30.0,
              fontsize=1.95)
    sc.leader("Enrobage 30 mm (XC4)", -26, 6, 3.0, 9.0, fontsize=1.9)

    # --- titre interne ----------------------------------------------------
    return sc


def cadre_poutre_appui() -> E.Scene:
    """Coupe sur appui (poteau) — 1/10, montre le chaînage et le chapeau."""
    sc = E.Scene()
    b, h = 30.0, 67.0
    xp, bp = 15.0, 25.0          # axe poteau, largeur poteau

    D.beton_rect(sc, 0, 0, b, h, sp=1.1)                    # poutre
    D.beton_rect(sc, xp - bp / 2, -25.0, bp, 25.0, sp=1.1)  # poteau (amorce)

    # étriers resserrés sur appui
    for i in range(4):
        D.etrier(sc, 3.0 + i * 2.0, 3.0, b - 6.0 - i * 4.0, h - 6.0,
                 lw=0.30, retour=4.0)
    # 4 HA 20 traversants ancrés
    for dx in (7.0, 23.0):
        D.point_barre(sc, dx, 4.0, 2.0)
        D.point_barre(sc, dx, 6.4, 2.0)
    # chapeau supérieur sur appui
    D.point_barre(sc, xp - 5.0, h - 4.2, 1.2)
    D.point_barre(sc, xp + 5.0, h - 4.2, 1.2)
    # attentes du poteau dans la poutre
    for dx in (xp - 8.0, xp + 8.0):
        sc.line(dx, 0, dx, h * 0.55, "STR_FERRAILLAGE", 0.35)
    # platine
    sc.rect(0, -2.5, b, 2.5, "STR_ACIER_PROFILS", 0.40)
    D.cote_h(sc, 0, b, -32.0, "30")
    D.cote_h(sc, xp - bp / 2, xp + bp / 2, -25.0, "25")
    sc.leader("Étriers resserrés e = 100 mm\nsur 1,5 h de part et d'autre "
              "de l'appui", 34, 54, b - 3.0, 40.0, fontsize=1.9)
    sc.leader("Attentes poteau HA 8 ancrées\n= 40 Ø dans la poutre", 34, 18,
              xp + 8.0, 30.0, fontsize=1.9)
    sc.leader("Platine 300 x 200 x 15\n+ mortier sans retrait", -22, 2,
              3.0, -2.0, fontsize=1.9)
    return sc


# ---------------------------------------------------------------------------
# Cadre B — poteau BA 25 x 25 (1/10)
# ---------------------------------------------------------------------------

def cadre_poteau() -> E.Scene:
    sc = E.Scene()
    b, h = 25.0, 25.0
    H = 320.0                     # hauteur libre 3,20 m — coupée

    D.beton_rect(sc, 0, 0, b, 78.0, sp=1.1)

    # 6 HA 8 : 3 par face, en attente dans le puits
    xs = (3.0, 12.5, 22.0)
    for x in xs:
        sc.line(x, -26.0, x, 72.0, "STR_FERRAILLAGE", 0.35)
    # cadres HA 8 e = 200
    for y in range(0, 71, 20):
        D.etrier(sc, 3.0, 3.0 + y, b - 6.0, min(20.0, 72.0 - y),
                 lw=0.25, retour=4.0)
    D.cote_h(sc, 0, b, -10.0, "25")
    D.cote_v(sc, 0, 20.0, -8.0, "20")
    D.cote_v(sc, 0, 72.0, 27.0, "")
    sc.leader("6 HA 8 verticaux (3 par face)", 30, 66, 22.0, 62.0,
              fontsize=1.85)
    sc.leader("Cadres HA 8 e = 200 mm", 30, 38, 22.0, 34.0, fontsize=1.85)
    sc.leader("Amorces dans le puits = 40 Ø", 30, 6, 22.0, 14.0,
              fontsize=1.85)
    return sc


# ---------------------------------------------------------------------------
# Cadre C — dalle terrasse (1/20)
# ---------------------------------------------------------------------------

def cadre_dalle() -> E.Scene:
    sc = E.Scene()
    ep = 20.0
    L1, L2 = 200.0, 120.0         # travée 2,00 m + console 1,20 m

    # façade existante
    sc.rect(-28.0, -42.0, 28.0, 84.0, "STR_EXISTANT", 0.35,
            hatch="ANSI31", angle=45.0, spacing=2.2)
    # dalle
    D.beton_rect(sc, 0, 0, L1 + L2, ep, sp=1.6)
    # poutre-acrotère (appui intermédiaire, à 2,00 m)
    D.beton_rect(sc, L1 - 15.0, -67.0, 30.0, 67.0, sp=1.6)
    # voile mitoyen en bout
    D.beton_rect(sc, L1 + L2, -50.0, 20.0, 50.0 + ep, sp=1.6)

    # --- nappe inférieure 4 HA 10 (travée) -------------------------------
    sc.line(-20.0, 4.0, L1 - 15.0, 4.0, "STR_FERRAILLAGE", 0.35)
    sc.line(-20.0, 6.2, L1 - 15.0, 6.2, "STR_FERRAILLAGE", 0.35)
    # --- nappe supérieure sur appui + console ----------------------------
    sc.line(L1 - 70.0, ep - 4.0, L1 + L2 + 8.0, ep - 4.0,
            "STR_FERRAILLAGE", 0.35)
    sc.line(L1 - 70.0, ep - 6.2, L1 + L2 + 8.0, ep - 6.2,
            "STR_FERRAILLAGE", 0.35)
    # --- ancrage dans la façade ------------------------------------------
    for dy in (4.0, 6.2):
        sc.line(-24.0, dy, -6.0, dy + 6.0, "STR_FERRAILLAGE", 0.30)

    # --- cotes ------------------------------------------------------------
    D.cote_h(sc, 0, L1, ep + 20.0, "2,00 m")
    D.cote_h(sc, L1, L1 + L2, ep + 20.0, "1,20 m")
    D.cote_v(sc, 0, ep, -40.0, "20")

    sc.leader("4 HA 10 filants — nappe inférieure", 60, -32, 60.0, 4.0,
              fontsize=1.9)
    sc.leader("Chapeau sur appui + nappe sup. de console", 250, 46,
              L1 + 20.0, ep - 4.0, fontsize=1.9)
    sc.leader("Scellement façade 25 cm", 40, 44, -14.0, 6.0, fontsize=1.9)
    sc.leader("Joint de dilatation 20 mm", 20, 34, 0.0, -0.5, fontsize=1.9)
    return sc


# ---------------------------------------------------------------------------
# Cadre D — tableau des aciers
# ---------------------------------------------------------------------------

def tableau_aciers(pb, x, y):
    p = RES["extension"]["poutre"]
    rows = [
        ("P1", "4 HA 20", "7,80", "2 lits", "12,57", "nappe basse poutre"),
        ("P2", "2 HA 12", "7,80", "1 lit", "2,26", "montage / chapeau"),
        ("P3", "4 HA 12", "7,80", "1 lit", "4,52", "peau poutre"),
        ("P4", "HA 8", "1,90", "46 u.", "—", "étriers e = 175"),
        ("C1", "6 HA 8", "3,60", "1 jeu", "3,02", "poteau 25 x 25"),
        ("C2", "HA 8", "1,06", "17 u.", "—", "cadres e = 200"),
        ("D1", "4 HA 10", "3,45", "2 lits", "3,14", "nappe inf. dalle"),
        ("D2", "4 HA 10", "2,10", "2 lits", "3,14", "chapeau / console"),
        ("D3", "HA 8", "1,00", "—", "—", "agrafes dalle"),
        ("V1", "4 HA 12", "5,40", "2 faces", "9,04", "voile mitoyen"),
        ("V2", "HA 8", "0,80", "—", "—", "répartition e = 250"),
    ]
    pb.tableau(x, y, "NOMENCLATURE DES ACIERS — B500B", [
        "Rep.", "Désignation", "Long. (m)", "Qté", "As (cm²)", "Emploi"],
        rows, [13, 26, 22, 16, 20, 62], size=2.15, hrow=5.6, hline=4.4)
    return y - 5.6 - 4.4 * len(rows)


def tableau_contraintes(pb, x, y):
    p = RES["extension"]["poutre"]
    rows = [
        ("M_Ed", "262,6 kN·m", "µ = 0,1366"),
        ("V_Ed", "130,8 kN", "V_Rd,max = 753,3 kN"),
        ("As requis", "10,52 cm²", "As mis 12,57 cm²"),
        ("Étriers", "s = 186 mm", "retenu e = 175 mm"),
        ("Flèche LT", "17,6 mm", "L/458 + contre-flèche 20"),
    ]
    pb.tableau(x, y, "VÉRIFICATIONS EC2 (DOC-03)", ["Grandeur", "Valeur",
                "Critère"], rows, [30, 32, 52], size=2.15, hrow=5.6,
               hline=4.4)
    return y - 5.6 - 4.4 * len(rows)


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
CARTOUCHE2["sous_titre"] = "Dalle terrasse, poteau BA et nomenclature des aciers"
CARTOUCHE2["echelle"] = "Échelles : 1/20 et 1/10"


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
    """Détail de façonnage : étrier, recouvrement 40 Ø, ancrage à 90°."""
    sc = E.Scene()

    # --- 1. étrier HA 8 (24 x 61) ----------------------------------------
    D.etrier(sc, 0, 0, 24.0, 61.0, lw=0.40, retour=8.0)
    D.cote_h(sc, 0, 24.0, -8.0, "24")
    D.cote_v(sc, 0, 61.0, -8.0, "61")
    sc.leader("Étrier HA 8 — 24 x 61\nretours d'angle 10 Ø = 8 cm",
              34, 66, 24.0, 58.0, fontsize=2.0)

    # --- 2. recouvrement de deux HA 20 (40 Ø = 80 cm) --------------------
    y = 120.0
    D.barre(sc, [(0, y), (86, y)], "HA 20", lw=0.45)
    D.barre(sc, [(74, y + 9), (160, y + 9)], "HA 20", lw=0.45)
    sc.line(74, y - 4, 74, y + 13, "STR_COTATIONS_TEXTES", 0.18)
    sc.line(86, y - 4, 86, y + 13, "STR_COTATIONS_TEXTES", 0.18)
    D.cote_h(sc, 74, 86, y - 9, "40 Ø = 80")
    sc.leader("Recouvrement des armatures\nde reprise : 40 Ø mini",
              40, y + 34, 80.0, y + 9, fontsize=2.0)

    # --- 3. ancrage à 90° dans l'appui -----------------------------------
    y2 = 62.0
    D.barre(sc, [(0, y2), (52, y2), (52, y2 - 16)], lw=0.45)
    D.cote_h(sc, 0, 52, y2 - 28, "40 Ø = 80")
    sc.leader("Ancrage à 90° dans l'appui\nlongueur droite = 40 Ø",
              64, y2 + 12, 40.0, y2 + 2, fontsize=2.0)
    return sc


def schema_principe() -> E.Scene:
    """Schéma de principe (sans échelle) : répartition des étriers."""
    sc = E.Scene()
    L, h = 290.0, 34.0
    sc.rect(0, 0, L, h, "STR_COFFRAGE_BA", 0.45, fill=True)
    # appuis
    for x in (0.0, L - 20.0):
        sc.rect(x - 20.0 if x else -20.0, -18.0, 20.0, 18.0,
                "STR_COFFRAGE_BA", 0.35, hatch="ANSI31", spacing=1.6)
    # étriers resserrés aux appuis
    x = 6.0
    while x < L - 4:
        resserre = (x < 60.0) or (x > L - 60.0)
        sc.line(x, 3.0, x, h - 3.0, "STR_FERRAILLAGE",
                0.35 if resserre else 0.20)
        x += 4.0 if resserre else 11.0
    # zones
    for x1, x2 in ((0.0, 60.0), (L - 60.0, L)):
        sc.line(x1, h + 8, x2, h + 8, "STR_COTATIONS_TEXTES", 0.18)
        sc.text("e = 100", (x1 + x2) / 2.0, h + 10, 2.1, align="center")
    sc.line(60.0, h + 8, L - 60.0, h + 8, "STR_COTATIONS_TEXTES", 0.18)
    sc.text("e = 175", L / 2.0, h + 10, 2.1, align="center")
    sc.text("ZONE D'ABOUT (1,5 h)  —  ZONE COURANTE  —  ZONE D'ABOUT",
            L / 2.0, -26, 2.0, align="center")
    return sc


def page1(pb):
    scA, scB, scS = cadre_poutre(), cadre_poutre_appui(), schema_principe()


    pb.frame(14, 158, 152, 104)
    placer(pb, scA, 14, 158, 152, 104, 10.0)
    pb.vtitle(14, 264.5, "A — COUPE A-A EN TRAVÉE — 1/10")

    pb.frame(176, 158, 152, 104)
    placer(pb, scB, 176, 158, 152, 104, 10.0)
    pb.vtitle(176, 264.5, "B — COUPE B-B SUR APPUI — 1/10")

    pb.frame(14, 74, 300, 74)
    placer(pb, scS, 14, 74, 300, 74, 14.0)
    pb.vtitle(14, 150.5, "H — SCHÉMA DE PRINCIPE DES ÉTRIERS (SANS ÉCHELLE)")

    pb.note_block(322, 144, "REPÈRES D'ARMATURES", [
        "1 — 4 HA 20 nappe basse (2 lits), ancrage 40 Ø.",
        "2 — 2 HA 12 de montage en chapeau.",
        "3 — 4 HA 12 de peau.",
        "4 — Étriers HA 8 : e = 100 aux appuis,",
        "     e = 175 en zone courante.",
        "5 — Attentes poteau HA 8 ancrées 40 Ø.",
    ], width=66)


def page2(pb):
    scC, scP, scG = cadre_poteau(), cadre_dalle(), cadre_ancrage()


    pb.frame(14, 132, 66, 144)
    placer(pb, scC, 14, 132, 66, 144, 10.0)
    pb.vtitle(14, 281, "C — POTEAU — 1/10")

    pb.frame(88, 132, 190, 122)
    placer(pb, scP, 88, 132, 190, 122, 20.0)
    pb.vtitle(88, 281, "D — DALLE TERRASSE — 1/20")

    pb.frame(286, 132, 118, 144)
    placer(pb, scG, 286, 132, 118, 144, 20.0)
    pb.vtitle(286, 281, "G — FAÇONNAGE ET ANCRAGES — 1/20")

    tableau_aciers(pb, 14, 126)
    tableau_contraintes(pb, 180, 126)
    pb.note_block(296, 126, "TOLÉRANCES", [
        "1. Armatures : ± 10 mm (± 5 mm sur enrobage).",
        "2. Étriers : écartement ± 15 mm, max 200 mm.",
        "3. Fond de coffrage : 5 mm sous règle de 2 m.",
        "4. Façonnage NF A 35-027 ; ancrages 40 Ø.",
        "5. Contre-flèche 20 mm sur la poutre-acrotère.",
    ], width=108)

    pb.note_block(180, 96, "MISE EN ŒUVRE", [
        "1. Aciers B500B, façonnage NF A 35-027.",
        "2. Enrobage 30 mm (XC4) — cales / 80 cm.",
        "3. Recouvrements attentes poteau/puits 40 Ø.",
        "4. Contre-flèche 20 mm poutre-acrotère.",
        "5. Pas de substitution de diamètre sans BET.",
    ], width=104)

    pb.note_block(296, 96, "CONTRÔLES", [
        "1. PV de conformité acier (NF A 35-080-1).",
        "2. Contrôle des enrobages avant coulage.",
        "3. Affaissement C25/30 : classe S3.",
        "4. PV de résistance à 28 j avant décoffrage.",
    ], width=108)


def cadre_elevation_poutre() -> E.Scene:
    """Élévation de la poutre : étriers, nappes et zones d'effort tranchant."""
    sc = E.Scene()
    L, h = 803.0, 67.0
    # contour
    sc.rect(0, 0, L, h, "STR_COFFRAGE_BA", 0.40)
    # appuis aux extrémités
    sc.rect(-25.0, -40.0, 25.0, -40.0 + 0 if False else 40.0, "STR_EXISTANT",
            0.35)
    sc.rect(L, -40.0, 25.0, 40.0, "STR_COFFRAGE_BA", 0.40)
    # étriers : resserrés sur 1,5 h = 100 cm aux appuis, puis 17,5 cm
    x = 10.0
    while x < L - 5:
        sc.line(x, 4.0, x, h - 4.0, "STR_FERRAILLAGE", 0.22)
        pas = 10.0 if (x < 110.0 or x > L - 110.0) else 17.5
        x += pas
    # nappe basse
    sc.line(-22.0, 4.0, L + 22.0, 4.0, "STR_FERRAILLAGE", 0.45)
    sc.line(-15.0, 9.0, L + 15.0, 9.0, "STR_FERRAILLAGE", 0.45)
    # cotes
    D.cote_h(sc, 0, 100.0, -18.0, "1,00 m")
    D.cote_h(sc, 100.0, L - 100.0, -18.0, "6,03 m")
    D.cote_h(sc, L - 100.0, L, -18.0, "1,00 m")
    D.cote_h(sc, 0, L, -30.0, "8,03 m")
    D.cote_v(sc, 0, h, -46.0, "67")
    # repères
    D.bulle(sc, 40.0, h * 0.55, "3", r=9.0, fs=2.6)
    sc.leader("Zone d'effort tranchant : étriers HA 8 e = 100",
              60, -46, 80.0, 4.0, fontsize=2.0)
    sc.leader("Zone courante : étriers HA 8 e = 175", 330, 96, 400.0, h - 4.0,
              fontsize=2.0)
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
             "Coupe en travée, coupe sur appui et schéma de principe des "
             "étriers — béton C25/30, acier B500B")
    page1(pb)
    pb.add_page(CARTOUCHE2)
    pb.titre("PL-04/2 — FERRAILLAGE : POTEAU, DALLE ET FAÇONNAGE",
             "Poteau BA 25 x 25 (1/10), dalle terrasse 20 cm (1/20) et "
             "façonnage des armatures (1/20)")
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
