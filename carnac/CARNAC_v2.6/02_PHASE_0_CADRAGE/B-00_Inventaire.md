Fichier 02_PHASE_0_CADRAGE/B-00_Inventaire.md — CARNAC v2.6
________________


B-00 — INVENTAIRE DES PIÈCES ET ÉNONCÉ DE MISSION
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
	Aucune (première brique du carnet)
	Brique suivante
	B-01 (Proposition de MPD)
	Modes d'appel
	COMPLET (mode normal) · PARTIEL-DÉCLARÉ (si une pièce est illisible : on la cite sans la commenter)
	Entrées lues
	Toutes les pièces fournies par le client (DOC-01), l'énoncé de mission du client
	Sortie unique
	Inventaire structuré + liste des contradictions + énoncé de mission reformulé (5 lignes max)
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : au démarrage de chaque projet, avant toute autre brique. B-00 est la première brique de la chaîne ; sans elle, B-01 ne peut pas proposer de MPD valide.
Ce que vous fournissez à l'IA : les pièces du projet (PDF, DXF, DWG, etc.) et l'énoncé de mission du client. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}} par les valeurs du projet.
Ce que vous validez à la sortie : l'inventaire des pièces, la liste des contradictions (non résolues), la reformulation de mission en 5 lignes.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir l'inventaire complet des pièces reçues pour l'opération {{ID-01}} — {{ID-02}}, et reformuler l'énoncé de mission. Tu ne dessines rien, tu ne calcules rien, tu ne conclus rien.


ÉTAPE 1 — Inventaire des pièces
Pour chaque fichier reçu, liste :
- nom du fichier et format (PDF vectoriel / PDF image / DXF / DWG / autre) ;
- pages ou folios utiles, avec leur objet ;
- indice et date de la pièce ;
- échelle (si cotée) ;
- orientation (si plan) ;
- pièces inexploitables : image illisible, fichier corrompu, calques vides — tu le dis explicitement.


ÉTAPE 2 — Éléments structurants extraits
Liste les éléments structurants cités dans les pièces, en rattachant CHACUN à sa source (fichier + folio/page + indice) :
- murs, refends, poteaux, profilés, sommiers, fondations ;
- niveaux, hauteurs, épaisseurs ;
- usages et surcharges annoncées ;
- contraintes de site (occupation, voisinage, accès).


ÉTAPE 3 — Contradictions détectées
Liste TOUTES les contradictions entre pièces, SANS LES TRANCHER :
- donnée concernée | pièce A (référence) | pièce B (référence) | nature de l'écart.
Ne propose aucune résolution — c'est moi qui décide.


ÉTAPE 4 — Énoncé de mission reformulé
En 5 lignes maximum :
- objet de la mission ;
- périmètre du lot ;
- livrables attendus ;
- exclusions explicites (désamiantage, déplombage, curage/démolition, espaces verts, dimensionnement de la protection au feu, fluides/CVC/électricité/VRD).


INTERDICTIONS
- Ne dessine rien.
- Ne calcule rien.
- N'invente aucune pièce : tout élément cité est rattaché à un fichier et un folio.
- Ne tranche aucune contradiction.
- Si une pièce est illisible, tu le dis — tu ne la commentes pas de mémoire.
- Aucun placeholder ne doit subsister dans ta sortie.


CRITÈRE D'ACCEPTATION
L'inventaire est accepté si :
- chaque pièce reçue figure avec son indice et ses folios utiles ;
- chaque élément structurant est rattaché à une source citée ;
- chaque contradiction est listée sans être résolue ;
- l'énoncé de mission tient en 5 lignes et cite les exclusions.
Si un seul de ces quatre points n'est pas satisfait, tu signales l'écart et tu t'arrêtes — tu ne produis pas une version partielle.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} (code projet) et {{ID-02}} (intitulé de l'opération) par les valeurs du projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	« Tu ne dessines rien, tu ne calcules rien, tu ne conclus rien »
	Empêche la contamination de l'inventaire par une production prématurée — c'est la cause directe des plans génériques produits dans la conversation d'origine (prompts 2 et 5)
	« rattachés à sa source (fichier + folio + indice) »
	Verrou V2 — tout élément cité doit être traçable. Un élément structurant sans source est un élément qui ne peut pas être vérifié
	« sans les trancher — c'est moi qui décide »
	Verrou V1 — les contradictions sont signalées, pas arbitrées par le modèle. Un modèle qui tranche une contradiction en B-00 fausse toute la chaîne aval
	« Si une pièce est illisible, tu le dis — tu ne la commentes pas de mémoire »
	Anti-hallucination — la pièce illisible est l'endroit exact où un modèle comble avec du plausible. Cette clause l'oblige à déclarer l'illisibilité
	« Aucun placeholder ne doit subsister dans ta sortie »
	Verrou V7 — un placeholder résiduel est une invitation pour le modèle à combler le vide à votre place
	« Si un seul des quatre points n'est pas satisfait, tu signales l'écart et tu t'arrêtes »
	Verrou V4 — pas de livraison partielle silencieuse. Un inventaire partiel présenté comme complet est plus dangereux qu'un inventaire absent
	________________


4. RÉFÉRENCES
Briques amont
Aucune — B-00 est la première brique de la chaîne.
Briques aval
Brique
	Ce qu'elle consomme de B-00
	B-01 (MPD)
	L'inventaire des pièces et l'énoncé de mission reformulé — sans eux, B-01 ne peut pas proposer de MPD valide
	B-13 (Contradictions)
	La liste des contradictions détectées à chaud par B-00 — B-13 les reprend pour les qualifier (gravité × nature) et les rattacher aux briques
	B-14 (Périmètre de lot)
	L'énoncé de mission reformulé et les exclusions citées — B-14 s'appuie dessus pour construire la matrice INCLUS/EXCLU/À TRANCHER
	Variables consommées
Code
	Libellé
	Statut dans B-00
	DOC-01
	Inventaire des pièces (fichier, folio, indice, échelle)
	BLOQUANTE
	ID-01
	Code projet
	BLOQUANTE (pour l'en-tête de sortie)
	ID-02
	Intitulé de l'opération
	BLOQUANTE (pour l'en-tête de sortie)
	Variables produites
B-00 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (inventaire + contradictions + mission reformulée) qui alimente B-01, B-13 et B-14, mais qui n'est pas une valeur unique stockée en FDC.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	DOC-01, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain : à la sortie de B-00, vous devez vérifier que chaque pièce reçue figure dans l'inventaire, et que les contradictions listées sont bien non résolues. Si le modèle a proposé une résolution, c'est une anomalie — vous la signalez et vous demandez une reprise.
Cas particulier — pièce illisible : si une pièce est illisible (image corrompue, PDF sans couche texte, calques vides dans le DXF), B-00 la cite avec la mention « pièce inexploitable » et son motif. Elle ne la commente pas de mémoire. Vous pouvez alors soit la remplacer, soit l'inscrire au RDR (B-03) comme réserve.
Cas particulier — absence de pièce : si une pièce attendue est absente (pas de CCTP, pas de diagnostic, pas de géotechnique), B-00 ne la cite pas dans l'inventaire (elle n'a pas été reçue). C'est B-01 qui statuera son statut (FOURNIE / NON NÉCESSAIRE / À PRODUIRE PAR GO / BLOQUANTE / PARTIELLE). B-00 ne prend pas cette décision.
Format de sortie attendu : quatre tableaux ou sections distinctes — (1) inventaire des pièces, (2) éléments structurants, (3) contradictions, (4) énoncé de mission reformulé. Chaque section est identifiée par son titre.
________________

