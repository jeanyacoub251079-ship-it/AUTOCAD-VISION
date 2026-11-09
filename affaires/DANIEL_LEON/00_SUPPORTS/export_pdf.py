#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export PDF (A1, 1/50) + aperçu PNG de la planche DXF.

Le DXF est en millimètres réels (1 unité = 1 mm). À l'échelle 1/50, la feuille
A1 (841 x 594 mm) représente 42.05 x 29.70 m de modèle : le cadre tracé dans
le DXF correspond exactement à cette surface.

Usage :
    python export_pdf.py PLAN.dxf [--pdf sortie.pdf] [--png sortie.png]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import ezdxf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt                                     # noqa: E402
from ezdxf.addons.drawing import Frontend, RenderContext             # noqa: E402
from ezdxf.addons.drawing.config import (BackgroundPolicy,          # noqa: E402
                                         Configuration)
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend        # noqa: E402

A1 = (841 / 25.4, 594 / 25.4)          # pouces (matplotlib)
VIEW = (-4.00e3, 38.05e3, -6.00e3, 23.70e3)   # cadre A1 au 1/50 (mm modèle)


def render(dxf_path: Path, out_png: Path, out_pdf: Path | None, dpi=150):
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    fig = plt.figure(figsize=A1, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(VIEW[0], VIEW[1])
    ax.set_ylim(VIEW[2], VIEW[3])
    ax.set_aspect("equal")
    ax.axis("off")
    ctx = RenderContext(doc)
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(msp)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=dpi, facecolor="white")
    if out_pdf:
        fig.savefig(out_pdf, format="pdf", facecolor="white")
        print("PDF :", out_pdf)
    print("PNG :", out_png)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dxf")
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--png", default=None)
    a = ap.parse_args()
    dxf = Path(a.dxf)
    base = dxf.with_suffix("")
    render(dxf,
           Path(a.png) if a.png else base.with_name(base.name + "_apercu.png"),
           Path(a.pdf) if a.pdf else base.with_name(base.name + "_A1.pdf"))


if __name__ == "__main__":
    main()
