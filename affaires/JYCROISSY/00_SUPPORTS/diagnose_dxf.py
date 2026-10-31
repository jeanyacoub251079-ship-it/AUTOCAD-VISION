#!/usr/bin/env python3
"""Diagnostic DXF : chargement, audit, détection des problèmes d'ouverture AutoCAD."""
import sys, os
import ezdxf

FILES = [
    "affaires/JYCROISSY/03_PHASE_1_SOCLE/B-30_Calage/B-30_FLORA_RSU_calé_v1.dxf",
    "affaires/JYCROISSY/03_PHASE_1_SOCLE/B-32_Vue_Nettoyee/SOCLE-GEOS_VUE-NETTOYEE_V1.dxf",
]

for f in FILES:
    print(f"\n{'='*70}\nFILE: {f}\n{'='*70}")
    # 1) Chargement
    try:
        doc = ezdxf.readfile(f)
        av = doc.header['$ACADVER'].val if '$ACADVER' in doc.header else '?'
        print(f"[OK] Lecture ezdxf réussie — ACADVER={av}")
    except Exception as e:
        print(f"[FAIL] Lecture ezdxf : {e}")
        continue

    # 2) Audit
    try:
        result = doc.audit()
        print(f"[AUDIT] entités={result.entities} ; erreurs={result.errors} ; avertissements={result.warnings}")
        for e in result.errors[:10]:
            print(f"  ERREUR: {e}")
    except Exception as e:
        print(f"[AUDIT FAIL] {e}")

    # 3) Comptage entités par type
    msp = doc.modelspace()
    from collections import Counter
    types = Counter(e.dxftype() for e in msp)
    print(f"[ENTITES] modelspace : {dict(types)}")

    # 4) Vérification des références dangèles (INSERT -> BLOCK)
    blocks = set(doc.blocks.keys())
    dangling_ins = 0
    for e in msp.query("INSERT"):
        nm = e.dxf.name
        if nm not in blocks:
            dangling_ins += 1
    print(f"[INSERTS] blocs définis={len(blocks)} ; INSERTs dangèles={dangling_ins}")

    # 5) Sections présentes
    print(f"[SECTIONS] {list(doc.sections.keys())}")

    # 6) Données binaires dans OBJECTS
    try:
        obj_section = doc.sections.get("OBJECTS")
        if obj_section is not None:
            # ezdxf ne expose pas directement le 310 ; on regarde le fichier brut
            pass
    except Exception:
        pass
