# B-60 — PLANS D'EXÉCUTION — type `MACON` — CROISSY-FLORA

> **`D-34` — mot pour mot, plan ET note.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission. Reprise chiffrée si non concluants.
> **`D-37` — on prescrit le coussin `w_b ≥ 300 mm` sous `R1` / `F2` / `F3`.** Ce n'est **pas** un linteau.
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.**

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`MACON`** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (`MAT-09`..`12` bloquants) |
| **Régime** | **OUTILLÉ** — `_scripts/b60_macon.py` (`V13`) |
| **Fond** | `B-32` Ind. D — **report, jamais redessin** |
| **Amont** | `B-46` A · `D-37` · `B-20` B · `B-32` D |
| **Aval** | `B-62` · `B-60 METAL` (`D-36`, profilés) |
| **`COMPLET`** | **INTERDIT** : `MAT-09`..`12` bloquants |

**Ce que cette note fait.** Elle implante les **six coussins** `w_b = 300 mm` sous les extrémités de `R1`, `F2` et `F3`, aux sommiers `B-20` élargis. Verdict inconditionnel (`N_Rdc ≥ 84 kN` dès `a₁ = 0`). Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle ne dimensionne **aucune** maçonnerie neuve. Elle n'implante **pas** `F1`/`R3` (LINTEAU livré). Elle ne coule **pas** le remplissage `D-36` (METAL). Elle n'invente **aucun** chaînage (`MAT-12` non relevé).

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `C-R1-O/E` | Coussins sous `R1` (`77,4 kN`) |
| `C-F2-O/E` | Coussins sous `F2` (`62,4 kN`) |
| `C-F3-O/E` | Coussins sous `F3` (`61,6 kN`) |
| `w_b` | Largeur d'appui — **`300 mm` mini** (`D-37`) |
| `D-37` | Prescription client 21/10 — `R-46-1`/`R-46-2` CLOSE |

---

## 2. IMPLANTATION (6 coussins)

| Rép. | Sous | `V_Ed` | Géométrie | Statut |
|---|---|---|---|---|
| `C-R1-O/E` | `R1` | `77,4 kN` | `300 × ~500 × 200` C25/30 | **D-37** |
| `C-F2-O/E` | `F2` | `62,4 kN` | `300 × ~400 × 200` C25/30 | **D-37** |
| `C-F3-O/E` | `F3` | `61,6 kN` | `300 × ~400 × 200` C25/30 | **D-37** |

Centré en épaisseur (`e ≤ t/4`). Mortier complet. `4 HA8` constructif. **Ne pas réduire `w_b`.**

`F1`/`R3`/`R2`/`F4` : **pas de coussin** (`B-46` : OK sans).

---

## 3. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit | **0** |
| Calques `MACON-*` | **9 / 9** |
| Entités `MACON-*` | **106** |
| Blocs | **11** (purge −443) |
| DXF | `968 922 o` |
| Filigrane | oui |
| Cloisons / isolation | **0** |

Script : `_scripts/b60_macon.py`. Planche : `_plans/FLORA_B60_MACON_EXE_IndA.{dxf,pdf,png}`.

---

## 4. RDL

| Livrable | Indice | Source | Positions | Vue | Date |
|---|---|---|---|---|---|
| `MACON EXE` | **A** | `B-46` A · `D-37` | `B-20` B | `B-32` D | 21/10/2026 |

**Types `B-60` restants :** `METAL` (`D-36` + profilés) · `CHARPENTE` · `ASSEMBLAGE`. `FOND` / `VERT` / `PLANCHER` / `LINTEAU` / `MACON` livrés.
