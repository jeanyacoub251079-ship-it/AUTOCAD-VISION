#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle du DXF produit : version, unités, calques, entités, cohérence.

Usage : python controle_dxf.py PLAN.dxf
Sortie : rapport texte + code retour 0 (OK) / 1 (anomalie bloquante).
"""
from __future__ import annotations

import sys
from collections import Counter

import ezdxf
from ezdxf.audit import Auditor

ATTENDU = {
    "MURS_EXT", "CLOISONS", "HACHURES", "OUVERTURES", "MENUISERIES",
    "ESCALIER", "SANITAIRES", "TERRASSE", "COTES", "TEXTES", "AXES",
    "COUPE", "CARTOUCHE", "TABLEAU",
}


def main(path: str) -> int:
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    ok = True
    print("Fichier      :", path)
    print("Version DXF  :", doc.dxfversion, "(AC1027 = R2013)")
    print("INSUNITS     :", doc.header.get("$INSUNITS"), "(4 = mm)")
    # ezdxf écrit volontairement EXTMIN = 1e20 (valeur "non calculée") :
    # AutoCAD recalcule l'étendue à l'ouverture. On contrôle donc les limites
    # de travail ($LIMMIN/$LIMMAX) et l'étendue réelle par bounding-box.
    from ezdxf import bbox
    print("LIMMIN/MAX   :", doc.header.get("$LIMMIN"), doc.header.get("$LIMMAX"))
    ext = bbox.extents(msp)
    print("Etendue reelle:", (round(ext.extmin.x), round(ext.extmin.y)),
          (round(ext.extmax.x), round(ext.extmax.y)))

    counts = Counter(e.dxftype() for e in msp)
    print("Entités      :", dict(sorted(counts.items())))
    layers = Counter(e.dxf.layer for e in msp)
    print("Calques      :", dict(sorted(layers.items())))
    manquants = ATTENDU - set(layers)
    if manquants:
        print("!! calques attendus vides :", manquants)
        ok = False
    hors = set(layers) - ATTENDU
    if hors:
        print("   calques non déclarés dans le contrôle :", hors)

    # textes non vides
    txts = [e for e in msp if e.dxftype() in ("TEXT", "MTEXT")]
    vides = [t for t in txts if not (t.dxf.text.strip() if t.dxftype() == "TEXT"
                                     else t.text.strip())]
    if vides:
        print("!! textes vides :", len(vides))
        ok = False
    print("Textes       :", len(txts))

    # cotes
    dims = [e for e in msp if e.dxftype() == "DIMENSION"]
    print("Cotes        :", len(dims))
    if not dims:
        ok = False

    # échelles / extensions
    print(f"Encombrement  : {(ext.extmax.x - ext.extmin.x) / 1000:.2f} x "
          f"{(ext.extmax.y - ext.extmin.y) / 1000:.2f} m")

    # audit ezdxf
    auditor = Auditor(doc)
    auditor.run()
    print("Audit ezdxf  :", "OK" if not auditor.has_errors else "ERREURS")
    for e in auditor.errors[:5]:
        print("   erreur :", e.message)
    if auditor.has_errors:
        ok = False

    print("RESULTAT     :", "CONFORME" if ok else "A CORRIGER")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
