#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-04 — PLAN DE TRAVAIL DÉGRADÉ (PTD) — JYCROISSY
Générateur / validateur (stdlib uniquement). Trois tableaux obligatoires +
synthèse — CARNAC v3.0.2, fiche B-04_PTD.md.

Entrées : MPD B-01 Ind B, FDC B-02 (17 VERROU), RDR B-03 (V-01…V-17), graphe de
dépendances (colonne « Bloque » / briques consommatrices du dictionnaire).
Sorties : PTD_JYCROISSY.md et PTD_jycroissy.csv.

Règles : blocage local jamais global ; aucun livrable exécutable en attente ;
PARAMÉTRIQUE filigrané + suffixe _P ; aucune brique SANS OBJET déclarée par le
modèle (réserve à la MPD) ; aucune valeur de repli.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "02_PHASE_0_CADRAGE"))

ID_01 = "JYCROISSY"

# ---------------------------------------------------------------------------
# Tableau 1 — Briques suspendues (brique | donnée bloquante | voie d'obtention |
# responsable | échéance). La brique consomme une donnée manquante produite par
# une autre brique, ou en attente d'une donnée externe.
# ---------------------------------------------------------------------------
SUSPENDUES = [
    ("B-13", "Détection et qualification des porteurs",
     "GEO-13 (matrice de recalage multi-sources vers le RSU)",
     "Production interne B-30 / B-31 (INTERNE-GO)",
     "BET d'exécution (MOE)", "Avant phase 2"),
    ("B-20", "Conception des ouvrages",
     "DEC-05 (hypothèses notifiées H-xx), GEO-13, NIV-07 (épaisseurs ASB / Fini)",
     "Production interne B-22 (DEC-05) et B-30 (GEO-13) ; NIV-07 ASB en attente "
     "(dallage « selon étude BA »)",
     "BET d'exécution (MOE)", "Phase 3"),
    ("B-34", "Carnet des réservations et trémies tous corps d'état",
     "DEC-05 (H-xx), GEO-13",
     "Production interne B-22 et B-30",
     "BET d'exécution (MOE)", "Phase 5"),
    ("B-60", "Plans d'exécution",
     "DEC-05 (H-xx), NIV-07 (épaisseurs ASB / Fini)",
     "Production interne B-22 ; NIV-07 ASB en attente",
     "BET d'exécution (MOE)", "Phase 5"),
    ("B-64", "Notice de synthèse",
     "DEC-02, DEC-03, DEC-05",
     "Production interne (DEC-02/DEC-03 déjà produits par B-03 ; DEC-05 par B-22)",
     "BET d'exécution (MOE)", "Phase 5"),
    ("B-70", "Auto-contrôle déclaré de synthèse",
     "DEC-01, DEC-02, DEC-03, DEC-05",
     "Production interne B-70 (DEC-01), B-03 (DEC-02/03), B-22 (DEC-05)",
     "BET d'exécution (MOE)", "Phase 6"),
    ("B-72", "Journal de clôture",
     "DEC-02, DEC-03, DEC-04, DOC-08",
     "Production interne B-72 (DOC-08, DEC-04) ; B-03 (DEC-02/03)",
     "BET d'exécution (MOE)", "Phase 6"),
]

# ---------------------------------------------------------------------------
# Tableau 2 — Briques exécutables immédiatement (brique | mode | motif).
# ---------------------------------------------------------------------------
# (brique, libellé, mode, motif)
EXECTABLES = [
    ("B-10", "Audit critique du CCTP", "COMPLET",
     "DOC-04 FOURNIE ; DEC-02 produit par B-03 (D-14)"),
    ("B-11", "Audit du diagnostic structure", "COMPLET",
     "DOC-05 FOURNIE ; s'appuie sur P2/P4/P5"),
    ("B-12", "Audit des pièces géotechniques", "PARTIEL-DÉCLARÉ",
     "Paramètres D-06 (qELS ≤ 0,30 MPa, qELU ≤ 0,49 MPa, ancrage 50 cm) ; G2 complet "
     "non reçu (réserve R-01)"),
    ("B-14", "Clarification du périmètre", "INTERNE-GO",
     "Périmètre à trancher produit par nos soins"),
    ("B-15", "Fiche de synthèse", "COMPLET",
     "DEC-03 produit par B-03 ; risques identifiés en phase 0"),
    ("B-21", "Note de calcul des charges", "COMPLET",
     "CHG-01…08 FOURNIE ou Décision (D-03)"),
    ("B-22", "Note d'hypothèses de conception", "INTERNE-GO",
     "Produit DEC-05 (hypothèses notifiées H-xx)"),
    ("B-23", "Vérification des éléments existants", "INTERNE-GO",
     "Produit EXI-05 (contrainte admissible transmise à l'existant)"),
    ("B-24", "Vérification des éléments existants non", "COMPLET",
     "DOC-05 FOURNIE ; PA-01 (D-06) encadre les inconnues physiques"),
    ("B-25", "Stabilité globale, contreventement, joints", "COMPLET",
     "CHG-07 FOURNIE ; STR-01 PARTIELLE"),
    ("B-30", "Calage des sources", "INTERNE-GO",
     "Produit GEO-07, GEO-08, GEO-12 (transformation, points de calage, seuils)"),
    ("B-31", "Recalage / superposition des niveaux", "INTERNE-GO",
     "Produit GEO-13 ; dépend de B-30 (GEO-07/08) et B-32 (GEO-11)"),
    ("B-32", "Exploitation vectorielle / nettoyage", "INTERNE-GO",
     "Produit GEO-10, GEO-11 (seuils d'épaisseur, superposition)"),
    ("B-33", "Vérification croisée", "COMPLET",
     "GEO-14 PARTIELLE ; DOC-02"),
    ("B-40", "Fondations superficielles", "PARTIEL-DÉCLARÉ",
     "SOL-01/02/03 décision D-06 ; B-40 non bloquante (D-12) ; PA-01 contrôle fouille"),
    ("B-42", "Verticaux BA", "COMPLET",
     "MAT-01/04 FOURNIE ; CHG-02 Décision (D-03)"),
    ("B-45", "Structure métallique", "COMPLET",
     "MAT-05 FOURNIE ; CHG-06 FOURNIE"),
    ("B-46", "Maçonnerie : vérification", "INTERNE-GO",
     "Produit EXI-05 par calcul interne"),
    ("B-47", "Escaliers", "COMPLET",
     "NIV-03 FOURNIE ; CHG-08 PARTIELLE"),
    ("B-49", "Linteaux et seuils", "COMPLET",
     "MAT-09 FOURNIE ; EXI-01 PARTIELLE"),
    ("B-50", "Assemblages et ancrages", "COMPLET",
     "MAT-04/09 FOURNIE ; EXI-01/03 PARTIELLE"),
    ("B-62", "Nomenclature / quantités", "COMPLET",
     "MAT-xx FOURNIE"),
    ("B-71", "Indicage et supersession documentaire", "INTERNE-GO",
     "Produit DEC-04 (documents supersédés)"),
]

# ---------------------------------------------------------------------------
# Tableau 3 — Briques exécutables en PARAMÉTRIQUE (brique | donnée en symbole |
# forme littérale possible | ce qui ne sera PAS produit).
# ---------------------------------------------------------------------------
PARAMETRiques = [
    ("B-43", "Planchers et dallages",
     "NIV-06 (épaisseurs plancher), NIV-07 (épaisseurs ASB / complexe)",
     "Dallage neuf « selon étude BA » (P1 p34-36) — symbole d'épaisseur",
     "Ne produit PAS : valeur d'épaisseur retenue, DXF exécutable, plan à diffuser"),
    ("B-44", "Charpente bois",
     "MAT-06 (classe bois C18/C24 — hypothèse du diagnostic), MAT-08 (classe de "
     "service)",
     "Bois C18/C24 en hypothèse (P2 p10-17) — symbole",
     "Ne produit PAS : valeur de classe de bois validée, note exécutable sans réserve"),
]

# ---------------------------------------------------------------------------
# Briques SANS OBJET — statut fixé par la MPD (jamais par le PTD).
# ---------------------------------------------------------------------------
SANS_OBJET = [
    ("B-41", "Fondations profondes", "D-11"),
    ("B-48", "Prédalles et planchers préfabriqués", "D-09"),
]

PRODUITS = ["B-00", "B-01", "B-02", "B-03", "B-04"]


def build_md():
    L = []
    a = L.append
    a("# B-04 — PLAN DE TRAVAIL DÉGRADÉ (PTD) — JYCROISSY")
    a("")
    a("| Champ | Valeur |")
    a("|---|---|")
    a("| Code projet (ID-01) | %s |" % ID_01)
    a("| Carnet | CARNAC v3.0.2 — fiche `02_PHASE_0_CADRAGE/B-04_PTD.md` |")
    a("| Indice | **B-04 — 2026-10-30** (PTD — instantané phase 0) |")
    a("| Entrées | MPD B-01 Ind B ; FDC B-02 ; RDR B-03 ; graphe de dépendances |")
    a("| Sortie | 3 tableaux (suspendues / exécutables / PARAMÉTRIQUE) + synthèse |")
    a("")
    a("> **Statut** : instantané des briques qui peuvent tourner et de celles qui sont "
      "bloquées à l'ouverture de la phase 1. Régénéré à chaque blocage. Le PTD est "
      "annexé au RDR (B-03).")
    a("")
    a("---")
    a("")
    a("## TABLEAU 1 — BRIQUES SUSPENDUES")
    a("")
    a("*%d briques.* Chaque brique suspendue identifie la donnée qui la bloque ; le "
      "projet, lui, n'est **pas** suspendu (blocage local, jamais global — verrou V11)."
      % len(SUSPENDUES))
    a("")
    a("| Brique | Donnée bloquante (code) | Voie d'obtention | Responsable | Échéance |")
    a("|---|---|---|---|---|")
    for br, lib, donnee, voie, resp, ech in SUSPENDUES:
        a("| %s (%s) | %s | %s | %s | %s |" % (br, lib, donnee, voie, resp, ech))
    a("")
    a("---")
    a("")
    a("## TABLEAU 2 — BRIQUES EXÉCUTABLES IMMÉDIATEMENT")
    a("")
    a("*%d briques.* Aucune dépendance à une donnée manquante non produite ; mode "
      "COMPLET, PARTIEL-DÉCLARÉ (décision RDR) ou INTERNE-GO (conception produite par "
      "nos soins)." % len(EXECTABLES))
    a("")
    a("| Brique | Mode | Motif (aucune dépendance à la donnée manquante) |")
    a("|---|---|---|")
    for br, lib, mode, motif in EXECTABLES:
        a("| %s (%s) | %s | %s |" % (br, lib, mode, motif))
    a("")
    a("---")
    a("")
    a("## TABLEAU 3 — BRIQUES EXÉCUTABLES EN PARAMÉTRIQUE")
    a("")
    a("*%d briques.* Une donnée manque sans décision RDR : le livrable est émis "
      "**filigrané** « PROVISOIRE — EN ATTENTE DE [donnée] » et **suffixé `_P`** — non "
      "exécutable, non diffusable." % len(PARAMETRiques))
    a("")
    a("| Brique | Donnée laissée en symbole | Forme littérale possible | Ce qui ne sera PAS produit |")
    a("|---|---|---|---|")
    for br, lib, sym, forme, nap in PARAMETRiques:
        a("| %s (%s) | %s | %s | %s |" % (br, lib, sym, forme, nap))
    a("")
    a("---")
    a("")
    a("## SYNTHÈSE (3 points)")
    a("")
    a("### a) Ce qui reste bloqué tant que la donnée n'est pas obtenue")
    a("")
    a("* **B-13** (détection/qualification) attend **GEO-13** (matrice de recalage RSU), "
      "produite en fin de phase 1 (B-30/B-31).")
    a("* **B-20** (conception) attend **DEC-05** (hypothèses H-xx, produites par B-22) "
      "et **GEO-13** ; **NIV-07** reste partiellement ouvert (cotes ASB / épaisseurs "
      "neuves, dallage « selon étude BA »).")
    a("* **B-34, B-60, B-64** (réservations, plans d'exécution, notice de synthèse) "
      "attendent **DEC-05** et **GEO-13**.")
    a("* **B-70, B-72** (auto-contrôle, journal de clôture) attendent **DEC-01/02/03/04/05** "
      "et **DOC-08** — ce sont des briques de clôture, donc leur suspension est "
      "terminale par construction.")
    a("* **Aucune donnée n'est Classe III rédhibitoire** (0 BLOQUANTE à ce stade, "
      "MPD Ind B) : chaque blocage est en attente d'une **production interne** "
      "(INTERNE-GO) ou d'une **donnée externe** (réserves R-01 à R-10 du RDR).")
    a("")
    a("### b) Impact sur la date de remise des livrables exécutables")
    a("")
    a("* **Phase 1 (socle géométrique)** : B-30 → B-32 → B-31 sont **exécutables dès "
      "maintenant** en INTERNE-GO : le calage, le nettoyage vectoriel et le recalage "
      "produisent eux-mêmes les paramètres (GEO-07 à GEO-13) qui leur manquaient. "
      "Aucun retard induit.")
    a("* **Phase 2 (audit croisé)** : B-10, B-11, B-12, B-14, B-15 exécutables "
      "immédiatement ; B-13 suit la phase 1.")
    a("* **Phase 3 (conception)** : B-20 (conception) est suspendue jusqu'à la "
      "production de DEC-05/GEO-13 ; B-21, B-24, B-25 exécutables ; B-22, B-23 "
      "INTERNE-GO.")
    a("* **Phase 5 (livrables d'exécution — B-60 plans d'exécution)** : la remise des "
      "plans exécutables est **reportée** tant que NIV-07 (épaisseurs ASB) et DEC-05 "
      "ne sont pas levés. Livrable intermédiaire : **B-43/B-44 en PARAMÉTRIQUE** "
      "(filigranés, non exécutables).")
    a("* **Phase 6 (clôture)** : B-70/B-71/B-72 terminales par construction.")
    a("")
    a("### c) Livrables PARAMÉTRIQUE émis immédiatement")
    a("")
    a("* **B-43** — note de calcul des planchers/dallages, **`_P`**, filigrané « "
      "PROVISOIRE — EN ATTENTE DE NIV-06/NIV-07 (épaisseurs) » — pas de valeur "
      "d'épaisseur retenue, pas de DXF exécutable.")
    a("* **B-44** — note de calcul de charpente bois, **`_P`**, filigrané « "
      "PROVISOIRE — EN ATTENTE DE MAT-06/MAT-08 (classe bois) » — pas de valeur de "
      "classe validée.")
    a("")
    a("---")
    a("")
    a("## RÉCAPITULATIF DES BRIQUES")
    a("")
    a("| Statut | Nb | Briques |")
    a("|---|---:|---|")
    a("| Produites (phase 0) | %d | %s |" % (len(PRODUITS), ", ".join(PRODUITS)))
    a("| Suspendues | %d | %s |" % (len(SUSPENDUES),
                                   ", ".join(b[0] for b in SUSPENDUES)))
    a("| Exécutables immédiatement | %d | %s |" % (len(EXECTABLES),
                                                  ", ".join(b[0] for b in EXECTABLES)))
    a("| Exécutables en PARAMÉTRIQUE | %d | %s |" % (len(PARAMETRiques),
                                                    ", ".join(b[0] for b in PARAMETRiques)))
    a("| SANS OBJET (MPD) | %d | %s |" % (len(SANS_OBJET),
                                         ", ".join(b[0] for b in SANS_OBJET)))
    a("")
    a("---")
    a("")
    a("## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE")
    a("")
    a("| Critère de la fiche B-04 | Statut |")
    a("|---|---|")
    a("| Chaque brique suspendue identifie la donnée qui la bloque | ✅ (tableau 1) |")
    a("| Chaque brique exécutable est justifiée | ✅ (tableau 2, motif par brique) |")
    a("| Chaque PARAMÉTRIQUE précise forme littérale et ce qui n'est pas produit | ✅ (tableau 3) |")
    a("| Aucune valeur de repli proposée | ✅ |")
    a("| Aucune brique déclarée SANS OBJET par le modèle | ✅ (B-41/B-48 fixés par la MPD D-11/D-09) |")
    a("| Synthèse mentionne explicitement l'impact planning | ✅ (§synthèse b) |")
    a("| Zéro placeholder (V7) | ✅")
    a("")
    a("**Brique B-04 livrée — en attente de votre GO pour la phase 1 (B-30/B-32/B-31) "
      "ou pour la prochaine brique exécutable selon le PTD.**")
    a("")
    return "\n".join(L)


def build_csv():
    path = os.path.join(OUT_DIR, "PTD_jycroissy.csv")
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Tableau", "Brique", "Libellé", "Colonne2", "Colonne3",
                    "Colonne4", "Colonne5"])
        for br, lib, donnee, voie, resp, ech in SUSPENDUES:
            w.writerow(["Suspendue", br, lib, donnee, voie, resp, ech])
        for br, lib, mode, motif in EXECTABLES:
            w.writerow(["Exécutable", br, lib, mode, motif, "", ""])
        for br, lib, sym, forme, nap in PARAMETRiques:
            w.writerow(["Paramétrique", br, lib, sym, forme, nap, ""])
        for br, lib, d in SANS_OBJET:
            w.writerow(["Sans objet", br, lib, d, "", "", ""])
    return path


def main():
    md = build_md()
    md_path = os.path.join(OUT_DIR, "PTD_JYCROISSY.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    csv_path = build_csv()

    allb = ([b[0] for b in SUSPENDUES] + [b[0] for b in EXECTABLES]
            + [b[0] for b in PARAMETRiques] + [b[0] for b in SANS_OBJET]
            + PRODUITS)
    assert len(allb) == len(set(allb)), "brique répétée dans le PTD"
    for b in SUSPENDUES:
        assert b[2] and b[2] != "—", b[0]
        assert b[3] and b[3] != "—", b[0]
    for b in EXECTABLES:
        assert b[2] in ("COMPLET", "PARTIEL-DÉCLARÉ", "INTERNE-GO"), b[0]
        assert b[3] and b[3] != "—", b[0]
    for b in PARAMETRiques:
        assert b[3] and b[4] and b[4] != "—", b[0]
    for line in (md + "\n").splitlines():
        assert "{{" not in line and "}}" not in line, "placeholder V7"

    print("B-04 PTD généré :")
    print("  -", md_path)
    print("  -", csv_path)
    print("  suspendues : %d | exécutables : %d | paramétrique : %d | "
          "sans objet : %d | produits : %d"
          % (len(SUSPENDUES), len(EXECTABLES), len(PARAMETRiques),
             len(SANS_OBJET), len(PRODUITS)))
    print("  validations : OK (donnée bloquante, motif, forme littérale, V7)")


if __name__ == "__main__":
    main()
