Fichier 02_PHASE_0_CADRAGE/B-02_FDC.md — CARNAC v2.6
________________


B-02 — FICHE DE DONNÉES DE CONCEPTION
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	0 — Cadrage
	Brique précédente
	B-01 (MPD validée)
	Brique suivante
	B-03 (RDR)
	Modes d'appel
	COMPLET (valeurs disponibles) · PARTIEL-DÉCLARÉ (décision RDR déclarée pour une valeur) · PARAMÉTRIQUE (variable restant en symbole)
	Entrées lues
	MPD validée (B-01), toutes les pièces du projet, décisions RDR déjà inscrites (le cas échéant)
	Sortie unique
	FDC complète (tableau valeurs + sources + fiabilité) + tableau des verrous en fin de fiche
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après validation de la MPD par vous. B-02 transforme la MPD en document exploitable : elle rassemble les valeurs effectivement lues par les briques, avec leurs sources et leur niveau de fiabilité.
Ce que vous fournissez à l'IA : la MPD validée, les pièces du projet, les décisions RDR déjà prises (s'il y en a). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} par le code projet.
Ce que vous validez à la sortie :
* chaque valeur et sa source ;
* le niveau de fiabilité (Contractuelle / Décision / À confirmer) ;
* la liste des verrous (variables BLOQUANTE qui n'ont pas de valeur).
Principe clé de la FDC : la FDC porte les valeurs et leur source, pas seulement des renvois. Un lecteur de note de calcul doit pouvoir lire la FDC sans ouvrir le CCTP. C'est ce qui garantit qu'une note de calcul reste opposable — chaque valeur qui y figure est traçable jusqu'à sa source.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la Fiche de Données de Conception (FDC) de l'opération {{ID-01}}, à partir de la MPD validée et des pièces du projet. La FDC porte les VALEURS et leur SOURCE — elle doit pouvoir être lue sans ouvrir le CCTP.


RÈGLES
1. Seules les variables lues par au moins une brique activée figurent en FDC. Une variable non lue n'apparaît pas.
2. Chaque ligne porte : code, libellé, valeur, unité, source (fichier + folio/page + indice) OU mention « VERROU » si la valeur est absente.
3. Niveau de fiabilité obligatoire pour chaque valeur :
   - Contractuelle — valeur issue d'une pièce du marché ;
   - Décision — valeur issue du RDR (numéro, auteur, date cités) ;
   - À confirmer — valeur de travail, non validée.
4. Aucune valeur de repli n'est proposée. Aucune « pratique courante » n'est invoquée comme source.
5. Les variables VERROU sont listées en fin de FDC avec la brique suspendue et la voie d'obtention.
6. Les conflits entre pièces (deux valeurs incompatibles pour le même code) ne sont PAS arbitrés : ils sont listés comme VERROU et inscrits au RDR (B-03).


INTERDICTIONS
- Ne remplis aucun champ sans source citée.
- Ne retiens aucune valeur sur la base d'une pratique courante, d'un ordre de grandeur ou d'une « valeur usuelle ».
- Ne tranche aucune contradiction entre pièces.
- Ne propose aucune décision qui appartient au RDR.


SORTIE
Tableau 1 : Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) consommatrice(s)
Tableau 2 (fin de fiche) : Code VERROU | Brique suspendue | Voie d'obtention proposée (relevé / essai / mission G / décision MOA) | Responsable pressenti


CRITÈRE D'ACCEPTATION
La FDC est acceptée si :
- chaque ligne a une source citée ou est marquée VERROU ;
- aucun champ n'est renseigné sans niveau de fiabilité ;
- les VERROU sont en fin de fiche avec voie d'obtention ;
- aucune contradiction n'a été tranchée silencieusement ;
- aucune variable non lue par une brique n'est présente en FDC.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} par le code projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	« lisible sans ouvrir le CCTP »
	La FDC est la référence des notes de calcul. Si elle ne porte pas les valeurs, chaque vérificateur (BC, BET, MOE) doit ouvrir le CCTP pour vérifier une note de calcul — ce qui est ingérable en pratique. La FDC porteuse des valeurs et de leurs sources est la seule forme opposable
	« Aucune valeur de repli… aucune pratique courante »
	C'est la faille la plus coûteuse de la conversation d'origine : 40 mm d'enrobage « au titre des exigences de tenue au feu du projet » ont été retenus sans que ces exigences existent. Cette clause interdit ce type de valeur non sourcée
	« deux valeurs incompatibles → VERROU + RDR »
	Traitement explicite de la contradiction XC2/35 mm vs XA3/50 mm du projet Flora : l'arbitrage est une décision RDR, pas une décision du modèle. Sans cette clause, un modèle peut « choisir » la valeur la plus favorable
	« aucune variable non lue n'apparaît »
	Évite la FDC « pour faire complet » qui vous obligeait à remplir des champs inutiles. Une FDC courte et exacte est plus utile qu'une FDC longue et remplie de champs vides
	« tu signales l'écart et tu t'arrêtes »
	Pas de FDC partielle silencieuse. Une FDC partielle présentée comme complète est une FDC qui sera lue comme complète — et les notes de calcul qui s'appuient dessus seront fausses
	Niveau de fiabilité obligatoire
	Un vérificateur doit pouvoir distinguer d'un coup d'œil une valeur contractuelle (que personne ne peut contester) d'une valeur de travail (qui peut être révisée). Sans cette distinction, toutes les valeurs sont traitées au même niveau — ce qui est faux
	Les trois niveaux de fiabilité — précision utile :
Niveau
	Signification
	Conséquence en cas de désaccord
	Contractuelle
	Issue d'une pièce du marché (CCTP, plan, marché)
	Ne se conteste pas unilatéralement ; doit passer par un avenant ou une décision MOA
	Décision
	Issue d'un arbitrage inscrit au RDR (auteur, date, justification)
	Peut être révisée par une nouvelle décision RDR, avec traçabilité
	À confirmer
	Hypothèse de travail, non validée
	Doit être confirmée avant exécution ; le livrable qui l'utilise porte une réserve
	________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-02
	B-01 (MPD validée)
	Le statut de chaque variable : FOURNIE, PARTIELLE, BLOQUANTE, À PRODUIRE PAR GO
	B-00 (Inventaire)
	La référence exacte des pièces (fichier + folio + indice)
	RDR (si déjà ouvert)
	Les décisions D-xx déjà prises (valeur déclarée, auteur, date) — peuvent alimenter la FDC avec fiabilité « Décision »
	Briques aval
Brique
	Ce qu'elle consomme de B-02
	B-03 (RDR)
	Les VERROU listés en fin de FDC — B-03 les inscrit au Registre des Verrous (section 3)
	B-04 (PTD)
	Les VERROU et les briques suspendues — B-04 produit le plan de travail dégradé à partir de ces informations
	Toutes les briques B-40 à B-50
	Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET
	Variables consommées
Code
	Libellé
	Statut dans B-02
	ID-01
	Code projet
	BLOQUANTE (pour l'en-tête de sortie)
	Toutes les variables statuées FOURNIE, PARTIELLE, BLOQUANTE ou À PRODUIRE PAR GO par B-01
	Selon la variable
	Selon le statut
	Variables produites
B-02 ne produit pas une variable au sens du dictionnaire : sa sortie est la FDC, qui contient les valeurs de toutes les variables retenues. La FDC est un document, pas une variable.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	Les 94 variables, avec leur nature (bloque/mentionnée)
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	MPD (sortie B-01)
	Statut de chaque variable pour le projet en cours
	Document de projet
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus important de cette brique : à la sortie de B-02, vous devez valider chaque valeur et valider son niveau de fiabilité. C'est le moment où vous décidez ce qui est contractuel, ce qui est votre décision, et ce qui est votre hypothèse de travail. Un modèle qui remplit la FDC avec des valeurs non sourcées produit une FDC qui ne vaut rien.
Cas particulier — valeur déclarée en mode PARTIEL-DÉCLARÉ : si vous avez déjà pris une décision RDR (par exemple, retenir XA3 en lieu et place de XC2), la FDC porte la valeur (XA3), la source (« Décision D-01 du 17/10/2026 ») et la fiabilité (« Décision »). La valeur XC2 du CCTP n'est pas effacée : elle est listée en VERROU (« contradiction XC2 vs XA3 »), et la décision RDR est citée dans la ligne.
Cas particulier — variable À PRODUIRE PAR GO : si AC-03 (BET structure de conception) est À PRODUIRE PAR GO, la FDC ne porte pas de valeur pour cette variable — elle est listée en VERROU avec la brique B-20 en mode INTERNE-GO comme producteur. La sortie de B-20 deviendra l'entrée des briques de calcul, sans passer par une nouvelle FDC (B-20 produit son propre dossier de conception).
Cas particulier — conflit entre deux pièces : si le CCTP dit XA4 et la décision RDR dit XA3, la FDC porte XA3 en valeur, Décision D-xx en fiabilité, et XA4 (CCTP, réf.) en VERROU. Le conflit n'est pas tranché en silence : il est tracé.
Format de sortie attendu : deux tableaux distincts — tableau 1 (variables résolues avec valeur, source, fiabilité), tableau 2 (VERROU avec brique suspendue et voie d'obtention). Chaque ligne du tableau 1 a impérativement une source citée.
Consignation : la FDC validée est annexée au RDR (B-03) comme décision D-xx (« validation de la FDC en date du … »). Elle est mise à jour à chaque nouvelle décision RDR qui modifie une valeur.
________________

