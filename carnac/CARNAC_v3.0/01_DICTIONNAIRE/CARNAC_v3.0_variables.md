Fichier 01_DICTIONNAIRE/CARNAC_v3.0_variables.md — CARNAC v3.0
________________


CARNAC — DICTIONNAIRE DES VARIABLES (v3.0)
1. NOTE DE COMPTE
Le dictionnaire v3.0 compte 106 variables : 94 variables reprises de la version précédente (aucune supprimée), dont deux libellés restaurés (LIV-01 « Conventions de calques DXF » et LIV-03 « Formats de sortie », corrompus en « B-61 » lors de la reconstruction antérieure), et 12 variables nouvelles (CFG-01 à CFG-03, DEC-05 à DEC-07, GEO-13, GEO-14, NIV-07, STR-01 à STR-03).

La colonne « Briques consommatrices » est reconstruite automatiquement, par développement des plages (SOL-01 à SOL-07, GEO-01 à GEO-05, LIV-01 à LIV-05, CHG-01 à CHG-03, etc.), à partir des tables « Variables consommées » des 39 fiches B-xx et des 4 prompts T-xx : elle est donc exacte par construction.

2. TABLE DES VARIABLES

| Code | Libellé | Briques consommatrices |
| --- | --- | --- |
| AC-01 | MOA | — (variable de référence) |
| AC-02 | Architecte | — (variable de référence) |
| AC-03 | BET structure de conception | B-20 |
| AC-06 | Bureau de contrôle | — (variable de référence) |
| CHG-01 | Usage des locaux par zone (catégories EC1) | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-02 | Surcharges d'exploitation par zone | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-03 | Poids propres des complexes de plancher | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-04 | Poids propres de toiture | B-21, B-44 |
| CHG-05 | Neige | B-21, B-44 |
| CHG-06 | Vent | B-21, B-44, B-45 |
| CHG-07 | Sismique (si applicable) | B-42, B-46 |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | B-21, B-43, B-47, B-48 |
| DEC-01 | Mode attribué à chaque brique | B-70 |
| DEC-02 | Décisions inscrites au RDR (valeur déclarée, auteur, date) | B-03, B-64, B-70, B-72, T-03 |
| DEC-03 | Verrous ouverts (donnée, brique suspendue, responsable) | B-03, B-04, B-13, B-15, B-64, B-70, B-72, T-03, T-04 |
| DEC-04 | Documents supersédés (indice, date) | B-71, B-72 |
| DOC-01 | Inventaire des pièces (fichier, folio, indice, échelle) | B-00, B-01 |
| DOC-02 | Plans architecte vectoriels | B-20, B-30, B-31, B-32, B-33, B-60 |
| DOC-03 | Plans BET structure (si disponibles) | B-10, B-11, B-20 |
| DOC-04 | CCTP / pièces contractuelles | B-10, B-14 |
| DOC-05 | Diagnostic structure de l'existant | B-11, B-23, B-24 |
| DOC-06 | Rapport géotechnique | B-12, B-41 |
| DOC-07 | Diagnostic amiante/plomb (cité en exemple v1.1, défini en v2.0) | — (variable de référence) |
| DOC-08 | Plans de récolement / DOE | B-11 |
| DOC-09 | Fiches techniques des prédalles | B-48, B-50 |
| EXI-01 | Sections des éléments existants | B-20, B-23, B-24, B-44, B-46, B-49 |
| EXI-02 | Pathologies relevées | B-23 |
| EXI-03 | Résistance des matériaux existants | B-20, B-24, B-44, B-46, B-49 |
| EXI-04 | Résultats de sondages destructifs ou semi-destructifs | B-24, B-41 |
| EXI-05 | Contrainte admissible transmise à l'existant | B-23, B-46 |
| GEO-01 | Emprise / contour du bâtiment | B-20, B-21, B-23, B-33, B-40, B-43, B-44, B-47, B-48, B-60 |
| GEO-02 | Axes et trames | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 |
| GEO-03 | Épaisseurs murs | B-20, B-21, B-23, B-33, B-40, B-46, B-49, B-60 |
| GEO-04 | Positions poteaux | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 |
| GEO-05 | Baies et ouvertures | B-20, B-23, B-33, B-40, B-42, B-46, B-47, B-49, B-60 |
| GEO-06 | Unités du fichier source (cm/m/mm) | B-30, B-32 |
| GEO-07 | Transformation du fichier (rotation, translation, échelle) | B-30, B-31 |
| GEO-08 | Points de calage identifiés (≥ 3 non alignés) | B-30, B-31 |
| GEO-09 | Échelle tracé | — (variable de référence) |
| ID-01 | Code projet | B-00, B-01, B-02, B-03, B-04, B-10, B-11, B-12, B-13, B-14, B-15, B-20, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-34, B-40, B-41, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-50, B-60, B-62, B-64, B-70, B-71, B-72, T-01, T-02, T-03, T-04 |
| ID-02 | Intitulé de l'opération | B-00, B-10, B-11, B-12, B-13, B-14, B-15, B-20, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-34, B-40, B-41, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-50, B-60, B-62, B-64, B-70, B-71, B-72, T-01, T-02, T-03, T-04 |
| ID-03 | Adresse | — (variable de référence) |
| ID-04 | Nature | — (variable de référence) |
| ID-05 | Indice du dossier en vigueur | B-03, B-64, B-71, B-72 |
| ID-06 | Phase | — (variable de référence) |
| ID-07 | Date de l'étude | B-03 |
| LIV-01 | Conventions de calques DXF (préfixes, suffixes, règles d'usage) | B-60 |
| LIV-02 | Échelles autorisées | B-60 |
| LIV-03 | Formats de sortie (DXF, PDF, PNG) et nommage des fichiers | B-60 |
| LIV-04 | Cartouche | B-60 |
| LIV-05 | Langue et unités | B-60 |
| MAT-01 | Classe de résistance du béton | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 |
| MAT-02 | Classe d'exposition | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 |
| MAT-03 | Enrobage nominal | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 |
| MAT-04 | Nuance d'acier BA | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 |
| MAT-05 | Nuance d'acier de charpente métallique | B-45, B-49, B-50, B-62 |
| MAT-06 | Classe de bois | B-43, B-44, B-50, B-62 |
| MAT-07 | Nature et résistance de la maçonnerie existante | B-46, B-49, B-50 |
| MAT-08 | Classe de service et durée de charge | B-43, B-44 |
| MAT-09 | Classe de bloc de maçonnerie neuve (NF EN 771-3) | B-46, B-50, B-62 |
| MAT-10 | Classe de mortier (M2,5 à M10) | B-46, B-50, B-62 |
| MAT-11 | Type de maçonnerie (chaînée / armée / non armée) | B-46, B-50, B-62 |
| MAT-12 | Présence et nature des chaînages existants | B-46 |
| NIV-01 | Niveau TN | B-40 |
| NIV-02 | Niveaux planchers | B-42, B-43, B-47, B-48, B-60 |
| NIV-03 | Hauteurs libres | B-42, B-47 |
| NIV-04 | Niveau assise | B-40 |
| NIV-05 | Niveau fini dallage | B-43, B-60 |
| NIV-06 | Épaisseurs plancher | B-43, B-48 |
| OUT-01 | Environnement d'exécution (interpréteur, bibliothèques, persistance) | — (variable de référence) |
| OUT-02 | Script de production ou de calcul versionné avec le livrable | — (variable de référence) |
| OUT-03 | Journal d'exécution et de relecture (comptages, résidus, écarts) | — (variable de référence) |
| OUT-04 | Rendu de contrôle visuel lu (PNG pleine page 300 dpi) | — (variable de référence) |
| SEC-01 | Degré coupe-feu exigé par élément | B-25, B-42, B-43, B-47, B-48, B-49 |
| SEC-02 | Catégorie ERP | — (variable de référence) |
| SEC-03 | Classement termites de la commune | B-43 |
| SEC-04 | Classe structurale | — (variable de référence) |
| SEC-05 | PMR | — (variable de référence) |
| SIT-01 | Site occupé | — (variable de référence) |
| SIT-02 | Contraintes de site (cité en exemple v1.1, défini en v2.0) | — (variable de référence) |
| SIT-03 | Accès | — (variable de référence) |
| SIT-04 | Voisinage | B-40 |
| SIT-05 | Emprise fouille | B-40 |
| SOL-01 | Contrainte admissible ELS | B-12, B-20, B-40, B-41, B-43 |
| SOL-02 | Contrainte admissible ELU | B-20, B-40, B-41 |
| SOL-03 | Profondeur de bon sol / ancrage minimal | B-20, B-40, B-41 |
| SOL-04 | Nature et succession des couches | B-20, B-41 |
| SOL-05 | Classe d'agressivité du sol (XA) | B-20, B-40, B-41, B-43 |
| SOL-06 | Nappe, hydrologie, drainage | B-40, B-41 |
| SOL-07 | Tassements admissibles / différentiels | B-40, B-41 |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | B-12, B-41 |
| GEO-10 | Seuils d'épaisseur de présomption porteuse (seuil bas / seuil haut, par système constructif) | B-32 |
| GEO-11 | Superposition des niveaux : recouvrement minimal et écart maximal d'axe entre niveaux | B-32 |
| GEO-12 | Seuils géométriques du projet (résidu de calage, écarts de superposition et de position) | B-30 |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | B-00, B-01, B-20, B-60 |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | B-01, B-04, B-25, B-34, B-60 |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | B-01, B-20, B-21, B-25, B-30, B-60 |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | B-03, B-20, B-22, B-25, B-34, B-40, B-60, B-64, B-70 |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | B-03, B-22, B-60, B-64 |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | B-03, B-24, B-34, B-40, B-41, B-44, B-46, B-60, B-64 |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | B-13, B-20, B-30, B-31, B-32, B-34 |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | B-11, B-13, B-20, B-31, B-32, B-33 |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | B-02, B-20, B-30, B-32, B-43, B-60 |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | B-20, B-21, B-25, B-42, B-44, B-45, B-46 |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | B-12, B-25, B-40, B-41, B-42, B-43 |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | B-32, B-34, B-42, B-43, B-48, B-60 |
