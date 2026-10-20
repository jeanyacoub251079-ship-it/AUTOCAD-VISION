# ÉTAPE 2 — SPÉCIFICATION DIRECTRICE DE REFONTE UNIVERSELLE `CARNAC v3.0`

| Champ | Valeur proposée (soumise à validation client avant Étape 3) |
|---|---|
| **Document** | Feuille de Spécification Directrice `CARNAC v2.6 → CARNAC v3.0` |
| **Date** | `20/10/2026` |
| **Statut** | **PROPOSITION DE CONCEPTION MÉTHODOLOGIQUE — AUCUN FICHIER DU CARNET MODIFIÉ À CE STADE** |
| **Périmètre couvert** | **Universel** : tailles **`S` / `M` / `L-XL`** · **Neuf / Extension / Surélévation / Réhabilitation** · **Avec ou sans BET Structure MOE (`CFG-1` à `CFG-4`)** |
| **Non-régression (`§8.3`)** | **100 % garantie** : `0` verrou supprimé (`V1..V13` conservés et renforcés + ajout de **`V14` et `V15`**), `0` brique supprimée |
| **Cible Qualité `carnac_lint.py`** | **`10 / 10 PASS` (`0 erreur`, `0 avertissement`)** sur l'intégralité du corpus compilé et de l'arborescence |

---

## 1. Synthèse Executive — Ce qui change entre `CARNAC v2.6` et `CARNAC v3.0`

La version `v2.0–v2.6` avait introduit avec succès le verrou `V13` (preuve d'exécution par script) et la reconnaissance des porteurs (`B-32 §R`). En revanche, sa mise à l'épreuve complète sur un dossier réel a révélé **huit angles morts structurels** qui font tomber tout modèle IA dans les mêmes pièges d'interprétation, ainsi que **9 anomalies référentielles internes** restées cachées dans les 15 974 lignes de `v2.6`.

La version **`v3.0`** est une **version majeure d'architecture** (`Annexe C §4.2`) reposant sur **8 piliers universels** :

1. **Posture Métier Universelle = BET d'Études d'Exécution (`EXE / PAC`) de l'Entreprise** face à **4 Configurations d'Entrée (`CFG-1` à `CFG-4`)**, remplaçant le binaire *« Avec ou Sans BET »* et supprimant définitivement le réflexe erroné de réclamer un « DXF coffrage MOE » ou de ne pas dessiner les ouvrages du BET MOE.
2. **Inversion de l'Architecture des Phases (`Socle Géométrique & Nettoyage` remonté en Phase 1)** : on cale, superpose et nettoie **d'abord** les plans (`B-30 / B-31 / B-32`), **puis** on audite les contradictions multi-pièces (`B-10..B-15`), **puis** on conçoit / synthétise (`B-20..B-25`). Plus aucun audit à l'aveugle ni aucun plan de principe tracé sur un fond architecte pollué.
3. **Verrou `V14` — Indissociabilité du Corpus Marché, Preuve d'Épuisement & Recalage Multi-Sources (`RSU`)** : interdiction absolue de traiter les pièces en silos ou de déclarer une donnée « absente / non localisable » sans preuve d'épuisement de 100 % des pièces (texte + cartouches + coupes + vecteurs PDF/DXF recalés dans un Repère Structurel Unique).
4. **Verrou `V15` — Différentiel Temporel (`EXISTANT / DÉMOLITION / PROJET`) & Continuité Mécanique Descendante (`Toiture → Fondations`)** : toute démolition/ouverture en réhab et tout porteur interrompu d'un niveau `N+1` sur `N` en neuf génèrent obligatoirement un dispositif de reprise suivi jusqu'au sol d'assise.
5. **Loi d'Airain Graphique — `0 %` Cloison & `0 %` Isolation/Doublage sur TOUT Plan de Structure + Antidotes aux 4 Pièges CAO** (`INSERT` récursif multi-calques, retrait du complexe isolant périphérique, purge spatiale des portes/cotes/hachures orphelines, table explicite `Plan Archi N ↔ PB N / PH N-1` et `Nu brut ASB vs Fini`).
6. **6e Mode Officiel `HYPOTHÈSE-NOTIFIÉE` + Prescriptions Chantier `ENC` & Points d'Arrêt `PA-xx`** : fin de la paralysie sous 50 réserves ou des notes symboliques illisibles ; tripartition universelle des incertitudes en **Classe I** (*hypothèse normative conservatrice sous nuage `H-xx` avec délai de visa contradictoire*), **Classe II** (*inconnue physique masquée levée en fouille/curage via prescription sur plan + Point d'Arrêt `PA-xx`*), et **Classe III** (*vrai verrou rédhibitoire*).
7. **Pré-Audit Flash d'Exécutabilité & Règle de Vérité du Titre** : contrôle systématique par ratios dès l'entrée (`L/h` flèche sous maçonnerie, portance semelles et `B_min`, élancement poteaux `H_0/b`, compression locale sous appuis) **même quand un BET MOE existe** ; obligation qu'un plan couvre 100 % de l'emprise avec coupes + schéma mécanique + **`0 collision` de textes**.
8. **Universalité d'Échelle (`Gabarits S / M / L-XL`) + 2 Nouvelles Briques Structurantes (`B-25` & `B-34`)** : ouverture de la **Voie Rapide aux Petites Affaires `S` MÊME SANS BET MOE** (3 portes compactes), et structuration des **Grandes Affaires `L / XL`** (blocs joints de dilatation `JD`, niveaux-types, stabilité globale / contreventement / sismique `B-25`, et synthèse des réservations techniques `B-34`).

---

## 2. Spécification Exacte des **15 Verrous** (`00_MASTER §2`)

Conformément à `00_MASTER §8.3`, **les 13 verrous `V1` à `V13` sont intégralement conservés** (`V1` et `V9` précisés sans retrait d'exigence) et **2 verrous universels (`V14`, `V15`)** sont ajoutés :

| Code | Statut `v3.0` | Intitulé & Règle Opposable |
|---|---|---|
| **`V1`** | **Précisé** | **Hiérarchie d'arbitrage des sources (sans exclusion).** Géométrie de référence = plan architecte ; porteurs conçus = BET structure MOE s'il existe ; sol = rapport géotechnique. **La hiérarchie arbitre une contradiction entre deux valeurs ; elle n'autorise jamais à ignorer une pièce secondaire (CCTP, DPGF, diagnostic, notice, coupe).** |
| **`V2`** | Conservé | **Traçabilité obligatoire.** Tout élément dessiné, calculé ou affirmé cite sa pièce source (fichier, folio/page, indice). |
| **`V3`** | Conservé | **Interdiction de combler un blanc en silence.** Aucune valeur implicite non déclarée. |
| **`V4`** | Conservé | **Critère d'acceptation vérifiable.** Sans critère observable atteint, on change de méthode — jamais de retouche à l'œil. |
| **`V5`** | Conservé | **Preuve avant poursuite.** Passage d'une étape à la suivante subordonné aux preuves lues et validées. |
| **`V6`** | Conservé | **Distinction permanente.** Qualification explicite : *certain (sourcé)* / *hypothèse notifiée sous nuage (`H-xx`)* / *de principe* / *point d'arrêt chantier (`PA-xx`)* / *verrou bloquant*. |
| **`V7`** | Conservé | **Zéro placeholder résiduel.** Aucun `[...]` ni `{{...}}` dans un prompt envoyé ni dans un livrable diffusé. |
| **`V8`** | Conservé | **Formules littérales avant application numérique.** Équation littérale + article normatif + application scriptée. |
| **`V9`** | **Enrichi** | **Conventions de livrable figées, Pureté Structurelle & Vérité du Titre.** Zéro cloison, zéro isolation/doublage, zéro menuiserie de distribution sur 100 % des plans de structure ; adéquation stricte entre le titre d'un plan et son contenu géométrique complet ; `0 collision` de textes. |
| **`V10`** | Conservé | **Neutralité d'outil.** Aucune dépendance à un fournisseur d'IA ni mention d'outil dans les livrables clients. |
| **`V11`** | Conservé | **Blocage local, jamais global.** Seules les briques réellement privées d'une donnée de Classe III sont suspendues (via `PTD`). |
| **`V12`** | **Précisé** | **Requalification à sens unique & Levée Traçable.** Une donnée de Classe III ne se débloque que par réception de pièce, décision `D-xx` au RDR (`PARTIEL-DÉCLARÉ`), ou hypothèse normative bornée validée par le client (`HYPOTHÈSE-NOTIFIÉE`). Jamais d'auto-attribution du mode `COMPLET`. |
| **`V13`** | Conservé | **Preuve d'exécution scriptée.** Tout livrable géométrique ou numérique est généré, relu et contrôlé visuellement par script versionné (`OUT-02 / OUT-03 / OUT-04`). |
| **`V14`** | **NOUVEAU `v3.0`** | **Indissociabilité du Corpus Marché & Preuve d'Épuisement.** Toutes les pièces reçues forment un corpus unique. Il est **interdit** de déclarer une donnée « absente » ou un ouvrage « non localisable » sans journal d'épuisement couvrant 100 % des pièces (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés dans le Repère Structurel Unique). |
| **`V15`** | **NOUVEAU `v3.0`** | **Différentiel Temporel & Continuité Mécanique Descendante.** En existant/phasage, tout ouvrage neuf est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET` ou à un désordre diagnostiqué. En neuf comme en réhab, **tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise** : toute discontinuité d'appui entre `N+1` et `N` impose un ouvrage de transfert explicitement conçu et reporté. |

---

## 3. Spécification Exacte des **6 Modes d'Exécution** & des **3 Classes d'Incertitude** (`00_MASTER §3`)

### 3.1 Les 6 Modes d'Exécution

| Mode | Condition d'emploi | Livrable produit | Exigences graphiques & documentaires obligatoires |
|---|---|---|---|
| **`COMPLET`** | 100 % des données nécessaires sont fournies, cohérentes et visées | Livrable d'exécution intégral (`EXE / BPE`) | Cartouche `EXE`, zéro nuage d'incertitude non levé |
| **`PARTIEL-DÉCLARÉ`** | Une donnée manque dans le DCE, mais le client / MOE a tranché une valeur écrite (`D-xx` au RDR) ou une prescription d'exécution (`ENC` / `PA-xx`) | Livrable chiffré et dessiné intégrant la décision et/ou le Point d'Arrêt chantier | Citation explicite de `D-xx`, encadré `ENC` in extenso sur plans et en tête de note |
| **`HYPOTHÈSE-NOTIFIÉE`** *(NOUVEAU `v3.0`)* | Donnée de **Classe I** (normative/usuelle bornable) absente des pièces ; production autorisée sous hypothèse conservatrice soumise à visa contradictoire | Livrable complet chiffré et dessiné avec valeurs enveloppes Eurocodes/DTU | **Nuage graphique repéré `H-xx` sur chaque zone concernée des plans + encadré en tête de note + tableau des hypothèses avec délai de contradiction `DEC-06` (ex. 2 j / 5 j ouvrés)** |
| **`PARAMÉTRIQUE`** | Donnée de **Classe III** non bornable mais formulation analytique demandée pour aide à la décision / sensibilité | Note littérale + abaque de sensibilité borné | Filigrane obligatoire `PROVISOIRE — EN ATTENTE DE [code]` — jamais exécutable |
| **`INTERNE-GO`** | **Conception ou Synthèse Structurelle** assurée par notre BE (`CFG-1` sans BET MOE, ou `CFG-2` synthèse/complément d'un principe MOE) | Dossier de conception / synthèse structurelle (note de prédimensionnement + planches de synthèse + coupes + schéma mécanique) | Filigrane obligatoire `PRINCIPE — NE PAS EXÉCUTER — Indice P` + alerte contractuelle si `CFG-1` |
| **`SANS OBJET`** | Brique hors périmètre validé ligne à ligne dans la `MPD` (`B-01`) | Une ligne de justification de périmètre uniquement | Jamais motivé par le manque d'une donnée (`V11`) |

---

## 4. Matrice Universelle d'Entrée : **4 Configurations MOE (`CFG-1..4`) × 3 Gabarits (`S / M / L-XL`)**

### 4.1 Les 4 Configurations Universelles de Maturité MOE (`CFG-01`, qualifiée dès `B-00`)
* **`CFG-1` — Sans BET Structure MOE** : création complète de la structure porteuse (`B-20` en `INTERNE-GO`) + **Alerte Contractuelle Obligatoire** sur l'extension de mission Conception et d'assurance décennale.
* **`CFG-2` — BET Structure MOE en PDF / Principe DCE (sans DWG coffrage)** : **zéro demande de DXF coffrage MOE** ; recalage vectoriel exact des PDF MOE sur le DXF Architecte (`B-30`), transcription vectorielle intégrale de **100 % des ouvrages MOE + interfaces manquantes** sur fond structurel pur (`B-32` → `B-20`), pré-audit flash des sections MOE, puis calculs `B-40..50` et plans d'exécution `B-60`.
* **`CFG-3` — BET Structure MOE Vectoriel Complet (DWG/DXF/IFC PRO-DCE + notes)** : recalage et audit croisé automatique `Archi ↔ Structure ↔ CCTP`, pré-audit flash des ratios critiques, `B-20` réduite à la note de synthèse de constructibilité/méthodes entreprise, puis `B-40..50` et `B-60`.
* **`CFG-4` — Mission Partielle Localisée (`Sous-Système`)** : calcul/plan d'un ouvrage isolé (ouverture porteur, escalier, prédalles, massif, charpente seule) ; activation ciblée des seules briques de la chaîne statique concernée + notification explicite des descentes de charges transmises aux ouvrages hors lot.

### 4.2 Les 3 Gabarits d'Opération (`CFG-02`, validé dès `B-01`, remplaçant l'ancien `§6` restrictif)
* **Gabarit `S` — Petite Affaire / Intervention Ponctuelle** *(1 à 5 porteurs, `< 100 m²` ou ouvrage unique, **AVEC ou SANS BET MOE**)* : **Voie Compacte en 3 Portes** (`Porte 1` : Cadrage + Calage/Vue nettoyée + Hypothèses `H-xx` ; `Porte 2` : Schéma mécanique `AVANT/APRÈS` + DDC + Note de calcul ; `Porte 3` : Plan EXE tout-en-un Implantation + Coupes + Ferraillage/Assemblages + Points d'Arrêt + Auto-contrôle).
* **Gabarit `M` — Bâtiment Unitaire Neuf ou Réhabilité** *(`100 à 2 500 m²`, 1 bloc)* : **Voie Standard en 6 Étapes réordonnées**.
* **Gabarit `L / XL` — Grand Ensemble / R+n / Multi-Bâtiments / Infra Lourde** *(`> 2 500 m²`, joints de dilatation `JD`, sous-sols, préfabrication)* : découpage par **Blocs `JD`** et **Niveaux-types**, activation obligatoire de **`B-25` (Stabilité globale / Contreventement / Torsions / Sismique `EC8` + Descente de charges générale)** et de **`B-34` (Synthèse des réservations techniques)**, et allotissement des livrables par jalons chantier (`Lot Infra` → `Lot Superstructure` → `Lot Secondaire`).

---

## 5. Nouvel Ordonnancement Universel des Phases (`00_MASTER §7 & §9`, `Annexe D`)

```text
Phase 0 — CADRAGE & QUALIFICATION        : B-00 → B-01 → B-02 → B-03 → B-04
                                              │
                                              ▼
Phase 1 — SOCLE GÉOMÉTRIQUE & NETTOYAGE  : B-30 (Calage RSU multi-sources)
          [REMONTÉE EN AMONT DE TOUT]      → B-32 (Reconnaissance §R + Vues nettoyées zéro cloison/isolant)
                                           → B-31 (Preuve de superposition multi-étages & multi-sources)
                                              │
                                              ▼
Phase 2 — AUDIT CROISÉ MULTI-PIÈCES      : B-10, B-11, B-12 → B-13 (Contradictions + Réconciliation quantités)
                                           → B-14 (Périmètre lot) → B-15 (Risques + Pré-Audit Flash sections)
                                              │
                                              ▼
Phase 3 — CONCEPTION / SYNTHÈSE & DDC    : B-20 (Conception ou Synthèse structurelle sur fond B-32)
                                           → B-25 [NOUVELLE] (Stabilité globale, Contreventement, JD & EC8)
                                           → B-21 (DDC) → B-22 (Hypothèses & Nuages H-xx)
                                           → B-23 (Exploitation diag) → B-24 (Existant non sondé & PA-xx)
                                              │
                                              ▼
Phase 4 — NOTES DE CALCUL D'EXÉCUTION    : B-40 à B-50 (scriptées V13, Eurocodes / DTU)
                                              │
                                              ▼
Phase 5 — SYNTHÈSE RÉSERVATIONS & PLANS  : B-34 [NOUVELLE] (Synthèse réservations & interfaces lots techniques)
          D'EXÉCUTION                      → B-60 (Plans coffrage / charpente / ferraillage EXE)
                                           → B-62 (Nomenclatures) → B-64 (Notice de synthèse)
                                              │
                                              ▼
Phase 6 — VÉRIFICATION CROISÉE & CLÔTURE : B-33 (Contrôle croisé final Plan ↔ Plan ↔ Note)
                                           → B-70 → B-71 → B-72
```

> **Astuce de stabilité des numéros (`00_MASTER §8`)** : **aucune brique existante ne change de code `B-xx` !** `B-30, B-31, B-32` gardent leurs codes historiques `B-30/31/32` tout en s'exécutant désormais en **Phase 1** (exactement comme dans un code de lois ou une norme Eurocode où les numéros d'articles historiques restent stables pour ne casser aucune archive de projet antérieur). Les 2 briques nouvelles utilisent des numéros libres (`B-25` et `B-34`).

---

## 6. Liste Fermée des Modifications du Dictionnaire (`94 → 106 Variables`)

### 6.1 Corrections d'errata sur les 94 variables existantes (`E-02` & `CC-02`)
1. **`LIV-01`** : restauration du libellé exact **`Conventions calques`** *(au lieu de `'B-61'`)* — consommatrice : `B-60`.
2. **`LIV-03`** : restauration du libellé exact **`Formats sortie`** *(au lieu de `'B-61'`)* — consommatrice : `B-60`.
3. **Synchronisation automatique 100 % exacte** de la colonne `Briques consommatrices` des 94 variables avec l'intégralité des tables `Variables consommées` des fiches (y compris développement automatique des plages `GEO-01 à GEO-05`, `SOL-01 à SOL-05`, `LIV-01 à LIV-05`, etc. → **suppression des 44 divergences actuelles de `v2.6`**).

### 6.2 Ajout fermé de **12 variables universelles** (`C-06` — total = **106 variables**)

| Code | Libellé exact proposé | Briques consommatrices | Justification universelle |
|---|---|---|---|
| **`CFG-01`** | Configuration de maturité MOE (`CFG-1` à `CFG-4`) | `B-00, B-01, B-20, B-60` | Pilote toute la posture BET EXE vs Conception et bloque la fausse demande de DXF coffrage |
| **`CFG-02`** | Gabarit d'opération (`S` / `M` / `L-XL`) | `B-01, B-04, B-25, B-34, B-60` | Pilote la Voie Compacte 3 portes (`S`) comme le découpage multi-bâtiments (`L/XL`) |
| **`CFG-03`** | Découpage en blocs structurels / joints de dilatation (`JD`) et niveaux-types | `B-01, B-20, B-21, B-25, B-30, B-60` | Indispensable dès qu'un bâtiment dépasse un bloc unitaire ou possède des étages courants |
| **`DEC-05`** | Hypothèses notifiées sous nuage (`H-xx` : valeur, norme, zone, statut) | `B-03, B-20, B-22, B-40, B-60, B-64, B-70` | Trace formellement chaque nuage `H-xx` sur plans et notes |
| **`DEC-06`** | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | `B-03, B-22, B-60, B-64` | Rend paramétrable par affaire le délai d'approbation tacite (ex. 2 j, 5 j, 10 j) |
| **`DEC-07`** | Prescriptions chantier opposables (`ENC`) et Points d'Arrêt (`PA-xx`) | `B-03, B-24, B-40, B-41, B-44, B-46, B-60, B-64` | Couvre toutes les inconnues physiques levées en fouille ou après curage |
| **`GEO-13`** | Matrice de recalage multi-sources vers le Repère Structurel Unique (`RSU`) | `B-13, B-20, B-30, B-31, B-32` | Consigne les transformations et résidus (mm) de tous les PDF/DXF secondaires recalés |
| **`GEO-14`** | Différentiel géométrique `EXISTANT / DÉMOLITION / PROJET` et continuités `N+1 → N` | `B-11, B-13, B-20, B-31, B-32, B-33` | Formalise le verrou `V15` en réhabilitation comme en neuf (reprises / transferts) |
| **`NIV-07`** | Table de correspondance `Plan Archi N ↔ PB/PH` et épaisseurs de complexes/finitions (`ASB` vs `Fini`) | `B-02, B-20, B-30, B-32, B-43, B-60` | Élimine 100 % des erreurs d'arase brute coffrage vs niveau fini architecte |
| **`STR-01`** | Système global de contreventement, centre de torsion et descente des efforts horizontaux | `B-20, B-21, B-25, B-42, B-44, B-45, B-46` | Indispensable pour tout bâtiment neuf ou restructuré (vent `EC1` + séisme `EC8`) |
| **`STR-02`** | Poussées des terres, surcharges de remblai et écrans de soutènement périphériques | `B-12, B-25, B-40, B-41, B-42, B-43` | Couvre tous les sous-sols, murs de soutènement, bêches et mitoyennetés enterrées |
| **`STR-03`** | Carnet des réservations et trémies tous corps d'état (`CVC / Plomberie / Élec / Ascenseur`) | `B-32, B-34, B-42, B-43, B-48, B-60` | Évite 80 % des reprises sur chantier en phase EXE (percements voiles/poutres/dalles) |

---

## 7. Plan d'Action Exhaustif Fiche par Fiche (**50 fichiers existants + 2 fiches nouvelles = 52 fichiers**)

| Groupe de fichiers | Nb | Action `v2.6 → v3.0` | Détail exact des modifications contrôlées |
|---|---|---|---|
| **`00_MASTER.md`** | 1 | **REFONTE MAJEURE (`C-07`)** | Intégration `CFG-1..4`, Gabarits `S/M/L-XL` (§6 refondu), 15 verrous (`V1..V15`), 6 modes (`HYPOTHÈSE-NOTIFIÉE` + `ENC/PA`), nouvel ordre en 6 étapes (`Phase 1 = Socle géométrique`), index 39 briques `B-xx` + 4 `T-xx`, compteur `106 variables`. |
| **`01_DICTIONNAIRE/` (`.md` + `.csv`)** | 2 | **GÉNÉRATION AUTO (`E-02, CC-02, C-06`)** | Correction `LIV-01 / LIV-03`, ajout des `12` variables `v3.0`, note de compte historique `88 / 92 / 93 / 94 → 106`, génération automatique `100 %` synchrone depuis les fiches. |
| **`10_ANNEXES/A_Conventions_Livrables.md`** | 1 | **ENRICHISSEMENT MAJEUR (`C-08`)** | Loi d'airain `0 % cloison / 0 % isolation-doublage`, charte graphique normalisée des **nuages `H-xx`**, des **encadrés `ENC / PA-xx`**, du triptyque `EXISTANT / DÉMOLITION / PROJET`, règle **Vérité du Titre** et contrôle **`0 collision` de textes**. |
| **`10_ANNEXES/O_Outillage.md`** | 1 | **ENRICHISSEMENT MAJEUR (`C-09`)** | Protocole CAO universel en 4 étapes (`INSERT` récursif multi-calques, retrait doublage isolant, purge spatiale des portes/cotes orphelines, table `PB/PH & ASB/Fini`), protocole de recalage multi-sources ICP/moindres carrés (`RSU`), script anti-collision de textes et audit `ezdxf == 0 erreur`. |
| **`10_ANNEXES/D_Mode_Emploi.md`** | 1 | **REFONTE MAJEURE (`C-10`)** | Nouveau schéma directeur des 6 phases réordonnées, guide pratique des 3 gabarits (`S` 3 portes sans BET inclus, `M`, `L-XL` multi-blocs `JD`), emploi des nuages `H-xx` et Points d'Arrêt `PA-xx`. |
| **`10_ANNEXES/C_Journal_Revisions.md`** | 1 | **MISE À JOUR CONTRÔLÉE (`E-03, C-11`)** | Restauration de la mention historique `CARNAC_v1.1_variables.csv` en §3.2 (`E-03`), ajout de la section `3.5 Version v3.0` complète, bandeau aligné `v3.0`. |
| **Phase 0 (`B-00` à `B-04`)** | 5 | **ENRICHISSEMENT CIBLÉ (`C-12`)** | `B-00` : qualification `CFG-01`, interdiction de réclamer un DXF coffrage hors `CFG-3`, inventaire vectoriel/raster de toutes les pièces. `B-01` : choix du gabarit `CFG-02` (`S/M/L-XL`) et découpage `JD` (`CFG-03`). `B-02` : table obligatoire `NIV-07` (`PB/PH`, `ASB/Fini`, `0,00 RELATIF`). `B-03` : registres dédiés Décisions `D-xx`, Nuages `H-xx` (`DEC-05/06`), Points d'Arrêt `PA-xx` (`DEC-07`) et Verrous Classe III. `B-04` : routage proportionné selon gabarit `S / M / L-XL`. |
| **Socle Géométrique — Phase 1 (`B-30, B-31, B-32`)** | 3 | **REFONTE MAJEURE (`C-13`)** | Bascule en Phase 1. `B-30` : recalage multi-sources vers le `RSU` (`GEO-13`, DXF + PDF structure + diag + géotech). `B-32` : purge obligatoire `100 %` cloisons + complexes isolants/doublages + entités orphelines, extraction différentielle `EXISTANT / DÉMOLITION / PROJET`, alignement `{{mode}}`. `B-31` : preuve de superposition multi-étages + multi-sources + détection des murs/poteaux non portés (`V15`). |
| **Audit Croisé — Phase 2 (`B-10` à `B-15`)** | 6 | **ENRICHISSEMENT CIBLÉ (`C-14`)** | Appui sur les superpositions `B-30/31/32` ; `V14` (preuve d'épuisement de toutes les pièces avant tout « absent ») ; `B-13` : matrice de réconciliation quantitative `Plans Archi ↔ Plans Structure ↔ CCTP/DPGF` ; `B-15` : **Pré-Audit Flash d'Exécutabilité** obligatoire sur 100 % des sections du dossier (`L/h`, `q_sol`, `H_0/b`, appuis). |
| **Conception / Synthèse — Phase 3 (`B-20..B-24` + `B-25`)** | 6 | **REFONTE MAJEURE (`C-15, C-16`)** | `B-20` : travail exclusif sur fond `B-32`, suppression de l'ambiguïté « ne pas redessiner le BET » au profit de la **transcription vectorielle intégrale + compléments d'interfaces**, alerte contractuelle `CFG-1`. Création de **`B-25` (Stabilité globale, Contreventement, Joints de dilatation & Sismique `EC8`)**. `B-22` & `B-24` : nuages `H-xx` et Points d'Arrêt `PA-xx`. |
| **Calculs d'Exécution — Phase 4 (`B-40` à `B-50`)** | 11 | **ENRICHISSEMENT CIBLÉ (`C-17`)** | Intégration du mode `HYPOTHÈSE-NOTIFIÉE`, report obligatoire en tête de note des prescriptions `ENC / PA-xx`, contrôle de flèche nuisible sous maçonnerie/cloisons fragiles (`B-43, B-44, B-45, B-49`), soutènements `STR-02` (`B-40, B-42`), réservations `STR-03` (`B-42, B-43, B-48`), et symétrisation à `100 %` des tables `Variables consommées` et `Briques amont/aval`. |
| **Synthèse EXE & Livrables — Phase 5 (`B-34` + `B-60, B-62, B-64`)** | 4 | **ENRICHISSEMENT & CRÉATION (`C-18`)** | Création de **`B-34` (Synthèse des réservations & interfaces lots techniques)**. `B-60` : Loi d'airain `0 cloison / 0 isolant`, Vérité du Titre, nuages `H-xx`, encadrés `ENC / PA-xx`, contrôle `0 collision` de textes + alignement `Rappel V7` (`B-60, B-62, B-64`). |
| **Contrôle Croisé & Clôture — Phase 6 (`B-33, B-70..B-72`)** | 4 | **ENRICHISSEMENT CIBLÉ (`C-19`)** | `B-33` placée en vérification croisée globale `Plan ↔ Plan ↔ Note` ; `B-70` enrichie du contrôle des nuages `H-xx`, délais expirés/actifs, Points d'Arrêt `PA-xx` et zéro collision ; `Rappel V7` aligné. |
| **Prompts Transverses (`T-01` à `T-04`)** | 4 | **CORRECTION & ENRICHISSEMENT (`E-04, C-20`)** | Correction des mentions obsolètes `v1.1` et `12 verrous → 15 verrous` dans `T-03` (`E-04`) ; `T-03` intègre nativement le passage obligatoire du compilateur `carnac_lint.py` (`10/10 PASS`) avant toute publication d'une future version `v3.x`. |
| **Historique & Exemples (`11_HISTORIQUE`, `12_EXEMPLES`)** | 2 | **ARCHIVE PROTÉGÉE (`CC-03, C-21`)** | `11_HISTORIQUE` : `0` caractère supprimé sur `v1.0 → v2.6`, bandeau corrigé `v2.5 → v3.0`, ajout complet des entrées `C-06..C-21 / E-02..E-04 / CC-02..CC-03` et `Entrée v3.0`. `12_EXEMPLES` : exemples `v1.1` préservés + normalisation des 2 sous-balises internes `Fin de l'exemple` pour parité `1:1` du compilateur. |

---

## 8. Point de Contrôle Humain — Vos **6 Arbitrages** avant Lancement des Étapes 3 à 6

Pour que je génère exactement le `CARNAC v3.0` que vous voulez (sans aucune initiative non validée), merci de me confirmer ou d'ajuster ces **6 choix fermés** *(si mes options recommandées vous conviennent toutes, vous pouvez simplement répondre : **« GO Étapes 3 à 6 avec les 6 recommandations »**)* :

1. **Q1 — Verrous (`15 verrous : V1 à V15`)** : validez-vous la conservation des 13 verrous actuels + l'ajout de **`V14` (Indissociabilité du corpus & preuve d'épuisement)** et **`V15` (Différentiel `EXISTANT/DÉMOLITION/PROJET` & continuité descendante `Toiture → Fondations`)** ? *(Recommandé : **OUI**)*
2. **Q2 — Modes d'exécution (`6 modes`)** : validez-vous l'officialisation du **6e mode `HYPOTHÈSE-NOTIFIÉE`** (nuage `H-xx` sur plans/notes + délai contradictoire paramétrable `DEC-06`) en complément des **Points d'Arrêt chantier `PA-xx` / `ENC`** ? *(Recommandé : **OUI**)*
3. **Q3 — Réordonnancement des Phases + Conservation des numéros `B-xx`** : validez-vous la **remontée du Socle Géométrique (`B-30 / B-32 / B-31`) en Phase 1** avant l'Audit (`B-10..15`) et la Conception (`B-20..`), **tout en conservant les numéros historiques `B-30, B-31, B-32`** pour ne casser aucune habitude ni archive ? *(Recommandé : **OUI**)*
4. **Q4 — Ajout des 2 Briques Universelles Grandes Affaires / Neuf (`37 → 39` fiches `B-xx`)** : validez-vous la création de **`B-25` (Stabilité globale, Contreventement, Joints de dilatation & Sismique `EC8`)** et **`B-34` (Synthèse des réservations & interfaces lots techniques)** ? *(Recommandé : **OUI** — c'est ce qui rend le CDC réellement complet sur un immeuble neuf R+n ou un chantier TCE)*
5. **Q5 — Dictionnaire (`106 variables`) & Correction `LIV-01 / LIV-03`** : validez-vous la restauration de `LIV-01 = Conventions calques` et `LIV-03 = Formats sortie` + l'ajout des **12 variables `v3.0`** listées au §6 ? *(Recommandé : **OUI**)*
6. **Q6 — Formatage des tableaux internes des fiches** : dans `v2.6`, 40 fiches avaient gardé des **tableaux indentés par tabulations** issus d'un ancien export Google Docs (`Col1 \n \tCol2`), peu lisibles en Markdown brut. Souhaitez-vous que je **convertisse proprement 100 % des tableaux des fiches en vraies tables Markdown standard `| Col 1 | Col 2 |`** (sans perdre un seul mot du contenu, ce qui donnera un rendu impeccable aussi bien en `.md` qu'en Google Docs et PDF), ou préférez-vous garder le format tabulé actuel ? *(Recommandé : **Conversion propre en vraies tables Markdown `|...|`**)*
