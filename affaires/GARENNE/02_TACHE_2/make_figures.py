"""Figures de la note DOC-03 (Tâche 2) — tracées depuis les résultats calculés."""

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
RES = os.path.join(HERE, "calculs_resultats.json")

BLEU = "#1F3864"
BLEU2 = "#2E75B6"
ROUGE = "#C00000"
GRIS = "#7F7F7F"
VERT = "#548235"


def _load():
    with open(RES, encoding="utf-8") as fh:
        return json.load(fh)


import sys
sys.path.insert(0, HERE)


# ---------------------------------------------------------------------------
# Fig. 1 — Courbes d'efforts de la poutre-acrotère (travée unique 8,03 m)
# ---------------------------------------------------------------------------
def fig_poutre_efforts():
    r = _load()["extension"]
    p_ = r["poutre"]
    L = p_["L"]
    b, h = p_["b"], p_["h"]
    q_elu = p_["q_elu"]
    q_els = p_["q_els"]
    Ie = p_["Ie"]

    x = np.linspace(0.0, L, 400)
    M = q_elu * x * (L - x) / 2.0
    V = q_elu * (L / 2.0 - x)

    # déformée : charge répartie sur inertie effective Ie, puis fluage
    E = 31000.0e3
    w = q_els
    y = (w * x * (L ** 3 - 2.0 * L * x ** 2 + x ** 3)
         / (24.0 * E * Ie) * 1000.0)
    y = y * (1.0 + 2.0)                    # fluage φ = 2

    fig, axs = plt.subplots(3, 1, figsize=(10.2, 8.0), sharex=True,
                            gridspec_kw=dict(height_ratios=[1.0, 1.0, 1.05]))

    # ---- moment
    ax0 = axs[0]
    ax0.plot(x, -M, color=BLEU2, lw=1.9,
             label=f"Moment de flexion ELU (q = {q_elu:.1f} kN/m)".replace(".", ","))
    ax0.fill_between(x, 0, -M, color=BLEU2, alpha=0.08)
    ax0.axhline(0, color="k", lw=0.9)
    ax0.plot([L / 2], [-M.max()], marker="o", ms=4, color=ROUGE)
    ax0.annotate(f"M max = {M.max():.1f} kN·m".replace(".", ","),
                 xy=(L / 2, -M.max()), xytext=(L / 2 + 0.45, -M.max() * 0.72),
                 fontsize=7.6, color=ROUGE,
                 arrowprops=dict(arrowstyle="->", color=ROUGE, lw=0.8))
    ax0.set_ylabel("Moment M (kN·m)", fontsize=8.2)
    ax0.invert_yaxis()
    ax0.grid(alpha=0.3, lw=0.4)
    ax0.legend(fontsize=7.5, loc="lower left", framealpha=0.95)
    ax0.set_title("Poutre-acrotère de rive 30 × 67 cm — travée isostatique de "
                  f"{L:.2f} m entre le voile de rive à créer et la console "
                  "(poteau à 1,30 m)".replace(".", ","), fontsize=9.5, color=BLEU,
                  pad=8)

    # ---- effort tranchant
    ax1 = axs[1]
    ax1.plot(x, V, color=VERT, lw=1.7)
    ax1.fill_between(x, 0, V, color=VERT, alpha=0.08)
    ax1.axhline(0, color="k", lw=0.9)
    ax1.annotate(f"V max = {p_['V']:.1f} kN".replace(".", ","),
                 xy=(0.05, V.max()), xytext=(0.75, V.max() * 0.55),
                 fontsize=7.6, color=VERT,
                 arrowprops=dict(arrowstyle="->", color=VERT, lw=0.8))
    ax1.set_ylabel("Effort tranchant V (kN)", fontsize=8.2)
    ax1.grid(alpha=0.3, lw=0.4)

    # ---- déformée
    ax2 = axs[2]
    ax2.plot(x, y, color=BLEU2, lw=1.9, label="flèche à long terme (φ = 2)")
    ax2.axhline(p_["fleche_lim_250"], color="#BF9000", lw=1.2, ls="-.",
                label=f"limite L/250 = {p_['fleche_lim_250']:.1f} mm".replace(".", ","))
    ax2.axhline(p_["fleche_lim_500"], color=ROUGE, lw=1.2, ls="--",
                label=f"limite L/500 = {p_['fleche_lim_500']:.1f} mm".replace(".", ","))
    ax2.axhline(-p_["contre_fleche"], color=GRIS, lw=1.0, ls=":",
                label=f"contre-flèche de coffrage {p_['contre_fleche']:.0f} mm")
    ax2.annotate((f"f = {y.max():.1f} mm  (L/{L*1000/y.max():.0f})").replace(".", ","),
                 xy=(L / 2, y.max()), xytext=(L / 2 + 0.45, y.max() * 0.80),
                 fontsize=7.6, color=BLEU,
                 arrowprops=dict(arrowstyle="->", color=BLEU, lw=0.8))
    ax2.axhline(0, color="k", lw=0.8)
    ax2.invert_yaxis()
    ax2.set_xlabel("Abscisse le long de la poutre (m) — 0 = voile de rive à "
                   f"créer, {L:.2f} = about de la console".replace(".", ","),
                   fontsize=8.5)
    ax2.set_ylabel("Flèche à long terme (mm)", fontsize=8.2)
    ax2.grid(alpha=0.3, lw=0.4)
    ax2.legend(fontsize=7.2, loc="lower left", ncol=2)
    ax2.set_xlim(0, L)

    fig.tight_layout()
    p = os.path.join(OUT, "fig10_poutre_efforts.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p


# ---------------------------------------------------------------------------
# Fig. 2 — Coupes transversales : poutre-acrotère (T) et ferraillage
# ---------------------------------------------------------------------------
def fig_coupe_poutre():
    r = _load()["extension"]["poutre"]
    b, h = r["b"], r["h"]
    e_d = r["e_d"]
    beff = r["beff"]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(9.2, 6.0),
                                  gridspec_kw=dict(width_ratios=[1.0, 1.15]))

    # ---- à gauche : coupe transversale avec la table collaborante
    ax.add_patch(Rectangle((0, 0), b, h, fc="#E8EEF7", ec=BLEU, lw=1.5))
    ax.add_patch(Rectangle((-0.0, h - e_d), beff, e_d, fc="#D6E4F5",
                           ec=BLEU, lw=1.2, alpha=0.9))
    ax.text(beff / 2, h - e_d / 2, "table collaborante (dalle 20 cm)",
            ha="center", va="center", fontsize=6.6, color=BLEU)
    ax.text(-0.05, h * 0.45, "âme 30 cm", rotation=90, ha="right",
            va="center", fontsize=7, color=BLEU)
    ax.annotate("", xy=(b, -0.06), xytext=(0, -0.06),
                arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(b / 2, -0.10, f"{b*100:.0f}", ha="center", fontsize=7.4)
    ax.annotate("", xy=(-0.10, 0), xytext=(-0.10, h),
                arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(-0.15, h / 2, f"{h*100:.0f}", va="center", rotation=90, fontsize=7.4)
    ax.annotate("", xy=(beff, h + 0.10), xytext=(0, h + 0.10),
                arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(beff / 2, h + 0.14, f"b_eff = {beff*100:.0f}", ha="center",
            fontsize=7.4)
    ax.set_xlim(-0.42, beff + 0.16)
    ax.set_ylim(-0.26, h + 0.26)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Coupe transversale — poutre-acrotère {b*100:.0f} × "
                 f"{h*100:.0f} cm", fontsize=9, color=BLEU, pad=6)

    # ---- à droite : ferraillage de l'âme
    enr = 0.03
    ax2.add_patch(Rectangle((0, 0), b, h, fc="#E8EEF7", ec=BLEU, lw=1.5))
    ax2.add_patch(Rectangle((enr, enr), b - 2 * enr, h - 2 * enr,
                            fc="none", ec=ROUGE, lw=1.2))
    barres = r["armature"]
    n = barres["n"]
    for i in range(n):
        xb = enr + 0.025 + (b - 2 * enr - 0.050) * (i / max(1, n - 1))
        ax2.add_patch(Circle((xb, enr + 0.025), 0.010, fc=BLEU, ec=BLEU))
    ax2.annotate("", xy=(b, -0.06), xytext=(0, -0.06),
                 arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax2.text(b / 2, -0.10, f"{b*100:.0f} cm", ha="center", fontsize=7.6)
    ax2.annotate("", xy=(-0.08, 0), xytext=(-0.08, h),
                 arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax2.text(-0.12, h / 2, f"{h*100:.0f} cm", va="center", rotation=90,
             fontsize=7.6)
    xr = b + 0.14
    ax2.annotate(f"{barres['libelle']} (A_s = {barres['As_cm2']:.2f} cm²)\n"
                 "en une seule nappe",
                 xy=(b - enr - 0.010, enr + 0.025), xytext=(xr, 0.10),
                 fontsize=7.2, color=BLEU, va="center",
                 arrowprops=dict(arrowstyle="->", lw=0.7, color=BLEU))
    ax2.annotate(f"étriers HA {int(r['etriers']['phi'])} e = "
                 f"{int(r['etriers']['s_retenu'])} mm",
                 xy=(b, h * 0.45), xytext=(xr, h * 0.52), fontsize=7.2,
                 color=ROUGE, va="center",
                 arrowprops=dict(arrowstyle="->", lw=0.7, color=ROUGE))
    ax2.annotate("enrobage 30 mm", xy=(enr, h * 0.22), xytext=(xr, h * 0.26),
                 fontsize=7.2, color=GRIS, va="center",
                 arrowprops=dict(arrowstyle="->", lw=0.7, color=GRIS))
    ax2.set_xlim(-0.20, b + 0.60)
    ax2.set_ylim(-0.16, h + 0.10)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("Ferraillage de l'âme", fontsize=9, color=BLEU, pad=6)

    fig.tight_layout()
    p = os.path.join(OUT, "fig11_coupe_poutre.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p


# ---------------------------------------------------------------------------
# Fig. 3 — Schéma de reprise en sous-œuvre type (coupe transversale)
# ---------------------------------------------------------------------------
def fig_schema_rso():
    """Elevation d'une baie de facade en cours de reprise en sous-oeuvre.

    Les jambages encadrent la baie, le sommier la coiffe, le profile repose
    sur le sommier et la maconnerie est conservee au-dessus. Les legendes
    sont placees a droite, hors de la zone dessinee.
    """
    fig, ax = plt.subplots(figsize=(8.6, 7.6))

    L_BAIE = 3.80            # largeur de baie (D2, cas le plus charge)
    H_BAIE = 2.15
    J = 0.25                 # largeur de jambage
    H_SOM = 0.40
    H_PRO = 0.20
    H_HAUT = 5.72
    H_TOT = H_BAIE + H_SOM + H_PRO + H_HAUT

    # jambages BA de part et d'autre de la baie
    ax.add_patch(Rectangle((0.0, 0.0), J, H_BAIE, fc="#BDD7EE", ec=BLEU2, lw=1.1))
    ax.add_patch(Rectangle((L_BAIE - J, 0.0), J, H_BAIE, fc="#BDD7EE", ec=BLEU2, lw=1.1))
    ax.text(J / 2, H_BAIE / 2, "jambage\nBA\n25 × 50", ha="center", va="center",
            fontsize=6.6, color=BLEU, rotation=90)
    ax.text(L_BAIE - J / 2, H_BAIE / 2, "jambage\nBA\n25 × 50", ha="center",
            va="center", fontsize=6.6, color=BLEU, rotation=90)

    # baie (vide)
    ax.add_patch(Rectangle((J, 0.0), L_BAIE - 2 * J, H_BAIE, fc="white",
                           ec="#7F6B4F", lw=0.9, ls="--"))
    ax.text(L_BAIE / 2, H_BAIE * 0.52, "BAIE LIBÉRÉE", ha="center",
            va="center", fontsize=8.5, color="#5B4A33")
    ax.text(L_BAIE / 2, H_BAIE * 0.40,
            "D2 3,80 m  ·  D4 2,00 m  ·  D6 1,54 m", ha="center",
            va="center", fontsize=7, color="#5B4A33")

    # sommier BA coiffant la baie
    ax.add_patch(Rectangle((0.0, H_BAIE), L_BAIE, H_SOM, fc="#9DC3E6",
                           ec=BLEU2, lw=1.1))
    ax.text(L_BAIE / 2, H_BAIE + H_SOM / 2, "SOMMIER BA 25 × 40 — chaînage 4 HA 10",
            ha="center", va="center", fontsize=6.8, color=BLEU)

    # profile metallique
    ax.add_patch(Rectangle((-0.10, H_BAIE + H_SOM), L_BAIE + 0.20, H_PRO,
                           fc="#F4B183", ec="#C55A11", lw=1.5))
    ax.text(L_BAIE / 2, H_BAIE + H_SOM + H_PRO / 2,
            "PROFILÉ S355 JUMELÉ — maté au mortier sans retrait",
            ha="center", va="center", fontsize=6.4, color="#7B3A08")

    # maconnerie conservee au-dessus
    ax.add_patch(Rectangle((0.0, H_BAIE + H_SOM + H_PRO), L_BAIE, H_HAUT,
                           fc="#DFD8CB", ec="#7F6B4F", lw=1.0, hatch="///",
                           alpha=0.75))
    ax.text(L_BAIE / 2, H_BAIE + H_SOM + H_PRO + H_HAUT * 0.62,
            "MAÇONNERIE CONSERVÉE\nmeulière hourdée — 5,72 m sur deux niveaux",
            ha="center", va="center", fontsize=8, color="#4A3B26")

    # planchers
    for y, lab in ((H_TOT, "plancher haut R+1"),
                   (H_BAIE + H_SOM + H_PRO + 2.86, "plancher haut RDC")):
        ax.plot([-0.55, L_BAIE + 0.55], [y, y], color=GRIS, lw=2.4)
        ax.plot([-0.55, L_BAIE + 0.55], [y - 0.10, y - 0.10], color=GRIS, lw=0.9)
        ax.text(L_BAIE + 0.62, y + 0.05, lab, fontsize=6.6, color=GRIS, ha="left")

    # fondation filante conservee
    ax.add_patch(Rectangle((-0.30, -0.38), L_BAIE + 0.60, 0.28, fc="#BFBFBF",
                           ec="#5B4A33", lw=1.0, hatch="...."))
    ax.plot([-0.75, L_BAIE + 0.75], [0.0, 0.0], color="#5B4A33", lw=1.3)
    ax.text(L_BAIE / 2, -0.55, "FONDATION FILANTE EN MEULIÈRE — intégralement "
            "conservée (H-01)", ha="center", fontsize=7.2, color="#5B4A33")

    # etai
    ax.annotate("", xy=(0.10, H_BAIE + H_SOM + H_PRO),
                xytext=(0.10, H_BAIE + H_SOM + H_PRO - 0.55),
                arrowprops=dict(arrowstyle="<|-", lw=1.6, color=ROUGE))
    ax.text(0.10, H_BAIE + H_SOM + H_PRO - 0.66, "étaiement", fontsize=6.6,
            color=ROUGE, ha="left")

    # cotes
    def cote_h(xa, xb, y, txt):
        ax.annotate("", xy=(xa, y), xytext=(xb, y),
                    arrowprops=dict(arrowstyle="<->", lw=0.7))
        ax.text((xa + xb) / 2, y + 0.07, txt, ha="center", fontsize=7.2)

    def cote_v(ya, yb, x, txt):
        ax.annotate("", xy=(x, ya), xytext=(x, yb),
                    arrowprops=dict(arrowstyle="<->", lw=0.7))
        ax.text(x - 0.10, (ya + yb) / 2, txt, rotation=90, ha="right",
                va="center", fontsize=7.2)

    cote_h(0, L_BAIE, -0.95, "3,80 (D2)")
    cote_v(0, H_BAIE, -0.45, "2,15")
    cote_v(H_BAIE, H_BAIE + H_SOM, -0.45, "")
    cote_v(H_BAIE + H_SOM, H_BAIE + H_SOM + H_PRO, -0.45, "")
    cote_v(H_BAIE + H_SOM + H_PRO, H_TOT, -0.45, "5,72")
    ax.text(-0.62, H_BAIE + (H_SOM + H_PRO) / 2, "0,40 + 0,20", rotation=90,
            ha="right", va="center", fontsize=6.6)

    ax.set_xlim(-1.05, L_BAIE + 1.90)
    ax.set_ylim(-1.15, H_TOT + 0.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Reprise en sous-œuvre type — élévation sur baie de façade (D2, D4, D6)",
                 fontsize=9.5, color=BLEU, pad=8)

    from matplotlib.patches import Patch
    leg = [Patch(fc="#BDD7EE", ec=BLEU2, label="jambage BA"),
           Patch(fc="#9DC3E6", ec=BLEU2, label="sommier BA"),
           Patch(fc="#F4B183", ec="#C55A11", label="profilé S355"),
           Patch(fc="#DFD8CB", ec="#7F6B4F", hatch="///", label="maçonnerie conservée"),
           Patch(fc="#BFBFBF", ec="#5B4A33", hatch="....", label="fondation conservée")]
    ax.legend(handles=leg, loc="upper center", bbox_to_anchor=(0.5, -0.02),
              fontsize=6.8, frameon=False, ncol=5, columnspacing=1.2,
              handlelength=1.6)

    fig.tight_layout()
    p = os.path.join(OUT, "fig12_schema_rso.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p


# ---------------------------------------------------------------------------
# Fig. 4 — Plan de fondation de l'extension
# ---------------------------------------------------------------------------
def fig_plan_fondation():
    """Plan de fondation de l'extension (schéma E-02 du 11/11/2026).

    Terrasse 8,03 x 2,00 m, poutre-acrotère comprise. La poutre de 8,03 m
    court en limite de dalle, à 2,00 m du nu de façade ; elle est isostatique
    entre le voile de rive à créer et l'about de la poutre perpendiculaire,
    qui franchit 1,30 m depuis la façade puis se poursuit en console de
    0,70 m sur le poteau BA 25 x 25.
    """
    r = _load()["extension"]
    L = 8.03
    P = 2.00                       # profondeur de terrasse
    YP = 1.70                      # nu intérieur de la poutre (axe 1,85)
    XP = 1.30                      # axe du poteau depuis le nu de façade
    fig, ax = plt.subplots(figsize=(10.6, 5.4))

    # façade existante
    ax.add_patch(Rectangle((0, 0), L, 0.49, fc="#D9D2C6", ec="#7F6B4F",
                           hatch="///", alpha=0.55, lw=1.2))
    ax.text(L / 2, 0.26, "façade existante — meulière ép. 49 cm", ha="center",
            va="center", fontsize=7.5, color="#5B4A33")

    # dalle de terrasse
    ax.add_patch(Rectangle((0, -P), L, P, fc="#F2F7FC", ec=BLEU2,
                           lw=1.0, ls="--"))
    ax.text(5.55, -0.72, "TERRASSE 8,03 × 2,00 m — poutre comprise",
            ha="center", va="center", fontsize=7.2, color=BLEU)

    # poutre-acrotère de rive (limite de dalle)
    ax.add_patch(Rectangle((0, -P), L, 0.30, fc="#F8CBD6", ec=ROUGE, lw=1.4))
    ax.text(4.35, -P + 0.15, "poutre-acrotère BA 30 × 67 — arase NGF 44,75",
            ha="center", va="center", fontsize=7.2, color=ROUGE)

    # poutre perpendiculaire (travée 1,30 + console 0,70)
    ax.add_patch(Rectangle((0, -P), 0.25, P, fc="#FBE3EA", ec=ROUGE, lw=1.1))
    ax.annotate("poutre perpendiculaire 25 × 67",
                xy=(0.30, -0.95), xytext=(0.75, -0.95), fontsize=6.9,
                color=ROUGE, va="center",
                arrowprops=dict(arrowstyle="->", lw=0.7, color=ROUGE))

    # poteau BA
    ax.add_patch(Rectangle((0, -XP - 0.125), 0.25, 0.25, fc=BLEU,
                           ec="black", lw=0.8, zorder=7))
    ax.annotate("poteau BA 25 × 25 — à 1,30 m du nu de façade (E-02)",
                xy=(0.27, -XP), xytext=(1.55, -1.42),
                fontsize=6.9, color=BLEU, ha="left",
                bbox=dict(fc="white", ec="none", pad=1.0),
                arrowprops=dict(arrowstyle="->", lw=0.8, color=BLEU))

    # voile de rive à créer + semelle filante
    ax.add_patch(Rectangle((L, -P), 0.20, P, fc="#BDD7EE", ec=BLEU2, lw=1.2))
    ax.add_patch(Rectangle((L - 0.225, -P), 0.65, 0.30, fc="none", ec=BLEU2,
                           lw=1.0, ls=(0, (4, 2))))
    ax.annotate("voile de rive BA 20 cm À CRÉER\nsur semelle filante 65 × 30",
                xy=(L + 0.20, -1.45), xytext=(L + 0.42, -2.05),
                fontsize=6.9, color=BLEU, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.8, color=BLEU))

    # puits
    for (cx, cy, d, lab) in [(0.125, -XP, r["puits_1"]["D"], "puits n° 1"),
                             (L + 0.10, -0.55, r["puits_2"]["D"],
                              "puits n° 2")]:
        ax.add_patch(Circle((cx, cy), d / 2, fc="none", ec="#806000", lw=1.4,
                            ls="-.", zorder=5))
        ax.text(cx, cy + d / 2 + 0.06, lab, ha="center", va="bottom",
                fontsize=6.6, color="#806000",
                bbox=dict(fc="white", ec="none", pad=1.0))

    # cotes
    ax.annotate("", xy=(0, 0.78), xytext=(L, 0.78),
                arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(L / 2, 0.85, "8,03 m", ha="center", fontsize=8)
    ax.annotate("", xy=(-0.95, 0), xytext=(-0.95, -P),
                arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(-1.05, -P / 2, "2,00 m", rotation=90, ha="right", va="center",
            fontsize=8)
    ax.annotate("", xy=(-0.50, 0), xytext=(-0.50, -YP),
                arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(-0.60, -YP / 2, "1,70", rotation=90, ha="right", va="center",
            fontsize=7.4)
    xd = 2.30
    for y0, y1, txt in [(0, -XP, "1,30"), (-XP, -P, "0,70")]:
        ax.annotate("", xy=(xd, y1), xytext=(xd, y0),
                    arrowprops=dict(arrowstyle="<->", lw=0.7, color=GRIS))
        ax.text(xd + 0.09, (y0 + y1) / 2, txt, ha="left", va="center",
                fontsize=7.0, color=GRIS)

    # joint de dilatation façade
    ax.plot([0, L], [-0.02, -0.02], color=VERT, lw=1.6, ls=(0, (3, 2)))
    ax.annotate("joint de dilatation 20 mm", xy=(2.4, -0.02), xytext=(2.2, 0.62),
                fontsize=6.6, color=VERT,
                arrowprops=dict(arrowstyle="->", lw=0.7, color=VERT))

    ax.set_xlim(-1.6, L + 2.55)
    ax.set_ylim(-2.55, 1.10)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Plan de fondation de l'extension — poutre-acrotère en limite de "
                 "dalle, poteau BA à 1,30 m, voile de rive à créer",
                 fontsize=9.4, color=BLEU, pad=8)

    fig.tight_layout()
    p = os.path.join(OUT, "fig13_plan_fondation.png")
    fig.savefig(p, dpi=200, facecolor="white")
    plt.close(fig)
    return p


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in (fig_poutre_efforts, fig_coupe_poutre, fig_schema_rso,
              fig_plan_fondation):
        print(f())


if __name__ == "__main__":
    main()
