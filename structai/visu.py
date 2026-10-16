"""Rendus visuels d'une option (PNG pour PDF/dashboards ; le frontend a son
propre SVG interactif)."""
from __future__ import annotations

from pathlib import Path

COLORS = {"poteau": "#c0392b", "poutre": "#2980b9", "voile": "#16a085",
          "dalle": "#95a5a6", "fondation": "#8e44ad", "semelle": "#8e44ad"}


def render_option_png(option: dict, out_path: Path, title: str = "", dpi: int = 160) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    st = option.get("structure", {})
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_aspect("equal")
    ax.axis("off")
    for d in st.get("dalles", []):
        poly = d.get("polygone", [])
        if len(poly) >= 3:
            xs = [p[0] for p in poly] + [poly[0][0]]
            ys = [p[1] for p in poly] + [poly[0][1]]
            ax.fill(xs, ys, color=COLORS["dalle"], alpha=0.18)
            ax.plot(xs, ys, color=COLORS["dalle"], linewidth=0.7, alpha=0.6)
    for w in st.get("voiles", []):
        ax.plot([w["debut"][0], w["fin"][0]], [w["debut"][1], w["fin"][1]],
                color=COLORS["voile"], linewidth=max(1, w.get("epaisseur", 0.2) * 30), alpha=0.8)
    for b in st.get("poutres", []):
        lw = 1 + b["section"][0] * 6
        ax.plot([b["debut"][0], b["fin"][0]], [b["debut"][1], b["fin"][1]],
                color=COLORS["poutre"], linewidth=lw, alpha=0.75)
    for f in st.get("fondations", []):
        if f.get("type") == "radier":
            continue
        pos = None
        for c in st.get("poteaux", []):
            if c["id"] == f.get("poteau"):
                pos = c["position"]
                break
        if pos:
            B, L = f.get("dimensions", [1.5, 1.5, 0.4])[:2]
            ax.add_patch(plt.Rectangle((pos[0] - B / 2, pos[1] - L / 2), B, L,
                                       fill=False, edgecolor=COLORS["fondation"], linewidth=1.2))
    for c in st.get("poteaux", []):
        w, h = c.get("section", [0.3, 0.3])
        ax.add_patch(plt.Rectangle((c["position"][0] - w / 2, c["position"][1] - h / 2),
                                   w, h, color=COLORS["poteau"]))
        ax.annotate(c["id"], xy=(c["position"][0] + w / 2 + 0.1, c["position"][1]),
                    fontsize=5.5, color="#333")
    ind = option.get("indicateurs", {}) or {}
    ax.set_title(title or f"Option {option.get('id','')}", fontsize=9)
    ax.text(0.01, -0.02, f"taux max {ind.get('taux_travail_max', '—')} · béton "
            f"{ind.get('volume_beton_m3', '—')} m³ · acier {ind.get('masse_acier_kg', '—')} kg",
            transform=ax.transAxes, fontsize=6.5, color="#555")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_path), dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path


def render_option_iso_svg(option: dict) -> str:
    """Projection isométrique simple (SVG) pour l'aperçu 3D du frontend."""
    st = option.get("structure", {})
    h = 2.8
    levels = sorted({int(b.get("niveau", 1)) for b in st.get("poutres", [])} |
                    {int(d.get("niveau", 1)) for d in st.get("dalles", [])} or {1})
    def proj(x, y, z):
        sx = (x - y) * 40
        sy = (x + y) * 20 - z * 34
        return sx, sy
    parts = []
    off = 0.0
    xmin = ymin = 1e9
    raw: list[tuple] = []
    for lvl in levels:
        z = lvl * h
        for b in st.get("poutres", []):
            if int(b.get("niveau", 1)) != lvl:
                continue
            p1 = proj(b["debut"][0], b["debut"][1], z)
            p2 = proj(b["fin"][0], b["fin"][1], z)
            raw.append(("L", p1, p2, "#2980b9"))
        for d in st.get("dalles", []):
            if int(d.get("niveau", 1)) != lvl:
                continue
            poly = [proj(p[0], p[1], z) for p in d.get("polygone", [])]
            if len(poly) >= 3:
                raw.append(("P", poly, None, "rgba(149,165,166,.12)"))
        for c in st.get("poteaux", []):
            lv = c.get("niveaux", [0, 0])
            if not (min(lv) <= lvl - 1 <= max(lv)):
                continue
            x, y = c["position"]
            p1 = proj(x, y, (lvl - 1) * h)
            p2 = proj(x, y, lvl * h)
            raw.append(("L", p1, p2, "#c0392b"))
    for r in raw:
        if r[0] == "L":
            (x1, y1), (x2, y2) = r[1], r[2]
            for pt in ((x1, y1), (x2, y2)):
                xmin = min(xmin, pt[0]); ymin = min(ymin, pt[1])
    for r in raw:
        if r[0] == "L":
            (x1, y1), (x2, y2) = r[1], r[2]
            parts.append(f'<line x1="{x1 - xmin + 30:.1f}" y1="{y1 - ymin + 30:.1f}" '
                         f'x2="{x2 - xmin + 30:.1f}" y2="{y2 - ymin + 30:.1f}" '
                         f'stroke="{r[3]}" stroke-width="2"/>')
        else:
            poly, col = r[1], r[3]
            pts = " ".join(f"{p[0] - xmin + 30:.1f},{p[1] - ymin + 30:.1f}" for p in poly)
            parts.append(f'<polygon points="{pts}" fill="{col}" stroke="#95a5a6" stroke-width="0.5"/>')
    w = hgt = 300
    if raw:
        xs = []
        for r in raw:
            if r[0] == "L":
                xs += [r[1][0], r[2][0], r[1][1], r[2][1]]
            else:
                xs += [p[0] for p in r[1]] + [p[1] for p in r[1]]
        w = max(200, int(max(xs) - min(xs)) + 80)
        hgt = max(160, int(w * 0.6))
    return (f'<svg viewBox="0 0 {w} {hgt}" width="100%" xmlns="http://www.w3.org/2000/svg">'
            + "".join(parts) + "</svg>")
