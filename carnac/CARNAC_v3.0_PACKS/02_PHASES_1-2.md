<!-- PACK CARNAC v3.0 — PACK 02 — PHASES 1 ET 2 : SOCLE GÉOMÉTRIQUE PUIS AUDIT CROISÉ (B-30, B-32, B-31 puis B-10 à B-15) -->

# PACK 02 — PHASES 1 ET 2 : SOCLE GÉOMÉTRIQUE PUIS AUDIT CROISÉ (B-30, B-32, B-31 puis B-10 à B-15)

**Quand coller ce pack** : Une fois le cadrage validé, avant toute conception.

**Ce qu'il contient** : B-30 calage multi-sources · B-32 vue nettoyée différentielle · B-31 preuve de superposition · puis B-10 à B-15 (audits, contradictions, périmètre de lot, risques et Pré-Audit Flash).

**Note d'usage** : Ordre imposé par le carnet : le calage et le nettoyage AVANT l'audit. Ne permutez pas les fiches dans ce pack.

**Prérequis** : le pack `00_SOCLE.md` doit être collé avant celui-ci, dans la même discussion.

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
**[Début du fichier : 03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md]**

Fichier 03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md — CARNAC v3.0
________________


B-10 — AUDIT CRITIQUE DU CCTP ET DES PIÈCES CONTRACTUELLES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-04 (PTD) — ou la première brique exécutable selon le PTD |
| Brique suivante | B-13 (Contradictions) — via B-14 (Périmètre de lot) si applicable |
| Modes d'appel | COMPLET (CCTP fourni) · PARTIEL-DÉCLARÉ (CCTP partiel ou non indicé : on signale l'indice manquant et on poursuit sur le périmètre disponible) · SANS OBJET (marché en conception-réalisation sans CCTP : à statuer par la MPD) |
| Entrées lues | DOC-04 (CCTP), DOC-03 (plans BET), énoncé de mission (B-00), MPD validée (B-01) |
| Sortie unique | Audit article par article + quatre tableaux (constats / lacunes / contradictions internes / points à lever) |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Clause | Pourquoi |
| --- | --- |
| « Tu produis un audit, pas une conception » | Un audit qui propose des solutions devient une conception implicite, non tracée, non visée — et qui engage votre responsabilité sans validation. La frontière avec B-20 (conception) et B-40 à B-50 (calculs) doit être nette : l'audit constate, la conception décide |
| « Tu ne proposes aucune solution technique, tu ne dimensionnes rien » | Frontière nette avec B-20/B-40 et suivantes : c'est la conception qui décide, pas l'audit. Sans cette clause, un modèle glisse vers la conception — et on se retrouve avec des décisions non tracées |
| « Tu ne cites aucune prescription de mémoire » | Verrou V2 — le CCTP est trop souvent « à peu près connu ». La citation exacte (numéro d'article ou intitulé) est la seule défense en cas de litige sur un périmètre. Un constat sans référence est un constat inopposable |
| « Tu ne qualifies pas un point de résolu parce qu'une pièce ultérieure semble le couvrir » | C'est la faille exacte de la conversation d'origine : la contradiction XC2/35 vs XA3/50 a été « résolue » par un arbitrage implicite. Cette clause interdit ce type de résolution silencieuse — le point reste listé, c'est vous qui tranchez (et la décision va au RDR) |
| « Destinataire + urgence » dans le tableau 4 | Un point à lever sans destinataire ne se lève jamais ; un point sans urgence est traité trop tard. Les deux colonnes sont indispensables pour que l'audit soit actionnable, pas seulement descriptif |
| « Brique concernée (B-40 à B-50) » dans le tableau 2 | Chaque lacune du CCTP a une conséquence sur une brique de calcul précise. Nommer la brique évite les lacunes « orphelines » que personne ne traite |
| « Synthèse en 10 lignes » | Force la hiérarchisation — un audit exhaustif sans synthèse n'est pas exploitable en réunion de lancement. Les 10 lignes forcent le modèle à choisir les trois points les plus importants |
| « Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes » | Verrou V4 — pas de livraison partielle silencieuse. Un audit partiel présenté comme complet est plus dangereux qu'un audit absent : il donne l'illusion que le CCTP est propre |

Les trois catégories de constats — précision utile :

| Catégorie | Définition |
| --- | --- |
| Traitement en aval | CONSTAT |
| Ce que le CCTP prescrit effectivement | Va en FDC (B-02) si c'est une valeur exploitable ; va en B-14 si c'est un périmètre |
| LACUNE | Ce que le CCTP aurait dû prescrire et ne prescrit pas |
| Va en B-13 (si c'est une contradiction avec une autre pièce) ou en réserve R-xx (RDR) | CONTRADICTION INTERNE |
| Deux articles ou deux pièces qui se contredisent | Va en B-13 pour qualification (gravité × nature) |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | L'inventaire des pièces, la référence exacte du CCTP (fichier + folio + indice), l'énoncé de mission reformulé |
| B-01 (Proposition de la matrice) | Le statut de DOC-04 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) |
| B-03 (Registre des décisions) | Les décisions déjà prises (par exemple, une décision de périmètre qui précise ce qui est dans le lot GO) |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-13 (Détection et qualification) | Les contradictions internes détectées par B-10 — B-13 les qualifie (gravité × nature) et les rattache aux briques |
| B-14 (Clarification du périmètre) | Les constats et les lacunes — B-14 construit la matrice INCLUS/EXCLU/À TRANCHER à partir de ces informations |
| B-15 (Fiche de synthèse) | Les points à lever et les prescriptions à confirmer — B-15 les intègre dans le registre des risques |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les points à lever avec destinataire — T-04 transforme ces points en demande formelle à la MOE / BET / MOA |

Variables consommées

| Code | Libellé | Statut dans B-10 |
| --- | --- | --- |
| DOC-04 | CCTP / pièces contractuelles | BLOQUANTE |
| DOC-03 | Plans BET structure (si disponibles) | NON BLOQUANTE (si absents, l'audit est fait sur le CCTP seul) |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| ID-02 | Intitulé de l'opération | BLOQUANTE (pour l'en-tête de sortie) |

Variables produites
B-10 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (audit CCTP) qui alimente B-13, B-14 et B-15.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-04, DOC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Ordre inversé.** L'audit croisé s'exécute désormais **après** le socle géométrique : B-10 lit les plans sur le fond calé et nettoyé (`B-30`, `B-32`), ce qui supprime les contradictions fantômes produites par les cloisons et les doublages.

**Preuve d'épuisement.** Avant d'inscrire une lacune, B-10 produit le journal d'épuisement `V14` : pièces examinées, passages, résultat par pièce. Une lacune non prouvée n'est pas une lacune : c'est une pièce non lue.

---

### 6. COMPLÉMENT v3.0.1 — PRESTATIONS NON ADRESSÉES · CARNET DES FAITS

**Tableau 5 obligatoire (nouveau).** Prestations **lues** dans le CCTP mais **non adressées** au BET d'exécution : désamiantage, déplombage, cantonnements, PGC, PPSPS, modes opératoires entreprise, PV de réception d'ouvrages que le programme ne nous charge pas de vérifier. Pour chacune : article CCTP | constat | **aucune demande `T-04`**.

**Programme vs diagnostic.** Une prescription absente du CCTP **et** des plans archi **et** des plans EVEN n'est pas une lacune de nos études — c'est un ouvrage hors programme. Interdit de la transformer en demande (arrêté termites, état des abouts, PV de renforts existants) si aucune intervention n'est prescrite.

**Carnet des faits.** B-10 alimente le carnet ouvert en B-00 : nature des planchers par zone, matériaux prescrits, neufs vs existants. Une « lacune » qui figure déjà au carnet est une non-conformité de lecture, pas une donnée manquante.
**[Fin de 03_PHASE_1_ANALYSE/B-10_Audit_CCTP.md]**

---

**[Début du fichier : 03_PHASE_1_ANALYSE/B-11_Audit_Diagnostic.md]**

Fichier 03_PHASE_1_ANALYSE/B-11_Audit_Diagnostic.md — CARNAC v3.0
________________


B-11 — AUDIT DU DIAGNOSTIC STRUCTURE EXISTANT
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-10 (Audit CCTP) — ou la première brique exécutable selon le PTD |
| Brique suivante | B-13 (Contradictions), B-14 (Périmètre de lot), B-23 (Exploitation du diagnostic) |
| Modes d'appel | COMPLET (diagnostic fourni et complet) · PARTIEL-DÉCLARÉ (diagnostic partiel, zones non relevées : on signale l'emprise non couverte) · SANS OBJET (bâtiment neuf, aucune pièce existante à diagnostiquer : à statuer par la MPD) |
| Entrées lues | DOC-05 (diagnostic structure), DOC-08 (récolement/DOE), DOC-03 (plans BET sur l'existant), B-00 (inventaire) |
| Sortie unique | Audit du diagnostic : quatre tableaux + liste des données manquantes + points à lever |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-10, ou en parallèle si le PTD le permet. B-11 est la brique d'audit du diagnostic structure de l'existant — elle est indispensable en réhabilitation, et sans objet en neuf.
Ce que vous fournissez à l'IA : le diagnostic structure de l'existant (DOC-05), les plans de récolement ou DOE (DOC-08), les plans BET structure sur l'existant (DOC-03), et l'inventaire (B-00). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * chaque désordre cité à sa source (page, paragraphe, numéro) ;
   * chaque cellule [ANALYSE GO] — c'est votre analyse, pas une reformulation du diagnostic ;
   * chaque prescription du diagnostic reprise, avec la mention « à valider par B-xx » ;
   * les données manquantes pour nos travaux ;
   * les zones non relevées et leur emprise.
Ce que B-11 apporte de spécifique — la distinction à trois niveaux :

| Niveau | Ce que c'est | Source |
| --- | --- | --- |
| CITATION | Ce que le diagnostic affirme, mot pour mot | Le diagnostic (référence exacte) |
| PRESCRIPTION | Ce que le diagnostic préconise comme travaux | Le diagnostic (référence exacte) |
| ANALYSE GO | Ce que vous, ingénieur EXE, en concluez pour nos travaux | Vous (introduit par [ANALYSE GO]) |

Cette distinction est le cœur de B-11 : elle répond directement à la question posée dans la conversation d'origine — « la colonne "Conséquence pour nos travaux" est-elle ton analyse ou celle du dossier ? ». La réponse est désormais sans ambiguïté : c'est une ANALYSE GO, jamais une citation, et elle est préfixée comme telle.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : effectuer l'audit critique du diagnostic structure de l'existant pour l'opération {{ID-01}} — {{ID-02}}. Tu n'acceptes pas les conclusions du diagnostic comme des prescriptions : tu les cites, tu les analyses, et tu distingues TOUJOURS ce que dit le diagnostic de ce que TU en conclus.


DISTINCTION OBLIGATOIRE — TROIS NIVEAUX
1. CITATION DU DIAGNOSTIC : ce que le diagnostic affirme, avec sa référence exacte (page, paragraphe, numéro de désordre). Tu cites, tu ne reformules pas.
2. PRESCRIPTION DU DIAGNOSTIC : ce que le diagnostic préconise comme travaux de renforcement, avec sa référence exacte. Tu cites la prescription, tu ne la reprends pas à ton compte.
3. ANALYSE GO : ce que TOI, ingénieur études d'exécution, tu en conclus pour nos travaux. Cette analyse est TON fait, pas celui du diagnostic. Elle est toujours introduite par la mention « [ANALYSE GO] ».


Toute colonne « conséquence pour nos travaux » est une ANALYSE GO, jamais une citation du diagnostic. Si tu reprends une prescription du diagnostic, tu l'écris : « [PRESCRIPTION DIAGNOSTIC — réf. p. X] », et tu ajoutes la mention « à valider par nos calculs B-xx ».


MÉTHODE
1. Extrais la liste numérotée des désordres, avec leur nature, leur localisation, le niveau de préjudice tel que cité par le diagnostic, et la prescription éventuelle.
2. Pour CHAQUE désordre, distingue :
   - ce qui relève de NOTRE lot (gros œuvre / structure) ;
   - ce qui relève d'un autre lot (charpente, couverture, zinguerie, fluides, menuiseries) ;
   - ce qui reste à trancher (interface entre notre lot et un autre).
3. Identifie ce que le diagnostic ne dit PAS et dont nous avons besoin pour nos travaux : sections des existants, matériaux, essais, sondages, niveaux d'assise, état parasitaire de la charpente, etc.
4. Identifie les zones NON RELEVÉES ou NON COUVERTES par le diagnostic et leur emprise.
5. Vérifie la cohérence entre les désordres décrits et les plans structure existants (les désordres localisés sur les plans correspondent-ils aux désordres décrits ?).
6. Ne propose AUCUN renforcement : tu listes ce qui doit être renforcé, pas comment.


INTERDICTIONS
- Ne reprends aucune prescription du diagnostic comme si elle était la nôtre.
- Ne mélange jamais citation et analyse dans la même cellule.
- N'accepte aucune conclusion du diagnostic sans la citer à sa source.
- Ne propose aucun dimensionnement, aucune section, aucune nuance.
- Ne déclare pas un désordre « hors lot » sans le rattacher à la décomposition en lots du marché.


SORTIE
Quatre tableaux obligatoires.


Tableau 1 — Désordres et analyse GO
N° | Nature du désordre (CITATION, réf. p.) | Niveau de préjudice (tel que cité) | Localisation | Conséquence pour NOS travaux [ANALYSE GO] | Prescription du diagnostic (CITATION, réf. p.) | Lot concerné


Tableau 2 — Prescriptions du diagnostic reprises
N° désordre | Prescription citée (réf. p.) | Ce que cette prescription implique pour nos ouvrages | Briques CARNAC à exécuter pour la valider


Tableau 3 — Données manquantes pour nos travaux
Donnée (code CARNAC) | Ce que le diagnostic aurait dû fournir | Impact sur nos calculs | Brique concernée


Tableau 4 — Points à lever
N° | Objet | Nature (donnée manquante / zone non relevée / interface de lot) | Destinataire (MOE / BET / MOA) | Urgence


Puis une synthèse de 8 lignes maximum :
- les désordres qui impactent le plus nos travaux ;
- les points où le diagnostic est insuffisant pour nos calculs ;
- les interfaces de lots à trancher avant démarrage.


CRITÈRE D'ACCEPTATION
L'audit est accepté si :
- chaque désordre est numéroté et cité à sa source (page/paragraphe) ;
- chaque cellule du tableau 1 distingue explicitement CITATION et ANALYSE GO ;
- chaque prescription du diagnostic reprise est marquée « à valider par B-xx » ;
- les données manquantes sont rattachées à leur code CARNAC et à leur brique ;
- les zones non relevées sont identifiées avec leur emprise ;
- aucun renforcement n'a été proposé par toi-même ;
- la synthèse tient en 8 lignes.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « La colonne "conséquence pour nos travaux" est une ANALYSE GO, jamais une citation » | C'est la réponse directe à votre question du projet Flora. Dans l'analyse initiale, la colonne mélangeait parfois les prescriptions du diagnostic et des analyses personnelles. Ici, la règle est explicite : chaque cellule porte la qualification [CITATION] ou [ANALYSE GO]. Un lecteur ne peut pas confondre ce que dit le diagnostic et ce que vous en concluez |
| « Tu n'acceptes pas les conclusions du diagnostic comme des prescriptions » | Un diagnostic de BET tiers n'est pas un visa : ses prescriptions engagent l'entreprise qui les exécute, pas le BET qui les a écrites. La validation par nos calculs est obligatoire — sans elle, vous exécutez un renforcement sur la seule foi d'un tiers, sans avoir vérifié qu'il est suffisant |
| « à valider par nos calculs B-xx » | Chaque prescription reprise doit être rattachée à une brique CARNAC qui la validera — jamais exécutée sur la seule foi du diagnostic. Le renvoi à B-xx rend la validation traçable |
| « zones non relevées identifiées avec leur emprise » | Point critique dans la conversation d'origine (deux zones « NON RELEVEE » du folio 02) : sans cette identification, on calcule sur des hypothèses qui ne sont pas déclarées. Une zone non relevée est une zone où on ne peut pas conclure — elle doit être signalée comme telle |
| « Ne déclare pas un désordre hors lot sans le rattacher à la décomposition en lots » | Dans le projet Flora, la charpente n'était pas dans le CCTP mais ses appuis conditionnaient nos ouvrages — l'interface doit être nommée, pas rejetée. Un désordre « hors lot » qui impacte nos travaux reste une contrainte pour nous |
| « Ne propose aucun renforcement » | Un renforcement proposé sans calcul est une conception implicite — c'est exactement la faute reprochée au diagnostic EVEN sur certains points. La conception relève de B-20 et B-40 à B-50, pas de l'audit |
| « Ne mélange jamais citation et analyse dans la même cellule » | Une cellule qui mélange citation et analyse est illisible : on ne sait pas qui parle. La distinction force la clarté et rend l'audit opposable |
| Synthèse en 8 lignes | Un audit exhaustif sans synthèse n'est pas exploitable en réunion de lancement. Les 8 lignes forcent le modèle à hiérarchiser |

Les trois niveaux — exemple concret :

| Niveau | Exemple (projet Flora) |
| --- | --- |
| CITATION | « Désordre n° 3 : fléchissement à vue d'œil de la poutre maîtresse (partie Est). Préjudice : important. » — réf. p. 12 du diagnostic EVEN du 24/03/2025 |
| PRESCRIPTION | « Moisage par profilés métalliques obligatoire, avec étaiement provisoire pendant travaux. » — réf. p. 14 du diagnostic EVEN |
| ANALYSE GO | « [ANALYSE GO] Le moisage doit être justifié par nos calculs EC3 + EC5 (B-44 et B-45), en tenant compte de l'interaction bois/métal. La prescription du diagnostic est un principe, pas un dimensionnement : à valider par nos calculs avant exécution. » |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte du diagnostic (fichier + folio + indice), les plans de récolement/DOE |
| B-01 (Proposition de la matrice) | Le statut de DOC-05 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) |
| B-03 (Registre des décisions) | Les décisions déjà prises (par exemple, une décision de périmètre qui précise les lots inclus) |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-13 (Détection et qualification) | Les désordres cités et les données manquantes — B-13 les qualifie et les rattache aux briques |
| B-14 (Clarification du périmètre) | Les interfaces de lots identifiées — B-14 construit la matrice INCLUS/EXCLU/À TRANCHER |
| B-15 (Fiche de synthèse) | Les zones non relevées et les données manquantes — B-15 les intègre dans le registre des risques |
| B-20 (Conception structure GO) | Les désordres cités, les prescriptions — B-20 les utilise pour identifier les renforts |
| B-23 (Exploitation du diagnostic existant) | Les désordres cités et les prescriptions — B-23 les exploite pour concevoir (contraintes de conception, renforcements à prévoir) |
| B-24 (Vérification d'éléments existants non) | Les données manquantes — B-24 produit une vérification en mode PARAMÉTRIQUE pour les éléments non sondés |
| B-44 (Charpente bois) | Les désordres de charpente existante (si applicable) — B-44 les cite |
| B-46 (Maçonnerie : vérification) | Les désordres de maçonnerie existante (si applicable) — B-46 les cite |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les points à lever avec destinataire — T-04 transforme ces points en demande formelle |

Variables consommées

| Code | Libellé | Statut dans B-11 |
| --- | --- | --- |
| DOC-05 | Diagnostic structure de l'existant | BLOQUANTE |
| DOC-08 | Plans de récolement / DOE | NON BLOQUANTE (si absents, l'audit est fait sur le diagnostic seul) |
| DOC-03 | Plans BET structure sur l'existant | NON BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |

Variables produites
B-11 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (audit du diagnostic) qui alimente B-13, B-14, B-15, B-23 et B-24.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-05, DOC-08, DOC-03, EXI-xx, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-11, vous devez vérifier que chaque cellule [ANALYSE GO] est bien la vôtre — pas une reformulation du diagnostic. C'est le moment où vous exercez votre jugement d'ingénieur EXE : ce que vous concluez du désordre, ce n'est pas ce que le diagnostic en dit.
Cas particulier — diagnostic avec zones non relevées : si le diagnostic contient des zones « NON RELEVÉES » (comme les deux zones du folio 02 dans la conversation d'origine), B-11 les liste explicitement avec leur emprise, et signale ce qu'on ne peut pas conclure dans ces zones. Ces zones deviennent :
   * soit une réserve au RDR (R-xx) : demande de relevé complémentaire ;
   * soit un verrou au RDR (V-xx) : la brique de calcul concernée est suspendue dans cette zone.
Cas particulier — diagnostic qui prescrit sans calculer : si le diagnostic prescrit un renforcement sans note de calcul (par exemple, « moisage par 2×UPE200 »), B-11 :
   1. cite la prescription (référence exacte) ;
   2. ajoute la mention « à valider par nos calculs B-xx » ;
   3. ne reprend pas la prescription à son compte.
C'est exactement la règle de l'option C pour les ancrages, appliquée aux prescriptions de diagnostic : la prescription du tiers est un principe, pas un dimensionnement. Elle doit être validée par nos calculs avant exécution.
Cas particulier — désordre hors lot : si le diagnostic identifie un désordre qui relève d'un autre lot (par exemple, couverture, zinguerie), B-11 le liste quand même dans le tableau 1, avec la mention « Hors lot GO — interface avec [lot concerné] ». Le désordre n'est pas rejeté : il est nommé, et son impact sur nos travaux est analysé.
Cas particulier — diagnostic absent : si le diagnostic est absent (bâtiment neuf), B-11 s'appelle en mode SANS OBJET (à statuer par la MPD). Ce sont B-10 (Audit CCTP) et B-12 (Audit géotechnique) qui couvrent l'analyse des pièces.
Format de sortie attendu : quatre tableaux distincts (désordres/analyse GO, prescriptions reprises, données manquantes, points à lever), suivis d'une synthèse en 8 lignes maximum. Chaque cellule du tableau 1 doit porter la qualification [CITATION] ou [ANALYSE GO] — c'est la règle fondamentale de B-11.
Consignation : l'audit B-11 est annexé au RDR (B-03) — il documente la lecture du diagnostic et alimente les réserves (R-xx) pour les données manquantes et les zones non relevées.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Exploitation du différentiel `EXISTANT / DÉMOLITION / PROJET`.** L'audit du diagnostic ne se limite plus aux désordres cités : il confronte chaque désordre à sa localisation réelle sur le fond calé et vérifie que les ouvrages conservés sont bien ceux que le projet sollicite (`GEO-14`).

**Zones non relevées.** Une zone non relevée n'est jamais un blanc : elle est soit couverte par une hypothèse `H-xx`, soit portée par une prescription `ENC` et un Point d'Arrêt `PA-xx` de reconnaissance.
**[Fin de 03_PHASE_1_ANALYSE/B-11_Audit_Diagnostic.md]**

---

**[Début du fichier : 03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md]**

Fichier 03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md — CARNAC v3.0
________________


B-12 — AUDIT DES PIÈCES GÉOTECHNIQUES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-10 (Audit CCTP), B-11 (Audit Diagnostic) — ou la première brique exécutable selon le PTD |
| Brique suivante | B-13 (Contradictions), B-40 (Fondations — si les données sont suffisantes) |
| Modes d'appel | COMPLET (rapport fourni et adapté) · PARTIEL-DÉCLARÉ (rapport fourni mais niveau de mission insuffisant : on signale l'écart et on poursuit) · SANS OBJET (MPD a statué que les fondations ne sont ni modifiées ni sollicitées) |
| Entrées lues | DOC-06 (rapport géotechnique), MPD validée, énoncé de mission |
| Sortie unique | Audit : données disponibles + adéquation aux besoins + données manquantes + recommandation de mission |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Clause | Pourquoi |
| --- | --- |
| « Tu ne retiens aucune valeur de calcul » | C'est la clause centrale de B-12. Le rapport géotechnique donne des valeurs de calcul au sens de la mission G2/G3 : nous les exploitons, nous ne les choisissons pas. Cette clause interdit la dérive « je retiens 0,25 MPa parce que la fourchette va de 0,20 à 0,30 » — qui fait perdre un litige (le géotechnicien engage sa responsabilité sur les valeurs qu'il fournit, pas nous) |
| « un G2 AVP est-il suffisant pour nos calculs d'exécution ? » | C'est le cas Flora : un G2 AVP ne suffit pas à des calculs EXE ; une G3 est nécessaire. La question est posée explicitement, pas laissée à l'appréciation du modèle. Sans cette question, un rapport G2 AVP est souvent accepté tel quel — et les calculs EXE sont faits sur des données qui n'ont pas été validées pour cet usage |
| « Tu ne décides pas à la place de la MOA si une mission complémentaire doit être commandée » | La commande d'une mission G3/G4 est une décision MOA, pas une décision de l'entreprise GO. Le rôle de l'audit est de la recommander, pas de la décider. Un modèle qui décide à la place de la MOA crée une décision implicite non opposable |
| « Conséquence si non commandée » | Le tableau 3 documente ce qui restera suspendu si la MOA ne commande pas la mission complémentaire — c'est ce qui vous protège en cas de litige. Si la MOA ne commande pas et que les fondations s'avèrent sous-dimensionnées, vous avez tracé que vous aviez recommandé la mission |
| « Ne déclare pas le rapport suffisant sans confronter chacun des codes SOL » | Empêche la conclusion « le G2 est là, on y va » qui masque les données manquantes. Un rapport peut sembler complet à la première lecture et manquer d'une donnée critique (par exemple, l'agressivité XA du sol, ou la nappe phréatique) |
| « Ne propose aucune hypothèse de repli » | Une hypothèse de repli est une décision RDR (PARTIEL-DÉCLARÉ), pas une proposition d'audit. Si vous décidez de retenir une valeur plancher, c'est une décision RDR avec auteur, date et justification — pas une initiative du modèle |
| « chaque donnée citée est rattachée à un paragraphe ou tableau du rapport » | Verrou V2 — une valeur sans référence n'est pas vérifiable. En cas de litige sur une valeur, on doit pouvoir dire « cette valeur figure au §3.2 tableau 4 page 12 du rapport GEOEXPERTS 25.13646 » |
| Synthèse en 8 lignes | Un audit exhaustif sans synthèse n'est pas exploitable en réunion de lancement. Les 8 lignes forcent le modèle à hiérarchiser |

Les trois adéquations possibles — précision utile :

| Adéquation | Définition | Conséquence |
| --- | --- | --- |
| Exploitable | La donnée est fournie avec une valeur claire, une méthode, et une référence explicite dans le rapport | Peut être utilisée en mode COMPLET par B-40 |
| Insuffisante | La donnée est fournie mais ne permet pas de conclure (valeur unique sans fourchette, absence de méthode, conditions de validité dépassées) | Nécessite une décision RDR (PARTIEL-DÉCLARÉ) ou une mission complémentaire |
| Ambiguë | La donnée est fournie mais avec une incertitude (fourchette large, méthode non justifiée, hypothèse non explicite) | Nécessite une clarification auprès du géotechnicien |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte du rapport géotechnique (fichier + folio + indice) |
| B-01 (Proposition de la matrice) | Le statut de DOC-06 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) et des variables SOL-01 à SOL-08 |
| B-03 (Registre des décisions) | Les décisions déjà prises (par exemple, une décision de périmètre qui précise que les fondations ne sont pas concernées) |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-13 (Détection et qualification) | Les écarts entre les données géotechniques et les autres pièces |
| B-15 (Fiche de synthèse) | Les données manquantes et les recommandations de mission — B-15 les intègre dans le registre des risques |
| B-20 (Conception structure GO) | Les données exploitables (SOL-01 à SOL-05) — B-20 les utilise pour prédimensionner les fondations |
| B-40 (Fondations superficielles) | Les valeurs exploitables (SOL-01, SOL-02, SOL-03, SOL-05) — B-40 ne peut pas s'exécuter en COMPLET si ces valeurs sont insuffisantes ou ambiguës |
| B-41 (Fondations profondes) | Les valeurs relatives aux pieux — B-41 les contrôle et recommande une mission G3/G4 si nécessaire |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | La recommandation de mission — T-04 transforme cette recommandation en demande formelle à la MOA |

Variables consommées

| Code | Libellé | Statut dans B-12 |
| --- | --- | --- |
| DOC-06 | Rapport géotechnique | BLOQUANTE |
| SOL-01 | Contrainte admissible ELS | BLOQUANTE (pour B-40, pas pour B-12 qui l'audite) |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | BLOQUANTE si sous-sol ou soutènement |

Variables produites
B-12 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (audit géotechnique) qui alimente B-13, B-15, B-40, B-41 et T-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-06, SOL-01 à SOL-08, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-12, vous devez décider si la mission complémentaire doit être commandée. C'est une décision MOA, mais c'est vous qui documentez la conséquence de la non-commande. Un audit qui recommande une G3 sans documenter la conséquence ne vous protège pas en cas de litige.
Cas particulier — G2 AVP insuffisant : si le rapport est un G2 AVP (avant-projet), il ne suffit pas pour des calculs d'exécution. B-12 recommande une G2 PRO ou une G3, avec la base normative (NF P 94-500) et la conséquence de la non-commande. C'est exactement le cas Flora : un G2 AVP sans G3 ne permet pas de conclure sur les fondations.
Cas particulier — rapport sans valeur de calcul : si le rapport géotechnique fournit des données (stratigraphie, essais) mais pas de valeurs de calcul (q_adm, tassements), B-12 signale que les données sont insuffisantes pour l'usage prévu (calculs EXE) et recommande une mission complémentaire. Un rapport de reconnaissance sans synthèse géotechnique n'est pas exploitable pour des calculs.
Cas particulier — conditions de validité dépassées : si le rapport a plus de 5 ans, ou si l'emprise a changé depuis, ou si des travaux ont modifié le sol, B-12 signale les conditions de validité qui ne sont plus remplies. Un rapport valide mais non applicable est aussi dangereux qu'un rapport absent.
Cas particulier — absence de géotechnique : si la MPD a statué que les fondations ne sont ni modifiées ni sollicitées (superstructure seule), B-12 s'appelle en mode SANS OBJET — avec une ligne de justification. Elle ne signale aucune donnée manquante : ce serait contraire à la décision de périmètre.
Format de sortie attendu : trois tableaux distincts (données disponibles, données manquantes, recommandation de mission), suivis d'une synthèse en 8 lignes maximum. Chaque donnée citée est rattachée à un paragraphe ou tableau du rapport.
Consignation : l'audit B-12 est annexé au RDR (B-03) — il documente la lecture du rapport géotechnique et alimente les réserves (R-xx) pour les données manquantes et les recommandations de mission.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 03_PHASE_1_ANALYSE/B-12_Audit_Geotechnique.md]**

---

**[Début du fichier : 03_PHASE_1_ANALYSE/B-13_Contradictions.md]**

Fichier 03_PHASE_1_ANALYSE/B-13_Contradictions.md — CARNAC v3.0
________________


B-13 — DÉTECTION ET QUALIFICATION DES CONTRADICTIONS INTER-PIÈCES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-10, B-11, B-12 (les trois audits) |
| Brique suivante | B-15 (Synthèse des risques) |
| Modes d'appel | COMPLET (B-10, B-11, B-12 tous exécutés en COMPLET) · PARTIEL-DÉCLARÉ (un des trois audits en mode dégradé : on signale les pièces non auditées et on limite la détection aux pièces couvertes) |
| Entrées lues | Sorties de B-10, B-11, B-12, inventaire B-00, MPD validée (B-01) |
| Sortie unique | Tableau des contradictions classées (gravité × nature) + tableau des briques impactées + inscription au RDR (B-03) |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-10, B-11 et B-12. B-13 est la brique de synthèse transversale des écarts entre les pièces — c'est elle qui qualifie les contradictions détectées à chaud par B-00, et qui en détecte de nouvelles.
Ce que vous fournissez à l'IA : les sorties de B-10, B-11 et B-12 (audits CCTP, diagnostic, géotechnique), l'inventaire B-00 (contradictions détectées à chaud), la MPD validée. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * le double classement (gravité × nature) de chaque contradiction ;
   * la brique impactée et le mode induit ;
   * l'inscription au RDR (V-xx si bloquante, R-xx si à lever ou à surveiller).
Ce que B-13 apporte de spécifique — la qualification systématique :

| Aspect | B-00 (détection à chaud) | B-13 (traitement systématique) |
| --- | --- | --- |
| Détection | Pendant l'inventaire | Après les trois audits, de manière exhaustive |
| Qualification | Non (liste brute) | Oui (gravité × nature) |
| Rattachement | Non | Oui (brique impactée, mode induit) |
| Inscription RDR | Non | Oui (V-xx ou R-xx) |
| Sortie | Liste de contradictions | Tableau qualifié + briques impactées |

Distinction fondamentale à respecter : B-13 ne traite que les contradictions au sens strict. Une lacune (une pièce ne dit rien sur un objet) ou une imprécision (une pièce dit quelque chose d'ambigu) ne sont pas des contradictions — elles relèvent de B-10, B-11 ou B-12. C'est ce qui évite que B-13 se transforme en second audit du CCTP.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : détecter et qualifier TOUTES les contradictions inter-pièces du DCE de l'opération {{ID-01}} — {{ID-02}}, à partir des audits B-10 (CCTP), B-11 (diagnostic existant) et B-12 (géotechnique). Tu ne tranches AUCUNE contradiction : tu les qualifies, tu les classes, tu les rattaches aux briques CARNAC concernées.


DÉFINITIONS STRICTES
- CONTRADICTION : deux pièces (ou deux passages) affirment des choses incompatibles sur un même objet. Les deux affirmations ne peuvent pas être vraies en même temps.
- LACUNE : une pièce ne dit rien sur un objet attendu. Ce N'EST PAS une contradiction. Traitée par B-10, B-11 ou B-12 — elle ne figure pas dans ta sortie.
- IMPRÉCISION : une pièce dit quelque chose d'ambigu. Ce N'EST PAS une contradiction. Traitée par B-10 — elle ne figure pas dans ta sortie.


CLASSEMENT OBLIGATOIRE EN DEUX COLONNES INDÉPENDANTES
Gravité :
- BLOQUANTE — empêche un calcul opposable, rend un livrable inexploitable, ou met en cause la sécurité structurale.
- À LEVER AVANT DÉMARRAGE — n'empêche pas les études mais doit être tranchée avant travaux.
- À SURVEILLER — ni bloquante ni critique, à documenter et suivre.
Nature :
- TECHNIQUE — deux valeurs, hypothèses ou prescriptions techniques incompatibles.
- CONTRACTUELLE — deux pièces du marché affirment des périmètres ou prestations incompatibles.
- D'INTERFACE — deux lots se renvoient la même prestation, ou aucun ne la prend.


MÉTHODE
1. Confronte systématiquement chaque paire de pièces auditée : CCTP ↔ plans BET, CCTP ↔ diagnostic, plans BET ↔ diagnostic, géotechnique ↔ plans BET, géotechnique ↔ CCTP, etc.
2. Confronte aussi chaque pièce à elle-même : une prescription du CCTP contredit-elle un autre article du CCTP ? Un désordre du diagnostic contredit-il un plan du même diagnostic ?
3. Élimine les doublons : une même contradiction vue sous deux angles reste UNE ligne.
4. Ne confonds pas contradiction et lacune/imprécision : si tu hésites, applique le test « les deux affirmations peuvent-elles être vraies en même temps ? ». Si oui, ce n'est pas une contradiction.
5. Pour chaque contradiction retenue : identifie la ou les briques CARNAC impactées (B-40 à B-50, ou B-20 à B-24) et le mode induit (COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE / INTERNE-GO).
6. Propose l'inscription au RDR : V-xx si BLOQUANTE, R-xx si À LEVER ou À SURVEILLER.


INTERDICTIONS
- Ne tranche AUCUNE contradiction : tu listes, c'est moi qui décide.
- N'invente aucune contradiction : chaque ligne cite les DEUX sources avec leur référence exacte (fichier + folio/page + indice).
- N'accepte aucune contradiction sur la foi d'une des deux pièces seule.
- Ne recopie pas les contradictions déjà détectées par B-00 sans les qualifier (gravité + nature + brique impactée) : B-00 a détecté à chaud, B-13 traite systématiquement.
- Ne mélange pas lacune ou imprécision dans la sortie : elles relèvent de B-10, B-11 ou B-12.


SORTIE
Tableau principal — Contradictions qualifiées :
N° | Objet | Source A (réf. exacte) | Source B (réf. exacte) | Nature de l'écart (en une phrase) | Gravité (B / ALVD / AS) | Nature (T / C / I) | Brique(s) impactée(s) | Mode induit | Inscription RDR proposée


Tableau secondaire — Répartition par brique :
Brique | Nombre de contradictions bloquantes | Nombre à lever avant démarrage | Nombre à surveiller | Mode consolidé induit


Puis une synthèse de 8 lignes maximum :
- les trois contradictions qui engagent le plus nos études (par gravité et par nombre de briques impactées) ;
- les contradictions qui ne sont pas nouvelles (déjà au RDR depuis B-00) et celles qui sont nouvelles ;
- le nombre total par gravité et par nature.


CRITÈRE D'ACCEPTATION
Le tableau est accepté si :
- chaque ligne cite les DEUX sources avec référence exacte ;
- chaque ligne porte un classement gravité et un classement nature ;
- aucune ligne ne relève d'une lacune ou d'une imprécision (test « les deux affirmations peuvent-elles être vraies ? ») ;
- chaque ligne identifie la brique impactée et le mode induit ;
- aucune contradiction n'a été tranchée par toi ;
- la synthèse tient en 8 lignes.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Définitions strictes de CONTRADICTION / LACUNE / IMPRÉCISION | Sans ces définitions, un modèle produit des « contradictions » qui sont en réalité des manques — et l'on retombe sur un second audit du CCTP au lieu d'un traitement ciblé. C'est la clause qui borne le périmètre de B-13 |
| Test « les deux affirmations peuvent-elles être vraies en même temps ? » | Test objectif qui permet de trancher entre contradiction et imprécision sans arbitrage subjectif. C'est le seul critère qui rend le classement reproductible — deux ingénieurs doivent aboutir au même résultat |
| « Ne tranche AUCUNE contradiction » | Verrou V1 — la contradiction est signalée, jamais résolue par le modèle. Un modèle qui tranche une contradiction en B-13 fausse toute la chaîne aval (B-40 à B-50 s'appuient sur les contradictions pour fixer leurs modes) |
| « Ne recopie pas les contradictions de B-00 sans les qualifier » | Empêche la redondance stérile : B-00 signale, B-13 qualifie et rattache aux briques. Une contradiction recopiée sans qualification est une contradiction qui ne sera jamais traitée |
| Double classement gravité × nature | Votre choix : les deux interlocuteurs ne sont pas les mêmes (le BET traite la technique, la MOE le contractuel, l'OPC l'interface). Un classement unique masque cette réalité |
| « Élimine les doublons » | Une même contradiction vue sous deux angles (par exemple, « XA4 du CCTP vs XA3 de la décision » et « enrobage 30 vs 50 ») est UNE seule ligne avec deux conséquences, pas deux lignes. Sans cette clause, le tableau explose en doublons |
| Mode induit | Chaque contradiction doit savoir à quoi elle conduit : si BLOQUANTE, brique suspendue ; si À LEVER, mode dégradé ; sinon, mode complet possible. Sans le mode induit, le tableau est descriptif mais non actionnable |
| « Ne mélange pas lacune ou imprécision dans la sortie » | Une contradiction, une lacune et une imprécision ont trois traitements différents (B-13, B-10, B-10). Les mélanger dans le même tableau rend le tri impossible |
| « chaque ligne cite les DEUX sources » | Verrou V2 — une contradiction qui ne cite qu'une source est une affirmation unilatérale, pas une contradiction. La double citation est la preuve qu'il y a bien deux affirmations incompatibles |
| Synthèse en 8 lignes | Un tableau de contradictions sans synthèse n'est pas exploitable en réunion. Les 8 lignes forcent la hiérarchisation |

Les trois niveaux de gravité — précision utile :

| Gravité | Définition objective | Action induite | Inscription RDR |
| --- | --- | --- | --- |
| BLOQUANTE | Empêche un calcul opposable, rend un livrable inexploitable, ou met en cause la sécurité structurale | Inscription immédiate au Registre des Verrous (V-xx) ; demande de décision MOE/MOA ; brique suspendue | V-xx |
| À LEVER AVANT DÉMARRAGE | N'empêche pas les études (on peut produire en PARAMÉTRIQUE ou PARTIEL-DÉCLARÉ), mais doit être tranchée avant le démarrage des travaux | Inscription au RDR avec échéance avant démarrage | R-xx |
| À SURVEILLER | Ne bloque ni les études ni le démarrage, mais doit être documentée et suivie (risque de dérive en phase travaux) | Inscription au RDR sans échéance ferme, revue à chaque réunion de chantier | R-xx |

Les trois natures — précision utile :

| Nature | Définition | Interlocuteur habituel |
| --- | --- | --- |
| TECHNIQUE | Deux valeurs, deux hypothèses ou deux prescriptions techniques incompatibles (ex. : deux classes d'exposition, deux sections, deux niveaux) | BET / MOE technique |
| CONTRACTUELLE | Deux pièces du marché affirment des périmètres ou des prestations incompatibles (ex. : CCTP et DPGF, CCTP et plan) | MOE / MOA |
| D'INTERFACE | Deux lots se renvoient la même prestation, ou aucun ne la prend (ex. : appuis de charpente sur nos sommiers) | MOE / OPC |

Une contradiction peut être BLOQUANTE et D'INTERFACE, ou À SURVEILLER et TECHNIQUE — les deux classements sont indépendants.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La liste des contradictions détectées à chaud par B-00 — B-13 les reprend pour les qualifier (gravité × nature) et les rattacher aux briques |
| B-01 (Proposition de la matrice) | Les décisions de périmètre — elles permettent de savoir si une contradiction est dans notre périmètre ou hors périmètre |
| B-10 (Audit critique du CCTP) | Les contradictions internes détectées par B-10 — B-13 les qualifie (gravité × nature) et les rattache aux briques |
| B-11 (Audit du diagnostic structure) | Les désordres cités et les données manquantes — B-13 les qualifie et les rattache aux briques |
| B-12 (Audit des pièces géotechniques) | Les écarts entre les données géotechniques et les autres pièces |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les propositions d'inscription (V-xx ou R-xx) — B-03 les inscrit dans la section correspondante |
| B-04 (Plan de travail dégradé) | Les briques suspendues par une contradiction BLOQUANTE — B-04 les intègre au plan de travail dégradé |
| B-14 (Clarification du périmètre) | Les contradictions d'interface identifiées — B-14 les intègre dans le tableau 3 |
| B-15 (Fiche de synthèse) | Les contradictions qualifiées — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise, responsable) |
| B-20 (Conception structure GO) | Les contradictions qualifiées — B-20 les signale et suspend les parties concernées |
| B-23 (Exploitation du diagnostic existant) | Les contradictions qui impactent les renforcements — B-23 les signale si elles bloquent une partie de la conception |
| B-40 (Fondations superficielles) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-41 (Fondations profondes) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-42 (Verticaux BA) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-43 (Planchers et dallages) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-44 (Charpente bois) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-45 (Structure métallique) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-46 (Maçonnerie : vérification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-47 (Escaliers) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-48 (Prédalles et planchers préfabriqués) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-49 (Linteaux et seuils) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-50 (Assemblages et ancrages) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-13 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE (B-13 ne peut pas qualifier une contradiction sans savoir si elle est déjà au registre) |
| Toutes les variables statuées FOURNIE, PARTIELLE, BLOQUANTE par B-01 | Selon la variable | Selon le statut |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |

Variables produites
B-13 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (tableau des contradictions qualifiées) qui alimente B-15, B-03 et B-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DEC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-13, vous devez valider le classement gravité × nature de chaque contradiction. C'est votre appréciation qui fait foi, notamment pour les À SURVEILLER que vous pourriez requalifier en À LEVER (verrou V12, sens unique : une fois requalifiée en À LEVER, une contradiction ne redevient jamais À SURVEILLER).
Cas particulier — contradiction déjà détectée par B-00 : si une contradiction a déjà été détectée à chaud par B-00, B-13 la reprend et la qualifie (gravité + nature + brique impactée). Elle ne la recopie pas sans qualification — c'est la règle de non-redondance.
Cas particulier — contradiction entre deux pièces contractuelles : si le CCTP et le marché se contredisent (par exemple, le CCTP inclut une prestation que le marché exclut), la contradiction est de nature CONTRACTUELLE et de gravité BLOQUANTE — elle doit être tranchée par la MOE avant de poursuivre. B-13 la liste, B-03 l'inscrit en V-xx, B-04 suspend les briques concernées.
Cas particulier — contradiction d'interface entre lots : si deux lots se renvoient la même prestation (par exemple, la charpente s'appuie sur nos sommiers BA mais le lot charpente n'est pas dans notre marché), la contradiction est de nature D'INTERFACE et de gravité À LEVER AVANT DÉMARRAGE — elle doit être tranchée par la MOE ou l'OPC avant travaux. B-13 la liste, B-03 l'inscrit en R-xx.
Cas particulier — contradiction interne au CCTP : si deux articles du CCTP se contredisent (par exemple, §01.2.1.5.5.1 prescrit une peinture intumescente et §01.2.1.5.5.2 mentionne un encoffrement), la contradiction est de nature CONTRACTUELLE et de gravité variable selon l'enjeu. B-13 la liste avec les deux articles.
Cas particulier — contradiction sans impact sur nos briques : si une contradiction existe entre deux pièces mais n'impacte aucune brique CARNAC (par exemple, deux revêtements de sol incompatibles dans le lot finitions), B-13 la liste quand même dans le tableau, avec la mention « brique impactée : aucune — hors périmètre CARNAC ». Le fait qu'elle soit hors périmètre ne dispense pas de la signaler : elle peut avoir un impact indirect sur la coordination.
Format de sortie attendu : un tableau principal (contradictions qualifiées) à 10 colonnes, un tableau secondaire (répartition par brique) à 4 colonnes, suivis d'une synthèse en 8 lignes maximum.
Consignation : le tableau des contradictions est annexé au RDR (B-03) — les contradictions BLOQUANTE deviennent des verrous (V-xx), les À LEVER et À SURVEILLER deviennent des réserves (R-xx).
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Réconciliation quantitative multi-pièces.** Le tableau de contradictions intègre une matrice de réconciliation `Plans Archi ↔ Plans Structure ↔ CCTP/DPGF ↔ Diagnostic ↔ Géotechnique` : surfaces, linéaires de voiles, nombres d'ouvertures, sections annoncées. Un écart quantitatif est une contradiction au même titre qu'un écart de valeur.

**Recalage commun.** Toute contradiction de position est arbitrée sur le `RSU` (`GEO-13`) : deux cotes divergentes sont comparées après recalage, jamais sur des fonds différents.
**[Fin de 03_PHASE_1_ANALYSE/B-13_Contradictions.md]**

---

**[Début du fichier : 03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md]**

Fichier 03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md — CARNAC v3.0
________________


B-14 — CLARIFICATION DU PÉRIMÈTRE DE LOT
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-10 (Audit CCTP), B-11 (Audit Diagnostic) |
| Brique suivante | B-15 (Synthèse des risques) |
| Modes d'appel | COMPLET (CCTP et décomposition en lots fournis) · PARTIEL-DÉCLARÉ (pas de DPGF ou de décomposition en lots : on signale l'absence et on poursuit sur ce que dit le CCTP) |
| Entrées lues | B-10 (audit CCTP : constats + lacunes), B-11 (interfaces de lots), énoncé de mission (B-00), MPD (B-01) |
| Sortie unique | Matrice du périmètre : ce qui est INCLUS / EXCLU / À TRANCHER (interfaces) + points à faire confirmer |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Clause | Pourquoi |
| --- | --- |
| Trois statuts seulement : INCLUS / EXCLU / À TRANCHER | Sans cette limite, un modèle produit des « partiellement inclus » qui masquent les ambiguïtés au lieu de les nommer. Trois statuts forcent la clarté : soit c'est à nous, soit c'est à un autre, soit personne ne l'a tranché |
| Tableau séparé pour les exclusions CARNAC | Un désamiantage n'est ni « inclus » ni « exclu du lot GO » : il est hors périmètre CARNAC — la nuance empêche le modèle de raisonner sur des prestations qu'il ne doit pas traiter |
| « Ne réaudite pas le CCTP » | Évite la redondance avec B-10 et libère de la place pour la vraie valeur ajoutée : la matrice de périmètre. Un modèle sans cette clause refait le travail de B-10 au lieu de le synthétiser |
| « Ne tranche AUCUNE attribution » | L'attribution d'une prestation à un lot est une décision contractuelle — jamais une décision du modèle. Un modèle qui tranche crée une décision implicite non opposable |
| « Ne déclare pas À TRANCHER une prestation qui figure explicitement dans le CCTP » | Empêche la sur-génération de « À TRANCHER » qui noie les vrais points d'interface. Si le CCTP dit clairement « cette prestation est au lot GO », elle est INCLUSE — pas À TRANCHER |
| « Destinataire pour trancher » | Un point d'interface sans destinataire ne se tranche jamais. La colonne « destinataire » transforme la matrice en outil actionnable |
| « Brique CARNAC qui validera » dans le tableau 1 | Chaque prestation INCLUSE a une brique CARNAC qui la validera techniquement (par exemple, une reprise en sous-œuvre par passes alternées → B-40). Le renvoi à la brique rend la matrice traçable |
| Synthèse en 10 lignes | Une matrice de périmètre sert en réunion de lancement — pas en lecture exhaustive. Les 10 lignes forcent la hiérarchisation |

Les trois natures d'ambiguïté — précision utile :

| Nature | Définition | Exemple |
| --- | --- | --- |
| Renvoi mutuel | Deux lots se renvoient la même prestation | « La charpente s'appuie sur les sommiers BA » — le lot charpente dit « c'est au GO de faire les sommiers », le lot GO dit « c'est au charpentier de prévoir ses appuis » |
| Silence | Aucune pièce ne dit qui fait la prestation | Le CCTP ne parle pas des réservations pour la VMC — ni le lot GO ni le lot CVC ne les revendique |
| Conflit | Deux pièces s'attribuent la même prestation à des lots différents | Le CCTP dit que l'isolation du dallage est au lot GO, le DPGF la met au lot isolation |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | L'énoncé de mission reformulé et les exclusions citées — B-14 s'appuie dessus pour construire la matrice INCLUS/EXCLU/À TRANCHER |
| B-01 (Proposition de la matrice) | Les décisions de périmètre (les NON NÉCESSAIRE validés) |
| B-10 (Audit critique du CCTP) | Les constats et les lacunes — B-14 construit la matrice INCLUS/EXCLU/À TRANCHER à partir de ces informations |
| B-11 (Audit du diagnostic structure) | Les interfaces de lots identifiées — B-14 construit la matrice INCLUS/EXCLU/À TRANCHER |
| B-13 (Détection et qualification) | Les contradictions d'interface identifiées — B-14 les intègre dans le tableau 3 |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les prestations À TRANCHER — B-03 les inscrit en réserves (R-xx) avec destinataire et échéance |
| B-15 (Fiche de synthèse) | Les prestations À TRANCHER — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise) |
| B-23 (Exploitation du diagnostic existant) | Les prestations INCLUSES et les interfaces — B-23 s'appuie sur cette matrice pour distinguer les renforcements de notre lot des interfaces |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les prestations À TRANCHER avec destinataire — T-04 les transforme en demande formelle |

Variables consommées

| Code | Libellé | Statut dans B-14 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DOC-04 | CCTP / pièces contractuelles | BLOQUANTE (pour le tableau 1 et 2) |

Variables produites
B-14 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (matrice de périmètre) qui alimente B-15, B-03 et T-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes, exclusions CARNAC | 00_MASTER.md |
| Dictionnaire de variables | DOC-04, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Périmètre technique et périmètre de mission.** La matrice `INCLUS / EXCLU / À TRANCHER` distingue explicitement ce qui relève du périmètre de l'entreprise (lot gros œuvre / structure), du périmètre d'intervention d'autres lots (charpente, métallerie, réservations techniques) et du périmètre de mission (études d'exécution, synthèse, OPC).
**[Fin de 03_PHASE_1_ANALYSE/B-14_Perimetre_Lot.md]**

---

**[Début du fichier : 03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md]**

Fichier 03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md — CARNAC v3.0
________________


B-15 — FICHE DE SYNTHÈSE DES RISQUES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-13 (Contradictions) — ou l'ensemble de la phase 1 |
| Brique suivante | B-20 (Conception GO) — ou la première brique de la phase 2 selon le PTD |
| Modes d'appel | COMPLET (périmètre d'analyse complet) · PARTIEL-DÉCLARÉ (périmètre limité à B-13 seule, décidé par vous) |
| Paramètre d'appel | {{périmètre_analyse}} = « B-13 seule » ou « ensemble de la phase Analyse » (B-10 à B-14) |
| Entrées lues | Selon {{périmètre_analyse}} : B-13 seule, ou B-10 + B-11 + B-12 + B-13 + B-14 |
| Sortie unique | Fiche de synthèse hiérarchisée des risques : cotation P×I, responsable, mesure de maîtrise, échéance |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-13 (ou après l'ensemble de la phase 1, selon votre choix). B-15 est la dernière brique de la phase 1 — elle synthétise les constats, contradictions et données manquantes en registre de risques hiérarchisé.
Ce que vous fournissez à l'IA : selon le paramètre {{périmètre_analyse}} :
   * « B-13 seule » : uniquement la sortie de B-13 (tableau des contradictions qualifiées) ;
   * « ensemble de la phase Analyse » : les sorties de B-10, B-11, B-12, B-13, B-14.
Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{périmètre_analyse}}.
Ce que vous validez à la sortie :
   * la cotation P × I de chaque risque (avec justification) ;
   * la mesure de maîtrise (action de pilotage, pas solution technique) ;
   * le responsable et l'échéance ;
   * les risques résiduels acceptés (c'est l'engagement qui vous engage).
Ce que B-15 apporte de spécifique — la distinction risque / contradiction :

| Notion | Ce qu'elle est | Ce qu'elle produit |
| --- | --- | --- |
| Contradiction (B-13) | Un état du dossier : deux pièces affirment des choses incompatibles | Un tableau qualifié, des verrous et réserves |
| Risque (B-15) | Un événement redouté : probabilité × impact, avec conséquence possible | Un registre hiérarchisé, avec mesures de maîtrise |

Une contradiction produit un ou plusieurs risques. Mais un risque peut aussi naître d'une lacune (B-10, B-11, B-12) ou d'une imprécision, pas seulement d'une contradiction. C'est pourquoi B-15 est une brique distincte, pas un simple sous-produit de B-13.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la fiche de synthèse des risques de l'opération {{ID-01}} — {{ID-02}}, à partir du périmètre d'analyse que je t'indique ci-dessous.


PÉRIMÈTRE D'ANALYSE (paramètre obligatoire)
{{périmètre_analyse}} = « B-13 seule » ou « ensemble de la phase Analyse ».
Si « B-13 seule » : tu ne lis QUE la sortie de B-13. Tu n'inventes aucun risque hors B-13.
Si « ensemble de la phase Analyse » : tu lis B-10, B-11, B-12, B-13 et B-14.


DÉFINITIONS
- RISQUE : événement redouté, avec une probabilité et un impact, et un rattachement obligatoire à une source (une ligne de B-10, B-11, B-12, B-13 ou B-14).
- Un risque n'est PAS une contradiction, une lacune ou une imprécision : c'est la conséquence possible de cette contradiction, lacune ou imprécision sur nos études, notre planning ou notre responsabilité.
- MESURE DE MAÎTRISE : action de pilotage (demande d'information, décision RDR, production en PARAMÉTRIQUE, confirmation écrite, inscription au RDR, commande de mission complémentaire). Ce N'EST PAS une solution technique.


COTATION
Probabilité (P) et impact (I) sur une échelle 1 à 3 :
- P1 : improbable (< 20 %)
- P2 : possible (20-60 %)
- P3 : probable (> 60 %)
- I1 : faible (retard < 1 semaine, ou impact mineur sur la note de calcul)
- I2 : moyen (retard 1 à 4 semaines, ou impact limité sur un livrable)
- I3 : fort (retard > 4 semaines, ou impact sur la sécurité, la conformité, ou notre responsabilité)
Criticité = P × I : 1-2 faible / 3-4 moyenne / 6-9 élevée.
Chaque cotation P et I doit être justifiée en une phrase courte — une cotation sans justification est rejetée.


MÉTHODE
1. Extrais tous les risques rattachables aux sources du périmètre d'analyse.
2. Élimine les doublons : deux formulations d'un même risque = un seul risque.
3. Cote chaque risque (P, I), en justifiant chaque cote en une phrase.
4. Identifie pour chaque risque : la brique CARNAC impactée, la mesure de maîtrise, le responsable (MOE / MOA / BET / BC / GO / OPC), et l'échéance (avant remise / avant démarrage / pendant EXE / à surveiller).
5. Hiérarchise par criticité décroissante.
6. Identifie les risques résiduels : ceux qu'on accepte de porter, avec justification.


INTERDICTIONS
- N'invente aucun risque : tout risque est rattaché à une source citée (B-xx, ligne n°).
- Ne confonds pas risque et contradiction : une contradiction produit un ou plusieurs risques, mais un risque peut naître d'une lacune ou d'une imprécision.
- Ne propose aucune solution technique comme mesure de maîtrise.
- Ne cote pas sans justifier : « P3 parce que la donnée est absente depuis deux mois » est une justification ; « P3 » seul ne l'est pas.
- Ne mets pas un risque sans responsable et sans échéance.
- Ne fusionne pas deux risques distincts pour « faire court » : la fiche peut faire plusieurs pages.


SORTIE
Tableau principal — Registre des risques :
N° | Risque (formulation en une phrase, au conditionnel) | Source (B-xx, ligne n°) | Nature (technique / contractuelle / d'interface / planning / réglementaire) | P (1-3) | Justification P | I (1-3) | Justification I | Criticité (P×I) | Brique impactée | Mesure de maîtrise | Responsable | Échéance


Tableau secondaire — Risques résiduels acceptés :
N° | Risque | Justification de l'acceptation | Responsable du suivi


Puis une synthèse de 10 lignes maximum :
- les trois risques de criticité élevée ;
- les risques qui impactent directement la remise de nos livrables ;
- les risques qui impactent notre responsabilité contractuelle ;
- les risques résiduels acceptés et leur justification.


CRITÈRE D'ACCEPTATION
La fiche est acceptée si :
- chaque risque est rattaché à une source citée ;
- chaque cotation P et I est justifiée ;
- chaque risque a un responsable et une échéance ;
- la mesure de maîtrise est une action de pilotage, pas une solution technique ;
- les risques résiduels sont identifiés et justifiés ;
- la synthèse tient en 10 lignes ;
- si le périmètre est « B-13 seule », aucun risque n'est introduit hors B-13.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{périmètre_analyse}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Paramètre {{périmètre_analyse}} explicite | Votre arbitrage : B-15 peut tourner seule sur B-13, ou sur toute la phase 1. Sans paramètre explicite, le modèle prend l'initiative — et sur B-13 seule, il peut « enrichir » avec des risques inventés hors B-13 |
| « Si B-13 seule : tu ne lis QUE B-13 » | Verrou anti-hallucination pour le mode limité. Le périmètre d'analyse est le seul qui définit ce qui peut être dit — un risque hors périmètre est un risque inventé |
| Définition RISQUE ≠ CONTRADICTION | Le risque est un événement redouté (probabilité × impact), la contradiction est un état du dossier. Confondre les deux produit une fiche illisible et sans hiérarchisation utile — et fait perdre la valeur ajoutée de B-15 (qui est d'identifier les conséquences possibles) |
| « MESURE DE MAÎTRISE : action de pilotage, pas solution technique » | Empêche B-15 de devenir une brique de conception. La maîtrise d'un risque « G3 non commandée » est « demander la commande du G3 », pas « utiliser 0,25 MPa au lieu de 0,30 ». C'est la frontière avec B-20 et B-40 à B-50 |
| Cotation P et I avec justification obligatoire | Une cotation sans justification est une note arbitraire — elle ne se défend pas en réunion. « P3 parce que la donnée est absente depuis deux mois » est une justification ; « P3 » seul ne l'est pas |
| Échelle P×I 1-3 plutôt que 1-5 | Sur des études d'exécution, une échelle fine (1-5) donne une fausse précision. Le 1-3 est plus robuste (moins de subjectivité) et plus rapide à coter en réunion de lancement |
| Tableau des risques résiduels | Un risque non identifié comme résiduel est un risque qu'on oublie. Le tableau l'oblige à être nommé et accepté formellement — c'est l'engagement qui vous engage |
| « Responsable + échéance » obligatoires | Un risque sans responsable ne se traite jamais ; un risque sans échéance est traité trop tard. Les deux colonnes rendent la fiche actionnable |
| « Ne fusionne pas deux risques distincts pour faire court » | La tentation de fusionner pour « faire propre » produit des fiches courtes mais inutilisables — un risque fusionné perd son responsable et son échéance. Une fiche longue et exacte vaut mieux qu'une fiche courte et fausse |
| Synthèse en 10 lignes | La fiche de synthèse est faite pour la réunion de lancement, pas pour la lecture exhaustive. Les 10 lignes forcent la hiérarchisation et permettent une présentation orale |

Les cinq natures de risque — précision utile :

| Nature | Définition | Exemple |
| --- | --- | --- |
| Technique | Risque lié à une incertitude technique (donnée manquante, méthode non validée, hypothèse non confirmée) | « Si q_adm n'est pas confirmée, les semelles dimensionnées en PARAMÉTRIQUE ne seront pas exécutables » |
| Contractuelle | Risque lié à un périmètre ambigu ou à une prestation non tranchée | « Si la prestation de reprise en sous-œuvre de la passerelle est refusée par la MOA, notre prix est faux » |
| D'interface | Risque lié à une interface entre lots | « Si le lot charpente n'est pas attribué avant notre démarrage, nos sommiers sont posés sans appuis » |
| Planning | Risque lié à un délai (donnée tardive, visa tardif, décision tardive) | « Si le visa BET n'est pas obtenu avant le 15/11, le livrable est remis en PARAMÉTRIQUE » |
| Réglementaire | Risque lié à une exigence réglementaire non satisfaite | « Si SEC-01 n'est pas fourni, l'enrobage de nos poteaux n'est pas conforme ERP » |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions et verrous déjà inscrits — B-15 en tient compte pour ne pas dupliquer un risque déjà traité |
| B-10 (Audit critique du CCTP) | Les points à lever et les prescriptions à confirmer — B-15 les intègre dans le registre des risques |
| B-11 (Audit du diagnostic structure) | Les zones non relevées et les données manquantes — B-15 les intègre dans le registre des risques |
| B-12 (Audit des pièces géotechniques) | Les données manquantes et les recommandations de mission — B-15 les intègre dans le registre des risques |
| B-13 (Détection et qualification) | Les contradictions qualifiées — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise, responsable) |
| B-14 (Clarification du périmètre) | Les prestations À TRANCHER — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise) |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les risques identifiés — chaque risque de criticité élevée devient une réserve R-xx (ou un verrou V-xx si le risque est déjà bloquant) |
| B-20 (Conception structure GO) | Les risques techniques (incertitudes sur les hypothèses) — B-20 les intègre dans sa note d'hypothèses (B-22) |
| B-72 (Journal de clôture) | Les risques résiduels — B-72 les intègre dans la section « points ouverts » |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les risques avec responsable et échéance — T-04 les transforme en demande formelle à la MOE / BET / MOA |

Variables consommées

| Code | Libellé | Statut dans B-15 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-03 | Verrous ouverts (via B-03) | NON BLOQUANTE (si B-03 n'est pas encore consultée, B-15 peut encore identifier les risques, mais elle doit signaler l'absence) |

Variables produites
B-15 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (fiche de synthèse des risques) qui alimente B-03, B-20, T-04 et B-72.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DEC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-15, vous devez valider les risques résiduels acceptés. C'est l'engagement qui vous engage — un risque que vous acceptez de porter est un risque que vous ne pourrez plus reprocher à la MOE en cas de réalisation. C'est votre décision, pas celle du modèle.
Cas particulier — périmètre « B-13 seule » : si vous choisissez le périmètre limité à B-13, B-15 ne lit que les contradictions qualifiées par B-13. Elle ne voit pas les lacunes de B-10, les zones non relevées de B-11, les données manquantes de B-12, ni les prestations À TRANCHER de B-14. Le périmètre limité est utile en cours de projet (après B-13, avant que les autres briques de la phase 1 ne soient terminées), mais il ne remplace pas une synthèse complète.
Cas particulier — périmètre « ensemble de la phase Analyse » : si vous choisissez le périmètre complet, B-15 lit l'ensemble de la phase 1. C'est la synthèse de référence, à utiliser en fin de phase 1 avant de passer à la phase 2.
Cas particulier — risque de criticité élevée sans mesure de maîtrise : si un risque est coté criticité 6 à 9 (élevée) mais qu'aucune mesure de maîtrise n'est identifiée, B-15 le signale explicitement. Un risque de criticité élevée sans mesure de maîtrise est une anomalie — soit le risque n'est pas correctement coté, soit il manque une action de pilotage.
Cas particulier — risque résiduel accepté : un risque résiduel est un risque qu'on accepte de porter parce que :
   * la mesure de maîtrise coûte plus cher que le risque lui-même ;
   * le risque est en dehors de notre périmètre mais on décide de le porter quand même ;
   * la MOA a explicitement accepté le risque.
Le tableau des risques résiduels documente pourquoi le risque est accepté, et qui le suit.
Cas particulier — risque déjà traité par une décision RDR : si un risque est déjà couvert par une décision RDR (par exemple, « risque de q_adm insuffisante — décision D-03 de produire en PARAMÉTRIQUE »), B-15 le mentionne avec la référence à la décision. Il n'est pas recopié sans mention — c'est la règle de non-redondance avec B-03.
Format de sortie attendu : un tableau principal (registre des risques) à 13 colonnes, un tableau secondaire (risques résiduels) à 4 colonnes, suivis d'une synthèse en 10 lignes maximum.
Consignation : la fiche B-15 est annexée au RDR (B-03) — chaque risque de criticité élevée devient une réserve (R-xx) avec responsable et échéance ; les risques résiduels acceptés sont consignés dans une section dédiée du RDR.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Pré-Audit Flash d'Exécutabilité obligatoire.** Avant toute production, B-15 contrôle par ratios l'exécutabilité de l'ensemble du dossier, **y compris lorsqu'un BET structure MOE existe** : élancement de flèche sous maçonnerie (`L/h`), portance et dimension minimale des semelles (`q_Ed` vs `q_adm`, `B_min`), élancement des poteaux (`H_0/b`), compression locale sous appuis et sous appareils d'appui. Un ratio hors bornes produit un risque de criticité élevée et une demande de complément `T-04`, jamais un silence.
**[Fin de 03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md]**

---

**[Début du fichier : 05_PHASE_3_CALAGE/B-30_Calage.md]**

Fichier 05_PHASE_3_CALAGE/B-30_Calage.md — CARNAC v3.0
________________


B-30 — CALAGE SUR DXF/DWG SOURCE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 1 — Socle géométrique et nettoyage |
| Brique précédente | B-24 (Existant non sondé) — ou la première brique exécutable selon le PTD |
| Brique suivante | B-31 (Preuve de superposition), B-32 (Vue nettoyée), B-33 (Vérification croisée) |
| Fréquence | Une fois par projet — donnée de projet, réutilisée par toutes les briques graphiques |
| Modes d'appel | COMPLET (fichier vectoriel exploitable) · PARTIEL-DÉCLARÉ (fichier image ou PDF non vectoriel : on signale l'impossibilité de calage exact et on passe en calage manuel déclaré) · SANS OBJET (aucun fond de plan nécessaire) |
| Entrées lues | DOC-02 (plans archi vectoriels), GEO-06 (unités), GEO-07 (transformation), GEO-08 (points de calage) |
| Sortie unique | Paramètres de calage validés (transformation, points de calage, résidu) + preuve de calage initiale + fichier recalé indicé |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : au début de la phase 3, avant toute production graphique (B-31, B-32, B-60). B-30 est la brique qui établit le calage entre le fichier source et notre repère de travail. Sans elle, aucune brique graphique ne peut garantir que ses ajouts tombent sur les positions réelles.
Ce que vous fournissez à l'IA : les plans architecte vectoriels (DOC-02, DXF ou DWG), les unités déclarées, et les points de calage identifiables (angles de murs, intersections d'axes). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * les points de calage (au moins 3 non alignés, avec coordonnées dans les deux repères) ;
   * la transformation (translation, rotation, échelle) ;
   * le résidu sur les points témoins (≤ 1 cm à l'échelle du bâtiment) ;
   * la preuve de superposition initiale ;
   * le fichier recalé (nommé et indicé).
Ce que B-30 apporte de spécifique — le calage comme donnée de projet :

| Aspect | B-30 (une fois par projet) | B-31 / B-32 / B-33 (à chaque livrable) |
| --- | --- | --- |
| Objet | Caler le fichier source sur notre repère | Vérifier / nettoyer / croiser chaque livrable produit |
| Fréquence | Une fois | À chaque livrable |
| Sortie | Paramètres + fichier recalé | Preuve / vue / rapport |
| Réutilisation | Le fichier recalé alimente toutes les briques graphiques | Chaque brique graphique s'appuie sur le fichier recalé |

La règle la plus importante : B-30 ne calcule JAMAIS une transformation par ajustement visuel. Le calage se fait par les coordonnées vectorielles du fichier source, avec au moins 3 points non alignés et une mesure de résidu sur des points témoins. C'est ce qui garantit que le calage est reproductible — deux ingénieurs doivent aboutir au même résultat.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir le calage géométrique entre le fichier source (DXF/DWG ou PDF vectoriel) de l'opération {{ID-01}} — {{ID-02}} et le repère de travail que nous utiliserons dans tous nos livrables. Le calage est UNE FOIS établi pour le projet, puis réutilisé par toutes les briques graphiques.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


MÉTHODE
1. Identifie le fichier source : nom, format, unités déclarées (GEO-06), orientation (rotation éventuelle), échelle déclarée.
2. Identifie au moins TROIS points de calage NON ALIGNÉS : angles de murs, intersections d'axes, points singuliers stables. Pour chaque point, cite les coordonnées dans le fichier source et dans le repère de travail.
3. Calcule la transformation : translation, rotation, échelle (facteur uniforme, sauf justification d'une anisotropie).
4. Vérifie le résidu de calage sur des points de contrôle NON utilisés pour le calage (points témoins). Résidu acceptable : ≤ seuil projet GEO-12 (défaut : 1 cm ouvrage neuf, 2 cm existant régulier ; au-delà, valeur déclarée au RDR — voir document maître §5). Si le résidu dépasse, tu changes de méthode (recherche d'erreur dans les points de calage ou dans les unités) — tu ne « déplaces pas à l'œil ».
5. Produis la preuve de calage : superposition du fichier source recalé sur un fond de contrôle, avec les points de calage annotés.
6. Consigne les paramètres dans le RDL : fichier source, version, transformation, résidu.


INTERDICTIONS
- Ne calcule JAMAIS une transformation par « ajustement visuel » ou « proportion d'image » : tu utilises les coordonnées vectorielles.
- N'utilise pas moins de TROIS points de calage non alignés.
- Ne valide pas un calage sans résidu mesuré sur des points témoins.
- Ne déplace aucun point pour « faire coller » : si le résidu est élevé, tu diagnostiques la cause (unités, rotation, points de calage mal choisis) et tu recalcules.
- Ne mélange pas calage et nettoyage des vues : le calage est une donnée, le nettoyage est B-32.
- Ne produis aucun plan : tu produis des paramètres de calage et une preuve.


SORTIE
Pièce 1 — Paramètres de calage
Fichier source | Format | Unités déclarées | Rotation déclarée | Transformation calculée (translation, rotation, échelle) | Points de calage utilisés | Résidu maximal sur points témoins | Résidu acceptable (Oui / Non)


Pièce 2 — Preuve de calage
Une superposition annotée : fichier source recalé + points de calage + points témoins + résidus. Format PDF + PNG.


Pièce 3 — Dossier de calage
Le fichier DXF/DWG recalé, nommé explicitement « calé » avec indice, prêt à être utilisé par B-32.


CRITÈRE D'ACCEPTATION
Le calage est accepté si :
- au moins TROIS points de calage non alignés sont identifiés avec leurs coordonnées dans les deux repères ;
- la transformation (translation, rotation, échelle) est calculée et justifiée ;
- le résidu sur points témoins est mesuré et comparé au seuil projet GEO-12 (document maître §5) ;
- la preuve de superposition est fournie en PDF et PNG ;
- le fichier recalé est nommé et indicé ;
- aucun ajustement visuel n'a été utilisé.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou SANS OBJET). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Une fois par projet, réutilisé | Le calage est une donnée de projet : la transformation entre le DXF et notre repère ne change pas d'un livrable à l'autre. La refaire à chaque livrable est une source d'erreur — deux calages successifs peuvent différer légèrement, et les livrables ne seraient plus cohérents entre eux |
| Trois points non alignés | Deux points ne définissent qu'une droite ; trois non alignés définissent une similitude complète (translation + rotation + échelle). En dessous de trois, le calage n'est pas déterminé — et un calage non déterminé est un calage faux |
| Points témoins non utilisés au calage | Un point utilisé au calage ne prouve rien : il est forcément juste (il a servi à déterminer la transformation). Les points témoins seuls mesurent la qualité du calage — c'est le seul contrôle qui garantit que la transformation est valide partout, pas seulement aux points de calage |
| « Ne déplace pas à l'œil » | Verrou V4 — c'est la réponse directe au décalage du projet Flora. Un calage qui ne colle pas se diagnostique (unités ? rotation ? points de calage mal choisis ?), il ne se retouche pas. La retouche visuelle produit un livrable faux pour une autre raison |
| Résidu ≤ 1 cm | À l'échelle d'un bâtiment, 1 cm est la tolérance au-delà de laquelle une cote devient fausse. En dessous, l'écart est négligeable (à l'échelle 1/50, 1 cm réel = 0,2 mm papier — invisible) |
| Fichier « calé » nommé et indicé | Le fichier recalé devient une donnée de projet, pas un fichier temporaire qui se perd. Il est réutilisé par B-32 (vue nettoyée), B-31 (preuve de superposition) et B-60 (plans d'exécution). S'il est perdu, toutes les briques graphiques doivent être refaites |
| Consignation au RDL | Le RDL (Registre des Livrables) enregistre le calage comme donnée de référence. En cas de modification de source, le RDL identifie les livrables impactés — c'est ce qui permet la mise à jour incrémentale (B-32) sans tout refaire |
| « Ne mélange pas calage et nettoyage » | Le calage est une transformation géométrique (donnée) ; le nettoyage est un filtrage des calques (production). Ce sont deux opérations distinctes — les mélanger conduit à un fichier « calé-netoyé » qui n'est ni l'un ni l'autre, et qui ne peut pas être réutilisé pour un autre livrable |

Le piège du calage visuel : un modèle qui reçoit un décalage visible a tendance à déplacer les points pour les faire coïncider. C'est exactement ce qu'il faut interdire :
   * le déplacement visuel corrige le décalage à un endroit, mais ne corrige pas la cause (unités, rotation, points mal choisis) ;
   * la cause persiste, et le décalage réapparaît ailleurs — souvent de manière plus insidieuse ;
   * le résultat est un fichier qui « a l'air calé » aux points de contrôle, mais qui est faux partout ailleurs.
La règle « diagnostic avant correction » est la seule qui garantit un calage valide.
Le cas du fichier non vectoriel : si le fichier source est une image (PDF rasterisé, scan, JPEG), B-30 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité de calage exact. Le calage manuel est déclaré comme tel — il porte une incertitude qui doit être reportée sur les livrables :
   * les plans produits en mode PARTIEL-DÉCLARÉ portent la mention « calage manuel — incertitude non mesurée » ;
   * les cotes de position sont arrondies (pas de précision au mm) ;
   * les livrables exécutables sont différés jusqu'à obtention d'un fichier vectoriel.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte du fichier source (DOC-02), son format, ses unités déclarées |
| B-01 (Proposition de la matrice) | Le statut de DOC-02 (FOURNIE, PARTIELLE, BLOQUANTE) et de GEO-06 à GEO-08 |
| B-20 (Conception structure GO) | La trame et les plans de principe — B-30 calcule le calage sur cette base |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-25 (Stabilité globale, contreventement, joints) | Le repère de référence dans lequel le schéma est établi |
| B-31 (Preuve de superposition) | Le fichier recalé — chaque preuve de superposition se fait sur le fichier calé, pas sur le fichier source brut |
| B-32 (Vue nettoyée par livrable) | Le fichier recalé — chaque vue nettoyée est extraite du fichier calé |
| B-33 (Vérification croisée) | Les paramètres de calage — pour vérifier la cohérence plan ↔ source |
| B-60 (Plans d'exécution) | Le fichier recalé — les plans d'exécution s'appuient sur la vue nettoyée (elle-même issue du fichier calé) |
| B-62 (Nomenclature et façonnage) | Le fichier recalé — B-62 utilise le calage pour identifier les positions si nécessaire |
| B-71 (Indiçage et supersession documentaire) | Le fichier recalé et son indice — consignés au RDL |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-30 |
| --- | --- | --- |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE |
| GEO-06 | Unités du fichier source (cm/m/mm) | BLOQUANTE |
| GEO-07 | Transformation du fichier (rotation, translation, échelle) | BLOQUANTE |
| GEO-08 | Points de calage identifiés (≥ 3 non alignés) | BLOQUANTE |
| GEO-12 | Seuils géométriques du projet (document maître §5) | BLOQUANTE (donnée FDC) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE si L / XL ou R+n |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |

Variables produites
B-30 ne produit pas de variable au sens du dictionnaire : sa sortie est un dossier de calage (paramètres + preuve + fichier recalé) qui alimente toutes les briques graphiques de la phase 3 et de la phase 5.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-02, GEO-06, GEO-07, GEO-08, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-30, vous devez valider le résidu de calage. Le critère objectif est le seuil projet GEO-12 (document maître §5) : 1 cm en neuf, 2 cm en existant régulier, valeur déclarée au RDR en existant irrégulier. Vous seul savez dans quelle colonne le bâtiment se situe ; un résidu supérieur au seuil mais expliqué par l'ouvrage est classé « écart justifié » et tracé au RDR — jamais retouché à l'œil.
Cas particulier — fichier source pivoté : si le fichier source est pivoté (par exemple, un plan orienté à 45° par rapport au nord), B-30 identifie la rotation déclarée (GEO-07) et la corrige dans la transformation. La preuve de calage montre le fichier source dans son orientation d'origine et dans l'orientation corrigée — pour que le lecteur puisse vérifier que la rotation a bien été appliquée.
Cas particulier — fichier source multi-calques : si le fichier DXF contient plusieurs calques (murs, cloisons, mobilier, cotations), B-30 identifie les calques utiles pour le calage (généralement les calques de murs) et ignore les autres. Le fichier recalé conserve tous les calques — c'est B-32 qui fera le filtrage.
Cas particulier — fichier source avec unités incohérentes : si le fichier DXF déclare des unités en cm mais que les cotes sont en mm, B-30 le signale et corrige la transformation en conséquence. La preuve de calage montre l'écart avant et après correction — pour que le lecteur comprenne que l'unité a été détectée et corrigée.
Cas particulier — fichier source partiel : si le fichier ne couvre qu'une partie du bâtiment (par exemple, seulement le RDC sans le R+1), B-30 le signale et limite le calage à la zone couverte. Les zones non couvertes ne peuvent pas être calées — elles sont déclarées comme telles, et les livrables qui en dépendent sont suspendus.
Cas particulier — recalage en cours de projet : si une nouvelle version du fichier source arrive (par exemple, un DXF Ind D), B-30 est rappelée pour recalculer le calage sur la nouvelle version. Les paramètres précédents sont conservés (traçabilité), et la nouvelle version est consignée au RDL avec son indice. Les livrables produits sur l'ancienne version sont impactés — B-32 (mise à jour incrémentale) les régénère.
Cas particulier — fichier source absent : si le fichier source vectoriel est absent (par exemple, seuls des PDF rasterisés sont fournis), B-30 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité de calage exact. Le calage manuel est déclaré, avec les limitations qui en découlent. Si aucun fichier source n'est disponible (ni vectoriel ni raster), B-30 s'appelle en mode SANS OBJET — et aucune brique graphique ne peut être produite.
Format de sortie attendu : trois pièces distinctes (paramètres de calage, preuve de calage, fichier recalé indicé). La preuve de calage est fournie en PDF et PNG — le PDF pour l'archivage, le PNG pour l'insertion dans les comptes rendus.
Consignation : le dossier B-30 est annexé au RDL (Registre des Livrables) — il documente le calage pour toutes les briques graphiques et permet la mise à jour incrémentale en cas de modification de source.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Calage multi-sources vers le Repère Structurel Unique (`RSU`).** Le calage ne porte plus sur un seul fichier architecte : il intègre toutes les sources vectorielles disponibles et les PDF structure MOE (extraction des tracés), avec une matrice de recalage `GEO-13` consignant pour chaque source la transformation appliquée (translation, rotation, échelle) et le résidu mesuré sur les points témoins.

**Séquence imposée.** Le calage précède désormais l'audit et la conception : il s'exécute en `Phase 1`, immédiatement après le cadrage. Aucun audit de contradiction ni aucune conception ne s'appuie sur un fond non calé.

**Détection des unités et des rotations déclaratives.** Le script de calage vérifie systématiquement la cohérence des unités (mm/cm/m) et l'orientation déclarée avant tout ajustement ; un écart d'unité est corrigé par la transformation, jamais par déplacement de points.
**[Fin de 05_PHASE_3_CALAGE/B-30_Calage.md]**

---

**[Début du fichier : 05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md]**

Fichier 05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md — CARNAC v3.0
________________


B-32 — VUE NETTOYÉE PAR LIVRABLE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 1 — Socle géométrique et nettoyage |
| Brique précédente | B-30 (Calage) |
| Brique suivante | B-31 (Preuve de superposition) — ou directement la brique de production du livrable |
| Fréquence | À chaque livrable graphique, versionnée avec lui. Mise à jour incrémentale en cas de modification de source. |
| Modes d'appel | COMPLET (fichier vectoriel exploitable) · PARTIEL-DÉCLARÉ (fichier image : nettoyage manuel déclaré, réserves notées) |
| Entrées lues | Fichier source calé (B-30), livrable concerné, liste des calques ou éléments à conserver/supprimer |
| Sortie unique | Vue nettoyée propre au livrable, versionnée, consignée au RDL |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : à chaque livrable graphique produit. La vue nettoyée est le fond de plan utilisé par la brique de production (B-60) — elle est versionnée avec le livrable, et régénérée en cas de modification de source.
Ce que vous fournissez à l'IA : le fichier source calé (B-30), le livrable concerné (type et indice), et la liste des calques ou entités à conserver/supprimer (selon le livrable). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{indice_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * la liste des calques (conservés / supprimés / à trancher) avec justification ;
   * le nom de la vue nettoyée (convention) ;
   * la consignation au RDL (ligne complétée) ;
   * en cas de mise à jour incrémentale : les livrables impactés identifiés via le RDL.
Ce que B-32 apporte de spécifique — la vue nettoyée par livrable :

| Aspect | Vue nettoyée unique (par projet) | Vue nettoyée par livrable (B-32) |
| --- | --- | --- |
| Fond de plan | Un seul fond pour tous les livrables | Un fond adapté à chaque livrable |
| Éléments conservés | Tous les éléments utiles au livrable le plus exigeant | Seuls les éléments utiles au livrable concerné |
| Mise à jour | Tout le projet est à refaire | Seuls les livrables impactés sont à refaire |
| Traçabilité | Un seul fond, un seul indice | Un fond par livrable, indicé avec le livrable |

Votre règle (validée au tronçon 6) : une vue nettoyée par livrable, versionnée avec lui. En cas de modification de source, seuls les livrables impactés sont régénérés — pas tout le projet.
La règle la plus importante : B-32 ne redessine aucun élément. La vue nettoyée est une extraction filtrée du fichier source calé — pas un redessin. Un redessin introduit des erreurs invisibles, et rend la vue incohérente avec le fichier source.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la vue nettoyée du livrable graphique {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir du fichier source calé (B-30), et en conservant uniquement les éléments nécessaires au livrable concerné.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


RÈGLES DE NETTOYAGE
Selon le livrable à produire, conserve :
- Livrable FONDATIONS : murs porteurs, refends, poteaux, semelles existantes, axes, cotations de position des appuis. Supprime : cloisons, menuiseries intérieures, revêtements, mobilier, fluides.
- Livrable PLANCHER : murs porteurs, poteaux, profilés, appuis, axes, trémies et réservations. Supprime : tout élément du second œuvre, y compris les menuiseries extérieures si le plancher ne les concerne pas.
- Livrable CHERPENTE : murs d'appui, pignons, fermes existantes, pannes, chevrons. Supprime : tout élément sous toiture sauf les appuis.
- Livrable VERTICAUX : murs, poteaux, axes, ouvertures (baies et passages), attentes de fondations. Supprime : tout le second œuvre.
- Livrable PLAN DE PRINCIPE : murs porteurs, axes, trames. Supprime : tout ce qui n'est pas porteur ou repère.


MÉTHODE
1. Reprends le fichier source calé (B-30).
2. AVANT tout classement par calque : applique le §R (protocole de reconnaissance des porteurs, en fin de fiche) — inventaire des entités, reconstruction des parois et mesure des épaisseurs, critères C1 à C6 (source BET souveraine, épaisseur vs GEO-10, superposition des niveaux vs GEO-11, schéma statique, position, indices graphiques). Les tronçons sont d'abord chaînés en parois complètes (R.3bis : segmentation aux intersections, regroupement des colinéaires, appariement des faces — on ne classe jamais un tronçon isolé). Si un plan BET vectoriel existe (DOC-03), ses porteurs sont projetés automatiquement sur les parois par recalage et recouvrement (R.4bis) : c'est cette projection qui vaut critère C1, et ses écarts sont signalés, jamais appariés de force. Chaque paroi reçoit une classe : PORTEUR CERTAIN, NON PORTEUR ou À LEVER, justifiée dans le tableau de reconnaissance. Si les calques du fichier séparent déjà explicitement les porteurs (sémantique vérifiée), le §R se réduit aux temps R.2, R.6 et R.7.
3. Identifie les calques (layers) du DXF ou les entités du PDF vectoriel, et pour chacun : CONSERVER, SUPPRIMER, ou À TRANCHER — en cohérence avec les classes du §R : un élément classé PORTEUR CERTAIN n'est jamais supprimé ; un élément À LEVER non arbitré est conservé en gris (calque EXISTANT).
4. Pour les calques À TRANCHER, applique la règle du livrable concerné : conserver si l'élément est structurant pour le livrable, supprimer sinon.
5. Extrais les entités conservées. NE REDESSINE AUCUN élément : la vue nettoyée est une extraction filtrée du fichier source, pas un redessin.
6. Nomme la vue nettoyée selon la convention : {{code_livrable}}_VUE-NETTOYEE_{{indice_livrable}}.dxf (ou .pdf, .png).
7. Consigne au RDL : livrable, source utilisée, calque de nettoyage, version. Consigne au journal OUT-03 les comptages par classe (PORTEUR CERTAIN / NON PORTEUR / À LEVER), les seuils GEO-10/GEO-11 utilisés et les arbitrages reçus.


MISE À JOUR INCRÉMENTALE (cas de modification)
Si une modification est découverte (source corrigée, calage corrigé, livrable corrigé) :
1. Consulte le RDL pour identifier les livrables impactés.
2. Pour chaque livrable impacté, régénère la vue nettoyée depuis le fichier source mis à jour.
3. Ne régénère JAMAIS les vues nettoyées des livrables non impactés.
4. Consigne la mise à jour au RDL (indice précédent, indice nouveau, motif, date).


INTERDICTIONS
- Ne redessine AUCUN élément : la vue nettoyée est une extraction filtrée du fichier source, jamais un redessin.
- Ne conserve pas un calque « au cas où » : si l'élément n'est pas nécessaire au livrable, il est supprimé.
- N'utilise jamais une vue nettoyée d'un livrable pour un autre livrable : chaque livrable a la sienne.
- Ne régénère pas toutes les vues nettoyées du projet sur une modification ponctuelle : tu identifies d'abord les livrables impactés via le RDL.
- Ne nomme pas les vues nettoyées de façon libre : tu utilises la convention {{code_livrable}}_VUE-NETTOYEE_{{indice_livrable}}.
- Ne mélange pas la vue nettoyée et le livrable : la vue nettoyée est un fond de plan, pas un plan d'exécution.


SORTIE
Pièce 1 — Vue nettoyée
Fichier DXF ou PDF + PNG, nommé selon la convention, avec la liste des calques conservés/supprimés/à trancher.


Pièce 2 — Tableau de nettoyage
Calque ou entité | Statut (conservé / supprimé / à trancher) | Justification | Livrable concerné


Pièce 3 — Consignation RDL
Ligne du RDL pour ce livrable : source utilisée (fichier + indice), version du calage B-30, version de la vue nettoyée, indice du livrable, date.


CRITÈRE D'ACCEPTATION
La vue nettoyée est acceptée si :
- la vue est une extraction filtrée du fichier source calé, sans redessin ;
- chaque calque ou entité a un statut explicite et une justification ;
- le nom respecte la convention ;
- la vue est propre au livrable (pas réutilisée d'un autre livrable) ;
- le RDL est mis à jour avec la ligne correspondante ;
- en cas de mise à jour incrémentale, seuls les livrables impactés ont été régénérés.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{indice_livrable}} et {{mode}} (par COMPLET ou PARTIEL-DÉCLARÉ). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Vue nettoyée par livrable | Votre choix — chaque livrable a ses propres besoins de fond de plan. Une vue unique oblige à conserver des éléments inutiles pour certains livrables (par exemple, les menuiseries sur un plan de fondations), et ne permet pas la mise à jour ciblée. La vue par livrable est plus légère (moins d'éléments) et plus maintenable (mise à jour ciblée) |
| Règles de nettoyage par livrable | Sans règles fixées, un modèle invente le nettoyage : il conserve les menuiseries sur un plan de fondations (parce que « c'est dans le DXF »), ou supprime des éléments structurants (parce qu'« ils ne sont pas porteurs »). Les règles écrites rendent le nettoyage reproductible — deux ingénieurs doivent aboutir au même résultat |
| « À TRANCHER » | Certains calques ne sont ni à conserver ni à supprimer dans l'absolu : la décision dépend du livrable. Par exemple, les trémies sont structurantes sur un plan de plancher, mais inutiles sur un plan de fondations. Les nommer explicitement évite les décisions implicites |
| « Extraction filtrée, jamais redessin » | Verrou V2 — la vue nettoyée n'invente rien, elle filtre. Un redessin introduit des erreurs invisibles : un mur dessiné légèrement décalé, une cote arrondie, une intersection mal recopiée. Ces erreurs sont indétectables sur la vue nettoyée — et se propagent au livrable |
| Mise à jour incrémentale + RDL | Votre règle : si on découvre une modification, on met à jour les livrables impactés, pas tout. Le RDL identifie les livrables impactés — sans lui, la règle est inapplicable, et la seule solution est de tout refaire |
| « Ne régénère jamais les vues non impactées » | Un modèle qui ne maîtrise pas la mise à jour incrémentale régénère tout — ce qui réintroduit des erreurs dans les livrables qui étaient bons (les paramètres de calage ont pu changer, ou le fichier source a été corrigé entre-temps, mais pas pour ce livrable). C'est l'inverse du résultat cherché |
| Convention de nommage | Le livrable et sa vue nettoyée doivent se retrouver par leur nom. Une convention libre casse la traçabilité — on ne sait plus quelle vue correspond à quel livrable |
| Consignation au RDL | La vue nettoyée doit être retrouvable quand une modification de source survient. Le RDL est ce qui permet de savoir quelle vue a été produite, à partir de quelle source, et à quelle version du calage |
| Tableau de nettoyage avec justification | Un calque « supprimé » sans justification est un calque qui peut être supprimé par erreur. La justification force le modèle à expliciter pourquoi un élément est conservé ou supprimé — et permet à un tiers de vérifier que la décision est correcte |

Les règles de nettoyage par livrable — précision utile :

| Livrable | Éléments conservés | Éléments supprimés |
| --- | --- | --- |
| FONDATIONS | Murs porteurs, refends, poteaux, semelles existantes, axes, cotations de position des appuis | Cloisons, menuiseries, revêtements, mobilier, fluides |
| PLANCHER | Murs porteurs, poteaux, profilés, appuis, axes, trémies et réservations | Tout élément du second œuvre (y compris menuiseries extérieures si non concernées) |
| CHARPENTE | Murs d'appui, pignons, fermes existantes, pannes, chevrons | Tout élément sous toiture sauf les appuis |
| VERTICAUX | Murs, poteaux, axes, ouvertures (baies et passages), attentes de fondations | Tout le second œuvre |
| PLAN DE PRINCIPE | Murs porteurs, axes, trames | Tout ce qui n'est pas porteur ou repère |

Le piège du « au cas où » : un modèle a tendance à conserver un calque « au cas où il serait utile ». C'est faux :
   * un calque conservé en trop encombre la vue, et masque les éléments essentiels ;
   * un calque conservé en trop perd son statut : on ne sait plus s'il est structurant ou non ;
   * un calque conservé en trop oblige à le supprimer plus tard — ce qui est un travail supplémentaire, et une source d'erreur.
La règle est simple : si l'élément n'est pas nécessaire au livrable, il est supprimé.
Le cas du PDF non vectoriel : si le fichier source est une image (PDF rasterisé, scan, JPEG), B-32 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité d'extraction filtrée. Le nettoyage est fait manuellement (par découpe des zones inutiles dans l'image), avec les limitations qui en découlent :
   * perte de la vectorisation (les cotes ne sont plus des objets, mais des pixels) ;
   * impossibilité de filtrer par calque ;
   * incertitude sur les positions (le calage est lui-même manuel).
La vue nettoyée en mode PARTIEL-DÉCLARÉ porte la mention « nettoyage manuel — calage partiel ».
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte du fichier source (DOC-02), ses calques ou entités |
| B-20 (Conception structure GO) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-30 (Calage sur dxf/dwg source) | Le fichier recalé — chaque vue nettoyée est extraite du fichier calé |
| B-31 (Preuve de superposition) | Le RDL — si une modification de source survient, les livrables avec preuve B-31 sont identifiés pour mise à jour |
| B-33 (Vérification croisée) | Le RDL — si une modification de source survient, les livrables avec vérification favorable sont identifiés pour mise à jour |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-25 (Stabilité globale, contreventement, joints) | Le fond structurel pur, support du schéma de contreventement |
| B-31 (Preuve de superposition) | La vue nettoyée — B-31 vérifie la cohérence livrable ↔ vue nettoyée |
| B-33 (Vérification croisée) | La vue nettoyée — B-33 compare le livrable à la vue nettoyée (section 1) |
| B-34 (Synthèse des réservations) | Le fond structurel pur sur lequel les réservations sont positionnées |
| B-60 (Plans d'exécution) | La vue nettoyée — B-60 produit le plan sur ce fond de plan |
| B-62 (Nomenclature et façonnage) | La vue nettoyée — B-62 s'appuie sur cette vue pour vérifier la cohérence |
| B-71 (Indiçage et supersession documentaire) | La vue nettoyée et son indice — consignés au RDL |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-32 |
| --- | --- | --- |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE (via B-30) |
| GEO-06 | Unités du fichier source | BLOQUANTE (via B-30) |
| GEO-10 | Seuils d'épaisseur de présomption porteuse (§R) | BLOQUANTE pour le §R (donnée FDC) |
| GEO-11 | Superposition des niveaux : recouvrement et écart d'axe (§R) | BLOQUANTE pour le §R (donnée FDC) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | NON BLOQUANTE (à défaut : PA-xx) |

Variables produites
B-32 ne produit pas de variable au sens du dictionnaire : sa sortie est un fichier (vue nettoyée) qui alimente B-60, B-31, B-33 et B-71.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-02, GEO-06, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-32, vous devez valider la liste des calques À TRANCHER. C'est votre appréciation de la nature du livrable qui fait foi — un élément peut être structurant sur un livrable et inutile sur un autre. Le modèle propose, vous décidez.
Cas particulier — plusieurs vues nettoyées pour un même livrable : si un livrable nécessite plusieurs vues nettoyées (par exemple, un plan de fondations qui s'étend sur plusieurs planches), chaque vue nettoyée est nommée avec un suffixe de planche : {{code_livrable}}_VUE-NETTOYEE_{{indice_livrable}}_{{num_planche}}.dxf. La règle de non-réutilisation reste la même : chaque vue nettoyée est propre à sa planche.
Cas particulier — calque À TRANCHER non résolu : si un calque reste À TRANCHER après la validation, il est conservé par défaut dans la vue nettoyée. Il sera tranché ultérieurement (par une nouvelle version de B-32, ou par une décision explicite). La conservation par défaut évite de supprimer un élément qui pourrait être structurant — c'est l'erreur la plus coûteuse.
Cas particulier — mise à jour incrémentale : si une modification est découverte (par exemple, le fichier source passe de l'indice B à l'indice C), B-32 est rappelée avec les mêmes paramètres. Elle consulte le RDL pour identifier les livrables impactés, puis :
   1. régénère uniquement les vues nettoyées des livrables impactés ;
   2. conserve les vues nettoyées des livrables non impactés ;
   3. consigne la mise à jour au RDL (indice précédent, indice nouveau, motif, date).
Cas particulier — modification de calage : si le calage (B-30) est modifié (par exemple, un recalage sur une nouvelle version du fichier source), toutes les vues nettoyées sont impactées — parce qu'elles sont toutes extraites du fichier calé. B-32 le signale et régénère toutes les vues nettoyées. C'est le seul cas où la mise à jour incrémentale est globale — et c'est pour cela que le calage est fait une fois (B-30), pas à chaque livrable.
Cas particulier — fichier source non vectoriel : si le fichier source est un PDF rasterisé (image), B-32 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité d'extraction filtrée. Le nettoyage est manuel, la vue nettoyée porte la mention « nettoyage manuel — calage partiel ».
Cas particulier — vue nettoyée pour la preuve de superposition (B-31) : si la vue nettoyée est produite spécifiquement pour la preuve de superposition B-31, elle peut inclure des éléments supplémentaires (par exemple, les cotes des éléments existants, pour mesurer l'écart). Dans ce cas, le nommage est : {{code_livrable}}_VUE-NETTOYEE-PREUVE_{{indice_livrable}}.dxf. La distinction permet de ne pas confondre la vue nettoyée « production » et la vue nettoyée « preuve ».
Format de sortie attendu : trois pièces distinctes (vue nettoyée, tableau de nettoyage, consignation RDL). La vue nettoyée est fournie en DXF et PDF + PNG — le DXF pour les outils, le PDF pour l'archivage, le PNG pour insertion.
Consignation : la vue nettoyée est versionnée avec le livrable et consignée au RDL (source utilisée, version du calage, indice de la vue, date). C'est cette consignation qui permet la mise à jour incrémentale en cas de modification.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

## COMPLÉMENT v2.1 — §R. PROTOCOLE DE RECONNAISSANCE DES PORTEURS (obligatoire avant tout nettoyage B-32)

### R.1 Objet et champ d'application
Le nettoyage B-32 filtre un fichier ; il ne sait pas, à lui seul, distinguer un porteur d'une cloison lorsque le fichier source ne les sépare pas. Le présent protocole produit, **avant** le filtrage, la classification des parois et poteaux du fichier calé (B-30) en trois classes — PORTEUR CERTAIN, NON PORTEUR, À LEVER — qui devient l'entrée du nettoyage.
Il est **obligatoire** dès que l'une de ces conditions est remplie : les calques du fichier mélangent parois porteuses et cloisons ; la sémantique des calques est absente, incohérente ou invérifiable ; aucun plan BET ne désigne les porteurs. Si le fichier sépare déjà explicitement les porteurs (calques dédiés dont la sémantique est vérifiée sur les cotes et les annotations), le protocole se réduit aux temps R.2, R.6 et R.7 (contrôle et consignation).

### R.2 Temps 1 — Inventaire des entités (script, annexe O)
Le script (OUT-02) énumère, par niveau : entités par calque et par type (lignes, polylignes ouvertes/fermées, hachures, blocs éclatés virtuellement), épaisseurs de trait, textes et annotations. Il produit le tableau d'inventaire (OUT-03) : calque | type | nombre | rôle supposé | indices de sémantique (nom de calque, annotations rencontrées). Aucune classification n'est faite à ce stade.

### R.3 Temps 2 — Reconstruction des parois
Le script reconstruit les parois élémentaires : appariement des lignes parallèles et des polylignes fermées, mesure de l'**épaisseur** de chaque tronçon (distance entre faces), segmentation aux intersections et aux ouvertures. Chaque paroi reçoit un identifiant (niveau, repère, position, longueur, épaisseur mesurée). Les poteaux sont détectés comme rectangles fermés de faible développement, pleins ou hachurés, notamment aux intersections de parois.

### R.3bis Chaînage des tronçons en parois (obligatoire — enseignement v2.2)
La classification ne porte jamais sur des tronçons isolés : elle porte sur des **parois chaînées**. Avant les critères (R.4), le script chaîne les tronçons :
1. **Segmentation** : les tronçons sont coupés à chaque intersection (croisement, jonction en T, angle) et à chaque ouverture détectée.
2. **Regroupement** : les tronçons colinéaires ou quasi colinéaires (écart angulaire ≤ 2°, écart d'axe ≤ 2 cm) séparés par moins de 5 cm sont fusionnés en un même alignement.
3. **Appariement des faces** : les alignements parallèles distants de l'épaisseur mesurée (moins de 5 % d'écart sur la longueur commune) sont appariés comme les deux faces d'une même paroi ; l'épaisseur de la paroi est la médiane des distances mesurées, et non une valeur par tronçon.
4. **Objet paroi** : chaque paroi reçoit un identifiant unique (niveau, repère), sa longueur cumulée, son épaisseur médiane, ses faces, ses ouvertures et ses éléments associés (jambages aux extrémités des baies, poteaux incorporés détectés en R.3). Une paroi interrompue par une baie est une seule paroi avec ouverture, pas trois tronçons.
5. **Cas non chaînables** : un tronçon qui ne peut être ni regroupé ni apparié (géométrie dégradée, arc, tracé libre) reste un élément isolé, classé au plus À LEVER, et signalé dans le journal OUT-03.
C'est l'objet paroi — pas le tronçon — qui est évalué par les critères C1 à C6, porté au tableau de reconnaissance et rendu sur le plan de contrôle.



### R.4 Temps 3 — Critères de reconnaissance (convergence obligatoire)
Chaque paroi est évaluée sur les critères suivants. **Aucun critère seul ne classe.**

| N° | Critère | Mesure (script) | Signal porteur | Signal non porteur |
|---|---|---|---|---|
| C1 | Source BET | Le plan structure (DOC-03) désigne-t-il cette paroi ? | Désignée : critère souverain (V1) | — |
| C2 | Épaisseur | Épaisseur mesurée vs seuils GEO-10 | ≥ seuil haut de présomption | ≤ seuil bas (cloison) |
| C3 | Superposition des niveaux | Recouvrement de l'empreinte entre niveaux successifs (longueur commune / longueur, écart maximal) vs GEO-11 | Paroi retrouvée aux niveaux adjacents dans la tolérance | Paroi propre à un seul niveau |
| C4 | Schéma statique | Continuité vers le bas (paroi, poteau, semelle au niveau inférieur), alignement avec fondations/poutres, portées résultantes | Chaîne d'appuis complète, portées plausibles au regard du plancher | Paroi « en l'air », portée résultante incohérente |
| C5 | Position et fonction | Façade, refend, noyau (escalier, ascenseur, gaines structurantes), mitoyenneté | Position structurante | Division intérieure d'un local |
| C6 | Indices graphiques | Hachure (pleine/dense = matériau structurel), épaisseur de trait, calque, annotations (« refend », « voile », « porteur »), baies avec jambages | Indices concordants | Cloison légère, doublage, menuiserie |

Seuils de projet (FDC, jamais des constantes du carnet) :
- **GEO-10** — seuils d'épaisseur de présomption : seuil bas (au plus : cloison présumée) et seuil haut (à partir de : porteur présumé), fixés selon l'époque et le système constructif (à titre de repère à valider par projet : cloison ≤ 10 cm ; zone indéterminée 10–18 cm ; présomption porteuse ≥ 18 cm ; murs anciens : seuils spécifiques déclarés).
- **GEO-11** — superposition : recouvrement minimal (repère : 80 % de la longueur) et écart maximal d'axe entre niveaux (repère : 5 cm en régulier ; valeur déclarée en existant irrégulier).
Entre le seuil bas et le seuil haut de GEO-10, le critère C2 est neutre : la classification repose sur C3, C4, C5, C6.


### R.4bis Projection automatique des porteurs BET (critère C1 — enseignement v2.2)
Lorsqu'un plan de structure existe (DOC-03) sous forme vectorielle (DXF/DWG ou PDF vectoriel), le critère C1 n'est pas apprécié « à l'œil » : il est **projeté géométriquement**.
1. **Extraction** : le script extrait du plan BET la géométrie de ses porteurs (calques structure, traits forts, hachures béton, symboles de poteaux/jambages) selon la même méthode d'inventaire que R.2.
2. **Recalage** : la géométrie BET est recalée sur le repère du fichier calé (B-30) par la transformation du plan BET s'il en existe une, sinon par au moins trois points communs identifiés (angles, axes) avec résidu consigné ; à défaut de recalage fiable, la projection est déclarée impossible et C1 repasse en appréciation humaine tracée.
3. **Appariement** : chaque paroi chaînée (R.3bis) est appariée aux porteurs BET par recouvrement (distance d'axe ≤ tolérance GEO-11, recouvrement de longueur ≥ 50 %). Une paroi appariée reçoit C1 positif → PORTEUR CERTAIN (sauf contradiction majeure signalée).
4. **Écarts obligatoirement signalés** : tout porteur BET sans paroi archi correspondante, et toute paroi archi épaisse et superposée (C2/C3 favorables) non désignée par le BET, sont listés comme **écarts de projection** dans le tableau de reconnaissance et renvoyés à B-13/B-33 — jamais appariés de force.
5. **Cas non vectoriel** : si le plan BET n'existe qu'en raster, la projection est manuelle et déclarée (mode PARTIEL-DÉCLARÉ) ; les porteurs reportés sont qualifiés « de principe » jusqu'à validation humaine à la porte B-32.

### R.5 Temps 4 — Règle de classification
- **PORTEUR CERTAIN** : C1 positif ; ou convergence d'au moins trois critères favorables dont C3 ou C4.
- **NON PORTEUR** : C2 bas **et** C3 négatif **et** C4 sans fonction d'appui ; aucun indice contraire (C5, C6).
- **À LEVER** : tout le reste — signaux contradictoires, données insuffisantes, paroi épaisse non superposée, paroi mince en position d'appui, poteau isolé sans chaîne d'appuis lisible.
La classification est produite paroi par paroi dans le **tableau de reconnaissance** : repère | niveau | épaisseur mesurée | superposition (C3) | appui (C4) | autres indices | classe | justification. Un **plan de contrôle** rend les trois classes dans trois couleurs, superposé au fichier source.

### R.6 Temps 5 — Porte humaine et traitement des À LEVER
La liste À LEVER est soumise à l'utilisateur à la porte B-32, élément par élément, avec les signaux contradictoires. L'arbitrage est consigné (RDR ou note d'hypothèses B-22). Tant qu'un élément À LEVER n'est pas arbitré, il est **conservé** dans la vue nettoyée, en gris sur le calque EXISTANT : on ne supprime jamais un porteur possible. Si l'arbitrage est impossible sur pièces et que l'élément est dimensionnant, la brique renvoie à B-24 (existant non sondé) ou à un sondage — elle ne tranche pas.

### R.7 Temps 6 — Nettoyage et consignation
Le filtrage B-32 proprement dit s'applique alors aux classes : PORTEUR CERTAIN conservé ; NON PORTEUR supprimé selon la règle du livrable ; À LEVER conservé en EXISTANT. Le journal OUT-03 consigne les comptages par classe et par calque, les seuils GEO-10/GEO-11 utilisés et les arbitrages. B-31 vérifie ensuite qu'aucun PORTEUR CERTAIN ne manque à la vue nettoyée ; B-33 la confronte aux livrables voisins.

### R.8 Cas dégradés et interdictions
- Fichier non vectoriel (raster) : pas de reconnaissance automatique ; mode PARTIEL-DÉCLARÉ, nettoyage manuel déclaré, mention portée sur la vue.
- Il est interdit de classer sur la seule continuité géométrique d'un segment (annexe O §4.4), sur la seule sémantique d'un nom de calque non vérifiée, ou sur un seuil d'épaisseur importé d'un autre projet.
- Il est interdit de supprimer un élément À LEVER non arbitré, et de présenter le plan de contrôle des classes comme un plan de structure : c'est une pièce de travail, pas un livrable BET.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Loi d'airain graphique.** La vue nettoyée supprime 100 % des cloisons, doublages, isolants, complexes de finition et menuiseries de distribution. Seuls subsistent : les porteurs (existants, conservés, démolis, neufs), les ouvertures mécaniques (baies, trémies, percements), la trémie et l'escalier, la structure neuve et les réservations techniques.

**Protocole CAO obligatoire en quatre temps.** (1) `INSERT` récursif multi-calques : reconnaissance des blocs imbriqués et reclassement des porteurs sur le calque structurel avant toute purge ; (2) retrait du complexe isolant et des doublages périphériques (décalage d'épaisseur vers le nu porteur) ; (3) purge spatiale des portes, cotes et hachures orphelines par distance aux segments porteurs ; (4) table explicite de correspondance `Plan Archi N ↔ PB/PH` et `nu brut ASB / nu fini` (`NIV-07`).

**Différentiel explicite.** La vue porte trois états graphiques distincts et lisibles (`EXISTANT` gris fin, `DÉMOLITION` pointillé, `PROJET` trait fort) et une légende normalisée. Une vue sans différentiel exploitable est refusée.
**[Fin de 05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md]**

---

**[Début du fichier : 05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md]**

Fichier 05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md — CARNAC v3.0
________________


B-31 — PREUVE DE SUPERPOSITION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 1 — Socle géométrique et nettoyage |
| Brique précédente | B-30 (Calage) — et la brique qui a produit le livrable à vérifier (B-20, B-40 à B-50, B-60) |
| Brique suivante | B-33 (Vérification croisée) |
| Fréquence | À chaque livrable graphique — le livrable repose sur une superposition qui doit être prouvée |
| Modes d'appel | COMPLET (calage B-30 disponible et livrable graphique produit) · PARTIEL-DÉCLARÉ (calage en mode dégradé : la preuve est fournie avec les réserves du calage) |
| Entrées lues | Paramètres de calage B-30, livrable graphique concerné, vue nettoyée B-32 utilisée |
| Sortie unique | Preuve de superposition propre au livrable : image annotée + tableau de contrôle des positions + verdict global |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : à chaque livrable graphique produit — plans d'exécution (B-60), plans de calcul (B-40 à B-50), plans de principe (B-20). La preuve de superposition est la seule démonstration que ce que nous avons ajouté tombe sur les positions réelles.
Ce que vous fournissez à l'IA : le fichier source calé (B-30), le livrable à vérifier, la vue nettoyée (B-32) utilisée pour ce livrable. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{code_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * le tableau de contrôle élément par élément (positions prévue vs mesurée, écart, verdict) ;
   * la superposition annotée au zoom réel du livrable ;
   * les écarts (signalés, non corrigés dans la preuve) ;
   * le verdict global (livrable validé / validé sous réserve / à corriger).
Ce que B-31 apporte de spécifique — la preuve par superposition :

| Aspect | B-30 (calage) | B-31 (preuve de superposition) |
| --- | --- | --- |
| Objet | Établir la transformation entre le fichier source et notre repère | Prouver que chaque ajout du livrable tombe au bon endroit |
| Fréquence | Une fois par projet | À chaque livrable |
| Sortie | Paramètres de calage + fichier recalé | Tableau de contrôle + superposition annotée |
| Contrôle | Résidu global sur points témoins | Vérification élément par élément |

La règle la plus importante : B-31 ne corrige aucun écart dans la preuve. Elle signale l'écart, identifie la cause probable, et renvoie la correction à la brique source (B-20, B-40 à B-50, B-60). Une preuve qui corrige n'est plus une preuve — c'est une version corrigée non tracée.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la preuve de superposition du livrable graphique {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, c'est-à-dire la démonstration que les éléments que nous avons ajoutés (porteurs, renforts, semelles, poteaux) tombent sur les positions réelles du fichier source calé en B-30.


MÉTHODE
1. Reprends le fichier source calé (B-30) et le livrable graphique à vérifier.
2. Superpose-les au même zoom, avec un code couleur lisible : source en gris fin, ajouts en couleur vive.
3. Vérifie les positions élément par élément, selon la nature du livrable :
   - poteaux : le symbole est-il centré sur le mur, le refend ou l'axe de trame ?
   - poutres et profilés : chaque extrémité aboutit-elle sur un appui réel (mur, poteau, sommier) ? Aucun about dans le vide ?
   - semelles : chaque semelle est-elle centrée sur son mur, avec débord de part et d'autre ? Aucune semelle flottante ?
   - ouvertures : les baies et passages sont-ils aux bonnes positions ?
4. Produis un TABLEAU DE CONTRÔLE : chaque élément ajouté, sa position prévue, sa position mesurée sur la superposition, l'écart, le verdict (conforme / écart acceptable / écart à corriger).
5. Si un écart est détecté, tu ne le corriges pas dans la preuve : tu le signales, tu identifies la cause probable (calage, saisie, saisie de la donnée), et tu renvoies la correction à la brique qui a produit le livrable (B-20, B-40 à B-50, B-60).
6. La preuve est annexée au livrable et consignée dans le RDL.


INTERDICTIONS
- Ne produis pas la preuve sur un zoom qui masque les écarts : tu produis au zoom réel du livrable, plus des zooms sur les points singuliers si nécessaire.
- Ne corrige AUCUN écart dans la preuve : tu le signales et tu renvoies la correction à la brique source.
- N'utilise pas le fichier source non calé : la preuve se fait sur le fichier calé B-30.
- Ne valide pas une preuve sans tableau de contrôle élément par élément.
- Ne déclare pas un élément « conforme » sans mesure d'écart.
- Ne produis pas la preuve en mode PARAMÉTRIQUE : soit le calage est disponible, soit le livrable ne peut pas être vérifié (et le livrable est suspendu).


SORTIE
Pièce 1 — Superposition annotée
Image PDF + PNG, au zoom réel, avec code couleur source/ajouts, et zooms sur les points singuliers.


Pièce 2 — Tableau de contrôle
Élément ajouté | Position prévue | Position mesurée | Écart | Verdict | Cause probable si écart | Brique à corriger


Pièce 3 — Synthèse
Nombre d'éléments contrôlés | Nombre conformes | Nombre d'écarts acceptables | Nombre d'écarts à corriger | Livrable validé (Oui / Non) | Si Non, briques à reprendre.


CRITÈRE D'ACCEPTATION
La preuve est acceptée si :
- la superposition est produite au zoom réel du livrable ;
- le tableau de contrôle couvre TOUS les éléments ajoutés ;
- chaque élément a une mesure d'écart (pas un simple « conforme ») ;
- les écarts sont signalés sans être corrigés dans la preuve ;
- la synthèse indique le verdict global et les briques à reprendre ;
- la preuve est annexée au livrable et consignée au RDL.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{code_livrable}} et {{mode}} (par COMPLET ou PARTIEL-DÉCLARÉ). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| À chaque livrable graphique | Un livrable sans preuve de superposition est un livrable dont on ne sait pas s'il est calé. La preuve est la seule protection contre les erreurs de position — et les erreurs de position sont les plus coûteuses, parce qu'elles sont invisibles sur le livrable lui-même (un poteau dessiné à 10 cm de son mur paraît juste si on ne superpose pas) |
| Tableau de contrôle élément par élément | Une superposition visuelle sans mesure est une impression. Le tableau transforme la preuve en contrôle mesuré, opposable. Sans tableau, on ne peut pas dire « ce poteau est conforme » — on peut seulement dire « il a l'air bien placé » |
| « Ne corrige aucun écart dans la preuve » | Une preuve qui corrige n'est plus une preuve : c'est une version corrigée non tracée. La preuve constate, la brique source corrige. Si la preuve corrige, on ne sait plus quelle version du livrable est la bonne — et la traçabilité est rompue |
| « Cause probable si écart » | Un écart sans diagnostic de cause se reproduit. La cause identifiée (calage ? saisie ? donnée ?) permet de corriger la méthode, pas seulement l'occurrence — et donc d'éviter que le même écart ne réapparaisse sur le livrable suivant |
| « Pas de preuve en PARAMÉTRIQUE » | Un livrable PARAMÉTRIQUE (filigrané, non exécutable) n'a pas à être vérifié en position — il n'est pas exécutable. La preuve ne s'applique qu'aux livrables produits en COMPLET ou PARTIEL-DÉCLARÉ |
| Zoom réel du livrable | Un zoom sur un détail peut masquer des écarts ailleurs. La preuve doit être produite au zoom réel du livrable (celui de la production), plus des zooms sur les points singuliers si nécessaire — mais jamais seulement des zooms |
| Consignation au RDL | La preuve doit être retrouvable quand une modification de source survient — c'est ce qui permet de savoir quels livrables doivent être reprouvés. Sans RDL, la preuve est un document isolé, qui ne sert à rien en cas de modification |
| Verdict global explicite | Un tableau sans verdict est un tableau qui laisse la décision au lecteur. Le verdict global (validé / validé sous réserve / à corriger) est la conclusion de la preuve — sans lui, la preuve n'est pas actionnable |
| Synthèse quantitative | Le nombre d'éléments contrôlés, conformes, en écart acceptable, à corriger, donne une vue d'ensemble que le tableau détaillé ne donne pas. C'est ce qui permet de décider si le livrable est globalement bon ou globalement mauvais |

Les trois verdicts possibles — précision utile :

| Verdict | Définition | Conséquence |
| --- | --- | --- |
| Conforme | Écart mesuré ≤ tolérance de position (généralement 2 cm à l'échelle du bâtiment) | L'élément est validé |
| Écart acceptable | Écart > tolérance, mais justifié par une contrainte (par exemple, un décalage de 5 cm pour éviter une réservation existante) | L'élément est validé avec mention de l'écart et de sa justification |
| Écart à corriger | Écart > tolérance, non justifié | L'élément est refusé — la brique source doit corriger |

Les trois causes probables d'écart — précision utile :

| Cause | Définition |
| --- | --- |
| Action | Calage |
| L'écart vient du calage (B-30) — la transformation entre le fichier source et notre repère est fausse | Recalculer le calage (B-30) |
| Saisie | L'écart vient de la production du livrable — la brique source a mal saisi la position |
| Corriger le livrable (brique source) | Donnée |
| L'écart vient de la donnée d'entrée — la position de l'élément dans le fichier source est fausse, ou la contrainte de conception est mal transcrite | Corriger la donnée (FDC ou B-20), puis régénérer le livrable |

Le piège du « c'est juste à quelques centimètres » : un écart de 5 cm sur un poteau peut paraître négligeable — sauf si ce poteau tombe sur une réservation existante, ou si l'écart cumulé sur plusieurs poteaux crée une trame fausse. La tolérance de position doit être fixée à l'avance (généralement 2 cm), et tout écart au-delà doit être justifié explicitement — pas implicitement accepté.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-20 (Conception structure GO) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-30 (Calage sur dxf/dwg source) | Le fichier recalé — chaque preuve de superposition se fait sur le fichier calé, pas sur le fichier source brut |
| B-32 (Vue nettoyée par livrable) | La vue nettoyée — B-31 vérifie la cohérence livrable ↔ vue nettoyée |
| B-40 (Fondations superficielles) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-41 (Fondations profondes) | Le livrable à vérifier et les positions prévues |
| B-42 (Verticaux BA) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-43 (Planchers et dallages) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-44 (Charpente bois) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-45 (Structure métallique) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-46 (Maçonnerie : vérification) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-47 (Escaliers) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-48 (Prédalles et planchers préfabriqués) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-49 (Linteaux et seuils) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-50 (Assemblages et ancrages) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-60 (Plans d'exécution) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| T-02 (Prompt de recadrage) | La preuve de correction — B-31 vérifie que la correction est effective |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-32 (Vue nettoyée par livrable) | Le RDL — si une modification de source survient, les livrables avec preuve B-31 sont identifiés pour mise à jour |
| B-33 (Vérification croisée) | La preuve de superposition — B-33 vérifie la cohérence plan ↔ source (section 1) en s'appuyant sur la preuve B-31 |
| B-70 (Auto-contrôle déclaré de synthèse) | Le verdict de la preuve — B-70 vérifie que chaque livrable a sa preuve et que le verdict est favorable |
| B-71 (Indiçage et supersession documentaire) | La preuve annexée au livrable — chaque livrable est indiçable avec sa preuve |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-31 |
| --- | --- | --- |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE (via B-30) |
| GEO-07 | Transformation du fichier | BLOQUANTE (via B-30) |
| GEO-08 | Points de calage identifiés | BLOQUANTE (via B-30) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |

Variables produites
B-31 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (preuve de superposition) qui alimente B-33, B-70, B-71 et B-32.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-02, GEO-07, GEO-08, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats (PDF + PNG) | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-31, vous devez valider le verdict global avant de diffuser le livrable. Un livrable avec un verdict « à corriger » ne doit pas être diffusé — il doit être repris par la brique source. Un livrable avec un verdict « validé sous réserve » peut être diffusé, mais les écarts acceptables doivent être justifiés explicitement.
Cas particulier — livrable avec écart de calage : si l'écart vient du calage (B-30), la preuve B-31 est fausse par construction — elle mesure un écart qui n'existe pas dans le livrable. B-31 le signale et renvoie à B-30 pour recalculer le calage. La preuve est alors suspendue jusqu'à ce que le calage soit corrigé.
Cas particulier — livrable avec plusieurs types d'éléments : si le livrable contient plusieurs types d'éléments (semelles + poteaux + profilés), B-31 vérifie chaque type avec les critères qui lui sont propres :
   * semelles : centrage sur le mur, débord équilibré ;
   * poteaux : centrage sur le mur ou sur l'axe de trame ;
   * profilés : about sur un appui réel, pas dans le vide ;
   * ouvertures : position par rapport aux murs.
Chaque type a ses critères — un seul critère global masque les écarts spécifiques.
Cas particulier — livrable avec erreur de saisie détectée : si un écart est détecté et que la cause est une saisie (par exemple, un poteau saisi à 4,50 m au lieu de 4,00 m), B-31 identifie l'écart et le renvoie à la brique source. La correction est faite par la brique source, pas par B-31 — et la preuve est refaite après correction.
Cas particulier — livrable avec erreur de donnée : si l'écart vient d'une donnée fausse (par exemple, une position de poteau mal transcrite dans la FDC), B-31 identifie l'écart, mais la correction ne relève pas de la brique source du livrable — elle relève de la FDC (B-02) ou de B-20 (conception). B-31 le signale avec la brique à corriger appropriée.
Cas particulier — zoom réel vs zoom détail : B-31 exige une preuve au zoom réel du livrable. C'est souvent insuffisant pour voir les écarts faibles (par exemple, un poteau décalé de 2 cm). B-31 produit donc des zooms complémentaires sur les points singuliers :
   * les appuis (about de profilé, sommier, semelle) ;
   * les passages (baies, trémies) ;
   * les angles (coins de murs, intersections de refends).
Les zooms complètent la preuve au zoom réel, ils ne la remplacent pas.
Cas particulier — livrable en cours de production : si le livrable est en cours de production (par exemple, un plan B-60 en cours de finalisation), B-31 n'est pas appelée. La preuve ne s'applique qu'aux livrables terminés — une preuve sur un livrable inachevé est une preuve de l'état courant, pas du livrable final.
Format de sortie attendu : trois pièces distinctes (superposition annotée, tableau de contrôle, synthèse). La superposition est fournie en PDF et PNG — le PDF pour l'archivage, le PNG pour insertion dans les comptes rendus. Le tableau de contrôle couvre tous les éléments ajoutés, sans exception.
Consignation : la preuve B-31 est annexée au livrable (dans le PDF du livrable ou dans un document séparé référencé) et consignée au RDL (avec la date, l'indice du livrable, le verdict).
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Preuve de superposition multi-étages et multi-sources.** La preuve ne se limite plus au fichier architecte : elle superpose, niveau par niveau, `EXISTANT`, `DÉMOLITION` et `PROJET`, ainsi que la source structure MOE transcrite. Elle détecte les **porteurs non portés** : mur ou poteau interrompu entre deux niveaux sans ouvrage de transfert, ce qui constitue une non-conformité `V15` à corriger avant tout calcul.
**[Fin de 05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md]**

<!-- FIN DU PACK — CARNAC v3.0 -->
