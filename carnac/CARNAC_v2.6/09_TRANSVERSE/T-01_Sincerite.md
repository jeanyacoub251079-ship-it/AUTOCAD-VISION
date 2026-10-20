Fichier 09_TRANSVERSE/T-01_Sincerite.md — CARNAC v2.6
________________


T-01 — PROMPT DE SINCÉRITÉ
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	Transverse (utilisable à tout moment, à toutes les phases)
	Brique précédente
	Aucune (T-01 s'applique à n'importe quel livrable, à n'importe quel moment)
	Brique suivante
	T-02 (recadrage) si un défaut est détecté — sinon retour à la phase en cours
	Modes d'appel
	COMPLET uniquement
	Entrées lues
	Le dernier livrable produit (plan, note de calcul, nomenclature, notice, ou tout document émis)
	Sortie unique
	Tableau « certain / de principe / à lever » + verdict de sincérité + recommandations
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique :
   * après chaque production graphique importante (plan d'exécution, note de calcul, nomenclature) ;
   * après chaque note de calcul ;
   * en cas de doute sur la fiabilité d'un livrable ;
   * avant transmission à un tiers (MOE, BC, entreprise).
Ce que vous fournissez à l'IA : le livrable à vérifier (plan, note, nomenclature, notice) et éventuellement la note de calcul ou la FDC de référence. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{code_livrable}}.
Ce que vous validez à la sortie :
   * le tableau détaillé (chaque élément classé : certain / de principe / à lever) ;
   * le verdict de sincérité (sincère / non sincère) ;
   * les recommandations pour chaque élément à lever (cause probable, brique CARNAC à exécuter, échéance).
Ce que T-01 apporte de spécifique — le test de sincérité :
Aspect
	Auto-contrôle de brique (B-40 à B-50)
	T-01 (sincérité)
	Objet
	Vérifier la conformité technique
	Vérifier la sincérité — ce qui est affirmé est-il sourcé ?
	Périmètre
	Une brique
	N'importe quel livrable, à n'importe quel moment
	Sortie
	Verdict technique (conforme / à corriger)
	Tableau certain / de principe / à lever + verdict de sincérité
	Angle
	« Le livrable est-il correct ? »
	« Le livrable est-il honnête sur ce qu'il affirme ? »
	Protection
	Protège contre les erreurs techniques
	Protège contre les affirmations non fondées
	T-01 est la brique qui a produit l'aveu structuré dans la conversation d'origine — elle force le modèle à distinguer explicitement ce qui est sourcé et vérifié de ce qui est choisi ou estimé. C'est ce qui a permis la reprise du projet Flora.
Les trois catégories — précision utile :
Catégorie
	Définition
	Conséquence
	CERTAIN
	L'élément est explicitement rattaché à une source citée (fichier + folio + indice) ou à un calcul tracé dans la note de calcul
	Peut être affirmé dans le livrable
	DE PRINCIPE
	L'élément est un choix de conception ou une valeur approchée, explicitement déclaré comme tel dans le livrable
	Doit être mentionné comme tel (mention « de principe » ou « sous hypothèse H-xx »)
	À LEVER
	L'élément est présent dans le livrable sans source et sans déclaration de principe — il a été inventé, estimé ou recopié sans traçabilité
	Ne doit pas être affirmé dans le livrable — il doit être levé (par une source ou par une déclaration)
	________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : effectuer le test de sincérité du livrable {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}. Tu réponds en toute franchise : ce livrable est-il conforme aux sources, ou contient-il des éléments inventés, estimés, ou non rattachés à une source ?


MÉTHODE


Étape 1 — Inventaire exhaustif des éléments du livrable
Liste TOUS les éléments du livrable : positions, cotes, sections, ferraillages, hypothèses, choix, mention de matériaux.


Étape 2 — Classement en trois catégories
Pour chaque élément, classe-le dans l'une des trois catégories :
- CERTAIN : l'élément est explicitement rattaché à une source citée (fichier + folio/page + indice) ou à un calcul tracé dans la note de calcul.
- DE PRINCIPE : l'élément est un choix de conception ou une valeur approchée, explicitement déclaré comme tel dans le livrable.
- À LEVER : l'élément est présent dans le livrable sans source et sans déclaration de principe — c'est-à-dire qu'il a été inventé, estimé ou recopié sans traçabilité.


Étape 3 — Tableau de synthèse
Tableau : élément | catégorie (certain / de principe / à lever) | justification (source citée, ou déclaration, ou absence de source).


Étape 4 — Verdict de sincérité
- Si tous les éléments sont certains ou de principe : verdict « sincère ».
- Si un ou plusieurs éléments sont à lever : verdict « non sincère », avec la liste des éléments à lever et la gravité (bloquante / à lever avant transmission / à surveiller).


Étape 5 — Recommandation
Pour chaque élément à lever :
- cause probable (brique source non exécutée, hypothèse non déclarée, données manquantes) ;
- brique CARNAC à exécuter pour le lever ;
- échéance.


INTERDICTIONS
- Ne justifie aucun élément à lever par « c'est une pratique courante » ou « c'est comme d'usage » : ces formulations sont précisément les symptômes d'un élément à lever.
- Ne requalifie pas un élément à lever en élément de principe après coup : le classement est fait avant le verdict, pas après.
- Ne minimise pas le nombre d'éléments à lever pour « faire propre » : c'est le contraire de l'objectif.
- Ne produis pas de verdict sans le tableau détaillé.


SORTIE
Pièce unique — Tableau détaillé + verdict + recommandations.


CRITÈRE D'ACCEPTATION
Le test est accepté si :
- chaque élément du livrable figure dans le tableau ;
- chaque élément est classé en certain / de principe / à lever ;
- chaque élément a une justification (source ou absence de source) ;
- le verdict est explicite et cohérent avec le tableau ;
- chaque élément à lever a une cause probable et une brique CARNAC pour le lever.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{code_livrable}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	« Ne justifie pas un élément à lever par "pratique courante" »
	C'est exactement la formulation qui produit les livrables non sincères : une valeur estimée « comme d'usage » qui n'est pas déclarée comme telle. C'est la faille du projet Flora (40 mm d'enrobage « au titre des exigences de tenue au feu » sans que ces exigences existent)
	« Classement fait avant verdict »
	Empêche le modèle de « réinterpréter » un élément à lever après coup pour le requalifier en élément de principe. Le classement doit être objectif — le verdict vient après, pas avant
	« Ne minimise pas le nombre »
	La tentation naturelle d'un modèle est de trouver peu d'éléments à lever. Le prompt force la rigueur — un livrable sincère peut avoir 0 élément à lever, mais il ne peut pas avoir 0 élément à lever par construction
	Tableau obligatoire
	Un verdict sans tableau est un avis. Le tableau est la preuve de la sincérité du test — il permet à un tiers de vérifier que chaque élément a été classé
	Trois catégories seulement
	Sans cette limite, un modèle produit des catégories intermédiaires (« plutôt certain », « probablement de principe ») qui ne sont pas des catégories mais des hésitations. Trois catégories forcent la clarté
	CERTAIN = source citée
	Verrou V2 — un élément qui n'est pas rattaché à une source ne peut pas être affirmé comme certain. La citation (fichier + folio + indice) est la seule preuve de certitude
	DE PRINCIPE = déclaré comme tel
	Un élément de principe qui n'est pas déclaré dans le livrable devient un élément à lever — c'est la règle qui garantit la traçabilité. Un modèle qui « oublie » de déclarer un choix de conception produit un livrable non sincère
	Recommandation avec brique CARNAC
	Un élément à lever sans brique CARNAC pour le lever est un élément qui reste à lever indéfiniment. La recommandation rend le test actionnable — elle identifie l'action à faire pour lever l'élément
	« Ne produis pas de verdict sans le tableau »
	Un verdict sans tableau est une affirmation, pas un test. Le tableau est la preuve que le test a été fait — sans lui, le verdict n'est pas opposable
	Les trois niveaux de gravité — précision utile :
Gravité
	Définition
	Conséquence
	Bloquante
	L'élément à lever est critique — il affecte la sécurité, la conformité, ou engage la responsabilité
	Le livrable ne doit pas être diffusé tant que l'élément n'est pas levé
	À lever avant transmission
	L'élément à lever n'est pas critique, mais il doit être levé avant diffusion (par exemple, une hypothèse non déclarée)
	Le livrable est diffusé après avoir levé l'élément
	À surveiller
	L'élément à lever n'est ni critique ni bloquant — il doit être documenté et suivi
	Le livrable est diffusé, avec l'élément inscrit au RDR (réserve R-xx)
	Le piège du « c'est de principe » : un modèle qui reçoit un livrable a tendance à classer trop d'éléments en « de principe » pour éviter de les classer en « à lever ». C'est exactement ce qu'il faut interdire :
   * un élément est « de principe » seulement s'il est explicitement déclaré comme tel dans le livrable (mention « de principe » ou « sous hypothèse H-xx ») ;
   * un élément qui n'est pas déclaré est « à lever » — même s'il paraît anodin ;
   * la déclaration est la seule preuve — pas l'apparence.
Un modèle qui classe « de principe » sans vérifier la déclaration produit un faux verdict de sincérité.
Le piège de la « pratique courante » : un modèle a tendance à invoquer la « pratique courante » pour justifier un élément à lever. C'est exactement ce qu'il faut interdire :
   * « c'est comme d'usage » n'est pas une source ;
   * « c'est la pratique courante » n'est pas une déclaration ;
   * ces formulations sont précisément les symptômes d'un élément à lever — elles apparaissent quand l'élément n'a pas de source.
Un élément à lever ne peut pas être justifié — il doit être levé.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à T-01
	Toutes les briques (B-00 à B-72)
	Le livrable à vérifier — T-01 s'applique à n'importe quel livrable
	B-02 (FDC)
	La FDC de référence — T-01 vérifie que les valeurs du livrable correspondent à la FDC
	B-22 (Note d'hypothèses)
	Les hypothèses H-xx — T-01 vérifie que les hypothèses sont bien déclarées dans le livrable
	Briques aval
Brique
	Ce qu'elle consomme de T-01
	T-02 (Recadrage)
	Le verdict « non sincère » — T-02 diagnostique la cause et corrige la méthode
	T-03 (Méta-amélioration)
	Les éléments à lever récurrents — T-03 propose des corrections au carnet
	B-03 (RDR)
	Les éléments à lever classés « à surveiller » — ils deviennent des réserves R-xx
	Variables consommées
Code
	Libellé
	Statut dans T-01
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Toutes les variables citées dans le livrable
	Selon le livrable
	BLOQUANTE (chaque variable doit être classée)
	Variables produites
T-01 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (tableau de sincérité) qui alimente T-02, T-03 et B-03.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-01, vous devez valider le verdict de sincérité — c'est votre appréciation qui fait foi, pas la seule liste. Un élément classé « à surveiller » par le modèle peut être en réalité « à lever avant transmission » — c'est votre jugement d'ingénieur qui décide.
Cas particulier — livrable avec 0 élément à lever : si tous les éléments sont certains ou de principe, le verdict est « sincère ». C'est le cas idéal — mais il est rare. Un livrable avec 0 élément à lever peut être parfaitement sincère, ou peut être le signe que le test a été mal fait. Vérifiez que le tableau est exhaustif (tous les éléments sont listés) et que les déclarations de principe sont bien présentes dans le livrable.
Cas particulier — livrable avec beaucoup d'éléments à lever : si le livrable a beaucoup d'éléments à lever (par exemple, plus de 5), c'est le signe que le livrable a été produit sur des bases fragiles. Vous pouvez :
   * soit lever les éléments un par un (par exemple, en ajoutant les sources manquantes) ;
   * soit requalifier le livrable en mode PARTIEL-DÉCLARÉ (les éléments à lever deviennent des éléments de principe déclarés) ;
   * soit suspendre le livrable et reprendre la production à la brique amont.
Chaque choix a des conséquences — c'est votre décision.
Cas particulier — élément à lever de gravité bloquante : si un élément à lever est de gravité bloquante (par exemple, une section de poutre non sourcée), le livrable ne doit pas être diffusé. L'élément doit être levé avant diffusion — soit par une source, soit par une déclaration explicite (hypothèse H-xx).
Cas particulier — test sur un livrable en mode PARAMÉTRIQUE : si le livrable est en mode PARAMÉTRIQUE (par exemple, un plan de fondations avec q_adm manquante), les éléments dépendant de la donnée manquante sont « de principe » (déclarés comme tels, avec la mention « sous hypothèse H-xx — à confirmer »). Ils ne sont pas « à lever » — ils sont déclarés. Mais les éléments qui ne devraient pas dépendre de la donnée manquante et qui sont pourtant non sourcés sont « à lever ».
Cas particulier — test sur un livrable en mode PARTIEL-DÉCLARÉ : si le livrable est en mode PARTIEL-DÉCLARÉ (valeur déclarée au RDR), les éléments utilisant la valeur déclarée sont « de principe » (déclarés comme tels, avec la référence à la décision RDR). Ils ne sont pas « à lever ».
Format de sortie attendu : tableau détaillé (chaque élément, sa catégorie, sa justification), verdict de sincérité (sincère / non sincère), recommandations (cause probable, brique CARNAC, échéance).
Consignation : le test T-01 est consigné au RDL (avec le code du livrable testé, la date, le verdict). En cas de verdict « non sincère », les éléments à lever sont inscrits au RDR comme réserves (R-xx) avec leur échéance.
________________

