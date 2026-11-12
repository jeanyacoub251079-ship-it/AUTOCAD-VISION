"""
PL-02 — Plan de coffrage de l'extension (terrasse accessible).

Échelle 1/50. Schéma retenu (arbitrage E-02 du 11/11/2026) :

    * terrasse 8,03 m x 2,00 m, poutre-acrotère de rive comprise ;
    * poutre-acrotère **isostatique** de 8,03 m en limite de dalle ;
    * **voile BA de rive à créer** sur **semelle filante à créer**, en
      limite de propriété, dans le prolongement du mur pignon ;
    * **poutre-acrotère perpendiculaire** à la façade, appuyée sur le
      **poteau BA à 1,30 m** et se poursuivant en **console de 0,70 m** ;
    * la poutre de 8,03 m repose sur l'extrémité de cette console.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "00_SOURCES"))

import plan_engine as E          # noqa: E402
import niveaux_retenus as NIV    # noqa: E402

OUT = os.path.join(HERE, "plans")

# Emprise (cm). y = 0 au nu de la façade existante, y croissant vers le
# jardin ; x = 0 au nu gauche du pignon, x = L au voile de rive.
L = NIV.L_EXTENSION * 100.0          # 803 cm
P = NIV.LARGEUR_TERRASSE * 100.0     # 200 cm
EP_FAC = 49.0                        # mur de façade existant (meulière)
EP_VOILE = NIV.EP_VOILE * 100.0      # 20 cm — voile de rive à créer
POS_POT = NIV.POS_POTEAU_FAÇADE * 100.0   # 130 cm
POT = 25.0
B_POUTRE = NIV.B_POUTRE * 100.0      # 30 cm
B_PERP = 25.0                        # poutre perpendiculaire 25 cm
CONSOLE = NIV.PORTE_A_FAUX * 100.0   # 70 cm
D1_PUITS = 135.0                     # Ø puits sous le poteau
SEMELLE_B = 65.0                     # largeur semelle filante
SEMELLE_H = 30.0

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-02 — PLAN DE COFFRAGE DE L'EXTENSION",
    "sous_titre": "Voile de rive sur semelle filante, poutre-acrotère "
                  "isostatique, console et poteau BA",
    "repere": "PL-02",
    "phase": "Tâche 3 — plans généraux",
    "indice": "Indice B — 11/11/2026",
    "date": "Échelle 1/50",
}


def build_scene() -> E.Scene:
    """x = 0 au nu du pignon (console), x = L au voile de rive (à créer).
    y = 0 au nu de la façade existante, y = P au nu extérieur de la
    poutre-acrotère (limite de dalle)."""
    sc = E.Scene()
    y_poutre = P - B_POUTRE              # nu intérieur de la poutre : 170
    y_axe = P - B_POUTRE / 2.0           # axe de la poutre : 185

    # ---- 1. Mur de façade existant (meulière) ---------------------------
    sc.rect(0, -EP_FAC, L, EP_FAC, "STR_EXISTANT", lw=0.35)
    for i in range(int(L / 16)):
        sc.line(i * 16, -EP_FAC, i * 16 + 7.0, 0, "STR_EXISTANT", lw=0.13)

    # ---- 2. Emprise de la terrasse ---------------------------------------
    sc.rect(0, 0, L, P, "STR_COFFRAGE_BA", lw=0.50, fill=True)

    # ---- 3. Voile de rive à créer (limite de propriété) ------------------
    sc.rect(L, 0, EP_VOILE, P, "STR_COFFRAGE_BA", lw=0.50,
            hatch="ANSI31", angle=45.0, spacing=2.0)
    # semelle filante sous le voile (hors emprise, en pointillé long)
    sc.rect(L - (SEMELLE_B - EP_VOILE) / 2.0, -SEMELLE_H, SEMELLE_B,
            SEMELLE_H, "STR_COFFRAGE_BA", lw=0.35)
    sc.line(L - (SEMELLE_B - EP_VOILE) / 2.0, -SEMELLE_H,
            L - (SEMELLE_B - EP_VOILE) / 2.0 + SEMELLE_B, -SEMELLE_H,
            "STR_COFFRAGE_BA", lw=0.50)

    # ---- 4. Poutre-acrotère isostatique de 8,03 m ------------------------
    sc.rect(0, y_poutre, L, B_POUTRE, "STR_COFFRAGE_BA", lw=0.50,
            hatch="ANSI31", angle=45.0, spacing=2.0)

    # ---- 5. Poutre-acrotère perpendiculaire + console --------------------
    # Elle court de la façade (y = 0) jusqu'au nu extérieur (y = P), et
    # s'appuie sur le poteau à y = POS_POT.
    sc.rect(0, 0, B_PERP, P, "STR_COFFRAGE_BA", lw=0.50,
            hatch="ANSI31", angle=45.0, spacing=2.0)

    # ---- 6. Poteau BA 25 × 25 à 1,30 m ----------------------------------
    sc.rect(B_PERP / 2.0 - POT / 2.0, POS_POT - POT / 2.0, POT, POT,
            "STR_COFFRAGE_BA", lw=0.50, hatch="ANSI37", angle=0.0,
            spacing=1.2)

    # ---- 7. Puits de gros béton sous le poteau --------------------------
    sc.circle(B_PERP / 2.0, POS_POT, D1_PUITS / 2.0, "STR_COFFRAGE_BA",
              lw=0.50)
    for i in (-1, 0, 1):
        sc.line(B_PERP / 2.0 - D1_PUITS / 2.0, POS_POT + i * 30,
                B_PERP / 2.0 + D1_PUITS / 2.0, POS_POT + i * 30 + 24,
                "STR_COFFRAGE_BA", lw=0.13)

    # ---- 8. Appuis de la poutre de 8,03 m -------------------------------
    # appui droit : le voile (matérialisé par un triangle)
    for (ax, ay, dx) in ((L, y_axe, -1), (0.0, y_axe, 1)):
        sc.poly([(ax, ay - 9), (ax + dx * 26, ay), (ax, ay + 9)],
                "STR_COTATIONS_TEXTES", 0.25, closed=True)
        sc.hatch_poly([(ax, ay - 9), (ax + dx * 26, ay), (ax, ay + 9)],
                      "STR_COTATIONS_TEXTES", 45.0, 1.4)

    # ---- 9. Verrière frontale (hors mission) ----------------------------
    sc.line(-30, P + 34, L + EP_VOILE + 20, P + 34, "STR_COTATIONS_TEXTES",
            lw=0.25)
    sc.text("VERRIÈRE FRONTALE (HORS MISSION)", 150, P + 60, 1.9,
            align="left")

    # ---- 10. Cotation ----------------------------------------------------
    sc.dim_h(0, L, P + 48, "8,03 m")
    sc.dim_h(L, L + EP_VOILE, P + 22, "20")
    # cotes de largeur à gauche
    sc.dim_v(0, POS_POT, -78, "1,30 m")
    sc.dim_v(POS_POT, P, -78, "0,70 m")
    sc.dim_v(0, P, -112, "2,00 m")
    # cote du poteau et du puits
    sc.dim_h(B_PERP / 2.0 - POT / 2.0, B_PERP / 2.0 + POT / 2.0,
             POS_POT + 40, "25")

    # ---- 11. Repérage ----------------------------------------------------
    repere = [
        ("A", 430, y_axe, 430, P + 96,
         "Poutre-acrotère isostatique 30 × 67 — arase 44,75"),
        ("B", 700, y_axe, 700, P + 66,
         "Poutre perpendiculaire 25 × 67 — 1,30 m + console 0,70 m"),
        ("C", B_PERP / 2.0, POS_POT, 150, P + 126,
         "Poteau BA 25 × 25 à 1,30 m de la façade"),
        ("D", L + EP_VOILE / 2.0, 170, L + 30, 120,
         "Voile de rive À CRÉER — ép. 20"),
        ("E", L, -16, L + 60, -30,
         "Semelle filante À CRÉER — 65 × 30"),
        ("F", B_PERP / 2.0, POS_POT - 6, 150, POS_POT - 46,
         "Puits Ø 1,35 en gros béton"),
    ]
    sc.text("DALLE BA TERRASSE ép. 20 cm — 8,03 × 2,00 m", 380, 60, 2.3,
            align="center", bold=True)
    for tag, x, y, tx, ty, lib in repere:
        sc.circle(x, y, 13, "STR_COTATIONS_TEXTES", lw=0.25)
        sc.text(tag, x, y - 2.2, 2.5, align="center", bold=True)
        sc.leader(f"{tag} — {lib}", tx, ty, x, y, fontsize=2.1)

    return sc


def main():
    os.makedirs(OUT, exist_ok=True)
    sc = build_scene()

    dxf = E.DxfBackend("PL-02")
    dxf.render(sc)
    p_dxf = dxf.save(os.path.join(OUT, "PL-02_Coffrage_Extension.dxf"))

    pb = E.PdfBackend("PL-02", CARTOUCHE)
    pb.new_page()
    pb.titre("PL-02 — PLAN DE COFFRAGE DE L'EXTENSION",
             "Terrasse 8,03 × 2,00 m — voile de rive sur semelle filante, "
             "poutre-acrotère isostatique, console 0,70 m — 1/50")
    pb.k = 10.0 / 50.0
    pb.set_origin(56.0, 128.0)
    pb.render(sc)

    pb.legende(272, 268, [
        ("STR_EXISTANT", "Maçonnerie existante conservée", "line"),
        ("STR_COFFRAGE_BA", "Béton armé à créer (coffrage)", "hatch"),
        ("STR_COTATIONS_TEXTES", "Cotes, repères, axes", "line"),
    ])
    pb.tableau(272, 244, "REPÉRAGE",
               ["Rep.", "Désignation", "Section"],
               [["A", "Poutre-acrotère isostatique", "30 × 67"],
                ["B", "Poutre-acrotère perpendiculaire", "25 × 67"],
                ["C", "Poteau BA", "25 × 25"],
                ["D", "Voile de rive (à créer)", "ép. 20"],
                ["E", "Semelle filante (à créer)", "65 × 30"],
                ["F", "Puits de gros béton", "Ø 135"],
                ["G", "Dalle terrasse", "ép. 20"]],
               [10, 58, 26])
    pb.tableau(272, 196, "NIVEAUX NGF",
               ["Repère", "Altitude"],
               [["Terrain / sol RDC", "41,11 / 41,46"],
                ["Arase fondations", "39,02"],
                ["Sous-face poutre-acrotère", "44,08"],
                ["Arase acrotère", "44,75"],
                ["Tête verrière", "45,90"]],
               [58, 30])

    pb.note_block(272, 150, "NOTES", [
        "1. Cotes en cm ; niveaux en m NGF (DOC-03 §1).",
        "2. Poutre 8,03 m isostatique : 4 HA 14 + étriers HA 8",
        "   e = 300 ; contre-flèche de coffrage 20 mm.",
        "3. Poutre perpendiculaire : 2 HA 12 + étriers HA 8 ;",
        "   console de 0,70 m reprise par la nappe supérieure.",
        "4. Poteau 25 × 25 : 6 HA 8, cadres HA 8 e = 200.",
        "5. Voile de rive À CRÉER : 4 HA 12 par face + HA 8 e = 250,",
        "   sur semelle filante 65 × 30 à NGF 39,02.",
        "6. Joint de dilatation 20 mm entre extension et façade.",
    ], width=134)

    p_pdf = os.path.join(OUT, "PL-02_Coffrage_Extension.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


if __name__ == "__main__":
    main()
