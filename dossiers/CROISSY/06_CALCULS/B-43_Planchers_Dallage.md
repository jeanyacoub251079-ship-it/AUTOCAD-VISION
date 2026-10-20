# B-43 — PLANCHERS, PLANCHER HAUT ET DALLAGE

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-43** — Planchers et dallages (note de calcul d'exécution) |
| Phase | **4 — Calculs d'exécution** (après `B-42`) |
| **Modes d'appel** | **COMPLET** pour la zone A (bois, toutes données disponibles) · **PARTIEL-DÉCLARÉ** pour la zone D (dallage : portance non mesurée, `D-02`/`D-03` contractuelles) · **RENVOI** pour la zone B (profilés → `B-45`) · **PARAMÉTRIQUE** pour la zone C (plancher haut non sondé, `E-07`) |
| Régime | **OUTILLÉ (V13)** — calcul intégral par script, journal et JSON conservés |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b43_planchers.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b43_planchers.txt` (7 218 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b43_planchers.json` (1 375 o) |
| Sortie graphique | `_plans/FLORA_B43_DALLAGE_IndA.dxf` (71 549 o · AC1032 · audit **0 erreur**) · `.pdf` (423 471 o) · `.png` (536 870 o) |
| **Indice** | **A** — création de la brique |
| Date | **20/10/2026** |
| Brique suivante | **`B-45`** (profilés de plancher et moisage `R1`) · **`B-50`** (assemblages et ancrages) |

> **Ce que cette brique fait.** Elle établit la **DDC d'exécution** des planchers et du dallage, distincte de la DDC préliminaire `B-21`, puis elle **vérifie** ce qui peut l'être : les **solives bois `8 × 18`** de l'aile Est (flexion, cisaillement, flèche différée, compression d'appui) et le **dallage** rechargé par `D-35` (portance, épaisseur, treillis, fissuration, joints, désolidarisation).
>
> **Ce qu'elle ne fait pas, et le dit.** Les **profilés métalliques** du plancher B relèvent de `B-45` ; le **plancher haut d'étage** n'a pas de nature établie et **ne peut pas être calculé** (`E-07`) ; les **assemblages** relèvent de `B-50`. Ces trois renvois ne sont pas des oublis : ils sont chiffrés, localisés, et portés par une réserve.

---

## 0. RÉPONSE DIRECTE — TROIS ZONES SUR QUATRE SONT TRANCHÉES

| Zone | Ce qu'elle est | Verdict de `B-43` |
|---|---|---|
| **A — plancher bois, aile Est** | Solives `8 × 18` @ `0,50 m`, portée `2,77 m`, `C18` | ✅ **CONFORME aux cinq vérifications EC5** — flexion `0,619`, cisaillement `0,362`, appui `0,316`, flèche instantanée `0,510`, flèche finale `0,576` |
| **B — plancher mixte, aile Ouest** | `IPE 160` @ `0,72 m` + hourdis briques + chape 10 cm + `IPE 330` | ⤴ **RENVOYÉ à `B-45`** — `B-43` fixe la charge : `7,28 kN/m` par solive. Le hourdis n'est ni BA ni bois |
| **C — plancher haut d'étage** | **Nature inconnue** (`D3` p. 4 et 10 : « non sondé ») | ⛔ **AUCUN CALCUL POSSIBLE** — `R-43-1`, point d'arrêt `PA-03` |
| **D — dallage** | BA `13 cm` sur fond de forme `40 cm`, **rechargé sur 100 % de l'emprise** (`D-35`) | ✅ **CONFORME** — portance sollicitée à **`2,9 %`** ; épaisseur et treillis gouvernés par la **fissuration**, pas par la flexion |

**Le résultat qui compte n'est pas un ratio, c'est un déplacement du problème.** Le dallage n'est pas une affaire de **portance** — `14,2 kPa` sur `490 kPa` admissibles, soit `2,9 %` — c'est une affaire de **retrait et de désolidarisation**. Un dallage de `111,15 m²` coulé d'un seul tenant, sans joint de retrait, **fissure** : la fissuration n'est pas un défaut esthétique, c'est le chemin par lequel l'eau entre et le carrelage se décolle. `B-43` prescrit donc les joints, le treillis et la désolidarisation — et il précise au passage que **les joints de retrait ne sont pas des joints de dilatation** : `D-28` interdit les seconds, il n'a jamais interdit les premiers.

---

## 1. GLOSSAIRE DES CODES — POUR LIRE CETTE NOTE SANS EN OUVRIR UNE AUTRE

| Code | Objet en clair |
|---|---|
| `A` / `B` / `C` / `D` | Zones de la présente note : plancher bois Est · plancher mixte Ouest · plancher haut d'étage · dallage |
| `E-07` | Plancher haut d'étage, **jamais sondé** (`B-24`) |
| `C18` | Classe de résistance du bois massif (`EN 338`) — **hypothèse de calcul** `EXI-03`, pas une mesure |
| `k_mod` | Coefficient d'altération : `0,80` retenu (classe de service 2, charge de moyenne durée) |
| `k_def` | Coefficient de fluage : `0,60` (classe de service 2) |
| `f_m,d` / `f_v,d` / `f_c,90,d` | Résistances de calcul en flexion / cisaillement / compression perpendiculaire |
| `w_inst` / `w_fin` | Flèche instantanée / flèche finale (fluage compris) |
| `ST25C` | Treillis soudé `Ø7 e150` — `257 mm²/m` dans chaque direction |
| `A_s,min` | Section d'acier minimale d'une dalle (`EC2` § 9.3.1.1) : `122 mm²/m` ici |
| `p_ELS` / `p_ELU` | Charges surfaciques de calcul (ELS caractéristique / ELU fondamental) |
| `D-28` | Décision : **aucun joint de dilatation** dans le bâtiment |
| `D-35` | Décision : la recharge de `15 cm` s'applique au **dallage**, sur **100 % de son emprise** |
| `PA-03` | Point d'arrêt créé par cette note : sondage du plancher haut d'étage |

---

## 2. DONNÉES D'ENTRÉE, MODES ET EXCLUSIONS

| Donnée | Valeur | Source | Statut |
|---|---|---|---|
| Solives A : section, entraxe, portée | `80 × 180 mm`, `0,50 m`, `2,77 m` | `D3` p. 10 · `EXI-01a` | **Contractuelle** |
| Classe de bois A | `C18` | `D3` p. 10 · `EXI-03` | **Hypothèse de calcul** du diagnostic |
| Poutre maîtresse A | `b = 200`, `h = 150 mm`, portée `4,34 m` | `D3` p. 10 · `EXI-01b` | **Contractuelle** |
| Plancher B | `IPE 160` @ `0,72 m`, `IPE 330`, hourdis `7 cm`, chape `10 cm` | `D3` p. 11-12 | **Contractuelle** |
| Plancher haut C | **inconnu** | `D3` p. 4 et 10 | **Donnée absente, prouvée** (`V14`) |
| Charges A / B / D | `1,80` / `4,71` / `7,75 kN/m²` (g) · `2,50` (q) | `B-21 Ind. C` § 3.5, 3.2, 3.6 | **Contractuelles** (`D-32`, `D-35`) |
| Portance du sol | `q_ELS ≤ 300 kPa` · `q_ELU ≤ 490 kPa` | `GEOEXPERTS` G2 AVP · `D-02`/`D-03` | **Contractuelle, non mesurée** |
| Béton dallage | `C25/30`, `c_nom = 30 mm` | `B-20` · `H-23` | **Contractuelle** |

**Exclusions déclarées, chacune avec son destinataire :**

| Exclu | Destinataire | Pourquoi |
|---|---|---|
| Section des `IPE 160` et `IPE 330` | **`B-45`** | EC3, pas EC2/EC5 |
| Moisage `R1` de la poutre `20 × 15` | **`B-45`** | Le renfort est un ouvrage métallique |
| Hourdis briques du plancher B | **`B-46`** (avis) | Maçonnerie existante, ni BA ni bois |
| Assemblages, sabots, connecteurs | **`B-50`** | Aucun assemblage n'est calculé ici |
| Tassements différentiels | **Hors mission** (`D-15`) | Mission géotechnique |
| Protection au feu | **Hors mission** | Mention reportée sur la planche |
| Vérification sismique | **Sans objet** (`D-26`) — zone de sismicité 1 | Aucune exigence EC8 |

---

## 3. DDC D'EXÉCUTION — PAR ZONE

| Zone | `g` (kN/m²) | `q` (kN/m²) | ELS car. | ELS freq. | ELS q-p | **ELU** |
|---|---|---|---|---|---|---|
| **A** — solives bois `8 × 18` @ `0,50` | 1,80 | 2,50 | 4,30 | 3,05 | 2,55 | **6,18** |
| **B** — mixte `IPE 160` @ `0,72` | 4,71 | 2,50 | 7,21 | 5,96 | 5,46 | **10,11** |
| **D** — dallage rechargé (`D-35`) | 7,75 | 2,50 | 10,25 | 9,00 | 8,50 | **14,21** |
| **C** — plancher haut | — | — | — | — | — | **non établi** |

`ψ_1 = 0,50` · `ψ_2 = 0,30` (EC0, tableau A1.1, catégorie B). Les charges permanentes de la zone A incluent le forfait cloisons `0,80 kN/m²` (`H-30`) ; celles du dallage incluent la recharge `3,30` (`D-35`) et les cloisons.

> **Ce que cette DDC a de plus que `B-21`.** `B-21` donnait des **effets de charge par porteur** ; celle-ci donne des **charges par zone de plancher**, avec les trois combinaisons ELS — parce que la flèche du bois se calcule sur la **quasi-permanente**, pas sur la caractéristique. C'est le seul endroit du dossier où cette distinction change un résultat.

---

## 4. ZONE A — SOLIVES BOIS `8 × 18` — EC5

### 4.1 Charges linéaires et sollicitations

| Grandeur | Valeur | Calcul |
|---|---|---|
| `p_ELU` | **`3,09 kN/m`** | `(1,35 × 1,80 + 1,50 × 2,50) × 0,50` |
| `M_Ed` | **`2,96 kN·m`** | `3,09 × 2,77² / 8` |
| `V_Ed` | **`4,28 kN`** | `3,09 × 2,77 / 2` |
| `W = b h²/6` | `432 000 mm³` | `80 × 180² / 6` |
| `I = b h³/12` | `38,88 × 10⁶ mm⁴` | `80 × 180³ / 12` |
| `f_m,d` | **`11,08 MPa`** | `0,80 × 18 / 1,30` (EC5 § 2.4.1, bois massif) |
| `f_v,d` | `1,23 MPa` | `0,80 × 2,0 / 1,30` |
| `f_c,90,d` | `1,35 MPa` | `0,80 × 2,2 / 1,30` |

### 4.2 Les cinq vérifications

| # | Vérification | Référence | `E_d` | `R_d` | **Ratio** | Verdict |
|---|---|---|---|---|---|---|
| 1 | Flexion | EC5 § 6.1.6 | `6,86 MPa` | `11,08 MPa` | **`0,619`** | ✅ |
| 2 | Cisaillement | EC5 § 6.1.7 | `0,446 MPa` | `1,23 MPa` | **`0,362`** | ✅ |
| 3 | Compression perpendiculaire d'appui (`l_appui = 100 mm`) | EC5 § 6.1.5 | `0,535 MPa` | `1,69 MPa` (`k_c,90 = 1,25`) | **`0,316`** | ✅ |
| 4 | Flèche instantanée (`G + Q`) | EC5 § 7.2 | `4,7 mm` | `9,2 mm` (`L/300`) | **`0,510`** | ✅ |
| 5 | Flèche finale (fluage) | EC5 § 7.2 | `6,4 mm` | `11,1 mm` (`L/250`) | **`0,576`** | ✅ |

**Le calcul de la flèche finale, en clair.** `w_fin = w_G (1 + k_def) + w_Q (1 + ψ_2 k_def)` avec `k_def = 0,60` : `1,97 × 1,60 + 2,74 × 1,18 =` **`6,4 mm`**. C'est la **seule** vérification où la charge permanente pèse plus lourd que l'exploitation — et c'est normal : le fluage ne s'applique qu'à ce qui reste.

**Déversement (EC5 § 6.3.3) : non déclenché.** Les solives sont maintenues latéralement en zone comprimée par le parquet continu et le lattis-plâtre. Le maintien est **continu**, pas ponctuel : `k_crit = 1`.

**Sur la classe `C18`.** C'est une **hypothèse de calcul du diagnostic** (`EXI-03`), pas une mesure. Si le bois s'avérait être du `C24`, les ratios baisseraient de `25 %` ; s'il s'agissait d'un résineux non classé, **aucune** des cinq vérifications ne serait opposable. La note ne prétend pas le contraire.

---

## 5. ZONE A — LA POUTRE `20 × 15` : CE QUE `B-43` TRANSMET, PAS CE QU'IL RÉSOUT

| Grandeur | Valeur |
|---|---|
| Charge apportée par les solives | **`4,28 kN/m`** |
| Réaction d'about (portée `4,34 m`) | **`9,29 kN`** par appui |
| Flèche constatée au diagnostic (`D3`) | **`72,8 mm`** pour `10,4 mm` admis (`L/417`) |

> **La poutre est hors limites d'un facteur 7, et ce n'est pas un résultat de `B-43`.** Le diagnostic l'a mesurée ; `B-20` a retenu un **moisage `R1` (`2 × UPE 200`)** ; son dimensionnement appartient à `B-45`. `B-43` fournit la **charge** (`4,28 kN/m`) et la **réaction** (`9,29 kN`) — ce sont les deux valeurs dont `B-45` a besoin, et elles sont plus faibles que celles de l'indice B de `B-21` puisque la recharge a quitté les planchers.
>
> **Ce que `B-43` peut dire de plus.** Les solives qui s'appuient sur cette poutre ne sont pas en cause : leur portée (`2,77 m`) est courte et leur flèche est vérifiée. **Le problème est la poutre, pas le plancher.**

---

## 6. ZONE B — PLANCHER MIXTE EXISTANT : RENVOI CHIFFRÉ À `B-45`

| Grandeur | Valeur |
|---|---|
| Charge surfacique ELU | **`10,11 kN/m²`** |
| Charge linéaire par solive (`e = 0,72 m`) | **`7,28 kN/m`** |
| Éléments porteurs | `IPE 160` et `IPE 330` — **EC3, `B-45`** |
| Hourdis briques `7 cm` + chape `10 cm` | Maçonnerie existante — **ni BA ni bois**, hors EC2/EC5 |
| Diagnostic (`D3` p. 12) | Flèche `IPE 160` OK · `IPE 330` OK · **déversement `IPE 160` instable** |
| Réaction d'appui `IPE 330` | **`6,9 t` = `67,7 kN`** — à vérifier sur l'appui existant (`B-46`) |

**Pourquoi `B-43` ne dimensionne pas cette zone.** Elle ne contient **aucun élément BA ni bois neuf** : des profilés (EC3 → `B-45`), un hourdis de briques (maçonnerie → `B-46` pour l'appui), un plancher existant conservé. Inventer ici un calcul EC2 sur un hourdis de briques serait une **erreur de méthode**, pas une approximation.

---

## 7. ZONE C — PLANCHER HAUT D'ÉTAGE : LE TROU DE LA CHAÎNE

| Constat | Référence |
|---|---|
| « Plancher haut non sondé » — cage centrale | `D3` p. 4 et p. 10 |
| Ni nature, ni épaisseur, ni portée établies | `B-24` § 6 (`E-07`, **sans plage plausible**) |
| La charge de toiture n'a pas de chemin démontré jusqu'au sol | `V15` — **continuité rompue** |

**Aucune formule n'est écrite, et aucune ne le sera avant le sondage.** C'est le seul endroit du dossier où `B-43` ne produit aucun chiffre — et c'est volontaire : un plancher dont on ignore s'il est en bois, en béton armé ou en hourdis ne se calcule pas « au plus défavorable », il se **sonde**.

> **Réserve `R-43-1` · Point d'arrêt `PA-03`** — sondage destructif du plancher haut d'étage (cage centrale), à réaliser **avant** `B-44` (charpente) et avant toute commande de renfort de toiture.

---

## 8. ZONE D — LE DALLAGE

### 8.1 Portance : le critère n'est pas celui qu'on croit

| Critère | Valeur | Admissible | Taux | Verdict |
|---|---|---|---|---|
| `σ_ELS` | **`10,2 kPa`** | `300 kPa` (`D-02`) | **`3,4 %`** | ✅ |
| `σ_ELU` | **`14,2 kPa`** | `490 kPa` (`D-03`) | **`2,9 %`** | ✅ |
| Charge totale à l'ELU | **`1 580 kN`** sur `111,15 m²` | — | — | — |

**Le sol ne voit pas le dallage.** `2,9 %` de sa capacité : la portance n'est pas un sujet. `B-40 Ind. F` l'avait déjà écrit ; `B-43` le confirme sur l'emprise complète.

### 8.2 Flexion : pourquoi il n'y a pas de moment à calculer

Sous une **charge répartie**, un dallage continu sur fond de forme **suit son support** : le moment de flexion tend vers zéro, et la contrainte dominante est la **compression**. Les moments réels viennent d'ailleurs :

| Source de moment | Traitement |
|---|---|
| **Tassements différentiels** | **Hors mission** (`D-15`) — mission géotechnique. Aucun moment n'est inventé à leur place |
| **Charges concentrées** | Aucune dans le programme actuel (`CHG-01`). Toute charge lourde ajoutée impose de rouvrir `B-43` |
| **Retrait gêné et effet de bord** | Traité par le **treillis** et les **joints** — c'est là que se joue la durabilité |

**Conséquence assumée :** l'épaisseur `13 cm` n'est pas « justifiée par un moment », elle est **retenue** (`B-20`) et **vérifiée par les dispositions constructives** — `A_s,min`, fissuration, joints, désolidarisation. Une note qui afficherait un moment calculé sur un dallage uniformément chargé afficherait un chiffre faux.

### 8.3 Treillis et fissuration

| Grandeur | Valeur | Référence |
|---|---|---|
| Hauteur utile | `d = 130 − 30 − 8 =` **`92 mm`** | `c_nom = 30 mm` (`H-23`), `XC1/XC2` — **pas** `50 mm` : le dallage n'est pas en fondation |
| `A_s,min` | **`122 mm²/m`** | `max(0,26 × 2,56 / 500 × b d ; 0,0013 b d)` — EC2 § 9.3.1.1 |
| Treillis retenu | **`ST25C` (`Ø7 e150`) = `257 mm²/m`** | **`2,10 ×`** `A_s,min` |
| Fissuration | `w_k ≤ 0,30 mm` | EC2 § 7.3 — règles indirectes : `Ø 7 ≤ 16 mm`, `e 150 ≤ 300 mm` |

**Le treillis n'est pas là pour reprendre la flexion — il n'y en a pas.** Il reprend le **retrait** et répartit les fissures : c'est exactement le rôle que lui donne le DTU 13.3, et c'est pourquoi il est placé **en partie haute** du dallage (à `40 mm` du nu supérieur), pas en bas.

### 8.4 Joints de retrait — et la distinction que personne ne doit confondre

| Disposition | Valeur | Justification |
|---|---|---|
| Type | **Joint de retrait scié** | NF DTU 13.3 / NF P11-213 |
| Profondeur | **`43 mm`** — `1/3` de l'épaisseur | Crée une amorce de rupture maîtrisée |
| Ouverture | Dès que le béton porte, **au plus tard 24 h** après coulage | Avant toute circulation |
| Espacement | **`4,50 m` maximum**, dans les deux sens | `111,15 m²` → **au moins 6 panneaux** de `20,25 m²` max |
| Armatures | **Aucune coupée** — le treillis est continu sous le joint | Le joint guide la fissure, il ne coupe pas la nappe |

> **`D-28` n'est pas contredite.** `D-28` interdit les **joints de dilatation** — ces dispositifs de `20 à 40 mm` qui traversent la structure et séparent deux blocs. Les **joints de retrait** sont l'exact contraire : ils ne séparent rien, ils **organisent** une fissuration qui se produirait de toute façon, et ils restent dans le même bloc structurel. Un dallage de `111,15 m²` sans joint de retrait ne serait pas « sans joint » : il serait **fissuré au hasard**.

### 8.5 Désolidarisation — la disposition qui évite le tassement différentiel

| Point | Prescription |
|---|---|
| **Périmètre** | Polystyrène `20 mm` sur toute la hauteur du dallage + mastic souple en surface |
| **Au droit de chaque semelle, poteau, mur** | Idem — y compris `SF1` (`80 × 80 × 25`, `D-30`), `P2`, `P3`, `J1` |
| **Film polyane** | `200 µm`, remonté sur `10 cm` en périphérie |
| **Consigne de coulage** | Dallage coulé **à même** la semelle ; **compactage interdit** sur le débord ; vibration à `200 mm` minimum du joint |
| **Pourquoi** | Une semelle se tasse plus qu'un dallage : sans désolidarisation, le dallage se fissure en arc au droit de l'appui |

Cette consigne est **une prescription de chantier, pas un calcul** — mais c'est celle dont l'oubli coûte le plus cher, parce qu'il ne se voit qu'après le carrelage.

### 8.6 Ce que `B-43` ne peut pas garantir sur le dallage

- **Les tassements différentiels** : hors mission (`D-15`), aucune valeur mesurée.
- **La portance réelle** : `D-02`/`D-03` sont **contractuelles**, pas mesurées ; le sondage sous `P2` reste ouvert (`PA-01`).
- **La présence de termites** : `SEC-03` n'est pas fourni. Si la commune est classée, une **barrière anti-termites physico-chimique** est à prévoir sous le dallage — réserve `R-43-4`.

---

## 9. EFFORTS AUX APPUIS — TRANSMIS À `B-50` ET `B-46`

| Appui | Ouvrage support | Effort | Unité | Destinataire |
|---|---|---|---|---|
| Solives A | mur / poutre `20 × 15` | **`4,28`** | kN par solive | `B-50` · `B-46` |
| Ligne d'appui A | appui continu | **`8,56`** | kN/m | `B-46` |
| Poutre `20 × 15` | about | **`9,29`** | kN | `B-45` · `B-50` |
| `IPE 160` (zone B) | charge linéaire | **`7,28`** | kN/m | `B-45` |
| `IPE 330` (zone B) | appui central | **`67,7`** | kN (`6,9 t`, `D3`) | `B-46` |
| Dallage | sol support | **`14,2`** | kPa (ELU) | `B-40` |

**Aucun assemblage n'est calculé ici.** `B-50` reçoit des efforts, pas des solutions : c'est lui qui choisit le sabot, la platine ou le boulon, et qui fait le contrôle croisé avec les logements prévus par `B-20`.

---

## 10. DISPOSITIONS CONSTRUCTIVES, RÉSERVATIONS ET TOLÉRANCES

| Sujet | Prescription |
|---|---|
| **Réservations** | Toute trémie coupe le treillis : elle doit être **encadrée** (2 `HA8` de part et d'autre + chapeaux). Aucune trémie n'est positionnée à ce stade — le carnet `STR-03` n'est pas fourni (`PA` si nécessaire) |
| **Rives et angles** | Renfort `HA8 e150` sur `0,80 m` en angle rentrant de dallage — zone de concentration de retrait |
| **Liaison avec `B-42`** | Les poteaux `P2`, `P3`, `J1` traversent le dallage **avec désolidarisation**, jamais en contact |
| **Liaison avec `B-40`** | `SF1` reçoit sa propre charge ; le dallage ne reprend **rien** de la semelle |
| **Enrobage** | `c_nom = 30 mm` = `c_min 15` + `Δc_dev 10` (classe d'exécution 2, NF EN 13670) — cohérent avec `H-23` |
| **Béton** | `C25/30`, `XC1` — le dallage n'est pas exposé aux chlorures ni au gel sévère |
| **Incendie** | **Hors lot GO** — mention reportée sur la planche |
| **Sismique** | **Sans objet** — `D-26`, zone de sismicité 1 |

---

## 11. AUTO-CONTRÔLE — HUIT POINTS, DÉCLARÉS SANS ARRONDIR

| # | Point de la fiche `B-43` | Verdict | Preuve / limite |
|---|---|---|---|
| 1 | Chaque zone a ses charges et ses combinaisons ELS et ELU | ✅ **CONFORME** | § 3 — 3 zones chiffrées, 4 combinaisons dont 3 ELS ; zone C déclarée **non établie** |
| 2 | Chaque zone a son ferraillage ou ses sections complètes | ⚠️ **PARTIEL DÉCLARÉ** | Zone A : 5 vérifications EC5 · zone D : treillis `ST25C` et `A_s,min` · **zone B renvoyée à `B-45`** (profilés), **zone C impossible** (`E-07`) |
| 3 | Chaque zone satisfait `A_min` et les dispositions constructives | ✅ **CONFORME** pour D | `257 mm²/m` ≥ `122 mm²/m` ; enrobage, joints, désolidarisation prescrits |
| 4 | Chaque appui a ses efforts transmis à `B-50` | ✅ **CONFORME** | § 9 — 6 appuis, efforts et destinataires nommés |
| 5 | Chaque réservation est compatible avec le ferraillage | ⚠️ **PARTIEL DÉCLARÉ** | Aucune trémie n'est fournie (`STR-03` absent) ; la **règle d'encadrement** est prescrite, le calepinage reste à faire |
| 6 | Joints de retrait et de désolidarisation prévus | ✅ **CONFORME** | § 8.4 et 8.5 — espacement, profondeur, délai, polystyrène, mastic, consigne de coulage |
| 7 | Échelle cohérente | ✅ **CONFORME** | Planche `IndA` : détails `1:5`, A3 paysage, unités DXF mm |
| 8 | Cartouche complet | ✅ **CONFORME** | Indice, date, mode `PARTIEL-DÉCLARÉ`, filigrane, mention incendie |

**Verdict : 6 conformes, 2 partiels déclarés — la brique n'est pas « 8/8 » et ne le prétend pas.** Les deux points partiels ne sont pas des négligences : l'un porte sur des éléments qui **ne relèvent pas de `B-43`** (profilés), l'autre sur une donnée **qui n'existe pas** (plancher haut non sondé). Les déclarer conformes serait exactement le genre de fausse complétude que le dossier cherche à éviter.

---

## 12. TRANSMISSIONS ET RÉSERVES

### 12.1 Ce que `B-43` transmet

| Brique | Ce qu'elle reçoit |
|---|---|
| **`B-45`** | `IPE 160` : `7,28 kN/m` · `IPE 330` : charge et réaction · poutre `20 × 15` : `4,28 kN/m` et `9,29 kN` par about — **moisage `R1` à dimensionner** |
| **`B-46`** | `8,56 kN/m` sur les murs d'appui des solives · `67,7 kN` sous l'`IPE 330` · contrainte de dallage `14,2 kPa` |
| **`B-50`** | Réactions d'appui (§ 9) ; aucune solution d'assemblage n'est proposée |
| **`B-60`** | Planche `FLORA_B43_DALLAGE_IndA` — les principes sont opposables, **le calepinage des joints reste à reporter sur la vue cotée** |
| **`B-03`** | `R-43-1` à `R-43-4` (§ 12.2) |

### 12.2 Réserves nées de cette brique

| Réf. | Objet | Conséquence si non levée | Destinataire |
|---|---|---|---|
| **`R-43-1`** | **Plancher haut d'étage non sondé** (`E-07`) | Aucune vérification possible ; la chaîne de charge de la toiture reste rompue (`V15`) | Sondage — `PA-03` · `B-44` |
| **`R-43-2`** | **Classe de bois `C18` non mesurée** (`EXI-03`) | Les 5 vérifications de la zone A valent pour `C18` ; un bois non classé les invaliderait | Relevé / `B-46` |
| **`R-43-3`** | **État sanitaire des abouts** des solives (reprise de `R-24-B2`) | Ne bloque pas le calcul, **bloque la réception** de la zone A | `B-60` / ouverture |
| **`R-43-4`** | **Classement termites inconnu** (`SEC-03` absent) | Si la commune est classée, barrière anti-termites à ajouter sous le dallage | MOE / mairie |

### 12.3 Point d'arrêt créé

**`PA-03` — sondage destructif du plancher haut d'étage** (cage centrale). Il conditionne `B-44` (charpente) et toute commande de renfort de toiture. Il ne conditionne **pas** le dallage, qui peut être coulé sans attendre.

---

## 13. POINT DE CONTRÔLE HUMAIN

**Trois questions, et trois seulement, attendent une réponse de votre part :**

1. **Le plancher haut doit-il être sondé maintenant ?** C'est le seul moyen de fermer `R-43-1` et de débloquer `B-44`. Sans lui, la charpente restera calculée sur une hypothèse de report.
2. **La commune est-elle classée termites ?** Un arrêté préfectoral suffit à répondre ; à défaut, la barrière est à prévoir par précaution (`R-43-4`).
3. **Les trémies et réservations sont-elles arrêtées ?** Tant qu'elles ne le sont pas, le treillis est prescrit **continu** et les encadrements seront à reporter au `B-60`.

**Brique `B-43` livrée en indice A — en attente de votre `GO` ou de vos observations.**
