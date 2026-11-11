"""
PL-01 — Plan de reprise en sous-œuvre RDC (existant + démolitions + appuis).

Génère le .dxf et le .pdf depuis la même scène (plan_engine).

Convention de repère : les coordonnées modèle sont celles du DXF AARKA
(centimètres, Y négatif). La scène est ensuite translatée dans un repère
local (origine = angle bas-gauche de l'emprise) pour la mise en page.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "00_SOURCES"))

import plan_engine as E          # noqa: E402

OUT = os.path.join(HERE, "plans")
FOND = json.load(open(os.path.join(HERE, "..", "00_SOURCES", "rdc_plan.json"),
                      encoding="utf-8"))

# Origine du repère local = angle bas-gauche de l'emprise relevée
OX, OY = 7869, -10510

# Repères D1..D6 : (repère, x, y, portée, épaisseur, libellé, profilé)
REPERES = [
    ("D1", 8093, -10088, 260, 16, "Refend entrée / bureau", "IPE 160"),
    ("D2", 8484, -10483, 380, 47, "Façade avant — salon", "IPE 270"),
    ("D3", 8693, -10277, 355, 57, "Refend central longitudinal", "IPE 300"),
    ("D4", 8889, -10482, 200, 49, "Façade avant — salle à manger", "IPE 180"),
    ("D5", 8875, -10088, 308, 16, "Refend transversal salle à manger", "IPE 180"),
    ("D6", 8876, -9799, 154, 46, "Façade arrière — cuisine", "IPE 160"),
]

# Trappes à linge (H-16) : abscisse DXF relevée, ouverture 30 × 31 cm
TRAPPES = [("Combles", 46491), ("R+1", 42890), ("RDC", 48491)]

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-01 — REPRISE EN SOUS-ŒUVRE RDC",
    "sous_titre": "Existant, démolitions D1 à D6, appuis BA et profilés",
    "repere": "PL-01",
    "phase": "Tâche 3 — plans généraux",
    "indice": "Indice A — 11/11/2026",
    "date": "Échelle 1/50",
}

# Emprise locale (cm) : largeur 1246, hauteur 840
W, H = 1246, 840


def lx(x):
    return x - OX


def ly(y):
    return y - OY


def _nuage(sc: E.Scene, x, y, w, h, rayon=6.0):
    """Nuage de révision : suite de petits arcs le long d'un rectangle."""
    def rangee(xa, ya, xb, yb):
        L = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
        n = max(2, int(L / (rayon * 1.6)))
        ux, uy = (xb - xa) / L, (yb - ya) / L
        nx, ny = -uy, ux
        for i in range(n):
            t0, t1 = i * L / n, (i + 1) * L / n
            cxm = xa + ux * (t0 + t1) / 2
            cym = ya + uy * (t0 + t1) / 2
            r = (t1 - t0) / 2
            # demi-cercle bombé vers l'extérieur
            sc.arc(cxm + nx * 0.0, cym + ny * 0.0, r,
                   0, 180, "STR_COTATIONS_TEXTES", lw=0.20)
    # quatre côtés, bombés vers l'extérieur
    rangee(x, y, x + w, y)
    rangee(x, y + h, x + w, y + h)
    rangee(x, y, x, y + h)
    rangee(x + w, y, x + w, y + h)


def build_scene() -> E.Scene:
    sc = E.Scene()

    # ---- 1. Existant conservé (fond DXF AARKA filtré) -------------------
    for x1, y1, x2, y2, lay in FOND["lines"]:
        if lay in ("ARK-MURS", "ARK-CLOIS"):
            sc.line(lx(x1), ly(y1), lx(x2), ly(y2), "STR_EXISTANT",
                    lw=0.35 if lay == "ARK-MURS" else 0.18)
    for pts, lay, closed in FOND["polys"]:
        if lay in ("ARK-MURS", "ARK-CLOIS"):
            sc.poly([(lx(a), ly(b)) for a, b in pts], "STR_EXISTANT",
                    lw=0.35 if lay == "ARK-MURS" else 0.18, closed=closed)
    for x1, y1, x2, y2, lay in FOND["lines"]:
        if lay == "ARK-VITRE":
            sc.line(lx(x1), ly(y1), lx(x2), ly(y2), "STR_EXISTANT", lw=0.13)
    for pts, lay, closed in FOND["polys"]:
        if lay == "ARK-VITRE":
            sc.poly([(lx(a), ly(b)) for a, b in pts], "STR_EXISTANT",
                    lw=0.13, closed=closed)

    # ---- 2. Démolitions : ouvertures D1 à D6 ---------------------------
    for tag, x, y, L, ep, lib, prof in REPERES:
        sc.rect(lx(x - L / 2), ly(y - ep / 2), L, ep, "STR_DEMOLITION",
                lw=0.25)

    # ---- 3. Appuis BA ---------------------------------------------------
    for tag, x, y, L, ep, lib, prof in REPERES:
        if tag in ("D2", "D4", "D6"):
            jb = 50 if tag != "D6" else 45
            for sx in (x - L / 2 - 25, x + L / 2):
                sc.rect(lx(sx), ly(y - jb / 2), 25, jb, "STR_COFFRAGE_BA",
                        lw=0.50, fill=True)
            sc.rect(lx(x - L / 2 - 25), ly(y - ep / 2), L + 50, ep,
                    "STR_COFFRAGE_BA", lw=0.50)

    # poteau BA D3/D5 au croisement
    px, py = 8693 + 355 / 2, -10277 + 57 / 2
    sc.rect(lx(px - 12.5), ly(py - 5), 25, 40, "STR_COFFRAGE_BA", lw=0.50,
            fill=True)

    # ---- 4. Profilés métalliques ---------------------------------------
    for tag, x, y, L, ep, lib, prof in REPERES:
        sc.rect(lx(x - L / 2), ly(y - 3.5), L, 7, "STR_ACIER_PROFILS",
                lw=0.50)

    # ---- 5. Repérage des six ouvertures ---------------------------------
    for tag, x, y, L, ep, lib, prof in REPERES:
        cx, cy = lx(x), ly(y)
        sc.circle(cx, cy, 17, "STR_COTATIONS_TEXTES", lw=0.25)
        sc.text(tag, cx, cy - 2.6, 3.0, align="center", bold=True)
        sc.line(cx + 12, cy + 12, cx + 30, cy + 34, "STR_COTATIONS_TEXTES",
                lw=0.18)

    # poteau BA D3/D5
    sc.circle(lx(px + 12.5), ly(py + 20), 22, "STR_COTATIONS_TEXTES", lw=0.25)
    sc.text("P", lx(px + 12.5), ly(py + 20) - 3.2, 3.2, align="center",
            bold=True)

    # ---- 6. Cotation générale ------------------------------------------
    sc.dim_h(0, lx(8484), H + 46, "6,15 m")
    sc.dim_h(lx(8484), W, H + 46, "6,31 m")
    sc.dim_h(0, W, H + 92, "12,46 m")
    sc.dim_v(0, H, -55, "8,40 m")

    # ---- 7. Axes --------------------------------------------------------
    for lab, x in (("01", 0), ("02", lx(8484)), ("03", W)):
        sc.line(x, -35, x, 0, "STR_COTATIONS_TEXTES", lw=0.13)
        sc.circle(x, 22, 8, "STR_COTATIONS_TEXTES", lw=0.18)
        sc.text(lab, x, 22, 2.2, align="center", bold=True)

    return sc


def main():
    os.makedirs(OUT, exist_ok=True)
    sc = build_scene()

    dxf = E.DxfBackend("PL-01")
    dxf.render(sc)
    p_dxf = dxf.save(os.path.join(OUT, "PL-01_Reprise_Sous_Oeuvre_RDC.dxf"))

    pb = E.PdfBackend("PL-01", CARTOUCHE)
    pb.new_page()
    pb.titre("PL-01 — REPRISE EN SOUS-ŒUVRE RDC",
             "Existant conservé, démolitions D1 à D6, appuis BA et profilés "
             "S355 — échelle 1/50")
    k = 10.0 / E.ECHELLE
    pb.set_origin(40.0, 62.0)
    pb.render(sc)

    # Trappes à linge (H-16) : renvoi + nuage, à droite du plan
    c = pb._c
    bx = 305.0
    c.setFont("Helvetica-Bold", 2.9)
    c.setFillColor(pb.Color(0, 0, 0))
    c.drawString(bx, 208.0, "TRAPPES À LINGE (H-16)")
    c.setFont("Helvetica", 2.2)
    c.drawString(bx, 204.0, "Position estimée depuis les plans ; chaque")
    c.drawString(bx, 200.4, "trappe est entourée d'un nuage de révision.")
    for i, (niv, xn) in enumerate(TRAPPES):
        ey = 190.0 - i * 14.0
        sc2 = E.Scene()
        _nuage(sc2, bx + 2, ey - 8, 10, 10, rayon=2.0)
        sc2.rect(bx + 2, ey - 8, 10, 10, "STR_COTATIONS_TEXTES", lw=0.25)
        _o, _k = pb.x0, pb.k
        pb.set_origin(0.0, 0.0)
        pb.k = 1.0
        pb.render(sc2)
        pb.x0, pb.k = _o, _k
        c.setFillColor(pb.Color(0, 0, 0))
        c.setFont("Helvetica-Bold", 2.4)
        c.drawString(bx + 18, ey - 2.0, f"{niv} — 30 × 31 cm")
        c.setFont("Helvetica", 2.2)
        c.drawString(bx + 18, ey - 5.6, f"x ≈ {xn} (relevé DXF)")

    pb.legende(bx, 146.0, [
        ("STR_EXISTANT", "Existant conservé", "line"),
        ("STR_DEMOLITION", "Maçonnerie démolie (D1 à D6)", "dashed"),
        ("STR_COFFRAGE_BA", "Béton armé coulé en place", "hatch"),
        ("STR_ACIER_PROFILS", "Profilé métallique S355 jumelé", "line"),
        ("STR_COTATIONS_TEXTES", "Cotes, axes, nuage de révision", "line"),
    ])
    pb.tableau(bx, 112.0, "REPRISES EN SOUS-ŒUVRE D1 À D6",
               ["Rep.", "Portée", "Mur", "Profilé"],
               [["D1", "2,60 m", "16 cm", "IPE 160"],
                ["D2", "3,80 m", "47 cm", "IPE 270"],
                ["D3", "3,55 m", "57 cm", "IPE 300"],
                ["D4", "2,00 m", "49 cm", "IPE 180"],
                ["D5", "3,08 m", "16 cm", "IPE 180"],
                ["D6", "1,54 m", "46 cm", "IPE 160"]],
               [10, 20, 16, 24])
    pb.note_block(18.0, 52.0, "NOTES", [
        "1. Cotes en cm ; niveaux en m NGF (sol RDC 41,46).",
        "2. Reprises D1 à D6 : profilés S355, matés au mortier sans",
        "   retrait (contact ≥ 90 %). Jambages et sommiers BA C25/30.",
        "3. Trappes à linge : position estimée (H-16), entourée d'un",
        "   nuage de révision — ajustement après relevé de l'entraxe",
        "   réel des solives, dans la zone de tolérance DOC-02 §6.2.",
        "4. D1 : fondation filante meulière continue conservée (H-01).",
        "5. Aucune démolition avant PV de résistance BA à 28 jours.",
    ], width=152)

    p_pdf = os.path.join(OUT, "PL-01_Reprise_Sous_Oeuvre_RDC.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


if __name__ == "__main__":
    main()
