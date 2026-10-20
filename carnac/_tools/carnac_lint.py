#!/usr/bin/env python3
"""
Compilateur de cohérence formelle CARNAC (Tests T1 à T10).
Supporte nativement les deux formats de tableaux du corpus CARNAC :
  1. Tables Markdown standard (| Col1 | Col2 | ...)
  2. Tables tabulées d'export Google Docs (Cell0 \\n \\tCell1 \\n \\tCell2 ...)

Peut être exécuté :
  - sur la baseline v2.6 (mode diagnostic complet avant migration) ;
  - sur toute candidate v3.0 (mode bloquant : exige 0 erreur et 0 avertissement).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from carnac_compiler import compile_tree, extract_variables_table, sha256_bytes

FRENCH_NUMS = {
    "un": 1, "une": 1,
    "deux": 2,
    "trois": 3,
    "quatre": 4,
    "cinq": 5,
    "six": 6,
    "sept": 7,
    "huit": 8,
    "neuf": 9,
    "dix": 10,
    "onze": 11,
    "douze": 12,
    "treize": 13,
    "quatorze": 14,
    "quinze": 15,
}

RE_BRICK_CODE = re.compile(r"\b([BT]-\d{2})\b")
RE_VAR_CODE = re.compile(r"\b([A-Z]{2,4}-\d{2})\b")
RE_VER_EXPLICIT = re.compile(
    r"(?:\b[vV][123]\.\d\b|(?:[Vv]ersion(?:\s+du\s+document)?\s*:\s*|^\s*Version\s*$)\s*([123]\.\d)\b)"
)


def find_version_tokens(lines: list[str], idx0: int) -> list[str]:
    """Détecte uniquement les vraies mentions de version (jamais les numéros de chapitres §1.1 / 2.3)."""
    line = lines[idx0]
    tokens = re.findall(r"\b[vV][123]\.\d\b", line)
    m_doc = re.search(r"[Vv]ersion(?:\s+du\s+document)?\s*:\s*([123]\.\d)\b", line)
    if m_doc:
        tokens.append(m_doc.group(1))
    # Cas du champ tabulé : ligne précédente == 'Version' et ligne courante == '\t2.6'
    if idx0 > 0 and lines[idx0 - 1].strip() == "Version" and re.match(r"^\t[123]\.\d\b", line):
        tokens.append(line.strip().split()[0])
    return tokens


def parse_tab_table_after(lines: list[str], start_idx: int, ncols: int) -> list[list[str]]:
    """Parse une table Google Docs exportée : Cell0 sans tab, puis toutes les cellules suivantes préfixées par \\t."""
    rows: list[list[str]] = []
    i = start_idx
    n = len(lines)
    while i < n and not lines[i].strip():
        i += 1
    while i < n:
        if lines[i].startswith("\t") or not lines[i].strip():
            break
        block = [lines[i].strip()]
        j = i + 1
        while j < n and lines[j].startswith("\t"):
            block.append(lines[j].strip())
            j += 1
        if len(block) < ncols:
            break
        full_rows = (len(block) // ncols) * ncols
        for k in range(0, full_rows, ncols):
            rows.append(block[k : k + ncols])
        i = j
        # Dans Google Docs, toute la table est un seul bloc continu -> s'arrêter dès la sortie du bloc tabulé
        break
    return rows


def parse_pipe_table_after(lines: list[str], start_idx: int) -> list[list[str]]:
    rows: list[list[str]] = []
    i = start_idx
    n = len(lines)
    while i < n and not lines[i].strip():
        i += 1
    while i < n and lines[i].strip().startswith("|"):
        parts = [c.strip() for c in lines[i].strip().split("|")[1:-1]]
        if parts and not all(set(p) <= {"-", ":"} for p in parts):
            rows.append(parts)
        i += 1
    return rows


def extract_table_under_heading(text: str, heading_regex: str, expected_cols: int) -> list[list[str]]:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if re.match(heading_regex, line.strip(), flags=re.I):
            # Regarder quel format suit
            j = idx + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().startswith("|"):
                t = parse_pipe_table_after(lines, j)
                return t[1:] if len(t) > 1 else []
            t = parse_tab_table_after(lines, j, expected_cols)
            return t[1:] if len(t) > 1 else []
    return []


def expand_var_expr(expr: str) -> list[str]:
    """Développe 'SOL-01 à SOL-05' ou 'EXI-01, EXI-03' en codes individuels."""
    out: list[str] = []
    # Plages type GEO-01 à GEO-05
    for m in re.finditer(r"\b([A-Z]{2,4})-(\d{2})\s*(?:à|a|->|–|-)\s*([A-Z]{2,4})-(\d{2})\b", expr):
        p1, n1, p2, n2 = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        if p1 == p2 and n1 <= n2 <= n1 + 30:
            for k in range(n1, n2 + 1):
                out.append(f"{p1}-{k:02d}")
    for m in RE_VAR_CODE.finditer(expr):
        code = m.group(1)
        if not code.startswith(("B-", "T-")) and code not in out:
            out.append(code)
    return out


def classify_version_occurrence(rel_path: str, line_no: int, line: str, target_ver: str) -> str:
    """Classifie chaque mention de version en HISTORIQUE_PROTEGE / COURANT_AUTO / CONTEXTUEL."""
    if rel_path.startswith("11_HISTORIQUE/") or rel_path.startswith("12_EXEMPLES/"):
        if line_no <= 3 and ("Fichier " in line or "Version du document" in line):
            return "COURANT_AUTO"
        return "HISTORIQUE_PROTEGE"
    if rel_path == "10_ANNEXES/C_Journal_Revisions.md":
        if line_no <= 3:
            return "COURANT_AUTO"
        return "HISTORIQUE_PROTEGE"
    if line_no <= 8 and (
        "CARNAC v" in line
        or "Version du document" in line
        or line.strip() == target_ver.lstrip("v")
        or "Dernière révision" in line
    ):
        return "COURANT_AUTO"
    if "CARNAC_v" in line and "_variables" in line:
        return "COURANT_AUTO"
    if any(
        kw in line.lower()
        for kw in [
            "nouveau en v",
            "enseignement v",
            "complément v",
            "additif v",
            "traces historiques",
            "version v1.",
            "depuis la v",
            "en v1.",
            "en v2.",
        ]
    ):
        return "HISTORIQUE_PROTEGE"
    return "CONTEXTUEL"


def run_lint(
    tree_dir: Path,
    manifest_path: Path,
    compiled_path: Path,
    target_version: str = "v2.6",
    expected_locks: int = 13,
    expected_modes: int = 5,
    expected_vars: int = 94,
    expected_b_sheets: int = 37,
    expected_t_sheets: int = 4,
    vacant_bricks: set[str] | None = None,
) -> dict:
    if vacant_bricks is None:
        vacant_bricks = {"B-61", "B-63"}

    ver_num = target_version.lstrip("v")
    results: dict[str, dict] = {}

    md_files = sorted(tree_dir.rglob("*.md"))
    rel_md = {str(p.relative_to(tree_dir)): p for p in md_files}
    brick_files: dict[str, str] = {}
    for rel in rel_md:
        m = re.search(r"/([BT]-\d{2})_", rel)
        if m:
            brick_files[m.group(1)] = rel

    # ------------------------------------------------------------------
    # T1 — Parité Arborescence <-> Compilé & Appariement des Balises
    # ------------------------------------------------------------------
    t1_errors, t1_notes = [], []
    compiled_text = compiled_path.read_text(encoding="utf-8")
    rebuilt = compile_tree(tree_dir, manifest_path)
    orig_bytes = compiled_path.read_bytes()
    if rebuilt != orig_bytes:
        t1_errors.append(f"Écart de recompilation : {len(rebuilt)} octets vs {len(orig_bytes)} octets")
    starts = re.findall(r"^\*\*\[Début du fichier : ([^\]]+)\]\*\*\s*$", compiled_text, re.M)
    all_ends = re.findall(r"^\*\*\[Fin de ([^\]]+)\]\*\*\s*$", compiled_text, re.M)
    file_ends = [e for e in all_ends if e in set(starts)]
    extra_ends = [e for e in all_ends if e not in set(starts)]
    if len(starts) != len(file_ends):
        t1_errors.append(f"Balises de fichiers désappariées : {len(starts)} débuts vs {len(file_ends)} fins")
    if extra_ends:
        t1_notes.append(
            f"{len(extra_ends)} marqueurs internes '[Fin de ...]' non-fichiers détectés dans 12_EXEMPLES : {extra_ends}"
        )
    results["T1_parite_compilation"] = {
        "status": "PASS" if not t1_errors else "FAIL",
        "errors": t1_errors,
        "warnings": t1_notes,
        "metrics": {
            "md_files": len(md_files),
            "bytes": len(orig_bytes),
            "sha256": sha256_bytes(orig_bytes),
            "start_tags": len(starts),
            "matching_end_tags": len(file_ends),
            "internal_example_end_tags": extra_ends,
        },
    }

    # ------------------------------------------------------------------
    # T2 — Audit & Classification des Mentions de Version
    # ------------------------------------------------------------------
    t2_errors, t2_warnings = [], []
    ver_inventory = []
    class_counts = defaultdict(int)
    for rel, p in rel_md.items():
        lines = p.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, 1):
            matches = find_version_tokens(lines, idx - 1)
            if not matches:
                continue
            cls = classify_version_occurrence(rel, idx, line, target_version)
            for tok in matches:
                class_counts[cls] += 1
                ver_inventory.append(
                    {"file": rel, "line": idx, "token": tok, "class": cls, "snippet": line.strip()[:120]}
                )
            # Détecter incohérences actives :
            if cls == "COURANT_AUTO" and any(t.lower().lstrip("v") != ver_num for t in matches):
                t2_errors.append(f"{rel}:{idx} — en-tête ou chemin non aligné sur {target_version}: '{line.strip()[:95]}'")
            elif cls == "CONTEXTUEL" and any(t.lower().lstrip("v") != ver_num for t in matches):
                t2_warnings.append(f"{rel}:{idx} — mention contextuelle hors {target_version}: '{line.strip()[:95]}'")

    # Détecter corruption historique connue dans C_Journal_Revisions §3.2 (v1.1 pointant vers CARNAC_v2.6_variables.csv)
    c_rev = (tree_dir / "10_ANNEXES/C_Journal_Revisions.md").read_text(encoding="utf-8").splitlines()
    in_32 = False
    for idx, line in enumerate(c_rev, 1):
        if line.strip().startswith("3.2 Version v1.1"):
            in_32 = True
        elif line.strip().startswith("3.3 Version"):
            in_32 = False
        if in_32 and "CARNAC_v2.6_variables.csv" in line:
            t2_errors.append(
                f"10_ANNEXES/C_Journal_Revisions.md:{idx} — corruption d'archive historique : section v1.1 cite '{line.strip()}' au lieu de v1.1"
            )

    results["T2_versions_et_chemins"] = {
        "status": "PASS" if not t2_errors and not t2_warnings else ("FAIL" if t2_errors else "WARN"),
        "errors": t2_errors,
        "warnings": t2_warnings,
        "metrics": {
            "total_version_tokens": len(ver_inventory),
            "by_class": dict(class_counts),
        },
        "inventory": ver_inventory,
    }

    # ------------------------------------------------------------------
    # T3 — Isomorphisme Dictionnaire <-> CSV <-> 41 Fiches
    # ------------------------------------------------------------------
    t3_errors, t3_warnings = [], []
    dict_md_files = list((tree_dir / "01_DICTIONNAIRE").glob("*.md"))
    dict_csv_files = list((tree_dir / "01_DICTIONNAIRE").glob("*.csv"))
    md_rows = extract_variables_table(dict_md_files[0].read_text(encoding="utf-8"))
    with dict_csv_files[0].open(encoding="utf-8") as f:
        csv_rows = list(csv.DictReader(f))
    if md_rows != csv_rows:
        t3_errors.append(f"Désalignement MD ({len(md_rows)}) vs CSV ({len(csv_rows)})")
    if len(md_rows) != expected_vars:
        t3_errors.append(f"Compte réel de variables ({len(md_rows)}) != attendu ({expected_vars})")

    dict_map: dict[str, set[str]] = {}
    for r in md_rows:
        code = r["Code"]
        lbl = r["Libellé"]
        if lbl in vacant_bricks or re.fullmatch(r"B-\d{2}", lbl):
            t3_errors.append(
                f"01_DICTIONNAIRE: variable {code} a un libellé corrompu '{lbl}' (vestige d'une ancienne colonne)"
            )
        consumers = set(RE_BRICK_CODE.findall(r["Briques consommatrices"]))
        for b in consumers:
            if b in vacant_bricks:
                t3_errors.append(f"01_DICTIONNAIRE: {code} référence une brique vacante {b}")
        dict_map[code] = consumers

    # Scanner les tables "Variables consommées" des 41 fiches
    sheet_vars: dict[str, set[str]] = defaultdict(set)
    unknown_vars_used = []
    for bcode, rel in sorted(brick_files.items()):
        txt = (tree_dir / rel).read_text(encoding="utf-8")
        rows = extract_table_under_heading(txt, r"^Variables consommées$", 3)
        for row in rows:
            for v in expand_var_expr(row[0]):
                sheet_vars[v].add(bcode)
                if v not in dict_map:
                    unknown_vars_used.append(f"{rel}: utilise variable hors dictionnaire '{v}' ({row[0]})")

    t3_errors.extend(unknown_vars_used)
    mismatch_consumers = []
    for vcode, d_bricks in sorted(dict_map.items()):
        s_bricks = sheet_vars.get(vcode, set())
        if d_bricks != s_bricks:
            only_dict = sorted(d_bricks - s_bricks)
            only_sheets = sorted(s_bricks - d_bricks)
            mismatch_consumers.append(
                f"{vcode}: dict_seul={only_dict} | fiches_seules={only_sheets}"
            )
    if mismatch_consumers:
        t3_warnings.extend(mismatch_consumers)

    results["T3_dictionnaire_variables"] = {
        "status": "PASS" if not t3_errors and not t3_warnings else ("FAIL" if t3_errors else "WARN"),
        "errors": t3_errors,
        "warnings": t3_warnings,
        "metrics": {
            "variables_in_dict": len(md_rows),
            "variables_in_csv": len(csv_rows),
            "consumer_mismatches_count": len(mismatch_consumers),
        },
    }

    # ------------------------------------------------------------------
    # T4 — Symétrie du Graphe Briques Amont <-> Briques Aval
    # ------------------------------------------------------------------
    t4_errors, t4_warnings = [], []
    declared_amont: dict[str, set[str]] = defaultdict(set)
    declared_aval: dict[str, set[str]] = defaultdict(set)
    for bcode, rel in sorted(brick_files.items()):
        txt = (tree_dir / rel).read_text(encoding="utf-8")
        for r in extract_table_under_heading(txt, r"^Briques amont$", 2):
            for ref in expand_brick_range(r[0], set(brick_files.keys())):
                if ref != bcode:
                    declared_amont[bcode].add(ref)
        for r in extract_table_under_heading(txt, r"^Briques aval$", 2):
            for ref in expand_brick_range(r[0], set(brick_files.keys())):
                if ref != bcode:
                    declared_aval[bcode].add(ref)

    for a in sorted(brick_files):
        for b in sorted(declared_aval[a]):
            if b in brick_files and a not in declared_amont[b]:
                t4_warnings.append(f"Asymétrie aval->amont : {a} cite {b} en aval, mais {b} ne cite pas {a} en amont")
        for b in sorted(declared_amont[a]):
            if b in brick_files and a not in declared_aval[b]:
                t4_warnings.append(f"Asymétrie amont->aval : {a} cite {b} en amont, mais {b} ne cite pas {a} en aval")

    results["T4_graphe_amont_aval"] = {
        "status": "PASS" if not t4_errors and not t4_warnings else ("FAIL" if t4_errors else "WARN"),
        "errors": t4_errors,
        "warnings": t4_warnings,
        "metrics": {
            "b_sheets": sum(1 for k in brick_files if k.startswith("B-")),
            "t_sheets": sum(1 for k in brick_files if k.startswith("T-")),
            "asymmetric_edges": len(t4_warnings),
        },
    }

    # ------------------------------------------------------------------
    # T5 — Compteurs Cardinaux dans la Prose & Critères d'Acceptation
    # ------------------------------------------------------------------
    t5_errors, t5_warnings = [], []
    for rel, p in rel_md.items():
        if rel.startswith("11_HISTORIQUE/") or rel.startswith("12_EXEMPLES/") or rel == "10_ANNEXES/C_Journal_Revisions.md":
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, 1):
            for m in re.finditer(r"\b(\d+|douze|treize|quatorze|quinze)\s+verrous\b", line, flags=re.I):
                raw = m.group(1).lower()
                val = int(raw) if raw.isdigit() else FRENCH_NUMS[raw]
                if val != expected_locks:
                    t5_errors.append(f"{rel}:{idx} — mention '{m.group(0)}' != {expected_locks} verrous : '{line.strip()[:90]}'")
            for m in re.finditer(r"\b(\d+|cinq|six)\s+modes\b", line, flags=re.I):
                raw = m.group(1).lower()
                val = int(raw) if raw.isdigit() else FRENCH_NUMS[raw]
                if val != expected_modes:
                    t5_warnings.append(f"{rel}:{idx} — mention '{m.group(0)}' != {expected_modes} modes")

        # Vérifier le compte des puces sous CRITÈRE D'ACCEPTATION dans les 41 fiches
        if any(rel.endswith(f) for f in [rel]) and re.search(r"/[BT]-\d{2}_", rel):
            in_crit = False
            bullets = 0
            stated_num = None
            stated_line = 0
            for idx, line in enumerate(lines, 1):
                s = line.strip()
                if s == "CRITÈRE D'ACCEPTATION":
                    in_crit = True
                    bullets = 0
                    continue
                if in_crit:
                    if s.startswith("- ") or s.startswith("* "):
                        bullets += 1
                    m_stop = re.search(
                        r"Si un seul de ces ([a-zéû0-9]+)\s+(?:points|critères)", s, flags=re.I
                    )
                    if m_stop:
                        tok = m_stop.group(1).lower()
                        stated_num = int(tok) if tok.isdigit() else FRENCH_NUMS.get(tok)
                        stated_line = idx
                        in_crit = False
                    elif s.startswith("Rappel V7") or s.startswith("____"):
                        in_crit = False
            if stated_num is not None and bullets > 0 and stated_num != bullets:
                t5_errors.append(
                    f"{rel}:{stated_line} — CRITÈRE D'ACCEPTATION annonce '{stated_num}' points mais liste {bullets} puces !"
                )

    results["T5_compteurs_cardinaux"] = {
        "status": "PASS" if not t5_errors and not t5_warnings else ("FAIL" if t5_errors else "WARN"),
        "errors": t5_errors,
        "warnings": t5_warnings,
    }

    # ------------------------------------------------------------------
    # T6 — Résolution de 100 % des Renvois Internes (B-xx, T-xx, V1..Vn)
    # ------------------------------------------------------------------
    t6_errors, t6_warnings = [], []
    valid_bricks = set(brick_files.keys()) | vacant_bricks
    for rel, p in rel_md.items():
        if rel.startswith("11_HISTORIQUE/") or rel.startswith("12_EXEMPLES/") or rel == "10_ANNEXES/C_Journal_Revisions.md":
            continue
        for idx, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for b in RE_BRICK_CODE.findall(line):
                if b not in valid_bricks and b not in {"B-51"}:
                    t6_errors.append(f"{rel}:{idx} — référence à une brique inexistante '{b}' : '{line.strip()[:85]}'")
                elif b in vacant_bricks and "vacante" not in line.lower() and "fusion" not in line.lower() and "intégr" not in line.lower() and not rel.startswith("01_DICTIONNAIRE"):
                    t6_warnings.append(f"{rel}:{idx} — référence active à la brique vacante '{b}' : '{line.strip()[:85]}'")

    results["T6_renvois_internes"] = {
        "status": "PASS" if not t6_errors and not t6_warnings else ("FAIL" if t6_errors else "WARN"),
        "errors": t6_errors,
        "warnings": t6_warnings,
    }

    # ------------------------------------------------------------------
    # T7 — Non-Régression des Verrous V1..V13 (00_MASTER §2)
    # ------------------------------------------------------------------
    master_txt = (tree_dir / "00_MASTER.md").read_text(encoding="utf-8")
    found_locks = set(re.findall(r"\*\*(V\d+)\s*[—–-]", master_txt))
    required_locks = {f"V{i}" for i in range(1, expected_locks + 1)}
    missing_locks = sorted(required_locks - found_locks)
    results["T7_non_regression_verrous"] = {
        "status": "PASS" if not missing_locks else "FAIL",
        "errors": [f"Verrous manquants dans 00_MASTER.md : {missing_locks}"] if missing_locks else [],
        "warnings": [],
        "metrics": {"locks_found": sorted(found_locks, key=lambda x: int(x[1:]))},
    }

    # ------------------------------------------------------------------
    # T8 — Contrôle V7 des Placeholders {{...}} vs ligne Rappel V7
    # ------------------------------------------------------------------
    t8_errors, t8_warnings = [], []
    for bcode, rel in sorted(brick_files.items()):
        txt = (tree_dir / rel).read_text(encoding="utf-8")
        # Extraire section 2 PROMPT jusqu'à 3. JUSTIFICATION
        m_sec = re.search(r"2\.\s*PROMPT(.*?)3\.\s*JUSTIFICATION", txt, flags=re.S)
        if not m_sec:
            t8_errors.append(f"{rel}: section '2. PROMPT' ou '3. JUSTIFICATION' introuvable")
            continue
        sec2 = m_sec.group(1)
        m_rappel = re.search(r"Rappel V7[^\n]*", sec2)
        if not m_rappel:
            t8_warnings.append(f"{rel}: ligne 'Rappel V7' absente en fin de section 2")
            continue
        prompt_body = sec2[: m_rappel.start()]
        rappel_line = m_rappel.group(0)
        body_ph = set(re.findall(r"\{\{([^{}\.]+)\}\}", prompt_body))
        rappel_ph = set(re.findall(r"\{\{([^{}\.]+)\}\}", rappel_line))
        if body_ph != rappel_ph:
            t8_warnings.append(
                f"{rel}: placeholders prompt={sorted(body_ph)} != Rappel V7={sorted(rappel_ph)}"
            )

    results["T8_placeholders_V7"] = {
        "status": "PASS" if not t8_errors and not t8_warnings else ("FAIL" if t8_errors else "WARN"),
        "errors": t8_errors,
        "warnings": t8_warnings,
    }

    # ------------------------------------------------------------------
    # T9 — Contrôle Journal des Modifications & Traces de Génération
    # ------------------------------------------------------------------
    t9_errors, t9_warnings = [], []
    forbidden_fragments = [
        "Bien sûr, voici",
        "Voici la version",
        "As an AI",
        "Certainly! Here is",
        "J'espère que cela",
    ]
    for rel, p in rel_md.items():
        txt = p.read_text(encoding="utf-8")
        for frag in forbidden_fragments:
            if frag.lower() in txt.lower():
                t9_errors.append(f"{rel}: trace conversationnelle interdite détectée ('{frag}')")
    hist_txt = (tree_dir / "11_HISTORIQUE/Journal_des_modifications.md").read_text(encoding="utf-8")
    if f"Entrée {target_version}" not in hist_txt:
        t9_errors.append(f"11_HISTORIQUE/Journal_des_modifications.md ne contient pas 'Entrée {target_version}'")

    results["T9_journal_et_proprete"] = {
        "status": "PASS" if not t9_errors and not t9_warnings else ("FAIL" if t9_errors else "WARN"),
        "errors": t9_errors,
        "warnings": t9_warnings,
    }

    # ------------------------------------------------------------------
    # T10 — Complétude Structurelle des En-têtes des 41 Fiches
    # ------------------------------------------------------------------
    t10_errors, t10_warnings = [], []
    if len([k for k in brick_files if k.startswith("B-")]) != expected_b_sheets:
        t10_errors.append("Nombre de fiches B-xx inattendu")
    if len([k for k in brick_files if k.startswith("T-")]) != expected_t_sheets:
        t10_errors.append("Nombre de fiches T-xx inattendu")
    for bcode, rel in sorted(brick_files.items()):
        txt = (tree_dir / rel).read_text(encoding="utf-8")
        for req in ["1. EN-TÊTE", "2. PROMPT", "3. JUSTIFICATION", "4. RÉFÉRENCES", "CRITÈRE D'ACCEPTATION"]:
            if req not in txt:
                t10_errors.append(f"{rel}: bloc obligatoire manquant '{req}'")
        m_ver = re.search(r"^\s*Version\s*\n\t([^\n]+)", txt, flags=re.M)
        if m_ver and m_ver.group(1).strip() != ver_num:
            t10_errors.append(f"{rel}: Version d'en-tête '{m_ver.group(1).strip()}' != '{ver_num}'")

    results["T10_completude_fiches"] = {
        "status": "PASS" if not t10_errors and not t10_warnings else ("FAIL" if t10_errors else "WARN"),
        "errors": t10_errors,
        "warnings": t10_warnings,
    }

    total_errors = sum(len(v["errors"]) for v in results.values())
    total_warnings = sum(len(v["warnings"]) for v in results.values())
    return {
        "target_version": target_version,
        "summary": {
            "total_tests": len(results),
            "pass_count": sum(1 for v in results.values() if v["status"] == "PASS"),
            "warn_count": sum(1 for v in results.values() if v["status"] == "WARN"),
            "fail_count": sum(1 for v in results.values() if v["status"] == "FAIL"),
            "total_errors": total_errors,
            "total_warnings": total_warnings,
        },
        "tests": results,
    }


def expand_brick_range(expr: str, known_bricks: set[str]) -> list[str]:
    out: list[str] = []
    for m in re.finditer(r"\b([BT])-(\d{2})\s*(?:à|a|–|-)\s*([BT])-(\d{2})\b", expr):
        p1, n1, p2, n2 = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        if p1 == p2 and n1 <= n2:
            for k in range(n1, n2 + 1):
                c = f"{p1}-{k:02d}"
                if c in known_bricks and c not in out:
                    out.append(c)
    for m in RE_BRICK_CODE.finditer(expr):
        c = m.group(1)
        if c in known_bricks and c not in out:
            out.append(c)
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", default="/home/user/AUTOCAD-VISION/carnac/CARNAC_v2.6")
    parser.add_argument("--manifest", default="/home/user/AUTOCAD-VISION/carnac/_meta/BASELINE_MANIFEST_v2.6.json")
    parser.add_argument("--compiled", default="/tmp/arena-coding-uploads/CARNAC_v2.6_compile.md")
    parser.add_argument("--target", default="v2.6")
    parser.add_argument("--json-out", default="/home/user/AUTOCAD-VISION/carnac/_meta/AUDIT_BASELINE_v2.6.json")
    args = parser.parse_args()

    rep = run_lint(Path(args.tree), Path(args.manifest), Path(args.compiled), target_version=args.target)
    Path(args.json_out).write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(rep["summary"], indent=2, ensure_ascii=False))
    for k, v in rep["tests"].items():
        print(f"[{v['status']:4s}] {k:30s} | errors={len(v['errors']):3d} | warnings={len(v['warnings']):3d}")
        for e in v["errors"][:5]:
            print(f"   ERR : {e}")
        for w in v["warnings"][:3]:
            print(f"   WARN: {w}")
