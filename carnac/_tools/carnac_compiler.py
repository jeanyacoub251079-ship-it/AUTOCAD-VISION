#!/usr/bin/env python3
"""
Décompilateur / Recompilateur bidirectionnel sans perte (lossless) du corpus CARNAC.
Garantit l'identité SHA-256 stricte (octet pour octet) entre l'arborescence de fichiers
et le document compilé mono-fichier.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

RE_START = re.compile(r"^\*\*\[Début du fichier : ([^\]]+)\]\*\*\s*$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_variables_table(md_text: str) -> list[dict[str, str]]:
    """Extrait la table Markdown des variables du fichier 01_DICTIONNAIRE/*.md."""
    rows: list[dict[str, str]] = []
    in_table = False
    for line in md_text.splitlines():
        s = line.strip()
        if s.startswith("| Code |") or s.startswith("|Code|"):
            in_table = True
            continue
        if in_table:
            if not s.startswith("|"):
                break
            parts = [p.strip() for p in s.split("|")[1:-1]]
            if len(parts) >= 3 and set(parts[0]) <= {"-", ":"}:
                continue
            if len(parts) >= 3:
                rows.append(
                    {
                        "Code": parts[0],
                        "Libellé": parts[1],
                        "Briques consommatrices": parts[2],
                    }
                )
    return rows


def decompile(compiled_path: Path, out_dir: Path, manifest_path: Path) -> dict:
    raw_bytes = compiled_path.read_bytes()
    text = raw_bytes.decode("utf-8")
    lines = text.splitlines(keepends=True)

    segments = []
    pos = 0
    n = len(lines)
    leading_prefix = ""

    # Trouver le premier marqueur de début
    while pos < n and not RE_START.match(lines[pos]):
        leading_prefix += lines[pos]
        pos += 1

    while pos < n:
        m = RE_START.match(lines[pos])
        if not m:
            break
        rel_path = m.group(1).strip()
        start_header = lines[pos]
        pos += 1
        end_marker = f"**[Fin de {rel_path}]**"
        body_lines = []
        found_end = False
        end_line = ""
        while pos < n:
            if lines[pos].strip() == end_marker:
                found_end = True
                end_line = lines[pos]
                pos += 1
                break
            body_lines.append(lines[pos])
            pos += 1
        if not found_end:
            raise ValueError(f"Marqueur de fin introuvable pour {rel_path}")

        between_lines = []
        while pos < n and not RE_START.match(lines[pos]):
            between_lines.append(lines[pos])
            pos += 1

        content_str = "".join(body_lines)
        # Normalisation propre sur disque : retirer uniquement le saut de ligne vide d'encadrement
        has_leading_nl = content_str.startswith("\n")
        has_trailing_nl = content_str.endswith("\n\n")
        clean_content = content_str
        if has_leading_nl:
            clean_content = clean_content[1:]
        if has_trailing_nl:
            clean_content = clean_content[:-1]

        dest = out_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(clean_content, encoding="utf-8")

        segments.append(
            {
                "index": len(segments) + 1,
                "rel_path": rel_path,
                "start_header": start_header,
                "has_leading_nl": has_leading_nl,
                "has_trailing_nl": has_trailing_nl,
                "end_line": end_line,
                "separator_after": "".join(between_lines),
                "bytes": len(clean_content.encode("utf-8")),
                "lines": clean_content.count("\n") + (0 if not clean_content or clean_content.endswith("\n") else 1),
                "sha256": sha256_bytes(clean_content.encode("utf-8")),
            }
        )

    # Générer également le CSV officiel à partir de 01_DICTIONNAIRE/*.md
    dict_files = [s for s in segments if s["rel_path"].startswith("01_DICTIONNAIRE/") and s["rel_path"].endswith(".md")]
    csv_info = None
    if dict_files:
        dict_md_path = out_dir / dict_files[0]["rel_path"]
        csv_rel_path = dict_files[0]["rel_path"][:-3] + ".csv"
        csv_path = out_dir / csv_rel_path
        rows = extract_variables_table(dict_md_path.read_text(encoding="utf-8"))
        with csv_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Code", "Libellé", "Briques consommatrices"])
            writer.writeheader()
            writer.writerows(rows)
        csv_bytes = csv_path.read_bytes()
        csv_info = {
            "rel_path": csv_rel_path,
            "variable_count": len(rows),
            "bytes": len(csv_bytes),
            "lines": csv_bytes.decode("utf-8").count("\n"),
            "sha256": sha256_bytes(csv_bytes),
        }

    manifest = {
        "source_compiled_file": str(compiled_path),
        "source_bytes": len(raw_bytes),
        "source_lines": text.count("\n"),
        "source_sha256": sha256_bytes(raw_bytes),
        "markdown_files_count": len(segments),
        "total_tree_files_count": len(segments) + (1 if csv_info else 0),
        "leading_prefix": leading_prefix,
        "generated_csv": csv_info,
        "files": segments,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def compile_tree(tree_dir: Path, manifest_path: Path, out_compiled: Path | None = None) -> bytes:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    parts = [manifest["leading_prefix"]]
    for seg in manifest["files"]:
        rel_path = seg["rel_path"]
        p = tree_dir / rel_path
        content = p.read_text(encoding="utf-8")
        body = content
        if seg.get("has_leading_nl", True):
            body = "\n" + body
        if seg.get("has_trailing_nl", True):
            body = body + "\n"
        parts.append(seg["start_header"])
        parts.append(body)
        parts.append(seg["end_line"])
        parts.append(seg["separator_after"])
    compiled_bytes = "".join(parts).encode("utf-8")
    if out_compiled is not None:
        out_compiled.parent.mkdir(parents=True, exist_ok=True)
        out_compiled.write_bytes(compiled_bytes)
    return compiled_bytes


if __name__ == "__main__":
    base = Path("/home/user/AUTOCAD-VISION/carnac")
    src = Path("/tmp/arena-coding-uploads/CARNAC_v2.6_compile.md")
    out_tree = base / "CARNAC_v2.6"
    manifest_file = base / "_meta" / "BASELINE_MANIFEST_v2.6.json"
    manifest = decompile(src, out_tree, manifest_file)
    rebuilt = compile_tree(out_tree, manifest_file)
    orig = src.read_bytes()
    assert rebuilt == orig, f"Mismatch! rebuilt={len(rebuilt)} vs orig={len(orig)}"
    print(f"OK LOSSLESS DECOMPILE/RECOMPILE:")
    print(f"  Source SHA-256 : {manifest['source_sha256']}")
    print(f"  Rebuilt SHA-256: {sha256_bytes(rebuilt)}")
    print(f"  Bytes          : {len(rebuilt):,} / {len(orig):,} (diff = 0 byte)")
    print(f"  MD files       : {manifest['markdown_files_count']}")
    print(f"  Total files    : {manifest['total_tree_files_count']} (incl. {manifest['generated_csv']['rel_path']} with {manifest['generated_csv']['variable_count']} vars)")
