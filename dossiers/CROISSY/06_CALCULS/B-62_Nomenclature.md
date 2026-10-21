# B-62 — NOMENCLATURE ET FAÇONNAGE — CROISSY-FLORA

> **NE PAS COMMANDER SANS VISA.** Mode **PARTIEL-DÉCLARÉ**. Filigrane opposable.
> **`D-34` — mot pour mot.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission.
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.**
> **`A4` — AUCUNE CAPACITÉ ÉCRITE.** `R-50-3` **reste ouverte.** Sabots **non inventés.**

| Champ | Valeur |
|---|---|
| **Brique** | `B-62` — Nomenclature et façonnage |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** |
| **Régime** | **OUTILLÉ** — `_scripts/b62_nomenclature.py` (`V13`) |
| **Amont** | 8 DXF `B-60` Ind. A (audit **0**) · notes `B-40`…`B-50` |
| **Aval** | `B-64` (notice) · `B-70` · `B-71` |
| **`COMPLET`** | **INTERDIT** : `H` non relevée · `D-19` · `A4` · sabots `DOC-09` · écart `P2` HA12 · forages `D-36` |

**Ce que cette note fait.** Elle **extrait** des calques `*-NOMENCLATURE` des 8 DXF `B-60` la liste de commande (barres, profilés, bois, connecteurs, béton), le **plan de façonnage BA**, le récapitulatif, l'export CSV et le rapport de cohérence. Rien n'est recalculé. Rien n'est ressaisi.

**Ce qu'elle ne fait pas.** Aucun devis. Aucune commande. Aucun sabot inventé. Aucun forage inventé. Elle **ne corrige pas** un écart plan ↔ note : elle le **signale**. Elle ne clôt **pas** `PA-03` / `R-50-3` / `R-42-1` / `R-45-1`.

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `L_dev` | Longueur développée de barre (mm) |
| `ÉQUERRE` | Forme coudée — `A1` / `P2` dans `SF1` |
| `DROITE` | Barre droite — `P3` / `J1` / nappe `SF1` |
| `CADRE` | Cadre fermé — `HA8` des fûts |
| `EN ATTENTE` | Ligne **non commandable** (donnée absente) |
| `ÉCART` | Divergence plan ↔ note — **non tranchée** |

---

## 2. ENTRÉES (étape 1)

| Entrée | Statut |
|---|---|
| 8 DXF `B-60` Ind. A | ✅ audit **0** · 44 TEXT nomenclature extraits |
| Notes amont `B-40` F · `B-42` B · `B-43` B · `B-44` A · `B-45` A · `B-46` A · `B-49` A · `B-50` A | ✅ |
| Nomenclature graphique intégrée aux plans | ✅ calques `*-NOMENCLATURE` |

**Épuisement (`V14`).** Les 8 DXF relus. Aucune quantité inventée. Masses linéaires = catalogues (`NF EN 10365`, `EN 10219`, `NF A 35-080`), pas des données de projet.

---

## 3. NOMENCLATURE — SYNTHÈSE (62 lignes)

| Famille | Lignes | Poids porté | Commandable ? |
|---|---|---|---|
| **Profilés `S275`** | 13 | **`1 406,5 kg`** + `Stab1` sans `L` | `Stab1` **non** · `P1` `L` hors calque |
| **Treillis `ST25C`** | 1 | **`224,5 kg`** (`111,15 m²` × `2,02`) | oui — emprise `B-43` non remesurée (`H-06`) |
| **Bois `C24`** | 4 | **`198,8 kg`** (`ρ_mean 420` info) | oui — commande en **m³** |
| **Barres `S500B`** | 20 | **`87,2 kg`** + lignes sans `L` | **`P2` HA12 non** (écart forme) · cadres `H` hyp. |
| **Connecteurs** | 4 | platines `9,42 kg` + `20 M16` + `8 M16` + `8 M12` | **`A4` M12 non** (`R-50-3`) |
| **Béton / divers** | 20 | volumes portés, pas de kg | `SF-T` / `GB` **selon fouille** |

**Profilés certains (lus `L` + `n` sur DXF) :**
`F1a/b/c` `2×HEA 200` · `F2 HEB 200` `2,85 m` · `F3 HEB 160` `3,85 m` (`R-45-1`) · `F4 IPE 200` `4,88 m` · `R1 2×UPE 200` `3,85 m` · `R2-N/S HEB 160` `3,82 m` · `R3-N/S UPE 200` `1,55 m` (**une fois**, pas deux : LINTEAU = METAL).

**Bois certains :** `PN1/2/3` `75×200` ×3 `L=3 200` · `DF-ent` `75×200` ×2 · `CF` `75×225` ×2 `L=2 620` **après purge**.

**Connecteurs certains :** `20` boulons `M16 8.8` + rondelles **larges** (`A2`) · `8` tiges `M16` pied `P1` (`A5`) · `2` platines `200×200×15`.

Export : `_rendus/B-62_{barres,profiles,bois,connecteurs,beton,nomenclature,coherence}.csv` (UTF-8, `;`).

---

## 4. FAÇONNAGE ACIERS BA

Planche `_plans/FLORA_B62_FACONNAGE_IndA.{png,pdf}`. Mandrin EC2 : `HA12 → 48 mm` · `HA8 → 32 mm`. Aucun recouvrement.

| Rép. | Forme | `L_dev` | n | Statut |
|---|---|---|---|---|
| `P2-HA12-EQ` | **ÉQUERRE** `H+l_bd+12φ` | `3 110` | 6 | **NON COMMANDABLE** (écart) |
| `P3-HA12-FAC` | DROITE `H+2×40φ` | `3 760` | 6 | INDICATIF (`R-42-1`) |
| `J1-HA12-FAC` | DROITE | `3 760` | 6 | INDICATIF |
| `P2/P3/J1-CAD` | CADRE | `720` / `1 720` / `1 320` | 20+15+15 | INDICATIF (note `B-42`, qté absente du DXF) |
| `SF1-HA8` | DROITE `800−2×50` | `700` | 12 | **CERTAIN** |
| Coussins `HA8` | DROITE *forme non dessinée* | `440`/`340` | 8+8+8 | constructif |
| `ST25C` | nappe | `111,15 m²` | 1 | **CERTAIN** (`H-06`) |
| Cadres `SF1` | e150 jusqu'au lit | — | — | **EN ATTENTE** (qté absente) |

---

## 5. ÉCARTS — SIGNALÉS, NON CORRIGÉS

| Quoi | Plan `B-60` | Note amont | B-62 |
|---|---|---|---|
| **`P2` 6 HA12 forme** | FOND : **ÉQUERRE** `l_bd 166` (`R-50-1` CLOSE) | `B-42` §6 : **DROITE** `3 760 mm` | **Ne tranche pas.** Commande bloquée. Renvoi `B-42` Ind. C **ou** `B-60` FOND Ind. B |
| `P1` `L` | NOMENCLATURE : SHS **sans L** | METAL §2 : `3,00 m` | `L` prise à la note, absence signalée |
| `DF-arb` `L` | NOMENCLATURE : `L_horiz=3 200` (entrait) | DETAILS / `B-44` : `3,62 m` | `L=3 620` du calque DETAILS |
| Forages `D-36` | HABILLAGE : « diam./entraxe → `B-62` » — **aucune cote** | `B-50` A3 : remplissage, pas le piquage | **Non inventé.** Renvoi `B-60` METAL Ind. B |
| Cadres fûts qté | VERT : `e150`/`e200`, **pas de n** | `B-42` : 20+15+15 | Portés **indicatifs** |

---

## 6. EN ATTENTE — NON COMMANDABLE

| Ligne | Motif | Levée |
|---|---|---|
| `P2` 6 HA12 | écart forme | `B-42` C ou `B-60` FOND B |
| Cadres `P2/P3/J1` | `H` hypothèse (`R-42-1`) | relevé de `H` |
| Cadres `SF1` | qté absente du plan | `B-60` FOND B |
| `Stab1` `IPE 120` ×4 | `L` unitaire absente | portée `IPE 160` |
| `A4` `8 M12` | capacité `DOC-09` (`R-50-3`) | fiche **ou** essai 1/4 files |
| `SF-T` / `GB` | fouille `D-19` | ouverture des fouilles |
| Forages `R3` | diam. / entraxe absents | `B-60` METAL B |
| Sabots `DF`/`PN` | `DOC-09` hors FDC | **non inventés** |

`PA-03` **reste ouvert.** `E-07` non chargé. Contreventement toiture absent au `D2` — non inventé. Feu hors lot GO.

---

## 7. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| 8 DXF relus, audit ezdxf | **0 / 0 / 0 / 0 / 0 / 0 / 0 / 0** |
| TEXT nomenclature extraits | **44** |
| Repères attendus retrouvés | **37 / 37** |
| Lignes produites | **62** |
| Écarts signalés (non corrigés) | **5** |
| En attente | **7** |
| CSV UTF-8 `;` | MASTER + 5 feuilles + cohérence |
| Planche façonnage | PNG `257 073 o` · PDF `54 293 o` |
| Devis / commande | **aucun** |
| Filigrane | `NE PAS COMMANDER SANS VISA` |

Script : `_scripts/b62_nomenclature.py`. Journal : `_rendus/b62_nomenclature.txt`. JSON : `_rendus/b62_nomenclature.json`.

---

## 8. RDL

| Livrable | Indice | Source | Date |
|---|---|---|---|
| Nomenclature + façonnage + CSV | **A** | 8× `B-60` A | 21/10/2026 |

**Suite :** `B-64` — Notice de synthèse. `B-41`/`B-47`/`B-48` **SANS OBJET** (`D-38`).
