"""
PL-02 — Plan de coffrage de l'extension (terrasse accessible).

Échelle 1/50. Décrit le voile mitoyen, le poteau BA à 2,00 m, la
poutre-acrotère 30 × 67, les puits de gros béton, les longrines et la
dalle de terrasse (travée 2,00 m + porte-à-faux 1,20 m).
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

# Emprise de l'extension (cm). Origine locale en bas à gauche.
L = 803.0            # largeur façade
P = 320.0            # profondeur
EP_FAC = 49.0        # mur de façade existant (meulière)
EP_VOILE = 20.0      # voile mitoyen BA
POS_POT = 200.0      # axe du poteau, depuis le nu de façade
POT = 25.0
B_POUTRE = 30.0      # poutre-acrotère 30 x 67
D1_PUITS = 205.0     # Ø puits n° 1
D2_PUITS = 220.0     # Ø puits n° 2

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-02 — PLAN DE COFFRAGE DE L'EXTENSION",
    "sous_titre": "Voile mitoyen, poteau BA, poutre-acrotère 30 × 67, "
                  "puits et dalle de terrasse",
    "repere": "PL-02",
    "phase": "Tâche 3 — plans généraux",
    "indice": "Indice A — 11/11/2026",
    "date": "Échelle 1/50",
}


def build_scene() -> E.Scene:
    """Repère local : x = 0 au nu gauche de l'extension, y = 0 à la verrière,
    y = P au nu de la façade existante. La poutre-acrotère est à 2,00 m du
    nu de façade, soit y = P - 200 = 120 cm."""
    sc = E.Scene()
    YP = P - POS_POT          # 120 cm : axe de la poutre-acrotère

    # ---- 1. Mur de façade existant (meulière) ---------------------------
    sc.rect(0, P, L, EP_FAC, "STR_EXISTANT", lw=0.35)
    for i in range(int(L / 14)):
        sc.line(i * 14, P, i * 14 + EP_FAC * 0.45, P + EP_FAC,
                "STR_EXISTANT", lw=0.13)

    # ---- 2. Emprise de la dalle de terrasse -----------------------------
    sc.rect(0, 0, L, P, "STR_COTATIONS_TEXTES", lw=0.18)

    # ---- 3. Voile mitoyen BA ép. 20 --------------------------------------
    sc.rect(L, 0, EP_VOILE, P, "STR_COFFRAGE_BA", lw=0.50, fill=True)

    # ---- 4. Poutre-acrotère 30 × 67 --------------------------------------
    sc.rect(0, YP - B_POUTRE / 2, L, B_POUTRE, "STR_COFFRAGE_BA", lw=0.50,
            fill=True)

    # ---- 5. Poteau BA 25 × 25 sous la poutre -----------------------------
    sc.rect(POS_POT - POT / 2, YP - POT / 2, POT, POT, "STR_COFFRAGE_BA",
            lw=0.50, fill=True)

    # ---- 6. Puits de gros béton (sous les appuis) ------------------------
    for cx, d in ((POS_POT, D1_PUITS), (L + EP_VOILE / 2, D2_PUITS)):
        sc.circle(cx, YP, d / 2, "STR_COFFRAGE_BA", lw=0.50)
        for i in range(-2, 3):
            sc.line(cx + i * 30, YP - d / 4, cx - i * 30, YP + d / 4,
                    "STR_COFFRAGE_BA", lw=0.13)

    # ---- 7. Longrine de rive sous la dalle -------------------------------
    sc.rect(0, 0, L, 25, "STR_COFFRAGE_BA", lw=0.35)

    # ---- 8. Verrière frontale (hors mission) -----------------------------
    sc.line(-35, -14, L + EP_VOILE + 35, -14, "STR_COTATIONS_TEXTES", lw=0.25)

    # ---- 9. Cotation ------------------------------------------------------
    sc.dim_h(0, L, -62, "8,03 m")
    sc.dim_h(0, POS_POT, -100, "2,00 m")
    sc.dim_h(POS_POT, L, -100, "6,03 m")
    sc.dim_v(-14, P, -58, "3,20 m")
    sc.dim_v(YP, P, L + EP_VOILE + 52, "2,00 m")
    sc.dim_v(-14, YP, L + EP_VOILE + 52, "1,20 m")

    # ---- 10. Repérage -----------------------------------------------------
    repere = [
        ("A", 470, YP, 470, YP + 92, "Poutre-acrotère BA 30 × 67 — arase 44,75"),
        ("B", POS_POT, YP, 300, YP + 118, "Poteau BA 25 × 25 — axe à 2,00 m"),
        ("C", L + EP_VOILE / 2, 265, L + 78, 268, "Voile mitoyen BA ép. 20"),
        ("D", POS_POT, YP, POS_POT + 78, YP - 128, "Puits n° 1 — Ø 2,05 m"),
        ("E", L + EP_VOILE / 2, YP, L + 120, YP - 52, "Puits n° 2 — Ø 2,20 m"),
    ]
    # dalle : libellé directement dans l'emprise
    sc.text("DALLE BA TERRASSE ép. 20 cm", 470, 58, 2.3, align="center",
            bold=True)
    for tag, x, y, tx, ty, lib in repere:
        sc.circle(x, y, 14, "STR_COTATIONS_TEXTES", lw=0.25)
        sc.text(tag, x, y - 2.4, 2.6, align="center", bold=True)
        sc.leader(f"{tag} — {lib}", tx, ty, x, y, fontsize=2.2)

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
             "Terrasse accessible — voile mitoyen, poteau BA à 2,00 m, "
             "poutre-acrotère 30 × 67, puits et longrines — 1/50")
    pb.set_origin(55.0, 152.0)
    pb.render(sc)

    pb.legende(262, 272, [
        ("STR_EXISTANT", "Maçonnerie existante conservée", "line"),
        ("STR_COFFRAGE_BA", "Béton armé coulé en place (coffrage)", "hatch"),
        ("STR_COTATIONS_TEXTES", "Cotes, repères, axes", "line"),
    ])
    pb.tableau(262, 248, "REPÉRAGE",
               ["Rep.", "Désignation", "Section"],
               [["A", "Poutre-acrotère", "30 × 67"],
                ["B", "Poteau BA verrière", "25 × 25"],
                ["C", "Voile mitoyen", "ép. 20"],
                ["D", "Puits n° 1", "Ø 205"],
                ["E", "Puits n° 2", "Ø 220"],
                ["F", "Dalle terrasse", "ép. 20"]],
               [10, 46, 22])
    pb.tableau(262, 196, "NIVEAUX NGF",
               ["Repère", "Altitude"],
               [["Terrain / sol RDC", "41,11 / 41,46"],
                ["Arase fondations", "39,02"],
                ["Sous-face plancher RDC", "44,08"],
                ["Arase acrotère", "44,75"],
                ["Tête verrière", "45,90"]],
               [52, 26])

    pb.note_block(262, 150, "NOTES", [
        "1. Cotes en cm ; niveaux en m NGF (DOC-03 §1).",
        "2. Poutre-acrotère : 4 HA 20 + étriers HA 8 e = 175,",
        "   contre-flèche de coffrage 20 mm.",
        "3. Poteau 25 × 25 : 6 HA 8, cadres HA 8 e = 200.",
        "4. Puits descendus à NGF 39,02 (assise des fondations",
        "   existantes) — béton C16/20 coulé en pleine fouille.",
        "5. Voile mitoyen : 4 HA 12 par face + HA 8 e = 250.",
        "6. Joint de dilatation 20 mm entre extension et façade.",
    ], width=125)

    p_pdf = os.path.join(OUT, "PL-02_Coffrage_Extension.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


if __name__ == "__main__":
    main()
