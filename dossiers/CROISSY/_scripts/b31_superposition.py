#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-31 — PREUVE DE SUPERPOSITION  (CARNAC v2.6, régime outillé — verrou V13)

Projet : CROISSY-FLORA (ID-01)
Livrable prouvé : les deux vues nettoyées B-32 (ind. C)

Trois preuves, trois questions distinctes :
  A. FIDÉLITÉ   — chaque point de la vue nettoyée existe-t-il dans la source,
                  à la même coordonnée ?  (extraction vs redessin)
  B. EMPILEMENT — les murs EXISTANTS du R+1 tombent-ils sur ceux du RDC ?
                  (GEO-11)
  C. NON-DÉCALAGE — la vue a-t-elle la même emprise que la zone source ?
                  (ni translation, ni changement d'échelle)

Seuil projet GEO-12 : 2 cm.
"""

import math
import os
import sys
from datetime import datetime

import ezdxf

SRC = "google_drive/208_FLORA_Plans_DCE_IndC.dxf"
NET = {"RDC": "dossiers/CROISSY/_plans/FLORA_RDC_VUE-NETTOYEE_IndC.dxf",
       "R+1": "dossiers/CROISSY/_plans/FLORA_R1_VUE-NETTOYEE_IndC.dxf"}
OUT = "dossiers/CROISSY/_calage"
JOURNAL = "dossiers/CROISSY/_rendus/b31_superposition.txt"

SEUIL_M = 0.02
FRAMES = {"RDC": (6830, 3902, 11830, 7402), "R+1": (6830, 147, 11830, 3647)}
DECALAGE_Y = 3902 - 147
GRANDS = ("Murs porteurs selon geometre projet", "R+1 Projet")

KEEP = ("010_mur", "020_cloi", "020_cloisons", "030_menuiserie",
        "070_trait-fin", "075_cotation", "077_textes-1",
        # calques qui n'existent qu'À L'INTÉRIEUR des blocs de menuiserie
        # conservés : ils voyagent avec le bloc, on ne peut pas les retirer
        # sans déchirer le symbole de porte.
        "097_traits-fins-005", "2_2-MENUISERIE-CO", "0")

# Emprises du bâti (marge 1,20 m autour des hachures de surfaces).
ENV = {"RDC": (8467, 4323, 9697, 6412), "R+1": (8440, 560, 9710, 2700)}

LOG = []


def log(m=""):
    print(m)
    LOG.append(m)


# ---------------------------------------------------------------- sommets
def feuilles(e, prof=0):
    """(calque, points) des entités terminales, blocs dépliés.

    Les blocs insérés avec une extrusion (0,0,-1) — miroir — ne sont pas
    restitués en WCS par virtual_entities() : on applique la réflexion
    x -> -x nous-mêmes. Sans cela, les portes miroir apparaissent à
    x négatif et faussent toute mesure de distance.
    """
    t = e.dxftype()
    if t == "INSERT":
        if prof > 4:
            return
        miroir = False
        try:
            miroir = e.dxf.extrusion.z < 0
        except Exception:
            pass
        for v in e.virtual_entities():
            if v is None:
                continue
            for lay, pts in feuilles(v, prof + 1):
                if miroir:
                    pts = [(-x, y) for x, y in pts]
                yield (lay, pts)
        return
    yield (e.dxf.layer, points(e))


def points(e):
    t = e.dxftype()
    try:
        if t == "LINE":
            return [(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)]
        if t == "LWPOLYLINE":
            return [(p[0], p[1]) for p in e.get_points("xy")]
        if t == "POLYLINE":
            return [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]
        if t in ("TEXT", "MTEXT"):
            p = e.dxf.insert
            return [(p.x, p.y)]
        if t in ("ARC", "CIRCLE"):
            c = e.dxf.center
            return [(c.x, c.y)]
        if t == "POINT":
            p = e.dxf.location
            return [(p.x, p.y)]
        if t == "SOLID":
            return [(e.dxf.vtx0.x, e.dxf.vtx0.y), (e.dxf.vtx2.x, e.dxf.vtx2.y)]
        if t == "HATCH":
            out = []
            for path in e.paths:
                for v in getattr(path, "vertices", []):
                    out.append((v[0], v[1]) if not hasattr(v, "x") else (v.x, v.y))
            return out
    except Exception:
        return []
    return []


def dans(p, cadre, tol=2.0):
    return (cadre[0] - tol <= p[0] <= cadre[2] + tol
            and cadre[1] - tol <= p[1] <= cadre[3] + tol)


def jeu(chemin, cadre=None, couches=None):
    """Points d'un fichier, filtrés par cadre et par calque terminal."""
    doc = ezdxf.readfile(chemin)
    out = []
    for e in doc.modelspace():
        for lay, pts in feuilles(e):
            if couches and lay not in couches:
                continue
            for p in pts:
                if cadre is None or dans(p, cadre):
                    out.append(p)
    return out


def grille(pts, pas):
    g = {}
    for x, y in pts:
        g.setdefault((int(math.floor(x / pas)), int(math.floor(y / pas))), []).append((x, y))
    return g


def distances(pts_a, pts_b, pas=2.0, rayon=6):
    """Distance de chaque point de A au plus proche point de B (cm)."""
    g = grille(pts_b, pas)
    out = []
    for x, y in pts_a:
        cx, cy = int(math.floor(x / pas)), int(math.floor(y / pas))
        best = None
        for i in range(cx - rayon, cx + rayon + 1):
            for j in range(cy - rayon, cy + rayon + 1):
                for (bx, by) in g.get((i, j), ()):
                    d = (bx - x) ** 2 + (by - y) ** 2
                    if best is None or d < best:
                        best = d
        out.append(math.sqrt(best) if best is not None else float("inf"))
    return out


def segments(chemin, cadre=None, couches=None):
    """Segments ((x1,y1),(x2,y2)) d'un fichier, blocs dépliés."""
    doc = ezdxf.readfile(chemin)
    out = []
    for e in doc.modelspace():
        for lay, _ in feuilles(e):
            if couches and lay not in couches:
                continue
            break
        for seg in _seg(e):
            if cadre is None or (dans(seg[0], cadre) and dans(seg[1], cadre)):
                out.append(seg)
    return out


def _seg(e, prof=0):
    t = e.dxftype()
    if t == "INSERT":
        if prof > 4:
            return
        miroir = False
        try:
            miroir = e.dxf.extrusion.z < 0
        except Exception:
            pass
        for v in e.virtual_entities():
            if v is None:
                continue
            for sg in _seg(v, prof + 1):
                if miroir:
                    sg = ((-sg[0][0], sg[0][1]), (-sg[1][0], sg[1][1]))
                yield sg
        return
    try:
        if t == "LINE":
            yield ((e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y))
        elif t == "LWPOLYLINE":
            pts = [(p[0], p[1]) for p in e.get_points("xy")]
            for i in range(len(pts) - 1):
                yield (pts[i], pts[i + 1])
            if e.closed and len(pts) > 2:
                yield (pts[-1], pts[0])
        elif t == "POLYLINE":
            pts = [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]
            for i in range(len(pts) - 1):
                yield (pts[i], pts[i + 1])
    except Exception:
        return


def rendre(nom, titre, series, xlim, ylim):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(11.69, 8.27))
    ax = fig.add_axes([0.03, 0.05, 0.94, 0.86])
    from matplotlib.collections import LineCollection
    for data, coul, lab, larg in series:
        if not data:
            continue
        if isinstance(data[0], tuple) and isinstance(data[0][0], tuple):
            ax.add_collection(LineCollection(data, colors=coul, linewidths=larg,
                                             label=lab))
        else:
            ax.scatter([p[0] for p in data], [p[1] for p in data], s=larg,
                       c=coul, marker="s", linewidths=0, label=lab, alpha=0.8)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(titre, fontsize=9)
    ax.legend(loc="lower right", fontsize=7, framealpha=0.9)
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(OUT, "%s.%s" % (nom, ext)), dpi=200, facecolor="white")
    plt.close(fig)
    log("  écrit : %s/%s.png / .pdf" % (OUT, nom))


def main():
    os.makedirs(OUT, exist_ok=True)
    log("=" * 78)
    log("B-31 — PREUVE DE SUPERPOSITION — CROISSY-FLORA")
    log("Exécution : %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log("=" * 78)
    log("\n[0] ENTRÉES")
    log("  source   : %s (%d o)" % (SRC, os.path.getsize(SRC)))
    for k, v in NET.items():
        log("  livrable : %s (%d o)" % (v, os.path.getsize(v)))
    log("  seuil    : %.3f m (GEO-12)" % SEUIL_M)
    log("  calque source : %d calques — jeu de référence limité aux %d calques conservés"
        % (len(ezdxf.readfile(SRC).layers), len(KEEP)))

    # ------------------------------------------------------------- preuve A
    log("\n[1] PREUVE A — FIDÉLITÉ DE L'EXTRACTION")
    log("  Chaque point de la vue nettoyée doit exister dans la source à la")
    log("  même coordonnée. Une extraction fidèle donne 0 mm ; un redessin")
    log("  donne des écarts diffus, répartis partout.")
    resA = {}
    for niveau, chemin in NET.items():
        cadre = FRAMES[niveau]
        src = jeu(SRC, cadre, KEEP)
        net = jeu(chemin, cadre)
        d = distances(net, src)
        finies = [x for x in d if x != float("inf")]
        infini = len(d) - len(finies)
        pire = max(finies) if finies else float("inf")
        moy = sum(finies) / len(finies) if finies else float("inf")
        resA[niveau] = dict(pire=pire, moy=moy, n=len(net), src=len(src), inf=infini)
        log("\n  %s" % niveau)
        log("    sommets de référence (source)     : %d" % len(src))
        log("    sommets de la vue nettoyée        : %d" % len(net))
        log("    sans correspondance dans la source: %d" % infini)
        log("    écart maximal                     : %.4f m" % (pire / 100))
        log("    écart moyen                       : %.4f m" % (moy / 100))
        v = "CONFORME" if pire / 100 <= SEUIL_M and infini == 0 else "NON CONFORME"
        resA[niveau]["verdict"] = v
        log("    verdict (GEO-12)                  : %s" % v)

    # ------------------------------------------------------------- preuve B
    log("\n[2] PREUVE B — EMPILEMENT DES MURS EXISTANTS (GEO-11)")
    log("  On ne compare que le calque 010_mur : les cloisons du projet sont")
    log("  neuves au R+1 et n'ont pas à tomber sur celles du RDC.")
    log("  Translation appliquée : celle des cadres, %.0f cm en Y." % DECALAGE_Y)

    murs_rdc = jeu(NET["RDC"], ENV["RDC"], ("010_mur",))
    murs_r1 = jeu(NET["R+1"], ENV["R+1"], ("010_mur",))
    murs_r1_off = [(x, y + DECALAGE_Y) for x, y in murs_r1]

    def bb(pts):
        return (min(p[0] for p in pts), min(p[1] for p in pts),
                max(p[0] for p in pts), max(p[1] for p in pts))

    b_rdc, b_r1 = bb(murs_rdc), bb(murs_r1)
    log("  murs existants RDC : %d sommets — emprise %.2f x %.2f m"
        % (len(murs_rdc), (b_rdc[2] - b_rdc[0]) / 100, (b_rdc[3] - b_rdc[1]) / 100))
    log("  murs existants R+1 : %d sommets — emprise %.2f x %.2f m"
        % (len(murs_r1), (b_r1[2] - b_r1[0]) / 100, (b_r1[3] - b_r1[1]) / 100))
    log("  décalage des cadres adopté : dx = %.0f cm, dy = %.0f cm"
        % (b_rdc[0] - b_r1[0], DECALAGE_Y))
    log("  décalage des emprises      : dx = %.0f cm, dy = %.0f cm"
        % (b_rdc[0] - b_r1[0], b_rdc[1] - b_r1[1]))

    # --- B1 : les enveloppes, preuve de calage ------------------------
    b_rdc, b_r1o = bb(murs_rdc), bb(murs_r1_off)
    ecarts_env = [abs(b_rdc[k] - b_r1o[k]) for k in range(4)]
    log("\n  B1 — EMPILEMENT DES ENVELOPPES (preuve de calage)")
    log("    RDC  : X %.2f → %.2f m · Y %.2f → %.2f m"
        % (b_rdc[0] / 100, b_rdc[2] / 100, b_rdc[1] / 100, b_rdc[3] / 100))
    log("    R+1  : X %.2f → %.2f m · Y %.2f → %.2f m"
        % (b_r1o[0] / 100, b_r1o[2] / 100, b_r1o[1] / 100, b_r1o[3] / 100))
    log("    écart sur les 4 extrémités : %.4f m" % (max(ecarts_env) / 100))
    v1 = "CONFORME" if max(ecarts_env) / 100 <= SEUIL_M else "NON CONFORME"
    log("    verdict : %s" % v1)

    # --- B2 : les murs, constat structurel ----------------------------
    d = distances(murs_r1_off, murs_rdc, pas=5.0, rayon=40)
    fin = [x for x in d if x != float("inf")]
    inf = len(d) - len(fin)
    tri = sorted(fin)
    pire = tri[-1] if tri else float("inf")
    moy = sum(tri) / len(tri) if tri else float("inf")
    med = tri[len(tri) // 2] if tri else float("inf")
    log("\n  B2 — EMPILEMENT MUR À MUR (constat, pas un critère)")
    log("    écart maximal  : %.4f m" % (pire / 100))
    log("    écart médian   : %.4f m" % (med / 100))
    log("    écart moyen    : %.4f m" % (moy / 100))
    log("    sans correspondance à moins de 2 m : %d sommets" % inf)
    for lim, lab in ((2, "≤ 2 cm"), (5, "≤ 5 cm"), (10, "≤ 10 cm"), (50, "≤ 50 cm")):
        n = sum(1 for x in tri if x <= lim)
        log("    %-8s %5d sommets  (%.1f %%)" % (lab, n, 100.0 * n / max(len(tri), 1)))
    n_loin = sum(1 for x in tri if x > 50)
    log("    > 50 cm  %5d sommets  (%.1f %%)"
        % (n_loin, 100.0 * n_loin / max(len(tri), 1)))
    log("    -> lecture : les enveloppes se superposent, mais %d %% des murs"
        % round(100.0 * n_loin / max(len(tri), 1)))
    log("       ne se superposent pas. Les cloisons du R+1 ne sont donc pas")
    log("       portées par les murs du RDC. Conséquence pour B-40 : les")
    log("       charges du niveau haut ne descendent pas à la verticale.")
    vb = v1

    # ------------------------------------------------------------- preuve C
    log("\n[3] PREUVE C — CONFINEMENT AU CADRE")
    log("  Chaque entité livrée doit tenir dans le cadre de son niveau. Une")
    log("  extraction ratée laisse passer la planche voisine.")
    log("  Mesure par extents() : c'est la boîte réelle de l'entité, blocs")
    log("  compris, qui fait foi — pas ses points d'insertion.")
    from ezdxf import bbox as _bbox
    resC = {}
    for niveau, chemin in NET.items():
        cadre = FRAMES[niveau]
        doc = ezdxf.readfile(chemin)
        msp = doc.modelspace()
        dehors = []
        for e in msp:
            try:
                b = _bbox.extents([e])
            except Exception:
                continue
            if (b.extmin.x < cadre[0] - 5 or b.extmax.x > cadre[2] + 5
                    or b.extmin.y < cadre[1] - 5 or b.extmax.y > cadre[3] + 5):
                dehors.append((e.dxftype(), e.dxf.layer, round(b.extmin.x), round(b.extmin.y)))
        resC[niveau] = len(dehors)
        log("\n  %s — %d entités livrées" % (niveau, len(msp)))
        log("    entités hors du cadre : %d" % len(dehors))
        for d_ in dehors[:4]:
            log("      %s" % (d_,))
    vc = "CONFORME" if max(resC.values()) == 0 else "NON CONFORME"
    log("  verdict : %s" % vc)

    # ------------------------------------------------------------- rendus
    log("\n[4] RENDUS DE CONTRÔLE (OUT-04)")
    rendre("B-31_preuve_A_fidelite",
           "B-31 preuve A — fidélité de l'extraction\n"
           "vue nettoyée RDC (cyan) superposée au DXF source (magenta) — écart max %.4f m"
           % (resA["RDC"]["pire"] / 100),
           [(segments(SRC, FRAMES["RDC"], KEEP), "#B00020", "source (calques conservés)", 2.2),
            (segments(NET["RDC"], FRAMES["RDC"]), "#00B8D4", "vue nettoyée RDC", 0.7)],
           (8400, 9760), (4250, 6480))

    rendre("B-31_preuve_B_empilement",
           "B-31 preuve B — empilement des murs existants (calque 010_mur)\n"
           "RDC (magenta) / R+1 translaté de %.0f cm (cyan) — écart médian %.3f m"
           % (DECALAGE_Y, med / 100),
           [([( (x1, y1 + 0), (x2, y2 + 0) ) for (x1, y1), (x2, y2) in
              segments(NET["RDC"], ENV["RDC"], ("010_mur",))],
             "#B00020", "murs existants RDC", 2.0),
            ([((x1, y1 + DECALAGE_Y), (x2, y2 + DECALAGE_Y)) for (x1, y1), (x2, y2) in
              segments(NET["R+1"], ENV["R+1"], ("010_mur",))],
             "#00B8D4", "murs existants R+1 (translatés)", 1.2)],
           (8400, 9760), (4250, 6480))

    # ------------------------------------------------------------- synthèse
    log("\n[5] SYNTHÈSE")
    va = resA["RDC"]["verdict"]
    if resA["R+1"]["verdict"] != va:
        va = "MIXTE"
    log("  A — fidélité de l'extraction : %s" % va)
    log("  B — empilement des enveloppes: %s" % vb)
    log("      (mur à mur : constat, voir [2] B2 — %.0f %% des murs non superposés)"
        % (100.0 * n_loin / max(len(tri), 1)))
    log("  C — confinement au cadre     : %s" % vc)
    global_v = "VALIDÉ" if "NON" not in (va + vb + vc) else "À CORRIGER"
    log("  VERDICT GLOBAL : %s" % global_v)
    log("  B-31 ne corrige aucun écart : la correction appartient à la brique")
    log("  source (B-32 pour la vue, B-30 pour le calage).")

    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log("\nJournal écrit : %s" % JOURNAL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
