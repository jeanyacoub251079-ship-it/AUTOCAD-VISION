"""
Moteur de plans d'exécution — Affaire GARENNE (Tâche 3).

Principe : une **géométrie unique** est construite en centimètres modèle
(~1 cm de bâtiment = 1 unité interne), puis rendue par deux back-ends :

    * `DxfBackend`  -> fichier .dxf (ezdxf, calques normalisés, mm)
    * `PdfBackend`  -> page A3 paysage, échelle 1/50, cartouche BET

Les deux sorties partagent donc strictement la même description de dessin :
aucune divergence possible entre le .dxf et le .pdf livrés.

Calques normalisés imposés par le cahier des charges (§ livrables) :

    STR_EXISTANT       blanc      0.18   existant conservé
    STR_DEMOLITION     rouge      0.25   tirets
    STR_COFFRAGE_BA    magenta    0.50   coffrage béton armé + hachures
    STR_ACIER_PROFILS  magenta    0.50   profilés métalliques
    STR_FERRAILLAGE    magenta    0.40   armatures (hachures pleines)
    STR_COTATIONS_TEXTES blanc    0.25   cotes, textes (>= 2,5 mm)

Echelles : le modèle est en centimètres, la feuille A3 (420 x 297 mm) est
manipulée en millimètres. A 1/50, 1 m de bâtiment = 20 mm de papier, soit
1 cm modèle = 0,2 mm papier.
"""
from __future__ import annotations

import math
import os
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Constantes de mise en page
# ---------------------------------------------------------------------------

A3_W, A3_H = 420.0, 297.0          # mm
ECHELLE = 50.0                      # 1/50
MM_PAR_CM = 10.0 / ECHELLE          # 1 cm modèle = 0,2 mm papier à 1/50

# Calques normalisés : (couleur ACI, épaisseur mm, type de ligne)
CALQUES = {
    "STR_EXISTANT":       (7, 0.18, "CONTINUOUS"),
    "STR_DEMOLITION":     (1, 0.25, "DASHED"),
    "STR_COFFRAGE_BA":    (6, 0.50, "CONTINUOUS"),
    "STR_ACIER_PROFILS":  (6, 0.50, "CONTINUOUS"),
    "STR_FERRAILLAGE":    (6, 0.40, "CONTINUOUS"),
    "STR_COTATIONS_TEXTES": (7, 0.25, "CONTINUOUS"),
}
CALQUE_AXES = "STR_COTATIONS_TEXTES"

BLANC, ROUGE, MAGENTA, CYAN = 7, 1, 6, 4


# ---------------------------------------------------------------------------
# Primitives de dessin (coordonnées modèle, en cm)
# ---------------------------------------------------------------------------

@dataclass
class Scene:
    """Conteneur de primitives, indépendant du back-end."""
    items: list = field(default_factory=list)

    # -- tracés ------------------------------------------------------------
    def line(self, x1, y1, x2, y2, layer="STR_EXISTANT", lw=None):
        self.items.append(("line", (x1, y1), (x2, y2), layer, lw))

    def rect(self, x, y, w, h, layer="STR_COFFRAGE_BA", lw=None, fill=None,
             hatch=None, angle=45.0, spacing=1.2):
        self.items.append(("rect", (x, y), (w, h), layer, lw, fill, hatch,
                           angle, spacing))

    def poly(self, pts, layer="STR_EXISTANT", lw=None, closed=False,
             fill=None, hatch=None, angle=45.0, spacing=1.2):
        self.items.append(("poly", pts, layer, lw, closed, fill, hatch,
                           angle, spacing))

    def circle(self, cx, cy, r, layer="STR_COTATIONS_TEXTES", lw=None,
               fill=None, hatch=None):
        self.items.append(("circle", (cx, cy), r, layer, lw, fill, hatch))

    def arc(self, cx, cy, r, a1, a2, layer="STR_EXISTANT", lw=None):
        self.items.append(("arc", (cx, cy), r, a1, a2, layer, lw))

    def text(self, s, x, y, fontsize=2.5, layer="STR_COTATIONS_TEXTES",
             align="left", angle=0.0, bold=False):
        self.items.append(("text", s, (x, y), fontsize, layer, align, angle,
                           bold))

    # -- cotation ----------------------------------------------------------
    def dim_h(self, x1, x2, y, label=None, fontsize=2.6, layer=None,
              tick=0.35):
        """Cote horizontale entre x1 et x2, ligne de cote en y (modèle)."""
        layer = layer or CALQUE_AXES
        self.line(x1, y, x2, y, layer, lw=0.18)
        for x in (x1, x2):
            self.line(x, y - 0.30, x, y + 0.30, layer, lw=0.25)
            self.line(x - tick, y - tick, x + tick, y + tick, layer, lw=0.25)
        lab = label if label is not None else _fmt_cm(x2 - x1)
        self.text(lab, (x1 + x2) / 2.0, y + 0.42, fontsize, layer, "center")

    def dim_v(self, y1, y2, x, label=None, fontsize=2.6, layer=None,
              tick=0.35):
        layer = layer or CALQUE_AXES
        self.line(x, y1, x, y2, layer, lw=0.18)
        for y in (y1, y2):
            self.line(x - 0.30, y, x + 0.30, y, layer, lw=0.25)
            self.line(x - tick, y - tick, x + tick, y + tick, layer, lw=0.25)
        lab = label if label is not None else _fmt_cm(abs(y2 - y1))
        self.text(lab, x - 0.55, (y1 + y2) / 2.0, fontsize, layer, "center",
                  angle=90.0)

    def leader(self, txt, xt, yt, xa, ya, fontsize=2.4, layer=None,
               width=None):
        """Ligne d'appel depuis (xa, ya) vers le texte posé en (xt, yt)."""
        layer = layer or CALQUE_AXES
        self.line(xa, ya, xt, yt, layer, lw=0.18)
        self.circle(xa, ya, 0.18, layer, lw=0.18)
        self.text(txt, xt + (0.35 if xt >= xa else -0.35), yt, fontsize,
                  layer, "left" if xt >= xa else "right")


    # -- symboles normalisés BET ------------------------------------------
    def arrow(self, x, y, ang, size=1.6, layer=None):
        """Flèche pleine, pointe en (x, y), orientée selon `ang` (degrés)."""
        layer = layer or CALQUE_AXES
        a = math.radians(ang)
        L, w = size, size * 0.26
        pts = [(x, y),
               (x - L * math.cos(a) + w * math.sin(a),
                y - L * math.sin(a) - w * math.cos(a)),
               (x - L * math.cos(a) - w * math.sin(a),
                y - L * math.sin(a) + w * math.cos(a))]
        self.items.append(("arrow", pts, layer))

    def hatch_poly(self, pts, layer="STR_FERRAILLAGE", angle=45.0,
                   spacing=0.8):
        """Hachures bornées à un polygone quelconque."""
        self.items.append(("hatchpoly", list(pts), layer, angle, spacing))

    def hatch_rect(self, x, y, w, h, layer="STR_EXISTANT", angle=45.0,
                   spacing=0.8):
        self.hatch_poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)],
                        layer, angle, spacing)

    def dia(self, cx, cy, d, layer="STR_COTATIONS_TEXTES", lw=0.22):
        """Symbole de diamètre : cercle barré."""
        r = d / 2.0
        self.circle(cx, cy, r, layer, lw)
        self.line(cx - r * 0.707, cy - r * 0.707,
                  cx + r * 0.707, cy + r * 0.707, layer, lw)

    def bar(self, pts, label=None, layer="STR_FERRAILLAGE", lw=0.35,
            fs=2.1, hook=None):
        """Barre d'armature : polyligne + étiquette optionnelle.
        `hook` = ('start'|'end', angle) ajoute un crochet à 90°."""
        self.poly(pts, layer, lw, closed=False)
        if hook:
            ext, ang = hook
            if ext == "start":
                (x0, y0), (x1, y1) = pts[0], pts[1]
            else:
                (x0, y0), (x1, y1) = pts[-1], pts[-2]
            a = math.radians(ang)
            L = 8.0
            self.line(x1 - L * math.cos(a), y1 - L * math.sin(a), x1, y1,
                      layer, lw)
        if label:
            self.text(label, pts[0][0], pts[0][1] + 0.7, fs, layer)


# Dimensions des profilés (cm) : h, b, tw, tf
PROFILES = {
    "IPE 160": (16.0, 8.2, 0.50, 0.74),
    "IPE 180": (18.0, 9.1, 0.53, 0.80),
    "IPE 200": (20.0, 10.0, 0.56, 0.85),
    "IPE 270": (27.0, 13.5, 0.66, 1.02),
    "IPE 300": (30.0, 15.0, 0.71, 1.07),
    "UPN 200": (20.0, 7.5, 0.85, 1.15),
}


def section_pts(profil, x, y, form="I"):
    """Contour d'un profilé, posé en (x, y) = coin inférieur gauche."""
    h, b, tw, tf = PROFILES[profil]
    if form == "U":
        return [(x, y), (x + b, y), (x + b, y + tf), (x + tw, y + tf),
                (x + tw, y + h - tf), (x + b, y + h - tf), (x + b, y + h),
                (x, y + h)]
    return [(x, y), (x + b, y), (x + b, y + tf),
            (x + b / 2 + tw / 2, y + tf),
            (x + b / 2 + tw / 2, y + h - tf),
            (x + b, y + h - tf), (x + b, y + h), (x, y + h),
            (x, y + h - tf), (x + b / 2 - tw / 2, y + h - tf),
            (x + b / 2 - tw / 2, y + tf), (x, y + tf)]

def _fmt_cm(v):
    """Formate une cote en cm ; au-delà de 100 cm, conversion en mètres."""
    v = round(v, 1)
    if abs(v) >= 100 and abs(v - round(v)) < 0.05:
        m = v / 100.0
        s = f"{m:.2f}".rstrip("0").rstrip(".")
        return s.replace(".", ",") + " m"
    return f"{v:g}".replace(".", ",")


# ---------------------------------------------------------------------------
# Back-end DXF
# ---------------------------------------------------------------------------

class DxfBackend:
    """Rendu DXF (ezdxf). Le modèle est en centimètres -> 1 unité = 1 cm,
    on déclare $INSUNITS en mètres * 100 pour rester en cm lisibles."""

    def __init__(self, title, scale=ECHELLE):
        import ezdxf
        self.ezdxf = ezdxf
        self.doc = ezdxf.new("R2013", setup=True)
        self.doc.units = ezdxf.units.CM
        for name, (color, lw, ltype) in CALQUES.items():
            if name not in self.doc.layers:
                self.doc.layers.add(name, color=color, linetype=ltype)
            self.doc.layers.get(name).dxf.lineweight = int(lw * 100)
        self.msp = self.doc.modelspace()
        self.title = title

    def _attribs(self, layer, lw=None):
        color, lw0, _ = CALQUES.get(layer, (7, 0.25, "CONTINUOUS"))
        a = {"layer": layer}
        if lw:
            a["lineweight"] = int(max(lw, 0.05) * 100)
        return a

    def render(self, scene: Scene):
        msp = self.msp
        for it in scene.items:
            kind = it[0]
            if kind == "line":
                _, p1, p2, layer, lw = it
                msp.add_line(p1, p2, dxfattribs=self._attribs(layer, lw))
            elif kind == "rect":
                _, (x, y), (w, h), layer, lw, fill, hatch, angle, sp = it
                pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
                msp.add_lwpolyline(pts + [pts[0]],
                                   dxfattribs=self._attribs(layer, lw))
                if hatch:
                    self._hatch(pts, layer, hatch, angle, sp)
            elif kind == "poly":
                _, pts, layer, lw, closed, fill, hatch, angle, sp = it
                pp = list(pts) + ([pts[0]] if closed else [])
                msp.add_lwpolyline(pp, dxfattribs=self._attribs(layer, lw))
                if hatch:
                    self._hatch(list(pts), layer, hatch, angle, sp)
            elif kind == "circle":
                _, (cx, cy), r, layer, lw, fill, hatch = it
                msp.add_circle((cx, cy), r, dxfattribs=self._attribs(layer, lw))
            elif kind == "arc":
                _, (cx, cy), r, a1, a2, layer, lw = it
                msp.add_arc((cx, cy), r, a1, a2,
                            dxfattribs=self._attribs(layer, lw))
            elif kind == "arrow":
                _, pts, layer = it
                msp.add_solid([pts[0], pts[1], pts[2], pts[2]],
                              dxfattribs={"layer": layer})
            elif kind == "hatchpoly":
                _, pts, layer, angle, sp = it
                self._hatch(pts, layer, "ANSI31", angle, sp)
            elif kind == "text":
                _, s, (x, y), size, layer, align, angle, bold = it
                mt = msp.add_mtext(
                    s.replace("\n", "\\P"),
                    dxfattribs={"layer": layer,
                                "char_height": size * 0.75,
                                "attachment_point": _MT_ATTACH[align],
                                "rotation": angle})
                mt.dxf.insert = (x, y)

    def _hatch(self, pts, layer, pattern, angle, spacing):
        try:
            h = self.msp.add_hatch(color=8, dxfattribs={"layer": layer})
            h.set_pattern_fill(pattern or "ANSI31",
                               scale=max(0.05, spacing / 1.0),
                               angle=angle)
            h.paths.add_polyline_path(pts, is_closed=True)
        except Exception:
            # hachure non critique : on n'interrompt jamais le rendu
            pass

    def tableau(self, x, y, titre, header, rows, widths, size=2.35,
                hrow=6.0, hline=4.6):
        """Tableau simple (en-tête grisé) posé en (x, y) = coin supérieur G."""
        c = self._c
        W = sum(widths)
        H = hrow + hline * len(rows)
        c.setLineWidth(0.3)
        c.setFillColor(self.Color(0.90, 0.90, 0.90))
        c.rect(x, y - hrow, W, hrow, stroke=1, fill=1)
        c.setFillColor(self.Color(0, 0, 0))
        c.rect(x, y - H, W, H, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", size + 0.3)
        c.drawString(x, y + 1.6, titre)
        c.setFont("Helvetica-Bold", size)
        cx = x
        for w, htxt in zip(widths, header):
            c.drawString(cx + 1.2, y - hrow + 1.8, htxt)
            cx += w
            if cx < x + W:
                c.line(cx, y - H, cx, y)
        c.setFont("Helvetica", size)
        cy = y - hrow
        for row in rows:
            cy -= hline
            cx = x
            for w, val in zip(widths, row):
                c.drawString(cx + 1.2, cy + 1.4, str(val))
                cx += w
            c.setLineWidth(0.12)
            c.line(x, cy, x + W, cy)
            c.setLineWidth(0.3)

    def save(self, path):
        self.doc.saveas(path)
        return path


_MT_ATTACH = {"left": 7, "center": 8, "right": 9}


# ---------------------------------------------------------------------------
# Back-end PDF (A3 paysage) — dessin vectoriel direct, échelle exacte
# ---------------------------------------------------------------------------

class PdfBackend:
    """Rendu PDF A3 paysage au 1/50 avec cartouche BET.

    Le repère papier est en millimètres, origine en bas à gauche.
    `X(x), Y(y)` transforment une coordonnée modèle (cm) en papier (mm).
    """

    def __init__(self, title, cartouche, scale=ECHELLE,
                 origin=(30.0, 55.0)):
        from reportlab.pdfgen import canvas
        from reportlab.lib.colors import Color
        self.Color = Color
        self.scale = scale
        self.k = 10.0 / scale                    # mm papier par cm modèle
        self.x0, self.y0 = origin                # origine du repère modèle
        self.title = title
        self.title_txt = ""
        self.title_sub = ""
        self.cartouche = cartouche
        self.canvas_mod = canvas
        import io
        self._buf = io.BytesIO()
        self._c = None
        self._colors = {
            "STR_EXISTANT": Color(0.18, 0.18, 0.18),
            "STR_DEMOLITION": Color(0.75, 0.05, 0.05),
            "STR_COFFRAGE_BA": Color(0.75, 0.0, 0.55),
            "STR_ACIER_PROFILS": Color(0.75, 0.0, 0.55),
            "STR_FERRAILLAGE": Color(0.75, 0.0, 0.55),
            "STR_COTATIONS_TEXTES": Color(0.10, 0.10, 0.10),
        }

    def X(self, x):
        return self.x0 + x * self.k

    def Y(self, y):
        return self.y0 + y * self.k

    def bbox(self, scene):
        xs, ys = [], []
        for it in scene.items:
            k = it[0]
            if k == "line":
                xs += [it[1][0], it[2][0]]; ys += [it[1][1], it[2][1]]
            elif k == "rect":
                xs += [it[1][0], it[1][0] + it[2][0]]
                ys += [it[1][1], it[1][1] + it[2][1]]
            elif k == "poly":
                for (a, b) in it[1]:
                    xs.append(a); ys.append(b)
            elif k == "circle":
                xs += [it[1][0] - it[2], it[1][0] + it[2]]
                ys += [it[1][1] - it[2], it[1][1] + it[2]]
            elif k == "arc":
                xs += [it[1][0] - it[2], it[1][0] + it[2]]
                ys += [it[1][1] - it[2], it[1][1] + it[2]]
            elif k == "text":
                s_, (tx, ty), fs_, al_ = it[1], it[2], it[3], it[5]
                n = max(len(x) for x in s_.split("\n"))
                tw = n * fs_ * 0.52
                if al_ == "center":
                    xs += [tx - tw / 2, tx + tw / 2]
                elif al_ == "right":
                    xs += [tx - tw, tx]
                else:
                    xs += [tx, tx + tw]
                nl = s_.count("\n") + 1
                ys += [ty - fs_ * 1.15 * (nl - 1) - fs_, ty]
            elif k == "arrow":
                for (a, b) in it[1]:
                    xs.append(a); ys.append(b)
            elif k == "hatchpoly":
                for (a, b) in it[1]:
                    xs.append(a); ys.append(b)
            elif k in ("dim_h",):
                xs += [it[1], it[2]]; ys.append(it[3])
            elif k in ("dim_v",):
                ys += [it[1], it[2]]; xs.append(it[3])
        return min(xs), min(ys), max(xs), max(ys)

    def place(self, scene, x_left, y_bottom, scale=None):
        """Place la scène pour que sa bbox commence en (x_left, y_bottom)."""
        if scale:
            self.k = 10.0 / scale
        x0, y0, _, _ = self.bbox(scene)
        self.set_origin(x_left - x0 * self.k, y_bottom - y0 * self.k)

    def set_origin(self, x0, y0):
        self.x0, self.y0 = x0, y0

    def _set(self, layer, lw=None):
        color, lw0, ltype = CALQUES.get(layer, (7, 0.25, "CONTINUOUS"))
        self._c.setStrokeColor(self._colors.get(layer, self.Color(0, 0, 0)))
        self._c.setLineWidth(lw if lw else lw0)
        if ltype == "DASHED":
            self._c.setDash([2.0, 1.4])
        else:
            self._c.setDash([])

    def render(self, scene: Scene):
        for it in scene.items:
            kind = it[0]
            if kind == "line":
                _, p1, p2, layer, lw = it
                self._set(layer, lw)
                self._c.line(self.X(p1[0]), self.Y(p1[1]),
                             self.X(p2[0]), self.Y(p2[1]))
            elif kind == "rect":
                _, (x, y), (w, h), layer, lw, fill, hatch, angle, sp = it
                self._set(layer, lw)
                self._c.rect(self.X(x), self.Y(y), w * self.k, h * self.k)
                if fill:
                    c = self._colors.get(layer, self.Color(0.8, 0.8, 0.8))
                    self._c.setFillColor(c)
                    self._c.setFillAlpha(0.10)
                    self._c.rect(self.X(x), self.Y(y), w * self.k, h * self.k,
                                 stroke=0, fill=1)
                    self._c.setFillAlpha(1)
                if hatch:
                    self._hatch_rect(x, y, w, h, layer, angle, sp)
            elif kind == "poly":
                _, pts, layer, lw, closed, fill, hatch, angle, sp = it
                self._set(layer, lw)
                p = self._c.beginPath()
                p.moveTo(self.X(pts[0][0]), self.Y(pts[0][1]))
                for (px, py) in pts[1:]:
                    p.lineTo(self.X(px), self.Y(py))
                if closed:
                    p.close()
                if fill:
                    c = self._colors.get(layer, self.Color(0.8, 0.8, 0.8))
                    self._c.setFillColor(c)
                    self._c.setFillAlpha(0.12)
                    self._c.drawPath(p, stroke=1, fill=1)
                    self._c.setFillAlpha(1)
                else:
                    self._c.drawPath(p, stroke=1, fill=0)
            elif kind == "circle":
                _, (cx, cy), r, layer, lw, fill, hatch = it
                self._set(layer, lw)
                self._c.circle(self.X(cx), self.Y(cy), r * self.k)
            elif kind == "arc":
                _, (cx, cy), r, a1, a2, layer, lw = it
                self._set(layer, lw)
                rx = r * self.k
                self._c.arc(self.X(cx) - rx, self.Y(cy) - rx,
                            self.X(cx) + rx, self.Y(cy) + rx, a1, a2 - a1)
            elif kind == "arrow":
                _, pts, layer = it
                self._c.setFillColor(self._colors.get(layer,
                                                      self.Color(0, 0, 0)))
                p = self._c.beginPath()
                p.moveTo(self.X(pts[0][0]), self.Y(pts[0][1]))
                for (px, py) in pts[1:]:
                    p.lineTo(self.X(px), self.Y(py))
                p.close()
                self._c.drawPath(p, stroke=0, fill=1)
            elif kind == "hatchpoly":
                _, pts, layer, angle, sp = it
                self._hatch_path(pts, layer, angle, sp)
            elif kind == "text":
                _, s, (x, y), size, layer, align, angle, bold = it
                self._set(layer)
                self._c.setFillColor(self._colors.get(layer,
                                                      self.Color(0, 0, 0)))
                self._c.setFont("Helvetica-Bold" if bold else "Helvetica",
                                max(1.6, size))
                lines = s.split("\n")
                if align == "center":
                    for i, ln in enumerate(lines):
                        self._c.drawCentredString(self.X(x), self.Y(y)
                                                  - i * size * 1.15, ln)
                elif align == "right":
                    for i, ln in enumerate(lines):
                        self._c.drawRightString(self.X(x), self.Y(y)
                                                - i * size * 1.15, ln)
                else:
                    for i, ln in enumerate(lines):
                        self._c.drawString(self.X(x), self.Y(y)
                                           - i * size * 1.15, ln)

    def _hatch_path(self, pts, layer, angle, sp):
        """Hachures parallèles bornées à un polygone (clipping PDF)."""
        c = self._c
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        self._set(layer)
        th = math.radians(angle)
        dx, dy = math.cos(th), math.sin(th)
        nx, ny = -dy, dx
        proj = [p[0] * nx + p[1] * ny for p in pts]
        lo, hi = min(proj), max(proj)
        span = max(xs) - min(xs) + max(ys) - min(ys) + 20
        c.saveState()
        p = c.beginPath()
        p.moveTo(self.X(pts[0][0]), self.Y(pts[0][1]))
        for (px, py) in pts[1:]:
            p.lineTo(self.X(px), self.Y(py))
        p.close()
        c.clipPath(p, stroke=0, fill=0)
        c.setLineWidth(0.13)
        cx0 = sum(xs) / len(xs)
        cy0 = sum(ys) / len(ys)
        s = lo
        while s < hi:
            bx, by = cx0 + nx * (s - (cx0 * nx + cy0 * ny)), \
                cy0 + ny * (s - (cx0 * nx + cy0 * ny))
            c.line(self.X(bx - dx * span), self.Y(by - dy * span),
                   self.X(bx + dx * span), self.Y(by + dy * span))
            s += sp
        c.restoreState()

    def _hatch_rect(self, x, y, w, h, layer, angle, sp):
        """Hachures parallèles bornées au rectangle (clipping par calcul)."""
        self._set(layer)
        th = math.radians(angle)
        dx, dy = math.cos(th), math.sin(th)
        nx, ny = -dy, dx
        corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        proj = [c[0] * nx + c[1] * ny for c in corners]
        lo, hi = min(proj), max(proj)
        s = math.ceil(lo / sp) * sp
        p = self._c.beginPath()
        while s < hi:
            cx, cy = nx * s, ny * s
            # intersections de la droite avec le rectangle
            ts = []
            for (px, py), (qx, qy) in zip(corners, corners[1:] + corners[:1]):
                ex, ey = qx - px, qy - py
                den = dx * ey - dy * ex
                if abs(den) < 1e-9:
                    continue
                t = ((px - cx) * ey - (py - cy) * ex) / den
                u = ((px - cx) * dy - (py - cy) * dx) / den
                if -1e-9 <= u <= 1 + 1e-9:
                    ts.append(t)
            if len(ts) >= 2:
                t1, t2 = min(ts), max(ts)
                p.moveTo(self.X(cx + t1 * dx), self.Y(cy + t1 * dy))
                p.lineTo(self.X(cx + t2 * dx), self.Y(cy + t2 * dy))
            s += sp
        self._c.setLineWidth(0.13)
        self._c.drawPath(p, stroke=1, fill=0)

    # -- feuille, cartouche ------------------------------------------------
    def new_page(self):
        self._c = self.canvas_mod.Canvas(self._buf, pagesize=(A3_W * 2.8346,
                                                             A3_H * 2.8346))
        self._c.scale(2.8346, 2.8346)     # -> millimètres
        self._frame()
        return self._c

    def add_page(self, cartouche=None):
        """Nouvelle planche dans le même document (après showPage)."""
        if cartouche:
            self.cartouche = cartouche
        self._c.showPage()
        self._c.scale(2.8346, 2.8346)
        self._frame()
        return self._c

    def _frame(self):
        c = self._c
        c.setStrokeColor(self.Color(0, 0, 0))
        c.setLineWidth(0.7)
        c.rect(10, 10, A3_W - 20, A3_H - 20)
        c.setLineWidth(0.25)
        c.rect(12, 12, A3_W - 24, A3_H - 24)
        # cartouche
        self._cartouche(c, A3_W - 12 - 175, 12, 175, 48)

    def _cartouche(self, c, x, y, w, h):
        info = self.cartouche
        c.setLineWidth(0.5)
        c.rect(x, y, w, h)
        c.setLineWidth(0.2)
        rows = [0, 12, 24, 34, 41]
        for r in rows[1:]:
            c.line(x, y + r, x + w, y + r)
        c.line(x + 95, y, x + 95, y + h)
        c.setFont("Helvetica-Bold", 3.4)
        c.drawString(x + 2.5, y + h - 6.0, "BET STRUCTURE — DOSSIER D'EXÉCUTION")
        c.setFont("Helvetica", 2.8)
        c.drawString(x + 2.5, y + 24 + 6.5, info.get("affaire", ""))
        c.drawString(x + 2.5, y + 24 + 2.0, info.get("adresse", ""))
        c.setFont("Helvetica-Bold", 3.6)
        tt = info.get("titre", "")
        while c.stringWidth(tt, "Helvetica-Bold", 3.6) > 88 and len(tt) > 8:
            tt = tt[:-1]
        c.drawString(x + 2.5, y + 12 + 4.2, tt)
        c.setFont("Helvetica", 2.3)
        sous = info.get("sous_titre", "")
        if len(sous) > 74:
            mots, lignes, cur = sous.split(), [], ""
            for m in mots:
                if len(cur) + len(m) + 1 > 74:
                    lignes.append(cur)
                    cur = m
                else:
                    cur = (cur + " " + m).strip()
            lignes.append(cur)
            for i, ln in enumerate(lignes[:2]):
                c.drawString(x + 2.5, y + 4.0 - i * 3.2, ln)
        else:
            c.drawString(x + 2.5, y + 3.0, sous)
        # colonne de droite
        c.setFont("Helvetica-Bold", 3.2)
        c.drawString(x + 97.5, y + h - 6.0, info.get("repere", ""))
        c.setFont("Helvetica", 2.6)
        c.drawString(x + 97.5, y + 34 + 3.0, info.get("phase", ""))
        c.drawString(x + 97.5, y + 24 + 6.5,
                     info.get("echelle", f"Échelle : 1/{int(ECHELLE)}"))
        c.drawString(x + 97.5, y + 24 + 2.0, info.get("format", "A3 paysage"))
        c.drawString(x + 97.5, y + 12 + 4.0, info.get("indice", ""))
        c.drawString(x + 97.5, y + 3.0, info.get("date", ""))

    def titre(self, txt, sous=""):
        self.title_txt, self.title_sub = txt, sous
        c = self._c
        c.setFont("Helvetica-Bold", 4.6)
        c.drawString(16, A3_H - 22, txt)
        if sous:
            c.setFont("Helvetica-Oblique", 2.9)
            c.drawString(16, A3_H - 27.5, sous)

    def vtitle(self, x, y, txt, size=2.9):
        """Titre de cadre, aligné à gauche en (x, y)."""
        c = self._c
        c.setFillColor(self.Color(0, 0, 0))
        c.setFont("Helvetica-Bold", size)
        c.drawString(x, y, txt)

    def frame(self, x, y, w, h, titre=None):
        """Cadre de détail + titre au-dessus."""
        c = self._c
        c.setStrokeColor(self.Color(0.35, 0.35, 0.35))
        c.setLineWidth(0.3)
        c.rect(x, y, w, h)
        if titre:
            self.vtitle(x, y + h + 3.2, titre)

    def legende(self, x, y, items):
        """items = [(layer, libellé, type_trait)] — type_trait: line/hatch."""
        c = self._c
        c.setFont("Helvetica-Bold", 2.8)
        c.drawString(x, y, "LÉGENDE")
        yy = y - 6
        for layer, lib, style in items:
            self._set(layer)
            if style == "hatch":
                n = 5
                for i in range(n):
                    c.line(x, yy + i * 1.1, x + 7, yy + i * 1.1 + 2.2)
            elif style == "dashed":
                c.setDash([2.0, 1.2])
                c.line(x, yy + 1.1, x + 7, yy + 1.1)
                c.setDash([])
            else:
                c.line(x, yy + 1.1, x + 7, yy + 1.1)
            c.setFillColor(self.Color(0, 0, 0))
            c.setFont("Helvetica", 2.5)
            c.drawString(x + 9, yy + 0.2, lib)
            yy -= 5.4

    def note_block(self, x, y, titre, lignes, width=95.0):
        c = self._c
        c.setLineWidth(0.3)
        h = 6.5 + 4.2 * len(lignes)
        c.rect(x, y - h, width, h)
        c.setFont("Helvetica-Bold", 2.7)
        c.drawString(x + 2, y - 5.0, titre)
        c.setFont("Helvetica", 2.4)
        for i, ln in enumerate(lignes):
            c.drawString(x + 2, y - 9.5 - i * 4.2, ln)

    def tableau(self, x, y, titre, header, rows, widths, size=2.35,
                hrow=6.0, hline=4.6):
        """Tableau simple (en-tête grisé) posé en (x, y) = coin supérieur G."""
        c = self._c
        W = sum(widths)
        H = hrow + hline * len(rows)
        c.setLineWidth(0.3)
        c.setFillColor(self.Color(0.90, 0.90, 0.90))
        c.rect(x, y - hrow, W, hrow, stroke=1, fill=1)
        c.setFillColor(self.Color(0, 0, 0))
        c.rect(x, y - H, W, H, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", size + 0.3)
        c.drawString(x, y + 1.6, titre)
        c.setFont("Helvetica-Bold", size)
        cx = x
        for w, htxt in zip(widths, header):
            c.drawString(cx + 1.2, y - hrow + 1.8, htxt)
            cx += w
            if cx < x + W:
                c.line(cx, y - H, cx, y)
        c.setFont("Helvetica", size)
        cy = y - hrow
        for row in rows:
            cy -= hline
            cx = x
            for w, val in zip(widths, row):
                c.drawString(cx + 1.2, cy + 1.4, str(val))
                cx += w
            c.setLineWidth(0.12)
            c.line(x, cy, x + W, cy)
            c.setLineWidth(0.3)

    def save(self, path):
        self._c.showPage()
        self._c.save()
        with open(path, "wb") as fh:
            fh.write(self._buf.getvalue())
        return path
