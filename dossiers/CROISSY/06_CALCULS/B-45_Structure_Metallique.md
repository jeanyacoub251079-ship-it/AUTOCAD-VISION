# B-45 — STRUCTURE MÉTALLIQUE : PROFILÉS, MOISAGE, ENTRETOISES

> **NOTE OBLIGATOIRE `D-09` — REPRODUITE EN TÊTE DE LA NOTE ET SUR LA PLANCHE :**
> **« AU MÊME NIVEAU QUE LES FONDATIONS EXISTANTES… RAJOUTER DU GROS BÉTON… CETTE NOTE EST À INDIQUER SUR LES PLANS ET NOTE DE CALCULS »** — sans objet direct ici : aucun appui métallique n'est en fondation. La note reste portée pour mémoire, conformément à la règle du dossier.
>
> **`D-28` — AUCUN JOINT DE DILATATION.** Aucun profilé ne traverse un joint : les barres s'appuient de part et d'autre, sans continuité.

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-45** — Structure métallique (profilé de plancher, poutre, poteau, entretoise) |
| Phase | **4 — Calculs d'exécution** (après `B-43`) |
| **Mode d'appel** | **COMPLET** — `MAT-05` (nuance) est **contractuelle** au `D2` p. 1 : **`S275`**. Aucune nuance supposée, donc aucun mode dégradé |
| Régime | **OUTILLÉ (V13)** — calcul intégral par script, journal et JSON conservés |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b45_metal.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b45_metal.txt` (8 846 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b45_metal.json` (5 465 o) |
| Sortie graphique | `_plans/FLORA_B45_METAL_IndA.dxf` (90 972 o · AC1032 · audit **0 erreur**) · `.pdf` (607 970 o) · `.png` (653 396 o) |
| **Indice** | **A** — création de la brique |
| Date | **21/10/2026** |
| Brique suivante | **`B-50`** (assemblages, ancrages, boulonnage du moisage) · **`B-46`** (appuis sur maçonnerie) |

> **Ce que cette brique fait.** Elle vérifie **onze barres** prescrites par le `D2` folio 01 et calculées jusqu'ici en prédimensionnement seulement : trois frangements `F1`, quatre poutres `F2/F3/F4`, trois renforts `R1/R2/R3`, deux poteaux `P1`, quatre files d'entretoises `Stab1`. Classification de section, flexion, cisaillement, interaction `M-V`, **déversement sans maintien supposé**, flèche ELS, flambement, pression diamétrale.
>
> **Ce qu'elle ne fait pas.** **Aucun assemblage n'est calculé** — ni boulon, ni soudure, ni platine, ni tige : c'est `B-50`. **Aucune protection au feu n'est dimensionnée** : mention générique seule. **Aucune nuance n'est inventée** : `S275` est écrit au `D2` p. 1.

---

## 0. RÉPONSE DIRECTE — TOUT PASSE, MAIS DEUX BARRES PASSENT DE JUSTESSE

| Constat | Chiffre | Conséquence |
|---|---|---|
| Barres vérifiées | **11 barres** + 3 familles (`F1a/b/c`, `R2-N/S`, `P1-N/S`) | Toutes conformes à l'ELU et à l'ELS |
| Toutes en **classe 1** | `c/t_f ≤ 7,9` pour `8,3` admis | Résistance **plastique** retenue — c'est le cas favorable, et il est justifié, pas supposé |
| Barre la plus sollicitée en **flexion** | **`F3`** — `0,609` | `HEB 160`, `M_Ed 59,3` pour `97,3 kN·m` |
| Barre la plus sollicitée en **flèche** | **`F3`** — **`0,971`** | **`12,5 mm` pour `12,8 mm` admis.** Il reste **`0,3 mm`** de marge : ce n'est pas une marge, c'est un constat de conformité |
| Barre la plus sollicitée en **déversement** | **`R1`** — **`0,880`** | Le moisage `2 × UPE 200` passe de peu, **sans maintien supposé** |
| Élément le plus confortable | **`F1a/b/c`** — `0,059` | `2 × HEA 200` pour un mur de moellons : **la poutre n'est pas le sujet, le mur l'est** |

**Le résultat qui compte n'est pas « tout est OK » : c'est `F3`.** La flèche de `F3` vaut `97 %` de la limite `L/300`. `B-20` avait écrit « point de vigilance flèche ELS à vérifier en `B-45` » : la vérification le confirme — **la barre est conforme, mais elle n'a aucune réserve**. Toute charge ajoutée sur `F3` la fait sortir. C'est une réserve, pas un slogan.

---

## 1. GLOSSAIRE DES CODES

| Code | Objet en clair |
|---|---|
| `MAT-05f` | Nuance d'acier — **`S275`**, contractuelle (`D2` p. 1) |
| `F1a/b/c` | **Frangements** : poutres `2 × HEA 200` en sous-œuvre de mur porteur |
| `F2 / F3 / F4` | **Poutres** neuves `HEB 200` / `HEB 160` / `IPE 200` |
| `R1` | **Moisage** de la poutre bois `20 × 15` par `2 × UPE 200` boulonnés |
| `R2-N / R2-S` | **Poutres de refend** `HEB 160` sous solivage bois |
| `R3-N / R3-S` | **Linteaux de baie** `UPE 200` sous `R2` |
| `Stab1` | **Entretoises** anti-déversement des `IPE 160` existants, encastrées dans le voutain |
| `P1-N / P1-S` | **Poteaux métalliques** tube carré `140 × 140` |
| `χ_LT` | Coefficient de déversement (EC3 § 6.3.2) — `1,0` = pas de réduction |
| `M_V,Rd` | Moment résistant réduit par l'effort tranchant (EC3 § 6.2.8) |
| `F_Rdu` | Résistance de la zone d'appui sur béton (EC2 § 6.7) |
| `PA`, `R-xx` | Point d'arrêt, réserve — registre `B-03` |

---

## 2. DONNÉES D'ENTRÉE

| Donnée | Valeur | Source | Statut |
|---|---|---|---|
| **Nuance** | **`S275`** — `f_y = 275 MPa`, `f_u = 430 MPa` | `D2` p. 1 · `MAT-05f` | **Contractuelle** |
| `γ_M0` / `γ_M1` | `1,00` / `1,00` | EC3 § 6.1 (NF) | Réglementaire |
| Sections | `2×HEA 200`, `HEB 200`, `HEB 160`, `IPE 200`, `2×UPE 200`, `UPE 200`, `SHS 140×140×6,3`, `IPE 120` | `D2` f. 01 · `MAT-05a` à `e` | **Contractuelles** |
| Charges `p_ELS` / `p_ELU` | `B-21 Ind. C` § 5 | `B-21` | **Contractuelles** |
| `N_ELU` des poteaux | `100,3 kN` | `B-21` § 6 | **Contractuelle** |
| Portées | `1,25` à `4,88 m` | `B-20` § 3 (mesures `D5`/`D4`) | **Contractuelles** |
| Propriétés de section | EN 10365 · tube calculé | Tables normalisées | Réglementaire |

**Écart assumé et déclaré :** `IPE 330` — la poutre du plancher B — **n'est pas calculée ici**. C'est un **ouvrage existant** : sa vérification relève de `B-24` (mode paramétrique) puis `B-46` si un sondage est disponible. `B-45` ne calcule que des profilés **neufs** posés par nos plans, plus les entretoises `Stab1` qui **maintiennent** un ouvrage existant.

---

## 3. CLASSIFICATION DE SECTION — EC3 § 5.5, AVANT TOUT CALCUL

`ε = √(235/275) = 0,924` · semelle en console : `9ε / 10ε / 14ε` = `8,3 / 9,2 / 12,9` · âme fléchie : `72ε / 83ε / 124ε` = `66,5 / 76,7 / 114,6`.

| Barre | Profilé | `c/t_f` | Limite cl. 1 | `d/t_w` | Limite cl. 1 | **Classe** |
|---|---|---|---|---|---|---|
| `F1a/b/c` | `2 × HEA 200` | `7,9` | `8,3` | `20,6` | `66,5` | **1** |
| `F2` | `HEB 200` | `5,2` | `8,3` | `14,9` | `66,5` | **1** |
| `F3`, `R2-N`, `R2-S` | `HEB 160` | `4,7` | `8,3` | `13,0` | `66,5` | **1** |
| `F4` | `IPE 200` | `4,1` | `8,3` | `28,4` | `66,5` | **1** |
| `R1` | `2 × UPE 200` | `2,1` | `8,3` | `23,2` | `66,5` | **1** |
| `R3-N/S` | `UPE 200` | `2,1` | `8,3` | `23,2` | `66,5` | **1** |

**Le `c/t_f` de `HEA 200` vaut `7,9` pour `8,3` admis : la classe 1 tient à `5 %`.** C'est le seul endroit où la classe aurait pu basculer en classe 2 — et une classe 2 aurait imposé `W_pl` identique, donc **aucun changement de résultat** pour la flexion. La vérification est faite avant le calcul, comme elle doit l'être, et elle est écrite.

---

## 4. FLEXION ET CISAILLEMENT — EC3 § 6.2.5 et § 6.2.6

`M_Ed = p_ELU · L² / 8` · `V_Ed = p_ELU · L / 2` · `M_c,Rd = W_pl f_y / γ_M0` (classe 1) · `V_pl,Rd = A_v f_y / (√3 γ_M0)`.

| Barre | `L` (m) | `p_ELU` (kN/m) | `M_Ed` (kN·m) | `M_Rd` (kN·m) | **Ratio** | `V_Ed` (kN) | `V_Rd` (kN) | **Ratio** |
|---|---|---|---|---|---|---|---|---|
| `F1a/b/c` | 1,25 | 71,4 | `13,9` | `236,2` | **`0,059`** | `44,6` | `573,2` | `0,078` |
| `F2` | 2,85 | 43,8 | `44,5` | `176,7` | **`0,252`** | `62,4` | `394,5` | `0,158` |
| **`F3`** | 3,85 | 32,0 | `59,3` | `97,3` | **`0,609`** | `61,6` | `94,3` | **`0,653`** |
| `F4` | 4,88 | 4,7 | `14,0` | `60,7` | **`0,231`** | `11,5` | `222,5` | `0,052` |
| **`R1`** | 3,85 | 40,2 | `74,5` | `123,2` | **`0,605`** | `77,4` | `439,4` | `0,176` |
| `R2-N` | 3,82 | 24,2 | `44,1` | `97,3` | **`0,453`** | `46,2` | `94,3` | `0,490` |
| `R2-S` | 3,82 | 18,8 | `34,3` | `97,3` | **`0,352`** | `35,9` | `94,3` | `0,381` |

**Interaction `M-V` (EC3 § 6.2.8) : déclenchée pour `F3` seulement.** `V_Ed = 61,6 kN > 0,5 V_pl,Rd = 47,2 kN` ⇒ `ρ = (2 × 0,653 − 1)² = 0,094` ⇒ `M_V,Rd = 97,3 × (1 − 0,094) =` **`88,2 kN·m`** ⇒ **`M_Ed / M_V,Rd = 0,672`** (contre `0,609` sans interaction). C'est le second point où `F3` se distingue : elle est la seule barre **cisaillée au-delà de la moitié** de sa résistance.

> **Sur `F1a/b/c` : `0,059`. Ce n'est pas une erreur de calcul, c'est une prescription.** `2 × HEA 200` en sous-œuvre de `1,25 m` est massivement surabondant — mais la section est **contractuelle** (`D2` f. 01). La réduire obligerait à une décision ; la note ne la prend pas à votre place, elle **signale** que `F1` est gouverné par le **mur**, pas par la poutre (`38,5 kN/m` de maçonnerie sur `45,7`, soit 84 %).

---

## 5. DÉVERSEMENT — EC3 § 6.3.2 — LE MAINTIEN N'EST JAMAIS SUPPOSÉ

**Hypothèse retenue : `L_cr = L`, aucune entretoise comptée, aucune collaboration du plancher.** C'est la position la plus défavorable possible, et elle est tenue pour **toutes** les barres. Si le maintien réel l'améliore, le résultat reste vrai.

`M_cr = C₁ π²EI_z/L² · √(I_w/I_z + L²GI_T/(π²EI_z))` avec `C₁ = 1,13` (charge répartie, appuis simples) · `λ̄_LT = √(W_el f_y / M_cr)` · courbes **a** (HE, `h/b ≤ 2`), **b** (IPE), **c** (`U`, par prudence — la courbe réelle d'un U est meilleure, on ne s'en sert pas).

| Barre | `L_cr` (m) | `M_cr` (kN·m) | `λ̄_LT` | `χ_LT` | `M_b,Rd` (kN·m) | **Ratio** |
|---|---|---|---|---|---|---|
| `F1a/b/c` | 1,25 | `34 228` | `0,079` | `1,000` | `213,9` | `0,065` |
| `F2` | 2,85 | `5 381` | `0,171` | `1,000` | `156,6` | `0,284` |
| **`F3`** | 3,85 | `1 051` | `0,285` | `0,981` | `84,0` | **`0,706`** |
| `F4` | 4,88 | `137` | `0,624` | `0,825` | `44,1` | `0,318` |
| **`R1`** | 3,85 | `328` | `0,566` | `0,805` | `84,6` | **`0,880`** |
| `R2-N` | 3,82 | `1 068` | `0,283` | `0,981` | `84,1` | `0,525` |
| `R2-S` | 3,82 | `1 068` | `0,283` | `0,981` | `84,1` | `0,408` |

**Deux enseignements, et le second est contre-intuitif.**

1. **`R1` est la barre la plus sensible au déversement** (`χ_LT = 0,805`) : un `UPE` a un `I_T` faible et un `I_w` quasi nul — c'est le profilé qui pardonne le moins l'absence de maintien. Le ratio `0,880` **reste conforme** parce que le moisage est boulonné sur la poutre bois, ce qui maintient la semelle — mais la note **ne compte pas ce maintien** : elle vérifie d'abord sans lui.
2. **Le diagnostic disait les `IPE 160` instables au déversement ; les profilés neufs, eux, ne le sont pas** — parce qu'ils sont courts (`L ≤ 4,88 m`) et massifs. La pathologie de l'existant ne se transpose pas aux renforts : c'est précisément pourquoi `Stab1` traite l'existant (§ 7) et pas le neuf.

---

## 6. FLÈCHE ELS — LE POINT DUR EST `F3`

`w = 5 p_ELS L⁴ / (384 E I_y)` · `E = 210 000 MPa`.

| Barre | `L` (m) | `w` (mm) | Limite | `w_lim` (mm) | **Ratio** | Verdict |
|---|---|---|---|---|---|---|
| `F1a/b/c` | 1,25 | `0,1` | `L/300` | `4,2` | `0,026` | ✅ |
| `F2` | 2,85 | `2,2` | `L/300` | `9,5` | `0,237` | ✅ |
| **`F3`** | 3,85 | **`12,5`** | `L/300` | **`12,8`** | **`0,971`** | ⚠️ **conforme, sans marge** |
| `F4` | 4,88 | `6,0` | `L/250` | `19,5` | `0,306` | ✅ |
| **`R1`** | 3,85 | `10,2` | `L/350` | `11,0` | **`0,927`** | ⚠️ conforme, peu de marge |
| `R2-N` | 3,82 | `9,1` | `L/350` | `10,9` | `0,835` | ✅ |
| `R2-S` | 3,82 | `7,1` | `L/350` | `10,9` | `0,650` | ✅ |

**Justification des limites, barre par barre** — ce n'est pas un choix esthétique :

- **`L/300`** pour `F2`, `F3` (planchers courants portant des cloisons) : limite usuelle pour éviter la fissuration des cloisons.
- **`L/250`** pour `F4` (sous toiture, sans cloison portée).
- **`L/350`** pour `R1`, `R2` : ces barres **supportent un plancher bois existant déjà fléchi** (`72,8 mm` consommés sur la poutre `20 × 15`). Une flèche ajoutée de `L/300` s'**additionnerait** à la flèche existante ; on resserre donc la limite pour ne pas aggraver un désordre déclaré.

> **`F3` à `0,971` : la phrase qu'il faut écrire.** La barre est **conforme**. Elle l'est de `0,3 mm`. Ce n'est pas une marge de sécurité, c'est un **constat de conformité à la limite près**. Conséquence pratique : **aucune charge ne peut être ajoutée sur `F3` sans rouvrir cette note**. C'est l'objet de la réserve `R-45-1`.

---

## 7. POTEAUX `P1-N / P1-S` — FLAMBEMENT EC3 § 6.3.1

Tube carré `140 × 140 × 6,3` — `A = 33,7 cm²`, `i = 54,6 mm` (calculé, pas tabulé).

| Grandeur | Valeur |
|---|---|
| `N_Ed` | **`100,3 kN`** (`B-21` § 6) |
| `L_cr` | `3,00 m` (articulé-articulé) |
| `λ = L_cr / i` | `54,9` |
| `λ̄ = λ / (93,9 ε)` | `0,633` |
| Courbe (tube formé à chaud, `h/b = 1`) | **a** → `χ = 0,877` |
| `N_b,Rd` | **`812,8 kN`** |
| **Taux** | **`0,123`** |

**L'épaisseur est tranchée : `6,3 mm`.** `B-20` laissait ouvert « `10 mm` ou `6,3 mm` mini ». À `6,3 mm`, le taux vaut `0,123` — l'épaisseur `10 mm` serait un gaspillage de `60 %` de matière sur un poteau qui n'utilise qu'un huitième de sa capacité. **Retenu : `6,3 mm`**, à condition que la nuance soit bien `S275` et que la corrosion soit traitée (§ 10).

---

## 8. `Stab1` — ENTRETOISES : LE CALCUL QUI NE DÉPEND PAS D'UNE DONNÉE MANQUANTE

**Le problème posé.** Les `IPE 160` existants sont **instables au déversement** au diagnostic (`D3` p. 12). Il faut les maintenir. Mais **aucune pièce n'écrit leur portée** — c'est un ouvrage existant, sa géométrie relève de `B-46`.

**La réponse : calculer sur un intervalle, et choisir le profilé qui couvre tout l'intervalle.** Effort de stabilisation `F_stab = 2,5 %` de l'effort de semelle comprimée `N_f = M / (h − t_f)`, avec `p_ELU = 10,11 × 0,72 = 7,28 kN/m` (`B-43` zone B).

| `L` supposée (m) | `M` (kN·m) | `N_f` (kN) | **`F_stab` (kN)** | `N_b,Rd` `IPE 120` (kN) | Taux |
|---|---|---|---|---|---|
| 2,50 | 5,7 | 50,0 | `1,25` | `363,3` | `0,003` |
| 3,00 | 8,2 | 72,0 | `1,80` | `363,3` | `0,005` |
| 3,60 | 11,8 | 103,7 | `2,59` | `363,3` | `0,007` |
| 4,20 | 16,1 | 141,2 | `3,53` | `363,3` | `0,010` |
| 4,80 | 21,0 | 184,4 | `4,61` | `363,3` | `0,013` |
| **5,40** | 26,5 | 233,4 | **`5,83`** | `363,3` | `0,016` |

**`IPE 120` retenu.** À `L = 5,40 m` — au-delà de toute portée plausible pour un plancher de ce bâtiment — l'effort reste **`5,83 kN` pour `363,3 kN` disponibles**. **La portée inconnue des `IPE 160` ne bloque donc pas `Stab1`** : c'est exactement ce qu'une note doit faire d'une donnée manquante quand elle peut s'en affranchir, plutôt que de la réclamer.

**Ce qui est transmis à `B-50` : `5,8 kN` par file**, en enveloppe. Le mode de fixation dans le voutain (saignée ponctuelle, `D2` f. 01) relève de `B-50`.

---

## 9. `R3-N / R3-S` — LINTEAUX : CONFORMES EN FLEXION, DÉFAILLANTS EN TORSION

`P_Ed = 46,2 kN` à mi-portée (`B-21` § 5) · `L_baie = 1,55 m` · `M_Ed = P·L/4`.

| Vérification | Valeur | Résistance | Taux |
|---|---|---|---|
| Flexion `M_Ed` | `17,9 kN·m` | `61,6 kN·m` | **`0,291`** ✅ |
| Cisaillement | `23,1 kN` | `452,5 kN` | `0,051` ✅ |
| Flèche (ponctuelle) | `0,89 mm` | `6,2 mm` (`L/250`) | `0,144` ✅ |
| **Torsion d'excentrement** | **`M_t = 1,85 kN·m`** | **non reprise par le `U` seul** | ⚠️ **à traiter** |

> **Ce que le calcul de flexion ne voit pas.** Un `UPE` est un profilé **asymétrique** : son axe de cisaillement est décalé de `40 mm` de l'axe de l'âme. La charge de `R2` appliquée sur l'axe de l'âme crée donc un moment de torsion `M_t = 46,2 × 0,040 = 1,85 kN·m` que **la vérification en flexion ignore complètement**. Trois issues, et **`B-45` n'en choisit aucune** : remplissage béton entre les ailes, platine de répartition soudée, ou reprise par le hourdis. **`B-50` tranche et chiffre.** Ce n'est pas un défaut de la note : c'est la frontière assumée entre le profilé et l'assemblage.

---

## 10. DISPOSITIONS CONSTRUCTIVES

| Sujet | Prescription |
|---|---|
| **Maintien latéral** | `IPE 160` existants → `Stab1`, 4 files, pas `2,50 m`, `F ≤ 5,8 kN`/file |
| **Moisage `R1`** | Le boulonnage assure **deux fonctions** : solidarisation acier/bois **et** maintien latéral de la semelle. Les deux sont chiffrées pour `B-50` |
| **Harnais de serrage** | **Interdit sur bois sec** : risque d'écrasement des fibres et de perte de précontrainte. Rondelles larges obligatoires (planche) |
| **Anticorrosion** | **Galvanisation à chaud `NF EN ISO 1461`**, `70 µm` minimum. En œuvre, si la galvanisation est impossible : peinture classe `C3` |
| **Réservations** | Aucune trémie dans les semelles. Les saignées `Stab1` sont **ponctuelles** dans le voutain (`D2` f. 01) |
| **Appuis sur maçonnerie** | `F1`, `F2`, `F3`, `F4`, `R1`, `R2`, `R3` : **`f_k` n'est pas mesuré** → `B-46` (`D-34`, `R-15`) |
| **Appui sur béton** | `P1` sur `SF1` : pression diamétrale EC2 § 6.7 ci-dessous |
| **Protection au feu** | **NON dimensionnée** — hors lot GO, mention seule |
| **Sismique** | **Sans objet** — `D-26`, zone de sismicité 1 |

### 10.1 Pression diamétrale sur béton — EC2 § 6.7

Seul appui métallique **sur béton** du lot : `P1-N/P1-S` sur `SF1` (`B-40`).

| Grandeur | Valeur |
|---|---|
| `N_Ed` | `100,3 kN` |
| Platine | `200 × 200 mm` → `A_c0 = 400 cm²` |
| `f_cd` (`C25/30`) | `0,85 × 25 / 1,5 = 14,17 MPa` |
| `F_Rdu = 1,5 f_cd A_c0` | **`850 kN`** |
| `σ_c = N_Ed / A_c0` | **`2,51 MPa`** |
| **Taux** | **`0,118`** ✅ |

`F1` à `R3` s'appuient sur **maçonnerie**, pas sur béton : la contrainte d'appui correspondante relève de `f_k` et appartient à `B-46`.

---

## 11. EFFORTS AUX ASSEMBLAGES — TRANSMIS À `B-50`

| Nœud / appui | Nature | `N_Ed` | `V_Ed` | `M_Ed` | Note |
|---|---|---|---|---|---|
| `F1a/b/c` — 2 appuis | Platine sur maçonnerie | — | **`44,6 kN`** | — | Réaction d'about |
| `F2` — 2 appuis | Platine sur maçonnerie | — | `62,4 kN` | — | + charge `F4` |
| `F3` — 2 appuis | Platine sur maçonnerie | — | `61,6 kN` | — | **`V_Ed = 0,653 V_pl,Rd`** |
| `F4` — 2 appuis | Platine sur maçonnerie | — | `11,5 kN` | — | — |
| `R1` — 2 appuis + **boulonnage bois** | **Moisage boulonné** | — | `77,4 kN` | `74,5 kN·m` | **Glissement + maintien latéral** |
| `R2-N/S` — 2 appuis | Platine sur maçonnerie | — | `46,2` / `35,9 kN` | — | Réaction = charge de `R3` |
| `R3-N/S` — 2 appuis | Platine sur maçonnerie | — | `23,1 kN` | **`M_t = 1,85 kN·m`** | **Torsion à reprendre** |
| `P1-N/S` — pied + tête | Platine boulonnée sur `SF1` | **`100,3 kN`** | — | — | Pression diamétrale `0,118` |
| **`Stab1` — 4 files** | **Encastrement dans voutain** | **`5,8 kN`** | — | — | Effort de stabilisation |

**Aucun boulon, aucune soudure, aucune platine n'est dimensionné ici.** `B-45` fournit les efforts et la nature de l'assemblage ; `B-50` choisit et vérifie.

---

## 12. AUTO-CONTRÔLE — ONZE POINTS, DÉCLARÉS

| # | Point de la fiche `B-45` | Verdict | Preuve / limite |
|---|---|---|---|
| 1 | Chaque donnée d'entrée vient de la FDC | ✅ **CONFORME** | § 2 — `MAT-05a` à `f`, `D2` f. 01 et p. 1, `B-21` |
| 2 | Chaque profilé a sa classification EC3 § 5.5 | ✅ **CONFORME** | § 3 — 7 profilés, tous **classe 1** |
| 3 | Flexion, cisaillement | ✅ **CONFORME** | § 4 — max `0,653` (`F3`, cisaillement) |
| 4 | Interaction `M-V` si `V_Ed > 0,5 V_pl,Rd` | ✅ **CONFORME** | § 4 — `F3` : `M_V,Rd = 88,2` → `0,672` |
| 5 | Flambement des éléments comprimés | ✅ **CONFORME** | § 7 — `P1` `0,123` |
| 6 | Déversement si semelle non maintenue | ✅ **CONFORME** | § 5 — **toutes** les barres vérifiées **sans maintien** ; max `0,880` (`R1`) |
| 7 | Flèche ELS | ⚠️ **CONFORME, MAIS SERVI** | § 6 — `F3` à **`0,971`**. Conforme, sans marge → `R-45-1` |
| 8 | Maintien latéral justifié, pas supposé | ✅ **CONFORME** | § 5 — hypothèse défavorable tenue ; `Stab1` chiffrée § 8 |
| 9 | Chaque nœud a ses efforts transmis à `B-50` | ✅ **CONFORME** | § 11 — 9 nœuds |
| 10 | Pression diamétrale EC2 § 6.7 | ✅ **CONFORME** | § 10.1 — `0,118` |
| 11 | Planche : filigrane, indice, mode, mention incendie | ✅ **CONFORME** | `FLORA_B45_METAL_IndA` — audit `0 erreur` |
| — | Aucune protection au feu dimensionnée | ✅ **CONFORME** | Mention seule (§ 10) |
| — | **`IPE 330` (ouvrage existant) calculé** | ⛔ **NON — ET C'EST VOLONTAIRE** | Existant non sondé → `B-24` puis `B-46`. Le calculer ici serait inventer sa géométrie |

**Verdict : 10 conformes, 1 conforme mais servi, 1 exclusion déclarée.** La brique n'est pas « 11/11 » : `F3` passe à `3 %` de la limite de flèche, et l'`IPE 330` n'est pas calculée parce qu'elle est existante.

---

## 13. TRANSMISSIONS ET RÉSERVES

### 13.1 Ce que `B-45` transmet

| Brique | Ce qu'elle reçoit |
|---|---|
| **`B-50`** | § 11 — efforts et **nature** d'assemblage des 9 nœuds · `M_t = 1,85 kN·m` sur `R3` · `F_stab = 5,8 kN` sur `Stab1` · boulonnage du moisage `R1` (glissement + maintien) |
| **`B-46`** | Réactions d'appui sur **maçonnerie** : `44,6` / `62,4` / `61,6` / `11,5` / `77,4` / `46,2` / `35,9` / `23,1 kN` — à confronter à `f_k` |
| **`B-60`** | Planche `FLORA_B45_METAL_IndA` — principes et tableau de synthèse opposables ; **cotes de pose restent à produire** |
| **`B-03`** | `R-45-1` à `R-45-3` |

### 13.2 Réserves nées de cette brique

| Réf. | Objet | Conséquence si non levée | Destinataire |
|---|---|---|---|
| **`R-45-1`** | **`F3` sans réserve de flèche** — `0,971` de `L/300` | Toute charge ajoutée sur `F3` (équipement lourd, salle de sport `C4` à `5,00 kN/m²` si elle tombe dans sa bande) fait sortir la barre. Il faudra **changer la section ou ajouter un appui** — les deux sont des décisions, pas des calculs | MOE · `B-46` |
| **`R-45-2`** | **`R1` à `0,880` en déversement** sans maintien | Si le boulonnage prévu par `B-50` ne maintient pas réellement la semelle, le ratio reste conforme mais la marge disparaît. `B-50` doit **concevoir** le maintien, pas seulement le boulon | `B-50` |
| **`R-45-3`** | **Torsion du `UPE 200` (`R3`)** — `1,85 kN·m` non reprise | Sans remplissage béton ni platine de répartition, le linteau travaille en torsion pure sur une section ouverte : **risque réel**, même si la flexion passe à `0,291` | `B-50` |

### 13.3 Ce que `B-45` ne demande pas

- **Rien sur l'`IPE 330`** : ouvrage existant, `B-24`/`B-46` en ont la charge.
- **Rien sur la portée des `IPE 160`** : `Stab1` couvre l'intervalle entier (`§ 8`).
- **Rien sur la protection au feu** : hors lot GO.

---

## 14. POINT DE CONTRÔLE HUMAIN

**Une question, et une seule, engage une décision :**

1. **`F3` tient à `3 %` de la limite de flèche.** Acceptez-vous cette conformité sans marge, ou demandez-vous un renfort (section supérieure ou appui intermédiaire) ? C'est une décision de maîtrise d'ouvrage : la note ne peut pas la prendre, parce qu'elle change la prescription du `D2`.

**Deux informations utiles, non bloquantes :** la **salle de sport en `C4` (`5,00 kN/m²`)** — si sa surface tombe dans la bande de `F3`, la barre ne passe plus et `R-45-1` devient bloquante ; et le **classement termites** (`SEC-03`), sans effet sur l'acier.

**Brique `B-45` livrée en indice A — en attente de votre `GO` ou de vos observations.**
