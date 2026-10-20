# B-42 — POTEAUX ET JAMBAGES EN BÉTON ARMÉ

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-42** — Verticaux BA (poteaux et jambages) |
| Phase | **4 — Calculs d'exécution** (première note de calcul opposable) |
| **Mode d'appel** | **COMPLET** — sections, matériaux et charges sont tous disponibles et tracés |
| Régime | **OUTILLÉ (V13)** — diagramme d'interaction et flambement calculés par script |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b42_ba.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b42_ba.txt` (2 976 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b42_ba.json` (1 726 o) |
| Sortie graphique | **Aucune** — le ferraillage est porté sur les plans `B-60` |
| **Indice** | **B** — `N_ELU` repris de `B-21 Ind. C` (la recharge de `15 cm` sort des planchers, `D-35`) ; sections et ferraillage **inchangés** |
| Date | **20/10/2026** |
| Brique suivante | **`B-43`** (planchers, plancher haut et **dallage** — `D-35`) |

> **Révision B — 20/10/2026 (`D-35`).** `B-21 Ind. C` a corrigé la localisation de la recharge de `15 cm` : elle pèse sur le **dallage**, pas sur les planchers hauts. Les efforts normaux baissent — `P2` de `217,7` à **`159,0 kN`** (`−27 %`), `P3` de `39,8` à `35,8`, `J1` de `44,3` à `39,8` — et **aucune section ni aucun ferraillage ne change** : `6 HA12` reste imposé par l'**espacement maximal** des barres sur les faces étroites, pas par la résistance. L'utilisation de `P2` passe de `0,400` à **`0,305`** ; la pression d'appui de `J1` sur la maçonnerie de `0,369` à **`0,332 MPa`** — le point dur du lot s'éloigne, il ne disparaît pas.
>
> **Ce que cette brique fait.** Trois porteurs verticaux en béton armé sont implantés par `B-20` : `P2` (`15 × 25`), `P3` (`50 × 40`) et `J1` (jambage `24 × 50`). `B-20` les avait **annoncés** surabondants — « capacité `510 kN` », « `850 kN` » — sans le démontrer. `B-42` remplace l'annonce par un **diagramme d'interaction `N-M`** calculé par compatibilité des déformations, un **flambement EC2 § 5.8** et un **ferraillage justifié**.

---

## 0. RÉPONSE DIRECTE — LES TROIS PORTEURS PASSENT, MAIS PAS POUR LA RAISON ANNONCÉE

| Constat | Chiffre | Conséquence |
|---|---|---|
| Porteurs vérifiés | **3** (`P2`, `P3`, `J1`) | Tous satisfont l'ELU de flexion composée |
| Porteur **gouvernant** | **`P2`** | `M_Ed / M_Rd = 0,305` — c'est le seul des trois réellement sollicité |
| `P3` et `J1` | `0,013` et `0,015` | Ce n'est pas la résistance qui les dimensionne : c'est le **minimum réglementaire** |
| Seul porteur **élancé** | **`P2`** | `lambda = 64,7` contre `lambda_lim = 19,7` : les effets du 2ᵉ ordre **doivent** être calculés |
| Ferraillage retenu | **6 HA12** partout | `679 mm²` — imposé par l'**espacement maximal** des barres, pas par la résistance |
| Points durs réels | **2** | (1) l'excentricité de l'appui de `F2` sur `P2` ; (2) la **pression d'appui de `J1` sur la maçonnerie** |

> **Le résultat qui compte n'est pas `0,305`, c'est `0,83`.** `J1` transmet `39,8 kN` sur `0,12 m²`, soit `0,332 MPa`. À `f_k = 1,5 MPa` (`D-34`), cela consomme **55 %** de la résistance de calcul ; à `f_k = 1,0 MPa`, **83 %** ; à `0,5 MPa`, **166 % — non satisfait**. Autrement dit : **la clause `D-34` n'est pas une formalité contractuelle, c'est le risque d'exécution le plus concret du lot.** Le béton, lui, est confortable partout — `P2` travaille à `19 %` de son effort normal résistant.

---

## 1. GLOSSAIRE DES CODES — POUR LIRE CETTE NOTE SANS EN OUVRIR UNE AUTRE

| Code | Objet en clair |
|---|---|
| `P2` | Poteau BA `15 × 25` sous la poutre acier `F2`, façade Ouest Nord |
| `P3` | Poteau BA `50 × 40` dans le refend intérieur |
| `J1` | Jambage BA `24 × 50` dans le refend central, sous le linteau `F1` |
| `N_Ed` | Effort normal de calcul à l'ELU (combinaison `1,35 G + 1,50 Q`) |
| `M_Ed` / `M_Rd` | Moment de calcul / moment résistant **pour l'effort normal appliqué** |
| **Interaction `N-M`** | Courbe qui donne `M_Rd` pour chaque `N_Ed` : un poteau ne se vérifie jamais en flexion seule |
| `lambda` | Élancement mécanique, `lambda = l0 / i` |
| `lambda_lim` | Élancement au-delà duquel les effets du 2ᵉ ordre sont obligatoires (EC2 § 5.8.3.1) |
| `l0` | Longueur efficace de flambement (ici `l0 = H` : appuis rotulés en pied et en tête) |
| `e_0` | Excentricité du 1ᵉʳ ordre, au minimum `max(h/30 ; 20 mm)` (EC2 § 6.1(4)) |
| `e_i` | Excentricité d'imperfection géométrique, `l0 / 400` |
| `e_2` | Excentricité du 2ᵉ ordre, calculée par la **courbure nominale** (EC2 § 5.8.8.3) |
| `K_r`, `K_phi` | Coefficients correcteurs de courbure : effort normal et fluage |
| `f_cd` / `f_yd` | Résistances de calcul du béton / de l'acier |
| `alpha_cc` | Coefficient de charge de longue durée : `0,85` retenu (valeur recommandée EC2, conservative) |
| `As,min` / `As,max` | Sections d'acier minimales et maximales d'un poteau (EC2 § 9.5.2) |
| `XA1` | Classe d'exposition du béton (`H-23`) — gouverne l'enrobage |
| `H-23` / `H-26` | Hypothèses : agressivité `XA1` · `f_vk0` et `gamma_M = 2,5` pour la maçonnerie |
| `D-34` | Clause maçonnerie : `f_k = 1,5 MPa`, essais **hors mission**, reprise d'étude chiffrée si non concluants |
| `D-26` | Zone de sismicité 1 : **aucune vérification sismique** |
| `SF1` | Semelle isolée `80 × 80 × 25` sous `P2` (`D-30`, `B-40`) |
| `B-60` / `B-62` | Plans d'exécution cotés / nomenclatures — le ferraillage y sera reporté |

---

## 2. DONNÉES D'ENTRÉE — CHAQUE VALEUR PORTE SA SOURCE

| Donnée | Valeur retenue | Source | Remarque |
|---|---|---|---|
| Effort normal `P2` | `N_ELU = 159,0 kN` | **`B-21 Ind. C`** § 6.2 (tableau 5) | `A_inf = 11,46 m²`, continuité `1,15`, **sans recharge** (`D-35`) |
| Effort normal `P3` | `N_ELU = 35,8 kN` | **`B-21 Ind. C`** § 6.2 | `A_inf = 0,23 m²` |
| Effort normal `J1` | `N_ELU = 39,8 kN` | **`B-21 Ind. C`** § 6.2 | `A_inf = 0,25 m²` |
| Section `P2` | `150 × 250 mm` | `B-20` planche 1 (`PH RDC`) | **Implantée : non modifiable sans reprise de `B-20`** |
| Section `P3` | `400 × 500 mm` | `B-20` planche 1 | Idem |
| Section `J1` | `240 × 500 mm` | `B-20` planche 1 | Idem |
| Béton | `C25/30` · `f_ck = 25 MPa` | `B-20` · planches | `f_cd = 0,85 × 25 / 1,5 = 14,17 MPa` |
| Acier | `S500` · `f_yk = 500 MPa` | `B-20` · planches | `f_yd = 500 / 1,15 = 434,8 MPa` |
| Enrobage | `c_nom = 30 mm` | `H-23` (classe `XA1`, hors fondation) | `50 mm` en fondation (`B-40`) |
| Hauteur d'étage `H` | `2 800 mm` | `B-20` § « `P3` & `J1` — `H ≈ 2,40 à 2,80 m` » | **Borne haute retenue** : `l0 = H` (appuis rotulés) |
| Fluage effectif | `phi_ef = 2,0` | EC2 § 5.8.4, `RH ≈ 50 %`, `h0 ≈ 94 mm` pour `P2` | `K_phi = 1 + 0,35 × 2,0 = 1,70` |
| Classe de ductilité | **sans objet** | `D-26` — zone de sismicité 1 | Aucune exigence de confinement sismique |
| Incendie | **hors mission** | Cadrage, `B-22` | Aucun dimensionnement au feu produit ni attendu |

> **Ce qui n'est pas une donnée d'entrée.** `H = 2,80 m` est la **borne haute de l'hypothèse de `B-20`**, pas un relevé. La sensibilité à `l0 = 3 500 mm` est traitée au § 8 : elle ne fait pas basculer la conclusion.

---

## 3. MÉTHODE

1. **Élancement** (EC2 § 5.8.3.1) : `lambda = l0 / i` avec `i = b_min / √12`. Si `lambda <= lambda_lim`, les effets du 2ᵉ ordre peuvent être négligés ; `lambda_lim = 20 · A · B · C / √n` avec `A = 0,7` (fluage inconnu), `B = 1,1`, `C = 0,7` (moments d'extrémité nuls — poteaux d'appui simple).
2. **Excentricités** : `e_tot = e_0 + e_i + e_2`, avec `e_0 = max(h/30 ; 20 mm)`, `e_i = l0 / 400`, et `e_2` par la **courbure nominale** (EC2 § 5.8.8.3) :
   `1/r = K_r · K_phi · eps_yd / (0,45 d)` puis `e_2 = (1/r) · l0² / pi²`.
3. **Flexion composée** : le couple `(N_Ed, M_Ed)` est confronté au **diagramme d'interaction** de la section, calculé par compatibilité des déformations — bloc rectangulaire `0,8 x`, acier élasto-plastique parfait, `eps_cu = 0,0035`, `d = h − c − phi_t − phi/2`. Le moment résistant `M_Rd` est interpolé **à l'effort normal appliqué**, jamais pris en flexion pure.
4. **Dispositions constructives** (EC2 § 9.5) : `As,min = max(0,10 N_Ed / f_yd ; 0,002 A_c)`, `As,max = 0,04 A_c`, au moins 4 barres, distance entre barres `<= min(20 phi ; b ; 400 mm)` (§ 9.5.3(3)), cadres `HA8` avec `phi_t >= max(6 ; phi_l/4)` et espacement `<= min(20 phi_l ; b ; 400 mm)` (§ 9.5.3(6)).
5. **Béton** : `alpha_cc = 0,85`. L'annexe nationale française autorise `1,0` ; je retiens la valeur **recommandée**, plus basse, donc conservative — c'est une réserve de sécurité non comptée.

---

## 4. `P2` — LE SEUL PORTEUR ÉLANCÉ

### 4.1 Élancement

| Grandeur | Valeur | Calcul |
|---|---|---|
| `b_min` | `150 mm` | Section `150 × 250` — axe faible |
| `i` | `43,3 mm` | `150 / √12` |
| `lambda` | **`64,7`** | `2 800 / 43,3` |
| `n = N_Ed / (A_c f_cd)` | `0,299` | `159 000 / (37 500 × 14,17)` |
| `lambda_lim` | **`19,7`** | `20 × 0,7 × 1,1 × 0,7 / √0,299` |
| Effets du 2ᵉ ordre | **OBLIGATOIRES** | `64,7 > 19,7` |

### 4.2 Excentricités et moment de calcul

| Grandeur | Valeur | Détail |
|---|---|---|
| `e_0` | `20,0 mm` | Minimum EC2 § 6.1(4) — `h/30 = 8,3 mm < 20 mm` |
| `e_i` | `7,0 mm` | `l0 / 400 = 2 800 / 400` |
| `K_r` | `1,00` | `(n_u − n)/(n_u − n_bal)` avec `n_u = 1,500`, `n_bal = 0,4` → `1,078`, **plafonné à `1,00`** |
| `K_phi` | `1,70` | `1 + 0,35 × 2,0` |
| `1/r` | `0,0403 m⁻¹` | `K_r · K_phi · 0,002174 / (0,45 × 0,204)` |
| `e_2` | **`32,0 mm`** | `0,0403 × 2,8² / pi²` |
| **`e_tot`** | **`59,0 mm`** | `20,0 + 7,0 + 32,0` |
| **`M_Ed`** | **`9,4 kN·m`** | `159,0 × 0,0590` |

> **Ce qui a changé avec `D-35`, et ce qui n'a pas changé.** La charge baisse, donc `n` baisse (`0,410 → 0,299`) et `lambda_lim` remonte (`16,8 → 19,7`) : le poteau reste **largement au-delà** du seuil du 2ᵉ ordre (`64,7`). L'excentricité du 2ᵉ ordre, elle, **augmente légèrement** (`31,7 → 32,0 mm`) — un effort normal plus faible courbe davantage —, mais le moment de calcul chute avec `N` (`12,8 → 9,4 kN·m`). **C'est le couple `(N, M)` qui compte, pas l'un ou l'autre.**

> Le bras utile est pris à `d = 204 mm` (soit `phi = 16 mm` supposé, alors que le ferraillage retenu est `HA12`). C'est **volontairement défavorable** : un `d` plus petit majore la courbure, donc `e_2`.

### 4.3 Vérification de la section et ferraillage

| Grandeur | Valeur | Verdict |
|---|---|---|
| `N_Rd,max` | `826,6 kN` | `A_c f_cd + A_s f_yd` — `N_Ed / N_Rd = 0,192` |
| `M_Rd` à `N_Ed = 159,0 kN` | `30,7 kN·m` | Interpolé sur le diagramme d'interaction (6 HA12) |
| **`M_Ed / M_Rd`** | **`0,305`** | ✅ **Satisfait** — marge `70 %` |
| `As` retenu | `6 HA12 = 679 mm²` | Soit `1,81 %` de `A_c` |
| `As,min` | `75 mm²` | `max(0,10 × 159 000 / 434,8 ; 0,002 × 37 500) = max(36,6 ; 75)` |
| `As,max` | `1 500 mm²` | `0,04 × 37 500` |
| Distance entre barres | `83 mm` | `<= min(20 × 12 ; 150 ; 400) = 150 mm` ✅ |
| Cadres | `HA8 e150` | `<= min(20 × 12 ; 150 ; 400) = 150 mm` ✅ — `phi_t = 8 >= max(6 ; 3)` |

**Pourquoi 6 barres et non 4.** Avec 2 barres par face, la distance entre barres vaudrait `166 mm` sur la face de `250 mm` — au-delà de la limite de `150 mm` imposée par la largeur `b = 150 mm`. `P2` est donc ferraillé à **3 barres par face**, non pas parce que la résistance l'exige (`0,305`), mais parce que la **géométrie étroite** l'impose. C'est un point à ne pas « optimiser » en exécution.

---

## 5. `P3` ET `J1` — LE MINIMUM RÉGLEMENTAIRE GOUVERNE

| Grandeur | `P3` (`50 × 40`) | `J1` (`24 × 50`) |
|---|---|---|
| `i` (axe faible) | `115,5 mm` (`400 / √12`) | `69,3 mm` (`240 / √12`) |
| `lambda` | `24,2` | `40,4` |
| `n` | `0,013` | `0,023` |
| `lambda_lim` | `95,9` | `70,5` |
| 2ᵉ ordre | **non nécessaire** | **non nécessaire** |
| `M_Ed` (avec `e_0 + e_i`) | `1,0 kN·m` | `1,1 kN·m` |
| `M_Rd` à `N_Ed` | `73,6 kN·m` | `72,1 kN·m` |
| **`M_Ed / M_Rd`** | **`0,013`** | **`0,015`** |
| `As,min` | `400 mm²` (`0,002 A_c`) | `240 mm²` (`0,002 A_c`) |
| `As` retenu | `6 HA12 = 679 mm²` | `6 HA12 = 679 mm²` |
| Cadres | `HA8 e200` | `HA8 e200` |

> **Ces deux porteurs sont massifs parce que le plan l'a voulu, pas parce que le calcul l'exige.** Un `50 × 40` sous `35,8 kN` travaille à `1,3 %` de son moment résistant. Je ne propose **pas** de réduire les sections : elles sont implantées, elles participent à la raideur et au contreventement, et `D-29` fait reposer la stabilité horizontale sur la maçonnerie **et** sur ces appuis. Réduire une section implantée serait une reprise de `B-20`, pas une optimisation de `B-42`.
>
> En revanche, `6 HA12` **est** le minimum utile : `4 HA12` ne satisferait pas l'espacement maximal sur la face de `500 mm` (`416 mm > 240 mm`).

---

## 6. SYNTHÈSE ET DÉBITS

| Élément | Section | `N_Ed` | `M_Ed` | `M_Rd` | Utilisation | Acier | Cadres |
|---|---|---|---|---|---|---|---|
| **`P2`** | `15 × 25` | `159,0 kN` | `9,4 kN·m` | `30,7 kN·m` | **`0,305`** | `6 HA12` | `HA8 e150` |
| **`P3`** | `50 × 40` | `35,8 kN` | `1,0 kN·m` | `73,6 kN·m` | `0,013` | `6 HA12` | `HA8 e200` |
| **`J1`** | `24 × 50` | `39,8 kN` | `1,1 kN·m` | `72,1 kN·m` | `0,015` | `6 HA12` | `HA8 e200` |

**Débits indicatifs**, à `H = 2 800 mm` (hypothèse `B-20`, à confirmer au relevé) — longueur de barre `H + 2 × 40 phi = 2 800 + 960 = 3 760 mm` :

| Élément | Barres | Longueur unitaire | Cadres | Longueur cadre | Poids estimé |
|---|---|---|---|---|---|
| `P2` | `6 HA12` | `3,76 m` | `20` | `0,72 m` (`2(150+250) − 8×30 + 2×80`) | `25,7 kg` |
| `P3` | `6 HA12` | `3,76 m` | `15` | `1,72 m` (`2(400+500) − 8×30 + 2×80`) | `30,2 kg` |
| `J1` | `6 HA12` | `3,76 m` | `15` | `1,32 m` (`2(240+500) − 8×30 + 2×80`) | `27,9 kg` |
| **Total** | **18 barres** | — | **50 cadres** | — | **`83,8 kg`** |

> Les débits sont **indicatifs** : ils dépendent de la hauteur réelle et des longueurs d'ancrage disponibles dans les appuis. `B-62` les établira sur la géométrie définitive, `B-50` vérifiera les ancrages.

---

## 7. LES DEUX POINTS DURS — APPUIS ET EXCENTRICITÉ

### 7.1 `P2` sur `SF1` — béton sur béton, sans objet

`P2` repose sur la semelle `SF1` (`80 × 80 × 25`, `D-30`, `B-40`), pas sur la maçonnerie : la pression vaut `159,0 / 0,64 = 0,25 MPa` sur du `C25/30` — soit `16 %` de `f_cd`, un rapport très faible. La vérification de `SF1` elle-même appartient à `B-40`.

### 7.2 `P3` et `J1` sur la maçonnerie — **le vrai point dur**

| Élément | `A_appui` | `sigma_d` | `f_k = 1,5 MPa` (`D-34`) | `f_k = 1,0 MPa` | `f_k = 0,5 MPa` |
|---|---|---|---|---|---|
| `P3` | `0,200 m²` | `0,179 MPa` | `0,30` ✅ | `0,45` ✅ | `0,89` ⚠️ |
| `J1` | `0,120 m²` | `0,332 MPa` | `0,55` ✅ | `0,83` ⚠️ | **`1,66` ❌** |

> **`J1` reste le point faible du lot.** Il consomme `55 %` de la résistance d'appui dans l'hypothèse `D-34` — contre `62 %` à l'indice A. Toute valeur de `f_k` inférieure à **`0,83 MPa`** le met en défaut (contre `1,15 MPa`). **Le dé de répartition n'est plus une urgence, il reste une option** : si les essais donnent `f_k < 1,5 MPa`, il devient nécessaire. Deux issues, **à trancher en `B-46`** et non ici : soit les essais confirment `f_k >= 1,5 MPa`, soit un **dé de répartition** est ajouté sous `J1` — ce qui modifie la planche et relève d'une décision `RDR`, pas d'une initiative de note de calcul.

### 7.3 Excentricité de l'appui de `F2` sur `P2`

`F2` (`HEB 200`, portée `2,85 m`, `p_ELU = 43,8 kN/m`) appuie sur `P2` par l'intermédiaire d'un appareil d'appui **non encore défini** (`B-50`). La note retient `e_0 = 20 mm` (minimum réglementaire). Si l'appui est excentré de `50 mm` — cas fréquent quand la poutre s'arrête au nu du poteau — la sensibilité du § 8 donne `0,461`, puis `0,563` en cumulant avec `l0 = 3 500 mm` : **la section tient encore**, avec `44 %` de marge.

---

## 8. SENSIBILITÉ DE CONCEPTION — NON CONTRACTUEL

> **NON CONTRACTUEL — POUR INFORMATION.** Balayage des deux incertitudes qui ne sont pas des données d'entrée : la hauteur de flambement `l0` (hypothèse `B-20`) et l'excentricité `e_0` de l'appui de `F2`. La disposition retenue (`6 HA12`) est conservée dans tous les cas.

| Élément | Nominal | `l0 = 3 500 mm` | `e_0 = 50 mm` | Les deux cumulés |
|---|---|---|---|---|
| **`P2`** | `0,305` | `0,407` | `0,461` | **`0,563`** ✅ |
| `P3` | `0,013` | `0,014` | `0,028` | `0,029` ✅ |
| `J1` | `0,015` | `0,016` | `0,031` | `0,032` ✅ |

**Lecture.** Le cas le plus défavorable reste inférieur à `1,0` : `P2` tient même avec une hauteur d'étage de `3,50 m` **et** un appui excentré de `50 mm`. La conclusion ne bascule pas — c'est ce qui autorise à livrer la note en indice `B` tout en portant les réserves du § 9.

---

## 9. RÉSERVES ET POINTS D'ARRÊT

| Réf. | Objet | Conséquence si non levée | Destinataire |
|---|---|---|---|
| **`R-42-1`** | Hauteur d'étage réelle (`H ≈ 2,40 à 2,80 m` est une hypothèse de `B-20`) | Débits et longueurs d'ancrage faux si `H > 2,80 m` ; la résistance, elle, reste satisfaisante jusqu'à `l0 = 3,50 m` | Relevé / `B-60` |
| **`R-42-2`** | Excentricité de l'appui de `F2` sur `P2` | Si `e_0 > 50 mm`, l'utilisation dépasse `0,57` et le ferraillage doit être repris | `B-50` (appareil d'appui) |
| **`R-42-3`** | Pression d'appui de `J1` sur la maçonnerie (`0,332 MPa`) | Défaut dès `f_k < 0,83 MPa` ; dé de répartition à décider selon le résultat des essais `D-34` | `B-46` + `D-34` |
| **`R-42-4`** | Longueur d'ancrage `40 phi = 480 mm` dans les appuis | Ancrage insuffisant si la semelle ou le chaînage est moins profond | `B-50` · `B-40` |
| **`R-42-5`** | Aucune vérification au feu | Hors mission, à la charge du bureau d'études incendie | Cadrage |

---

## 10. AUTO-CONTRÔLE — 8 POINTS

| # | Point | Verdict | Preuve |
|---|---|---|---|
| 1 | Les 3 porteurs et leurs `N_ELU` de `B-21 Ind. C` figurent dans la note | ✅ | § 2 (`159,0` / `35,8` / `39,8 kN`) et § 4 à 6 |
| 2 | Diagramme d'interaction `N-M` explicité (pas de flexion pure) | ✅ | § 3.3, § 4.3, § 5 |
| 3 | Sections identiques aux plans `B-20` | ✅ | `15 × 25` · `50 × 40` · `24 × 50` |
| 4 | Enrobage `30 mm` et classe `XA1` (`H-23`) rappelés | ✅ | § 2 |
| 5 | `As,min` / `As,max` EC2 § 9.5.2 contrôlés | ✅ | § 4.3, § 5 |
| 6 | Espacement des cadres `<= min(20 φ ; b ; 400 mm)` | ✅ | § 4.3, § 5 |
| 7 | Sismique (`D-26`) et incendie déclarés hors mission | ✅ | § 2, § 9 (`R-42-5`) |
| 8 | Débits cohérents avec les sections retenues | ✅ | § 6 |

**Contrôle machine** : `_scripts/b42_ba.py` → **8/8 CONFORME**. Journal : `_rendus/b42_ba.txt` · résultats : `_rendus/b42_ba.json`.

---

## 11. CE QUE CETTE BRIQUE NE FAIT PAS

| Sujet | Brique | Motif |
|---|---|---|
| Semelle `SF1` et reprise en sous-œuvre | `B-40` | Déjà traité, indice `E` |
| Appareils d'appui, ancrages, platines de `F2` | `B-50` | Conditionne `R-42-2` et `R-42-4` |
| Pression d'appui sur maçonnerie, chaînages | `B-46` | Conditionne `R-42-3` ; `f_k` reste `H-25` |
| Poteau acier `P1-N` / `P1-S` | `B-45` | Structure métallique, pas béton armé |
| Plans cotés de coffrage et ferraillage | `B-60` / `B-62` | Le présent calcul les alimente |
| Vérification sismique | — | **Aucune** : `D-26`, zone de sismicité 1 |
| Vérification au feu | — | Hors mission |
