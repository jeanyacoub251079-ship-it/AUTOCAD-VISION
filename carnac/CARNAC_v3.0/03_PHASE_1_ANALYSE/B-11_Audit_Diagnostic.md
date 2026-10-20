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