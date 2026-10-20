# B-21 — DDC PRÉLIMINAIRE — CONCEPTION

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-21** — Descente de charges préliminaire |
| Phase | **3 — Conception et synthèse structurelle** (`B-20` → **`B-21`** → `B-22`) |
| **Mode d'appel** | **HYPOTHÈSE-NOTIFIÉE** — `CHG-03` (poids propres) et `CHG-04` (toiture) ne sont pas fournis par le marché ; `CHG-02` est en conflit entre deux pièces. Traités par `H-28` à `H-30` (charges) et tranchés par `D-31` (usage sportif), `D-32` (exploitation) et `D-35` (périmètre de la recharge) |
| Régime | **OUTILLÉ (V13)** — calcul intégral par script, journal d'exécution conservé |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b21_ddc.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b21_ddc.txt` (12 852 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b21_ddc.json` (10 363 o) |
| Sortie graphique | **Aucune** — la fiche `B-21` n'exige aucun livrable graphique |
| **Indice** | **C** — remplace et annule l'indice B du 20/10/2026 (décision `D-35` : la recharge de sol est un ouvrage de **dallage**, pas une charge de plancher) |
| Date | **20/10/2026** |
| Brique suivante | **`B-22`** (note d'hypothèses consolidée), puis **`B-43`** (planchers et dallage) |

> **Ce qui change à l'indice C — une localisation, pas un calcul.**
> L'indice B appliquait `+3,30 kN/m²` de recharge de sol aux **planchers** `A` et `B`, « sur toute la surface ». **C'était faux, et la vérification des pièces le démontre** : la recharge n'apparaît que **deux fois** dans les 29 planches du DCE graphique (`D4`) — `p. 5`, planche `PLANS DE DEMOLITION`, plan `RDC FLORA Projet` ; et `p. 14`, planche `SANITAIRES PMR RDC` à 1/50. **Aucune occurrence sur les planches de R+1**, dont les finitions sont pourtant nommées une à une. Contrôle croisé décisif : la vérification EVEN de la solive `8 × 18` (`w = 7,7 mm` pour `7,0` admis à `150 daN/m²`) n'est compatible **qu'avec un plancher non rechargé**.
>
> **`D-35` — décision du 20/10/2026 : « qui peut le plus peut le moins ».** La recharge est réputée s'appliquer à **100 % de l'emprise du dallage**, par hypothèse défavorable. Le dallage est donc calculé et dimensionné pour le cas le plus lourd ; toute surface non rechargée lui est favorable.
>
> **Conséquence chiffrée :** les planchers `A` et `B` perdent `3,30 kN/m²` (`g` de `B` : `8,01 → 4,71 kN/m²`), **toutes les poutres de plancher sont soulagées de 30,6 %**, et le **dallage devient l'ouvrage le plus chargé du bâtiment** (`14,21 kN/m²` à l'ELU). Les écarts avec `B-20` restent défavorables, mais deux fois moindres.

> **Titre opposable : DDC PRÉLIMINAIRE — CONCEPTION.**
> Cette note sert à **choisir et contrôler les sections en conception**. Elle **ne remplace pas** les DDC d'exécution des briques `B-40` à `B-50`, qui refont le calcul sur les schémas statiques réels, avec les surfaces d'influence exactes et les coefficients de continuité issus du schéma.
> **Aucune vérification de section et aucun ferraillage ne sont produits ici.** Les effets de charge sont calculés ; leur comparaison à une résistance appartient aux briques de calcul. Le **dimensionnement du dallage appartient à `B-43`** : `B-21` en produit la **charge**, pas l'épaisseur ni le treillis.

---

## 0. RÉPONSE DIRECTE — CE QUE LA DDC CHANGE DANS LE DOSSIER

**L'indice C corrige une localisation, pas une erreur d'arithmétique.** La recharge de sol de `15 cm` pesait sur les planchers hauts ; elle pèse désormais sur le dallage, là où les planches la dessinent. Six constats en découlent.

| # | Constat | Chiffre | Conséquence |
|---|---|---|---|
| **1** | **La recharge ne charge pas les planchers.** `D4 p. 5` (planche de démolition, plan `RDC`) et `p. 14` (`SANITAIRES PMR RDC`) la portent au RDC ; aucune planche de R+1 ne la mentionne | `g` du plancher B : **`8,01 → 4,71 kN/m²`** (`−41 %`) · plancher A : `5,10 → 1,80` | Tout `B-43` / `B-44` / `B-45` repart de charges plus basses |
| **2** | **Toutes les poutres de plancher sont soulagées de `30,6 %`** | `F2` `63,1 → 43,8` · `F3` `46,1 → 32,0` · `R1` `57,9 → 40,2` · `R2-N` `34,8 → 24,2` | Les sections de `B-20` redeviennent crédibles — sans être justifiées pour autant |
| **3** | **`F3` et `R1` restent hors prédimensionnement, mais deux fois moins** | `F3` **`+45 %`** (au lieu de `+109 %`) · `R1` **`+57 %`** (au lieu de `+126 %`) | `B-45` garde la priorité ; le dépassement n'est plus un facteur 2,3 mais 1,6 |
| **4** | **Le dallage devient l'ouvrage le plus chargé du bâtiment** | `14,21 kN/m²` à l'ELU sur `111,15 m²` = **`1 579 kN`** — davantage que les `1 290 kN` transmis aux voiles par le R+1 | `B-43` doit traiter le dallage **avant** les planchers : c'est lui qui porte le plus |
| **5** | **`SF1` en `80 × 80` est conforme** | `N_ELS = 130,5 kN` → `σ = 204 kPa ≤ 300 kPa` · `N_ELU = 182,9 kN` → `286 kPa ≤ 490 kPa` | `D-30` **reste nécessaire** : en 60 × 60, `σ` vaudrait `362 kPa` (`+21 %` sur l'admissible) — l'excès tombe de `67 %` à `21 %`, il ne disparaît pas |
| **6** | **`H-27` est encore plus conservatrice** | `σ_d` réel `0,069 MPa` (au lieu de `0,094`) → `f_vk` majoré de **`52 %`** | `B-25` peut garder son `σ_d = 0,300 MPa` ; `τ/f_vk` passerait de `0,028` à `0,043` |

**Ce qui ne change pas :** la **nature** des écarts avec `B-20` — `F3`, `R1`, `F2`, `R2-N` restent au-dessus du prédimensionnement, `P2` reste à `+87 %` de son `N_ELU` d'origine. La conclusion de `B-21` est **plus basse, pas renversée**.

---

## 1. DONNÉES D'ENTRÉE ET STATUT

| Variable | Valeur | Source | Statut |
|---|---|---|---|
| `CHG-01a` Programme RDC | Plateau technique 33,14 · Box kiné 11,20 / 9,60 / 9,15 · Bureaux 16,08 / 12,80 · Sanitaire PMR 5,19 | D4 p. 6 et 9 | **Contractuelle** |
| `CHG-01b` Programme R+1 | **Salle de sport 34,25** · Salle commune 11,75 · Vestiaire 9,32 · Douche 2,37 · Bureaux consult. 13,26 / 16,50 · Dégagement 5,96 · Attente 8,38 | D4 p. 6 et 9 | **Contractuelle** |
| `CHG-02` Exploitation | **2,50 kN/m²** (cat. B) — enveloppe retenue | D2 p. 1 (250 daN/m²) vs D3 p. 10-11 (150 daN/m² logement) | **`D-32`** — `2,50 kN/m²` confirmés le 20/10/2026 pour tout le bâtiment |
| `CHG-03` Poids propres plancher | **Recalculé par couches** : plancher A `0,80` · plancher B `3,91` — **sans recharge** | D3 p. 10-12 | **`H-28`** — valeurs déclarées au cartouche : 1,00 et 3,50 |
| `CHG-03b` Recharge de sol `15 cm` | **`3,30 kN/m²` sur le DALLAGE uniquement** (`D4` p. 5 et 14), **100 % de l'emprise** | D4 p. 5 et 14 (épaisseur) + EC1 (densité) | **`D-35`** + `H-28` — la densité reste une hypothèse |
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

### 3.3 La recharge de sol n'est pas une charge de plancher (`D-35`)

**Ce que les pièces disent, et rien de plus.** La chaîne « recharg » apparaît **deux fois** dans les 29 planches du DCE graphique (`D4`) :

| Planche | Cartouche | Occurrence | Plan |
|---|---|---|---|
| `D4` **p. 5** | `PLANS DE DEMOLITION` — 1/100 | « Sol à recharger de 15cm » à `x = 158 · y = 232` | **`RDC FLORA` — Projet** |
| `D4` **p. 14** | `SANITAIRES PMR RDC` — 1/50 | « sol à recharger de 15cm », sous le carrelage | **RDC** — sanitaire |

**Aucune occurrence sur les planches de R+1** (`p. 16` à `p. 18`), dont les finitions sont nommées une à une : moquette grand trafic, parquet, sol souple acoustique, carrelage — **sans recharge**.

**Trois recoupements qui confirment la lecture :**

1. **Position sur la planche `p. 5`** : l'annotation tombe dans la bande des annotations de RDC (avec « dépose des dalles », « sol décaissé en pente 10 % `h : 16,8 cm` », « ouverture mur », « `Hspo : 2.75` »), et non dans celle du R+1 (« cloisons démolies », repères `Z : 204,42`).
2. **Le diagnostic** : EVEN vérifie la solive `8 × 18` à `150 daN/m²` et trouve `w = 7,7 mm` pour `7,0` admis. Avec `3,30 kN/m²` de recharge, la flèche triplerait (≈ `25 mm`). **Le chiffre d'EVEN n'est compatible qu'avec un plancher non rechargé.**
3. **La nature du plancher bas** : `D2` folio 03 = « Vue en plan **PB RDC** — **Dallage** » ; `B-20` retient un dallage BA désolidarisé `ép. 13 cm` sur forme `40 cm`. La recharge est un **ouvrage de sol en contact avec le terrain**.

> **`D-35` — décision du 20/10/2026, mot pour mot : « qui peut le plus peut le moins. Pour avancer, nous allons calculer et dimensionner le dallage comme si la surcharge de 15 cm est sur la totalité de l'emprise du dallage. Hypothèse défavorable. »**
> La recharge est donc portée à **100 % de l'emprise du dallage** (`111,15 m²`). C'est **volontairement défavorable** : si le dallage tient sur toute sa surface, il tient sur les seules zones réellement rechargées (entrée et sanitaires PMR identifiés). **L'emprise exacte n'est pas tracée au DCE** — les deux planches portent une annotation avec ligne de rappel, jamais une trame hachurée. Cette imprécision **cesse d'avoir un effet sur le calcul** : elle est absorbée par l'hypothèse défavorable.
>
> **Ce que `D-35` ferme :** la réserve `R-24-B1` de `B-24 Ind. B` (périmètre de la recharge) est **close**.
> **Ce que `D-35` n'autorise pas :** appliquer la recharge aux planchers hauts. La décision porte sur le **dallage** ; elle ne dit pas que les planchers sont rechargés.

### 3.4 Toiture — combles et versants

| Couche | Épaisseur (m) | γ (kN/m³) | `g` (kN/m²) | Source |
|---|---|---|---|---|
| Tuiles + liteaux | 0,050 | 8,0 | 0,40 | D2 f. 02 — `H-29` |
| Chevrons + volige | 0,080 | 5,5 | 0,15 | D2 f. 02 — `H-29` |
| Pannes + fermes (ramené au m²) | — | — | 0,25 | D2 f. 02 — `H-29` |
| Plafond de combles | 0,020 | 12,0 | 0,15 | D2 f. 02 — `H-29` |
| **TOTAL toiture** | | | **0,95** | |

### 3.5 Synthèse des charges permanentes des PLANCHERS

| Zone | `g` par couches | Déclaré `D2` | Recharge | Cloisons `H-30` | **`g` total retenu** |
|---|---|---|---|---|---|
| Plancher A (aile Est) | 0,80 | 1,00 | **aucune** (`D-35`) | +0,80 | **1,80 kN/m²** |
| Plancher B (aile Ouest) | 3,91 | 3,50 | **aucune** (`D-35`) | +0,80 | **4,71 kN/m²** |
| Toiture | 0,95 | — | — | — | **0,95 kN/m²** |

### 3.6 Le dallage — la recharge est ici

| Couche | Épaisseur (m) | γ (kN/m³) | `g` (kN/m²) | Source |
|---|---|---|---|---|
| Dallage BA `C25/30` | 0,130 | 25,0 | 3,25 | `B-20` § infrastructure — dallage BA désolidarisé `ép. 13 cm` sur forme `40 cm` |
| Revêtement de sol (carrelage / sol souple) | 0,020 | 20,0 | 0,40 | `D4` p. 8 (plans sols) |
| **Recharge de sol 15 cm** | **0,150** | **22,0** | **3,30** | **`D-35`** — `H-28` pour la densité ; **100 % de l'emprise** |
| Cloisons forfaitaires | — | — | 0,80 | `H-30` — EC1-1-1 § 6.3.1.2 |
| **TOTAL `g`** | | | **7,75** | |
| Exploitation `q` (cat. B) | — | — | 2,50 | `D-32` |
| **`p_ELS`** | | | **10,25 kN/m²** | |
| **`p_ELU`** | | | **14,21 kN/m²** | |

> **Pourquoi la charge de cloisons sur un dallage.** `H-30` est un **forfait de charge**, pas un élément dessiné : `V9` et `D-25` interdisent de représenter cloisons et isolants sur une vue structurelle, ils n'interdisent pas de compter leur poids. Un dallage qui porte des cloisons doit les compter.
>
> **La valeur de `p_ELU` du dallage n'est pas un dimensionnement.** Elle fixe la **charge** ; l'épaisseur, le treillis, les joints et le poinçonnement relèvent de `B-43`. Ce que `B-21` peut dire, c'est que cette charge — `14,21 kN/m²`, soit `0,014 MPa` — reste **très inférieure** à la contrainte admissible du sol (`0,30 MPa` à l'ELS, `D-02`). **Le dallage n'est pas un problème de portance ; il sera un problème de fissuration et de désolidarisation.**

---

## 4. TABLEAU 3 — CHARGES D'EXPLOITATION PAR CATÉGORIE EC1

| Zone | Usage (catégorie EC1) | `q_k` (kN/m²) | Cloisons (kN/m²) | Total (kN/m²) | Source |
|---|---|---|---|---|---|
| **RDC et R+1 — ensemble** | **B** — bureaux / cabinet paramédical | **2,50** | +0,80 | **3,30** | D2 p. 1 (250 daN/m²) — **enveloppe** vs 150 daN/m² de D3 |
| **R+1 — salle de sport (34,25 m²)** | **C4** — activités physiques | **5,00** | +0,80 | **5,80** | **`D-31`** — catégorie confirmée le 20/10/2026 (§ 4.1) |
| **Toiture** | **H** — toiture inaccessible, pente > 20° | **0,40** | — | **0,40** | EC1-1-1 tableau 6.10 |
| **Toiture — neige** | Neige (action climatique) | **0,45** | — | **0,45** | `CHG-05` — zone A1, `s_k = 45 daN/m²` |

### 4.1 `D-31` — la salle de sport n'est pas un bureau (confirmé le 20/10/2026)

`CHG-01b` nomme une **salle de sport de 34,25 m²** au R+1. Le cartouche `D2` applique **2,50 kN/m² à l'ensemble du bâtiment**, sans distinguer les locaux. Or une salle de sport relève de la **catégorie C4** de l'EC1-1-1 (`q_k = 5,00 kN/m²`) — **le double**.

| Effet | Calcul | Valeur |
|---|---|---|
| Surface concernée | `CHG-01b` | 34,25 m² |
| Majoration de charge | `34,25 × (5,00 − 2,50)` | **+85,6 kN** à l'ELS |
| Part de la charge totale du R+1 | `85,6 / 1 036` | **+8,3 %** |
| Effet sur une poutre traversant la zone | `(5,00−2,50) × bande` | jusqu'à **+2,5 kN/m²** localement |

**Arbitrage rendu.** Le client a confirmé le **20/10/2026** l'usage sportif du local : la **catégorie C4** s'applique et devient **opposable**. `H-31` est **promue décision `D-31`** — elle ne figure plus au registre des hypothèses notifiées, mais au registre des décisions.

> **Ce que la confirmation verrouille.** `+85,6 kN` à l'ELS remontent jusqu'aux voiles et `+2,5 kN/m²` localement sur les poutres traversant la zone. Ce supplément **n'est plus une réserve** : il entre en dur dans `B-43`, `B-44` et `B-45`. Un retour ultérieur à `2,50 kN/m²` exigerait une **nouvelle décision écrite** modifiant `D-31`, pas une simple observation — c'est la contrepartie de l'arbitrage, et c'est ce qui protège le dimensionnement du bavardage de chantier.

**Ce que la décision ne dit pas.** `D-31` fixe la **catégorie**, pas la **répartition des charges concentrées**. Une salle de sport reçoit des engins et des agrès dont les points d'appui sont des charges ponctuelles que `5,00 kN/m²` ne couvre pas nécessairement. `B-44` doit demander à la MOA la **liste des équipements fixes** (bancs, espaliers, machines) avant d'arrêter les solives de la zone Est.

### 4.2 `D-32` — `CHG-02` est tranchée : 2,50 kN/m² partout

`D2` annonce `250 daN/m²` (bureaux), `D3` retenait `150 daN/m²` (logement). Le client a **confirmé le 20/10/2026** la valeur de **`2,50 kN/m²`** partout, hors le local `D-31`. Le conflit entre les deux pièces est **clos par décision `D-32`** : la DDC ne repose plus sur une enveloppe prudentielle mais sur une valeur opposable.

> **Ce que cela ferme.** La réserve `R-06` du RDR (« 250 vs 150, avant `B-21` ») et le verrou `V-06` qui imposait de mener `B-22` à `B-24` **en paramétrique sur les deux valeurs** tombent. `B-22` n'a plus deux hypothèses à porter en parallèle : elle en porte une.

---

## 5. CHARGES LINÉIQUES SUR LES POUTRES ET LINTEAUX

`p = cont × [bande tributaire × (g + q) + mur porté]`. **Sans recharge** depuis `D-35`. Le **coefficient de continuité** `cont` est le même à l'ELS et à l'ELU : une poutre continue l'est dans les deux combinaisons, et la flèche (`B-43`) se calcule sur la même ligne d'influence que le moment.

| Poutre | `L` (m) | Bande (m) | Mur (kN/m) | `p_ELS` (kN/m) | `p_ELU` (kN/m) |
|---|---|---|---|---|---|
| **F1a** | 1,00 | 1,00 | 38,5 | 52,6 | **71,4** |
| **F1b** | 0,90 | 1,00 | 38,5 | 52,6 | **71,4** |
| **F1c** | 0,85 | 1,00 | 38,5 | 52,6 | **71,4** |
| **F2** | 2,85 | 3,77 | — | 31,3 | **43,8** |
| **F3** | 3,85 | 2,75 | — | 22,8 | **32,0** |
| **F4** | 4,88 | 1,615 | — | 3,3 | **4,7** |
| **R1** | 3,85 | 3,455 | — | 28,6 | **40,2** |
| **R2-N** | 3,82 | 2,08 | — | 17,2 | **24,2** |
| **R2-S** | 3,82 | 1,62 | — | 13,4 | **18,8** |

**`R3-N` et `R3-S` ne portent aucune charge répartie.** Ce sont les linteaux de baie qui reprennent la réaction de `R2-N` / `R2-S` à mi-portée : `24,2 × 3,82 / 2 =` **`46,2 kN`** à l'ELU, `32,9 kN` à l'ELS. Leur calcul appartient à `B-45`.

**Détail du mur porté en sous-œuvre.** `F1a`, `F1b` et `F1c` percent un mur de moellons de **50 cm** d'épaisseur. Elles reprennent la maçonnerie située au-dessus de l'ouverture : `0,50 × 3,50 × 22 = 38,5 kN/m`. À cela s'ajoute la bande de plancher de `1,00 m` : `1,00 × (4,71 + 2,50) = 7,21 kN/m`, soit `45,7 kN/m` avant continuité et **`52,6 kN/m`** après application du coefficient `1,15`. **C'est la charge de mur qui domine** (`38,5` sur `45,7`, soit 84 %) — c'est pourquoi `F1a/b/c` varient peu d'un indice à l'autre.

**Ce que le retrait de la recharge fait aux poutres.** Les poutres qui ne portent **que du plancher** perdent exactement `1,35 × 3,30 × bande` :

| Poutre | Bande | Perte `p_ELU` | `p_ELU` indice B | `p_ELU` indice C |
|---|---|---|---|---|
| `F2` | 3,770 m | `−19,3 kN/m` | 63,1 | **43,8** |
| `F3` | 2,750 m | `−13,6 kN/m` | 46,1 | **32,0** |
| `R1` | 3,455 m | `−17,7 kN/m` | 57,9 | **40,2** |
| `R2-N` | 2,080 m | `−10,7 kN/m` | 34,8 | **24,2** |
| `R2-S` | 1,620 m | `−8,3 kN/m` | 27,1 | **18,8** |
| `F1a/b/c` | 1,000 m | `−5,1 kN/m` | 76,5 | **71,4** |
| `R3-N / R3-S` | — | `−20,3 kN` (réaction) | 66,5 | **46,2 kN** |

**`−30,6 %` sur les cinq poutres de plancher**, `−6,7 %` sur les trois frangements de façade (dont la charge est dominée par le mur).

---

## 6. DESCENTE DE CHARGES PAR PORTEUR

### 6.1 TABLEAU 4 — ELS : `N_ELS = ΣG_k + Q_k,1`

| Porteur | `A_inf` | `G` | `Q` | Coeff. continuité | **`N_ELS`** |
|---|---|---|---|---|---|
| **P1-N** | 0,63 m² | 67,3 kN | 6,3 kN | **1,00** | **73,6 kN** |
| **P1-S** | 0,63 m² | 67,3 kN | 6,3 kN | **1,00** | **73,6 kN** |
| **P2** | 11,46 m² | 74,6 kN | 38,9 kN | **1,15** | **113,5 kN** |
| **P3** | 0,23 m² | 24,0 kN | 2,2 kN | **1,00** | **26,3 kN** |
| **J1** | 0,25 m² | 26,7 kN | 2,5 kN | **1,00** | **29,2 kN** |
| **M11** | 4,115 ml | 23,3 kN/m | 13,8 kN/m | **1,15** | **37,1 kN/m** |
| **M03** | 3,455 ml | 19,6 kN/m | 11,6 kN/m | **1,15** | **31,1 kN/m** |
| **SF1** | 11,46 m² | 85,8 kN | 44,7 kN | **1,15** | **130,5 kN** |

### 6.2 TABLEAU 5 — ELU : `N_ELU = 1,35·ΣG_k + 1,5·Q_k,1`

| Porteur | `1,35·G` | `1,5·Q` | Coeff. continuité | **`N_ELU`** | `N/A_inf` (kN/m²) |
|---|---|---|---|---|---|
| **P1-N** | 90,9 kN | 9,4 kN | 1,00 | **100,3 kN** | 159,2 |
| **P1-S** | 90,9 kN | 9,4 kN | 1,00 | **100,3 kN** | 159,2 |
| **P2** | 100,7 kN | 58,3 kN | 1,15 | **159,0 kN** | 13,9 |
| **P3** | 32,5 kN | 3,4 kN | 1,00 | **35,8 kN** | 155,8 |
| **J1** | 36,1 kN | 3,8 kN | 1,00 | **39,8 kN** | 159,2 |
| **M11** | 31,4 kN/m | 20,7 kN/m | 1,15 | **59,9 kN/m** | 14,6 |
| **M03** | 26,4 kN/m | 17,4 kN/m | 1,15 | **50,3 kN/m** | 14,6 |
| **SF1** | 115,8 kN | 67,1 kN | 1,15 | **182,9 kN** | 16,0 |

**Ce que le tableau montre.** Le porteur le plus chargé reste `SF1` (`182,9 kN` — c'est la réaction de `P2` transmise au sol, pas un porteur indépendant). Le poteau le plus chargé reste **`P2` à `159,0 kN`** — soit `−27 %` par rapport à l'indice B. Les ratios `N/A_inf` de `P1`, `P3` et `J1` sont **quasiment inchangés** (`159` au lieu de `177 kN/m²`) : leur charge vient du **mur porté**, pas du plancher.

### 6.3 Justification du classement rive / intermédiaire

| Porteur | Classement | Coefficient | Justification |
|---|---|---|---|
| **P1-N, P1-S** | **Rive** | 1,00 | Extrémités d'une baie de façade : le plancher ne continue pas au-delà |
| **P2** | **Intermédiaire** | 1,15 | En file 5, entre deux travées de plancher continues de part et d'autre |
| **P3, J1** | **Rive** | 1,00 | Appuis de rive des frangements `F1b` et `F1a` — le linteau ne continue pas au-delà |
| **M11, M03** | **Intermédiaire** | 1,15 | Voiles continus sur toute la longueur de la travée, chargés de part et d'autre |
| **SF1** | **Intermédiaire** | 1,15 | Reçoit `P2` avec le même coefficient de continuité que lui |

---

## 7. VÉRIFICATION DE L'HYPOTHÈSE `H-27` DE `B-25`

`B-25 Ind. B` a retenu `σ_d = 0,300 MPa` comme contrainte verticale moyenne sur les voiles, pour calculer `f_vk = (f_vk0 + 0,4 σ_d)/γ_M = 108 kPa`. **Cette valeur n'avait pas été calculée — elle était posée.** `B-21` la vérifie :

| Grandeur | Valeur |
|---|---|
| Charge totale ELU transmise aux voiles | **1 290 kN** |
| Aire portante des 12 voiles RDC (`B-25`) | **18,79 m²** |
| **`σ_d` calculé** | `1 290 / 18,79 = 69 kPa =` **`0,069 MPa`** |
| `σ_d` retenu par `H-27` | **`0,300 MPa`** |
| `f_vk` avec `H-27` | 108 kPa |
| `f_vk` avec la valeur calculée | **71 kPa** |

**Conséquence sur `B-25` :** `H-27` **majore `f_vk` de 52 %** — davantage encore qu'à l'indice B (44 %), puisque la charge descend. En retenant la valeur réellement calculée, `τ/f_vk` passerait de `0,028` à **`0,043`**. **La conclusion de `B-25` est inchangée** (la capacité reste utilisée à moins de 5 %), et l'hypothèse reste **conservatrice dans le sens favorable** — la seule direction acceptable pour une hypothèse de résistance.

> **Ce que ce chiffre confirme, en passant.** `H-27` retient une contrainte `4,3 ×` la contrainte réelle. Ce n'est pas une erreur : c'est une hypothèse déclarée, tracée, et qui va dans le sens de la sécurité. Mais elle **ne doit jamais servir à justifier `B-25`** : c'est `B-25` qui est juste, parce qu'elle est très peu sollicitée — pas l'inverse.

---

## 8. CONTRÔLE DE COHÉRENCE AVEC LE PRÉDIMENSIONNEMENT DE `B-20`

**Ce tableau compare des effets de charge, jamais des résistances.** `M_Ed = p_ELU·L²/8` est un effet des charges ; sa comparaison à `M_el,Rd` relève de `B-45`.

| Élément | `M_Ed` retenu par `B-20` | `M_Ed` calculé par `B-21` | Écart | Conséquence |
|---|---|---|---|---|
| **F1a** | 10,7 kN·m | 8,9 kN·m | **−17 %** | Cohérent |
| **F1b** | 10,7 kN·m | 7,2 kN·m | **−32 %** | Cohérent |
| **F1c** | 10,7 kN·m | 6,4 kN·m | **−40 %** | Cohérent |
| **F2** | 50,0 kN·m | 44,5 kN·m | **−11 %** | Cohérent |
| **F3** | 40,8 kN·m | **59,2 kN·m** | **+45 %** | **`B-45` PRIORITAIRE** |
| **F4** | 20,1 kN·m | 14,1 kN·m | **−30 %** | Cohérent |
| **R1** | 47,5 kN·m | **74,4 kN·m** | **+57 %** | **`B-45` PRIORITAIRE** |
| **R2-N** | 43,5 kN·m | 44,1 kN·m | **+1 %** | Cohérent |
| **R2-S** | 43,5 kN·m | 34,4 kN·m | **−21 %** | Cohérent |

| Poteau | `N_ELU` retenu par `B-20` | `N_ELU` calculé | Écart | Conséquence |
|---|---|---|---|---|
| **P1-N / P1-S** | 45 à 75 kN | **100,3 kN** | **+67 %** | `B-45` — tube `140×140` : capacité ≈ 546 kN, marge conservée |
| **P2** | 85 kN | **159,0 kN** | **+87 %** | **`B-42`** — **re-livrée en Ind. B** : utilisation `0,305` |
| **SF1** (`N_ELS`) | 63,2 kN | **130,5 kN** | **+106 %** | **`B-40`** — voir § 9 |

### 8.1 Ce que le retrait de la recharge change — et ce qu'il ne change pas

Trois écarts **changent de signe** : `F2` passe de `+28 %` à `−11 %`, `R2-N` de `+46 %` à `+1 %`, `R2-S` de `+14 %` à `−21 %`. **Le prédimensionnement de `B-20` n'était donc pas mauvais : il était simplement établi sans la recharge… et la recharge n'était pas là.**

Deux écarts **restent défavorables, divisés par plus de deux** :

| Élément | Écart indice B | Écart indice C | Facteur |
|---|---|---|---|
| `F3` | `+109 %` | **`+45 %`** | ÷ 2,4 |
| `R1` | `+126 %` | **`+57 %`** | ÷ 2,2 |
| `P1-N` | `+86 %` | **`+67 %`** | ÷ 1,3 |
| `P2` | `+156 %` | **`+87 %`** | ÷ 1,8 |
| `SF1` | `+186 %` | **`+106 %`** | ÷ 1,8 |

> **Ce que cela dit de la méthode.** Une erreur de **localisation** de charge se propage à toutes les briques aval sans jamais se voir : chaque calcul est juste, chaque tableau est cohérent, et le résultat est faux. Elle n'a été détectée qu'en **rouvrant les planches** pour vérifier où la recharge était dessinée. C'est exactement ce que `V14` (épuisement des pièces) exige — et ce que `B-21` indice B n'avait pas fait.

---

## 9. `SF1` — LA SEMELLE EN 80 × 80 EST CONFORME

| Grandeur | Valeur |
|---|---|
| Semelle retenue (`D-30`) | **80 × 80 cm = 0,64 m²** |
| Minimum opposable (`D-10` / `D-14`) | 60 × 60 cm — le plancher reste contractuel |
| `N_ELS` selon `B-21` | **130,5 kN** |
| **`σ_ELS`** | `130,5 / 0,64 =` **`204 kPa = 0,20 MPa`** |
| Admissible (`D-02`) | **0,30 MPa** |
| **Verdict** | ✅ **CONFORME** — 68 % de l'admissible |
| Largeur strictement requise | `B ≥ √(130,5 / 300) =` **`0,66 m`** |
| `N_ELU` | `182,9 kN` sur `0,64 m²` = **`286 kPa ≤ 490 kPa`** — conforme |

### 9.1 L'aire d'influence de `P2` reste la question, mais elle ne bloque plus

`B-40 Ind. E` a vérifié `SF1` avec `N_ELS = 63,2 kN`, ce qui correspond à une aire d'influence de **6,5 m²** environ. La trame de `B-20` donne **11,46 m²**. Les deux valeurs ne peuvent pas être vraies en même temps.

| Hypothèse sur `P2` | `A_inf` | `N_ELS` | `σ_ELS` sur 80 × 80 | Verdict |
|---|---|---|---|---|
| Aire d'influence de la **trame** (demi-portées complètes) | 11,46 m² | 130,5 kN | **0,20 MPa** | ✅ **CONFORME** |
| Aire **réduite** : `P2` ne reprend que ce que le portique lui transmettait | ≈ 6,5 m² | ≈ 74 kN | **0,12 MPa** | ✅ Conforme, large |

> **`D-30` reste nécessaire, mais pour une autre raison.** L'indice B justifiait le passage à 80 × 80 par un dépassement de `67 %` en 60 × 60. Avec la recharge au bon endroit, le `60 × 60` donnerait `130,5 / 0,36 = 362 kPa`, soit `121 %` de l'admissible — **encore non conforme, de `21 %`**. Le `80 × 80` ramène la contrainte à `68 %` de l'admissible. **La décision est confirmée, son motif est divisé par trois.**
>
> **Ce qui reste ouvert** : l'aire d'influence réelle de `P2` (`PA-01`, sondage du soubassement), et la portance des alluvions, qui n'est **toujours pas mesurée** (`D-15` : tassements hors mission). `SF1` est conforme **sur l'hypothèse de `D-02`**, pas sur une mesure.

---

## 10. SYNTHÈSE EN HUIT LIGNES

1. **La recharge de `15 cm` est un ouvrage de dallage** (`D-35`) : elle quitte les planchers `A` et `B`, qui passent à `1,80` et `4,71 kN/m²`.
2. **Toutes les poutres de plancher sont soulagées de `30,6 %`** ; les frangements de façade de `6,7 %` seulement, car leur charge est dominée par le mur porté (`38,5 kN/m`).
3. **Le dallage porte plus que tout le reste** : `14,21 kN/m²` à l'ELU sur `111,15 m²`, soit **`1 579 kN`** — au-delà des `1 290 kN` transmis aux voiles. C'est l'ouvrage à traiter **en premier** en `B-43`.
4. **Porteur le plus chargé : `P2`, à `159,0 kN`** (`N_ELU`) ; `SF1` transmet `182,9 kN` au sol et reste conforme en `80 × 80` (`0,20 MPa` à l'ELS contre `0,30` admissible).
5. **Deux éléments restent hors prédimensionnement de `B-20`** : `F3` (**`+45 %`**) et `R1` (**`+57 %`**) — prioritaires en `B-45`, mais deux fois moins qu'annoncé à l'indice B.
6. **Trois écarts changent de signe** (`F2` `−11 %`, `R2-N` `+1 %`, `R2-S` `−21 %`) : le prédimensionnement de `B-20` était juste, il lui manquait… une recharge qui n'était pas là.
7. **`H-27` est vérifiée et très conservatrice** : `σ_d` réel `0,069 MPa` contre `0,300` retenu — `f_vk` majoré de `52 %`.
8. **Hypothèses de charges encore à confirmer en EXE :** `H-28` (densité de la recharge, `22 kN/m³`), `H-29` (toiture, `0,95 kN/m²`), `H-30` (cloisons, `0,80 kN/m²`).

---

## 11. AUTO-CONTRÔLE DES SEPT CRITÈRES D'ACCEPTATION

| # | Critère de la fiche `B-21` | État | Preuve |
|---|---|---|---|
| 1 | Chaque porteur a une surface d'influence justifiée | ✅ **CONFORME** | § 2 — 8 porteurs surfaciques avec `L_t`, `l_t`, `A_inf` et demi-portées ; 14 porteurs linéaires avec bande tributaire |
| 2 | Chaque charge permanente est rattachée à une couche et à un poids volumique | ✅ **CONFORME** | § 3.1, 3.2, 3.4 et **3.6** — 16 couches, chacune avec épaisseur, `γ` et pièce source |
| 3 | Chaque charge d'exploitation est rattachée à une catégorie EC1 | ✅ **CONFORME** | § 4 — cat. B, C4, H et neige, chacune avec sa valeur et sa source |
| 4 | Chaque coefficient de continuité est justifié | ✅ **CONFORME** | § 6.3 — classement rive/intermédiaire justifié porteur par porteur ; `1,00` appliqué à 5 porteurs sur 8 |
| 5 | Les tableaux ELS et ELU sont distincts | ✅ **CONFORME** | § 6.1 et § 6.2 — deux tableaux, deux combinaisons |
| 6 | La sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION » | ✅ **CONFORME** | En-tête et bandeau de tête |
| 7 | Aucune vérification de section ni aucun ferraillage n'a été produit | ✅ **CONFORME** | § 8 compare des **effets de charge** à des effets de charge ; § 9 est un **ordre de grandeur de surface d'assise** renvoyé à `B-40` ; **§ 3.6 donne la charge du dallage, jamais son épaisseur ni son treillis** — le dimensionnement est en `B-43` |

**Verdict de la brique `B-21` (Indice C) : ✅ CONFORME — 7/7.**

> **Sur la révision d'indice.** Le passage de B à C **corrige une erreur de localisation**, contrairement au passage de A à B qui n'enregistrait que des arbitrages. Elle a été trouvée en rouvrant les planches du DCE — pas par un contrôle interne, qui ne pouvait pas la voir : tous les tableaux de l'indice B étaient arithmétiquement justes.
>
> **Critère 7 tenu malgré l'ajout du dallage** : `B-21` produit `14,21 kN/m²` comme **charge**, et ne dit rien de l'épaisseur, du treillis, des joints ni du poinçonnement. La phrase « le dallage sera un problème de fissuration et de désolidarisation » est une **orientation**, pas un dimensionnement.

---

## 12. HYPOTHÈSES CRÉÉES ET TRANSMISSIONS

### 12.1 Hypothèses notifiées

| Code | Hypothèse | Norme d'appui | Si rectifiée |
|---|---|---|---|
| **H-28** | Densité de la recharge **`22 kN/m³`** ; plancher B recalculé à **`3,91 kN/m²`** (au lieu des `3,50` déclarés) | `D4` p. 5 et 14 (épaisseur) + EC1 (densité) | Si sable (`18 kN/m³`) : `−0,60 kN/m²` **sur le dallage**, `p_ELU` de `14,21` à `13,40 kN/m²` (`−6 %`) — conclusion inchangée |
| **H-29** | Toiture à **`0,95 kN/m²`** (tuiles, chevrons, pannes, plafond) | `D2` f. 02 — constitution sans charge | Si ardoises ou béton : `+0,20 kN/m²` — effet < 5 % sur `F4` |
| **H-30** | Cloisons forfaitaires **`0,80 kN/m²`** | EC1-1-1 § 6.3.1.2 | Si cloisons lourdes (`1,20`) : `+0,40 kN/m²` sur planchers **et** dallage |
| **H-31** | ~~Salle de sport R+1 en catégorie C4~~ — **PROMUE DÉCISION `D-31`** le 20/10/2026 | EC1-1-1 tableau 6.1 | N'est plus une hypothèse. Sortie du registre, inscrite au RDR |

### 12.2 Transmissions aux briques aval

| Brique | Ce qu'elle reçoit de `B-21 Ind. C` |
|---|---|
| **`B-43`** | **Le dallage en priorité** : `g = 7,75 kN/m²`, `q = 2,50`, **`p_ELU = 14,21 kN/m²` sur 100 % de l'emprise** (`D-35`). Puis les planchers : `A` `1,80` / `B` `4,71 kN/m²`, solives `8 × 18` @ `0,50 m` et `IPE 160` @ `0,72 m` |
| **`B-40`** | `SF1` : **`N_ELS = 130,5 kN`**, `σ = 0,20 MPa` en `80 × 80` — **conforme** ; l'aire d'influence de `P2` reste à confirmer (`PA-01`). Le **dallage** y entre aussi : `D-35` ajoute `15 cm` de recharge au-dessus du dallage BA `13 cm` |
| **`B-42`** | `P2` : `N_ELU = 159,0 kN` (au lieu de `217,7`) · `P3` : `35,8` · `J1` : `39,8` — **repris dans la note `Ind. B`** : sections et ferraillage inchangés, utilisation `0,305` |
| **`B-45`** | **`F3` (`+45 %`)** et **`R1` (`+57 %`)** en priorité ; `F2`, `R2-N`, `R2-S` revenus dans l'enveloppe ; `P1` à `100,3 kN` (capacité `546 kN`, marge conservée) |
| **`B-46`** | Réactions aux sommiers `S1`/`S2` ; `σ_d = 0,069 MPa` pour la maçonnerie (au lieu de `0,094`) |
| **`B-25`** | `H-27` vérifiée et **encore plus conservatrice** (`f_vk` majoré de `52 %`) ; `τ/f_vk` recalculé `0,043` — conclusion inchangée |
| **`B-24`** | **`R-24-B1` close par `D-35`** ; l'élément `E-03` (solives) est vérifié par `B-43`, pas par `B-24` |

### 12.3 Point d'arrêt

Aucun point d'arrêt chantier n'est créé par `B-21`. Deux points d'arrêt restent ouverts et **la révision d'indice ne les ferme pas** :

- **`PA-01`** — reconnaissance du soubassement sous `P2`, qui décide de l'aire d'influence réelle ;
- **`PA-02`** — liaison charpente-maçonnerie.

**L'emprise exacte de la recharge n'est plus un point d'arrêt** : `D-35` l'absorbe par hypothèse défavorable. Elle reste une question à poser à la MOE pour le **calepinage** du dallage (zones rechargées / non rechargées), pas pour son calcul.

---

## 13. POINT DE CONTRÔLE HUMAIN

**Tranché le 20/10/2026.** `D-28` (aucun joint), `D-30` (`SF1` 80 × 80), `D-31` (catégorie C4) et `D-32` (`2,50 kN/m²` partout) sont consignées. **Aucune de ces quatre décisions ne modifie un chiffre de cette note** : elles convertissent des valeurs conditionnelles en valeurs opposables.

**Reste ouvert, et ne relève pas de cette brique : `D-29`** — *le contreventement en service est la maçonnerie existante seule*. Cette décision est portée par `B-25` (§ 10), pas par `B-21` ; elle conditionne la lecture de `σ_d = 0,069 MPa` au § 7 et donc la requalification de `H-27`. **Tant que `D-29` est ouverte, `H-27` reste une hypothèse vérifiée mais non arbitrée.**

**Reste ouvert côté client : `T-04`** — la note de stabilité provisoire à demander à la MOE structure de conception, avec les grandeurs du § 6.2 de `B-25`.

**Brique B-21 re-livrée en indice C — en attente de votre GO ou de vos observations.**
