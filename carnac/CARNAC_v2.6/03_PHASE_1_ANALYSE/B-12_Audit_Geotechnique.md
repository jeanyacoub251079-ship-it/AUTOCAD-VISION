Fichier 03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md — CARNAC v2.6
________________


B-12 — AUDIT DES PIÈCES GÉOTECHNIQUES
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
	B-10 (Audit CCTP), B-11 (Audit Diagnostic) — ou la première brique exécutable selon le PTD
	Brique suivante
	B-13 (Contradictions), B-40 (Fondations — si les données sont suffisantes)
	Modes d'appel
	COMPLET (rapport fourni et adapté) · PARTIEL-DÉCLARÉ (rapport fourni mais niveau de mission insuffisant : on signale l'écart et on poursuit) · SANS OBJET (MPD a statué que les fondations ne sont ni modifiées ni sollicitées)
	Entrées lues
	DOC-06 (rapport géotechnique), MPD validée, énoncé de mission
	Sortie unique
	Audit : données disponibles + adéquation aux besoins + données manquantes + recommandation de mission
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-10 et B-11, ou en parallèle si le PTD le permet. B-12 est la brique d'audit des pièces géotechniques — elle est indispensable si le projet comporte des fondations à concevoir ou à vérifier.
Ce que vous fournissez à l'IA : le rapport géotechnique (DOC-06), la MPD validée (B-01), l'énoncé de mission (B-00). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * le niveau de mission (G1/G2/G3) et son adéquation à nos besoins ;
   * les données disponibles et leur adéquation (exploitable / insuffisante / ambiguë) ;
   * les données manquantes et leur impact sur nos calculs ;
   * la recommandation de mission complémentaire (G3, G4, essais) ;
   * la décision de commander ou non cette mission.
Point de vigilance : B-12 ne retient aucune valeur de calcul. Elle cite ce que le rapport géotechnique fournit (q_adm, stratigraphie, essais), elle contrôle l'adéquation de ces valeurs à nos besoins, mais elle ne choisit jamais une valeur à la place du géotechnicien. La distinction est capitale : le géotechnicien engage sa responsabilité sur les valeurs qu'il fournit dans le cadre de sa mission G2/G3. Si nous retenons une valeur de notre propre initiative, nous engageons la nôtre — sans en avoir les moyens.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : effectuer l'audit critique des pièces géotechniques de l'opération {{ID-01}} — {{ID-02}}. Tu ne retiens aucune valeur de calcul : tu cites ce que dit le rapport, tu évalues son adéquation à NOS besoins, et tu identifies ce qui manque.


MÉTHODE
1. Identifie la mission : G1 / G2 (AVP / PRO) / G3, ou combinaison. Cite la référence de la norme NF P 94-500 et le niveau de mission déclaré dans le rapport.
2. Identifie les conditions de validité : date, nombre de sondages, emprise couverte, profondeur d'investigation, hypothèses de calcul retenues par le géotechnicien.
3. Liste les données disponibles, en les rattachant à un paragraphe ou un tableau du rapport (référence exacte).
4. Compare ces données à NOS besoins (dictionnaire CARNAC, famille SOL) et identifie :
   - les données fournies et directement exploitables ;
   - les données fournies mais insuffisantes (valeur unique sans fourchette, absence de méthode de calcul, etc.) ;
   - les données manquantes.
5. Évalue l'adéquation du niveau de mission à NOS besoins : un G2 AVP est-il suffisant pour nos calculs d'exécution ? Une G3 est-elle nécessaire ?
6. Identifie les conditions de validité qui ne sont plus remplies (date, emprise, hypothèses).


INTERDICTIONS
- Ne retiens aucune valeur de calcul : cite ce que dit le rapport, jamais une valeur « retenue ».
- Ne propose aucune hypothèse de repli.
- Ne décide pas à la place de la MOA si une mission complémentaire doit être commandée : tu la recommandes, avec sa base normative, et tu listes les conséquences si elle ne l'est pas.
- Ne déclare pas le rapport « suffisant » sans le confronter à chacun des codes de la famille SOL du dictionnaire.


SORTIE
Trois tableaux obligatoires.


Tableau 1 — Données disponibles et adéquation
Code CARNAC | Libellé | Valeur citée | Unité | Référence rapport (§, tableau, page) | Adéquation (exploitable / insuffisante / ambiguë)


Tableau 2 — Données manquantes et impact
Code CARNAC | Libellé | Impact sur nos calculs | Brique suspendue | Voie d'obtention proposée (essai / mission complémentaire / décision MOA)


Tableau 3 — Recommandation de mission
Mission proposée (G2 PRO / G3 / essais complémentaires) | Base normative (NF P 94-500 et références) | Justification | Conséquence si non commandée (briques suspendues, réserves à porter)


Puis une synthèse de 8 lignes maximum :
- niveau de mission actuel et suffisance ;
- les trois données dont l'absence bloque le plus nos calculs ;
- la recommandation de mission complémentaire et son impact planning.


CRITÈRE D'ACCEPTATION
L'audit est accepté si :
- le niveau de mission est identifié avec sa référence normative ;
- chaque donnée citée est rattachée à un paragraphe ou tableau du rapport ;
- chaque donnée manquante est rattachée à son code CARNAC et à sa brique suspendue ;
- la recommandation de mission cite sa base normative et la conséquence de sa non-commande ;
- aucune valeur de calcul n'a été retenue par toi ;
- la synthèse tient en 8 lignes.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	« Tu ne retiens aucune valeur de calcul »
	C'est la clause centrale de B-12. Le rapport géotechnique donne des valeurs de calcul au sens de la mission G2/G3 : nous les exploitons, nous ne les choisissons pas. Cette clause interdit la dérive « je retiens 0,25 MPa parce que la fourchette va de 0,20 à 0,30 » — qui fait perdre un litige (le géotechnicien engage sa responsabilité sur les valeurs qu'il fournit, pas nous)
	« un G2 AVP est-il suffisant pour nos calculs d'exécution ? »
	C'est le cas Flora : un G2 AVP ne suffit pas à des calculs EXE ; une G3 est nécessaire. La question est posée explicitement, pas laissée à l'appréciation du modèle. Sans cette question, un rapport G2 AVP est souvent accepté tel quel — et les calculs EXE sont faits sur des données qui n'ont pas été validées pour cet usage
	« Tu ne décides pas à la place de la MOA si une mission complémentaire doit être commandée »
	La commande d'une mission G3/G4 est une décision MOA, pas une décision de l'entreprise GO. Le rôle de l'audit est de la recommander, pas de la décider. Un modèle qui décide à la place de la MOA crée une décision implicite non opposable
	« Conséquence si non commandée »
	Le tableau 3 documente ce qui restera suspendu si la MOA ne commande pas la mission complémentaire — c'est ce qui vous protège en cas de litige. Si la MOA ne commande pas et que les fondations s'avèrent sous-dimensionnées, vous avez tracé que vous aviez recommandé la mission
	« Ne déclare pas le rapport suffisant sans confronter chacun des codes SOL »
	Empêche la conclusion « le G2 est là, on y va » qui masque les données manquantes. Un rapport peut sembler complet à la première lecture et manquer d'une donnée critique (par exemple, l'agressivité XA du sol, ou la nappe phréatique)
	« Ne propose aucune hypothèse de repli »
	Une hypothèse de repli est une décision RDR (PARTIEL-DÉCLARÉ), pas une proposition d'audit. Si vous décidez de retenir une valeur plancher, c'est une décision RDR avec auteur, date et justification — pas une initiative du modèle
	« chaque donnée citée est rattachée à un paragraphe ou tableau du rapport »
	Verrou V2 — une valeur sans référence n'est pas vérifiable. En cas de litige sur une valeur, on doit pouvoir dire « cette valeur figure au §3.2 tableau 4 page 12 du rapport GEOEXPERTS 25.13646 »
	Synthèse en 8 lignes
	Un audit exhaustif sans synthèse n'est pas exploitable en réunion de lancement. Les 8 lignes forcent le modèle à hiérarchiser
	Les trois adéquations possibles — précision utile :
Adéquation
	Définition
	Conséquence
	Exploitable
	La donnée est fournie avec une valeur claire, une méthode, et une référence explicite dans le rapport
	Peut être utilisée en mode COMPLET par B-40
	Insuffisante
	La donnée est fournie mais ne permet pas de conclure (valeur unique sans fourchette, absence de méthode, conditions de validité dépassées)
	Nécessite une décision RDR (PARTIEL-DÉCLARÉ) ou une mission complémentaire
	Ambiguë
	La donnée est fournie mais avec une incertitude (fourchette large, méthode non justifiée, hypothèse non explicite)
	Nécessite une clarification auprès du géotechnicien
	________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-12
	B-00 (Inventaire)
	La référence exacte du rapport géotechnique (fichier + folio + indice)
	B-01 (MPD validée)
	Le statut de DOC-06 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) et des variables SOL-01 à SOL-08
	B-03 (RDR)
	Les décisions déjà prises (par exemple, une décision de périmètre qui précise que les fondations ne sont pas concernées)
	Briques aval
Brique
	Ce qu'elle consomme de B-12
	B-13 (Contradictions)
	Les écarts entre les données géotechniques et les autres pièces
	B-15 (Synthèse des risques)
	Les données manquantes et les recommandations de mission — B-15 les intègre dans le registre des risques
	B-40 (Fondations superficielles)
	Les valeurs exploitables (SOL-01, SOL-02, SOL-03, SOL-05) — B-40 ne peut pas s'exécuter en COMPLET si ces valeurs sont insuffisantes ou ambiguës
	B-41 (Fondations profondes)
	Les valeurs relatives aux pieux — B-41 les contrôle et recommande une mission G3/G4 si nécessaire
	T-04 (Demande de complément)
	La recommandation de mission — T-04 transforme cette recommandation en demande formelle à la MOA
	Variables consommées
Code
	Libellé
	Statut dans B-12
	DOC-06
	Rapport géotechnique
	BLOQUANTE
	SOL-01
	Contrainte admissible ELS
	BLOQUANTE (pour B-40, pas pour B-12 qui l'audite)
	SOL-08
	Mission géotechnique disponible (G1/G2/G3)
	BLOQUANTE
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-12 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (audit géotechnique) qui alimente B-13, B-15, B-40, B-41 et T-04.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	DOC-06, SOL-01 à SOL-08, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-12, vous devez décider si la mission complémentaire doit être commandée. C'est une décision MOA, mais c'est vous qui documentez la conséquence de la non-commande. Un audit qui recommande une G3 sans documenter la conséquence ne vous protège pas en cas de litige.
Cas particulier — G2 AVP insuffisant : si le rapport est un G2 AVP (avant-projet), il ne suffit pas pour des calculs d'exécution. B-12 recommande une G2 PRO ou une G3, avec la base normative (NF P 94-500) et la conséquence de la non-commande. C'est exactement le cas Flora : un G2 AVP sans G3 ne permet pas de conclure sur les fondations.
Cas particulier — rapport sans valeur de calcul : si le rapport géotechnique fournit des données (stratigraphie, essais) mais pas de valeurs de calcul (q_adm, tassements), B-12 signale que les données sont insuffisantes pour l'usage prévu (calculs EXE) et recommande une mission complémentaire. Un rapport de reconnaissance sans synthèse géotechnique n'est pas exploitable pour des calculs.
Cas particulier — conditions de validité dépassées : si le rapport a plus de 5 ans, ou si l'emprise a changé depuis, ou si des travaux ont modifié le sol, B-12 signale les conditions de validité qui ne sont plus remplies. Un rapport valide mais non applicable est aussi dangereux qu'un rapport absent.
Cas particulier — absence de géotechnique : si la MPD a statué que les fondations ne sont ni modifiées ni sollicitées (superstructure seule), B-12 s'appelle en mode SANS OBJET — avec une ligne de justification. Elle ne signale aucune donnée manquante : ce serait contraire à la décision de périmètre.
Format de sortie attendu : trois tableaux distincts (données disponibles, données manquantes, recommandation de mission), suivis d'une synthèse en 8 lignes maximum. Chaque donnée citée est rattachée à un paragraphe ou tableau du rapport.
Consignation : l'audit B-12 est annexé au RDR (B-03) — il documente la lecture du rapport géotechnique et alimente les réserves (R-xx) pour les données manquantes et les recommandations de mission.
________________

