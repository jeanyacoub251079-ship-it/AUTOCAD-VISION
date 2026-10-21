# B-60 — PLANS D'EXÉCUTION — type `CHARPENTE` — CROISSY-FLORA

> **`D-34` — mot pour mot, plan ET note.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission. Reprise chiffrée si non concluants.
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION. `D-38` — pas de pieu, pas de prédalle.**
> **`E-07` NON CHARGÉ.** `PA-03` **reste ouvert** (`B-43`). Ne pas clore.

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`CHARPENTE`** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (`H-29` · existant hors calcul · `PA-03` ouvert) |
| **Régime** | **OUTILLÉ** — `_scripts/b60_charpente.py` (`V13`) |
| **Fond** | `B-32` Ind. D **R+1** — **report, jamais redessin** |
| **Amont** | `B-44` A · `B-20` B (planche 3) · `B-32` D |
| **Aval** | `B-62` · `B-60 ASSEMBLAGE` (sabots, ancrages) |
| **`COMPLET`** | **INTERDIT** : `E-05/06` non sondés · `ZN1/ZN2` · feu hors lot |

**Ce que cette note fait.** Elle implante les **bois neufs** de `B-44` **sur le fond `B-32` R+1**, aux positions `B-20` (millimètre, `DY = −3 726 cm`). Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle ne calcule **aucun** existant (`E-04` supprimés, `E-05`/`E-06` → `B-24`). Elle ne charge **pas** `E-07`. Elle n'invente **aucun** contreventement de toiture (absent au `D2`). Elle ne dimensionne **aucun** assemblage.

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `PN1/2/3` | Pannes neuves `75 × 200 C24` |
| `DF1/DF2` | Demi-fermes : arb. `100 × 200` + entrait `75 × 200` — **désolidarisées** |
| `CF` | Contrefiches `75 × 225 C24` — **après purge** `E-05` |
| `E-07` | Plancher haut — **non chargé** |
| `PA-03` | Sondage `E-07` — **reste ouvert** |
| `ZN1/ZN2` | Zones non relevées — nuage `D-19`, aucun calcul |

---

## 2. IMPLANTATION (report `B-20` R+1)

| Rép. | Section | `L` | Taux | Note |
|---|---|---|---|---|
| `PN1/2/3` | `75 × 200 C24` | `3,20 m` | **`0,830`** (flèche) | entraxe `1,60 m` |
| `DF-arb` | `100 × 200 C24` | `3,62 m` | **`0,626`** (flambement) | `N = 31,72 kN` |
| `DF-ent` | `75 × 200 C24` | `3,20 m` | **`0,108`** (traction) | `N = 14,00 kN` |
| `CF` | `75 × 225 C24` | `2,62 m` | **`0,940`** (flambement) | **après purge** |

Classe **`C24`** = spécification. Service **2** (`MAT-08`). Appuis des `DF` : murs Files A et C (`V = 14,89 kN`) — sabots → `ASSEMBLAGE`.

**Phasage `E-04`.** 1. Pose `DF`. 2. Reprise pannes. 3. Dépose potelets. Inverse **interdit**.
**Phasage `E-05`.** 1. Purge. 2. Traitement. 3. Pose `CF`. Inverse **interdit**.

---

## 3. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit | **0** |
| Calques `CHARPENTE-*` | **11 / 11** |
| Entités `CHARPENTE-*` | **263** |
| Blocs | **7** (purge −447) |
| DXF | `974 250 o` |
| Filigrane | oui |
| Cloisons / isolation | **0** |
| `PA-03` | **ouvert** |

Script : `_scripts/b60_charpente.py`. Planche : `_plans/FLORA_B60_CHARPENTE_EXE_IndA.{dxf,pdf,png}`.

---

## 4. RDL

| Livrable | Indice | Source | Positions | Vue | Date |
|---|---|---|---|---|---|
| `CHARPENTE EXE` | **A** | `B-44` A | `B-20` B pl. 3 | `B-32` D R+1 | 21/10/2026 |

**Types `B-60` restants :** `ASSEMBLAGE`. `FOND` / `VERT` / `PLANCHER` / `LINTEAU` / `MACON` / `METAL` / `CHARPENTE` livrés.
