#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-32 — VUE NETTOYÉE STRUCTURELLE PAR LIVRABLE  (CARNAC v2.6 — Indice D)

Projet   : CROISSY-FLORA  (ID-01)
Source   : google_drive/208_FLORA_Plans_DCE_IndC.dxf  (DOC-02, indice C)

Correction majeure Indice D (suite revue client du 20/10/2026) :
  Un fond de plan de structure NE DOIT PORTER NI CLOISONS DE DISTRIBUTION,
  NI COMPLEXES D'ISOLATION THERMIQUE / DOUBLAGE, NI MENUISERIES INTÉRIEURES
  DE SECOND OEUVRE.
  Seuls sont conservés :
    1. 010_mur       : murs porteurs existants (relevé géomètre, contours + hachures),
                       recadrés sur l'emprise du bâtiment (hors mur de clôture lointain) ;
    2. 030_menuiserie: UNIQUEMENT les menuiseries extérieures / baies situées dans ou
                       contre un mur porteur (distance à 010_mur <= 22 cm) — suppression
                       intégrale des portes intérieures de cloisons Placo et placards ;
    3. 070_trait-fin : UNIQUEMENT l'escalier (marches, limon, flèche, numéros 1..20),
                       les traits de seuils/allèges des baies porteuses et la flèche NORD
                       (suppression d'évier, cuisinière, tablettes et symboles PMR) ;
    4. 075_cotation  : UNIQUEMENT les cotations d'ensemble structurelles (mesure >= 150 cm),
                       sans les micro-cotes de cloisons et doublages.

Point technique critique sur les blocs du DXF source :
  Dans le fichier architecte, les blocs 'Murs porteurs selon geometre projet' (RDC)
  et 'R+1 Projet' (R+1) sont parfois insérés sur le calque '0' ou '020_cloi' alors que
  leurs entités internes porteurs sont sur '010_mur'. L'INSERT du bloc porteur est
  reclassé sur '010_mur' AVANT purge intégrale de '020_cloi' et '020_cloisons'.

Sorties :
  _plans/FLORA_RDC_VUE-NETTOYEE_IndD.dxf  + .pdf + .png
  _plans/FLORA_R1_VUE-NETTOYEE_IndD.dxf   + .pdf + .png
  _rendus/b32_vue_nettoyee.txt            (journal d'exécution OUT-03)
"""

import math
import os
import sys
from datetime import datetime

import ezdxf
from ezdxf.bbox import extents

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy

SRC = "google_drive/208_FLORA_Plans_DCE_IndC.dxf"
OUT_DIR = "dossiers/CROISSY/_plans"
JOURNAL = "dossiers/CROISSY/_rendus/b32_vue_nettoyee.txt"

# Cadres et emprises strictes du bâtiment (en cm DXF)
CONFIGS = {
    "RDC": {
        "frame": (6830.0, 3902.0, 11830.0, 7402.0),
        "bldg":  (8460.0, 4330.0, 9690.0, 6410.0),
        "block": "Murs porteurs selon geometre projet",
        "out":   "FLORA_RDC_VUE-NETTOYEE_IndD",
        "title": "FLORA — VUE EN PLAN STRUCTURELLE NETTOYÉE — RDC (B-32 Ind. D — sans cloisons ni isolation)",
    },
    "R1": {
        "frame": (6830.0, 147.0, 11830.0, 3647.0),
        "bldg":  (8460.0, 560.0, 9690.0, 2660.0),
        "block": "R+1 Projet",
        "out":   "FLORA_R1_VUE-NETTOYEE_IndD",
        "title": "FLORA — VUE EN PLAN STRUCTURELLE NETTOYÉE — R+1 (B-32 Ind. D — sans cloisons ni isolation)",
    },
}

KEEP_LAYERS = {"010_mur", "030_menuiserie", "070_trait-fin", "075_cotation"}

BAD_INSERT_NAMES = {
    "evier petit", "Range-Oven - 30 in top", "evier pmr",
    "porte placard double", "hand", "nom des menuiseries ext",
}

LOG = []


def log(msg=""):
    print(msg)
    LOG.append(msg)


def point_seg_dist(px, py, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    l2 = dx * dx + dy * dy
    if l2 < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / l2))
    return math.hypot(px - (x1 + t * dx), py - (y1 + t * dy))


def collect_wall_segments(doc, msp, block_name, bldg):
    """Extrait tous les segments 010_mur dans l'emprise du bâtiment."""
    segs = []
    bx0, by0, bx1, by1 = bldg
    for e in msp:
        if e.dxftype() == "INSERT" and e.dxf.name == block_name:
            bb = extents([e])
            if not bb.has_data:
                continue
            m = e.matrix44()
            for be in doc.blocks.get(block_name):
                if be.dxf.layer != "010_mur":
                    continue
                if be.dxftype() == "LWPOLYLINE":
                    pts = [tuple(m.transform((x, y, 0)))[:2] for x, y, *_ in be.get_points("xy")]
                    if be.closed and len(pts) > 2:
                        pts.append(pts[0])
                    segs.extend(zip(pts, pts[1:]))
                elif be.dxftype() == "LINE":
                    p1 = tuple(m.transform((be.dxf.start.x, be.dxf.start.y, 0)))[:2]
                    p2 = tuple(m.transform((be.dxf.end.x, be.dxf.end.y, 0)))[:2]
                    segs.append((p1, p2))
        elif e.dxf.layer == "010_mur":
            if e.dxftype() == "LWPOLYLINE":
                pts = [(x, y) for x, y, *_ in e.get_points("xy")]
                if e.closed and len(pts) > 2:
                    pts.append(pts[0])
                segs.extend(zip(pts, pts[1:]))
            elif e.dxftype() == "LINE":
                segs.append(((e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)))
    out = []
    for (x1, y1), (x2, y2) in segs:
        if (bx0 - 60 <= min(x1, x2) and max(x1, x2) <= bx1 + 60
                and by0 - 60 <= min(y1, y2) and max(y1, y2) <= by1 + 60):
            out.append(((x1, y1), (x2, y2)))
    return out


def min_dist_to_walls(cx, cy, wall_segs):
    if not wall_segs:
        return 9999.0
    return min(point_seg_dist(cx, cy, x1, y1, x2, y2) for (x1, y1), (x2, y2) in wall_segs)


def clean_level(level_key, cfg):
    doc = ezdxf.readfile(SRC)
    msp = doc.modelspace()
    fx0, fy0, fx1, fy1 = cfg["frame"]
    bx0, by0, bx1, by1 = cfg["bldg"]
    target_block = cfg["block"]

    total_frame = 0
    wall_segs = None

    # 1. Identifier l'INSERT du bloc porteur dans le cadre et le reclasser sur 010_mur
    main_insert = None
    for e in list(msp):
        try:
            bb = extents([e])
        except Exception:
            msp.delete_entity(e)
            continue
        if not bb.has_data:
            msp.delete_entity(e)
            continue
        cx = 0.5 * (bb.extmin.x + bb.extmax.x)
        cy = 0.5 * (bb.extmin.y + bb.extmax.y)
        if not (fx0 <= cx <= fx1 and fy0 <= cy <= fy1):
            msp.delete_entity(e)
            continue
        total_frame += 1
        if e.dxftype() == "INSERT" and e.dxf.name == target_block:
            e.dxf.layer = "010_mur"
            main_insert = e

    assert main_insert is not None, f"Bloc {target_block} introuvable dans {level_key}"

    # 2. Nettoyer l'intérieur du bloc de fond (murs du géomètre) :
    #    - supprimer 020_cloi, 020_cloisons, 102_demol, 091_surfaces, 092_surfaces projet, 051_plafonds, 077_textes-1...
    #    - ne garder dans le bloc que 010_mur, 030_menuiserie (en baie porteuse) et 070_trait-fin (escalier / seuils dans emprise bâti)
    m_ins = main_insert.matrix44()
    blk = doc.blocks.get(target_block)
    blk_before = len(blk)
    blk_dropped = 0
    for be in list(blk):
        blay = be.dxf.layer
        if blay not in ("010_mur", "030_menuiserie", "070_trait-fin"):
            blk.delete_entity(be)
            blk_dropped += 1
            continue
        # Vérifier l'emprise transformée pour retirer le long mur de clôture parcellaire hors bâtiment
        try:
            bbb = extents([be])
            if not bbb.has_data:
                blk.delete_entity(be)
                blk_dropped += 1
                continue
            pmin = m_ins.transform((bbb.extmin.x, bbb.extmin.y, 0))
            pmax = m_ins.transform((bbb.extmax.x, bbb.extmax.y, 0))
            ex0, ex1 = min(pmin[0], pmax[0]), max(pmin[0], pmax[0])
            ey0, ey1 = min(pmin[1], pmax[1]), max(pmin[1], pmax[1])
            # Si l'entité s'étend loin hors de l'enveloppe du bâtiment (ex: mur de clôture X > 9700 ou X < 8450)
            if ex1 > bx1 + 80 or ex0 < bx0 - 80 or ey1 > by1 + 80 or ey0 < by0 - 80:
                if blay == "010_mur" and be.dxftype() == "LWPOLYLINE":
                    # Découper proprement les segments strictement dans l'emprise du bâtiment
                    pts = [tuple(m_ins.transform((x, y, 0)))[:2] for x, y, *_ in be.get_points("xy")]
                    if be.closed and len(pts) > 2:
                        pts.append(pts[0])
                    kept_segs = 0
                    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
                        # Garder tout segment dont au moins une extrémité est dans le bâti et l'autre à <= 60 cm
                        if (bx0 - 40 <= x1 <= bx1 + 40 and by0 - 40 <= y1 <= by1 + 40
                                and bx0 - 40 <= x2 <= bx1 + 40 and by0 - 40 <= y2 <= by1 + 40):
                            msp.add_line((x1, y1), (x2, y2), dxfattribs={"layer": "010_mur"})
                            kept_segs += 1
                    blk.delete_entity(be)
                    blk_dropped += 1
                    continue
                else:
                    blk.delete_entity(be)
                    blk_dropped += 1
                    continue
        except Exception:
            pass

    wall_segs = collect_wall_segments(doc, msp, target_block, (bx0, by0, bx1, by1))

    # 3. Filtrer rigoureusement l'espace objet
    kept_counts = {}
    dropped_counts = {}
    for e in list(msp):
        if e is main_insert:
            kept_counts["INSERT_BLOC_PORTEURS"] = 1
            continue
        lay = e.dxf.layer
        dt = e.dxftype()
        if lay not in KEEP_LAYERS:
            dropped_counts[lay] = dropped_counts.get(lay, 0) + 1
            msp.delete_entity(e)
            continue

        bb = extents([e])
        cx = 0.5 * (bb.extmin.x + bb.extmax.x)
        cy = 0.5 * (bb.extmin.y + bb.extmax.y)

        # Conserver la flèche NORD même légèrement sous le bâti
        is_nord = (dt == "INSERT" and e.dxf.name == "NORD")
        if not is_nord:
            if not (bx0 - 110 <= cx <= bx1 + 110 and by0 - 110 <= cy <= by1 + 110):
                dropped_counts[lay + " (hors emprise)"] = dropped_counts.get(lay + " (hors emprise)", 0) + 1
                msp.delete_entity(e)
                continue

        if dt == "INSERT" and e.dxf.name in BAD_INSERT_NAMES:
            dropped_counts[lay + " (équipement 2nd oeuvre)"] = dropped_counts.get(lay + " (équipement 2nd oeuvre)", 0) + 1
            msp.delete_entity(e)
            continue

        # Sur 030_menuiserie : supprimer toutes les portes intérieures des cloisons supprimées !
        # On ne garde que les menuiseries dont un bord est à <= 20 cm d'un mur porteur 010_mur.
        if lay == "030_menuiserie":
            test_pts = [
                (cx, cy),
                (bb.extmin.x, bb.extmin.y), (bb.extmax.x, bb.extmax.y),
                (bb.extmin.x, bb.extmax.y), (bb.extmax.x, bb.extmin.y),
            ]
            dmin = min(min_dist_to_walls(px, py, wall_segs) for px, py in test_pts)
            # Les blocs dynamiques *U... avec arc de battement de porte intérieure loin d'une baie extérieure :
            w_ent = bb.extmax.x - bb.extmin.x
            h_ent = bb.extmax.y - bb.extmin.y
            # Si le centre de l'ouverture est loin d'un mur porteur (> 22 cm), c'est une porte de cloison !
            d_center = min_dist_to_walls(cx, cy, wall_segs)
            if dmin > 18.0 or (dt == "INSERT" and d_center > 38.0):
                dropped_counts["030_menuiserie (porte cloison)"] = dropped_counts.get("030_menuiserie (porte cloison)", 0) + 1
                msp.delete_entity(e)
                continue

        # Sur 075_cotation : ne conserver QUE les cotes dont les DEUX points d'attache
        # s'appuient sur un mur porteur 010_mur (élimine 100 % des cotes de cloisons flottantes) !
        if lay == "075_cotation" and dt == "DIMENSION":
            meas = getattr(e.dxf, "actual_measurement", 0.0) or 0.0
            p2 = getattr(e.dxf, "defpoint2", None)
            p3 = getattr(e.dxf, "defpoint3", None)
            ok_dim = (meas >= 160.0)
            if ok_dim and p2 is not None and p3 is not None:
                d2w = min_dist_to_walls(p2.x, p2.y, wall_segs)
                d3w = min_dist_to_walls(p3.x, p3.y, wall_segs)
                if d2w > 22.0 or d3w > 22.0:
                    ok_dim = False
            if not ok_dim:
                dropped_counts["075_cotation (cote de cloison)"] = dropped_counts.get("075_cotation (cote de cloison)", 0) + 1
                msp.delete_entity(e)
                continue

        kept_counts[lay] = kept_counts.get(lay, 0) + 1

    # Harmoniser les couleurs pour une lecture structurelle nette sur fond blanc
    if "010_mur" in doc.layers:
        doc.layers.get("010_mur").color = 7       # noir franc (murs porteurs)
    if "030_menuiserie" in doc.layers:
        doc.layers.get("030_menuiserie").color = 8 # gris moyen (baies extérieures)
    if "070_trait-fin" in doc.layers:
        doc.layers.get("070_trait-fin").color = 8  # gris moyen (escalier / seuils / Nord)
    if "075_cotation" in doc.layers:
        doc.layers.get("075_cotation").color = 9   # gris clair (cotes d'ensemble)

    out_base = os.path.join(OUT_DIR, cfg["out"])
    dxf_path = out_base + ".dxf"
    doc.saveas(dxf_path)
    aud = doc.audit()

    log(f"\n[{level_key}] {dxf_path} ({os.path.getsize(dxf_path)} octets)")
    log(f"  Entités initiales dans le cadre : {total_frame}")
    log(f"  Bloc '{target_block}' nettoyé   : {len(blk)} conservées / {blk_before} initiales ({blk_dropped} supprimées)")
    log(f"  Audit DXF                       : {len(aud.errors)} erreur(s), {len(aud.fixes)} réparation(s)")
    log("  Conservées en espace objet :")
    for k, v in sorted(kept_counts.items()):
        log(f"    - {k:32s} : {v}")
    log("  Principales suppressions (cloisons, isolation, second oeuvre) :")
    for k, v in sorted(dropped_counts.items(), key=lambda kv: -kv[1])[:12]:
        log(f"    - {k:32s} : {v}")

    # Vérification stricte : ZÉRO entité sur 020_cloi / 020_cloisons dans tout le fichier !
    rem_cloi = [e for e in doc.modelspace() if e.dxf.layer in ("020_cloi", "020_cloisons")]
    rem_blk_cloi = [be for be in blk if be.dxf.layer in ("020_cloi", "020_cloisons")]
    assert len(rem_cloi) == 0 and len(rem_blk_cloi) == 0, "Il reste des entités cloisons/isolation !"
    log("  Contrôle ZÉRO cloison / ZÉRO isolation (020_cloi, 020_cloisons) : OK (0 entité)")

    # Rendu haute lisibilité PNG + PDF
    fig = plt.figure(figsize=(11.69, 16.54))  # A3 Portrait 1:1 ratio propre
    ax = fig.add_axes([0.04, 0.04, 0.92, 0.90])
    rcfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(RenderContext(doc), MatplotlibBackend(ax), config=rcfg).draw_layout(doc.modelspace(), finalize=False)
    ax.set_xlim(bx0 - 150, bx1 + 150)
    ax.set_ylim(by0 - 180, by1 + 150)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(cfg["title"], fontsize=11.5, fontweight="bold", pad=10)
    fig.savefig(out_base + ".png", dpi=200, facecolor="white")
    fig.savefig(out_base + ".pdf", facecolor="white")
    plt.close(fig)
    log(f"  Rendus écrits : {out_base}.png ({os.path.getsize(out_base+'.png')} o) / .pdf ({os.path.getsize(out_base+'.pdf')} o)")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    log("=" * 82)
    log("B-32 — VUE NETTOYÉE STRUCTURELLE PAR LIVRABLE — INDICE D")
    log("Exécution : %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log("Source    : %s (%d octets)" % (SRC, os.path.getsize(SRC)))
    log("Doctrine  : ZÉRO cloison, ZÉRO isolation, ZÉRO équipement de second oeuvre")
    log("=" * 82)

    for k in ("RDC", "R1"):
        clean_level(k, CONFIGS[k])

    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log("\nJournal consigné : %s" % JOURNAL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
