# B-00 — INVENTAIRE DES PIÈCES ET ÉNONCÉ DE MISSION

| Champ | Valeur |
|---|---|
| Code session (ID-01) | **JYCROISSY** — codes portés par les pièces : site **n° 208** (cartouches SCI GEMS RC), dossier EVEN STRUCTURES **24.09.356E**, affaire EICP **014-2024-08** |
| Opération (ID-02) | **Aménagement d'un cabinet paramédical dans le pavillon Flora — EHPAD/Résidence La Roseraie, 11 rue Paul Demange, 78290 Croissy-sur-Seine** (adresse officialisée par **D-04**) |
| Carnet de référence | CARNAC v3.0.2 (fiche `02_PHASE_0_CADRAGE/B-00_Inventaire.md`) |
| Indice de livrable | **Ind B — 2026-10-23** — intégration du compte rendu officiel du **20/10/2026** (réponses architecte/client) |
| Historique | Ind A (2026-10-23) : première émission, 11 écarts ouverts · **Ind B (2026-10-23) : 5 écarts soldés par D-01 à D-05, paramètres géotechniques officialisés par D-06, PA-01 ouvert, 6 écarts restent ouverts** |
| Mode d'appel | **COMPLET** (toutes les pièces reçues ouvertes et exploitées ; aucune pièce inexploitable) |
| Posture | BET d'exécution entreprise, mission **EXE / PAC** (confirmée par CCTP §01.2.1.1.6) |
| Pièces d'entrée | 5 pièces de projet + 1 carnet de protocole (détail §1) + 1 compte rendu de décisions du 20/10/2026 |
| Documents liés | `RDR_provisoire_en_attente_B03.md` (D-01…D-06, PA-01) ; `../00_SUPPORTS/journal_B00.md` ; `../00_SUPPORTS/extraction_b00.py` |

> Verrous respectés : V1 (hiérarchie des sources, aucune pièce écartée), V2 (tout fait porte sa source), V3 (aucun blanc comblé), V7 (zéro placeholder), V14 (preuve d'épuisement §6). Les décisions du CR 20/10/2026 prévalent sur toute valeur contradictoire des pièces initiales, sans effacer le fait historique (la valeur d'origine reste citée et datée).

---

## 0. SYNTHÈSE DES CHANGEMENTS IND A → IND B (revue de porte)

1. **C-02 soldée (D-01)** : ancrage des fondations = **0,50 m dans les alluvions anciennes** ; la mention CCTP de 40 cm est caduque.
2. **C-03 soldée (D-02)** : poteau P1 = **tube carré 14 × 14 cm** (le « 14 × 14 mm » du CCTP est une erreur de frappe).
3. **C-04 soldée (D-03)** : SE de référence = **250 daN/m² (250 kg/m²)** pour le futur cabinet ; les calculs du diagnostic à 150 daN/m² deviennent des données historiques, une re-vérification EXE sera nécessaire (briques aval, sans conclusion en B-00).
4. **C-01 soldée (D-04)** : adresse unique = **11 rue Paul Demange**.
5. **C-05 soldée (D-05)** : MOA de référence = **UNIVI** ; SCI GEMS RC reste une mention documentaire.
6. **Géotechnique (D-06)** : le rapport G2 complet n'est toujours pas reçu, mais ses paramètres de dimensionnement (qELS ≤ 0,30 MPa, qELU ≤ 0,49 MPa, ancrage 50 cm) sont officiellement transmis ; un **point d'arrêt PA-01** (contrôle d'arase en fouille) est ouvert.
7. Restent **ouverts et non tranchés** : C-06, C-07, C-08, C-09, C-10, C-11 (§3.2).
8. CFG-01, mission reformulée, inventaire des pièces et preuve d'épuisement : inchangés.

---

## 1. INVENTAIRE DES PIÈCES

### 1.1 Pièce de protocole (hors pièces de projet)

| Fichier | Format | Nature | Indice / date |
|---|---|---|---|
| Copy of 07 — CARNAC v3.0.2 — Document compilé source (.md) | Markdown, 1 216 325 o. | Carnet de prompts CARNAC (compilé mono-fichier de l'arborescence de référence) | v3.0.2 |

### 1.2 Pièces de projet (5)

| # | Fichier (copie Drive) | Format / mode d'exploitation | Pages / folios utiles et objet | Indice et date | Échelle / orientation |
|---|---|---|---|---|---|
| P1 | **CCTP LOT 01 GROS OEUVRE - STRUCTURES - DEPLOMBAGE - INSTALLATION DE CHANTIER** | **PDF vectoriel** (texte natif, 0 XObject image, A4) — 38 p., 1 148 344 o. Producteur MS Print To PDF, auteur S. Dubois (EICP) | p1 couverture ; p2-4 sommaire ; p5-9 généralités ; p10-13 préparation, implantation, **études béton**, hypothèses ; p14-20 désamiantage/déplombage ; p20-21 curage ; p21-25 démolitions, frangements, percements, **renforts métalliques** ; p26-28 terrassements et **fondations** ; p28-33 assainissement/fourreaux ; p33-36 **dallages** (géotextile, termites, essais à la plaque) ; p36-37 **élévations** ; p37-38 DOE | **V1, stade PRO, 13/03/2026** (affaire EICP 014-2024-08) | Sans objet (texte) |
| P2 | **208_FLORA_DIAG structure** | **PDF vectoriel** (texte natif, 0 XObject image, A4) — 19 p., 1 361 521 o. Source MS Word, auteur « even es » (EVEN STRUCTURES) | p3 objet/description ; p4 principe structurel ; p5-9 **désordres 1 à 9** ; p10-11 plancher A bois (EC5) ; p12-13 plancher B métallique (EC3, ROBOT) ; p14-15 conclusions/charpente ; p16-17 portiques bois Est/Ouest ; p18-19 préconisations renforts planchers | Phase **DIAG, indice « - », 24/03/2025** (1ère diffusion ; visite site 20/02/2025 ; n° dossier 24.09.356E) | Sans objet (texte + vues) |
| P3 | **24.09.356E DCE indice C FLORA 16.03.2026** | **PDF vectoriel** (export AutoCAD LT 2020, A3) — 5 p., 545 655 o. | p1 sommaire + **données d'études** ; p2 **folio 1 « Vue en plan PH RDC »** + légende des ouvrages ; p3 folio 2 « Vue en plan Charpente » (28 car. texte, quasi exclusivement graphique) ; p4 folio 3 « Vue en plan PB RDC » + nota semelles/XA4 ; p5 folio 4 « Fondations passerelle château » (40 car. texte) | Pièce dite **indice C du 16/03/2026**, mais folios d'indices hétérogènes : folio 1 **C**, folios 2 et 3 **« - »**, folio 4 **B** (écart **C-09**, toujours ouvert) | Folio 1 coté **1/50 - 1/20** ; autres folios non cotées en texte |
| P4 | **208_FLORA_DCE_Pièces graphiques_IndC** | **PDF vectoriel** (assemblage iLovePDF, A3, 0 XObject image) — **29 p.**, 5 796 487 o. — dossier **architecte Truelle** | Détail des 29 planches au §1.3 | **Indice C, 13/03/2026, DCE** | 1/500, 1/100, 1/50 selon planches (§1.3) ; nord graphique |
| P5 | **208_FLORA_Plans_DCE_IndC.dxf** | **Vecteur natif DXF R2018 (AC1032)**, ANSI 1252, `$INSUNITS = 5` (cm — à confirmer au calage B-30), 4 399 016 o. | **1 582 entités modelspace** (LWPOLYLINE 464, TEXT 416, INSERT 224, DIMENSION 163, LINE 158, MTEXT 97, HATCH 28, CIRCLE 15, ARC 7, ELLIPSE 7, POINT 3) ; 31 calques (**9 calques vides**, journal §3.2) ; 46 blocs nommés ; 1 présentation papier `Layout1` (2 VIEWPORT) | **Ind C** (nom de fichier, cohérent avec P4) | Échelles non portées en modelspace ; flèche nord présente (blocs `NORD`, `Fléche-Nord-1`) |

**Réserves d'exploitation (pièces non inexploitables, limites déclarées) :**

* P3 folios 2 et 4 : texte quasi absent ; exploitation par le graphique vectoriel en aval, aucune valeur supputée en B-00.
* P4 : libellés de cartouche des planches 3, 16, 17 et 25 non reconstituables par extraction texte ; désignations §1.3 marquées `[déduit]`.
* P5 : 9 calques sans entité modelspace (liste journal §3.2) ; DXF limité aux plans Flora RDC/R+1 (écart C-08 ouvert).
* P5 est un DXF **architecte** (calques `010_mur`, `020_cloisons`, `030_menuiserie`, `040_meubles`, `080_plomb-cvc`, `102_demol`…) : aucune entité de structure (coffrage, semelles, armatures) détectée.

### 1.3 Détail des 29 planches de P4 (cartouches réels comparés au sommaire p1 — écart C-06 ouvert)

| Page | Désignation au cartouche | Échelle | Page | Désignation au cartouche | Échelle |
|---:|---|---|---:|---|---|
| 1 | Sommaire | — | 16 | Détail bureaux R+1 `[déduit : coupes OO]` | 1/50 |
| 2 | Plan masse existant | 1/500 | 17 | Détail salle de sport `[déduit : coupes PP/QQ/RR]` | 1/50 |
| 3 | Plan masse projet `[déduit]` | 1/500 | 18 | Détail salle commune, vestiaire, sanitaire et douche R+1 | 1/50 |
| 4 | Plans existant (RDC & R+1 Flora) | 1/100 | 19 | Façades existant Nord-Est | 1/100 |
| 5 | Plans de démolition | 1/100 | 20 | Façades Ouest-Sud (existant) | 1/100 |
| 6 | Plans projet (RDC & R+1 Flora) | 1/100 | 21 | Façades projet Sud-Est | 1/100 |
| 7 | Plan aménagement extérieur | 1/100 | 22 | Façades projet Nord-Ouest | 1/100 |
| 8 | Plans de sols | 1/100 | 23 | Nomenclature des portes | 1/50 |
| 9 | Plans de repérage des murs | 1/100 | 24 | Nomenclature menuiseries RDC | 1/50 |
| 10 | Plans de plafonds | 1/100 | 25 | Nomenclature menuiseries R+1 et toiture `[titre partiel]` | 1/50 |
| 11 | Détail boxs kiné et bureau | 1/50 | 26 | Toitures existant | 1/100 |
| 12 | Détail bureaux RDC et attente | 1/50 | 27 | Toitures projet | 1/100 |
| 13 | Détail plateau technique | 1/50 | 28 | Plan installation de chantier (base vie dans le Gardien) | 1/100 |
| 14 | Détail sanitaires PMR RDC | 1/50 | 29 | Phase préparatoire / Aménagement Bagatelle — plans sous-sol | 1/100 |
| 15 | Détail dégagement escalier | 1/50 | | | |

### 1.4 Acteurs nommés dans les pièces

* Maîtrise d'ouvrage de référence : **UNIVI** (54 bd de la Liberté, Lille) — **D-05**. La mention « SCI GEMS RC — site 208 » (20 rue Jacques Daguerre, Rueil-Malmaison) des cartouches P4 reste documentaire.
* Architecte : **Truelle Architectes** (Sandy Iglesias, Arcueil).
* BET structure MOE : **EVEN STRUCTURES** (Angers). BET fluides : AB Ingénierie. Économiste : EICP (S. Dubois).
* Géotechnique : **GEOEXPERTS** (Lille), G2 AVP n° 25.13646/ES/GIF du 22/01/2026 — rapport non reçu, paramètres officialisés par **D-06**.

---

## 2. ÉLÉMENTS STRUCTURANTS EXTRAITS (chacun rattaché à sa source)

### 2.1 Existant (diagnostic P2, plans architecte P4/P5)

| Fait | Valeur extraite | Source |
|---|---|---|
| Typologie du pavillon | Ancien bâtiment R+1/combles, anciennement habitation à l'étage et locaux techniques EHPAD au RDC | P2 p3 |
| Fondations existantes | **Inconnues**, probablement soubassements maçonnés type semelle filante ; soubassement en pierre dure constaté en pied de portiques | P2 p3, p17, p18 |
| Élévations existantes | Poteaux bois et briques, maçonnerie ; façades partie haute en briques sous enduit | P2 p3, p5 |
| Plancher type A (bois) | Solives bois 8×18, poutre 20×15, lambourdes/parquet et lattis-plâtre ; hypothèse bois C18 à 12 % (EC5) | P2 p10-11 |
| Plancher type B (mixte) | Solives **IPE160**, hourdis briques creuses 7 cm + polystyrène 8 cm + chape béton 10 cm ; poutre **IPE330** (EC3, calculs ROBOT) | P2 p12-13 |
| Portiques bois de façade | Est et Ouest, poutre 23×15, poteaux 15×15, remplissage brique ; bois C25 ; profilé métallique intérieur ajouté en renfort des planchers | P2 p16-17 |
| Charpente | Ferme centrale, chevrons, potelets, lattis ; altérations humidité, potelets nord « théoriquement instables » | P2 p7-9, p14-15 |
| Désordres structurants | 9 désordres D1 à D9 (linteaux ouest, fissures jonction bois/brique, flèche poutre maîtresse est, humidité EP, fissures plafond, ferme altérée, humidité intérieure, chevrons est, lattis-plâtre) | P2 p5-9 |
| Capacités plancher A (sous 150 daN/m² logement — référence historique) | Solive non justifiée en flèche (7,7 mm > 7 mm) ; poutre non justifiée (72,8 mm > 10,4 mm ; contrainte +200 %) | P2 p11, p19 |
| Capacités plancher B (sous 150 daN/m² — référence historique) | Solive IPE160 instable au déversement (flèche OK) ; poutre IPE330 justifiée, réaction d'appui 6,9 t (6 870 daN ELU) | P2 p12-13, p18 |
| Portiques | Est justifié (contraintes en pied à la limite) ; **Ouest non justifié** → préconisation poteau à mi-travée + semelle de répartition ; sommier béton si augmentation de charges | P2 p16-18 |
| Niveaux altimétriques | RDC Z ≈ 201,03 à 201,26 ; R+1 Z ≈ 203,59 à 204,43 (repères plan, unité NGF non explicitée sur planche) | P4 p4, p6 ; textes P5 |
| Hauteurs sous plafond | hsp RDC 2,16 à 3,08 m ; R+1 2,39 à 3,25 m ; hsfp 2,19 à 2,80 m ; contraintes H < 1,80 m et Hmin 1,67 m (combles) | P4 p4-6, p9-10 ; P5 |

### 2.2 Ouvrages projet (P3, P1, P4) — valeurs officielles après décisions CR 20/10/2026

| Fait | Valeur extraite / retenue | Source |
|---|---|---|
| Renforts métalliques de linteaux/frangements | F1 = 2× HEA 200 ; F2 = HEB 200 ; F3 = HEB 160 ; F4 = IPE 200 ; R1 = 2× UPE200 ; R2 = HEB 160 ; R3 = UPE 200 ; Stab1 = entretoise anti-dévers IPE incorporée au voutain brique | P3 folio 1 ; P1 p25-26 |
| Poteaux / sommiers / jambages projet | **P1 = tube carré 14 × 14 cm (D-02)** ; P2 poteau 15×25 BA ; P3 poteau 50×40 BA ; S1 sommier 20×40×20 ht BA ; S2 20 × ép. mur × 20 ht BA ; J1 jambage 24 × ép. maçonnerie BA | P3 folio 1 ; P1 p22-23 ; CR D-02 |
| Fondations neuves | Semelles filantes BA, bêches hydrauliques BA, ossature BA en fondation, soubassements agglo, arase étanche (feutre bitumineux entre 2 chapes hydrofugées 2 cm, 600 kg), membrane bitume-élastomère (FONDAPLY/éq.) | P1 p26-28 |
| **Ancrage au sol (valeur officielle)** | **RSO ancrées d'au moins 0,50 m dans les alluvions anciennes (D-01, D-06). Capacité 3 bars ELS = qELS ≤ 0,30 MPa ; qELU ≤ 0,49 MPa (D-06).** La mention « 40 cm » du CCTP p13 est caduque. Contrôle d'arase en fouille : **PA-01** | P3 p1 ; P1 p13 ; CR 20/10/2026 |
| Dallage neuf | Dallage BA sur terre-plein ; fond de forme 40 cm (P3) ; GNT 0/31,5, sablage, XPS 105 mm (R = 3,60), polyane 200 µm ; compactage 95 % OPN, essais à la plaque EV2 ≥ 50 MPa, Kw ≥ 50 MPa/m, K ≤ 2,0 (DTU 13-3) ; rampe et décaissé sanitaire PMR | P3 p1 ; P1 p33-36 |
| Sols agressifs | **XA4** : géotextile anti-contaminant sous couche de forme (≥ 150 g/m²) ; barrière termites physico-chimique 150 µm (TERMIFILM UV+/éq.) | P3 p1, p4 ; P1 p33-34 |
| Bétons / aciers | C25/30 (structure), C16/20 (gros béton) ; enrobages XC1/XC2/XF1/XC4 ; HA S500, lisses S220 ; acier métal S275 | P3 p1 ; P1 p7-8 |
| **Charges (valeurs officielles)** | CP plancher métallique 350 daN/m², plancher bois 100 daN/m² ; **SE cabinet paramédical/bureaux = 250 daN/m² (250 kg/m²) — D-03** ; toiture inaccessible 80 daN/m² (utilisée dans P2) | P3 p1 ; P2 p16 ; CR D-03 |
| Données climatiques | Neige A1, sk 45 daN/m², altitude < 200 m ; vent zone 2, vb 24 m/s ; séisme zone 1, classe sol III, classe bâtiment II | P3 p1 ; P1 p13 |
| Géotechnique | Rapport G2 AVP GEOEXPERTS n° 25.13646/ES/GIF du 22/01/2026 **non reçu** ; paramètres officiels repris par **D-06** ; dallage prescrit suivant ce rapport | P3 p1 ; P1 p13 ; CR D-06 |
| Démolitions / modifications | Murs et cloisons démolis, ouvertures de baies (passage 90×210), modification escalier, décaissements (16,8 cm pente 10 % ; 3,2 cm pente 6 %), sol à recharger de 15 cm, pavés grès réemployés ; trémies bouchées au béton de vermiculite (CF) | P4 p5 ; P1 p21-25 |
| Ouvrage spécifique | « Fondations passerelle château » (folio 4 P3, indice B) — objet et dimensionnement non décrits en texte | P3 p5 |
| Sécurité incendie | Stabilité au feu par encoffrement (P3) ; peinture intumescente PROMAPAINT/éq. (P1) — **dimensionnement de la protection feu hors périmètre CARNAC** (mention seule) | P3 p1 ; P1 p26 |
| Contraintes de site | EHPAD en exploitation, mitoyenneté, accès rue Paul Demange (**D-04**), base vie dans le Gardien, phase préparatoire Bagatelle (sous-sol : local repos, bureau maintenance, déplacement chaudière/adoucisseur) ; constat d'huissier avant/après ; PPSPS/PGCSPS | P1 p10-12 ; P4 p28-29 |

### 2.3 Carnet des faits (tableau unique consommé par les briques aval — addendum A1 v3.0.1)

| Fait | Valeur | Source (pièce + folio/page) | Zone |
|---|---|---|---|
| Nature plancher — type A | Bois : solives 8×18 + poutre 20×15, lambourde/parquet, lattis-plâtre ; non justifié en flèche/contrainte sous 150 daN/m² (référence historique) | P2 p10-11, p19 | Vue plancher A (P2 p10) |
| Nature plancher — type B | Mixte : IPE160 + hourdis brique 7 cm + PS 8 cm + chape 10 cm, poutre IPE330 ; déversement à traiter | P2 p12-13, p18 | Vue plancher B (P2 p10) |
| Nature plancher — dallage neuf | BA sur terre-plein, forme 40 cm, XPS 105 mm, polyane, sous géotextile anti-contaminant | P1 p33-36 ; P3 p1 | RDC projet |
| Planchers non sondés | Toute partie hors campagne P2 est **non sondée** (à instruire B-23/B-24) | P2 p10 | — |
| Matériaux prescrits | C25/30, C16/20, HA S500, S220, S275, agglo blocs pleins 30/40 B80 et creux 50 B40 | P3 p1 ; P1 p8-9 | Tous ouvrages GO |
| Ouvrages existants | Façades briques/bois, portiques Est/Ouest, charpente, planchers A/B, soubassement pierre | P2 §3-5 | Pavillon Flora |
| Ouvrages neufs | Renforts HEA/HEB/IPE/UPE, **P1 tube 14×14 cm (D-02)**, poteaux/sommiers/jambages BA, semelles/bêches, dallage, arase/membrane, rampe PMR | P3 folio 1 ; P1 §01.2.1.5 à .10 ; CR D-02 | RDC & R+1 Flora |
| Niveaux | RDC Z ≈ 201,0-201,3 ; R+1 Z ≈ 203,6-204,4 ; hsp/hsfp recensés §2.1 | P4 p4-6 ; P5 | Flora RDC/R+1 |
| **Surcharge d'exploitation cible** | **250 daN/m² (D-03)** — remplace 150 daN/m² du diagnostic pour les vérifications EXE ; re-vérification des planchers existants à programmer en B-21/B-23 | CR D-03 ; P3 p1 ; P2 | Ensemble planchers réutilisés |
| **Ancrage fondations** | **≥ 0,50 m alluvions anciennes, qELS 0,30 MPa / qELU 0,49 MPa (D-01, D-06) ; PA-01 contrôle en fouille** | CR 20/10/2026 ; P3 p1 | Toutes semelles neuves |
| MOA / adresse de référence | **UNIVI (D-05) ; 11 rue Paul Demange (D-04)** | CR 20/10/2026 | Tous documents EXE |
| Exclusions de mission | Désamiantage, déplombage, curage/démolition (phasage), espaces verts, protection feu (dimensionnement), fluides/CVC/élec/VRD, thermique/acoustique, second œuvre de distribution, G1-G3 | P1 p14-21 ; CARNAC §1.4 | — |

---

## 3. CONTRADICTIONS ET ÉCARTS

### 3.1 Écarts soldés par décision officielle (CR du 20/10/2026) — registre `D-xx`

| Code | Donnée | Pièce A | Pièce B | Décision de référence |
|---|---|---|---|---|
| C-02 | Ancrage des semelles | P3 p1 : ≥ 0,50 m | P1 p13 : 40 cm | **Soldée — D-01 : 0,50 m retenu** |
| C-03 | Section poteau P1 | P3 : « 14×14 » (unité absente) | P1 p23 : « 14×14 mm » | **Soldée — D-02 : 14 × 14 cm, erreur de frappe CCTP** |
| C-04 | Charge d'exploitation | P2 : 150 daN/m² (logement) | P3 p1 : 250 daN/m² (cabinet) | **Soldée — D-03 : 250 daN/m² (250 kg/m²) ; re-vérification EXE à programmer** |
| C-01 | Adresse | P2 : 2 rue Alfred Dormeuil | P3/P4/P1 : 11 rue Paul Demange | **Soldée — D-04 : 11 rue Paul Demange** |
| C-05 | Dénomination MOA | P1 : UNIVI | P4 : SCI GEMS RC site 208 | **Soldée — D-05 : UNIVI retenu (pas d'incidence technique)** |
| — | Rapport G2 non reçu | Rapport cité mais non joint (P3, P1) | Paramètres transmis par CR | **D-06 : paramètres officiels retenus ; rapport complet toujours non reçu ; PA-01 ouvert** |

### 3.2 Écarts restant **ouverts, non tranchés** (verrou V1 — votre décision reste requise)

| Code | Donnée concernée | Pièce A | Pièce B | Nature de l'écart |
|---|---|---|---|---|
| C-06 | Numérotation des planches graphiques | P4 p1 sommaire (repérage murs en 29, installation chantier 19-20, extérieurs 26) | Cartouches réels (repérage murs p9, installation p28, extérieurs p7, Bagatelle p29) | Décalage sommaire/planches ; les citations aval utiliseront le n° de page PDF réel |
| C-07 | Périmètre bâti Gardien / Bagatelle | P1 intitulé « Flora & Gardien », un seul bloc `01.2.1 Flora` (pas de `01.2.2`) | P4 p28-29 : base vie Gardien + aménagement Bagatelle ; P3/P5 sans contenu Gardien | Périmètre structure Gardien/Bagatelle non décrit ni dessiné par le BET |
| C-08 | Couverture du DXF | P5 : uniquement Flora RDC/R+1, 1 layout papier | P4 : 29 planches (masse, façades, toitures, nomenclatures, Bagatelle…) | Le vecteur natif ne couvre pas tout le DCE architecte ; cartographie à faire en B-30 |
| C-09 | Indices des folios BET | P3 nommé « indice C », folio 1 en C | Folios 2 et 3 « - », folio 4 « B » | Folios non remis à jour dans une pièce dite indice C |
| C-10 | Échelle plan sous-sol | P4 p29 cartouche : 1/100 | Mention interne p29 : « 1/2000 » | Coquille probable (1/200 ?), sans impact structure direct |
| C-11 | Titre du document P2 | Couverture : « Diagnostic structurel » | Pieds de page : « Diagnostic charpente » | Périmètre éditorial ambigu (le document traite aussi planchers, portiques, fondations) |

### 3.3 Pièces tierces citées mais non jointes (fait documenté ; statut réservé à B-01)

* Rapport G2 AVP GEOEXPERTS n° 25.13646/ES/GIF : **non reçu** (trop volumineux pour chargement) ; paramètres de dimensionnement officialisés par D-06, contrôle fouille par PA-01.
* Rapport de repérage amiante avant travaux du 31/12/2024 (P1 §01.2.1.2.1) ; rapport plomb (P1 §01.2.1.3.1).
* PGC/SPS, PPSPS, CCAP, Cahier des Prescriptions Communes (P1 p9-10).
* Plans de géomètre (blocs P5 `Plan existant mi geometre rdc`, `Murs porteurs selon geometre projet` ; DOE géomètre P1 p37).
* Annexes de calcul 1 et 2 et modèles ROBOT du diagnostic (P2 p11-13).
* DPGF/bordereau ; bureau de contrôle non nommé dans les pièces lues.
* Diagnostic parasitaire préconisé par P2 p14, non commandé à ce jour.

---

## 4. ÉNONCÉ DE MISSION REFORMULÉ (5 lignes maximum)

1. **Objet** : produire, en BET d'exécution entreprise (EXE/PAC), les études et plans d'exécution gros œuvre/structure de la réhabilitation du pavillon Flora en cabinet paramédical (RDC + R+1, structure existante mixte bois/brique/métal/BA), en transcrivant et complétant les principes du BET MOE EVEN STRUCTURES.
2. **Périmètre du lot** : démolitions structurelles représentées (reprises, frangements, percements, rebouchages), renforts métalliques et BA, reprises en sous-œuvre éventuelles, fondations superficielles (ancrage 0,50 m, D-01/D-06), dallages, élévations maçonnerie/BA et réservations pour coordination.
3. **Livrables attendus** : notes de calcul d'exécution (y compris re-vérification des planchers existants sous 250 daN/m², D-03), plans de coffrage, d'armatures et PAC, détails, auto-contrôle, récolement DOE (DXF/DWG) et pièces pour contrôle technique.
4. **Exclusions explicites** : désamiantage, déplombage, curage/démolition (mode opératoire et phasage), espaces verts, dimensionnement de la protection au feu (mention seule), fluides/CVC/électricité/VRD (réservations/attentes seules), thermique et acoustique, second œuvre de distribution, études géotechniques G1 à G3.
5. **Contraintes de fonctionnement** : site EHPAD occupé et mitoyen, corpus indissociable (V14), toute contradiction reste non tranchée tant que vous ne l'avez pas arbitrée (registre D/H/PA), toute donnée manquante passe par hypothèse notifiée `H-xx` ou point d'arrêt `PA-xx` — jamais par valeur de repli.

---

## 5. QUALIFICATION DE LA CONFIGURATION DE MATURITÉ MOE — **CFG-01 = CFG-2** (inchangée)

BET structure MOE existant (EVEN STRUCTURES : DIAG + principes DCE PDF), **sans vecteur structure natif** (le DXF P5 est architecte) → **`CFG-2`**. Conséquences : interdiction de réclamer un DXF de coffrage MOE ; recalage vectoriel des PDF MOE, transcription intégrale des ouvrages et interfaces, puis calculs et plans d'exécution à notre charge (B-30 → B-32 → B-20 et suivantes). Mission EXE/PAC confirmée par P1 §01.2.1.1.6.

---

## 6. PREUVE D'ÉPUISEMENT DU CORPUS (verrou V14)

* 5 pièces de projet intégralement parcourues (91 pages PDF + 1 DXF) ; détail des passages au journal `../00_SUPPORTS/journal_B00.md` §4.
* PDF : extraction page par page (pypdf 6.21.2), 0 XObject image sur 91 pages, pages à faible texte (P3 p3/p5) signalées en réserve.
* DXF : ezdxf 1.4.5, totalité des 1 582 entités, 31 calques, 46 blocs, 513 textes (241 uniques), 2 layouts ; recherche explicite de contenus structure/Gardien/Bagatelle → aucun résultat (C-07/C-08).
* Décisions CR 20/10/2026 intégrées ligne à ligne et réversibles traçablement (valeur d'origine conservée et datée) ; empreintes SHA-256 et reproductibilité via `extraction_b00.py`.

## 7. CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque pièce reçue figure avec indice et folios utiles | ✅ §1 |
| Chaque élément structurant rattaché à une source citée | ✅ §2 (pièce + page/folio + décision D-xx le cas échéant) |
| Chaque contradiction listée sans être résolue par le modèle | ✅ §3.1 (soldées **uniquement** par vos décisions D-01…D-06) et §3.2 (6 écarts toujours ouverts, sans arbitrage du modèle) |
| Énoncé de mission en 5 lignes avec exclusions | ✅ §4 |
| Zéro placeholder résiduel (V7) | ✅ contrôlé |
| CFG-01 qualifiée | ✅ §5 : CFG-2 |
| Décisions conversationnelles consignées (§0.2.5) | ✅ `RDR_provisoire_en_attente_B03.md` (D-01…D-06, PA-01), à entériner en B-03 |

**Point de contrôle humain :** vérifier la transcription fidèle des six décisions (en particulier D-02 « 14 × 14 cm » et D-06 avec PA-01), et confirmer que les six écarts ouverts (C-06 à C-11) restent bien à instruire plus avant.

---

**Brique B-00 re-livrée en Ind B — en attente de votre GO ou de nouvelles observations.**
Conformément au §0.2.4, la présence de corrections dans votre message impose cette re-livraison et ce nouvel arrêt : je n'ai pas engagé B-01. Un **« GO B-01 »** explicite après votre vérification déclenchera la proposition de MPD (matrice de périmètre et de disponibilité).
