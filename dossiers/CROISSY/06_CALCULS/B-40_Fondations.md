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
| Plan combiné (implantation + type) | `_plans/FLORA_FONDATIONS_TYPE_IndF.dxf` (2 770 141 o · audit **0 erreur**) · `.pdf` · `.png` *(sur fond `B-32 Ind. D` sans cloisons ni isolation)* |
| **Indice** | **F** *(remplace l'indice E du 20/10/2026 — `SF1` portée à **80 × 80 × 25** par `D-30` et **dallage rechargé sur 100 % de son emprise** par `D-35`)* |
| Date | **20/10/2026** |
| Statut | ✅ **IMPLANTÉ & CONFORME EN PARTIEL-DÉCLARÉ** *(soumis aux réceptions de fouilles `D-09` et nuages `D-19`)* |
| Brique amont | **`B-21 Ind. C`** — `N_ELS(SF1) = 130,5 kN` · `N_ELU = 182,9 kN` · dallage `14,21 kN/m²` |
| Brique aval liée | **B-50** (ancrages / platines / attentes) · **B-60** (plans d'exécution) |

---

## 0. PRESCRIPTION D'EXÉCUTION OPPOSABLE (`ENC v3` — FDC IND. F)

1. **Arase inférieure des fondations nouvelles : `−1,00 m` par rapport au terrain naturel, MINIMUM (`D-08 / D-09 / D-12`).** Cote plancher : elle peut être approfondie, **jamais remontée**.
2. **Encastrement minimal dans les alluvions anciennes : `0,50 m`** (toit des alluvions déduit à `−0,50 m`) ; contraintes admissibles **`q_ELS ≤ 0,30 MPa`**, **`q_ELU ≤ 0,49 MPa`** (`G2 AVP GEOEXPERTS` + `D-02 / D-03`).
3. **Dimension minimale absolue : `60 × 60 cm` (`D-14`).** La semelle `25 × 25 cm` indiquée au plan `D2 Folio 01 / Folio 03` (`EXI-07a`) est portée à **`60 × 60 × 30 cm BA` minimum** (type courant) et à **`80 × 80 × 25 cm`** pour `SF1` sous `P2` (`D-30`, § 2.3).
4. **Égalisation obligatoire avec l'existant (`D-09`)** : à l'ouverture des fouilles, l'entreprise vérifie systématiquement le niveau des fondations existantes adjacentes. **Si la fondation existante est plus profonde**, descendre à son niveau et rattraper l'écart **sous la semelle BA par du gros béton `C16/20`**. **Si l'existant est moins profond**, maintenir `−1,00 m / TN` minimum sans jamais déchausser l'existant.
5. **Absence de nappe phréatique déclarée (`D-16`)** : toute venue d'eau constitue un **point d'arrêt** avec constat contradictoire.
6. **Tassements hors mission GO (`D-15`)** : ils relèvent de la mission géotechnique (`GEOEXPERTS`) et ne sont pas vérifiés dans la présente note (ni absolus, ni différentiels).
7. **Réception contradictoire de fond de fouille obligatoire (`D-13`)** avant coulage du gros béton / béton de propreté.
8. **Dallage rechargé sur 100 % de son emprise (`D-35`)** : la recharge de sol de `15 cm` (`3,30 kN/m²`) est réputée couvrir **toute la surface du dallage** (`111,15 m²`), par hypothèse défavorable. Charge de calcul du dallage : **`g = 7,75` · `q = 2,50` ⇒ `p_ELS = 10,25` · `p_ELU = 14,21 kN/m²`**. Le dallage repose sur le fond de forme `40 cm` (`D2` f. 03) et **ne reporte rien sur les semelles** : il transmet directement au sol.

---

## 1. IMPLANTATION EN PLAN DES OUVRAGES D'INFRASTRUCTURE (`PLS` — LEVÉE TOTALE DE LA RÉSERVE DE L'INDICE D)

Grâce au calage vectoriel exact `D2 ↔ D5` établi en **B-20 Ind. B** (échelle exacte `1/80`, résidu médian `21,0 mm`), **tous les ouvrages d'infrastructure sont désormais implantés et cotés sur la vue en plan nettoyée du RDC (`FLORA_FONDATIONS_TYPE_IndF` et `FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB`)** :

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

### 2.2 Charges surfaciques conservatoires (`CHG-02 / CHG-03`, `D-35`)

**Deux charges distinctes, deux destinations distinctes.** Les fondations reprennent les **planchers hauts** ; le dallage repose sur le sol et ne charge aucune semelle.

| Destination | `g` (kN/m²) | `q` (kN/m²) | `p_ELS` | `p_ELU` | Source |
|---|---|---|---|---|---|
| **Fondations** (planchers hauts, cloisons incluses) | **`4,71`** | `2,50` | **`7,21`** | **`10,11`** | `B-21 Ind. C` § 3.5 — **sans recharge** (`D-35`) |
| **Dallage** (BA `13 cm` + revêtement + **recharge `15 cm`** + cloisons) | **`7,75`** | `2,50` | **`10,25`** | **`14,21`** | `B-21 Ind. C` § 3.6 — **100 % de l'emprise** (`D-35`) |

> **Pourquoi le dallage n'entre pas dans la descente de charges des semelles.** Un dallage désolidarisé posé sur un fond de forme `40 cm` transmet sa charge **au sol**, sur toute sa surface — pas aux semelles. L'ajouter à `SF1` serait une faute de modèle : cela compterait deux fois le même sol. `D-35` demande de **dimensionner le dallage** pour la recharge, pas de la reporter sur les fondations.

### 2.2 bis Le dallage sous `D-35` — ce que `B-40` en dit, et ce qu'il n'en dit pas

| Grandeur | Valeur | Verdict |
|---|---|---|
| `p_ELU` du dallage | **`14,21 kN/m²` = `14,2 kPa`** | — |
| `q_ELU` admissible du sol (`D-03`) | `490 kPa` | **`2,9 %`** de l'admissible |
| `q_ELS` admissible (`D-02`) | `300 kPa` | `p_ELS = 10,25 kPa` ⇒ **`3,4 %`** |
| Portance du dallage | — | ✅ **Sans objet** : le sol est sollicité à moins de 4 % de sa capacité |

**Le dallage ne se dimensionne donc pas en portance, il se dimensionne en fissuration et en désolidarisation** — épaisseur, treillis, joints de retrait, poinçonnement local sous charges concentrées. **Ce dimensionnement appartient à `B-43`**, qui le porte sous sa forme complète. `B-40` livre ici la **charge** et la **preuve que le sol ne la voit pas**.

### 2.3 Vérification directe de `SF1` sous le poteau `P2` — `80 × 80 × 25` (`D-30`)

Les efforts sont repris **tels quels** de `B-21 Ind. C` (coefficient de continuité `1,15` et poids propre inclus) — `B-40` ne les recalcule pas, il les oppose à la portance.

| Grandeur | Valeur | Comparaison | Verdict |
|---|---|---|---|
| Semelle retenue (`D-30`) | **`80 × 80 × 25 cm` = `0,640 m²`** | — | — |
| `N_ELS` (`B-21 Ind. C`) | **`130,5 kN`** | `σ_ELS = 130,5 / 0,640 =` **`0,204 MPa`** ≤ `0,300` | ✅ `68 %` de l'admissible |
| `N_ELU` (`B-21 Ind. C`) | **`182,9 kN`** | `σ_ELU = 182,9 / 0,640 =` **`0,286 MPa`** ≤ `0,490` | ✅ `58 %` de l'admissible |

**Pourquoi `80 × 80` et pas `60 × 60`.** En `60 × 60` (`0,36 m²`), `σ_ELS` vaudrait `362 kPa`, soit `121 %` de l'admissible — **non conforme de 21 %**. `D-30` reste donc nécessaire : ce n'est plus un dépassement de `67 %` (chiffre de `B-21 Ind. B`, fondé sur une recharge mal placée), c'est `21 %`.

**Autres points sous réserve de fouille.** Si `Z-P1N`, `Z-P1S` ou `Z-P3` devaient recevoir une semelle neuve `60 × 60 × 30 cm`, toute descente de charge correspondant à l'abaque du § 3 (`A ≤ 14 m²` avec `60 × 60`) est **directement couverte par le type** — avec les charges de l'indice C, plus basses.

---

## 3. ABAQUE COMPLET DE SENSIBILITÉ `B(A)` — PORTANCE ELS / ELU

Charges du § 2.2 (fondations, **sans recharge**) : `p_ELS = 7,21` · `p_ELU = 10,11 kN/m²`. Épaisseur type `30 cm`, poids propre de semelle inclus.

| Aire d'influence `A` (m²) | Côté retenu `B` (m) | `N_ELS` (kN) | `σ_ELS` (MPa) ≤ `0,30` | `N_ELU` (kN) | `σ_ELU` (MPa) ≤ `0,49` | Verdict |
|---|---|---|---|---|---|---|
| **6,5** | **0,60 m** | 49,6 | 0,138 | 69,4 | 0,193 | ✅ **CONFORME** |
| **9,0** | **0,60 m** | 67,6 | 0,188 | 94,6 | 0,263 | ✅ **CONFORME** |
| **11,0** | **0,60 m** | 82,0 | 0,228 | 114,8 | 0,319 | ✅ **CONFORME** |
| **12,0** | **0,60 m** | 89,2 | 0,248 | 124,9 | 0,347 | ✅ **CONFORME** |
| **14,0** *(limite du `60 × 60`)* | **0,60 m** | 103,6 | 0,288 | 144,6 | 0,402 | ✅ **CONFORME** |
| **15,0** | **0,65 m** | 111,3 | 0,263 | 155,9 | 0,369 | ✅ **CONFORME** |
| **18,0** | **0,70 m** | 133,5 | 0,272 | 186,9 | 0,381 | ✅ **CONFORME** |
| **21,0** | **0,75 m** | 155,6 | 0,277 | 218,0 | 0,388 | ✅ **CONFORME** |
| **24,0** | **0,80 m** | 177,8 | 0,278 | 249,1 | 0,389 | ✅ **CONFORME** |
| **`SF1` / `P2`** *(cas particulier)* | **`0,80 m`** (`D-30`) | **130,5** | **0,204** | **182,9** | **0,286** | ✅ **CONFORME** |

> **L'abaque a été refait, pas retouché.** L'indice E tablait sur `g = 6,80` et un `60 × 60` jusqu'à `11,3 m²`. L'indice F tablit sur `g = 4,71` (plancher seul) : un `60 × 60` couvre désormais **`14 m²`**, un `80 × 80` **`24 m²`**. La ligne `SF1` sort du calcul `p·A` parce que sa charge ne vient pas d'une bande tributaire : elle est **produite par `B-21`** (`130,5 kN`, continuité incluse).

---

## 4. FERRAILLAGE, RIGIDITÉ, POINÇONNEMENT & NOTE PORTANCE `D-24 / R-36`

- **Rigidité (`EC2 §9.8.3`)** : `d = 242 mm ≥ (B − b) / 4` pour le type `60 × 60 × 30` (`75 mm`) ; pour `SF1` `80 × 80 × 25`, `d = 192 mm ≥ (800 − 250) / 4 = 138 mm` ✅.
- **Flexion & Section minimale (`EC2 §9.2.1.1`)** : type `60 × 60` à `A = 12 m²`, `M_Ed = 2,34 kN·m → A_s,calc = 41 mm²/m`, gouverné par **`A_s,min = 323 mm²/m`** → **choix retenu : `HA8 e150` dans les deux sens (`335 mm²/m`, soit `4 HA8` par direction pour `60 × 60`, `5 HA8` pour `70 × 70`, `6 HA8` pour `80 × 80`)**.
- **Poinçonnement (`EC2 §6.4`) — `SF1` `80 × 80 × 25`** : `v_Ed = 0,279 MPa ≤ v_Rd,c = 0,392 MPa` (`taux = 71 %` — ✅ OK sans armatures de poinçonnement). L'indice E annonçait `45 %` ; le passage à `h = 25 cm` **réduit `d`** et fait monter le taux. **La marge reste suffisante, elle n'est plus confortable** : aucune réduction d'épaisseur sous `25 cm` n'est admise.
- **Justification attachée à `D-24` (fermeture technique de `R-36`)** : avec `B = 0,60 m` et un toit des alluvions anciennes à `−0,50 m` pour une arase inférieure à `−1,00 m / TN mini` (`D-08`), la fiche d'encastrement effectif dans l'horizon porteur graveleux est de **`D_e = 0,50 m`**, soit **`D_e / B = 0,83`**, et la totalité du bulbe de poinçonnement sous la base (`−1,00 m` à `−1,90 m`) se développe **intégralement au sein des alluvions anciennes compactes** (aucune couche molle sous-jacente identifiée dans `D2 p. 1`), sous contrainte modérée (`σ_ELS(SF1) = 0,204 MPa`, soit **68 %** de `q_ELS = 0,30 MPa`). Sous réserve de la réception visuelle contradictoire du fond de fouille (`ENC v3 alinéa 10`), le maintien de `−1,00 m / TN mini` (`D-24`) est **mécaniquement cohérent** pour `SF1`.

---

## 5. VERDICT DE LA BRIQUE `B-40` (INDICE F)

**Statut : ✅ CONFORME EN MODE PARTIEL-DÉCLARÉ — FONDATIONS IMPLANTÉES SUR VUE EN PLAN NETTOYÉE (`PLS`).**

La planche `_plans/FLORA_FONDATIONS_TYPE_IndF` (`.dxf`, `.pdf`, `.png`) réunit sur un seul support sans cloisons ni isolation **l'implantation cotée de toutes les zones de fondations** et **les détails d'exécution Plan + Coupe A-A ferraillés**, avec la note `D-09` reproduite intégralement mot pour mot.
