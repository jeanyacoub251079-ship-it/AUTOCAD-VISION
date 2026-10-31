# B-01 — MATRICE DE PÉRIMÈTRE ET DE DISPONIBILITÉ (MPD) — JYCROISSY

| Champ | Valeur |
|---|---|
| Opération | JYCROISSY — Aménagement d'un cabinet paramédical, pavillon Flora, EHPAD La Roseraie, 11 rue Paul Demange, Croissy-sur-Seine (D-04) |
| Carnet | CARNAC v3.0.2 — fiche `02_PHASE_0_CADRAGE/B-01_MPD.md` |
| Indice | **Ind A — 2026-10-23** (proposition initiale, aucune validation humaine encore acquise) |
| Entrées | B-00 Ind B, pré-RDR (D-01…D-06, PA-01), dictionnaire des 106 variables |
| CFG-01 | **CFG-2** (BET structure MOE en PDF, sans vecteur coffrage) — repris de B-00 |
| CFG-02 (proposition) | **Gabarit M** — bâtiment unitaire, emprise très inférieure à 2 500 m², plus de cinq porteurs (P1/P2/P3, F1-F4, R1-R3, sommiers), sans joint de dilatation ni sous-sol pour Flora ; voie standard en six phases |
| CFG-03 (proposition) | Un bloc structurel unique « Flora », sans JD ; niveaux : fondations/soubassements → PH RDC → plancher haut RDC/palier → PB R+1 → charpente/combles (nomenclature P3) ; statut PARTIELLE, formalisation en B-20/B-30 |
| Statut des propositions | **Tu PROPOSES, je VALIDE** : aucun statut n'est définitif avant validation explicite ; les NON NÉCESSAIRE appellent une validation ligne par ligne (§3) |

> Règles tenues : jamais de NON NÉCESSAIRE justifié par une indisponibilité (motif de périmètre obligatoire) ; aucun mode COMPLET sur variable BLOQUANTE ; aucune valeur de repli ; chaque ligne cite sa source ou sa raison d'absence. Machine-readable : `MPD_jycroissy.csv` ; générateur/validateur : `../00_SUPPORTS/build_b01.py`.

---

## 1. MATRICE COMPLÈTE (106 variables, 8 colonnes)


### Famille Acteurs

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| AC-01 | MOA | **FOURNIE** | — | UNIVI retenu MOA (D-05) ; CCTP P1 p1, cartouches P4 | — (variable de référence) | COMPLET (référence) |
| AC-02 | Architecte | **FOURNIE** | — | Truelle Architectes (S. Iglesias), P3/P4/P1 | — (variable de référence) | COMPLET (référence) |
| AC-03 | BET structure de conception | **FOURNIE** | — | EVEN STRUCTURES, BET structure MOE existant (P2 DIAG, P3 DCE) ; CFG-2 : livraisons PDF sans vecteur coffrage (voir DOC-03) | B-20 | COMPLET transcription CFG-2 ; compléments locaux INTERNE-GO (B-20) |
| AC-06 | Bureau de contrôle | **PARTIELLE** | — | Rôle « Bureau de contrôle » aux cartouches P3 mais organisme non nommé dans aucune pièce reçue ; variable de référence, ne suspend aucune brique | — (variable de référence) | PARTIEL-DÉCLARÉ (demande à émettre) |

### Famille Configuration

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | **FOURNIE** | — | CFG-2 qualifiée en B-00 Ind B §5 | B-00, B-01, B-20, B-60 | COMPLET |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | **FOURNIE** | — | Proposition B-01 : gabarit M (bâtiment unitaire, emprise < 2 500 m², plus de 5 porteurs, sans joint de dilatation ni sous-sol Flora) | B-01, B-04, B-25, B-34, B-60 | COMPLET (proposition à valider) |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | **PARTIELLE** | — | Niveaux repérables (PH RDC, PB RDC, Charpente, fondations P3 ; RDC/R+1/combles P4) mais découpage structurel formel non établi | B-01, B-20, B-21, B-25, B-30, B-60 | PARTIEL-DÉCLARÉ ; formalisation B-20/B-30 |

### Famille Charges

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| CHG-01 | Usage des locaux par zone (catégories EC1) | **PARTIELLE** | — | Usages nommés par pièce (P4 p6, P5 : box kiné, bureaux, plateau technique, salle de sport) ; catégories EC1 non attribuées formellement | B-21, B-42, B-43, B-45, B-47, B-48, B-49 | PARTIEL-DÉCLARÉ ; B-21/B-22 |
| CHG-02 | Surcharges d'exploitation par zone | **PARTIELLE** | — | 250 daN/m² global officiel (D-03) ; toiture 80 daN/m² (P2 p16) ; ventilation par zone (sanitaires, circulations, stockage) non établie | B-21, B-42, B-43, B-45, B-47, B-48, B-49 | PARTIEL-DÉCLARÉ (D-03 au RDR) ; B-21 |
| CHG-03 | Poids propres des complexes de plancher | **PARTIELLE** | — | Complexes existants A/B documentés et chiffrés (P2 p10-13) ; dallage neuf décrit (P1 p34-36) ; récapitulatif EXE à produire | B-21, B-42, B-43, B-45, B-47, B-48, B-49 | PARTIEL-DÉCLARÉ ; B-21 |
| CHG-04 | Poids propres de toiture | **PARTIELLE** | — | Charge charpente 150 daN/ml reprise (P2 p16-17) ; complexe de couverture (tuiles/étanchéité) non décrit | B-21, B-44 | PARTIEL-DÉCLARÉ ; B-21/B-44 |
| CHG-05 | Neige | **FOURNIE** | — | Neige A1, sk 45 daN/m², altitude < 200 m (P3 p1, P1 p13) | B-21, B-44 | COMPLET |
| CHG-06 | Vent | **FOURNIE** | — | Vent zone 2, vb 24 m/s, coefficients direction/saison (P3 p1, P1 p13) | B-21, B-44, B-45 | COMPLET |
| CHG-07 | Sismique (si applicable) | **FOURNIE** | — | Séisme zone 1, classe de sol III, classe bâtiment II (P3 p1, P1 p13) | B-42, B-46 | COMPLET |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | **PARTIELLE** | — | Cloisons 7/10/12 cm dessinées (P4 p9, P5) ; équipements lourds et charges ponctuelles non chiffrés | B-21, B-43, B-47, B-48 | PARTIEL-DÉCLARÉ ; B-21 |

### Famille Décision/pilotage

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| DEC-01 | Mode attribué à chaque brique | **À PRODUIRE PAR GO** | Modes des briques fixés par la MPD validée | Aucune source projet : produit de la présente MPD | B-70 | INTERNE-GO (B-01, suivi B-70) |
| DEC-02 | Décisions inscrites au RDR (valeur déclarée, auteur, date) | **À PRODUIRE PAR GO** | RDR officiel à ouvrir | Pré-RDR existant (D-01…D-06, PA-01) ; RDR à quatre registres non encore ouvert | B-03, B-64, B-70, B-72, T-03 | INTERNE-GO (B-03) |
| DEC-03 | Verrous ouverts (donnée, brique suspendue, responsable) | **À PRODUIRE PAR GO** | Registre des verrous à ouvrir | Aucun verrou formel encore enregistré hors pré-RDR | B-03, B-04, B-13, B-15, B-64, B-70, B-72, T-03, T-04 | INTERNE-GO (B-03/B-04) |
| DEC-04 | Documents supersédés (indice, date) | **À PRODUIRE PAR GO** | Suivi des documents supersédés | Aucun document supersédé à ce jour ; suivi de vie série plus tard | B-71, B-72 | INTERNE-GO (B-71/B-72) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | **À PRODUIRE PAR GO** | Hypothèses notifiées H-xx à produire | Aucune H-xx à ce jour (les inconnues sont passées en D-xx/PA-01) | B-03, B-20, B-22, B-25, B-34, B-40, B-60, B-64, B-70 | INTERNE-GO (B-22) |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | **PARTIELLE** | — | Délai carnet par défaut 2 jours ouvrés (CARNAC §3) ; délai contractuel réel dans CCAP non reçu | B-03, B-22, B-60, B-64 | PARTIEL-DÉCLARÉ |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | **PARTIELLE** | — | PA-01 ouvert (contrôle d'arase de fouille, D-06) ; prescriptions ENC complètes à produire au fil des briques | B-03, B-24, B-34, B-40, B-41, B-44, B-46, B-60, B-64 | PARTIEL-DÉCLARÉ ; B-24/B-34/B-40 |

### Famille Documents

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| DOC-01 | Inventaire des pièces (fichier, folio, indice, échelle) | **FOURNIE** | — | Inventaire B-00 Ind B (5 pièces de projet + carnet) | B-00, B-01 | COMPLET |
| DOC-02 | Plans architecte vectoriels | **PARTIELLE** | — | DXF P5 natif R2018 mais limité à Flora RDC/R+1 (écart C-08) ; les autres planches n'existent qu'en PDF vectoriel P4 | B-20, B-30, B-31, B-32, B-33, B-60 | PARTIEL-DÉCLARÉ ; B-30 |
| DOC-03 | Plans BET structure (si disponibles) | **PARTIELLE** | — | Plans BET P3 en PDF seulement, 4 folios, indices hétérogènes C/-/-/B (C-09), sans vecteur coffrage ni notes PRO-DCE | B-10, B-11, B-20 | PARTIEL-DÉCLARÉ ; CFG-2, B-10/B-11/B-20 |
| DOC-04 | CCTP / pièces contractuelles | **FOURNIE** | — | CCTP P1, V1 stade PRO, 38 pages, intégralement lu | B-10, B-14 | COMPLET ; B-10/B-14 |
| DOC-05 | Diagnostic structure de l'existant | **FOURNIE** | — | Diagnostic P2 DIAG, 19 pages : 9 désordres, sondages, vérifications EC3/EC5 | B-11, B-23, B-24 | COMPLET ; B-11/B-23/B-24 |
| DOC-06 | Rapport géotechnique | **PARTIELLE** | — | G2 AVP GEOEXPERTS n° 25.13646/ES/GIF non reçu (volume) ; paramètres clés officialisés par D-06 | B-12, B-41 | PARTIEL-DÉCLARÉ (D-06 au RDR) ; B-12 |
| DOC-07 | Diagnostic amiante/plomb (cité en exemple v1.1, défini en v2.0) | **NON NÉCESSAIRE** | Périmètre : désamiantage et déplombage exclus des livrables CARNAC (§1.4) ; seules les contraintes de phasage/coordination sont remontées | Rapports amiante (31/12/2024) et plomb cités P1 p14-20 mais non joints ; exclusion de périmètre, pas défaut de disponibilité | — (variable de référence) | SANS OBJET (proposition à valider) |
| DOC-08 | Plans de récolement / DOE | **À PRODUIRE PAR GO** | Récolement/DOE à produire en clôture de mission | Aucun plan de récolement existant reçu ; P1 p37 exige le DOE avec plans DXF/DWG | B-11 | INTERNE-GO (B-72) ; B-11 s'appuie sur P2/P4/P5 |
| DOC-09 | Fiches techniques des prédalles | **NON NÉCESSAIRE** | Périmètre : aucune prédalle ni plancher préfabriqué dans l'opération (dallage coulé en place P1 p35 ; planchers existants conservés/renforcés) | Fiches techniques sans objet dans le projet | B-48, B-50 | SANS OBJET (proposition à valider) ; B-48 en SANS OBJET corrélatif |

### Famille Existant

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| EXI-01 | Sections des éléments existants | **PARTIELLE** | — | Sections connues des seuls éléments sondés/calculés (P2 : solives 8×18, poutre 20×15, IPE160, IPE330, portiques 23×15/15×15) ; inventaire exhaustif et fondations inconnus | B-20, B-23, B-24, B-44, B-46, B-49 | PARTIEL-DÉCLARÉ ; B-23/B-24 |
| EXI-02 | Pathologies relevées | **FOURNIE** | — | Neuf désordres D1-D9 localisés et décrits (P2 p5-9) | B-23 | COMPLET ; B-23 |
| EXI-03 | Résistance des matériaux existants | **PARTIELLE** | — | Caractéristiques conventionnelles C18/C24 posées par le diag sur critère d'âge, sans essais ; aucune mesure de résistance | B-20, B-24, B-44, B-46, B-49 | PARTIEL-DÉCLARÉ ; essais ENC/PA si inconnue physique (B-24) |
| EXI-04 | Résultats de sondages destructifs ou semi-destructifs | **PARTIELLE** | — | Campagne de sondages des planchers réalisée (P2 §4) ; aucun sondage de fondations ou de maçonneries porteuses | B-24, B-41 | PARTIEL-DÉCLARÉ ; B-24 |
| EXI-05 | Contrainte admissible transmise à l'existant | **À PRODUIRE PAR GO** | Contraintes admissibles transmises à l'existant à établir par nos vérifications | Non fournie : résulte des calculs B-23/B-46 sur base EXI-03, avec ENC si inconnue physique | B-23, B-46 | INTERNE-GO (B-23/B-46) |

### Famille Géométrie

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| GEO-01 | Emprise / contour du bâtiment | **FOURNIE** | — | Emprise et contour dans P4/P5, blocs géomètre du DXF | B-20, B-21, B-23, B-33, B-40, B-43, B-44, B-47, B-48, B-60 | COMPLET |
| GEO-02 | Axes et trames | **PARTIELLE** | — | Calque 090_repères-axes (9 entités) mais pas de trame structurelle formelle | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 | PARTIEL-DÉCLARÉ ; B-20/B-30 |
| GEO-03 | Épaisseurs murs | **PARTIELLE** | — | Épaisseurs de cloisons 7/10/12 cm (P4 p9, P5) ; épaisseur des murs porteurs non éprouvée partout | B-20, B-21, B-23, B-33, B-40, B-46, B-49, B-60 | PARTIEL-DÉCLARÉ ; B-20/B-32 |
| GEO-04 | Positions poteaux | **PARTIELLE** | — | Positions P1/P2/P3 graphiques (P3) et bloc « Murs porteurs selon geometre projet » (P5) ; coordonnées EXE à établir | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 | PARTIEL-DÉCLARÉ ; B-30 |
| GEO-05 | Baies et ouvertures | **FOURNIE** | — | Baies et menuiseries : nomenclatures P4 p23-25, calque 030_menuiserie P5 | B-20, B-23, B-33, B-40, B-42, B-46, B-47, B-49, B-60 | COMPLET |
| GEO-06 | Unités du fichier source (cm/m/mm) | **PARTIELLE** | — | $INSUNITS = 5 (cm) détecté par script ; confirmation obligatoire au calage | B-30, B-32 | PARTIEL-DÉCLARÉ ; B-30 |
| GEO-07 | Transformation du fichier (rotation, translation, échelle) | **À PRODUIRE PAR GO** | Transformation de recalage à déterminer | Non connue avant calage des sources | B-30, B-31 | INTERNE-GO (B-30) |
| GEO-08 | Points de calage identifiés (≥ 3 non alignés) | **À PRODUIRE PAR GO** | Points de calage ≥ 3 non alignés à identifier | Aucun point de calage encore posé | B-30, B-31 | INTERNE-GO (B-30/B-31) |
| GEO-09 | Échelle tracé | **FOURNIE** | — | Échelles aux cartouches 1/500, 1/100, 1/50, 1/50-1/20 (P3/P4) | — (variable de référence) | COMPLET (référence) |
| GEO-10 | Seuils d'épaisseur de présomption porteuse (seuil bas / seuil haut, par système constructif) | **À PRODUIRE PAR GO** | Seuils d'épaisseur de présomption porteuse à fixer | Paramètre méthode d'exploitation vectorielle, non fourni par le client | B-32 | INTERNE-GO (B-32) |
| GEO-11 | Superposition des niveaux : recouvrement minimal et écart maximal d'axe entre niveaux | **À PRODUIRE PAR GO** | Recouvrement minimal et écart d'axe entre niveaux à fixer | Paramètre méthode de superposition | B-32 | INTERNE-GO (B-32) |
| GEO-12 | Seuils géométriques du projet (résidu de calage, écarts de superposition et de position) | **À PRODUIRE PAR GO** | Seuils géométriques (résidu de calage, superposition) à fixer | Paramètre méthode de calage | B-30 | INTERNE-GO (B-30) |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | **À PRODUIRE PAR GO** | Matrice de recalage multi-sources vers le RSU à construire | RSU non encore créé | B-13, B-20, B-30, B-31, B-32, B-34 | INTERNE-GO (B-30/B-31) |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | **PARTIELLE** | — | Trois états EXISTANT/DÉMOLITION/PROJET présents (P4 p4-6 ; blocs R+1 Existant/Projet et calque 102_demol P5) ; différentiel formel non produit | B-11, B-13, B-20, B-31, B-32, B-33 | PARTIEL-DÉCLARÉ ; B-31/B-32 |

### Famille Identité

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| ID-01 | Code projet | **FOURNIE** | — | JYCROISSY ; codes projet 208 / EVEN 24.09.356E / EICP 014-2024-08 | B-00, B-01, B-02, B-03, B-04, B-10, B-11, B-12, B-13, B-14, B-15, B-20, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-34, B-40, B-41, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-50, B-60, B-62, B-64, B-70, B-71, B-72, T-01, T-02, T-03, T-04 | COMPLET |
| ID-02 | Intitulé de l'opération | **FOURNIE** | — | Aménagement d'un cabinet paramédical dans le pavillon Flora | B-00, B-10, B-11, B-12, B-13, B-14, B-15, B-20, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-34, B-40, B-41, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-50, B-60, B-62, B-64, B-70, B-71, B-72, T-01, T-02, T-03, T-04 | COMPLET |
| ID-03 | Adresse | **FOURNIE** | — | 11 rue Paul Demange, 78290 Croissy-sur-Seine (D-04) | — (variable de référence) | COMPLET (référence) |
| ID-04 | Nature | **FOURNIE** | — | Réhabilitation de bâtiment existant, mission EXE/PAC | — (variable de référence) | COMPLET (référence) |
| ID-05 | Indice du dossier en vigueur | **PARTIELLE** | — | Indices hétérogènes (C-09) : archi Ind C, CCTP V1, DIAG « - », folios BET C/-/-/B ; indice EXE à créer | B-03, B-64, B-71, B-72 | PARTIEL-DÉCLARÉ |
| ID-06 | Phase | **FOURNIE** | — | Pièces au stade DCE/PRO ; mission EXE/PAC (P1 §01.2.1.1.6) | — (variable de référence) | COMPLET (référence) |
| ID-07 | Date de l'étude | **FOURNIE** | — | Pièces datées 2025-2026 ; étude en cours depuis le 23/10/2026 | B-03 | COMPLET |

### Famille Livrables

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| LIV-01 | Conventions de calques DXF (préfixes, suffixes, règles d'usage) | **À PRODUIRE PAR GO** | Conventions de calques DXF des livrables à définir | Aucune convention client reçue ; référence annexe A CARNAC | B-60 | INTERNE-GO (B-60) |
| LIV-02 | Échelles autorisées | **À PRODUIRE PAR GO** | Échelles autorisées des livrables à définir | À bâtir à partir des échelles des pièces reçues | B-60 | INTERNE-GO (B-60) |
| LIV-03 | Formats de sortie (DXF, PDF, PNG) et nommage des fichiers | **À PRODUIRE PAR GO** | Formats et nommage des fichiers à définir | DOE en DXF/DWG exigé (P1 p37) mais charte non fournie | B-60 | INTERNE-GO (B-60) |
| LIV-04 | Cartouche | **PARTIELLE** | — | Cartouches Truelle/EVEN existants comme référence ; cartouche EXE entreprise à créer | B-60 | PARTIEL-DÉCLARÉ ; B-60 |
| LIV-05 | Langue et unités | **FOURNIE** | — | Langue française, unités SI (cm dans le DXF, daN/m², MPa) | B-60 | COMPLET |

### Famille Matériaux

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| MAT-01 | Classe de résistance du béton | **FOURNIE** | — | Bétons C25/30 (structure) et C16/20 (gros béton), P3 p1 | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 | COMPLET |
| MAT-02 | Classe d'exposition | **FOURNIE** | — | XC1/XC2/XF1/XC4 (P3 p1) et agressivité sol XA4 (P3, P1 p33) | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 | COMPLET |
| MAT-03 | Enrobage nominal | **PARTIELLE** | — | Classe structurale S4 et enrobage nominal 30 mm lisibles de façon fragmentée P3 p1 ; donnée à confirmer | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 | PARTIEL-DÉCLARÉ ; B-42 |
| MAT-04 | Nuance d'acier BA | **FOURNIE** | — | HA S500 (fyk 500 MPa), aciers lisses S220, P3 p1 | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 | COMPLET |
| MAT-05 | Nuance d'acier de charpente métallique | **FOURNIE** | — | Acier de charpente S275, P3 p1 | B-45, B-49, B-50, B-62 | COMPLET |
| MAT-06 | Classe de bois | **PARTIELLE** | — | Bois C18 (planchers) et C24 (portiques) : hypothèses du diag P2 sur critère d'âge, sans essais | B-43, B-44, B-50, B-62 | PARTIEL-DÉCLARÉ ; B-44 |
| MAT-07 | Nature et résistance de la maçonnerie existante | **PARTIELLE** | — | Natures connues (briques, agglomérés, pierre dure en soubassement) ; résistances non mesurées | B-46, B-49, B-50 | PARTIEL-DÉCLARÉ ; B-46 avec ENC si besoin |
| MAT-08 | Classe de service et durée de charge | **PARTIELLE** | — | EC5 appliqué par P2 ; classe de service non explicitée (présomption classe 1 en intérieur chauffé) | B-43, B-44 | PARTIEL-DÉCLARÉ ; B-43/B-44 |
| MAT-09 | Classe de bloc de maçonnerie neuve (NF EN 771-3) | **FOURNIE** | — | Blocs pleins 30/40 B80 et blocs creux 50 B40, P1 p9 | B-46, B-50, B-62 | COMPLET |
| MAT-10 | Classe de mortier (M2,5 à M10) | **PARTIELLE** | — | Mortiers hydrofugé/bâtard/chaux cités ; classe M2,5-M10 non spécifiée | B-46, B-50, B-62 | PARTIEL-DÉCLARÉ ; B-46 |
| MAT-11 | Type de maçonnerie (chaînée / armée / non armée) | **PARTIELLE** | — | Maçonnerie neuve avec chaînages BA (P1 p23, p36) ; typologie formelle à confirmer au calcul | B-46, B-50, B-62 | PARTIEL-DÉCLARÉ ; B-46 |
| MAT-12 | Présence et nature des chaînages existants | **PARTIELLE** | — | Maçonnerie existante non sondée, présomption d'absence de chaînage (bâtiment ancien) | B-46 | PARTIEL-DÉCLARÉ ; ENC B-24/B-46 |

### Famille Niveaux

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| NIV-01 | Niveau TN | **PARTIELLE** | — | TN déclaré variable (P1 p14) ; altimétrie Z ≈ 201 mais niveau TN précis non coté | B-40 | PARTIEL-DÉCLARÉ ; B-40 |
| NIV-02 | Niveaux planchers | **PARTIELLE** | — | Z par pièce 201,0-201,3 (RDC) et 203,6-204,4 (R+1) ; table de niveaux formelle non établie | B-42, B-43, B-47, B-48, B-60 | PARTIEL-DÉCLARÉ ; B-42/B-43 |
| NIV-03 | Hauteurs libres | **FOURNIE** | — | Hauteurs hsp/hsfp recensées 2,16 à 3,25 m (P4/P5) | B-42, B-47 | COMPLET |
| NIV-04 | Niveau assise | **PARTIELLE** | — | Assise en alluvions anciennes, ancrage prescrit 50 cm (D-01/D-06) ; niveau réel vérifié en fouille (PA-01) | B-40 | PARTIEL-DÉCLARÉ (PA-01) ; B-40 |
| NIV-05 | Niveau fini dallage | **PARTIELLE** | — | Fini dallage RDC Z ≈ 201,0 avec pentes et décaissés (P4 p5) ; niveau fini formel à établir | B-43, B-60 | PARTIEL-DÉCLARÉ ; B-43 |
| NIV-06 | Épaisseurs plancher | **PARTIELLE** | — | Épaisseurs des planchers A/B connues (P2) ; épaisseur du dallage neuf « selon étude BA » non fixée | B-43, B-48 | PARTIEL-DÉCLARÉ ; B-43/B-48 |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | **À PRODUIRE PAR GO** | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB/Fini à produire | Nomenclature P3 (PH RDC, PB RDC, Charpente) disponible mais table de correspondance inexistante | B-02, B-20, B-30, B-32, B-43, B-60 | INTERNE-GO (B-02) |

### Famille Outillage

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| OUT-01 | Environnement d'exécution (interpréteur, bibliothèques, persistance) | **FOURNIE** | — | Environnement démontré : venv, pypdf 6.21.2, ezdxf 1.4.5, persistance workspace | — (variable de référence) | COMPLET (référence) |
| OUT-02 | Script de production ou de calcul versionné avec le livrable | **FOURNIE** | — | Scripts versionnés extraction_b00.py et build_b01.py | — (variable de référence) | COMPLET (référence) |
| OUT-03 | Journal d'exécution et de relecture (comptages, résidus, écarts) | **FOURNIE** | — | Journaux journal_B00.md et pré-RDR | — (variable de référence) | COMPLET (référence) |
| OUT-04 | Rendu de contrôle visuel lu (PNG pleine page 300 dpi) | **PARTIELLE** | — | Aucun rendu PNG pleine page 300 dpi encore produit ; à venir B-30/B-31 | — (variable de référence) | PARTIEL-DÉCLARÉ |

### Famille Sécurité/incendie

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| SEC-01 | Degré coupe-feu exigé par élément | **PARTIELLE** | — | Principe encoffrement (P3), peinture intumescente et vermiculite (P1) ; degrés CF/SF non chiffrés (champs vierges P3 p1) ; dimensionnement de la protection feu exclu CARNAC | B-25, B-42, B-43, B-47, B-48, B-49 | PARTIEL-DÉCLARÉ (mention seule) |
| SEC-02 | Catégorie ERP | **PARTIELLE** | — | Activité ERP cabinet paramédical ; catégorie et effectif non indiqués | — (variable de référence) | PARTIEL-DÉCLARÉ (référence) |
| SEC-03 | Classement termites de la commune | **PARTIELLE** | — | Barrière anti-termites prescrite P1 p34 (présomption de zone exposée) ; classement préfectoral non cité ; donnée normative bornable | B-43 | PARTIEL-DÉCLARÉ ; H-xx éventuelle B-22 |
| SEC-04 | Classe structurale | **PARTIELLE** | — | Classe structurale S4 lisible de façon fragmentée P3 p1 ; à confirmer | — (variable de référence) | PARTIEL-DÉCLARÉ (référence) |
| SEC-05 | PMR | **FOURNIE** | — | Sanitaire PMR (P4 p14), rampe (P1 p36), cercles PMR dans le DXF | — (variable de référence) | COMPLET (référence) |

### Famille Site

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| SIT-01 | Site occupé | **FOURNIE** | — | EHPAD en exploitation pendant les travaux (P1, P4 p28) | — (variable de référence) | COMPLET (référence) |
| SIT-02 | Contraintes de site (cité en exemple v1.1, défini en v2.0) | **FOURNIE** | — | Base vie dans le Gardien, PGC/PPSPS, constat d'huissier, mitoyenneté (P1 p10-12, P4 p28) | — (variable de référence) | COMPLET (référence) |
| SIT-03 | Accès | **FOURNIE** | — | Accès par la rue Paul Demange, plan d'installation P4 p28 | — (variable de référence) | COMPLET (référence) |
| SIT-04 | Voisinage | **PARTIELLE** | — | Mitoyenneté signalée P1 p10 ; nature précise des mitoyens non détaillée | B-40 | PARTIEL-DÉCLARÉ ; B-40 |
| SIT-05 | Emprise fouille | **PARTIELLE** | — | Fouilles en rigoles selon plans BET ; emprise précise à dessiner | B-40 | PARTIEL-DÉCLARÉ ; B-40 |

### Famille Sol/géotechnique

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| SOL-01 | Contrainte admissible ELS | **FOURNIE** | — | qELS ≤ 0,30 MPa, officialisé D-06 (cohérent P3/P1) | B-12, B-20, B-40, B-41, B-43 | COMPLET (D-06) ; B-40 |
| SOL-02 | Contrainte admissible ELU | **FOURNIE** | — | qELU ≤ 0,49 MPa, officialisé D-06 (P1 p13) | B-20, B-40, B-41 | COMPLET (D-06) ; B-40 |
| SOL-03 | Profondeur de bon sol / ancrage minimal | **FOURNIE** | — | Ancrage 50 cm dans les alluvions anciennes (D-01/D-06), contrôle d'arase PA-01 | B-20, B-40, B-41 | COMPLET (prescrit) + PA-01 ; B-40 |
| SOL-04 | Nature et succession des couches | **BLOQUANTE** | — | Succession lithologique détaillée dans le G2 non reçu ; seule la couche d'alluvions anciennes est citée. Levée : fourniture du G2 ou reconnaissance en fouille (PA-01) | B-20, B-41 | SUSPENSION V11 (mode exécution interdit avant levée) ; B-12, B-20, B-41 |
| SOL-05 | Classe d'agressivité du sol (XA) | **FOURNIE** | — | Agressivité XA4, géotextile anti-contaminant (P3 p1/p4, P1 p33) | B-20, B-40, B-41, B-43 | COMPLET ; B-40/B-43 |
| SOL-06 | Nappe, hydrologie, drainage | **BLOQUANTE** | — | Nappe, hydrologie et drainage absents des paramètres transmis et des pièces reçues. Levée : G2 ou étude hydrogéologique | B-40, B-41 | SUSPENSION V11 (mode exécution interdit avant levée) ; B-40/B-41 |
| SOL-07 | Tassements admissibles / différentiels | **BLOQUANTE** | — | Tassements admissibles/différentiels non fournis. Levée : G2 (ou étude spécifique) | B-40, B-41 | SUSPENSION V11 (mode exécution interdit avant levée) ; B-40/B-41 |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | **PARTIELLE** | — | G2 AVP existant chez le client mais non reçu ; G3 absent (commande éventuelle hors production CARNAC, exclusion G1-G3) | B-12, B-41 | PARTIEL-DÉCLARÉ ; B-12 |

### Famille Structure

| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |
|---|---|---|---|---|---|---|
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | **PARTIELLE** | — | Éléments Stab1 (entretoises anti-dévers IPE) repérés P3 ; contreventement global et centre de torsion non synthétisés | B-20, B-21, B-25, B-42, B-44, B-45, B-46 | PARTIEL-DÉCLARÉ ; B-25 |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | **NON NÉCESSAIRE** | Périmètre : pas de sous-sol ni d'écran de soutènement pour Flora (fondations superficielles, dallage sur terre-plein). Sous réserve du périmètre Gardien/Bagatelle (écart C-07 toujours ouvert) | Aucun ouvrage de soutènement décrit dans les pièces Flora ; proposition liée au périmètre, pas à la disponibilité | B-12, B-25, B-40, B-41, B-42, B-43 | SANS OBJET (proposition à valider, réserve C-07) |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | **PARTIELLE** | — | Percements et réservations dispersés (P1 p23-24, calque 080_plomb-cvc P5) ; carnet consolidé tous corps d'état inexistant | B-32, B-34, B-42, B-43, B-48, B-60 | PARTIEL-DÉCLARÉ ; B-34 |

---

## 2. SYNTHÈSE RÉGLEMENTAIRE (trois paragraphes)

### 2.1 Variables BLOQUANTES et briques suspendues
3 variables bloquantes, toutes géotechniques et consécutives à la non-réception du rapport G2 complet (les paramètres transmis par D-06 préservent par ailleurs le dimensionnement aux contraintes) :

- **SOL-04 — Nature et succession des couches** : Succession lithologique détaillée dans le G2 non reçu ; seule la couche d'alluvions anciennes est citée. Levée : fourniture du G2 ou reconnaissance en fouille (PA-01) Briques impactées : B-20, B-41. Mode : SUSPENSION V11 (mode exécution interdit avant levée) ; B-12, B-20, B-41.
- **SOL-06 — Nappe, hydrologie, drainage** : Nappe, hydrologie et drainage absents des paramètres transmis et des pièces reçues. Levée : G2 ou étude hydrogéologique Briques impactées : B-40, B-41. Mode : SUSPENSION V11 (mode exécution interdit avant levée) ; B-40/B-41.
- **SOL-07 — Tassements admissibles / différentiels** : Tassements admissibles/différentiels non fournis. Levée : G2 (ou étude spécifique) Briques impactées : B-40, B-41. Mode : SUSPENSION V11 (mode exécution interdit avant levée) ; B-40/B-41.

Conséquences proposées (à entériner en B-04/PTD) : **B-12** exécutable en PARTIEL-DÉCLARÉ sur les seuls paramètres D-06, sections lithologie/nappe/tassements en attente ; **B-40 (fondations superficielles)** dimensionnable aux contraintes (SOL-01/02/03/05 FOURNIS) mais vérifications de tassement (SOL-07) et de nappe (SOL-06) suspendues, l'assise physique étant couverte par le point d'arrêt **PA-01** ; **B-41 (fondations profondes)** : aucune fondation profonde dans aucune pièce → proposition SANS OBJET qui sera instruite en B-14/B-04.

### 2.2 Variables À PRODUIRE PAR GO (17) et briques INTERNE-GO
- **DEC-01 — Mode attribué à chaque brique** : Modes des briques fixés par la MPD validée → INTERNE-GO (B-01, suivi B-70).
- **DEC-02 — Décisions inscrites au RDR (valeur déclarée, auteur, date)** : RDR officiel à ouvrir → INTERNE-GO (B-03).
- **DEC-03 — Verrous ouverts (donnée, brique suspendue, responsable)** : Registre des verrous à ouvrir → INTERNE-GO (B-03/B-04).
- **DEC-04 — Documents supersédés (indice, date)** : Suivi des documents supersédés → INTERNE-GO (B-71/B-72).
- **DEC-05 — Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut)** : Hypothèses notifiées H-xx à produire → INTERNE-GO (B-22).
- **DOC-08 — Plans de récolement / DOE** : Récolement/DOE à produire en clôture de mission → INTERNE-GO (B-72) ; B-11 s'appuie sur P2/P4/P5.
- **EXI-05 — Contrainte admissible transmise à l'existant** : Contraintes admissibles transmises à l'existant à établir par nos vérifications → INTERNE-GO (B-23/B-46).
- **GEO-07 — Transformation du fichier (rotation, translation, échelle)** : Transformation de recalage à déterminer → INTERNE-GO (B-30).
- **GEO-08 — Points de calage identifiés (≥ 3 non alignés)** : Points de calage ≥ 3 non alignés à identifier → INTERNE-GO (B-30/B-31).
- **GEO-10 — Seuils d'épaisseur de présomption porteuse (seuil bas / seuil haut, par système constructif)** : Seuils d'épaisseur de présomption porteuse à fixer → INTERNE-GO (B-32).
- **GEO-11 — Superposition des niveaux : recouvrement minimal et écart maximal d'axe entre niveaux** : Recouvrement minimal et écart d'axe entre niveaux à fixer → INTERNE-GO (B-32).
- **GEO-12 — Seuils géométriques du projet (résidu de calage, écarts de superposition et de position)** : Seuils géométriques (résidu de calage, superposition) à fixer → INTERNE-GO (B-30).
- **GEO-13 — Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU)** : Matrice de recalage multi-sources vers le RSU à construire → INTERNE-GO (B-30/B-31).
- **LIV-01 — Conventions de calques DXF (préfixes, suffixes, règles d'usage)** : Conventions de calques DXF des livrables à définir → INTERNE-GO (B-60).
- **LIV-02 — Échelles autorisées** : Échelles autorisées des livrables à définir → INTERNE-GO (B-60).
- **LIV-03 — Formats de sortie (DXF, PDF, PNG) et nommage des fichiers** : Formats et nommage des fichiers à définir → INTERNE-GO (B-60).
- **NIV-07 — Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini** : Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB/Fini à produire → INTERNE-GO (B-02).

Pour mémoire (CFG-2) : AC-03 reste FOURNIE (le BET MOE existe) ; l'INTERNE-GO ne porte que sur les ouvrages non conçus par le BET et sur les productions d'exécution, en aucun cas sur une réclamation de DXF de coffrage MOE, interdite par la configuration.

### 2.3 Variables NON NÉCESSAIRE (3) — **validation ligne par ligne requise**
Chaque proposition repère un motif de périmètre, jamais une indisponibilité. Une réponse « ok » globale ne suffit pas : il faut une décision explicite par ligne (reprise au RDR B-03 en D-xx).

- [ ] **DOC-07 — Diagnostic amiante/plomb (cité en exemple v1.1, défini en v2.0)** : Périmètre : désamiantage et déplombage exclus des livrables CARNAC (§1.4) ; seules les contraintes de phasage/coordination sont remontées. Effet : SANS OBJET (proposition à valider).
- [ ] **DOC-09 — Fiches techniques des prédalles** : Périmètre : aucune prédalle ni plancher préfabriqué dans l'opération (dallage coulé en place P1 p35 ; planchers existants conservés/renforcés). Effet : SANS OBJET (proposition à valider) ; B-48 en SANS OBJET corrélatif.
- [ ] **STR-02 — Poussées des terres, surcharges de remblai et écrans de soutènement** : Périmètre : pas de sous-sol ni d'écran de soutènement pour Flora (fondations superficielles, dallage sur terre-plein). Sous réserve du périmètre Gardien/Bagatelle (écart C-07 toujours ouvert). Effet : SANS OBJET (proposition à valider, réserve C-07).

Corrélats briques à confirmer : B-48 (prédalles) en SANS OBJET si DOC-09 validée ; B-41 (fondations profondes) en SANS OBJET probable ; STR-02 reste conditionnée à la réponse sur l'écart C-07 (Gardien/Bagatelle).

---

## 3. DÉCISIONS ATTENDUES À CETTE PORTE

1. Validation ou correction du **gabarit M (CFG-02)** et du découpage CFG-03 (un bloc, zéro JD).
2. Validation **ligne par ligne** des trois NON NÉCESSAIRE (DOC-07, DOC-09, STR-02), avec traitement du cas C-07 pour STR-02.
3. Confirmation du maintien en BLOQUANTE de SOL-04/SOL-06/SOL-07 (et donc de la demande de transmission du G2 complet), ou inscription d'une décision alternative au RDR.
4. Toute correction d'un statut proposé : je reprends la MPD en indice incrémenté, sans avancer sur B-02.

## 4. CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère de la fiche | Statut |
|---|---|
| Toute variable lue par une brique activée figure (106/106) | ✅ validé par build_b01.py |
| Tout NON NÉCESSAIRE porte un motif de périmètre | ✅ les 3 lignes sont motivées (périmètre, pas disponibilité) |
| Tout BLOQUANTE rattaché à une brique identifiée | ✅ SOL-04/06/07 rattachées aux briques du dictionnaire |
| Tout À PRODUIRE PAR GO identifie la brique INTERNE-GO | ✅ contrôlé par script |
| Aucune décision SANS OBJET sans validation explicite | ✅ toutes en proposition, cases à cocher §2.3 |
| Aucun mode COMPLET sur variable BLOQUANTE | ✅ contrôlé par script |
| Zéro placeholder (V7) | ✅ |

**Brique B-01 livrée (Ind A, proposition) — en attente de votre GO ou de vos observations.** Le GO suivant déclenchera **B-02 (Fiche de Données de Conception, table NIV-07)** ; la MPD validée sera annexée au RDR (B-03) comme décision D-xx datée.