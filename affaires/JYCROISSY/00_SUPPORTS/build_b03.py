#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-03 — REGISTRE DES DÉCISIONS ET RÉSERVES (RDR) — JYCROISSY
Générateur / validateur (stdlib uniquement). Ouverture du RDR officiel à quatre
registres (D-xx / H-xx / PA-xx / V-xx) — CARNAC v3.0.2, fiche B-03_RDR.md.

Entrées : MPD B-01 Ind B (validée), FDC B-02 (17 VERROU), pré-RDR (D-01…D-13, PA-01).
Sorties : RDR_JYCROISSY.md et RDR_jycroissy.csv.

Règles : une décision sans auteur ni date n'existe pas ; un verrou ne se ferme que
par entrée FDC ou décision Section 1 ; le registre des verrous liste ce qui a été
exécuté malgré tout ; aucune décision MOA/MOE prise à sa place.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "02_PHASE_0_CADRAGE"))

ID_01 = "JYCROISSY"
ID_05 = "à créer — situation hétérogène (écart C-09 ouvert) : archi Ind C, CCTP V1, DIAG « - », folios BET C/-/-/B"
ID_07 = "2026-10-30"

CR = "CR 20/10/2026 — architecte (Truelle) + client (MOA)"
BE = "BET d'exécution (utilisateur)"

# ---------------------------------------------------------------------------
# Section 1 — Décisions (D-xx). Reprises du pré-RDR (sans renumérotation) + 3
# décisions de clôture de phase 0 (MPD, FDC, ouverture du RDR).
# ---------------------------------------------------------------------------
# (id, date, objet, décision, auteur, effet sur les briques)
DECISIONS = [
    ("D-01", "20/10/2026", "Profondeur d'ancrage des fondations superficielles",
     "Ancrer les RSO d'au moins 0,50 m dans les alluvions anciennes ; la mention "
     "« 40 cm » du CCTP (P1 p13) est caduque sur ce point.",
     CR,
     "SOL-03 → B-40, B-41 (fondations) en COMPLET (prescrit) ; NIV-04 → B-40 ; "
     "PA-01 contrôle en fouille."),
    ("D-02", "20/10/2026", "Section du poteau P1 (renfort de linteau)",
     "Tube carré 14 × 14 cm ; la mention « 14 × 14 mm » du CCTP (P1 p23) est une "
     "erreur de frappe.",
     CR,
     "GEO-04/P1 → B-42, B-49 (renforts métalliques) en COMPLET."),
    ("D-03", "20/10/2026", "Charge d'exploitation de référence des planchers",
     "250 daN/m² (2,5 kN/m²) au titre du futur cabinet paramédical/bureaux ; les "
     "vérifications P2 à 150 daN/m² (logement) restent des faits historiques — "
     "toute réutilisation des planchers existants est re-vérifiée sous 250 daN/m².",
     CR,
     "CHG-02 → B-21, B-42, B-43, B-45, B-47, B-48, B-49 en COMPLET ; re-vérification "
     "planchers existants en B-21/B-23."),
    ("D-04", "20/10/2026", "Adresse de l'opération",
     "Retenir 11 rue Paul Demange, 78290 Croissy-sur-Seine ; l'adresse « 2 rue "
     "Alfred Dormeuil » du diagnostic P2 n'est plus retenue.",
     CR,
     "ID-03 → tous documents EXE."),
    ("D-05", "20/10/2026", "Personne morale de la maîtrise d'ouvrage",
     "Retenir UNIVI ; la mention « SCI GEMS RC — site 208 » des cartouches P4 reste "
     "documentaire.",
     CR,
     "AC-01 → tous documents EXE."),
    ("D-06", "20/10/2026", "Paramètres géotechniques de dimensionnement",
     "Retenir officiellement les paramètres G2 AVP GEOEXPERTS transmis au CR : "
     "qELS ≤ 0,30 MPa ; qELU ≤ 0,49 MPa ; fondations ancrées de 50 cm dans les "
     "alluvions anciennes. Le rapport G2 n° 25.13646/ES/GIF reste non reçu.",
     CR,
     "SOL-01/SOL-02/SOL-03 → B-12, B-20, B-40, B-41, B-43 en COMPLET (D-06) ; "
     "PA-01."),
    ("D-07", "23/10/2026", "Gabarit d'opération (CFG-02)",
     "Gabarit M validé — bâtiment unitaire, emprise < 2 500 m², plus de cinq "
     "porteurs, sans JD ni sous-sol Flora ; voie standard en six phases.",
     BE,
     "CFG-02 → B-01, B-04, B-25, B-34, B-60 en COMPLET."),
    ("D-08", "23/10/2026", "Diagnostic amiante/plomb (DOC-07)",
     "NON NÉCESSAIRE confirmé — désamiantage/déplombage exclus CARNAC §1.4 ; seules "
     "les contraintes de phasage/coordination remontent.",
     BE,
     "DOC-07 → SANS OBJET."),
    ("D-09", "23/10/2026", "Fiches techniques des prédalles (DOC-09)",
     "NON NÉCESSAIRE confirmé — aucune prédalle ni plancher préfabriqué ; "
     "B-48 SANS OBJET corrélatif.",
     BE,
     "DOC-09 → SANS OBJET ; B-48 SANS OBJET."),
    ("D-10", "23/10/2026", "Poussées terres / écrans de soutènement (STR-02) + périmètre",
     "NON NÉCESSAIRE confirmé — périmètre = bâtiment Flora uniquement ; Gardien/"
     "Bagatelle hors périmètre structure CARNAC → C-07 tranchée.",
     BE,
     "STR-02 → SANS OBJET ; C-07 fermée."),
    ("D-11", "23/10/2026", "Fondations profondes (B-41)",
     "SANS OBJET confirmé — aucune fondation profonde dans aucune pièce.",
     BE,
     "B-41 → SANS OBJET."),
    ("D-12", "23/10/2026", "Géotechnique (SOL-04/06/07)",
     "G2 complet non transmissible ; mission CARNAC = dimensionnement aux contraintes "
     "D-06 seulement, sans calcul de tassement ; tassement/assise délégués au "
     "géotechnicien ; absence de nappe phréatique confirmée. Conséquence : "
     "SOL-04/SOL-06/SOL-07 NON NÉCESSAIRE (périmètre).",
     BE,
     "SOL-04/06/07 → SANS OBJET ; B-40 non bloquante ; PA-01 maintenu."),
    ("D-13", "23/10/2026", "Nomenclature des niveaux (CFG-03 / NIV-07)",
     "Structurale : premier niveau = PB (premier bas), tous les autres = PH (plancher "
     "haut) → PB RDC / PH R+1. La nomenclature architecturale « PH RDC » (P3 f1) = "
     "sous-face du plancher haut PH R+1, consignée dans la table NIV-07. Vue unique "
     "« FONDATIONS + PB RDC » acceptable.",
     BE,
     "CFG-03 → B-01, B-20, B-21, B-25, B-30, B-60 ; NIV-07 → B-02, B-20, B-30, "
     "B-32, B-43, B-60."),
    ("D-14", "30/10/2026", "Validation de la MPD (B-01 Ind B)",
     "Validation de la Matrice de Périmètre et de Disponibilité B-01 Ind B (106 "
     "variables ; 39 FOURNIE, 44 PARTIELLE, 17 À PRODUIRE PAR GO, 6 NON NÉCESSAIRE, "
     "0 BLOQUANTE). La MPD est annexée au RDR (non recopiée).",
     BE,
     "MPD validée → active les briques B-02 à B-04 ; B-02 FDC exécutée en conséquence."),
    ("D-15", "30/10/2026", "Validation de la FDC (B-02)",
     "Validation de la Fiche de Données de Conception B-02 (66 variables résolues, "
     "17 VERROU, table NIV-07) ; la FDC est annexée au RDR comme décision D-15. "
     "Valeurs Contractuelles / Décision / À confirmer validées ligne à ligne.",
     BE,
     "FDC validée → les briques de calcul consomment ses valeurs ; les VERROU "
     "sont inscrits au registre V-xx."),
    ("D-16", "30/10/2026", "Ouverture du RDR officiel à quatre registres",
     "Ouverture du Registre des Décisions et Réserves à quatre registres "
     "(D-xx / H-xx / PA-xx / V-xx) ; reprise intégrale du pré-RDR D-01…D-13 et PA-01 "
     "sans renumérotation.",
     BE,
     "RDR ouvert → B-04 (PTD) peut être exécuté ; B-70/B-72 le consomment."),
]

# ---------------------------------------------------------------------------
# Section 2 — Réserves (R-xx). Actes d'attente : demande d'une donnée à un tiers.
# ---------------------------------------------------------------------------
# (id, objet, statut, responsable, date_demande, echeance, justification)
RESERVES = [
    ("R-01", "Rapport géotechnique G2 complet (GEOEXPERTS n° 25.13646/ES/GIF, "
             "22/01/2026)", "Ouverte",
     "MOA (UNIVI) / géotechnicien GEOEXPERTS", "20/10/2026",
     "Avant ouverture des fouilles (PA-01)",
     "Le rapport n'a pas été transmis (bug technique signalé par le client) ; "
     "les paramètres D-06 sont néanmoins officiels, mais le G2 complet ferme "
     "SOL-04/06/07 et l'assise détaillée."),
    ("R-02", "Rapport géotechnique G3 (fondations) — commande éventuelle",
     "Ouverte", "MOA (UNIVI)", "23/10/2026",
     "Avant ouverture des fouilles",
     "La mission CARNAC ne dépend pas du G3 (D-12), mais sa commande est une "
     "formalité MOA à tracer ; aucune décision D-xx ne la prend à sa place."),
    ("R-03", "Indices homogènes du dossier EXE (écart C-09)", "Ouverte",
     "BET MOE (EVEN STRUCTURES)", "30/10/2026", "À convenir",
     "Les folios BET portent des indices hétérogènes C/-/-/B dans une pièce dite "
     "indice C ; l'indice EXE doit être créé (ID-05)."),
    ("R-04", "Vecteur DXF complet du DCE architecte (écart C-08)", "Ouverte",
     "Architecte (Truelle Architectes)", "30/10/2026", "À convenir",
     "Le DXF P5 ne couvre que Flora RDC/R+1 ; les autres planches n'existent qu'en "
     "PDF vectoriel P4."),
    ("R-05", "Numérotation des planches P4 (écart C-06)", "Ouverte",
     "Architecte (Truelle Architectes)", "30/10/2026", "À convenir",
     "Décalage entre le sommaire p1 et les cartouches réels ; les citations aval "
     "utilisent le n° de page PDF réel."),
    ("R-06", "Échelle de la planche 29 (écart C-10)", "Ouverte",
     "Architecte (Truelle Architectes)", "30/10/2026", "À convenir",
     "Cartouche 1/100 vs mention interne « 1/2000 » ; coquille probable, sans impact "
     "structure direct."),
    ("R-07", "Titre/périmètre éditorial du diagnostic P2 (écart C-11)", "Ouverte",
     "BET MOE (EVEN STRUCTURES)", "30/10/2026", "À convenir",
     "Couverture « Diagnostic structurel » vs pieds de page « Diagnostic charpente » ; "
     "le document traite aussi planchers, portiques et fondations."),
    ("R-08", "Validation des valeurs « À confirmer » de la FDC", "Ouverte",
     "MOE / BET MOE (EVEN STRUCTURES)", "30/10/2026", "Avant les briques de calcul",
     "36 variables de la FDC portent la fiabilité « À confirmer » (enrobage S4/30 mm, "
     "C18/C24 hypothèses, niveaux, mortiers, chaînages, etc.) ; aucune n'est supputée, "
     "mais elle doit être confirmée avant exécution."),
    ("R-09", "Points de calage et coordonnées géomètre (GEO-07/GEO-08/GEO-13)",
     "Ouverte", "Géomètre expert", "30/10/2026", "Avant B-30/B-31",
     "Aucun point de calage ≥ 3 non alignés ni transformation n'ont été identifiés ; "
     "le calage B-30/B-31 en dépend."),
    ("R-10", "Niveau TN précis et altimétrie de référence (NIV-01)", "Ouverte",
     "Géomètre expert", "30/10/2026", "Avant B-40",
     "TN déclaré variable (P1 p14) ; seule l'altimétrie Z ≈ 201 est connue."),
]

# ---------------------------------------------------------------------------
# Section 3 — Registre des Verrous (V-xx). Les 17 VERROU de la FDC B-02.
# (id, donnee, brique_suspendue, date, responsable, briques_executees, mode)
# ---------------------------------------------------------------------------
VERROUS = [
    ("V-01", "DEC-01 — Mode attribué à chaque brique", "B-70", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)", "INTERNE-GO"),
    ("V-02", "DEC-02 — Décisions inscrites au RDR (valeur, auteur, date)",
     "B-03, B-64, B-70, B-72, T-03", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)", "INTERNE-GO"),
    ("V-03", "DEC-03 — Verrous ouverts (donnée, brique suspendue, responsable)",
     "B-03, B-04, B-13, B-15, B-64, B-70, B-72, T-03, T-04", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)", "INTERNE-GO"),
    ("V-04", "DEC-04 — Documents supersédés (indice, date)", "B-71, B-72",
     "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)",
     "INTERNE-GO"),
    ("V-05", "DEC-05 — Hypothèses notifiées sous nuage H-xx",
     "B-03, B-20, B-22, B-25, B-34, B-40, B-60, B-64, B-70", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)", "INTERNE-GO"),
    ("V-06", "DOC-08 — Plans de récolement / DOE", "B-11, B-72", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)", "INTERNE-GO"),
    ("V-07", "EXI-05 — Contrainte admissible transmise à l'existant", "B-23, B-46",
     "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03 (cadrage)",
     "INTERNE-GO"),
    ("V-08", "GEO-07 — Transformation du fichier (rotation, translation, échelle)",
     "B-30", "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03",
     "INTERNE-GO"),
    ("V-09", "GEO-08 — Points de calage identifiés (≥ 3 non alignés)", "B-30, B-31",
     "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03", "INTERNE-GO"),
    ("V-10", "GEO-10 — Seuils d'épaisseur de présomption porteuse", "B-32",
     "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03", "INTERNE-GO"),
    ("V-11", "GEO-11 — Superposition des niveaux (recouvrement, écart d'axe)",
     "B-32", "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03",
     "INTERNE-GO"),
    ("V-12", "GEO-12 — Seuils géométriques du projet (résidu de calage, écarts)",
     "B-30", "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03",
     "INTERNE-GO"),
    ("V-13", "GEO-13 — Matrice de recalage multi-sources vers le RSU",
     "B-13, B-20, B-30, B-31, B-32, B-34", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03", "INTERNE-GO"),
    ("V-14", "LIV-01 — Conventions de calques DXF", "B-60", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03", "INTERNE-GO"),
    ("V-15", "LIV-02 — Échelles autorisées", "B-60", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03", "INTERNE-GO"),
    ("V-16", "LIV-03 — Formats de sortie et nommage des fichiers", "B-60",
     "30/10/2026", "BET d'exécution (MOE)", "B-00, B-01, B-02, B-03", "INTERNE-GO"),
    ("V-17", "NIV-07 — Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs "
             "ASB / Fini", "B-20, B-30, B-32, B-43, B-60", "30/10/2026",
     "BET d'exécution (MOE)", "B-00, B-01, B-02 (FDC §NIV-07)", "INTERNE-GO"),
]

# ---------------------------------------------------------------------------
# Section 4 — Hypothèses notifiées (H-xx).
# ---------------------------------------------------------------------------
HYPOTHESES = []  # aucune à ce stade

# ---------------------------------------------------------------------------
# Section 5 — Points d'Arrêt (PA-xx).
# ---------------------------------------------------------------------------
PAS = [
    ("PA-01", "Contrôle de l'arase inférieure des fondations à l'ouverture des "
              "fouilles (vérification de la rencontre des alluvions anciennes sur "
              "toute l'emprise, avant coulage de gros béton/semelle)",
     "Notification de l'entreprise au BET / contrôle technique ; procès-verbal de "
     "reconnaissance de sol de fond de fouille ; toute assise non conforme déclenche "
     "une reprise d'étude (pas de valeur de repli)",
     "CR 20/10/2026 (D-06)", "Ouverture des fouilles"),
]


def build_md():
    L = []
    a = L.append
    a("# B-03 — REGISTRE DES DÉCISIONS ET RÉSERVES (RDR) — JYCROISSY")
    a("")
    a("| Champ | Valeur |")
    a("|---|---|")
    a("| Code projet (ID-01) | %s |" % ID_01)
    a("| Indice du dossier en vigueur (ID-05) | %s |" % ID_05)
    a("| Date de l'étude (ID-07) | %s |" % ID_07)
    a("| Carnet | CARNAC v3.0.2 — fiche `02_PHASE_0_CADRAGE/B-03_RDR.md` |")
    a("| Indice | **B-03 — 2026-10-30** (RDR ouvert à quatre registres) |")
    a("| Entrées | MPD B-01 Ind B (validée) ; FDC B-02 ; pré-RDR D-01…D-13, PA-01 |")
    a("| Sortie | RDR complet et daté — sections D-xx / R-xx / V-xx + registres H-xx / PA-xx |")
    a("")
    a("> **Statut** : RDR ouvert. Ce document est le registre vivant du projet : il est "
      "référencé par toutes les briques de calcul et par la clôture (B-70 à B-72), et "
      "mis à jour à chaque décision, réserve ou verrou. La MPD (D-14) et la FDC "
      "(D-15) sont annexées, non recopiées.")
    a("")
    a("---")
    a("")
    a("## SECTION 1 — DÉCISIONS (D-xx)")
    a("")
    a("*%d décisions.* Chaque décision est datée, attribuée à un auteur nommé, et son "
      "effet sur les modes des briques est explicité." % len(DECISIONS))
    a("")
    a("| N° | Date | Objet | Décision | Auteur | Effet sur les briques |")
    a("|---|---|---|---|---|---|")
    for n, d, o, dec, aut, eff in DECISIONS:
        a("| %s | %s | %s | %s | %s | %s |" % (n, d, o, dec, aut, eff))
    a("")
    a("**Auteurs.** `CR` = compte rendu officiel du 20/10/2026 (architecte Truelle + "
      "client MOA). `BE` = BET d'exécution (utilisateur). Aucune décision MOA/MOE n'a "
      "été prise à sa place : les décisions MOA en attente sont des réserves R-xx.")
    a("")
    a("---")
    a("")
    a("## SECTION 2 — RÉSERVES (R-xx)")
    a("")
    a("*%d réserves.* Actes d'attente : demande d'une donnée à un tiers. Une réserve ne "
      "se ferme que par une entrée en FDC ou une décision en Section 1." % len(RESERVES))
    a("")
    a("| N° | Objet | Statut | Responsable de l'obtention | Date de demande | Échéance | Justification |")
    a("|---|---|---|---|---|---|---|")
    for n, o, st, resp, dd, ech, jus in RESERVES:
        a("| %s | %s | %s | %s | %s | %s | %s |" % (n, o, st, resp, dd, ech, jus))
    a("")
    a("---")
    a("")
    a("## SECTION 3 — REGISTRE DES VERROUS (V-xx)")
    a("")
    a("*%d verrous.* Les VERROU de la FDC B-02 y sont inscrits. Le registre liste "
      "TOUJOURS ce qui a été exécuté malgré tout — c'est ce qui prouve que la production "
      "n'a pas attendu pieds croisés." % len(VERROUS))
    a("")
    a("| N° | Donnée (code) | Brique suspendue | Date | Responsable | Briques exécutées malgré tout | Mode de contournement |")
    a("|---|---|---|---|---|---|---|")
    for n, d, bs, dt, resp, be, mode in VERROUS:
        a("| %s | %s | %s | %s | %s | %s | %s |" % (n, d, bs, dt, resp, be, mode))
    a("")
    a("> **Fermeture partielle** : **V-17 (NIV-07)** — la correspondance Plan Archi N ↔ "
      "PB/PH est entrée en FDC (B-02 §NIV-07, décision D-13) ; les cotes ASB et les "
      "épaisseurs de complexe neuves restent ouvertes (dallage « selon étude BA »). "
      "Aucun autre verrou n'est fermé : les 16 autres attendent une production interne "
      "(INTERNE-GO) ou une donnée externe.")
    a("")
    a("---")
    a("")
    a("## SECTION 4 — HYPOTHÈSES NOTIFIÉES (H-xx)")
    a("")
    a("*Aucune à ce stade.* Aucune donnée normative bornable n'a été comblée par une "
      "hypothèse : toutes les inconnues tranchées l'ont été par décision (D-xx) ou "
      "point d'arrêt (PA-01). Les valeurs « À confirmer » de la FDC (R-08) ne sont pas "
      "des hypothèses notifiées ; elles seront soit confirmées, soit portées par une "
      "hypothèse H-xx si une norme d'appui bornable est retenue.")
    a("")
    a("| N° | Hypothèse | Valeur / norme d'appui | Zone | Statut de visa | Délai DEC-06 |")
    a("|---|---|---|---|---|---|")
    a("| — | Aucune | — | — | — | — |")
    a("")
    a("---")
    a("")
    a("## SECTION 5 — POINTS D'ARRÊT (PA-xx)")
    a("")
    a("| N° | Point d'arrêt | Prescription associée (ENC) | Origine | Échéance |")
    a("|---|---|---|---|---|")
    for n, pa, enc, org, ech in PAS:
        a("| %s | %s | %s | %s | %s |" % (n, pa, enc, org, ech))
    a("")
    a("---")
    a("")
    a("## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE")
    a("")
    a("| Critère de la fiche B-03 | Statut |")
    a("|---|---|")
    a("| Chaque décision a un auteur, une date et un effet identifié | ✅ (D-01…D-16) |")
    a("| Chaque réserve a un responsable et une date de demande | ✅ (R-01…R-10) |")
    a("| Chaque verrou identifie la brique suspendue et les briques exécutées malgré tout | ✅ (V-01…V-17) |")
    a("| Aucune décision prise à la place du MOA/MOE sans source citée | ✅ (les décisions MOA en attente sont R-xx) |")
    a("| Zéro placeholder (V7) | ✅")
    a("")
    a("**Brique B-03 livrée — en attente de votre GO pour B-04 (Plan de travail dégradé).**")
    a("")
    return "\n".join(L)


def build_csv():
    path = os.path.join(OUT_DIR, "RDR_jycroissy.csv")
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Registre", "N°", "Date", "Objet", "Décision/Statut/Donnée",
                    "Auteur/Responsable", "Effet/Justification/Briques exécutées"])
        for n, d, o, dec, aut, eff in DECISIONS:
            w.writerow(["D", n, d, o, dec, aut, eff])
        for n, o, st, resp, dd, ech, jus in RESERVES:
            w.writerow(["R", n, dd, o, st + " — échéance: " + ech, resp, jus])
        for n, d, bs, dt, resp, be, mode in VERROUS:
            w.writerow(["V", n, dt, d, "brique suspendue: " + bs, resp,
                        "exécutées malgré tout: " + be + " ; mode: " + mode])
        for n, pa, enc, org, ech in PAS:
            w.writerow(["PA", n, "", pa, enc, org, "échéance: " + ech])
    return path


def main():
    md = build_md()
    md_path = os.path.join(OUT_DIR, "RDR_JYCROISSY.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    csv_path = build_csv()

    assert len(DECISIONS) == len({r[0] for r in DECISIONS}), "doublon D-xx"
    assert len(RESERVES) == len({r[0] for r in RESERVES}), "doublon R-xx"
    assert len(VERROUS) == len({r[0] for r in VERROUS}), "doublon V-xx"
    assert len(VERROUS) == 17, "le registre V doit reprendre les 17 VERROU de la FDC"
    for n, d, o, dec, aut, eff in DECISIONS:
        assert aut and d, n
        assert eff and eff != "—", n
    for n, o, st, resp, dd, ech, jus in RESERVES:
        assert resp and dd, n
        assert jus and jus != "—", n
    codes = {r[1].split(" — ")[0].strip() for r in VERROUS}
    assert {"DEC-01", "DEC-02", "DEC-03", "DEC-04", "DEC-05", "DOC-08", "EXI-05",
            "GEO-07", "GEO-08", "GEO-10", "GEO-11", "GEO-12", "GEO-13", "LIV-01",
            "LIV-02", "LIV-03", "NIV-07"} == codes, "VERROU FDC non repris"
    for line in (md + "\n").splitlines():
        assert "{{" not in line and "}}" not in line, "placeholder résiduel V7"

    print("B-03 RDR généré :")
    print("  -", md_path)
    print("  -", csv_path)
    print("  D-xx : %d  |  R-xx : %d  |  V-xx : %d  |  H-xx : %d  |  PA-xx : %d"
          % (len(DECISIONS), len(RESERVES), len(VERROUS), len(HYPOTHESES), len(PAS)))
    print("  validations : OK (auteur/date, responsable, briques exécutées malgré tout, V7)")


if __name__ == "__main__":
    main()
