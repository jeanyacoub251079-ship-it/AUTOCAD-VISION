# Journal d'exécution — B-02 FDC JYCROISSY (preuve d'exécution, verrou V3/V14)

## 1. Chaîne de production (reproductible)

1. **Entrée** : MPD B-01 Ind B (`../02_PHASE_0_CADRAGE/B-01_MPD_IndB.md` et
   `MPD_jycroissy.csv`, 106 variables) — statuts FOURNIE / PARTIELLE /
   À PRODUIRE PAR GO / NON NÉCESSAIRE.
2. **Relecture B-02 des pièces** (connecteur Google Drive `read_file_text`) :
   - **P1** = CCTP LOT 01 (`1QwpoVBJG356Z3vXmkpDWcH55Hr-jecfj`) — 38 p. ; couverture,
     sommaire, p37-38 DOE captés ; corps p5-36 tronqué par le connecteur (les
     valeurs du corps sont reprises de B-00 Ind B §2, elles-mêmes sourcées).
   - **P2** = DIAG structure (`1fyzT9BC6WjAPZ9GJreOKa9MlAtRwM-it`) — 19 p. ; §2-5
     (planchers A/B, portiques, soubassement pierre) capturés.
   - **P3** = DCE indice C (`17NHerp8YJn2E0PKyZSc2zEi6Qb9oS0YC`) — 5 p. ; f1
     « données d'études » (bétons, armatures, neige/vent/sismicité, charges) et
     légende des ouvrages F1/F2/F3/R1/R2/R3/S1/S2/J1/P1/P2/P3/Stab1 capturés.
   - **P4** (`1AOLRDSNyTg_-i5_vZFNTnZIoDiuTcYOI`) et **P5** (`1iMF4U7KNustRDQqG7bQPjUTDxNZ-TrY2`) :
     nettoyés entre sessions ; leurs valeurs (emprises, hauteurs, nomenclatures,
     calques) sont transcrites de **B-00 Ind B §1.3/§2.1**, qui a consommé 100 % de
     ces deux pièces (preuve §6 du journal B-00).
3. **Format NIV-07** : annexe O §9.5 du CARNAC (local, l.1227-1231) — table
   `Plan Archi N ↔ PB/PH / nu brut ASB / nu fini / FINI − ASB`.
4. **Exécution** : `python3 affaires/JYCROISSY/00_SUPPORTS/build_b02.py`
   (stdlib uniquement) → `B-02_FDC_JYCROISSY.md` + `FDC_jycroissy.csv`.

## 2. Validations automatiques (toutes passes)

* Aucune variable n'figure à la fois en tableau 1 et tableau 2 (assertion sur
  ensembles disjoints).
* Fiabilité ∈ {Contractuelle, Décision, À confirmer} sur chaque ligne du tableau 1.
* Source non vide sur chaque ligne du tableau 1.
* Zéro placeholder `{{...}}` (V7).
* Variables de référence (17) ne sont **pas** présentes en FDC (règle 1).
* Variables NON NÉCESSAIRE (DOC-07, DOC-09, SOL-04, SOL-06, SOL-07, STR-02)
  absentes de la FDC.
* Aucune valeur de repli ; les écarts C-06, C-08, C-09 restent ouverts (pas
  d'arbitrage silencieux).

## 3. Décompte final

| Tableau | Nb | Explication |
|---|---:|---|
| Tableau 1 — variables résolues | 66 | FOURNIE + PARTIELLE avec valeur (variables lues par brique) |
| Tableau 2 — VERROU | 17 | À PRODUIRE PAR GO (0 BLOQUANTE à ce stade) |
| Annexe — références hors FDC | 17 | Variables de référence (règle 1) |
| NON NÉCESSAIRE (hors FDC) | 6 | DOC-07, DOC-09, SOL-04, SOL-06, SOL-07, STR-02 |
| **Total** | **106** | Répartition exhaustive du dictionnaire |

## 4. Niveaux de fiabilité retenus

* **Contractuelle** : valeurs lues dans une pièce du marché (P1/P2/P3/P4/P5).
* **Décision** : valeurs officialisées par le RDR — D-01…D-13 (CR 20/10/2026) :
  ancrage 0,50 m (D-01/D-06), SE 250 daN/m² (D-03), gabarit M (D-07), périmètre
  Flora (D-10), nomenclature PB RDC / PH R+1 (D-13).
* **À confirmer** : valeurs fragmentaires ou de travail, à valider (enrobage S4/30 mm
  P3, C18/C24 hypothèses P2, niveaux, mortiers, etc.).

## 5. Points de jugement majeurs (tracés)

* **NIV-07** est le cœur de la FDC (variable produite par B-02). La correspondance
  architecturale « PH RDC » (P3 f1) = plancher haut **PH R+1** est fixée par **D-13**.
  Les cotes ASB (nu brut) et les épaisseurs de complexe neufs restent **VERROU**
  (dallage « selon étude BA » non fixé) : aucune épaisseur n'est supputée.
* **Partielle ≠ complète** : une variable PARTIELLE porte sa valeur connue avec
  fiabilité « À confirmer », jamais une valeur complétée par supposition.
* **Aucune variable non lue** : 17 variables de référence sont explicitement
  hors FDC (règle 1), les 6 NON NÉCESSAIRE sont exclues par périmètre.

## 6. Preuve d'épuisement (verrou V14)

* Pièces consommées par B-02 : P1 (couverture/sommaire/DOE + corps repris de B-00),
  P2 (intégralité du texte §1-5), P3 (intégralité, 5 folios).
* P4/P5 : consommation documentée en **B-00 Ind B §6** (91 pages PDF + 1 DXF,
  0 XObject image, 1 582 entités DXF, 31 calques) ; B-02 en reprend les valeurs
  transcrites. Réessai possible via connecteur si un écart l'exige.
* Décisions CR 20/10/2026 intégrées ligne à ligne et réversibles (valeur d'origine
  conservée et datée). Aucune pièce déclarée absente/illisible sans preuve.

## 7. Limites déclarées

* Le corps du CCTP P1 (p5-36) est tronqué par le connecteur ; les valeurs de ce
  corps sont sourcées de B-00 Ind B §2 (extraction exhaustive antérieure).
* P4/P5 n'ont pas été re-extraits cette session (nettoyés entre sessions) ;
  transcription de B-00 Ind B.

## 8. Porte suivante

Un **GO B-03** explicite déclenche le Registre des Décisions (RDR) : les 17 VERROU
de la FDC y sont inscrits au registre des verrous, et la FDC validée y est annexée
comme décision D-xx datée.
