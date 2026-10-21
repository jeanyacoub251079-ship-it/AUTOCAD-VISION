# B-46 — MAÇONNERIE : VÉRIFICATION ET CONCEPTION — CROISSY-FLORA

> **NOS ÉTUDES SONT RÉALISÉES AVEC LES HYPOTHÈSES `f_k = 1,5 MPa`, `E = 1 500 MPa` ET `f_vk0 = 0,15 MPa`.**
> **LA CONFIRMATION PAR ESSAIS EST HORS DE NOTRE MISSION ET À LA CHARGE DU MAÎTRE D'OUVRAGE.**
> **SI LES ESSAIS NE SONT PAS CONCLUANTS, LA REPRISE DE NOS ÉTUDES FAIT L'OBJET D'UNE PRESTATION COMPLÉMENTAIRE CHIFFRÉE** (`D-34`, 20/10/2026).
> **`D-09` — « AU MÊME NIVEAU QUE LES FONDATIONS EXISTANTES… RAJOUTER DU GROS BÉTON… CETTE NOTE EST À INDIQUER SUR LES PLANS ET NOTE DE CALCULS »** — arase à **−1,00 m / TN MINIMUM**, égalisation par gros béton si écart.
> **`D-28` — AUCUN JOINT DE DILATATION.** Aucun chaînage, aucun sommier ne franchit un joint : les appuis s'arrêtent à `20 mm` du nu de toute discontinuité.
> **`D-26` — SANS OBJET SISMIQUE** : zone de sismicité 1, **AUCUNE vérification sismique** n'est produite.

| Champ | Valeur |
|---|---|
| **Brique / famille** | `B-46` — Maçonnerie (vérification de l'existant + orientations de renforcement) — **famille MACONNERIE** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** — hypothèses notifiées `H-25` / `H-26` / `H-27` consommées sous `D-34` |
| **Bloc** | **A** (vérification de l'existant) + **orientations** du bloc B (`MAT-09` à `MAT-12` bloquantes : aucun dimensionnement de maçonnerie neuve) |
| **Régime** | **OUTILLÉ** — script `_scripts/b46_maconnerie.py` (`V13`), journal `_rendus/b46_maconnerie.txt` / `.json` |
| **Fiche de référence** | `carnac/CARNAC_v3.0/06_PHASE_4_CALCULS/B-46_Maconnerie.md` — Étapes A1–A3, B1–B6 |
| **Briques amont** | `B-20` (sommiers `S1`/`S2`, implantation) · `B-21` Ind. C (efforts transmis) · `B-24` Ind. C (`E-01` à `E-08`) · `B-25` (voiles, vent) · `B-40` (soubassement, `D-19`) · `B-45` Ind. A (8 réactions) · `B-50` Ind. A (`R-50-5`) |
| **Briques aval** | `B-49` (linteaux existants `E-08`) · `B-50` (scellements — aucun transmis ici) · `B-60` (plans, chaînages, coussins) |
| **`COMPLET`** | **INTERDIT** (`V12`) : `MAT-07` non mesurée · `EXI-05` verrou · `GEO-03` non relevé · `MAT-09`/`MAT-10`/`MAT-11`/`MAT-12` bloquantes |

**Ce que cette note fait.** Elle vérifie la maçonnerie existante du pavillon Flora sous les contraintes que **nos propres ouvrages** lui transmettent : compression des voiles, **contrainte localisée sous les 8 appuis** `F1` à `R3` (c'est la réponse à `R-50-5`), appuis des neufs sur le soubassement, flambement, cisaillement. Puis elle déclare les **orientations** de renforcement possibles — sans rien dimensionner qui dépende de `MAT-09` à `MAT-12`.

**Ce qu'elle ne fait pas.** Elle ne calcule **aucun scellement** (`B-50`). Elle ne conçoit **aucune technique de spécialiste** (injection, tirants actifs, précontrainte, reprise en sous-œuvre → `B-40` + phasage). Elle ne dimensionne **aucune protection incendie** : mention générique seule. Elle ne produit **aucune vérification sismique** (`D-26`). Elle ne corrige **aucune contrainte transmise** : si un appui passe pas, c'est le sommier ou l'appui qui se renforce — jamais la réaction qui diminue.

---

## 1. GLOSSAIRE DES CODES

| Code | Objet |
|---|---|
| `MAT-07` | Nature et résistance de la maçonnerie — **non mesurée** (`D-2` f. 03, `D4` p. 19) |
| `MAT-09` / `MAT-10` / `MAT-11` / `MAT-12` | Classe de bloc / classe de mortier / type de maçonnerie / chaînages — **tous bloquants ou non relevés** (`D1 § 01.2.1.7.5`) |
| `EXI-05` | Contrainte admissible transmise à l'existant — **verrou** (« à la limite », `D3` p. 17) |
| `GEO-03` | Épaisseurs des murs — **non relevées** (`B-01`) ; `t_eq` issus des blocs `D5` via `B-25` |
| `H-25` / `H-26` / `H-27` | `f_k = 1,5 MPa` · `E = 1 500 MPa` · `f_vk0 = 0,15 MPa` · `σ_d = 0,30 MPa` — hypothèses de `B-25`, arbitrées par `D-34` |
| `D-34` | Hypothèse de maçonnerie — essais hors mission, reprise chiffrée si essais non concluants |
| `D-35` | Recharge `15 cm` sur le **dallage seul** (sans effet ici : les voiles sont chargés par `B-21` Ind. C) |
| `S1` / `S2` | Sommiers BA d'appui en tête de mur : `20×40×20` (`800 cm²`) / `20×ép. mur×20` (`1 000 cm²`) — `B-20`, `D2` Folio 01 |
| `E-01` à `E-08` | Éléments existants non sondés de `B-24` (`E-01` = murs de moellons) |
| `R-15` / `R-16` | Réserves historiques : contrainte admissible · résistance des moellons et du mortier — **maintenues** |
| `R-50-5` | Réserve `B-50` : les 8 appuis sur maçonnerie non justifiés — **traitée par la présente note** |
| `PA-01` / `PA-03` | Points d'arrêt : reconnaissance des voiles et chaînages · sondage du plancher haut |

---

## 2. `A1` — DONNÉES D'ENTRÉE ET PREUVE D'ÉPUISEMENT (`V14`)

| Code | Objet | Statut retenu | Source consommée |
|---|---|---|---|
| `MAT-07` | Résistance de la maçonnerie | **Hypothèse `H-25`** (`f_k = 1,5 MPa`) sous `D-34` | `D2` f. 03 · `D4` p. 19 |
| `EXI-05` | Contrainte admissible | **Verrou** — remplacé par `f_d = f_k/γ_M` sous `D-34` | `D3` p. 17 |
| `GEO-03` | Épaisseurs des murs | **`t_eq` `0,15` à `0,88 m`** (blocs `D5`, `B-25` § 2.3) — épaisseur réelle non mesurée (`PA-01`) | `B-25` § 2.3 |
| `MAT-09` à `MAT-11` | Bloc / mortier / type | **Bloquants** → bloc B limité aux orientations | `D1 § 01.2.1.7.5` |
| `MAT-12` | Chaînages existants | **Aucun relevé** → orientation `EC6 § 8.5` | `D2` · `D3` · `PA-01` |
| `CHG-07` | Sismique | **SANS OBJET** (`D-26`, zone 1) | `D2` p. 1 |
| Appuis `F1`→`R3` | 8 réactions `11,5` à `77,4 kN` | **Transmises par `B-45` Ind. A § 11** | `B-45` |
| Sommiers | `S1` ×10, `S2` ×6 | Aires `800` / `1 000 cm²` (`B-20`) | `D2` Folio 01 |

**Preuve d'épuisement (V14).** `D2` f. 03 (soubassement moellons, semelle `25×25`) · `D3` p. 10–17 (planchers, pieds de poteaux « à la limite ») · `D4` p. 19 (« mur moellons apparents ») · `D5` (blocs géomètre, géométrie des voiles) · `B-20` § 4–5 (sommiers, implantation des appuis) · `B-21` Ind. C § 6–7 (`N_ELU` par porteur) · `B-24` Ind. C § 2 (`E-01` à `E-08`) · `B-25` § 2–3 (voiles, vent) · `B-45` § 10–11 (8 réactions) · `B-50` § 8 (`A6`, `R-50-5`). **Aucune donnée n'est déclarée absente sans avoir été cherchée dans ces pièces.**

**Faits acquis.** Le pavillon est en **maçonnerie porteuse de moellons** (façades mi-brique mi-moellons, refends `50 cm`, soubassement « pierre dure ») : `B-25` § 2 en a extrait **12 voiles au RDC** et **9 au R+1**. Les appuis de nos frangements et renforts passent par **16 sommiers BA en tête de mur** (`S1`, `S2` — `B-20`), pas par des platines posées à nu.

---

## 3. Z1 — VOILES PORTEURS : COMPRESSION ET FLAMBEMENT (`EC6 § 6.1.2`, `§ 5.5`)

**Méthode.** Compression : `σ_d ≤ Φ_i · f_d` avec `f_d = f_k/γ_M = 1,5/2,5 = 0,60 MPa` (`EC6 § 3.6.1`, `γ_M` = 2,5 usage `B-25`/`H-26`). Flambement (`EC6 § 5.5`) : `λ = h_ef/t_ef ≤ 27`, `e_init = h_ef/450`, `Φ_i = 1 − 2·e_init/t` (`Annexe G`), `h_ef = 1,00·h = 3 000 mm` (planchers bois/mixtes → `ρ₂ = 1,0`, par prudence).

| Grandeur | Valeur | Origine |
|---|---|---|
| Contrainte moyenne sur les voiles RDC | `σ_d = 0,069 MPa` | `B-21` Ind. C § 7 (`1 290 kN / 18,79 m²`) |
| Contrainte locale retenue | `σ_d = 0,159 MPa` (max `N/A_inf`, sous `P1`) | `B-21` Ind. C § 6.2 |
| `λ = h/t_eq` | `3,4` (`M03`, `0,88 m`) à **`20,0`** (`M05`, `0,15 m`) | `B-25` § 2.3 — **tous ≤ 27** |
| `Φ_i` minimum | **`0,911`** (`M05`) | `e_init = 6,7 mm` |
| **Taux maximum** | **`0,290`** (`M05`, `0,159/(0,911×0,60)`) | script `[2]` |
| **Verdict Z1** | **OK — 12/12 voiles** | — |

**Cisaillement.** `f_vk = f_vk0 + 0,4·σ_d = 0,15 + 0,4×0,069 = 0,178 MPa` → `f_vd = 0,071 MPa` (`γ_M = 2,5`). La sollicitation est celle du vent, déjà arbitrée en `B-25` : **`τ/f_vk ≤ 0,043`** (§ 7, `H-27`). **Z1 OK** — la maçonnerie existante est très peu sollicitée en compression ; c'est **l'appui localisé qui gouverne** (Z2).

---

## 4. Z2 — LES 8 APPUIS SUR MAÇONNERIE : RÉPONSE À `R-50-5` (`EC6 § 6.1.3`)

**Méthode — charge concentrée (`EC6 § 6.1.3`).** `N_Edc ≤ N_Rdc = β · A_b · f_d` **(6.10)**, avec le facteur de majoration **(6.11)** :

> `β = (1 + 0,3·a₁/h_c) · (1,5 − 1,1·A_b/A_ef)`, plafonné par `min(β ; 1,5 ; 1,25 + a₁/(2·h_c))`, plancher `1,0` ; `A_b/A_ef ≤ 0,45`.
> `l_efm = min(a₁; s) + w_b + min(a₂; s)` avec `s = (h_c/2)·tan 30° = 866 mm` (dispersion `60°` vers la mi-hauteur, fig. 6.2) ; `A_ef = l_efm · t`.
> `A_b` = aire du sommier (`S1` 800 cm², `S2` 1 000 cm² — `B-20`) · appui minimum `90 mm` (`EC6 § 8.1.6`) · excentricité `≤ t/4` (`6.1.3(4)`) → **sommier centré en épaisseur, porté au plan**.

**`a₁` (distance au bout de mur) n'est pas relevée** (implantation cotée à lever — `B-20` Planche 1 / `B-60`) : la vérification est menée sur la **plage déclarée** `a₁ = 0 / 0,50 / 1,00 / 2,00 m`, avec le seuil `a₁*` calculé. **(`R-46-1`)**

| Appui | `V_Ed` | Sommier | `N_Rdc (β=1)` | `N_Rdc (a₁=0)` | `N_Rdc (a₁=2 m)` | `a₁*` | Verdict |
|---|---|---|---|---|---|---|---|
| `F1a/b/c` | `44,6 kN` | `S2` | `60,0` | `75,0` | `90,0` | — | **OK** |
| `F2` | `62,4 kN` | `S1` | `48,0` | `60,0` | `72,0` | **`0,30 m`** | **OK si `a₁ ≥ 0,30 m`** |
| `F3` | `61,6 kN` | `S1` | `48,0` | `60,0` | `72,0` | **`0,20 m`** | **OK si `a₁ ≥ 0,20 m`** |
| `F4` | `11,5 kN` | `S1` | `48,0` | `60,0` | `72,0` | — | **OK** |
| `R1` | `77,4 kN` | `S2` | `60,0` | `75,0` | `90,0` | **`0,24 m`** | **OK si `a₁ ≥ 0,24 m`** |
| `R2-N` | `46,2 kN` | `S2` | `60,0` | `75,0` | `90,0` | — | **OK** |
| `R2-S` | `35,9 kN` | `S2` | `60,0` | `75,0` | `90,0` | — | **OK** |
| `R3-N/S` | `23,1 kN` | `S1` | `48,0` | `60,0` | `72,0` | — | **OK** |

*(résistances en kN — script `[3]`, `_rendus/b46_maconnerie.json`)*

**Lecture — trois points, dans cet ordre.**

1. **Cinq appuis sur huit sont admissibles même sans majoration** (`β = 1`) : `F1a/b/c`, `F4`, `R2-N`, `R2-S`, `R3-N/S`. Leur verdict ne dépend ni de `a₁`, ni du groupe des unités.
2. **`R1`, `F2` et `F3` — les trois plus chargés — exigent la majoration `EC6 § 6.1.3`** (`β ≈ 1,25 à 1,5`) **et** un sommier posé à plus de `0,20` à `0,30 m` du bout de mur. En borne basse `a₁ = 0`, ils sont **NON admissibles** (`η = 1,03` à `1,04`).
3. **En `β = 1`** (unités des groupes 2/3/4 — `EC6 § 6.1.3(3)` — ou lit de mortier partiel), **`R1`, `F2`, `F3` sont NON conformes** (`η = 1,28` à `1,29`). Le groupe des moellons n'est pas établi : **(`R-46-2`)**.

**Ce que la note ne fait pas ici.** Elle ne « fait pas passer » les trois appuis en retenant `a₁` favorable : elle **signale** que leur admissibilité dépend de deux données non relevées (`a₁`, groupe des unités) et elle **prescrit le renfort** qui rend le verdict inconditionnel : **coussin de répartition ou sommier élargi `w_b ≥ 300 mm`** sous `R1`, `F2`, `F3` (orientation bloc B, § 8). Avec `w_b = 300 mm`, les trois appuis passent **dès `a₁ = 0`** (`N_Rdc ≥ 84 kN`) — le renfort supprime la dépendance.

---

## 5. Z3 — APPUIS DES NEUFS SUR SOUBASSEMENT MOELLONS

Les pieds `P1-N`, `P1-S`, `P3`, `J1` reposent sur le soubassement moellons (`D2` f. 03, `B-40` Z-xx) : **vérification en fouille ou semelle type `60×60` (`D-14`)**, sous nuages `D-19`.

| Appui | `N_ELU` (`B-21` C) | `A` (semelle `60×60`) | `σ` | Taux vs `f_d = 0,60` | Verdict |
|---|---|---|---|---|---|
| `P1-N` / `P1-S` | `100,3 kN` | `0,36 m²` | `0,279 MPa` | `0,464` | **OK** |
| `P3` | `35,8 kN` | `0,36 m²` | `0,099 MPa` | `0,166` | **OK** |
| `J1` | `39,8 kN` | `0,36 m²` | `0,111 MPa` | `0,184` | **OK** |

Sous réserve de la **reconnaissance du soubassement en fouille** (`D-19`, `R-31bis`, `H-15`) — qui est une condition de chantier, pas un calcul.

---

## 6. Z4 — LINTEAUX EXISTANTS SOUS NOS APPUIS (`E-08`)

`B-24` Ind. C (`E-08`) : les linteaux existants au-dessus des baies (désordre 1, façade Est) **n'ont pas de capacité connue**. `B-20` place les sommiers `S1` de `R3` **sur les abouts de murs**, l'ancien linteau bois déformé étant court-circuité. Reste à garantir que **tout sommier tombe sur maçonnerie saine**, hors emprise des linteaux : **(`R-46-4`)**, vérification des linteaux eux-mêmes → **`B-49`**.

---

## 7. SENSIBILITÉ `f_k` — NON CONTRACTUELLE (méthode `B-24`)

Taux `= V_Ed / N_Rdc(a₁ = 2 m)` — borne favorable — pour `f_k` de `0,5` à `2,0 MPa` :

| Appui | `f_k = 0,5` | `f_k = 1,0` | `f_k = 1,5` *(retenu)* | `f_k = 2,0` |
|---|---|---|---|---|
| `F1a/b/c` | `1,49` | `0,74` | `0,50` | `0,37` |
| `F2` | `2,60` | `1,30` | `0,87` | `0,65` |
| `F3` | `2,57` | `1,28` | `0,86` | `0,64` |
| `F4` | `0,48` | `0,24` | `0,16` | `0,12` |
| `R1` | `2,58` | `1,29` | `0,86` | `0,65` |
| `R2-N` | `1,54` | `0,77` | `0,51` | `0,39` |
| `R2-S` | `1,20` | `0,60` | `0,40` | `0,30` |
| `R3-N/S` | `0,96` | `0,48` | `0,32` | `0,24` |

**Lecture.** `R1`, `F2`, `F3` dépassent `1,0` dès `f_k ≤ 1,2 MPa` environ, **même à `a₁` favorable** : leur admissibilité **repose entièrement sur l'hypothèse `f_k = 1,5 MPa`** (`D-34`). C'est exactement le cas prévu par la clause : les essais ne sont pas notre affaire, mais leur résultat a un prix — celui de la reprise.

---

## 8. BLOC B — ORIENTATIONS DE RENFORCEMENT (`MAT-09` à `MAT-12` bloquants)

1. **`R1`, `F2`, `F3` — coussin de répartition ou sommier élargi (`w_b ≥ 300 mm`).** Orientation portée au plan (`B-60`) ; dimensionnement définitif **reporté** (classe de bloc, mortier et type de maçonnerie bloqués). Aucune valeur de résistance de coussin n'est chiffrée ici.
2. **Chaînages (`EC6 § 8.5`) — aucun chaînage existant relevé (`MAT-12`).** Prescription d'orientation : **chaînage horizontal en tête de mur**, liaison planchers/murs et fondations, continuité aux angles (`EC6 § 8.5.1` à `8.5.3`). Ces dispositions relèvent des **dispositions constructives** de l'`EC6` — **pas d'une vérification sismique** (`D-26`). Aucun scellement n'est calculé : les efforts des chaînages rapportés seraient transmis à `B-50`, **mais aucun chaînage n'est dimensionné dans cette note**.
3. **Spécialiste.** Injection de résine, tirants actifs, précontrainte → **spécialiste** (`G5`). Reprise en sous-œuvre par passes alternées → **`B-40` + phasage**. Signalés, jamais conçus.
4. **Protection incendie** : « protection au feu adéquate à prévoir — hors lot GO » — **mention générique seule**, jamais dimensionnée.

---

## 9. RÉSERVES ET EFFETS SUR LE REGISTRE

| Réserve | Objet | Statut | Fondement | Levée par |
|---|---|---|---|---|
| **`R-46-1`** | `a₁` réel (sommier → bout de mur) non relevé — `R1`, `F2`, `F3` non admissibles en `a₁ = 0` | **Ouverte** | `GEO-03` non relevé · implantation cotée `B-20` | Relevé sur `B-20` Planche 1 / chantier — ou **coussin (`§ 8.1`)** qui rend le verdict inconditionnel |
| **`R-46-2`** | Groupe des unités de moellons (β = 1 si groupes 2/3/4 — `EC6 § 6.1.3(3)`) | **Ouverte** | `MAT-07` non mesurée | Essais `D-34` (hors mission) ou coussin (`§ 8.1`) |
| **`R-46-3`** | Épaisseurs réelles (`GEO-03`) et chaînages (`MAT-12`) non relevés — orientations `EC6 § 8.5` non dimensionnables | **Ouverte** | `PA-01` | Sondages `PA-01` |
| **`R-46-4`** | Tout sommier doit tomber sur maçonnerie saine, hors emprise des linteaux `E-08` | **Ouverte** | `B-24` `E-08` | `B-49` + contrôle d'implantation `B-60` |

**Effets sur les réserves existantes.**

- **`R-50-5` (`B-50`) — CLOSE par la présente note.** Les 8 appuis sont vérifiés : **5 justifiés sans réserve, 3 (`R1`, `F2`, `F3`) poursuivis en `R-46-1`/`R-46-2`** avec la prescription de coussin qui les rend inconditionnels.
- **`R-15` / `R-16` (contrainte admissible, résistance moellons/mortier) — MAINTENUES.** `D-34` fixe l'hypothèse d'étude, pas la mesure : les réserves ne ferment qu'aux essais.
- **`D-36` (21/10/2026)** — le client accepte le **remplissage béton `C25/30`** des `UPE 200` de `R3` : `R-50-2` est **close**, l'exécution du remplissage est renvoyée à `B-60`.

---

## 10. AUTO-CONTRÔLE DÉCLARÉ — ZONE PAR ZONE

| Zone | Vérifications | Verdict | Preuve / limite |
|---|---|---|---|
| **Z1** voiles (12 RDC) | Compression `EC6 § 6.1.2` + flambement `§ 5.5` | **OK** — taux max `0,290` | `Φ_i ≥ 0,911`, `λ ≤ 20 ≤ 27` |
| **Z2** 8 appuis | `EC6 § 6.1.3` (6.10)/(6.11) | **5 OK · 3 sous réserve** | `R-46-1`, `R-46-2` — coussin prescrit |
| **Z3** neufs sur soubassement | `σ ≤ f_d` | **OK sous fouille** | Nuages `D-19`, `R-31bis` |
| **Z4** linteaux `E-08` | — | **RENVOI `B-49`** | `R-46-4` |
| Cisaillement | `τ/f_vk` (`B-25` § 7) | **OK** (`≤ 0,043`) | `H-27`, `f_vd = 0,071 MPa` |
| Chaînages `EC6 § 8.5` | `MAT-12` non relevé | **ORIENTATION** | `R-46-3`, `B-60` |

**Points DE PRINCIPE.** Aucune capacité inventée · aucune contrainte transmise réduite · `f_k` reste une hypothèse (`D-34`) · aucun scellement calculé · aucune protection incendie dimensionnée · aucune vérification sismique (`D-26`).

**Points À LEVER.** `a₁` réel (`R-46-1`) · groupe des unités (`R-46-2`) · épaisseurs et chaînages (`R-46-3`, `PA-01`) · implantation des sommiers hors linteaux (`R-46-4` → `B-49`).

---

## 11. LIVRABLES ET CHAÎNE

| Pièce | Fichier | Contenu |
|---|---|---|
| Note | `06_CALCULS/B-46_Maconnerie.md` | La présente |
| Script | `_scripts/b46_maconnerie.py` | Calculs `EC6 § 5.5/6.1/6.2`, sensibilité, planche (`V13`) |
| Journal | `_rendus/b46_maconnerie.txt` / `.json` | Toutes les applications numériques citées |
| Planche | `_plans/FLORA_B46_MACONNERIE_IndA.{dxf,pdf,png}` | Calques `MACON-*` · **filigrane `NE PAS EXÉCUTER SANS EXE COTÉ ET VISA`** · clause `D-34` en majuscules · `AUCUN JOINT DE DILATATION` · `D-09` · zéro cloison, zéro isolation · audit DXF **0 erreur** |

**Chaîne.** `B-45` Ind. A (8 réactions) → **`B-46` Ind. A** (contraintes localisées, `R-50-5` traitée) → `B-49` (`E-08`) · `B-60` (coussins, chaînages, plans) · `B-03` (**Ind. AA** : `D-36`, `R-50-2` close, `R-50-5` close, `R-46-1..4`).

**Nomenclature des appuis (à conserver).** `10` sommiers `S1` `20×40×20 BA` · `6` sommiers `S2` `20×ép. mur×20 BA` — **centrés en épaisseur** (`e ≤ t/4`), lit de mortier complet, jamais sur linteau existant.
