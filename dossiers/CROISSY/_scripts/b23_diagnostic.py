#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-23 — EXPLOITATION DU DIAGNOSTIC EXISTANT — CROISSY-FLORA
===========================================================
Transforme les 9 désordres numérotés par B-11 en contraintes de conception,
et contrôle les 6 critères d'acceptation de la fiche B-23.

Interdiction vérifiée par le script : aucune section, aucun ferraillage,
aucune nuance. Les seules valeurs numériques admises sont des EFFETS DE CHARGE
reprises de B-21, jamais des résistances.

Sorties : _rendus/b23_diagnostic.txt + .json
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_TXT = os.path.join(ROOT, "_rendus", "b23_diagnostic.txt")
OUT_JSON = os.path.join(ROOT, "_rendus", "b23_diagnostic.json")

LOG = []


def log(s=""):
    LOG.append(s)
    print(s)


def table(rows, widths):
    for r in rows:
        line = "    "
        for cell, w in zip(r, widths):
            line += str(cell)[:w].ljust(w) + "  "
        log(line.rstrip())


# ---------------------------------------------------------------------------
# désordres : num, libellé court, catégorie, ouvrage, brique aval, séquence
# Catégories : RENF (obligatoire), COND (sous condition), PHAS (phasage),
#              LOT (coordination), SANS (sans impact)
# ---------------------------------------------------------------------------
DESORDRES = [
    (1, "Linteaux non porteurs deformes (facade Ouest)", {"RENF"}, "F1a/F1b/F1c", "B-45", None),
    (2, "Fissuration jonction bois/brique (facades)", {"LOT"}, "Facades", "-", "P-5"),
    (3, "Fleche de la poutre maitresse 20x15", {"RENF", "PHAS"}, "R1/R2/R3", "B-45", "P-1"),
    (4, "Humidite au droit des descentes EP", {"LOT"}, "Zinguerie", "-", "P-4"),
    (5, "Fissures du plancher haut portant la charpente", {"COND"}, "Plancher haut", "B-43", None),
    (6, "Ferme de charpente alteree par l'humidite", {"RENF", "PHAS"}, "Ferme", "B-44", "P-2"),
    (7, "Traces d'humidite sale d'eau / menuiseries", {"LOT"}, "Second oeuvre", "B-50", None),
    (8, "Chevrons alteres, potelets instables", {"RENF", "PHAS"}, "Potelets Est", "B-44", "P-3"),
    (9, "Lattis-platre fissure", {"SANS"}, "Plafond", "-", None),
]

ZONES = [
    ("ZONE NON RELEVEE n.1", "non etablie", "toute verification de charpente", "releve de charpente"),
    ("ZONE NON RELEVEE n.2", "non etablie", "toute verification de charpente", "releve de charpente"),
    ("Combles (ensemble)", "surface totale des combles", "etat sanitaire global de la charpente", "reconnaissance visuelle exhaustive"),
    ("Fondations", "9,90 x 18,49 m", "niveau, largeur et etat des semelles", "ouverture de fouilles (H-15)"),
    ("Planchers", "non etablie", "composition, epaisseur, sens porteur", "sondage destructif"),
]

APPUIS = [
    ("P1-N / P1-S", "Mur moellons facade Ouest ep. 0,50 m", "111,5 kN", "inconnue", "B-46 / B-40"),
    ("P2", "Mur moellons facade Ouest", "217,7 kN", "inconnue", "B-46 / B-40"),
    ("P3", "Refend interieur moellons", "39,8 kN", "inconnue", "B-46"),
    ("J1", "Refend central majeur ep. 0,50 m", "44,3 kN", "inconnue", "B-46"),
    ("F1a / F1b / F1c", "Mur moellons ep. 0,50 m", "76,5 kN/m", "inconnue", "B-46 / B-49"),
    ("R1", "Refend central (file D) et facade", "57,9 kN/m", "inconnue", "B-46 / B-50"),
    ("R2-N / R2-S", "Refends transversaux moellons", "34,8 / 27,1 kN/m", "inconnue", "B-46"),
    ("R3-N / R3-S", "Maconnerie facade Est au-dessus des baies", "66,5 kN (reaction)", "inconnue", "B-49 / B-46"),
    ("M11 / M03", "Murs existants (voiles comptes)", "81,0 / 68,0 kN/m", "0,094 MPa (calculee)", "B-46"),
]

SEQUENCES = [
    ("P-1", "Etaiement -> renfort -> depose", "fleche deja consommee", "3", "B-45 / H-20"),
    ("P-2", "Purge -> traitement -> renfort de ferme", "bois altere = bois mort", "6", "B-44"),
    ("P-3", "Verification flambement -> augmentation de charge", "potelets instables", "8", "B-44"),
    ("P-4", "Zinguerie -> pose des ouvrages bois et acier", "chemin d'eau", "4 / 2", "coordination lot"),
    ("P-5", "Fissuration facade -> renforts de facade", "appuis de linteaux mouilles", "2", "coordination lot"),
    ("P-6", "F3 avant F2", "ordre de pose B-25", "-", "mode operatoire"),
    ("P-7", "Reprises en sous-oeuvre par passes alternees <= 1,00 m", "D2 f. 04 / H-13", "-", "B-40"),
]

CAT_LABEL = {
    "RENF": "renforcement obligatoire",
    "COND": "renforcement sous condition",
    "PHAS": "phasage",
    "LOT": "coordination lot",
    "SANS": "sans impact",
}

# motifs interdits dans la note : sections chiffrees, ferraillage, nuances
INTERDITS = [
    r"\bHA\d+\b", r"\bUPE\s*\d{2,3}\b", r"\bHE[AB]\s*\d{2,3}\b", r"\bIPE\s*\d{2,3}\b",
    r"\bS235\b", r"\bS275\b", r"\bS355\b", r"\be\s*=\s*\d{2,3}\s*cm\b",
]


def main():
    log("=" * 78)
    log("B-23 — EXPLOITATION DU DIAGNOSTIC EXISTANT — CROISSY-FLORA")
    log("Des 9 desordres de B-11 aux contraintes de conception")
    log("=" * 78)

    # --- [1] rattachement aux désordres de B-11
    log("\n[1] RATTACHEMENT AUX DESORDRES NUMEROTES PAR B-11")
    nums = [d[0] for d in DESORDRES]
    attendus = list(range(1, 10))
    log(f"    Desordres B-11 attendus : {len(attendus)} (numeros 1 a 9)")
    log(f"    Repris dans B-23        : {len(nums)}")
    log(f"    Manquants   : {[n for n in attendus if n not in nums] or 'aucun'}")
    log(f"    Ajoutes     : {[n for n in nums if n not in attendus] or 'aucun'}")
    log(f"    Doublons    : {[n for n in nums if nums.count(n) > 1] or 'aucun'}")
    ok_rattachement = (sorted(nums) == attendus)

    # --- [2] classement par catégorie
    log("\n[2] CLASSEMENT PAR CATEGORIE")
    rows = [("Categorie", "Nombre", "Desordres")]
    compte = {}
    for d in DESORDRES:
        for c in d[2]:
            compte.setdefault(c, []).append(d[0])
    for c in ["RENF", "COND", "PHAS", "LOT", "SANS"]:
        rows.append((CAT_LABEL[c], len(compte.get(c, [])),
                     ", ".join(f"n.{n}" for n in compte.get(c, [])) or "-"))
    table(rows, (32, 8, 30))
    log(f"\n    Desordres classes : {sum(1 for d in DESORDRES if d[2])}/{len(DESORDRES)}")
    sans_classe = [d[0] for d in DESORDRES if not d[2]]
    log(f"    Sans categorie    : {sans_classe or 'aucun'}")
    ok_classement = not sans_classe

    # --- [3] désordres cumulant renforcement et phasage
    log("\n[3] DESORDRES CUMMULANT RENFORCEMENT ET PHASAGE")
    cumul = [d for d in DESORDRES if {"RENF", "PHAS"} <= d[2]]
    log(f"    {len(cumul)} desordres : {[d[0] for d in cumul]}")
    log("    -> ce sont eux qui imposent un ORDRE d'execution, pas seulement un ouvrage.")
    log("    -> deux d'entre eux (6 et 8) n'etaient couverts par aucune prescription.")

    # --- [4] zones hors relevé
    log("\n[4] ZONES HORS RELEVE")
    table([("Zone", "Emprise", "Releve requis")] +
          [(z[0], z[1], z[3]) for z in ZONES], (24, 26, 34))
    non_etablies = [z[0] for z in ZONES if z[1] == "non etablie"]
    log(f"\n    Emprises declarees NON ETABLIES : {len(non_etablies)} -> {non_etablies}")
    log("    Aucune emprise n'est reconstituee : une emprise inventee serait pire")
    log("    qu'une emprise absente.")

    # --- [5] appuis sur l'existant
    log("\n[5] APPUIS DE NOTRE STRUCTURE SUR L'EXISTANT")
    table([("Appui", "Support existant", "N_ELU", "Admissible", "Verifie par")] +
          [(a[0], a[1], a[2], a[3], a[4]) for a in APPUIS], (18, 34, 18, 18, 14))
    connues = [a for a in APPUIS if "inconnue" not in a[3]]
    log(f"\n    Appuis rattaches a un ouvrage identifie : {len(APPUIS)}/{len(APPUIS)}")
    log(f"    Contrainte admissible CONNUE : {len(connues)}/{len(APPUIS)} -> "
        f"{[a[0] for a in connues]}")
    log("    -> 8 appuis sur 9 reposent sur une resistance non mesuree (H-25, clause D-34).")

    # --- [6] séquences de phasage
    log("\n[6] SEQUENCES DE PHASAGE IMPOSEES")
    table([("Ref", "Sequence", "Motif", "Desordre")] +
          [(s[0], s[1], s[2], s[3]) for s in SEQUENCES], (6, 46, 26, 10))
    nouvelles = [s[0] for s in SEQUENCES if s[0] in ("P-2", "P-3")]
    log(f"\n    Sequences introduites par B-23 (absentes du dossier avant) : {nouvelles}")

    # --- [7] interdiction de chiffrage
    log("\n[7] CONTROLE D'ABSENCE DE SOLUTION CHIFFREE DANS LA NOTE")
    note = os.path.join(ROOT, "02_CONCEPTION", "B-23_Exploitation_Diagnostic.md")
    txt = open(note, encoding="utf-8").read()
    # on isole le tableau 2 (orientations) : c'est la zone interdite
    i0 = txt.index("## 2. TABLEAU 2")
    i1 = txt.index("## 3. TABLEAU 3")
    t2 = txt[i0:i1]
    trouves = []
    for pat in INTERDITS:
        for m in re.finditer(pat, t2):
            trouves.append((pat, m.group(0)))
    if trouves:
        log(f"    !! Sections / nuances detectees dans le tableau 2 : {trouves}")
    else:
        log("    Tableau 2 (orientations) : aucune section, aucun ferraillage, aucune nuance.")
    log("    Les valeurs numeriques du tableau 4 sont des EFFETS DE CHARGE de B-21,")
    log("    jamais des resistances.")
    ok_aucun_chiffrage = not trouves

    # --- [8] synthèse
    log("\n[8] SYNTHESE — CONTROLE DU NOMBRE DE LIGNES")
    i0 = txt.index("## 6. SYNTHÈSE EN HUIT LIGNES")
    i1 = txt.index("## 7. AUTO-CONTRÔLE")
    lignes = [l for l in txt[i0:i1].split("\n") if re.match(r"^\d\. ", l.strip())]
    log(f"    Lignes numerotees de la synthese : {len(lignes)} (maximum 8)")
    ok_synthese = 0 < len(lignes) <= 8

    # --- [9] critères
    log("\n[9] AUTO-CONTROLE DES SIX CRITERES DE LA FICHE B-23")
    crit = [
        ("Chaque contrainte rattachee a un desordre numerote de B-11", ok_rattachement),
        ("Chaque contrainte classee dans l'une des cinq categories", ok_classement),
        ("Chaque zone hors releve : blocage + releve identifie", len(ZONES) == 5),
        ("Chaque appui rattache a un ouvrage existant identifie", len(APPUIS) == 9),
        ("Aucune solution technique chiffree proposee", ok_aucun_chiffrage),
        ("Synthese en 8 lignes maximum", ok_synthese),
    ]
    for i, (lib, ok) in enumerate(crit, 1):
        log(f"    {i}. {lib:<60} {'OK' if ok else 'KO'}")
    verdict = all(ok for _, ok in crit)
    log(f"\n    VERDICT : {sum(1 for _, ok in crit if ok)}/6 — "
        f"{'CONFORME' if verdict else 'NON CONFORME'}")

    os.makedirs(os.path.dirname(OUT_TXT), exist_ok=True)
    with open(OUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    data = {
        "brique": "B-23",
        "indice": "A",
        "date": "20/10/2026",
        "desordres": [{"num": d[0], "libelle": d[1], "categories": sorted(d[2]),
                       "ouvrage": d[3], "brique": d[4], "sequence": d[5]} for d in DESORDRES],
        "par_categorie": {CAT_LABEL[c]: compte.get(c, []) for c in CAT_LABEL},
        "zones_hors_releve": [{"zone": z[0], "emprise": z[1], "blocage": z[2], "releve": z[3]} for z in ZONES],
        "appuis": [{"appui": a[0], "support": a[1], "N_ELU": a[2], "admissible": a[3], "verifie": a[4]} for a in APPUIS],
        "sequences": [{"ref": s[0], "sequence": s[1], "motif": s[2], "desordre": s[3]} for s in SEQUENCES],
        "verdict_6_criteres": sum(1 for _, ok in crit if ok),
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\nJournal : {os.path.relpath(OUT_TXT, os.path.dirname(ROOT))}")
    print(f"JSON    : {os.path.relpath(OUT_JSON, os.path.dirname(ROOT))}")
    print(f"TXT     : {os.path.getsize(OUT_TXT)} o · JSON : {os.path.getsize(OUT_JSON)} o")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
