# B-50 — ASSEMBLAGES ET ANCRAGES

> **NOTE OBLIGATOIRE `D-09` — REPRODUITE EN TÊTE DE LA NOTE :**
> **« AU MÊME NIVEAU QUE LES FONDATIONS EXISTANTES… RAJOUTER DU GROS BÉTON… CETTE NOTE EST À INDIQUER SUR LES PLANS ET NOTE DE CALCULS »** — appliquée ici à l'ancrage `A1` : les `6 HA12` de `P2` descendent dans `SF1` **au-dessus du gros béton**, jamais dans la maçonnerie de rattrapage.
>
> **`D-28` — AUCUN JOINT DE DILATATION.** Aucun assemblage ne franchit un joint : les platines d'about s'arrêtent à `20 mm` du nu de l'appui.

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-50** — Assemblages et ancrages (brique pivot aval) |
| Phase | **4 — Calculs d'exécution** (après `B-45`) |
| **Mode d'appel** | **PARTIEL-DÉCLARÉ** — les capacités de boulonnerie et les ancrages BA sont **calculées** (EC3-1-8, EC2 § 8.4, EC5 § 8.2) ; les **scellements dans la maçonnerie** et les **sabots** exigeraient des **fiches techniques** — la FDC les exclut (`D-05`, `DOC-09` = fiches de prédalles, `B-48` sans objet) |
| Famille | **TOUS** — ancrages BA, assemblages métalliques, assemblages bois, scellements maçonnerie |
| Régime | **OUTILLÉ (V13)** — calcul intégral par script, journal et JSON conservés |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b50_assemblages.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b50_assemblages.txt` (10 691 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b50_assemblages.json` (374 o) |
| Sortie graphique | `_plans/FLORA_B50_ASSEMBLAGES_IndA.dxf` (79 292 o · AC1032 · audit **0 erreur**) · `.pdf` (633 352 o) · `.png` (649 302 o) |
| **Indice** | **A** — création de la brique |
| Date | **21/10/2026** |
| Brique suivante | **`B-60`** (plans d'exécution cotés) · **`B-46`** (appuis sur maçonnerie) |

> **Ce que cette brique fait.** Elle prend les efforts que les briques amont ont calculés et les transforme en **connecteurs dimensionnés** : longueur d'ancrage des `6 HA12` de `P2` dans `SF1`, boulonnerie du moisage `R1`, torsion du linteau `R3`, scellement des entretoises `Stab1`, platine de pied `P1`. Puis elle fait le **contrôle croisé** : ce qui est calculé tient-il dans ce que les autres briques ont prévu ?
>
> **Ce qu'elle ne fait pas, et qui est le cœur de la brique.** Elle **ne corrige rien**. Si un assemblage ne rentre pas, elle **signale, identifie la brique responsable et renvoie**. C'est la règle de circulation : `B-50` n'agrandit pas une semelle, n'affaiblit pas un boulon, ne réduit pas une barre.

---

## 0. RÉPONSE DIRECTE — QUATRE ASSEMBLAGES SUR SIX SONT CONFORMES

| Réf. | Assemblage | Verdict |
|---|---|---|
| **`A1`** | `6 HA12` de `P2` dans `SF1` | ✅ **CONFORME** — `l_bd = 166 mm` pour `200 mm` disponibles |
| **`A2`** | Moisage `R1` — `10 M16 8.8` par face | ✅ **CONFORME** — taux **`0,69`**, et **c'est le bois qui gouverne** |
| **`A3`** | Linteau `R3` — torsion du `UPE 200` | ⛔ **NON CONFORME** — `τ = 222 MPa` pour `159` admis : **taux `1,40`** |
| **`A4`** | `Stab1` — scellement dans le voutain | ⚠️ **NON CALCULABLE** — fiche technique absente (`DOC-09` exclue) et `f_k` non mesuré |
| **`A5`** | Platine de pied `P1` sur `SF1` | ✅ **CONFORME** — pression diamétrale `0,12` |
| **`A6`** | 8 appuis sur maçonnerie | ⤴ **RENVOI** à `B-46` — c'est `f_k` qui décide |

**Le résultat qui compte est `A3`, et il contredit `B-45`.** `B-45` avait trouvé le `UPE 200` de `R3` conforme en flexion à `0,291` — et c'était juste, **mais incomplet**. Un `U` est un profilé **ouvert et asymétrique** : la charge tombe sur l'axe de l'âme, l'axe de cisaillement est à `40 mm` de là, et il en résulte un moment de torsion `M_t = 1,85 kN·m`. Calculé à la Saint-Venant sur `I_T = 96 000 mm⁴`, cela donne **`τ_t = 222 MPa` pour `159 MPa` admissibles**.

**Le linteau `R3` est donc non conforme — non pas en flexion, mais en torsion.** Et ce n'est pas un défaut de `B-50` : c'est exactement ce que `B-45` avait signalé comme « torsion non reprise par le `U` seul, renvoi `B-50` ». Le renvoi a produit son verdict.

---

## 1. GLOSSAIRE DES CODES

| Code | Objet en clair |
|---|---|
| `A1` à `A6` | Assemblages de la présente note (ancrage BA, moisage, torsion, scellement, platine, appuis) |
| `f_bd` | Contrainte d'adhérence acier/béton (EC2 § 8.4.2) |
| `l_b,rqd` / `l_bd` | Longueur d'ancrage de référence / de calcul |
| `α1…α5` | Coefficients réducteurs d'ancrage (EC2 § 8.4.4, tableau 8.2) |
| `F_v,Rd` | Résistance de calcul d'un boulon au cisaillement |
| `f_h,k` | Résistance caractéristique à l'écrasement local du bois (EC5 § 8.5.1.1) |
| `M_y,Rk` | Moment plastique caractéristique de la tige (EC5 § 8.5.1.1) |
| `I_T` | Moment d'inertie de torsion — **très faible pour une section ouverte** |
| `τ_t` | Contrainte de cisaillement due à la torsion de Saint-Venant |
| `DOC-09` | Fiches techniques des connecteurs — **exclue de la FDC** (`D-05`) |
| `MAT-07` | Résistance `f_k` de la maçonnerie — **non mesurée** (`R-15`) |

---

## 2. INVENTAIRE ET ORIGINE DES EFFORTS

| Réf. | Assemblage | Émetteur | Efforts transmis | Référentiel |
|---|---|---|---|---|
| **`A1`** | Ancrage des `6 HA12` de `P2` dans `SF1` | `B-42 Ind. B` | `N 159,0 kN` · `M 9,4 kN·m` | EC2 § 8.4.4 |
| **`A2`** | Boulonnage du moisage `R1` | `B-45 Ind. A` | `V 77,4 kN` · `M 74,5 kN·m` | EC5 § 8.2 + EC3-1-8 § 3.6 |
| **`A3`** | Linteau `R3` — torsion d'excentrement | `B-45 Ind. A` | `V 23,1 kN` · `M_t 1,85 kN·m` | EC3 § 6.2.7 |
| **`A4`** | Scellement des `Stab1` dans le voutain | `B-45 Ind. A` | `F 5,8 kN` par file | EC6 § 8 |
| **`A5`** | Platine de pied `P1` sur `SF1` | `B-45 Ind. A` | `N 100,3 kN` | EC2 § 6.7 + EC3-1-8 § 3.6 |
| **`A6`** | Appuis `F1` à `R3` sur maçonnerie | `B-45 Ind. A` | `44,6` à `77,4 kN` | EC6 § 8 — renvoi `B-46` |

---

## 3. `A1` — ANCRAGE DES `6 HA12` DE `P2` DANS `SF1` (EC2 § 8.4)

### 3.1 Calcul

| Étape | Formule | Valeur |
|---|---|---|
| `f_ctd` | `f_ctk,0,05 / γ_C = 1,8 / 1,5` | **`1,20 MPa`** |
| `f_bd` | `2,25 η₁ η₂ f_ctd` (EC2 § 8.4.2) | **`2,70 MPa`** |
| `σ_sd` | `f_yd = 500 / 1,15` (cas enveloppe) | **`434,8 MPa`** |
| `l_b,rqd` | `(Φ/4)(σ_sd/f_bd)` | **`483 mm`** |
| `α₁` | équerre (tableau 8.2) | `0,70` |
| `α₂` | `c_nom 50 ≥ 3Φ = 36 mm` | `0,70` |
| `α₃` | confinement par cadres `HA8 e150` | `0,70` |
| **`l_bd`** | `α₁α₂α₃ l_b,rqd = 0,70³ × 483` | **`166 mm`** |
| `l_b,min` | `max(0,3 l_b,rqd ; 10Φ ; 100)` | **`145 mm`** |
| Disponible | `h 250 − c_nom 50` | **`200 mm`** |

**`l_bd = 166 mm ≤ 200 mm` : conforme, avec `34 mm` de marge.**

### 3.2 Ce que cette marge signifie réellement

**Les trois réductions sont obligatoires — et c'est écrit noir sur blanc.** Si l'**équerre** est supprimée, `l_bd` remonte à `237 mm` : **la barre ne rentre plus** dans `SF1`. La conformité de `A1` n'est donc pas acquise par le calcul seul : elle **dépend de trois dispositions constructives** que le plan coté doit porter.

> **Réserve `R-50-1`** — `A1` est conforme **sous trois conditions cumulatives** : équerre en pied, `c_nom = 50 mm` sur les 4 faces, cadres `HA8 e150` jusqu'au lit inférieur. **Aucune des trois ne peut être « ajustée » sur chantier.** Si l'une tombe, c'est `B-40` qui doit augmenter `h` — pas `B-50` qui raccourcit l'ancrage.

---

## 4. `A2` — BOULONNAGE DU MOISAGE `R1` (EC5 § 8.2, Johansen)

### 4.1 Le bois gouverne — et de très loin

`d = 16 mm` · `t₁ = 200 mm` (largeur de la poutre) · `ρ_k = 350 kg/m³` · `f_u,k = 400 MPa` · `k_mod = 0,80` · `γ_M,conn = 1,3`.

| Grandeur | Formule (EC5 § 8.5.1.1) | Valeur |
|---|---|---|
| `f_h,0,k` | `0,082 (1 − 0,01 d) ρ_k` | **`24,11 MPa`** |
| `M_y,Rk` | `0,3 f_u,k d^2,6` | **`162 141 N·mm`** |
| Mode a | `f_h t₁ d` | `77,1 kN` |
| Mode b | `f_h t₁ d [√(2 + 4M_y/(f_h d t₁²)) − 1]` | `33,1 kN` |
| Mode c | `2,3 √(M_y f_h d)` | **`18,2 kN`** ← gouverne |
| **`F_v,Rk`** | `min(a, b, c)` | **`18,2 kN`** |
| **`F_v,Rd`** | `k_mod F_v,Rk / γ_M,conn` | **`11,19 kN`** |
| Côté acier `M16 8.8` | `0,6 f_ub A_s / γ_M2` × 2 plans | `120,6 kN` |

**C'est le bois qui rompt à `18,2 kN`, l'acier tient `120,6 kN`.** Autrement dit : **la ruine est un brochage du bois, pas une rupture de boulon**. Choisir une classe `10.9` ne changerait rien ; augmenter le diamètre **aggraverait** (`f_h` décroît avec `d`). La seule variable utile est le **nombre** de boulons.

### 4.2 Dimensionnement retenu

| Grandeur | Valeur |
|---|---|
| `V_Ed` (`B-45`) | **`77,4 kN`** |
| Boulons nécessaires | `77,4 / 11,19 =` **`6,9`** |
| **Retenu** | **`10 M16 8.8` par face**, soit **5 rangées de 2** |
| Capacité | `10 × 11,19 =` **`111,9 kN`** |
| **Taux** | **`0,691`** |

**Espacements EC5 § 8.2.2 :** `e₁ ≥ 4d = 64 mm` · `e₂ ≥ 4d = 64 mm` · `e₃ ≥ max(7d ; 80) = 112 mm` · `e₄ ≥ 3d = 48 mm`. Sur `3,85 m` de poutre, `5` rangées à `700 mm` : `e₁ = 700 >> 112`. Sur `150 mm` de hauteur, `2` boulons à `50 mm` du nu : `e₂ = 90 > 64`. **Tout est tenu.**

**Et le maintien latéral de `R-45-2` est assuré par le même boulonnage** : les deux `UPE` sont serrés de part et d'autre, l'effort de stabilisation `5,8 kN` est repris par les mêmes tiges. **Le maintien est conçu, pas supposé.**

---

## 5. `A3` — LE LINTEAU `R3` EST NON CONFORME EN TORSION

### 5.1 Le calcul que `B-45` n'avait pas fait

| Grandeur | Formule | Valeur |
|---|---|---|
| Excentrement | `e = b/2 = 80/2` (axe de l'âme / axe de cisaillement) | **`40 mm`** |
| Torsion | `M_t = P × e = 46,2 × 0,040` | **`1,85 kN·m`** |
| `I_T` (`UPE 200`) | table EN 10365 | **`96 000 mm⁴`** |
| `τ_t` | `M_t t_f / I_T = 1,85×10⁶ × 11,5 / 96 000` | **`221,6 MPa`** |
| `τ_Rd` | `f_y / (√3 γ_M0) = 275 / 1,732` | **`158,8 MPa`** |
| **Taux** | `221,6 / 158,8` | **`1,40`** ⛔ |

### 5.2 Pourquoi `B-45` ne l'a pas vu — et pourquoi ce n'est pas une erreur de `B-45`

**`B-45` a fait exactement ce qu'elle devait faire** : elle a vérifié le profilé en **flexion et cisaillement** (`0,291` et `0,051`) et elle a **explicitement écrit** que la torsion d'excentrement du `U` n'était pas reprise, en la renvoyant à `B-50`. Le renvoi a été honoré. Ce que la chaîne montre ici, c'est que **le contrôle en flexion d'un profilé asymétrique ne suffit jamais** : sur un `U`, la torsion peut dépasser la résistance **avant** que la flexion n'atteigne la moitié de la sienne.

### 5.3 La prescription — une seule, et elle est constructive

> **REMPLISSAGE BÉTON `C25/30` ENTRE LES AILES DU `UPE 200`, SUR TOUTE LA LONGUEUR DU LINTEAU.**

La section devient **fermée** : `I_T` passe de `9,6 × 10⁴` à l'ordre de `10⁷ mm⁴` et la torsion cesse d'être un critère. **Variante possible :** platine de répartition soudée en continu (à porter au `B-60`).

**Sans ce remplissage, le linteau `R3-N/S` est non conforme et ne peut pas être posé.** Ce n'est pas une recommandation : c'est la condition d'exécution.

> **Réserve `R-50-2`** — remplissage béton à porter **sur le plan coté** (`B-60`) et à vérifier à la réception. Le contrôle croisé renvoie l'écart à `B-60`, **pas** à `B-45` : `B-45` avait signalé.

---

## 6. `A4` — `Stab1` : AUCUNE CAPACITÉ N'EST INVENTÉE

| Donnée nécessaire | État | Conséquence |
|---|---|---|
| Fiche technique du scellement | **`DOC-09` exclue de la FDC** (`D-05` : fiches de prédalles, `B-48` sans objet) | Aucune capacité résistante disponible |
| `f_k` de la maçonnerie (`MAT-07`) | **Non mesurée** (`R-15`) | Contrainte d'appui non vérifiable |
| Support réel | Voutain de briques creuses `7 cm` — **pas du béton** | Les règles `NF EN 1992-4` ne s'appliquent pas directement |

**Ce qui est prescrit sans capacité chiffrée — et déclaré comme tel :**

- `2` tiges `M12` par file, entraxe `≥ 100 mm`, distance aux bords `≥ 150 mm` ;
- scellement chimique à résine, profondeur `≥ 80 mm`, **jamais dans une alvéole creuse** ;
- **reprise de l'effort par butée** sur le hourdis en plus du scellement : l'entretoise est en **appui**, pas en traction pure.

> **Réserve `R-50-3`** — capacité à justifier par **fiche technique + essai d'arrachement sur 1 file sur 4** avant généralisation. **Aucune valeur n'est écrite ici, parce qu'aucune ne peut l'être.**

---

## 7. `A5` — PLATINE DE PIED `P1` SUR `SF1`

| Vérification | Valeur | Résistance | Taux |
|---|---|---|---|
| Pression diamétrale EC2 § 6.7 — platine `200 × 200` | `2,51 MPa` | `F_Rdu = 850 kN` | **`0,118`** ✅ |
| `4` tiges `M16 8.8` au cisaillement | — | `241,2 kN` | minimum constructif |

**Ce qui est dit et non sous-entendu :** aucun effort horizontal n'est transmis à la base de `P1` — la stabilité horizontale est assurée par la maçonnerie (`D-29`), le vent n'est pas traité (`CHG-06` non applicable, `D-26` pour le sismique). Les `4` tiges sont donc un **minimum constructif**, pas un dimensionnement.

> **Réserve `R-50-4`** — si un effort horizontal apparaît (vent, choc, modification de la stabilité), le nombre de tiges se recalcule. Il n'y a pas de marge cachée.

---

## 8. `A6` — APPUIS SUR MAÇONNERIE : `B-50` NE CALCULE PAS, IL RENVOIE

Les **8 appuis** de `F1a/b/c`, `F2`, `F3`, `F4`, `R1`, `R2-N/S`, `R3-N/S` reposent sur de la **maçonnerie en moellons**. La contrainte d'appui `σ = V_Ed / (a × b)` est calculable ; **la résistance `f_k` ne l'est pas** — `MAT-07` n'est pas mesurée. `D-34` fixe `f_k = 1,5 MPa` comme **hypothèse**, pas comme mesure.

**`B-50` transmet les réactions et renvoie à `B-46`**, qui porte la maçonnerie. C'est la règle de circulation : chaque brique vérifie son élément, `B-50` ne vérifie pas la maçonnerie à sa place.

> **Réserve `R-50-5`** — les 8 appuis sont à vérifier en `B-46` avec `f_k`. Sans `B-46`, aucun de ces appuis n'est justifié.

---

## 9. CONTRÔLE CROISÉ — PIÈCE 4

| Réf. | Ancrage calculé | Logement vérifié | Contrôle | Verdict | Renvoi |
|---|---|---|---|---|---|
| **`A1`** | `6 HA12` — `l_bd 166` | `SF1 80×80×25`, `c_nom 50` | `166 ≤ 200` ✅ | **OK** sous 3 conditions | — |
| **`A2`** | `10 M16 8.8` | poutre `20×15`, `3,85 m` | `e₁ 700` / `e₂ 90` ✅ | **OK** — `0,691` | — |
| **`A3`** | `M_t 1,85 kN·m` | `UPE 200` **section ouverte** | `τ 222 > 159` ⛔ | **NON** | **`B-60`** (remplissage) |
| **`A4`** | `F 5,8 kN`/file | voutain brique `7 cm` | capacité inconnue | **NON CALCULABLE** | `DOC-09` + `MAT-07` |
| **`A5`** | `4 M16` | `SF1`, platine `200×200` | `σ_c 2,51 MPa` ✅ | **OK** — `0,118` | — |
| **`A6`** | `8` appuis `23 à 77 kN` | moellons, `f_k` non mesuré | σ non calculable | **RENVOI** | **`B-46`** |

**Règle appliquée :** `B-50` **ne corrige aucun écart**. Deux écarts constatés (`A3`, `A4`), deux renvois (`B-60`, `B-46`), **aucune capacité inventée, aucune valeur réduite**.

---

## 10. NOMENCLATURE DES CONNECTEURS

| Désignation | Qté | Emploi |
|---|---|---|
| Boulon `M16 8.8` + écrou + `2` rondelles | **`20 u`** | Moisage `R1` (`10` par face) |
| Tige `M16 8.8` à scellement chimique | `8 u` | Platine de pied `P1` (`4` par poteau) |
| Tige `M12` à scellement chimique | `8 u` | `Stab1` (`2` par file, `4` files) |
| Platine `200 × 200 × 15` | `2 u` | Pied de `P1-N` et `P1-S` |
| Platine d'about `160 × 160 × 12` | `18 u` | Appuis `F1` à `R3` sur maçonnerie |
| Béton `C25/30` de remplissage | — | Remplissage des `UPE 200` de `R3` |

**Anticorrosion :** galvanisation à chaud `NF EN ISO 1461`, `70 µm` mini pour toute la boulonnerie et les platines. **Protection au feu : non dimensionnée** — hors lot GO.

---

## 11. AUTO-CONTRÔLE

| # | Point de la fiche `B-50` | Verdict | Preuve / limite |
|---|---|---|---|
| 1 | Inventaire des assemblages, émetteur cité pour chacun | ✅ **CONFORME** | § 2 — `6` assemblages, `5` émetteurs |
| 2 | Ancrages BA calculés (EC2 § 8.4) | ✅ **CONFORME** | § 3 — `A1`, `l_bd 166 ≤ 200` |
| 3 | Assemblages métalliques calculés (EC3-1-8) | ✅ **CONFORME** | § 4 et 7 — `A2` côté acier, `A5` |
| 4 | Assemblages bois calculés (EC5 § 8.2, Johansen) | ✅ **CONFORME** | § 4 — modes a/b/c, le bois gouverne |
| 5 | Scellements maçonnerie | ⚠️ **PARTIEL DÉCLARÉ** | § 6 — `A4` **aucune capacité** : `DOC-09` exclue, `f_k` non mesuré |
| 6 | Contrôle croisé avec les logements | ✅ **CONFORME** | § 9 — `6` lignes, `2` écarts identifiés et renvoyés |
| 7 | Aucun écart corrigé par `B-50` | ✅ **CONFORME** | § 9 — renvois à `B-60` et `B-46` |
| 8 | Aucune capacité de connecteur inventée | ✅ **CONFORME** | Tout est calculé par formule, sauf `A4` déclaré non calculable |
| 9 | Planche : filigrane, indice, mode, cartouche | ✅ **CONFORME** | `FLORA_B50_ASSEMBLAGES_IndA` — audit `0 erreur` |
| 10 | Protection au feu non dimensionnée | ✅ **CONFORME** | § 10 — mention seule |
| 11 | Mode `COMPLET` déclarable ? | ⛔ **NON — et c'est le mode qui le dit** | `DOC-09` manque (`V12`) ⇒ **PARTIEL-DÉCLARÉ**, assumé dans l'en-tête |

**Verdict : 8 conformes, 1 partiel déclaré, 1 exclusion assumée, 1 mode dégradé justifié.**

---

## 12. TRANSMISSIONS ET RÉSERVES

### 12.1 Ce que `B-50` transmet

| Brique | Ce qu'elle reçoit |
|---|---|
| **`B-60`** | `A3` : remplissage béton du `UPE 200` à porter **sur le plan coté** · `A2` : `10 M16` à `700 mm` d'entraxe · `A1` : équerre + cadres jusqu'au lit inférieur |
| **`B-46`** | `A6` : les `8` réactions d'appui sur maçonnerie, à confronter à `f_k` |
| **`B-62`** | § 10 — nomenclature des connecteurs |
| **`B-03`** | `R-50-1` à `R-50-5` |

### 12.2 Réserves nées de cette brique

| Réf. | Objet | Conséquence si non levée | Destinataire |
|---|---|---|---|
| **`R-50-1`** | `A1` conforme **sous 3 conditions** (équerre, `c_nom 50`, cadres jusqu'au lit) | Sans l'équerre, `l_bd = 237 mm > 200 mm` : l'ancrage ne rentre plus dans `SF1` | `B-60` (plan) |
| **`R-50-2`** | **`A3` non conforme en torsion** — remplissage béton obligatoire | Sans remplissage, le linteau `R3` **ne peut pas être posé** | `B-60` |
| **`R-50-3`** | `A4` : capacité de scellement non calculable | Sans fiche technique et essai d'arrachement, le `Stab1` n'est pas justifié | `DOC-09` + `MAT-07` |
| **`R-50-4`** | `A5` : `4` tiges = minimum constructif, sans effort horizontal | Si un effort horizontal apparaît, re-dimensionner | À surveiller |
| **`R-50-5`** | `A6` : 8 appuis sur maçonnerie non vérifiés par `B-50` | Sans `B-46`, aucun de ces appuis n'est justifié | `B-46` |

---

## 13. POINT DE CONTRÔLE HUMAIN

**Une décision, et une seule, est attendue :**

1. **Le remplissage béton du `UPE 200` de `R3` est-il accepté ?** C'est la seule issue constructive qui rend le linteau conforme sans changer de profilé. L'alternative — passer à un `HEB 160` ou à un `HEB 200` — changerait la prescription du `D2` et relancerait `B-45`. **Le choix vous revient ; les deux sont chiffrables.**

**Une information utile :** la **fiche technique du scellement chimique** (`DOC-09`). Elle ne concerne pas les prédalles — c'est le motif pour lequel elle avait été exclue — mais elle est **indispensable** à `A4`. Un extrait suffirait à fermer `R-50-3`.

**Brique `B-50` livrée en indice A — en attente de votre `GO` ou de vos observations.**
