Fichier 07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md — CARNAC v3.0
________________


B-64 — NOTICE DE SYNTHÈSE DU LIVRABLE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 5 — Synthèse et livrables d'exécution |
| Brique précédente | B-60 (Plans d'exécution), B-62 (Nomenclature) |
| Brique suivante | B-70 (Auto-contrôle de synthèse), B-71 (Indiçage) |
| Fréquence | Une fois par livrable complet (à la fin de la chaîne : après B-60 et B-62) |
| Modes d'appel | COMPLET (toutes les briques amont en COMPLET) · PARTIEL-DÉCLARÉ (briques amont en modes dégradés, déclarées) · PARAMÉTRIQUE (briques amont en PARAMÉTRIQUE : la notice est filigranée) |
| Paramètre d'appel | {{type_livrable}} = même paramètre que B-60 (FOND / VERT / PLANCHER / CHARPENTE / METAL / MACON / ESCALIER / PREDALLE / LINTEAU / ASSEMBLAGE) |
| Entrées lues | Note de calcul de la brique amont, plans B-60, nomenclature B-62, RDL, RDR (décisions et verrous) |
| Sortie unique | Notice de synthèse (2 à 4 pages max) : présentation du livrable, hypothèses retenues, points de principe, points à lever, réserves, visas requis, indiçage |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-60 et B-62, quand les plans et la nomenclature sont produits. B-64 est la brique qui transforme les documents techniques en document de synthèse lisible — elle est destinée à un lecteur (MOE, BC, entreprise) qui doit comprendre le livrable sans ouvrir la note de calcul complète.
Ce que vous fournissez à l'IA : la note de calcul de la brique amont, les plans B-60, la nomenclature B-62, le RDL (registre des livrables), le RDR (décisions et verrous). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * la présentation du livrable (objet, périmètre, pièces jointes) ;
   * les hypothèses retenues (H-xx actives, avec statut) ;
   * les points de principe (ce qui relève d'un choix de conception) ;
   * les points à lever (données manquantes, décisions à prendre, réserves) ;
   * les réserves et limites ;
   * les visas requis ;
   * l'indiçage et la supersession.
Ce que B-64 produit — le périmètre exact :

| Élément | Nature |
| --- | --- |
| Présentation du livrable | Objet, périmètre, pièces jointes |
| Hypothèses retenues | Liste des hypothèses H-xx actives et de leur statut |
| Points de principe | Ce qui relève d'un choix de conception, non d'un calcul |
| Points à lever | Ce qui reste à confirmer ou à décider (verrous, réserves) |
| Réserves et limites | Limites de la note de calcul, points hors périmètre |
| Visas requis | Qui doit viser le livrable avant exécution |
| Indiçage et supersession | Indice du livrable, documents supersédés |

Ce que B-64 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Note de calcul | Brique amont (B-40 à B-50) |
| Plans | B-60 |
| Nomenclature | B-62 |
| Auto-contrôle déclaré | Brique amont (chaque fiche de calcul contient son propre auto-contrôle) |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

La raison d'être de B-64 : sans notice de synthèse, un lecteur (MOE, BC) doit ouvrir toutes les pièces du livrable pour comprendre :
   * ce que couvre le livrable ;
   * quelles hypothèses sont prises ;
   * quels points restent à lever ;
   * quels visas sont requis.
La notice de synthèse est le document d'entrée du livrable — elle permet au lecteur de décider s'il doit approfondir, ou si le livrable est suffisamment clair.

**v3.0.1.** Ordre de lecture : en-tête cinq lignes → §0 hypothèses → périmètre → points de principe → points à lever → visas. Codes `D-xx`/`H-xx` en fin ou omis s'ils n'aident pas le BC. Voir addendum A1 `LIV-07`.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : rédiger la notice de synthèse du livrable {{type_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir de la note de calcul de la brique amont, des plans B-60, de la nomenclature B-62, du RDL et du RDR. La notice tient en 2 à 4 pages maximum et permet à un lecteur de comprendre le livrable sans ouvrir la note de calcul.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


MÉTHODE — DANS CET ORDRE


Étape 1 — Présentation du livrable
- Objet : ce que le livrable couvre (fondations / verticaux / plancher / charpente / etc.) ;
- Périmètre : ce qui est inclus dans le livrable ;
- Pièces jointes : liste des notes de calcul, plans, nomenclatures associés ;
- Brique source et indice du livrable ;
- Date.


Étape 2 — Hypothèses retenues
- Liste des hypothèses H-xx actives (issues de B-22) ;
- Statut de chaque hypothèse (À CONFIRMER / CONFIRMÉE) ;
- Si des hypothèses sont À CONFIRMER, mention explicite : « livrable établi sous hypothèses H-xx à confirmer ».


Étape 3 — Points de principe
- Ce qui relève d'un choix de conception et non d'un calcul ;
- Justification de chaque choix en une phrase ;
- Renvoi aux documents qui détaillent (B-20 pour la conception, note de calcul pour les calculs).


Étape 4 — Points à lever
- Liste des points ouverts (issus du RDR) : données manquantes, décisions à prendre, réserves ;
- Pour chaque point : nature, conséquence sur le livrable, destinataire, échéance.


Étape 5 — Réserves et limites
- Limites de la note de calcul (ce qui n'est pas couvert : existant non sondé, données manquantes, éléments hors périmètre) ;
- Réserves sur les hypothèses ;
- Mention « protection au feu adéquate à prévoir (hors lot GO) ».


Étape 6 — Visas requis
- Qui doit viser le livrable avant exécution : BET structure, bureau de contrôle, MOE, MOA ;
- Nature du visa (visa de conception, visa d'exécution, visa de conformité) ;
- Mention obligatoire : « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA ».


Étape 7 — Indiçage et supersession
- Indice du livrable (A, B, C...) ;
- Documents supersédés (le cas échéant) : indice précédent, date, motif de révision ;
- Mention « ce livrable remplace et annule l'indice précédent ».


INTERDICTIONS
- Ne produis pas une notice de plus de 4 pages : c'est une synthèse, pas une duplication de la note de calcul.
- Ne recopie pas la note de calcul : tu synthétises.
- N'omets aucun point à lever : un point à lever omis est un point qui sera oublié à l'exécution.
- Ne mentionne pas de visas non requis : seuls les visas effectivement nécessaires sont listés.
- Ne produis pas une notice qui ne correspond pas aux plans et nomenclatures produits (cohérence obligatoire).
- Ne produis pas de notice exécutable si le livrable est en mode PARAMÉTRIQUE : la notice est filigranée et suffixée _P.


SORTIE
Pièce unique — Notice de synthèse (2 à 4 pages), structurée en sections 1 à 7.


CRITÈRE D'ACCEPTATION
La notice est acceptée si :
- toutes les entrées (note de calcul, plans, nomenclature, RDL, RDR) sont disponibles et cohérentes ;
- la présentation du livrable identifie l'objet, le périmètre et les pièces jointes ;
- les hypothèses actives sont listées avec leur statut ;
- les points de principe sont identifiés avec justification ;
- les points à lever sont listés avec destinataire et échéance ;
- les limites et réserves sont explicites ;
- les visas requis sont identifiés ;
- l'indiçage et la supersession sont documentés ;
- la mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » figure en tête ;
- la mention « protection au feu adéquate à prévoir (hors lot GO) » figure ;
- la notice tient en 4 pages maximum ;
- si le livrable est PARAMÉTRIQUE : notice filigranée et suffixée _P.
Si un seul de ces douze points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| 4 pages maximum | Une notice de synthèse qui dépasse 4 pages n'est plus une synthèse — c'est une duplication de la note de calcul. Le lecteur (MOE, BC) ne la lit plus — et la notice perd sa fonction |
| Hypothèses avec statut | Une hypothèse « confirmée » et une hypothèse « à confirmer » n'ont pas le même poids. Le statut doit figurer dans la notice — sinon le lecteur croit que tout est confirmé |
| Points à lever avec destinataire et échéance | Un point à lever sans destinataire ne se lève jamais. Sans échéance, il se lève trop tard. La notice est le document qui rend les points à lever actionnables |
| Visas requis explicites | Un livrable sans visa explicite finit par être exécuté sans visa. La notice est le document qui rappelle les visas nécessaires — et qui vous protège si l'exécution commence sans visa |
| Indiçage et supersession | Un livrable indice C qui ne dit pas qu'il remplace l'indice B crée de la confusion (quel document est en vigueur ?). La supersession est indispensable pour la gestion documentaire |
| Mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » | La notice est le dernier document lu avant exécution. C'est là que la mention a le plus d'impact |
| Filigrane si PARAMÉTRIQUE | Une notice qui accompagne un livrable PARAMÉTRIQUE sans filigrane donne l'impression que le livrable est exécutable. Le filigrane protège |
| Cohérence avec plans et nomenclature | Une notice qui cite des plans ou des nomenclatures qui ne correspondent pas (parce que B-60 ou B-62 ont été modifiés entre-temps) est une notice fausse. La cohérence est vérifiée à l'étape 1 |
| « Ne recopie pas la note de calcul » | Une notice qui recopie la note de calcul est une notice inutile — elle ne fait que dupliquer un document qui existe déjà. La notice doit synthétiser, pas dupliquer |
| « N'omets aucun point à lever » | Un point à lever omis est un point qui sera oublié à l'exécution. La notice est le document qui rassemble tous les points à lever en un seul endroit lisible — c'est sa fonction principale |
| « Ne mentionne pas de visas non requis » | Une notice qui liste des visas non requis crée de la confusion (qui doit viser ?). Seuls les visas effectivement nécessaires doivent être listés — c'est votre appréciation du contexte contractuel qui fait foi |
| Filigrane + suffixe _P | Une notice PARAMÉTRIQUE qui accompagne un livrable PARAMÉTRIQUE doit porter le filigrane — sinon elle est diffusée comme une notice normale, et le lecteur croit que le livrable est exécutable |

Les sept sections de la notice — précision utile :

| Section | Objet | Lecteur cible |
| --- | --- | --- |
| 1. Présentation du livrable | Objet, périmètre, pièces jointes, indice | Tous |
| 2. Hypothèses retenues | H-xx actives, statut | MOE, BET, BC |
| 3. Points de principe | Choix de conception, justification | MOE, BET |
| 4. Points à lever | Données manquantes, décisions à prendre | MOE, MOA, BET |
| 5. Réserves et limites | Ce qui n'est pas couvert, ce qui reste à confirmer | Tous |
| 6. Visas requis | Qui doit viser, nature du visa | MOE, BC, BET |
| 7. Indiçage et supersession | Indice, documents supersédés | Tous |

Le piège de la notice trop longue : un modèle qui reçoit une note de calcul, des plans et une nomenclature a tendance à produire une notice qui récapitule tout. C'est exactement ce qu'il faut interdire :
   * une notice trop longue n'est plus lue ;
   * elle duplique les documents existants (note, plans, nomenclature) ;
   * elle ajoute du volume sans apporter d'information nouvelle.
La notice doit synthétiser — c'est-à-dire extraire l'essentiel (hypothèses, points de principe, points à lever, visas) pour permettre au lecteur de décider s'il doit approfondir.
Le piège des points à lever : un modèle a tendance à minimiser les points à lever (par exemple, « quelques points mineurs à lever ») pour présenter un livrable « propre ». C'est exactement ce qu'il faut interdire :
   * un point à lever omis est un point qui sera oublié à l'exécution ;
   * la notice est le document qui rassemble les points à lever en un seul endroit lisible ;
   * c'est ce qui permet à la MOE/BC de décider si le livrable est suffisamment mûr pour être exécuté.
La notice doit lister les points à lever, pas les minimiser.
Le piège de la cohérence : un modèle a tendance à produire la notice sans vérifier que les plans et nomenclatures cités sont bien ceux qui ont été produits. C'est faux :
   * si B-60 a été modifié après B-62 (par exemple, une correction de plan), la nomenclature ne correspond plus ;
   * si B-62 a été modifié après B-60 (par exemple, une correction de quantité), la notice doit en tenir compte ;
   * la notice doit vérifier que les documents cités sont cohérents entre eux — c'est la première vérification de la notice (étape 1).
Une notice incohérente est une notice qui trompe le lecteur — et qui vous engage.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions, réserves et verrous — B-64 les intègre dans les points à lever |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — B-64 les liste avec leur statut |
| B-34 (Synthèse des réservations) | La liste des réservations et des Points d'Arrêt |
| B-40 (Fondations superficielles) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-41 (Fondations profondes) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-42 (Verticaux BA) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-43 (Planchers et dallages) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-44 (Charpente bois) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-45 (Structure métallique) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-46 (Maçonnerie : vérification) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-47 (Escaliers) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-48 (Prédalles et planchers préfabriqués) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-49 (Linteaux et seuils) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-50 (Assemblages et ancrages) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-60 (Plans d'exécution) | Les plans produits — B-64 les cite dans la notice |
| B-62 (Nomenclature et façonnage) | La nomenclature — B-64 la cite dans la notice |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-70 (Auto-contrôle déclaré de synthèse) | La notice — B-70 vérifie que chaque livrable a sa notice |
| B-71 (Indiçage et supersession documentaire) | La notice — B-71 l'indice avec le livrable |
| B-72 (Journal de clôture) | La notice — B-72 la cite dans la liste des livrables produits |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-64 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| ID-05 | Indice du dossier en vigueur | BLOQUANTE (pour l'indiçage et la supersession) |
| DEC-02 | Décisions inscrites au RDR | BLOQUANTE (pour les visas requis et les décisions appliquées) |
| DEC-03 | Verrous ouverts | BLOQUANTE (pour les points à lever) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |

Variables produites
B-64 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (notice de synthèse) qui alimente B-70, B-71, B-72 et les destinataires externes.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, ID-05, DEC-02, DEC-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-64, vous devez valider les visas requis — c'est vous qui savez qui doit viser (BC, BET, MOE) selon le contexte contractuel. Un livrable qui n'est pas visé par le bon tiers peut être refusé à la réception — ou engager votre responsabilité en cas de problème.
Cas particulier — mode PARAMÉTRIQUE : si le livrable est en mode PARAMÉTRIQUE (par exemple, SEC-01 manquante pour un livrable de verticaux), la notice porte :
   * le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * le nom du fichier est suffixé _P ;
   * la mention « livrable provisoire, ne pas exécuter » en tête de notice ;
   * les points à lever sont exhaustifs — y compris la donnée manquante qui bloque l'exécution.
La notice PARAMÉTRIQUE peut être diffusée à la MOE/BC à titre informatif, avec mention explicite « provisoire, ne pas exécuter ».
Cas particulier — livrable avec plusieurs indices : si le livrable a plusieurs indices successifs (par exemple, A → B → C), la notice porte :
   * l'indice en vigueur (C) ;
   * les indices supersédés (A, B) avec leurs dates ;
   * le motif des révisions (correction d'erreur, modification de conception, etc.) ;
   * la mention « ce livrable remplace et annule les indices A et B ».
Sans cette traçabilité, l'entreprise peut exécuter sur un indice périmé — c'est un risque majeur.
Cas particulier — points à lever nombreux : si le livrable a beaucoup de points à lever (par exemple, 10 ou plus), la notice doit :
   * les hiérarchiser (critiques / importants / de suivi) ;
   * identifier les plus critiques (ceux qui bloquent l'exécution) ;
   * recommander une décision (attendre, exécuter partiellement, exécuter sous réserve).
La notice n'est pas seulement un constat — c'est un outil de décision pour la MOE/BC.
Cas particulier — visas déjà obtenus : si le livrable a déjà été visé (par exemple, le BC a visé une version antérieure), la notice porte :
   * les visas déjà obtenus (avec date) ;
   * les visas restant à obtenir ;
   * la mention « les visas de la version antérieure ne valent pas pour l'indice actuel ».
Un visa antérieur ne vaut pas pour un nouvel indice — c'est une règle de gestion documentaire qui évite les confusions.
Cas particulier — livrable d'exécution vs livrable de principe : si le livrable est un plan de principe (produit par B-20), la notice porte :
   * la mention « Étude de conception — ne se substitue pas à l'EXE » ;
   * les points à faire valider par un tiers (BET, BC) avant de passer à l'exécution ;
   * les visas requis (visa de conception, pas visa d'exécution).
Un plan de principe n'est pas un plan d'exécution — la notice doit le préciser.
Cas particulier — livrable avec écart de contrôle croisé : si B-50 (assemblages) a identifié un écart de contrôle croisé (par exemple, un ancrage qui ne rentre pas dans la semelle), la notice porte :
   * l'écart identifié ;
   * la brique responsable (B-40 qui doit s'agrandir, ou B-42 qui doit revoir ses barres) ;
   * l'action en cours (correction de B-40 en cours, décision en attente).
Un livrable avec écart de contrôle croisé non traité n'est pas exécutable — la notice doit le signaler.
Format de sortie attendu : notice unique (2 à 4 pages), structurée en sections 1 à 7, avec les mentions obligatoires. La notice porte le filigrane si le livrable est en mode PARAMÉTRIQUE.
Consignation : la notice B-64 est annexée au livrable et consignée au RDL — elle fait partie du dossier de livraison, avec les plans et la nomenclature.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Notice de synthèse et points d'arrêt.** La notice reprend les hypothèses `H-xx` actives, les prescriptions `ENC`, les Points d'Arrêt `PA-xx`, le mode d'exécution, les réservations `B-34` et les limites de mission. Elle constitue la pièce contractuelle de référence en cas d'écart d'exécution.