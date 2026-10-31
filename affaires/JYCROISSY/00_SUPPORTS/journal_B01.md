# Journal d'exécution — B-01 JYCROISSY (preuve d'exécution, verrou V3)

## 1. Chaîne de production (reproductible)

1. Extraction de la table officielle des 106 variables depuis le carnet
   compilé (balises `01_DICTIONNAIRE/CARNAC_v3.0_variables.md`) :
   `data/JYCROISSY/extraction/dictionnaire_carnac.csv` (106 lignes, 18 variables
   de référence sans brique consommatrice).
2. Saisie des propositions de statut dans `build_b01.py` (table `STATUTS`,
   une ligne par variable, source/raison + mode induit), à partir de B-00
   Ind B, du pré-RDR (D-01…D-06, PA-01) et des pièces lues.
3. Exécution : `.venv/bin/python affaires/JYCROISSY/00_SUPPORTS/build_b01.py`
   — le script valide les cinq règles de la fiche B-01 et génère
   `MPD_jycroissy.csv` et `B-01_MPD_IndA.md`.

## 2. Validations automatiques (toutes passes)

* Couverture : 106/106 variables, exactement un statut chacune (assertion
  sur ensembles `manquants`/`en_trop`).
* NON NÉCESSAIRE : motif de périmètre obligatoire contenant le mot
  « Périmètre » et mode SANS OBJET (3 lignes : DOC-07, DOC-09, STR-02).
* BLOQUANTE : rattachée à une brique consommatrice du dictionnaire, aucun
  mode COMPLET (3 lignes : SOL-04, SOL-06, SOL-07).
* À PRODUIRE PAR GO : brique INTERNE-GO identifiée (17 lignes).
* Zéro placeholder `{{...}}` (vérification grep, exit 1).

## 3. Décompte final des statuts

| Statut | Nb |
|---|---:|
| FOURNIE | 39 |
| PARTIELLE | 44 |
| À PRODUIRE PAR GO | 17 |
| BLOQUANTE | 3 |
| NON NÉCESSAIRE (proposition, à valider ligne par ligne) | 3 |
| **Total** | **106** |

## 4. Points de jugement majeurs (tracés)

* **CFG-02 proposé = gabarit M** (bâtiment unitaire, emprise < 2 500 m²,
  plus de 5 porteurs, pas de JD ni de sous-sol Flora) ; CFG-03 = un bloc
  « Flora », cinq niveaux fonctionnels, statut PARTIELLE.
* **DOC-06 (G2) = PARTIELLE et non BLOQUANTE** : la pièce n'est pas reçue
  mais les paramètres de dimensionnement sont officialisés par D-06 ; les
  variables manquantes du rapport (SOL-04, SOL-06, SOL-07) portent
  individuellement le statut BLOQUANTE avec leur brique. Le risque de
  confondre « pièce absente » et « donnée disponible » est ainsi évité.
* **Aucun NON NÉCESSAIRE pour indisponibilité** : DOC-07 (exclusion
  désamiantage/déplombage), DOC-09 (pas de prédalle), STR-02 (pas de
  soutènement Flora, réserve C-07) relèvent tous du périmètre.
* **B-41 (fondations profondes)** et **B-48 (prédalles)** proposées en
  SANS OBJET corrélatif ; décision réservée à la validation humaine puis
  B-14/B-04.
* En CFG-2, AC-03 reste FOURNIE : l'INTERNE-GO ne porte que sur les
  compléments de conception, jamais sur une demande de DXF coffrage MOE.

## 5. Limites déclarées

* 18 variables de référence (aucun consommateur brique) reçoivent quand
  même un statut pour exhaustivité du tableau ; elles ne suspendent rien.
* Les modes PARTIEL-DÉCLARÉ supposent l'inscription des décisions
  correspondantes au RDR officiel B-03 (le pré-RDR accueille d'ores et
  déjà D-01…D-13 et PA-01).

## 6. Évolution Ind A → Ind B (2026-10-23) — prise en compte des validations/corrections

Réception des décisions de l'utilisateur (message du 23/10/2026), consignées
au pré-RDR en D-07 à D-13 :

* **D-07** — CFG-02 = gabarit **M validé**.
* **D-08** — DOC-07 (amiante/plomb) **NON NÉCESSAIRE confirmé**.
* **D-09** — DOC-09 (prédalles) **NON NÉCESSAIRE confirmé** ; B-48 SANS OBJET.
* **D-10** — STR-02 **NON NÉCESSAIRE confirmé** ; périmètre = **bâtiment Flora
  uniquement** → **C-07 tranchée** (Gardien/Bagatelle hors périmètre structure).
* **D-11** — B-41 (fondations profondes) **SANS OBJET confirmé**.
* **D-12** — Géotechnique : **G2 complet non transmissible** (bug) ; mission
  CARNAC = **dimensionnement aux contraintes D-06 seulement, sans calcul de
  tassement** ; tassement/assise délégués au géotechnicien ; **absence de
  nappe phréatique confirmée** → SOL-04/SOL-06/SOL-07 **NON NÉCESSAIRE**
  (périmètre) ; B-40 non bloquante.
* **D-13** — CFG-03 nomenclature corrigée : **premier niveau = PB (premier
  bas)**, autres = **PH (plancher haut)** → **PB RDC** / **PH R+1** ;
  « PH RDC » archi (P3 f1) = sous-face du plancher haut PH R+1 ; **vue unique
  « FONDATIONS + PB RDC »** acceptable.

Conséquences sur la MPD :
* **0 BLOQUANTE** (levées par D-12) ; **6 NON NÉCESSAIRE** (DOC-07, DOC-09,
  SOL-04, SOL-06, SOL-07, STR-02), toutes tranchées.
* Décompte Ind B : FOURNIE 39, PARTIELLE 44, À PRODUIRE PAR GO 17,
  NON NÉCESSAIRE 6, BLOQUANTE 0 = **106**.
* Écarts B-00 tranchés en supplémentaire : **C-07** (D-10). Restent ouverts :
  C-06, C-08, C-09, C-10, C-11.

Note de production : le venv (`.venv`) et le dossier `data/` (gitignorés)
ont été nettoyés entre sessions. `build_b01.py` ne dépend que de la
bibliothèque standard (csv/os/collections) ; le dictionnaire
`dictionnaire_carnac.csv` a été reconstruit à partir du livrable persistant
`B-01_MPD_IndA.md` (106 variables) avant relance du générateur.

