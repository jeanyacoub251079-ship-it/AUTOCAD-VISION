#!/usr/bin/env python3
"""Génère le dictionnaire CARNAC v3.0 (MD + CSV) depuis les fiches consommatrices."""
from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
SRC = BASE / "CARNAC_v2.6"
DST = BASE / "CARNAC_v3.0"

sys.path.insert(0, str(BASE / "_tools"))
from carnac_lint import extract_table_under_heading, expand_var_expr  # noqa: E402

NEW_LABELS = {
    "CFG-01": "Configuration de maturité MOE (CFG-1 à CFG-4)",
    "CFG-02": "Gabarit d'opération (S / M / L-XL)",
    "CFG-03": "Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types",
    "DEC-05": "Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut)",
    "DEC-06": "Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés)",
    "DEC-07": "Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx)",
    "GEO-13": "Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU)",
    "GEO-14": "Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N",
    "NIV-07": "Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini",
    "STR-01": "Système global de contreventement, centre de torsion et descente des efforts horizontaux",
    "STR-02": "Poussées des terres, surcharges de remblai et écrans de soutènement",
    "STR-03": "Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur)",
}

LABEL_FIX = {
    "LIV-01": "Conventions de calques DXF (préfixes, suffixes, règles d'usage)",
    "LIV-03": "Formats de sortie (DXF, PDF, PNG) et nommage des fichiers",
}


def load_baseline() -> list[dict[str, str]]:
    p = SRC / "01_DICTIONNAIRE" / "CARNAC_v2.6_variables.csv"
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build() -> tuple[list[dict[str, str]], dict[str, set[str]]]:
    baseline = load_baseline()
    sheets: dict[str, set[str]] = defaultdict(set)
    for p in sorted(DST.rglob("*.md")):
        rel = str(p.relative_to(DST))
        if not re.search(r"/[BT]-\d{2}_", rel):
            continue
        code = re.search(r"/([BT]-\d{2})_", rel).group(1)
        txt = p.read_text(encoding="utf-8")
        for row in extract_table_under_heading(txt, r"^Variables consommées$", 3):
            for v in expand_var_expr(row[0]):
                sheets[v].add(code)

    rows: list[dict[str, str]] = []
    seen = set()
    for r in baseline:
        code = r["Code"]
        if code in seen:
            continue
        seen.add(code)
        label = LABEL_FIX.get(code, r["Libellé"])
        consumers = sorted(sheets.get(code, set()))
        rows.append(
            {
                "Code": code,
                "Libellé": label,
                "Briques consommatrices": ", ".join(consumers) if consumers else "— (variable de référence)",
            }
        )
    for code, label in NEW_LABELS.items():
        rows.append(
            {
                "Code": code,
                "Libellé": label,
                "Briques consommatrices": ", ".join(sorted(sheets.get(code, set()))) or "— (variable de référence)",
            }
        )
    unknown = {k: v for k, v in sheets.items() if k not in seen and k not in NEW_LABELS}
    return rows, unknown


def write_outputs(rows: list[dict[str, str]]) -> None:
    out_dir = DST / "01_DICTIONNAIRE"
    out_dir.mkdir(parents=True, exist_ok=True)
    header = (
        "Fichier 01_DICTIONNAIRE/CARNAC_v3.0_variables.md — CARNAC v3.0\n"
        "________________\n\n\n"
        "CARNAC — DICTIONNAIRE DES VARIABLES (v3.0)\n"
        "1. NOTE DE COMPTE\n"
        "Le dictionnaire v3.0 compte 106 variables : 94 variables reprises de la v2.6 (aucune supprimée), "
        "dont deux libellés restaurés (LIV-01 « Conventions de calques DXF » et LIV-03 « Formats de sortie », "
        "corrompus en « B-61 » lors de la reconstruction v2.0), et 12 variables nouvelles "
        "(CFG-01 à CFG-03, DEC-05 à DEC-07, GEO-13, GEO-14, NIV-07, STR-01 à STR-03).\n\n"
        "La colonne « Briques consommatrices » est reconstruite automatiquement, par développement des plages "
        "(SOL-01 à SOL-07, GEO-01 à GEO-05, LIV-01 à LIV-05, CHG-01 à CHG-03, etc.), à partir des tables "
        "« Variables consommées » des 39 fiches B-xx et des 4 prompts T-xx : elle est donc exacte par construction.\n\n"
        "2. TABLE DES VARIABLES\n\n"
        "| Code | Libellé | Briques consommatrices |\n"
        "| --- | --- | --- |\n"
    )
    lines = [f"| {r['Code']} | {r['Libellé']} | {r['Briques consommatrices']} |" for r in rows]
    (out_dir / "CARNAC_v3.0_variables.md").write_text(header + "\n".join(lines) + "\n", encoding="utf-8")
    with (out_dir / "CARNAC_v3.0_variables.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Code", "Libellé", "Briques consommatrices"])
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    rows, unknown = build()
    write_outputs(rows)
    print(f"Variables écrites : {len(rows)}")
    if unknown:
        print("VARIABLES UTILISÉES HORS DICTIONNAIRE :")
        for k, v in sorted(unknown.items()):
            print(f"  {k} -> {sorted(v)}")
