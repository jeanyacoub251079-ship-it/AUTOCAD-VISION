# B-00 — INVENTAIRE DES PIÈCES ET ÉNONCÉ DE MISSION

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-00** — Inventaire des pièces et énoncé de mission |
| Phase | 0 — Cadrage |
| **Indice du livrable** | **C** (remplace l'indice B du 19/10/2026) |
| Mode d'appel | **COMPLET** (les 4 pièces projet sont désormais lisibles) |
| Code projet `ID-01` | `CROISSY-FLORA` *(proposé — à valider)* |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Date | 19/10/2026 |
| Brique suivante | B-01 (Proposition de MPD) — non engagée |

> **Indice C — 19/10/2026** : la pièce **D5 (DXF indice C)** a été retrouvée dans le Google Drive du dossier Croissy et **inventoriée par script** (`ezdxf` 1.4.5). L'inventaire des indices A et B la déclarait absente : **c'était une erreur de recherche, pas une absence de pièce**. Voir § 0 et `02_ANALYSE/D5_Inventaire_DXF.md`.

**Périmètre** : inventaire, éléments structurants sourcés, contradictions non tranchées, énoncé de mission.
**Interdictions B-00 respectées** : aucun dessin, aucun calcul, aucune conclusion, aucune résolution de contradiction.

---

## 0. ACCUSÉ DE RÉCEPTION DES PIÈCES

| Réf. | Pièce | Format | Indice / date | Étendue | État de lecture |
|---|---|---|---|---|---|
| **C0** | `CARNAC_v2.6_compile.md` | Markdown compilé | v2.6 | 15 973 lignes | **Lu** (maître §0 à §10, dictionnaire, annexes A/D/O, fiche B-00) |
| **D1** | `CCTP LOT 01 GO – STRUCTURES – DÉPLOMBAGE – INSTALLATION DE CHANTIER.pdf` | PDF | V1 — PRO — 13/03/2026 | **38 pages** | **Lu partiellement : 8 pages** (p. 1-5, 15, 26, 27). Les 30 autres pages sont **identifiées au sommaire** mais **non lues** |
| **D2** | `24.09.356E DCE indice C FLORA 16.03.2026.pdf` | PDF vectoriel | **C** — 16/03/2026 | **5 pages** (1 cartouche + 4 folios) | **Lu intégralement** — texte natif + rendu graphique des 5 pages |
| **D3** | `208_FLORA_DIAG structure.pdf` | PDF | – — 24/03/2025 | 18 pages | **Lu intégralement** (couche texte) |
| **D4** | `208_FLORA_DCE_Pièces graphiques_IndC.pdf` | PDF vectoriel | **C** — 13/03/2026 | **29 pages** (A3) | **Lu intégralement en texte** ; **lecture graphique** des pages 6 et 9 |
| **D5** | `208_FLORA_Plans_DCE_IndC.dxf` | **DXF AC1032** | **C** | **4 399 016 o** · 1 582 entités · 31 calques | ✅ **Lu par script** (`ezdxf` 1.4.5). SHA-256 consigné. **Fichier d'architecte** — aucune donnée de structure |

**Déclaration de méthode (traçabilité de la lecture) :**
- Les folios 02, 03 et 04 de D2 portent des annotations en **police vectorielle SHX** (traits, non texte). Elles ont été lues par **rendu image haute résolution**. Une annotation de très petite taille pourrait avoir échappé : ce point est déclaré, non dissimulé.
- D4 pages 1 à 29 : texte natif intégralement extrait. La lecture graphique (géométrie) n'a été faite que sur les pages 6 et 9.
- D1 : **8 pages sur 38**. Aucun élément des 30 pages non lues n'est cité ci-après.
- **Pièce D5 (DXF)** : retrouvée dans le Drive le 19/10/2026, inventoriée par script. L'inventaire des indices A et B la déclarait absente — **erreur de recherche de ma part, corrigée ici** et non dissimulée. Elle ne contient **aucune donnée de structure** (voir `02_ANALYSE/D5_Inventaire_DXF.md`).

---

## 1. INVENTAIRE DES PIÈCES

### 1.1 D2 — Dossier structure EVEN STRUCTURES, 24.09.356E, indice C

| Page | Repère cartouche | Désignation | Indice du folio | Échelle au cartouche | Échelle portée sur le plan | Format |
|---|---|---|---|---|---|---|
| 1 | — | **Sommaire** + cartouche **DONNÉES D'ÉTUDES** | C (16/03/2026) | — | — | A3 |
| 2 | `01 / 01` | **Vue en plan PH RDC — Charpente** (plancher haut rez-de-chaussée) | **C** | 1/50 – 1/20 | **(1/80)** | A3 |
| 3 | `01 / 02` | **Vue en plan Charpente** (combles) | **–** *(aucun indice)* | non portée | **(1/80)** | A3 |
| 4 | `01 / 03` | **Vue en plan PB RDC** (plancher bas — fondations) | **B** | non portée | **(1/80)** | A3 |
| 5 | `01 / 04` | **Fondations passerelle château** | **B** | non portée | **(1/50)** | A3 |

**Historique d'indice porté au cartouche de la page 1 :**

| Indice | Date | Modifications |
|---|---|---|
| – | 15/10/2025 | 1re diffusion |
| B | 09/02/2026 | MAJ zone dallage + réception G2 AVP |
| **C** | **16/03/2026** | **modif aménagement / décalage ouverture** |

### 1.2 D4 — Pièces graphiques architecte, indice C, 13 mars 2026

| Page | Désignation | Échelle | Contenu utile au structure |
|---|---|---|---|
| 1 | Sommaire | — | Index des 29 pages |
| 2 | Plan masse existant | 1/500 | Emprise, mitoyenneté |
| 3 | Plan masse projet | 1/500 | Création de 4 stationnements, accès PMR |
| **4** | **Plans existant** (RDC + R+1 Flora) | 1/100 | **Hauteurs, niveaux Z, menuiseries existantes** |
| **5** | **Plans de démolition** (RDC + R+1) | 1/100 | **Murs démolis, ouvertures, décaissements, modification d'escalier** |
| **6** | **Plans projet** (RDC + R+1) | 1/100 | **Programme des locaux, cloisons** |
| 7 | Plan aménagement extérieur | 1/100 | — |
| 8 | Plans de sols | 1/100 | Revêtements (charges permanentes) |
| **9** | **Plans de repérage des murs** | 1/100 | **Typologie des cloisons : 7 / 10 / 12 cm + gaines** |
| 10 | Plans de plafonds | 1/100 | Hauteurs sous faux plafond (hsfp 2,20 → 2,80 m) |
| 11-18 | Détails 1/50 (box kiné, plateau technique, sanitaires PMR, escalier, bureaux, salle de sport, espaces communs) | 1/50 | Coupes de principe, hauteurs |
| 19-20 | Façades existant | 1/100 | Niveaux de référence (Z 201,00 → 210,32) |
| 21-22 | Façades projet | 1/100 | Remplissage de maçonnerie, reprises d'enduit |
| 23 | Nomenclature des portes | 1/50 | — |
| 24-25 | Nomenclatures menuiseries RDC et R+1 | 1/50 | — |
| 26-27 | Toitures existant et projet | 1/100 | **Reprises d'étanchéité, faîtages, gouttières** |
| 28 | Plan installation chantier | 1/100 | **Bâtiments FLORA et GARDIEN, zones de stockage, accès** |
| 29 | Phase préparatoire Bagatelle | 1/100 | Local repos du personnel, sous-sol |

### 1.3 D1 — CCTP lot 01 : pages lues et pages identifiées

**Pages lues (8) :**

| Page | Objet |
|---|---|
| 1 | Page de garde, intervenants, n° d'affaire 014-2024-08 EICP |
| 2-4 | Sommaire complet (01.1 à 01.2.1.11) |
| 5-9 | Prescriptions techniques, prescriptions complémentaires, limites, implantation |
| 15 | Plan de retrait amiante (procédure) |
| 26 | Terrassements pour fondations (01.2.1.6), gros béton (01.2.1.7.1) |
| 27 | Semelles filantes (01.2.1.7.2), bêches (7.3), ossature BA (7.4), soubassements (7.5), arase étanche (7.6) |

**Sections identifiées au sommaire, non lues (à couvrir en B-10) :**
01.2.1.5.5.1 (renforcement par profilés métalliques) · 01.2.1.7.7 à 7.8 · 01.2.1.8 (assainissement / fourreaux) · **01.2.1.9 (dallages — 7 sous-articles)** · **01.2.1.10 (élévations en superstructure)** · 01.2.1.11 (fin de chantier).

> **Aucune section « charpente bois » n'apparaît au sommaire du CCTP lot 01.** Ce point est repris en contradiction C-13.

---

## 2. ÉLÉMENTS STRUCTURANTS EXTRAITS

Chaque élément porte sa source : **fichier + page + indice**.

### 2.1 Existant — description et porteurs

| Élément | Valeur / description | Source |
|---|---|---|
| Typologie | RDC + **1 étage** + combles ; ancien bâtiment d'habitation | D3 p. 2 ; D4 p. 4 |
| Fondations | « Système **inconnu** (probablement soubassements maçonnés type semelle filante) » | D3 p. 2 |
| Soubassement réel | **Moellons existants**, « pierre dure », bon état apparent, contraintes en pied « à la limite de l'admissible » | D2 folio 03 (annotation) ; D3 p. 17 |
| Semelles existantes | **Existence confirmée** par le DCE : « Reprise en sous-œuvre des semelles existantes par passes alternées de gros béton » | **D2 folio 04** (annotation) |
| Élévations | Poteaux **bois**, **briques**, maçonnerie ; façades mi-brique mi-moellons | D3 p. 2, 4 ; D4 p. 19 (« mur moellons apparents ») |
| Hauteurs | RDC hsp 2,16 → 3,25 m ; R+1 hsp 2,31 → 2,62 m ; H<1,80 en combles | D4 p. 4, 6 |
| Niveaux | RDC Z = 201,03 → 201,26 m ; R+1 Z = 203,59 → 204,43 m ; faîtages Z = 209,19 → 210,32 m ; gouttières Z = 205,41 → 206,57 m | D4 p. 4, 26, 27 |

### 2.2 Planchers (issue du diagnostic)

| Élément | Constitution | Portée / entraxe | Source |
|---|---|---|---|
| **Plancher A (bois)** | Solives **8×18**, bois massif **C18** à 12 % ; poutre **20×15** | entraxe **0,50 m** ; solive ≈ 2,77 m ; poutre ≈ 4,34 m | D3 p. 10, 16 |
| Plancher A — complexe | Lambourde + parquet (20 daN/m²) + lattis-plâtre (20 daN/m²) | — | D3 p. 10 |
| **Plancher B (mixte)** | Solives **IPE 160** @ **0,72 m** ; poutre **IPE 330** | réaction d'appui centrale **6,9 t** (nœud 8) | D3 p. 11, 12 |
| Plancher B — complexe | Hourdis **briques creuses 7 cm** + **polystyrène 8 cm** + **chape béton 10 cm** | — | D3 p. 11 |
| Plancher haut étage | Fissures en plafond ; reprend la charpente par potelets | — | D3 p. 6 (désordre 5) |

### 2.3 Charpente — interventions projetées (D2 folio 02)

> Annotations lues au rendu, en police SHX (non présentes dans la couche texte).

| Élément | Intervention prescrite | Source |
|---|---|---|
| **Panne faitière** | « Panne faitière existante » — conservée | D2 folio 02 |
| **Panne** | « **Panne à ajouter** » (2 occurrences, une par versant) | D2 folio 02 |
| **Demi-ferme** | « **demi ferme à créer en sous-œuvre des existants** » | D2 folio 02 |
| **Ferme traditionnelle** | « **Ferme tradi à renforcer, ajout de contrefiche** » + « ajout de contrefiches » | D2 folio 02 |
| **Poteaux / pannes verticales** | « Pannes existantes » et « **Panne à ajouter** » (verticales, en travée) | D2 folio 02 |
| **Zones non relevées** | « **ZONE NON RELEVEE** » — **2 zones** du plan de charpente | D2 folio 02 |

### 2.4 Renforcements — plancher haut RDC (D2 folio 01)

| Repère | Désignation | Fonction |
|---|---|---|
| **F1** | **2 × HEA 200** | Renfort du linteau bois existant |
| **F2** | **HEB 200** | Frangement de mur |
| **F3** | **HEB 160** | Frangement de mur |
| **F4** | **IPE 200** | Frangement de mur |
| **P1** | **Tube carré 140 × 140** | Poteau, en renfort du linteau bois |
| **P2** | **15 × 25 BA** | Poteau béton armé |
| **P3** | **50 × 40 BA** | Poteau / massif béton armé |
| **R1** | **2 × UPE 200** | Renfort / moisage de poutre |
| **R2** | **HEB 160** | Renfort de poutre |
| **R3** | **UPE 200** | Renfort de poutre |
| **S1** | **20 × 40 × 20 ht BA** | Sommier sous poteau |
| **S2** | **20 × ep. mur × 20 ht BA** | Sommier filant en pied de mur |
| **J1** | **24 × ep. maçonnerie BA** | Jambage de baie |
| **Stab1** | Entretoise anti-déversement IPE | **Incorporée dans le voutain brique** (saignée ponctuelle) |

### 2.5 Fondations et dallage — **D2 folio 03 (PB RDC)**

> **Correction majeure par rapport à l'indice A** : le DCE **comporte bien un plan de fondations du pavillon** (folio 03). L'indice A affirmait le contraire — voir § 3.4.

| Prescription | Libellé exact | Source |
|---|---|---|
| Semelle nouvelle | « **Remplacement poteau et allège pour création d'une semelle BA 25×25 sur soubassement moellons existant** » | D2 folio 03 |
| Vérification | « **vérification du soubassement** » (cote de contrôle sur la façade) | D2 folio 03 |
| Débord existant | « **Débord de semelle, rendu apparent à conserver en l'état** » | D2 folio 03 |
| Arase | « **arase béton à prévoir pour alignement avec dallage** » | D2 folio 03 |
| Bêche | « **Bêche pour réhausse niveau dallage** » | D2 folio 03 |
| Reprise sous-œuvre | « Reprise en sous-œuvre des semelles existantes par **passes alternées de gros béton** » | **D2 folio 04** |
| Fissures | « Reprises des fissures après stabilisation de la **RSO** » | D2 folio 04 |
| Joint | « **Joint de dilatation à traiter** » | D2 folio 04 |
| Dallage | « Certaines semelles sont au contact du dallage à créer : couler le dallage **à même la semelle**, ne pas compacter sur ce débord » | D2 folio 03 (nota) |
| Compactage | « distance de sécurité le long des soubassements » | D2 folio 03 (nota) |
| Altimétries | « Les altimétries des semelles **peuvent varier sur une même pièce** » | D2 folio 03 (nota) |

### 2.6 Sol et géotechnique

| Paramètre | Valeur | Source |
|---|---|---|
| Étude | **GEOEXPERTS** — rapport **n° 25.13646/ES/GIF** du **22/01/2026** ; mission **G2 AVP** | D2 page 1 |
| Contrainte admissible | **0,3 MPa (3 bars) ELS** — « à vérifier à l'ouverture des fouilles » | D2 page 1 |
| Ancrage | « **RSO** ancrées d'au moins **0,5 m dans les Alluvions anciennes**, capacité 3 bars ELS » | D2 page 1 |
| Dallage | « sur fond de forme **40 cm** ep, suivant prescription GEOEXPERTS » | D2 page 1 |
| Agressivité | « **XA4** », géotextile anti-contaminant sous couche de forme | D2 page 1 et folio 03 |

### 2.7 Matériaux (cartouche D2 — valeurs exactes)

| Donnée | Valeur |
|---|---|
| Béton de structure | **C25/30** |
| Gros béton | **C16/20** |
| Ouverture de fissure | **wk = 0,4 mm** |
| Acier HA | **S500B** — f<sub>yk</sub> = 500 MPa |
| Acier lisse | **S220B** — f<sub>yk</sub> = 220 MPa |
| Enrobage nominal | **c<sub>nom</sub> = 30 mm** |
| Classe structurale | **S4** |
| Acier de charpente | **S275** |
| Classes d'exposition | **XC1** (voiles int.) · **XC2** (BA au contact de la terre) · **XF1** (voiles ext.) · **XC4** (contact de l'eau) · **XA4** (sols) |

### 2.8 Actions (cartouche D2 — valeurs exactes)

| Action | Valeur | Remarque |
|---|---|---|
| Permanentes — plancher métallique | **350 daN/m²** | — |
| Permanentes — plancher bois | **100 daN/m²** | — |
| Exploitation — cabinet paramédical / bureaux | **250 daN/m²** | — |
| Neige | Zone **A1**, altitude **< 200 m**, **sk = 45 daN/m²**, **sAd = « – »** | sAd non renseigné |
| Vent | Zone **2**, **vb = 24 m/s**, c<sub>d</sub> = 1 (10°-150° : 0,70), saison 1 (avril-sept. : 0,80), terrain **III** | — |
| Séisme | Zone **1**, catégorie d'importance **II**, **a<sub>gr</sub> = [vide]**, **classe de sol = [vide]** | Deux champs vides |
| Incendie | « Stabilité au feu des ouvrages obtenue par encoffrement » | Section **intégralement vide** |

### 2.9 Programme réel des locaux (D4 pages 6 et 9)

| Niveau | Locaux | Surface |
|---|---|---|
| **RDC** | Plateau technique · Box kiné 1 / 2 / 3 · Bureau 1 / 2 · Sanitaire PMR · Casiers · Entrée · Circulation · Palier | 33,14 m² · 11,20 · 9,60 · 9,15 m² · 16,08 · 12,80 m² · 5,19 m² |
| **R+1** | **Salle de sport** · Salle commune · Vestiaire · Douche · Bureau de consultation 3 / 4 · Dégagement · Attente · Sanitaire | **34,25 m²** · 11,75 · 9,32 · 2,37 m² · 13,26 · 16,50 m² · 5,96 · 8,38 m² |

### 2.10 Travaux de démolition prescrits (D4 page 5)

| Travail | Libellé |
|---|---|
| Murs | « **mur démoli** » ×3 · « **ouverture mur** » · « ouverture porte **agrandie** » |
| Passage | « ouverture pour passage **90 × 210 cm** » |
| Sol | « **dépose des dalles** » · « Sol à décaisser de 6 cm » · « **Sol à recharger de 15 cm** » |
| Rampes | « sol décaissé en pente 10 % h : 16,8 cm » · « pente 6 % h : 3,2 cm » · « sol décaissé de 16,8 cm » |
| Escalier | « **modification escalier** » · « dépose moquette escalier » |

### 2.11 Contraintes de site

| Contrainte | Source |
|---|---|
| Site occupé — installations, moyens de levage, clôtures, compte prorata | D1 p. 10-12 |
| Constat d'huissier préalable | D1 p. 10 |
| Désamiantage et déplombage préalables | D1 p. 14-20 |
| **Bâtiments FLORA et GARDIEN** sur le plan d'installation de chantier | D4 p. 28 |
| Phase préparatoire « Bagatelle » (local repos du personnel, sous-sol) | D4 p. 29 |
| Accès chantier véhicule + accès piéton rue Paul Demange | D4 p. 28 |

---

## 3. CONTRADICTIONS DÉTECTÉES — **NON TRANCHÉES**

### 3.1 Contradictions entre pièces

| N° | Donnée | Pièce A | Pièce B | Nature de l'écart |
|---|---|---|---|---|
| **C-01** | Adresse | **D3 p. 1** : « 2 Rue Alfred Dormeuil, 78290 Croissy » | **D2 p. 1** et **D4 p. 1** : « **11 rue Paul Demange**, 78290 Croissy-sur-Seine » ; **D1** : sans adresse | Deux adresses pour le même pavillon |
| **C-02** | Charge d'exploitation | **D3 p. 10-11** : **150 daN/m²** (logement) | **D2 p. 1** : **250 daN/m²** (cabinet paramédical / bureaux) | **+67 %** sur la même structure |
| **C-03** | Destination | **D3 p. 2** : habitation + service technique EHPAD ; **D1** : « EHPAD La Roseraie – Flora & Gardien » | **D2 p. 1** et **D4** : « Aménagement d'un cabinet paramédical » | Programme divergent |
| **C-04** | Maître d'ouvrage | **D1 p. 1** : **UNIVI**, 54 bd de la Liberté, 59000 Lille | **D4 p. 1** : **SCI GEMS RC – site 208**, 20 rue Jacques Daguerre, 92500 Rueil-Malmaison | Deux entités MOA |
| **C-05** | Renforcement des solives du plancher A | **D3 p. 18** : « le renforcement des solives **n'est pas jugé utile** » (à 150 daN/m²) | **D2 folio 01** : renforts R1 / R2 / R3 contractualisés | Conclusion du diagnostic contredite par la prescription |
| **C-06** | Périmètre du lot | **D1 titre** : « Flora **& Gardien** » | **D1 sommaire** : seule la partie « Flora » est décrite ; **D4 p. 28** montre deux bâtiments (FLORA + GARDIEN) | Bâtiment Gardien annoncé au titre, absent du CCTP |
| **C-07** | Charpente bois | **D2 folio 02** : pannes à ajouter, demi-ferme à créer en sous-œuvre, ferme tradi à renforcer + contrefiches | **D1 sommaire** : **aucune section « charpente bois »** ; seul 01.2.1.5.5.1 « renforcement par profilés métalliques » | Travaux de charpente dessinés mais **non spécifiés au CCTP** |
| **C-08** | Charges permanentes — plancher bois | **D2 p. 1** : **100 daN/m²** | **D4 p. 5 et p. 14** : « **Sol à recharger de 15 cm** » | 15 cm de recharge ≈ 255 à 330 daN/m² selon matériau — **2,5 à 3,3 fois** l'hypothèse |
| **C-09** | Murs démolis / frangements | **D4 p. 5** : 3 murs démolis, 1 ouverture mur, 1 ouverture agrandie, 1 passage 90×210 | **D2 folio 01** : F1 à F4 + J1 — **sans dimensions ni cotes de position** | Correspondance **impossible à établir** entre murs démolis et frangements |
| **C-10** | Usage « salle de sport » | **D4 p. 6 et 17** : **salle de sport 34,25 m²** | **D2 p. 1** : **250 daN/m²** (catégorie bureaux) | Une salle d'activité physique relève d'une catégorie plus sévère ; écart à qualifier |
| **C-11** | Reprise en sous-œuvre | **D2 folio 04** : « reprise en sous-œuvre des semelles existantes par passes alternées de gros béton » | **D1 § 01.2.1.7.2** : semelles filantes BA **neuves**, sections « selon BET » | Pas de plan de coffrage des semelles neuves ; la reprise est dessinée sur le folio de la **passerelle**, pas sur celui du pavillon |
| **C-12** | Échelle | **D2 folio 01 cartouche** : « **1/50 – 1/20** » | **D2 folio 01 plan** : « **(1/80)** » ; folios 02 et 03 également (1/80) | Échelle du cartouche ≠ échelle du dessin |
| **C-13** | Indice des folios | **D2 page 1 (sommaire)** : folio 3 = « **–** » | **D2 folio 03 cartouche** : « **B** » | Indice du sommaire ≠ indice du folio |
| **C-14** | Orientation des façades | **D4 page 1 (sommaire)** : p. 21 « Façades projet **nord est** », p. 22 « **ouest sud** » | **D4 p. 21** : « FACADES PROJET **SUD EST** » ; **p. 22** : « **NORD OUEST** » | Quatre orientations différentes pour deux planches |

### 3.2 Contradictions internes à une pièce

| N° | Donnée | Énoncé A | Énoncé B | Nature |
|---|---|---|---|---|
| **C-15** | Classe d'exposition | « Agressivité des sols **XA4** » (D2 p. 1) | **NP EN 206+A1** citée en référence (D1 § 01.1.1) — n'existe que XA1 à XA3 | Classe non normative |
| **C-16** | Enrobage | « c<sub>nom</sub> = **30 mm** » (D2 p. 1) | Classe structurale **S4** + exposition **XC4** + wk = 0,4 mm (même cartouche) | Cohérence c<sub>nom</sub> / (c<sub>min,dur</sub> + Δc<sub>dev</sub>) non démontrée |
| **C-17** | Sécurité incendie | « Stabilité au feu obtenue par **encoffrement** » (D2 p. 1) | Section SECURITE INCENDIE **intégralement vide** : catégorie du bâtiment, CF, SF, locaux à risques | Prescription sans exigence de référence |
| **C-18** | Séisme | Zone **1**, catégorie **II** (D2 p. 1) | **a<sub>gr</sub> = [vide]**, **classe de sol = [vide]** | Action sismique **non calculable** en l'état |
| **C-19** | Relevé de charpente | Plans de charpente établis (folio 02) | « **ZONE NON RELEVEE** » sur **deux zones** du même folio | Relevé **incomplet**, déclaré par le BET lui-même |
| **C-20** | Sigle « RSO » | « **RSO** ancrées d'au moins 0,5 m dans les alluvions » (D2 p. 1) → désigne un **élément de fondation** | « après **stabilisation de la RSO** » (D2 folio 04) → désigne un **ouvrage** | Acronyme employé dans deux sens incompatibles, non défini |

### 3.3 Points signalés hors périmètre CARNAC (exclusions § 1.3)

| Objet | Source | Traitement |
|---|---|---|
| Désamiantage, déplombage | D1 p. 14-20 | Contrainte de phasage uniquement |
| Curage, démolition, dépose | D1 § 01.2.1.4 et 01.2.1.5 ; **D4 p. 5** | Contrainte de coordination uniquement — **non intégré aux livrables** |
| Protection au feu des renforts | D2 p. 1 | Seule mention autorisée : « une protection au feu adéquate doit être prévue » |
| Fluides, CVC, électricité, VRD | D1 § 01.2.1.8 ; D4 (TGBT, courants forts/faibles) | Réservations et attentes uniquement |
| Études géotechniques G1 à G3 | D2 p. 1 (G2 AVP) | Exploitée, non produite |

### 3.4 Corrections apportées à l'indice A — traçabilité des retraits

| Réf. indice A | Statut | Motif |
|---|---|---|
| « D4 et D5 inexploitables » | **Levé** | **D4 lue intégralement** (29 pages) et **D5 lue par script** (DXF AC1032, 1 582 entités) |
| « Aucun plan de fondations du pavillon » | **RETIRÉ — ERREUR DE L'INDICE A** | Le **folio 03 (PB RDC)** est précisément le plan de fondations du pavillon, avec 6 prescriptions dont la semelle BA 25×25 sur moellons. La lecture de l'indice A n'avait pas décodé les annotations SHX |
| C-08 indice A (« fondations prescrites sans folio ») | **RETIRÉ** | Le folio 03 existe et porte les fondations. Il est remplacé par **C-11** (semelles neuves non coffrées) |
| C-04 indice A (« fondations inconnues vs existantes ») | **RÉVISÉ** | D3 dit « inconnu » ; D2 folio 03 confirme des **moellons** et des **semelles existantes**. Il ne reste que la **dimension et la portance** comme inconnues → devient **C-11** |
| « sAd = 24 daN/m² » | **CORRIGÉ** | 24 est la **vitesse de base du vent** (m/s). **sAd = « – »** (non renseigné) |
| « D2 = 4 folios » | **CORRIGÉ** | **5 pages** : 1 cartouche + 4 folios |
| « échelle 1/50-1/20 » | **CORRIGÉ** | Cartouche 1/50-1/20 mais **plans cotés (1/80)** → **C-12** |
| « Le CCTP prévoit une arase étanche sur semelle existante » | **MAINTENU** | D1 § 01.2.1.7.6, p. 27 — confirmé |

---

## 4. ÉNONCÉ DE MISSION REFORMULÉ (5 lignes)

1. **Objet** — Études d'exécution gros œuvre / structure du pavillon Flora : réhabilitation lourde d'un existant bois / brique / moellons, en vue de l'aménagement d'un cabinet paramédical (kinésithérapie, plateau technique, salle de sport).
2. **Périmètre** — Renforcements repérés R, P, S, J et Stab, frangements F1 à F4, renforcement de charpente (pannes, demi-ferme, contrefiches), fondations et reprises en sous-œuvre, dallage, y compris coordination des réservations.
3. **Livrables** — Plans d'exécution, notes de calcul, nomenclature, notice de synthèse, auto-contrôle, indiçage et journal de clôture.
4. **Exclusions** — Désamiantage, déplombage, curage et démolition, espaces verts, dimensionnement et choix de la protection au feu, fluides / CVC / électricité / VRD, thermique, acoustique, études géotechniques G1 à G3.
5. **Réserve** — Mission en mode **COMPLET sous réserve déclarée** : C-19 (relevé de charpente partiel) et C-18 (action sismique non calculable) sont des données manquantes à porter à la FDC ; D5 (DXF) est désormais **fournie et inventoriée** ; elle ne porte en revanche **aucune donnée de structure** (R-37).

---

## 5. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-00) | État | Observation |
|---|---|---|
| Chaque pièce reçue figure avec son indice et ses folios utiles | ✅ satisfait | C0 + D1 (8 p. lues / 38 déclarées) + D2 (5 pages détaillées) + D3 (18 p.) + D4 (29 pages détaillées) |
| Chaque élément structurant est rattaché à une source citée | ✅ satisfait | § 2 : 11 sous-ensembles, chaque ligne portant fichier + page/folio + indice |
| Chaque contradiction est listée sans être résolue | ✅ satisfait | **20 contradictions** (C-01 à C-20), aucune résolution proposée |
| L'énoncé de mission tient en 5 lignes et cite les exclusions | ✅ satisfait | § 4 |

**Placeholders résiduels (V7)** : aucun. `ID-01` et `ID-02` renseignés (valeur proposée, soumise à validation).
**Retrait d'un élément de l'indice A** : tracé en § 3.4, avec motif et conséquence — conformément au principe de sincérité de session (§ 0.4).

---

## 6. POINT DE CONTRÔLE HUMAIN

1. Les **5 pièces** sont-elles toutes présentes et correctement indicées ? (C0, D1, D2, D3, D4)
2. Les **20 contradictions** sont-elles bien non tranchées ? Toute résolution serait une anomalie.
3. Le code projet `CROISSY-FLORA` et l'intitulé `ID-02` sont-ils retenus ?
4. **Décision attendue sur les deux points suivants**, qui conditionnent la phase 2 :
   - **C-08** (recharge de 15 cm vs 100 daN/m²) : maintenir l'hypothèse, la réviser, ou commander une note de charge ?
   - **C-10** (salle de sport) : confirmer la catégorie d'usage retenue pour 34,25 m² ?
5. Le **BET** peut-il fournir un **DXF de coffrage / structure** ? Le DXF d'architecte (D5) ne contient ni fondation, ni coffrage, ni altimétrie (R-37).

---

*Brique B-00, indice B, livrée. Aucune production des briques aval n'a été engagée.*
