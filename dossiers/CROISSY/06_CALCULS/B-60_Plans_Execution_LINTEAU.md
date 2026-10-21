# B-60 — PLANS D'EXÉCUTION — type `LINTEAU` — CROISSY-FLORA

> **`D-34` — mot pour mot, plan ET note.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission. Reprise chiffrée si non concluants.
> **`D-36` — remplissage `C25/30` des `UPE 200` de `R3` : ACCEPTÉ.**
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.**
> **`D-37` — coussins `R1`/`F2`/`F3` : PAS des linteaux → `B-60 MACON`.**

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`LINTEAU`** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** |
| **Régime** | **OUTILLÉ** — `_scripts/b60_linteau.py` (`V13`) |
| **Fond** | `B-32` Ind. D — **report, jamais redessin** |
| **Amont** | `B-49` A · `B-20` B (positions) · `B-32` D · `B-30` |
| **Aval** | `B-62` · `B-60 METAL` (coulage `D-36`) · `B-60 MACON` (`D-37`) |
| **`COMPLET`** | **INTERDIT** : `SEC-01` hors lot |

**Ce que cette note fait.** Elle implante les **cinq linteaux neufs** de `B-49` **sur le fond `B-32`**, aux positions `B-20` (millimètre). Elle cote les **`S1` de `R3` sur les abouts de mur**, hors bois (`R-46-4`). Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle n'implante **pas** `F2`/`F3`/`R1` (pas des linteaux). Elle ne coule **pas** le remplissage (`B-60 METAL`). Elle ne calcule **aucun** bois (`E-08` court-circuité). Seuils BA : **SANS OBJET**.

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `F1a/b/c` | `2 × HEA 200` — frangements neufs |
| `R3-N/S` | `UPE 200` + béton `D-36` — façade Est |
| `S1` / `S2` | Sommiers `200×400×200` / `200×500×200` |
| `E-08` | Linteaux bois Est — **court-circuités**, bois reste |
| `D-36` | Remplissage `C25/30` des `UPE 200` |

---

## 2. IMPLANTATION (report `B-20`)

| Rép. | Position (m) | Section | `L` | Appui | Taux |
|---|---|---|---|---|---|
| `F1a` | File D `89,77` / `53,20→54,64` | `2 × HEA 200` | `1,00 m` | `S2` + `J1` | `0,010` / `0,059` |
| `F1b` | File 4 `92,80→94,28` / `54,89` | `2 × HEA 200` | `0,90 m` | `S2` + `P3` | `0,008` / `0,059` |
| `F1c` | File 3 `94,08→95,33` / `52,14` | `2 × HEA 200` | `0,85 m` | `2 × S2` | `0,007` / `0,059` |
| `R3-N` | Est `85,71` / `55,84→58,34` | `UPE 200`+B | `1,55 m` | `2 × S1` abouts | `0,291` |
| `R3-S` | Est `85,71` / `50,08→52,58` | `UPE 200`+B | `1,55 m` | `2 × S1` abouts | `0,291` |

**`S1` hors bois.** Quatre sommiers `200 × 400 × 200` sur abouts de mur, **hors emprise** des linteaux bois `E-08`. Aucun sommier sur le bois. Aucun relevé de bois.

---

## 3. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit | **0** |
| Calques `LINTEAU-*` | **10 / 10** |
| Entités `LINTEAU-*` | **131** |
| Blocs | **11** (purge −443) |
| DXF | `975 411 o` |
| Filigrane | oui |
| Cloisons / isolation | **0** |

Script : `_scripts/b60_linteau.py`. Planche : `_plans/FLORA_B60_LINTEAU_EXE_IndA.{dxf,pdf,png}`.

---

## 4. RDL

| Livrable | Indice | Source | Positions | Vue | Date |
|---|---|---|---|---|---|
| `LINTEAU EXE` | **A** | `B-49` A | `B-20` B | `B-32` D | 21/10/2026 |

**Types `B-60` restants :** `MACON` (`D-37`) · `METAL` (`D-36` coulage) · `CHARPENTE` · `ASSEMBLAGE`. `FOND` / `VERT` / `PLANCHER` / `LINTEAU` livrés.
