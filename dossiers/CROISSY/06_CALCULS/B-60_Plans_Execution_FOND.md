# B-60 — PLANS D'EXÉCUTION — type `FOND` — CROISSY-FLORA

> **ENC v3 — PRESCRIPTION FONDATIONS — CROISSY-FLORA — 19/10/2026**
> **Arase inférieure : `−1,00 m / TN MINIMUM`. Jamais une cote fixe. Jamais de remontée.**
> **Semelles ≥ `600 × 600 mm`. Gros béton `C16/20` SOUS la semelle si l'existant est plus profond.**
> **Un plan portant la seule cote `−1,00 m` est INCOMPLET par omission (`D-09` ④, alinéa 12).**
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE. `D-28` — AUCUN JOINT DE DILATATION.**
> **`D-34` — `f_k = 1,5 MPa` · essais hors mission.**

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`FOND`** — un type par plan (fiche : ne pas fusionner) |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (amont `B-40` F · nuages `D-19`) |
| **Titre opposable** | **`PLS`** (`D-11`) |
| **Régime** | **OUTILLÉ** — `_scripts/b60_fond.py` (`V13`) |
| **Fond** | `B-32` Ind. D — **report, jamais redessin** |
| **Amont** | `B-40` F · `B-42` B · `B-50` A (`A1`) · `B-30` · `B-32` D |
| **Aval** | `B-62` (façonnage) · `B-60` types suivants · `B-31` / `B-33` |
| **`COMPLET`** | **INTERDIT** : fouille `D-19` non levée |

**Ce que cette note fait.** Elle transforme `B-40` Ind. F en **plan d'exécution coté** : implantation sur le fond `B-32`, semelles types en millimètres, coupe A-A avec les **attentes `6 HA12`** de `B-50 A1` (équerre, `l_bd 166 mm`, trois conditions `R-50-1`), ENC v3 **intégrale**, nomenclature graphique. Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle ne fusionne **aucun** autre type (`VERT`, `MACON`, `METAL`, `CHARPENTE`…). Elle ne lève **aucun** nuage `D-19`. Elle ne produit **pas** la nomenclature de façonnage (`B-62`). Elle ne dimensionne **aucune** protection incendie. Elle ne corrige **pas** l'écart `R+1`/`RDC` (`D-23` : c'est une donnée).

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| `PLS` | Plan de fondations (`D-11`) — titre obligatoire |
| `SF1` | Semelle isolée `800 × 800 × 250 mm` sous `P2` (`D-30`) |
| `A1` | Ancrage `6 HA12` de `P2` dans `SF1` — `l_bd = 166 mm` (`B-50`) |
| `R-50-1` | Trois conditions cumulatives : équerre, `c_nom 50 mm` 4 faces, cadres jusqu'au lit |
| `ENC v3` | Prescription d'exécution 12 alinéas (`B-02` § 0sexies) |
| `D-19` | Nuages de reconnaissance en fouille (`Z-P1N/S`, `Z-P3`, `Z-J1`) |
| `D-23` | Écart d'aplomb `R+1`/`RDC` `10,1 cm` — **donnée**, non corrigée |

---

## 2. ENTRÉES (étape 1 de la fiche)

| Entrée | Statut |
|---|---|
| Note `B-40` Ind. F | ✅ disponible |
| Vue nettoyée `B-32` Ind. D | ✅ `2 719 320 o` — 0 cloison, 0 isolation |
| Calage `B-30` | ✅ résidu médian `21,0 mm` |
| `B-50 A1` | ✅ `l_bd 166 ≤ 200 mm` |
| `B-34` réservations | `STR-03` **NON BLOQUANTE** — à défaut `PA-xx` |
| `B-33` | aval (phase 6) — n'est pas une entrée bloquante ici |

**Épuisement (`V14`).** `B-40` F · `B-42` B · `B-50` A · `B-02` ENC v3 · `B-03` `D-09` à `D-17`, `D-23`, `D-30` · `B-32` D · `B-30`. Aucune position n'est inventée.

---

## 3. IMPLANTATION (report `B-40`, cotes en mm)

| Repère | `X` / `Y` (m) | Ouvrage | Statut |
|---|---|---|---|
| **`SF1`** | `95,35` / `59,29` | `800 × 800 × 250` C25/30 | **CERTAIN** |
| `Z-P1N` | `95,41` / `49,04` | vérif. moellons ou `600 × 600` | **`D-19`** |
| `Z-P1S` | `95,41` / `47,78` | idem | **`D-19`** |
| `Z-P3` | `94,09` / `54,89` | appui `P3` + GB | **`D-19`** |
| `Z-J1` | `89,78` / `54,52` | appui `J1` + GB | **`D-19`** |
| Bêche | `86,67 → 89,53` / `46,77` | `200 mm × 2 850 mm` | `EXI-07c` |
| RSO passerelle | `87,70 → 93,50` / `63,3 → 64,3` | passes `≤ 1 000 mm` C16/20 | `EXI-07e` |

---

## 4. `SF1` — CE QUE LE PLAN PORTE EN PLUS DE `B-40`

| Disposition | Valeur | Source | Opposable |
|---|---|---|---|
| Attentes | **`6 HA12` équerre** | `B-50 A1` | oui |
| `l_bd` | **`166 mm ≤ 200 mm`** | `B-50` | oui |
| Sans équerre | `l_bd = 237 mm` — **non conforme** | `R-50-1` | oui |
| Cadres | `HA8 e150` **jusqu'au lit inférieur** | `R-50-1` | oui |
| `c_nom` | `50 mm` **4 faces** — non ajustable | `D-06` | oui |
| Lit inf. | `HA8 e150`, 6+6 barres | `B-40` | oui |

**`R-50-1` CLOSE** : les trois conditions sont **sur le plan**, pas seulement dans la note.

---

## 5. NOMENCLATURE GRAPHIQUE (façonnage → `B-62`)

| Rép. | Désignation | Section | Qté | Matériau |
|---|---|---|---|---|
| `SF1` | Semelle isolée | `800 × 800 × 250` | 1 | C25/30 |
| `SF-T` | Type si fouille | `600 × 600 × 300` mini | selon `D-19` | C25/30 |
| `HA8` | Lit + cadres | e150 | 6+6 / `SF1` | S500B |
| `HA12` | Attentes `P2` | équerre, `l_bd 166` | 6 | S500B |
| `GB` | Rattrapage | C16/20 | selon fouille | sous semelle |
| `BP` | Propreté | `50 mm` | sous `SF1` | — |
| Bêche | Réhausse SE | `200 × 2 850` | 1 | C25/30 |
| RSO | Passerelle | passes `≤ 1 000` | 1 zone | C16/20 |

---

## 6. AUTO-CONTRÔLE DXF (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit ezdxf | **0 erreur** |
| Calques `FOND-*` attendus | **11 / 11** — aucun manquant |
| Entités `FOND-*` | **196** |
| Calque `0` (nos ajouts) | **0** |
| Trois formats | DXF `2 756 413 o` · PNG · PDF |
| Filigrane | `NE PAS EXÉCUTER SANS EXE COTÉ ET VISA` |
| Titre `PLS` | oui (`D-11`) |
| ENC v3 | oui (12 alinéas, condensés lisibles) |
| Cloisons / isolation | **0** |

Script : `_scripts/b60_fond.py`. Journal : `_rendus/b60_fond.txt`. Planche : `_plans/FLORA_B60_FOND_EXE_IndA.{dxf,pdf,png}`.

---

## 7. RDL (consignation)

| Livrable | Indice | Source | Calage | Vue nettoyée | Date |
|---|---|---|---|---|---|
| `FOND EXE` / `PLS` | **A** | `B-40` F + `B-50` A1 | `B-30` | `B-32` D | 21/10/2026 |

**Types `B-60` restants :** `VERT` · `PLANCHER` · `CHARPENTE` · `METAL` (`D-36` remplissage `R3`) · `MACON` (`D-37` coussins) · `LINTEAU` · `ASSEMBLAGE`. `ESCALIER` / `PREDALLE` : SANS OBJET (`D-38`).
