Fichier 11_HISTORIQUE/Journal_des_modifications.md — CARNAC v2.5
1. OBJET
Ce journal recense toutes les modifications apportées au carnet CARNAC depuis la version de travail v1.0. Il permet à un utilisateur qui dispose d'une version antérieure de savoir ce qui a changé, pourquoi, et quels fichiers sont impactés.
Règle de lecture : chaque fiche du carnet porte en en-tête la mention « Dernière révision : vX.Y — voir Journal_des_modifications.md, entrée C-XX ». Un utilisateur qui ouvre une fiche sait immédiatement si elle a été révisée et pourquoi.
________________


2. TABLEAU RÉCAPITULATIF DES MODIFICATIONS
N°
	Type
	Date
	Objet
	Fiches impactées
	Version
	C-01
	Contenu
	17/10/2026
	Ajout de 4 variables (MAT-09 à MAT-12) pour la conception de maçonnerie
	Dictionnaire, B-46
	v1.1
	C-02
	Structure
	17/10/2026
	Fusion de B-61 (coupes et détails) dans B-60
	B-60, B-61 (vacante)
	v1.1
	C-03
	Structure
	17/10/2026
	Intégration de B-63 (export DXF) dans B-60
	B-60, B-63 (vacante)
	v1.1
	C-04
	Erratum
	17/10/2026
	Correction de numérotation : B-48 → B-50 pour les assemblages
	B-50
	v1.1
	C-05
	Structure
	17/10/2026
	Renumérotation des phases 4, 5 et 6 (voir §4)
	B-47 à B-50, B-60 à B-72
	v1.0 → v1.1
	E-01
	Erratum
	17/10/2026
	Compte de variables : 74 → 92
	00_MASTER.md
	v1.1
	CC-01
	Cohérence
	17/10/2026
	Mentions de B-61 corrigées en B-60 dans le dictionnaire (LIV-01 à LIV-03)
	Dictionnaire
	v1.1
	Ensemble du carnet
	v2.0
	V2.0
	Refonte
	10/2026
	Verrou V13, annexe O (outillage), dictionnaire intégré, seuils adaptatifs GEO-09, compléments normatifs, corpus assaini
	B-32, dictionnaire, document maître
	v2.1
	V2.1
	Complément de brique
	10/2026
	Protocole de reconnaissance des porteurs (B-32 §R) ; variables GEO-10, GEO-11
	B-32, annexe O, document maître
	v2.2
	V2.2
	Complément de brique
	10/2026
	Chaînage des parois (R.3bis), projection automatique des porteurs BET (R.4bis) — après test FLORA
	Ensemble du carnet
	v2.3
	V2.3
	Correctif de versionnage
	10/2026
	En-têtes normalisés, annexe C et récapitulatif à jour, compte de variables unifié (93), renvois dictionnaire corrigés — aucun changement de fond
	Ensemble du carnet
	v2.4
	V2.4
	Correctif de cohérence
	10/2026
	Création de GEO-12 (seuils), compte de briques corrigé (37), compléments intégrés avant les marqueurs de fin, synthèse v2.x en annexe D
	Ensemble du carnet
	v2.5
	V2.5
	Correctif final (relectures externes)
	10/2026
	Annexe C et récapitulatif prolongés, exemples expurgés et requalifiés historiques, bandeau B-41 ajusté ; relecture externe complète avant publication
	Ensemble du carnet
	v2.6
	V2.6
	Consolidation (relecture externe, point par point)
	10/2026
	Exemples expurgés des traces de génération, note de compte 92/93/94 au dictionnaire, §0.5 formulations du GO, phrase §0.1, formulations B-41, règle de diffusion et balises du compilé, garde-fous d'usage en annexe D
	________________


3. DÉTAIL DES MODIFICATIONS
C-01 — Ajout de quatre variables pour la conception de maçonnerie
Date : 17/10/2026
Nature : ajout de contenu (dictionnaire de variables)
Motif : décision entreprise — B-46 traite désormais la conception de maçonnerie, en plus de la vérification de l'existant.
Variables ajoutées :
Code
	Libellé
	Bloque
	Mentionnée
	MAT-09
	Classe de bloc de maçonnerie neuve (NF EN 771-3)
	B-46 (Bloc B)
	B-50
	MAT-10
	Classe de mortier (M2,5 à M10)
	B-46 (Bloc B)
	—
	MAT-11
	Type de maçonnerie (chaînée / armée / non armée)
	B-46 (Bloc B)
	B-50
	MAT-12
	Présence et nature des chaînages existants
	B-46 (Bloc A)
	B-20
	Fiches impactées :
* 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv (4 lignes ajoutées)
* 06_PHASE_4_CALCULS/B-46_Maconnerie.md (paramètre {{bloc}} = A / B / A+B)
Conséquence pour l'utilisateur : toute FDC de projet comportant de la maçonnerie neuve ou du renforcement de maçonnerie existante doit renseigner MAT-09 à MAT-12.
________________


C-02 — Fusion de B-61 dans B-60
Date : 17/10/2026
Nature : modification de structure (suppression d'une brique)
Motif : décision entreprise — production graphique unique (plans + coupes + détails) pour garantir la cohérence entre plan, coupe et détail.
Avant : B-60 (plans) et B-61 (coupes et détails) étaient deux briques distinctes.
Après : B-60 produit plans + coupes + détails + export DXF. B-61 devient vacante.
Fiches impactées :
* 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md (fusion)
* 00_MASTER.md §4.2 (index des fiches : B-61 marquée vacante)
* 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv (LIV-01 à LIV-03 : voir CC-01)
Conséquence pour l'utilisateur : ne pas appeler B-61. Toute production graphique passe par B-60, qui produit les trois éléments ensemble.
________________


C-03 — Intégration de B-63 dans B-60
Date : 17/10/2026
Nature : modification de structure (suppression d'une brique)
Motif : décision entreprise — l'export DXF se fait au moment de la production graphique, pour éviter la désynchronisation entre plan et fichier DXF.
Avant : B-63 (export DXF) était une brique autonome.
Après : l'export DXF est intégré à B-60 (étape 6 du prompt). B-63 devient vacante.
Fiches impactées :
* 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md (intégration)
* 00_MASTER.md §4.2 (index des fiches : B-63 marquée vacante)
Conséquence pour l'utilisateur : ne pas appeler B-63. Toute production graphique passe par B-60, qui produit DXF + PNG + PDF ensemble.
________________


C-04 — Correction de numérotation : B-48 → B-50 pour les assemblages
Date : 17/10/2026
Nature : erratum (correction d'une erreur de référence)
Motif : la brique des assemblages et ancrages est B-50. La mention « B-48 » apparue dans la question du tronçon 6 était une erreur : B-48 est déjà affectée aux prédalles.
Avant : la brique des assemblages et ancrages est référencée « B-48 » dans certains documents intermédiaires.
Après : B-50 est la brique des assemblages et ancrages. B-48 reste Prédalles et planchers préfabriqués.
Fiches impactées :
* 06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md
* 06_PHASE_4_CALCULS/B-48_Predalles.md (confirmation de son périmètre)
* 00_MASTER.md §4.2 (index des fiches)
Conséquence pour l'utilisateur : dans tout document antérieur à v1.1, une mention de « B-48 » pour les assemblages est à lire comme « B-50 ».
________________


C-05 — Renumérotation des phases 4, 5 et 6
Date : 17/10/2026
Nature : modification de structure (renumérotation)
Motif : la décision de créer des briques dédiées pour les escaliers, prédalles, linteaux et assemblages (tronçon 1) a nécessité de réaffecter les numéros de la phase 4. Pour préserver la continuité, les phases 5 et 6 ont été décalées.
Avant (proposition initiale au tronçon 1) :
Phase
	Plage de numéros
	Phase 4 — Calculs
	B-40 à B-49
	Phase 5 — Livrables
	B-50 à B-54
	Phase 6 — Contrôle et clôture
	B-60 à B-62
	Après (v1.1) :
Phase
	Plage de numéros
	Phase 4 — Calculs
	B-40 à B-50
	Phase 5 — Livrables
	B-60 à B-64
	Phase 6 — Contrôle et clôture
	B-70 à B-72
	Briques ajoutées en phase 4 :
Numéro
	Intitulé
	B-47
	Escaliers
	B-48
	Prédalles et planchers préfabriqués
	B-49
	Linteaux et seuils
	B-50
	Assemblages et ancrages
	Fiches impactées :
* 00_MASTER.md §4.2 (index des fiches)
* Toutes les fiches de la phase 4 (B-40 à B-50)
* Toutes les fiches de la phase 5 (B-60, B-62, B-64)
* Toutes les fiches de la phase 6 (B-70 à B-72)
Conséquence pour l'utilisateur : dans tout document antérieur à v1.1, une mention « B-50 » pour les plans d'exécution est à lire comme « B-60 » ; une mention « B-60 » pour l'auto-contrôle est à lire comme « B-70 ».
Note : cette renumérotation a eu lieu avant la production des fiches définitives. Les fiches produites en v1.1 portent directement la numérotation finale. Aucune fiche n'a été publiée avec l'ancienne numérotation.
________________


E-01 — Erratum sur le compte de variables
Date : 17/10/2026
Nature : erratum
Motif : la synthèse finale du tronçon 10 annonçait « 74 variables (70 v1.0 + 4 v1.1) ». Le compte réel est 88 en v1.0 et 92 en v1.1.
Avant : « 74 variables (70 v1.0 + 4 v1.1) »
Après : « 92 variables (88 v1.0 + 4 v1.1) »
Détail par famille (v1.1) :
Famille
	Nombre
	ID
	7
	AC
	9
	DOC
	9
	GEO
	9
	NIV
	6
	SOL
	8
	MAT
	12
	CHG
	8
	EXI
	5
	SEC
	5
	SIT
	5
	LIV
	5
	DEC
	4
	Total
	92
	Fiches impactées :
* 00_MASTER.md §4 et §7
* 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv
________________


CC-01 — Mentions de B-61 corrigées en B-60 dans le dictionnaire
Date : 17/10/2026
Nature : correction de cohérence
Motif : les variables LIV-01, LIV-02 et LIV-03 du dictionnaire initial (tronçon 2) référençaient B-61 (coupes et détails) comme brique de livraison. Après fusion de B-61 dans B-60 (C-02), ces mentions sont devenues obsolètes.
Avant :
Code
	Bloque
	LIV-01
	B-61
	LIV-02
	B-60, B-61
	LIV-03
	B-61
	Après :
Code
	Bloque
	LIV-01
	B-60 (export)
	LIV-02
	B-60
	LIV-03
	B-60
	Fiches impactées :
* 01_DICTIONNAIRE/CARNAC_v1.1_variables.csv
________________


4. DÉCISIONS STRUCTURANTES (à ne pas confondre avec les modifications)
Ces décisions ont façonné le carnet, mais ne sont pas des modifications à proprement parler : elles ont été prises avant la production des fiches définitives et sont donc intégrées à la v1.1 dès sa première émission. Elles sont listées ici pour mémoire, afin qu'un lecteur qui reprendrait les notes de rédaction puisse s'y retrouver.
N°
	Décision
	Fiches concernées
	D-01
	5 modes d'exécution (COMPLET, PARTIEL-DÉCLARÉ, PARAMÉTRIQUE, INTERNE-GO, SANS OBJET)
	Toutes
	D-02
	Blocage local et PTD (V11)
	Toutes, B-04
	D-03
	Requalification à sens unique (V12)
	Toutes
	D-04
	Une note d'hypothèses unique par projet
	B-22
	D-05
	Une vue nettoyée par livrable (et non une seule par projet)
	B-32
	D-06
	Option C : brique dédiée aux ancrages (B-50), contrôle croisé
	B-50, B-40, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49
	D-07
	Brique unique pour plans + coupes + détails + export DXF
	B-60
	D-08
	Fiches dédiées pour les prompts transverse
	T-01 à T-04
	D-09
	Une fiche par brique (pas de fiche-mère commune)
	B-40 à B-50
	D-10
	B-46 traite vérification ET conception de maçonnerie
	B-46
	________________


5. FICHIERS IMPACTÉS PAR LES MODIFICATIONS
Tableau récapitulatif : pour chaque fichier du carnet, quelles modifications l'ont touché.
Fichier
	Modifications
	00_MASTER.md
	C-02, C-03, C-05, E-01
	01_DICTIONNAIRE/CARNAC_v1.1_variables.csv
	C-01, CC-01, E-01
	06_PHASE_4_CALCULS/B-46_Maconnerie.md
	C-01
	06_PHASE_4_CALCULS/B-48_Predalles.md
	C-04
	06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md
	C-04
	07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md
	C-02, C-03
	Toutes les fiches phase 4
	C-05
	Toutes les fiches phase 5
	C-05
	Toutes les fiches phase 6
	C-05
	________________


6. RÈGLES DE TENUE DU JOURNAL
1. Chaque modification reçoit un numéro unique (C-xx pour les modifications de contenu ou de structure, E-xx pour les errata, CC-xx pour les corrections de cohérence).
2. Une modification ne peut pas être supprimée du journal — même si elle est annulée, elle reste documentée avec la mention « annulée par C-xx ».
3. Chaque modification identifie les fichiers impactés — sans quoi elle n'est pas traçable.
4. Une modification sans motif documenté est une anomalie : elle ne doit pas exister.
5. Le journal est mis à jour à chaque révision du carnet — pas seulement aux versions majeures.
________________


7. PROCHAINES VERSIONS PRÉVUES
Version
	Condition de production
	Contenu prévu
	v1.2
	Après le premier projet complet exécuté avec v1.1
	Corrections issues de T-03 (méta-amélioration), ajustements de fiches, ajout de briques si nécessaire
	v2.0
	Après trois projets complets avec la même version majeure
	Révision de fond si un changement d'architecture est nécessaire
	________________
---

## Entrée v2.0 — REFONTE (rédacteur : refonte assistée, validée par l'utilisateur)
Nature : refonte de carnet (incrémentation majeure v1.1 → v2.0).
Modifications :
1. Ajout du verrou V13 (preuve d'exécution) et de l'annexe O (couche outillage) ; fiches B-30 à B-33, B-40 à B-50, B-60, B-62 complétées du régime outillé ; suppression du test de relecture « simulé » de B-60.
2. Dictionnaire de variables intégré au carnet (01_DICTIONNAIRE, 92 variables reconstruites depuis les fiches + famille OUT nouvelle).
3. Seuils géométriques adaptatifs (GEO-09) : document maître §5 ; B-30, B-31, B-33 alignées.
4. Compléments normatifs des briques de calcul : ELS fissuration/déformations, combinaisons EC0 complètes (ψ, quasi-permanente), position EC8 explicite, poussées de terres/hydrostatique et actions d'exécution EC1-1-6 (B-40/B-41), tolérances NF EN 13670, enrobage c_nom = c_min + Δc_dev ; annexe A §11.
5. Correction de la contradiction d'unités v1.1 (cotes de plan : millimètres partout ; B-60 alignée sur l'annexe A).
6. Assainissement du corpus : suppression des fragments conversationnels de génération, déduplication de l'annexe D (version normalisée conservée), index du document maître mis à jour (statuts « produites »).
7. Voie rapide petites affaires (document maître §6) ; hiérarchie interne du carnet précisée (V1).
Aucun verrou supprimé (non-régression §8.3 du document maître).


---

## Entrée v2.1 — PROTOCOLE DE RECONNAISSANCE DES PORTEURS (B-32 §R)
Nature : complément de brique (incrémentation mineure v2.0 → v2.1), validé par l'utilisateur.
Motif : la v2.0 nettoyait par calques en présupposant les porteurs identifiés ; la reconnaissance élément par élément (pratiquée sur l'affaire FLORA, où le DXF architecte séparait déjà les calques) n'était écrite nulle part.
Modifications :
1. B-32 : ajout du §R (inventaire des entités, reconstruction des parois et mesure des épaisseurs, critères C1 source BET souveraine / C2 épaisseur / C3 superposition des niveaux / C4 schéma statique / C5 position / C6 indices graphiques, règle de classification en trois classes, porte humaine sur les À LEVER conservés par défaut, consignation OUT-03). Le prompt de B-32 (méthode, étapes 2 à 7) renvoie explicitement au §R.
2. Dictionnaire : ajout de GEO-10 (seuils d'épaisseur de présomption) et GEO-11 (superposition des niveaux), données de projet portées par la FDC — 93 variables.
3. Annexe O §4.4 et document maître §10 : renvois au §R.
Aucun verrou supprimé ni modifié (non-régression).


---

## Entrée v2.2 — CHAÎNAGE DES PAROIS ET PROJECTION BET (B-32 §R.3bis et §R.4bis)
Nature : complément de brique (incrémentation mineure v2.1 → v2.2), sur GO explicite de l'utilisateur, à la suite du test du protocole sur l'affaire FLORA.
Motif (enseignements du test) : (1) la classification par tronçons laissait 42 % des murs en À LEVER, les deux faces d'une même paroi étant jugées séparément ; (2) le critère C1 (porteurs désignés par le BET) n'était pas projeté géométriquement.
Modifications :
1. B-32 §R.3bis nouveau : chaînage obligatoire (segmentation aux intersections et ouvertures, regroupement des colinéaires, appariement des faces, objet paroi identifié portant longueur cumulée et épaisseur médiane) ; la classification C1 à C6 porte sur la paroi chaînée.
2. B-32 §R.4bis nouveau : projection automatique des porteurs BET vectoriels (extraction, recalage sur le repère B-30 avec résidu consigné, appariement par recouvrement, écarts de projection signalés à B-13/B-33 et jamais appariés de force ; repli manuel déclaré si BET raster).
3. Prompt de B-32 (étape 2) et document maître §10 mis à jour en conséquence.
Aucun verrou supprimé ni modifié (non-régression).


---

## Entrée v2.3 — PASSE CORRECTIVE DE VERSIONNAGE
Nature : correctif documentaire (incrémentation mineure v2.2 → v2.3), sur GO explicite de l'utilisateur, à la suite d'une revue externe vérifiée point par point.
Motif : incohérences de versionnage résiduelles héritées des bascules successives (en-têtes de fiches non normalisés, annexe C désignant v1.1 comme version en vigueur, récapitulatif du journal incomplet, comptes de variables 91/92/93 coexistant, renvois fonctionnels vers CARNAC_v1.1_variables.csv).
Corrections (aucun changement de fond, aucun prompt modifié dans sa méthode) :
1. En-têtes des fiches et annexes normalisés : champ Version = 2.3, ligne « Dernière révision » uniformisée.
2. Annexe C : version en vigueur = v2.3 ; v1.1 reléguée en référence historique ; feuille de route (v1.2 non produite, v2.0 produite) mise à jour ; additif v2.0–v2.3.
3. Journal des modifications : lignes v2.0, v2.1, v2.2, v2.3 ajoutées au tableau récapitulatif.
4. Compte de variables unifié à 93 dans les renvois fonctionnels (document maître, B-01, B-02, annexe D) ; les mentions historiques (journal, annexe C §détail v1.1, exemples) sont conservées comme telles.
5. Renvois fonctionnels au dictionnaire corrigés en CARNAC_v2.5_variables.csv (hors journal et exemples, mentions historiques préservées).
6. B-32 : GEO-10 et GEO-11 ajoutées au tableau des variables consommées ; briques en régime outillé (B-30, B-31, B-32, B-33, B-60, B-62) : variables OUT-01 à OUT-03 ajoutées à leurs tableaux de consommation.
7. Annexe D : durées indicatives de la voie rapide ajoutées.


---

## Entrée v2.4 — COHÉRENCE INTERNE (GEO-12, compte de briques, compléments intégrés)
Nature : correctif de cohérence (incrémentation mineure v2.3 → v2.4), sur GO explicite de l'utilisateur, à la suite d'une revue externe de la v2.2 vérifiée point par point.
Motif : conflit sémantique sur GEO-09 (le dictionnaire le définit « Échelle tracé » depuis la v1.1, le document maître l'utilisait depuis la v2.0 pour les seuils géométriques) ; compte de briques faux (« 30 » pour 37 fiches) ; compléments de version placés après les marqueurs « Fin de » des fiches et du journal ; synthèse v2.x absente de l'annexe D.
Corrections (aucun changement de fond, aucune méthode de prompt modifiée) :
1. Création de GEO-12 (seuils géométriques du projet) ; GEO-09 rendue à son sens unique « Échelle tracé » ; document maître §5/§10, B-30, annexe O réalignés ; dictionnaire porté à 94 variables et compte unifié dans les renvois fonctionnels.
2. Document maître §7 : « 37 fiches de brique opérationnelles » (comptage réel des fichiers).
3. Compléments de version (blocs v2.0 à v2.4) intégrés dans le corps des fiches, avant leur marqueur « Fin de » ; entrées v2.0 à v2.4 du présent journal replacées avant son marqueur de fin.
4. Annexe D : synthèse d'usage des versions v2.x (V13/annexe O, §R, GEO-09 à GEO-12, voie rapide).


---

## Entrée v2.5 — PASSE CORRECTIVE FINALE (relectures externes)
Nature : correctif documentaire (incrémentation mineure v2.4 → v2.5), sur GO explicite de l'utilisateur.
Motif : résidus relevés par deux relectures externes indépendantes de la v2.2 puis de la v2.4, vérifiés point par point : annexe C restée à « version en vigueur : v2.3 », récapitulatif du journal sans lignes v2.4/v2.5, section 12_EXEMPLES contenant encore des fragments conversationnels de génération tout en se disant « nettoyée », bandeau « régime outillé » générique mal ajusté à B-41 (brique sans mode COMPLET par construction).
Corrections (aucun changement de fond) :
1. Annexe C : version en vigueur = v2.5 ; règle permanente ajoutée (la dernière entrée du présent journal fait foi).
2. Journal : lignes V2.4 et V2.5 ajoutées au tableau récapitulatif (§2).
3. 12_EXEMPLES : fragments conversationnels supprimés ; bandeau « exemples historiques v1.1 » ajouté en tête ; le mot « nettoyés » retiré de l'intitulé. Les valeurs d'époque (92 variables, renvoi CSV v1.1, projet fictif LES LILAS) sont conservées comme traces et explicitement sans valeur de référence fonctionnelle.
4. B-41 : phrase du complément « régime outillé » ajustée à la nature de la brique (contrôles chiffrés scriptés ; pas de référence au mode COMPLET).
5. Relecture externe complète du carnet avant publication (rapport de relecture joint au dossier de la version) : en-têtes, versions en vigueur, comptes (94 variables, 37 fiches), renvois de fichiers, marqueurs de fin uniques, variables GEO, absence de fragments conversationnels.


---

## Entrée v2.6 — CONSOLIDATION DES CORRECTIONS (relecture externe, point par point)
Nature : correctif documentaire (incrémentation mineure v2.5 → v2.6), sur GO explicites successifs de l'utilisateur, un point traité par étape dans un dossier de travail avant consolidation.
Motif : relecture externe de la v2.5 ayant relevé des traces de génération subsistant dans 12_EXEMPLES malgré l'entrée v2.5, une cohabitation de comptes peu lisible, une fragilité interprétative du « GO », deux formulations à reprendre (document maître §0.1, fiche B-41), la forme du document compilé, et trois risques d'usage (non-application, faux sentiment de rigueur, inflation documentaire).
Corrections (aucun changement de fond) :
1. 12_EXEMPLES expurgée de toutes ses traces de génération (français et anglais) ; seul subsistent les quatre exemples et leurs commentaires ; marqueur de fin propre à la section restauré.
2. Signalétique des comptes : note de compte au dictionnaire (« 94 en vigueur ; 92 et 93 = traces historiques ») ; étiquettes d'époque des exemples restaurées en v1.1.
3. Protocole de session : §0.5 nouveau « Comment donner un GO » (déclenchement lexical, formulations types, messages ne valant pas GO) ; phrase du §0.1 reformulée (« avant l'activation de la brique B-00 »).
4. B-41 : formulations positives des modes d'appel (PARAMÉTRIQUE par défaut, PARTIEL-DÉCLARÉ, SANS OBJET), sans référence défensive au mode COMPLET.
5. Diffusion : la référence est l'arborescence, le compilé mono-fichier n'est qu'une aide de lecture (document maître §1.2) ; chaque fichier y est balisé « Début du fichier : [chemin] ».
6. Annexe D : application proportionnée (trois parcours selon la taille d'affaire, briques activées par le PTD) et garde-fous d'usage, dont le contrôle anti-fragments obligatoire avant toute diffusion.
