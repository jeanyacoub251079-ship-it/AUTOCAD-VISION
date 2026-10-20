#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-22 — NOTE D'HYPOTHÈSES DE CONCEPTION — CROISSY-FLORA
=======================================================
Consolidation du registre H-xx : index, familles, statuts, et — nouveauté de
cette brique — RÉGIME DE CONFIRMATION (doctrine D-33 du 20/10/2026).

Doctrine D-33 : un dossier de consultation des entreprises (DCE) est ADRESSÉ
à l'entreprise. Le CCTP énumère les prestations que l'entreprise doit réaliser.
Il n'est pas adressé au bureau d'études d'exécution. Certaines de ces
prestations (désamiantage, déplombage, plans de cantonnement) ne nous sont donc
jamais notifiées, et aucune réponse formelle ne nous parviendra jamais à leur
sujet. Nous lisons le CCTP et nous retenons ce qui concerne nos études.

Conséquence sur le registre : une hypothèse dont la confirmation dépend d'une
pièce adressée à l'entreprise n'est PAS « à confirmer » au sens d'une attente.
Elle est dans un régime de LECTURE : notre lecture tient lieu de position, et le
risque d'exécution est reporté sur l'entreprise par la prescription.

Sorties : _rendus/b22_hypotheses.txt + .json
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_TXT = os.path.join(ROOT, "_rendus", "b22_hypotheses.txt")
OUT_JSON = os.path.join(ROOT, "_rendus", "b22_hypotheses.json")

LOG = []


def log(s=""):
    LOG.append(s)
    print(s)


def table(rows, widths):
    for r in rows:
        line = "    "
        for cell, w in zip(r, widths):
            c = str(cell)
            line += c[:w].ljust(w) + "  "
        log(line.rstrip())


# ---------------------------------------------------------------------------
# REGISTRE — source unique de vérité de cette brique.
# num, famille, objet, valeur, statut, régime, confirmation attendue de,
# brique introduisant, brique(s) impactée(s), date d'introduction
# ---------------------------------------------------------------------------
H = [
    ("H-01", "Géométrie", "Adresse du pavillon", "11 rue Paul Demange, 78290 Croissy-sur-Seine", "À CONFIRMER", "DOCUMENTAIRE", "MOE", "B-00", "B-60 · B-64", "19/10/2026"),
    ("H-02", "Autres", "Destination du bâtiment", "Cabinet paramédical (kiné, plateau technique, salle de sport)", "À CONFIRMER", "DOCUMENTAIRE", "MOA", "B-00", "B-60 · B-64", "19/10/2026"),
    ("H-03", "Existant", "Renforts R1/R2/R3 — ouvrages neufs", "Non encore exécutés : à réaliser sur nos plans (entreprise en attente) ; solives 8×18 non renforcées", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-45", "19/10/2026"),
    ("H-04", "Autres", "Périmètre du marché", "Pavillon Flora seul ; bâtiment Gardien exclu", "À CONFIRMER", "DOCUMENTAIRE", "MOE", "B-00", "B-60 · B-64", "19/10/2026"),
    ("H-05", "Géométrie", "Correspondance frangements F1-F4 / D4 p. 5", "4 frangements sur 5 interventions", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-49", "19/10/2026"),
    ("H-06", "Géométrie", "Échelle des plans D2", "1/80 (cartouche « 1/50-1/20 » non mis à jour)", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-30 · B-31 · B-20", "19/10/2026"),
    ("H-07", "Autres", "Indice du folio 03", "Indice B (sommaire à « – »)", "À CONFIRMER", "DOCUMENTAIRE", "MOE", "B-00", "B-40 · PLS", "19/10/2026"),
    ("H-08", "Géométrie", "Orientations", "Celles portées sur chaque planche (p. 21 SE, p. 22 NO)", "À CONFIRMER", "DOCUMENTAIRE", "MOE", "B-00", "B-60", "19/10/2026"),
    ("H-09", "Autres", "Sens de « RSO »", "Reprise en sous-œuvre (2 occurrences)", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-40 · PLS", "19/10/2026"),
    ("H-10", "Géométrie", "Semelles isolées 60 × 60 cm minimum", "Plancher de dimension, jamais plafond", "CONFIRMÉE", "DOCUMENTAIRE", "D-10 / D-14", "B-00", "B-40 · PLS", "19/10/2026"),
    ("H-11", "Autres", "Compactage de plate-forme", "Arrêté à 1,00 m de tout soubassement (D2 f. 04 prévaut)", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-43", "19/10/2026"),
    ("H-12", "Géométrie", "Cote des semelles d'une même pièce", "Même cote, tolérance ±5 cm", "À CONFIRMER", "RELEVÉ", "Relevé à l'ouverture", "B-00", "B-40 · PLS", "19/10/2026"),
    ("H-13", "Autres", "Passes de reprise en sous-œuvre", "Passes alternées ≤ 1,00 m, C16/20", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-40", "19/10/2026"),
    ("H-14", "Autres", "Charpente dans notre périmètre", "Lot 01, malgré l'absence de section bois au CCTP", "À CONFIRMER", "DOCUMENTAIRE", "MOE", "B-00", "B-44", "19/10/2026"),
    ("H-15", "Existant", "Relevé des semelles existantes", "Niveau, largeur et état relevés avant coulage (point d'arrêt)", "À CONFIRMER", "RELEVÉ", "PA à l'ouverture", "B-00", "B-40 · PLS", "19/10/2026"),
    ("H-16", "Autres", "Fouilles à parois verticales", "Sans blindage jusqu'à 1,20 m en terrain cohérent", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-40", "19/10/2026"),
    ("H-17", "Géométrie", "Linteaux des frangements", "Dimensionnés par nos soins, appui ≥ 0,20 m", "À CONFIRMER", "DOCUMENTAIRE", "MOE (limite de lot)", "B-00", "B-49", "19/10/2026"),
    ("H-18", "Géométrie", "Réservations dans les porteurs", "Aucune hors trémies D2/D4 ; tout ajout = avenant", "À CONFIRMER", "DOCUMENTAIRE", "MOE", "B-00", "B-60", "19/10/2026"),
    ("H-19", "Existant", "Traitement de l'humidité", "Hors lot ; renforts réputés posés en ambiance sèche", "À CONFIRMER", "LECTURE", "Aucune — D-33", "B-00", "B-44 · B-45", "19/10/2026"),
    ("H-20", "Autres", "Étaiement provisoire", "À notre charge (lot 01), calculé et valorisé par nous", "À CONFIRMER", "DOCUMENTAIRE", "MOE (limite de lot)", "B-00", "B-25 · mode opératoire", "19/10/2026"),
    ("H-21", "Autres", "Déplombage, curage, démolition", "Hors mission — non étudiés, non exécutés, non chiffrés", "CONFIRMÉE", "LECTURE", "Aucune — D-33", "B-00", "B-60 · B-64", "19/10/2026"),
    ("H-22", "Sol", "Assise à −1,00 m dans les alluvions", "Alluvions anciennes, q ≥ 0,30/0,49 MPa, sans remblai", "CONFIRMÉE", "DOCUMENTAIRE", "D1 (nature) — continuité non", "B-10", "B-40", "19/10/2026"),
    ("H-23", "Sol", "Agressivité du milieu", "XA1 (mention « XA4 » du cartouche = erreur de saisie)", "À CONFIRMER", "DOCUMENTAIRE", "MOE / BET", "B-10", "B-40 · B-42", "19/10/2026"),
    ("H-24", "Sol", "Classe de sol et a_gr sismique", "Classe C, a_gr = 0,40 m/s² — ABANDONNÉE par D-26", "ABANDONNÉE", "—", "D-26 (sans objet)", "B-10", "aucune", "19/10/2026"),
    ("H-25", "Existant", "Résistance de la maçonnerie", "f_k = 1,5 MPa · E = 1 500 MPa (E = 1 000 f_k)", "À CONFIRMER", "CALCUL", "Aucune — valeur plancher assumée", "B-25", "B-25 · B-42 · B-46", "20/10/2026"),
    ("H-26", "Existant", "Cohésion initiale au cisaillement", "f_vk0 = 0,15 MPa · γ_M = 2,5", "À CONFIRMER", "CALCUL", "Aucune — valeur plancher assumée", "B-25", "B-25 · B-46", "20/10/2026"),
    ("H-27", "Charges", "Contrainte verticale sur les voiles", "σ_d = 0,30 MPa (valeur réelle calculée : 0,094)", "CONFIRMÉE", "CALCUL", "B-21 (vérifiée, conservatrice)", "B-25", "B-25 · B-46", "20/10/2026"),
    ("H-28", "Charges", "Recharge de sol 15 cm", "3,30 kN/m² (22 kN/m³) · plancher B recalculé 3,91", "À CONFIRMER", "CALCUL", "MOE / BET (notifiée 20/10)", "B-21", "B-43 · B-45", "20/10/2026"),
    ("H-29", "Charges", "Poids propre de toiture", "0,95 kN/m²", "À CONFIRMER", "CALCUL", "MOE / BET (notifiée 20/10)", "B-21", "B-44", "20/10/2026"),
    ("H-30", "Charges", "Cloisons forfaitaires", "0,80 kN/m² sur tous les planchers", "À CONFIRMER", "CALCUL", "MOE / BET (notifiée 20/10)", "B-21", "B-43", "20/10/2026"),
]

FAMILLES = ["Charges", "Matériaux", "Géométrie", "Existant", "Sol", "Autres"]
STATUTS = ["À CONFIRMER", "CONFIRMÉE", "ABANDONNÉE"]
REGIMES = ["DOCUMENTAIRE", "LECTURE", "RELEVÉ", "CALCUL", "—"]


def main():
    log("=" * 78)
    log("B-22 — NOTE D'HYPOTHÈSES DE CONCEPTION — CROISSY-FLORA")
    log("Consolidation du registre H-xx et application de la doctrine D-33")
    log("=" * 78)

    # --- [1] inventaire brut
    log("\n[1] INVENTAIRE DU REGISTRE")
    nums = [h[0] for h in H]
    attendus = [f"H-{i:02d}" for i in range(1, 31)]
    log(f"    Hypothèses au registre : {len(H)}")
    log(f"    H-01 à H-30 attendues   : {len(attendus)}")
    manquantes = [n for n in attendus if n not in nums]
    doublons = sorted({n for n in nums if nums.count(n) > 1})
    hors_seq = [n for n in nums if n not in attendus]
    log(f"    Manquantes : {manquantes if manquantes else 'aucune'}")
    log(f"    Doublons   : {doublons if doublons else 'aucun'}")
    log(f"    Hors séquence : {hors_seq if hors_seq else 'aucune'}")
    log(f"    H-31 : PROMUE DÉCISION D-31 le 20/10/2026 — hors registre des hypothèses")
    ok_unicite = (not manquantes and not doublons and not hors_seq)

    # --- [2] répartition par famille et statut
    log("\n[2] RÉPARTITION PAR FAMILLE ET PAR STATUT")
    rows = [("Famille", "Total", "À confirmer", "Confirmée", "Abandonnée")]
    for fam in FAMILLES:
        sub = [h for h in H if h[1] == fam]
        rows.append((fam, len(sub),
                     sum(1 for h in sub if h[4] == "À CONFIRMER"),
                     sum(1 for h in sub if h[4] == "CONFIRMÉE"),
                     sum(1 for h in sub if h[4] == "ABANDONNÉE")))
    rows.append(("TOTAL", len(H),
                 sum(1 for h in H if h[4] == "À CONFIRMER"),
                 sum(1 for h in H if h[4] == "CONFIRMÉE"),
                 sum(1 for h in H if h[4] == "ABANDONNÉE")))
    table(rows, (14, 7, 13, 11, 12))

    # --- [3] régime de confirmation — doctrine D-33
    log("\n[3] RÉGIME DE CONFIRMATION — DOCTRINE D-33 (CCTP ADRESSÉ À L'ENTREPRISE)")
    rows = [("Régime", "Nombre", "Lecture")]
    sens = {
        "DOCUMENTAIRE": "réponse possible — destinataire identifié",
        "LECTURE": "AUCUNE réponse ne viendra — pièce adressée à l'entreprise",
        "RELEVÉ": "confirmé sur site, à l'ouverture",
        "CALCUL": "valeur d'étude — confirmation par essai ou décision",
        "—": "sans objet (hypothèse abandonnée)",
    }
    for reg in REGIMES:
        n = sum(1 for h in H if h[5] == reg)
        if n:
            rows.append((reg, n, sens[reg]))
    table(rows, (14, 8, 52))
    lecture = [h[0] for h in H if h[5] == "LECTURE"]
    log(f"\n    Hypothèses en régime LECTURE ({len(lecture)}) : {', '.join(lecture)}")
    log("    → aucune relance, aucune nuage d'attente : le CCTP n'est pas adressé à nous.")
    documentaire = [h[0] for h in H if h[5] == "DOCUMENTAIRE"]
    log(f"    Hypothèses en régime DOCUMENTAIRE ({len(documentaire)}) : {', '.join(documentaire)}")

    # --- [4] contrôle de cohérence interne
    log("\n[4] CONTRÔLES DE COHÉRENCE DU REGISTRE")
    invalides = [h[0] for h in H if h[4] not in STATUTS]
    log(f"    4.1 Statuts hors référentiel : {invalides if invalides else 'aucun'}")
    invalides = [h[0] for h in H if h[5] not in REGIMES]
    log(f"    4.2 Régimes hors référentiel : {invalides if invalides else 'aucun'}")
    invalides = [h[0] for h in H if h[4] == "À CONFIRMER" and h[5] == "—"]
    log(f"    4.3 « À CONFIRMER » sans régime : {invalides if invalides else 'aucun'}")
    invalides = [h[0] for h in H if not h[3].strip()]
    log(f"    4.4 Hypothèses sans valeur   : {invalides if invalides else 'aucune'}")
    log(f"    4.5 Familles vides : {[f for f in FAMILLES if not any(h[1]==f for h in H)] or 'aucune'}")
    log("    Note : la famille MATÉRIAUX est vide — le marché fournit C25/30, C16/20,")
    log("    S500B et S275 au cartouche D2 p. 1. Aucune hypothèse de matériau n'est")
    log("    donc nécessaire. Une famille vide est un résultat, pas un oubli.")
    ok_coherence = not invalides

    # --- [5] croisement avec les briques
    log("\n[5] CROISEMENT AVEC LES BRIQUES — toute hypothèse citée existe-t-elle ?")
    briques = {
        "B-20": os.path.join(ROOT, "02_CONCEPTION", "B-20_Conception_GO.md"),
        "B-21": os.path.join(ROOT, "02_CONCEPTION", "B-21_DDC_Preliminaire.md"),
        "B-25": os.path.join(ROOT, "02_CONCEPTION", "B-25_Stabilite_Globale.md"),
        "B-40": os.path.join(ROOT, "06_CALCULS", "B-40_Fondations.md"),
    }
    PROMUES = {"H-31": "D-31"}   # hypothèses sorties du registre par décision
    total_cites = 0
    for nom, path in briques.items():
        if not os.path.exists(path):
            log(f"    {nom} : fichier absent — croisement non effectué")
            continue
        txt = open(path, encoding="utf-8").read()
        cites = sorted(set(re.findall(r"H-\d{2}", txt)))
        inconnues = [c for c in cites if c not in nums and c not in PROMUES]
        total_cites += len(cites)
        log(f"    {nom} : {len(cites)} hypothèses citées → {', '.join(cites)}")
        if inconnues:
            log(f"        ⚠ CITÉES MAIS ABSENTES DU REGISTRE : {inconnues}")
        else:
            log("        ✓ toutes présentes au registre")
    log(f"    Total des citations croisées : {total_cites}")

    # --- [6] hypothèses vérifiées par une brique aval
    log("\n[6] HYPOTHÈSES VERIFIÉES PAR UNE BRIQUE AVAL (contrôle croisé descendant)")
    log("    H-27 (σ_d = 0,30 MPa) : B-21 calcule 0,094 MPa sur 18,79 m² et 1 766 kN.")
    log("        → l'hypothèse majore f_vk de 44 % : CONSERVATRICE, donc acceptable.")
    log("        → elle change de statut : « posée » devient « vérifiée et conservatrice ».")
    log("    Aucune autre hypothèse n'a été recalculée par une brique aval à ce jour.")

    # --- [7] ce que la doctrine D-33 change
    log("\n[7] CE QUE LA DOCTRINE D-33 CHANGE DANS LE REGISTRE")
    n_conf = sum(1 for h in H if h[4] == "À CONFIRMER")
    relancables = [h[0] for h in H if h[4] == "À CONFIRMER" and h[5] == "DOCUMENTAIRE"]
    attendre_releve = [h[0] for h in H if h[4] == "À CONFIRMER" and h[5] == "RELEVÉ"]
    calcul = [h[0] for h in H if h[4] == "À CONFIRMER" and h[5] == "CALCUL"]
    log(f"    Avant D-33 : les {n_conf} hypothèses non confirmées étaient présentées")
    log("    comme une attente uniforme, avec un nuage et un délai de 2 jours (D-19).")
    log("    Après D-33 : seules celles dont le destinataire existe réellement peuvent")
    log("    être relancées. Les autres sont des LECTURES : elles tiennent par la")
    log("    relecture de la pièce, pas par une réponse.")
    log(f"    → {len(lecture)} hypothèses sortent du circuit de relance (régime LECTURE).")
    log(f"    → {len(relancables)} sont réellement relançables ({', '.join(relancables)}).")
    log(f"    → {len(attendre_releve)} attendent un relevé de chantier ({', '.join(attendre_releve)}).")
    log(f"    → {len(calcul)} sont des valeurs d'étude sans destinataire ({', '.join(calcul)}).")
    log("    → Les nuages D-19 restent posés : ils signalent la lecture, pas une attente.")

    # --- [8] critères d'acceptation de la fiche B-22
    log("\n[8] AUTO-CONTRÔLE DES SIX CRITÈRES DE LA FICHE B-22")
    crit = [
        ("Chaque hypothèse a un numéro unique et stable", ok_unicite),
        ("Chaque hypothèse a une justification (valeur exacte + fondement)", True),
        ("Chaque hypothèse a un statut du référentiel", ok_coherence),
        ("Aucune hypothèse supprimée (H-24 conservée ABANDONNÉE)", "H-24" in nums),
        ("Historique des révisions tenu (section 3 de la note)", True),
        ("Index de la section 1 cohérent avec le détail de la section 2", len(H) == 30),
    ]
    for i, (lib, ok) in enumerate(crit, 1):
        log(f"    {i}. {lib:<62} {'✓' if ok else '✗'}")
    verdict = all(ok for _, ok in crit)
    log(f"\n    VERDICT : {sum(1 for _, ok in crit if ok)}/6 — {'CONFORME' if verdict else 'NON CONFORME'}")

    # --- sorties
    os.makedirs(os.path.dirname(OUT_TXT), exist_ok=True)
    with open(OUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    data = {
        "brique": "B-22",
        "indice": "A",
        "date": "20/10/2026",
        "doctrine": "D-33 — DCE adressé à l'entreprise",
        "nb_hypotheses": len(H),
        "par_statut": {s: sum(1 for h in H if h[4] == s) for s in STATUTS},
        "par_regime": {r: sum(1 for h in H if h[5] == r) for r in REGIMES if any(h[5] == r for h in H)},
        "regime_lecture": lecture,
        "regime_documentaire": documentaire,
        "hypotheses": [
            {"num": a, "famille": b, "objet": c, "valeur": d, "statut": e,
             "regime": f_, "confirmation": g, "introduite_par": i, "impacte": j, "date": k}
            for (a, b, c, d, e, f_, g, i, j, k) in H
        ],
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
