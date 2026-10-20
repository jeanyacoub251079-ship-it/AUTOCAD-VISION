# B-25 — STABILITÉ GLOBALE, CONTREVENTEMENT, JOINTS DE DILATATION ET SISMIQUE

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-25** — Stabilité globale, contreventement, joints de dilatation et sismique |
| Phase | **3 — Conception et synthèse structurelle** (après `B-20`, avant `B-21` et les calculs `B-40` à `B-50`) |
| **Mode d'appel** | **HYPOTHÈSE-NOTIFIÉE** — Géométrie et système porteur établis ; caractéristiques mécaniques de la maçonnerie portées par `H-25` à `H-27` |
| Régime | **OUTILLÉ (V13)** — extraction vectorielle `ezdxf` des fonds `B-32 Ind. D`, calcul intégral par script, journal d'exécution conservé |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Gabarit `CFG-02` | **M** (deux niveaux, emprise 11,1 × 17,5 m, 218 m² de plancher) |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b25_stabilite.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b25_stabilite.txt` (7 216 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b25_stabilite.json` (13 409 o) |
| Planche `B-25` | `_plans/FLORA_B25_CONTREVENTEMENT_IndC` (`.dxf` · `.pdf` · `.png`) |
| **Indice** | **C** — remplace et annule l'indice B du 20/10/2026 (décision `D-28`) |
| Date | **20/10/2026** |
| Brique suivante | **`B-22`** (note d'hypothèses), `B-21` étant livrée en indice B |

> **Ce qui change à l'indice C.** Une seule chose, et elle ne touche aucun résultat : **`D-28` est consignée.** L'absence de joint de dilatation cesse d'être une proposition soumise à arbitrage ; elle devient une **décision ferme du client du 20/10/2026**. Toutes les raideurs, tous les centres de rigidité, tous les `τ/f_vk` de cette note sont **inchangés** — un joint qui n'existe pas ne modifie aucune raideur, et c'est précisément pour cela qu'il fallait trancher avant d'y revenir un jour par inadvertance.
>
> **Ce que la décision ne change pas.** L'absence de joint reste **conditionnelle au maintien de l'emprise** : elle devient fausse dès qu'une extension est accolée sans joint ou qu'une reprise en sous-œuvre coupe le bloc. La clause figure au § 5 et n'est pas levée par `D-28`.

> **Ce qui change à l'indice B — rectificatif factuel.** L'indice A produisait une vérification sismique de sensibilité et une vérification complète de la stabilité en phase provisoire. **Ces deux productions sortent du livrable**, sur décision du client du 20/10/2026 :
> - **`D-26`** — zone de sismicité 1 (Île-de-France), séisme très faible : **aucune vérification sismique n'est produite**, ni réglementaire, ni de sensibilité.
> - **`D-27`** — dans un bâtiment existant, la vérification du contreventement en phase provisoire **incombe à la maîtrise d'œuvre structure de conception**. Elle sort de notre mission.
>
> Ce qui reste, et qui est notre travail : le **système de contreventement en service**, la **torsion**, la **régularité**, les **joints**, et la **transmission des grandeurs** utiles à la MOE pour sa propre vérification provisoire. Les sections 6 et 7 de l'indice A sont **retirées** ; elles ne sont ni résumées, ni conservées « au cas où ».

> **Périmètre de cette brique.** `B-25` **ne dimensionne aucun élément porteur**. Les sections, ferraillages et assemblages relèvent de `B-40` à `B-50`. Aucune valeur de cette note ne peut être reprise comme justification d'exécution d'un élément.

---

## 0. RÉPONSE DIRECTE — LES QUATRE VERDICTS DE LA BRIQUE

| # | Question posée par la fiche `B-25` | Verdict | Preuve |
|---|---|---|---|
| 1 | **Quel système reprend les efforts horizontaux en service ?** | **La maçonnerie porteuse existante, et elle seule** — 12 voiles au RDC, 9 au R+1, raideur d'ensemble `ΣK = 1,21 à 1,64 GN/m`. Aucun cadre neuf n'est compté | § 2 · `b25_stabilite.txt` § [1] et [2] |
| 2 | **Le cheminement est-il continu de la toiture au sol ?** | **Oui, avec deux ruptures localisées traitées** (`F2` et `F3` suppriment deux murs ; `F1a` perce un troisième). Traitement par frangement, **aucune rupture non traitée** | § 3 |
| 3 | **La torsion est-elle maîtrisée ?** | **Oui** — excentricité structurale mesurée `≤ 0,14 m` au R+1 et `≤ 0,04 m` au RDC ; avec l'excentrique accidentelle `±0,05 L`, le mur le plus chargé reste à **`τ/f_vk ≤ 0,028`** | § 4 |
| 4 | **Faut-il des joints de dilatation ?** | **Aucun joint à créer** — dilatation libre `5,2 mm` sur 17,5 m, maçonnerie stabilisée, frangements appuyés. **`D-28` consignée** | § 5 |

**Deux questions ne sont plus posées, et c'est une décision, pas un oubli :**

| Sujet | Statut | Décision |
|---|---|---|
| **Vérification sismique** | **NON PRODUITE** — zone 1, séisme très faible (Île-de-France). L'arrêté du 22/10/2010, art. 3, ne soumet aucune catégorie d'importance aux règles EC8 en zone 1 | **`D-26`** |
| **Contreventement en phase provisoire** | **NON VÉRIFIÉ PAR NOUS** — la vérification incombe à la maîtrise d'œuvre structure de conception | **`D-27`** |

**Conséquence pratique pour la suite de la chaîne :** le système est **surdimensionné en résistance** (taux de travail inférieur à 3 % sous vent) mais **non chaîné** au sens de l'EC6. La stabilité en service n'est donc pas une question de capacité : c'est une question de **continuité et de liaisonnement**. C'est ce que cette note établit et documente.

---

## 1. DONNÉES D'ENTRÉE QUALIFIÉES AVANT CALCUL

| Donnée | Valeur retenue | Source | Statut |
|---|---|---|---|
| Zone de sismicité | **1** (très faible) — Île-de-France | D2 p. 1 + localisation du projet | **Contractuelle** — **sans effet : aucune vérification (D-26)** |
| Catégorie d'importance | **II** | D2 p. 1 | **Contractuelle** — sans effet (D-26) |
| Vent — zone | **2** · `v_b = 24 m/s` | D2 p. 1 (CHG-06) | **Contractuelle** |
| Vent — catégorie de terrain | **III** · `z_0 = 0,30 m` · `z_min = 5 m` | CHG-06 | **Contractuelle** |
| `c_pe,net` · `c_s c_d` | **1,30** · **1,00** | EC1-1-4 § 7.2 · bâtiment < 15 m | Méthode |
| Hauteurs libres | RDC **3,00 m** · R+1 **3,00 m** · faîtage **6,30 m** | D2 (P2 `H = 3,00 m`) + D5 | Contractuelle |
| Maçonnerie — `f_k` | **1,5 MPa** | H-25 (moellons + mortier bâtard) | **Hypothèse notifiée** |
| Maçonnerie — `E` | **1 500 MPa** (`E = 1 000 f_k`, EC6 § 3.7.2) | H-25 | **Hypothèse notifiée** |
| Maçonnerie — `f_vk0` | **0,15 MPa** | H-26 | **Hypothèse notifiée** |
| Contrainte verticale `σ_d` | **0,30 MPa** | H-27 | **Hypothèse notifiée** |
| Surfaces de plancher | RDC **111,15 m²** · R+1 **106,92 m²** | D-22 | Décision client |

**Preuve d'épuisement du corpus (V14).** Les pièces `D1` à `D5`, `B-02 Ind. G`, `B-03 Ind. Q`, `B-20 Ind. B`, `B-32 Ind. D` et `B-40 Ind. E` ont été relues pour cette brique. Les seules grandeurs non fournies par le marché sont les caractéristiques mécaniques de la maçonnerie ancienne : elles n'existent dans aucune pièce et relèvent de l'hypothèse notifiée, pas d'un oubli de lecture.

---

## 2. PIÈCE 1 — SYSTÈME DE CONTREVENTEMENT

### 2.1 Nature et implantation

Le pavillon Flora est un bâtiment **en maçonnerie porteuse** (moellons et pierre) de deux niveaux, avec planchers bois et métalliques et charpente bois. Il ne comporte **aucun voile béton, aucun noyau, aucune palée triangulée**. Le système de reprise des efforts horizontaux en service est donc **la maçonnerie existante elle-même**, travaillant en voiles console encastrés en pied.

La géométrie a été extraite **des fonds nettoyés `B-32 Ind. D`** (blocs géomètre `D5`), sans redessin : 18 polygones surfaciques au RDC et 10 au R+1, dont sont retenus **12 voiles au RDC** et **9 au R+1** après écartement des liserés non surfaciques (aire < 0,15 m², arêtes du relevé sans épaisseur).

| Élément | Compté | Justification |
|---|---|---|
| **Murs porteurs en maçonnerie** (12 RDC · 9 R+1) | **OUI — système unique** | Continus du sol à la toiture, surfaciques, liaisonnés aux angles ; aire cumulée 18,79 m² (RDC) et 24,10 m² (R+1) |
| **Façades en moellons** (hors bloc géomètre) | **NON — en réserve** | Épaisseur et continuité non relevées dans `D5` ; jamais comptées comme appui nécessaire. Qualifiées par `PA-01` |
| **Frangements neufs** `F1a/b/c`, `F2`, `F3`, `F4` | **NON** | Appuis simples, aucune continuité d'encastrement, aucune triangulation : ils reprennent le **vertical**, jamais l'horizontal |
| **Renforts** `R1`, `R2-N/S`, `R3-N/S`, `Stab1` | **NON** | Renforts de flexion locale ; `Stab1` est un anti-déversement, pas une triangulation |
| **Poteaux** `P1-N`, `P1-S`, `P2`, `P3`, `J1` | **NON** | Compression seule ; `P2` est élancé (`H/b = 20`) |
| **Charpente bois et couverture** | **NON** | Toiture non diaphragme : aucun contreventement de toiture dans `D2` |
| **Planchers** (bois 8×18, voutains + IPE 160) | **NON — diaphragme réputé flexible** | Assemblage sans dispositif de reprise d'effort horizontal ; hypothèse défavorable retenue (§ 2.2) |
| **Cloisons, doublages, isolants** | **NON — exclus par `V9`** | Aucun remplissage n'est compté comme contreventement |

### 2.2 Hypothèse de répartition — diaphragme flexible

Les planchers n'étant pas justifiés comme diaphragmes rigides, la répartition est faite **par raideur de mur, niveau par niveau, sans redistribution par plancher** : c'est l'hypothèse **défavorable** (elle sollicite les murs les plus raides et crée la plus grande torsion).

La raideur horizontale de chaque voile est calculée en **console encastrée en pied**, par superposition flexion + cisaillement :

$$K_i=\left[\frac{h^{3}}{3EI_{i}}+\frac{1{,}2\,h}{GA_{i}}\right]^{-1}$$

avec `E = 1 500 MPa`, `G = E / 2,4 = 625 MPa`, `I_i` = inertie du polygone réel (formules de Green sur le contour), `A_i` = aire du polygone, `h = 3,00 m`.

> **Pourquoi le cisaillement domine.** Pour un voile de 5 m de long et 0,50 m d'épaisseur, le terme de flexion vaut `8,6 × 10⁻⁷ m/kN` et le terme de cisaillement `1,5 × 10⁻⁶ m/kN` : la déformation de cisaillement représente près des deux tiers de la déformation totale. Ignorer le cisaillement — erreur classique sur les voiles courts — aurait surestimé les raideurs relatives d'un facteur 2 à 3 et faussé le centre de rigidité.

### 2.3 Caractéristiques des voiles retenus

**RDC — 12 voiles · `ΣK_x = 1 205 006 kN/m` · `ΣK_y = 1 641 231 kN/m`**

| Voile | Aire (m²) | Long. (m) | `t_eq = A/L` (m) | Dir. (°) | Centre B-30 (m) | `K_x` (kN/m) | `K_y` (kN/m) |
|---|---|---|---|---|---|---|---|
| M01 | 0,49 | 1,57 | 0,31 | 93 | (+0,69 ; +2,80) | 662 | 13 521 |
| M02 | 0,80 | 2,04 | 0,39 | 143 | (+0,12 ; +5,20) | 21 180 | 20 005 |
| **M03** | **4,58** | **5,19** | **0,88** | 67 | (+5,01 ; +7,21) | **525 216** | **439 310** |
| M04 | 1,76 | 3,06 | 0,57 | 82 | (+9,78 ; +7,57) | 17 609 | 100 161 |
| M05 | 0,16 | 1,08 | 0,15 | 81 | (−0,22 ; +7,99) | 144 | 1 518 |
| M06 | 0,42 | 1,76 | 0,24 | 83 | (−0,28 ; +8,74) | 771 | 9 426 |
| M07 | 0,17 | 0,81 | 0,21 | 126 | (+3,80 ; +10,48) | 438 | 604 |
| M08 | 0,62 | 1,71 | 0,36 | 87 | (−0,23 ; +11,08) | 1 139 | 19 627 |
| M09 | 2,79 | 3,28 | 0,85 | 82 | (+9,50 ; +11,34) | 113 878 | 192 477 |
| M10 | 0,79 | 1,65 | 0,48 | 20 | (+0,07 ; +14,21) | 16 859 | 12 758 |
| **M11** | **5,49** | **9,07** | **0,60** | 64 | (+4,27 ; +15,49) | **503 490** | **815 171** |
| M12 | 0,60 | 1,65 | 0,37 | 104 | (+9,44 ; +18,26) | 3 620 | 16 653 |

**R+1 — 9 voiles · `ΣK_x = 2 060 350 kN/m` · `ΣK_y = 2 818 175 kN/m`**

| Voile | Aire (m²) | Long. (m) | `t_eq` (m) | Dir. (°) | Centre B-30 (m) | `K_x` (kN/m) | `K_y` (kN/m) |
|---|---|---|---|---|---|---|---|
| M01 | 2,30 | 3,62 | 0,64 | 142 | (+4,41 ; +0,82) | 147 636 | 146 780 |
| M02 | 3,35 | 7,41 | 0,45 | 77 | (+9,21 ; +3,33) | 142 065 | 480 133 |
| **M03** | **5,50** | **7,88** | **0,70** | 52 | (+3,02 ; +6,70) | **631 744** | **773 316** |
| M04 | 0,89 | 4,92 | 0,18 | 0 | (+7,78 ; +7,85) | 103 419 | 441 |
| M05 | 0,58 | 1,54 | 0,37 | 89 | (−0,30 ; +8,35) | 1 169 | 15 847 |
| M06 | 0,89 | 5,04 | 0,18 | 0 | (+7,95 ; +10,37) | 107 825 | 908 |
| M07 | 0,60 | 1,54 | 0,39 | 92 | (−0,29 ; +11,15) | 1 311 | 16 272 |
| **M08** | **6,37** | **8,75** | **0,73** | 46 | (+3,32 ; +15,62) | **789 200** | **871 781** |
| M09 | 3,47 | 7,35 | 0,47 | 101 | (+9,27 ; +15,78) | 135 980 | 512 697 |

> **Lecture.** Quatre voiles portent la quasi-totalité de la raideur : **95,1 %** au RDC (`M11`, `M03`, `M09`, `M04`) et **88,9 %** au R+1 (`M08`, `M03`, `M09`, `M02`). C'est une structure **à noyaux de maçonnerie concentrés**, pas une structure cellulaire régulière.
>
> L'épaisseur `t_eq = A/L` est une **épaisseur équivalente** : les voiles `M03`, `M11` (RDC) et `M03`, `M08` (R+1) sont des voiles **coudés** (retours d'angle intégrés au polygone). Les voiles droits mesurent 0,31 à 0,57 m.

### 2.4 Ce que le système ne garantit pas — et qu'il faut écrire

1. **Aucune ductilité.** Une maçonnerie de moellons est fragile : elle reprend l'effort tant qu'elle reste élastique, puis rompt sans préavis. Le taux de travail de 3 % ne rend pas la structure ductile — il rend seulement la rupture improbable sous l'action de calcul.
2. **Aucun chaînage.** Les murs ne sont pas chaînés au sens de l'EC6 § 8. Nos calculs supposent la continuité ; elle n'est **pas prouvée**. C'est l'objet de `PA-01`.
3. **Aucune liaison plancher-mur en cisaillement.** Rien dans `D3` ne décrit un ancrage des solives ou des voutains. L'hypothèse de diaphragme flexible est donc à la fois défavorable pour la répartition et **réaliste**.

---

## 3. PIÈCE 2 — CHEMINEMENT DES EFFORTS HORIZONTAUX

### 3.1 Tableau par niveau

| Niveau | Origine de l'effort | Valeur de calcul | Éléments de reprise identifiés | Transmission au niveau inférieur | Rupture |
|---|---|---|---|---|---|
| **Toiture** (z = 6,30 m) | Vent sur versants et pignons — `q_p(6,00) = 500 Pa` | Report aux pignons et aux fermes | **Pignons Nord et Sud en moellons** + fermes traditionnelles | Par les pignons et murs d'aplomb jusqu'au plancher haut R+1 | **NON** |
| **R+1** (3,00 → 6,00 m) | `V_x = 31,9 kN` · `V_y = 20,2 kN` | Par voile : `M08` reprend 14,6 kN sous vent X (avec torsion) | **9 voiles R+1** · `ΣK_x = 2,06 GN/m` · `ΣK_y = 2,82 GN/m` | Par les voiles R+1 aux voiles RDC — **appui direct mur sur mur** aux files A, D et E | **NON** — alignement vérifié (`B-31` : écart d'emprises `0,10 m`) |
| **RDC** (0 → 3,00 m) | `V_x = 31,4 kN` · `V_y = 19,9 kN` | Par voile : `M11` reprend 16,4 kN sous vent X (avec torsion) | **12 voiles RDC** · `ΣK_x = 1,21 GN/m` · `ΣK_y = 1,64 GN/m` | Aux **fondations existantes** par semelles filantes et soubassements en moellons ; à `SF1` (sous `P2`) et aux sommiers `S1/S2` pour les charges verticales des frangements | **OUI — deux ruptures**, § 3.2 |
| **Fondations** | Effort tranchant global `V_x = 63,2 kN` · `V_y = 40,0 kN` | — | Semelles existantes en moellons et béton de chaux ; `SF1` `60×60×30` sous `P2` ; arase `−1,00 m / TN MINIMUM` (`D-08`/`D-12`) | Sol : alluvions anciennes, `q_ELS ≤ 0,30 MPa` | — (relève de `B-40`) |

### 3.2 Les deux ruptures de cheminement et leur traitement

| Rupture | Nature | Effet mécanique | Traitement retenu |
|---|---|---|---|
| **R-1 · `F2` (HEB 200, `L = 2,85 m`) et `F3` (HEB 160, `L = 3,85 m`)** | Suppression de deux murs porteurs de l'aile Est. La fonction **verticale** est reprise par les poutres ; la fonction **horizontale** du panneau supprimé est **définitivement perdue** | Les murs restants reprennent l'effort et le centre de rigidité se déplace | **Aucun transfert horizontal n'est reconstitué** (ce serait un portique non conçu pour cela). Le système en service est calculé **sans les murs supprimés** ; la vérification de la situation provisoire relève de la MOE (`D-27`) |
| **R-2 · `F1a` (2×HEA 200, `L = 1,00 m`) percé dans le refend central de 50 cm** | Ouverture dans un voile. Le linteau reprend le vertical ; **la maçonnerie au-dessus ne reprend aucun cisaillement** | Le voile est scindé en deux trumeaux ; la raideur du panneau diminue | Le voile est déjà décompté **en trumeaux séparés** par le relevé (les ouvertures existantes sont des vides dans les polygones). L'ouverture retire **0,50 m²** d'un voile de 4,58 m², soit `11 %` de ce voile et `2,7 %` de la raideur totale du RDC |

**Aucune autre discontinuité n'a été trouvée.** Le contrôle porte sur les 21 voiles des deux niveaux et sur les 4 files d'appui (`A`, `D`, `E`, `4`) : chaque niveau dispose d'une reprise identifiée jusqu'aux fondations. `V15` est satisfait : **aucun effort ne s'arrête en chemin dans l'état en service**.

### 3.3 Le cas des frangements — pourquoi ils ne contreventent pas

1. **Les assemblages sont des appuis simples.** `F4` s'appuie sur `F2` et sur un sommier `S1` ; `F2` s'appuie sur deux `S1`. Aucun nœud n'est encastré : la structure est isostatique, donc **cinématiquement libre** sous effort horizontal.
2. **Aucune triangulation.** Aucun profilé n'est disposé en diagonale. Un portique non triangulé et non encastré ne reprend pas d'effort horizontal.
3. **Les sommiers `S1`/`S2` sont des appareils de répartition**, pas des fondations de portique : ils reprennent une compression verticale. Les solliciter en moment d'encastrement serait une erreur de conception.

**Conclusion :** compter les frangements en contreventement aurait été une faute de conception, et déclarer la structure « contreventée par portiques » un abus de langage opposable. Le système est **la maçonnerie, rien que la maçonnerie**.

---

## 4. PIÈCE 3 — TORSION ET RÉGULARITÉ

### 4.1 Centres de masse et de rigidité

Le **centre de masse** `G` est pris au barycentre surfacique de l'enveloppe du niveau, les charges permanentes et d'exploitation étant uniformément réparties. L'aire de l'enveloppe calculée (`108,4 m²` au RDC, `114,0 m²` au R+1) est comparée aux surfaces utiles de `D-22` (`111,15` et `106,92 m²`) : l'écart de `±4 %` borne l'incertitude du barycentre à **`± 0,15 m`**, très inférieure aux excentricités accidentelles appliquées.

| Niveau | `G` (m) | `CR` vent X (Y) | `CR` vent Y (X) | `e` struct. X | `e` struct. Y | `K_T,x` (kN·m²/rad) | `K_T,y` (kN·m²/rad) |
|---|---|---|---|---|---|---|---|
| **R+1** | (+5,46 ; +10,17) | **+10,32** | **+5,34** | **−0,14 m** | **+0,11 m** | 55 406 367 | 23 959 356 |
| **RDC** | (+5,24 ; +11,13) | **+11,17** | **+5,27** | **−0,04 m** | **−0,03 m** | 18 980 307 | 8 715 280 |

**Lecture.** Les centres de masse et de rigidité sont quasiment confondus : `4 cm` d'écart au RDC, `14 cm` au R+1. C'est la signature d'une maçonnerie cellulaire dont les murs sont répartis sur le pourtour et sur les refends. La structure est **intrinsèquement peu sensible à la torsion**.

### 4.2 Torsion de calcul

L'excentrique accidentelle réglementaire est appliquée : `e_a = ± 0,05 L`, soit `±0,87 m` pour un vent selon X et `±0,55 m` pour un vent selon Y — **six à vingt fois l'excentricité structurale mesurée**. Le moment de torsion vaut `M_t = V (e_struct + e_a)`.

### 4.3 Vérification sous vent — EC1-1-4 et EC6 § 3.6.2

`q_b = 0,5 × 1,25 × 24² = 360 Pa` · `c_e(3 m) = 1,28` · `c_e(6 m) = 1,39` · `q_p = 461 / 500 Pa`.
Largeurs chargées : `17,5 m` (façades Nord/Sud) et `11,1 m` (façades Est/Ouest).
`f_vk = (f_vk0 + 0,4 σ_d)/γ_M = (150 + 0,4 × 300)/2,5 = 108 kPa`.

| Cas | `V` (kN) | `e_struct` (m) | `e_a` (m) | `M_t` (kN·m) | Mur le plus chargé | `V_i` (kN) | `τ` (kPa) | **`τ/f_vk`** |
|---|---|---|---|---|---|---|---|---|
| R+1 — vent X | 31,9 | 0,14 | ±0,87 | 32,4 | M08 | 14,6 | 2,3 | **0,021** |
| R+1 — vent Y | 20,2 | 0,11 | ±0,55 | 13,4 | M08 | 5,3 | 0,8 | **0,008** |
| RDC — vent X | 31,4 | 0,04 | ±0,87 | 28,6 | M11 | 16,4 | 3,0 | **0,028** |
| RDC — vent Y | 19,9 | 0,03 | ±0,55 | 11,6 | M11 | 8,8 | 1,6 | **0,015** |

**Verdict : la capacité au cisaillement est utilisée à moins de 3 %.** Ce n'est pas un résultat confortable, c'est un résultat **inquiétant à sa manière** : la marge est telle que **le vrai risque n'est pas la rupture sous vent, mais l'absence de liaisonnement et la fragilité en phase transitoire** — et cette phase relève de la MOE (`D-27`).

### 4.4 Stabilité hors plan

Élancement maximal `h/t_eq` : **17,0** au R+1 (voile `M06`, `t_eq = 0,18 m`) et **20,0** au RDC (voile `M05`, `t_eq = 0,15 m`) — la limite de l'EC6 § 5.5.1.2 pour un mur non chargé latéralement de façon continue est de **20**. Le RDC est **exactement à la limite**, sur un trumeau de 0,16 m².

> **Conséquence :** le voile `M05` ne doit **jamais** être sollicité comme appui de contreventement principal. Il est conservé dans le modèle parce qu'il existe, mais **exclu des prescriptions de reprise**, et fait l'objet du point d'arrêt `PA-01`.

### 4.5 Régularité — verdict et méthode d'analyse

| Critère EC8 § 4.2.3 | Constat géométrique | Verdict |
|---|---|---|
| **Régularité en plan** | Emprise `11,1 × 17,5 m` en **L**, réentrant marqué à l'aile Est, ailes dissymétriques, façade Sud biaise | **IRRÉGULIER** |
| **Régularité en élévation** | Deux niveaux de hauteur identique, aucun décrochement de masse, files alignées (`B-31` : `0,10 m`) | **RÉGULIER** |
| **Diaphragme** | Planchers bois/voutains non justifiés en diaphragme | **Flexible — répartition par raideur** |
| **Méthode d'analyse** | Statique linéaire par niveau, répartition en raideur, **excentrique accidentelle `±0,05 L` dans les deux directions** | **Cohérente avec l'irrégularité** |

> **Note de méthode.** La régularité est statuée ici au sens de l'EC8 **comme critère de forme** — c'est-à-dire comme justification du choix de la méthode de répartition et de l'application de l'excentrique accidentelle. Ce n'est **pas** une vérification sismique : celle-ci n'est pas produite (`D-26`).

**Le point important :** une structure irrégulière en plan est celle où l'on applique l'excentrique accidentelle **sans discussion**. C'est fait. Le réentrant de l'aile Est est en outre le lieu où le diagnostic `D3` situe trois désordres (linteaux, plancher, fissuration de plafond) — conséquence mécanique d'un point singulier de la géométrie, traité par les renforts `R1`, `R2`, `R3` de `B-20`.

---

## 5. PIÈCE 4 — JOINTS DE DILATATION

| Bloc `JD` | Position | Largeur | Motif du découpage | Report plan | Report coupe |
|---|---|---|---|---|---|
| **Aucun** | — | — | Aucun joint créé — **`D-28` consignée le 20/10/2026** | Sans objet | Sans objet |

**Justification chiffrée — les cinq motifs de la fiche testés un par un :**

| Motif possible de joint | Vérification | Conclusion |
|---|---|---|
| **Longueur** | Dimension maximale du bloc : **`17,5 m`**, très inférieure aux `25 à 40 m` au-delà desquels la maçonnerie non ferraillée exige classiquement un joint | Pas de joint de longueur |
| **Température** | `ΔL = α·ΔT·L = 10⁻⁵ × 30 × 17,5 = 5,2 mm` — déplacement libre absorbé par la maçonnerie et les appuis coulissants de charpente | Pas de joint de température |
| **Retrait** | Maçonnerie ancienne de plus d'un siècle : le retrait du mortier est **épuisé**. Aucun désordre de retrait dans `D3` | Pas de joint de retrait |
| **Tassements différentiels** | **Hors mission** (`D-15`). Aucune ligne de tassement différencié dans `D3`. Un joint créé pour un tassement non mesuré serait un joint sans justification | Pas de joint de tassement — réserve `R-36` maintenue (`B-40`) |
| **Phasage** | Les frangements neufs sont **appuyés** (`0,85 à 4,88 m`), sans continuité mécanique longue | Pas de joint de phasage |

> **Ce que cette absence engage.** Un bâtiment sans joint travaille en continu sur 17,5 m. C'est acceptable **ici** parce que le bâti l'a fait pendant plus d'un siècle sans désordre de dilatation, et qu'aucun élément neuf n'impose de mouvement relatif. Cela deviendrait faux si une reprise en sous-œuvre coupait le bloc en deux ou si une extension était accolée sans joint. **La décision est conditionnelle et doit être réexaminée à toute modification d'emprise.**

---

## 6. EXCLUSION DE MISSION — STABILITÉ EN PHASE PROVISOIRE (`D-27`)

### 6.1 La règle appliquée

**Dans un bâtiment existant, la vérification du contreventement en phase provisoire incombe à la maîtrise d'œuvre structure de conception.** Cette vérification **n'est pas produite** par nos soins, et l'indice A qui la produisait est **retiré** : il revendiquait une responsabilité qui n'est pas la nôtre.

| Ce qui relève de la MOE structure de conception | Ce qui reste de notre lot |
|---|---|
| Le **système de contreventement pendant les travaux** : quels voiles reprennent les efforts quand un mur est démoli, quelle raideur subsiste, quel déplacement du centre de rigidité est admissible | **L'étaiement d'exécution** sous les poutres et linteaux posés (`H-20`) : calcul, implantation, dépose |
| La **justification écrite** de la stabilité provisoire, y compris sous vent de chantier | Le **mode opératoire de pose** de chaque frangement : ordre, clavetage, décinrement |
| La **validation du phasage** de démolition au regard de la stabilité d'ensemble | La **demande formelle** des pièces et validations manquantes (`T-04`) |
| Le **dimensionnement** des dispositifs de stabilité provisoire d'ensemble | La **sécurité immédiate** de nos propres ouvrages en cours d'exécution |

> **La frontière est nette et elle est écrite pour être opposable dans les deux sens.** Nous ne produisons pas une note de stabilité provisoire : nous ne l'avons pas en mission, et une note produite hors mission est une note qui nous engage sans nous être commandée. En sens inverse, la MOE ne peut pas nous reprocher de ne pas avoir vérifié ce qu'elle devait vérifier — à condition que la demande ait été formée et tracée.

### 6.2 Ce que nous transmettons à la MOE

Nous ne produisons pas la vérification, mais nous **fournissons les grandeurs** sans lesquelles elle ne peut pas être faite. C'est un livrable de notre lot : la donnée d'entrée de la MOE.

| Grandeur transmise | R+1 | RDC |
|---|---|---|
| Raideur d'ensemble | `ΣK_x = 2 060 350 kN/m` · `ΣK_y = 2 818 175 kN/m` | `ΣK_x = 1 205 006 kN/m` · `ΣK_y = 1 641 231 kN/m` |
| Centre de rigidité `CR` | `(+5,34 ; +10,32)` m | `(+5,27 ; +11,17)` m |
| Raideur torsionnelle | `K_T,x = 55 406 367` · `K_T,y = 23 959 356 kN·m²/rad` | `K_T,x = 18 980 307` · `K_T,y = 8 715 280 kN·m²/rad` |
| Voiles majeurs (part de raideur) | **M08, M03, M09, M02 — 88,9 %** | **M11, M03, M09, M04 — 95,1 %** |
| Voiles directement concernés par une démolition | `M03`, `M08` (aile Est / refend) | `M11`, `M03` (refend central, frangement `F1a`) |
| Mur de raideur marginal à écarter | `M06` (`K_y = 908 kN/m`) | `M05` (`K_y = 1 518 kN/m`, `h/t = 20`) |
| Excentrique accidentelle de référence | `±0,05 L` soit `±0,87 m` (X) et `±0,55 m` (Y) | idem |

**Contenu de la demande `T-04` à adresser à la MOE :** la note de stabilité provisoire couvrant (1) la démolition de `F2` et `F3`, (2) l'ouverture `F1a` dans le refend central, (3) les phases de dépose et repose de charpente, (4) le vent de chantier sur les murs non liaisonnés en tête — avec les grandeurs ci-dessus en données d'entrée.

### 6.3 Ce que nous maintenons de notre propre initiative — et pourquoi ce n'est pas une vérification

Trois prescriptions restent dans notre livrable, mais **aucune ne porte sur la stabilité d'ensemble** :

| Prescription | Nature | Pourquoi elle reste de notre lot |
|---|---|---|
| **Étaiement préalable avant toute découpe**, clavetage du frangement avant décinrement | **Mode opératoire** (`H-20`) | C'est la sécurité de notre propre geste d'exécution : un linteau posé sans étaiement n'est pas un calcul, c'est une faute de chantier |
| **Ordre `F3` avant `F2`** | **Constructibilité** | `F3` s'appuie en tête sur les `S1` ; démolir `F2` d'abord priverait `F3` de son appui transversal. C'est un constat d'assemblage, pas une vérification de stabilité |
| **Étaiement latéral des pignons avant dépose de couverture** | **Sécurité des personnes** | Un pignon en console de 3,00 m avec `h/t = 20` est instable sous la moindre poussée parasite. La prescription est une mesure de sécurité, pas une justification de calcul |

> **Ce que nous ne disons plus.** L'indice A affirmait, calcul à l'appui, que « jamais deux voiles majeurs ne doivent être ouverts simultanément ». Cette prescription reste **utile et physiquement fondée** — les voiles majeurs portent 95 % de la raideur — mais elle n'est plus **opposable de notre fait** : elle relève de la note de stabilité provisoire de la MOE. Nous la formulons désormais comme une **recommandation transmise**, sans en faire un critère de notre brique.

---

## 7. PIÈCE 5 — SCHÉMA DE CONTREVENTEMENT REPORTÉ SUR LE FOND `B-32`

La planche **`FLORA_B25_CONTREVENTEMENT_IndC`** (`.dxf` · `.pdf` · `.png`, A3 paysage, `1/80`) reporte sur le fond structurel pur `B-32 Ind. D` :

- les **12 voiles RDC comptés**, repérés `M01` à `M12`, avec leur raideur `K_x`/`K_y` et leur aire ;
- les **quatre voiles majeurs** (`M11`, `M03`, `M09`, `M04` — 95,1 % de la raideur) mis en évidence ;
- les **deux ruptures de cheminement** `R-1` (`F2`, `F3`) et `R-2` (`F1a`), avec leur traitement ;
- le **centre de rigidité `CR`** et le **centre de masse `G`**, la distance `e` entre eux et le moment de torsion appliqué ;
- les **flèches de vent** `V_x = 63,2 kN` et `V_y = 40,0 kN` avec leur ligne d'action ;
- la mention **« AUCUN JOINT DE DILATATION »** et sa justification en trois lignes ;
- le **renvoi de mission `D-26` / `D-27`** : ni vérification sismique, ni vérification de la stabilité provisoire, avec les grandeurs transmises à la MOE ;
- la note **`D-09` intégrale**, le filigrane **`PRINCIPE — NE PAS EXÉCUTER — Indice P`** et le cartouche `B-25 Ind. C` ;
- la mention **`D-28` consignée le 20/10/2026** dans la pièce 4, en lieu et place de la « proposition » de l'indice B.

Les repères `M01` à `M12` sont **identiques** à ceux du journal `b25_stabilite.txt`, ce qui rend la planche vérifiable ligne à ligne contre le calcul — condition du critère de report graphique de la fiche.

---

## 8. HYPOTHÈSES, POINTS D'ARRÊT ET ARBITRAGES

### 8.1 Hypothèses notifiées actives sur cette brique

| Code | Hypothèse | Norme d'appui | Conséquence si démentie |
|---|---|---|---|
| **H-25** | `f_k = 1,5 MPa` · `E = 1 500 MPa` (`E = 1 000 f_k`) | EC6 § 3.7.2 et tableau 3.1 | Si `f_k = 1,0 MPa` : raideurs toutes divisées par 1,5 → `CR` et répartition **inchangés**, `τ/f_vk` de 0,028 à 0,045. **Conclusion inchangée** |
| **H-26** | `f_vk0 = 0,15 MPa` | EC6 § 3.6.2 | Si `f_vk0 = 0,10 MPa` : `f_vk = 80 kPa`, `τ/f_vk` de 0,028 à 0,038. **Conclusion inchangée** |
| **H-27** | `σ_d = 0,30 MPa` | EC6 § 3.6.2 (terme `0,4 σ_d`) | Si `σ_d = 0,20 MPa` : `f_vk = 92 kPa`, effet < 15 % sur les taux. **Conclusion inchangée** |

**`H-24` (classe de sol C, `a_gr = 0,40 m/s²`) est marquée SANS OBJET** par `D-26` : aucune vérification sismique n'étant produite, la classe de sol et l'accélération n'ont plus d'emploi dans le dossier. L'hypothèse n'est pas supprimée — elle est **neutralisée**, et le resterait si un reclassement de zone survenait.

### 8.2 Points d'arrêt chantier

| Code | Point d'arrêt | Quand | Qui | Conséquence si non conforme |
|---|---|---|---|---|
| **PA-01** | **Reconnaissance contradictoire de la continuité des voiles** : épaisseur réelle, présence de chaînages, liaisons d'angle, état de la maçonnerie (sondages à la pointe et au burin) sur `M11`, `M03`, `M04` (RDC), `M08`, `M03`, `M09` (R+1) et sur le trumeau `M05` | **Avant toute démolition** | Entreprise + MOE | Si un voile majeur est discontinu ou désolidarisé : arrêt de la phase et **saisine de la MOE structure de conception** (`D-27`) |
| **PA-02** | **Vérification de la liaison charpente-maçonnerie** : nature des appuis de pannes et de fermes sur les pignons, présence de sabots ou de scellements | Avant dépose de la couverture | Entreprise + MOE | Si appuis simplement posés : risque de soulèvement au vent, repose avec sabots obligatoire |

### 8.3 Décisions consignées et arbitrages encore ouverts

| Code | Objet | Statut |
|---|---|---|
| **`D-26`** | **Aucune vérification sismique** — zone 1 (Île-de-France), séisme très faible | ✅ **CONSIGNÉE** le 20/10/2026 |
| **`D-27`** | **Stabilité provisoire — MOE structure de conception** : la vérification du contreventement en phase provisoire dans un bâtiment existant lui incombe, hors de notre mission | ✅ **CONSIGNÉE** le 20/10/2026 |
| **`D-28`** | **Aucun joint de dilatation** sur le pavillon Flora | ✅ **CONSIGNÉE** le 20/10/2026 — décision ferme du client |
| **`D-29`** | **Le contreventement en service est la maçonnerie existante seule** ; aucun cadre métallique n'est réputé contreventant | ⏳ **PROPOSÉE** — en attente de votre arbitrage (§ 9, point 1) |

---

## 9. AUTO-CONTRÔLE DES CRITÈRES D'ACCEPTATION

Les sept critères de la fiche `B-25` sont repris, **avec le statut réel de chacun après `D-26` et `D-27`**.

| # | Critère de la fiche `B-25` | État | Preuve / motif |
|---|---|---|---|
| 1 | Chaque niveau dispose d'une reprise d'efforts horizontaux explicitement identifiée, jusqu'aux fondations | ✅ **CONFORME** | § 3.1 : quatre niveaux, 21 voiles, deux ruptures identifiées et traitées |
| 2 | Les centres de masse et de rigidité, les excentricités et l'effet de torsion sont calculés pour chaque niveau | ✅ **CONFORME** | § 4.1 et 4.2 : `G`, `CR`, `e_struct`, `M_t` au RDC et au R+1 |
| 3 | La régularité en plan et en élévation est statuée avec la méthode d'analyse correspondante | ✅ **CONFORME** | § 4.5 : irrégulier en plan, régulier en élévation, statique + excentrique accidentelle |
| 4 | Chaque zone sismique, catégorie d'importance et classe de sol est sourcée ou porte un repère d'hypothèse avec norme d'appui | ✅ **CONFORME (sans objet)** | Zone 1 et catégorie II sourcées (`D2`) ; **aucune vérification sismique produite — `D-26`**. Aucune grandeur sismique n'est donc engagée dans un calcul |
| 5 | Chaque joint de dilatation est justifié, coté et reporté en plan et en coupe | ✅ **CONFORME (sans objet justifié)** | § 5 : les cinq motifs sont testés et écartés un par un |
| 6 | Les phases provisoires sont étudiées | **HORS MISSION — `D-27`** | § 6 : la vérification incombe à la MOE structure de conception ; les **grandeurs d'entrée lui sont transmises** (§ 6.2) et la demande est formalisée (`T-04`). **Ce n'est pas une non-conformité : c'est un retrait de périmètre décidé par le client** |
| 7 | Aucun élément porteur n'a été dimensionné dans cette brique | ✅ **CONFORME** | Aucune section, aucun ferraillage, aucun assemblage ; `f_vk` est une **capacité existante** vérifiée, pas un dimensionnement |

**Verdict de la brique `B-25` (Indice C) : 6 critères satisfaits sur 6 applicables, 1 critère hors mission par décision (`D-27`).**

> **Sur la traçabilité de ce retrait.** Le critère 6 de la fiche n'est pas « non satisfait » : il est **retiré du périmètre par une décision écrite et datée**, ce qui est la seule manière propre de sortir d'un critère. Un critère non satisfait sans décision est une non-conformité ; un critère sorti par `D-27` est un périmètre. La distinction est consignée au RDR, pas seulement dans cette note.

---

## 10. POINT DE CONTRÔLE HUMAIN

**`D-28` est close** le 20/10/2026 : aucun joint de dilatation. La question ne sera pas reposée.

**Une seule décision reste ouverte — `D-29` :**

1. **Le contreventement en service est la maçonnerie existante seule** — aucun frangement, aucun renfort, aucun poteau compté comme élément de reprise horizontale. **Confirmez-vous ?** C'est la décision qui verrouille toutes les suivantes : compter un jour les frangements supposerait de les concevoir encastrés et triangulés, ce qui n'est pas le projet. **Tant qu'elle est ouverte, `H-27` (contrainte `σ_d`) reste une hypothèse examinée mais non arbitrée, et `B-21` en hérite au § 7.**

Et une action à votre main, qui ne dépend pas de nous : **adresser la demande `T-04` à la MOE structure de conception** pour sa note de stabilité provisoire, avec les grandeurs du § 6.2. Sans cette note, le phasage de démolition ne peut pas être ouvert sur le chantier — et ce n'est pas notre production qui y supplée.

Dans l'attente de vos observations, `PA-01` (reconnaissance des voiles) et `PA-02` (liaison charpente-maçonnerie) sont **ouverts** et conditionnent le démarrage des travaux, sans bloquer les briques documentaires suivantes.

**Brique B-25 livrée en indice C — en attente de votre GO ou de vos observations.**
