#!/usr/bin/env python3
"""Vérification V13 : chaque fichier présent dans un pack est identique à l'octet près à sa source."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
SRC = BASE / "CARNAC_v3.0"
PACKS = BASE / "CARNAC_v3.0_PACKS"

RE_START = re.compile(r"^\*\*\[Début du fichier : ([^\]]+)\]\*\*\s*$", re.M)


def main() -> int:
    seen: dict[str, str] = {}
    errors = 0
    total_files = 0
    for pack in sorted(PACKS.glob("*.md")):
        text = pack.read_text(encoding="utf-8")
        starts = list(RE_START.finditer(text))
        for i, m in enumerate(starts):
            rel = m.group(1).strip()
            body_start = m.end() + 1  # saut de ligne après la balise
            end_tag = f"**[Fin de {rel}]**"
            body_end = text.index(end_tag, body_start)
            body = text[body_start:body_end]
            # retire le "\n" ajouté avant la balise de fin
            if body.endswith("\n"):
                body = body[:-1]
            got = hashlib.sha256(body.encode("utf-8")).hexdigest()
            want = hashlib.sha256((SRC / rel).read_bytes()).hexdigest()
            total_files += 1
            if got != want:
                errors += 1
                print(f"  ÉCART  {pack.name:22s} {rel}")
            if rel in seen:
                print(f"  DOUBLON {rel} (déjà dans {seen[rel]})")
            seen[rel] = pack.name

    all_src = {str(p.relative_to(SRC)) for p in SRC.rglob("*.md")}
    missing = sorted(all_src - set(seen))
    print(f"\nFichiers vérifiés : {total_files} · identiques : {total_files - errors} · écarts : {errors}")
    print(f"Couverture : {len(seen)}/{len(all_src)} fichiers Markdown de l'arborescence")
    if missing:
        print("Hors packs (archives, volontairement exclues) :")
        for m in missing:
            print(f"  - {m}")
    manifest = json.loads((PACKS / "PACKS_MANIFEST.json").read_text(encoding="utf-8"))
    declared = sum(len(p["files"]) for p in manifest)
    print(f"Cohérence manifeste : {declared} fichiers déclarés / {total_files} retrouvés")
    return 0 if errors == 0 and declared == total_files else 1


if __name__ == "__main__":
    raise SystemExit(main())
