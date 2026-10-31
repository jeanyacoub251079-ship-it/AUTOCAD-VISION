#!/usr/bin/env python3
"""JYCROISSY / B-00 — Script d'inventaire technique des pièces reçues.

Preuve d'exécution CARNAC v3.0 (verrou V3) : ce script produit, sans aucune
valeur inventée, les faits techniques utilisés par la brique B-00 :
  * métadonnées et nombre de pages des PDF (pypdf) ;
  * nature vectorielle des PDF (comptage des XObject image) ;
  * extraction plein texte page par page (fichiers data/JYCROISSY/extraction/) ;
  * inventaire DXF : version, unités, calques, entités, blocs, textes (ezdxf).

Entrée : copies locales des pièces Drive dans google_drive/ (non versionnées).
Sortie : résumé JSON sur stdout + fichiers .txt dans data/JYCROISSY/extraction/.

Usage :
  .venv/bin/python affaires/JYCROISSY/00_SUPPORTS/extraction_b00.py
"""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter

import ezdxf
from pypdf import PdfReader

DRIVE_DIR = "google_drive"
OUT_DIR = "data/JYCROISSY/extraction"


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def audit_pdf(path: str) -> dict:
    reader = PdfReader(path)
    pages, full_text = [], []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        full_text.append(f"\n\n===== PAGE {index} =====\n{text}")
        try:
            n_images = len(list(page.images))
        except Exception:
            n_images = None
        mb = page.mediabox
        pages.append({
            "page": index,
            "chars": len(text.strip()),
            "images_xobjects": n_images,
            "size_pt": [round(float(mb.width)), round(float(mb.height))],
        })
    base = os.path.basename(path).replace("Copy of ", "").replace(".pdf", "")
    safe = base.replace(" ", "_").replace("é", "e")
    with open(os.path.join(OUT_DIR, safe + ".txt"), "w", encoding="utf-8") as fh:
        fh.write("".join(full_text))
    meta = reader.metadata or {}
    return {
        "format": "PDF",
        "bytes": os.path.getsize(path),
        "sha256": sha256(path),
        "pages": len(reader.pages),
        "metadata": {k: str(v) for k, v in meta.items()},
        "page_checks": pages,
    }


def audit_dxf(path: str) -> dict:
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    entities = Counter(e.dxftype() for e in msp)
    used_layers = {e.dxf.layer for e in msp}
    all_layers = [layer.dxf.name for layer in doc.layers]
    texts = []
    for e in msp:
        if e.dxftype() == "TEXT":
            texts.append(e.dxf.text)
        elif e.dxftype() == "MTEXT":
            texts.append(e.text)
    named_blocks = [b.name for b in doc.blocks if not b.name.startswith("*")]
    layouts = []
    for layout in doc.layouts:
        layouts.append({
            "name": layout.name,
            "paper_space": layout.is_any_paperspace,
            "entities": sum(1 for _ in layout),
        })
    return {
        "format": "DXF",
        "bytes": os.path.getsize(path),
        "sha256": sha256(path),
        "acad_version": doc.header.get("$ACADVER"),
        "acad_release": doc.acad_release,
        "codepage": doc.header.get("$DWGCODEPAGE"),
        "insunits": doc.header.get("$INSUNITS"),
        "extmin": str(doc.header.get("$EXTMIN")),
        "extmax": str(doc.header.get("$EXTMAX")),
        "modelspace_entities": dict(entities.most_common()),
        "modelspace_entity_total": sum(entities.values()),
        "layers_total": len(all_layers),
        "layers_empty": sorted(l for l in all_layers if l not in used_layers),
        "named_blocks": len(named_blocks),
        "layouts": layouts,
        "text_occurrences": len(texts),
        "text_unique": len(set(texts)),
    }


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    report = {}
    for name in sorted(os.listdir(DRIVE_DIR)):
        path = os.path.join(DRIVE_DIR, name)
        if name.lower().endswith(".pdf"):
            report[name] = audit_pdf(path)
        elif name.lower().endswith(".dxf"):
            report[name] = audit_dxf(path)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
