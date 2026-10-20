#!/usr/bin/env python3
"""
Convertisseur exact et sans perte des tableaux exportés depuis Google Docs (cellules préfixées par \\t)
vers des tables Markdown normalisées (| Col 1 | Col 2 | ... |).
"""
from __future__ import annotations


TWO_COL_HEADERS = {
    ("Champ", "Valeur"),
    ("Clause", "Pourquoi"),
    ("Exclu", "Renvoyé à"),
    ("B-11 (Analyse)", "B-23 (Conception)"),
    ("Fichier", "Contenu"),
    ("Fichier", "Modifications"),
    ("Format", "Paramètre"),
    ("Mention", "Position"),
    ("Niveau", "Exemple (projet Flora)"),
    ("Numéro", "Intitulé"),
    ("Phase", "Plage de numéros"),
    ("Problème", "Que faire"),
    ("Type de valeur", "Règle d'arrondi"),
    ("Élément", "Nature"),
    ("Élément", "Statut en v1.0"),
    ("Élément", "Statut en v1.1"),
    ("Élément à calculer", "Fiche"),
    ("Événement", "Incrémentation"),
}

THREE_COL_THIRD = {
    "Auto-contrôle de synthèse (B-70)",
    "T-01 (sincérité)",
    "B-13 (traitement systématique)",
    "B-46 (mode COMPLET)",
    "Brique d'indiçage (B-71)",
    "Méta-amélioration (T-03)",
    "Sortie",
    "Conséquence",
    "Conséquence en cas de désaccord",
    "Fichier",
    "Usage",
    "Nommage",
    "Éléments supprimés",
    "Mention au cartouche",
    "Livrable",
    "Exemple",
    "Interlocuteur habituel",
    "Source",
    "Livrables principaux",
    "Vérifications principales",
    "Ce qui gouverne",
    "Fonction",
    "Lecteur cible",
    "Nature",
    "Livrable produit",
    "Utilisation",
    "Vérifications spécifiques",
    "Dispositions constructives critiques",
    "Brique source",
    "Contenu",
    "Exemples",
    "Ce que vous validez",
    "Unité",
    "Précision",
    "À qui s'adresse-t-elle ?",
}


def detect_table_shape(cells: list[str], rel_path: str) -> tuple[int, bool]:
    c0, c1 = cells[0], cells[1] if len(cells) > 1 else ""
    c2 = cells[2] if len(cells) > 2 else ""

    if rel_path == "12_EXEMPLES/Exemples_Phase_0.md":
        if (c0, c1) == ("Code", "Libellé"):
            return (7, True)
        if c0 == "Code VERROU":
            return (6, True)
        if (c0, c1) == ("N°", "Date"):
            return (6, True)
        if (c0, c1) == ("N°", "Objet"):
            return (6, True)
        if (c0, c1) == ("N°", "Donnée (code)"):
            return (7, True)
        if (c0, c1) == ("Répertoire", "Nature"):
            return (4, True)
        if (c0, c1) == ("Rôle", "Nom"):
            return (4 if c2 == "Date" else 5, True)

    if (c0, c1) == ("Élément", "Nature") and c2 == "Renvoi":
        return (3, True)
    if (c0, c1) in TWO_COL_HEADERS:
        return (2, True)
    if c0 == "Brique" and (c1.startswith("Ce qu") or c1 == "Rôle"):
        return (2, True)
    if c0.startswith("Ce que ") and c1.startswith("Ce que "):
        return (2, True)
    if (c0, c1) == ("N°", "Type") and c2 == "Date":
        return (6, True)
    if (c0, c1) == ("Code", "Libellé") and c2 == "Bloque":
        return (4, True)
    if (c0, c1) == ("Version", "Date") and c2 == "Statut":
        return (5, True)
    if (c0, c1) == ("N°", "Nature") and c2 == "Fiches impactées":
        return (4, True)
    if (c0, c1) == ("Ordre", "Fiche") and c2 == "Ce que vous faites":
        return (4, True)
    if (c0, c1) == ("Gravité", "Définition objective") and c2 == "Action induite":
        return (4, True)
    if (c0, c1) == ("Document", "Vue") and c2.startswith("Question"):
        return (3, True)

    n = len(cells) - 1
    if n % 3 == 0 and (n % 2 != 0 or c2 in THREE_COL_THIRD or c2.startswith("Statut dans ")):
        return (3, True)
    if n % 2 == 0:
        return (2, True)
    if n % 3 == 0:
        return (3, True)
    raise ValueError(f"Forme de tableau non résolue dans {rel_path}: {cells[:6]} (len={len(cells)})")


def format_md_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    ncols = len(rows[0])
    out = [
        "| " + " | ".join(c.replace("|", "\\|") for c in rows[0]) + " |",
        "| " + " | ".join("---" for _ in range(ncols)) + " |",
    ]
    for r in rows[1:]:
        padded = list(r) + [""] * (ncols - len(r))
        out.append("| " + " | ".join(c.replace("|", "\\|") for c in padded[:ncols]) + " |")
    return out


def pre_fix_known_tab_quirks(text: str, rel_path: str) -> str:
    """Corrige les cellules vides Google Docs (\\t\\n\\n\\t) et les 2 anomalies structurelles détectées à l'Étape 1."""
    import re as _re
    while _re.search(r"\t *\n\n(?=\t)", text):
        text = _re.sub(r"\t *\n\n(?=\t)", "\t—\n", text)
    if rel_path == "10_ANNEXES/C_Journal_Revisions.md":
        # Ligne v2.0 manquait sa cellule Date ('10/2026')
        text = text.replace(
            "\tv2.0\n\tProduite (refonte), puis v2.1, v2.2, v2.3, v2.4, v2.5 ; version en vigueur : v2.6",
            "\tv2.0\n\t10/2026\n\tProduite (refonte), puis v2.1, v2.2, v2.3, v2.4, v2.5 ; version en vigueur : v2.6",
        )
    elif rel_path == "11_HISTORIQUE/Journal_des_modifications.md":
        # Réordonner dans le tableau §2 les 7 lignes V2.0..V2.6 dont les colonnes étaient permutées (Fiches, Version, N°, Type, Date, Objet -> N°, Type, Date, Objet, Fiches, Version)
        lines = text.splitlines()
        fixed_lines = []
        i = 0
        while i < len(lines):
            if i + 5 < len(lines) and lines[i + 2].strip() in {"V2.0", "V2.1", "V2.2", "V2.3", "V2.4", "V2.5", "V2.6"}:
                fiches_imp = lines[i].strip()
                ver_str = lines[i + 1].strip()
                num_str = lines[i + 2].strip()
                typ_str = lines[i + 3].strip()
                dat_str = lines[i + 4].strip()
                obj_str = lines[i + 5].strip()
                fixed_lines.extend(
                    [f"\t{num_str}", f"\t{typ_str}", f"\t{dat_str}", f"\t{obj_str}", f"\t{fiches_imp}", f"\t{ver_str}"]
                )
                i += 6
                continue
            fixed_lines.append(lines[i])
            i += 1
        text = "\n".join(fixed_lines)
    elif rel_path == "12_EXEMPLES/Exemples_Phase_0.md":
        # Ligne vide dans la cellule Nature de Total à la fin du fichier
        text = text.replace(
            "\tTotal\n\t\n\n\t49 fichiers\n\t✔ Complet",
            "\tTotal\n\t—\n\t49 fichiers\n\t✔ Complet",
        )
        text = text.replace(
            "\tTotal\n\t \n\n\t49 fichiers\n\t✔ Complet",
            "\tTotal\n\t—\n\t49 fichiers\n\t✔ Complet",
        )
    return text


def normalize_tables_in_markdown(text: str, rel_path: str) -> str:
    text = pre_fix_known_tab_quirks(text, rel_path)
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        if i + 1 < n and lines[i].strip() and not lines[i].startswith("\t") and lines[i + 1].startswith("\t"):
            j = i + 1
            while j < n and lines[j].startswith("\t"):
                j += 1
            cells = [lines[k].strip() for k in range(i, j)]
            ncols, has_trail = detect_table_shape(cells, rel_path)
            body_cells = cells[:-1] if has_trail else cells
            trailing = cells[-1] if has_trail else ""
            assert len(body_cells) % ncols == 0, f"Cell count mismatch in {rel_path}:{i+1}"
            rows = [body_cells[k : k + ncols] for k in range(0, len(body_cells), ncols)]
            if out and out[-1].strip():
                out.append("")
            out.extend(format_md_table(rows))
            out.append("")
            if trailing:
                out.append(trailing)
            i = j
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    from pathlib import Path

    src = Path("/home/user/AUTOCAD-VISION/carnac/CARNAC_v2.6")
    total_converted = 0
    for p in sorted(src.rglob("*.md")):
        rel = str(p.relative_to(src))
        conv = normalize_tables_in_markdown(p.read_text(encoding="utf-8"), rel)
        assert "\n\t" not in conv, f"Residual tab in {rel}!"
        total_converted += 1
    print(f"SUCCESS: {total_converted}/49 files normalized to pure Markdown tables with 0 residual tabs!")
