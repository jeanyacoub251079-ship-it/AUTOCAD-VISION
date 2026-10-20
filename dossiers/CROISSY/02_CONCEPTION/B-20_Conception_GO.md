# B-20 — SYNTHÈSE STRUCTURELLE & CONCEPTION STRUCTURE GO

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 — enrichi des **Articles P1 à P8 (Synthèse structurelle du dossier, D-25)** |
| Brique | **B-20** — Conception & Synthèse structurelle GO |
| Phase | **2 — Conception / Synthèse d'exécution** |
| **Mode d'appel** | **PARTIEL-DÉCLARÉ** *(BET de conception EVEN existant mais partiel : plans de principe D2 + diagnostic D3 fournis sans DXF structure ni notes de calcul d'exécution des renforts — D-17)* |
| Régime | **OUTILLÉ (V13)** — extraction vectorielle Python/PyMuPDF + `ezdxf`, audit `0 erreur`, contrôle visuel des 3 planches |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Corpus synthétisé (P1) | **D1** (CCTP Lot 01 GO, 38 p.) · **D2** (Plans MOE Structure EVEN `24.09.356E` Ind. C, 5 folios) · **D3** (Diagnostic structure EVEN du 24/03/2025, 19 p.) · **D4** (Plans Architecte Truelle Ind. C, 29 p.) · **D5** (DXF Architecte Ind. C) · `B-02` Ind. F · `B-03` Ind. P · `B-32` Ind. D |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b20_conception.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b20_conception.txt` |
| **Planches graphiques** | **Planche 1** : `_plans/FLORA_B20_PH-RDC_PRINCIPE-STRUCTUREL_IndB` (dxf, pdf, png) · **Planche 2** : `_plans/FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB` (dxf, pdf, png) · **Planche 3** : `_plans/FLORA_B20_CHARPENTE_COUPES_SCHEMA_IndB` (dxf, pdf, png) |
| **Indice** | **B** *(remplace et annule l'indice A du 19/10/2026 — refonte complète)* |
| Date | **20/10/2026** |
| Brique suivante | **B-21** (DDC préliminaire) · **B-22** (Note d'hypothèses consolidée D-19) · **B-42 à B-50** (Calculs d'exécution par famille) |

> **Prescription obligatoire D-09 — reproduite intégralement en tête :**
> **« AU MEME NIVEAU QUE LES FONDATIONS EXISTANTES... RAJOUTER DU GROS BETON... CETTE NOTE EST A INDIQUER SUR LES PLANS ET NOTE DE CALCULS »**

---

## 0. POURQUOI L'INDICE B REMPLACE INTÉGRALEMENT L'INDICE A — RECTIFICATIF FACTUEL

L'indice A reposait sur un cadrage erroné (*« aucun lien D5 ↔ D2 — impossible d'implanter les porteurs neufs »*) et sur quatre erreurs de lecture documentaire que la synthèse intégrale du dossier (**Articles P1 à P8, décision D-25**) corrige par preuve géométrique et textuelle :

| Point | Affirmation erronée de l'indice A | Fait vérifié dans le corpus du marché (D1 à D5) | Impact direct sur l'étude |
|---|---|---|---|
| **1. Lien géométrique `D2 ↔ D5`** | « Lien D5 ↔ D2 non établi — porteurs non plaçables » | **D2 est un PDF vectoriel tracé par EVEN exactement à l'échelle `1/80` (`2,82222 cm/pt`) sur le même relevé géomètre que D5.** L'inscription par moindres carrés donne un écart d'échelle de **−14,6 ppm** et un **résidu médian de `21,0 mm`** sur les murs porteurs | **100 % des ouvrages neufs de D2 (Folio 01, Folio 02, Folio 03, Folio 04) sont implantés et cotés dans le repère B-30 / D5** |
| **2. Poteaux métalliques `P1` et nuance** | « Un seul poteau P1 reprenant 71 à 83 % des 1 382 kN du R+1 ; nuance S235/S275 inconnue » | **D2 p. 1 fixe contractuellement `Acier : S275`.** **D2 Folio 01 implante DEUX poteaux `P1` (`P1-N` et `P1-S`)**, tubes carrés `140×140` en façade Ouest Sud *« en renfort du linteau bois existant »* | Chaque `P1` ne reprend qu'une fraction du linteau bois de façade (**`N_Ed ≈ 45 à 75 kN`**), et non le bâtiment entier |
| **3. Confusion `S1` (sommier vs semelle) et omission `P2 / P3 / J1 / S2`** | `S1` lu comme semelle ; `P2`, `P3`, `J1` et `S2` absents de la note et des plans | Sur **D2 Folio 01**, **`S1` = Sommier BA `20×40×20ht` (×10)** et **`S2` = Sommier BA `20×ép. mur×20ht` (×6)** ; **`P2` = Poteau BA `15×25`**, **`P3` = Poteau BA `50×40`**, **`J1` = Jambage BA `24×50`**. La **semelle BA neuve `25×25` (`EXI-07a`, portée à `60×60` mini par `D-14`)** se situe **sous `P2`** (Folio 01 & Folio 03) | Distinction rigoureuse entre **16 sommiers BA en tête de murs** (`S1`, `S2`) et **fondation `SF1` en pied de `P2`** + **nuages `D-19`** sous `P1-N`, `P1-S`, `P3` et `J1` |
| **4. Sondages des planchers & épaisseur des murs** | « Aucun sondage n'existe ; épaisseur des murs en moellons inconnue (6 à 8 cm) » | **D3 p. 10 à 13** restitue les **sondages destructifs** des **Planchers A (bois 8×18 + BM 15×20)** et **B (IPE 160 + voutains briques + chape 10 cm + IPE 330)** ; seule la **cage centrale** est marquée *« plancher haut non sondé »* (D3 p. 4 & 10). Et le refend central mesure **`50,0 cm`** (`X = 89,525 → 90,025 m`) | Périmètre d'incertitude cerné avec précision par **nuage `D-19`** sur la seule trémie/hall central et les 2 zones de charpente |

---

## SECTION 1 — HYPOTHÈSES DE CONCEPTION & DOCTRINE DE SYNTHÈSE

### 1.1 Positionnement de mission (Article P4 / D1 art. 01.2.1.1.6)

Conformément à **D1 p. 13 (`01.2.1.1.6 Études béton`)**, la conception de principe a été établie par **EVEN STRUCTURES** (`24.09.356E` Ind. C). Notre mission de **bureau d'études d'exécution Gros Œuvre de l'entreprise** consiste à :
1. **Synthétiser sur un fond structurel unique** — expurgé des cloisons de second œuvre et complexes d'isolation (`B-32 Ind. D`) — l'état **EXISTANT**, les **DÉMOLITIONS** (`102_demol`), les **PATHOLOGIES** (`D3`) et **l'intégralité des ouvrages neufs** (`D1 + D2`) ;
2. **Contrôler en prédimensionnement** la cohérence mécanique et les ratios de chaque ouvrage avant les notes de calcul d'exécution détaillées (`B-40` à `B-50`) et les plans de coffrage/ferraillage (`B-60`, `D-17`).

### 1.2 Données contractuelles et hypothèses de conception retenues

| Code FDC / RDR | Paramètre | Valeur retenue | Source & statut |
|---|---|---|---|
| `MAT-01a / 01b` | Bétons | Structure **`C25/30`** (`f_cd = 14,17 MPa`) · Gros béton **`C16/20`** | **D2 p. 1** — Contractuelle |
| `MAT-04` | Armatures BA | **`S500B`** (`f_yk = 500 MPa`, `f_yd = 434,8 MPa`) | **D2 p. 1** — Contractuelle |
| `MAT-05f` | Acier de construction | **`S275`** (`f_y = 275 MPa`, `E = 210 GPa`) | **D2 p. 1** — Contractuelle |
| `MAT-03a / 03b` | Enrobages nominaux | **`50 mm`** en fondations (XC2) · **`30 mm`** en superstructure (S4) | **D-06** — Décision client |
| `SOL-01 / 02 / 03` | Sol & assise | Alluvions anciennes dès `−0,50 m` · **`q_ELS ≤ 0,30 MPa`** · **`q_ELU ≤ 0,49 MPa`** · arase **`−1,00 m / TN mini`** · dim. mini **`60 × 60 cm`** · hors nappe | **D-02 / D-03 / D-08 / D-09 / D-12 / D-14 / D-16** |
| `NIV-01` | Référence altimétrique | **`0,00 RELATIF`** = plancher bas du RDC existant | **D-20 / D-21** — Décision client |
| `CHG-02` | Exploitation plancher R+1 | **`q = 2,50 kN/m²`** (cabinet paramédical, D2 p. 1 ; vs `1,50 kN/m²` logement D3) | Enveloppe haute déclarée |
| `CHG-03` | Permanentes plancher R+1 | Sans recharge : **`g_A = 2,00 kN/m²`** (bois) / **`g_B = 3,50 kN/m²`** (voutains D2/D3) · Enveloppe avec recharge 15 cm D4 : **`g_env = 6,80 kN/m²`** | Enveloppe déclarée — verrou MOE |
| `INC-01` | Sécurité incendie | **Une protection au feu adéquate doit être prévue** (D2 p. 1 / D1 p. 26) — aucun dimensionnement incendie produit ici | Règle CARNAC B-20 |

---

## SECTION 2 — TRAME STRUCTURELLE & SYNTHÈSE EXISTANT → PROJET

### 2.1 Calage vectoriel exact `D2 (EVEN) ↔ D5 (Architecte)`

L'analyse vectorielle comparée des murs porteurs du bloc `Murs porteurs selon geometre projet` (`D5`) et des tracés d'épaisseur `1,44 pt` du folio 01 (`D2`, page tournée à `270°`, échelle annoncée `1/80`) établit la relation affine directe en centimètres DXF :

$$X_{\text{DXF}} = 8\,114{,}33 + 2{,}82222 \cdot x_{\text{vis,F01}} \qquad ; \qquad Y_{\text{DXF}} = 6\,606{,}50 - 2{,}82222 \cdot y_{\text{vis,F01}}$$

avec décalages inter-folios constants au centième de point : `(Δx, Δy) = (+33,00 ; −3,12) pt` pour **Folio 02 (Charpente)** et `(+54,06 ; +33,66) pt` pour **Folio 03 (PB RDC)**. Sur les sommets homologues des murs porteurs, l'écart d'échelle est de **−14,6 ppm** et le **résidu médian d'inscription est de `21,0 mm` (`p95 = 29,2 mm`)**.

### 2.2 Files de la trame structurelle retenue

| File | Orientation | Cote DXF (m) | Cote repère B-30 (m) | Support physique / Rôle porteur |
|---|---|---|---|---|
| **File A** | Verticale (N–S) | `X = 85,55 m` | `X_B30 = −0,32 m` | Façade Est de l'aile Est (baies Désordre 1, linteaux `R3-N`, `R3-S`, sommiers `S1`/`S2`, demi-fermes) |
| **File B** | Verticale (N–S) | `X = 86,55 m` | `X_B30 = +0,68 m` | Façade Est en retrait de l'extension Sud-Est (appui Ouest de `F2`, `Bêche BA`) |
| **File C** | Verticale (N–S) | `X = 88,75 m` | `X_B30 = +2,88 m` | Axe du mur longitudinal démoli Sud-Est → poutre `F4 (IPE 200)` ; panne ajoutée R+1 (`X = 88,56 m`) |
| **File D** | Verticale (N–S) | `X = 89,78 m` | `X_B30 = +3,91 m` | **Refend central majeur en moellons ép. `50 cm`** (`89,53 → 90,03 m`) : appui central de `R1, R2, F2, F3`, frangement `F1a`, jambage `J1` |
| **File E** | Verticale (N–S) | `X = 95,35 m` | `X_B30 = +9,48 m` | **Façade Ouest** : portique Nord remplacé par `P2 (15×25 BA)` sur semelle `SF1 (60×60)`, portique Sud renforcé par `P1-N` et `P1-S (140×140)`, ferme tradi à renforcer |
| **File 1** | Horizontale (E–O) | `Y = 44,60 m` | `Y_B30 = +0,17 m` | Mur pignon Sud biais en moellons (appui Sud `S1` de `F4` et solivage Sud) |
| **File 2** | Horizontale (E–O) | `Y = 49,54 m` | `Y_B30 = +5,11 m` | Mur Sud de l'aile Est démoli → frangement **`F2 (HEB 200)`** recevant `F4` |
| **File 3** | Horizontale (E–O) | `Y = 52,14 m` | `Y_B30 = +7,71 m` | Refend Sud du hall central en moellons ép. `50 cm` (`51,88 → 52,41 m`) : frangement **`F1c (2×HEA 200)`** ; voisin de **`F3 (HEB 160)`** à `Y = 53,12 m` |
| **File 4** | Horizontale (E–O) | `Y = 54,89 m` | `Y_B30 = +10,46 m` | Alignement transversal majeur : **poutre bois `15×20` moisée par `R1 (2×UPE 200)`** à l'Est + **refend Nord du hall (`54,64 → 55,14 m`)** percé par **`F1b (2×HEA 200)`** + poteau **`P3 (50×40 BA)`** |
| **File 5** | Horizontale (E–O) | `Y = 59,05 m` | `Y_B30 = +14,62 m` | Pignon Nord de l'aile Est + poteau **`P2 (15×25 BA)`** et **semelle neuve `SF1`** à `Y = 59,29 m` |
| **File 6** | Horizontale (E–O) | `Y = 63,12 m` | `Y_B30 = +18,69 m` | Pignon Nord principal en moellons + joint de dilatation et **RSO passerelle château** (`Y = 63,3 → 64,3 m`) |

### 2.3 Matrice exhaustive de synthèse `EXISTANT → DÉMOLITION / PATHOLOGIE → OUVRAGE PROJETÉ` (Article P3)

Chaque ouvrage neuf du dossier est rattaché à **un écart architectural `102_demol` ou un désordre diagnostiqué `D3`** — aucun élément n'est orphelin :

| Zone | État EXISTANT (D3 / D5) | Modification PROJET / Désordre (D3 / D4 / D5 `102_demol`) | Ouvrages neufs synthétisés (D1 + D2 + Décisions) |
|---|---|---|---|
| **Refend central (File D)** | Mur porteur en moellons ép. `50 cm` | Création d'ouverture `L_libre = 1,00 m` au RDC entre hall et aile Est (`102_demol`) | **`F1a` (`2×HEA 200`)** + jambage Nord **`J1` (`24×50 BA`)** + sommier Sud **`S2` (`20×50×20 BA`)** + nuage pied `Z-J1` |
| **Mur Nord hall (File 4 Ouest)** | Mur moellons `50 cm` + linteau bois existant | Élargissement / modification baie et appui de linteau (`102_demol`) | **`F1b` (`2×HEA 200`)** + sommier Ouest **`S2`** + poteau Est **`P3` (`50×40 BA`)** + nuage pied `Z-P3` |
| **Mur Sud hall (File 3 Ouest)** | Mur moellons `50 cm` + baie existante | Création / élargissement baie vers salle Sud (`102_demol`) | **`F1c` (`2×HEA 200`)** + **`2 × S2` (`20×50×20 BA`)** |
| **Aile Est — refends intérieurs** | Parois porteuses transversales (`Y = 53,12` et `49,54 m`) et longitudinale Sud-Est (`X = 88,75 m`) | **Démolition complète** au RDC pour créer les plateaux/bureaux paramédicaux (`102_demol`) | **`F3` (`HEB 160`, `L=3,85 m`)** + **`F2` (`HEB 200`, `L=2,85 m`)** + **`F4` (`IPE 200`, `L=4,88 m`)** + **`5 × S1` (`20×40×20 BA`)** |
| **Aile Est — Plancher A** | Solives bois `8×18` (`e=0,50 m`) sur poutre maîtresse bois `20×15` | **Désordre 3** (`W = 72,8 mm > 10,4 mm`, surcontrainte `+200 %`) + hausse d'exploitation `150 → 250 daN/m²` | Moisage **`R1` (`2×UPE 200`, `L=3,85 m`)** sur **`2×S2`** + 2 poutres sous-solivage **`R2-N / R2-S` (`HEB 160`, `L=3,82 m`)** |
| **Façade Est (File A)** | 2 baies avec linteaux bois déformés non porteurs | **Désordre 1** + report des réactions d'appui Est de `R2-N` et `R2-S` au-dessus des 2 baies (`L=1,55 m`) | **`R3-N` & `R3-S` (`UPE 200`)** reposant sur **`4 × S1` (`20×40×20 BA`)** |
| **Aile Ouest — Plancher B** | Solives `IPE 160` (`e=0,72 m`) + voutains briques 7 cm + chape 10 cm + `2×IPE 330` | Instabilité au **déversement** des solives `IPE 160` diagnostiquée sous Robot (**D3 p. 12 & 18**) | **`4 files Stab1`** : entretoises `IPE` anti-déversement incorporées par saignées ponctuelles dans les voutains briques |
| **Façade Ouest Nord (File E)** | Portique bois `23×15` sur poteaux bois `15×15`, allège maçonnée | Portique **non justifié en flèche et contrainte** (**D3 p. 17**) + contraintes élevées en pied | Remplacement poteau + allège par **`P2` (`15×25 BA`)** fondé sur **semelle neuve `SF1` (`60×60×30 BA mini`, `D-14`)** + gros béton `D-09` |
| **Façade Ouest Sud (File E)** | Grande baie sous portique/linteau bois `23×15` | Contraintes élevées en pied et soulagement du linteau bois (**D3 p. 16**, **D2 f.01**) | **`2 × P1` (`P1-N` et `P1-S`, `tube carré 140×140 S275`)** sous linteau bois + vérification soubassement moellons (**nuages `Z-P1N / Z-P1S`**) |
| **Combles / Charpente R+1** | Charpente bois avec potelets sur plancher haut et ferme altérée | **Désordre 5** (fissures plafond), **Désordre 6** (ferme humide), **Désordre 8** (potelets instables) | **2 demi-fermes en sous-œuvre** désolidarisées du plancher + **3 pannes neuves** + **contrefiches sur ferme tradi** (**D2 f.02**, lot GO `H-14`) |
| **Infrastructure & Passerelle** | Terre-plein ancien, soubassements moellons, passerelle Nord | Création dallage paramédical PMR + fissures passerelle | **Dallage BA désolidarisé `ép. 13 cm`** sur forme `40 cm` + géotextile XA4 + **Bêche BA `ép. 20 cm`** (`EXI-07c`) + **RSO passerelle** en gros béton (`EXI-07e`) |

---

## SECTION 3 — PRÉDIMENSIONNEMENT DES OUVRAGES NEUFS (RATIOS & FORMULES APPROCHÉES)

> **Règle CARNAC B-20 respectée strictement :** aucune section n'est posée « par expérience » ; chaque section est contrôlée par **une formule approchée ou un ratio explicite**, sans calcul fin d'exécution (réservé à `B-42`, `B-44`, `B-45`, `B-46`, `B-50`).

| Élément (qté) | Section retenue | Portée / Hauteur mesurée | Formule / Ratio de prédimensionnement | Calcul approché chiffré | Ratio / Verdict de principe |
|---|---|---|---|---|---|
| **`F1a, F1b, F1c`** (3) | **`2 × HEA 200`** (`S275`, `2·I_y = 7 380 cm⁴`, `2·W_el = 779 cm³`) | `L_libre = 0,85 à 1,00 m` (`L_calc = 1,25 m`) | Sous-œuvre de mur porteur en moellons : `h ≥ L_calc / 15` et `σ_Ed = M_Ed / W_el ≤ f_y` | Pour `p_ELU ≈ 55 kN/ml` (mur + plancher + toit), `M_Ed = 55 × 1,25² / 8 = 10,7 kN·m << M_el,Rd = 214 kN·m` | **`h / L_calc = 1 / 6,6`** (`>> 1/15`) — **Très rigide (OK)** |
| **`F2`** (1) | **`HEB 200`** (`S275`, `W_el = 570 cm³`, `I_y = 5 696 cm⁴`) | `L = 2,85 m` | Poutre de reprise avec charge ponctuelle de `F4` : `h ≥ L / 15 = 190 mm` | `M_Ed,app ≈ q_ELU·L²/8 + P_F4·L/4 ≈ 22 + 28 = 50 kN·m < M_el,Rd = 157 kN·m` | **`h / L = 1 / 14,3`** (`≥ 1/15`) — **Conforme (OK)** |
| **`F3`** (1) | **`HEB 160`** (`S275`, `W_el = 311 cm³`, `I_y = 2 492 cm⁴`) | `L = 3,85 m` | Poutre de plancher courant : `h ≈ L / 20 = 193 mm` ; résistance `M_el,Rd = W_el · f_y` | Sans recharge (`p_ELU ≈ 22 kN/ml`), `M_Ed ≈ 40,8 kN·m < M_el,Rd = 85,5 kN·m` ; avec recharge `CHG-03`, flèche ELS gouvernante | **`h / L = 1 / 24,1`** — **⚠️ Point de vigilance flèche ELS à vérifier en `B-45`** |
| **`F4`** (1) | **`IPE 200`** (`S275`, `W_el = 194 cm³`, `I_y = 1 943 cm⁴`) | `L = 4,88 m` | Poutre sous toiture basse sans étage R+1 au-dessus : `h ≈ L / 25 = 195 mm` | Sous toiture légère (`g+q ≈ 2,3 kN/m²`, bande `1,9 m`), `M_Ed ≈ 20,1 kN·m < M_el,Rd = 53,4 kN·m` | **`h / L = 1 / 24,4`** — **Conforme sous toiture seule ; déversement en `B-45`** |
| **`R1`** (1) | **`2 × UPE 200`** (`S275`, `2·W_el = 382 cm³`, `2·I_y = 3 820 cm⁴`) | `L = 3,85 m` | Moisage de poutre maîtresse plancher : `h ≈ L / 20 = 193 mm` | Bande `1,98 m` : `M_Ed ≈ 31,1 kN·m` (hors recharge) à `47,5 kN·m` (avec `CHG-03`) `< M_el,Rd = 105 kN·m` | **`h / L = 1 / 19,3`** (`≥ 1/20`) — **Conforme (OK)** |
| **`R2-N, R2-S`** (2) | **`HEB 160`** (`S275`, `W_el = 311 cm³`, `I_y = 2 492 cm⁴`) | `L = 3,82 m` | Poutre de refend sous solivage bois divisant la portée par 2 : `h ≈ L / 20` | Bande `1,85 m` : `M_Ed ≈ 21,8 à 43,5 kN·m < M_el,Rd = 85,5 kN·m` | **`h / L = 1 / 23,9`** — **⚠️ Contrôle flèche ELS `L/350` requis en `B-45`** |
| **`R3-N, R3-S`** (2) | **`UPE 200`** (`S275`, `W_el = 191 cm³`, `I_y = 1 910 cm⁴`) | `L_baie = 1,55 m` (`L_tot = 2,50 m`) | Linteau sous charge ponctuelle à mi-travée (`R2`) : `h ≥ L / 10 = 155 mm` | Charge ponctuelle `R_2,Ed ≈ 42 kN` à mi-portée → `M_Ed = P·L/4 = 16,3 kN·m < M_el,Rd = 52,5 kN·m` | **`h / L = 1 / 7,8`** — **OK (torsion d'excentrement UPE à bloquer en `B-50`)** |
| **`Stab1`** (4 files) | **Entretoises `IPE`** (`S275`, hauteur adaptée `IPE 120/140`) | Pas `≈ 2,50 m` sur solives `IPE 160` | Maintien latéral anti-déversement d'aile comprimée : effort de stabilisation `F_stab ≈ N_comp / 100` | Solive `IPE 160` : `F_stab < 2 kN` par file → profilé léger largement surabondant | **Conforme au principe `D3 p. 18`** |
| **`P1-N, P1-S`** (2) | **`Tube carré 140 × 140`** (`S275`, ép. dessinée `10 mm` ou `6,3 mm` mini) | `H ≈ 3,00 m` | Élancement mécanique courant `L_0 / i ≤ 80` (`i ≈ 0,39·b = 55 mm`) et `N_Rd,app ≈ 0,6 · A · f_y` | `L_0 / i ≈ 55 ≤ 80` ; même en `ep. 6,3 mm` (`A = 33,1 cm²`), `N_Rd,app ≈ 546 kN >> N_Ed ≈ 65 kN/poteau` | **Taux `< 15 %`** — **Épaisseur nominale `t` à figer en `B-45`** |
| **`P2`** (1) | **`Poteau BA 15 × 25 cm`** (`C25/30`, `A_c = 375 cm²`) | `H ≈ 3,00 m` | Prédimensionnement poteau BA : `A_c ≥ N_Ed / (0,3 · f_cd)` | `0,3 · A_c · f_cd = 0,3 × 37 500 × 14,17 = 159 kN > N_Ed ≈ 85 kN` | **OK en compression ; élancement `H / b = 20` à vérifier au flambement en `B-42`** |
| **`P3`** (1) & **`J1`** (1) | **`Poteau BA 50 × 40 cm`** (`2 000 cm²`) · **`Jambage BA 24 × 50 cm`** (`1 200 cm²`) | `H ≈ 2,40 à 2,80 m` | Appuis BA massifs dans maçonnerie : `A_c ≥ N_Ed / (0,3 · f_cd)` et diffusion `< 1,0 MPa` | Capacité `510 kN` (`J1`) et `850 kN` (`P3`) `>> N_Ed ≈ 90 à 140 kN` (`σ_ELS < 0,8 MPa`) | **Largement surabondant (OK)** |
| **`S1` (×10) & `S2` (×6)** | **`S1 : 20 × 40 × 20ht BA`** (`800 cm²`) · **`S2 : 20 × 50 × 20ht BA`** (`1 000 cm²`) | `h = 20 cm` | Sommier d'appui sur moellons : `A_appui ≥ R_ELS / σ_adm,mac` (`σ_adm ≈ 0,8 MPa`) | `R_ELS,adm = 64 kN` (`S1`) et `80 kN` (`S2`) `> réactions R_ELS ≈ 20 à 55 kN` | **Conforme (OK — `B-46 / B-50`)** |
| **`SF1`** (1 certaine + 4 en nuage `D-19`) | **`Semelle BA 60 × 60 × 30 cm mini`** (`D-14`, remplaçant `25×25` EVEN) | `B ≥ 0,60 m`, `h = 0,30 m` | Portance `B ≥ √(N_ELS / q_ELS)` avec `q_ELS = 0,30 MPa` | Sous `P2` (`A ≈ 6,5 m²`) : `N_ELS = 63,2 kN ≤ 108 kN` (`B_req = 0,46 m → 0,60 m mini D-14`) | **`σ_ELS = 0,18 MPa ≤ 0,30 MPa` — OK (`B-40 Ind. E`)** |

---

## SECTION 4 — RENFORTS DE L'EXISTANT & RATTACHEMENT AU DIAGNOSTIC (`B-11`)

| Désordre `B-11` (`D3`) | Pathologie constatée dans `D3` | Ouvrage de reprise retenu | Justification mécanique & précaution de phasage |
|---|---|---|---|
| **Désordre 1** *(D3 p. 5)* | Déformation des deux linteaux non porteurs de la façade Est | **`R3-N` & `R3-S` (`UPE 200`)** + **`4 × S1`** | Les nouvelles poutres `R2-N` et `R2-S` s'appuient au droit de ces baies : `R3` court-circuite totalement les anciens linteaux bois déformés |
| **Désordre 3 & 9** *(D3 p. 6, 9, 11, 19)* | Fléchissement excessif de la poutre bois `20×15` (`W = 72,8 mm`) et fissuration du plafond lattis-plâtre | **`R1` (`2×UPE 200` moisé)** + **`R2-N / R2-S` (`HEB 160`)** + **`S1 / S2`** | Étaiement complet avant boulonnage de moisage ; arrêt définitif du fluage et division par 2 de la portée des solives `8×18` |
| **Plancher B** *(D3 p. 12 & 18)* | Instabilité au déversement des solives `IPE 160` | **`4 files Stab1`** (entretoises `IPE` dans voutains briques) | Maintien latéral de la semelle comprimée par saignées ponctuelles dans les hourdis briques sans démolir le plancher |
| **Portiques façade Ouest** *(D3 p. 16–18)* | Portique Nord non justifié ; fortes contraintes en pieds sur soubassement pierre | **`P2` (`15×25 BA`) + `SF1` (`60×60×30`)** au Nord · **`2 × P1` (`140×140 S275`)** au Sud | Reprise directe des charges verticales et soulagement définitif des linteaux bois de façade |
| **Désordres 5, 6 & 8** *(D3 p. 7–9, 14–15)* | Ferme altérée par l'humidité, chevrons fléchis et potelets instables chargeant le plancher haut R+1 | **2 demi-fermes en sous-œuvre** + **3 pannes neuves** + **contrefiches sur ferme tradi** (`D2 f.02`, lot GO `H-14`) | Suppression des potelets instables et **désolidarisation vis-à-vis du plancher haut** ; purge sanitaire des bois altérés préalable obligatoire |
| **Désordres 2, 4 & 7** *(D3 p. 5–8, 14)* | Infiltrations façades, descentes EP bouchées, étanchéité SDB | **Hors lot structure (`H-19`)** — interface lots façades / couverture / plomberie | Mise hors d'eau impérative avant habillage et protection des profilés |

---

## SECTION 5 — POINTS À FAIRE VALIDER PAR UN TIERS (ET NUAGES `D-19`)

| # | Point soumis à validation / Nuage `D-19` | Brique CARNAC aval | Intervenant viseur | Régime |
|---|---|---|---|---|
| **1** | **Pieds des 2 poteaux `P1-N` & `P1-S` (`Z-P1N / Z-P1S`)** : confirmation de la portance du soubassement en moellons à l'ouverture de fouille (`D2 f.03`), à défaut création de semelles `60×60×30 BA` (`D-14`) + gros béton (`D-09`) | `B-40` / `B-46` | MOE / Géotechnicien | **Nuage `D-19`** (2 jours) |
| **2** | **Pieds du poteau `P3 (50×40 BA)` et du jambage `J1 (24×50 BA)` (`Z-P3 / Z-J1`)** : reconnaissance du soubassement des refends intérieurs à l'ouverture des fouilles et rattrapage éventuel en gros béton `C16/20` (`D-09`) | `B-40` / `B-46` | MOE / Entreprise | **Nuage `D-19`** (2 jours) |
| **3** | **Zone centrale « Plancher haut non sondé »** (`D3 p. 4 & p. 10`) : sondage destructif contradictoire à réaliser en début de chantier (`D1 art. 01.2.1.5.3.3`) | `B-43` | Entreprise / MOE | **Nuage `D-19`** |
| **4** | **Deux « ZONES NON RELEVÉES » de charpente** (`D2 Folio 02`) : relevé géométrique et sanitaire des bois après dépose des faux-plafonds avant taille/renfort (`H-14`) | `B-44` | Entreprise / MOE | **Nuage `D-19`** |
| **5** | **Flèche ELS des profilés élancés `F3 (HEB 160, L=3,85 m)` et `R2 (HEB 160, L=3,82 m)`** (`h/L ≈ 1/24`), surtout si la recharge de 15 cm (`CHG-03`) s'applique sur l'aile Est → passage éventuel en `HEB 180 / HEB 200` si flèche active `> L/350` | **`B-45`** | BET Structure / BC | Validation calcul EXE |
| **6** | **Épaisseur nominale `t` des tubes carrés `P1 (140×140 S275)`** (`t = 6,3 mm` ou `8 mm` ou `10 mm` dessiné en D2) et **élancement de flambement de `P2 (15×25 BA)`** (`H = 3,00 m`) | **`B-42` / `B-45`** | BET Structure / BC | Validation calcul EXE |
| **7** | **Levée des verrous de charges `CHG-02` (`250 vs 150 daN/m²`) et `CHG-03` (étendue exacte de la recharge de sol de `15 cm` de `D4 p. 5 & 14`)** | **`B-21` / `B-43` / `B-45`** | MOA / Architecte | Arbitrage programme |

---

## SECTION 6 — PLANCHES GRAPHIQUES PRODUITES (ZÉRO CLOISON, ZÉRO ISOLATION)

Les trois planches ont été générées par `b20_conception.py` sur les fonds nettoyés `B-32 Ind. D` (**0 entité** sur `020_cloi` et `020_cloisons`), contrôlées par `doc.audit()` (**`0 erreur`** sur les 3 DXF) et inspectées visuellement en PNG haute définition :

| Planche | Fichiers (`dossiers/CROISSY/_plans/`) | Échelle / Format | Contenu de synthèse |
|---|---|---|---|
| **Planche 1 — PH RDC** | `FLORA_B20_PH-RDC_PRINCIPE-STRUCTUREL_IndB` (`.dxf` 2 790 594 o · `.pdf` · `.png`) | `1/80` — A3 Paysage | Fond porteur pur RDC + démolitions `102_demol` + trame `A–E / 1–6` + implantation cotée de `F1a/b/c, F2, F3, F4, R1, R2-N/S, R3-N/S, 4×Stab1, P1-N/S, P2, P3, J1, 10×S1, 6×S2` + nuage `D-19` plancher non sondé + nomenclature + note `D-09` + filigrane `PRINCIPE — NE PAS EXÉCUTER — Indice P` |
| **Planche 2 — PB RDC / « PLS »** | `FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB` (`.dxf` 2 767 496 o · `.pdf` · `.png`) | `1/80` — A3 Paysage | Implantation sur fond RDC sans cloisons : semelle `SF1 (60×60×30 BA mini)` sous `P2`, nuages `D-19` (`Z-P1N, Z-P1S, Z-P3, Z-J1`), `Bêche BA EXI-07c`, débord semelle arasé, `RSO passerelle EXI-07e`, dallage BA `13 cm`, coupe de principe + note `D-09` & `ENC v3` |
| **Planche 3 — R+1, Charpente & Coupes** | `FLORA_B20_CHARPENTE_COUPES_SCHEMA_IndB` (`.dxf` 2 729 761 o · `.pdf` · `.png`) | `1/80` — A3 Paysage | Plan R+1 sans cloisons avec renforts de charpente (`2 demi-fermes`, `3 pannes`, `contrefiches`, `2 zones non relevées`) + **Coupe transversale A-A** + **Coupe longitudinale B-B** + **Schéma synoptique de cheminement des charges** |

---

## SECTION 7 — LISTE DES POINTS À LEVER POUR LES BRIQUES AVAL

| # | Objet | Raison technique | Brique qui tranchera | Échéance |
|---|---|---|---|---|
| 1 | Étendue exacte de la recharge de 15 cm (`CHG-03`) | Gouverne la flèche de `F3`, `R1`, `R2` (`37 %` d'écart de charge permanente) | `B-21` → `B-45` | Avant `B-45` |
| 2 | Vérification EC3 de flèche de `F3 (HEB 160)` et `R2 (HEB 160)` | Élancement `L / 24` sur `3,82 à 3,85 m` | `B-45` | Phase 4 |
| 3 | Flambement EC2 du poteau élancé `P2 (15×25 BA, H=3,00 m)` | Ratio géométrique `H / b = 20` | `B-42` | Phase 4 |
| 4 |Assemblages `R2 / R3`, boulonnage de moisage `R1` et chevilles/scellements | Efforts locaux et torsion d'excentrement des profils `UPE 200` | `B-50` | Avant `B-60` |
| 5 | Reconnaissance des soubassements sous `P1-N, P1-S, P3, J1` et sondage plancher hall | Validation chantier des nuages `D-19` + égalisation en gros béton `D-09` | `B-40` / `B-46` | Ouverture fouilles |
| 6 | Relevé des 2 zones de charpente non relevées (`D2 f.02`) et purge bois humides | Indispensable avant taille et pose des pannes/demi-fermes (`H-14`) | `B-44` | Avant exécution charpente |

---

## SECTION 8 — AUTO-CONTRÔLE DES SEPT CRITÈRES D'ACCEPTATION CARNAC `B-20`

| # | Critère d'acceptation de la fiche `B-20` | État | Preuve |
|---|---|---|---|
| 1 | Chaque position de porteur est justifiée par la géométrie archi, le diagnostic ou une contrainte citée | ✅ **CONFORME** | Tableau § 2.3 + calage vectoriel `1/80` (`21,0 mm` de résidu) sur les 3 planches |
| 2 | Chaque section retenue est justifiée par une méthode de prédimensionnement citée et un calcul approché chiffré | ✅ **CONFORME** | Tableau § 3 (13 postes chiffrés, **zéro** « par expérience », **2 alertes d'élancement `L/24`** identifiées pour `B-45`) |
| 3 | Chaque renfort est rattaché au désordre qu'il corrige (référence `B-11`) | ✅ **CONFORME** | Tableau § 4 (`D1` à `D9` + Plancher B + Portiques Ouest) |
| 4 | Chaque plan porte le filigrane « PRINCIPE — NE PAS EXÉCUTER » et un indice P | ✅ **CONFORME** | Bandeau rouge + cartouche `PRINCIPE — NE PAS EXECUTER — Indice P` sur les 3 planches + 2 coupes A-A et B-B |
| 5 | Aucun calcul d'exécution fin n'a été produit dans `B-20` | ✅ **CONFORME** | Ratios et formules d'ordre de grandeur uniquement ; calculs EC2/EC3/EC5 renvoyés à `B-42..B-50` |
| 6 | Aucune protection au feu n'a été dimensionnée | ✅ **CONFORME** | Mention générique seule (§ 1.2 & Planche 1) |
| 7 | La liste des points à faire valider est complète (sections, hypothèses, choix constructifs) | ✅ **CONFORME** | Section 5 (7 points dont 4 matérialisés en nuages `D-19` sur les plans) |

**Verdict de la brique `B-20` (Indice B) : ✅ CONFORME.**

---

## SECTION 9 — POINT DE CONTRÔLE HUMAIN

Vous disposez désormais, **sur votre Google Drive (`LIVRABLES_ARENA`) et sans aucune cloison ni isolation sur les fonds de plans**, de l'intégralité du support de synthèse et d'implantation :

1. **Implantation en plan PH RDC (`Planche 1`)** : confirmez-vous l'implantation des frangements (`F1a, F1b, F1c, F2, F3, F4`), renforts (`R1, R2-N/S, R3-N/S, Stab1`), poteaux (`P1-N, P1-S, P2, P3`), jambage (`J1`) et sommiers (`S1, S2`) — ou souhaitez-vous déplacer/modifier certains repères ?
2. **Implantation des fondations « PLS » (`Planche 2` & `B-40 Ind. E`)** :
   - Confirmez-vous la **semelle isolée `SF1` (`60×60×30 BA mini`)** sous **`P2`** ?
   - Pour les **4 zones en nuage `D-19` (`P1-N`, `P1-S`, `P3`, `J1`)**, maintenez-vous le principe d'appui sur soubassement moellons vérifié à l'ouverture des fouilles (avec rattrapage gros béton `D-09`), ou souhaitez-vous que nous prévoyions **dès maintenant des semelles BA `60×60×30` systématiques** sous `P1-N`, `P1-S` et/ou `P3` ?
3. **Suite de la chaîne CARNAC** : à votre **« GO »**, j'engage la suite des briques de calcul d'exécution (**`B-21 / B-22`** puis **`B-42` Poteaux/Jambages BA** et **`B-45` Profilés métalliques — vérification prioritaire de la flèche de `F3` et `R2` en `HEB 160`**).
