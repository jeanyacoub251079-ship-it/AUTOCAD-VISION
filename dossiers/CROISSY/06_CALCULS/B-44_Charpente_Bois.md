# B-44 — CHARPENTE BOIS — CROISSY-FLORA

> **NOS ÉTUDES SONT RÉALISÉES AVEC LES HYPOTHÈSES `f_k = 1,5 MPa`, `E = 1 500 MPa` ET `f_vk0 = 0,15 MPa`.**
> **LA CONFIRMATION PAR ESSAIS EST HORS DE NOTRE MISSION ET À LA CHARGE DU MAÎTRE D'OUVRAGE.**
> **SI LES ESSAIS NE SONT PAS CONCLUANTS, LA REPRISE DE NOS ÉTUDES FAIT L'OBJET D'UNE PRESTATION COMPLÉMENTAIRE CHIFFRÉE** (`D-34`, 20/10/2026).
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE** (zone de sismicité 1).
> **`D-28` — AUCUN JOINT DE DILATATION.**
> **`D-38` — `B-41` ET `B-48` SANS OBJET** (« il n'y en a pas sur le projet », 21/10/2026).

| Champ | Valeur |
|---|---|
| **Brique / famille** | `B-44` — Charpente bois |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (`H-29` toiture, `H-14` périmètre, existant non sondé) |
| **Régime** | **OUTILLÉ** — `_scripts/b44_charpente.py` (`V13`) |
| **Fiche** | `carnac/CARNAC_v3.0/06_PHASE_4_CALCULS/B-44_Charpente_Bois.md` |
| **Amont** | `B-20` B · `B-21` C · `B-22` · `B-23` · `B-24` C · `B-25` E · `B-43` B |
| **Aval** | `B-50` (efforts fournis, aucun Johansen ici) · `B-60` (contreventement de toiture, ventilation) |
| **`COMPLET`** | **INTERDIT** (`V12`) : `EXI-01g` / `MAT-06` existant absents, `CHG-04` = `H-29`, deux zones non cotées |

**Ce que cette note fait.** Elle dimensionne les **bois neufs** prescrits au `D2` f. 02 et repris par `B-20` : **3 pannes**, **2 demi-fermes** (arbalétrier + entrait), **contrefiches** sur la ferme tradi. Classe **`C24`** : c'est une **spécification d'approvisionnement** (comme `S275` pour l'acier), pas une mesure. Classe de service **2** (`MAT-08`, produite ici). Les demi-fermes sont **désolidarisées du plancher** : elles chargent les murs Files A et C, **pas** `E-07`.

**Ce qu'elle ne fait pas.** Elle ne calcule **aucun bois existant** (`E-04`, `E-05`, `E-06` restent à `B-24` PARAMÉTRIQUE). Elle ne calcule **aucun assemblage** (`B-50`). Elle ne dimensionne **aucune protection incendie**. Elle ne relève **aucune** des deux zones non cotées. Elle ne réduit **aucune** contrainte `B-45` / `B-46`. Elle ne déclare pas `PA-03` close : ce point d'arrêt appartient à `B-43`.

---

## 1. GLOSSAIRE DES CODES

| Code | Objet |
|---|---|
| `PN1` / `PN2` / `PN3` | Trois pannes **neuves** `C24` `75 × 200` (`D2` f. 02, `B-20`) |
| `DF1` / `DF2` | Deux demi-fermes **neuves** en sous-œuvre, File A–C, **désolidarisées** du plancher |
| `CF` | Contrefiches **neuves** sur la ferme tradi Ouest (désordre 6), **après purge** |
| `E-04` | Potelets existants (désordre 8) — **supprimés** par `DF1`/`DF2` |
| `E-05` | Ferme tradi existante (désordre 6) — `B-24`, hors calcul |
| `E-06` | Pannes existantes — `B-24`, hors calcul |
| `E-07` | Plancher haut d'étage, nature inconnue — **non chargé** par les neufs |
| `PA-03` | Sondage de `E-07` — point d'arrêt de **`B-43`**, pas de `B-44` |
| `H-14` | Charpente dans le lot 01 malgré l'absence de section bois au CCTP (`C-07` / `R-22`) |
| `H-29` | `G_toiture = 0,95 kN/m²` (`CHG-04` absent) |
| `MAT-08` | Classe de service **2** — produite par la présente |
| `D-38` | `B-41` et `B-48` **SANS OBJET** (21/10/2026) |
| `ZN1` / `ZN2` | Deux « ZONES NON RELEVÉES » du `D2` f. 02 — nuage `D-19` |

---

## 2. INVENTAIRE ET PREUVE D'ÉPUISEMENT (`V14`)

| Réf. | Ouvrage | Section | `L` | Statut |
|---|---|---|---|---|
| **`PN1/2/3`** | Pannes neuves | **`75 × 200 C24`** | `3,20 m` | **NEUF — OK `0,830`** |
| **`DF-arb`** | Arbalétrier demi-ferme | **`100 × 200 C24`** | `3,62 m` | **NEUF — OK `0,626`** |
| **`DF-ent`** | Entrait demi-ferme | **`75 × 200 C24`** | `3,20 m` | **NEUF — OK `0,108`** |
| **`CF`** | Contrefiches | **`75 × 225 C24`** | `2,62 m` | **NEUF — OK `0,940`** |
| `E-04` | Potelets | non sondé | — | **SUPPRIMÉS** par `DF` |
| `E-05` | Ferme tradi | non sondé | `9,90 m` | `B-24` — purge puis `CF` |
| `E-06` | Pannes existantes | non sondé | `3,20 m` | `B-24` |
| `E-07` | Plancher haut | nature inconnue | — | **NON CHARGÉ** |
| `ZN1`/`ZN2` | Zones non relevées | — | — | **AUCUN CALCUL** — `D-19` |

**Épuisement.** `D1` (aucune section bois — `C-07`) · `D2` f. 02 (2 demi-fermes, 3 pannes, contrefiches, 2 zones non cotées) · `D3` p. 7–9 et 14–15 (désordres 5, 6, 8) · `D4` p. 26–27 (`NIV-02c`) · `B-20` planche 3 · `B-21` `H-29` · `B-23` `P-2`/`P-3` · `B-24` `E-04` à `E-07` · `B-25` `q_p = 500 Pa` · `B-43` `R-43-1`. **Aucun pieu. Aucune prédalle.**

---

## 3. HYPOTHÈSES DE CALCUL

| Grandeur | Valeur | Source | Qualité |
|---|---|---|---|
| `G` toiture | `0,95 kN/m²` | `H-29` / `B-21` | Hypothèse notifiée (`CHG-04` absent) |
| Neige `s_k` | `0,45 kN/m²` | `CHG-05`, zone A1 | **Contractuelle** — `μ₁` **non réduit** |
| Cat. H | `0,40 kN/m²` | `B-21` | Non combinée à la neige |
| `q_p (6 m)` | `0,50 kN/m²` | `B-25` | Déjà calculé |
| `α` | `28°` | `NIV-02c` min : `atan((209,19 − 206,57) / 4,90)` | Contractuelle |
| `L` panne / DF | `3,20 m` | File A `X = 85,55` → File C `X = 88,75` (`B-20`) et `B-24 E-06` | Coté |
| Entraxe pannes | `1,60 m` | Demi File A–C — parti de calcul | Parti `B-44` |
| Bois neuf | **`C24`** | NF EN 338 | **Spécification** |
| Classe de service | **2** | Toiture, désordre 6 | **`MAT-08` produit** |
| `k_mod` / `k_def` / `k_cr` / `γ_M` | `0,80` / `0,80` / `0,67` / `1,30` | EC5 T3.1, T3.2, §6.1.7(2), NA | Norme |

`p_ELU = 1,35 × 0,95 + 1,5 × 0,45 =` **`1,958 kN/m²`**.

Soulèvement : `1,5 × 0,50 × 0,70 − 1,0 × 0,95 =` **`−0,425 kN/m²`** — **pas de soulèvement net** (`G` gouverne). Ancrages de rive → `B-50`.

**`D-26` : EC8 non applicable (zone 1).**

---

## 4. PANNES NEUVES `PN1/PN2/PN3`

**Méthode.** Appuis simples, `L = 3,20 m`, `e = 1,60 m`. Semelle comprimée **non maintenue** (chevrons existants altérés, désordre 8) : `k_crit` calculé, pas supposé égal à 1.

> `M_Ed = p L² / 8` · `σ_m,d = M_Ed / W ≤ k_crit · f_m,d` (EC5 §6.1.6 + §6.3.3)
> `τ_d = 1,5 V_Ed / (k_cr b h) ≤ f_v,d` (EC5 §6.1.7)
> `w_fin = w_G (1 + k_def) + w_Q (1 + ψ₂ k_def)` ≤ `L/300` (EC5 T7.2)

Premier `C24` du catalogue qui passe **toutes** les vérifications : **`75 × 200`**.

| Vérification | Sollicitation | Résistance | Taux |
|---|---|---|---|
| Flexion + déversement | `M_Ed = 4,09 kN·m` · `k_crit = 1,00` (`λ_rel,m = 0,69`) | `f_m,d = 14,77 MPa` | **`0,554`** |
| Cisaillement | `V_Ed = 5,11 kN` | `k_cr = 0,67` | **`0,310`** |
| Compression 90° (appui `100 mm`) | `k_c,90 = 1,5` | `f_c,90,d` | **`0,295`** |
| Flèche finale | `w_fin = 8,86 mm` | `L/300 = 10,67 mm` | **`0,830`** |

**Gouverne : la flèche.** `k_crit = 1,00` : à `L = 3,20 m` et `b/h = 75/200`, le déversement ne réduit pas. Il a tout de même été **vérifié sans maintien**.

---

## 5. DEMI-FERMES `DF1` / `DF2`

`L_horiz = 3,20 m` · `α = 28°` · `L_arb = 3,62 m` · `h = 1,70 m`. Surface tributaire `15,22 m²`. `W_ELU = 29,79 kN`.

Treillis triangle isostatique (charge de faîtage conservatrice `W L / 4`) :

| Effort | Formule | Valeur |
|---|---|---|
| Traction entrait | `(W L / 4) / h` | **`14,00 kN`** |
| Compression arbalétrier | `(W / 2) / sin α` | **`31,72 kN`** |
| Réaction d'appui | `W / 2` | **`14,89 kN`** |

| Pièce | Section | Vérification | Taux |
|---|---|---|---|
| Arbalétrier | **`100 × 200 C24`** | Flambement `λ_rel = 2,13` · `k_c = 0,20` + flexion PP (EC5 6.23) | **`0,626`** |
| Entrait | **`75 × 200 C24`** | Traction `σ_t,0,d / f_t,0,d` | **`0,108`** |

Les demi-fermes **ne touchent pas** `E-07`. Vide de désolidarisation entre entrait et plancher (coupe A-A de `B-20`). Les `14,89 kN` d'appui vont aux **murs** Files A et C → `B-46` / `B-50` (`PA-02` maintenu).

**Séquence `E-04`.** 1. Pose `DF1`/`DF2`. 2. Reprise des pannes. 3. Dépose des potelets. L'ordre inverse rechargerait des potelets « théoriquement instables » (`B-23 P-3`) : il est interdit.

---

## 6. CONTREFICHES SUR FERME TRADI

`L_ef = 2,62 m` (hauteur de versant `NIV-02c` min, conservateur). `N_Ed = 44,03 kN` (File C–E `6,60 m`, `W / sin α`).

> `N_Ed / (k_c A f_c,0,d) ≤ 1` (EC5 §6.3.2) — **pas de flexion** (bielles).

Premier `C24` qui passe : **`75 × 225`**. `λ_rel = 2,05` · `k_c = 0,215` · taux **`0,940`**.

**Gouverne : le flambement.** Taux serré, section minimale du catalogue qui passe. Pas de « repli » : c'est le premier qui satisfait la formule.

**Séquence `E-05` (`B-23 P-2`).** 1. Purge du bois mort. 2. Traitement. 3. Pose des contrefiches. L'ordre inverse pose du neuf sur du bois sans résistance : il est interdit. La ferme existante **n'est pas calculée** (section résiduelle inconnue, `B-24`).

---

## 7. CE QUI RESTE HORS CALCUL

| Élément | Pourquoi | Devenir |
|---|---|---|
| `E-04` potelets | **Supprimés** par les demi-fermes | Plus rien à vérifier en place |
| `E-05` ferme | Section et résiduel inconnus | `B-24` + purge + `CF` |
| `E-06` pannes existantes | Section inconnue | `B-24` — les 3 neuves s'**ajoutent**, elles ne les remplacent pas par décret |
| `E-07` plancher haut | Nature inconnue **et** non chargé par les neufs | `PA-03` reste à `B-43` |
| `ZN1` / `ZN2` | Emprises non cotées (`B-23`) | Relevé avant taille — **déjà prescrit** (`B-20` point 6, `D-19`) |

`PA-03` **ne bloque pas** `B-44` : le chemin de descente des neufs va aux murs, pas à `E-07`. Il conditionne toujours le **plancher existant** (`B-43`). Si la charpente sortait du programme, `PA-03` tombait avec elle ; le GO de `B-44` la **maintient** dans le programme (`H-14`).

Aucune valeur de sensibilité de `B-24` n'est retenue.

---

## 8. EFFORTS TRANSMIS À `B-50`

| Nœud | `N_Ed` | `V_Ed` | `M_Ed` | Nature |
|---|---|---|---|---|
| Panne / sablière ou DF | `0` | `5,11 kN` | `0` | Sabot ou entaille |
| Entrait / mur File A ou C | `14,00 kN` | `14,89 kN` | `0` | Sabot + ancrage |
| Arbalétrier / poinçon | `31,72 kN` | `0` | `0` | Boulonné / entaillé |
| Contrefiche / `E-05` (×2) | `44,03 kN` | `0` | `0` | Boulonné — **après purge** |

Aucun Johansen. Aucun sabot chiffré. `PA-02` (liaison charpente-maçonnerie) **maintenu**.

---

## 9. DISPOSITIONS CONSTRUCTIVES

- **Contreventement de toiture : absent au `D2`** (`B-25`). Les pannes neuves **ne font pas** diaphragme. Croix de Saint-André / entretoises → `B-60`.
- **Ventilation de sous-face** : lame d'air + chatières — prescription, pas un calcul.
- **Classe de service 2** — toiture, humidité. Pas de classe 1.
- **Termites** : `D1 § 01.2.1.9.2` déjà prescrit (ne pas rouvrir).
- **Protection au feu** : adéquate à prévoir (hors lot GO) — **non dimensionnée**.

---

## 10. AUTO-CONTRÔLE DÉCLARÉ

| Réf. | Élément | Section | Taux | Verdict |
|---|---|---|---|---|
| `PN1/2/3` | Pannes neuves | `75 × 200 C24` | **`0,830`** | **OK** — flèche |
| `DF-arb` | Arbalétrier | `100 × 200 C24` | **`0,626`** | **OK** — flambement |
| `DF-ent` | Entrait | `75 × 200 C24` | **`0,108`** | **OK** — traction |
| `CF` | Contrefiches | `75 × 225 C24` | **`0,940`** | **OK** — flambement |
| `E-04`…`ZN2` | Existant / zones | — | — | **Hors calcul** — déclaré |

Script : `_scripts/b44_charpente.py`. Journal : `_rendus/b44_charpente.txt` (`12 317 o`). Planche : `_plans/FLORA_B44_CHARPENTE_IndA.{dxf,pdf,png}` — DXF `70 537 o`, audit **0 erreur**.

**`R-28` CLOSE** (`MAT-08` = classe de service 2). `R-20` / `R-21` / `R-22` **maintenues** (existant, classement, CCTP). `PA-03` **maintenu** (c'est `B-43`).
