# B-49 — LINTEAUX ET SEUILS — CROISSY-FLORA

> **NOS ÉTUDES SONT RÉALISÉES AVEC LES HYPOTHÈSES `f_k = 1,5 MPa`, `E = 1 500 MPa` ET `f_vk0 = 0,15 MPa`.**
> **LA CONFIRMATION PAR ESSAIS EST HORS DE NOTRE MISSION ET À LA CHARGE DU MAÎTRE D'OUVRAGE.**
> **SI LES ESSAIS NE SONT PAS CONCLUANTS, LA REPRISE DE NOS ÉTUDES FAIT L'OBJET D'UNE PRESTATION COMPLÉMENTAIRE CHIFFRÉE** (`D-34`, 20/10/2026).
> **`D-09` — ARASE −1,00 m / TN MINIMUM** — égalisation par gros béton si écart.
> **`D-28` — AUCUN JOINT DE DILATATION.**
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE** (zone de sismicité 1).
> **`D-36` — remplissage béton `C25/30` des `UPE 200` de `R3` : ACCEPTÉ.**
> **`D-37` — coussin `w_b ≥ 300 mm` sous `R1`, `F2`, `F3` : ACCEPTÉ** (ces trois-là ne sont **pas** des linteaux).

| Champ | Valeur |
|---|---|
| **Brique / famille** | `B-49` — Linteaux et seuils — **famille LINTEAU** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (`SEC-01` non dimensionnée — hors lot GO) |
| **Type** | **Linteau métallique** (5 neufs) · **Seuils BA : SANS OBJET** |
| **Régime** | **OUTILLÉ** — `_scripts/b49_linteaux.py` (`V13`) |
| **Fiche** | `carnac/CARNAC_v3.0/06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md` |
| **Amont** | `B-20` · `B-21` C · `B-23` · `B-24` C (`E-08`) · `B-45` A · `B-46` A |
| **Aval** | `B-50` (aucun scellement nouveau) · `B-60` (implantation `S1` hors bois, coussins `D-37`) |
| **`COMPLET`** | **INTERDIT** (`V12`) : `SEC-01` hors lot |

**Ce que cette note fait.** Elle inventorie **tous** les linteaux du pavillon, applique le **triangle de charge** aux trois linteaux courts `F1a/b/c` (la fiche l'impose : un linteau court n'est pas une poutre longue), confronte le résultat à l'enveloppe déjà vérifiée en `B-45`, confirme `R3` sous charge ponctuelle **avec** le remplissage `D-36`, et **déclare** que les bois existants ne se calculent pas.

**Ce qu'elle ne fait pas.** Elle ne calcule **aucun scellement** (`B-50`). Elle ne dimensionne **aucune protection incendie**. Elle ne calcule **aucun bois existant** : ni `E-08` (court-circuité par `R3`), ni le linteau Ouest `23×15` (soulagé par `P1`) — aucune intervention sur le bois n'est prescrite. Elle ne réduit **aucune** contrainte déjà transmise à `B-46`.

---

## 1. GLOSSAIRE DES CODES

| Code | Objet |
|---|---|
| `F1a` / `F1b` / `F1c` | Frangements `2 × HEA 200` en sous-œuvre de mur porteur — **linteaux neufs** (`D2` f. 01, `MAT-05a`) |
| `R3-N` / `R3-S` | Linteaux de baie `UPE 200` façade Est, remplis `C25/30` (`D-36`) |
| `E-08` | Deux linteaux bois déformés de la façade Est (désordre 1, `B-24`) — **court-circuités** |
| `S1` / `S2` | Sommiers BA `20×40×20` / `20×50×20` (`B-20`) |
| `D-36` | Remplissage béton des `UPE 200` de `R3` — accepté le 21/10/2026 |
| `D-37` | Coussin `w_b ≥ 300 mm` sous `R1`, `F2`, `F3` — accepté le 21/10/2026 |
| `R-46-4` | Sommiers hors emprise des linteaux `E-08` — **close par la présente** |
| `GEO-05` | Nomenclatures de baies (`D4` p. 23–25) — aucun seuil structurel |

---

## 2. INVENTAIRE ET PREUVE D'ÉPUISEMENT (`V14`)

| Réf. | Ouvrage | Section | `L` | Statut |
|---|---|---|---|---|
| **`L1`** | `F1a` — refend central File D | `2 × HEA 200` | `1,00 m` | **NEUF** — `D2` f. 01 |
| **`L2`** | `F1b` — mur Nord hall File 4 | `2 × HEA 200` | `0,90 m` | **NEUF** |
| **`L3`** | `F1c` — mur Sud hall File 3 | `2 × HEA 200` | `0,85 m` | **NEUF** |
| **`L4`** | `R3-N` — façade Est baie Nord | `UPE 200` + béton | `1,55 m` | **NEUF** — `D-36` |
| **`L5`** | `R3-S` — façade Est baie Sud | `UPE 200` + béton | `1,55 m` | **NEUF** — `D-36` |
| `E-08` | 2 linteaux bois, désordre 1 | existant déformé | `1,55 m` | **COURT-CIRCUITÉ** par `R3` |
| — | Linteau bois Ouest `23×15` | existant | `2,52 m` | **SOULAGÉ** par `P1` — hors lot |
| — | Seuils BA | — | — | **SANS OBJET** |

**Épuisement.** `D1` (aucun seuil BA, aucun linteau BA) · `D2` f. 01 (`F1`, `R3`, `P1` sous linteau bois) · `D3` p. 5 (désordre 1) · `D3` p. 16 (linteau Ouest `23×15`) · `D4` p. 23–25 (`GEO-05`) · `B-20` § 4–5 · `B-21` § 5 · `B-23` · `B-24` `E-08` · `B-45` § 4 et § 9 · `B-46` Z2/Z4 · `B-50` `A3`. **Aucun linteau BA. Aucun seuil BA. Aucun linteau maçonnerie neuf.**

---

## 3. `F1a/b/c` — LINTEAUX COURTS : TRIANGLE DE CHARGE

**Méthode (fiche `B-49`, étape 2).** Un linteau dont la portée est inférieure à la hauteur de maçonnerie au-dessus **n'est pas chargé sur toute la hauteur du mur**. La charge de maçonnerie est un **triangle isocèle à 60°** (pratique FR / NF DTU 20.1) :

> `h_Δ = L × √3/2` · `W_k = ½ · L · h_Δ · t · γ` si `h_Δ ≤ H_mur`.
> `M_Ed = W_ELU · L / 6 + p_plan · L² / 8` (triangle + uniforme, appuis simples).

`t = 0,50 m` · `γ = 22 kN/m³` · `H_mur = 3,50 m` (`B-21` § 5) · plancher `p_ELU = 1,35×4,71 + 1,5×2,50 = 10,11 kN/m` (bande `1,00 m`, **sans** coefficient de continuité : le linteau est isostatique).

| Linteau | `L` | `h_Δ` | Triangle formé | `W_k` | `M_Δ` | `M_env` (`B-45`) | Taux Δ | Taux env. |
|---|---|---|---|---|---|---|---|---|
| `F1a` | `1,00 m` | `0,866 m` | **oui** (`< 3,50`) | `4,76 kN` | `2,34 kN·m` | `13,9 kN·m` | **`0,010`** | **`0,059`** |
| `F1b` | `0,90 m` | `0,779 m` | oui | `3,86 kN` | `1,80 kN·m` | `13,9` | **`0,008`** | **`0,059`** |
| `F1c` | `0,85 m` | `0,736 m` | oui | `3,44 kN` | `1,57 kN·m` | `13,9` | **`0,007`** | **`0,059`** |

`M_Rd (2 × HEA 200) = 236,2 kN·m` · `V_Rd = 573,2 kN` (`B-45`, classe 1).

**Deux chiffres, un seul verdict.** Le triangle est la **méthode du linteau court** — c'est elle qui décrit le chemin de charge : la maçonnerie au-dessus du triangle va aux **jambages**, pas au linteau. L'enveloppe `B-45` (`p_ELU = 71,4 kN/m` sur `L_calc = 1,25 m`, mur pleine hauteur) reste l'enveloppe **conservatrice déjà opposable** ; `B-49` ne la réduit pas. Les deux passent. `F1` n'est pas le sujet : la section est **contractuelle** (`D2` f. 01).

**Appui.** Sommier `S2` `20×50×20`, `w_b = 200 mm ≥ 90 mm` (`EC6 § 8.1.6`). `B-46` Z2 : `N_Rdc (β=1) = 60 kN ≥ V_Ed` enveloppe `44,6 kN` — **OK**, coussin `D-37` non requis.

---

## 4. `R3-N` / `R3-S` — CHARGE PONCTUELLE, TORSION CLOSE

`R3` ne porte **aucune charge répartie** (`B-21` § 5) : il reprend la réaction de `R2` à mi-baie.

| Grandeur | Valeur | Origine |
|---|---|---|
| `P_Ed` | `46,2 kN` | Réaction `R2-N` ELU (`B-21` § 5) |
| `L_baie` | `1,55 m` (profilé livré `2,50 m`) | `B-20` |
| `M_Ed = P·L/4` | **`17,9 kN·m`** | script `[3]` |
| `M_Rd` (`UPE 200`, `W_pl`) | `61,6 kN·m` | `B-45` |
| **Taux flexion** | **`0,291`** | `B-45` § 9 — **inchangé** |
| Flèche | `0,9 mm / 6,2 mm` (`L/250`) → `0,144` | script `[3]` |
| Torsion | **CLOSE** — remplissage `C25/30` (`D-36`) | `R-50-2` close |
| Appui | `2 × S1` par linteau, `w_b = 200 mm` | `B-46` Z2 **OK** même en `a₁ = 0` |

Le coussin `D-37` **n'est pas requis** sur `R3`.

---

## 5. `E-08` ET LINTEAU OUEST — PAS DE CALCUL, PAS DE RELEVÉ DE BOIS

**Façade Est, désordre 1** (`D3` p. 5). Deux linteaux bois déformés, **non porteurs**. `B-20` § 5 : `R3-N/S` + `4 × S1` **court-circuitent totalement** ces bois. Les sommiers `S1` tombent sur les **abouts de mur**, hors emprise des linteaux.

> **`R-46-4` est CLOSE.** Aucun sommier n'est censé reposer sur un linteau bois. Le contrôle d'implantation est une **cotation de `B-60`**, pas un sondage de bois. Aucune intervention sur le bois n'est prescrite au CCTP, au `D2` ni au `D4` — donc **aucun relevé n'est demandé**.

**Façade Ouest Sud.** Linteau bois `23×15` (`D3` p. 16), `L = 2,52 m` entre `P1-N` et `P1-S`. `D2` f. 01 : `P1` « en renfort du linteau bois existant » — le bois **reste**, `P1` le soulage. `P1` est un **poteau** (`B-45`, `B-42`), pas un linteau. Pas de relevé.

---

## 6. SEUILS BA — SANS OBJET

`D1` : aucun seuil BA au CCTP GO. `D2` f. 01–04 : aucun seuil coté. `D4` p. 23–25 (`GEO-05`) : nomenclatures de baies, pas de seuil structurel. Le dallage (`B-43`) est désolidarisé `20 mm` — ce n'est pas un seuil.

**Verdict : SANS OBJET.** Réactivable si un seuil porteur est prescrit.

---

## 7. RÉSERVES — EFFETS SUR LE REGISTRE

| Réserve | Effet |
|---|---|
| **`D-37`** (21/10/2026) | Coussin `w_b ≥ 300 mm` sous `R1`, `F2`, `F3` — **accepté**. Exécution `B-60`. |
| **`R-46-1`** (`a₁` de `R1`/`F2`/`F3`) | **CLOSE** : le coussin rend le verdict inconditionnel (`a₁ = 0` admissible). |
| **`R-46-2`** (groupe des unités, `β = 1`) | **CLOSE** pour ces trois appuis : le coussin ne s'appuie pas sur la majoration `β`. |
| **`R-46-4`** (sommiers hors `E-08`) | **CLOSE** : `S1` de `R3` sur abouts de mur (`B-20`). |
| **`R-46-3`** | **Maintenue** (`GEO-03`, `MAT-12`, `PA-01`) — hors linteaux. |
| `R-15` / `R-16` | **Maintenues** — `D-34` fixe l'hypothèse, pas la mesure. |

**Aucun scellement nouveau transmis à `B-50`.** Les efforts d'appui de `F1` et `R3` étaient déjà dans `B-45` § 11 / `B-46` Z2.

---

## 8. AUTO-CONTRÔLE DÉCLARÉ

| Linteau | Vérifications | Verdict | Limite |
|---|---|---|---|
| `F1a` / `F1b` / `F1c` | Triangle 60° + enveloppe `B-45` + appui `EC6 § 8.1.6` | **OK** `0,010` / `0,059` | Section contractuelle, ne pas réduire |
| `R3-N` / `R3-S` | Ponctuel + flexion `B-45` + `D-36` + appui | **OK** `0,291` | Torsion close |
| `E-08` | Court-circuité | **HORS CALCUL** | `R-46-4` close |
| Seuils BA | 0 prescription | **SANS OBJET** | — |

**Points DE PRINCIPE.** Triangle appliqué aux linteaux courts · enveloppe `B-45` non réduite · aucun bois calculé · aucun scellement · pas de feu.

**Points À LEVER.** Aucun sur les cinq linteaux neufs. Implantation `S1` hors bois = cotation `B-60`.

---

## 9. LIVRABLES

| Pièce | Fichier |
|---|---|
| Note | `06_CALCULS/B-49_Linteaux_Seuils.md` |
| Script | `_scripts/b49_linteaux.py` |
| Journal | `_rendus/b49_linteaux.txt` / `.json` |
| Planche | `_plans/FLORA_B49_LINTEAUX_IndA.{dxf,pdf,png}` — calques `LINTEAU-*` · filigrane `NE PAS EXÉCUTER SANS EXE COTÉ ET VISA` · `D-34` en majuscules · audit DXF **0 erreur** |

**Chaîne.** `B-45` / `B-46` → **`B-49` Ind. A** → `B-60` (coussins `D-37`, implantation `S1`) · `B-03` **Ind. AB** (`D-37`, `R-46-1/2/4` closes).
