# B-02 — FICHE DE DONNÉES DE CONCEPTION (FDC) — JYCROISSY

| Champ | Valeur |
|---|---|
| Opération | Aménagement d'un cabinet paramédical, pavillon Flora, EHPAD La Roseraie, 11 rue Paul Demange, Croissy-sur-Seine (D-04) |
| Carnet | CARNAC v3.0.2 — fiche `02_PHASE_0_CADRAGE/B-02_FDC.md` |
| Indice | **B-02 — 2026-10-30** (FDC — valeurs et sources ; verrous en fin de fiche) |
| Entrées | MPD B-01 Ind B (validée) ; pièces P1-P5 ; pré-RDR D-01…D-13 + PA-01 |
| Sortie | Tableau 1 (valeurs résolues) + Tableau 2 (VERROU) + table NIV-07 |
| Mode d'appel | COMPLET (valeurs disponibles) / PARTIEL-DÉCLARÉ (décision RDR) / PARAMÉTRIQUE (symbole) |

> Règles tenues : aucune valeur sans source citée ; aucun repli ; aucun arbitrage silencieux ; seules les variables lues par une brique activée figurent (règle 1) ; niveau de fiabilité obligatoire (règle 3) ; les VERROU en fin de fiche (règle 5). Machine-readable : `FDC_jycroissy.csv` ; générateur/validateur : `../00_SUPPORTS/build_b02.py`.

---

## TABLEAU 1 — Variables résolues (valeur, source, fiabilité)

*66 variables.* Seules les variables lues par au moins une brique activée sont reprises (règle 1 de la fiche B-02).

| Code | Libellé | Valeur | Unité | Source (pièce + folio/page) | Fiabilité | Brique(s) consommatrice(s) |
|---|---|---|---|---|---|---|
| AC-03 | BET structure de conception | EVEN STRUCTURES — BET MOE existant (DIAG + DCE PDF), mission EXE/PAC ; livraisons PDF sans vecteur coffrage (CFG-2) | — | P2 DIAG couverture + p2 ; P3 DCE indice C couverture ; B-00 §5 | Contractuelle | B-20 |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | CFG-2 — BET MOE en PDF, sans vecteur structure natif | — | P3 DCE indice C ; P2 DIAG ; qualification B-00 §5 | Contractuelle | B-00, B-01, B-20, B-60 |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | M — bâtiment unitaire, emprise < 2 500 m², plus de 5 porteurs, sans JD ni sous-sol Flora | — | D-07 (CR 20/10/2026) ; B-00 §0 | Décision | B-01, B-04, B-25, B-34, B-60 |
| CFG-03 | Découpage blocs structurels / JD / niveaux-types | Bloc unique « Flora » ; niveaux PB RDC (premier bas) / PH R+1 (plancher haut) / charpente-combles ; « PH RDC » archi (P3 f1) = sous-face du plancher haut PH R+1 ; vue unique FONDATIONS + PB RDC acceptable | — | D-13 (CR 20/10/2026) ; nomenclature P3 folio 1 | Décision | B-01, B-20, B-21, B-25, B-30, B-60 |
| CHG-01 | Usage des locaux par zone (catégories EC1) | Usages nommés : box kiné, bureaux, plateau technique, salle de sport ; catégories EC1 non attribuées formellement | — | P4 p6 ; P5 (calque 040_meubles) | À confirmer | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-02 | Surcharges d'exploitation par zone | 250 daN/m² (cabinet paramédical / bureaux) ; toiture 80 daN/m² | daN/m² | D-03 (CR 20/10/2026) ; P2 p16 | Décision | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-03 | Poids propres des complexes de plancher | Complexes A/B chiffrés (P2) ; dallage neuf décrit (P1) ; récap EXE à produire | daN/m² | P2 p10-13 ; P1 p34-36 | À confirmer | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-04 | Poids propres de toiture | Charge charpente 150 daN/ml ; complexe de couverture non décrit | daN/ml | P2 p16-17 | À confirmer | B-21, B-44 |
| CHG-05 | Neige | Région A1 ; sk 45 daN/m² ; altitude < 200 m | daN/m² | P3 DCE f1 p1 (NEIGE) ; P1 p13 | Contractuelle | B-21, B-44 |
| CHG-06 | Vent | Zone 2 ; vitesse de base 24 m/s ; coef. direction 1 (10°-150° : 0,70) ; coef. saison 1 (avr-sept : 0,80) ; catégorie terrain 1 | m/s | P3 DCE f1 p1 (VENT) ; P1 p13 | Contractuelle | B-21, B-44, B-45 |
| CHG-07 | Sismique | Zone 1 ; classe de sol III ; catégorie bâtiment II | — | P3 DCE f1 p1 (SEISME) ; P1 p13 | Contractuelle | B-42, B-46 |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | Cloisons 7/10/12 cm dessinées ; équipements lourds / charges ponctuelles non chiffrés | cm | P4 p9 ; P5 (calque 020_cloisons) | À confirmer | B-21, B-43, B-47, B-48 |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées | 2 jours ouvrés (délai carnet par défaut) ; délai contractuel réel CCAP non reçu | jours ouvrés | CARNAC §3 (défaut) ; CCAP non reçu | À confirmer | B-03, B-22, B-60, B-64 |
| DEC-07 | Prescriptions chantier (ENC) et Points d'Arrêt (PA-xx) | PA-01 ouvert — contrôle d'arase de fouille ; prescriptions ENC complètes à produire | — | D-06 (CR 20/10/2026) | Décision | B-03, B-24, B-34, B-40, B-41, B-44, B-46, B-60, B-64 |
| DOC-01 | Inventaire des pièces (fichier, folio, indice, échelle) | 5 pièces de projet + carnet de protocole ; B-00 Ind B | — | B-00 §1 (DOC-01) | Contractuelle | B-00, B-01 |
| DOC-02 | Plans architecte vectoriels | DXF P5 (Flora RDC/R+1) + PDF vectoriel P4 (29 planches) | — | P5 DXF Ind C ; P4 Ind C 13/03/2026 ; écart C-08 (ouvert) | À confirmer | B-20, B-30, B-31, B-32, B-33, B-60 |
| DOC-03 | Plans BET structure | PDF P3, 4 folios, indices hétérogènes C/-/-/B, sans vecteur coffrage ni notes PRO-DCE | — | P3 folios 1-4 ; écart C-09 (ouvert) | À confirmer | B-10, B-11, B-20 |
| DOC-04 | CCTP / pièces contractuelles | P1 — CCTP LOT 01, V1 stade PRO, 38 p., 13/03/2026 | — | P1 couverture + sommaire | Contractuelle | B-10, B-14 |
| DOC-05 | Diagnostic structure de l'existant | P2 — DIAG structure, 19 p., 9 désordres, campagne de sondages | — | P2 couverture + §3-5 | Contractuelle | B-11, B-23, B-24 |
| DOC-06 | Rapport géotechnique | G2 AVP GEOEXPERTS n° 25.13646/ES/GIF du 22/01/2026 non reçu ; paramètres de dimensionnement officialisés par D-06 | — | P3 f1 p1 ; P1 p13 ; D-06 | Décision | B-12, B-41 |
| EXI-01 | Sections des éléments existants | Solives 8×18 ; poutre 20×15 ; IPE160 ; IPE330 ; portiques 23×15 / 15×15 (éléments sondés/calculés) ; inventaire exhaustif et fondations inconnus | cm | P2 p10-17 | À confirmer | B-20, B-23, B-24, B-44, B-46, B-49 |
| EXI-02 | Pathologies relevées | 9 désordres D1 à D9 localisés et décrits | — | P2 p5-9 | Contractuelle | B-23 |
| EXI-03 | Résistance des matériaux existants | Bois C18 (planchers) et C24 (portiques) posés par hypothèse d'âge, sans essais | — | P2 p10-17 | À confirmer | B-20, B-24, B-44, B-46, B-49 |
| EXI-04 | Résultats de sondages destructifs / semi-destructifs | Campagne de sondages des planchers réalisée ; aucun sondage de fondations ni de maçonneries porteuses | — | P2 §4 (p9-10) | À confirmer | B-24, B-41 |
| GEO-01 | Emprise / contour du bâtiment | Emprise Flora dans P4 p4-6 et blocs géomètre P5 | — | P4 p4-6 ; P5 (blocs géomètre) | Contractuelle | B-20, B-21, B-23, B-33, B-40, B-43, B-44, B-47, B-48, B-60 |
| GEO-02 | Axes et trames | Calque 090_repères-axes (9 entités) ; trame structurelle formelle absente | — | P5 calque 090_repères-axes | À confirmer | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 |
| GEO-03 | Épaisseurs murs | Cloisons 7/10/12 cm ; épaisseur des murs porteurs non éprouvée partout | cm | P4 p9 ; P5 | À confirmer | B-20, B-21, B-23, B-33, B-40, B-46, B-49, B-60 |
| GEO-04 | Positions poteaux | Positions P1/P2/P3 graphiques ; coordonnées EXE à établir | — | P3 folio 1 ; P5 (bloc « Murs porteurs selon geometre projet ») | À confirmer | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 |
| GEO-05 | Baies et ouvertures | Nomenclatures des portes P4 p23 et menuiseries P4 p24-25 ; calque 030_menuiserie P5 | — | P4 p23-25 ; P5 calque 030_menuiserie | Contractuelle | B-20, B-23, B-33, B-40, B-42, B-46, B-47, B-49, B-60 |
| GEO-06 | Unités du fichier source (cm/m/mm) | $INSUNITS = 5 (cm) détecté par script ; confirmation obligatoire au calage | — | P5 ($INSUNITS, script ezdxf) | À confirmer | B-30, B-32 |
| GEO-14 | Différentiel EXISTANT / DÉMOLITION / PROJET | Trois états présents (P4 p4-6 ; blocs R+1 Existant/Projet ; calque 102_demol) ; différentiel formel non produit | — | P4 p4-6 ; P5 calque 102_demol | À confirmer | B-11, B-13, B-20, B-31, B-32, B-33 |
| ID-01 | Code projet | JYCROISSY — site n° 208 / EVEN 24.09.356E / EICP 014-2024-08 | — | P1 ; P2 ; P3 ; P4 ; P5 (cartouches) | Contractuelle | B-00, B-01, B-02, B-03, B-04, B-10-B-15, B-20-B-25, B-30-B-34, B-40-B-50, B-60-B-64, B-70-B-72, T-01-T-04 |
| ID-02 | Intitulé de l'opération | Aménagement d'un cabinet paramédical dans le pavillon Flora | — | P1 ; P2 ; P3 | Contractuelle | B-00, B-10-B-15, B-20-B-25, B-30-B-34, B-40-B-50, B-60-B-64, B-70-B-72, T-01-T-04 |
| ID-05 | Indice du dossier en vigueur | Indices hétérogènes (archi Ind C, CCTP V1, DIAG « - », folios BET C/-/-/B) ; indice EXE à créer | — | P3 folios 1-4 ; P4 ; P1 ; écart C-09 (ouvert) | À confirmer | B-03, B-64, B-71, B-72 |
| ID-07 | Date de l'étude | Pièces datées 2025-2026 ; étude en cours depuis le 23/10/2026 | — | P1 (13/03/2026) ; P2 (24/03/2025) ; P3 (16/03/2026) | À confirmer | B-03 |
| LIV-04 | Cartouche | Cartouches Truelle (archi) / EVEN (structure) existantes ; cartouche EXE entreprise à créer | — | P3 ; P4 ; P5 | À confirmer | B-60 |
| LIV-05 | Langue et unités | Français ; unités SI (cm dans le DXF, daN/m², MPa) | — | P5 ($INSUNITS=5) ; P3 f1 p1 | Contractuelle | B-60 |
| MAT-01 | Classe de résistance du béton | C25/30 (structure) ; C16/20 (gros béton) | MPa | P3 DCE f1 p1 (Tableau des bétons) | Contractuelle | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 |
| MAT-02 | Classe d'exposition | XC1 / XC2 / XF1 / XC4 ; agressivité sol XA4 | — | P3 DCE f1 p1 ; P3 f3 p4 (XA4) ; P1 p33 | Contractuelle | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 |
| MAT-03 | Enrobage nominal | Classe structurale S4 ; enrobage nominal 30 mm | mm | P3 DCE f1 p1 (fragmentaire) | À confirmer | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 |
| MAT-04 | Nuance d'acier BA | HA S500 (fyk 500 MPa) ; aciers lisses S220 | MPa | P3 DCE f1 p1 (Armatures) | Contractuelle | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 |
| MAT-05 | Nuance d'acier de charpente métallique | Acier de charpente S275 | — | P3 DCE f1 p1 (METAL) | Contractuelle | B-45, B-49, B-50, B-62 |
| MAT-06 | Classe de bois | C18 (planchers) ; C24 (portiques) — hypothèses du diag sur critère d'âge | — | P2 p10-17 | À confirmer | B-43, B-44, B-50, B-62 |
| MAT-07 | Nature et résistance de la maçonnerie existante | Briques, agglomérés, pierre dure (soubassement) ; résistances non mesurées | — | P2 p3, p17, p18 | À confirmer | B-46, B-49, B-50 |
| MAT-08 | Classe de service et durée de charge | EC5 appliqué par P2 ; classe de service non explicitée (présomption classe 1 intérieur chauffé) | — | P2 ; présomption | À confirmer | B-43, B-44 |
| MAT-09 | Classe de bloc de maçonnerie neuve (NF EN 771-3) | Blocs pleins 30/40 B80 ; blocs creux 50 B40 | cm | P1 p9 | Contractuelle | B-46, B-50, B-62 |
| MAT-10 | Classe de mortier (M2,5 à M10) | Mortiers hydrofugé / bâtard / chaux cités ; classe M2,5-M10 non spécifiée | — | P1 | À confirmer | B-46, B-50, B-62 |
| MAT-11 | Type de maçonnerie (chaînée / armée / non armée) | Maçonnerie neuve avec chaînages BA ; typologie formelle à confirmer | — | P1 p23, p36 | À confirmer | B-46, B-50, B-62 |
| MAT-12 | Présence et nature des chaînages existants | Présomption d'absence de chaînage (bâtiment ancien, non sondé) | — | P2 ; présomption | À confirmer | B-46 |
| NIV-01 | Niveau TN | TN déclaré variable (P1 p14) ; altimétrie Z ≈ 201 | m | P1 p14 ; P4 p5 | À confirmer | B-40 |
| NIV-02 | Niveaux planchers | Z RDC 201,0-201,3 ; Z R+1 203,6-204,4 ; table de niveaux formelle non établie | m | P4 p4-6 ; P5 | À confirmer | B-42, B-43, B-47, B-48, B-60 |
| NIV-03 | Hauteurs libres | hsp/hsfp recensées 2,16 à 3,25 m | m | P4/P5 | Contractuelle | B-42, B-47 |
| NIV-04 | Niveau assise | Assise en alluvions anciennes ; ancrage prescrit 50 cm ; contrôle d'arase en fouille PA-01 | m | D-01 / D-06 (CR 20/10/2026) ; PA-01 | Décision | B-40 |
| NIV-05 | Niveau fini dallage | Fini dallage RDC Z ≈ 201,0 avec pentes et décaissés ; niveau fini formel à établir | m | P4 p5 | À confirmer | B-43, B-60 |
| NIV-06 | Épaisseurs plancher | Épaisseurs planchers A/B connues ; dallage neuf « selon étude BA » non fixé | cm | P2 ; P1 p34-36 | À confirmer | B-43, B-48 |
| SEC-01 | Degré coupe-feu exigé par élément | Principe encoffrement ; peinture intumescente et vermiculite ; degrés CF/SF non chiffrés (champs vierges) ; dimensionnement feu hors périmètre CARNAC | — | P3 f1 p1 ; P1 p26 | À confirmer | B-25, B-42, B-43, B-47, B-48, B-49 |
| SEC-03 | Classement termites de la commune | Barrière anti-termites prescrite (présomption zone exposée) ; classement préfectoral non cité | — | P1 p34 | À confirmer | B-43 |
| SIT-04 | Voisinage | Mitoyenneté signalée ; nature précise des mitoyens non détaillée | — | P1 p10 | À confirmer | B-40 |
| SIT-05 | Emprise fouille | Fouilles en rigoles selon plans BET ; emprise précise à dessiner | — | P1 p26 ; P3 | À confirmer | B-40 |
| SOL-01 | Contrainte admissible ELS | qELS ≤ 0,30 MPa | MPa | D-06 (CR 20/10/2026) ; P3 f1 p1 ; P1 p13 | Décision | B-12, B-20, B-40, B-41, B-43 |
| SOL-02 | Contrainte admissible ELU | qELU ≤ 0,49 MPa | MPa | D-06 (CR 20/10/2026) ; P1 p13 | Décision | B-20, B-40, B-41 |
| SOL-03 | Profondeur de bon sol / ancrage minimal | Ancrage ≥ 0,50 m dans les alluvions anciennes ; contrôle d'arase en fouille | m | D-01 / D-06 (CR 20/10/2026) ; PA-01 | Décision | B-20, B-40, B-41 |
| SOL-05 | Classe d'agressivité du sol (XA) | XA4 ; géotextile anti-contaminant sous couche de forme | — | P3 f1 p1 et f3 p4 ; P1 p33 | Contractuelle | B-20, B-40, B-41, B-43 |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | G2 AVP existant chez le client mais non reçu ; G3 absent | — | D-06 ; P3 f1 p1 | À confirmer | B-12, B-41 |
| STR-01 | Système global de contreventement / centre de torsion | Éléments Stab1 (entretoises anti-dévers IPE) repérés P3 ; contreventement global et centre de torsion non synthétisés | — | P3 folio 1 | À confirmer | B-20, B-21, B-25, B-42, B-44, B-45, B-46 |
| STR-03 | Carnet des réservations et trémies tous corps d'état | Percements et réservations dispersés ; carnet consolidé tous corps d'état inexistant | — | P1 p23-24 ; P5 calque 080_plomb-cvc | À confirmer | B-32, B-34, B-42, B-43, B-48, B-60 |

### Niveaux de fiabilité

- **Contractuelle** — valeur issue d'une pièce du marché ; ne se conteste pas unilatéralement.
- **Décision** — valeur issue du RDR (numéro, auteur, date cités : D-01…D-13, CR 20/10/2026).
- **À confirmer** — valeur de travail / donnée fragmentaire ; à valider avant exécution (le livrable porte une réserve).

---

## TABLEAU 2 — VERROU (variables sans valeur)

*17 variables.* Aucune valeur n'est proposée (règle 4) ; la contradiction n'est jamais tranchée en silence (règle 6).

| Code VERROU | Libellé | Brique suspendue | Voie d'obtention proposée | Responsable pressenti |
|---|---|---|---|---|
| DEC-01 | Mode attribué à chaque brique | B-70 | Décision MOA / MOE (inscription au RDR) | BET d'exécution (MOE) |
| DEC-02 | Décisions inscrites au RDR (valeur, auteur, date) | B-03, B-64, B-70, B-72, T-03 | Ouverture du RDR officiel à quatre registres | BET d'exécution (MOE) |
| DEC-03 | Verrous ouverts (donnée, brique suspendue, responsable) | B-03, B-04, B-13, B-15, B-64, B-70, B-72, T-03, T-04 | Registre des verrous à ouvrir | BET d'exécution (MOE) |
| DEC-04 | Documents supersédés (indice, date) | B-71, B-72 | Suivi de vie série des documents | BET d'exécution (MOE) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx | B-03, B-20, B-22, B-25, B-34, B-40, B-60, B-64, B-70 | Production H-xx via B-22 (INTERNE-GO) | BET d'exécution (MOE) |
| DOC-08 | Plans de récolement / DOE | B-11, B-72 | Récolement / DOE en clôture de mission | BET d'exécution (MOE) |
| EXI-05 | Contrainte admissible transmise à l'existant | B-23, B-46 | Calculs B-23/B-46 sur base EXI-03 (INTERNE-GO) | BET d'exécution (MOE) |
| GEO-07 | Transformation du fichier (rotation, translation, échelle) | B-30 | Détermination par calage des sources (INTERNE-GO) | BET d'exécution (MOE) |
| GEO-08 | Points de calage identifiés (≥ 3 non alignés) | B-30, B-31 | Identification lors du calage (INTERNE-GO) | BET d'exécution (MOE) |
| GEO-10 | Seuils d'épaisseur de présomption porteuse | B-32 | Fixation par méthode d'exploitation vectorielle (INTERNE-GO) | BET d'exécution (MOE) |
| GEO-11 | Superposition des niveaux (recouvrement, écart d'axe) | B-32 | Fixation par méthode de superposition (INTERNE-GO) | BET d'exécution (MOE) |
| GEO-12 | Seuils géométriques du projet (résidu de calage, écarts) | B-30 | Fixation par méthode de calage (INTERNE-GO) | BET d'exécution (MOE) |
| GEO-13 | Matrice de recalage multi-sources vers le RSU | B-13, B-20, B-30, B-31, B-32, B-34 | Construction du RSU (INTERNE-GO) | BET d'exécution (MOE) |
| LIV-01 | Conventions de calques DXF | B-60 | Définition (référence annexe A CARNAC) | BET d'exécution (MOE) |
| LIV-02 | Échelles autorisées | B-60 | À bâtir à partir des échelles des pièces reçues | BET d'exécution (MOE) |
| LIV-03 | Formats de sortie et nommage des fichiers | B-60 | Charte à définir (DOE DXF/DWG exigé P1 p37) | BET d'exécution (MOE) |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | B-20, B-30, B-32, B-43, B-60 | Production B-02 (INTERNE-GO) — table présentée au §NIV-07 de cette FDC | BET d'exécution (MOE) |

---

## §NIV-07 — Table de correspondance des niveaux et des épaisseurs

Format imposé par l'annexe O §9.5 du CARNAC : aucune cote de niveau n'est reprise d'un plan architecte sans passer par cette table ; un écart non renseigné est un écart bloquant pour B-43 et B-60.

### a) Correspondance Plan Archi N ↔ PB / PH (D-13)

| Plan architecte | Folio / page | Niveau | Plancher bas (PB) | Plancher haut (PH) | Source |
|---|---|---|---|---|---|
| « PH RDC » (vue en plan) | P3 folio 1 (indice C) | R+1 | — | PH R+1 = plancher haut R+1 | D-13 ; nomenclature P3 f1 |
| « PB RDC » (vue en plan) | P3 folio 3 (indice « - ») | RDC | PB RDC = plancher bas RDC | — | D-13 ; nomenclature P3 f3 |
| « Charpente » (vue en plan) | P3 folio 2 (indice « - ») | combles | — | — | P3 f2 |
| Plans existant / projet RDC | P4 p4-6 | RDC | PB RDC Z ≈ 201,0-201,3 | — | P4 p4-6 ; P5 |
| Plans existant / projet R+1 | P4 p4-6 | R+1 | — | PH R+1 Z ≈ 203,6-204,4 | P4 p4-6 ; P5 |

### b) Cotes PB / PH / ASB / Fini

| Niveau N | Cote PB_N | Cote PH_N | Cote ASB_N | Cote FINI_N | Source |
|---|---|---|---|---|---|
| RDC | 201,0-201,3 (P4 p4-6) | — | VERROU | 201,0 (fini dallage, P4 p5) | P4 p4-6, p5 |
| R+1 | — | 203,6-204,4 (P4 p4-6) | VERROU | VERROU | P4 p4-6 ; complexe non levé |

### c) Épaisseurs de complexe (FINI − ASB)

| Système | Description du complexe | Source | Épaisseur de complexe |
|---|---|---|---|
| Plancher existant type A (bois) | solives 8×18 + lambourde/parquet + lattis-plâtre | P2 p10-11 | VERROU (épaisseur de complexe non cotée) |
| Plancher existant type B (mixte) | hourdis brique 7 cm + PS 8 cm + chape 10 cm | P2 p12-13 | 25 cm (somme des couches citées, P2) |
| Dallage neuf RDC projet | coulé en place, fond de forme 40 cm, XPS 105 mm | P1 p33-36 ; P3 f1 p1 | VERROU (épaisseur « selon étude BA » non fixée) |
| Planchers neufs R+1 | non décrits en pièces | — | VERROU |

> Le nu brut ASB et les cotes FINI des niveaux non levés restent **VERROU** : aucune épaisseur n'est supputée. Le dallage neuf « selon étude BA » (P1 p34-36) n'est pas encore fixé.

---

## ANNEXE — Variables de référence (hors FDC)

Règle 1 de la fiche B-02 : seules les variables lues par au moins une brique activée figurent en FDC. Les 17 variables de référence ci-dessous ne consomment aucune brique et ne figurent donc ni dans le tableau 1 ni dans le tableau 2 ; elles sont portées à titre documentaire.

| Code | Libellé | Valeur / source |
|---|---|---|
| AC-01 | MOA | UNIVI (D-05) ; CCTP P1 p1, cartouches P4 |
| AC-02 | Architecte | Truelle Architectes (S. Iglesias), P3/P4/P1 |
| AC-06 | Bureau de contrôle | Rôle aux cartouches P3 ; organisme non nommé (PARTIELLE) |
| GEO-09 | Échelle tracé | 1/500, 1/100, 1/50, 1/50-1/20 (P3/P4) |
| ID-03 | Adresse | 11 rue Paul Demange, 78290 Croissy-sur-Seine (D-04) |
| ID-04 | Nature | Réhabilitation de bâtiment existant, mission EXE/PAC |
| ID-06 | Phase | Pièces DCE/PRO ; mission EXE/PAC (P1 §01.2.1.1.6) |
| SEC-02 | Catégorie ERP | ERP cabinet paramédical ; catégorie/effectif non indiqués (PARTIELLE) |
| SEC-04 | Classe structurale | S4 (P3 f1, fragmentaire) (PARTIELLE) |
| SEC-05 | PMR | Sanitaire PMR (P4 p14), rampe (P1 p36), cercles PMR dans le DXF |
| OUT-01 | Environnement d'exécution | venv ; pypdf 6.21.2 ; ezdxf 1.4.5 ; workspace |
| OUT-02 | Script versionné | extraction_b00.py, build_b01.py, build_b02.py |
| OUT-03 | Journal d'exécution | journal_B00.md, journal_B01.md, journal_B02.md |
| OUT-04 | Rendu PNG 300 dpi | À venir (B-30/B-31) (PARTIELLE) |
| SIT-01 | Site occupé | EHPAD en exploitation pendant les travaux (P1, P4 p28) |
| SIT-02 | Contraintes de site | Base vie Gardien, PGC/PPSPS, constat d'huissier, mitoyenneté (P1 p10-12, P4 p28) |
| SIT-03 | Accès | Accès rue Paul Demange ; plan d'installation P4 p28 |

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère de la fiche B-02 | Statut |
|---|---|
| Chaque ligne a une source citée ou est marquée VERROU | ✅ (tableau 1 : toutes les lignes citent une pièce/folio ; tableau 2 : VERROU) |
| Aucun champ renseigné sans niveau de fiabilité | ✅ (3 niveaux utilisés) |
| Les VERROU sont en fin de fiche avec voie d'obtention | ✅ (tableau 2) |
| Aucune contradiction tranchée silencieusement | ✅ (les écarts C-06/C-08/C-09 restent ouverts) |
| Aucune variable non lue par une brique n'est présente en FDC | ✅ (variables de référence en annexe hors FDC) |
| Zéro placeholder (V7) | ✅

**Brique B-02 livrée — en attente de votre GO pour B-03 (RDR).** La FDC validée sera annexée au RDR comme décision D-xx datée.
