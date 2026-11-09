#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendu de contrôle d'un DXF en PNG (aperçu de la planche).

Usage :
    python render_dxf.py plan.dxf apercu.png [xmin xmax ymin ymax]

Dépendances : ezdxf + matplotlib (facultatif, usage de contrôle).
"""
from __future__ import annotations

import sys

import ezdxf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt                                   # noqa: E402
from ezdxf.addons.drawing import Frontend, RenderContext           # noqa: E402
from ezdxf.addons.drawing.config import (BackgroundPolicy,        # noqa: E402
                                         Configuration)
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend      # noqa: E402


def main():
    src, out = sys.argv[1], sys.argv[2]
    lims = [float(v) for v in sys.argv[3:7]] if len(sys.argv) > 6 else None
    doc = ezdxf.readfile(src)
    msp = doc.modelspace()
    fig = plt.figure(figsize=(20, 14), dpi=110)
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
    Frontend(ctx, MatplotlibBackend(ax), config=cfg).draw_layout(msp)
    if lims:
        ax.set_xlim(lims[0], lims[1])
        ax.set_ylim(lims[2], lims[3])
    ax.set_aspect("equal")
    fig.savefig(out, dpi=110, facecolor="white")
    print("ok", out)


if __name__ == "__main__":
    main()
