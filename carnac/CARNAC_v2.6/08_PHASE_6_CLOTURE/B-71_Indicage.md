Fichier 08_PHASE_6_CLOTURE/B-71_Indicage.md — CARNAC v2.6
________________


B-71 — INDIÇAGE ET SUPERSESSION DOCUMENTAIRE
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	6 — Contrôle et clôture
	Brique précédente
	B-70 (Auto-contrôle de synthèse)
	Brique suivante
	B-72 (Journal de clôture)
	Fréquence
	À chaque révision d'un livrable (nouvel indice) et en fin de projet (état documentaire final)
	Modes d'appel
	COMPLET uniquement (l'indiçage est un acte administratif, pas une production)
	Paramètre d'appel
	{{périmètre}} = livrable (révision d'un livrable) / projet (état documentaire complet)
	Entrées lues
	RDL (Registre des Livrables), B-70 (verdict de cohérence), RDR (décisions et réserves), les livrables eux-mêmes (indices actuels)
	Sortie unique
	Tableau d'indiçage complet + tableau de supersession + RDL mis à jour + liste des documents en vigueur + rapport des orphelins
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique :
   * à chaque révision d'un livrable (nouvel indice) — après B-70, quand un livrable est corrigé et prêt à être réindicé ;
   * en fin de projet (état documentaire final) — avant B-72, pour figer l'état documentaire.
Ce que vous fournissez à l'IA : le RDL (Registre des Livrables), le verdict de cohérence (B-70), le RDR (décisions et réserves), et les livrables eux-mêmes (indices actuels). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{périmètre}}.
Ce que vous validez à la sortie :
   * le tableau d'indiçage (chaque document, son indice, sa date, son statut) ;
   * le tableau de supersession (révisions documentées, avec motif et auteur) ;
   * le RDL mis à jour (ligne par ligne) ;
   * la liste des documents en vigueur (indice en cours à un instant donné) ;
   * le rapport des orphelins (documents dont l'indice n'est ni en vigueur ni superseded ni annulé).
Ce que B-71 apporte de spécifique — l'administration documentaire :
Aspect
	Brique de production (B-60, B-62, B-64)
	Brique d'indiçage (B-71)
	Objet
	Produire le document
	Administrer son état (indice, supersession)
	Action
	Créer, modifier
	Figer, indiçer, superséder
	Sortie
	Le document lui-même
	Le tableau d'indiçage et la liste en vigueur
	Contenu
	Technique
	Administratif
	Responsable
	Ingénieur qui produit
	Ingénieur qui administre
	La règle la plus importante : B-71 administre les documents, elle ne les modifie pas. Un document qui change d'indice sans motif documenté est une anomalie — c'est B-71 qui la détecte.
La notion de supersession : un document est superseded quand il est remplacé par une version plus récente. Un document en vigueur est celui qui doit être utilisé à un instant donné. Un document annulé est celui qui est retiré sans être remplacé. Ces trois statuts sont les seuls possibles — il n'y a pas de statut « provisoire » ou « ancien » dans le registre.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir l'indiçage et la supersession documentaire du {{périmètre}} (livrable / projet) {{ID-01}} — {{ID-02}}, à partir du RDL, de l'auto-contrôle B-70, du RDR et des livrables eux-mêmes. Tu ne modifies AUCUN document : tu administres leur état.


MÉTHODE — DANS CET ORDRE


Étape 1 — Inventaire des documents produits
Liste tous les documents produits pour ce périmètre :
- code du document (ex. Plan_fondations_FLORA, Note_verticaux_FLORA, Nomenclature_fondations_FLORA) ;
- intitulé ;
- indice actuel (A, B, C...) ;
- date de production ;
- brique source (B-40, B-60, B-62, B-64...) ;
- statut actuel (en vigueur / superseded / annulé).


Étape 2 — Vérification de l'indice
- Chaque document a-t-il un indice attribué ?
- L'indice est-il cohérent avec l'historique (une première émission est A, une révision est B, etc.) ?
- Aucun indice n'est sauté sans raison documentée.


Étape 3 — Supersession
Pour chaque révision :
- document concerné ;
- indice précédent (superseded) ;
- indice nouveau (en vigueur) ;
- motif de la révision (correction, modification, ajout) ;
- date de la révision ;
- auteur de la révision ;
- référence à la décision RDR ou à la brique qui a produit la révision.
Une révision sans motif documenté est une révision non traçable : tu la signales.


Étape 4 — Mise à jour du RDL
Pour chaque ligne du RDL concernée :
- code livrable ;
- nouvel indice ;
- nouvelle date ;
- nouvelle version de la vue nettoyée B-32 (si applicable) ;
- nouvelle version de la preuve B-31 (si applicable) ;
- nouvelle version de la vérification B-33 (si applicable).
Le RDL est mis à jour ligne par ligne, pas remplacé en bloc.


Étape 5 — Documents en vigueur
Vue synthétique : pour chaque type de document (plans, notes, nomenclatures, notices), quel est l'indice en vigueur. C'est la liste que l'entreprise doit utiliser pour l'exécution.


Étape 6 — Détection des orphelins
- Documents dont l'indice n'est ni en vigueur, ni superseded, ni annulé : anomalie.
- Documents produits mais absents du RDL : anomalie.
- Lignes du RDL qui pointent vers un document non produit : anomalie.
Chaque anomalie est signalée avec identification de la cause probable (oubli de saisie RDL, document produit hors chaîne, etc.).


INTERDICTIONS
- Ne modifie AUCUN document : tu administres leur état, tu ne les révises pas.
- Ne change pas un indice sans motif documenté : un indice « qui a changé tout seul » est une anomalie.
- Ne remplace pas le RDL en bloc : tu le mets à jour ligne par ligne.
- Ne déclare pas un document « en vigueur » sans date : un document sans date n'est pas opposable.
- Ne fusionne pas la liste des documents en vigueur et la liste complète : ce sont deux sorties distinctes.
- Ne tolère aucun orphelin : tout document a un statut explicite, ou il est signalé.


SORTIE
Pièce 1 — Tableau d'indiçage (documents avec indice, date, statut).
Pièce 2 — Tableau de supersession (révisions documentées).
Pièce 3 — RDL mis à jour (ligne par ligne).
Pièce 4 — Liste des documents en vigueur.
Pièce 5 — Rapport des orphelins (avec cause probable).


CRITÈRE D'ACCEPTATION
L'indiçage est accepté si :
- chaque document a un indice attribué et une date ;
- chaque révision a un motif documenté (brique ou décision RDR) ;
- le RDL est mis à jour ligne par ligne (pas remplacé) ;
- la liste des documents en vigueur est produite ;
- tous les orphelins sont détectés et signalés avec leur cause probable ;
- aucun document n'est déclaré en vigueur sans date.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{périmètre}} (par livrable ou projet). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Administrer, pas modifier
	B-71 est une brique d'administration documentaire, pas de production. Confondre les deux conduit à des révisions faites « en passant » qui ne sont pas traçables — et à des documents qui changent sans que personne ne s'en aperçoive
	Indice cohérent avec l'historique
	Une première émission est A. Une révision est B. Un indice sauté (A → C) sans raison est une anomalie de traçabilité — c'est souvent le signe qu'une révision a été faite sans passer par B-71
	Supersession avec motif et auteur
	Un document qui change d'indice sans motif documenté n'est pas opposable en cas de litige. Le motif (brique source ou décision RDR) est la protection — il permet de dire « ce document a été révisé parce que B-40 a corrigé une erreur, ou parce que D-05 a modifié une valeur »
	RDL mis à jour ligne par ligne
	Un RDL remplacé en bloc perd l'historique. Un RDL mis à jour ligne par ligne conserve la traçabilité des versions — et permet de savoir quand un document a été modifié, par qui, et pourquoi
	Liste des documents en vigueur
	C'est le livrable opérationnel : l'entreprise doit savoir quel document utiliser à un instant donné. Sans cette liste, elle risque d'utiliser un indice périmé — c'est un risque majeur
	Détection des orphelins
	Un document dont l'indice n'est ni en vigueur, ni superseded, ni annulé est un document qui échappe au contrôle. Il doit être signalé, jamais ignoré
	« Ne déclare pas en vigueur sans date »
	Un document en vigueur sans date n'est pas datable, donc pas opposable. La date est un élément de validité, pas un ornement
	Trois statuts seulement (en vigueur / superseded / annulé)
	Sans cette limite, un modèle produit des statuts « provisoire », « ancien », « à réviser » — qui ne sont pas des statuts mais des états intermédiaires non définis. Trois statuts forcent la clarté
	« Ne fusionne pas la liste en vigueur et la liste complète »
	La liste en vigueur est ce que l'entreprise doit utiliser ; la liste complète est l'historique. Les fusionner rend la lecture ambiguë — on ne sait plus quel document est en vigueur
	Rapport des orphelins
	Le rapport des orphelins est la preuve que la vérification a été faite. Sans lui, l'indiçage est une affirmation — et les anomalies de traçabilité ne sont pas détectées
	Les trois statuts d'un document — précision utile :
Statut
	Définition
	Utilisation
	En vigueur
	Le document est la version actuelle — celle qui doit être utilisée pour l'exécution
	L'entreprise utilise cette version
	Superseded
	Le document a été remplacé par une version plus récente — il est conservé pour traçabilité
	Personne ne l'utilise, mais il est conservé
	Annulé
	Le document est retiré sans être remplacé — il ne doit pas être utilisé
	Personne ne l'utilise, et il est marqué comme obsolète
	Le piège du « faux nouveau » : un modèle qui reçoit une révision de livrable a tendance à :
   * soit créer un nouveau document (par exemple, « Plan_fondations_FLORA_v2 ») au lieu de réviser l'indice ;
   * soit modifier le document existant sans changer l'indice.
Les deux sont faux :
   * créer un nouveau document casse la traçabilité (on ne sait plus quel document est en vigueur) ;
   * modifier sans changer l'indice trompe l'entreprise (elle croit utiliser l'indice A alors qu'il a été modifié).
La règle est : un document = un code = un indice qui évolue. Le code reste le même, l'indice change (A → B → C). C'est la convention qui garantit la traçabilité.
Le piège de l'orphelin : un document orphelin est un document qui n'a pas de statut clair :
   * il n'est pas en vigueur (personne ne l'utilise) ;
   * il n'est pas superseded (aucune version ne le remplace) ;
   * il n'est pas annulé (personne ne l'a retiré).
C'est un document « flottant » — qui peut être utilisé par erreur, ou qui peut être perdu. B-71 doit le détecter et le signaler :
   * soit c'est un document qui devrait être en vigueur (le statut n'a pas été mis à jour) ;
   * soit c'est un document qui devrait être superseded (une version plus récente existe mais la supersession n'a pas été enregistrée) ;
   * soit c'est un document qui devrait être annulé (il est obsolète mais le statut n'a pas été mis à jour) ;
   * soit c'est un document qui devrait être dans le RDL mais qui n'y est pas (oubli de saisie).
Chaque orphelin est une anomalie de traçabilité — qui peut avoir des conséquences graves (utilisation d'un document périmé, perte d'un document valide).
Le piège du motif de révision : une révision sans motif documenté est une révision non traçable. Un modèle a tendance à :
   * soit inventer un motif (par exemple, « révision pour amélioration ») ;
   * soit omettre le motif (par exemple, « indice B » sans explication).
Les deux sont faux :
   * inventer un motif crée une fausse traçabilité (on croit savoir pourquoi le document a été révisé, mais c'est faux) ;
   * omettre le motif rend la révision non opposable (on ne sait pas pourquoi le document a changé).
La règle est : une révision = un motif documenté = un auteur = une date. C'est ce qui rend la révision défendable en cas de litige.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-71
	B-70 (Auto-contrôle de synthèse)
	Le verdict de cohérence — l'indiçage ne se fait que si le verdict est favorable
	RDL (Registre des Livrables)
	La liste des documents produits et leurs indices actuels
	B-03 (RDR)
	Les décisions et réserves — le motif de révision peut être une décision RDR
	B-60, B-62, B-64
	Les documents produits — B-71 les indice et gère leur supersession
	Briques aval
Brique
	Ce qu'elle consomme de B-71
	B-72 (Journal de clôture)
	La liste des documents en vigueur — B-72 la cite dans le journal
	MOE, BC, BET (destinataires)
	La liste des documents en vigueur — ils l'utilisent pour vérifier le dossier
	Entreprise (destinataire)
	La liste des documents en vigueur — elle l'utilise pour l'exécution
	Variables consommées
Code
	Libellé
	Statut dans B-71
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	ID-05
	Indice du dossier en vigueur
	BLOQUANTE
	DEC-04
	Documents supersédés (indice, date)
	BLOQUANTE
	Variables produites
Code
	Libellé
	Description
	DEC-04
	Documents supersédés
	Chaque document avec son indice, sa date, son statut (en vigueur / superseded / annulé)
	Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	ID-01, ID-02, ID-05, DEC-04
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Nommage, indiçage, formats
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-71, vous devez valider les motifs de révision — c'est vous qui savez si une révision est justifiée. Un modèle qui invente un motif crée une fausse traçabilité — qui peut vous être reprochée en cas de litige.
Cas particulier — première émission : si le document est une première émission, l'indice est A. La date est la date de production. Le statut est en vigueur. Il n'y a pas de supersession (aucune version antérieure).
Cas particulier — révision : si le document est une révision, l'indice est B, C, D.... La date est la date de révision. Le statut est en vigueur (le nouvel indice remplace l'ancien). L'ancien indice passe en superseded. Le motif de révision est documenté (brique source ou décision RDR).
Cas particulier — annulation : si le document est retiré sans être remplacé (par exemple, un plan qui n'est plus nécessaire), le statut est annulé. La date et le motif d'annulation sont documentés.
Cas particulier — plusieurs révisions successives : si un document a plusieurs indices successifs (par exemple, A → B → C), chaque indice a son statut :
   * A : superseded (remplacé par B) ;
   * B : superseded (remplacé par C) ;
   * C : en vigueur (version actuelle).
Le RDL conserve toutes les versions (pour traçabilité), mais la liste des documents en vigueur ne cite que C.
Cas particulier — document orphelin : si un document est orphelin (indice sans statut clair), B-71 le signale dans son rapport des orphelins. Vous devez alors :
   * soit compléter le statut (en vigueur, superseded, annulé) ;
   * soit retirer le document (s'il n'a pas lieu d'être).
Un document orphelin ne peut pas rester dans le RDL sans statut — c'est une anomalie qui doit être corrigée.
Cas particulier — document produit mais absent du RDL : si un document a été produit (par exemple, un plan B-60) mais n'est pas dans le RDL, B-71 le signale. Vous devez :
   * soit ajouter la ligne du RDL (avec l'indice, la date, le statut) ;
   * soit identifier l'oubli (le document a été produit hors chaîne, ou la saisie RDL a été omise).
Un document produit hors RDL est un document non traçable — c'est une anomalie de production.
Cas particulier — document dans le RDL mais non produit : si le RDL cite un document qui n'a pas été produit (par exemple, une ligne « Plan_fondations_B » alors que B-60 n'a produit que l'indice A), B-71 le signale. Vous devez :
   * soit corriger la ligne du RDL (indice erroné) ;
   * soit produire le document (B-60 en mode COMPLET).
Un document cité mais non produit est un document qui n'existe pas — c'est une anomalie de traçabilité.
Format de sortie attendu : cinq pièces distinctes (tableau d'indiçage, tableau de supersession, RDL mis à jour, liste des documents en vigueur, rapport des orphelins). La liste des documents en vigueur est la sortie opérationnelle — c'est ce que l'entreprise utilisera pour l'exécution.
Consignation : l'indiçage B-71 est consigné au RDL (ligne par ligne, pour chaque document concerné) — il fait partie du dossier de livraison.
________________

