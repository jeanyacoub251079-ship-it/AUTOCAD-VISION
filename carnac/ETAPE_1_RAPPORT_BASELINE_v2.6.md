# ÉTAPE 1 — RAPPORT D'EXTRACTION & AUDIT FORMEL DE LA BASELINE `CARNAC v2.6`

| Champ | Valeur certifiée par script (`V13`) |
|---|---|
| **Date d'exécution** | `20/10/2026` |
| **Source compilée lue** | `CARNAC_v2.6_compile.md` (`934 431 octets` · `15 973 sauts de ligne`) |
| **Empreinte SHA-256 source** | `1116327ae6dbf29b49ec20088f44172f699dad79fe5efe7351139842f5870603` |
| **Empreinte SHA-256 recompilée** | `1116327ae6dbf29b49ec20088f44172f699dad79fe5efe7351139842f5870603` (**identique octet pour octet — `0 octet` d'écart**) |
| **Arborescence extraite** | `carnac/CARNAC_v2.6/` — **`50 fichiers`** (`49` fichiers `.md` + `1` fichier `.csv` reconstruit) |
| **Dictionnaire extrait** | `01_DICTIONNAIRE/CARNAC_v2.6_variables.csv` — **`94 variables`** (`5273 octets`) |
| **Scripts d'outillage créés** | `carnac/_tools/carnac_compiler.py` · `carnac/_tools/carnac_lint.py` |
| **Statut Baseline `v2.6`** | **FIGÉE EN LECTURE SEULE** (`BASELINE_MANIFEST_v2.6.json` + contrôle SHA-256) |

---

## 1. Preuve de Décompilation / Recompilation Sans Perte (`0 octet` d'écart)

Le compilateur bidirectionnel `carnac/_tools/carnac_compiler.py` a décomposé `CARNAC_v2.6_compile.md` en son arborescence de référence `carnac/CARNAC_v2.6/`, généré le fichier tabulaire `01_DICTIONNAIRE/CARNAC_v2.6_variables.csv`, puis réassemblé les 49 fichiers Markdown en mémoire pour vérifier la fidélité absolue de l'extraction :

- **Octets fichier original** : `934 431` octets
- **Octets fichier réassemblé** : `934 431` octets (**différence = `0 octet`**)
- **Fiches de briques opérationnelles (`B-xx`)** : **37 fiches** (`B-00` à `B-72`, numéros `B-61` et `B-63` vacants)
- **Prompts transverses (`T-xx`)** : **4 fiches** (`T-01` à `T-04`)
- **Documents maîtres, dictionnaire, annexes, historique & exemples** : **8 fichiers `.md` + `1` fichier `.csv`**

### Inventaire intégral des 50 fichiers de la Baseline `CARNAC v2.6`

| # | Chemin relatif dans `CARNAC_v2.6/` | Lignes | Octets | SHA-256 (16 premiers car.) |
|---|---|---|---|---|
| 1 | `00_MASTER.md` | 312 | 26,116 | `aa1835e356f0fff9` |
| 2 | `01_DICTIONNAIRE/CARNAC_v2.6_variables.md` | 103 | 6,987 | `c33db68a70b2667e` |
| 3 | `10_ANNEXES/A_Conventions_Livrables.md` | 531 | 14,766 | `c290b4af17070502` |
| 4 | `10_ANNEXES/O_Outillage.md` | 67 | 7,146 | `e1147df83d8f4c3d` |
| 5 | `10_ANNEXES/D_Mode_Emploi.md` | 450 | 22,414 | `9a630563611ea852` |
| 6 | `10_ANNEXES/C_Journal_Revisions.md` | 261 | 10,225 | `a049e5c4fc13e3a8` |
| 7 | `02_PHASE_0_CADRAGE/B-00_Inventaire.md` | 157 | 8,097 | `9121ac46f1be6e4d` |
| 8 | `02_PHASE_0_CADRAGE/B-01_MPD.md` | 148 | 9,806 | `ab5a12a19dcadc79` |
| 9 | `02_PHASE_0_CADRAGE/B-02_FDC.md` | 167 | 10,179 | `25692ae76685c13c` |
| 10 | `02_PHASE_0_CADRAGE/B-03_RDR.md` | 214 | 13,171 | `511b41be464f3629` |
| 11 | `02_PHASE_0_CADRAGE/B-04_PTD.md` | 186 | 10,928 | `00478553acf5cdf5` |
| 12 | `03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md` | 209 | 12,191 | `001e23bcabecbd93` |
| 13 | `03_PHASE_1_ANALYSE/B-11_Audit_Diagnostic.md` | 234 | 14,949 | `33ceb59d979599a6` |
| 14 | `03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md` | 202 | 13,403 | `c14e69e1c201a485` |
| 15 | `03_PHASE_1_ANALYSE/B-13_Contradictions.md` | 249 | 15,921 | `17a16ad45f8f3c6d` |
| 16 | `03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md` | 209 | 13,617 | `54c55e78a3c42607` |
| 17 | `03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md` | 247 | 15,564 | `14f7a05d698efa24` |
| 18 | `04_PHASE_2_CONCEPTION/B-20_Conception_GO.md` | 264 | 17,473 | `c2e33413a7f5dead` |
| 19 | `04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md` | 249 | 13,875 | `4ff218e2083f3538` |
| 20 | `04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md` | 252 | 13,901 | `9a8ef91b86320b89` |
| 21 | `04_PHASE_2_CONCEPTION/B-23_Exploitation_Diagnostic.md` | 234 | 15,967 | `2a1f941cc64ab85d` |
| 22 | `04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md` | 254 | 16,920 | `de8904f5254225e5` |
| 23 | `05_PHASE_3_CALAGE/B-30_Calage.md` | 220 | 16,222 | `b47a174c4331a9fe` |
| 24 | `05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md` | 244 | 16,391 | `99817a8846b3b032` |
| 25 | `05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md` | 328 | 29,187 | `f9cac6904052b302` |
| 26 | `05_PHASE_3_CALAGE/B-33_Verification_Croisee.md` | 240 | 16,802 | `5935d6c6a8332cd9` |
| 27 | `06_PHASE_4_CALCULS/B-40_Fondations_Superficielles.md` | 389 | 25,098 | `7ff1ace5e45a3b48` |
| 28 | `06_PHASE_4_CALCULS/B-41_Fondations_Profondes.md` | 317 | 21,686 | `4443a3a9acd94f35` |
| 29 | `06_PHASE_4_CALCULS/B-42_Verticaux_BA.md` | 427 | 27,352 | `291541a0c125a060` |
| 30 | `06_PHASE_4_CALCULS/B-43_Planchers_Dallages.md` | 423 | 26,394 | `5bbd013079daaff1` |
| 31 | `06_PHASE_4_CALCULS/B-44_Charpente_Bois.md` | 356 | 22,990 | `aa6cbef3a9037744` |
| 32 | `06_PHASE_4_CALCULS/B-45_Structure_Metallique.md` | 344 | 22,749 | `939723e2f28d32fd` |
| 33 | `06_PHASE_4_CALCULS/B-46_Maconnerie.md` | 435 | 27,113 | `2d0090e14f28e8b5` |
| 34 | `06_PHASE_4_CALCULS/B-47_Escaliers.md` | 375 | 23,895 | `a17917c5b8eb7796` |
| 35 | `06_PHASE_4_CALCULS/B-48_Predalles.md` | 369 | 24,808 | `65f271153af15ff9` |
| 36 | `06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md` | 427 | 25,950 | `766ac917630261b1` |
| 37 | `06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md` | 423 | 29,988 | `96ac51909f4675ea` |
| 38 | `07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md` | 342 | 21,416 | `97be91a7912855ae` |
| 39 | `07_PHASE_5_LIVRABLES/B-62_Nomenclature.md` | 336 | 18,005 | `9e2398d5ff9abf79` |
| 40 | `07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md` | 337 | 18,614 | `ae8bc50a5e374dcd` |
| 41 | `08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md` | 307 | 20,382 | `4c1dbdbda447dc4a` |
| 42 | `08_PHASE_6_CLOTURE/B-71_Indicage.md` | 304 | 17,351 | `e66cb6b88318eabe` |
| 43 | `08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md` | 263 | 16,420 | `7760fd6026c2f90f` |
| 44 | `09_TRANSVERSE/T-01_Sincerite.md` | 242 | 15,189 | `7b5621b2a4b57bea` |
| 45 | `09_TRANSVERSE/T-02_Recadrage.md` | 272 | 17,158 | `daa60c0faa1ad1f6` |
| 46 | `09_TRANSVERSE/T-03_Meta_Amelioration.md` | 275 | 17,060 | `0b04f9a613ce2291` |
| 47 | `09_TRANSVERSE/T-04_Demande_Complement.md` | 269 | 16,180 | `7996af3a808083c3` |
| 48 | `11_HISTORIQUE/Journal_des_modifications.md` | 462 | 22,402 | `667818e57eccce53` |
| 49 | `12_EXEMPLES/Exemples_Phase_0.md` | 1706 | 67,785 | `c8a88f460d14a62c` |
| 50 | `01_DICTIONNAIRE/CARNAC_v2.6_variables.csv` *(généré depuis table MD)* | 95 | 5,273 | `d4290c69db299c54` |

---

## 2. Diagnostic Initial de `CARNAC v2.6` par le Compilateur `carnac_lint.py` (Tests `T1` à `T10`)

> **Pourquoi cet audit initial est décisif avant d'écrire `v3.0`** : en passant `CARNAC v2.6` telle quelle au crible des **10 contrôles automatiques `T1–T10`**, le script a mis au jour **9 erreurs internes résiduelles** et **4 familles d'asymétries cachées** qui avaient survécu aux révisions `v2.0 → v2.6`. Les connaître dès l'Étape 1 permet de les purger intégralement en `v3.0` afin d'atteindre **`10/10 PASS (0 erreur, 0 avertissement)`**.

| Code Test | Intitulé du Contrôle Automatique | Verdict `v2.6` | Erreurs | Alertes | Diagnostic synthétique sur `v2.6` |
|---|---|---|---|---|---|
| **`T1`** | `T1_parite_compilation` | **`PASS`** | `0` | `1` | `0` écart d'octet ; `49` débuts = `49` fins de fichiers + `2` balises internes dans `12_EXEMPLES` à normaliser |
| **`T2`** | `T2_versions_et_chemins` | **`FAIL`** | `5` | `50` | `4` en-têtes restés en `v2.5` + `1` corruption d'archive `v1.1` en `Annexe C §3.2` + `T-03` restée en `v1.1` |
| **`T3`** | `T3_dictionnaire_variables` | **`FAIL`** | `2` | `44` | `LIV-01` et `LIV-03` corrompus en `'B-61'` (vrais noms retrouvés dans `12_EXEMPLES`) + `44` variables à consommateurs incomplets |
| **`T4`** | `T4_graphe_amont_aval` | **`WARN`** | `0` | `221` | `221` liens `Amont ↔ Aval` non réciproques entre les 41 fiches (ex. `B-01 → B-40..50` sans retour) |
| **`T5`** | `T5_compteurs_cardinaux` | **`FAIL`** | `2` | `0` | `2` mentions résiduelles de *« 12 verrous »* dans `T-03` (alors que `00_MASTER` en compte `13`) ; `0` erreur de compte de puces |
| **`T6`** | `T6_renvois_internes` | **`PASS`** | `0` | `0` | `100 %` des codes `B-xx` et `T-xx` cités dans le corpus actif pointent vers des fiches existantes |
| **`T7`** | `T7_non_regression_verrous` | **`PASS`** | `0` | `0` | Les `13` verrous `V1` à `V13` sont bien présents et complets dans `00_MASTER.md` |
| **`T8`** | `T8_placeholders_V7` | **`WARN`** | `0` | `6` | `6` fiches ont un écart entre les `{{...}}` du `PROMPT` et la ligne `Rappel V7` (`B-30, B-32, B-60, B-62, B-64, B-70`) |
| **`T9`** | `T9_journal_et_proprete` | **`PASS`** | `0` | `0` | `0` fragment conversationnel résiduel ; `Entrée v2.6` bien présente dans `11_HISTORIQUE` |
| **`T10`** | `T10_completude_fiches` | **`PASS`** | `0` | `0` | `37/37` fiches `B-xx` et `4/4` fiches `T-xx` possèdent leurs 4 sections réglementaires et `Version = 2.6` |

### Détail nominatif des 9 erreurs résiduelles découvertes dans `CARNAC v2.6` (et leur correction prévue en `v3.0`)

1. **`[T2]`** 01_DICTIONNAIRE/CARNAC_v2.6_variables.md:6 — en-tête ou chemin non aligné sur v2.6: '**Note de compte (à lire avant toute citation d'un nombre de variables).** Le compte en vigueur'
2. **`[T2]`** 10_ANNEXES/C_Journal_Revisions.md:2 — en-tête ou chemin non aligné sur v2.6: '> Version du document : 2.5 (carnet CARNAC v2.6) — historique des modifications : 11_HISTORIQUE'
3. **`[T2]`** 10_ANNEXES/O_Outillage.md:2 — en-tête ou chemin non aligné sur v2.6: '> Version du document : 2.5 (carnet CARNAC v2.6) — historique des modifications : 11_HISTORIQUE'
4. **`[T2]`** 11_HISTORIQUE/Journal_des_modifications.md:1 — en-tête ou chemin non aligné sur v2.6: 'Fichier 11_HISTORIQUE/Journal_des_modifications.md — CARNAC v2.5'
5. **`[T2]`** 10_ANNEXES/C_Journal_Revisions.md:128 — corruption d'archive historique : section v1.1 cite 'Dictionnaire (01_DICTIONNAIRE/CARNAC_v2.6_variables.csv)' au lieu de v1.1
6. **`[T3]`** 01_DICTIONNAIRE: variable LIV-01 a un libellé corrompu 'B-61' (vestige d'une ancienne colonne)
7. **`[T3]`** 01_DICTIONNAIRE: variable LIV-03 a un libellé corrompu 'B-61' (vestige d'une ancienne colonne)
8. **`[T5]`** 09_TRANSVERSE/T-03_Meta_Amelioration.md:162 — mention '12 verrous' != 13 verrous : 'Les 12 verrous sont la protection du carnet contre les dérives. Une correction qui supprim'
9. **`[T5]`** 09_TRANSVERSE/T-03_Meta_Amelioration.md:182 — mention '12 verrous' != 13 verrous : '* les 12 verrous sont la protection du carnet contre les dérives ;'

> **Restitution archéologique des variables `LIV-01` et `LIV-03`** : l'analyse croisée avec `12_EXEMPLES/Exemples_Phase_0.md` (lignes 452 et 466) a permis de retrouver avec certitude les libellés d'origine écrasés par un décalage de colonne lors de la reconstruction `v2.0` :
> - **`LIV-01`** = **`Conventions calques`** *(consommée par `B-60`)* ;
> - **`LIV-03`** = **`Formats sortie`** *(DXF, PDF, PNG — consommée par `B-60`)*. 

### Détail nominatif des 6 écarts `Rappel V7` découverts dans `CARNAC v2.6` (`T8`)

1. 05_PHASE_3_CALAGE/B-30_Calage.md: placeholders prompt=['ID-01', 'ID-02'] != Rappel V7=['ID-01', 'ID-02', 'mode']
2. 05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md: placeholders prompt=['ID-01', 'ID-02', 'code_livrable', 'indice_livrable'] != Rappel V7=['ID-01', 'ID-02', 'code_livrable', 'indice_livrable', 'mode']
3. 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md: placeholders prompt=['ID-01', 'ID-02', 'indice', 'mode', 'type_livrable'] != Rappel V7=['ID-01', 'ID-02', 'mode', 'type_livrable']
4. 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md: placeholders prompt=['ID-01', 'ID-02', 'type_livrable'] != Rappel V7=['ID-01', 'ID-02', 'mode', 'type_livrable']
5. 07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md: placeholders prompt=['ID-01', 'ID-02', 'type_livrable'] != Rappel V7=['ID-01', 'ID-02', 'mode', 'type_livrable']
6. 08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md: placeholders prompt=['ID-01', 'ID-02', 'périmètre'] != Rappel V7=['ID-01', 'ID-02', 'mode', 'périmètre']

---

## 3. Classification Automatique des `456` Mentions de Version de `CARNAC v2.6`

Le parseur sémantique `find_version_tokens()` (qui distingue les numéros de version `vX.Y` / `Version : X.Y` des numéros de chapitres `§1.1`, `2.3`) a recensé exactement **`472` jetons de version** dans les 49 fichiers :

| Classe de gouvernance | Nombre de jetons | Règle appliquée lors du passage en `v3.0` |
|---|---|---|
| **`HISTORIQUE_PROTÉGÉ`** | **`229`** | **Verrouillés contre tout remplacement** (`11_HISTORIQUE/`, `12_EXEMPLES/`, corps de `Annexe C`, mentions *« nouveau en v2.0 »*) — **hors** la restauration de l'archive corrompue `CARNAC_v1.1_variables.csv` en `Annexe C §3.2` |
| **`COURANT_AUTO`** | **`61`** | Bascule contrôlée vers `v3.0` / `3.0` (bandeaux de titre des 50 fichiers, champ `Version`, chemins `CARNAC_v3.0_variables.csv/.md` — y compris correction des 4 en-têtes oubliés en `v2.5`) |
| **`CONTEXTUEL`** | **`182`** | Dont **`41`** lignes standard *« Modifications depuis v1.0 »* (conservées telles quelles) et **`9` occurrences contextuelles** revues individuellement (`00_MASTER.md:259` `v2.4 → v3.0`, `T-03` `v1.1 → v3.0`, etc.) |
