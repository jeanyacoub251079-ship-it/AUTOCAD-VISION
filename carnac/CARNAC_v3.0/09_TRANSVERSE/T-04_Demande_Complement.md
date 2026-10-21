Fichier 09_TRANSVERSE/T-04_Demande_Complement.md — CARNAC v3.0
________________


T-04 — PROMPT DE DEMANDE DE COMPLÉMENT
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | Transverse — à tout moment |
| Brique précédente | B-04 (PTD) — ou toute brique qui identifie une donnée bloquante manquante |
| Brique suivante | Retour à la brique concernée (B-40 à B-50) une fois la réponse obtenue |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | RDR (points ouverts), briques suspendues, MPD (variables bloquantes) |
| Sortie unique | Demande de complément formelle à la MOE / au BET / au MOA, structurée et datée, avec échéance et conséquence de non-réponse, + mise à jour du RDR |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Aspect | Point ouvert au RDR (B-03) | Demande de complément (T-04) |
| --- | --- | --- |
| Objet | Constater un point ouvert | Le transformer en demande formelle à un destinataire |
| Forme | Ligne de tableau | Courrier structuré et daté |
| Destinataire | Mentionné | Explicitement adressé |
| Échéance | Mentionnée | Explicite et opposable |
| Conséquence | Implicite | Explicite (« si non-réponse, alors… ») |
| Traçabilité | Au RDR | Au RDR + courrier envoyé |

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
- N'oublie aucun point ouvert **légitime** : chaque point du RDR qui passe le test des trois conditions (§ v3.0.1) a sa demande ; les autres sont **clos comme non adressés**, pas relancés.
- Ne produis pas de demande sans consignation au RDR : une demande non consignée n'est pas opposable.
- **v3.0.1 — Ne rédige aucune demande qui échoue au test des trois conditions** (addendum A1) : (1) donnée absente après épuisement `V14` ; (2) nécessaire à un ouvrage **de notre mission** ; (3) destinataire = celui à qui la pièce est adressée. Interdit : arrêté termites / état des abouts / PV de réception si le programme (CCTP + archi + EVEN) ne prescrit pas l'intervention ; interdit : relancer MOA/MOE sur désamiantage, déplombage, cantonnements, PGC.


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

| Clause | Pourquoi |
| --- | --- |
| Conséquence de non-réponse obligatoire | Une demande sans conséquence (« merci de fournir le G2 ») est une demande qui ne se traite pas. La conséquence (« la brique B-40 reste suspendue, le livrable de fondations ne peut pas être émis ») est ce qui déclenche la réponse — elle rend le destinataire responsable du retard |
| Échéance obligatoire | Une demande sans échéance se traite quand le destinataire a le temps — c'est-à-dire tard. L'échéance rend la demande prioritaire |
| Priorisation URGENTE / IMPORTANTE / DE SUIVI | Sans priorisation, toutes les demandes sont traitées au même niveau, ce qui revient à traiter les urgentes trop tard. La priorisation permet au destinataire de savoir ce qui bloque et ce qui peut attendre |
| Consignation au RDR | Une demande orale ou par mail non consignée n'est pas opposable. La consignation au RDR transforme la demande en trace formelle — c'est ce qui vous protège en cas de litige |
| Chaque point du RDR = une demande | Un point du RDR sans demande est un point qui reste ouvert indéfiniment. La correspondance stricte point ↔ demande garantit que rien n'est oublié |
| Demande précise (pas vague) | Une demande vague (« fournir les données manquantes ») ne permet pas au destinataire de savoir quoi fournir. Une demande précise (« fournir q_adm ELS selon NF P 94-261, référence SOL-01 du RDR ») permet une réponse rapide |
| Forme respectée (en-tête, corps, clôture, signature) | Un courrier sans forme n'est pas un courrier — c'est un message. La forme (en-tête, date, destinataire, signature) rend la demande officielle — elle peut être produite en justice si nécessaire |
| Clôture avec accusé de réception | L'accusé de réception est la preuve que la demande a été reçue. Sans lui, le destinataire peut nier avoir reçu la demande — l'accusé est votre protection |
| « Ne mélange pas URGENTES et DE SUIVI » | Un courrier qui mélange les urgentes et les demandes de suivi dilue les urgentes — le destinataire traite tout au même niveau, et les urgentes ne sont pas traitées en priorité. Les séparer rend la demande lisible |
| « Ne produis pas de demande sans consignation au RDR » | Une demande sans consignation est une demande « dans le vide » — elle n'est pas traçable, elle ne peut pas être suivie, elle ne peut pas être opposée en cas de litige |

Les trois niveaux de priorité — précision utile :

| Priorité | Définition | Exemple |
| --- | --- | --- |
| URGENTE | Bloque la remise d'un livrable majeur ou l'engagement de la phase suivante | q_adm manquante — bloque le livrable de fondations |
| IMPORTANTE | Bloque une partie de la production mais n'empêche pas les autres briques | Section d'une panne existante non sondée — bloque la vérification de la charpente, mais les autres briques tournent |
| DE SUIVI | À traiter avant l'exécution, mais pas avant la remise des études | Niveau d'assise exact des fondations — à préciser à l'ouverture des fouilles, pas avant |

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

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les variables BLOQUANTE — T-04 les cite comme objets de demande |
| B-03 (Registre des décisions) | Les réserves (Section 2) — T-04 transforme les réserves en demande formelle à la MOE / BET / MOA |
| B-04 (Plan de travail dégradé) | Les briques suspendues et les voies d'obtention — T-04 transforme ces informations en demande formelle à la MOE / BET / MOA |
| B-10 (Audit critique du CCTP) | Les points à lever avec destinataire — T-04 transforme ces points en demande formelle à la MOE / BET / MOA |
| B-11 (Audit du diagnostic structure) | Les points à lever avec destinataire — T-04 transforme ces points en demande formelle |
| B-12 (Audit des pièces géotechniques) | La recommandation de mission — T-04 transforme cette recommandation en demande formelle à la MOA |
| B-14 (Clarification du périmètre) | Les prestations À TRANCHER avec destinataire — T-04 les transforme en demande formelle |
| B-15 (Fiche de synthèse) | Les risques avec responsable et échéance — T-04 les transforme en demande formelle à la MOE / BET / MOA |
| B-24 (Vérification d'éléments existants non) | Les essais à commander — T-04 les transforme en demande formelle à la MOA |
| B-41 (Fondations profondes) | Les recommandations de mission — T-04 les transforme en demande formelle à la MOA |
| B-72 (Journal de clôture) | Les points ouverts (verrous, réserves, décisions en attente) — T-04 les transforme en demandes formelles à la MOE/BET/MOA |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les demandes consignées (statut envoyée / en attente / répondue) — le RDR est mis à jour |
| B-40 (Fondations superficielles) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-41 (Fondations profondes) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-42 (Verticaux BA) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-43 (Planchers et dallages) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-44 (Charpente bois) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-45 (Structure métallique) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-46 (Maçonnerie : vérification) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-47 (Escaliers) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-48 (Prédalles et planchers préfabriqués) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-49 (Linteaux et seuils) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-50 (Assemblages et ancrages) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-72 (Journal de clôture) | Les demandes non répondues à la date de clôture — B-72 les cite dans les points ouverts |

Variables consommées

| Code | Libellé | Statut dans T-04 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE (T-04 ne peut pas produire de demande sans la liste des verrous) |
| Toutes les variables BLOQUANTE de la FDC | Selon la variable | BLOQUANTE (chaque variable bloquante doit être l'objet d'une demande) |

Variables produites
T-04 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (demande formelle + tableau de synthèse + RDR mis à jour) qui alimente le RDR, la brique concernée et B-72.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, DEC-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).