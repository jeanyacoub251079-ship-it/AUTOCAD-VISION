"""
PL-03 — Coupes et élévations de l'extension.

Trois cadres sur la planche A3 paysage :
  1. coupe transversale de la terrasse à l'échelle 1/50, avec altimétrie NGF ;
  2. élévation du poteau BA et de la poutre perpendiculaire avec console,
     à l'échelle 1/40 ;
  3. coupe du voile de rive neuf sur semelle filante, à l'échelle 1/60.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "00_SOURCES"))

import plan_engine as E          # noqa: E402
import detail_lib as D           # noqa: E402
import niveaux_retenus as N      # noqa: E402
NIV = N

OUT = os.path.join(HERE, "plans")

CARTOUCHE = {
    "affaire": "Affaire GA-2026-58AIGLE — BET Structure",
    "adresse": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "titre": "PL-03 — COUPES ET ÉLÉVATIONS",
    "sous_titre": "Coupe transversale, élévation du poteau / console et coupe du voile neuf",
    "repere": "PL-03",
    "phase": "Tâche 3 — plans généraux",
    "indice": "Indice A — 11/11/2026",
    "date": "Échelles : 1/40, 1/50 et 1/60",
}

# ---------------------------------------------------------------------------
# Cadre 1 — coupe verticale (unités : cm, x = 0 au nu de façade)
# ---------------------------------------------------------------------------

X_FACADE = 0.0        # nu extérieur de la façade existante
EP_FAC = 49.0
P = NIV.LARGEUR_TERRASSE * 100.0   # largeur de terrasse (200 cm)
Y_POT = NIV.POS_POTEAU_FAÇADE * 100.0   # 130 cm
B_POUTRE = 30.0
H_POUTRE = 67.0

Z = 100.0             # facteur : 1 m NGF = 100 cm dans la scène


def z(ngf):
    """Altitude NGF (m) -> ordonnée scène (cm), sol RDC à 0."""
    return (ngf - N.NGF_SOL_RDC) * Z


def build_coupe() -> E.Scene:
    """Coupe A-A transversale sur la terrasse (arbitrage E-02).

    x = 0   : nu extérieur de la façade existante
    x = 170 : nu intérieur de la poutre-acrotère de rive
    x = 200 : nu extérieur (limite de dalle), axe de la poutre à 1,85 m
    z       : altitude NGF ramenée au sol fini RDC (41,46 -> 0)

    La coupe est prise à mi-longueur de la poutre de 8,03 m : elle ne coupe
    donc ni le poteau (à 1,30 m de la façade, en rive gauche) ni le voile de
    rive (en rive droite). Le poteau et la console sont décrits au cadre B.
    """
    sc = E.Scene()

    y_ph = z(N.NGF_PH_RDC)
    y_pb = z(N.NGF_POUTRE_BAS)
    y_pt = z(N.NGF_POUTRE_HAUT)
    y_fond = z(N.NGF_FONDATION)
    y_ver = z(N.NGF_VERRIERE_HEAD)
    y_terr = z(N.NGF_TERRAIN)
    x_pb = P - B_POUTRE            # 170
    x_pt = P                       # 200

    # ---- 1. Façade existante conservée (coupée au niveau du terrain) ----
    y_bas = y_terr - 4
    sc.rect(-EP_FAC, y_bas, EP_FAC, y_ph - y_bas, "STR_EXISTANT", lw=0.35)
    for i in range(8):
        yy = y_bas + i * 28
        sc.line(-EP_FAC, yy, -EP_FAC + 24, yy + 28, "STR_EXISTANT", lw=0.13)
    sc.line(-EP_FAC, y_bas - 6, -EP_FAC + EP_FAC, y_bas - 6,
            "STR_COTATIONS_TEXTES", lw=0.18)
    sc.rect(-EP_FAC, y_ph - 22, EP_FAC, 22, "STR_EXISTANT", lw=0.25)

    # ---- 2. Dalle de terrasse en console depuis la façade ----------------
    # La dalle (20 cm) porte depuis la façade et s'encastre sur la poutre-
    # acrotère de rive : c'est un porte-à-faux de 1,70 m.
    sc.rect(0, y_ph, x_pb, 20, "STR_COFFRAGE_BA", lw=0.50, fill=True)

    # ---- 3. Poutre-acrotère de rive 30 x 67 ------------------------------
    sc.rect(x_pb, y_pb, B_POUTRE, y_pt - y_pb, "STR_COFFRAGE_BA", lw=0.50,
            fill=True)

    # ---- 4. Garde-corps / acrotère au-dessus de la dalle ----------------
    sc.line(0, y_pt, x_pb, y_pt, "STR_COTATIONS_TEXTES", lw=0.13)
    sc.line(0, y_ph + 20, 0, y_pt, "STR_COTATIONS_TEXTES", lw=0.13)

    # ---- 5. Verrière frontale (hors mission) ----------------------------
    sc.line(x_pt, y_ph, x_pt, y_ver, "STR_COTATIONS_TEXTES", lw=0.30)
    sc.line(x_pt - 55, y_ver, x_pt + 55, y_ver, "STR_COTATIONS_TEXTES", lw=0.18)

    # ---- 6. Sols et terrain ----------------------------------------------
    sc.line(-EP_FAC - 30, y_terr, x_pt + 40, y_terr, "STR_EXISTANT", lw=0.25)
    sc.line(-EP_FAC, 0, x_pt, 0, "STR_EXISTANT", lw=0.35)
    sc.text("Terrain NGF 41,11", x_pt + 46, y_terr + 4, 2.0, align="left")

    # ---- 7. Annotations ---------------------------------------------------
    sc.leader("Poutre-acrotère de rive 30 × 67\narase 44,75 — "
              "isostatique 8,03 m", 96, y_pt + 44,
              x_pb + B_POUTRE / 2, y_pt - 10, fontsize=1.9)
    sc.leader("Dalle BA 20 cm en console — porte-à-faux 1,70 m", 16,
              y_ph - 62, 85, y_ph + 14, fontsize=1.9)
    sc.leader("Aucun poteau dans cette coupe\n(poteau en rive gauche — "
              "cadre B)", 100, y_ph - 118, 152, y_ph - 16, fontsize=1.9)
    sc.leader("Verrière (hors mission)", x_pt - 60, y_ver + 2,
              x_pt, y_ver - 6, fontsize=1.9)

    # ---- 8. Cotation des niveaux NGF -------------------------------------
    xc = -78.0
    for ngf, lab in ((N.NGF_SOL_RDC, "41,46"),
                     (N.NGF_PH_RDC, "44,08"),
                     (N.NGF_ACROTERE, "44,75"),
                     (N.NGF_VERRIERE_HEAD, "45,90")):
        yy = z(ngf)
        sc.line(xc - 14, yy, -EP_FAC - 30, yy, "STR_COTATIONS_TEXTES",
                lw=0.13)
        sc.text(lab, xc - 18, yy - 3, 2.0, align="right")

    # ---- 9. Cotation horizontale -----------------------------------------
    sc.dim_h(0, x_pb, y_ph - 30, "1,70 m")
    sc.dim_h(x_pb, x_pt, y_ph - 30, "30")
    sc.dim_h(0, x_pt, y_pt + 90, "2,00 m")

    return sc


def build_bord_gauche() -> E.Scene:
    """Cadre B — élévation du bord gauche : poutre perpendiculaire, poteau
    et console de 0,70 m (échelle 1/40)."""
    sc = E.Scene()
    y_ph = z(N.NGF_PH_RDC)
    y_pb = z(N.NGF_POUTRE_BAS)
    y_pt = z(N.NGF_POUTRE_HAUT)
    y_terr = z(N.NGF_TERRAIN)

    # façade en bout
    sc.rect(-EP_FAC, y_terr, EP_FAC, y_ph - y_terr, "STR_EXISTANT", lw=0.30,
            hatch="ANSI31", angle=45.0, spacing=3.0)
    # poteau BA 25 x 25 à 1,30 m
    sc.rect(Y_POT - 12.5, 0, 25, y_pb, "STR_COFFRAGE_BA", lw=0.50, fill=True)
    # Tête du puits représentée en coupe raccourcie, avec rupture graphique.
    # La profondeur complète (2,40 m de calcul, arase NGF 39,02) est donnée
    # dans les notes et sur PL-02/PL-04.
    sc.rect(Y_POT - 67.5, -60.0, 135.0, 60.0, "STR_COFFRAGE_BA", lw=0.45)
    D.ligne_rupture(sc, Y_POT, -58.0, -38.0, amp=3.0)
    # poutre perpendiculaire : de la façade (x=0) au nu extérieur (x=P)
    sc.rect(0, y_pb, P, y_pt - y_pb, "STR_COFFRAGE_BA", lw=0.50, fill=True)
    # console : hachurée différemment au-delà du poteau
    sc.rect(Y_POT, y_pb, P - Y_POT, y_pt - y_pb, "STR_COFFRAGE_BA", lw=0.50,
            hatch="ANSI37", angle=0.0, spacing=1.4)
    # about de la poutre de 8,03 m (perpendiculaire au plan)
    sc.rect(P - B_POUTRE, y_pb, B_POUTRE, y_pt - y_pb, "STR_COTATIONS_TEXTES",
            lw=0.25)
    # dalle
    sc.rect(0, y_ph, P, 20, "STR_COFFRAGE_BA", lw=0.35)
    # sols
    sc.line(-EP_FAC, 0, P + 20, 0, "STR_EXISTANT", lw=0.30)
    sc.line(-EP_FAC, y_terr, P + 20, y_terr, "STR_EXISTANT", lw=0.22)

    sc.dim_h(0, Y_POT, y_pb - 26, "1,30 m")
    sc.dim_h(Y_POT, P, y_pb - 26, "0,70 m")
    sc.dim_v(0, y_pb, -14, "2,62 m")
    sc.text("About de la poutre de rive 8,03 m", P + 18.0, y_pb + 48.0, 2.0)
    return sc


# ---------------------------------------------------------------------------
# Cadre 3 — coupe du voile de rive sur semelle (1/60)
# ---------------------------------------------------------------------------

def build_detail() -> E.Scene:
    """Cadre C — coupe sur le voile de rive et sa semelle filante (1/60)."""
    sc = E.Scene()
    ep = 20.0

    # voile de rive à créer (coupe, hauteur 5,28 m ramenée)
    H = 264.0
    D.beton_rect(sc, 0, 0, ep, H, sp=1.2)
    # semelle filante à créer 65 x 30
    D.beton_rect(sc, -(65 - ep) / 2, -30.0, 65.0, 30.0, sp=1.4)
    # amorce de la dalle
    sc.rect(-60, H, 140, 20, "STR_COFFRAGE_BA", lw=0.45, fill=True)

    # armatures verticales du voile (4 HA 12 par face)
    for x in (5.0, 15.0):
        sc.line(x, 2.0, x, H - 2.0, "STR_FERRAILLAGE", 0.32)
    # horizontales HA 8 e = 250
    for y in range(14, int(H), 25):
        sc.line(3.0, y, 17.0, y, "STR_FERRAILLAGE", 0.22)
    # attentes de la semelle dans le voile (crosses)
    for x in (5.0, 15.0):
        sc.line(x, -2.0, x - 10.0, -12.0, "STR_FERRAILLAGE", 0.32)
    # filants de la semelle
    for y in (-6.0, -24.0):
        sc.line(-30.0, y, 30.0, y, "STR_FERRAILLAGE", 0.30)

    D.cote_h(sc, 0, ep, H + 34, "20")
    D.cote_h(sc, -32.5, 32.5, -44.0, "65")
    D.cote_v(sc, -30.0, 0.0, 46.0, "30")
    sc.leader("Voile de rive BA 20 cm À CRÉER\n4 HA 12 par face + HA 8 e = 250",
              54, H - 40, 15.0, H - 60, fontsize=2.0)
    sc.leader("Semelle filante 65 × 30 À CRÉER\nsous le voile, arase 39,02",
              54, -24, 30.0, -15.0, fontsize=2.0)
    sc.leader("Attentes HA 12 avec cross\ndans la semelle", -54, -20, -8.0,
              -8.0, fontsize=2.0)
    return sc


def _shift(sc, ox, oy):
    t = E.Scene()
    for it in sc.items:
        k = it[0]
        if k == "line":
            _, p1, p2, *r = it
            t.items.append(("line", (p1[0] + ox, p1[1] + oy),
                            (p2[0] + ox, p2[1] + oy), *r))
        elif k == "rect":
            _, (x, y), (w, h), *r = it
            t.items.append(("rect", (x + ox, y + oy), (w, h), *r))
        elif k == "poly":
            _, pts, *r = it
            t.items.append(("poly", [(a + ox, b + oy) for a, b in pts], *r))
        elif k == "circle":
            _, (cx, cy), rad, *r = it
            t.items.append(("circle", (cx + ox, cy + oy), rad, *r))
        elif k == "text":
            _, txt, (x, y), *r = it
            t.items.append(("text", txt, (x + ox, y + oy), *r))
        elif k == "dim_h":
            _, x1, x2, y, *r = it
            t.items.append(("dim_h", x1 + ox, x2 + ox, y + oy, *r))
        elif k == "dim_v":
            _, y1, y2, x, *r = it
            t.items.append(("dim_v", y1 + oy, y2 + oy, x + ox, *r))
        elif k == "hatchpoly":
            _, pts, *r = it
            t.items.append(("hatchpoly", [(a + ox, b + oy) for a, b in pts],
                            *r))
        else:
            t.items.append(it)
    return t


def _placer(pb, sc, x, y, w, h, scale):
    """Centre la scène dans le cadre (x, y, w, h) à l'échelle donnée."""
    pb.k = 10.0 / scale
    x0, y0, x1, y1 = pb.bbox(sc)
    cw, ch = (x1 - x0) * pb.k, (y1 - y0) * pb.k
    pb.set_origin(x + (w - cw) / 2.0 - x0 * pb.k,
                  y + (h - ch) / 2.0 - y0 * pb.k)
    pb.render(sc)


def main():
    os.makedirs(OUT, exist_ok=True)
    sc1 = build_coupe()
    sc2 = build_bord_gauche()
    sc3 = build_detail()

    # ---------- DXF -------------------------------------------------------
    dxf = E.DxfBackend("PL-03")
    for sc, (ox, oy) in ((sc1, (0, 0)), (sc2, (0, -520)),
                         (sc3, (420, -520))):
        dxf.render(_shift(sc, ox, oy))
    p_dxf = dxf.save(os.path.join(OUT, "PL-03_Coupes_Elevations.dxf"))

    # ---------- PDF -------------------------------------------------------
    pb = E.PdfBackend("PL-03", CARTOUCHE)
    pb.new_page()
    pb.titre("PL-03 — COUPES ET ÉLÉVATIONS DE L'EXTENSION",
             "Coupe transversale A-A, élévation du bord gauche et coupe sur "
             "le voile de rive")

    # cadre A : coupe transversale 1/50
    pb.frame(14, 152, 190, 100)
    _placer(pb, sc1, 14, 152, 190, 100, 50.0)
    pb.vtitle(14, 256, "A — COUPE TRANSVERSALE A-A — 1/50")

    # cadre B : bord gauche 1/40
    pb.frame(214, 152, 190, 100)
    _placer(pb, sc2, 214, 152, 190, 100, 40.0)
    pb.vtitle(214, 256, "B — BORD GAUCHE : POTEAU ET CONSOLE — 1/40")

    # cadre C : voile de rive 1/60
    pb.frame(14, 38, 116, 102)
    _placer(pb, sc3, 14, 38, 116, 102, 60.0)
    pb.vtitle(14, 144, "C — VOILE DE RIVE ET SEMELLE — 1/60")

    pb.legende(146, 132, [
        ("STR_COFFRAGE_BA", "Béton armé à créer", "hatch"),
        ("STR_FERRAILLAGE", "Armatures B500B", "line"),
        ("STR_EXISTANT", "Maçonnerie existante", "line"),
    ])
    pb.note_block(146, 106, "NOTES", [
        "1. Niveaux en m NGF ; sol fini RDC = 41,46 (DOC-01 §5).",
        "2. Poutre-acrotère isostatique 8,03 m, arase 44,75, sous-face 44,08.",
        "3. La dalle porte en console de 1,70 m depuis la façade.",
        "4. Poteau BA 25 × 25 à 1,30 m du nu de façade (arbitrage E-02).",
        "5. Puits de gros béton sous poteau : Ø 1,35 m, prof. 2,40 m, arase 39,02.",
        "6. Voile de rive À CRÉER sur semelle filante 65 × 30, arase 39,02.",
        "7. Contre-flèche de coffrage 20 mm sur la poutre de 8,03 m.",
    ], width=260)

    p_pdf = os.path.join(OUT, "PL-03_Coupes_Elevations.pdf")
    pb.save(p_pdf)
    print(p_dxf)
    print(p_pdf)


if __name__ == "__main__":
    main()
