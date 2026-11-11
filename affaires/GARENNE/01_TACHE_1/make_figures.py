"""Generation des figures de la Tache 1 (extraits annotes des planches AARKA).

Les figures sont des recadrages a haute definition des planches PDF fournies,
avec les reperes de reprise en sous-oeuvre D1 a D6 reportes par le BET.
"""
from __future__ import annotations

import os
import pymupdf

SRC = ("google_drive/DOSSIER PROJET COUPES SUPPLEMENTAIRES DCE "
       "MAISON LAIGLE LA GARENNE COLOMBES 05112026.pdf")
OUT = "affaires/GARENNE/01_TACHE_1/figures"

# (page 1-based, clip dans l'espace page, dpi)
JOBS = {
    "fig01_rdc_demolitions": (1, (600, 140, 800, 470), 210),
    "fig02_rdc_projet_extension": (2, (600, 140, 800, 470), 210),
    "fig03_coupe03_projet": (8, (100, 60, 900, 860), 190),
    "fig04_coupe02_projet": (6, (100, 60, 900, 860), 190),
}


def main():
    os.makedirs(OUT, exist_ok=True)
    doc = pymupdf.open(SRC)
    for name, (page, clip, dpi) in JOBS.items():
        pg = doc[page - 1]
        pix = pg.get_pixmap(dpi=dpi, clip=pymupdf.Rect(*clip))
        path = os.path.join(OUT, name + ".png")
        pix.save(path)
        print(f"{path}  {pix.width}x{pix.height}  {os.path.getsize(path)//1024} Ko")
    doc.close()


if __name__ == "__main__":
    main()
