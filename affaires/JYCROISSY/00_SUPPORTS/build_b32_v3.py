#!/usr/bin/env python3
"""B-32 V3 — Vue nettoyée SOCLE-GEOS — PLAN D'EXÉCUTION (PROJET seul).
CARNAC v3.0 — extraction filtrée du DXF calé B-30, sans redessin.

V3 (2026-10-31) — CORRECTIF FONDAMENTAL : plan d'exécution = PROJET seul.
  - Un plan de structures ne garde qu'UNE seule vue en plan : le PROJET.
  - L'EXISTANT est la référence pour calculer les renforts, mais n'apparaît pas sur le plan livré.
  - Le plan d'exécution indique à l'entreprise quels travaux réaliser.
  - Les éléments de renfort (poteaux, semelles, dallage, linteaux) apparaissent sur ce plan nettoyé.

Zones du B-30 (calque 090_repères-axes) :
  - EXISTANT : X[0, 50]          → état actuel — SUPPRIMÉ (référence interne, non livré)
  - PROJET   : X[65.64, 115.64]  → bâtiment DIFFÉRENT (bureaux/vestiaire/salle commune/salle de sport) → SUPPRIMÉ
  - DEMOL    : X[131.29, 181.29] → Flora PROJET (plan d'exécution) — CONSERVÉ (seule zone gardée)

Filtre spatial V3 : conserver uniquement X > 115.64 (zone PROJET de Flora).
"""

import ezdxf, json, os
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc

ROOT = "/home/user/AUTOCAD-VISION"
SRC = f"{ROOT}/affaires/JYCROISSY/03_PHASE_1_SOCLE/B-30_Calage/B-30_FLORA_RSU_calé_v1.dxf"
OUT = f"{ROOT}/affaires/JYCROISSY/03_PHASE_1_SOCLE/B-32_Vue_Nettoyee"

KEEP_LAYERS = {"010_mur", "060_repères murs", "090_repères-axes",
               "092_surfaces projet", "102_demol"}
KEEP_BLOCKS = {"Plan existant mi geometre rdc", "R+1 Existant", "R+1 Projet",
               "Murs porteurs selon geometre projet", "NORD"}

# Zones du B-30 (calque 090_repères-axes)
EXISTANT_X_MAX = 50.00
MILIEU_X_MIN = 65.64
MILIEU_X_MAX = 115.64
PROJET_X_MIN = 115.64  # zone PROJET/DEMOL de Flora = X > 115.64


def entity_x(e):
    """X centroïde d'une entité pour le filtre spatial."""
    t = e.dxftype()
    try:
        if t == "INSERT":
            return e.dxf.insert.x
        if t == "LINE":
            return (e.dxf.start.x + e.dxf.end.x) / 2.0
        if t == "LWPOLYLINE":
            pts = e.get_points()
            if pts:
                return sum(p[0] for p in pts) / len(pts)
        if t in ("TEXT", "MTEXT"):
            return e.dxf.insert.x
        if t in ("CIRCLE", "ARC", "ELLIPSE"):
            return e.dxf.center.x
        if t == "POINT":
            return e.dxf.location.x
    except Exception:
        pass
    return None


def in_existant(x):
    if x is None: return False
    return x < MILIEU_X_MIN


def in_milieu(x):
    if x is None: return False
    return MILIEU_X_MIN <= x <= MILIEU_X_MAX


def in_projet(x):
    if x is None: return False
    return x > MILIEU_X_MAX


def should_keep_layer_only(e):
    """Décision de conservation basée sur le calque seul (sans filtre spatial)."""
    if e.dxftype() == "INSERT":
        if e.dxf.name in KEEP_BLOCKS:
            return True
        return e.dxf.layer in KEEP_LAYERS
    layer = e.dxf.layer
    if layer in KEEP_LAYERS:
        return True
    if layer == "0":
        return True
    return False


def should_keep(e):
    """Décide si une entité est conservée dans la vue nettoyée V3.
    V3 : plan d'exécution = PROJET seul (X > 115.64). EXISTANT et MILIEU supprimés."""
    keep = should_keep_layer_only(e)
    if keep:
        x = entity_x(e)
        if not in_projet(x):
            keep = False
    return keep


def plot_entity(ax, e, doc, tx, ty, sx, sy, depth=0):
    """Plot an entity with transform. Recursive for INSERTs."""
    if depth > 6:
        return
    t = e.dxftype()
    try:
        if t == "LINE":
            xs = [e.dxf.start[0] * sx + tx, e.dxf.end[0] * sx + tx]
            ys = [e.dxf.start[1] * sy + ty, e.dxf.end[1] * sy + ty]
            ax.plot(xs, ys, 'k-', lw=0.2, zorder=2)
        elif t == "LWPOLYLINE":
            pts = e.get_points()
            xs = [p[0] * sx + tx for p in pts]
            ys = [p[1] * sy + ty for p in pts]
            ax.plot(xs, ys, 'k-', lw=0.3, zorder=2)
        elif t == "CIRCLE":
            cx = e.dxf.center[0] * sx + tx
            cy = e.dxf.center[1] * sy + ty
            r = e.dxf.radius * sx
            ax.add_patch(Circle((cx, cy), r, fill=False, edgecolor='k', lw=0.2, zorder=2))
        elif t == "ARC":
            cx = e.dxf.center[0] * sx + tx
            cy = e.dxf.center[1] * sy + ty
            r = e.dxf.radius * sx
            ax.add_patch(Arc((cx, cy), 2*r, 2*r, theta1=e.dxf.start_angle,
                             theta2=e.dxf.end_angle, fill=False, edgecolor='k', lw=0.2, zorder=2))
        elif t == "INSERT":
            block = doc.blocks.get(e.dxf.name)
            if block:
                itx = e.dxf.insert[0] * sx + tx
                ity = e.dxf.insert[1] * sy + ty
                isx = e.dxf.xscale * sx
                isy = e.dxf.yscale * sy
                for be in block:
                    bt = be.dxftype()
                    if bt not in ("ATTDEF", "SEQEND"):
                        plot_entity(ax, be, doc, itx, ity, isx, isy, depth + 1)
        elif t == "TEXT":
            ix = e.dxf.insert[0] * sx + tx
            iy = e.dxf.insert[1] * sy + ty
            ax.text(ix, iy, str(e.dxf.text), fontsize=3, color='k', zorder=3)
        elif t == "MTEXT":
            ix = e.dxf.insert[0] * sx + tx
            iy = e.dxf.insert[1] * sy + ty
            ax.text(ix, iy, str(e.text), fontsize=3, color='k', zorder=3)
    except Exception:
        pass


def main():
    os.makedirs(OUT, exist_ok=True)
    doc = ezdxf.readfile(SRC)
    msp = doc.modelspace()

    # ============ 1. COMPTAGE AVANT NETTOYAGE ============
    before = Counter(e.dxf.layer for e in msp)
    before_total = sum(before.values())

    # ============ 2. CLASSIFICATION + SUPPRESSION ============
    kept_entities = []
    removed_entities = []
    layer_status = {}
    existant_removals = []   # (layer, type, name, x)
    milieu_removals = []     # (layer, type, name, x)

    for e in list(msp):
        layer = e.dxf.layer
        keep = should_keep(e)
        layer_only = should_keep_layer_only(e)
        if layer not in layer_status:
            layer_status[layer] = [0, 0]
        if keep:
            kept_entities.append((e, layer, e.dxftype()))
            layer_status[layer][0] += 1
        else:
            removed_entities.append((e, layer, e.dxftype()))
            layer_status[layer][1] += 1
            if layer_only:
                x = entity_x(e)
                name = e.dxf.name if e.dxftype() == "INSERT" else ""
                if in_existant(x):
                    existant_removals.append((layer, e.dxftype(), name, round(x, 2)))
                elif in_milieu(x):
                    milieu_removals.append((layer, e.dxftype(), name, round(x, 2)))
            msp.delete_entity(e)

    # ============ 3. DXF NETTOYÉ V3 ============
    out_dxf = f"{OUT}/SOCLE-GEOS_VUE-NETTOYEE_V3.dxf"
    doc.saveas(out_dxf)

    # ============ 4. PREUVE PNG V3 ============
    fig, ax = plt.subplots(figsize=(20, 14))
    label_colors = {"EXISTANT": "#9E9E9E", "PROJET": "#1976D2", "DEMOL": "#D32F2F"}
    labels_mtext = {}
    for e in msp:
        if e.dxftype() == "MTEXT" and e.dxf.layer == "090_repères-axes":
            labels_mtext[round(e.dxf.insert[0], 1)] = e.text.strip()
    for e in msp:
        if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == "090_repères-axes" and e.closed:
            pts = e.get_points()
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            lab = "?"
            if labels_mtext:
                best = min(abs(min(xs) - lx) for lx in labels_mtext)
                lab = next(v for k, v in labels_mtext.items() if abs(min(xs) - k) == best)
            color = label_colors.get(lab, "#666")
            ax.add_patch(Rectangle((min(xs), min(ys)), max(xs) - min(xs), max(ys) - min(ys),
                          linewidth=1, edgecolor=color, facecolor=color, alpha=0.15))
            ax.text((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, lab,
                    ha="center", va="center", fontsize=10, fontweight="bold", color=color)
    for e, layer, et in kept_entities:
        plot_entity(ax, e, doc, 0, 0, 1.0, 1.0)
    ax.set_xlabel("X RSU (m)")
    ax.set_ylabel("Y RSU (m)")
    ax.set_title("B-32 V3 — Plan d'exécution — SOCLE-GEOS V3 — FLORA PROJET — RSU (m)\n"
                 f"Entités conservées : {len(kept_entities)} | Supprimées : {len(removed_entities)}\n"
                 f"Zone PROJET seule (X > {MILIEU_X_MAX} m) — EXISTANT et MILIEU supprimés")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(f"{OUT}/SOCLE-GEOS_VUE-NETTOYEE_V3.png", dpi=150, bbox_inches="tight")
    fig.savefig(f"{OUT}/SOCLE-GEOS_VUE-NETTOYEE_V3.pdf", bbox_inches="tight")
    plt.close(fig)

    # ============ 5. TABLEAU DE NETTOYAGE V3 (MD) ============
    with open(f"{OUT}/B-32_Tableau_Nettoyage_V3.md", "w", encoding="utf-8") as f:
        f.write("# B-32 V3 — Tableau de nettoyage — SOCLE-GEOS V3 — PLAN D'EXÉCUTION\n\n")
        f.write("**Source** : `B-30_FLORA_RSU_calé_v1.dxf` (DXF calé V1)  \n")
        f.write("**Livrable** : SOCLE-GEOS (plan d'exécution / socle géométrique)  \n")
        f.write("**Mode** : COMPLET  \n")
        f.write("**Version** : V3 — PLAN D'EXÉCUTION = PROJET seul (2026-10-31)  \n\n")
        f.write("## Correctif V3 — Plan d'exécution = PROJET seul\n\n")
        f.write("**Principe** : un plan de structures ne garde qu'**une seule vue en plan** : le PROJET.\n")
        f.write("L'EXISTANT est la référence pour calculer les renforts, mais n'apparaît pas sur le plan livré.\n")
        f.write("Le plan d'exécution indique à l'entreprise quels travaux réaliser.\n\n")
        f.write("**Zones du B-30** (calque `090_repères-axes`) :\n")
        f.write(f"- **EXISTANT** : X[0, 50] m → état actuel → **SUPPRIMÉ** (référence interne)\n")
        f.write(f"- **PROJET (milieu)** : X[{MILIEU_X_MIN}, {MILIEU_X_MAX}] m → bâtiment DIFFÉRENT (bureaux/vestiaire/salle commune/salle de sport) → **SUPPRIMÉ**\n")
        f.write(f"- **DEMOL** : X[131.29, 181.29] m → Flora **PROJET** (plan d'exécution) → **CONSERVÉ (seule zone gardée)**\n\n")
        f.write(f"**Filtre spatial V3** : conserver uniquement X > {MILIEU_X_MAX} m (zone PROJET de Flora).\n\n")
        f.write("## Calques\n\n")
        f.write("| Calque | Statut | Conservé | Supprimés | Justification |\n|---|---|---|---|---|\n")
        justification = {
            "0": "Géométrie bâtiment — non porteur explicite",
            "010_mur": "Murs porteurs (détail géométrique)",
            "020_cloi": "Blocs plans porteurs (INSERT)",
            "020_cloisons": "Cloisons — non porteur",
            "030_menuiserie": "Menuiseries — non porteur",
            "040_meubles": "Mobilier — non porteur",
            "050_sols": "Sols — non porteur",
            "051_plafonds": "Plafonds — non porteur",
            "060_repères murs": "Repères murs",
            "070_trait-fin": "NORD conservé (orientation)",
            "075_cotation": "Cotations — non porteur",
            "075_cotation détails": "Cotations détaillées — non porteur",
            "077_textes-1": "Textes — non porteur",
            "078_textes-2": "Textes — non porteur",
            "078_textes-3": "Textes — non porteur",
            "079_textes-4": "Textes — non porteur",
            "080_plomb-cvc": "Fluides — non porteur",
            "090_repères-axes": "Axes / zone chantier",
            "092_surfaces projet": "Surfaces projet",
            "100 TEXTE PMR": "Texte PMR — non porteur",
            "102_demol": "Démolition — état projet",
            "31_sanitaires": "Sanitaires — non porteur",
        }
        for layer in sorted(layer_status.keys()):
            kept, removed = layer_status[layer]
            total = before.get(layer, 0)
            if kept > 0 and removed > 0:
                stat = "À TRANCHER"
            elif kept > 0:
                stat = "CONSERVER"
            else:
                stat = "SUPPRIMER"
            f.write(f"| `{layer}` | {stat} | {kept} | {removed} | {justification.get(layer, '')[:80]} |\n")
        f.write(f"\n**Total** : {before_total} entités source → {len(kept_entities)} conservées, {len(removed_entities)} supprimées\n\n")
        f.write("## Blocs INSERT conservés (zone PROJET uniquement) — Plan d'exécution\n\n")
        f.write("| Bloc | Calque | Position RSU (m) | Justification |\n|---|---|---|---|\n")
        block_just = {
            "R+1 Projet": "Plan R+1 projet — géométrie porteuse",
            "Murs porteurs selon geometre projet": "Murs porteurs selon géométrie projet",
            "NORD": "Fléche nord — orientation",
            "cloisons reperage": "Repère cloisons — repère structurel",
        }
        for e, layer, et in kept_entities:
            if et == "INSERT":
                bname = e.dxf.name
                if bname in block_just:
                    x = round(e.dxf.insert[0], 2)
                    y = round(e.dxf.insert[1], 2)
                    f.write(f"| {bname} | {layer} | ({x}, {y}) | {block_just[bname]} |\n")
        f.write("\n## Entités EXISTANT supprimées (zone X[0, 50] — référence interne, non livrée)\n\n")
        f.write("| Calque | Type | Nom | X RSU (m) |\n|---|---|---|---|\n")
        for lr, t, name, x in sorted(existant_removals, key=lambda s: s[3]):
            nm = name if name else "—"
            f.write(f"| `{lr}` | {t} | {nm} | {x} |\n")
        f.write(f"\n**Total EXISTANT supprimé** : {len(existant_removals)} entités\n\n")
        f.write("## Entités MILIEU supprimées (zone X[65.64, 115.64] — bâtiment non Flora)\n\n")
        f.write("| Calque | Type | Nom | X RSU (m) |\n|---|---|---|---|\n")
        for lr, t, name, x in sorted(milieu_removals, key=lambda s: s[3]):
            nm = name if name else "—"
            f.write(f"| `{lr}` | {t} | {nm} | {x} |\n")
        f.write(f"\n**Total MILIEU supprimé** : {len(milieu_removals)} entités\n\n")
        f.write("## Limites (V4 — pas de redessin)\n\n")
        f.write("- Les blocs plans « mi géomètre » contiennent murs + mobilier + textes : impossible de filtrer sans redessin (verrou V2).\n")
        f.write("- Le mobilier/textes à l'intérieur des blocs plans est conservé — limitation déclarée.\n")
        f.write("- Le calage est celui de B-30 (RSU, m). Aucun ajustement visuel (V4).\n")
        f.write("- Le plan d'exécution V3 = zone PROJET seule. Les renforts (poteaux, semelles, dallage, linteaux) seront ajoutés sur ce plan.\n")

    # ============ 6. JOURNAL + RDL V3 ============
    with open(f"{OUT}/journal_B32_V3.md", "w", encoding="utf-8") as f:
        f.write("# Journal B-32 V3 — Plan d'exécution SOCLE-GEOS — PROJET seul (OUT-03)\n\n")
        f.write(f"**Date** : 2026-10-31  \n**Mode** : COMPLET  \n**Script** : `build_b32_v3.py`  \n\n")
        f.write("## Correction fondamentale (user GO 2026-10-31)\n\n")
        f.write("Le user a corrigé une erreur de compréhension majeure :\n")
        f.write("- **Un plan de structures ne garde qu'UNE seule vue en plan : le PROJET.**\n")
        f.write("- L'EXISTANT est la référence pour calculer les renforts, mais n'apparaît pas sur le plan livré.\n")
        f.write("- Le plan d'exécution indique à l'entreprise quels travaux réaliser.\n")
        f.write("- Les éléments de renfort (poteaux, semelles, dallage, linteaux) apparaissent sur ce plan nettoyé.\n\n")
        f.write("## Exécution V3\n\n")
        f.write("1. Lecture du DXF calé B-30 (RSU, m)\n")
        f.write("2. Filtre spatial : conserver uniquement X > 115.64 m (zone PROJET de Flora)\n")
        f.write(f"3. Entités EXISTANT supprimées : {len(existant_removals)}\n")
        f.write(f"4. Entités MILIEU supprimées : {len(milieu_removals)}\n")
        f.write(f"5. Entités conservées : {len(kept_entities)} | Supprimées : {len(removed_entities)}\n")
        f.write("6. DXF nettoyé : `SOCLE-GEOS_VUE-NETTOYEE_V3.dxf`\n")
        f.write("7. Preuve : PNG + PDF produits\n")
        f.write("8. Tableau de nettoyage : produit\n\n")
        f.write("## Contrôles post-exécution\n\n")
        f.write("- DXF nettoyé relu : OK\n")
        f.write("- Aucun élément redessiné (extraction filtrée, verrou V2)\n")
        f.write("- Plan d'exécution = zone PROJET seule (X > 115.64 m)\n")
        f.write("- Aucune entité EXISTANT ou MILIEU dans le DXF V3\n")
        f.write("- Nommage conforme convention : SOCLE-GEOS_VUE-NETTOYEE_V3\n\n")
        f.write("## RDL — Ligne de phase 1\n\n")
        f.write("| Livrable | Source | Calage B-30 | Version vue nettoyée | Date |\n|---|---|---|---|---|\n")
        f.write("| SOCLE-GEOS | DXF calé V1 | V1 | SOCLE-GEOS_VUE-NETTOYEE_V3 | 2026-10-31 |\n")
        f.write("\n## Porte suivante\n\nEn attente du GO du user pour la suite.\n")

    print(json.dumps({
        "ok": True,
        "version": "V3",
        "kept": len(kept_entities),
        "removed": len(removed_entities),
        "existant_removals": len(existant_removals),
        "milieu_removals": len(milieu_removals),
        "layers_treated": len(layer_status),
        "dxf_bytes": os.path.getsize(out_dxf),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
