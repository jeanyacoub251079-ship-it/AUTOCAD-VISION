# 12_EXEMPLES — Exemples historiques (produits sous CARNAC v1.1)

> **Bandeau de qualification (v2.6)** — Les exemples qui suivent ont été produits sous CARNAC **v1.1**, sur le projet fictif « LES LILAS ». Ils sont conservés comme **traces pédagogiques historiques** : leurs valeurs d'époque (92 variables, renvoi à CARNAC_v1.1_variables.csv, statuts et totaux de la production v1.1) sont celles de leur version d'origine et n'ont **aucune valeur de référence fonctionnelle** pour le carnet en vigueur. Pour les définitions et comptes actuels, seuls font foi le dictionnaire (01_DICTIONNAIRE) et le document maître (00_MASTER).
________________


Exemples conservés dans cette section : exemple de FDC remplie, exemple de RDR rempli, récapitulatif-arborescence du carnet, check-list de démarrage de projet — tous sur le projet fictif « LES LILAS » (voir bandeau de qualification ci-dessus).

Exemple de FDC remplie — Projet fictif
Projet « LES LILAS » — Rénovation d'un immeuble de bureaux en logements
Adresse : 45 rue des Lilas, 75020 Paris
Opération : réhabilitation lourde d'un immeuble R+4 en 18 logements
Maître d'ouvrage : SCI LES LILAS
Architecte : Atelier Martin & Associés
BET Structure : BET STRUCTURE PARTIEL — note de calcul des planchers existants fournie, conception des renforcements à notre charge
BET Fluides : non désigné à ce stade
Bureau de contrôle : SOCOTEC
Code projet (ID-01) : LILAS-2026
Indice du dossier (ID-05) : Ind C du 10/10/2026
Date de l'étude (ID-07) : 17/10/2026
________________


Tableau 1 — Variables résolues

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) consommatrice(s) |
| --- | --- | --- | --- | --- | --- | --- |
| ID-01 | Code projet | LILAS-2026 | — | Décision interne | Décision | Toutes |
| ID-02 | Intitulé | Rénovation bureaux → 18 logements | — | Pièce marché | Contractuelle | B-00 |
| ID-03 | Adresse | 45 rue des Lilas, 75020 Paris | — | Plans archi Ind C | Contractuelle | B-00 |
| ID-04 | Nature | RÉHAB | — | Pièce marché | Contractuelle | B-01 |
| ID-05 | Indice dossier | Ind C | — | Plans archi | Contractuelle | B-70, B-71 |
| ID-06 | Phase | EXE | — | Pièce marché | Contractuelle | B-01, B-20 |
| ID-07 | Date étude | 17/10/2026 | — | Décision interne | Décision | B-70 |
| AC-01 | MOA | SCI LES LILAS | — | Pièce marché | Contractuelle | B-10 |
| AC-02 | Architecte | Atelier Martin & Associés | — | Pièce marché | Contractuelle | B-30 |
| AC-03 | BET structure | BET STRUCTURE PARTIEL (planchers uniquement) | — | Pièce marché | Contractuelle | B-20 (INTERNE-GO partiel) |
| AC-06 | Bureau de contrôle | SOCOTEC | — | Pièce marché | Contractuelle | B-70 |
| DOC-02 | Plans architecte vectoriels | DXF Ind C — 45 rue des Lilas — 6 planches | — | Pièce reçue | Contractuelle | B-30, B-32, B-60 |
| DOC-03 | Plans BET structure | Note de calcul planchers existants + plans de principe Ind B — 2 planches | — | Pièce reçue | Contractuelle | B-20 (PARTIEL-DÉCLARÉ) |
| DOC-04 | CCTP | CCTP Lot 01 GO Ind C du 10/10/2026 | — | Pièce marché | Contractuelle | B-10 |
| DOC-05 | Diagnostic structure | Diagnostic BATIDIAG du 15/09/2026 — 8 désordres, 3 zones non relevées | — | Pièce reçue | Contractuelle | B-11, B-23 |
| DOC-06 | Rapport géotechnique | GEOEXPERTS n° 26.04.123 — G2 AVP du 12/06/2026 | — | Pièce reçue | Contractuelle | B-12, B-40 (PARAMÉTRIQUE) |
| DOC-09 | Fiches techniques | Prédalles, boulons, résines — 4 fiches reçues | — | Pièce reçue | Contractuelle | B-50 |
| GEO-01 | Emprise | 22 × 14 m, R+4, emprise au sol 308 m² | m | Plans archi | Contractuelle | B-30, B-32 |
| GEO-02 | Axes et trames | 5 axes longitudinalx (3,50 m) × 3 axes transversaux (4,00 m) | m | Plans archi | Contractuelle | B-30, B-42, B-50 |
| GEO-03 | Épaisseurs murs | Murs porteurs façade : 45 cm. Refends : 30 cm. | cm | Plans archi + diagnostic | Contractuelle | B-40, B-42, B-46 |
| GEO-04 | Positions poteaux | 15 poteaux existants (cf. plans archi) — renforcement à créer sur 3 poteaux | — | Plans archi + note BET | Contractuelle | B-42, B-45, B-50 |
| GEO-05 | Baies et ouvertures | 47 baies identifiées (cf. plans archi) — 12 linteaux à créer | — | Plans archi | Contractuelle | B-49, B-42 |
| GEO-06 | Unités source | cm | — | DXF déclaré | Contractuelle | B-30 |
| GEO-07 | Transformation | Rotation 0°, translation à calculer | — | À calculer en B-30 | À confirmer | B-30 |
| GEO-08 | Points de calage | 3 angles de murs (à identifier) | — | À calculer en B-30 | À confirmer | B-30 |
| GEO-09 | Échelle tracé | 1/50 (plans courants), 1/20 (détails) | — | Décision interne | Décision | B-60 |
| NIV-01 | Niveau TN | Terrain naturel : 42,30 m NGF | m | Plans archi | Contractuelle | B-40 |
| NIV-02 | Niveaux planchers | RDC : 42,60 — R+1 : 45,30 — R+2 : 48,00 — R+3 : 50,70 — R+4 : 53,40 — Toiture : 56,10 | m NGF | Plans archi | Contractuelle | B-42, B-43, B-60 |
| NIV-03 | Hauteurs libres | RDC : 2,80 m — étages : 2,70 m | m | Plans archi | Contractuelle | B-42 |
| NIV-04 | Niveau assise | Fondations existantes : radier à 40,90 m NGF (zone Sud) / semelles filantes à 41,20 m NGF (zone Nord) | m NGF | Plans archi + diagnostic | Contractuelle | B-40 |
| NIV-05 | Niveau fini dallage | 42,60 m NGF | m NGF | Plans archi | Contractuelle | B-43 |
| NIV-06 | Épaisseurs plancher | Planchers existants : 22 cm (hourdis + dalle BA). Planchers neufs : 25 cm (dalle BA + chape). | cm | Diagnostic | Contractuelle | B-43, B-48 |
| MAT-01 | Classe béton | C25/30 pour tous les nouveaux ouvrages | — | CCTP Lot 01 §… | Contractuelle | B-40, B-42, B-43, B-47, B-48, B-49 |
| MAT-02 | Classe exposition | XC2 (intérieur) / XC4 (extérieur au contact de la terre) | — | CCTP Lot 01 §… | Contractuelle | B-40, B-42, B-43 |
| MAT-03 | Enrobage nominal | 40 mm (XC4) / 30 mm (XC2) | mm | CCTP Lot 01 §… | Contractuelle | B-40, B-42, B-43, B-47, B-48, B-49 |
| MAT-04 | Nuance acier BA | B500B | — | CCTP Lot 01 §… | Contractuelle | B-40, B-42, B-43, B-47, B-48, B-49 |
| MAT-05 | Nuance acier métallique | S235 | — | CCTP Lot 01 §… | Contractuelle | B-45, B-50 |
| MAT-06 | Classe bois | C24 | — | CCTP Lot 01 §… | Contractuelle | B-44 |
| MAT-07 | Maçonnerie existante | Moellons calcaire + briques pleines — résistance estimée 2,0 MPa | MPa | Diagnostic BATIDIAG | À confirmer (non testée) | B-46 |
| MAT-08 | Classe service bois | Classe 2 (combles ventilés) | — | CCTP Lot 01 §… | Contractuelle | B-44 |
| MAT-09 | Classe blocs neufs | Blocs béton B80 (classe C25/30 selon NF EN 771-3) | — | CCTP Lot 01 §… | Contractuelle | B-46 |
| MAT-10 | Classe mortier | M10 (mortier ciment) | — | CCTP Lot 01 §… | Contractuelle | B-46 |
| MAT-11 | Type maçonnerie | Chaînée (avec chaînages horizontaux et verticaux) | — | CCTP Lot 01 §… | Contractuelle | B-46 |
| MAT-12 | Chaînages existants | Présents sur 2 façades sur 4 — discontinus | — | Diagnostic BATIDIAG | À confirmer (non relevé) | B-46 |
| CHG-01 | Usages des locaux | Logements : catégorie A (1,5 kN/m²). Circulations : catégorie B (2,5 kN/m²). | — | Programme architecte | Contractuelle | B-20, B-43 |
| CHG-02 | Surcharges exploitation | Séjour/Chambre : 1,5 kN/m². Circulation : 2,5 kN/m². Balcon : 3,5 kN/m². | kN/m² | Programme architecte | Contractuelle | B-20, B-40, B-42, B-43, B-44, B-45, B-47, B-48 |
| CHG-03 | Poids propres planchers | Existant : 4,2 kN/m². Neuf : 5,8 kN/m². | kN/m² | Diagnostic + Décision interne | À confirmer (complexe neuf non détaillé) | B-20, B-42, B-43 |
| CHG-04 | Poids propres toiture | 1,80 kN/m² (tuiles + charpente + isolation) | kN/m² | CCTP Lot 01 + Décision interne | À confirmer | B-44 |
| CHG-05 | Neige | Zone A1, s_k = 0,45 kN/m² | kN/m² | NF EN 1991-1-3/NA | Contractuelle | B-44 |
| CHG-06 | Vent | Zone 2, v_b = 24 m/s, terrain catégorie III | m/s | NF EN 1991-1-4/NA | Contractuelle | B-44, B-45 |
| CHG-07 | Sismique | Zone 1, catégorie II | — | NF EN 1998-1/NA | Contractuelle | B-20, B-40, B-42 |
| CHG-08 | Cloisons, équipements | Cloisons légères : 0,5 kN/m². Escalier métallique : 8 kN (charge ponctuelle). | kN/m² et kN | Programme architecte | À confirmer (escalier non détaillé) | B-43, B-47, B-48 |
| SEC-02 | Catégorie ERP | Habitation — 3e famille — effectif ≤ 100 personnes | — | Programme architecte | Contractuelle | B-13 |
| SEC-03 | Termites | Zone non classée (Paris 20e — arrêté préfectoral 2003) | — | Arrêté préfectoral | Contractuelle | B-43 |
| SEC-04 | Classe structurale | S4 (durée de vie 50 ans) | — | Décision interne | Décision | B-20, B-40 |
| SEC-05 | PMR | Accessibilité ERP — 2 logements PMR sur 18 | — | Programme architecte | Contractuelle | B-60 |
| SIT-01 | Site occupé | NON (immeuble vide) | — | Pièce marché | Contractuelle | B-13, B-50 |
| SIT-03 | Accès | Rue étroite (6 m) — accès camion possible — pas de grue à tour possible | — | Visite site | Décision | B-13 |
| SIT-04 | Voisinage | Immeuble mitoyen à l'Est (mur mitoyen) — distance de sécurité 1,50 m pour les fouilles | — | Diagnostic | Contractuelle | B-40 |
| SIT-05 | Emprise fouille | Cour intérieure de 8 × 6 m disponible pour les fouilles | m² | Plans archi | Contractuelle | B-40 |
| LIV-01 | Conventions calques | Annexe A du carnet CARNAC v1.1 | — | Carnet | Contractuelle | B-60 |
| LIV-02 | Échelles autorisées | 1/200, 1/100, 1/50, 1/20, 1/10, 1/5 | — | Carnet | Contractuelle | B-60 |
| LIV-03 | Formats sortie | DXF, PDF, PNG | — | Carnet | Contractuelle | B-60 |
| LIV-04 | Cartouche | Modèle unique CARNAC v1.1 | — | Carnet | Contractuelle | B-60 |
| LIV-05 | Langue et unités | Français — mètres (cotes plan) / millimètres (sections) | — | Carnet | Contractuelle | B-60 |
| DEC-01 | Modes d'exécution | Cf. MPD validée du 17/10/2026 | — | Décision RDR D-01 | Décision | Toutes |
| DEC-04 | Documents supersédés | Aucun (première émission) | — | RDL | Contractuelle | B-71 |

________________


Tableau 2 — VERROU (variables bloquantes manquantes)

| Code VERROU | Libellé | Brique(s) suspendue(s) | Voie d'obtention proposée | Responsable pressenti | SOL-01 |
| --- | --- | --- | --- | --- | --- |
| Contrainte admissible ELS | B-40 (fondations superficielles) | Mission G3 (recommandée par B-12) ou décision MOA de retenir une valeur plancher du G2 AVP (0,20 MPa — non contractuel) | MOA (SCI LES LILAS) | SOL-02 | Contrainte admissible ELU |
| B-40 | Idem SOL-01 (G3 ou décision MOA) | MOA | SOL-03 | Profondeur de bon sol | B-40 |
| Mission G3 ou sondage complémentaire (2 sondages supplémentaires) | MOA | SOL-05 | Classe d'agressivité du sol (XA) | B-40, B-42, B-43 (enrobages) | Analyse chimique du sol (sulfates, pH) — non fournie dans le G2 AVP |
| MOA | SEC-01 | Degré coupe-feu exigé par élément | B-42, B-43, B-47, B-48, B-49 (enrobages) | Note du bureau de contrôle SOCOTEC — non fournie à ce stade | MOE / Architecte |
| EXI-01 | Sections des éléments existants (pannes de charpente) | B-44 (charpente bois) | Relevé sur site (sondage visuel + mesure) — non fourni dans le diagnostic | GO | EXI-03 |
| Résistance des matériaux existants (maçonnerie) | B-46 (maçonnerie) | Essai de résistance (scléromètre ou carottage) — non fourni | GO (à commander) | EXI-05 | Contrainte admissible transmise à l'existant |
| B-40, B-46, B-49 | Analyse structurelle de l'existant (BET STRUCTURE PARTIEL ne l'a pas fournie) | BET / MOE | GEO-07 | Transformation du fichier | B-30 (calage) |
| À calculer en B-30 (3 points de calage non alignés) — pas une donnée manquante, mais une donnée à produire | GO | GEO-08 | Points de calage | B-30 | À identifier en B-30 |
| GO | MAT-12 | Nature exacte des chaînages existants | B-46 | Relevé sur site — le diagnostic mentionne leur présence mais pas leur nature | GO |

________________


Tableau 3 — Synthèse de la FDC

| Catégorie | Nombre |
| --- | --- |
| Détail | Variables résolues (Tableau 1) |
| 72 | Toutes avec source citée et fiabilité |
| Variables VERROU (Tableau 2) | 11 |
| Toutes avec brique suspendue et voie d'obtention | Total |
| 83 | Sur 92 variables du dictionnaire |

Les 9 variables non listées sont celles qui ne sont pas lues par les briques activées dans ce projet (par exemple, certaines variables DOC-07 ou SIT-02, hors périmètre). Elles n'apparaissent pas en FDC — conformément à la règle « aucune variable non lue ».
Répartition par fiabilité :

| Fiabilité | Nombre | Détail |
| --- | --- | --- |
| Contractuelle | 55 | Issues des pièces du marché (CCTP, plans, programme, diagnostic) |
| Décision | 12 | Issues de décisions internes ou du RDR (D-01, D-05, etc.) |
| À confirmer | 5 | Hypothèses de travail (MAT-07, MAT-12, CHG-03, CHG-04, CHG-08) |
| VERROU | 11 | Données bloquantes manquantes |

________________


Ce que cette FDC illustre
1. Le principe « valeurs + sources » : chaque ligne porte une valeur et sa source — le lecteur peut vérifier sans ouvrir le CCTP.
2. Le principe « trois niveaux de fiabilité » :
   * Contractuelle (55) : issues du marché, ne se contestent pas unilatéralement.
   * Décision (12) : issues du RDR, avec auteur et date, peuvent être révisées par une nouvelle décision.
   * À confirmer (5) : hypothèses de travail, doivent être confirmées avant exécution.
3. Le principe « aucune valeur hors FDC » : aucune valeur n'est « par expérience ». Chaque valeur vient d'une pièce ou d'une décision.
4. Le principe « VERROU en fin de FDC » : les 11 variables bloquantes sont listées avec leur brique suspendue et leur voie d'obtention — elles ne sont pas noyées dans le tableau principal.
5. Le principe « aucune variable non lue » : les 9 variables du dictionnaire non lues par les briques activées n'apparaissent pas — la FDC ne contient que ce qui est utile.
6. Le cas SEC-01 : le degré coupe-feu n'est pas fourni. C'est une donnée bloquante pour toutes les briques BA (B-42, B-43, B-47, B-48, B-49). Sans SEC-01, ces briques ne peuvent pas être en mode COMPLET — elles seront en PARAMÉTRIQUE jusqu'à obtention de la note du bureau de contrôle.
7. Le cas MAT-07 / EXI-03 : la résistance de la maçonnerie existante est estimée à 2,0 MPa par le diagnostic — mais elle n'a pas été testée. C'est une valeur À confirmer — B-46 sera en mode PARTIEL-DÉCLARÉ (avec décision RDR) ou PARAMÉTRIQUE (sans décision).
8. Le cas GEO-07 / GEO-08 : la transformation et les points de calage ne sont pas fournis — mais ce ne sont pas des données manquantes au sens strict. Ce sont des données à produire par B-30 (calage). Elles figurent en VERROU pour être tracées, mais leur voie d'obtention est interne (GO).
9. Le cas SOL-01 / SOL-02 : la contrainte admissible n'est pas fournie — le G2 AVP est insuffisant pour des calculs d'exécution. C'est la décision de mission G3 (recommandée par B-12) qui débloquera B-40. Sans G3, B-40 sera en mode PARAMÉTRIQUE (formules littérales, tableau de sensibilité non contractuel).
________________


**[Fin — exemple de FDC]**
Exemple de RDR rempli — Projet fictif
Projet « LES LILAS » — Rénovation d'un immeuble de bureaux en logements
Code projet (ID-01) : LILAS-2026
Indice du dossier (ID-05) : Ind C du 10/10/2026
Date du RDR : 17/10/2026
Version du RDR : v1.0 (ouverture)
Rappel du rôle du RDR : c'est le document qui vous protège en cas de litige sur un délai, une valeur déclarée, ou un livrable partiel. Il prouve que vous avez :
   1. pris les décisions qui vous appartenaient (Section 1) ;
   2. demandé les données manquantes dans les délais (Section 2) ;
   3. exécuté tout ce qui était faisable malgré les blocages (Section 3 — Registre des Verrous).
________________


Section 1 — DÉCISIONS

| N° | Date | Objet | Décision | Auteur | Effet sur les briques |
| --- | --- | --- | --- | --- | --- |
| D-01 | 17/10/2026 | Validation de la MPD | La MPD proposée par B-01 est validée. Les NON NÉCESSAIRE suivants sont confirmés : DOC-07 (amiante/plomb — hors périmètre GO), SIT-02 (contraintes d'exploitation — site vide), CHG-05 (neige — le projet est en région A1, confirmé) | GO (vous) | Active les briques B-00 à B-04, B-10 à B-15, B-20 à B-24, B-30 à B-33, B-40 à B-50, B-60, B-62, B-64, B-70 à B-72 |
| D-02 | 17/10/2026 | Validation de la FDC | La FDC proposée par B-02 est validée. Les valeurs À confirmer (MAT-07, MAT-12, CHG-03, CHG-04, CHG-08) sont acceptées comme hypothèses de travail, inscrites en H-xx dans la note d'hypothèses (B-22) | GO | Active les briques qui consomment ces variables, avec mention « sous hypothèse H-xx » |
| D-03 | 17/10/2026 | Mode de B-20 (Conception GO) | B-20 est exécutée en mode PARTIEL-DÉCLARÉ : le BET STRUCTURE PARTIEL fournit les plans de planchers existants, la conception des renforcements est à notre charge. Les plans du BET sont repris tels quels, sans redessin | GO | B-20 en PARTIEL-DÉCLARÉ |
| D-04 | 17/10/2026 | Mode de B-40 (Fondations) | B-40 est exécutée en mode PARAMÉTRIQUE (G2 AVP insuffisant pour des calculs d'exécution). Aucune valeur de repli n'est retenue : les formules sont en littéral, un tableau de sensibilité non contractuel est produit. Le livrable est filigrané _P | GO | B-40 en PARAMÉTRIQUE |
| D-05 | 17/10/2026 | Mode de B-46 (Maçonnerie) | B-46 Bloc A est exécutée en mode PARTIEL-DÉCLARÉ : la résistance de la maçonnerie existante est estimée à 2,0 MPa par le diagnostic BATIDIAG, sans essai. Cette valeur est acceptée comme hypothèse de travail (H-03). B-46 Bloc B (maçonnerie neuve) est en mode COMPLET (MAT-09 à MAT-11 disponibles) | GO | B-46 Bloc A en PARTIEL-DÉCLARÉ, Bloc B en COMPLET |
| D-06 | 17/10/2026 | Demande de mission G3 | Une mission G3 (mission géotechnique d'exécution) est recommandée par B-12. La MOA n'a pas encore répondu. En attente de décision (voir R-01) | GO | B-40 reste en PARAMÉTRIQUE jusqu'à réponse MOA |
| D-07 | 17/10/2026 | Demande de note coupe-feu | La note de coupe-feu (SEC-01) n'est pas fournie. Le bureau de contrôle SOCOTEC est sollicité (voir R-02). En attente de réponse | GO | B-42, B-43, B-47, B-48, B-49 restent en PARAMÉTRIQUE jusqu'à réponse BC |
| D-08 | 17/10/2026 | Exclusions confirmées | Les exclusions suivantes sont confirmées pour ce projet : désamiantage (diagnostic DOC-07 non fourni — l'immeuble est antérieur à 1997, un diagnostic est requis avant travaux), déplombage (idem), curage/démolition (hors périmètre GO), espaces verts (hors périmètre), dimensionnement de la protection au feu (hors périmètre GO) | GO | Ces domaines ne sont pas traités par les briques CARNAC |
| D-09 | 17/10/2026 | Mode de B-44 (Charpente bois) | B-44 est exécutée en mode PARAMÉTRIQUE : les sections des pannes existantes ne sont pas connues (EXI-01 VERROU), le relevé n'a pas été fait. Le livrable est filigrané _P | GO | B-44 en PARAMÉTRIQUE jusqu'à relevé |
| D-10 | 17/10/2026 | Mode de B-41 (Fondations profondes) | B-41 est exécutée en mode SANS OBJET : le projet ne comporte pas de fondations profondes (radier existant en zone Sud, semelles filantes existantes en zone Nord). Aucune fondation profonde n'est prévue | GO | B-41 en SANS OBJET — ligne de justification |

________________


Section 2 — RÉSERVES

| N° | Objet | Statut | Responsable de l'obtention | Date de demande | Échéance |
| --- | --- | --- | --- | --- | --- |
| R-01 | Mission G3 (géotechnique d'exécution) | Ouverte | MOA (SCI LES LILAS) | 17/10/2026 | 31/10/2026 |
| R-02 | Note coupe-feu (SEC-01) | Ouverte | Bureau de contrôle SOCOTEC (via MOE) | 17/10/2026 | 31/10/2026 |
| R-03 | Relevé des sections des pannes existantes (EXI-01) | Ouverte | GO (nous) | 17/10/2026 | 24/10/2026 (visite site) |
| R-04 | Essai de résistance de la maçonnerie existante (EXI-03) | Ouverte | GO (nous, à commander) | 17/10/2026 | 31/10/2026 |
| R-05 | Analyse structurelle de l'existant (EXI-05) | Ouverte | BET STRUCTURE PARTIEL | 17/10/2026 | 15/11/2026 |
| R-06 | Nature exacte des chaînages existants (MAT-12) | Ouverte | GO (relevé site) | 17/10/2026 | 24/10/2026 (visite site) |
| R-07 | Détail du complexe de plancher neuf (CHG-03) | Ouverte | Architecte (Atelier Martin) | 17/10/2026 | 24/10/2026 |
| R-08 | Détail du complexe de toiture (CHG-04) | Ouverte | Architecte (Atelier Martin) | 17/10/2026 | 24/10/2026 |
| R-09 | Détail de l'escalier métallique (CHG-08) | Ouverte | Architecte (Atelier Martin) | 17/10/2026 | 24/10/2026 |
| R-10 | Diagnostic amiante / plomb | Ouverte | MOA (SCI LES LILAS) | 17/10/2026 | Avant démarrage travaux |

Règles : une réserve ne se ferme que par une entrée en FDC (valeur + source) ou une décision en Section 1 (valeur déclarée, avec auteur et date).
________________


Section 3 — REGISTRE DES VERROUS

| N° | Donnée (code) | Brique suspendue | Date | Responsable | Briques exécutées malgré tout | Mode de contournement |
| --- | --- | --- | --- | --- | --- | --- |
| V-01 | SOL-01 (q_adm ELS) | B-40 (Fondations) | 17/10/2026 | MOA (via R-01) | B-21, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-60 (hors fondations) | PARAMÉTRIQUE (cf. D-04) |
| V-02 | SOL-02 (q_adm ELU) | B-40 | 17/10/2026 | MOA (via R-01) | Idem V-01 | PARAMÉTRIQUE |
| V-03 | SOL-03 (profondeur bon sol) | B-40 | 17/10/2026 | MOA (via R-01) | Idem V-01 | PARAMÉTRIQUE |
| V-04 | SOL-05 (agressivité sol) | B-40, B-42, B-43 | 17/10/2026 | MOA (via R-01) | B-42, B-43 (avec hypothèse XC2 en attendant) | PARAMÉTRIQUE (B-40) / PARTIEL-DÉCLARÉ (B-42, B-43 — hypothèse XC2) |
| V-05 | SEC-01 (coupe-feu) | B-42, B-43, B-47, B-48, B-49 | 17/10/2026 | BC SOCOTEC (via R-02) | B-42, B-43, B-47, B-48, B-49 (formules complètes, enrobage en littéral) | PARAMÉTRIQUE |
| V-06 | EXI-01 (sections charpente) | B-44 (Charpente bois) | 17/10/2026 | GO (via R-03) | B-44 (formules complètes, sections en littéral) | PARAMÉTRIQUE (cf. D-09) |
| V-07 | EXI-03 (résistance maçonnerie) | B-46 (Maçonnerie Bloc A) | 17/10/2026 | GO (via R-04) | B-46 Bloc B (maçonnerie neuve) | PARTIEL-DÉCLARÉ (cf. D-05) |
| V-08 | EXI-05 (contrainte admissible existant) | B-40, B-46, B-49 | 17/10/2026 | BET STRUCTURE PARTIEL (via R-05) | B-40 (PARAMÉTRIQUE), B-46 Bloc A (PARTIEL-DÉCLARÉ), B-49 (PARAMÉTRIQUE) | PARTIEL-DÉCLARÉ / PARAMÉTRIQUE |
| V-09 | MAT-12 (nature chaînages existants) | B-46 (Maçonnerie Bloc A) | 17/10/2026 | GO (via R-06) | B-46 Bloc B (maçonnerie neuve) | PARTIEL-DÉCLARÉ |
| V-10 | CHG-03 (complexe plancher neuf) | B-42, B-43 | 17/10/2026 | Architecte (via R-07) | B-42, B-43 (avec hypothèse 5,8 kN/m²) | PARTIEL-DÉCLARÉ (hypothèse H-05) |
| V-11 | CHG-04 (complexe toiture) | B-44 (Charpente bois) | 17/10/2026 | Architecte (via R-08) | B-44 (avec hypothèse 1,80 kN/m²) | PARTIEL-DÉCLARÉ (hypothèse H-06) |
| V-12 | CHG-08 (escalier métallique) | B-47, B-50 | 17/10/2026 | Architecte (via R-09) | B-47, B-50 (formules complètes, charge en littéral) | PARAMÉTRIQUE |

Règles :
   * Un verrou ne se ferme que par entrée en FDC ou décision en Section 1.
   * La requalification NON BLOQUANTE → BLOQUANTE est autorisée (avec suspension immédiate). L'inverse est interdit (verrou V12).
   * Le Registre des Verrous liste toujours ce qui a été fait malgré tout — c'est ce qui vous protège en cas de litige.
________________


Synthèse du RDR

| Catégorie | Nombre |
| --- | --- |
| Détail | Décisions (Section 1) |
| 10 | D-01 à D-10, toutes avec auteur et date |
| Réserves (Section 2) | 10 |
| R-01 à R-10, toutes ouvertes à la date du 17/10/2026 | Verrous (Section 3) |
| 12 | V-01 à V-12, tous avec brique suspendue et briques exécutées malgré tout |

Ce que le RDR vous permet de dire en réunion de lancement
Sur les décisions :
« La MPD est validée (D-01), la FDC est validée (D-02). La conception structure GO est en mode PARTIEL-DÉCLARÉ (D-03) — le BET fournit les plans des planchers existants, nous concevons les renforcements. Les fondations sont en mode PARAMÉTRIQUE (D-04) — le G2 AVP ne suffit pas, une G3 est recommandée. La maçonnerie existante est en mode PARTIEL-DÉCLARÉ (D-05) — résistance estimée à 2,0 MPa, sans essai. La charpente bois est en mode PARAMÉTRIQUE (D-09) — les sections ne sont pas relevées. Les fondations profondes sont SANS OBJET (D-10) — il n'y en a pas. »
Sur les réserves :
« Nous avons demandé la mission G3 à la MOA (R-01, échéance 31/10), la note coupe-feu au BC (R-02, échéance 31/10), le relevé des pannes et des chaînages à notre équipe (R-03, R-06, échéance 24/10), l'essai de résistance de la maçonnerie (R-04, échéance 31/10), l'analyse structurelle de l'existant au BET (R-05, échéance 15/11), les détails du complexe de plancher, de toiture et de l'escalier à l'architecte (R-07 à R-09, échéance 24/10), et le diagnostic amiante/plomb à la MOA (R-10, avant démarrage). »
Sur les verrous :
« Douze données sont bloquantes. Pour chacune, nous avons identifié la brique suspendue et exécuté tout ce qui était faisable. Le Registre des Verrous documente précisément ce qui reste à obtenir, auprès de qui, et pour quand. Les briques concernées sont en mode PARAMÉTRIQUE (formules littérales, non exécutables) ou PARTIEL-DÉCLARÉ (valeur déclarée avec hypothèse). Aucune brique n'est en mode COMPLET sur une donnée bloquante manquante. »
Sur les modes dégradés :
« Sur les 11 briques de calcul, 4 sont en mode COMPLET (B-42, B-43, B-45, B-48), 4 en mode PARTIEL-DÉCLARÉ (B-42, B-43, B-46, B-47), 3 en mode PARAMÉTRIQUE (B-40, B-44, B-49), 1 en mode SANS OBJET (B-41). Le mode global du projet est PARTIEL-DÉCLARÉ — les livrables concernés portent la mention « sous hypothèse » et les livrables PARAMÉTRIQUE sont filigranés _P. »
Sur la clôture :
« À la clôture (B-72), les points ouverts seront listés : les 10 réserves, les 15 verrous non fermés, les décisions en attente. Le journal de clôture ne déclarera pas le projet clos substantiellement — il déclarera la production des études remise, avec les points ouverts explicitement listés. C'est ce qui nous protège en cas de litige sur un retard ou sur une malfaçon. »
________________


Ce que ce RDR illustre
1. Le principe « une décision sans auteur et sans date n'existe pas » : chaque décision (D-01 à D-10) a un auteur (GO) et une date (17/10/2026). Elle est donc opposable.
2. Le principe « six modes, cinq décisions » : chaque brique qui n'est pas en COMPLET a une décision explicite qui justifie son mode :
   * D-03 : B-20 en PARTIEL-DÉCLARÉ (BET partiel).
   * D-04 : B-40 en PARAMÉTRIQUE (G2 AVP insuffisant).
   * D-05 : B-46 Bloc A en PARTIEL-DÉCLARÉ (résistance estimée).
   * D-09 : B-44 en PARAMÉTRIQUE (sections non relevées).
   * D-10 : B-41 en SANS OBJET (pas de fondations profondes).
3. Le principe « une réserve par donnée manquante » : chaque réserve (R-01 à R-10) correspond à une donnée manquante, avec un responsable et une échéance. Rien n'est laissé au hasard.
4. Le principe « un verrou par brique suspendue » : chaque verrou (V-01 à V-12) correspond à une brique suspendue, avec la liste des briques exécutées malgré tout. C'est ce qui prouve que vous n'avez pas attendu les pieds croisés.
5. Le principe « requalification à sens unique » : si une donnée NON BLOQUANTE se révèle BLOQUANTE en cours de projet (par exemple, une donnée qu'on croyait secondaire devient indispensable), la requalification est inscrite au registre avec :
   * la donnée concernée ;
   * la brique suspendue ;
   * la date de requalification ;
   * la raison.
L'inverse (une donnée BLOQUANTE qui devient NON BLOQUANTE) est interdit — sauf par une décision RDR écrite (valeur déclarée, avec auteur et date).
6. Le cas des modes dégradés : sur 11 briques de calcul, aucune n'est en COMPLET sur une donnée bloquante manquante. Les modes dégradés sont :
   * PARTIEL-DÉCLARÉ : B-20, B-42, B-43, B-46 (Bloc A) ;
   * PARAMÉTRIQUE : B-40, B-44, B-49 ;
   * SANS OBJET : B-41 ;
   * COMPLET : B-45, B-48, B-46 (Bloc B).
7. Le cas de la clôture : à la clôture (B-72), les 10 réserves et les 15 verrous seront listés. Le journal de clôture ne déclarera pas le projet clos substantiellement — il déclarera la production des études remise, avec les points ouverts explicitement listés. C'est ce qui vous protège en cas de litige sur un retard ou sur une malfaçon.
________________


**[Fin — exemple de RDR]**
Récapitulatif complet — Arborescence CARNAC v1.1
1. Vue d'ensemble
Le carnet CARNAC v1.1 est organisé en 11 répertoires contenant 49 fichiers :

| Répertoire | Nature | Nombre de fichiers | Statut |
| --- | --- | --- | --- |
| 00_MASTER.md (racine) | Document maître | 1 | ✔ Produit |
| 01_DICTIONNAIRE/ | Bibliothèque de variables | 1 | ✔ Produit |
| 02_PHASE_0_CADRAGE/ | Fiches B-00 à B-04 | 5 | ✔ Produit |
| 03_PHASE_1_ANALYSE/ | Fiches B-10 à B-15 | 6 | ✔ Produit |
| 04_PHASE_2_CONCEPTION/ | Fiches B-20 à B-24 | 5 | ✔ Produit |
| 05_PHASE_3_CALAGE/ | Fiches B-30 à B-33 | 4 | ✔ Produit |
| 06_PHASE_4_CALCULS/ | Fiches B-40 à B-50 | 11 | ✔ Produit |
| 07_PHASE_5_LIVRABLES/ | Fiches B-60, B-62, B-64 | 3 | ✔ Produit |
| 08_PHASE_6_CLOTURE/ | Fiches B-70 à B-72 | 3 | ✔ Produit |
| 09_TRANSVERSE/ | Fiches T-01 à T-04 | 4 | ✔ Produit |
| 10_ANNEXES/ | Annexes A, C, D | 3 | ✔ Produit |
| 11_HISTORIQUE/ | Journal des modifications | 1 | ✔ Produit |
| Total | — | 49 fichiers | ✔ Complet |

________________


2. Arborescence complète
text
CARNAC_v1.1/
│
├── 00_MASTER.md
│   └── Document maître : index, principes, 15 verrous, 5 modes, arborescence
│
├── 01_DICTIONNAIRE/
│   └── CARNAC_v1.1_variables.csv
│       └── 92 variables avec bloque/mentionnée, version (v1.0 ou v1.1)
│
├── 02_PHASE_0_CADRAGE/
│   ├── B-00_Inventaire.md              ← Inventaire des pièces + mission reformulée
│   ├── B-01_MPD.md                     ← Matrice de Périmètre et de Disponibilité
│   ├── B-02_FDC.md                     ← Fiche de Données de Conception
│   ├── B-03_RDR.md                     ← Registre des Décisions et Réserves
│   └── B-04_PTD.md                     ← Plan de Travail Dégradé
│
├── 03_PHASE_1_ANALYSE/
│   ├── B-10_Audit_CCTP.md              ← Audit critique du CCTP
│   ├── B-11_Audit_Diagnostic.md        ← Audit du diagnostic existant
│   ├── B-12_Audit_Geotechnique.md      ← Audit des pièces géotechniques
│   ├── B-13_Contradictions.md          ← Détection et qualification des contradictions
│   ├── B-14_Perimetre_Lot.md           ← Clarification du périmètre de lot
│   └── B-15_Synthese_Risques.md        ← Fiche de synthèse des risques
│
├── 04_PHASE_2_CONCEPTION/
│   ├── B-20_Conception_GO.md           ← Conception structure GO (INTERNE-GO)
│   ├── B-21_DDC_Preliminaire.md        ← Descente de charges préliminaire
│   ├── B-22_Note_Hypotheses.md         ← Note d'hypothèses unique du projet
│   ├── B-23_Exploitation_Diagnostic.md ← Exploitation du diagnostic existant
│   └── B-24_Existant_Non_Sonde.md      ← Vérification de l'existant non sondé
│
├── 05_PHASE_3_CALAGE/
│   ├── B-30_Calage.md                  ← Calage sur DXF/DWG source (une fois par projet)
│   ├── B-31_Preuve_Superposition.md    ← Preuve de superposition (à chaque livrable)
│   ├── B-32_Vue_Nettoyee.md            ← Vue nettoyée par livrable
│   └── B-33_Verification_Croisee.md    ← Vérification croisée (plan ↔ source + plan ↔ plan)
│
├── 06_PHASE_4_CALCULS/
│   ├── B-40_Fondations_Superficielles.md
│   ├── B-41_Fondations_Profondes.md
│   ├── B-42_Verticaux_BA.md
│   ├── B-43_Planchers_Dallages.md
│   ├── B-44_Charpente_Bois.md
│   ├── B-45_Structure_Metallique.md
│   ├── B-46_Maconnerie.md
│   ├── B-47_Escaliers.md
│   ├── B-48_Predalles.md
│   ├── B-49_Linteaux_Seuils.md
│   └── B-50_Assemblages_Ancrages.md    ← Brique pivot du contrôle croisé (option C)
│
├── 07_PHASE_5_LIVRABLES/
│   ├── B-60_Plans_Execution.md         ← Plans + coupes + détails + export DXF
│   ├── B-62_Nomenclature.md            ← Nomenclature et façonnage
│   └── B-64_Notice_Synthese.md         ← Notice de synthèse du livrable
│
├── 08_PHASE_6_CLOTURE/
│   ├── B-70_AutoControle_Synthese.md   ← Auto-contrôle de synthèse et de cohérence
│   ├── B-71_Indicage.md                ← Indiçage et supersession documentaire
│   └── B-72_Journal_Cloture.md         ← Journal de clôture du projet
│
├── 09_TRANSVERSE/
│   ├── T-01_Sincerite.md               ← Test de sincérité d'un livrable
│   ├── T-02_Recadrage.md               ← Recadrage par diagnostic (cause + méthode)
│   ├── T-03_Meta_Amelioration.md       ← Méta-amélioration (corrections au carnet)
│   └── T-04_Demande_Complement.md      ← Demande formelle à la MOE/BET/MOA
│
├── 10_ANNEXES/
│   ├── A_Conventions_Livrables.md      ← Calques, échelles, formats, cartouche, unités
│   ├── C_Journal_Revisions.md          ← Versions du carnet (v1.0, v1.1, v1.2, v2.0)
│   └── D_Mode_Emploi.md                ← Mode d'emploi en 6 étapes + précautions
│
└── 11_HISTORIQUE/
    └── Journal_des_modifications.md    ← Détail de toutes les modifications (C-01 à C-05, E-01, CC-01)
________________


3. Relations entre les fichiers
3.1 Documents de référence (lus en permanence)
text
00_MASTER.md ◄──── Toutes les fiches (référence pour les verrous et les modes)
    │
    ├── 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv (92 variables)
    │
    ├── 10_ANNEXES/A_Conventions_Livrables.md (calques, échelles, cartouche)
    │
    ├── 10_ANNEXES/C_Journal_Revisions.md (versions du carnet)
    │
    ├── 10_ANNEXES/D_Mode_Emploi.md (comment utiliser le carnet)
    │
    └── 11_HISTORIQUE/Journal_des_modifications.md (traçabilité des modifications)
3.2 Chaîne de production (ordre d'exécution)
text
Phase 0 — Cadrage
B-00 ──► B-01 ──► B-02 ──► B-03 ──► B-04
(inventaire)  (MPD)  (FDC)  (RDR)  (PTD)
    │          │      │      │      │
    └──────────┴──────┴──────┴──────┘
                    │
                    ▼
Phase 1 — Analyse
B-10 ──► B-11 ──► B-12 ──► B-13 ──► B-14 ──► B-15
(CCTP) (diag)  (géo)  (contra) (périmètre) (risques)
                    │
                    ▼
Phase 2 — Conception
B-20 ──► B-21 ──► B-22 ──► B-23 ──► B-24
(GO)   (DDC)  (hypothèses) (exploitation) (existant non sondé)
                    │
                    ▼
Phase 3 — Calage (B-30 une fois) + B-31/B-32/B-33 (à chaque livrable)
B-30 ──► B-32 ──► B-31 ──► B-33
                    │
                    ▼
Phase 4 — Calculs
B-40 à B-50 (chaque brique : DDC, vérifications, dispositions, efforts B-50)
                    │
                    ▼
Phase 5 — Livrables
B-60 ──► B-62 ──► B-64
(plans) (nomenclature) (notice)
                    │
                    ▼
Phase 6 — Clôture
B-70 ──► B-71 ──► B-72
(auto-contrôle) (indiçage) (journal)
3.3 Prompts transverse (à tout moment)
text
T-01 (sincérité)     → T-02 (recadrage) si défaut détecté
T-02 (recadrage)     → La brique source corrige
T-03 (méta-amélioration) → Nouvelle version du carnet
T-04 (demande complément) → La brique concernée attend la réponse
________________


4. Fichiers à créer au démarrage d'un projet
Pour chaque nouveau projet, vous créez les documents de projet suivants (distincts du carnet) :
text
[PROJET]/
│
├── 00_MPD_du_projet.md            ← Sortie de B-01 (validée par vous)
├── 01_FDC_du_projet.md            ← Sortie de B-02 (valeurs + sources)
├── 02_RDR_du_projet.md            ← Sortie de B-03 (décisions + réserves + verrous)
├── 03_PTD_du_projet.md            ← Sortie de B-04 (plan de travail dégradé)
├── 04_Hypotheses_du_projet.md     ← Sortie de B-22 (note d'hypothèses unique)
├── 05_RDL_du_projet.md            ← Registre des Livrables (créé et mis à jour à chaque livrable)
├── 06_Notes_de_calcul/            ← B-40 à B-50 (une note par brique exécutée)
├── 07_Plans/                      ← B-60 (plans, coupes, détails, DXF)
├── 08_Nomenclatures/              ← B-62 (nomenclatures + façonnage)
├── 09_Notices/                    ← B-64 (notice de synthèse par livrable)
└── 10_Auto-controles/             ← B-70 (auto-contrôles de synthèse)
________________


5. Guide de lecture pour un nouvel utilisateur
Si vous découvrez le carnet :
   1. Lire 00_MASTER.md (10 à 15 pages) — pour comprendre les principes, les verrous, les modes.
   2. Lire 10_ANNEXES/D_Mode_Emploi.md (5 à 6 pages) — pour comprendre comment utiliser le carnet.
   3. Consulter 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv — pour connaître les variables disponibles.
Si vous démarrez un projet :
   1. Ouvrir 02_PHASE_0_CADRAGE/B-00_Inventaire.md — copier le prompt, fournir les pièces.
   2. Suivre la chaîne : B-00 → B-01 → B-02 → B-03 → B-04.
   3. Continuer phase par phase.
Si vous avez un doute sur un livrable :
   1. Ouvrir 09_TRANSVERSE/T-01_Sincerite.md — tester la sincérité.
   2. Si défaut détecté : ouvrir 09_TRANSVERSE/T-02_Recadrage.md.
   3. Si défaut récurrent : ouvrir 09_TRANSVERSE/T-03_Meta_Amelioration.md.
Si une donnée bloque :
   1. Consulter 02_PHASE_0_CADRAGE/B-04_PTD.md — savoir ce qui est faisable.
   2. Ouvrir 09_TRANSVERSE/T-04_Demande_Complement.md — demander la donnée.
________________


6. Ce que contient chaque fichier en résumé
Documents de référence (5 fichiers)

| Fichier | Objet | Pages |
| --- | --- | --- |
| 00_MASTER.md | Index, principes, 15 verrous, 5 modes, arborescence | 10-15 |
| 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv | 92 variables avec bloque/mentionnée | 1 (CSV) |
| 10_ANNEXES/A_Conventions_Livrables.md | Calques, échelles, formats, cartouche, unités | 8-10 |
| 10_ANNEXES/C_Journal_Revisions.md | Versions du carnet (v1.0, v1.1, v1.2, v2.0) | 5-6 |
| 10_ANNEXES/D_Mode_Emploi.md | Comment utiliser le carnet | 5-6 |
| 11_HISTORIQUE/Journal_des_modifications.md | Traçabilité des modifications | 6-8 |

Fiches de brique (37 fichiers)
Chaque fiche comporte :
   * En-tête : version, phase, modes, entrées, sortie, critère d'acceptation (pour vous) ;
   * Prompt : bloc de code à copier dans l'IA ;
   * Justification : pourquoi chaque clause existe (pour vous) ;
   * Références : briques amont/aval, variables consommées.
Chaque fiche fait 3 à 6 pages.
Prompts transverse (4 fichiers)
Même structure que les fiches de brique — utilisables à tout moment.
________________


7. Les 5 règles à retenir
   1. Un projet = 37 briques + 4 prompts transverse. Chaque brique est autonome — vous ouvrez la fiche, vous copiez le prompt, vous fournissez les entrées.
   2. Le mode doit être honnête. Une brique dont une donnée bloquante manque ne peut pas être en mode COMPLET. Un livrable PARAMÉTRIQUE doit être filigrané.
   3. Les sources doivent être citées. Tout élément dessiné, calculé ou affirmé est rattaché à une pièce. Sans source, pas de production.
   4. La mise à jour est incrémentale. Une modification de source ne régénère que les livrables impactés (via le RDL) — pas tout le projet.
   5. Les textes avant/après les prompts sont pour vous. Vous copiez dans l'IA uniquement le bloc de code entre triples backquotes.
________________


8. Prochaines étapes possibles
Le carnet est complet et prêt à être utilisé. Vous pouvez :
   1. Le tester à blanc sur un projet existant (par exemple, rejouer Flora avec CARNAC v1.1) — pour identifier les ajustements nécessaires.
   2. L'enrichir après chaque projet réel (T-03 → v1.2) — pour intégrer les corrections issues de la pratique.
   3. Le réviser après trois projets (v2.0) — si un changement d'architecture s'avère nécessaire.
   4. Le diffuser à votre équipe — avec les documents de référence (master, mode d'emploi, dictionnaire) et les fiches de brique.
________________


Fin du récapitulatif complet.
Check-list de démarrage de projet — CARNAC v1.1
Mode d'emploi de cette check-list
Cette check-list est conçue pour être imprimée et cochée au fur et à mesure de l'avancement du projet. Elle reprend les étapes du mode d'emploi (annexe D) et les organise en cases à cocher, avec les points de contrôle critiques.
Convention :
   * ☐ case à cocher — action à faire
   * ⚠ point de contrôle critique — validation obligatoire par vous
   * 📄 document à produire — sortie attendue
________________


PHASE 0 — CADRAGE (1 à 2 jours)
Avant de commencer
☐ Vérifier que le carnet CARNAC v1.1 est complet (49 fichiers)
☐ Vérifier que le dictionnaire de variables est à jour (92 variables)
☐ Créer le répertoire projet [CODE_PROJET]/ avec l'arborescence standard
☐ Préparer la liste des pièces reçues (fichiers, formats, indices)
Étape 0.1 — Inventaire (B-00)
☐ Ouvrir 02_PHASE_0_CADRAGE/B-00_Inventaire.md
☐ Copier le bloc de code de la section 2
☐ Remplacer {{ID-01}} et {{ID-02}} par les valeurs du projet
☐ Fournir à l'IA : toutes les pièces du projet + énoncé de mission
☐ Récupérer la sortie : inventaire + contradictions + mission reformulée
⚠ Valider : chaque pièce est listée avec son indice ; les contradictions sont listées sans être résolues ; la mission tient en 5 lignes
📄 Sauvegarder : [PROJET]/00_B00_Inventaire.md
Étape 0.2 — Matrice de Périmètre et de Disponibilité (B-01)
☐ Ouvrir 02_PHASE_0_CADRAGE/B-01_MPD.md
☐ Copier le bloc de code
☐ Remplacer {{ID-01}}
☐ Fournir : sortie de B-00 + dictionnaire de variables
☐ Récupérer la sortie : MPD proposée (tableau 8 colonnes)
⚠ Valider LIGNE PAR LIGNE les NON NÉCESSAIRE (périmètre) — c'est votre décision
⚠ Vérifier : chaque NON NÉCESSAIRE a un motif de périmètre (pas « pas dispo ») ; chaque BLOQUANTE est rattaché à une brique ; chaque À PRODUIRE PAR GO identifie la brique INTERNE-GO
📄 Sauvegarder : [PROJET]/01_B01_MPD.md (version validée)
Étape 0.3 — Fiche de Données de Conception (B-02)
☐ Ouvrir 02_PHASE_0_CADRAGE/B-02_FDC.md
☐ Copier le bloc de code
☐ Remplacer {{ID-01}}
☐ Fournir : MPD validée + pièces du projet + décisions déjà prises
☐ Récupérer la sortie : FDC avec valeurs + sources + fiabilité + verrous
⚠ Valider chaque valeur et son niveau de fiabilité (Contractuelle / Décision / À confirmer)
⚠ Vérifier : chaque ligne a une source citée ou est marquée VERROU ; aucun champ sans fiabilité ; les VERROU sont en fin de FDC avec voie d'obtention
📄 Sauvegarder : [PROJET]/02_B02_FDC.md (version validée)
Étape 0.4 — Registre des Décisions et Réserves (B-03)
☐ Ouvrir 02_PHASE_0_CADRAGE/B-03_RDR.md
☐ Copier le bloc de code
☐ Remplacer {{ID-01}}, {{ID-05}}, {{ID-07}}
☐ Fournir : MPD validée + FDC + échanges MOA/MOE/BET
☐ Récupérer la sortie : RDR en 3 sections (Décisions / Réserves / Verrous)
⚠ Valider chaque décision (auteur, date, effet sur les briques) — c'est votre signature
⚠ Valider chaque réserve (responsable, échéance)
⚠ Valider chaque verrou (brique suspendue, briques exécutées malgré tout)
📄 Sauvegarder : [PROJET]/03_B03_RDR.md (version validée)
Étape 0.5 — Plan de Travail Dégradé (B-04)
☐ Ouvrir 02_PHASE_0_CADRAGE/B-04_PTD.md
☐ Copier le bloc de code
☐ Remplacer {{ID-01}}
☐ Fournir : MPD + FDC + RDR + dictionnaire
☐ Récupérer la sortie : PTD en 3 tableaux (suspendues / exécutables / paramétriques)
⚠ Vérifier : chaque brique suspendue identifie la donnée bloquante ; chaque brique exécutable est justifiée ; chaque PARAMÉTRIQUE précise ce qui ne sera pas produit ; aucun SANS OBJET décidé par le modèle
📄 Sauvegarder : [PROJET]/04_B04_PTD.md
Fin de la phase 0
☐ Créer le RDL : [PROJET]/05_RDL_du_projet.md (Registre des Livrables) — première ligne : le RDL lui-même
☐ Créer le fichier des hypothèses : [PROJET]/04_Hypotheses_du_projet.md (note d'hypothèses unique, à alimenter en B-22)
⚠ Réunion de lancement : présenter à la MOE le PTD (ce qui est suspendu, ce qui est exécutable, ce qui est en attente)
☐ Envoyer les demandes de complément urgentes via T-04 (si données bloquantes)
________________


PHASE 1 — ANALYSE (3 à 5 jours)
Étape 1.1 — Audit CCTP (B-10)
☐ Ouvrir 03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : CCTP + plans BET + énoncé de mission + MPD
☐ Récupérer la sortie : 4 tableaux (constats / lacunes / contradictions / points à lever)
⚠ Valider : chaque constat est rattaché à un article précis ; chaque lacune identifie la brique concernée ; chaque point à lever a un destinataire et une urgence
📄 Sauvegarder : [PROJET]/10_B10_Audit_CCTP.md
Étape 1.2 — Audit Diagnostic (B-11)
☐ Ouvrir 03_PHASE_1_ANALYSE/B-11_Audit_Diagnostic.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : diagnostic + récolement/DOE + plans BET sur existant
☐ Récupérer la sortie : 4 tableaux (désordres / prescriptions / données manquantes / points à lever)
⚠ Vérifier : chaque [ANALYSE GO] est bien la vôtre, pas une reformulation du diagnostic ; chaque prescription du diagnostic est marquée « à valider par B-xx »
📄 Sauvegarder : [PROJET]/11_B11_Audit_Diagnostic.md
Étape 1.3 — Audit Géotechnique (B-12)
☐ Ouvrir 03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : rapport géotechnique + MPD + énoncé de mission
☐ Récupérer la sortie : 3 tableaux (données disponibles / données manquantes / recommandation de mission)
⚠ Décider : commander (ou non) la mission complémentaire — c'est une décision MOA
⚠ Vérifier : chaque recommandation cite sa base normative et la conséquence de sa non-commande
📄 Sauvegarder : [PROJET]/12_B12_Audit_Geotechnique.md
Étape 1.4 — Contradictions (B-13)
☐ Ouvrir 03_PHASE_1_ANALYSE/B-13_Contradictions.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : B-10 + B-11 + B-12 + B-00 + MPD
☐ Récupérer la sortie : tableau des contradictions qualifiées (gravité × nature) + tableau par brique
⚠ Valider : le classement gravité × nature ; chaque contradiction est rattachée à une brique ; les doublons sont éliminés
⚠ Vérifier : test « les deux affirmations peuvent-elles être vraies en même temps ? » appliqué
📄 Sauvegarder : [PROJET]/13_B13_Contradictions.md
Étape 1.5 — Périmètre de lot (B-14)
☐ Ouvrir 03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : B-10 + B-11 + énoncé de mission
☐ Récupérer la sortie : 4 tableaux (INCLUSES / EXCLUES / À TRANCHER / hors CARNAC)
⚠ Valider : les prestations À TRANCHER — une prestation que vous acceptez implicitement devient la vôtre
⚠ Vérifier : chaque prestation INCLUSE cite l'article du CCTP ; chaque prestation EXCLUE cite la pièce qui l'attribue à un autre lot
📄 Sauvegarder : [PROJET]/14_B14_Perimetre_Lot.md
Étape 1.6 — Synthèse des risques (B-15)
☐ Ouvrir 03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{périmètre_analyse}}
☐ Choisir le périmètre : « B-13 seule » ou « ensemble de la phase Analyse »
☐ Fournir : les sorties correspondantes
☐ Récupérer la sortie : registre des risques (cotation P×I) + risques résiduels
⚠ Valider : les risques résiduels acceptés — c'est l'engagement qui vous engage
⚠ Vérifier : chaque risque est rattaché à une source ; chaque cotation est justifiée ; chaque risque a un responsable et une échéance
📄 Sauvegarder : [PROJET]/15_B15_Synthese_Risques.md
Fin de la phase 1
☐ Mettre à jour le RDR : les points à lever, risques, contradictions deviennent des réserves (R-xx) ou des décisions (D-xx)
☐ Envoyer les demandes de complément via T-04 (si nouvelles données bloquantes)
⚠ Réunion de synthèse : présenter à la MOE les risques, contradictions, périmètre à trancher
________________


PHASE 2 — CONCEPTION (2 à 10 jours)
Étape 2.1 — Conception GO (B-20)
☐ Ouvrir 04_PHASE_2_CONCEPTION/B-20_Conception_GO.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{mode}} (par INTERNE-GO, PARTIEL-DÉCLARÉ ou SANS OBJET)
☐ Fournir : MPD + B-11 + B-12 + B-23 + B-24 (si exécutée) + plans archi + énoncé de mission
☐ Récupérer la sortie : note de prédimensionnement + plans de principe + liste des points à faire valider
⚠ Viser la conception : par vous, un BET, ou le BC — avant que les briques de calcul ne s'appuient dessus
⚠ Vérifier : chaque position de porteur est justifiée ; chaque section est justifiée par une méthode citée ; chaque plan porte le filigrane « PRINCIPE — NE PAS EXÉCUTER » et un indice P
📄 Sauvegarder : [PROJET]/20_B20_Conception_GO.md + plans de principe
Étape 2.2 — DDC préliminaire (B-21)
☐ Ouvrir 04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{mode}}
☐ Fournir : charges d'exploitation + poids propres + géométrie + porteurs B-20
☐ Récupérer la sortie : 5 tableaux (surfaces / G / Q / ELS / ELU)
⚠ Valider : les catégories d'usage EC1 et les cloisons forfaitaires — c'est votre appréciation
⚠ Vérifier : la sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION » ; les tableaux ELS et ELU sont distincts ; aucune vérification de section n'a été produite
📄 Sauvegarder : [PROJET]/21_B21_DDC_Preliminaire.md
Étape 2.3 — Note d'hypothèses (B-22)
☐ Ouvrir 04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : FDC + RDR + toutes les briques de phase 2
☐ Récupérer la sortie : note d'hypothèses unique (index / détail / historique)
⚠ Valider chaque hypothèse à son introduction — une hypothèse validée trop tard est une hypothèse qui a déjà contaminé les calculs
⚠ Vérifier : chaque hypothèse a un numéro stable H-xx ; chaque hypothèse a une justification ; les hypothèses abandonnées sont conservées
📄 Sauvegarder : [PROJET]/04_Hypotheses_du_projet.md (mis à jour)
Étape 2.4 — Exploitation du diagnostic (B-23)
☐ Ouvrir 04_PHASE_2_CONCEPTION/B-23_Exploitation_Diagnostic.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : B-11 + B-20 + diagnostic + plans existants
☐ Récupérer la sortie : 4 tableaux (contraintes / renforcements / zones hors relevé / appuis sur existant)
⚠ Valider : la catégorisation des contraintes (renforcement obligatoire / sous condition / phasage / coordination lot / sans impact)
⚠ Vérifier : aucune solution technique chiffrée n'est proposée ; les zones hors relevé sont identifiées avec leur emprise
📄 Sauvegarder : [PROJET]/23_B23_Exploitation_Diagnostic.md
Étape 2.5 — Existant non sondé (B-24)
☐ Ouvrir 04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : EXI-01 à EXI-04 (si partielles) + B-11 + B-23
☐ Récupérer la sortie : 4 tableaux (éléments non sondés / sensibilité / essais / impact)
⚠ Vérifier : le tableau de sensibilité est marqué « NON CONTRACTUEL » ; les essais sont listés avec référentiel, nombre, emprise ; aucune valeur n'est retenue
⚠ Décider : commander les essais, ou inscrire au RDR une valeur déclarée
📄 Sauvegarder : [PROJET]/24_B24_Existant_Non_Sonde.md
Fin de la phase 2
☐ Mettre à jour le RDR : les décisions de mode (B-20 en INTERNE-GO ou PARTIEL-DÉCLARÉ, etc.), les essais à commander, les hypothèses à confirmer
⚠ Réunion de conception : présenter la conception GO et les hypothèses à la MOE/BET/BC
________________


PHASE 3 — CALAGE (1 à 2 jours + à chaque livrable)
Étape 3.1 — Calage (B-30) — UNE FOIS par projet
☐ Ouvrir 05_PHASE_3_CALAGE/B-30_Calage.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{mode}}
☐ Fournir : plans archi vectoriels + unités + points de calage
☐ Récupérer la sortie : paramètres de calage + preuve + fichier recalé indicé
⚠ Valider le résidu de calage (≤ 1 cm) — c'est votre appréciation de la tolérance
⚠ Vérifier : ≥ 3 points de calage non alignés ; résidu mesuré sur points témoins ; fichier recalé nommé et indicé
📄 Sauvegarder : [PROJET]/30_B30_Calage.md + fichier recalé
Étape 3.2 à 3.4 — À CHAQUE livrable graphique
Pour chaque livrable (B-40 à B-50) :
☐ Ouvrir 05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{indice_livrable}}, {{mode}}
☐ Fournir : fichier calé + type de livrable
☐ Récupérer la sortie : vue nettoyée + tableau de nettoyage + consignation RDL
⚠ Valider : la liste des calques À TRANCHER
📄 Sauvegarder : [PROJET]/32_B32_Vue_Nettoyee_[livrable].md + vue nettoyée
☐ Ouvrir 05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{mode}}
☐ Fournir : fichier calé + livrable + vue nettoyée
☐ Récupérer la sortie : superposition + tableau de contrôle + synthèse
⚠ Valider le verdict global : conforme / écart acceptable / à corriger
📄 Sauvegarder : [PROJET]/31_B31_Preuve_Superposition_[livrable].md
☐ Ouvrir 05_PHASE_3_CALAGE/B-33_Verification_Croisee.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{code_livrable}}
☐ Fournir : livrable + fichier calé + vue nettoyée + RDL (liste des livrables antérieurs)
☐ Récupérer la sortie : rapport section 1 (plan ↔ source) + section 2 (plan ↔ plan) + synthèse
⚠ Valider : les écarts section 2 avant de relancer la brique source
📄 Sauvegarder : [PROJET]/33_B33_Verification_Croisee_[livrable].md
________________


PHASE 4 — CALCULS (10 à 30 jours)
Pour chaque brique de calcul (B-40 à B-50)
Choisir la brique selon le type d'élément (cf. mode d'emploi §3.4.3)
☐ Ouvrir la fiche correspondante (06_PHASE_4_CALCULS/B-xx_[nom].md)
☐ Lire l'en-tête : mode d'appel, entrées lues, sortie attendue
☐ Copier le bloc de code
☐ Remplacer tous les {{...}} : {{ID-01}}, {{ID-02}}, {{mode}}, et le paramètre spécifique ({{élément}}, {{type}}, {{bloc}}, {{phase}}, {{famille}})
☐ Fournir les données d'entrée (FDC, DDC, hypothèses, notes amont)
☐ Récupérer la sortie : note de calcul + plans + auto-contrôle
⚠ Vérifier le mode : la brique est-elle en COMPLET si toutes les données sont disponibles, PARAMÉTRIQUE sinon ?
⚠ Vérifier l'auto-contrôle : chaque élément a son verdict
⚠ Valider les points spécifiques :
   * B-42 : type d'élément (poteau / jambage / voile)
   * B-43 : type de plancher (dalle / dallage / bois)
   * B-46 : frontière avec le spécialiste
   * B-47 : méthode pour escalier balancé ou hélicoïdal
   * B-49 : méthode de charge pour linteau court (triangulaire vs linéique)
   * B-50 : rapport de contrôle croisé
📄 Sauvegarder : [PROJET]/06_Notes_de_calcul/B-xx_[nom].md
Pour chaque brique de calcul : vérifications post-production
☐ Vérifier les données d'entrée : toutes les valeurs viennent de la FDC (aucune valeur hors FDC)
☐ Vérifier les formules : les formules littérales sont exposées avant application numérique
☐ Vérifier les références : chaque formule cite sa référence normative (EC2 §, EC3 §, EC5 §, EC7 §)
☐ Vérifier les dispositions constructives : présentes et conformes
☐ Vérifier les plans : filigrane, cartouche, indice, mode
⚠ Consigner au RDL : ligne du RDL pour le livrable produit
Après chaque livrable complet (B-40 à B-50)
☐ Exécuter B-32 (vue nettoyée) — si pas encore fait
☐ Exécuter B-31 (preuve de superposition)
☐ Exécuter B-33 (vérification croisée)
☐ Exécuter T-01 (sincérité) — si doute sur la fiabilité
________________


PHASE 5 — LIVRABLES (3 à 5 jours)
Étape 5.1 — Plans d'exécution (B-60)
☐ Ouvrir 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{type_livrable}}, {{mode}}
☐ Fournir : note de calcul + vue nettoyée + fichier calé + cartouche modèle
☐ Récupérer la sortie : plans + coupes + détails + DXF + PNG + PDF
⚠ Valider : le cartouche et l'indice — c'est vous qui décidez de l'indice (A, B, C)
⚠ Vérifier : la structure DXF (calques normalisés, un élément = un calque) ; les trois formats (DXF, PNG, PDF) ; le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » ; la mention générique de protection au feu
📄 Sauvegarder : [PROJET]/07_Plans/B-60_[livrable]/
Étape 5.2 — Nomenclature (B-62)
☐ Ouvrir 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{type_livrable}}, {{mode}}
☐ Fournir : plans B-60 + note de calcul
☐ Récupérer la sortie : nomenclature + façonnage + récapitulatif + export tableur + rapport de cohérence
⚠ Valider : la nomenclature avant transmission au fournisseur
⚠ Vérifier : chaque élément dessiné figure dans la nomenclature ; le plan de façonnage est produit ; l'export tableur est produit ; la nomenclature est filigranée si B-60 en PARAMÉTRIQUE
📄 Sauvegarder : [PROJET]/08_Nomenclatures/B-62_[livrable]/
Étape 5.3 — Notice de synthèse (B-64)
☐ Ouvrir 07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{type_livrable}}, {{mode}}
☐ Fournir : note de calcul + plans + nomenclature + RDL + RDR
☐ Récupérer la sortie : notice 2 à 4 pages (7 sections)
⚠ Valider : les visas requis — c'est vous qui savez qui doit viser
⚠ Vérifier : la notice tient en 4 pages max ; la mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » ; la mention générique de protection au feu ; les points à lever sont exhaustifs
📄 Sauvegarder : [PROJET]/09_Notices/B-64_[livrable].md
________________


PHASE 6 — CLÔTURE (1 à 2 jours)
Étape 6.1 — Auto-contrôle de synthèse (B-70)
☐ Ouvrir 08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{périmètre}} (par livrable ou projet), {{mode}}
☐ Fournir : tous les auto-contrôles des briques + B-50 + RDR + RDL + B-31 + B-33
☐ Récupérer la sortie : 6 pièces (inventaire / agrégé / incohérences / interfaces / modes / verdict)
⚠ Valider le verdict global : cohérent / cohérent avec réserves / incohérent
⚠ Vérifier : les incohérences sont identifiées avec brique responsable ; les interfaces sont vérifiées ; les modes sont conformes au RDR (V12)
📄 Sauvegarder : [PROJET]/10_Auto-controles/B-70_AutoControle_Synthese.md
Étape 6.2 — Indiçage (B-71)
☐ Ouvrir 08_PHASE_6_CLOTURE/B-71_Indicage.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{périmètre}}
☐ Fournir : RDL + B-70 + RDR + livrables eux-mêmes
☐ Récupérer la sortie : tableau d'indiçage + supersession + RDL mis à jour + liste en vigueur + rapport des orphelins
⚠ Valider : les motifs de révision — c'est vous qui savez si une révision est justifiée
⚠ Vérifier : chaque document a un indice et une date ; chaque révision a un motif documenté ; la liste des documents en vigueur est produite ; les orphelins sont détectés
📄 Sauvegarder : [PROJET]/11_Indicage/B-71_Indicage.md
Étape 6.3 — Journal de clôture (B-72)
☐ Ouvrir 08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : RDL + RDR + B-70 + B-71 + briques exécutées
☐ Récupérer la sortie : journal en 3 sections (livrables / points ouverts / synthèse)
⚠ Valider : la liste des points ouverts avant transmission à la MOA
⚠ Vérifier : la section 1 liste tous les livrables avec mode ; la section 2 liste les 4 sous-sections ; la section 3 contient le bilan, les points de vigilance, les recommandations ; la mention finale figure
📄 Sauvegarder : [PROJET]/12_Cloture/B-72_Journal_Cloture.md
________________


À TOUT MOMENT
T-01 — Sincérité (doute sur un livrable)
☐ Ouvrir 09_TRANSVERSE/T-01_Sincerite.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{code_livrable}}
☐ Fournir : le livrable à tester
☐ Récupérer la sortie : tableau certain / de principe / à lever + verdict + recommandations
⚠ Valider : le verdict de sincérité
⚠ Si non sincère : lever les éléments à lever avant diffusion
T-02 — Recadrage (défaut visible sur un livrable)
☐ Ouvrir 09_TRANSVERSE/T-02_Recadrage.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{description_du_defaut}}
☐ Fournir : le livrable défaillant + description observable du défaut
☐ Récupérer la sortie : reformulation + diagnostic + méthode + version corrigée + preuve + non-régression
⚠ Valider : le diagnostic (cause dans la méthode) et la preuve de correction
⚠ Relancer la brique source avec la nouvelle méthode
T-03 — Méta-amélioration (après un projet, ou incident significatif)
☐ Ouvrir 09_TRANSVERSE/T-03_Meta_Amelioration.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}
☐ Fournir : carnet CARNAC + B-72 + corrections T-02 + RDR
☐ Récupérer la sortie : inventaire + analyse + propositions + tri GÉNÉRALE/PROJET/À ÉTUDIER + proposition de version
⚠ Valider : les corrections GÉNÉRALES à intégrer au carnet
⚠ Si nouvelle version : incrémenter la version (v1.2) et mettre à jour le journal des révisions
T-04 — Demande de complément (donnée bloquante)
☐ Ouvrir 09_TRANSVERSE/T-04_Demande_Complement.md
☐ Copier le bloc de code, remplacer {{ID-01}}, {{ID-02}}, {{destinataire}}
☐ Fournir : RDR + briques suspendues + MPD
☐ Récupérer la sortie : courrier formel + tableau de synthèse + RDR mis à jour
⚠ Valider : les conséquences de non-réponse — c'est votre engagement
⚠ Envoyer le courrier au destinataire
⚠ Consigner au RDR (statut envoyée)
________________


CHECK-LIST DES POINTS DE CONTRÔLE CRITIQUES
Les 10 validations obligatoires (à ne jamais sauter)
☐ B-01 : validation ligne par ligne des NON NÉCESSAIRE de la MPD
☐ B-02 : validation des valeurs et de leur fiabilité (Contractuelle / Décision / À confirmer)
☐ B-03 : validation des décisions avec auteur, date, effet
☐ B-15 : validation des risques résiduels acceptés
☐ B-20 : visa de la conception avant que les briques de calcul ne s'appuient dessus
☐ B-42, B-43, B-47, B-48, B-49 : validation du type d'élément pour chaque brique paramétrée
☐ B-50 : validation du rapport de contrôle croisé
☐ B-60 : validation de l'indice du livrable
☐ B-70 : validation du verdict global de cohérence
☐ B-72 : validation des points ouverts à la clôture
Les 5 précautions permanentes
☐ Ne copier que le bloc de code dans l'IA (pas les en-têtes, pas les justifications)
☐ Remplacer tous les {{...}} avant envoi (verrou V7 — zéro placeholder résiduel)
☐ Vérifier le mode avant d'appeler une brique (V12)
☐ Vérifier le critère d'acceptation à la fin de chaque brique
☐ Consigner au RDL et au RDR chaque livrable et chaque décision
________________


CHECK-LIST DES LIVRABLES À PRODUIRE PAR PROJET
Documents de référence projet (5)
☐ 00_MPD_du_projet.md (B-01)
☐ 01_FDC_du_projet.md (B-02)
☐ 02_RDR_du_projet.md (B-03) — mis à jour à chaque décision
☐ 03_PTD_du_projet.md (B-04) — mis à jour à chaque blocage
☐ 04_Hypotheses_du_projet.md (B-22) — mis à jour à chaque hypothèse
Registre des Livrables (1)
☐ 05_RDL_du_projet.md — mis à jour à chaque livrable produit
Documents d'analyse (6)
☐ 10_B10_Audit_CCTP.md
☐ 11_B11_Audit_Diagnostic.md
☐ 12_B12_Audit_Geotechnique.md
☐ 13_B13_Contradictions.md
☐ 14_B14_Perimetre_Lot.md
☐ 15_B15_Synthese_Risques.md
Documents de conception (5)
☐ 20_B20_Conception_GO.md + plans de principe
☐ 21_B21_DDC_Preliminaire.md
☐ 22_B22_Note_Hypotheses.md (ou mis à jour dans 04_Hypotheses_du_projet.md)
☐ 23_B23_Exploitation_Diagnostic.md
☐ 24_B24_Existant_Non_Sonde.md
Documents de calage (1 + 3 × N)
☐ 30_B30_Calage.md + fichier recalé (une fois)
☐ 32_B32_Vue_Nettoyee_[livrable].md (à chaque livrable)
☐ 31_B31_Preuve_Superposition_[livrable].md (à chaque livrable)
☐ 33_B33_Verification_Croisee_[livrable].md (à chaque livrable)
Notes de calcul (N)
☐ 06_Notes_de_calcul/B-40_[nom].md
☐ 06_Notes_de_calcul/B-42_[nom].md
☐ 06_Notes_de_calcul/B-43_[nom].md
☐ 06_Notes_de_calcul/B-44_[nom].md
☐ 06_Notes_de_calcul/B-45_[nom].md
☐ 06_Notes_de_calcul/B-46_[nom].md
☐ 06_Notes_de_calcul/B-47_[nom].md
☐ 06_Notes_de_calcul/B-48_[nom].md
☐ 06_Notes_de_calcul/B-49_[nom].md
☐ 06_Notes_de_calcul/B-50_[nom].md
(seules les briques exécutées sont produites — les briques en SANS OBJET produisent une ligne de justification)
Plans d'exécution (N × 3 formats)
☐ 07_Plans/B-60_[livrable]/[livrable].dxf
☐ 07_Plans/B-60_[livrable]/[livrable].pdf
☐ 07_Plans/B-60_[livrable]/[livrable].png
Nomenclatures (N)
☐ 08_Nomenclatures/B-62_[livrable]/nomenclature.xlsx (ou CSV)
☐ 08_Nomenclatures/B-62_[livrable]/faconnage.pdf
Notices (N)
☐ 09_Notices/B-64_[livrable].md
Clôture (3)
☐ 10_Auto-controles/B-70_AutoControle_Synthese.md
☐ 11_Indicage/B-71_Indicage.md
☐ 12_Cloture/B-72_Journal_Cloture.md
________________


CHECK-LIST DES DEMANDES DE COMPLÉMENT (T-04)
Demandes envoyées
☐ R-01 : Mission G3 — MOA — échéance [date]
☐ R-02 : Note coupe-feu — BC — échéance [date]
☐ R-03 : Relevé sections pannes — GO — échéance [date]
☐ R-04 : Essai résistance maçonnerie — GO — échéance [date]
☐ R-05 : Analyse structurelle existant — BET — échéance [date]
☐ R-06 : Nature chaînages — GO — échéance [date]
☐ R-07 : Complexe plancher neuf — Architecte — échéance [date]
☐ R-08 : Complexe toiture — Architecte — échéance [date]
☐ R-09 : Détail escalier — Architecte — échéance [date]
☐ R-10 : Diagnostic amiante/plomb — MOA — avant démarrage
Réponses reçues
☐ R-01 : Reçue le [date] — [référence pièce reçue]
☐ R-02 : Reçue le [date] — [référence pièce reçue]
☐ R-03 : Reçue le [date] — [référence pièce reçue]
☐ R-04 : Reçue le [date] — [référence pièce reçue]
☐ R-05 : Reçue le [date] — [référence pièce reçue]
☐ R-06 : Reçue le [date] — [référence pièce reçue]
☐ R-07 : Reçue le [date] — [référence pièce reçue]
☐ R-08 : Reçue le [date] — [référence pièce reçue]
☐ R-09 : Reçue le [date] — [référence pièce reçue]
☐ R-10 : Reçue le [date] — [référence pièce reçue]
Mise à jour du RDR et de la FDC
☐ Pour chaque réponse reçue : mettre à jour la FDC (valeur + source) et le RDR (réserve fermée)
☐ Pour chaque réponse reçue : relancer la brique suspendue en mode COMPLET (ou PARTIEL-DÉCLARÉ si réponse partielle)
________________


SIGNATURES
Ouverture du projet :

| Rôle | Nom | Date | Signature |
| --- | --- | --- | --- |
| Ingénieur (vous) | — | — | — |
| Chef de projet | — | — | — |

Clôture du projet :

| Rôle | Nom | Date | Signature |
| --- | --- | --- | --- |
| Ingénieur (vous) | — | — | — |
| Chef de projet | — | — | — |
| MOE (visa de réception) | — | — | — |

________________


Ce que cette check-list garantit
1. Aucune étape n'est oubliée : les 37 briques et les 4 prompts transverse sont listés, avec les fichiers associés.
2. Aucun point de contrôle critique n'est sauté : les 10 validations obligatoires sont rappelées en fin de document.
3. Aucune donnée manquante n'est oubliée : les 10 demandes de complément sont listées avec leur échéance.
4. Aucun livrable n'est oublié : la liste exhaustive des livrables à produire est fournie.
5. La traçabilité est assurée : chaque action produit un document sauvegardé, chaque validation est signée.
6. La clôture est documentée : les signatures d'ouverture et de clôture sont enregistrées.
________________


Fin de la check-list de démarrage de projet.
________________

