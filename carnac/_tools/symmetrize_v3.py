#!/usr/bin/env python3
"""Symétrisation du graphe « Briques amont » / « Briques aval » des fiches CARNAC v3.0."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
DST = BASE / "CARNAC_v3.0"
sys.path.insert(0, str(BASE / "_tools"))
from carnac_lint import expand_brick_range, extract_table_under_heading  # noqa: E402


def fiche_map() -> dict[str, Path]:
    out = {}
    for p in sorted(DST.rglob("*.md")):
        m = re.search(r"/([BT]-\d{2})_", str(p.relative_to(DST)))
        if m:
            out[m.group(1)] = p
    return out


def label_for(code: str, text: str) -> str:
    m = re.search(rf"^{code} — (.+)$", text, flags=re.M)
    if not m:
        return code
    title = m.group(1).strip().split("(")[0].strip()
    words = title.split()
    words = words[:4]
    ACR = {"cctp", "ba", "ddc", "mpd", "fdc", "rdr", "ptd", "go", "dxf", "dwg", "pdf", "ec8",
           "jd", "asb", "rsu", "enc", "cvc", "nom", "els", "elu"}
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if lw in ACR:
            out.append(w.upper())
        elif i == 0:
            out.append(w.capitalize())
        else:
            out.append(lw)
    while out and out[-1].lower() in {"de", "des", "du", "et", "la", "le", "les", "d'", "à", "en"}:
        out.pop()
    return f"{code} ({' '.join(out)})"


def rewrite_table(text: str, heading: str, rows: list[tuple[str, str]]) -> str:
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == heading:
            start = i
            break
    if start is None:
        return text
    j = start + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines) or not lines[j].strip().startswith("|"):
        return text
    k = j
    while k < len(lines) and lines[k].strip().startswith("|"):
        k += 1
    new = ["| Brique | " + ("Ce qu'elle fournit" if heading == "Briques amont" else "Ce qu'elle consomme") + " |",
           "| --- | --- |"]
    for ref, desc in rows:
        new.append(f"| {ref} | {desc} |")
    return "\n".join(lines[:j] + new + lines[k:])


def main() -> None:
    fiches = fiche_map()
    known = set(fiches)
    labels = {c: label_for(c, p.read_text(encoding="utf-8")) for c, p in fiches.items()}

    desc: dict[tuple[str, str], str] = {}  # (fournisseur, consommateur) -> description
    for code, p in fiches.items():
        txt = p.read_text(encoding="utf-8")
        for row in extract_table_under_heading(txt, r"^Briques amont$", 2):
            for ref in expand_brick_range(row[0], known):
                if ref != code:
                    desc.setdefault((ref, code), row[1].strip())
        for row in extract_table_under_heading(txt, r"^Briques aval$", 2):
            for ref in expand_brick_range(row[0], known):
                if ref != code:
                    desc[(code, ref)] = row[1].strip()

    amont = defaultdict(set)
    aval = defaultdict(set)
    for (a, b) in desc:
        if a in known and b in known:
            aval[a].add(b)
            amont[b].add(a)

    for code, p in fiches.items():
        txt = p.read_text(encoding="utf-8")
        a_rows = []
        for other in sorted(amont[code]):
            d = desc.get((other, code), f"Sortie de {other} — voir la fiche {other} §2")
            a_rows.append((labels[other], d))
        v_rows = []
        for other in sorted(aval[code]):
            d = desc.get((code, other), f"La sortie de {code} — voir la fiche {other} §2")
            v_rows.append((labels[other], d))
        if not a_rows:
            a_rows = [("Aucune — première brique de la chaîne", "—")]
        if not v_rows:
            v_rows = [("Aucune — dernière brique de la chaîne", "—")]
        txt = rewrite_table(txt, "Briques amont", a_rows)
        txt = rewrite_table(txt, "Briques aval", v_rows)
        p.write_text(txt, encoding="utf-8")

    print(f"Graphe symétrisé : {len(desc)} arêtes, {len(fiches)} fiches")


if __name__ == "__main__":
    main()
