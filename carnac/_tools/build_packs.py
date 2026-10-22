#!/usr/bin/env python3
"""Génération des packs prêts à coller dans une discussion (CARNAC v3.0)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
SRC = BASE / "CARNAC_v3.0"
OUT = BASE / "CARNAC_v3.0_PACKS"

SOCLE = [
    "00_MASTER.md",
    "10_ANNEXES/A_Conventions_Livrables.md",
    "10_ANNEXES/A1_Addendum_v3.0.1.md",
    "10_ANNEXES/D_Mode_Emploi.md",
    "10_ANNEXES/O_Outillage.md",
    "01_DICTIONNAIRE/CARNAC_v3.0_variables.md",
]
P0 = [f"02_PHASE_0_CADRAGE/{n}.md" for n in [
    "B-00_Inventaire", "B-01_MPD", "B-02_FDC", "B-03_RDR", "B-04_PTD"]]
P12 = [f"03_PHASE_1_ANALYSE/{n}.md" for n in [
    "B-10_Audit_CCTP", "B-11_Audit_Diagnostic", "B-12_Audit_Geotechnique",
    "B-13_Contradictions", "B-14_Perimetre_Lot", "B-15_Synthese_Risques"]] + [
    f"05_PHASE_3_CALAGE/{n}.md" for n in [
        "B-30_Calage", "B-32_Vue_Nettoyee", "B-31_Preuve_Superposition"]]
P3 = [f"04_PHASE_2_CONCEPTION/{n}.md" for n in [
    "B-20_Conception_GO", "B-25_Stabilite_Globale", "B-21_DDC_Preliminaire",
    "B-22_Note_Hypotheses", "B-23_Exploitation_Diagnostic", "B-24_Existant_Non_Sonde"]]
P4 = [f"06_PHASE_4_CALCULS/{n}.md" for n in [
    "B-40_Fondations_Superficielles", "B-41_Fondations_Profondes", "B-42_Verticaux_BA",
    "B-43_Planchers_Dallages", "B-44_Charpente_Bois", "B-45_Structure_Metallique",
    "B-46_Maconnerie", "B-47_Escaliers", "B-48_Predalles", "B-49_Linteaux_Seuils",
    "B-50_Assemblages_Ancrages"]]
P56 = [f"07_PHASE_5_LIVRABLES/{n}.md" for n in [
    "B-34_Synthese_Reservations", "B-60_Plans_Execution", "B-62_Nomenclature",
    "B-64_Notice_Synthese"]] + ["05_PHASE_3_CALAGE/B-33_Verification_Croisee.md"] + [
    f"08_PHASE_6_CLOTURE/{n}.md" for n in [
        "B-70_AutoControle_Synthese", "B-71_Indicage", "B-72_Journal_Cloture"]]
TRANSVERSE = [f"09_TRANSVERSE/{n}.md" for n in [
    "T-01_Sincerite", "T-02_Recadrage", "T-03_Meta_Amelioration", "T-04_Demande_Complement"]]

PACKS = [
    {
        "file": "00_SOCLE.md",
        "titre": "PACK 00 — SOCLE (à coller en premier, toujours)",
        "quand": "À l'ouverture de CHAQUE nouvelle discussion, avant toute pièce de projet.",
        "contient": "Document maître (protocole §0, 15 verrous, 6 modes, `CFG-1..4`, gabarits, ordonnancement) · annexe A (livrables, pureté structurelle) · annexe D (mode d'emploi) · annexe O (outillage et protocole CAO) · dictionnaire des 106 variables.",
        "note": "Ce pack suffit à faire comprendre le protocole à une IA. Il ne permet pas encore de produire une brique : il faut y ajouter le pack de la phase concernée.",
        "files": SOCLE,
    },
    {
        "file": "01_PHASE_0.md",
        "titre": "PACK 01 — PHASE 0 : CADRAGE (B-00 à B-04)",
        "quand": "Après le socle, au démarrage de l'affaire.",
        "contient": "B-00 inventaire et qualification `CFG-01` · B-01 MPD, gabarit `CFG-02`, découpage `CFG-03` · B-02 FDC et table `NIV-07` · B-03 RDR à quatre registres · B-04 PTD.",
        "note": "À la sortie de ce pack, vous devez avoir validé : la configuration MOE, le gabarit, la MPD ligne à ligne et la table des niveaux.",
        "files": P0,
    },
    {
        "file": "02_PHASES_1-2.md",
        "titre": "PACK 02 — PHASES 1 ET 2 : SOCLE GÉOMÉTRIQUE PUIS AUDIT CROISÉ (B-30, B-32, B-31 puis B-10 à B-15)",
        "quand": "Une fois le cadrage validé, avant toute conception.",
        "contient": "B-30 calage multi-sources · B-32 vue nettoyée différentielle · B-31 preuve de superposition · puis B-10 à B-15 (audits, contradictions, périmètre de lot, risques et Pré-Audit Flash).",
        "note": "Ordre imposé par le carnet : le calage et le nettoyage AVANT l'audit. Ne permutez pas les fiches dans ce pack.",
        "files": P12,
    },
    {
        "file": "03_PHASE_3.md",
        "titre": "PACK 03 — PHASE 3 : CONCEPTION ET SYNTHÈSE STRUCTURELLE (B-20 à B-25)",
        "quand": "Après validation de l'audit croisé.",
        "contient": "B-20 synthèse indissociable sur fond nettoyé · B-25 stabilité globale et contreventement · B-21 descente de charges · B-22 hypothèses `H-xx` · B-23 exploitation du diagnostic · B-24 existant non sondé et `PA-xx`.",
        "note": "C'est le pack qui contient les deux fiches les plus sensibles du carnet (B-20 et B-25) : c'est ici que se joue la conformité de la synthèse.",
        "files": P3,
    },
    {
        "file": "04_PHASE_4.md",
        "titre": "PACK 04 — PHASE 4 : CALCULS D'EXÉCUTION (B-40 à B-50)",
        "quand": "Quand la conception et la stabilité globale sont visées.",
        "contient": "Onze fiches de calcul : fondations superficielles et profondes, verticaux BA, planchers et dallages, charpente bois, structure métallique, maçonnerie, escaliers, prédalles, linteaux et seuils, assemblages et ancrages.",
        "note": "Pack le plus lourd (~97 000 tokens). Si votre contexte est limité, deux coupures possibles sont matérialisées dans le fichier : `B-40` à `B-45`, puis `B-46` à `B-50`.",
        "files": P4,
        "coupes": ["06_PHASE_4_CALCULS/B-45_Structure_Metallique.md"],
    },
    {
        "file": "05_PHASES_5-6.md",
        "titre": "PACK 05 — PHASES 5 ET 6 : RÉSERVATIONS, LIVRABLES, VÉRIFICATION ET CLÔTURE (B-34, B-60 à B-64, B-33, B-70 à B-72)",
        "quand": "Quand les notes de calcul sont visées.",
        "contient": "B-34 réservations tous corps d'état · B-60 plans d'exécution purs · B-62 nomenclature · B-64 notice · B-33 vérification croisée globale · B-70 auto-contrôle · B-71 indiçage · B-72 clôture. En annexe, les quatre prompts transverse T-01 à T-04.",
        "note": "L'annexe transverse est séparée par un repère de coupure : vous ne la collez que si vous invoquez T-01, T-02, T-03 ou T-04.",
        "files": P56,
        "annexe": {"titre": "ANNEXE AU PACK 05 — PROMPTS TRANSVERSE (T-01 à T-04), à coller seulement si nécessaire", "files": TRANSVERSE},
    },
]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def build_pack(spec: dict) -> tuple[str, dict]:
    parts: list[str] = []
    total_tokens = 0
    integrity = []
    prerequis = (
        "**Prérequis** : aucun — ce pack se colle en premier, à l'ouverture de la discussion."
        if spec["file"] == "00_SOCLE.md"
        else "**Prérequis** : le pack `00_SOCLE.md` doit être collé avant celui-ci, dans la même discussion."
    )
    header = f"""<!-- PACK CARNAC v3.0 — {spec['titre']} -->

# {spec['titre']}

**Quand coller ce pack** : {spec['quand']}

**Ce qu'il contient** : {spec['contient']}

**Note d'usage** : {spec['note']}

{prerequis}

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
"""
    parts.append(header)

    def emit(files: list[str]) -> None:
        nonlocal total_tokens
        for i, rel in enumerate(files):
            content = (SRC / rel).read_text(encoding="utf-8")
            integrity.append({"rel_path": rel, "bytes": len(content.encode()), "sha256": sha(content.encode())})
            total_tokens += int(len(content) / 3.3)
            parts.append(f"**[Début du fichier : {rel}]**\n")
            parts.append("\n" + content + "\n")
            parts.append(f"**[Fin de {rel}]**\n")
            last = i == len(files) - 1
            if not last:
                parts.append("\n---\n\n")
            if spec.get("coupes") and rel == spec["coupes"][0]:
                parts.append(
                    "\n<!-- ================= COUPURE POSSIBLE ================= -->\n"
                    "> **Coupure de confort (facultative)** : si votre fenêtre de contexte est limitée, vous pouvez arrêter le collage ici "
                    "et coller la suite (`B-46` à `B-50`) dans une seconde discussion. Aucune règle du carnet ne dépend de la continuité de ce pack.\n\n"
                )

    emit(spec["files"])

    if spec.get("annexe"):
        parts.append("\n---\n\n<!-- ================= COUPURE ================= -->\n\n")
        parts.append(f"# {spec['annexe']['titre']}\n\n---\n\n")
        emit(spec["annexe"]["files"])

    parts.append("\n<!-- FIN DU PACK — CARNAC v3.0 -->\n")
    text = "".join(parts)
    return text, {
        "pack": spec["file"],
        "titre": spec["titre"],
        "bytes": len(text.encode()),
        "chars": len(text),
        "estimated_tokens": total_tokens,
        "files": integrity,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for spec in PACKS:
        text, meta = build_pack(spec)
        (OUT / spec["file"]).write_text(text, encoding="utf-8")
        manifest.append(meta)
        print(f"{spec['file']:22s} {meta['bytes']:9,d} octets  ~{meta['estimated_tokens']:7,d} tokens  ({len(meta['files'])} fichiers)")
    (OUT / "PACKS_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    total = sum(m["estimated_tokens"] for m in manifest)
    print(f"{'TOTAL des 6 packs':22s} {'':9s}          ~{total:7,d} tokens")


if __name__ == "__main__":
    main()
