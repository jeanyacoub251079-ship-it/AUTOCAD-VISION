# B-60 — PLANS D'EXÉCUTION — type `ASSEMBLAGE` — CROISSY-FLORA

> **`D-34` — mot pour mot, plan ET note.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission. Reprise chiffrée si non concluants.
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.** Platines d'about à `20 mm` du nu.
> **`A4` — AUCUNE CAPACITÉ ÉCRITE** (`DOC-09` exclue). `R-50-3` **reste ouverte**.

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`ASSEMBLAGE`** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (`A4` `DOC-09` · sabots non catalogués · feu hors lot) |
| **Régime** | **OUTILLÉ** — `_scripts/b60_assemblage.py` (`V13`) |
| **Fond** | `B-32` Ind. D **RDC** — **report, jamais redessin** |
| **Amont** | `B-50` A · `B-20` B · `B-32` D |
| **Aval** | `B-62` (nomenclature détaillée) |
| **`COMPLET`** | **INTERDIT** : `A4` non chiffré · sabots `DOC-09` |

**Ce que cette note fait.** Elle implante les **connecteurs chiffrés** de `B-50` sur le fond `B-32` : `A2` (`10 M16` sur `R1`), `A5` (platines `P1`), `A4` (`M12` `Stab1`, **sans capacité**). Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle n'invente **aucune** capacité `A4`. Elle n'invente **aucun** type de sabot charpente. Elle ne redessine pas `A1` (déjà `FOND`), `A3` (déjà `METAL` `D-36`), `A6` (déjà `MACON`).

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `A1` | `6 HA12` équerre dans `SF1` — **déjà `FOND`** · `R-50-1` CLOSE |
| `A2` | `10 M16 8.8` / face sur moisage `R1` — **ce plan** |
| `A3` | Remplissage `D-36` de `R3` — **déjà `METAL`** · `R-50-2` CLOSE |
| `A4` | `2 M12` / file `Stab1` — **non chiffré** · `R-50-3` ouverte |
| `A5` | Platine `200 × 200 × 15` + `4 M16` constructif |
| `A6` | 8 appuis maçonnerie — **déjà `MACON`** · `R-50-5` CLOSE |

---

## 2. IMPLANTATION (report `B-20` / `B-50`)

| Réf. | Connecteur | Effort | Taux / statut | Plan |
|---|---|---|---|---|
| `A1` | `6 HA12` équerre `l_bd 166` | `N 159 kN` | `166 ≤ 200` — 3 conditions | `FOND` |
| `A2` | `10 M16 8.8` / face, `e = 700 mm` | `V 77,4 kN` | **`0,691`** — **bois gouverne** | **ce plan** |
| `A3` | béton `C25/30` entre ailes | `M_t 1,85 kN·m` | `D-36` obligatoire | `METAL` |
| `A4` | `2 M12` / file, `p ≥ 80 mm` | `F ≤ 5,8 kN` | **NON CHIFFRÉ** | **ce plan** |
| `A5` | platine `200 × 200 × 15` + `4 M16` | `N 100,3 kN` | `σ 0,118` constructif | **ce plan** |
| `A6` | coussins `w_b = 300` | `23` à `77 kN` | `D-37` | `MACON` |

**`A4` prescrit sans capacité :** entraxe `≥ 100 mm`, bords `≥ 150 mm`, résine `p ≥ 80 mm`, **jamais en alvéole**, butée hourdis. Essai d'arrachement 1 file / 4 avant généralisation.

**Sabots `DF`/`PN`.** Efforts `B-44` (`V = 14,89` / `5,11 kN`). Type **non catalogué** (`DOC-09`) — **non inventé**.

---

## 3. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit | **0** |
| Calques `ASSEMBLAGE-*` | **11 / 11** |
| Entités `ASSEMBLAGE-*` | **129** |
| Blocs | **11** (purge −443) |
| DXF | `972 082 o` |
| Filigrane | oui |
| Cloisons / isolation | **0** |
| `R-50-3` | **ouverte** |

Script : `_scripts/b60_assemblage.py`. Planche : `_plans/FLORA_B60_ASSEMBLAGE_EXE_IndA.{dxf,pdf,png}`.

---

## 4. RDL

| Livrable | Indice | Source | Positions | Vue | Date |
|---|---|---|---|---|---|
| `ASSEMBLAGE EXE` | **A** | `B-50` A | `B-20` B | `B-32` D | 21/10/2026 |

**Types `B-60` restants : aucun.** `FOND` / `VERT` / `PLANCHER` / `LINTEAU` / `MACON` / `METAL` / `CHARPENTE` / `ASSEMBLAGE` livrés.
