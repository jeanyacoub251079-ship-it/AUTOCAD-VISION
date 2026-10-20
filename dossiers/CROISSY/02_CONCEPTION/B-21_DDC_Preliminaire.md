# B-21 — DDC PRÉLIMINAIRE — CONCEPTION

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-21** — Descente de charges préliminaire |
| Phase | **3 — Conception et synthèse structurelle** (`B-20` → **`B-21`** → `B-22`) |
| **Mode d'appel** | **HYPOTHÈSE-NOTIFIÉE** — `CHG-03` (poids propres) et `CHG-04` (toiture) ne sont pas fournis par le marché ; `CHG-02` est en conflit entre deux pièces. Traités par `H-28` à `H-31` |
| Régime | **OUTILLÉ (V13)** — calcul intégral par script, journal d'exécution conservé |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b21_ddc.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b21_ddc.txt` (12 239 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b21_ddc.json` (10 120 o) |
| Sortie graphique | **Aucune** — la fiche `B-21` n'exige aucun livrable graphique |
| **Indice** | **A** — création de la brique |
| Date | **20/10/2026** |
| Brique suivante | **`B-22`** (note d'hypothèses consolidée), puis `B-40` à `B-50` |

> **Titre opposable : DDC PRÉLIMINAIRE — CONCEPTION.**
> Cette note sert à **choisir et contrôler les sections en conception**. Elle **ne remplace pas** les DDC d'exécution des briques `B-40` à `B-50`, qui refont le calcul sur les schémas statiques réels, avec les surfaces d'influence exactes et les coefficients de continuité issus du schéma.
> **Aucune vérification de section et aucun ferraillage ne sont produits ici.** Les effets de charge sont calculés ; leur comparaison à une résistance appartient aux briques de calcul.

---

## 0. RÉPONSE DIRECTE — CE QUE LA DDC CHANGE DANS LE DOSSIER

Quatre résultats sortent de cette brique, et trois d'entre eux **contredisent le prédimensionnement de `B-20`**.

| # | Constat | Chiffre | Conséquence |
|---|---|---|---|
| **1** | **La recharge de sol de 15 cm change tout le plancher B.** `D4 p. 5 et 14` prescrit « sol à recharger de 15 cm » ; `D2` ne la compte pas | `+3,30 kN/m²` sur **toute** la surface du plancher B, soit `g = 8,01 kN/m²` au lieu de `3,50` | `F3`, `F2`, `R1`, `R2` reçoivent **+28 % à +126 %** d'effet de charge par rapport à `B-20` |
| **2** | **`F3 (HEB 160)` dépasse de 109 % l'effet de charge utilisé pour son prédimensionnement** | `M_Ed` passe de `40,8` à **`85,3 kN·m`** | `B-45` doit reprendre `F3` **en priorité** — le point de vigilance annoncé par `B-20` n'était pas une flèche, c'est un moment |
| **3** | **`R1 (2×UPE 200)` dépasse de 126 %** — mais il partage la charge avec la poutre bois `20×15` qu'il moisit | `M_Ed` passe de `47,5` à **`107,2 kN·m`** | `B-45` doit établir la **répartition moisage/bois**, jamais faite jusqu'ici |
| **4** | **`SF1` (60 × 60) est insuffisante** si l'aire d'influence de `P2` est celle de la trame | `N_ELS = 180,5 kN` → `σ = 0,50 MPa` **> 0,30 MPa** | `B-40` doit passer en **80 × 80**, ou justifier une aire d'influence réduite |

**Le reste est confortable :** les voiles travaillent à `σ_d = 0,094 MPa` (l'hypothèse `H-27` de `B-25` en retenait `0,300` — elle est donc **conservatrice de 69 %**), les poteaux BA `P3` et `J1` sont sous `45 kN`, et les poutres `F1a/b/c` et `F4` sont **cohérentes** avec `B-20`.

---

## 1. DONNÉES D'ENTRÉE ET STATUT

| Variable | Valeur | Source | Statut |
|---|---|---|---|
| `CHG-01a` Programme RDC | Plateau technique 33,14 · Box kiné 11,20 / 9,60 / 9,15 · Bureaux 16,08 / 12,80 · Sanitaire PMR 5,19 | D4 p. 6 et 9 | **Contractuelle** |
| `CHG-01b` Programme R+1 | **Salle de sport 34,25** · Salle commune 11,75 · Vestiaire 9,32 · Douche 2,37 · Bureaux consult. 13,26 / 16,50 · Dégagement 5,96 · Attente 8,38 | D4 p. 6 et 9 | **Contractuelle** |
| `CHG-02` Exploitation | **2,50 kN/m²** (cat. B) — enveloppe retenue | D2 p. 1 (250 daN/m²) vs D3 p. 10-11 (150 daN/m² logement) | **Contractuelle haute** — l'écart est tranché par enveloppe, pas par décision |
| `CHG-03` Poids propres plancher | **Recalculé par couches** : plancher A `0,80` · plancher B `3,91 ` · + recharge `3,30` | D3 p. 10-12 + D4 p. 5 et 14 | **`H-28`** — valeurs déclarées au cartouche : 1,00 et 3,50 |
| `CHG-04` Poids propres toiture | **0,95 kN/m²** par couches | D2 f. 02 (constitution) — aucune charge au cartouche | **`H-29`** |
| `CHG-05` Neige | **0,45 kN/m²** — zone A1, altitude < 200 m, `s_k = 45 daN/m²` | D2 p. 1 | **Contractuelle** |
| `CHG-06` Vent | `v_b = 24 m/s`, terrain III | D2 p. 1 | **Non intégré** — relève de `B-25` (déjà traité) et `B-44`/`B-45` |
| `CHG-08` Cloisons | **0,80 kN/m²** forfaitaire | EC1-1-1 § 6.3.1.2 — aucune charge de cloison dans le DCE | **`H-30`** |
| Surfaces | RDC **111,15 m²** · R+1 **106,92 m²** | `D-22` | **Décision client** |

> **Note sur `CHG-08` et la règle `V9`.** Le forfait de cloisons `0,80 kN/m²` est une **charge**, pas un élément dessiné. `V9` et `D-25` interdisent de représenter cloisons et isolants sur une vue structurelle — ils n'interdisent pas de compter leur poids dans une descente de charges. Confondre les deux serait une faute : une structure dimensionnée sans cloisons s'affaisse sous leur poids.

---

## 2. TABLEAU 1 — SURFACES D'INFLUENCE

Trame de référence : `B-20 Ind. B § 2.2` — files verticales `A` (`X = −0,32`) · `B` (`+0,68`) · `C` (`+2,88`) · `D` (`+3,91`) · `E` (`+9,48`) ; files horizontales `1` (`Y = +0,17`) · `2` (`+5,11`) · `3` (`+7,71`) · `4` (`+10,46`) · `5` (`+14,62`) · `6` (`+18,69`), en mètres du repère `B-30`.

| Porteur | `L_t` (m) | `l_t` (m) | `A_inf` (m²) | Justification (demi-portées adjacentes) |
|---|---|---|---|---|
| **P1-N** | 1,26 | 0,50 | **0,63** | Demi-portée du linteau bois de façade Ouest Sud (`L = 2,52 m` entre `P1-N` et `P1-S`) × épaisseur de mur porté (0,50 m) |
| **P1-S** | 1,26 | 0,50 | **0,63** | Idem — second appui de la même baie |
| **P2** | 2,785 | 4,115 | **11,46** | Demi-portée `D→E` (`5,57/2`) × demi-portées `4→5` et `5→6` (`(4,16+4,07)/2`) |
| **P3** | 0,45 | 0,50 | **0,23** | Demi-portée de `F1b` (`L = 0,90 m`) × épaisseur de mur porté (0,50 m) |
| **J1** | 0,50 | 0,50 | **0,25** | Demi-portée de `F1a` (`L = 1,00 m`) × épaisseur du refend central (0,50 m) |
| **M11** (voile RDC) | — | — | **4,115 ml** | Largeur tributaire par mètre linéaire = `(4,16+4,07)/2` — pignon Nord |
| **M03** (voile RDC) | — | — | **3,455 ml** | Largeur tributaire par mètre linéaire = `(2,75+4,16)/2` — refend central |
| **SF1** | — | — | **11,46** | Reçoit l'intégralité de la réaction de `P2` |

**Cas particuliers — porteurs sans surface d'influence au sens strict :**

| Porteur | Mode de reprise | Charge reprise |
|---|---|---|
| **`F1a`, `F1b`, `F1c`** | Linteau dans un mur porteur | Mur de moellons au-dessus (`0,50 × 3,50 m` à `22 kN/m³`) + bande de plancher de 1,00 m |
| **`F2`, `F3`, `F4`, `R1`, `R2-N`, `R2-S`** | Poutre sous plancher | Bande tributaire = somme des demi-portées adjacentes |
| **`R3-N`, `R3-S`** | Linteau de baie | **Réaction de `R2`** à mi-portée, pas une bande de plancher |
| **`S1` (×10), `S2` (×6)** | Sommier de répartition | **Réaction du poteau ou du linteau** qu'il reçoit — vérifié au § 6 |

> **Contrôle de cohérence.** La somme des aires d'influence des cinq poteaux (`13,20 m²`) ne couvre que **12,3 %** de la surface du R+1. Ce n'est pas une erreur : le pavillon Flora est un bâtiment **en maçonnerie porteuse**, où les planchers s'appuient directement sur les murs. Les poteaux ne reprennent que les points singuliers (façade Ouest, hall, refend).

---

## 3. TABLEAU 2 — CHARGES PERMANENTES PAR COUCHE

### 3.1 Plancher A — aile Est (solives bois 8×18)

| Couche | Épaisseur (m) | γ (kN/m³) | `g` (kN/m²) | Source |
|---|---|---|---|---|
| Parquet + volige | 0,030 | 6,0 | 0,18 | D3 p. 10 — constitution du plancher bois |
| Solives bois 8×18, e = 0,50 m | 0,180 | 5,5 | 0,16 | D3 p. 10 (section × entraxe) |
| Plafond lattis-plâtre | 0,025 | 12,0 | 0,30 | D3 p. 9 (désordre 9) |
| Divers (clouage, lambourdes) | — | — | 0,06 | `H-28` — forfait de liaison |
| Câblages et gaines dans le vide | — | — | 0,10 | D4 p. 6 (programme technique) |
| **Total par couches** | | | **0,80** | |
| **Valeur déclarée `D2 p. 1`** | | | **1,00** | 100 daN/m² |
| **VALEUR RETENUE** | | | **1,00** | **La plus élevée des deux** (`V3`) |

### 3.2 Plancher B — aile Ouest (voutains + `IPE 160`)

| Couche | Épaisseur (m) | γ (kN/m³) | `g` (kN/m²) | Source |
|---|---|---|---|---|
| Revêtement de sol | 0,020 | 20,0 | 0,40 | D4 p. 5 (sol projeté) |
| Chape 10 cm | 0,100 | 22,0 | 2,20 | D3 p. 11 — « chape 10 cm » |
| Voutains briques 7 cm + hourdis | 0,070 | 15,0 | 1,05 | D3 p. 11 |
| Solives `IPE 160`, e = 0,72 m | 0,160 | 5,0 | 0,11 | D3 p. 11 (15,8 kg/m ÷ 0,72 m) |
| Plafond + suspension | — | — | 0,15 | D3 p. 12 |
| **Total par couches** | | | **3,91** | |
| **Valeur déclarée `D2 p. 1`** | | | **3,50** | 350 daN/m² |
| **VALEUR RETENUE** | | | **3,91** | **La plus élevée — `D2` sous-déclare de 12 %** |

### 3.3 Recharge de sol (`D4 p. 5 et 14`)

| Couche | Épaisseur (m) | γ (kN/m³) | `g` (kN/m²) | Source |
|---|---|---|---|---|
| **Recharge de sol 15 cm** | **0,150** | **22,0** | **3,30** | **`H-28`** — `D4` prescrit l'épaisseur, jamais la densité |

> **Pourquoi 22 kN/m³.** `D4` dit « sol à recharger de 15 cm » sans préciser la nature du matériau de recharge. `22 kN/m³` est la densité d'un **béton de forme ou d'une chape lourde** — la valeur haute d'une recharge courante. Une recharge en sable (`18 kN/m³`) donnerait `2,70 kN/m²`, soit `−0,60 kN/m²` et `−7 %` sur l'effet de charge de `F3` : la conclusion du § 0 ne basculerait pas.

### 3.4 Toiture — combles et versants

| Couche | Épaisseur (m) | γ (kN/m³) | `g` (kN/m²) | Source |
|---|---|---|---|---|
| Tuiles + liteaux | 0,050 | 8,0 | 0,40 | D2 f. 02 — `H-29` |
| Chevrons + volige | 0,080 | 5,5 | 0,15 | D2 f. 02 — `H-29` |
| Pannes + fermes (ramené au m²) | — | — | 0,25 | D2 f. 02 — `H-29` |
| Plafond de combles | 0,020 | 12,0 | 0,15 | D2 f. 02 — `H-29` |
| **TOTAL toiture** | | | **0,95** | |

### 3.5 Synthèse des charges permanentes retenues

| Zone | `g` par couches | Déclaré `D2` | Recharge | Cloisons `H-30` | **`g` total retenu** |
|---|---|---|---|---|---|
| Plancher A (aile Est) | 0,80 | 1,00 | +3,30 | +0,80 | **5,10 kN/m²** |
| Plancher B (aile Ouest) | 3,91 | 3,50 | +3,30 | +0,80 | **8,01 kN/m²** |
| Toiture | 0,95 | — | — | — | **0,95 kN/m²** |

---

## 4. TABLEAU 3 — CHARGES D'EXPLOITATION PAR CATÉGORIE EC1

| Zone | Usage (catégorie EC1) | `q_k` (kN/m²) | Cloisons (kN/m²) | Total (kN/m²) | Source |
|---|---|---|---|---|---|
| **RDC et R+1 — ensemble** | **B** — bureaux / cabinet paramédical | **2,50** | +0,80 | **3,30** | D2 p. 1 (250 daN/m²) — **enveloppe** vs 150 daN/m² de D3 |
| **R+1 — salle de sport (34,25 m²)** | **C4** — activités physiques | **5,00** | +0,80 | **5,80** | **`H-31`** — voir § 4.1 |
| **Toiture** | **H** — toiture inaccessible, pente > 20° | **0,40** | — | **0,40** | EC1-1-1 tableau 6.10 |
| **Toiture — neige** | Neige (action climatique) | **0,45** | — | **0,45** | `CHG-05` — zone A1, `s_k = 45 daN/m²` |

### 4.1 `H-31` — la salle de sport n'est pas un bureau

`CHG-01b` nomme une **salle de sport de 34,25 m²** au R+1. Le cartouche `D2` applique **2,50 kN/m² à l'ensemble du bâtiment**, sans distinguer les locaux. Or une salle de sport relève de la **catégorie C4** de l'EC1-1-1 (`q_k = 5,00 kN/m²`) — **le double**.

| Effet | Calcul | Valeur |
|---|---|---|
| Surface concernée | `CHG-01b` | 34,25 m² |
| Majoration de charge | `34,25 × (5,00 − 2,50)` | **+85,6 kN** à l'ELS |
| Part de la charge totale du R+1 | `85,6 / 1 036` | **+8,3 %** |
| Effet sur une poutre traversant la zone | `(5,00−2,50) × bande` | jusqu'à **+2,5 kN/m²** localement |

> **Ce n'est pas une hypothèse de confort.** Une salle de sport reçoit des charges concentrées et des efforts dynamiques que la catégorie B ne couvre pas. Retenir `B` sur ce local serait une **sous-déclaration opposable**. `H-31` est donc notifiée sous nuage, avec la conséquence explicite : si la MOA confirme l'usage sportif, `F3`, `R1` et les solives de la zone Est doivent être recalculés avec `q = 5,00` — et le différentiel de `+85,6 kN` remonte jusqu'aux voiles.

### 4.2 Ce que `CHG-02` ne tranche pas

`D2` annonce `250 daN/m²` (bureaux), `D3` retenait `150 daN/m²` (logement). La DDC retient **2,50 kN/m²** partout : c'est l'**enveloppe**, et c'est la seule valeur défendable tant que la MOA n'a pas écrit sa décision. Une DDC bâtie sur `1,50` serait une DDC qui **minore le programme contractualisé de 67 %** — exactement ce que le diagnostic de `D3` ne couvre plus.

---

## 5. CHARGES LINÉIQUES SUR LES POUTRES ET LINTEAUX

`p = bande tributaire × (g + q)` , majorée du **mur porté** pour les linteaux en sous-œuvre.

| Poutre | `L` (m) | Bande (m) | Mur (kN/m) | `p_ELS` (kN/m) | `p_ELU` (kN/m) |
|---|---|---|---|---|---|
| **F1a** | 1,00 | 1,00 | 38,5 | 49,0 | **76,5** |
| **F1b** | 0,90 | 1,00 | 38,5 | 49,0 | **76,5** |
| **F1c** | 0,85 | 1,00 | 38,5 | 49,0 | **76,5** |
| **F2** | 2,85 | 3,77 | — | 39,6 | **63,1** |
| **F3** | 3,85 | 2,75 | — | 28,9 | **46,1** |
| **F4** | 4,88 | 1,615 | — | 2,9 | **4,7** |
| **R1** | 3,85 | 3,455 | — | 36,3 | **57,9** |
| **R2-N** | 3,82 | 2,08 | — | 21,9 | **34,8** |
| **R2-S** | 3,82 | 1,62 | — | 17,0 | **27,1** |
| **R3-N / R3-S** (réaction) | 1,55 | — | — | 41,8 kN | **66,5 kN** |

**Détail du mur porté en sous-œuvre.** `F1a`, `F1b` et `F1c` percent un mur de moellons de **50 cm** d'épaisseur. Elles reprennent la maçonnerie située au-dessus de l'ouverture : `0,50 × 3,50 × 22 = 38,5 kN/m`. À cela s'ajoute la bande de plancher de 1,00 m de part et d'autre. **C'est cette charge de mur qui domine** — et c'est elle qui explique l'écart avec `B-20`, qui avait retenu `55 kN/m` au total.

---

## 6. DESCENTE DE CHARGES PAR PORTEUR

### 6.1 TABLEAU 4 — ELS : `N_ELS = ΣG_k + Q_k,1`

| Porteur | `A_inf` | `G` | `Q` | Coeff. continuité | **`N_ELS`** |
|---|---|---|---|---|---|
| **P1-N** | 0,63 m² | 75,6 kN | 6,3 kN | **1,00** | **81,9 kN** |
| **P1-S** | 0,63 m² | 75,6 kN | 6,3 kN | **1,00** | **81,9 kN** |
| **P2** | 11,46 m² | 118,1 kN | 38,9 kN | **1,15** | **157,0 kN** |
| **P3** | 0,23 m² | 27,0 kN | 2,2 kN | **1,00** | **29,3 kN** |
| **J1** | 0,25 m² | 30,0 kN | 2,5 kN | **1,00** | **32,5 kN** |
| **M11** | 4,115 ml | 36,9 kN/m | 13,8 kN/m | **1,15** | **50,7 kN/m** |
| **M03** | 3,455 ml | 31,0 kN/m | 11,6 kN/m | **1,15** | **42,5 kN/m** |
| **SF1** | 11,46 m² | 135,8 kN | 44,7 kN | **1,15** | **180,5 kN** |

### 6.2 TABLEAU 5 — ELU : `N_ELU = 1,35·ΣG_k + 1,5·Q_k,1`

| Porteur | `1,35·G` | `1,5·Q` | Coeff. continuité | **`N_ELU`** | `N/A_inf` (kN/m²) |
|---|---|---|---|---|---|
| **P1-N** | 102,1 kN | 9,4 kN | 1,00 | **111,5 kN** | 177,1 |
| **P1-S** | 102,1 kN | 9,4 kN | 1,00 | **111,5 kN** | 177,1 |
| **P2** | 159,4 kN | 58,3 kN | 1,15 | **217,7 kN** | 19,0 |
| **P3** | 36,5 kN | 3,4 kN | 1,00 | **39,8 kN** | 173,2 |
| **J1** | 40,5 kN | 3,8 kN | 1,00 | **44,3 kN** | 177,1 |
| **M11** | 49,8 kN/m | 20,7 kN/m | 1,15 | **81,0 kN/m** | 19,7 |
| **M03** | 41,8 kN/m | 17,4 kN/m | 1,15 | **68,0 kN/m** | 19,7 |
| **SF1** | 183,3 kN | 67,1 kN | 1,15 | **250,4 kN** | 21,8 |

### 6.3 Justification du classement rive / intermédiaire

| Porteur | Classement | Coefficient | Justification |
|---|---|---|---|
| **P1-N, P1-S** | **Rive** | 1,00 | Extrémités d'une baie de façade : le plancher ne continue pas au-delà |
| **P2** | **Intermédiaire** | 1,15 | En file 5, entre deux travées de plancher continues de part et d'autre |
| **P3** | **Rive** | 1,00 | Appui d'extrémité de `F1b` contre le refend |
| **J1** | **Rive** | 1,00 | Piédroit d'ouverture : le linteau `F1a` s'y arrête |
| **M11, M03** | **Intermédiaire** | 1,15 | Voiles courants : le plancher est continu de part et d'autre |
| **SF1** | **Intermédiaire** | 1,15 | Reçoit `P2`, lui-même intermédiaire — la continuité se transmet |

> **Le piège du 1,15, évité.** Le coefficient n'est **pas** appliqué partout : trois porteurs sur cinq sont en rive et reçoivent **1,00**. Appliquer `1,15` aux cinq aurait majoré la DDC de 15 % sur les poteaux de façade — une erreur qui, en exécution, se paie en acier inutile ou en section fausse.

### 6.4 Réactions aux sommiers `S1` et `S2`

| Sommier | Charge reçue | `R_ELS` | `R_ELU` | Admissible `B-20` (`σ_adm ≈ 0,8 MPa`) |
|---|---|---|---|---|
| **`S2` sous `F1a`** | Réaction du linteau | 24,5 kN | 38,3 kN | 80 kN — **OK** |
| **`S1` sous `F3`** | Réaction de `F3` | 55,6 kN | 88,7 kN | 64 kN — **OK en ELS, à confirmer en ELU par `B-40`** |
| **`S1` sous `R3-N`** | Réaction de `R3-N` | 41,8 kN | 66,5 kN | 64 kN — **OK** |

> **Point de vigilance transmis à `B-40`.** `S1` sous `F3` reçoit `55,6 kN` à l'ELS pour un admissible de `64 kN` : la marge n'est que de **13 %**. Les sommiers `S1` sont des appareils de **20 × 40 cm** seulement — `B-40` doit vérifier la diffusion dans la maçonnerie sous `F3`, et non seulement la compression du béton.

---

## 7. VÉRIFICATION DE L'HYPOTHÈSE `H-27` DE `B-25`

`B-25 Ind. B` a retenu `σ_d = 0,300 MPa` comme contrainte verticale moyenne sur les voiles, pour calculer `f_vk = (f_vk0 + 0,4 σ_d)/γ_M = 108 kPa`. **Cette valeur n'avait pas été calculée — elle était posée.** `B-21` la vérifie :

| Grandeur | Valeur |
|---|---|
| Charge totale ELU transmise aux voiles | **1 766 kN** |
| Aire portante des 12 voiles RDC (`B-25`) | **18,79 m²** |
| **`σ_d` calculé** | `1 766 / 18,79 = 94 kPa = ` **`0,094 MPa`** |
| `σ_d` retenu par `H-27` | **`0,300 MPa`** |
| `f_vk` avec `H-27` | 108 kPa |
| `f_vk` avec la valeur calculée | **75 kPa** |

**Conséquence sur `B-25` :** `H-27` **majore `f_vk` de 44 %**. En retenant la valeur réellement calculée, `τ/f_vk` passerait de `0,028` à **`0,040`** — soit exactement le niveau de l'enveloppe de démolition de l'indice A. **La conclusion de `B-25` est inchangée** (la capacité reste utilisée à moins de 5 %), mais l'hypothèse doit être requalifiée : elle est **conservatrice dans le sens favorable**, ce qui est la seule direction acceptable pour une hypothèse de résistance.

> **Ce que `B-21` apporte à `B-25`.** Deux briques se contrôlent l'une l'autre : `B-25` avait besoin d'un `σ_d` qu'elle ne pouvait pas calculer, `B-21` le produit et constate que l'hypothèse tenait. C'est le fonctionnement attendu de la chaîne — et c'est la première fois dans ce dossier qu'une hypothèse de `B-25` est **vérifiée par une brique aval**, et non seulement déclarée.

---

## 8. CONTRÔLE DE COHÉRENCE AVEC LE PRÉDIMENSIONNEMENT DE `B-20`

**Ce tableau compare des effets de charge, jamais des résistances.** `M_Ed = p_ELU·L²/8` est un effet des charges ; sa comparaison à `M_el,Rd` relève de `B-45`.

| Élément | `M_Ed` retenu par `B-20` | `M_Ed` calculé par `B-21` | Écart | Conséquence |
|---|---|---|---|---|
| **F1a** | 10,7 kN·m | 9,6 kN·m | **−11 %** | Cohérent |
| **F1b** | 10,7 kN·m | 7,7 kN·m | **−28 %** | Cohérent |
| **F1c** | 10,7 kN·m | 6,9 kN·m | **−35 %** | Cohérent |
| **F2** | 50,0 kN·m | **64,1 kN·m** | **+28 %** | **`B-45` à reprendre** |
| **F3** | 40,8 kN·m | **85,3 kN·m** | **+109 %** | **`B-45` PRIORITAIRE** |
| **F4** | 20,1 kN·m | 14,1 kN·m | **−30 %** | Cohérent |
| **R1** | 47,5 kN·m | **107,2 kN·m** | **+126 %** | **`B-45` PRIORITAIRE** |
| **R2-N** | 43,5 kN·m | **63,5 kN·m** | **+46 %** | **`B-45` à reprendre** |
| **R2-S** | 43,5 kN·m | 49,5 kN·m | +14 % | Cohérent |

| Poteau | `N_ELU` retenu par `B-20` | `N_ELU` calculé | Écart | Conséquence |
|---|---|---|---|---|
| **P1-N / P1-S** | 45 à 75 kN | **111,5 kN** | **+86 %** | `B-45` — tube `140×140` : capacité ≈ 546 kN, marge conservée |
| **P2** | 85 kN | **217,7 kN** | **+156 %** | **`B-42`** — flambement et section à reprendre |
| **SF1** (`N_ELS`) | 63,2 kN | **180,5 kN** | **+186 %** | **`B-40`** — voir § 9 |

### 8.1 Pourquoi `F1a/b/c` baissent et `F2/F3/R1` explosent

Ce n'est pas une incohérence de calcul, c'est une conséquence directe de la **nature des charges** :

- `F1a/b/c` reprennent surtout **un mur** (38,5 kN/m), et la bande de plancher qui s'y ajoute est étroite (`1,00 m`). `B-20` avait surestimé le mur mais surestimé aussi la bande : les deux erreurs se compensent partiellement.
- `F2`, `F3` et `R1` reprennent **du plancher pur** sur des bandes larges (`2,75 à 3,77 m`). Tout l'écart vient de la **recharge de 15 cm** que `B-20` n'avait pas intégrée dans ses `22 kN/m`.

---

## 9. `SF1` — LA SEMELLE DEVIENT INSUFFISANTE SI L'AIRE D'INFLUENCE EST CELLE DE LA TRAME

| Grandeur | Valeur |
|---|---|
| Semelle actuelle (`D-14`) | **60 × 60 cm = 0,36 m²** |
| `N_ELS` selon `B-21` | **180,5 kN** |
| **`σ_ELS`** | **501 kPa = 0,50 MPa** |
| Admissible (`D-02`) | **0,30 MPa** |
| **Verdict** | **NON CONFORME** — dépassement de 67 % |
| Largeur requise | `B ≥ √(180,5 / 300) = ` **`0,78 m`** → **80 × 80 cm** (0,64 m²) |
| `σ_ELS` en 80 × 80 | **282 kPa ≤ 300 kPa** — conforme |
| `σ_ELU` en 80 × 80 | `250,4 / 0,64 = 391 kPa ≤ 490 kPa` — conforme |

### 9.1 L'écart n'est pas dans le calcul, il est dans l'aire d'influence

`B-40 Ind. E` a vérifié `SF1` avec `N_ELS = 63,2 kN`, ce qui correspond à une aire d'influence de **6,5 m²** environ. La trame de `B-20` donne **11,46 m²**. Les deux valeurs ne peuvent pas être vraies en même temps.

| Hypothèse sur `P2` | `A_inf` | `N_ELS` | `σ_ELS` sur 60 × 60 | Verdict |
|---|---|---|---|---|
| Aire d'influence de la **trame** (demi-portées complètes) | 11,46 m² | 180,5 kN | **0,50 MPa** | **NON CONFORME** |
| Aire **réduite** : `P2` ne reprend que ce que le portique lui transmettait | ≈ 6,5 m² | ≈ 102 kN | **0,28 MPa** | Conforme de justesse |

**Laquelle est vraie ?** Aucune pièce ne le dit. `P2` remplace un portique bois de façade Ouest Nord ; si le mur de moellons de part et d'autre reste continu et porteur, il reprend l'essentiel du plancher et `P2` ne reçoit que la réaction du portique. **Mais si `P2` est le seul appui vertical de la baie — ce que suggère la suppression du portique — c'est la valeur de la trame qui s'applique.**

> **Décision à prendre — `D-30` proposée.** Trois issues, dans l'ordre de sécurité :
> 1. **Élargir `SF1` à 80 × 80 cm** — coût négligeable, sécurité maximale, décision immédiate. **C'est la recommandation.**
> 2. Justifier l'aire d'influence réduite par la continuité du mur de façade, et la consigner — ce qui suppose un relevé de la maçonnerie de part et d'autre de la baie.
> 3. Attendre le sondage de soubassement (`PA-01`, nuage `Z-P2`) et dimensionner sur le résultat — mais on ne décide pas d'une fondation après avoir ouvert la fouille.

---

## 10. SYNTHÈSE EN HUIT LIGNES

1. **Porteur le plus chargé en `N_ELU` :** `P2`, avec **217,7 kN** — suivi de `SF1` (250,4 kN, qui n'est que sa réaction transmise au sol).
2. **Plus fort ratio `N/A_inf` :** `P1-N` et `P1-S`, à **177,1 kN/m²** — conséquence d'un linteau étroit qui porte un mur de 50 cm : la charge est concentrée sur 0,63 m².
3. **Zone la plus pénalisante en exploitation :** la **salle de sport du R+1** (34,25 m²), à `5,00 kN/m²` si `H-31` est confirmée — **+85,6 kN** sur le niveau, **+8,3 %** de la charge totale.
4. **Charge totale du R+1 :** `1 036 kN` à l'ELS, **`1 766 kN` à l'ELU**, transmis aux voiles sur `18,79 m²` → `σ_d = 0,094 MPa`.
5. **Trois éléments sortent du prédimensionnement de `B-20` :** `F3` (**+109 %**), `R1` (**+126 %**), `F2` (**+28 %**), `R2-N` (**+46 %**). `F3` et `R1` sont prioritaires en `B-45`.
6. **`SF1` doit passer à 80 × 80 cm** si l'aire d'influence de `P2` est celle de la trame (`D-30` proposée).
7. **`H-27` est vérifiée et conservatrice** : `σ_d` réel `0,094 MPa` contre `0,300` retenu — `f_vk` est majoré de 44 %, dans le sens favorable.
8. **Hypothèses à confirmer en EXE :** `H-28` (densité de la recharge, 22 kN/m³), `H-29` (poids de toiture, 0,95 kN/m²), `H-30` (cloisons, 0,80 kN/m²), `H-31` (salle de sport en catégorie C4).

---

## 11. AUTO-CONTRÔLE DES SEPT CRITÈRES D'ACCEPTATION

| # | Critère de la fiche `B-21` | État | Preuve |
|---|---|---|---|
| 1 | Chaque porteur a une surface d'influence justifiée | ✅ **CONFORME** | § 2 — 8 porteurs surfaciques avec `L_t`, `l_t`, `A_inf` et demi-portées ; 14 porteurs linéaires avec bande tributaire |
| 2 | Chaque charge permanente est rattachée à une couche et à un poids volumique | ✅ **CONFORME** | § 3 — 14 couches, chacune avec épaisseur, `γ` et pièce source |
| 3 | Chaque charge d'exploitation est rattachée à une catégorie EC1 | ✅ **CONFORME** | § 4 — cat. B, C4, H et neige, chacune avec sa valeur et sa source |
| 4 | Chaque coefficient de continuité est justifié | ✅ **CONFORME** | § 6.3 — classement rive/intermédiaire justifié porteur par porteur ; `1,00` appliqué à 3 porteurs sur 5 |
| 5 | Les tableaux ELS et ELU sont distincts | ✅ **CONFORME** | § 6.1 et § 6.2 — deux tableaux, deux combinaisons |
| 6 | La sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION » | ✅ **CONFORME** | En-tête et bandeau de tête |
| 7 | Aucune vérification de section ni aucun ferraillage n'a été produit | ✅ **CONFORME** | § 8 compare des **effets de charge** à des effets de charge, jamais à une résistance ; § 9 est un **ordre de grandeur de surface d'assise** explicitement renvoyé à `B-40` ; aucun ferraillage |

**Verdict de la brique `B-21` (Indice A) : ✅ CONFORME — 7/7.**

---

## 12. HYPOTHÈSES CRÉÉES ET TRANSMISSIONS

### 12.1 Hypothèses notifiées

| Code | Hypothèse | Norme d'appui | Si rectifiée |
|---|---|---|---|
| **H-28** | Recharge de sol 15 cm à **`22 kN/m³`** ; plancher B recalculé à **`3,91 kN/m²`** (au lieu des `3,50` déclarés) | D4 p. 5 et 14 (épaisseur) + EC1 (densité) | Si sable (`18 kN/m³`) : `−0,60 kN/m²`, `F3` à `−7 %` — conclusion inchangée |
| **H-29** | Toiture à **`0,95 kN/m²`** (tuiles, chevrons, pannes, plafond) | D2 f. 02 — constitution sans charge | Si ardoises ou béton : `+0,20 kN/m²` — effet < 5 % sur `F4` |
| **H-30** | Cloisons forfaitaires **`0,80 kN/m²`** | EC1-1-1 § 6.3.1.2 | Si cloisons lourdes (`1,20`) : `+0,40 kN/m²` sur tout le plancher |
| **H-31** | Salle de sport R+1 en **catégorie C4** (`5,00 kN/m²`) | EC1-1-1 tableau 6.1 | Si la MOA confirme un usage bureaux : retour à `2,50`, `−85,6 kN` |

### 12.2 Transmissions aux briques aval

| Brique | Ce qu'elle reçoit de `B-21` |
|---|---|
| **`B-22`** | Les 4 hypothèses de charges à consigner et à notifier sous nuage |
| **`B-40`** | `SF1` : `N_ELS = 180,5 kN` → **80 × 80** ou justification d'aire réduite ; `S1` sous `F3` : marge de 13 % seulement |
| **`B-42`** | `P2` : `N_ELU = 217,7 kN` (contre 85 kN au prédimensionnement) — **flambement à reprendre**, `H/b = 20` |
| **`B-45`** | **`F3` (+109 %)** et **`R1` (+126 %)** en priorité ; puis `F2` (+28 %) et `R2-N` (+46 %) ; `P1` à 111,5 kN (capacité conservée) |
| **`B-46`** | Réactions aux sommiers `S1`/`S2` et `σ_d = 0,094 MPa` pour la vérification de la maçonnerie |
| **`B-25`** | `H-27` **vérifiée** et requalifiée comme conservatrice (`f_vk` majoré de 44 %) |

### 12.3 Point d'arrêt

Aucun point d'arrêt chantier n'est créé par `B-21`. Les deux points d'arrêt de `B-25` (`PA-01` reconnaissance des voiles, `PA-02` liaison charpente-maçonnerie) **restent ouverts** et intègrent le nuage `Z-P2` pour la reconnaissance du soubassement sous `P2`, qui conditionne le choix entre `SF1` 60 × 60 et 80 × 80.

---

## 13. POINT DE CONTRÔLE HUMAIN

Trois décisions vous appartiennent :

1. **`D-30` — `SF1` : 80 × 80 cm, ou justification de l'aire d'influence réduite de `P2` ?** Je recommande l'élargissement : le coût est de quelques dizaines de kilos de béton, l'économie d'une discussion sur une aire d'influence non démontrable.
2. **`H-31` — la salle de sport est-elle bien un usage sportif ?** Si oui, la catégorie C4 (`5,00 kN/m²`) s'applique et `F3`/`R1` sont recalculés avec cette charge. Si c'est une salle polyvalente, la catégorie C3 ou B peut se défendre — mais il faut une décision écrite.
3. **`CHG-02` — `2,50 kN/m²` confirmé partout ailleurs ?** L'enveloppe est retenue ; une décision MOA à `1,50` serait une minoration du programme contractualisé.

**Brique B-21 livrée en indice A — en attente de votre GO ou de vos observations.**
