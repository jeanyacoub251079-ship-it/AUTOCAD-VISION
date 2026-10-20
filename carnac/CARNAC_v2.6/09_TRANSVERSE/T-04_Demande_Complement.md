Fichier 09_TRANSVERSE/T-04_Demande_Complement.md — CARNAC v2.6
________________


T-04 — PROMPT DE DEMANDE DE COMPLÉMENT
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
	B-04 (PTD) — ou toute brique qui identifie une donnée bloquante manquante
	Brique suivante
	Retour à la brique concernée (B-40 à B-50) une fois la réponse obtenue
	Modes d'appel
	COMPLET uniquement
	Entrées lues
	RDR (points ouverts), briques suspendues, MPD (variables bloquantes)
	Sortie unique
	Demande de complément formelle à la MOE / au BET / au MOA, structurée et datée, avec échéance et conséquence de non-réponse, + mise à jour du RDR
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique :
   * à la fin de la phase 0 (cadrage) — pour les données bloquantes identifiées à la MPD ;
   * à tout moment si une donnée bloquante est découverte en cours de production ;
   * avant remise d'une offre ou d'un livrable important.
Ce que vous fournissez à l'IA : le RDR (points ouverts, verrous), la liste des briques suspendues, la MPD (variables bloquantes) et le destinataire (MOE / BET / MOA / BC). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{destinataire}}.
Ce que vous validez à la sortie :
   * la liste des demandes (une par point ouvert) ;
   * la conséquence de non-réponse pour chaque demande ;
   * l'échéance pour chaque demande ;
   * la priorisation (URGENTE / IMPORTANTE / DE SUIVI) ;
   * la forme de la demande (courrier formel) ;
   * la consignation au RDR (section 2 et 3).
Ce que T-04 apporte de spécifique — la demande formelle :
Aspect
	Point ouvert au RDR (B-03)
	Demande de complément (T-04)
	Objet
	Constater un point ouvert
	Le transformer en demande formelle à un destinataire
	Forme
	Ligne de tableau
	Courrier structuré et daté
	Destinataire
	Mentionné
	Explicitement adressé
	Échéance
	Mentionnée
	Explicite et opposable
	Conséquence
	Implicite
	Explicite (« si non-réponse, alors… »)
	Traçabilité
	Au RDR
	Au RDR + courrier envoyé
	T-04 est la brique qui transforme un point ouvert en demande opposable. Un point ouvert au RDR est un constat interne — il ne déclenche pas d'action. Une demande formelle est un acte administratif — elle déclenche une réponse, ou elle documente l'absence de réponse (ce qui vous protège en cas de litige).
La règle la plus importante : T-04 ne rédige aucune demande sans conséquence de non-réponse et sans échéance. Une demande sans conséquence est une demande qui ne se traite pas — elle reste dans la pile du destinataire.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : rédiger la demande de complément formelle de l'opération {{ID-01}} — {{ID-02}} à destination de {{destinataire}} (MOE / BET / MOA / BC), à partir des points ouverts du RDR et des briques suspendues. La demande doit être structurée, datée, et opposer à chaque point une conséquence de non-réponse.


MÉTHODE


Étape 1 — Inventaire des points ouverts
Reprends du RDR et du Registre des Verrous :
- les variables BLOQUANTES manquantes (FDC) ;
- les briques suspendues et leurs conséquences ;
- les décisions en attente (RDR section 1) ;
- les hypothèses à confirmer (RDR section 4).


Étape 2 — Structuration de la demande
Chaque demande comporte obligatoirement :
- numéro de demande (D-xx ou R-xx, cohérent avec le RDR) ;
- objet de la demande (donnée manquante, décision à prendre, confirmation d'hypothèse) ;
- brique(s) concernée(s) ;
- conséquence de non-réponse : quelle(s) brique(s) reste(nt) suspendue(s), quel(s) livrable(s) ne peu(ven)t pas être émis, quel impact sur le planning ;
- échéance souhaitée ;
- destinataire.


Étape 3 — Priorisation
Classe les demandes en trois catégories :
- URGENTES : bloquent la remise d'un livrable majeur ou l'engagement de la phase suivante.
- IMPORTANTES : bloquent une partie de la production mais n'empêchent pas les autres briques.
- DE SUIVI : à traiter avant l'exécution, mais pas avant la remise des études.


Étape 4 — Rédaction formelle
Rédige la demande en respectant les formes :
- en-tête : projet, date, destinataire, objet ;
- corps : liste numérotée des demandes, structurée comme à l'étape 2 ;
- clôture : demande d'accusé de réception et de réponse écrite dans les délais ;
- signature : nom et fonction de l'expéditeur (à remplir).


Étape 5 — Traçabilité
Chaque demande est consignée au RDR (section 2 ou 3) :
- numéro de demande ;
- date d'envoi ;
- destinataire ;
- échéance ;
- statut (envoyée / en attente / répondue).


INTERDICTIONS
- Ne rédige aucune demande sans conséquence de non-réponse : une demande sans conséquence est une demande qui ne se traite pas.
- Ne rédige aucune demande sans échéance : une demande sans échéance est une demande sans priorité.
- Ne mélange pas les demandes URGENTES et les demandes de suivi : elles n'ont pas le même traitement.
- Ne rédige pas de demande vague (« fournir les données manquantes ») : chaque demande porte sur une donnée précise, avec sa référence au RDR.
- N'oublie aucun point ouvert : chaque point du RDR doit avoir sa demande correspondante.
- Ne produis pas de demande sans consignation au RDR : une demande non consignée n'est pas opposable.


SORTIE
Pièce 1 — Demande formelle (courrier).
Pièce 2 — Tableau de synthèse des demandes (numéro, objet, brique, échéance, destinataire, conséquence de non-réponse).
Pièce 3 — Mise à jour du RDR (section 2 et 3).


CRITÈRE D'ACCEPTATION
La demande est acceptée si :
- chaque point ouvert du RDR a sa demande correspondante ;
- chaque demande a une conséquence de non-réponse explicite ;
- chaque demande a une échéance ;
- chaque demande est classée en URGENTE / IMPORTANTE / DE SUIVI ;
- la forme est respectée (en-tête, corps, clôture, signature) ;
- chaque demande est consignée au RDR.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{destinataire}} (par MOE, BET, MOA ou BC). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Conséquence de non-réponse obligatoire
	Une demande sans conséquence (« merci de fournir le G2 ») est une demande qui ne se traite pas. La conséquence (« la brique B-40 reste suspendue, le livrable de fondations ne peut pas être émis ») est ce qui déclenche la réponse — elle rend le destinataire responsable du retard
	Échéance obligatoire
	Une demande sans échéance se traite quand le destinataire a le temps — c'est-à-dire tard. L'échéance rend la demande prioritaire
	Priorisation URGENTE / IMPORTANTE / DE SUIVI
	Sans priorisation, toutes les demandes sont traitées au même niveau, ce qui revient à traiter les urgentes trop tard. La priorisation permet au destinataire de savoir ce qui bloque et ce qui peut attendre
	Consignation au RDR
	Une demande orale ou par mail non consignée n'est pas opposable. La consignation au RDR transforme la demande en trace formelle — c'est ce qui vous protège en cas de litige
	Chaque point du RDR = une demande
	Un point du RDR sans demande est un point qui reste ouvert indéfiniment. La correspondance stricte point ↔ demande garantit que rien n'est oublié
	Demande précise (pas vague)
	Une demande vague (« fournir les données manquantes ») ne permet pas au destinataire de savoir quoi fournir. Une demande précise (« fournir q_adm ELS selon NF P 94-261, référence SOL-01 du RDR ») permet une réponse rapide
	Forme respectée (en-tête, corps, clôture, signature)
	Un courrier sans forme n'est pas un courrier — c'est un message. La forme (en-tête, date, destinataire, signature) rend la demande officielle — elle peut être produite en justice si nécessaire
	Clôture avec accusé de réception
	L'accusé de réception est la preuve que la demande a été reçue. Sans lui, le destinataire peut nier avoir reçu la demande — l'accusé est votre protection
	« Ne mélange pas URGENTES et DE SUIVI »
	Un courrier qui mélange les urgentes et les demandes de suivi dilue les urgentes — le destinataire traite tout au même niveau, et les urgentes ne sont pas traitées en priorité. Les séparer rend la demande lisible
	« Ne produis pas de demande sans consignation au RDR »
	Une demande sans consignation est une demande « dans le vide » — elle n'est pas traçable, elle ne peut pas être suivie, elle ne peut pas être opposée en cas de litige
	Les trois niveaux de priorité — précision utile :
Priorité
	Définition
	Exemple
	URGENTE
	Bloque la remise d'un livrable majeur ou l'engagement de la phase suivante
	q_adm manquante — bloque le livrable de fondations
	IMPORTANTE
	Bloque une partie de la production mais n'empêche pas les autres briques
	Section d'une panne existante non sondée — bloque la vérification de la charpente, mais les autres briques tournent
	DE SUIVI
	À traiter avant l'exécution, mais pas avant la remise des études
	Niveau d'assise exact des fondations — à préciser à l'ouverture des fouilles, pas avant
	Le piège de la demande vague : un modèle a tendance à produire des demandes vagues (« fournir les données manquantes », « confirmer les hypothèses »). C'est exactement ce qu'il faut interdire :
   * une demande vague ne permet pas au destinataire de savoir quoi fournir ;
   * elle ne permet pas de savoir quand la réponse est attendue ;
   * elle n'a pas de conséquence de non-réponse claire — donc elle ne déclenche rien.
La règle est : une demande = une donnée précise = un code RDR. C'est la seule forme qui déclenche une réponse.
Le piège de la « conséquence vague » : un modèle a tendance à produire des conséquences vagues (« retard sur le planning », « impact sur les livrables »). C'est exactement ce qu'il faut interdire :
   * une conséquence vague ne permet pas de mesurer l'impact réel ;
   * elle ne permet pas de décider si le retard est critique ou non ;
   * elle ne permet pas d'opposer la demande en cas de litige.
La règle est : une conséquence précise = une brique suspendue = un livrable non émis. C'est la seule forme qui a du poids.
Le piège du courrier unique : un modèle a tendance à produire un seul courrier qui regroupe toutes les demandes. C'est acceptable si les demandes sont de même priorité et au même destinataire — sinon, il faut séparer :
   * courrier urgent (destinataire MOA) — pour les données qui bloquent la remise ;
   * courrier important (destinataire BET) — pour les données qui bloquent une partie de la production ;
   * courrier de suivi (destinataire MOE) — pour les données à préciser avant l'exécution.
Séparer les courriers permet au destinataire de traiter par priorité — et rend la traçabilité plus claire.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à T-04
	B-03 (RDR)
	Les points ouverts (verrous, réserves, décisions en attente, hypothèses à confirmer) — T-04 les transforme en demandes
	B-04 (PTD)
	Les briques suspendues et les données manquantes — T-04 les cite dans les demandes
	B-02 (FDC)
	Les variables BLOQUANTE — T-04 les cite comme objets de demande
	B-12 (Audit Géotechnique)
	Les recommandations de mission — T-04 les reprend comme demandes à la MOA
	Briques aval
Brique
	Ce qu'elle consomme de T-04
	RDR (B-03)
	Les demandes consignées (statut envoyée / en attente / répondue) — le RDR est mis à jour
	La brique concernée (B-40 à B-50)
	La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ
	B-72 (Journal de clôture)
	Les demandes non répondues à la date de clôture — B-72 les cite dans les points ouverts
	MOE, BET, MOA, BC (destinataires)
	Les demandes — ils répondent dans les délais
	Variables consommées
Code
	Libellé
	Statut dans T-04
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	DEC-03
	Verrous ouverts
	BLOQUANTE (T-04 ne peut pas produire de demande sans la liste des verrous)
	Toutes les variables BLOQUANTE de la FDC
	Selon la variable
	BLOQUANTE (chaque variable bloquante doit être l'objet d'une demande)
	Variables produites
T-04 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (demande formelle + tableau de synthèse + RDR mis à jour) qui alimente le RDR, la brique concernée et B-72.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	ID-01, ID-02, DEC-03
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-04, vous devez valider les conséquences de non-réponse — c'est votre appréciation de la criticité qui fait foi. Une conséquence « retard sur le livrable de fondations de 2 semaines » est votre engagement — elle doit être réaliste et défendable.
Cas particulier — demandes à plusieurs destinataires : si les demandes concernent plusieurs destinataires (par exemple, une donnée MOA et une donnée BET), T-04 produit un courrier par destinataire — pas un courrier unique. Chaque destinataire reçoit uniquement les demandes qui le concernent.
Cas particulier — demandes de priorités différentes : si les demandes ont des priorités différentes (par exemple, deux urgentes et trois de suivi), T-04 peut produire :
   * un courrier urgent (destinataire concerné) — pour les demandes qui bloquent la remise ;
   * un courrier de suivi (destinataire concerné) — pour les demandes à traiter avant l'exécution.
Le courrier urgent est envoyé immédiatement ; le courrier de suivi peut être envoyé dans un délai plus long.
Cas particulier — demande déjà envoyée : si une demande a déjà été envoyée (par exemple, dans un courrier antérieur), T-04 ne la reproduit pas — elle est relancée (rappel avec la date du premier envoi et la date de relance). Le RDR est mis à jour avec le statut « relancée ».
Cas particulier — demande répondue : si une demande a été répondue, T-04 ne la reproduit pas — elle est clôturée au RDR (statut « répondue », avec la date de réponse et la référence à la pièce reçue). La brique concernée est relancée en mode COMPLET (ou PARTIEL-DÉCLARÉ si la réponse est partielle).
Cas particulier — demande refusée : si une demande est refusée par le destinataire (par exemple, la MOA refuse de commander un G3), T-04 ne la reproduit pas — elle est clôturée au RDR (statut « refusée », avec la date et le motif du refus). La brique concernée est relancée en mode PARTIEL-DÉCLARÉ (avec la décision de repli) ou reste suspendue (avec la mention « refusée »).
Cas particulier — demande sans réponse à la clôture : si une demande est sans réponse à la date de clôture, T-04 la cite dans le journal de clôture (B-72) comme point ouvert — avec la date d'envoi, l'échéance, et la conséquence de non-réponse. C'est ce qui vous protège en cas de litige : la demande a été envoyée, la réponse n'est pas venue, et vous avez documenté la conséquence.
Format de sortie attendu : trois pièces distinctes (demande formelle, tableau de synthèse, RDR mis à jour). La demande formelle est rédigée au format courrier — en-tête, corps, clôture, signature.
Consignation : la demande T-04 est consignée au RDR (section 2 pour les réserves, section 3 pour les verrous) — elle fait partie de la traçabilité du projet.
________________

