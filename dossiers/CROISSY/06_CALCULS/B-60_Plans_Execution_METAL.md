# B-60 — PLANS D'EXÉCUTION — type `METAL` — CROISSY-FLORA

> **`D-36` — remplissage `C25/30` des `UPE 200` de `R3` : ACCEPTÉ.** Sans ce béton, `R3-N/S` est **non conforme** (`B-50` `A3`, `τ = 1,40`) — **ne pas poser**.
> **`D-34` — mot pour mot, plan ET note.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission. Reprise chiffrée si non concluants.
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.**
> **`D-37` — coussins `R1`/`F2`/`F3` : PAS ce plan → `B-60 MACON` (livré).**

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`METAL`** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (assemblages → `ASSEMBLAGE` · feu hors lot · `A4` `DOC-09`) |
| **Régime** | **OUTILLÉ** — `_scripts/b60_metal.py` (`V13`) |
| **Fond** | `B-32` Ind. D — **report, jamais redessin** |
| **Amont** | `B-45` A · `D-36` · `B-20` B · `B-32` D |
| **Aval** | `B-62` · `B-60 ASSEMBLAGE` (boulons, platines, scellements) |
| **`COMPLET`** | **INTERDIT** : assemblages non portés · feu non dimensionné · `A4` non chiffré |

**Ce que cette note fait.** Elle implante les **profilés neufs** de `B-45` **sur le fond `B-32`**, aux positions `B-20` (millimètre). Elle porte le **coulage `D-36`** des `UPE 200` de `R3`. Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle n'implante **pas** `F1a/b/c` (LINTEAU livré). Elle ne coule **pas** les coussins (`MACON` livré). Elle ne dimensionne **aucun** assemblage (`10 M16` de `R1`, platines `P1`, scellement `Stab1`) — `B-60 ASSEMBLAGE`. Elle ne dimensionne **aucune** protection au feu.

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `F2` / `F3` / `F4` | `HEB 200` / `HEB 160` / `IPE 200` — poutres neuves |
| `R1` | Moisage `2 × UPE 200` de la poutre bois `20 × 15` |
| `R2-N/S` | `HEB 160` — poutres de refend |
| `R3-N/S` | `UPE 200` + béton `D-36` — linteaux Est (profilés déjà LINTEAU) |
| `P1-N/S` | Tube `140 × 140 × 6,3` sur `SF1` |
| `Stab1` | 4 files `IPE 120` — anti-déversement des `IPE 160` existants |
| `D-36` | Remplissage `C25/30` des `UPE 200` de `R3` — **condition de pose** |
| `R-45-1` | `F3` flèche `0,971` de `L/300` — **aucune charge ajoutée** |

---

## 2. IMPLANTATION (report `B-20`)

| Rép. | Profilé | `L` | `V_Ed` / `N_Ed` | Ratio gouvernant | Appui |
|---|---|---|---|---|---|
| `F2` | `HEB 200` | `2,85 m` | `62,4 kN` | `M 0,252` | coussin `MACON` |
| `F3` | `HEB 160` | `3,85 m` | `61,6 kN` | **`w 0,971`** | coussin `MACON` |
| `F4` | `IPE 200` | `4,88 m` | `11,5 kN` | `M 0,231` | `S1` |
| `R1` | `2 × UPE 200` | `3,85 m` | `77,4 kN` | **`LT 0,880`** | coussin `MACON` |
| `R2-N` | `HEB 160` | `3,82 m` | `46,2 kN` | `M 0,453` | `S1` |
| `R2-S` | `HEB 160` | `3,82 m` | `35,9 kN` | `M 0,352` | `S1` |
| `R3-N/S` | `UPE 200`+B | `1,55 m` | `23,1 kN` | `M 0,291` + **`D-36`** | `S1` abouts |
| `P1-N/S` | `SHS 140×6,3` | `3,00 m` | `100,3 kN` | flamb. `0,123` | platine `200×200` / `SF1` |
| `Stab1` | `IPE 120` ×4 | pas `2,50 m` | `F ≤ 5,8 kN` | `0,016` | voutain — `A4` non chiffré |

**`D-36`.** Béton `C25/30` entre les ailes, **toute la longueur**. `I_T` passe de `9,6×10⁴` à `~10⁷ mm⁴`. Forages de remplissage en semelle supérieure (diamètres / entraxe → `B-62`). Contrôle à réception : béton affleurant, sans vide. **`R-50-2` CLOSE.**

Nuance **`S275`** (`MAT-05f`, `D2` p. 1). Galvanisation `ISO 1461` `70 µm` (`B-45` § 10).

---

## 3. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit | **0** |
| Calques `METAL-*` | **12 / 12** |
| Entités `METAL-*` | **146** |
| Blocs | **11** (purge −443) |
| DXF | `977 886 o` |
| Filigrane | oui |
| Cloisons / isolation | **0** |

Script : `_scripts/b60_metal.py`. Planche : `_plans/FLORA_B60_METAL_EXE_IndA.{dxf,pdf,png}`.

---

## 4. RDL

| Livrable | Indice | Source | Positions | Vue | Date |
|---|---|---|---|---|---|
| `METAL EXE` | **A** | `B-45` A · `D-36` | `B-20` B | `B-32` D | 21/10/2026 |

**Types `B-60` restants :** `CHARPENTE` · `ASSEMBLAGE`. `FOND` / `VERT` / `PLANCHER` / `LINTEAU` / `MACON` / `METAL` livrés.
