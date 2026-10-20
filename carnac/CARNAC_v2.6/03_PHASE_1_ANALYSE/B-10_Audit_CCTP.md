Fichier 03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md — CARNAC v2.6
________________


B-10 — AUDIT CRITIQUE DU CCTP ET DES PIÈCES CONTRACTUELLES
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	1 — Analyse
	Brique précédente
	B-04 (PTD) — ou la première brique exécutable selon le PTD
	Brique suivante
	B-13 (Contradictions) — via B-14 (Périmètre de lot) si applicable
	Modes d'appel
	COMPLET (CCTP fourni) · PARTIEL-DÉCLARÉ (CCTP partiel ou non indicé : on signale l'indice manquant et on poursuit sur le périmètre disponible) · SANS OBJET (marché en conception-réalisation sans CCTP : à statuer par la MPD)
	Entrées lues
	DOC-04 (CCTP), DOC-03 (plans BET), énoncé de mission (B-00), MPD validée (B-01)
	Sortie unique
	Audit article par article + quatre tableaux (constats / lacunes / contradictions internes / points à lever)
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : au début de la phase 1 (Analyse), après la phase 0 (Cadrage). B-10 est la première brique d'audit — elle analyse le CCTP, pas le diagnostic existant (B-11) ni la géotechnique (B-12).
Ce que vous fournissez à l'IA : le CCTP complet (lot gros œuvre / structure), les plans BET structure (si disponibles), l'énoncé de mission reformulé (sortie de B-00), et la MPD validée. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * les constats (chaque constat rattaché à un article précis du CCTP) ;
   * les lacunes (ce que le CCTP ne dit pas et qui impacte nos études) ;
   * les contradictions internes (sans être résolues) ;
   * les points à lever (avec destinataire et urgence).
Ce que B-10 ne fait pas : B-10 n'est pas une brique de conception. Elle ne propose aucune solution technique, ne dimensionne rien, n'arbitre aucune contradiction. C'est une brique de constat — c'est la brique amont de B-13 (qualification des contradictions) et de B-14 (matrice de périmètre).
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : effectuer l'audit critique du CCTP lot gros œuvre de l'opération {{ID-01}} — {{ID-02}}, pour notre compte (entreprise GO). Tu produis un audit, pas une conception : tu ne proposes aucune solution technique, tu ne dimensionnes rien, tu n'arbitres aucune contradiction.


PÉRIMÈTRE DE L'AUDIT
- Toutes les prescriptions qui engagent le lot gros œuvre / structure.
- Les prestations incluses et exclues du lot.
- Les interfaces avec les autres lots.
- Les prescriptions qui engagent NOTRE responsabilité contractuelle (reprises en sous-œuvre, déchaussement, démolitions, aléas géotechniques, phasage).
- Les prescriptions qui renvoient à des valeurs, classes ou normes que nous devrons respecter dans nos notes de calcul.


MÉTHODE
1. Parcours le CCTP article par article. Pour chaque article qui intéresse le lot GO, identifie : ce qui est prescrit, ce qui manque, ce qui est contradictoire avec une autre pièce du DCE.
2. Distingue trois catégories de constats :
   - CONSTAT : ce que le CCTP prescrit effectivement.
   - LACUNE : ce que le CCTP aurait dû prescrire et ne prescrit pas.
   - CONTRADICTION INTERNE : deux articles du CCTP, ou deux pièces contractuelles, qui se contredisent.
3. Ne tranche aucune contradiction. Tu la listes.
4. Ne propose aucune solution technique. Tu listes les points à lever, avec le destinataire.


INTERDICTIONS
- Tu ne dimensionnes rien, tu ne choisis aucune classe de matériau, tu ne proposes aucune section, aucun ferraillage, aucune nuance.
- Tu ne tranches aucune contradiction entre articles ou entre pièces.
- Tu ne cites aucune prescription de mémoire : chaque constat est rattaché à un article précis du CCTP (numéro ou intitulé).
- Tu ne qualifies pas un point de « résolu » parce qu'une pièce ultérieure semble le couvrir : tu le listes, c'est moi qui tranche.


SORTIE
Quatre tableaux obligatoires.


Tableau 1 — Constats
Article CCTP | Prescription | Nature (prescriptive / normative / de renvoi) | Impact sur nos études | Source


Tableau 2 — Lacunes
Objet de la lacune | Ce que le CCTP ne dit pas | Conséquence pour nos études | Brique concernée (B-40 à B-50)


Tableau 3 — Contradictions internes au DCE (CCTP vs autres pièces contractuelles)
Objet | Article A (référence) | Pièce B (référence) | Nature de l'écart | Statut (à lever)


Tableau 4 — Points à lever
N° | Objet | Nature (lacune / contradiction / imprécision) | Destinataire (MOE / MOA / BET / BC) | Urgence (avant remise / avant démarrage / pendant EXE)


Puis une synthèse de 10 lignes maximum :
- les trois points qui engagent le plus notre responsabilité ;
- les trois points qui auront le plus d'impact sur nos notes de calcul ;
- la liste des prescriptions qui nécessitent une confirmation écrite avant de démarrer les études.


CRITÈRE D'ACCEPTATION
L'audit est accepté si :
- chaque constat est rattaché à un article précis du CCTP ;
- chaque lacune identifie la brique aval qu'elle bloque ou qu'elle fragilise ;
- chaque contradiction est listée sans être résolue ;
- chaque point à lever identifie un destinataire et une urgence ;
- aucune solution technique n'a été proposée ;
- la synthèse tient en 10 lignes.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	« Tu produis un audit, pas une conception »
	Un audit qui propose des solutions devient une conception implicite, non tracée, non visée — et qui engage votre responsabilité sans validation. La frontière avec B-20 (conception) et B-40 à B-50 (calculs) doit être nette : l'audit constate, la conception décide
	« Tu ne proposes aucune solution technique, tu ne dimensionnes rien »
	Frontière nette avec B-20/B-40 et suivantes : c'est la conception qui décide, pas l'audit. Sans cette clause, un modèle glisse vers la conception — et on se retrouve avec des décisions non tracées
	« Tu ne cites aucune prescription de mémoire »
	Verrou V2 — le CCTP est trop souvent « à peu près connu ». La citation exacte (numéro d'article ou intitulé) est la seule défense en cas de litige sur un périmètre. Un constat sans référence est un constat inopposable
	« Tu ne qualifies pas un point de résolu parce qu'une pièce ultérieure semble le couvrir »
	C'est la faille exacte de la conversation d'origine : la contradiction XC2/35 vs XA3/50 a été « résolue » par un arbitrage implicite. Cette clause interdit ce type de résolution silencieuse — le point reste listé, c'est vous qui tranchez (et la décision va au RDR)
	« Destinataire + urgence » dans le tableau 4
	Un point à lever sans destinataire ne se lève jamais ; un point sans urgence est traité trop tard. Les deux colonnes sont indispensables pour que l'audit soit actionnable, pas seulement descriptif
	« Brique concernée (B-40 à B-50) » dans le tableau 2
	Chaque lacune du CCTP a une conséquence sur une brique de calcul précise. Nommer la brique évite les lacunes « orphelines » que personne ne traite
	« Synthèse en 10 lignes »
	Force la hiérarchisation — un audit exhaustif sans synthèse n'est pas exploitable en réunion de lancement. Les 10 lignes forcent le modèle à choisir les trois points les plus importants
	« Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes »
	Verrou V4 — pas de livraison partielle silencieuse. Un audit partiel présenté comme complet est plus dangereux qu'un audit absent : il donne l'illusion que le CCTP est propre
	Les trois catégories de constats — précision utile :
Catégorie
	Définition
	Traitement en aval
	CONSTAT
	Ce que le CCTP prescrit effectivement
	Va en FDC (B-02) si c'est une valeur exploitable ; va en B-14 si c'est un périmètre
	LACUNE
	Ce que le CCTP aurait dû prescrire et ne prescrit pas
	Va en B-13 (si c'est une contradiction avec une autre pièce) ou en réserve R-xx (RDR)
	CONTRADICTION INTERNE
	Deux articles ou deux pièces qui se contredisent
	Va en B-13 pour qualification (gravité × nature)
	________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-10
	B-00 (Inventaire)
	L'inventaire des pièces, la référence exacte du CCTP (fichier + folio + indice), l'énoncé de mission reformulé
	B-01 (MPD validée)
	Le statut de DOC-04 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET)
	B-03 (RDR)
	Les décisions déjà prises (par exemple, une décision de périmètre qui précise ce qui est dans le lot GO)
	Briques aval
Brique
	Ce qu'elle consomme de B-10
	B-13 (Contradictions)
	Les contradictions internes détectées par B-10 — B-13 les qualifie (gravité × nature) et les rattache aux briques
	B-14 (Périmètre de lot)
	Les constats et les lacunes — B-14 construit la matrice INCLUS/EXCLU/À TRANCHER à partir de ces informations
	B-15 (Synthèse des risques)
	Les points à lever et les prescriptions à confirmer — B-15 les intègre dans le registre des risques
	T-04 (Demande de complément)
	Les points à lever avec destinataire — T-04 transforme ces points en demande formelle à la MOE / BET / MOA
	Variables consommées
Code
	Libellé
	Statut dans B-10
	DOC-04
	CCTP / pièces contractuelles
	BLOQUANTE
	DOC-03
	Plans BET structure (si disponibles)
	NON BLOQUANTE (si absents, l'audit est fait sur le CCTP seul)
	ID-01
	Code projet
	BLOQUANTE (pour l'en-tête de sortie)
	ID-02
	Intitulé de l'opération
	BLOQUANTE (pour l'en-tête de sortie)
	Variables produites
B-10 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (audit CCTP) qui alimente B-13, B-14 et B-15.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	DOC-04, DOC-03, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus important : à la sortie de B-10, vous devez vérifier que :
   1. chaque constat est rattaché à un article précis du CCTP (pas « le CCTP dit que… » sans référence) ;
   2. chaque lacune identifie la brique concernée (B-40 à B-50) — c'est ce qui permet de la traiter ;
   3. chaque contradiction interne est listée sans être résolue ;
   4. chaque point à lever a un destinataire et une urgence.
Cas particulier — CCTP partiel : si le CCTP est fourni en plusieurs lots, B-10 audite le lot gros œuvre uniquement. Les autres lots (fluides, électricité, etc.) ne sont pas audités — ils sont traités par les briques de coordination uniquement.
Cas particulier — CCTP non indicé : si le CCTP n'a pas d'indice (pièce « provisoire » ou « pour consultation »), B-10 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'absence d'indice dans la synthèse. L'absence d'indice est une réserve en soi : toute prescription du CCTP non indicé peut être révisée unilatéralement par la MOE.
Cas particulier — CCTP absent (conception-réalisation) : si le marché est en conception-réalisation et qu'il n'y a pas de CCTP mais un « programme fonctionnel », B-10 s'appelle en mode SANS OBJET (à statuer par la MPD). Ce sont B-20 (Conception GO) et B-14 (Périmètre de lot) qui couvrent alors la définition du périmètre — pas B-10.
Format de sortie attendu : quatre tableaux distincts (constats, lacunes, contradictions internes, points à lever), suivis d'une synthèse en 10 lignes maximum.
Consignation : l'audit B-10 est annexé au RDR (B-03) — il documente la lecture du CCTP et alimente les réserves (R-xx) pour les points à lever.
________________

