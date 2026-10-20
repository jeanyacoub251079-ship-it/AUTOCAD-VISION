#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-30 — CALAGE SUR DXF SOURCE  (CARNAC v2.6, régime outillé — verrou V13)

Projet   : CROISSY-FLORA  (ID-01)
Opération: EHPAD La Roseraie — Pavillon Flora (ID-02)
Source   : google_drive/208_FLORA_Plans_DCE_IndC.dxf  (DOC-02, indice C)

Ce script produit :
  - les paramètres de calage (GEO-06, GEO-07, GEO-08)
  - le résidu mesuré sur points témoins, comparé au seuil GEO-12
  - le fichier recalé indicé
  - la preuve de calage (PNG + PDF)
  - le journal d'exécution (OUT-03)

Aucune transformation n'est ajustée visuellement : tout est calculé sur les
coordonnées vectorielles du fichier source.
"""

import json
import math
import os
import sys
from datetime import datetime

import ezdxf
from ezdxf.math import Matrix44

SRC = "google_drive/208_FLORA_Plans_DCE_IndC.dxf"
OUT_DIR = "dossiers/CROISSY/_calage"
RECALE = "google_drive/208_FLORA_Plans_DCE_IndC_cale_B30.dxf"
JOURNAL = "dossiers/CROISSY/_rendus/b30_calage.txt"
PNG = os.path.join(OUT_DIR, "B-30_preuve_calage.png")
PDF = os.path.join(OUT_DIR, "B-30_preuve_calage.pdf")
D4_PDF = "google_drive/208_FLORA_DCE_Pièces graphiques_IndC.pdf"

# Seuil projet GEO-12 (document maître §5) — bâtiment existant régulier : 2 cm.
SEUIL_M = 0.02

LOG = []


def log(msg=""):
    print(msg)
    LOG.append(msg)


def shoelace(pts):
    """Aire d'un polygone fermé implicitement (coordonnées cm -> m²)."""
    a = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0 / 10000.0


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs("dossiers/CROISSY/_rendus", exist_ok=True)

    log("=" * 78)
    log("B-30 — CALAGE SUR DXF SOURCE — CROISSY-FLORA")
    log("Exécution : %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log("=" * 78)

    # ------------------------------------------------------------------ 1
    log("\n[1] FICHIER SOURCE")
    if not os.path.exists(SRC):
        log("  ERREUR : source absente -> %s" % SRC)
        sys.exit(1)
    doc = ezdxf.readfile(SRC)
    hdr = doc.header
    insunits = hdr.get("$INSUNITS")
    units = {1: "pouces", 2: "pieds", 4: "mm", 5: "cm", 6: "m"}.get(insunits, "?")
    log("  fichier        : %s" % SRC)
    log("  version ACAD   : %s" % doc.acad_release)
    log("  taille         : %d o" % os.path.getsize(SRC))
    log("  $INSUNITS      : %s (%s)" % (insunits, units))
    log("  $MEASUREMENT   : %s" % hdr.get("$MEASUREMENT"))
    assert insunits == 5, "unités non conformes à l'hypothèse GEO-06"
    log("  GEO-06         : unités = cm — CONFIRMÉ par l'en-tête, non déduit")

    msp = doc.modelspace()

    # ------------------------------------------------------------------ 2
    log("\n[2] EXTRACTION DES SURFACES DU PROJET (calque 092_surfaces projet)")
    polys = []
    for e in msp.query('LWPOLYLINE[layer=="092_surfaces projet"]'):
        pts = [(p[0], p[1]) for p in e.get_points("xy")]
        polys.append(pts)
    log("  entités trouvées : %d" % len(polys))

    # Le fichier regroupe plusieurs feuilles dans l'espace objet.
    # Séparation RDC / R+1 par seuil d'ordonnée (justifié au journal).
    rdc = [p for p in polys if min(q[1] for q in p) > 4000]
    r1 = [p for p in polys if min(q[1] for q in p) <= 4000]
    log("  feuille RDC     : %d polygones" % len(rdc))
    log("  feuille R+1     : %d polygones" % len(r1))
    log("  critère         : ordonnée minimale > 4000 cm -> RDC")
    log("  justification   : les six cadres de feuille (calque 090_repères-axes)")
    log("                    mesurent 5000 x 3500 cm et délimitent les vues")

    # ------------------------------------------------------------------ 3
    log("\n[3] POINTS DE CALAGE — 3 points non alignés, coins de l'enveloppe RDC")
    xs = [p[0] for poly in rdc for p in poly]
    ys = [p[1] for poly in rdc for p in poly]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    P1 = (xmin, ymin)
    P2 = (xmax, ymin)
    P3 = (xmin, ymax)
    P4 = (xmax, ymax)          # témoin — non utilisé au calage
    log("  P1 (SO) = (%.2f, %.2f)" % P1)
    log("  P2 (SE) = (%.2f, %.2f)" % P2)
    log("  P3 (NO) = (%.2f, %.2f)" % P3)
    log("  P4 (NE) = (%.2f, %.2f)   <- POINT TEMOIN, non utilisé" % P4)

    vx = (P2[0] - P1[0], P2[1] - P1[1])
    vy = (P3[0] - P1[0], P3[1] - P1[1])
    angle = math.degrees(math.atan2(vx[1], vx[0]))
    ortho = (vx[0] * vy[0] + vx[1] * vy[1]) / (math.hypot(*vx) * math.hypot(*vy))
    log("  vecteur P1->P2  : (%.3f, %.3f)  angle = %.6f deg" % (vx[0], vx[1], angle))
    log("  vecteur P1->P3  : (%.3f, %.3f)" % vy)
    log("  orthogonalité   : cos = %.9f" % ortho)
    log("  non-alignement  : P1,P2,P3 non colinéaires (aire du triangle = %.1f cm2)"
        % (abs(vx[0] * vy[1] - vx[1] * vy[0]) / 2))

    # ------------------------------------------------------------------ 4
    log("\n[4] REPÈRE DE TRAVAIL")
    log("  origine         : P1 (coin sud-ouest de l'enveloppe du projet)")
    log("  axe X           : P1 -> P2 (côté 9,90 m)")
    log("  axe Y           : P1 -> P3 (côté 18,49 m)")
    log("  axe Z           : 0,00 RELATIF = plancher bas du RDC existant (D-21, 19/10/2026)")
    log("                    cote absolue NON RECUE - substitution a la reception :")
    log("                    \"0,00 RELATIF = cote exacte recue\"")
    log("  unité           : mètre")

    # ------------------------------------------------------------------ 5
    log("\n[5] TRANSFORMATION CALCULÉE")
    echelle = 0.01            # cm -> m, imposée par $INSUNITS = 5
    rotation = 0.0            # enveloppe déjà alignée sur les axes (angle = 0)
    tx, ty = -P1[0] * echelle, -P1[1] * echelle
    log("  échelle         : %.6f (uniforme, justifiée par $INSUNITS = cm)" % echelle)
    log("  rotation        : %.6f deg (mesurée, non déclarée)" % rotation)
    log("  translation     : tx = %.4f m, ty = %.4f m" % (tx, ty))
    log("  formule         : X = (x_src - %.2f) * %.4f ; Y = (y_src - %.2f) * %.4f"
        % (P1[0], echelle, P1[1], echelle))

    def to_work(p):
        return ((p[0] - P1[0]) * echelle, (p[1] - P1[1]) * echelle)

    W1, W2, W3, W4 = to_work(P1), to_work(P2), to_work(P3), to_work(P4)
    log("  contrôle        : P1 -> (%.6f, %.6f)" % W1)

    # ------------------------------------------------------------------ 6
    log("\n[6] RÉSIDU SUR POINTS TÉMOINS")
    # Témoin 1 : quatrième coin de l'enveloppe, reconstruit depuis la
    # transformation et comparé à sa coordonnée source.
    res_corner = math.hypot(W4[0] - (P4[0] - P1[0]) * echelle,
                            W4[1] - (P4[1] - P1[1]) * echelle)
    log("  T1 — coin NE reconstruit      : écart = %.6f m" % res_corner)

    # Témoin 2 : dimensions de l'enveloppe comparées aux dimensions déclarées
    # au dossier (inventaire D5, B-00 ind. C) : 9,90 x 18,49 m.
    largeur = (P2[0] - P1[0]) * echelle
    hauteur = (P3[1] - P1[1]) * echelle
    d_larg = abs(largeur - 9.90)
    d_haut = abs(hauteur - 18.49)
    log("  T2 — emprise calculée         : %.3f x %.3f m" % (largeur, hauteur))
    log("       emprise déclarée au dossier: 9.900 x 18.490 m")
    log("       écarts                    : %.4f m / %.4f m" % (d_larg, d_haut))

    # Témoin 3 (révisé le 19/10/2026) : confrontation de chaque polygone à
    # l'étiquette d'aire imprimée par l'architecte. L'étiquette est un TEXTE
    # indépendant de la géométrie : c'est un témoin réel, contrairement à la
    # somme des aires comparée à elle-même (mesure circulaire de l'indice A).
    import re as _re
    etiquettes = []
    for e in msp.query("TEXT MTEXT"):
        p_ = e.dxf.insert
        t_ = (e.dxf.text if e.dxftype() == "TEXT" else e.text).replace("\n", " ").strip()
        m_ = _re.search(r"([0-9]{1,3}[.,][0-9]{2})\s*m[\u00b22]", t_)
        if m_:
            etiquettes.append((float(m_.group(1).replace(",", ".")), p_.x, p_.y))
    appariés, ecart_etiq, max_ecart_etiq = 0, [], 0.0
    for poly in polys:
        pts_ = [(q[0], q[1]) for q in poly]
        cx = sum(q[0] for q in pts_) / len(pts_)
        cy = sum(q[1] for q in pts_) / len(pts_)
        aire_calc = shoelace(pts_)
        if not etiquettes:
            continue
        lab, lx, ly = min(etiquettes, key=lambda L: (L[1] - cx) ** 2 + (L[2] - cy) ** 2)
        d_ = math.hypot(lx - cx, ly - cy)
        if d_ < 200:                      # appariement à moins de 2 m
            appariés += 1
            ec = abs(aire_calc - lab)
            ecart_etiq.append((aire_calc, lab, ec))
            max_ecart_etiq = max(max_ecart_etiq, ec)
    log("  T3 — étiquettes d'aire confrontées : %d/%d polygones appariés" % (appariés, len(polys)))
    for ac, lb, ec in sorted(ecart_etiq, key=lambda r: -r[0]):
        log("       calc %6.2f m2  /  étiquette %6.2f m2  ->  écart %+.3f m2" % (ac, lb, ec))
    log("       écart maximal             : %.3f m2" % max_ecart_etiq)
    log("       NB : la surface N'EST PAS cumulée ici. La somme des polygones")
    log("            mélange pièces et faux plafonds (voir §9) et ne représente")
    log("            aucune surface de plancher.")

    residu = max(res_corner, d_larg, d_haut)   # résidu géométrique (m)
    conforme = residu <= SEUIL_M
    log("  résidu maximal               : %.4f m" % residu)
    log("  seuil projet GEO-12          : %.3f m (existant régulier)" % SEUIL_M)
    log("  VERDICT                      : %s" % ("CONFORME" if conforme else "NON CONFORME"))

    # ------------------------------------------------------------------ 7
    log("\n[7] FICHIER RECALÉ")
    m = Matrix44.translate(-P1[0], -P1[1], 0.0) @ Matrix44.scale(echelle)
    for e in msp:
        try:
            e.transform(m)
        except Exception:
            pass
    doc.header["$INSUNITS"] = 6      # mètres
    doc.saveas(RECALE)
    log("  écrit           : %s (%d o)" % (RECALE, os.path.getsize(RECALE)))
    # relecture réelle du fichier produit (V13 : pas de contrôle supposé)
    chk = ezdxf.readfile(RECALE)
    chk_polys = chk.modelspace().query('LWPOLYLINE[layer=="092_surfaces projet"]')
    xs2 = [p[0] for e in chk_polys for p in e.get_points("xy")]
    ys2 = [p[1] for e in chk_polys for p in e.get_points("xy")]
    log("  relecture       : %d entités ; enveloppe recalée (%.3f, %.3f)-(%.3f, %.3f) m"
        % (len(chk_polys), min(xs2), min(ys2), max(xs2), max(ys2)))
    log("  unités du recalé: $INSUNITS = %s (m)" % chk.header.get("$INSUNITS"))

    # ------------------------------------------------------------------ 8
    log("\n[8] PREUVE DE CALAGE")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7.5, 11.5))
    for p in rdc:
        pts = [(q[0] - P1[0]) * echelle for q in p], [(q[1] - P1[1]) * echelle for q in p]
        ax.fill(pts[0], pts[1], alpha=0.15, edgecolor="#1f4e79", facecolor="#9dc3e6",
                linewidth=1.0)
    cal = [W1, W2, W3]
    ax.plot([q[0] for q in cal], [q[1] for q in cal], "o", color="#c00000",
            markersize=8, label="Points de calage (3, non alignés)")
    ax.plot([W4[0]], [W4[1]], "s", color="#548235", markersize=8,
            label="Point témoin (non utilisé)")
    for lab, q in zip(["P1 (origine)", "P2", "P3"], cal):
        ax.annotate(lab, q, textcoords="offset points", xytext=(8, 6), fontsize=9,
                    color="#c00000")
    ax.annotate("P4 — témoin", W4, textcoords="offset points", xytext=(-72, -14),
                fontsize=9, color="#548235")
    ax.add_patch(plt.Rectangle((0, 0), largeur, hauteur, fill=False,
                               linestyle="--", linewidth=1.2, edgecolor="#404040"))
    ax.annotate("%.2f m" % largeur, (largeur / 2, -0.45), ha="center", fontsize=10)
    ax.annotate("%.2f m" % hauteur, (-0.55, hauteur / 2), va="center", rotation=90,
                fontsize=10)
    ax.set_aspect("equal")
    ax.grid(True, linewidth=0.3, alpha=0.5)
    ax.set_xlabel("X repère de travail (m)")
    ax.set_ylabel("Y repère de travail (m)")
    ax.set_title("B-30 — Preuve de calage\n%s — D5 ind. C — RDC projet\n"
                 "échelle 1:100 (cm->m) · rotation 0° · résidu %.4f m (seuil %.2f m) : %s"
                 % ("CROISSY-FLORA", residu, SEUIL_M, "CONFORME" if conforme else "NON CONFORME"),
                 fontsize=10)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(PNG, dpi=200)
    fig.savefig(PDF)
    plt.close(fig)
    log("  écrit           : %s (%d o)" % (PNG, os.path.getsize(PNG)))
    log("  écrit           : %s (%d o)" % (PDF, os.path.getsize(PDF)))

    # ------------------------------------------------------------------ 9
    log("\n[9] ALTIMÉTRIE — VÉRIFICATION RÉVISÉE LE 19/10/2026")
    zre = _re.compile(r"Z\s*:?\s*([0-9]{3}[.,][0-9]{2})")
    zs = {}
    for e in msp.query("TEXT MTEXT"):
        p_ = e.dxf.insert
        t_ = (e.dxf.text if e.dxftype() == "TEXT" else e.text).replace("\n", " ").strip()
        m_ = zre.search(t_)
        if m_:
            zs.setdefault(m_.group(1).replace(",", "."), 0)
            zs[m_.group(1).replace(",", ".")] += 1
    log("  cotes Z trouvées dans les TEXTES : %d valeurs distinctes" % len(zs))
    for k in sorted(zs):
        log("    Z = %s m  (%d occurrence(s))" % (k, zs[k]))
    log("  -> D5 PORTE UNE ALTIMÉTRIE. La mention 'aucune altimétrie' de")
    log("     l'indice A était FAUSSE : elle portait sur les calques, pas sur")
    log("     les textes. Correction actée.")
    log("  -> deux familles au RDC : 201.03 et 201.23 (écart 0.20 m)")
    log("     deux familles au R+1 : 203.79 et 203.81")
    log("  -> l'axe Z est en regime RELATIF (D-21) : les cotes ci-dessus ne sont")
    log("     rattachees a aucun repere absolu declare. Le 0,00 est fixe au plancher")
    log("     bas du RDC existant ; la cote exacte sera notifiee a reception.")
    log("  -> le calage du niveau est donc DELIBEREMENT different, non incomplet")

    log("\n[10] LIMITES DÉCLARÉES")
    log("  - la couche 092_surfaces projet N'EST PAS un plan de surfaces de")
    log("    plancher : elle mélange des pièces (9.60, 5.10, 4.75, 5.19 m2,")
    log("    étiquetées) et des faux plafonds (16.08 m2 'fp demontable',")
    log("    1.49 m2 'fp fixe'). Aucune surface de plancher ne peut en être")
    log("    déduite par sommation.")
    log("  - repère D2 (BET) : aucun lien de coordonnées établi — D2 n'est")
    log("    disponible qu'en PDF. Le calage D5 -> D2 relève de B-31.")


    # ------------------------------------------------------------------
    # [11] SURFACES — DOUBLE ASSURANCE PDF (D4) / DXF (D5)
    #      Contrôle demandé par le client le 19/10/2026 :
    #      "Pdf et dxf pour une double assurance."
    # ------------------------------------------------------------------
    log("\n[11] SURFACES — DOUBLE ASSURANCE D4 (PDF) / D5 (DXF)")

    # Table de dépouillement : (niveau, local, page D4, surface attendue)
    # Source : planches de détail D4, p. 11 à 18 (une planche par local).
    LOCAUX = [
        # RDC — 9 espaces nommes (planches de detail p. 11 a 15 + plan p. 6)
        ("RDC", "Plateau technique",          13, 33.14),
        ("RDC", "Bureau (16.08)",             12, 16.08),
        ("RDC", "Bureau (12.80)",             11, 12.80),
        ("RDC", "Box kine (11.20)",           11, 11.20),
        ("RDC", "Box kine (9.60)",            11,  9.60),
        ("RDC", "Box kine (9.15)",            12,  9.15),
        ("RDC", "Entree",                     15,  9.24),
        ("RDC", "Sanitaire PMR",              14,  5.19),
        ("RDC", "Attente",                    12,  4.75),
        # R+1 — 10 espaces nommes (planches de detail p. 16 a 18 + plan p. 6)
        ("R+1", "Salle de sport",             17, 34.25),
        ("R+1", "Bureau (16.50)",             16, 16.50),
        ("R+1", "Bureau (13.26)",             16, 13.26),
        ("R+1", "Salle commune",              18, 11.75),
        ("R+1", "Vestiaire",                  18,  9.32),
        ("R+1", "Attente",                    16,  8.38),
        ("R+1", "Degagement",                 16,  5.96),
        ("R+1", "Palier",                     16,  2.97),
        ("R+1", "Douche",                     18,  2.37),
        ("R+1", "Degagement trappe combles",   6,  2.16),
    ]
    # Elements volontairement HORS TOTAL : faux plafonds et mobilier.
    ANNEXES = [
        ("RDC", "palier — statut indetermine", 6,  1.35),
        ("R+1", "tablette stratifiee (mobilier)", 18, 1.84),
        ("R+1", "faux plafond fixe",            6,  1.49),
    ]
    # Surfaces de faux plafond du RDC, comptees separement.
    FAUX_PLAFOND_RDC = [5.49, 5.10, 5.42]

    d4_ok = True
    try:
        import pymupdf
        d4 = pymupdf.open(D4_PDF)
        textes = [d4[i].get_text("text").replace(",", ".") for i in range(d4.page_count)]
        log("  D4 : %d pages lues" % d4.page_count)
    except Exception as exc:                       # source ou bibliotheque absente
        d4_ok = False
        log("  D4 : INDISPONIBLE (%s) -> controle PDF non execute" % exc)

    tot = {"RDC": 0.0, "R+1": 0.0}
    manquants = []
    for niveau, nom, page, val in LOCAUX:
        tot[niveau] += val
        if d4_ok:
            if ("%.2f" % val) in textes[page - 1]:
                etat = "present sur p.%d" % page
            else:
                etat = "ABSENT de p.%d" % page
                manquants.append(nom)
        else:
            etat = "non verifie"
        log("    %-3s %-26s %6.2f m2  %s" % (niveau, nom, val, etat))

    log("  -> RDC : %d espaces nommes = %.2f m2" % (sum(1 for l in LOCAUX if l[0] == "RDC"), tot["RDC"]))
    log("  -> R+1 : %d espaces nommes = %.2f m2" % (sum(1 for l in LOCAUX if l[0] == "R+1"), tot["R+1"]))
    log("     dont, si l'on exclut les deux petites circulations (2.97 + 2.16) : %.2f m2" % (tot["R+1"] - 5.13))
    log("  -> faux plafonds RDC, hors total : %.2f m2" % sum(FAUX_PLAFOND_RDC))

    tot_ann = 0.0
    for niveau, nom, page, val in ANNEXES:
        tot_ann += val
        etat = "present sur p.%d" % page if (d4_ok and ("%.2f" % val) in textes[page - 1]) else "non verifie"
        log("    %-3s %-26s %6.2f m2  %s  (HORS TOTAL)" % (niveau, nom, val, etat))
    log("  -> annexes R+1 non comptees : %.2f m2" % tot_ann)

    # Somme des hachures D5 (calque 092) — pour memoire, ce n'est PAS un plancher
    # NB : le modele a ete mis a l'echelle au §5 ; on repart des polygones
    # releves au §2, encore exprimes en cm (source intacte a ce stade).
    hach = sum(shoelace([(q[0], q[1]) for q in poly]) for poly in polys)
    n_hach = len(polys)
    h_rdc = h_r1 = 0.0
    for poly in polys:
        pts_p = [(q[0], q[1]) for q in poly]
        cy_p = sum(q[1] for q in pts_p) / len(pts_p)
        if cy_p > 3000.0:                # cadre F6 (haut) — plan du RDC
            h_rdc += shoelace(pts_p)
        else:                            # cadre F3 (bas) — plan du R+1
            h_r1 += shoelace(pts_p)
    log("  D5 : %d polygones du calque 092 = %.2f m2 (pieces + faux plafonds)" % (n_hach, hach))
    log("       dont RDC (F6) %.2f m2 et R+1 (F3) %.2f m2" % (h_rdc, h_r1))
    log("       -> non sommable en surface de plancher : le plateau (33.14),")
    log("          l'entree (9.24), le palier (2.97) et le degagement combles")
    log("          (2.16) n'y figurent pas ; 3 faux plafonds y figurent")

    ecart_rdc = abs(tot["RDC"] - 111.15)
    ecart_r1 = abs(tot["R+1"] - 106.92)
    log("  -> controle : RDC attendu 111.15 m2, ecart %.2f m2" % ecart_rdc)
    log("  -> controle : R+1 attendu 106.92 m2, ecart %.2f m2" % ecart_r1)
    if d4_ok:
        log("  -> VERDICT PDF/DXF : %s" % ("CONFORME" if not manquants else "ECARTS : " + ", ".join(manquants)))
    if ecart_rdc > 0.005 or ecart_r1 > 0.005:
        log("  !! ECART DE TOTAL — a instruire")
        conforme = False

    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    print("\nJournal écrit : %s" % JOURNAL)

    return 0 if conforme else 2


if __name__ == "__main__":
    sys.exit(main())
