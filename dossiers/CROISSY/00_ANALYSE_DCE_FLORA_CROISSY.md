# Analyse du dossier CROISSY — Pavillon FLORA (EHPAD La Roseraie)

**Note de revue documentaire et technique — phase préparation d'étude d'exécution**
Rédacteur : ingénieur structure (revue de dossier) · Date : 19/10/2026 · Version : A

> **Objet** : analyse du dossier Google Drive « CROISSY » (5 pièces, DCE indice C) en vue de la
> préparation des études d'exécution gros œuvre / structure.
> **Nature** : note de revue de dossier. Elle ne vaut ni validation de la conception, ni note de calcul,
> ni visa. Toute reprise en sous-œuvre et tout renfort doivent être justifiés par une note de calcul
> signée et validés par le BET et le bureau de contrôle.

---

## 1. Synthèse pour décision — 12 messages clés

| # | Message | Criticité |
|---|---|---|
| 1 | Il s'agit d'une **réhabilitation lourde d'un pavillon ancien** (RDC + étage + combles, structure bois/brique/acier), pas d'une construction neuve. Le DCE structure est un **dossier de renforcement**, pas un dossier d'exécution. | Structurant |
| 2 | **Le programme a changé entre le diagnostic et le DCE** : DIAG (24/03/2025) = réhabilitation EHPAD, exploitation retenue **150 daN/m²** ; DCE (16/03/2026) = **cabinet paramédical**, exploitation **250 daN/m²** (+67 %). Les vérifications du DIAG ne couvrent donc plus le programme contractualisé. | **Bloquant pour la conception** |
| 3 | Le DIAG conclut déjà, à 150 daN/m², à une **poutre bois 20×15 non justifiée** (flèche 72,8 mm pour 10,4 mm admis, contrainte +200 %) et à des **solives IPE160 non justifiées au déversement**. À 250 daN/m² ces éléments sont hors service : les renforts sont **obligatoires**, pas optionnels. | **Majeur** |
| 4 | Le renforcement repose sur un **système mixte acier/bois/béton** (F1 2×HEA200, R1 2×UPE200, R2 HEB160, R3 UPE200, P1 tube 140, S1/S2 sommiers BA, J1 jambages). La **compatibilité des assemblages et le phasage d'étaiement** constituent le vrai risque d'exécution. | **Majeur** |
| 5 | **Aucun plan de fondations du pavillon Flora n'existe dans le DCE indice C** : le seul folio de fondations concerne la **passerelle « château »**. Or le CCTP prévoit semelles filantes, bêches, soubassements et arase étanche sur semelle existante. | **Pièce manquante** |
| 6 | Le **système de fondations de l'existant est inconnu** (probablement semelles filantes maçonnées / soubassements pierre). Le CCTP réutilise une « semelle filante existante » sans qu'aucune reconnaissance ne l'atteste → **fouilles de reconnaissance obligatoires** avant exécution. | **Majeur** |
| 7 | Géotechnique : mission **G2 AVP** GEOEXPERTS n° 25.13646/ES/GIF du 22/01/2026, contrainte admissible **0,3 MPa ELS**, fondations **ancrées ≥ 0,50 m dans les alluvions anciennes**, dallage sur **couche de forme 40 cm**. Une mission **G2 PRO/G4** doit être commandée. | Majeur |
| 8 | **Incohérence de classe d'exposition** : le DCE affiche **XA4**, classe qui **n'existe pas** dans la NF EN 206/CN (XA1 à XA3). Le tableau des bétons laisse par ailleurs vides la classe structurale, l'enrobage et les exigences CF/SF. | Majeur |
| 9 | **Trois adresses différentes** circulent pour le même ouvrage (2 rue Alfred Dormeuil / 11 rue Paul Demange / « Croissy-sur-Seine » sans adresse). À régler : DCE, autorisations, DT/DICT, récolement. | Moyen |
| 10 | Le CCTP lot 01 est titré « **Flora & Gardien** » mais son sommaire ne contient **aucun chapitre « Gardien »** : périmètre du lot à clarifier. | Moyen |
| 11 | **L'enveloppe n'est pas traitée** : 9 désordres relevés dont infiltrations en toiture, descentes EP et étanchéité de salle d'eau. Tant que l'eau entre, **tout renfort bois ou acier est un cautère sur une jambe de bois** (pourrissement, corrosion). L'ordre logique est : enveloppe → structure. | **Majeur** |
| 12 | Le dossier est **exploitable à ~80 %** : le PDF des pièces graphiques (5,8 Mo) et le DXF (4,4 Mo) n'ont pas pu être lus par le connecteur. Le **plan de coffrage** reste à produire. | Méthode |

---

## 2. Fiche d'identité de l'opération

| Rubrique | Donnée |
|---|---|
| Opération | EHPAD La Roseraie — Pavillon **FLORA** (+ « Gardien » au CCTP) |
| Nature | Réhabilitation lourde / restructuration intérieure d'un pavillon ancien |
| Programme (DCE ind. C) | Aménagement d'un **cabinet paramédical** dans le pavillon Flora |
| Adresse | 78290 **Croissy-sur-Seine** — voir § 8.2 (adresses divergentes) |
| Maître d'ouvrage | **UNIVI** — 54 bd de la Liberté, 59000 Lille |
| Architecte | **TRUELLE Architectes** — 24 av. Vladimir Ilitch Lénine, 94110 Arcueil |
| BET Structure | **EVEN STRUCTURES** — 5 rue des Petites Maulévries, 49007 Angers |
| BET Fluides | AB Ingénierie — 49124 Saint-Barthélemy-d'Anjou |
| Économiste | EICP — 75012 Paris |
| N° affaire structure | **24.09.356E** (EVEN) / **014-2024-08** (EICP) |
| Stade / indice | DIAG (24/03/2025) → DCE ind. **A** 15/10/2025 → **B** 09/02/2026 → **C** 16/03/2026 |
| CCTP lot 01 | V1 — stade **PRO** — 13/03/2026 — 38 pages |

### 2.1 Chaîne d'indices (traçabilité)

| Indice | Date | Objet de la modification |
|---|---|---|
| – | 24/03/2025 | Diagnostic structurel — diffusion initiale (1re diffusion) |
| A | 15/10/2025 | 1re diffusion DCE |
| B | 09/02/2026 | MAJ zone dallage + réception **G2 AVP** |
| C | 16/03/2026 | Modification aménagement / **décalage d'ouverture** |

> **Point de méthode** : l'indice C modifie l'aménagement et la position d'une ouverture. Toute
> étude d'exécution doit être indexée sur cet indice ; les indices A et B sont à archiver.

---

## 3. Registre documentaire

| Réf. | Pièce | Type | Indice / date | Taille | Exploitation |
|---|---|---|---|---|---|
| D1 | `CCTP LOT 01 GO – STRUCTURES – DÉPLOMBAGE – INSTALLATION DE CHANTIER.pdf` | CCTP | V1 PRO — 13/03/2026 | 1,15 Mo | Texte extrait (partiel : § 01.2.1.7) |
| D2 | `24.09.356E DCE indice C FLORA 16.03.2026.pdf` | Plans structure (4 folios + cartouche de données d'études) | **C** — 16/03/2026 | 546 ko | Texte extrait (intégral) |
| D3 | `208_FLORA_DIAG structure.pdf` | Diagnostic structurel (18 p.) | – — 24/03/2025 | 1,36 Mo | Texte extrait (intégral) |
| D4 | `208_FLORA_DCE_Pièces graphiques_IndC.pdf` | Pièces graphiques architecte | C | 5,80 Mo | **Non lu** (extraction en échec) |
| D5 | `208_FLORA_Plans_DCE_IndC.dxf` | Plans CAO | C | 4,40 Mo | **Non lu** (format non supporté par le connecteur) |

### 3.1 Contenu du jeu de plans structure (D2)

| Folio | Désignation | Échelle | Observation |
|---|---|---|---|
| 01 | Vue en plan **PH RDC — Charpente** | 1/50 – 1/20 | Plan de renforcement du plancher haut RDC |
| 02 | Vue en plan **Charpente** | – | Repérage F / R / P / S / J / Stab |
| 03 | Vue en plan **PB RDC** (plancher bas) | – | Dallage / fondations ponctuelles |
| B04 | **Fondations passerelle « château »** | – | **Seul** folio de fondations du DCE |

> **Constat** : 4 folios pour un lot gros œuvre complet, c'est très peu. Il manque, a minima,
> un plan de fondations du pavillon, les coupes/détails d'assemblage et les plans de coffrage.

---

## 4. Description de l'existant (source D3 — diagnostic EVEN du 24/03/2025)

| Élément | Description |
|---|---|
| Typologie | Ancien bâtiment d'habitation à **un étage + combles**, RDC occupé par le service technique de l'EHPAD |
| Fondations | **Inconnues** — probablement soubassements maçonnés type **semelle filante**, pierre dure en bon état apparent |
| Élévations | **Poteaux bois**, **briques**, maçonnerie ; partie haute des façades en brique sur enduit peint |
| Plancher haut RDC | Solives et poutres **bois massif** + profilés **métalliques** + dalles BA (mixte) |
| Charpente | Fermes bois, chevrons, potelets ; assemblages « rotulés » |

### 4.1 Constitution des planchers (sondages destructifs)

**Plancher A — bois**
- Solives **8×18** @ **0,50 m**, portée ≈ 2,77 m, bois massif **C18** (12 % d'humidité, hypothèse de calcul)
- Poutre **20×15** (b = 200, h = 150 mm) — portée déduite ≈ 4,3 m
- Complexe : lambourde + parquet (20 daN/m²) + lattis-plâtre (20 daN/m²)

**Plancher B — mixte acier/maçonnerie**
- Solives **IPE 160** @ **0,72 m**, poutre **IPE 330**
- Hourdis **briques creuses 7 cm** (900 daN/m³) + **polystyrène 8 cm** + **chape béton 10 cm**

### 4.2 Résultats des vérifications du DIAG

| Élément | Vérification | Résultat | Verdict |
|---|---|---|---|
| Solive 8×18 (A) | Flèche (EC5, 150 daN/m²) | w = 7,7 mm > wlim = 7,0 mm | **Non justifiée** (+10 %) |
| Poutre 20×15 (A) | Flèche (EC5, 150 daN/m²) | w = **72,8 mm** > wlim = 10,4 mm | **Non justifiée** (≈ 7×) |
| Poutre 20×15 (A) | Contrainte | **+200 %** | **Non justifiée** |
| Solive IPE 160 (B) | Déversement (EC3, ROBOT) | instable | **Non justifiée** |
| Solive IPE 160 (B) | Flèche | OK | Justifiée |
| Poutre IPE 330 (B) | Flèche + contrainte | OK | Justifiée |
| Poutre IPE 330 (B) | Réaction d'appui centrale | **6,9 t** | À vérifier sur l'appui existant |
| Portique Ouest | Linteau | flèche + contrainte hors limites | **Non justifié** |
| Pieds de poteaux | Contrainte | 3,30 à 3,66 MPa | **À la limite** de l'admissible |

> **Lecture d'ingénieur** : une poutre de 150 mm de hauteur sur ~4,3 m de portée présente un
> élancement L/h ≈ 29. Ce n'est pas un défaut de calcul, c'est un **sous-dimensionnement
> structurel d'origine**, aggravé par le fluage et probablement par les désordres d'humidité.
> La flèche calculée (72,8 mm) est cohérente avec le désordre 3 relevé sur site (« flèche visible
> à l'œil nu »). Le renforcement par moisage acier (R1/R2/R3) est donc la bonne réponse.

### 4.3 Les 9 désordres relevés (visite du 20/02/2025)

| N° | Désordre | Localisation | Préjudice retenu |
|---|---|---|---|
| 1 | Déformation de 2 linteaux (non porteurs) | Façade Ouest | Faible |
| 2 | Fissuration à mi-niveau des façades (jonction bois/brique) | Façades Est | Faible (esthétique) → risque d'infiltration |
| 3 | Flèche excessive de la poutre maîtresse | Intérieur Est | **Structurel** |
| 4 | Humidité / mousses au droit des descentes EP | Façades | **Moyen → structurel à terme** |
| 5 | Fissures en plafond du plancher haut étage (reprend la charpente) | Intérieur | À surveiller |
| 6 | Ferme de charpente altérée par l'humidité | Combles | **Structurel** |
| 7 | Traces d'humidité intérieures (salle d'eau, menuiseries) | Intérieur | Faible → moyen |
| 8 | Chevrons très altérés, potelets théoriquement instables | Charpente Est | **Structurel** |
| 9 | Doublage lattis-plâtre fissuré, chevrons visibles | Intérieur | Flèche + infiltrations |

---

## 5. Renforcements projetés (source D2 — DCE ind. C)

### 5.1 Légende et repérage

| Repère | Désignation | Fonction |
|---|---|---|
| **F** | Frangement de mur | Ouverture dans maçonnerie existante |
| **F1** | **2× HEA 200** | Renfort du **linteau bois existant** |
| **F2** | **HEB 200** | Frangement / linteau métallique |
| **F3** | **HEB 160** | Frangement / linteau métallique |
| **F4** | **IPE 200** | Frangement / linteau métallique |
| **P** | Poteaux | Appuis nouveaux |
| **P1** | **Tube carré 140×140** | Poteau de renfort (portique Ouest) |
| **P2** | **15×25 BA** | Poteau béton armé |
| **P3** | **50×40 BA** | Poteau / massif béton armé |
| **R** | Renfort | Renforcement de poutraison |
| **R1** | **2× UPE 200** | Moisage de la poutre bois 20×15 |
| **R2** | **HEB 160** | Renfort de poutre |
| **R3** | **UPE 200** | Renfort de poutre |
| **S** | Sommier | Répartition sur appui existant |
| **S1** | **20×40×20 ht BA** | Sommier sous poteau |
| **S2** | **20 × ep. mur × 20 ht BA** | Sommier filant en pied de mur |
| **J** | Jambage | Renfort de baie |
| **J1** | **24 × ep. maçonnerie BA** | Jambage de baie |
| **Stab** | Élément de stabilité | Anti-déversement |
| **Stab1** | **Entretoise anti-dévers IPE** | Incorporée dans les **hourdis brique** (saignée ponctuelle) |

### 5.2 Adéquation renforts ↔ désordres

| Désordre | Réponse DCE | Cohérence |
|---|---|---|
| 1 — Linteaux Ouest déformés | F1 (2×HEA200) en renfort du linteau bois + éventuel P1 | ✅ cohérent |
| 3 — Flèche poutre maîtresse | R1 (2×UPE200), R2 (HEB160), R3 (UPE200) | ✅ cohérent |
| Déversement IPE 160 | Stab1 (entretoises + saignée hourdis) | ✅ cohérent |
| Réactions 6,9 t / pieds de poteaux | S1 / S2 sommiers BA | ✅ cohérent |
| 2 — Fissuration bois/brique | Bande solin / rejointoiement (hors lot structure) | ⚠️ **à intégrer au lot façades** |
| 4, 7, 9 — Humidité | **Non traité par le lot structure** | ❌ **à traiter AVANT renforts** |
| 6, 8 — Charpente altérée | **Non traité par le DCE ind. C** | ❌ **manque au dossier** |
| 5 — Fissures plafond étage | Non traité | ⚠️ à investiguer |

---

## 6. Fondations, dallage et géotechnique

### 6.1 Données de sol (cartouche D2)

| Paramètre | Valeur au DCE | Commentaire |
|---|---|---|
| Étude géotechnique | **GEOEXPERTS** — rapport **n° 25.13646/ES/GIF** du **22/01/2026** | Mission **G2 AVP** (mentionnée en révision B) |
| Contrainte admissible | **0,3 MPa (3 bars) ELS** | Valeur de dimensionnement des semelles |
| Ancrage | **≥ 0,50 m dans les alluvions anciennes** | Le bon sol n'est pas en surface |
| Dallage | Couche de forme **40 cm** selon prescriptions GEOEXPERTS | À confirmer par le rapport complet |
| Agressivité | **XA4** + géotextile anti-contaminant sous couche de forme | Voir § 8.4 |

### 6.2 Prescriptions d'exécution issues des plans (D2, folio B04)

> - « Les altimétries des semelles peuvent varier sur une même pièce. »
> - « Certaines semelles sont au contact du dallage à créer. Dans ce cas il conviendra de couler le
>   dallage à même la semelle et de **ne pas compacter sur ce débord**, au risque de déstabiliser
>   les fondations. »
> - « De manière générale le compactage devra être réalisé avec une **distance de sécurité le long
>   des soubassements**. »
> - « Se référer au rapport d'étude de sol **G2 AVP** pour les reconnaissances de fondations. »

Ces trois points sont **structurants pour la méthode d'exécution** : ils imposent un phasage
dallage / compactage / fondations et interdisent le compactage à l'aplomb des semelles.

### 6.3 Prescriptions du CCTP lot 01 (§ 01.2.1.6 et 01.2.1.7)

| Article | Ouvrage | Prescription |
|---|---|---|
| 01.2.1.6.1 | Fouilles en rigoles | Pour fondations |
| 01.2.1.6.2 | Remblais de fondations | — |
| 01.2.1.6.3 | Déblais excédentaires | Évacuation |
| 01.2.1.7.1 | **Gros béton** | Rattrapage du niveau de bon sol **selon nécessité**, sous l'ensemble des ouvrages de fondation |
| 01.2.1.7.2 | **Semelles filantes BA** | Section et armatures **suivant étude BET**, coulage à pleines fouilles sur béton de propreté, armatures de liaisonnement |
| 01.2.1.7.3 | **Bêches hydrauliques BA** | Coulage à pleines fouilles |
| 01.2.1.7.4 | Ossature BA en fondations | Départs de poteaux infrastructure/superstructure |
| 01.2.1.7.5 | **Soubassements agglomérés** | Blocs pleins/semi-pleins, mortier **hydrofugé** |
| 01.2.1.7.6 | **Arase étanche** | Feutre bitumeux entre 2 chapes dosées 600 kg, 2 cm — **sur semelle filante existante** |
| 01.2.1.7.7 | Protection des soubassements | Membrane d'étanchéité |

> **Incohérence relevée** : le CCTP décrit des **semelles filantes neuves** (§ 01.2.1.7.2) et une
> **arase étanche sur semelle filante existante** (§ 01.2.1.7.6). Le DIAG indique que le système de
> fondations est **inconnu**. La coexistence « existant + neuf » n'est pas décrite par un plan.

### 6.4 Dallage (CCTP § 01.2.1.9)

Le CCTP prévoit : géotextile anti-contaminant, **protection anti-termites** (01.2.1.9.2),
nivellement/compactage de plate-forme, remblai complémentaire, sablage d'égalisation,
**isolation sous dallage**, **film polyane**, **essais à la plaque**, **dallage BA**, empochements,
réservations.

> **Point de contrôle** : les critères de réception de plate-forme (EV2, EV2/EV1) et l'épaisseur /
> le ferraillage du dallage ne figurent **ni dans le CCTP ni dans le DCE ind. C**. À réclamer.

---

## 7. Hypothèses d'études, matériaux et actions (cartouche D2)

### 7.1 Bétons et aciers

| Donnée | Valeur au DCE | Commentaire |
|---|---|---|
| Béton de structure | **C25/30** | Sauf indications contraires |
| Gros béton | **C16/20** | Propreté / rattrapage de fond de fouille |
| Aciers HA | **S500** (fyk = 500 MPa) | — |
| Aciers lisses | **S220** | — |
| Ouverture de fissure | **w = 0,40 mm** | À confirmer (valeur du cartouche partiellement lisible) |
| Enrobage | **c = 30 mm** | Classe structurale annoncée **S4** — voir § 8.4 |
| Classes d'exposition | **XC1** voiles int. · **XC2** BA au contact de la terre · **XF1** voiles ext. · **XC4** contact de l'eau | + **XA4** pour l'agressivité des sols |
| Acier de charpente | **S275** | Profilés de renfort |

### 7.2 Actions

| Action | Valeur | Source |
|---|---|---|
| Charges permanentes — plancher métallique | **350 daN/m²** | Cartouche D2 |
| Charges permanentes — plancher bois | **100 daN/m²** | Cartouche D2 |
| Exploitation — cabinet paramédical / bureaux | **250 daN/m²** | Cartouche D2 (cat. B, EC1-1-1) |
| Neige | Zone **A1**, altitude < 200 m, **sk = 45 daN/m²**, **sAd = 24 daN/m²** | EC1-1-3 + AN |
| Vent | **Zone 2**, **vb = 24 m/s**, cd = 1, terrain **cat. III** | EC1-1-4 + AN |
| Séisme | **Zone 1**, catégorie d'importance **II**, ag ≈ **0,4 m/s²** | EC8 + AN (champs partiellement lisibles) |
| Incendie | Stabilité au feu obtenue par **encoffrement** ; CF/SF non renseignés | Cartouche D2 |

### 7.3 Contrôle de cohérence des charges — plancher B

| Couche | Calcul | Charge |
|---|---|---|
| Hourdis briques 7 cm | 900 × 0,07 | 63,0 daN/m² |
| Polystyrène 8 cm | 30 × 0,08 | 2,4 daN/m² |
| Chape béton 10 cm | 2 500 × 0,10 | 250,0 daN/m² |
| Solives IPE 160 @ 0,72 | 15,49 / 0,72 | 21,5 daN/m² |
| **Total** | | **≈ 337 daN/m²** |

→ L'hypothèse de **350 daN/m²** du DCE est **cohérente et légèrement sécuritaire** (+4 %). ✅

### 7.4 Contrôle de cohérence — plancher A

| Couche | Charge |
|---|---|
| Solive 8×18 @ 0,50 | 10,9 daN/m² |
| Lambourde + parquet | 20,0 daN/m² |
| Lattis-plâtre | 20,0 daN/m² |
| **Total** | **≈ 51 daN/m²** |

→ L'hypothèse de **100 daN/m²** est **très sécuritaire** (+96 %) ; elle couvre vraisemblablement
les cloisons et le ragréage futurs. ✅ — à confirmer par la note de calcul.

---

## 8. Écarts, incohérences et ambiguïtés — à lever avant exécution

### 8.1 Changement de programme entre DIAG et DCE — **point n° 1**

| | DIAG — 24/03/2025 | DCE — 16/03/2026 |
|---|---|---|
| Programme | Réhabilitation EHPAD | **Cabinet paramédical** |
| Exploitation | **150 daN/m²** (logement) | **250 daN/m²** (bureaux/cabinet) |
| Conclusion plancher A | « renfort des solives non utile si charges fragiles conservées » | Renforts R1/R2/R3 contractualisés |

> **Conséquence directe** : la conclusion « le renfort des solives n'est pas jugé utile » du DIAG
> **ne peut pas être reprise**. Elle reposait sur 150 daN/m² et sur la conservation des charges
> fragiles. Le DCE, lui, retient 250 daN/m² et modifie l'aménagement (ind. C : décalage d'ouverture).
> **Toutes les vérifications de plancher doivent être reprises** à 250 daN/m², avec les cloisons
> réelles et les équipements du cabinet (imagerie, baignoire de balnéothérapie, archives…).
> C'est un **écart de conception**, pas une nuance.

### 8.2 Adresses divergentes

| Document | Adresse |
|---|---|
| DIAG (D3) | **2 rue Alfred Dormeuil**, 78290 Croissy |
| DCE structure (D2) | **11 rue Paul Demange**, 78290 Croissy-sur-Seine |
| CCTP (D1) | « CROISSY SUR SEINE » (sans adresse) |

À trancher avec la MOE : impact sur le DCE, les autorisations, les **DT/DICT**, le récolement.

### 8.3 Périmètre « Flora & Gardien »

Le CCTP lot 01 est titré « **EHPAD La Roseraie — Flora & Gardien** », mais son sommaire ne
comporte que la partie **01.2.1 Flora** (38 pages). Aucun chapitre « Gardien ». Deux hypothèses :
lot limité à Flora, ou omission. **À clarifier avant consultation**, sous peine de litige sur le
périmètre.

### 8.4 Classes d'exposition et durabilité — **point n° 2**

| Anomalie | Analyse |
|---|---|
| **XA4** | La NF EN 206/CN ne définit que **XA1, XA2 et XA3**. « XA4 » n'est pas une classe d'exposition normative. Soit il s'agit d'une **coquille pour XA3**, soit d'une référence au rapport géotechnique mal retranscrite. Dans les deux cas, **à faire confirmer par le BET** avant commande béton. |
| **C16/20 en sol XA** | Un gros béton non armé en ambiance XA doit malgré tout respecter les prescriptions ciment/E-C. C16/20 est faible pour un sol agressif. |
| **c = 30 mm avec XC4 / S4** | Pour XC4 et S4, cmin,dur = 30 mm ; avec Δcdev = 10 mm on obtient **cnom = 40 mm**. Un cnom de 30 mm suppose Δcdev = 0 (maîtrise de la qualité renforcée). **À trancher explicitement.** |
| **XF1** | Voiles extérieurs : XF1 seul est faible pour un ouvrage enterré/semi-enterré en Île-de-France ; vérifier XF2/XF3 selon exposition réelle. |
| Champs vides | Classe structurale, enrobage, CF/SF, catégorie de bâtiment, classe de sol sismique, altitude : **non renseignés** dans le cartouche. |

### 8.5 Sigle « RSO »

Le cartouche indique : « **RSO** ancrées d'au moins 0,5 m dans les alluvions anciennes, capacité
3 bars ELS ». Le sigle n'est pas explicité dans les pièces analysées et ne correspond à aucune
notation normalisée courante. **À faire préciser par EVEN STRUCTURES** : s'agit-il de semelles,
de pieux, de micro-pieux, ou d'un type de fondation propre au rapport GEOEXPERTS ?

### 8.6 Pièces manquantes (liste à réclamer)

| # | Pièce | Pourquoi |
|---|---|---|
| 1 | **Rapport GEOEXPERTS n° 25.13646/ES/GIF complet** + annexes (coupes, sondages, portance, agressivité, sulfates, nappe) | Base du dimensionnement des fondations |
| 2 | **Mission G2 PRO + G4** | Supervision géotechnique en phase travaux |
| 3 | **Plan de fondations du pavillon Flora** (existant + projeté) | Aucun au DCE ind. C |
| 4 | **Plans de coffrage / ferraillage** des ouvrages BA (S1, S2, P2, P3, J1) | Nécessaires à l'exécution |
| 5 | **Note de calcul EVEN ind. C** (hypothèses, descente de charges, vérification des renforts à 250 daN/m²) | Vérifier la reprise du programme |
| 6 | **Détails d'assemblage** acier/bois/béton (moisage UPE, appuis, boulonnage, boîtes d'appui) | Risque principal d'exécution |
| 7 | **Plans architecte ind. C** (D4) + plan de démolition | Lisible seulement en local |
| 8 | **Diagnostic sanitaire des bois** (insectes, champignons) + rapport parasitaire | Renforts sur bois altéré = non-sens |
| 9 | **Rapports amiante et plomb** cités au CCTP (§ 01.2.1.2 et 01.2.1.3) | Préalable au déplombage/désamiantage |
| 10 | **Note sécurité incendie** + exigences CF/SF des profilés et encoffrements | Cartouche vide |
| 11 | **Étude de faisabilité / note de synthèse** sur la réutilisation des fondations existantes | Arase étanche sur semelle existante sans reconnaissance |

---

## 9. Points de vigilance pour l'étude d'exécution

### 9.1 Structure et renforts

1. **Étaiement avant toute dépose.** Le moisage d'une poutre bois 20×15 par 2×UPE200 suppose une
   **décharge complète** de la poutre. La note d'étaiement doit être produite par l'entreprise et
   visée par le BET : vérification des appuis d'étai (dallage existant ? portance ?), séquence de
   mise en charge, dépose progressive.
2. **Assemblage acier/bois.** Boulons traversants avec diamètre ≥ 12 mm, entraxe et distances aux
   bords selon EC5 ; éviter le contact direct acier/bois en ambiance humide (interposition,
   traitement). Vérifier le **cisaillement aux abouts** de la poutre bois au droit des appuis.
3. **Entretoises anti-dévers Stab1.** Le DCE précise qu'elles sont **incorporées dans l'épaisseur
   des hourdis brique**, avec **saignée ponctuelle**. Prévoir la méthode de saignée (carottage /
   disqueuse avec aspiration) et la reconstitution du hourdis.
4. **Sommiers S1/S2 sous poteaux existants.** Reprise en sous-œuvre : calage, purge du soubassement
   en pierre, **mortier de calage sans retrait**, contrôle du contact. Le DIAG note que les
   contraintes en pied sont **à la limite** : toute augmentation de charge impose le sommier.
5. **Réaction de 6,9 t** sur l'appui central de l'IPE330 : vérifier l'élément porteur existant
   (poteau bois ? maçonnerie ?) et la diffusion dans le soubassement.
6. **Compatibilité des matériaux** : S275 avec bois C18 et béton C25/30 — prévoir les
   **interfaces** (platine, tiges, scellement chimique) et les tolérances de pose.
7. **Flèche résiduelle.** La poutre présente déjà une flèche de fait (désordre 3). Le renfort ne la
   **redressera pas** : il faut définir avec la MOE le niveau de reprise (contre-flèche par vérins ?
   acceptation de la flèche résiduelle ?) et la **compatibilité avec les cloisons et les sols**.
8. **Feu.** Stabilité au feu « obtenue par encoffrement » : les profilés de renfort en sous-face de
   plancher bois doivent être encoffrés. Vérifier l'épaisseur et la compatibilité avec les hauteurs
   libres (souvent le point dur en réhabilitation).

### 9.2 Enveloppe et humidité — **préalable indispensable**

Les désordres 4, 6, 7, 8 et 9 sont tous liés à l'eau. Renforcer une poutre dont les abouts sont
pourris, ou poser un UPE sur un chevron altéré, c'est **transférer la charge sur un élément qui
n'existe plus**. L'ordre d'intervention doit être :

1. **Mise hors d'eau / hors d'air** (couverture, zinguerie, descentes EP, étanchéité salle d'eau)
2. **Purge et traitement** des bois altérés, remplacement des éléments non portants
3. **Renforts structurels**
4. **Second œuvre**

À inscrire noir sur blanc dans le phasage contractuel, sinon la réception des supports sera
impossible.

### 9.3 Fondations et dallage

1. **Fouilles de reconnaissance obligatoires** avant métré définitif : nature, largeur, profondeur
   et état des semelles existantes ; recherche de fosses, puisards, anciens réseaux.
2. **Ancrage ≥ 0,50 m dans les alluvions anciennes** : le fond de fouille est donc **profond**.
   Prévoir blindage, épuisement, gestion des terres.
3. **Ne pas compacter au droit des semelles** (prescription D2) : à traduire en consigne de
   chantier et en plan de compactage.
4. **Dallage à même la semelle** sur les zones de contact : à repérer sur plan avant coulage.
5. **Couche de forme 40 cm** : essais à la plaque (EV2 et EV2/EV1) — critères à faire préciser.
6. **Géotextile anti-contaminant** sous couche de forme (sol XA).
7. **Traitement anti-termites** du CCTP : vérifier l'arrêté préfectoral du 78 et la pertinence de
   la prescription.

### 9.4 Qualité béton et contrôle

- **XA** : type de ciment (CEM III/A ou B), E/C maximal, dosage minimal, teneur en C3A.
  À faire préciser par le BET / le fournisseur béton.
- **Essais** : affaissement/étalement, air occlus, éprouvettes 7-28 j, conformité EN 206.
- **Enrobage** : cales certifiées, contrôle avant coulage, procès-verbal.
- **Fissuration** : w ≤ 0,4 mm — si la valeur est confirmée, elle est sévère pour des ouvrages
  enterrés ; à recouper avec la classe XC4.

---

## 10. Méthodologie proposée pour la suite (études d'exécution)

| Phase | Contenu | Livrable |
|---|---|---|
| **P0** | Revue de dossier (la présente note) + registre + liste des pièces manquantes | Note de revue ✅ |
| **P1** | Reconnaissances : fouilles de semelles, relevé géométrique (scan 3D ou relevé manuel), inspection sanitaire des bois, sondages complémentaires | Rapport de reconnaissance |
| **P2** | Note d'hypothèses + descente de charges actualisée (250 daN/m², EC1, neige A1, vent 2/III, séisme zone 1) | Note d'hypothèses |
| **P3** | Plans d'exécution : repérage des renforts, plans de coffrage BA (S1, S2, P2, P3, J1), plan de fondations, détails types d'assemblage | Dossier de plans |
| **P4** | Phasage + note d'étaiement + plan de contrôle (points d'arrêt) | Note de phasage |
| **P5** | Quantitatifs (acier, béton, maçonnerie, bois, étaiement) et planning | Métrés + planning |
| **P6** | Suivi d'exécution : PA/PC, réception des fouilles, contrôle des flèches, DOE | Dossier de suivi |

### 10.1 Ce que l'outil `AUTOCAD-VISION` / `StructAI` peut apporter — et ce qu'il ne peut pas

Le dépôt de ce projet est une application de **conception de bâtiments neufs en béton armé**
(moteur EC2/EC8, génération d'options, plans DXF de fondations/coffrage/ferraillage, quantitatifs).
Sur ce dossier :

| Attendu | Faisable ? | Commentaire |
|---|---|---|
| Extraction des calques / entités du DXF, rendu PNG | ✅ | Nécessite le DXF **en local** (le connecteur Drive ne le lit pas) |
| Plan de coffrage des ouvrages BA neufs (sommeils, poteaux, jambages) | ✅ | Le module `export/dxf_plans.py` produit ce type de folio |
| Quantitatifs béton/acier/coffrage des ouvrages neufs | ✅ | Module `export/quantities.py` |
| Dimensionnement des **renforts acier sur bois existant** | ❌ | Hors périmètre du moteur (BA neuf uniquement) |
| Reprise en sous-œuvre / phasage d'étaiement | ❌ | À produire par calcul manuel + note de phasage |
| Vérification des planchers bois EC5 et acier EC3 existants | ❌ | À produire hors outil |

> Autrement dit : l'outil couvre environ **20 à 25 %** du besoin (les ouvrages béton neufs et leurs
> quantitatifs). Le cœur du dossier — renforcement d'une structure bois/acier ancienne — relève de
> l'ingénierie d'exécution classique.

---

## 11. Limites de la présente analyse

1. Analyse fondée sur l'**extraction texte** des PDF. Les **pièces graphiques (D4, 5,8 Mo)** et le
   **DXF (D5, 4,4 Mo)** n'ont pas pu être lus par le connecteur : aucune lecture visuelle des
   plans n'a été faite. Les positions, longueurs et quantités de renforts **ne sont pas vérifiées**.
2. L'extraction du CCTP est **partielle** (les articles 01.2.1.5.5 « renforcement par profilés
   métalliques » et 01.2.1.9 « dallages » n'ont pas été lus intégralement).
3. Certains champs du cartouche sont **illisibles à l'extraction** (CF/SF, classe de sol, altitude,
   catégorie de bâtiment) : ils sont signalés « à confirmer » et non interprétés.
4. Aucune vérification de calcul n'a été refaite : les valeurs citées sont celles du DIAG et du DCE.
5. La note ne vaut pas **avis technique** au sens de la mission de maîtrise d'œuvre.

---

## 12. Actions immédiates (proposées)

| Priorité | Action | Responsable |
|---|---|---|
| **P1** | Faire confirmer par EVEN STRUCTURES la reprise des vérifications à **250 daN/m²** et la liste des éléments effectivement renforcés | MOE / BET |
| **P1** | Obtenir le **rapport GEOEXPERTS complet** et le **plan de fondations Flora** | MOE / BET |
| **P1** | Trancher **XA4 vs XA3**, l'enrobage (30 ou 40 mm) et le type de ciment | BET |
| **P1** | Programmer les **fouilles de reconnaissance** des semelles existantes | Entreprise / MOE |
| **P2** | Clarifier l'**adresse** et le **périmètre « Gardien »** | MOE |
| **P2** | Traiter l'**enveloppe** avant tout renfort (couverture, EP, étanchéité) | MOE / lot façades |
| **P2** | Diagnostic **sanitaire des bois** | MOE |
| **P3** | Déposer le DXF et les pièces graphiques en local pour lancer l'extraction CAO | Études |

---

*Document produit à partir des 5 pièces du dossier Drive « CROISSY ». Les citations entre
guillemets sont issues des documents sources ; les appréciations sont celles du rédacteur.*
