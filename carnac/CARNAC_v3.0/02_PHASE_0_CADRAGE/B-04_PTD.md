Fichier 02_PHASE_0_CADRAGE/B-04_PTD.md — CARNAC v3.0
________________


B-04 — PLAN DE TRAVAIL DÉGRADÉ
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 0 — Cadrage et qualification |
| Brique précédente | B-03 (RDR) |
| Brique suivante | B-10 (Audit CCTP) — ou la première brique exécutable selon le PTD |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | MPD validée (B-01), FDC (B-02), RDR (B-03), graphe de dépendances (colonne « Bloque » du dictionnaire) |
| Sortie unique | PTD complet : briques suspendues, exécutables, paramétriques + impact planning |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-03, avant de lancer la phase 1. Puis à chaque blocage en cours de projet, pour régénérer le plan de travail.
Ce que vous fournissez à l'IA : la MPD validée, la FDC, le RDR, le dictionnaire de variables. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}.
Ce que vous validez à la sortie :
   * la liste des briques suspendues (et la donnée qui les bloque) ;
   * la liste des briques exécutables immédiatement ;
   * la liste des briques exécutables en PARAMÉTRIQUE (avec la mention de ce qui ne sera pas produit) ;
   * l'impact planning.
Ce que le PTD vous apporte concrètement : il répond à votre question du début — « si une donnée manque, comment continuer ? ». Le PTD vous dit exactement ce qui est faisable, sans que vous ayez à le déduire. C'est ce qui vous permet de travailler malgré les blocages, sans jamais produire un livrable exécutable faux.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire le Plan de Travail Dégradé (PTD) de l'opération {{ID-01}}, à partir de la MPD validée, de la FDC, du RDR et du graphe de dépendances. Le PTD s'applique à chaque blocage, y compris en cours de projet.


RÈGLES
1. Blocage local, jamais global. Une donnée bloquante manquante suspend UNIQUEMENT les briques qui la consomment (colonne « Bloque » du dictionnaire).
2. Tout ce qui n'est pas en aval d'une donnée manquante reste exécutable : tu le listes.
3. Aucun livrable exécutable n'est émis en attente d'une donnée. Les livrables issus d'un mode PARAMÉTRIQUE sont filigranés « PROVISOIRE — EN ATTENTE DE [donnée] » et suffixés _P.
4. Tu ne déclares jamais une brique SANS OBJET : c'est la MPD qui statue.


SORTIE
Trois tableaux obligatoires :


Tableau 1 — Briques suspendues
Brique | Donnée bloquante (code) | Voie d'obtention (relevé / essai / mission G / décision MOA) | Responsable | Échéance


Tableau 2 — Briques exécutables immédiatement
Brique | Mode (COMPLET / INTERNE-GO) | Motif (aucune dépendance à la donnée manquante)


Tableau 3 — Briques exécutables en PARAMÉTRIQUE
Brique | Donnée laissée en symbole | Forme littérale possible | Ce qui ne sera PAS produit (valeur retenue, livrable exécutable, DXF)


Puis un paragraphe de synthèse :
- ce qui reste bloqué tant que la donnée n'est pas obtenue ;
- l'impact sur la date de remise des livrables exécutables ;
- la liste des livrables PARAMÉTRIQUE qui pourront être émis immédiatement, avec leur filigrane.


INTERDICTIONS
- Ne propose aucune valeur de repli pour débloquer une brique.
- Ne déclare aucune brique SANS OBJET.
- Ne propose aucun livrable exécutable en attente.
- Ne confonds pas « brique suspendue » et « projet suspendu ».


CRITÈRE D'ACCEPTATION
Le PTD est accepté si :
- chaque brique suspendue identifie la donnée qui la bloque ;
- chaque brique exécutable est justifiée (aucune dépendance à la donnée manquante) ;
- chaque PARAMÉTRIQUE précise la forme littérale possible et ce qui ne sera pas produit ;
- aucune valeur de repli n'a été proposée ;
- aucune brique n'a été déclarée SANS OBJET par le modèle ;
- la synthèse mentionne explicitement l'impact planning.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} par le code projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Blocage local, jamais global » | Verrou V11 — c'est votre règle : « on peut toujours travailler sur d'autres points ». Un modèle sans cette consigne a tendance à suspendre tout le projet dès qu'une donnée manque. Le PTD au contraire vous montre ce qui reste faisable |
| « tu ne déclares jamais une brique SANS OBJET » | Le SANS OBJET découle de la MPD validée, pas du PTD. Un PTD qui déclare une brique SANS OBJET parce qu'elle est bloquée est une erreur : la brique n'est pas « sans objet », elle est suspendue — et elle redeviendra exécutable dès que la donnée arrivera |
| « Ne confonds pas brique suspendue et projet suspendu » | Empêche le réflexe « tout s'arrête » que produirait un modèle sans cette consigne. Le PTD est précisément l'outil qui prouve que le projet continue malgré le blocage |
| « Aucun livrable exécutable en attente » | Un DXF « au cas où » finit toujours par être exécuté. Un livrable PARAMÉTRIQUE doit être filigrané et suffixé _P pour qu'on ne puisse pas le confondre avec un livrable exécutable |
| « chaque PARAMÉTRIQUE précise… ce qui ne sera pas produit » | Un livrable PARAMÉTRIQUE ne produit pas la même chose qu'un livrable COMPLET. Il faut le dire explicitement : pas de valeur retenue, pas de DXF exécutable, pas de plan à diffuser. Sinon, on croit avoir un livrable complet alors qu'on n'a qu'une note suspendue |
| « Impact sur la date de remise » | Le PTD n'est pas qu'un tableau technique — c'est un outil de pilotage de délai. Il vous permet de dire à la MOA : « si vous fournissez le G3 le 15/11, le livrable de fondations sera remis le 22/11 ; sinon, il sera remis sous forme paramétrique le 8/11, mais ne sera pas exécutable. » |
| « Ne propose aucune valeur de repli » | La valeur de repli est une décision RDR (PARTIEL-DÉCLARÉ), jamais une proposition du modèle. Un modèle qui propose une valeur de repli transforme un blocage en décision implicite |

Les trois niveaux de dégradation — précision utile :

| Situation | Conséquence sur la brique | Livrable produit |
| --- | --- | --- |
| Toutes les données bloquantes disponibles | Mode COMPLET | Livrable intégral, exécutable après visa |
| Une donnée manque, une décision RDR existe | Mode PARTIEL-DÉCLARÉ | Livrable avec valeur déclarée, mention de l'auteur et de la date |
| Une donnée manque, aucune décision | Mode PARAMÉTRIQUE | Livrable filigrané, non exécutable, formule littérale |

Ce que le PTD n'est pas : le PTD n'est pas un plan de production au sens planning détaillé (qui relève de la conduite de projet). C'est un instantané des briques qui peuvent tourner et de celles qui sont bloquées, à un moment donné. Il est régénéré à chaque blocage.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Les variables BLOQUANTE et les briques suspendues — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-02 (Fiche de données) | Les VERROU et les briques suspendues — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-03 (Registre des décisions) | Les verrous (Section 3) et les réserves (Section 2) — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-13 (Détection et qualification) | Les briques suspendues par une contradiction BLOQUANTE — B-04 les intègre au plan de travail dégradé |
| B-24 (Vérification d'éléments existants non) | Les éléments en attente de données et les essais nécessaires — B-04 les intègre dans le plan de travail dégradé |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-72 (Journal de clôture) | L'historique des PTD — B-72 liste les points ouverts qui restent à traiter après remise |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les briques suspendues et les voies d'obtention — T-04 transforme ces informations en demande formelle à la MOE / BET / MOA |

Variables consommées

| Code | Libellé | Statut dans B-04 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| DEC-03 | Verrous ouverts | BLOQUANTE (B-04 ne peut pas produire de PTD sans la liste des verrous) |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | BLOQUANTE (dès B-01) |

Variables produites
B-04 ne produit pas de variable au sens du dictionnaire : sa sortie est le PTD lui-même, qui est un document de pilotage, pas une valeur.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes (en particulier V11 et V12) | 00_MASTER.md |
| Dictionnaire de variables | Colonne « Bloque » pour chaque variable | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain : à la sortie de B-04, vous devez vérifier que :
   1. chaque brique suspendue l'est pour une vraie raison (une donnée bloquante manquante, pas une décision implicite du modèle) ;
   2. chaque brique exécutable l'est effectivement (aucune dépendance cachée à la donnée manquante) ;
   3. chaque brique PARAMÉTRIQUE précise bien ce qui ne sera pas produit (pas de valeur, pas de DXF exécutable).
Cas particulier — blocage en cours de projet : si une donnée qui était disponible devient manquante (par exemple, une valeur est retirée par la MOA), ou si une donnée NON BLOQUANTE se révèle BLOQUANTE (requalification V12), le PTD doit être régénéré. Il ne s'agit pas d'une nouvelle brique B-04 — c'est la même brique, rappelée avec les nouvelles entrées.
Cas particulier — blocage multiple : si plusieurs données bloquantes manquent simultanément, le PTD les liste toutes dans le tableau 1, avec pour chacune la brique suspendue correspondante. Il ne fusionne pas les blocages : chaque donnée manquante est une ligne distincte.
Cas particulier — brique INTERNE-GO : une brique INTERNE-GO (par exemple, B-20 quand AC-03 est À PRODUIRE PAR GO) n'est pas une brique suspendue — c'est une brique exécutable, mais dans un mode de conception (pas d'exécution). Le PTD la liste dans le tableau 2 (briques exécutables immédiatement), avec le mode INTERNE-GO et le motif « conception à produire par nos soins ».
Format de sortie attendu : trois tableaux distincts (briques suspendues, briques exécutables, briques PARAMÉTRIQUE), suivis d'un paragraphe de synthèse en 3 points (ce qui reste bloqué, impact planning, livrables PARAMÉTRIQUE émis immédiatement).
Consignation : le PTD est annexé au RDR (B-03) — il est le document qui prouve que vous avez exécuté tout ce qui était faisable malgré les blocages. En cas de litige sur un retard, le PTD est votre preuve.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).