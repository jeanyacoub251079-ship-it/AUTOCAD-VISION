# B-60 — PLANS D'EXÉCUTION — type `VERT` — CROISSY-FLORA

> **`D-34` — mot pour mot, plan ET note.** `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa`. Essais hors mission. Reprise chiffrée si non concluants.
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.**
> **`c_nom = 30 mm`** hors fondation (`H-23`, `XA1`). Les `50 mm` restent au type `FOND`.

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`VERT`** — un type par plan |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (nuages `D-19` · `H` hypothèse · `D-34`) |
| **Régime** | **OUTILLÉ** — `_scripts/b60_vert.py` (`V13`) |
| **Fond** | `B-32` Ind. D — **report, jamais redessin** |
| **Amont** | `B-42` B · `B-50` A1 · `B-60` FOND A · `B-30` · `B-32` D |
| **Aval** | `B-62` · `B-60` types suivants · `B-31` / `B-33` |
| **`COMPLET`** | **INTERDIT** : `D-19` non levé, `H` non relevée |

**Ce que cette note fait.** Elle transforme `B-42` Ind. B en **plan d'exécution coté** : `P2`, `P3` et `J1` **implantés sur le fond `B-32`**, sections coffrage + ferraillage en millimètres, coupe de `P2`, `D-34` intégral, nomenclature. Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle ne fusionne **aucun** autre type (`FOND` déjà livré, `PLANCHER`, `MACON`, `METAL`, `LINTEAU`, `CHARPENTE`…). Elle n'implante **pas** `P1-N/S` (acier, `B-45`), ni `R1`/`R2`/`R3`/`F2`/`F3`. Elle ne lève **aucun** nuage `D-19`. Elle ne clôt **pas** `R-42-1` (`H` non relevée). Elle ne dimensionne **aucune** protection incendie.

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `P2` | Poteau BA `150 × 250 mm` sous `F2`, sur `SF1` — **CERTAIN** |
| `P3` | Poteau BA `400 × 500 mm` en refend — pied **`D-19`** |
| `J1` | Jambage BA `240 × 500 mm` en refend — pied **`D-19`** |
| `A1` | Ancrage `6 HA12` équerre dans `SF1` — déjà sur `B-60` FOND |
| `D-19` | Nuage de reconnaissance en fouille |
| `D-34` | `f_k = 1,5 MPa` — essais hors mission |
| `R-42-1` | `H = 2 800 mm` = hypothèse `B-20`, **pas un relevé** |

---

## 2. ENTRÉES

| Entrée | Statut |
|---|---|
| Note `B-42` Ind. B | ✅ `8/8 CONFORME` |
| Vue nettoyée `B-32` Ind. D | ✅ |
| Calage `B-30` | ✅ |
| Ancrage `B-50` A1 / `B-60` FOND | ✅ `l_bd 166 mm` |
| `B-34` réservations | `STR-03` **NON BLOQUANTE** |

**Épuisement (`V14`).** `B-42` B · `B-21` C (`N_Ed`) · `B-50` A1 · `B-60` FOND · `B-40` F (positions) · `B-32` D · `B-30`. Aucune position inventée.

---

## 3. IMPLANTATION (cotes en mm)

| Rép. | `X` / `Y` (m) | Section | Ferraillage | Statut |
|---|---|---|---|---|
| **`P2`** | `95,35` / `59,29` | `150 × 250` | `6 HA12` + `HA8 e150` | **CERTAIN** (sur `SF1`) |
| **`P3`** | `94,09` / `54,89` | `400 × 500` | `6 HA12` + `HA8 e200` | **`D-19`** |
| **`J1`** | `89,78` / `54,52` | `240 × 500` | `6 HA12` + `HA8 e200` | **`D-19`** |

`N_Ed` : `159,0` / `35,8` / `39,8 kN`. Utilisation : `0,305` / `0,013` / `0,015`. **`6 HA12` est imposé par l'espacement maximal**, pas par la résistance.

---

## 4. CE QUE LE PLAN PORTE EN PLUS DE `B-42`

| Disposition | Valeur | Opposable |
|---|---|---|
| Implantation sur `B-32` | 3 fûts cotés | oui |
| `c_nom` | `30 mm` (pas `50`) | oui |
| Ancrage pied `P2` | renvoi `B-60` FOND / `B-50` A1 | oui |
| `H` | `2 800 mm` **HYPOTHÈSE** | porté, `R-42-1` **ouverte** |
| `D-34` | mot pour mot | oui |
| `J1` `σ_d` | `0,332 MPa` — défaut si `f_k < 0,83` | `R-42-3` ouverte |

---

## 5. NOMENCLATURE GRAPHIQUE (façonnage → `B-62`)

| Rép. | Désignation | Section | Qté | Matériau |
|---|---|---|---|---|
| `P2` | Poteau sous `F2` | `150 × 250` | 1 | C25/30 · `6 HA12` · `HA8 e150` |
| `P3` | Poteau refend | `400 × 500` | 1 | C25/30 · `6 HA12` · `HA8 e200` |
| `J1` | Jambage refend | `240 × 500` | 1 | C25/30 · `6 HA12` · `HA8 e200` |
| `HA12` | Longitudinal | HA12 | 18 | S500B |
| `HA8` | Cadres | HA8 | `e150`/`e200` | S500B |

Débits : **indicatifs** (`H` non relevée) → `B-62`.

---

## 6. AUTO-CONTRÔLE DXF (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit ezdxf | **0 erreur** |
| Calques `VERT-*` | **10 / 10** |
| Entités `VERT-*` | **155** |
| Calque `0` (ajouts) | **0** |
| Trois formats | DXF · PNG · PDF |
| Filigrane | `NE PAS EXÉCUTER SANS EXE COTÉ ET VISA` |
| Cloisons / isolation | **0** |

Script : `_scripts/b60_vert.py`. Journal : `_rendus/b60_vert.txt`. Planche : `_plans/FLORA_B60_VERT_EXE_IndA.{dxf,pdf,png}`.

---

## 7. RDL

| Livrable | Indice | Source | Calage | Vue nettoyée | Date |
|---|---|---|---|---|---|
| `VERT EXE` | **A** | `B-42` B | `B-30` | `B-32` D | 21/10/2026 |

**Types `B-60` restants :** `PLANCHER` (dallage sur RDC BAS) · `MACON` (`D-37` coussins) · `METAL` (`D-36` remplissage `R3`) · `CHARPENTE` · `LINTEAU` · `ASSEMBLAGE`. `FOND` livré. `ESCALIER` / `PREDALLE` : SANS OBJET (`D-38`).
