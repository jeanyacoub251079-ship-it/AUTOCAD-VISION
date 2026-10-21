#!/usr/bin/env python3
"""Compilation du carnet CARNAC v3.0 (arborescence -> compile + manifeste + CSV)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
DST = BASE / "CARNAC_v3.0"
META = BASE / "_meta"
COMPILED = BASE / "CARNAC_v3.0_COMPILE.md"

ORDER = [
    "00_MASTER.md",
    "01_DICTIONNAIRE/CARNAC_v3.0_variables.md",
    "10_ANNEXES/A_Conventions_Livrables.md",
    "10_ANNEXES/A1_Addendum_v3.0.1.md",
    "10_ANNEXES/O_Outillage.md",
    "10_ANNEXES/D_Mode_Emploi.md",
    "10_ANNEXES/C_Journal_Revisions.md",
    "02_PHASE_0_CADRAGE/B-00_Inventaire.md",
    "02_PHASE_0_CADRAGE/B-01_MPD.md",
    "02_PHASE_0_CADRAGE/B-02_FDC.md",
    "02_PHASE_0_CADRAGE/B-03_RDR.md",
    "02_PHASE_0_CADRAGE/B-04_PTD.md",
    "03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md",
    "03_PHASE_1_ANALYSE/B-11_Audit_Diagnostic.md",
    "03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md",
    "03_PHASE_1_ANALYSE/B-13_Contradictions.md",
    "03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md",
    "03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md",
    "04_PHASE_2_CONCEPTION/B-20_Conception_GO.md",
    "04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md",
    "04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md",
    "04_PHASE_2_CONCEPTION/B-23_Exploitation_Diagnostic.md",
    "04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md",
    "04_PHASE_2_CONCEPTION/B-25_Stabilite_Globale.md",
    "05_PHASE_3_CALAGE/B-30_Calage.md",
    "05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md",
    "05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md",
    "05_PHASE_3_CALAGE/B-33_Verification_Croisee.md",
    "06_PHASE_4_CALCULS/B-40_Fondations_Superficielles.md",
    "06_PHASE_4_CALCULS/B-41_Fondations_Profondes.md",
    "06_PHASE_4_CALCULS/B-42_Verticaux_BA.md",
    "06_PHASE_4_CALCULS/B-43_Planchers_Dallages.md",
    "06_PHASE_4_CALCULS/B-44_Charpente_Bois.md",
    "06_PHASE_4_CALCULS/B-45_Structure_Metallique.md",
    "06_PHASE_4_CALCULS/B-46_Maconnerie.md",
    "06_PHASE_4_CALCULS/B-47_Escaliers.md",
    "06_PHASE_4_CALCULS/B-48_Predalles.md",
    "06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md",
    "06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md",
    "07_PHASE_5_LIVRABLES/B-34_Synthese_Reservations.md",
    "07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md",
    "07_PHASE_5_LIVRABLES/B-62_Nomenclature.md",
    "07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md",
    "08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md",
    "08_PHASE_6_CLOTURE/B-71_Indicage.md",
    "08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md",
    "09_TRANSVERSE/T-01_Sincerite.md",
    "09_TRANSVERSE/T-02_Recadrage.md",
    "09_TRANSVERSE/T-03_Meta_Amelioration.md",
    "09_TRANSVERSE/T-04_Demande_Complement.md",
    "11_HISTORIQUE/Journal_des_modifications.md",
    "12_EXEMPLES/Exemples_Phase_0.md",
]


def main() -> None:
    from carnac_compiler import extract_variables_table, sha256_bytes

    actual = {str(p.relative_to(DST)) for p in DST.rglob("*.md")}
    assert actual == set(ORDER), f"Écart d'arborescence : {sorted(actual ^ set(ORDER))}"

    entries = []
    for i, rel in enumerate(ORDER):
        content = (DST / rel).read_text(encoding="utf-8")
        entries.append(
            {
                "index": i + 1,
                "rel_path": rel,
                "has_leading_nl": True,
                "has_trailing_nl": True,
                "start_header": f"**[Début du fichier : {rel}]**\n",
                "end_line": f"**[Fin de {rel}]**\n",
                "separator_after": "\n---\n\n" if i < len(ORDER) - 1 else "",
                "bytes": len(content.encode("utf-8")),
                "lines": content.count("\n") + (0 if content.endswith("\n") else 1),
                "sha256": sha256_bytes(content.encode("utf-8")),
            }
        )

    dict_rel = "01_DICTIONNAIRE/CARNAC_v3.0_variables.md"
    rows = extract_variables_table((DST / dict_rel).read_text(encoding="utf-8"))
    import csv

    csv_path = DST / "01_DICTIONNAIRE/CARNAC_v3.0_variables.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Code", "Libellé", "Briques consommatrices"])
        w.writeheader()
        w.writerows(rows)

    parts = ["---\n\n"]
    for e in entries:
        body = "\n" + (DST / e["rel_path"]).read_text(encoding="utf-8") + "\n"
        parts += [e["start_header"], body, e["end_line"], e["separator_after"]]
    compiled = "".join(parts)
    COMPILED.write_text(compiled, encoding="utf-8")

    manifest = {
        "source_compiled_file": str(COMPILED),
        "source_bytes": len(compiled.encode("utf-8")),
        "source_lines": compiled.count("\n"),
        "source_sha256": sha256_bytes(compiled.encode("utf-8")),
        "markdown_files_count": len(entries),
        "total_tree_files_count": len(entries) + 1,
        "leading_prefix": "---\n\n",
        "generated_csv": {
            "rel_path": "01_DICTIONNAIRE/CARNAC_v3.0_variables.csv",
            "variable_count": len(rows),
            "bytes": csv_path.stat().st_size,
        },
        "files": entries,
    }
    (META / "MANIFEST_v3.0.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    # Contrôle aller-retour
    sys.path.insert(0, str(BASE / "_tools"))
    from carnac_compiler import compile_tree

    rebuilt = compile_tree(DST, META / "MANIFEST_v3.0.json")
    assert rebuilt == compiled.encode("utf-8"), "Recompilation non identique"
    print(f"Compilé : {manifest['source_bytes']:,} octets — SHA-256 {manifest['source_sha256']}")
    print(f"Fichiers Markdown : {len(entries)} · variables : {len(rows)} · aller-retour : 0 octet d'écart")


if __name__ == "__main__":
    main()
