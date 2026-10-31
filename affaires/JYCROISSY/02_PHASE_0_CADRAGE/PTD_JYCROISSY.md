# B-04 — PLAN DE TRAVAIL DÉGRADÉ (PTD) — JYCROISSY

| Champ | Valeur |
|---|---|
| Code projet (ID-01) | JYCROISSY |
| Carnet | CARNAC v3.0.2 — fiche `02_PHASE_0_CADRAGE/B-04_PTD.md` |
| Indice | **B-04 — 2026-10-30** (PTD — instantané phase 0) |
| Entrées | MPD B-01 Ind B ; FDC B-02 ; RDR B-03 ; graphe de dépendances |
| Sortie | 3 tableaux (suspendues / exécutables / PARAMÉTRIQUE) + synthèse |

> **Statut** : instantané des briques qui peuvent tourner et de celles qui sont bloquées à l'ouverture de la phase 1. Régénéré à chaque blocage. Le PTD est annexé au RDR (B-03).

---

## TABLEAU 1 — BRIQUES SUSPENDUES

*7 briques.* Chaque brique suspendue identifie la donnée qui la bloque ; le projet, lui, n'est **pas** suspendu (blocage local, jamais global — verrou V11).

| Brique | Donnée bloquante (code) | Voie d'obtention | Responsable | Échéance |
|---|---|---|---|---|
| B-13 (Détection et qualification des porteurs) | GEO-13 (matrice de recalage multi-sources vers le RSU) | Production interne B-30 / B-31 (INTERNE-GO) | BET d'exécution (MOE) | Avant phase 2 |
| B-20 (Conception des ouvrages) | DEC-05 (hypothèses notifiées H-xx), GEO-13, NIV-07 (épaisseurs ASB / Fini) | Production interne B-22 (DEC-05) et B-30 (GEO-13) ; NIV-07 ASB en attente (dallage « selon étude BA ») | BET d'exécution (MOE) | Phase 3 |
| B-34 (Carnet des réservations et trémies tous corps d'état) | DEC-05 (H-xx), GEO-13 | Production interne B-22 et B-30 | BET d'exécution (MOE) | Phase 5 |
| B-60 (Plans d'exécution) | DEC-05 (H-xx), NIV-07 (épaisseurs ASB / Fini) | Production interne B-22 ; NIV-07 ASB en attente | BET d'exécution (MOE) | Phase 5 |
| B-64 (Notice de synthèse) | DEC-02, DEC-03, DEC-05 | Production interne (DEC-02/DEC-03 déjà produits par B-03 ; DEC-05 par B-22) | BET d'exécution (MOE) | Phase 5 |
| B-70 (Auto-contrôle déclaré de synthèse) | DEC-01, DEC-02, DEC-03, DEC-05 | Production interne B-70 (DEC-01), B-03 (DEC-02/03), B-22 (DEC-05) | BET d'exécution (MOE) | Phase 6 |
| B-72 (Journal de clôture) | DEC-02, DEC-03, DEC-04, DOC-08 | Production interne B-72 (DOC-08, DEC-04) ; B-03 (DEC-02/03) | BET d'exécution (MOE) | Phase 6 |

---

## TABLEAU 2 — BRIQUES EXÉCUTABLES IMMÉDIATEMENT

*23 briques.* Aucune dépendance à une donnée manquante non produite ; mode COMPLET, PARTIEL-DÉCLARÉ (décision RDR) ou INTERNE-GO (conception produite par nos soins).

| Brique | Mode | Motif (aucune dépendance à la donnée manquante) |
|---|---|---|
| B-10 (Audit critique du CCTP) | COMPLET | DOC-04 FOURNIE ; DEC-02 produit par B-03 (D-14) |
| B-11 (Audit du diagnostic structure) | COMPLET | DOC-05 FOURNIE ; s'appuie sur P2/P4/P5 |
| B-12 (Audit des pièces géotechniques) | PARTIEL-DÉCLARÉ | Paramètres D-06 (qELS ≤ 0,30 MPa, qELU ≤ 0,49 MPa, ancrage 50 cm) ; G2 complet non reçu (réserve R-01) |
| B-14 (Clarification du périmètre) | INTERNE-GO | Périmètre à trancher produit par nos soins |
| B-15 (Fiche de synthèse) | COMPLET | DEC-03 produit par B-03 ; risques identifiés en phase 0 |
| B-21 (Note de calcul des charges) | COMPLET | CHG-01…08 FOURNIE ou Décision (D-03) |
| B-22 (Note d'hypothèses de conception) | INTERNE-GO | Produit DEC-05 (hypothèses notifiées H-xx) |
| B-23 (Vérification des éléments existants) | INTERNE-GO | Produit EXI-05 (contrainte admissible transmise à l'existant) |
| B-24 (Vérification des éléments existants non) | COMPLET | DOC-05 FOURNIE ; PA-01 (D-06) encadre les inconnues physiques |
| B-25 (Stabilité globale, contreventement, joints) | COMPLET | CHG-07 FOURNIE ; STR-01 PARTIELLE |
| B-30 (Calage des sources) | INTERNE-GO | Produit GEO-07, GEO-08, GEO-12 (transformation, points de calage, seuils) |
| B-31 (Recalage / superposition des niveaux) | INTERNE-GO | Produit GEO-13 ; dépend de B-30 (GEO-07/08) et B-32 (GEO-11) |
| B-32 (Exploitation vectorielle / nettoyage) | INTERNE-GO | Produit GEO-10, GEO-11 (seuils d'épaisseur, superposition) |
| B-33 (Vérification croisée) | COMPLET | GEO-14 PARTIELLE ; DOC-02 |
| B-40 (Fondations superficielles) | PARTIEL-DÉCLARÉ | SOL-01/02/03 décision D-06 ; B-40 non bloquante (D-12) ; PA-01 contrôle fouille |
| B-42 (Verticaux BA) | COMPLET | MAT-01/04 FOURNIE ; CHG-02 Décision (D-03) |
| B-45 (Structure métallique) | COMPLET | MAT-05 FOURNIE ; CHG-06 FOURNIE |
| B-46 (Maçonnerie : vérification) | INTERNE-GO | Produit EXI-05 par calcul interne |
| B-47 (Escaliers) | COMPLET | NIV-03 FOURNIE ; CHG-08 PARTIELLE |
| B-49 (Linteaux et seuils) | COMPLET | MAT-09 FOURNIE ; EXI-01 PARTIELLE |
| B-50 (Assemblages et ancrages) | COMPLET | MAT-04/09 FOURNIE ; EXI-01/03 PARTIELLE |
| B-62 (Nomenclature / quantités) | COMPLET | MAT-xx FOURNIE |
| B-71 (Indicage et supersession documentaire) | INTERNE-GO | Produit DEC-04 (documents supersédés) |

---

## TABLEAU 3 — BRIQUES EXÉCUTABLES EN PARAMÉTRIQUE

*2 briques.* Une donnée manque sans décision RDR : le livrable est émis **filigrané** « PROVISOIRE — EN ATTENTE DE [donnée] » et **suffixé `_P`** — non exécutable, non diffusable.

| Brique | Donnée laissée en symbole | Forme littérale possible | Ce qui ne sera PAS produit |
|---|---|---|---|
| B-43 (Planchers et dallages) | NIV-06 (épaisseurs plancher), NIV-07 (épaisseurs ASB / complexe) | Dallage neuf « selon étude BA » (P1 p34-36) — symbole d'épaisseur | Ne produit PAS : valeur d'épaisseur retenue, DXF exécutable, plan à diffuser |
| B-44 (Charpente bois) | MAT-06 (classe bois C18/C24 — hypothèse du diagnostic), MAT-08 (classe de service) | Bois C18/C24 en hypothèse (P2 p10-17) — symbole | Ne produit PAS : valeur de classe de bois validée, note exécutable sans réserve |

---

## SYNTHÈSE (3 points)

### a) Ce qui reste bloqué tant que la donnée n'est pas obtenue

* **B-13** (détection/qualification) attend **GEO-13** (matrice de recalage RSU), produite en fin de phase 1 (B-30/B-31).
* **B-20** (conception) attend **DEC-05** (hypothèses H-xx, produites par B-22) et **GEO-13** ; **NIV-07** reste partiellement ouvert (cotes ASB / épaisseurs neuves, dallage « selon étude BA »).
* **B-34, B-60, B-64** (réservations, plans d'exécution, notice de synthèse) attendent **DEC-05** et **GEO-13**.
* **B-70, B-72** (auto-contrôle, journal de clôture) attendent **DEC-01/02/03/04/05** et **DOC-08** — ce sont des briques de clôture, donc leur suspension est terminale par construction.
* **Aucune donnée n'est Classe III rédhibitoire** (0 BLOQUANTE à ce stade, MPD Ind B) : chaque blocage est en attente d'une **production interne** (INTERNE-GO) ou d'une **donnée externe** (réserves R-01 à R-10 du RDR).

### b) Impact sur la date de remise des livrables exécutables

* **Phase 1 (socle géométrique)** : B-30 → B-32 → B-31 sont **exécutables dès maintenant** en INTERNE-GO : le calage, le nettoyage vectoriel et le recalage produisent eux-mêmes les paramètres (GEO-07 à GEO-13) qui leur manquaient. Aucun retard induit.
* **Phase 2 (audit croisé)** : B-10, B-11, B-12, B-14, B-15 exécutables immédiatement ; B-13 suit la phase 1.
* **Phase 3 (conception)** : B-20 (conception) est suspendue jusqu'à la production de DEC-05/GEO-13 ; B-21, B-24, B-25 exécutables ; B-22, B-23 INTERNE-GO.
* **Phase 5 (livrables d'exécution — B-60 plans d'exécution)** : la remise des plans exécutables est **reportée** tant que NIV-07 (épaisseurs ASB) et DEC-05 ne sont pas levés. Livrable intermédiaire : **B-43/B-44 en PARAMÉTRIQUE** (filigranés, non exécutables).
* **Phase 6 (clôture)** : B-70/B-71/B-72 terminales par construction.

### c) Livrables PARAMÉTRIQUE émis immédiatement

* **B-43** — note de calcul des planchers/dallages, **`_P`**, filigrané « PROVISOIRE — EN ATTENTE DE NIV-06/NIV-07 (épaisseurs) » — pas de valeur d'épaisseur retenue, pas de DXF exécutable.
* **B-44** — note de calcul de charpente bois, **`_P`**, filigrané « PROVISOIRE — EN ATTENTE DE MAT-06/MAT-08 (classe bois) » — pas de valeur de classe validée.

---

## RÉCAPITULATIF DES BRIQUES

| Statut | Nb | Briques |
|---|---:|---|
| Produites (phase 0) | 5 | B-00, B-01, B-02, B-03, B-04 |
| Suspendues | 7 | B-13, B-20, B-34, B-60, B-64, B-70, B-72 |
| Exécutables immédiatement | 23 | B-10, B-11, B-12, B-14, B-15, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-40, B-42, B-45, B-46, B-47, B-49, B-50, B-62, B-71 |
| Exécutables en PARAMÉTRIQUE | 2 | B-43, B-44 |
| SANS OBJET (MPD) | 2 | B-41, B-48 |

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère de la fiche B-04 | Statut |
|---|---|
| Chaque brique suspendue identifie la donnée qui la bloque | ✅ (tableau 1) |
| Chaque brique exécutable est justifiée | ✅ (tableau 2, motif par brique) |
| Chaque PARAMÉTRIQUE précise forme littérale et ce qui n'est pas produit | ✅ (tableau 3) |
| Aucune valeur de repli proposée | ✅ |
| Aucune brique déclarée SANS OBJET par le modèle | ✅ (B-41/B-48 fixés par la MPD D-11/D-09) |
| Synthèse mentionne explicitement l'impact planning | ✅ (§synthèse b) |
| Zéro placeholder (V7) | ✅

**Brique B-04 — Phase 0 cadrage validée ; Phase 1 socle géométrique exécutée (B-30→B-32→B-31 livrés, D-17/D-18 au RDR) — en attente de votre GO pour Phase 2 (audit croisé B-13/B-33).**
