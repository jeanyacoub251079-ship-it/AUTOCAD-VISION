"""Figures schematiques de repérage (Tâche 1) tracees depuis le DXF AARKA.

Rendu filtre par zone (LINE / LWPOLYLINE / ARC / CIRCLE) afin d'obtenir des
extraits lisibles et rapides, puis report des repères D1 a D6 et des cotes
mesurees par le BET.
"""
from __future__ import annotations

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

import ezdxf
from ezdxf import bbox as ezbbox

SRC = ("google_drive/DCE_58 RUE DE L'AIGLE_LA GARENNE COLOMBES MODIF "
       "05112026-export.dxf")
OUT = "affaires/GARENNE/01_TACHE_1/figures"

Y0, NGF0 = -7234.6, 41.46


def ngf(y):
    return round(NGF0 + (y - Y0) / 100.0, 3)


def collect(msp, box, layers=None):
    """Entites geometriques simples dont la bbox est dans box."""
    segs, polys, arcs = [], [], []
    x0, x1, y0, y1 = box
    for e in msp:
        t = e.dxftype()
        if t not in ("LINE", "LWPOLYLINE", "POLYLINE", "ARC", "CIRCLE"):
            continue
        lay = e.dxf.layer
        if layers and lay not in layers:
            continue
        try:
            b = ezbbox.extents([e])
        except Exception:
            continue
        cx, cy = (b.extmin.x + b.extmax.x) / 2, (b.extmin.y + b.extmax.y) / 2
        if not (x0 <= cx <= x1 and y0 <= cy <= y1):
            continue
        if t == "LINE":
            segs.append((e.dxf.start.x, e.dxf.start.y,
                         e.dxf.end.x, e.dxf.end.y, lay))
        elif t == "ARC":
            arcs.append((e.dxf.center.x, e.dxf.center.y, e.dxf.radius,
                         e.dxf.start_angle, e.dxf.end_angle, lay))
        elif t == "CIRCLE":
            arcs.append((e.dxf.center.x, e.dxf.center.y, e.dxf.radius,
                         0, 360, lay))
        else:
            try:
                pts = [(p[0], p[1]) for p in e.get_points("xy")]
            except Exception:
                continue
            if len(pts) > 1:
                polylines = True
                if e.closed:
                    pts = pts + [pts[0]]
                polylines = pts
                polys.append((polylines, lay))
    return segs, polys, arcs


def draw(ax, segs, polys, arcs, wall_lw=1.5):
    from matplotlib.patches import Arc as MplArc
    for x0, y0, x1, y1, lay in segs:
        lw = wall_lw if lay == "ARK-MURS" else 0.5
        col = "#333333" if lay == "ARK-MURS" else "#9a9a9a"
        if lay == "ARK-DEMOL":
            col, lw = "#c00000", 1.2
        ax.plot([x0, x1], [y0, y1], color=col, lw=lw, solid_capstyle="butt",
                zorder=3 if lay == "ARK-MURS" else 1)
    for pts, lay in polys:
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        if lay == "ARK-DEMOL":
            ax.plot(xs, ys, color="#c00000", lw=1.2, zorder=4)
        elif lay == "ARK-MURS":
            ax.plot(xs, ys, color="#333333", lw=wall_lw, zorder=3)
        else:
            ax.plot(xs, ys, color="#9a9a9a", lw=0.5, zorder=1)
    for cx, cy, r, a1, a2, lay in arcs:
        if r > 400:
            continue
        col = "#333333" if lay == "ARK-MURS" else "#b0b0b0"
        ax.add_patch(MplArc((cx, cy), 2 * r, 2 * r, theta1=a1, theta2=a2,
                            color=col, lw=0.6, zorder=2))


# --------------------------------------------------------------------------
# Figure 1 : plan RDC état actuel, repérage D1..D6
# --------------------------------------------------------------------------
def fig_rdc(msp):
    box = (7820, 9150, -10560, -9720)
    segs, polys, arcs = collect(msp, box)
    fig, ax = plt.subplots(figsize=(9.2, 10.6))
    draw(ax, segs, polys, arcs)

    reperes = [
        ("D1", 8093, -10088, "Mur de refend\nEntrée / Bureau", 260, 16, "n"),
        ("D2", 8484, -10483, "Façade avant\nSalon", 380, 47, "s"),
        ("D3", 8693, -10277, "Refend central\nlongitudinal", 355, 57, "w"),
        ("D4", 8889, -10482, "Façade avant\nSalle à manger", 200, 49, "s"),
        ("D5", 8875, -10088, "Refend transversal\nSalle à manger", 308, 16, "e"),
        ("D6", 8876, -9799, "Façade arrière\nCuisine", 154, 46, "n"),
    ]
    for tag, x, y, lib, L, ep, side in reperes:
        ax.plot([x], [y], marker="o", ms=13, mfc="none", mec="#c00000",
                mew=1.4, zorder=8)
        ax.text(x, y - 4, tag, color="#c00000", ha="center", va="center",
                fontsize=9.5, fontweight="bold", zorder=9)
        dx = {"n": 0, "s": 0, "e": 130, "w": -130}[side]
        dy = {"n": 130, "s": -150, "e": 0, "w": 0}[side]
        ax.annotate(f"{tag} — {lib}\nL = {L} cm · e mur = {ep} cm",
                    xy=(x, y), xytext=(x + dx, y + dy),
                    fontsize=7.2, ha="center", va="center", color="#1F3864",
                    bbox=dict(boxstyle="round,pad=0.28", fc="white",
                              ec="#1F3864", lw=0.7, alpha=0.95),
                    arrowprops=dict(arrowstyle="-", color="#1F3864", lw=0.7),
                    zorder=10)

    ax.set_aspect("equal")
    ax.set_xlim(box[0] - 20, box[1] + 20)
    ax.set_ylim(box[2] - 20, box[3] + 60)
    ax.axis("off")
    ax.set_title("Plan RDC — état actuel : repérage des reprises en sous-œuvre "
                 "D1 à D6\n(d'après planche P08a — Cabinet AARKA, 05.11.2026)",
                 fontsize=9, pad=8, color="#1F3864")
    # nord / echelle
    ax.plot([7860, 8060], [-9745, -9745], color="black", lw=1)
    ax.text(7960, -9732, "2,00 m", ha="center", fontsize=6.5)
    fig.tight_layout()
    p = os.path.join(OUT, "fig05_reperage_rdc.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p


# --------------------------------------------------------------------------
# Figure 2 : coupe verticale schematique et altimetrie
# --------------------------------------------------------------------------
def fig_coupe_schema():
    fig, ax = plt.subplots(figsize=(10.4, 7.0))

    niv = {
        "Fond de fouille existante": 39.02,
        "Sol S/Sol fini": 39.26,
        "Sous-face PH RDC": 44.08,
        "Sol R+1 fini": 44.32,
        "Sous-face PH R+1": 46.94,
        "Sol Combles": 47.14,
        "Gouttière": 47.47,
        "Faîtage": 50.16,
        "Acrotère terrasse": 44.75,
    }
    # sol
    ax.fill_between([-1, 9.0], 38.6, 39.26, color="#e8e4d8", zorder=0)
    ax.fill_between([11.4, 15.5], 38.6, 41.46, color="#e8e4d8", zorder=0)
    ax.plot([-1, 9.0], [41.46, 41.46], color="#8a7f60", lw=0.8, ls="--", zorder=1)
    ax.plot([11.4, 15.5], [41.46, 41.46], color="#8a7f60", lw=0.8, ls="--", zorder=1)
    ax.annotate("Sol RDC fini — NGF 41,46", xy=(0.2, 41.46), xytext=(2.6, 41.9),
                fontsize=7, color="#1F3864",
                arrowprops=dict(arrowstyle="-", lw=0.5, color="#1F3864"))

    # murs / planchers (schema)
    lw = dict(color="#1F3864", lw=2.2)
    # mur gauche RDC/R+1 jusqu'au rampant
    ax.plot([0, 0], [41.46, 47.47], **lw)
    ax.plot([0, 0], [39.02, 41.46], color="#595959", lw=2.2)
    # planchers
    for (y0, y1) in [(44.08, 44.32), (46.94, 47.14), (41.10, 41.46)]:
        ax.add_patch(Rectangle((0, y0), 9.0, y1 - y0, fc="#1F3864", ec="none",
                               alpha=0.85, zorder=3))
    # fondations
    ax.add_patch(Rectangle((-0.35, 39.02), 0.35, 2.08, fc="#595959", ec="none"))
    ax.add_patch(Rectangle((-0.55, 39.02), 0.75, 0.25, fc="#595959", ec="none"))
    # extension
    ax.plot([9.0, 11.2], [41.46, 41.46], color="#8a7f60", lw=2)
    ax.add_patch(Rectangle((9.6, 39.02), 0.5, 2.44, fc="#7f7f7f", ec="none"))
    ax.add_patch(Rectangle((9.3, 39.02), 1.1, 0.3, fc="#7f7f7f", ec="none"))
    # poteau BA et verriere
    ax.add_patch(Rectangle((9.6, 41.46), 0.25, 2.72, fc="#2E75B6", ec="none"))
    # poutre retroussée + acrotère
    ax.add_patch(Rectangle((9.6, 44.18), 1.6, 0.30, fc="#2E75B6", ec="none",
                           alpha=0.9))
    ax.add_patch(Rectangle((9.6, 44.48), 0.25, 0.27, fc="#2E75B6", ec="none"))
    ax.plot([9.85, 11.2], [44.32, 44.32], color="#C55A11", lw=2.4)
    # dalles extension
    ax.add_patch(Rectangle((9.85, 44.08), 1.35, 0.24, fc="#C55A11", ec="none",
                           alpha=0.85))
    ax.plot([0, 9.85], [44.32, 44.32], color="#C55A11", lw=0.8, ls=":")

    for label, y in niv.items():
        ax.annotate(f"{label}  —  NGF {y:.2f}".replace(".", ","),
                    xy=(11.35, y), xytext=(11.6, y),
                    fontsize=7, va="center", color="#1F3864",
                    arrowprops=dict(arrowstyle="-", lw=0.5, color="#1F3864"))
        ax.plot([-1, 11.3], [y, y], color="#BFBFBF", lw=0.4, ls=":", zorder=0)

    ax.text(4.5, 45.3, "R+1 (Chambres)", ha="center", fontsize=8,
            color="#1F3864")
    ax.text(4.5, 42.6, "RDC (Séjour / Salle à manger)", ha="center", fontsize=8,
            color="#1F3864")
    ax.text(4.5, 40.2, "Sous-sol (Cave / Buanderie)", ha="center", fontsize=8,
            color="#404040")
    ax.text(10.4, 42.9, "Extension\nSalon d'été", ha="center", fontsize=7.6,
            color="#C55A11")
    ax.text(10.45, 44.62, "Poutre retroussée\n+ acrotère", ha="center",
            fontsize=7, color="#2E75B6")
    ax.text(9.72, 42.2, "Poteau\nBA 25", rotation=90, ha="center",
            fontsize=6.4, color="white", va="center")

    ax.set_xlim(-1.2, 15.4)
    ax.set_ylim(38.5, 50.6)
    ax.set_xlabel("Coupe schématique — altimétrie NGF (m)", fontsize=8)
    ax.set_yticks([39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    ax.tick_params(labelsize=7)
    ax.grid(True, axis="y", lw=0.3, alpha=0.4)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title("Coupe verticale de principe — niveaux NGF relevés sur les "
                 "coupes P09b / P10b / P11b", fontsize=9, color="#1F3864")
    fig.tight_layout()
    p = os.path.join(OUT, "fig06_coupe_principe.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p




# --------------------------------------------------------------------------
# Figure 3 : plan schematique de l'extension (releve DXF P08b)
# --------------------------------------------------------------------------
def fig_extension():
    """Plan de principe de l'extension, cotes en cm (releve DXF P08b)."""
    fig, ax = plt.subplots(figsize=(10.6, 6.4))

    L, P = 803.0, 320.0          # largeur facadée, profondeur
    EP_FAC, EP_MIT = 49.0, 35.0  # epaisseur mur facade / mur mitoyen
    POT = 25.0
    Y_POT = 119.0                # axe poteau depuis le nu de la facade

    # --- existant (au-dessus de la facade)
    ax.add_patch(Rectangle((-80, 0), L + 260, 300, fc="#EDEDED", ec="none",
                           zorder=0))
    ax.text(L / 2, 150, "MAISON EXISTANTE  —  RDC (Salon / Salle à manger)",
            ha="center", va="center", fontsize=8.5, color="#7f7f7f",
            style="italic")
    # mur de facade existant
    ax.add_patch(Rectangle((-80, -EP_FAC), L + 240, EP_FAC, fc="#BFBFBF",
                           ec="#595959", lw=0.8, zorder=2))
    ax.text(L / 2, -EP_FAC / 2, "mur de façade existant (meulière, ép. 49 cm)",
            ha="center", va="center", fontsize=6.6, color="#333333", zorder=5)

    # --- extension
    ax.add_patch(Rectangle((0, -P), L, P, fc="#F7F9FC", ec="#1F3864", lw=1.4,
                           zorder=1))
    # verriere frontale
    ax.plot([0, L], [-P, -P], color="#2E75B6", lw=3.2, zorder=4)
    ax.text(L / 2, -P - 26, "verrière frontale aluminium (hors mission) — "
                            "appui sur longrine BA", ha="center", fontsize=7,
            color="#2E75B6")
    # verriere laterale ouest + poteau
    ax.plot([0, 0], [-P, 0], color="#2E75B6", lw=2.4, zorder=4)
    ax.add_patch(Rectangle((-POT / 2, -Y_POT - POT / 2), POT, POT,
                           fc="#1F3864", ec="black", lw=0.8, zorder=6))
    # voile mitoyen
    ax.add_patch(Rectangle((L, -P), EP_MIT, P, fc="#DDEBF7", ec="#1F3864",
                           lw=1.0, hatch="///", zorder=3))
    ax.text(L + EP_MIT + 16, -P - 20,
            "voile BA mitoyen 20 cm solidaire\ndu mur existant 35 cm",
            fontsize=6.4, color="#1F3864", va="top")

    # --- poutre retroussée
    ax.annotate("", xy=(0, -P / 2), xytext=(L, -P / 2),
                arrowprops=dict(arrowstyle="<->", color="#C00000", lw=1.1,
                                ls=(0, (5, 3))))
    ax.text(L / 2, -P / 2 + 14,
            "Poutre retroussée BA  —  portée 8,03 m  —  acrotère NGF 44,75",
            ha="center", fontsize=8, color="#C00000", fontweight="bold")

    # --- axes (les axes 01 a 03 encadrent la facade ; le poteau est un
    # element interieur, cote depuis le nu de facade et non depuis un axe)
    for i, x in enumerate([0, 387, L]):
        ax.plot([x, x], [60, 40], color="#7f7f7f", lw=0.7, ls="-.")
        ax.plot([x, x], [-P - 60, -P - 40], color="#7f7f7f", lw=0.7, ls="-.")
        ax.add_patch(plt.Circle((x, 30), 17, fc="white", ec="#7f7f7f", lw=0.7,
                                zorder=6))
        ax.text(x, 30, f"0{i + 1}", ha="center", va="center", fontsize=7,
                zorder=7)
        ax.add_patch(plt.Circle((x, -P - 72), 17, fc="white", ec="#7f7f7f",
                                lw=0.7, zorder=6))
        ax.text(x, -P - 72, f"0{i + 1}", ha="center", va="center", fontsize=7,
                zorder=7)

    # --- cotes
    def dim_h(x0, x1, y, txt, off=0):
        ax.annotate("", xy=(x0, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="<->", color="black", lw=0.6,
                                    shrinkA=0, shrinkB=0))
        ax.text((x0 + x1) / 2, y + off, txt, ha="center", va="center",
                fontsize=7, bbox=dict(fc="white", ec="none", pad=1.2))

    def dim_v(y0, y1, x, txt):
        ax.annotate("", xy=(x, y0), xytext=(x, y1),
                    arrowprops=dict(arrowstyle="<->", color="black", lw=0.6,
                                    shrinkA=0, shrinkB=0))
        ax.text(x - 9, (y0 + y1) / 2, txt, ha="center", va="center",
                fontsize=7, rotation=90,
                bbox=dict(fc="white", ec="none", pad=1.2))

    dim_h(0, 387, 82, "387")
    dim_h(387, L, 82, "416")
    dim_h(0, L, 112, "803")
    dim_v(0, -Y_POT, -46, "119")
    dim_v(-Y_POT, -P, -46, "201")
    # cote horizontale de l'axe du poteau depuis le nu de la facade (axe 01)
    ax.annotate("", xy=(0, -Y_POT - 78), xytext=(0, -Y_POT - 78),
                arrowprops=dict(arrowstyle="-", color="none"))
    ax.plot([0, 0], [-Y_POT - 62, -Y_POT - 34], color="#7f7f7f", lw=0.7, ls=":")
    ax.plot([0, 0], [-Y_POT - 62, -Y_POT - 34], color="#7f7f7f", lw=0.7, ls=":")
    dim_v(0, -P, L + EP_MIT + 150, "320")

    # --- reperes des baies
    for x, tag, lib in [(150, "D2", "Salon"), (620, "D4", "Salle à manger")]:
        ax.add_patch(plt.Circle((x, -EP_FAC / 2), 22, fc="none", ec="#C00000",
                                lw=1.1, zorder=7))
        ax.text(x, -EP_FAC / 2, tag, ha="center", va="center", fontsize=7,
                color="#C00000", fontweight="bold", zorder=8)
        ax.text(x, 24, f"{tag} — baie élargie\n{lib}", ha="center",
                fontsize=6.4, color="#C00000")

    # --- cote poteau
    ax.annotate("Poteau BA 25 × 25\nappui avant de la poutre\n(axe à 1,19 m du nu "
                "de façade)",
                xy=(0, -Y_POT), xytext=(95, -255),
                fontsize=6.8, color="#1F3864",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1F3864",
                          lw=0.7),
                arrowprops=dict(arrowstyle="-", color="#1F3864", lw=0.7))

    ax.plot([40, 140], [-P - 44, -P - 44], color="black", lw=1.2)
    ax.text(90, -P - 38, "1,00 m", ha="center", fontsize=6.4)

    ax.set_aspect("equal")
    ax.set_xlim(-90, L + 230)
    ax.set_ylim(-P - 105, 310)
    ax.axis("off")
    ax.set_title("Extension en façade avant — plan de principe coté (cotes en cm, "
                 "relevé DXF P08b)", fontsize=9.5, color="#1F3864", pad=10)
    fig.tight_layout()
    p = os.path.join(OUT, "fig07_extension_plan.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p




# --------------------------------------------------------------------------
# Figure 4 : diagramme de phasage (Gantt sequentiel)
# --------------------------------------------------------------------------
def fig_gantt():
    # (repere, libelle, duree en jours ouvres, decalage de demarrage, couleur)
    phases = [
        ("0", "Constat, relevés, sondages préalables", 3, 0, "#7F7F7F"),
        ("1", "Installation, étaiement provisoire", 4, 3, "#7F7F7F"),
        ("2", "Terrassement des puits d'extension", 4, 7, "#806000"),
        ("3", "Puits gros béton + longrines BA", 6, 9, "#806000"),
        ("4", "Voile mitoyen + poteau BA verrière", 5, 14, "#2E75B6"),
        ("5", "Jambages et poteaux BA du RDC (D1→D6)", 18, 15, "#2E75B6"),
        ("6", "Démolition des murs D1 à D6 (par passes)", 10, 33, "#C00000"),
        ("7", "Pose des profilés métalliques D1→D6", 8, 38, "#7030A0"),
        ("8", "Poutre retroussée + dalle de terrasse", 7, 42, "#2E75B6"),
        ("9", "Décoffrage, réception, levé final", 3, 49, "#7F7F7F"),
    ]
    fig, ax = plt.subplots(figsize=(10.6, 5.2))
    labels = []
    for i, (tag, lib, d, off, col) in enumerate(phases):
        ax.barh(i, d, left=off, height=0.58, color=col, alpha=0.92,
                edgecolor="white", linewidth=0.9, zorder=3)
        ax.text(off + d + 0.6, i, f"{d} j", va="center", fontsize=6.6,
                color="#404040")
        labels.append(f"{tag} — {lib}")
    ax.set_yticks(range(len(phases)))
    ax.set_yticklabels(labels, fontsize=7.6)
    ax.invert_yaxis()
    ax.set_xlabel("Jours ouvrés cumulés (indicatif, une équipe)", fontsize=8)
    ax.grid(True, axis="x", lw=0.4, alpha=0.4, zorder=0)
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.set_xlim(0, 60)

    jalons = [(3, "PA-1\nsol réceptionné"),
              (33, "PA-2/3\nbéton 28 j"),
              (46, "PA-4\nmatage"),
              (49, "PA-5\nferraillage"),
              (52, "PA-6\nréception")]
    for k, (x, txt) in enumerate(jalons):
        ax.axvline(x, color="#C00000", lw=0.9, ls=(0, (4, 3)), zorder=1)
        # alternance sur trois hauteurs pour eviter tout chevauchement
        yy = -1.55 - 0.70 * (k % 3)
        ax.text(x, yy, txt.replace("\n", " — "), ha="center", va="bottom",
                fontsize=5.9, color="#C00000",
                bbox=dict(fc="white", ec="none", pad=0.8, alpha=0.9))
    ax.set_ylim(len(phases) - 0.3, -3.8)
    ax.text(0.0, -3.6, "PA = point d'arrêt bloquant (levée par le BET uniquement)",
            fontsize=6.2, color="#C00000", style="italic")

    fig.tight_layout()
    p = os.path.join(OUT, "fig08_phasage_gantt.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p


def main():
    os.makedirs(OUT, exist_ok=True)
    doc = ezdxf.readfile(SRC)
    msp = doc.modelspace()
    print(fig_rdc(msp))
    print(fig_coupe_schema())
    print(fig_extension())
    print(fig_gantt())


if __name__ == "__main__":
    main()
