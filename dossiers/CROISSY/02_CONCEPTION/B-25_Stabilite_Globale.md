# B-25 — STABILITÉ GLOBALE, CONTREVENTEMENT, JOINTS DE DILATATION ET SISMIQUE

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-25** — Stabilité globale, contreventement, joints de dilatation et sismique |
| Phase | **3 — Conception et synthèse structurelle** (après `B-20`, avant `B-21` et les calculs `B-40` à `B-50`) |
| **Mode d'appel** | **HYPOTHÈSE-NOTIFIÉE** — Géométrie, système porteur et charges établis ; `a_gr` et classe de sol portés par `H-24` ; caractéristiques mécaniques de la maçonnerie portées par `H-25` à `H-27` |
| Régime | **OUTILLÉ (V13)** — extraction vectorielle `ezdxf` des fonds `B-32 Ind. D`, calcul intégral par script, journal d'exécution conservé |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Gabarit `CFG-02` | **M** (deux niveaux, emprise 11,1 × 17,5 m, 218 m² de plancher) |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b25_stabilite.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b25_stabilite.txt` (8 009 o) |
| Résultats machine | `dossiers/CROISSY/_rendus/b25_stabilite.json` (21 723 o) |
| Planche `B-25` | `_plans/FLORA_B25_CONTREVENTEMENT_IndA` (`.dxf` · `.pdf` · `.png`) — schéma de contreventement reporté sur le fond `B-32 Ind. D` |
| **Indice** | **A** — création de la brique |
| Date | **20/10/2026** |
| Brique suivante | **`B-21`** (DDC préliminaire), puis `B-22` (note d'hypothèses consolidée) et `B-40` à `B-50` |

> **Périmètre de cette brique.** `B-25` **ne dimensionne aucun élément porteur**. Elle établit le système qui reprend les efforts horizontaux, vérifie qu'il est continu, mesure la torsion, statue sur les joints, et organise la stabilité des phases provisoires. Les sections, ferraillages et assemblages relèvent de `B-40` à `B-50`. Aucune valeur de cette note ne peut être reprise comme justification d'exécution d'un élément.

---

## 0. RÉPONSE DIRECTE — LES SIX VERDICTS DE LA BRIQUE

| # | Question posée par la fiche `B-25` | Verdict | Preuve |
|---|---|---|---|
| 1 | **Quel système reprend les efforts horizontaux ?** | **La maçonnerie porteuse existante, et elle seule** — 12 voiles au RDC, 9 au R+1, raideur d'ensemble `ΣK = 1,21 à 1,64 GN/m`. Aucun cadre neuf n'est compté | § 2 · `b25_stabilite.txt` § [1] et [2] |
| 2 | **Le cheminement est-il continu de la toiture au sol ?** | **Oui, avec deux ruptures localisées traitées** (`F2` et `F3` suppriment deux murs ; `F1a/F1b/F1c` percent un troisième). Traitement par frangement + étaiement, **aucune rupture non traitée** | § 3 |
| 3 | **La torsion est-elle maîtrisée ?** | **Oui** — excentricité structurale mesurée `≤ 0,14 m` au R+1 et `≤ 0,04 m` au RDC ; avec l'excentrique accidentelle `±0,05 L`, le mur le plus chargé reste à **`τ/f_vk ≤ 0,028`** sous vent | § 4 |
| 4 | **Le bâtiment est-il régulier ?** | **Irrégulier en plan** (réentrants et ailes dissymétriques), **régulier en élévation**. Verdict opposable : la méthode de calcul retenue intègre l'excentrique accidentelle | § 4.5 |
| 5 | **Faut-il des joints de dilatation ?** | **Aucun joint à créer** — dilatation libre `5,2 mm` sur 17,5 m, maçonnerie stabilisée, frangements appuyés | § 5 |
| 6 | **La position sismique est-elle tenue ?** | **EC8 non applicable** : zone 1, quelle que soit la catégorie d'importance (arrêté du 22/10/2010, art. 3). Vérification de sensibilité en catégorie III : `V_b = 150,5 kN`, `τ/f_vk ≤ 0,069` | § 6 |

**Conséquence pratique pour la suite de la chaîne :** le système de contreventement est **surdimensionné en résistance** (taux de travail inférieur à 7 % partout) mais **non chaîné** au sens de l'EC6/EC8. La stabilité globale n'est donc pas une question de capacité : c'est une question de **continuité, de phasage et de liaisonnement**. C'est exactement ce que cette note organise.

---

## 1. DONNÉES D'ENTRÉE QUALIFIÉES AVANT CALCUL

| Donnée | Valeur retenue | Source | Statut |
|---|---|---|---|
| Zone de sismicité | **1** (très faible) | D2 p. 1 — cartouche | **Contractuelle** |
| Catégorie d'importance | **II** | D2 p. 1 — cartouche | **Contractuelle** — *voir réserve § 6.2* |
| `a_gr` | **0,40 m/s²** | H-24 + arrêté du 22/10/2010, art. 4 (tableau zone 1) | **Hypothèse notifiée** |
| Classe de sol | **C** — sites meubles (alluvions) | H-24 | **Hypothèse notifiée** |
| Vent — zone | **2** · `v_b = 24 m/s` | D2 p. 1 (CHG-06) | **Contractuelle** |
| Vent — catégorie de terrain | **III** · `z_0 = 0,30 m` · `z_min = 5 m` | CHG-06 | **Contractuelle** |
| `c_pe,net` · `c_s c_d` | **1,30** (auvent + sous-le-vent) · **1,00** | EC1-1-4 § 7.2 · bâtiment < 15 m | Méthode |
| Hauteurs libres | RDC **3,00 m** · R+1 **3,00 m** · faîtage **6,30 m** | D2 (P2 `H = 3,00 m`) + D5 | Contractuelle |
| Maçonnerie — `f_k` | **1,5 MPa** | H-25 (moellons + mortier bâtard) | **Hypothèse notifiée** |
| Maçonnerie — `E` | **1 500 MPa** (`E = 1 000 f_k`, EC6 § 3.7.2) | H-25 | **Hypothèse notifiée** |
| Maçonnerie — `f_vk0` | **0,15 MPa** | H-26 | **Hypothèse notifiée** |
| Contrainte verticale moyenne `σ_d` | **0,30 MPa** | H-27 | **Hypothèse notifiée** |
| Surfaces de plancher | RDC **111,15 m²** · R+1 **106,92 m²** | D-22 | Décision client |

**Preuve d'épuisement du corpus (V14).** Les pièces `D1` à `D5`, `B-02 Ind. F`, `B-03 Ind. P`, `B-20 Ind. B`, `B-32 Ind. D` et `B-40 Ind. E` ont été relues pour cette brique. Les grandeurs de vent, de neige, de sismicité, de matériaux et de géométrie y ont été cherchées **pièce par pièce** ; aucune n'est déclarée « absente » sans que les cinq pièces aient été consultées. Les seules valeurs non fournies par le marché sont les caractéristiques mécaniques de la maçonnerie ancienne — elles n'existent dans aucune pièce et relèvent donc de l'hypothèse notifiée, pas d'un oubli de lecture.

---

## 2. PIÈCE 1 — SYSTÈME DE CONTREVENTEMENT

### 2.1 Nature et implantation

Le pavillon Flora est un bâtiment **en maçonnerie porteuse** (moellons et pierre) de deux niveaux, avec planchers bois et métalliques et charpente bois. Il ne comporte **aucun voile béton, aucun noyau, aucune palée triangulée**. Le système de reprise des efforts horizontaux est donc **la maçonnerie existante elle-même**, travaillant en voiles console encastrés en pied.

La géométrie a été extraite **des fonds nettoyés `B-32 Ind. D`** (blocs géomètre `D5`), sans redessin : 18 polygones surfaciques au RDC et 10 au R+1, dont sont retenus **12 voiles au RDC** et **9 au R+1** après écartement des liserés non surfaciques (aire < 0,15 m², arêtes du relevé sans épaisseur).

| Élément | Compté dans le contreventement | Justification |
|---|---|---|
| **Murs porteurs en maçonnerie** (12 RDC · 9 R+1) | **OUI — système unique** | Continus du sol à la toiture, surfaciques, liaisonnés entre eux aux angles ; aire cumulée 18,79 m² (RDC) et 24,10 m² (R+1) |
| **Façades en moellons** (hors bloc géomètre) | **NON — en réserve** | Épaisseur et continuité non relevées dans `D5` ; comptées uniquement en réserve favorable, jamais comme appui nécessaire. Qualifiées par `PA-01` |
| **Frangements métalliques neufs** `F1a/b/c`, `F2`, `F3`, `F4` | **NON** | Appuis simples, aucune continuité d'encastrement, aucune triangulation : ils reprennent le **vertical**, jamais l'horizontal |
| **Renforts** `R1`, `R2-N/S`, `R3-N/S`, `Stab1` | **NON** | Renforts de flexion locale ; `Stab1` est un anti-déversement, pas une triangulation |
| **Poteaux** `P1-N`, `P1-S`, `P2`, `P3`, `J1` | **NON** | Compression seule ; `P2` est élancé (`H/b = 20`) et ne peut pas être mobilisé en portique |
| **Charpente bois et couverture** | **NON** | Toiture non diaphragme : pas de voilement travaillant, pas de contreventement de toiture identifié dans `D2` |
| **Planchers** (bois 8×18, voutains + IPE 160) | **NON — diaphragme réputé flexible** | Assemblage solives/murs sans dispositif de reprise d'effort horizontal ; hypothèse défavorable retenue (voir § 2.2) |
| **Cloisons, doublages, isolants** | **NON — exclus par `V9`** | Aucun remplissage n'est compté comme système de contreventement (interdiction explicite de la fiche) |

### 2.2 Hypothèse de répartition — diaphragme flexible

Les planchers n'étant pas justifiés comme diaphragmes rigides, la répartition des efforts horizontaux est faite **par raideur de mur, niveau par niveau, sans redistribution par plancher** : c'est l'hypothèse **défavorable** (elle sollicite les murs les plus raides et crée la plus grande torsion). Toute redistribution par un plancher rigide ne pourrait que réduire les efforts dans les murs les plus chargés.

La raideur horizontale de chaque voile est calculée en **console encastrée en pied**, par superposition flexion + cisaillement :

$$K_i=\left[\frac{h^{3}}{3EI_{i}}+\frac{1{,}2\,h}{GA_{i}}\right]^{-1}$$

avec `E = 1 500 MPa`, `G = E / 2,4 = 625 MPa`, `I_i` = inertie du polygone par rapport à l'axe de flexion (calcul exact par formules de Green sur le contour réel), `A_i` = aire du polygone, `h = 3,00 m`.

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

> **Lecture.** Quatre voiles portent plus de 80 % de la raideur : `M03` et `M11` au RDC (86 %), `M03` et `M08` au R+1 (86 %). C'est une structure **à noyaux de maçonnerie concentrés**, pas une structure cellulaire régulière. Toute intervention sur l'un de ces quatre voiles met en péril la stabilité d'ensemble — c'est le fondement des prescriptions de phasage du § 7.
>
> L'épaisseur `t_eq = A/L` est une **épaisseur équivalente** : les voiles `M03`, `M11` (RDC) et `M03`, `M08` (R+1) sont des voiles **coudés** (retours d'angle intégrés au polygone), ce qui explique des valeurs de 0,60 à 0,88 m. Les voiles droits mesurent 0,31 à 0,57 m.

### 2.4 Ce que le système ne garantit pas — et qu'il faut écrire

1. **Aucune ductilité.** Une maçonnerie de moellons est fragile : elle reprend l'effort tant qu'elle reste dans son domaine élastique, puis rompt sans préavis. Le taux de travail de 3 % sous vent ne rend pas la structure ductile — il rend seulement la rupture improbable sous l'action de calcul.
2. **Aucun chaînage.** Les murs ne sont pas chaînés horizontalement ni verticalement au sens de l'EC6 § 8. Nos calculs supposent la continuité ; elle n'est **pas prouvée**. C'est l'objet de `PA-01`.
3. **Aucune liaison plancher-mur en cisaillement.** Rien dans `D3` ne décrit un ancrage des solives ou des voutains dans les murs. L'hypothèse de diaphragme flexible est donc à la fois défavorable pour la répartition et **réaliste pour le contreventement**.

---

## 3. PIÈCE 2 — CHEMINEMENT DES EFFORTS HORIZONTAUX

### 3.1 Tableau par niveau

| Niveau | Origine de l'effort | Valeur de calcul | Éléments de reprise identifiés | Transmission au niveau inférieur | Rupture détectée |
|---|---|---|---|---|---|
| **Toiture** (z = 6,30 m) | Vent sur versants et pignons — `q_p(6,00) = 500 Pa` | Report aux pignons et aux fermes | **Pignons Nord et Sud en moellons** (voiles `M11`, `M12` en partie) + fermes traditionnelles | Par les pignons et les murs d'aplomb jusqu'au plancher haut R+1 | **NON** — à condition que la charpente ne soit pas déposée sans étaiement (§ 7) |
| **R+1** (z = 3,00 → 6,00 m) | Vent sur la bande haute — `V_x = 31,9 kN` · `V_y = 20,2 kN` | Par voile : `M08` reprend 14,6 kN sous vent X (avec torsion) | **9 voiles R+1** · `ΣK_x = 2,06 GN/m` · `ΣK_y = 2,82 GN/m` | Par les voiles R+1 aux voiles RDC, à travers le plancher bas R+1 — **appui direct mur sur mur** aux files A, D et E | **NON** — les voiles R+1 et RDC sont alignés sur les mêmes files (écart d'empilement des emprises : `0,10 m`, `B-31`) |
| **RDC** (z = 0 → 3,00 m) | Vent sur la bande basse + report du R+1 — `V_x = 31,4 kN` · `V_y = 19,9 kN` | Par voile : `M11` reprend 16,4 kN sous vent X (avec torsion) | **12 voiles RDC** · `ΣK_x = 1,21 GN/m` · `ΣK_y = 1,64 GN/m` | Aux **fondations existantes** par les semelles filantes et soubassements en moellons ; aux **semelles neuves** `SF1` (sous `P2`) et sommiers `S1/S2` pour les charges verticales apportées par les frangements | **OUI — deux ruptures**, voir § 3.2 |
| **Fondations** | Effort tranchant global `V_x = 63,2 kN` · `V_y = 40,0 kN` (vent cumulé) · `V_b = 150,5 kN` (sensibilité sismique) | — | Semelles existantes en moellons et béton de chaux ; `SF1` `60×60×30` sous `P2` ; arase `−1,00 m / TN MINIMUM` (`D-08`/`D-12`) | Sol : alluvions anciennes, `q_ELS ≤ 0,30 MPa` | — (hors objet de `B-25` : `B-40`) |

### 3.2 Les deux ruptures de cheminement et leur traitement

| Rupture | Nature | Effet mécanique | Traitement retenu | Preuve |
|---|---|---|---|---|
| **R-1 · `F2` (HEB 200, `L = 2,85 m`) et `F3` (HEB 160, `L = 3,85 m`)** | Suppression de deux murs porteurs de l'aile Est. La fonction **verticale** est reprise par les poutres ; la fonction **horizontale** du panneau supprimé est **définitivement perdue** | La raideur d'ensemble chute ; les murs restants reprennent l'effort et le centre de rigidité se déplace | **Aucun transfert horizontal n'est reconstitué** (ce serait un portique non conçu pour cela). Le système est recalculé **sans les murs supprimés** : voir l'enveloppe de démolition § 7.2. Vérification : `ΣK_y` restant `38,6 %` (RDC), `τ/f_vk = 0,027` — **capacité conservée** | `b25_stabilite.txt` § [7] et [7bis] |
| **R-2 · `F1a` (2×HEA 200, `L = 1,00 m`) percé dans le refend central de 50 cm** | Ouverture dans un voile de contreventement. Le linteau reprend le vertical ; **la maçonnerie au-dessus de l'ouverture ne reprend aucun cisaillement** | Le voile est scindé en deux trumeaux ; la raideur du panneau diminue | Le voile est déjà décompté **en trumeaux séparés** par le relevé géométrique (les ouvertures existantes sont des vides dans les polygones). L'ouverture nouvelle retire **0,50 m²** d'un voile de 4,58 m², soit `11 %` de ce voile et `2,7 %` de la raideur totale — couvert par l'enveloppe de phasage qui teste le **retrait complet** du voile | § 7.2 |

**Aucune autre discontinuité n'a été trouvée.** Le contrôle porte sur les 21 voiles des deux niveaux et sur les 4 files d'appui (`A`, `D`, `E`, `4`) : chaque niveau dispose d'une reprise identifiée jusqu'aux fondations. `V15` est satisfait : **aucun effort ne s'arrête en chemin**.

### 3.3 Le cas des frangements — pourquoi ils ne contreventent pas

Un frangement métallique inséré dans une maçonnerie est souvent présenté, à tort, comme un « cadre de contreventement ». Trois raisons techniques l'interdisent ici :

1. **Les assemblages sont des appuis simples.** `F4` s'appuie sur `F2` et sur un sommier `S1` ; `F2` s'appuie sur deux `S1`. Aucun nœud n'est encastré : la structure est isostatique, donc **cinématiquement libre** sous effort horizontal.
2. **Aucune triangulation.** Aucun des profilés n'est disposé en diagonale. Un portique non triangulé et non encastré ne reprend pas d'effort horizontal — il le transmet par flexion de nœuds, ce qui n'existe pas ici.
3. **Les sommiers `S1`/`S2` sont des appareils de répartition**, pas des fondations de portique : ils sont posés sur la maçonnerie et reprennent une compression verticale. Les solliciter en moment d'encastrement serait une erreur de conception.

**Conclusion :** compter les frangements en contreventement aurait été une faute de conception, et la déclarer « structure contreventée par portiques » aurait été un abus de langage opposable. Le système est **la maçonnerie, rien que la maçonnerie**.

---

## 4. PIÈCE 3 — TORSION ET RÉGULARITÉ

### 4.1 Centres de masse et de rigidité

Le **centre de masse** `G` est pris au barycentre surfacique de l'enveloppe du niveau, les charges permanentes et d'exploitation étant réparties uniformément (`g = 4,50` · `q = 2,50` · `ψ₂ = 0,30 kN/m²`). L'aire de l'enveloppe calculée (`108,4 m²` au RDC, `114,0 m²` au R+1) est comparée aux surfaces utiles de `D-22` (`111,15` et `106,92 m²`) : l'écart de `±4 %` borne l'incertitude du barycentre à **`± 0,15 m`**, très inférieure aux excentricités mesurées et aux excentricités accidentelles appliquées.

| Niveau | `G` (m) | `CR` vent X (Y) | `CR` vent Y (X) | `e` struct. vent X | `e` struct. vent Y | `K_T,x` (kN·m²/rad) | `K_T,y` (kN·m²/rad) |
|---|---|---|---|---|---|---|---|
| **R+1** | (+5,46 ; +10,17) | **+10,32** | **+5,34** | **−0,14 m** | **+0,11 m** | 55 406 367 | 23 959 356 |
| **RDC** | (+5,24 ; +11,13) | **+11,17** | **+5,27** | **−0,04 m** | **−0,03 m** | 18 980 307 | 8 715 280 |

**Lecture.** Les centres de masse et de rigidité sont quasiment confondus : `4 cm` d'écart au RDC, `14 cm` au R+1. Ce n'est pas un hasard — c'est la signature d'une maçonnerie cellulaire dont les murs sont répartis sur le pourtour et sur les refends. La structure est **intrinsèquement peu sensible à la torsion**.

### 4.2 Torsion de calcul

L'excentrique accidentelle réglementaire est appliquée : `e_a = ± 0,05 L` (`L` = dimension perpendiculaire à l'action), soit `±0,87 m` pour un vent selon X et `±0,55 m` pour un vent selon Y — **six à vingt fois l'excentricité structurale mesurée**. Le moment de torsion vaut :

$$M_t = V\,(e_{struct} + e_a)$$

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

**Verdict : la capacité au cisaillement est utilisée à moins de 3 %.** Ce n'est pas un résultat confortable, c'est un résultat **inquiétant à sa manière** : il signifie que la marge est telle que **le vrai risque n'est pas la rupture sous vent, mais l'absence de liaisonnement et la fragilité en phase provisoire**. Une structure qui travaille à 3 % n'a plus besoin d'être renforcée : elle a besoin d'être **tenue**.

### 4.4 Stabilité hors plan

Élancement maximal `h/t_eq` : **17,0** au R+1 (voile `M06`, `t_eq = 0,18 m`) et **20,0** au RDC (voile `M05`, `t_eq = 0,15 m`) — la limite de l'EC6 § 5.5.1.2 pour un mur non chargé latéralement de façon continue est de **20**. Le RDC est **exactement à la limite**, sur un petit trumeau de 0,16 m².

> **Conséquence :** le voile `M05` (`0,16 m²`, épaisseur équivalente 0,15 m) ne doit **jamais** être sollicité comme appui de contreventement principal. Il est conservé dans le modèle parce qu'il existe, mais il est **exclu des prescriptions de reprise** et fait l'objet du point d'arrêt `PA-01` (reconnaissance de son épaisseur réelle et de son état à l'ouverture).

### 4.5 Régularité — verdict et méthode d'analyse

| Critère EC8 § 4.2.3 | Constat géométrique | Verdict |
|---|---|---|
| **Régularité en plan** — rapport des côtés, réentrants | Emprise `11,1 × 17,5 m` en **L**, avec réentrant marqué à l'aile Est, ailes dissymétriques Nord/Sud, façade Sud biaise | **IRRÉGULIER** |
| **Régularité en élévation** — masses et raideurs continues | Deux niveaux de hauteur identique, aucun décrochement de masse, files alignées (`B-31` : écart d'empilement des emprises `0,10 m`) ; seule variation : comble et versants | **RÉGULIER** |
| **Diaphragme** | Planchers bois/voutains non justifiés en diaphragme | **Flexible — répartition par raideur, sans redistribution** |
| **Méthode d'analyse retenue** | Statique linéaire par niveau, répartition en raideur, **excentrique accidentelle `±0,05 L` appliquée dans les deux directions** | **Cohérente avec l'irrégularité constatée** |

**Le point important :** une structure irrégulière en plan est celle où l'on applique l'excentrique accidentelle **sans discussion**. C'est fait. Le réentrant de l'aile Est est en outre le lieu où le diagnostic `D3` situe trois désordres (linteaux, plancher, fissuration de plafond) — ce n'est pas une coïncidence, c'est la conséquence mécanique d'un point singulier de la géométrie, traité par les renforts `R1`, `R2`, `R3` de `B-20`.

---

## 5. PIÈCE 4 — JOINTS DE DILATATION

| Bloc `JD` | Position | Largeur | Motif du découpage | Report plan | Report coupe |
|---|---|---|---|---|---|
| **Aucun** | — | — | Aucun joint créé | Sans objet | Sans objet |

**Justification chiffrée — les quatre motifs de la fiche sont testés un par un :**

| Motif possible de joint | Vérification | Conclusion |
|---|---|---|
| **Longueur** | Dimension maximale du bloc : **`17,5 m`**, très inférieure aux `25 à 40 m` au-delà desquels la maçonnerie non ferraillée exige classiquement un joint | Pas de joint de longueur |
| **Température** | `ΔL = α·ΔT·L = 10⁻⁵ × 30 × 17,5 m = 5,2 mm` — déplacement libre absorbé par la maçonnerie et les appuis coulissants de charpente | Pas de joint de température |
| **Retrait** | Maçonnerie ancienne de plus d'un siècle : le retrait du mortier est **épuisé**. Aucun désordre de retrait dans `D3` (les désordres 1 à 9 sont d'origine mécanique et d'humidité) | Pas de joint de retrait |
| **Tassements différentiels** | **Hors mission** (`D-15`). Aucune ligne de tassement différencié n'est décrite dans `D3`. Un joint créé pour un tassement non mesuré serait un joint sans justification | Pas de joint de tassement — réserve `R-36` maintenue (`B-40`) |
| **Phasage** | Les frangements neufs sont **appuyés** (portées `0,85 à 4,88 m`), sans continuité mécanique longue. Aucune reprise de dilatation ne traverse la structure neuve | Pas de joint de phasage |

> **Ce que cette absence de joint engage.** Un bâtiment sans joint est un bâtiment dont la maçonnerie travaille en continu sur 17,5 m. C'est acceptable **ici** parce que le bâti l'a déjà fait pendant plus d'un siècle sans désordre de dilatation, et parce qu'aucun élément neuf n'impose de mouvement relatif. Cela deviendrait faux si une reprise en sous-œuvre venait à couper le bloc en deux ou si une extension était accolée sans joint. **La décision est donc conditionnelle et doit être réexaminée à toute modification d'emprise.**

---

## 6. POSITION SISMIQUE

### 6.1 Le cadre réglementaire, cité exactement

L'arrêté du 22 octobre 2010 relatif à la classification et aux règles de construction parasismique applicables aux bâtiments de la classe dite « à risque normal » dispose, à son **article 3**, que les règles de construction parasismique s'appliquent :

1. aux bâtiments neufs des catégories d'importance **III et IV** en **zone 2** ;
2. aux bâtiments neufs des catégories **II, III et IV** en **zones 3, 4 et 5**.

**Le pavillon Flora est en zone 1 (très faible).** Aucune catégorie d'importance n'est donc soumise à l'EC8 en zone 1 pour une construction neuve. La position sismique de la brique est en conséquence : **SANS OBJET RÉGLEMENTAIRE**, avec vérification de sensibilité produite ci-dessous.

### 6.2 Réserve sur la catégorie d'importance — à consigner

`D2 p. 1` annonce la **catégorie II**. Or le même arrêté classe en **catégorie III** « les établissements recevant du public des 1ʳᵉ, 2ᵉ et 3ᵉ catégories » et les **établissements sanitaires et sociaux**. Un EHPAD relève typiquement de l'une de ces rubriques.

| Point | Constat | Conséquence |
|---|---|---|
| Catégorie déclarée | **II** (D2 p. 1) | Retenue comme base contractuelle |
| Catégorie possible | **III** si l'établissement est qualifié ERP de 1ʳᵉ à 3ᵉ catégorie ou établissement sanitaire et social | `γ_I` passerait de `1,00` à `1,20` — **sans effet en zone 1** : l'obligation reste nulle |
| Effet sur la présente brique | **Aucun** sur l'obligation ; effet uniquement sur la vérification de sensibilité (déjà faite avec `γ_I = 1,20`) | **Écart documentaire à consigner au RDR** (`D-26` proposé) |

### 6.3 Vérification de sensibilité — enveloppe catégorie III

Elle est produite **pour que la réponse existe** si la MOE, l'exploitant ou un bureau de contrôle la demande, et pour vérifier que la structure ne serait pas mise en défaut par un reclassement.

| Grandeur | Formule | Valeur |
|---|---|---|
| Masse sismique | `W = (111,15 + 106,92) × (4,50 + 0,30 × 2,50) + 106,92 × 0,80` | **1 230 kN** (125,4 t) |
| Période fondamentale | `T₁ = C_t·H^0,75 = 0,05 × 6,30^0,75` | **0,199 s** → plateau |
| Spectre de calcul | `S_d(T₁) = a_gr·S·2,5/q·γ_I = 0,40 × 1,50 × 2,5/1,50 × 1,20` | **1,20 m/s²** |
| Effort tranchant à la base | `V_b = S_d·W/g` | **150,5 kN** |
| Répartition en hauteur | `F_i = V_b·z_i·m_i/Σ z_j·m_j` | `F_R+1 = 103,7 kN` · `F_RDC = 46,8 kN` |

| Cas | `F` (kN) | `M_t` (kN·m) | Mur le plus chargé | `V_i` (kN) | **`τ/f_vk`** |
|---|---|---|---|---|---|
| R+1 — séisme X | 103,7 | 105,4 | M08 | 47,7 | **0,069** |
| R+1 — séisme Y | 103,7 | 69,1 | M08 | 27,0 | **0,039** |
| RDC — séisme X | 46,8 | 42,7 | M11 | 24,4 | **0,041** |
| RDC — séisme Y | 46,8 | 27,2 | M11 | 20,7 | **0,035** |

**Le séisme d'enveloppe catégorie III vaut 2,4 fois le vent, et reste à moins de 7 % de la capacité de cisaillement de la maçonnerie.** Autrement dit : même dans l'hypothèse la plus défavorable — reclassement en catégorie III et application volontaire de l'EC8 — **la structure porte**. Ce qui ne serait pas couvert est la **ductilité** exigée par l'EC8-1 § 9 (chaînages, dispositions parasismiques de la maçonnerie), qui relève d'une mission de conception et non d'exécution.

### 6.4 Dispositions constructives retenues, sans obligation réglementaire

Bien que non imposées, quatre dispositions sont **prescrites** parce qu'elles coûtent peu et corrigent les faiblesses identifiées au § 2.4 :

1. **Liaisonnement des trumeaux** : chaque ouverture nouvelle (`F1a`, `F1b`, `F1c`) reçoit un linteau **ancré dans la maçonnerie** sur 25 cm de chaque côté, avec un chaînage horizontal noyé dans l'enduit au droit du linteau.
2. **Liaison charpente-maçonnerie** : chaque panne et chaque ferme repose sur un **sabot ou une platine** solidaire du mur, jamais en appui simple glissant, pour empêcher le soulèvement au vent.
3. **Chaînage d'angle des pignons** : les quatre angles de pignon reçoivent un chaînage vertical en acier inoxydable scellé, sur la hauteur du pignon.
4. **Étaiement des phases provisoires** : voir § 7, prescription non négociable.

---

## 7. PIÈCE 5 — PHASES PROVISOIRES

### 7.1 Les cinq situations de chantier qui rompent le contreventement

| # | Phase | Ce qui est interrompu | Durée de l'interruption | Vérification produite |
|---|---|---|---|---|
| **P-1** | Démolition du mur Sud de l'aile Est (`F2`, `HEB 200`, `L = 2,85 m`) | Un voile E-O retiré | De la démolition au boulonnage de `F2` et au clavetage des `S1` | Retrait du voile dans le modèle : § 7.2 |
| **P-2** | Démolition du refend central de l'aile Est (`F3`, `HEB 160`, `L = 3,85 m`) | Un voile N-S retiré | Idem | Retrait du voile dans le modèle : § 7.2 |
| **P-3** | Création de l'ouverture `F1a` dans le refend de 50 cm | Le panneau est coupé en deux ; la maçonnerie au-dessus du linteau est **instable latéralement** tant qu'elle n'est pas reprise | De la découpe au clavetage du linteau `2×HEA 200` | § 7.3 |
| **P-4** | Dépose de la couverture et des potelets de charpente | Les pignons perdent leur butée en tête ; ils deviennent des murs **en console** de 3,00 m | De la dépose à la repose de la charpente | § 7.3 |
| **P-5** | Ouverture des fouilles sous `P1-N`, `P1-S`, `P3`, `J1` | Le soubassement est dégagé sur 1,00 m de profondeur | Jusqu'au coulage de `SF1` et de l'égalisation en gros béton | `PA-01` + `B-40 Ind. E` |

### 7.2 Recalcul avec un voile retiré — preuve chiffrée

Pour chaque voile, le modèle est recalculé **sans ce voile** : nouveau centre de rigidité, nouvelle raideur d'ensemble, nouvelle répartition avec torsion, nouveau taux de travail. Les huit situations les plus défavorables :

| Niveau | Voile retiré | Déplacement du `CR` | Raideur restante `ΣK_y` | Mur le plus chargé | `V_i` (kN) | **`τ/f_vk`** |
|---|---|---|---|---|---|---|
| R+1 | **M09** | **−0,87 m** | 2 305 478 / 2 818 175 (**81,8 %**) | M02 | 8,8 | **0,024** |
| R+1 | M02 | −0,79 m | 2 338 042 (**83,0 %**) | M09 | 8,7 | 0,023 |
| R+1 | M08 | +0,90 m | 1 946 394 (**69,1 %**) | M09 | 7,7 | 0,021 |
| RDC | M03 | +0,10 m | 1 201 921 (**73,2 %**) | M11 | 12,1 | 0,021 |
| R+1 | M03 | +0,88 m | 2 044 858 (**72,6 %**) | M09 | 7,5 | 0,020 |
| RDC | M11 | +0,99 m | 826 061 (**50,3 %**) | M03 | 8,2 | 0,017 |
| RDC | M09 | −0,56 m | 1 448 754 (**88,3 %**) | M11 | 9,5 | 0,016 |
| RDC | M04 | −0,29 m | 1 541 070 (**93,9 %**) | M11 | 9,0 | 0,015 |

**Enveloppe de démolition — retrait simultané des deux voiles les plus défavorables :**

| Niveau | Voiles retirés | Déplacement du `CR` | Raideur restante | **`τ/f_vk`** |
|---|---|---|---|---|
| **R+1** | **M08 + M03** | **+3,03 m** | **41,6 %** | **0,040** |
| **RDC** | **M11 + M09** | 0,00 m | **38,6 %** | **0,027** |

> **Le résultat décisif de cette brique.** Retirer **un** voile majeur est absorbable : la raideur reste supérieure à 69 %, le `CR` se déplace de moins de 1 m, la capacité n'est pas entamée. Retirer **deux** voiles majeurs du même niveau déplace le centre de rigidité de **3 mètres** et divise la raideur par 2,4. La structure tient encore en capacité (`τ/f_vk = 0,040`), mais elle devient **mécaniquement aberrante** : les efforts se concentrent sur un voile, la torsion n'est plus maîtrisée par la géométrie, et le moindre défaut de liaison devient critique.
>
> **Prescription non négociable :** *jamais deux voiles majeurs du même niveau ouverts simultanément.* Le phasage doit garantir qu'**un seul** voile majeur (`M03`, `M11` au RDC ; `M03`, `M08` au R+1) est interrompu à un instant donné, et que l'ouvrage de reprise est **clavé et boulonné avant** l'ouverture du suivant.

### 7.3 Prescriptions de stabilité provisoire

| Phase | Prescription | Justification |
|---|---|---|
| **P-1 / P-2** | **Étaiement préalable** de la zone démolie par étançons sous poutre de répartition, **avant toute découpe**. Le frangement est posé, calé et **clavé** ; les étais ne sont retirés qu'après 7 jours et contrôle du serrage | Un mur porteur ne se démode pas : on ne coupe que ce qui est déjà repris |
| **P-2** | Ordre imposé : `F3` **puis** `F2` (jamais l'inverse) | `F3` s'appuie sur les `S1` en tête de mur ; démolir `F2` d'abord priverait `F3` de son appui transversal |
| **P-3** | **Cintre latéral** du panneau au-dessus du linteau `F1a` pendant la découpe ; linteau `2×HEA 200` mis en place, claveté au mortier sans retrait, puis décinrement | La maçonnerie au-dessus d'une ouverture n'a aucune résistance à la traction ; sans cintre, elle fissure en travers |
| **P-4** | **Étaiement latéral des pignons** sur toute leur hauteur avant dépose de la couverture ; maintien jusqu'à repose des pannes. **Interdiction de déposer la charpente et les pignons dans la même journée** sans reprise | Le pignon en console de 3,00 m avec `h/t = 20` (cf. § 4.4) est stable hors plan par sa seule épaisseur : la moindre poussée parasite le déstabilise |
| **P-5** | Fouilles **par passes alternées**, jamais sur plus de 2 m linéaires en une fois ; remblaiement et gros béton `C16/20` le jour même ; **aucune fouille ouverte le soir** | Le soubassement en moellons est un appui : une fouille ouverte sur toute la longueur supprime l'encastrement des voiles |
| **Toutes phases** | **Interdiction de stocker** des matériaux sur les planchers bois au droit des zones démolies ; charges de chantier limitées à `150 daN/m²` sur les planchers existants | Les planchers bois `8×18` ne sont pas dimensionnés pour une recharge de chantier |

---

## 8. PIÈCE 6 — SCHÉMA DE CONTREVENTEMENT REPORTÉ SUR LE FOND `B-32`

La planche **`FLORA_B25_CONTREVENTEMENT_IndA`** (`.dxf` · `.pdf` · `.png`, A3 paysage, `1/80`) reporte sur le fond structurel pur `B-32 Ind. D` :

- les **12 voiles RDC comptés**, repérés `M01` à `M12`, avec leur raideur `K_x`/`K_y` et leur aire ;
- les **quatre voiles majeurs** (`M03`, `M11` au RDC ; `M03`, `M08` au R+1) mis en évidence comme **voiles à ne jamais ouvrir simultanément** ;
- les **deux ruptures de cheminement** `R-1` (`F2`, `F3`) et `R-2` (`F1a`), avec leur traitement ;
- le **centre de rigidité `CR`** et le **centre de masse `G`** de chaque niveau, la distance `e` entre eux et le **moment de torsion** appliqué ;
- les **flèches de vent** `V_x = 63,2 kN` et `V_y = 40,0 kN` avec leur ligne d'action ;
- la mention **« AUCUN JOINT DE DILATATION »** et sa justification en trois lignes ;
- le tableau des **phases provisoires** et la prescription « un seul voile majeur à la fois » ;
- la note **`D-09` intégrale**, le filigrane **`PRINCIPE — NE PAS EXÉCUTER — Indice P`** et le cartouche `B-25 Ind. A`.

Les repères `M01` à `M12` sont **identiques** à ceux du journal `b25_stabilite.txt`, ce qui rend la planche vérifiable ligne à ligne contre le calcul — condition du critère de report graphique de la fiche.

---

## 9. HYPOTHÈSES NOTIFIÉES, POINTS D'ARRÊT ET PROPOSITIONS D'ARBITRAGE

### 9.1 Hypothèses notifiées créées par cette brique

| Code | Hypothèse | Norme d'appui | Conséquence si démentie | Report |
|---|---|---|---|---|
| **H-25** | La maçonnerie de moellons a `f_k = 1,5 MPa` et `E = 1 500 MPa` (`E = 1 000 f_k`) | EC6 § 3.7.2 et tableau 3.1 (maçonnerie de pierre naturelle) | Si `f_k = 1,0 MPa` : `E = 1 000 MPa`, raideurs divisées par 1,5, `CR` inchangé (les raideurs sont toutes affectées du même facteur), efforts par voile inchangés, `f_vk` abaissé → `τ/f_vk` passerait de 0,03 à 0,045. **Conclusion inchangée** | Note `B-25` · `B-42` · `B-46` |
| **H-26** | `f_vk0 = 0,15 MPa` (cohésion initiale de la maçonnerie ancienne au cisaillement) | EC6 § 3.6.2, valeur plancher pour maçonnerie de pierre à mortier de chaux | Si `f_vk0 = 0,10 MPa` : `f_vk = 80 kPa`, `τ/f_vk` passerait de 0,028 à 0,038. **Conclusion inchangée** | Note `B-25` · `B-46` |
| **H-27** | Contrainte verticale moyenne de service `σ_d = 0,30 MPa` sur les voiles | Estimation de descente de charges (`g + q` sur 218 m² répartis sur 43 m² de voiles) | Si `σ_d = 0,20 MPa` : `f_vk` passe à 92 kPa, effet < 15 % sur les taux. **Conclusion inchangée** | Note `B-25` · `B-21` (vérification) |

### 9.2 Points d'arrêt chantier

| Code | Point d'arrêt | Quand | Qui | Conséquence si non conforme |
|---|---|---|---|---|
| **PA-01** | **Reconnaissance contradictoire de la continuité des voiles de contreventement** : épaisseur réelle, présence de chaînages, liaisons d'angle, état de la maçonnerie (sondages à la pointe et au burin) sur `M03`, `M11` (RDC), `M03`, `M08` (R+1) et sur le trumeau `M05` | **Avant toute démolition** et à l'ouverture des fouilles | Entreprise + MOE | Si un voile majeur est discontinu ou désolidarisé : le système de contreventement est à reconsidérer, arrêt de la phase, reprise de `B-25` à un indice neuf |
| **PA-02** | **Vérification de la liaison charpente-maçonnerie** : nature des appuis de pannes et de fermes sur les pignons, présence de sabots ou de scellements | Avant dépose de la couverture | Entreprise + MOE | Si appuis simplement posés : risque de soulèvement au vent, repose avec sabots obligatoire (disposition § 6.4.2) |

### 9.3 Propositions d'arbitrage soumises au client (non consignées au RDR avant votre décision)

| Code proposé | Objet | Valeur proposée | Effet |
|---|---|---|---|
| **D-26** | **Aucun joint de dilatation** n'est créé sur le pavillon Flora | Confirmé par calcul (§ 5) | Aucun impact plan ; décision à réexaminer en cas de modification d'emprise |
| **D-27** | **Le système de contreventement est la maçonnerie existante seule** ; aucun cadre métallique n'est réputé contreventant | Confirmé par analyse (§ 2) | Interdit toute justification ultérieure par portique ; verrouille la conception |
| **D-28** | **Catégorie d'importance sismique** : `II` (valeur `D2`) maintenue au dossier, avec mention de l'écart possible vers `III` (établissement sanitaire et social) | À viser par la MOE | Sans effet en zone 1 ; conditionne la réponse en cas de reclassement |

---

## 10. AUTO-CONTRÔLE DES SEPT CRITÈRES D'ACCEPTATION

| # | Critère de la fiche `B-25` | État | Preuve |
|---|---|---|---|
| 1 | Chaque niveau dispose d'une reprise d'efforts horizontaux explicitement identifiée, jusqu'aux fondations | ✅ **CONFORME** | § 3.1 : quatre niveaux (toiture, R+1, RDC, fondations), 21 voiles, deux ruptures identifiées et traitées |
| 2 | Les centres de masse et de rigidité, les excentricités et l'effet de torsion sont calculés pour chaque niveau | ✅ **CONFORME** | § 4.1 et 4.2 : `G`, `CR`, `e_struct` mesurés au RDC et au R+1 ; `M_t` calculé avec `e_a = ±0,05 L` |
| 3 | La régularité en plan et en élévation est statuée avec la méthode d'analyse correspondante | ✅ **CONFORME** | § 4.5 : irrégulier en plan, régulier en élévation, méthode statique avec excentrique accidentelle |
| 4 | Chaque zone sismique, catégorie d'importance et classe de sol est sourcée ou porte un repère d'hypothèse avec norme d'appui | ✅ **CONFORME** | § 1 : zone 1 et catégorie II (`D2`, contractuel) ; `a_gr = 0,40` et sol C (`H-24`, arrêté du 22/10/2010) |
| 5 | Chaque joint de dilatation est justifié, coté et reporté en plan et en coupe | ✅ **CONFORME (sans objet justifié)** | § 5 : les cinq motifs de joint sont testés et écartés un par un ; aucun joint à reporter |
| 6 | Les phases provisoires sont étudiées | ✅ **CONFORME** | § 7 : cinq phases, recalcul complet par retrait de voile, enveloppe de démolition, six prescriptions |
| 7 | Aucun élément porteur n'a été dimensionné dans cette brique | ✅ **CONFORME** | Aucune section, aucun ferraillage, aucun assemblage produit ; `f_vk` est une **capacité existante** vérifiée, pas un dimensionnement |

**Verdict de la brique `B-25` (Indice A) : ✅ CONFORME — 7/7.**

---

## 11. POINT DE CONTRÔLE HUMAIN

Trois décisions vous appartiennent et ne peuvent pas être prises par le modèle :

1. **Le système de contreventement retenu** — la maçonnerie existante seule, sans aucun cadre métallique compté. **Confirmez-vous ?** C'est la décision qui verrouille toutes les suivantes : si vous vouliez compter un jour les frangements, il faudrait les concevoir encastrés et triangulés, ce qui n'est pas le projet.
2. **L'absence de joint de dilatation** sur 17,5 m de maçonnerie. **Confirmez-vous ?**
3. **La prescription « un seul voile majeur ouvert à la fois »** (`M03`, `M11` au RDC ; `M03`, `M08` au R+1), avec étaiement préalable et clavetage avant décinrement. **Est-elle compatible avec le phasage de l'entreprise ?** Si le planning impose d'ouvrir deux voiles simultanément, c'est le planning qui doit changer — pas la prescription.

Dans l'attente de vos observations, les deux points d'arrêt `PA-01` (reconnaissance des voiles) et `PA-02` (liaison charpente-maçonnerie) sont **ouverts** et conditionnent le démarrage des travaux, sans bloquer les briques documentaires suivantes.

**Brique B-25 livrée — en attente de votre GO ou de vos observations.**
