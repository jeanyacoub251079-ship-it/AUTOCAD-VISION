Fichier 03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md — CARNAC v2.6
________________


B-14 — CLARIFICATION DU PÉRIMÈTRE DE LOT
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
	B-10 (Audit CCTP), B-11 (Audit Diagnostic)
	Brique suivante
	B-15 (Synthèse des risques)
	Modes d'appel
	COMPLET (CCTP et décomposition en lots fournis) · PARTIEL-DÉCLARÉ (pas de DPGF ou de décomposition en lots : on signale l'absence et on poursuit sur ce que dit le CCTP)
	Entrées lues
	B-10 (audit CCTP : constats + lacunes), B-11 (interfaces de lots), énoncé de mission (B-00), MPD (B-01)
	Sortie unique
	Matrice du périmètre : ce qui est INCLUS / EXCLU / À TRANCHER (interfaces) + points à faire confirmer
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-10 et B-11, avant B-15. B-14 est la brique qui transforme l'audit en matrice de périmètre — elle ne réaudite pas le CCTP, elle utilise les constats de B-10 pour dire ce qui est à nous.
Ce que vous fournissez à l'IA : les sorties de B-10 et B-11, l'énoncé de mission (B-00), la MPD validée. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * les prestations INCLUSES (avec l'article du CCTP qui les prescrit) ;
   * les prestations EXCLUES (avec la pièce qui les attribue à un autre lot) ;
   * les prestations À TRANCHER (avec la nature de l'ambiguïté et un destinataire) ;
   * les prestations hors périmètre CARNAC (tableau séparé).
Ce que B-14 apporte de spécifique — la matrice de périmètre : B-10 dit « le CCTP est-il bien écrit ? ». B-14 dit « qu'est-ce qui est à nous ? ». C'est une sortie radicalement différente, et c'est cette matrice qui vous permet de :
   1. Ne pas accepter implicitement une prestation que le CCTP ne prescrit pas clairement (une prestation que vous acceptez implicitement devient la vôtre) ;
   2. Ne pas refuser une prestation que le CCTP prescrit explicitement (un refus non fondé est un manquement contractuel) ;
   3. Identifier les interfaces — les prestations que deux lots se renvoient, ou qu'aucun ne prend.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la matrice du périmètre du lot gros œuvre de l'opération {{ID-01}} — {{ID-02}}, à partir de l'audit CCTP (B-10), de l'audit du diagnostic (B-11) et de l'énoncé de mission (B-00). Tu ne réaudites pas le CCTP : tu utilises les constats de B-10 pour dire ce qui est à nous.


MÉTHODE
1. Liste les prestations qui touchent le lot gros œuvre / structure, qu'elles soient citées dans le CCTP, dans le diagnostic, dans les plans, ou implicites.
2. Pour chaque prestation, attribue un statut unique parmi :
   - INCLUS : le CCTP prescrit la prestation à notre lot, sans ambiguïté.
   - EXCLU : le CCTP attribue explicitement la prestation à un autre lot, ou l'énoncé de mission la cite en exclusion.
   - À TRANCHER : aucune pièce ne tranche clairement — soit deux lots se renvoient la prestation, soit aucun ne la prend, soit le CCTP est silencieux.
3. Distingue soigneusement :
   - prestation EXCLUE (quelqu'un d'autre la fait) ;
   - prestation À TRANCHER (personne ne l'a prise, ou deux personnes la revendiquent) ;
   - prestation hors périmètre CARNAC (désamiantage, déplombage, curage, espaces verts, dimensionnement protection au feu, fluides, VRD) — elle n'entre NI en INCLUS NI en EXCLU : elle est listée en tableau séparé, conformément aux exclusions du carnet.
4. Pour chaque prestation À TRANCHER, identifie : le lot pressenti (si l'un est plus probable), la pièce qui crée l'ambiguïté, la conséquence pour nos études si elle n'est pas tranchée.
5. Pour chaque prestation INCLUSE qui comporte une prescription technique à valider (ex. : reprise en sous-œuvre par passes alternées), identifie la brique CARNAC qui devra la valider.


INTERDICTIONS
- Ne tranche AUCUNE attribution : tu listes, c'est moi qui décide (et la MOE qui confirme).
- Ne réaudite pas le CCTP : tu utilises les constats de B-10.
- N'inscris jamais une prestation INCLUSE sans citer l'article du CCTP qui la prescrit.
- N'inscris jamais une prestation EXCLUE sans citer la pièce qui l'attribue à un autre lot.
- Ne déclare pas « À TRANCHER » une prestation qui figure explicitement dans le CCTP : si le CCTP est clair, elle est INCLUSE ou EXCLUE.
- Ne mets pas en INCLUS ou EXCLU les prestations hors périmètre CARNAC (désamiantage, etc.) : elles ont un tableau séparé.


SORTIE
Trois tableaux principaux et un tableau séparé.


Tableau 1 — Prestations INCLUSES dans notre lot
Prestation | Article CCTP (réf. exacte) | Ce que cela implique techniquement | Brique CARNAC qui validera | Points à lever (si prescription incomplète)


Tableau 2 — Prestations EXCLUES de notre lot
Prestation | Pièce qui l'attribue à un autre lot (réf.) | Lot pressenti | Interface éventuelle avec notre lot


Tableau 3 — Prestations À TRANCHER
Prestation | Pièce(s) en cause (réf.) | Nature de l'ambiguïté (renvoi mutuel / silence / conflit) | Lot pressenti | Conséquence pour nos études | Destinataire pour trancher


Tableau 4 — Hors périmètre CARNAC (à titre documentaire)
Prestation | Motif de l'exclusion (référence aux exclusions du carnet)


Puis une synthèse de 10 lignes maximum :
- les trois prestations INCLUSES les plus engageantes (en volume, en risque, en délai) ;
- les trois prestations À TRANCHER les plus critiques (impact sur les études ou sur le planning) ;
- la liste des confirmations à obtenir avant démarrage des études.


CRITÈRE D'ACCEPTATION
La matrice est acceptée si :
- chaque prestation INCLUSE cite l'article du CCTP qui la prescrit ;
- chaque prestation EXCLUE cite la pièce qui l'attribue à un autre lot ;
- chaque prestation À TRANCHER identifie la nature de l'ambiguïté et un destinataire ;
- aucune attribution n'a été tranchée par toi ;
- les prestations hors périmètre CARNAC sont dans un tableau séparé ;
- la synthèse tient en 10 lignes.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Trois statuts seulement : INCLUS / EXCLU / À TRANCHER
	Sans cette limite, un modèle produit des « partiellement inclus » qui masquent les ambiguïtés au lieu de les nommer. Trois statuts forcent la clarté : soit c'est à nous, soit c'est à un autre, soit personne ne l'a tranché
	Tableau séparé pour les exclusions CARNAC
	Un désamiantage n'est ni « inclus » ni « exclu du lot GO » : il est hors périmètre CARNAC — la nuance empêche le modèle de raisonner sur des prestations qu'il ne doit pas traiter
	« Ne réaudite pas le CCTP »
	Évite la redondance avec B-10 et libère de la place pour la vraie valeur ajoutée : la matrice de périmètre. Un modèle sans cette clause refait le travail de B-10 au lieu de le synthétiser
	« Ne tranche AUCUNE attribution »
	L'attribution d'une prestation à un lot est une décision contractuelle — jamais une décision du modèle. Un modèle qui tranche crée une décision implicite non opposable
	« Ne déclare pas À TRANCHER une prestation qui figure explicitement dans le CCTP »
	Empêche la sur-génération de « À TRANCHER » qui noie les vrais points d'interface. Si le CCTP dit clairement « cette prestation est au lot GO », elle est INCLUSE — pas À TRANCHER
	« Destinataire pour trancher »
	Un point d'interface sans destinataire ne se tranche jamais. La colonne « destinataire » transforme la matrice en outil actionnable
	« Brique CARNAC qui validera » dans le tableau 1
	Chaque prestation INCLUSE a une brique CARNAC qui la validera techniquement (par exemple, une reprise en sous-œuvre par passes alternées → B-40). Le renvoi à la brique rend la matrice traçable
	Synthèse en 10 lignes
	Une matrice de périmètre sert en réunion de lancement — pas en lecture exhaustive. Les 10 lignes forcent la hiérarchisation
	Les trois natures d'ambiguïté — précision utile :
Nature
	Définition
	Exemple
	Renvoi mutuel
	Deux lots se renvoient la même prestation
	« La charpente s'appuie sur les sommiers BA » — le lot charpente dit « c'est au GO de faire les sommiers », le lot GO dit « c'est au charpentier de prévoir ses appuis »
	Silence
	Aucune pièce ne dit qui fait la prestation
	Le CCTP ne parle pas des réservations pour la VMC — ni le lot GO ni le lot CVC ne les revendique
	Conflit
	Deux pièces s'attribuent la même prestation à des lots différents
	Le CCTP dit que l'isolation du dallage est au lot GO, le DPGF la met au lot isolation
	________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-14
	B-00 (Inventaire)
	L'énoncé de mission reformulé (avec les exclusions explicites)
	B-01 (MPD validée)
	Les décisions de périmètre (les NON NÉCESSAIRE validés)
	B-10 (Audit CCTP)
	Les constats et les lacunes — B-14 les utilise pour construire la matrice
	B-11 (Audit Diagnostic)
	Les interfaces de lots — B-14 les reprend pour la colonne « interface éventuelle »
	B-13 (Contradictions)
	Les contradictions d'interface identifiées — B-14 les intègre dans le tableau 3
	Briques aval
Brique
	Ce qu'elle consomme de B-14
	B-15 (Synthèse des risques)
	Les prestations À TRANCHER — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise)
	B-03 (RDR)
	Les prestations À TRANCHER — B-03 les inscrit en réserves (R-xx) avec destinataire et échéance
	Toutes les briques de calcul
	Les prestations INCLUSES — chaque brique sait ce qu'elle doit produire, et ce qu'elle ne doit pas produire (les EXCLUES)
	T-04 (Demande de complément)
	Les prestations À TRANCHER avec destinataire — T-04 les transforme en demande formelle
	Variables consommées
Code
	Libellé
	Statut dans B-14
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	DOC-04
	CCTP / pièces contractuelles
	BLOQUANTE (pour le tableau 1 et 2)
	Variables produites
B-14 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (matrice de périmètre) qui alimente B-15, B-03 et T-04.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes, exclusions CARNAC
	00_MASTER.md
	Dictionnaire de variables
	DOC-04, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-14, vous devez valider les prestations À TRANCHER avant transmission à la MOE. Une prestation que vous acceptez implicitement (parce qu'elle est « À TRANCHER » et que vous ne la contestez pas) devient la vôtre, même si le CCTP ne la prescrit pas. C'est votre responsabilité de contester les prestations que vous ne voulez pas exécuter.
Cas particulier — pas de DPGF ou de décomposition en lots : si le marché ne comporte pas de DPGF (décomposition du prix global et forfaitaire) ni de décomposition en lots, B-14 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'absence dans la synthèse. La matrice est construite sur le CCTP seul, avec les limites que cela implique (certaines prestations ne peuvent pas être attribuées sans ambiguïté).
Cas particulier — prestation INCLUSE avec prescription incomplète : si le CCTP prescrit une prestation (par exemple, la reprise en sous-œuvre de la passerelle château) mais sans en préciser les modalités techniques, la prestation est INCLUSE et elle porte un « point à lever » (colonne 5 du tableau 1). Elle n'est pas À TRANCHER — elle est à nous, mais sa prescription est incomplète.
Cas particulier — prestation EXCLUE qui impacte nos travaux : si une prestation est EXCLUE (par exemple, la charpente bois n'est pas dans notre marché) mais que son exécution impacte nos ouvrages (les appuis de charpente sur nos sommiers), la prestation est EXCLUE et elle porte une « interface éventuelle » (colonne 4 du tableau 2). L'interface doit être nommée, pas rejetée.
Cas particulier — prestation hors périmètre CARNAC : le tableau 4 liste les prestations hors périmètre CARNAC (désamiantage, déplombage, curage, espaces verts, dimensionnement protection au feu, fluides, VRD). Elles ne sont ni INCLUSES ni EXCLUES — elles sont hors du périmètre du carnet. Leur attribution à un lot est une décision MOE qui n'a pas à figurer dans la matrice.
Cas particulier — conflit entre deux pièces : si le CCTP attribue une prestation au lot GO et que le DPGF l'attribue à un autre lot, la prestation est À TRANCHER (nature : conflit). B-14 liste les deux pièces et le destinataire (MOE). Le modèle ne tranche pas.
Format de sortie attendu : quatre tableaux distincts (INCLUSES, EXCLUES, À TRANCHER, hors périmètre CARNAC), suivis d'une synthèse en 10 lignes maximum.
Consignation : la matrice B-14 est annexée au RDR (B-03) — les prestations À TRANCHER deviennent des réserves (R-xx) avec destinataire et échéance.
________________

