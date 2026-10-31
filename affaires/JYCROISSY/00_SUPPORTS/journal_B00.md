# Journal d'exécution — B-00 JYCROISSY (preuve d'exécution, verrou V3)

> Session du 2026-10-23. Toutes les pièces sources sont des copies locales du
> dossier Drive **JYCROISSY**, déposées dans `google_drive/` (répertoire non
> versionné, ajouté au `.gitignore`). Aucune valeur ci-dessous n'est affirmée
> sans exécution reproductible.

## 1. Environnement

* Python 3 (venv projet `.venv/`, non versionné) ; bibliothèques installées
  depuis PyPI : `pypdf 6.21.2`, `ezdxf 1.4.5`.
* Script de preuve : `affaires/JYCROISSY/00_SUPPORTS/extraction_b00.py`
  (inventaire PDF + DXF, empreintes SHA-256, extraction plein texte).
* Textes extraits : `data/JYCROISSY/extraction/*.txt` (données locales,
  non versionnées).
* Le réseau sandbox n'autorise que GitHub/PyPI/npm : les pièces ne peuvent
  provenir que du connecteur Google Drive (téléchargement intégral, vérifié
  par taille et empreinte).

## 2. Empreintes des pièces reçues (SHA-256)

| Pièce | Octets | SHA-256 |
|---|---:|---|
| Copy of 07 — CARNAC v3.0.2 — Document compilé source (.md) | 1 216 325 | `820ae6ebc995333854f135bb2cf18a1308fc4dc179b46550d8e85640f352d368` |
| Copy of 208_FLORA_DCE_Pièces graphiques_IndC.pdf | 5 796 487 | `6e000700ed4a511a31274ac01ffaf9cf6a646527d6e5188e158cd5100d82a025` |
| Copy of 208_FLORA_DIAG structure.pdf | 1 361 521 | `8e85a911e588cb8b5884823bc4237e25b5c4cc0061007949eb657e8fb045b561` |
| Copy of 208_FLORA_Plans_DCE_IndC.dxf | 4 399 016 | `45f41e3113a909cef201ec4bb466d95cd82307ed6cd3fa9e016b69e53b39dcf1` |
| Copy of 24.09.356E DCE indice C FLORA 16.03.2026.pdf | 545 655 | `2c5723967ebfc4e4a89a328872cba94e889319c87f6069e6bc64093394c23773` |
| Copy of CCTP LOT 01 GROS OEUVRE - STRUCTURES - DEPLOMBAGE - INSTALLATION DE CHANTIER.pdf | 1 148 344 | `3020f52bf6c267b975a3a58cbe95e3a45e0313da1bbc5c530ebb4d7228402912` |

## 3. Résultats d'exécution (synthèse)

### 3.1 PDF (pypdf, toutes pages traitées, 0 XObject image détecté → PDF textes/vectoriels)

| Fichier | Pages | Format page | Producteur / origine | Pièces sans couche texte |
|---|---:|---|---|---|
| Pièces graphiques_IndC | 29 | A3 (842×1191 pt) | iLovePDF (assemblage) | aucune |
| DIAG structure | 19 | A4 (595×842 pt) | Microsoft Word (EVEN STRUCTURES) | aucune |
| 24.09.356E indice C | 5 | A3 (842×1191 pt) | AutoCAD LT 2020 (`pdfplot15`) | aucune (folio 2 : 28 car., folio 4 : 40 car. — plans quasi exclusivement graphiques) |
| CCTP Lot 01 | 38 | A4 (595×842 pt) | Microsoft Print To PDF | aucune |

### 3.2 DXF (ezdxf)

* `$ACADVER = AC1032` (AutoCAD R2018), code page ANSI 1252,
  `$INSUNITS = 5` (centimètres — unité à vérifier au calage B-30).
* Modelspace : **1 582 entités** — LWPOLYLINE 464, TEXT 416, INSERT 224,
  DIMENSION 163, LINE 158, MTEXT 97, HATCH 28, CIRCLE 15, ARC 7,
  ELLIPSE 7, POINT 3.
* 31 calques dont 9 sans entité modelspace : `091_surfaces`, `Defpoints`,
  `097_traits-fins-005`, `HAB-HAB-D`, `2_2-MENUISERIE-VU`,
  `2_2-MENUISERIE-CO`, `BLC-ATT-T`, `BLC-CUI-S`,
  `*ADSK_ASSOC_ENTITY_BACKUPS`.
* 46 blocs nommés ; 2 présentations papier (`Model`, `Layout1` — 2 VIEWPORT).
* Contenu vérifié par les textes/boîtes : plans **architecte Flora RDC/R+1**
  (existant, projet, démolition, sols, plafonds, repérage murs). Aucun texte
  de structure (fondations, semelles, poteaux BA, coffrage), aucun contenu
  Gardien/Bagatelle/sous-sol.

## 4. Passages consultés (preuve d'épuisement V14)

| Pièce | Pièces/paragraphes effectivement consultés |
|---|---|
| CCTP (38 p.) | Sommaire p2-4 ; généralités p5-9 ; Nota TCE p9 ; travaux préparatoires, implantation, études béton, hypothèses générales p10-14 ; désamiantage/déplombage p14-20 (exclusions CARNAC, lues pour délimitation) ; curage p20-21 ; démolitions/frangements/percements p21-25 ; renforts profilés métalliques p25-26 ; terrassements/fondations p26-28 ; assainissement/fourreaux p28-33 ; géotextile, termites, dallages, essais à la plaque p33-36 ; élévations p36 ; DOE p37-38 |
| DIAG (19 p.) | Objet/description p3 ; principe structurel p4 ; désordres 1 à 9 p5-9 ; planchers A (bois EC5) p10-11 ; plancher B (métal EC3/ROBOT) p12-13 ; conclusions et préconisations p14-15 ; portiques Est/Ouest p16-18 ; renforts planchers p19 |
| BET 24.09.356E (5 p.) | Sommaire + données d'études (normes, sol, bétons, aciers, neige/vent/séisme, charges) p1 ; folio 1 PH RDC (légende ouvrages) p2 ; folio 2 Charpente p3 ; folio 3 PB RDC (nota semelles, XA4) p4 ; folio 4 Fondations passerelle château p5 |
| Pièces graphiques (29 p.) | Sommaire p1 ; les 29 cartouches extraits et comparés au sommaire ; contenu détaillé p2-6 (masse, existant, démolition, projet), p28 (installation chantier/Gardien), p29 (Bagatelle/sous-sol) |
| DXF | Toutes les entités modelspace, la totalité des 31 calques, les 46 blocs, 513 occurrences de texte (241 uniques), les 2 layouts |
| CARNAC v3.0.2 | §0 (protocole/portes), §1 (posture/exclusions), §2 (verrous), §6.1 (CFG-01), §7 (arborescence), §9 (ordonnancement), fiche B-00 complète |

## 5. Évolution Ind A → Ind B (2026-10-23) — prise en compte du CR officiel du 20/10/2026

Réception des réponses architecte/client consignées au compte rendu : 5 décisions
tranchantes (D-01…D-05), 1 décision géotechnique (D-06) et 1 point d'arrêt
(PA-01 provisoire). Création du registre de transition
`02_PHASE_0_CADRAGE/RDR_provisoire_en_attente_B03.md`, qui sera repris sans
renumérotation à l'ouverture officielle du RDR en B-03.

* C-01 → soldée D-04 (adresse 11 rue Paul Demange)
* C-02 → soldée D-01 (ancrage 0,50 m alluvions anciennes)
* C-03 → soldée D-02 (P1 = tube 14 × 14 cm)
* C-04 → soldée D-03 (SE 250 daN/m² ; re-vérification EXE à programmer)
* C-05 → soldée D-05 (MOA UNIVI)
* G2 non reçu → D-06 (qELS 0,30 MPa, qELU 0,49 MPa, ancrage 50 cm) + PA-01 (contrôle d'arase en fouille)
* Restent ouverts : C-06, C-07, C-08, C-09, C-10, C-11.

Conformément au §0.2.4, la re-livraison B-00 Ind B s'accompagne d'un nouvel
arrêt : B-01 n'est pas engagée dans le même mouvement, malgré le « GO »
terminal du message, car celui-ci coexistait avec des corrections (règle
anti-enchaînement masqué ; doute de portée traité par re-confirmation).
