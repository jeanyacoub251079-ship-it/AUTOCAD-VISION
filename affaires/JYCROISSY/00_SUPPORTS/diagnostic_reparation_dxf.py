#!/usr/bin/env python3
"""
Diagnostic + réparation des DXF Phase 1.

Problème : AutoCAD refuse d'ouvrir les DXF produits par ezdxf 1.4.5.
Hypothèse : section binaire OBJECTS (groupes 310) mal formée — ezdxf lit
car il est permissif, AutoCAD est strict.

Stratégie de réparation :
  1. Diagnostic : chargement, audit, inspection section 310.
  2. Réparation : saveas() propre (régénère la section binaire interne).
  3. Réparation alternative : enregistrement R12 (AC1009, pas de section 310).
  4. Vérification : le fichier réparé doit se recharger sans erreur.
"""
import sys, os, glob, traceback, subprocess, shutil
from collections import Counter

import ezdxf

BASE = "affaires/JYCROISSY/03_PHASE_1_SOCLE"

def diagnostic(fpath):
    """Chargement, audit, inspection de la section binaire."""
    print(f"  [DIAG] Chargement : {os.path.basename(fpath)}")
    try:
        doc = ezdxf.readfile(fpath)
        av = doc.header['$ACADVER']
        print(f"  [DIAG] ACADVER = {av if isinstance(av, str) else av.val}")
    except Exception as e:
        print(f"  [DIAG] ERREUR chargement : {e}")
        traceback.print_exc()
        return None

    # Audit
    try:
        auditor = doc.audit()
        errs = getattr(auditor, 'errors', [])
        print(f"  [AUDIT] erreurs={len(errs)}")
        for e in errs[:3]:
            print(f"    ERREUR: {e}")
    except Exception as e:
        print(f"  [AUDIT] ERREUR : {e}")

    # Entités modelspace
    msp = doc.modelspace()
    types = Counter(e.dxftype() for e in msp)
    print(f"  [ENTITES] {dict(types)}")

    # INSERTs dangling
    try:
        block_names = set(doc.blocks.names())
    except Exception:
        block_names = set()
    dang = sum(1 for e in msp.query("INSERT") if e.dxf.name not in block_names)
    print(f"  [INSERTS] dangling={dang} (blocs définis={len(block_names)})")

    # Section binaire 310 (dans le fichier brut)
    try:
        with open(fpath, 'rb') as fh:
            raw = fh.read()
        text = raw.decode('latin-1')
        lines = text.split('\n')
        idx_310 = [i for i, l in enumerate(lines) if l.strip() == '310']
        if idx_310:
            last_hex = lines[idx_310[-1] + 1].strip()
            marker = last_hex[-20:]
            print(f"  [310] {len(idx_310)} chunks — dernier: ...{marker}")
            if '4E4544AE426082' in last_hex:
                print("  [310] EOF standard OK")
            elif '49454E44AE426082' in last_hex:
                print("  [310] SUSPECT: 'I' (0x49) avant 'END'")
            else:
                print(f"  [310] EOF inconnu")
        else:
            print("  [310] pas de section binaire")
    except Exception as e:
        print(f"  [310] ERREUR inspection : {e}")

    return doc

def reparer_saveas(doc, fpath):
    """saveas() propre — régénère la section binaire interne."""
    out = fpath.replace(".dxf", "_fixed.dxf")
    try:
        doc.saveas(out)
        print(f"  [FIX] saveas OK → {os.path.basename(out)} ({os.path.getsize(out)} B)")
        # Vérification
        doc2 = ezdxf.readfile(out)
        print(f"  [FIX] Vérification : rechargement OK, {len(list(doc2.modelspace()))} entités")
        # Inspection section 310 du fichier fixé
        with open(out, 'rb') as fh:
            raw2 = fh.read()
        text2 = raw2.decode('latin-1')
        lines2 = text2.split('\n')
        idx2 = [i for i, l in enumerate(lines2) if l.strip() == '310']
        if idx2:
            last2 = lines2[idx2[-1] + 1].strip()
            print(f"  [FIX] section 310 : {len(idx2)} chunks — ...{last2[-20:]}")
        else:
            print("  [FIX] section 310 : ABSENTE (bon signe)")
        return out
    except Exception as e:
        print(f"  [FIX] saveas ERREUR : {e}")
        traceback.print_exc()
        return None

def reparer_r12(doc, fpath):
    """Enregistrement R12 — pas de section binaire, compatibilité maximale."""
    out = fpath.replace(".dxf", "_r12.dxf")
    try:
        doc.saveas(out, version="R12")
        print(f"  [R12] OK → {os.path.basename(out)} ({os.path.getsize(out)} B)")
        doc2 = ezdxf.readfile(out)
        print(f"  [R12] Vérification : rechargement OK, {len(list(doc2.modelspace()))} entités")
        return out
    except Exception as e:
        print(f"  [R12] ERREUR : {e}")
        return None

def main():
    files = sorted(glob.glob(f"{BASE}/**/*.dxf", recursive=True))
    if not files:
        print("Aucun DXF trouvé")
        return
    print(f"{len(files)} DXF à traiter")
    print("=" * 70)

    for f in files:
        print(f"\n{f}")
        print("-" * 70)
        doc = diagnostic(f)
        if doc is None:
            continue
        print("  [REPAIR] saveas()")
        fixed = reparer_saveas(doc, f)
        print("  [REPAIR] R12")
        r12 = reparer_r12(doc, f)
        print()

if __name__ == "__main__":
    main()
