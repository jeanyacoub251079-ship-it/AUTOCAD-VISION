# ÉTAPES 3 À 6 — RÉALISATION, CONTRÔLE ET LIVRAISON DE `CARNAC v3.0`

| Champ | Valeur certifiée par script (`V13`) |
|---|---|
| **Date d'exécution** | `20/10/2026` |
| **Décision de lancement** | `GO` du client sur les **6 recommandations** de l'Étape 2 (`Q1` à `Q6` : 15 verrous, 6 modes, phases réordonnées, `B-25` + `B-34`, 106 variables, tables Markdown normalisées) |
| **Arborescence produite** | `carnac/CARNAC_v3.0/` — **`52` fichiers** (`51` fichiers `.md` + `1` dictionnaire `.csv` de `106` variables) |
| **Document compilé** | `carnac/CARNAC_v3.0_COMPILE.md` — **`1 194 287` octets** · `SHA-256 = 4601a209eb0a5666b377db782ac25b585ba6a7239f747e7ecd5eeba91f56aa2f` |
| **Aller-retour `decompile → recompile`** | **`0` octet d'écart** (`compile_tree` recompilé à l'identique de bout en bout) |
| **Résultat du contrôle `T1` à `T10`** | **`10 / 10 PASS` — `0` erreur — `0` avertissement** |
| **Baseline `v2.6` (rappel Étape 1)** | `5 PASS` · `2 WARN` · `3 FAIL` — `9` erreurs dures — `322` avertissements |
| **Non-régression** | `0` verrou supprimé (`V1` à `V13` conservés), `0` brique supprimée, `0` variable supprimée, `0` numéro de brique renuméroté |

---

## 1. Ce qui a été produit (Étape 3 — reconstruction)

### 1.1 Arborescence livrée

| Répertoire | Fichiers | Évolution `v2.6 → v3.0` |
|---|---|---|
| `00_MASTER.md` | 1 | **Réécrit** : posture BET d'exécution, `CFG-1..4`, gabarits `S/M/L-XL`, **15 verrous**, **6 modes**, tripartition des incertitudes, ordonnancement en 6 phases, index des 52 fichiers |
| `01_DICTIONNAIRE/` | 2 | **`106` variables** : `94` reprises + **`12` nouvelles** ; libellés `LIV-01` et `LIV-03` restaurés ; consommateurs reconstruits par développement des plages |
| `02_PHASE_0_CADRAGE/` | 5 | Enrichies : qualification `CFG-01`, gabarit `CFG-02`, découpage `CFG-03`, table `NIV-07`, registres `D-xx` / `H-xx` / `PA-xx` / `V-xx` |
| `03_PHASE_1_ANALYSE/` | 6 | Enrichies : preuve d'épuisement `V14`, réconciliation quantitative, Pré-Audit Flash d'Exécutabilité |
| `04_PHASE_2_CONCEPTION/` | 6 | `B-20` refondue + **`B-25` créée** (stabilité globale, contreventement, `JD`, sismique) |
| `05_PHASE_3_CALAGE/` | 4 | Socle géométrique **remonté en Phase 1**, calage multi-sources `RSU`, vue nettoyée différentielle |
| `06_PHASE_4_CALCULS/` | 11 | Enrichies : hypothèses `H-xx` actives, `ENC` / `PA-xx`, flèches sous maçonnerie, soutènements |
| `07_PHASE_5_LIVRABLES/` | 4 | **`B-34` créée** (réservations tous corps d'état) + `B-60` loi d'airain, vérité du titre, `0` collision |
| `08_PHASE_6_CLOTURE/` | 3 | `B-33` devenu vérification croisée finale ; `B-70` contrôle des hypothèses et points d'arrêt |
| `09_TRANSVERSE/` | 4 | `T-03` corrigée (**15 verrous**, passage obligatoire du compilateur `10/10 PASS`) |
| `10_ANNEXES/` | 4 | `A` **§8** pureté structurelle et rendu ; `O` **§9** protocole CAO ; `D` ordonnancement v3.0 ; `C` **§3.5** |
| `11_HISTORIQUE/` | 1 | **Entrée v3.0** complète (`E-02..E-05`, `C-06..C-21`, `CC-03`), archives `v1.0 → v2.6` intactes |
| `12_EXEMPLES/` | 1 | Archive conservée, tableaux reformatés à l'identique |

### 1.2 Contenu normatif ajouté

* **Verrou `V14`** — indissociabilité du corpus et preuve d'épuisement : interdiction de déclarer une donnée absente ou un ouvrage « non plaçable » sans journal d'épuisement de 100 % des pièces (texte, cartouches, notes générales, coupes, nomenclatures, vecteurs recalés).
* **Verrou `V15`** — différentiel `EXISTANT / DÉMOLITION / PROJET` et continuité mécanique descendante `Toiture → Fondations`, avec détection des porteurs non portés.
* **Mode `HYPOTHÈSE-NOTIFIÉE`** et tripartition **Classe I** (normative bornable, nuage `H-xx` + délai `DEC-06`), **Classe II** (inconnue physique, `ENC` + `PA-xx`), **Classe III** (verrou rédhibitoire).
* **`B-25`** — système de contreventement, cheminement des efforts niveau par niveau, centres de masse et de rigidité, torsion, régularité `EC8`, joints de dilatation `JD`, phases provisoires.
* **`B-34`** — carnet unique des réservations tous corps d'état, compatibilité structurale, renforcements renvoyés aux briques de calcul, matrice des interfaces avec responsable de cote, contrôle de collisions.
* **Protocole CAO en quatre temps** (annexe O §9) : `INSERT` récursif multi-calques, retrait des doublages et isolants, purge spatiale des porteurs orphelines (seuil 22 cm), recalage multi-sources `GEO-13`, table `NIV-07`, anti-collision de textes.

---

## 2. Ce qui a été corrigé (Étape 4 — assainissement)

Les **9 erreurs dures** et **322 avertissements** hérités de `CARNAC v2.6` sont tous soldés :

| Anomalie `v2.6` | Correction `v3.0` | Contrôle |
|---|---|---|
| `LIV-01` et `LIV-03` avec libellé `B-61` | Libellés restaurés : **`Conventions de calques DXF`** et **`Formats de sortie`** | `T3` **PASS** |
| `44 / 94` variables aux consommateurs incomplets (plages non développées) | Consommateurs reconstruits automatiquement depuis les fiches (`GEO-01 à GEO-05`, `SOL-01 à SOL-08`, `LIV-01 à LIV-05`…) | `T3` **PASS** |
| `221` arêtes `Amont ↔ Aval` asymétriques | Graphe **symétrisé intégralement** : `428` arêtes vérifiées réciproques, descriptions miroir | `T4` **PASS** |
| `5` mentions de version résiduelles (`v2.5`, `v1.1`, bandeau, archive `v1.1`) | Alignement total sur `3.0` + restauration de l'archive `CARNAC_v1.1_variables.csv` en annexe C §3.2 | `T2` **PASS** |
| `2` mentions « 12 verrous » dans `T-03` | Corrigées en **15 verrous** | `T5` **PASS** |
| `6` fiches désalignées `Rappel V7` (`B-30`, `B-32`, `B-60`, `B-62`, `B-64`, `B-70`) | Placeholders alignés prompt ↔ rappel | `T8` **PASS** |
| `405` tableaux au format export Google Docs (`\n\t`) | **`428` tables Markdown normalisées `\| … \|` — `0` ligne tabulée résiduelle** | `T1` / `T10` **PASS** |
| `2` marqueurs internes de fin de fichier dans `12_EXEMPLES` | Reformulés sans balise de parité | `T1` **PASS** |

---

## 3. Preuve de contrôle (Étape 5)

```text
T1_parite_compilation     PASS    0 erreur   0 avertissement
T2_versions_et_chemins    PASS    0 erreur   0 avertissement
T3_dictionnaire_variables PASS    0 erreur   0 avertissement
T4_graphe_amont_aval      PASS    0 erreur   0 avertissement
T5_compteurs_cardinaux    PASS    0 erreur   0 avertissement
T6_renvois_internes       PASS    0 erreur   0 avertissement
T7_non_regression_verrous PASS    0 erreur   0 avertissement
T8_placeholders_V7        PASS    0 erreur   0 avertissement
T9_journal_et_proprete    PASS    0 erreur   0 avertissement
T10_completude_fiches     PASS    0 erreur   0 avertissement
------------------------------------------------------------
TOTAL                     10/10 PASS   ·   0 erreur   ·   0 avertissement
```

**Mesures associées au contrôle** : `51` fichiers Markdown, `39` fiches `B-xx` + `4` fiches `T-xx`, `106` variables au dictionnaire, `15` verrous présents dans `00_MASTER`, `6` modes, `428` tables Markdown, `0` tabulation résiduelle, `1 194 287` octets compilés, aller-retour `0` octet d'écart.

**Outils versionnés livrés avec le carnet** (dossier `carnac/_tools/`) : `carnac_compiler.py` (décompilation/recompilation sans perte), `carnac_lint.py` (contrôles `T1..T10`), `table_normalizer.py` (normalisation des tableaux), `build_v3.py`, `build_dictionnaire_v3.py`, `symmetrize_v3.py`, `finalize_v3.py`, `build_compile_v3.py`.

---

## 4. Ce qui reste ouvert (Étape 6 — après livraison)

1. **Recette humaine du carnet `v3.0`** : lecture ciblée de `00_MASTER.md` (§2 verrous, §3 modes, §9 ordonnancement) puis de `B-25` et `B-34` (briques nouvelles).
2. **Première affaire réelle en `v3.0`** : application sur un dossier neuf, avec contrôle de la qualification `CFG-01`, du gabarit `CFG-02` et du protocole CAO de l'annexe O §9.
3. **Retour d'expérience `T-03`** : toute anomalie constatée en affaire devient une correction `C-xx` du carnet et une nouvelle version mineure (`v3.1`), sans jamais supprimer de verrou.

> **Rappel de gouvernance** : le carnet `v3.0` est publié comme **version en vigueur**. Il ne se substitue à aucune décision de projet : chaque affaire reste régie par sa MPD, sa FDC et son RDR.
