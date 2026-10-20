# B-40 — FONDATIONS SUPERFICIELLES & IMPLANTATION « PLS »

> **NOTE OBLIGATOIRE D-09 — REPRODUITE INTÉGRALEMENT EN TÊTE DE LA NOTE DE CALCUL :**
> **« AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON... CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »**

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 — Articles P1 à P8 intégrés |
| Brique | **B-40** — Fondations superficielles & Plan d'implantation « PLS » (`D-11`) |
| Phase | **4 — Calculs d'exécution** |
| **Mode d'appel** | **PARTIEL-DÉCLARÉ** — enveloppe haute sur `CHG-02 / CHG-03` ; reconnaissance en fouille sur nuages `D-19` |
| Régime | **OUTILLÉ (V13)** — script `b40_fondations.py` exécuté, journal 8 sections, audit DXF `0 erreur` |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b40_fondations.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b40_fondations.txt` |
| Plan combiné (implantation + type) | `_plans/FLORA_FONDATIONS_TYPE_IndE.dxf` (2 770 072 o) · `.pdf` · `.png` *(sur fond `B-32 Ind. D` sans cloisons ni isolation)* |
| **Indice** | **E** *(remplace l'indice D du 19/10/2026 — ajoute l'implantation complète en vue en plan)* |
| Date | **20/10/2026** |
| Statut | ✅ **IMPLANTÉ & CONFORME EN PARTIEL-DÉCLARÉ** *(soumis aux réceptions de fouilles `D-09` et nuages `D-19`)* |
| Brique aval liée | **B-50** (ancrages / platines / attentes) · **B-60** (plans d'exécution) |

---

## 0. PRESCRIPTION D'EXÉCUTION OPPOSABLE (`ENC v3` — FDC IND. F)

1. **Arase inférieure des fondations nouvelles : `−1,00 m` par rapport au terrain naturel, MINIMUM (`D-08 / D-09 / D-12`).** Cote plancher : elle peut être approfondie, **jamais remontée**.
2. **Encastrement minimal dans les alluvions anciennes : `0,50 m`** (toit des alluvions déduit à `−0,50 m`) ; contraintes admissibles **`q_ELS ≤ 0,30 MPa`**, **`q_ELU ≤ 0,49 MPa`** (`G2 AVP GEOEXPERTS` + `D-02 / D-03`).
3. **Dimension minimale absolue : `60 × 60 cm` (`D-14`).** La semelle `25 × 25 cm` indiquée au plan `D2 Folio 01 / Folio 03` (`EXI-07a`) est portée à **`60 × 60 × 30 cm BA` minimum (`SF1`)**.
4. **Égalisation obligatoire avec l'existant (`D-09`)** : à l'ouverture des fouilles, l'entreprise vérifie systématiquement le niveau des fondations existantes adjacentes. **Si la fondation existante est plus profonde**, descendre à son niveau et rattraper l'écart **sous la semelle BA par du gros béton `C16/20`**. **Si l'existant est moins profond**, maintenir `−1,00 m / TN` minimum sans jamais déchausser l'existant.
5. **Absence de nappe phréatique déclarée (`D-16`)** : toute venue d'eau constitue un **point d'arrêt** avec constat contradictoire.
6. **Tassements hors mission GO (`D-15`)** : ils relèvent de la mission géotechnique (`GEOEXPERTS`) et ne sont pas vérifiés dans la présente note (ni absolus, ni différentiels).
7. **Réception contradictoire de fond de fouille obligatoire (`D-13`)** avant coulage du gros béton / béton de propreté.

---

## 1. IMPLANTATION EN PLAN DES OUVRAGES D'INFRASTRUCTURE (`PLS` — LEVÉE TOTALE DE LA RÉSERVE DE L'INDICE D)

Grâce au calage vectoriel exact `D2 ↔ D5` établi en **B-20 Ind. B** (échelle exacte `1/80`, résidu médian `21,0 mm`), **tous les ouvrages d'infrastructure sont désormais implantés et cotés sur la vue en plan nettoyée du RDC (`FLORA_FONDATIONS_TYPE_IndE` et `FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB`)** :

| Repère plan | Nature de l'ouvrage | Position DXF `(X ; Y)` | Repère `B-30` `(X ; Y)` | Dimensions & Prescription | Statut |
|---|---|---|---|---|---|
| **`SF1`** | **Semelle isolée BA neuve sous poteau `P2 (15×25 BA)`** *(remplacement poteau + allège façade Ouest Nord, `EXI-07a`)* | `X = 95,35 m` · `Y = 59,29 m` | `+9,48 m` · `+14,87 m` | **`60 × 60 × 30 cm BA mini`** (`C25/30`, `HA8 e150` croisés, `c_nom = 50 mm`) + béton propreté `5 cm` + gros béton `D-09` | **CERTAIN (Contractuel D2 + D-14)** |
| **`Z-P1N`** | Pied du poteau métallique **`P1-N (tube 140×140 S275)`** en façade Ouest Sud | `X = 95,41 m` · `Y = 49,04 m` | `+9,54 m` · `+4,62 m` | `D2 Folio 03` prescrit *« vérification du soubassement »* moellons. **Si soubassement insuffisant en fouille : création d'une semelle type `60 × 60 × 30 cm BA` (`D-14`) + gros béton `D-09`** | **Nuage `D-19`** *(validation client / fouille)* |
| **`Z-P1S`** | Pied du poteau métallique **`P1-S (tube 140×140 S275)`** en façade Ouest Sud | `X = 95,41 m` · `Y = 47,78 m` | `+9,54 m` · `+3,36 m` | Idem `Z-P1N` : vérification soubassement moellons ou création semelle type **`60 × 60 × 30 cm BA`** | **Nuage `D-19`** *(validation client / fouille)* |
| **`Z-P3`** | Pied du poteau BA **`P3 (50×40 BA)`** au refend Nord du hall | `X = 94,09 m` · `Y = 54,89 m` | `+8,22 m` · `+10,46 m` | Appui sur soubassement du refend existant — reconnaissance à l'ouverture des fouilles + gros béton `C16/20` (`D-09`) ou semelle `60×60` mini | **Nuage `D-19`** *(validation client / fouille)* |
| **`Z-J1`** | Pied du jambage BA **`J1 (24×50 BA)`** dans le refend central | `X = 89,78 m` · `Y = 54,52 m` | `+3,91 m` · `+10,09 m` | Appui sur soubassement moellons `50 cm` — reconnaissance en fouille (`D-09`) | **Nuage `D-19`** *(validation client / fouille)* |
| **`BECHE`** | **Bêche BA de réhausse niveau dallage** Sud-Est (`EXI-07c`) | `X = 86,67 → 89,53 m` · `Y = 46,77 m` | `+0,80 → +3,66 m` · `+2,34 m` | Épaisseur `20 cm`, longueur `2,85 m`, BA `C25/30` | **Contractuel D2 Folio 03 / D1 p. 27** |
| **`RSO-PASS`** | **Reprise en sous-œuvre des semelles de la passerelle château** (`EXI-07e`) | `X = 87,70 → 93,50 m` · `Y = 63,3 → 64,3 m` | `+1,83 → +7,63 m` · `+18,9 → +19,9 m` | **Passes alternées `≤ 1,00 m` (`H-13`) en gros béton `C16/20`** jusqu'aux alluvions anciennes (`≥ −1,00 m/TN`) + traitement joint de dilatation | **Contractuel D2 Folio 04** |

---

## 2. MATÉRIAUX & DESCENTE DE CHARGES D'EXÉCUTION

### 2.1 Caractéristiques de calcul EC2

- Béton **`C25/30`** : `f_ctm = 2,56 MPa` · `f_cd = 0,85 × 25 / 1,5 = 14,17 MPa` · `γ_b = 25,0 kN/m³`
- Gros béton **`C16/20`** : `f_ck = 16 MPa` (rattrapage d'assise sous semelles et passes RSO)
- Acier BA **`S500B`** : `f_yk = 500 MPa` · `f_yd = 500 / 1,15 = 434,8 MPa`
- Enrobage nominal en fondation : **`c_nom = 50 mm`** (`D-06`) → hauteur utile `d = 300 − 50 − 8 = 242 mm`

### 2.2 Charges surfaciques conservatoires (enveloppe haute `CHG-02 / CHG-03`)

- Permanente enveloppe haute : **`g = 6,80 kN/m²`** (`3,50 kN/m²` plancher B voutains D2 + `3,30 kN/m²` recharge 15 cm D4)
- Exploitation cabinet paramédical : **`q = 2,50 kN/m²`** (`D2 p. 1`)
- Combinaisons EC0 : **`p_ELS = g + q = 9,30 kN/m²`** · **`p_ELU = 1,35·g + 1,50·q = 12,93 kN/m²`**

### 2.3 Vérification directe de `SF1` sous le poteau `P2` (portique façade Ouest Nord)

Pour une aire d'influence tributaire conservatoire de **`A(P2) = 6,50 m²`** et un poids propre de semelle `W_SF1 = 0,60² × 0,30 × 25 = 2,70 kN` :

$$N_{ELS}(SF1) = 9{,}30 \times 6{,}50 + 2{,}70 = \mathbf{63{,}2\ kN} \le 108{,}0\ \text{kN} \quad (\sigma_{ELS} = \mathbf{0{,}175\ MPa} \le 0{,}300\ \text{MPa})$$

$$N_{ELU}(SF1) = 12{,}93 \times 6{,}50 + 1{,}35 \times 2{,}70 = \mathbf{87{,}7\ kN} \le 176{,}4\ \text{kN} \quad (\sigma_{ELU} = \mathbf{0{,}244\ MPa} \le 0{,}490\ \text{MPa})$$

Même si `Z-P1N`, `Z-P1S` ou `Z-P3` devaient recevoir une semelle neuve `60 × 60 × 30 cm` après ouverture de fouille, toute descente de charge correspondant à **`A ≤ 11,3 m²`** (`N_ELS ≤ 108,0 kN`, `N_ELU ≤ 176,4 kN`) est **directement couverte par la semelle type `60 × 60 × 30 cm`**.

---

## 3. ABAQUE COMPLET DE SENSIBILITÉ `B(A)` — PORTANCE ELS / ELU

| Aire d'influence `A` (m²) | Côté retenu `B` (m) | `N_ELS` (kN) | `σ_ELS` (MPa) ≤ `0,30` | `N_ELU` (kN) | `σ_ELU` (MPa) ≤ `0,49` | Verdict |
|---|---|---|---|---|---|---|
| **6,5 *(cas `SF1 / P2`)*** | **0,60 m** | **63,2** | **0,175** | **87,7** | **0,244** | ✅ **CONFORME** |
| **9,0** | **0,60 m** | 86,4 | 0,240 | 120,0 | 0,333 | ✅ **CONFORME** |
| **11,0** *(max `60×60` = `11,3 m²`)* | **0,60 m** | 105,0 | 0,292 | 145,9 | 0,405 | ✅ **CONFORME** |
| **12,0** *(réf. ferraillage)* | **0,65 m** | 114,8 | 0,272 | 159,4 | 0,377 | ✅ **CONFORME** |
| **15,0** | **0,70 m** | 143,2 | 0,292 | 198,9 | 0,406 | ✅ **CONFORME** |
| **18,0** | **0,80 m** | 172,2 | 0,269 | 239,2 | 0,374 | ✅ **CONFORME** |
| **21,0** | **0,85 m** | 200,7 | 0,278 | 278,8 | 0,386 | ✅ **CONFORME** |
| **24,0** | **0,90 m** | 229,3 | 0,283 | 318,5 | 0,393 | ✅ **CONFORME** |

---

## 4. FERRAILLAGE, RIGIDITÉ, POINÇONNEMENT & NOTE PORTANCE `D-24 / R-36`

- **Rigidité (`EC2 §9.8.3`)** : `d = 242 mm ≥ (B − b) / 4` vérifié pour `B = 0,60 m` (`75 mm`), `0,70 m` (`100 mm`) et `0,80 m` (`125 mm`), et jusqu'à `B = 1,27 m`.
- **Flexion & Section minimale (`EC2 §9.2.1.1`)** : pour `B = 0,65 m` (`N_Ed = 159,4 kN`), `M_Ed = 3,76 kN·m → A_s,calc = 61 mm²/m`, gouverné par **`A_s,min = 323 mm²/m`** → **choix retenu : `HA8 e150` dans les deux sens (`335 mm²/m`, soit `4 HA8` par direction pour `60 × 60`, `5 HA8` pour `70 × 70`, `6 HA8` pour `80 × 80`)**.
- **Poinçonnement (`EC2 §6.4`)** : `v_Ed = 0,155 MPa ≤ v_Rd,c = 0,347 MPa` (`taux = 45 %` — ✅ OK sans armatures de poinçonnement).
- **Justification attachée à `D-24` (fermeture technique de `R-36`)** : avec `B = 0,60 m` et un toit des alluvions anciennes à `−0,50 m` pour une arase inférieure à `−1,00 m / TN mini` (`D-08`), la fiche d'encastrement effectif dans l'horizon porteur graveleux est de **`D_e = 0,50 m`**, soit **`D_e / B = 0,83`**, et la totalité du bulbe de poinçonnement sous la base (`−1,00 m` à `−1,90 m`) se développe **intégralement au sein des alluvions anciennes compactes** (aucune couche molle sous-jacente identifiée dans `D2 p. 1`), sous contrainte modérée (`σ_ELS(SF1) = 0,175 MPa`, soit **58 %** de `q_ELS = 0,30 MPa`). Sous réserve de la réception visuelle contradictoire du fond de fouille (`ENC v3 alinéa 10`), le maintien de `−1,00 m / TN mini` (`D-24`) est **mécaniquement cohérent** pour `SF1`.

---

## 5. VERDICT DE LA BRIQUE `B-40` (INDICE E)

**Statut : ✅ CONFORME EN MODE PARTIEL-DÉCLARÉ — FONDATIONS IMPLANTÉES SUR VUE EN PLAN NETTOYÉE (`PLS`).**

La planche `_plans/FLORA_FONDATIONS_TYPE_IndE` (`.dxf`, `.pdf`, `.png`) réunit sur un seul support sans cloisons ni isolation **l'implantation cotée de toutes les zones de fondations** et **les détails d'exécution Plan + Coupe A-A ferraillés**, avec la note `D-09` reproduite intégralement mot pour mot.
