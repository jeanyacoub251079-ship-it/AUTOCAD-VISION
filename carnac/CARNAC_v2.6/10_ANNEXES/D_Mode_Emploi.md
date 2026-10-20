Fichier 10_ANNEXES/D_Mode_Emploi.md — CARNAC v2.6
________________


D — MODE D'EMPLOI DU CARNET
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Nature
	Document de référence — annexe D du carnet
	Objet
	Expliquer comment utiliser le carnet CARNAC au quotidien, projet par projet
	Public
	Ingénieur qui pilote la production d'études d'exécution
	Statut
	Document stable — ne change qu'avec une révision du carnet
	Distinction avec le document maître (00_MASTER.md) :
   * le document maître décrit ce qu'est le carnet (principes, verrous, modes, arborescence) ;
   * ce mode d'emploi décrit comment s'en servir (quelle fiche ouvrir, quel prompt copier, dans quel ordre, avec quelles précautions).
________________


2. CE QUE VOUS AVEZ EN MAIN
Le carnet CARNAC se compose de trois types de documents :
Type
	Nature
	Usage
	Documents de référence (ce document, document maître, dictionnaire, annexes)
	Stables, consultés en permanence
	Comprendre le carnet, vérifier une convention, connaître un verrou
	Fiches de brique (B-xx_Intitulé.md)
	Une fiche par tâche
	Ouvrir la fiche quand vous devez exécuter la tâche correspondante
	Prompts transverse (T-xx_Intitulé.md)
	Utilisables à tout moment
	Ouvrir quand vous avez besoin de contrôler, recadrer, demander un complément
	Chaque fiche de brique contient quatre sections :
Section
	Contenu
	À qui s'adresse-t-elle ?
	1. En-tête
	Version, phase, modes d'appel, entrées, sortie, critère d'acceptation
	À vous : pour savoir quand et comment appeler la brique
	2. Prompt
	Le bloc de code entre triples backquotes
	À l'IA : c'est le seul texte à copier-coller
	3. Justification des clauses clés
	Pourquoi chaque clause existe
	À vous : pour comprendre et pouvoir modifier
	4. Références
	Briques amont, briques aval, variables consommées
	À vous : pour savoir ce qui alimente et ce qui dépend de la brique
	Ce que vous copiez dans l'IA : uniquement le bloc de code de la section 2. Le reste est de la documentation pour vous.
________________


3. DÉMARRAGE D'UN NOUVEAU PROJET — LES 6 ÉTAPES
Vue d'ensemble
text
Phase 0 (Cadrage) ──► Phase 1 (Analyse) ──► Phase 2 (Conception)
      │                                           │
      │                                           ▼
      └──► Phase 3 (Calage) ──► Phase 4 (Calculs) ──► Phase 5 (Livrables)
                                                                 │
                                                                 ▼
                                                        Phase 6 (Clôture)
Durée indicative par phase (variable selon le projet) :
Phase
	Durée indicative
	Livrables principaux
	0 — Cadrage
	1 à 2 jours
	Inventaire, MPD, FDC, RDR, PTD
	1 — Analyse
	3 à 5 jours
	Audits, contradictions, périmètre, risques
	2 — Conception
	2 à 10 jours selon complexité
	Conception GO, DDC préliminaire, hypothèses
	3 — Calage
	1 à 2 jours
	Calage, preuve, vues nettoyées
	4 — Calculs
	10 à 30 jours selon volume
	Notes de calcul, plans
	5 — Livrables
	3 à 5 jours
	DXF/PDF/PNG, nomenclatures, notices
	6 — Clôture
	1 à 2 jours
	Auto-contrôle, indiçage, journal
	________________


Étape 1 — Cadrage (Phase 0)
Objectif : constituer les trois documents d'entrée (MPD, FDC, RDR) et identifier immédiatement ce qui bloque.
Fiches à exécuter, dans l'ordre :
Ordre
	Fiche
	Ce que vous faites
	Ce que vous validez
	1
	B-00 Inventaire
	Copier le prompt, fournir les pièces du projet
	La liste des pièces, la reformulation de mission
	2
	B-01 MPD
	Copier le prompt, fournir l'inventaire B-00
	Ligne par ligne les NON NÉCESSAIRE (périmètre)
	3
	B-02 FDC
	Copier le prompt, fournir la MPD validée
	Chaque valeur et sa source
	4
	B-03 RDR
	Copier le prompt, fournir la FDC
	Chaque décision (auteur, date) et chaque réserve
	5
	B-04 PTD
	Copier le prompt, fournir la MPD, la FDC et le RDR
	Le PTD : ce qui est suspendu, ce qui est exécutable
	Point de contrôle critique : à l'issue de B-01, vous validez (ou refusez) chaque NON NÉCESSAIRE. C'est votre décision, pas celle du modèle. Un NON NÉCESSAIRE mal validé bloque une brique qui aurait dû s'exécuter.
Si une donnée bloquante manque : B-04 produit un PTD. Vous savez immédiatement ce qui est faisable et ce qui ne l'est pas. T-04 peut être utilisée pour demander le complément.
________________


Étape 2 — Analyse (Phase 1)
Objectif : auditer les pièces, identifier les contradictions, clarifier le périmètre, hiérarchiser les risques.
Fiches à exécuter :
Fiche
	Ce que vous faites
	Ce que vous validez
	B-10 Audit CCTP
	Copier le prompt, fournir le CCTP
	La liste des points à lever avec destinataires
	B-11 Audit Diagnostic
	Copier le prompt, fournir le diagnostic
	Chaque [ANALYSE GO] est bien la vôtre
	B-12 Audit Géotechnique
	Copier le prompt, fournir le rapport G2
	La recommandation de mission complémentaire
	B-13 Contradictions
	Copier le prompt, fournir B-10, B-11, B-12
	Le classement gravité × nature
	B-14 Périmètre de lot
	Copier le prompt, fournir B-10, B-11
	Les prestations À TRANCHER
	B-15 Synthèse des risques
	Copier le prompt, indiquer le périmètre
	Les risques résiduels acceptés
	Points de contrôle critiques :
   * B-10 : avant transmission à la MOE, valider les destinataires et urgences.
   * B-11 : chaque cellule [ANALYSE GO] doit être votre analyse, pas une reformulation du diagnostic.
   * B-12 : la décision de commander (ou non) une mission G3/G4 est une décision MOA, pas la vôtre.
   * B-14 : une prestation que vous acceptez implicitement devient la vôtre, même si le CCTP ne la prescrit pas.
   * B-15 : valider les risques résiduels acceptés — c'est l'engagement qui vous engage.
________________


Étape 3 — Conception (Phase 2)
Objectif : concevoir la structure GO si le BET de conception est absent, ou compléter ce qu'il n'a pas fourni ; prédimensionner et produire les plans de principe ; poser les hypothèses.
Fiches à exécuter (dans l'ordre) :
Fiche
	Ce que vous faites
	Ce que vous validez
	B-20 Conception GO
	Copier le prompt, choisir le mode (INTERNE-GO / PARTIEL-DÉCLARÉ / SANS OBJET), fournir la géométrie archi et les contraintes existantes
	La trame, les sections de principe, la liste des points à faire valider par un tiers
	B-21 DDC préliminaire
	Copier le prompt, fournir les charges et les usages
	Les catégories d'usage EC1 et les cloisons forfaitaires
	B-22 Note d'hypothèses
	Copier le prompt, fournir la FDC
	Chaque hypothèse à son introduction (pas après)
	B-23 Exploitation diagnostic
	Copier le prompt, fournir B-11 et B-20
	Les orientations de renforcement ne sont pas des dimensionnements
	B-24 Existant non sondé
	Copier le prompt, fournir EXI-xx
	Le tableau de sensibilité est bien marqué « NON CONTRACTUEL »
	Points de contrôle critiques :
   * B-20 : le visa de la conception (par vous, un BET, ou le BC) avant que les briques de calcul ne s'appuient dessus.
   * B-21 : les catégories d'usage sont vos choix, pas ceux du modèle.
   * B-22 : une hypothèse validée trop tard est une hypothèse qui a déjà contaminé les calculs. Validez à l'introduction.
   * B-24 : décider de commander les essais, ou d'inscrire au RDR une valeur déclarée (PARTIEL-DÉCLARÉ).
Cas particulier — pas de BET de conception : B-20 s'appelle en mode INTERNE-GO. La sortie de B-20 (trame, sections de principe, plans de principe filigranés) devient l'entrée de toutes les briques de calcul.
________________


Étape 4 — Calage et calculs (Phases 3 et 4)
Objectif : caler la géométrie sur le fichier source, puis produire les notes de calcul et les plans d'exécution.
4.1 Calage (une fois par projet)
Fiche
	Ce que vous faites
	Ce que vous validez
	B-30 Calage
	Copier le prompt, fournir le DXF/DWG source
	Le résidu de calage (≤ 1 cm) et la preuve de superposition
	B-30 est exécutée une seule fois pour le projet. Le fichier « calé » est une donnée de projet, réutilisée par toutes les briques graphiques.
4.2 Pour chaque livrable graphique (à chaque brique de calcul)
Fiche
	Ce que vous faites
	Ce que vous validez
	B-32 Vue nettoyée
	Copier le prompt, fournir le fichier calé et le type de livrable
	La liste des calques À TRANCHER
	B-31 Preuve de superposition
	Copier le prompt, fournir le livrable produit
	Le verdict global sur chaque livrable
	B-33 Vérification croisée
	Copier le prompt, fournir le livrable et le RDL
	Les écarts section 2 (plan ↔ plan) avant de relancer la brique source
	4.3 Briques de calcul (phase 4)
Choisir la brique selon le type d'élément :
Élément à calculer
	Fiche
	Fondations superficielles
	B-40
	Fondations profondes (vérification)
	B-41
	Poteaux, jambages, voiles
	B-42 (paramètre {{élément}})
	Planchers, dallages
	B-43 (paramètre {{type}})
	Charpente bois
	B-44 (paramètre {{élément}})
	Structure métallique
	B-45 (paramètre {{élément}})
	Maçonnerie (vérification et conception)
	B-46 (paramètre {{bloc}} = A / B / A+B)
	Escaliers
	B-47 (paramètre {{type}})
	Prédalles
	B-48 (paramètre {{phase}})
	Linteaux et seuils
	B-49 (paramètre {{type}})
	Assemblages et ancrages
	B-50 (paramètre {{famille}})
	Pour chaque brique de calcul :
   1. Ouvrir la fiche.
   2. Lire l'en-tête : mode d'appel, entrées lues, sortie attendue.
   3. Copier le bloc de code.
   4. Remplacer les {{...}} par les valeurs du projet (mode, élément, type).
   5. Fournir les données d'entrée (FDC, DDC, hypothèses, notes amont).
   6. Vérifier l'auto-contrôle produit par la brique.
Points de contrôle critiques :
   * B-40 à B-50 : vérifier que la brique est bien en mode COMPLET si toutes les données sont disponibles, PARAMÉTRIQUE sinon.
   * B-42 : valider le type d'élément (poteau / jambage / voile) pour chaque vertical.
   * B-43 : valider le type de plancher (dalle / dallage / plancher bois).
   * B-46 : valider la frontière avec le spécialiste (injection, tirants).
   * B-47 : valider la méthode de calcul pour escalier balancé ou hélicoïdal.
   * B-49 : valider la méthode de charge pour linteau court (triangulaire vs linéique).
   * B-50 : valider le contrôle croisé — c'est vous qui décidez quelle brique corrige.
Si une donnée bloquante manque : la brique s'appelle en mode PARAMÉTRIQUE. Le livrable est filigrané et suffixé _P. Consulter le PTD (B-04) pour savoir ce qui reste faisable.
________________


Étape 5 — Livrables (Phase 5)
Objectif : produire les plans d'exécution, les nomenclatures et la notice de synthèse.
Fiches à exécuter, dans l'ordre :
Ordre
	Fiche
	Ce que vous faites
	Ce que vous validez
	1
	B-60 Plans d'exécution
	Copier le prompt, fournir la note de calcul et la vue nettoyée
	Le cartouche, l'indice, la structure DXF
	2
	B-62 Nomenclature
	Copier le prompt, fournir les plans B-60
	La nomenclature avant transmission au fournisseur
	3
	B-64 Notice de synthèse
	Copier le prompt, fournir la note, les plans, la nomenclature, le RDL et le RDR
	Les visas requis
	Points de contrôle critiques :
   * B-60 : c'est vous qui décidez du numéro d'indice (A, B, C) en fonction du cycle de révision.
   * B-60 : validation de la structure DXF avant diffusion — un DXF mal structuré est inutilisable.
   * B-62 : une erreur de quantité commandée coûte cher.
   * B-64 : c'est vous qui savez qui doit viser (BC, BET, MOE) selon le contexte contractuel.
________________


Étape 6 — Clôture (Phase 6)
Objectif : faire l'auto-contrôle de synthèse, indiçer les documents, produire le journal de clôture.
Fiches à exécuter, dans l'ordre :
Ordre
	Fiche
	Ce que vous faites
	Ce que vous validez
	1
	B-70 Auto-contrôle de synthèse
	Copier le prompt, fournir tous les auto-contrôles des briques
	Le verdict global
	2
	B-71 Indiçage
	Copier le prompt, fournir le RDL et les documents
	Les motifs de révision
	3
	B-72 Journal de clôture
	Copier le prompt, fournir le RDL, le RDR, B-70 et B-71
	Les points ouverts à traiter avant remise
	Points de contrôle critiques :
   * B-70 : votre appréciation de la criticité des incohérences fait foi, pas la seule liste.
   * B-71 : vous seul savez si une révision est justifiée.
   * B-72 : certains points ouverts peuvent être « acceptés » par votre décision, d'autres pas. C'est vous qui décidez lesquels doivent être traités avant remise.
________________


4. UTILISATION DES PROMPTS TRANSVERSE
Ces prompts s'utilisent à tout moment, pas dans une phase particulière.
T-01 — Sincérité
Quand : après chaque production graphique importante, après chaque note de calcul, en cas de doute sur la fiabilité d'un livrable, avant transmission à un tiers.
Ce qu'il fait : classe tous les éléments du livrable en trois catégories (certain / de principe / à lever) et donne un verdict de sincérité.
Ce que vous validez : le verdict et la liste des éléments à lever.
T-02 — Recadrage
Quand : quand un livrable présente un défaut visible, quand une deuxième version ne corrige pas la première, quand un modèle « corrige » sans expliquer.
Ce qu'il fait : diagnostique la cause du défaut dans la méthode, propose une nouvelle méthode reproductible, applique et prouve la correction.
Ce que vous validez : le diagnostic et la preuve de correction.
T-03 — Méta-amélioration
Quand : après chaque projet terminé, après un incident significatif (T-02 déclenché), après l'ajout ou la suppression d'une brique.
Ce qu'il fait : analyse les incidents du projet, propose des corrections au carnet, classe en GÉNÉRALE / PROJET / À ÉTUDIER.
Ce que vous validez : les corrections GÉNÉRALES à intégrer au carnet (c'est vous qui décidez d'une nouvelle version).
T-04 — Demande de complément
Quand : à la fin de la phase 0 (données bloquantes identifiées), à tout moment si une donnée bloquante est découverte, avant remise d'un livrable important.
Ce qu'il fait : rédige une demande formelle à la MOE/BET/MOA, structurée et datée, avec conséquence de non-réponse et échéance.
Ce que vous validez : la forme de la demande et la priorisation (URGENTE / IMPORTANTE / DE SUIVI).
________________


5. LES CINQ PRÉCAUTIONS À PRENDRE
Précaution 1 — Ne copier que le bloc de code
Le prompt est dans la section 2 de la fiche, entre triples backquotes. Les en-têtes et les justifications sont pour vous, pas pour l'IA.
Précaution 2 — Remplacer tous les {{...}} avant envoi
Aucun {{...}} ne doit subsister dans le prompt envoyé. C'est le verrou V7 (zéro placeholder résiduel). Si vous en oubliez un, l'IA peut le combler à votre place — et ce ne sera pas votre choix.
Précaution 3 — Vérifier le mode avant d'appeler une brique
Le mode (COMPLET, PARTIEL-DÉCLARÉ, PARAMÉTRIQUE, INTERNE-GO, SANS OBJET) doit être cohérent avec la disponibilité des données. Un COMPLET sur une donnée bloquante manquante est une faute (V12).
Précaution 4 — Vérifier le critère d'acceptation à la fin
Chaque brique a un critère d'acceptation dans son en-tête. Si le critère n'est pas satisfait, la brique n'est pas terminée — et l'IA doit le signaler.
Précaution 5 — Consigner au RDL et au RDR
Chaque livrable produit est consigné au RDL (registre des livrables). Chaque décision, réserve ou verrou est consigné au RDR. Sans cette consignation, la traçabilité est rompue — et la mise à jour incrémentale (B-32) devient impossible.
________________


6. QUE FAIRE EN CAS DE PROBLÈME
Problème
	Que faire
	Une donnée bloquante manque
	B-04 (PTD) vous dit ce qui est faisable. T-04 rédige la demande de complément.
	Un livrable est défaillant
	T-02 diagnostique la cause et corrige la méthode.
	Un livrable est douteux (sincérité)
	T-01 classe les éléments en certain / de principe / à lever.
	Une incohérence entre briques
	B-70 détecte et identifie la brique responsable.
	Un défaut se répète
	T-03 propose une correction générale au carnet.
	Une donnée change en cours de projet
	B-32 met à jour uniquement les livrables impactés (via le RDL).
	Une décision est à prendre
	RDR section 1 : décision avec auteur, date, justification.
	Une demande de complément est sans réponse
	T-04 relance, puis B-72 la cite dans les points ouverts à la clôture.
	________________


7. CE QUE VOUS NE FAITES PAS
   * Vous ne copiez pas les en-têtes et justifications dans l'IA.
   * Vous ne validez pas un NON NÉCESSAIRE sans vérifier qu'il est justifié par le périmètre (pas par la disponibilité).
   * Vous ne validez pas un COMPLET sur une donnée bloquante manquante (V12).
   * Vous ne laissez pas un {{...}} dans un prompt envoyé (V7).
   * Vous ne diffusez pas un livrable PARAMÉTRIQUE sans filigrane et sans mention.
   * Vous n'exécutez pas un livrable sans visa.
   * Vous ne modifiez pas le carnet sans passer par T-03 et une révision de version.
________________


8. CE QUE VOUS FAITES SYSTÉMATIQUEMENT
   * Vous validez ligne par ligne les NON NÉCESSAIRE de la MPD (B-01).
   * Vous validez les valeurs et leur fiabilité à la FDC (B-02).
   * Vous validez les décisions avec auteur, date et effet (B-03).
   * Vous validez les risques résiduels acceptés (B-15).
   * Vous visez la conception avant que les briques de calcul ne s'appuient dessus (B-20).
   * Vous validez le type d'élément pour chaque brique paramétrée (B-42, B-43, B-47, B-48, B-49).
   * Vous validez le rapport de contrôle croisé (B-50).
   * Vous validez l'indice du livrable (B-60, B-71).
   * Vous validez le verdict global de l'auto-contrôle de synthèse (B-70).
   * Vous validez les points ouverts à la clôture (B-72).
________________


9. RENVOIS
Document
	Contenu
	Fichier
	Document maître
	Index, principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	94 variables
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Calques, échelles, formats, cartouche
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des révisions
	Versions du carnet
	10_ANNEXES/C_Journal_Revisions.md
	Journal des modifications
	Détail des modifications unitaires
	11_HISTORIQUE/Journal_des_modifications.md
	________________


10. RÉSUMÉ EN UNE PAGE
Un projet = 6 phases = 37 briques = 4 prompts transverse.
Ce que vous faites à chaque projet :
   1. Cadrage : B-00 à B-04 — 1 à 2 jours — inventaire, MPD, FDC, RDR, PTD.
   2. Analyse : B-10 à B-15 — 3 à 5 jours — audits, contradictions, périmètre, risques.
   3. Conception : B-20 à B-24 — 2 à 10 jours — conception GO, DDC, hypothèses.
   4. Calage et calculs : B-30 à B-50 — 10 à 30 jours — calage, preuves, vérifications, notes de calcul.
   5. Livrables : B-60, B-62, B-64 — 3 à 5 jours — plans, nomenclatures, notices.
   6. Clôture : B-70 à B-72 — 1 à 2 jours — auto-contrôle, indiçage, journal.
À tout moment : T-01 (sincérité), T-02 (recadrage), T-03 (méta-amélioration), T-04 (demande de complément).
Les trois règles qui gouvernent tout :
   1. Le mode doit être honnête — pas de COMPLET sur une donnée manquante.
   2. Les sources doivent être citées — tout élément est rattaché à une pièce.
   3. La mise à jour est incrémentale — seuls les livrables impactés sont régénérés.
________________


Additif v2.3 — Durées indicatives en voie rapide (document maître §6) : pour une affaire simple (un seul type de livrable, BET de conception présent, aucune contradiction bloquante), les phases 0 et 1 fusionnées en une seule passe représentent indicativement 1 à 3 jours, sans suppression d'aucune sortie ; les durées des phases 2 à 6 du tableau ci-dessus restent inchangées. Tout blocage fait repasser en voie normale.
---

### Additif v2.4 — Ce que les versions v2.x changent à l'usage quotidien
- **Verrou V13 et annexe O** : les briques géométriques et de calcul (phase 3, phase 4, B-60/B-62) travaillent par scripts exécutés et relus ; sans environnement d'exécution, elles ne peuvent pas être déclarées COMPLET.
- **Protocole B-32 §R** : avant tout nettoyage, les parois sont chaînées (R.3bis) puis classées PORTEUR CERTAIN / NON PORTEUR / À LEVER (critères C1 à C6) ; les porteurs BET vectoriels sont projetés (R.4bis). Votre arbitrage porte sur la liste À LEVER, à la porte B-32.
- **Seuils du projet** : GEO-09 = échelle tracé ; GEO-10/GEO-11 = reconnaissance des porteurs ; GEO-12 = seuils géométriques (calage, superposition, position). Ces quatre variables sont des données FDC : vérifiez-les en phase 0.
- **Voie rapide** : phases 0 et 1 fusionnables pour les affaires simples (voir l'additif v2.3 ci-dessus et le document maître §6).

### Additif — Application proportionnée et garde-fous d'usage
Le carnet est un menu, pas un programme obligatoire : le nombre de briques réellement activées est fixé par le PTD (B-04) selon l'affaire, jamais par défaut à 37.
- **Petite affaire** (un livrable, BET de conception présent, pas de contradiction bloquante) : voie rapide — phases 0 et 1 fusionnées, seules les briques du livrable visé sont activées.
- **Affaire moyenne** : phases 0 à 6 dans l'ordre, en n'activant que les briques de calcul et de livrables correspondant au périmètre GO réel.
- **Affaire lourde ou réhabilitation** : parcours complet, protocole B-32 §R et contrôles croisés inclus.
Restent **incompressibles à toute échelle** : le protocole de session (§0, portes et GO), le triptyque MPD/FDC/RDR, et pour tout livrable diffusé les verrous V7 (document propre, sans trace de génération), V11 (aucune invention, blocages déclarés) et V13 (preuve d'exécution des livrables géométriques et numériques). Le risque symétrique — n'appliquer que la partie « promesse » du carnet — se traite ici : avant de diffuser un livrable ou une version du carnet, l'assistant exécute et montre un contrôle anti-fragments (recherche des traces de génération en français et en anglais, lecture des jonctions entre documents) ; aucune mention « complet », « assaini » ou « vérifié » n'est écrite sans la sortie de ce contrôle. Le prompt T-01 (sincérité) peut être invoqué par l'utilisateur à tout moment pour l'exiger.
