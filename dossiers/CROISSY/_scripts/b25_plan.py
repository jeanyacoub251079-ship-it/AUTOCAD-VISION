#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-25 — PLANCHE DE CONTREVENTEMENT (Indice C) — CROISSY-FLORA
Report du schéma de contreventement sur le fond structurel pur B-32 Ind. D.

Sortie : dossiers/CROISSY/_plans/FLORA_B25_CONTREVENTEMENT_IndC.{dxf,pdf,png}
Filigrane obligatoire : PRINCIPE — NE PAS EXÉCUTER — Indice P
Note D-09 reproduite intégralement.
"""

import json
import math
import os
import sys

import ezdxf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.config import BackgroundPolicy, Configuration
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b25_stabilite as b25  # noqa: E402

SRC = "dossiers/CROISSY/_plans/FLORA_RDC_VUE-NETTOYEE_IndD.dxf"
JSON = "dossiers/CROISSY/_rendus/b25_stabilite.json"
OUT = "dossiers/CROISSY/_plans/FLORA_B25_CONTREVENTEMENT_IndC"
X0, Y0 = b25.B30


def dxf(x, y):
    return (X0 + 100.0 * x, Y0 + 100.0 * y)


LAYERS = [
    ("B25-VOILE", 4),          # cyan
    ("B25-VOILE-MAJ", 1),      # rouge
    ("B25-FLECHE", 5),         # bleu
    ("B25-CENTRE", 2),         # jaune
    ("B25-TEXTE", 7),
    ("B25-CADR", 7),
    ("B25-ALERTE", 1),
]


def add_rect(sp, x0, y0, x1, y1, layer, fill=None):
    sp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                      dxfattribs={"layer": layer})
    if fill is not None:
        h = sp.add_hatch(dxfattribs={"layer": layer})
        h.set_solid_fill(color=fill)
        h.paths.add_polyline_path([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], is_closed=True)


def add_txt(sp, x, y, text, h=12.0, layer="B25-TEXTE"):
    e = sp.add_text(text, height=h, dxfattribs={"layer": layer})
    e.set_placement((x, y))
    return e


def add_leader(sp, tx, ty, px, py, text, h=12.0, layer="B25-TEXTE"):
    sp.add_lwpolyline([(px, py), (tx, ty), (tx + len(text) * h * 0.62, ty)],
                      dxfattribs={"layer": layer})
    add_txt(sp, tx + 6, ty + 4, text, h=h, layer=layer)


def arrow(sp, p1, p2, layer, h=45.0):
    sp.add_line(p1, p2, dxfattribs={"layer": layer})
    ang = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    for s in (+1, -1):
        a = ang + math.pi - s * 0.35
        sp.add_line(p2, (p2[0] + h * math.cos(a), p2[1] + h * math.sin(a)),
                    dxfattribs={"layer": layer})


def main():
    data = json.load(open(JSON, encoding="utf-8"))
    doc = ezdxf.readfile(SRC)
    msp = doc.modelspace()
    for name, col in LAYERS:
        if name not in doc.layers:
            doc.layers.add(name, color=col)
    for lay in ("010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"):
        if lay in doc.layers:
            doc.layers.get(lay).color = 8 if lay == "010_mur" else 9

    walls = b25.extract_walls(SRC, b25.BLOCK_RDC)
    rdc = data["levels"]["RDC"]
    maj = {"M03", "M11", "M09"}
    byid = {w["id"]: w for w in walls}

    # ---------------------------------------------------------------- voiles
    for w in walls:
        pts = [dxf(*p) for p in w["pts"]]
        layer = "B25-VOILE-MAJ" if w["id"] in maj else "B25-VOILE"
        sp_pts = pts + [pts[0]]
        msp.add_lwpolyline(sp_pts, dxfattribs={"layer": layer})
        h = msp.add_hatch(dxfattribs={"layer": layer})
        h.set_solid_fill(color=1 if layer == "B25-VOILE-MAJ" else 4)
        h.transparency = 0.55
        h.paths.add_polyline_path(pts, is_closed=True)
        c = dxf(*w["c"])
        add_txt(msp, c[0] - 22, c[1] - 8, w["id"], h=22.0, layer=layer)

    # ---------------------------------------------------------------- centres
    cr = dxf(rdc["cr_x"], rdc["cr_y"])
    g = dxf(*rdc["G"])
    r = 38.0
    msp.add_circle(cr, r, dxfattribs={"layer": "B25-CENTRE"})
    msp.add_line((cr[0] - r * 1.5, cr[1]), (cr[0] + r * 1.5, cr[1]), dxfattribs={"layer": "B25-CENTRE"})
    msp.add_line((cr[0], cr[1] - r * 1.5), (cr[0], cr[1] + r * 1.5), dxfattribs={"layer": "B25-CENTRE"})
    add_txt(msp, cr[0] + 50, cr[1] - 8, "CR", h=18.0, layer="B25-CENTRE")
    add_txt(msp, cr[0] + 50, cr[1] - 30, f"({rdc['cr_x']:+.2f} ; {rdc['cr_y']:+.2f})", h=11.5,
            layer="B25-CENTRE")

    t = 30.0
    msp.add_lwpolyline([(g[0], g[1] + t * 1.4), (g[0] - t * 1.3, g[1] - t),
                        (g[0] + t * 1.3, g[1] - t), (g[0], g[1] + t * 1.4)],
                       dxfattribs={"layer": "B25-CENTRE"})
    add_txt(msp, g[0] - 118, g[1] - 8, "G", h=18.0, layer="B25-CENTRE")
    add_txt(msp, g[0] - 200, g[1] - 34,
            f"e = {abs(rdc['e_struct'][0]):.2f} / {abs(rdc['e_struct'][1]):.2f} m", h=11.0,
            layer="B25-CENTRE")

    # ---------------------------------------------------------------- vent
    vy, vx = data["wind"]["wy"], data["wind"]["wx"]
    VY = sum(vy.values())
    VX = sum(vx.values())
    arrow(msp, dxf(-1.55, 6.4), dxf(-0.55, 6.4), "B25-FLECHE")
    add_txt(msp, X0 + 100 * -1.50, Y0 + 100 * 6.52, f"VENT Y = {VY:.1f} kN", h=15.0, layer="B25-FLECHE")
    arrow(msp, dxf(4.6, 20.4), dxf(4.6, 19.2), "B25-FLECHE")
    add_txt(msp, X0 + 100 * 4.75, Y0 + 100 * 20.2, f"VENT X = {VX:.1f} kN", h=17.0, layer="B25-FLECHE")

    # ---------------------------------------------------------------- repères numérotés
    def bubble(x, y, num):
        p = dxf(x, y)
        msp.add_circle(p, 22.0, dxfattribs={"layer": "B25-CENTRE"})
        add_txt(msp, p[0] - 7, p[1] - 8, str(num), h=17.0, layer="B25-CENTRE")

    bubble(1.40, 5.11, 1)     # R-1  F2 / F3
    bubble(3.90, 9.30, 2)     # R-2  F1a
    bubble(5.20, 16.20, 3)    # M11 voile majeur
    bubble(9.50, 11.34, 4)    # M09 voile majeur
    bubble(2.60, 6.40, 5)     # CR / G

    # ---------------------------------------------------------------- colonne droite
    tx0, tx1 = 9740.0, 11260.0
    y_bot, y_top = 4480.0, 6470.0
    add_rect(msp, tx0, y_bot, tx1, y_top, "B25-CADR")
    add_rect(msp, tx0, y_top - 92, tx1, y_top, "B25-ALERTE")
    add_rect(msp, tx0 + 8, y_top - 84, tx1 - 8, y_top - 8, "B25-ALERTE")
    add_txt(msp, tx0 + 30, y_top - 60,
            "PRINCIPE — NE PAS EXECUTER — Indice P   (B-25 Ind. C)", h=21.0, layer="B25-ALERTE")

    y = y_top - 140
    add_txt(msp, tx0 + 24, y, "1. SYSTEME DE CONTREVENTEMENT — VERDICT", h=16.0)
    y -= 34
    for line in [
        "La maçonnerie porteuse existante, et elle seule.",
        "12 voiles comptes au RDC · 9 au R+1 · ΣKx = 1,21 GN/m · ΣKy = 1,64 GN/m",
        "EXCLUS : frangements F1a/b/c, F2, F3, F4 · renforts R1/R2/R3/Stab1",
        "         poteaux P1-N/S, P2, P3, J1 · charpente · planchers (diaphragme flexible)",
        "         cloisons / doublages / isolants (V9 : jamais sur une vue structurelle)",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=11.6)
        y -= 22
    y -= 12
    add_txt(msp, tx0 + 24, y, "2. VOILES COMPTES AU RDC — RAIDEURS HORIZONTALES", h=16.0)
    y -= 26
    add_txt(msp, tx0 + 30, y, "ID     A(m²)   L(m)  t_eq(m)   Kx(kN/m)    Ky(kN/m)", h=11.0)
    y -= 20
    for w in rdc["walls"]:
        star = " *" if w["id"] in maj else "  "
        add_txt(msp, tx0 + 30, y,
                f"{w['id']}{star}  {w['A']:6.2f} {w['L']:5.2f}  {w['t_eq']:5.2f}   "
                f"{w['Kx']:9.0f}  {w['Ky']:10.0f}", h=11.0)
        y -= 19
    add_txt(msp, tx0 + 30, y - 2, "* voile majeur (M03 + M11 = 86 % de la raideur RDC)", h=10.5)
    y -= 30

    y -= 6
    add_txt(msp, tx0 + 24, y, "REPERES DE LA PLANCHE", h=15.0)
    y -= 24
    for line in [
        "1  R-1 : F2 + F3 supprimes -> fonction horizontale perdue, non reconstituee",
        "2  R-2 : F1a perce le refend 50 cm -> voile scinde en 2 trumeaux",
        "3  M11 voile majeur RDC (815 171 kN/m en Y) — grandeur transmise a la MOE",
        "4  M09 voile majeur RDC cote Est (192 477 kN/m en Y) — idem M03",
        "5  CR / G du RDC — ecart e_struct = 0,04 m (X) / 0,03 m (Y)",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=10.8)
        y -= 19
    y -= 14
    add_txt(msp, tx0 + 24, y, "3. TORSION ET VERIFICATION SOUS VENT (EC1 / EC6)", h=16.0)
    y -= 28
    chk = data["wind"]["checks"]
    for line in [
        f"G = ({rdc['G'][0]:+.2f} ; {rdc['G'][1]:+.2f}) m   ·   CR = ({rdc['cr_x']:+.2f} ; {rdc['cr_y']:+.2f}) m",
        f"e_struct : {abs(rdc['e_struct'][1]):.2f} m (vent X) · {abs(rdc['e_struct'][0]):.2f} m (vent Y)",
        f"e_accidentelle = ± 0,05 L = ± 0,87 m (X) · ± 0,55 m (Y)  → elle gouverne",
        f"Mt = {chk['RDC-X']['Mt']:.1f} kN·m (X) · {chk['RDC-Y']['Mt']:.1f} kN·m (Y)",
        f"fvk = (0,15 + 0,4 x 0,30) / 2,5 = {data['wind']['fvk']:.0f} kPa",
        f"tau/fvk max = {max(c['ratio'] for c in chk.values()):.3f}  →  CAPACITE LARGEMENT TENUE",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=11.4)
        y -= 21
    y -= 12

    add_txt(msp, tx0 + 24, y, "4. JOINTS DE DILATATION — AUCUN JOINT", h=16.0)
    y -= 26
    for line in [
        "Emprise 11,1 x 17,5 m · dilatation libre 5,2 mm · maçonnerie stabilisee",
        "Frangements appuyes (portee <= 4,88 m) : aucune reprise de dilatation",
        "-> D-28 consignee le 20/10/2026 : aucun joint · a reexaminer si l'emprise est modifiee",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=11.4)
        y -= 21
    y -= 12

    add_txt(msp, tx0 + 24, y, "5. PHASE PROVISOIRE — HORS MISSION (D-27)", h=16.0)
    y -= 26
    major = data["major_walls"]
    for line in [
        "La verification du contreventement en phase provisoire incombe a la",
        "maitrise d'oeuvre structure de conception (batiment existant).",
        "AUCUNE verification provisoire n'est produite par nos soins.",
        "Grandeurs transmises a la MOE (T-04) :",
        f"  R+1  4 voiles majeurs = {100*major[0]['part']:.1f} % de la raideur totale",
        f"       {', '.join(major[0]['ids'])}",
        f"  RDC  4 voiles majeurs = {100*major[1]['part']:.1f} % de la raideur totale",
        f"       {', '.join(major[1]['ids'])}",
        "Restent de notre lot : etaiement d'execution (H-20) · mode operatoire",
        "de pose · ordre F3 avant F2 · etaiement lateral des pignons (securite)",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=10.8)
        y -= 18
    y -= 8

    add_txt(msp, tx0 + 24, y, "6. POSITION SISMIQUE — NON VERIFIEE (D-26)", h=16.0)
    y -= 26
    for line in [
        "Zone 1 (Ile-de-France) · seisme tres faible.",
        "Arrete du 22/10/2010, art. 3 : aucune categorie d'importance n'est",
        "soumise aux regles EC8 en zone 1 -> EC8 NON APPLICABLE.",
        "DECISION CLIENT : aucune verification sismique produite, ni reglementaire,",
        "ni de sensibilite. H-24 (sol C, agr 0,40) est neutralisee, non supprimee.",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=10.8)
        y -= 18
    y -= 10

    add_txt(msp, tx0 + 24, y, "7. POINTS D'ARRET OUVERTS", h=16.0)
    y -= 26
    for line in [
        "PA-01 reconnaissance contradictoire de la continuite des voiles",
        "      M11/M03/M04 · M08/M03/M09 · trumeau M05 — AVANT TOUTE DEMOLITION",
        "PA-02 verification de la liaison charpente-maconnerie des pignons — AVANT DEPOSE",
    ]:
        add_txt(msp, tx0 + 30, y, line, h=10.8)
        y -= 18

    # note D-09 intégrale
    ny = y_bot + 300
    add_rect(msp, tx0 + 18, ny, tx1 - 18, ny + 132, "B25-ALERTE")
    for k, line in enumerate([
        "PRESCRIPTION OBLIGATOIRE D-09 (REPRODUCTION INTEGRALE) :",
        "« AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON...",
        "  CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »",
        "0,00 RELATIF = plancher bas du RDC (D-20/D-21) · arase -1,00 m/TN mini (D-08/D-12) · 60x60 mini (D-14) · SF1 80x80 (D-30)",
    ]):
        add_txt(msp, tx0 + 30, ny + 100 - k * 26, line, h=11.4,
                layer="B25-ALERTE" if k < 3 else "B25-TEXTE")

    # cartouche
    cy1 = y_bot + 268
    cy0 = y_bot + 30
    add_rect(msp, tx0, cy0, tx1, cy1, "B25-CADR")
    for txt, hh, yy, lay in [
        ("EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 18.0, cy1 - 42, "B25-CADR"),
        ("SCHEMA DE CONTREVENTEMENT — STABILITE GLOBALE (PH RDC)", 14.0, cy1 - 82, "B25-CADR"),
        ("Brique B-25 · Indice C · 20/10/2026 · Mode HYPOTHESE-NOTIFIEE · Regime OUTILLE (V13)", 11.5, cy1 - 118, "B25-CADR"),
        ("Fond B-32 Ind. D · Echelle 1/80 · Unites DXF cm · Repere B-30 (P1)", 11.5, cy1 - 148, "B25-CADR"),
        ("PRINCIPE — NE PAS EXECUTER — Indice P", 19.0, cy1 - 196, "B25-ALERTE"),
    ]:
        add_txt(msp, tx0 + 26, yy, txt, h=hh, layer=lay)

    doc.saveas(OUT + ".dxf")
    aud = doc.audit()
    print(f"[DXF] {OUT}.dxf — {os.path.getsize(OUT + '.dxf')} o — audit {len(aud.errors)} erreur(s)")

    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.012, 0.02, 0.976, 0.93])
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(msp, finalize=False)
    ax.set_xlim(8380.0, 11300.0)
    ax.set_ylim(4460.0, 6490.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(
        "CROISSY-FLORA — B-25 (Ind. C) — CONTREVENTEMENT, TORSION ET JOINTS — STABILITÉ EN SERVICE\n"
        "PRINCIPE — NE PAS EXÉCUTER — Indice P   (ni vérification sismique D-26, ni stabilité provisoire D-27)",
        fontsize=11.5, fontweight="bold", pad=8)
    fig.savefig(OUT + ".png", dpi=220, facecolor="white")
    fig.savefig(OUT + ".pdf", facecolor="white")
    plt.close(fig)
    print(f"[PNG] {OUT}.png — {os.path.getsize(OUT + '.png')} o")
    print(f"[PDF] {OUT}.pdf — {os.path.getsize(OUT + '.pdf')} o")


if __name__ == "__main__":
    main()
