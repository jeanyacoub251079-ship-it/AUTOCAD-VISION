Fichier 09_TRANSVERSE/T-01_Sincerite.md — CARNAC v3.0
________________


T-01 — PROMPT DE SINCÉRITÉ
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | Transverse — à tout moment |
| Brique précédente | Aucune (T-01 s'applique à n'importe quel livrable, à n'importe quel moment) |
| Brique suivante | T-02 (recadrage) si un défaut est détecté — sinon retour à la phase en cours |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | Le dernier livrable produit (plan, note de calcul, nomenclature, notice, ou tout document émis) |
| Sortie unique | Tableau « certain / de principe / à lever » + verdict de sincérité + recommandations |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * après chaque production graphique importante (plan d'exécution, note de calcul, nomenclature) ;
   * après chaque note de calcul ;
   * en cas de doute sur la fiabilité d'un livrable ;
   * avant transmission à un tiers (MOE, BC, entreprise).
Ce que vous fournissez à l'IA : le livrable à vérifier (plan, note, nomenclature, notice) et éventuellement la note de calcul ou la FDC de référence. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{code_livrable}}.
Ce que vous validez à la sortie :
   * le tableau détaillé (chaque élément classé : certain / de principe / à lever) ;
   * le verdict de sincérité (sincère / non sincère) ;
   * les recommandations pour chaque élément à lever (cause probable, brique CARNAC à exécuter, échéance).
Ce que T-01 apporte de spécifique — le test de sincérité :

| Aspect | Auto-contrôle de brique (B-40 à B-50) | T-01 (sincérité) |
| --- | --- | --- |
| Objet | Vérifier la conformité technique | Vérifier la sincérité — ce qui est affirmé est-il sourcé ? |
| Périmètre | Une brique | N'importe quel livrable, à n'importe quel moment |
| Sortie | Verdict technique (conforme / à corriger) | Tableau certain / de principe / à lever + verdict de sincérité |
| Angle | « Le livrable est-il correct ? » | « Le livrable est-il honnête sur ce qu'il affirme ? » |
| Protection | Protège contre les erreurs techniques | Protège contre les affirmations non fondées |

T-01 est la brique qui a produit l'aveu structuré dans la conversation d'origine — elle force le modèle à distinguer explicitement ce qui est sourcé et vérifié de ce qui est choisi ou estimé. C'est ce qui a permis la reprise du projet Flora.
Les trois catégories — précision utile :

| Catégorie | Définition | Conséquence |
| --- | --- | --- |
| CERTAIN | L'élément est explicitement rattaché à une source citée (fichier + folio + indice) ou à un calcul tracé dans la note de calcul | Peut être affirmé dans le livrable |
| DE PRINCIPE | L'élément est un choix de conception ou une valeur approchée, explicitement déclaré comme tel dans le livrable | Doit être mentionné comme tel (mention « de principe » ou « sous hypothèse H-xx ») |
| À LEVER | L'élément est présent dans le livrable sans source et sans déclaration de principe — il a été inventé, estimé ou recopié sans traçabilité | Ne doit pas être affirmé dans le livrable — il doit être levé (par une source ou par une déclaration) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : effectuer le test de sincérité du livrable {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}. Tu réponds en toute franchise : ce livrable est-il conforme aux sources, ou contient-il des éléments inventés, estimés, ou non rattachés à une source ?


MÉTHODE


Étape 1 — Inventaire exhaustif des éléments du livrable
Liste TOUS les éléments du livrable : positions, cotes, sections, ferraillages, hypothèses, choix, mention de matériaux.


Étape 2 — Classement en trois catégories
Pour chaque élément, classe-le dans l'une des trois catégories :
- CERTAIN : l'élément est explicitement rattaché à une source citée (fichier + folio/page + indice) ou à un calcul tracé dans la note de calcul.
- DE PRINCIPE : l'élément est un choix de conception ou une valeur approchée, explicitement déclaré comme tel dans le livrable.
- À LEVER : l'élément est présent dans le livrable sans source et sans déclaration de principe — c'est-à-dire qu'il a été inventé, estimé ou recopié sans traçabilité.


Étape 3 — Tableau de synthèse
Tableau : élément | catégorie (certain / de principe / à lever) | justification (source citée, ou déclaration, ou absence de source).


Étape 4 — Verdict de sincérité
- Si tous les éléments sont certains ou de principe : verdict « sincère ».
- Si un ou plusieurs éléments sont à lever : verdict « non sincère », avec la liste des éléments à lever et la gravité (bloquante / à lever avant transmission / à surveiller).


Étape 5 — Recommandation
Pour chaque élément à lever :
- cause probable (brique source non exécutée, hypothèse non déclarée, données manquantes) ;
- brique CARNAC à exécuter pour le lever ;
- échéance.


INTERDICTIONS
- Ne justifie aucun élément à lever par « c'est une pratique courante » ou « c'est comme d'usage » : ces formulations sont précisément les symptômes d'un élément à lever.
- Ne requalifie pas un élément à lever en élément de principe après coup : le classement est fait avant le verdict, pas après.
- Ne minimise pas le nombre d'éléments à lever pour « faire propre » : c'est le contraire de l'objectif.
- Ne produis pas de verdict sans le tableau détaillé.


SORTIE
Pièce unique — Tableau détaillé + verdict + recommandations.


CRITÈRE D'ACCEPTATION
Le test est accepté si :
- chaque élément du livrable figure dans le tableau ;
- chaque élément est classé en certain / de principe / à lever ;
- chaque élément a une justification (source ou absence de source) ;
- le verdict est explicite et cohérent avec le tableau ;
- chaque élément à lever a une cause probable et une brique CARNAC pour le lever.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{code_livrable}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Ne justifie pas un élément à lever par "pratique courante" » | C'est exactement la formulation qui produit les livrables non sincères : une valeur estimée « comme d'usage » qui n'est pas déclarée comme telle. C'est la faille du projet Flora (40 mm d'enrobage « au titre des exigences de tenue au feu » sans que ces exigences existent) |
| « Classement fait avant verdict » | Empêche le modèle de « réinterpréter » un élément à lever après coup pour le requalifier en élément de principe. Le classement doit être objectif — le verdict vient après, pas avant |
| « Ne minimise pas le nombre » | La tentation naturelle d'un modèle est de trouver peu d'éléments à lever. Le prompt force la rigueur — un livrable sincère peut avoir 0 élément à lever, mais il ne peut pas avoir 0 élément à lever par construction |
| Tableau obligatoire | Un verdict sans tableau est un avis. Le tableau est la preuve de la sincérité du test — il permet à un tiers de vérifier que chaque élément a été classé |
| Trois catégories seulement | Sans cette limite, un modèle produit des catégories intermédiaires (« plutôt certain », « probablement de principe ») qui ne sont pas des catégories mais des hésitations. Trois catégories forcent la clarté |
| CERTAIN = source citée | Verrou V2 — un élément qui n'est pas rattaché à une source ne peut pas être affirmé comme certain. La citation (fichier + folio + indice) est la seule preuve de certitude |
| DE PRINCIPE = déclaré comme tel | Un élément de principe qui n'est pas déclaré dans le livrable devient un élément à lever — c'est la règle qui garantit la traçabilité. Un modèle qui « oublie » de déclarer un choix de conception produit un livrable non sincère |
| Recommandation avec brique CARNAC | Un élément à lever sans brique CARNAC pour le lever est un élément qui reste à lever indéfiniment. La recommandation rend le test actionnable — elle identifie l'action à faire pour lever l'élément |
| « Ne produis pas de verdict sans le tableau » | Un verdict sans tableau est une affirmation, pas un test. Le tableau est la preuve que le test a été fait — sans lui, le verdict n'est pas opposable |

Les trois niveaux de gravité — précision utile :

| Gravité | Définition | Conséquence |
| --- | --- | --- |
| Bloquante | L'élément à lever est critique — il affecte la sécurité, la conformité, ou engage la responsabilité | Le livrable ne doit pas être diffusé tant que l'élément n'est pas levé |
| À lever avant transmission | L'élément à lever n'est pas critique, mais il doit être levé avant diffusion (par exemple, une hypothèse non déclarée) | Le livrable est diffusé après avoir levé l'élément |
| À surveiller | L'élément à lever n'est ni critique ni bloquant — il doit être documenté et suivi | Le livrable est diffusé, avec l'élément inscrit au RDR (réserve R-xx) |

Le piège du « c'est de principe » : un modèle qui reçoit un livrable a tendance à classer trop d'éléments en « de principe » pour éviter de les classer en « à lever ». C'est exactement ce qu'il faut interdire :
   * un élément est « de principe » seulement s'il est explicitement déclaré comme tel dans le livrable (mention « de principe » ou « sous hypothèse H-xx ») ;
   * un élément qui n'est pas déclaré est « à lever » — même s'il paraît anodin ;
   * la déclaration est la seule preuve — pas l'apparence.
Un modèle qui classe « de principe » sans vérifier la déclaration produit un faux verdict de sincérité.
Le piège de la « pratique courante » : un modèle a tendance à invoquer la « pratique courante » pour justifier un élément à lever. C'est exactement ce qu'il faut interdire :
   * « c'est comme d'usage » n'est pas une source ;
   * « c'est la pratique courante » n'est pas une déclaration ;
   * ces formulations sont précisément les symptômes d'un élément à lever — elles apparaissent quand l'élément n'a pas de source.
Un élément à lever ne peut pas être justifié — il doit être levé.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-01 (Proposition de la matrice) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-02 (Fiche de données) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-03 (Registre des décisions) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-04 (Plan de travail dégradé) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-10 (Audit critique du CCTP) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-11 (Audit du diagnostic structure) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-12 (Audit des pièces géotechniques) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-13 (Détection et qualification) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-14 (Clarification du périmètre) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-15 (Fiche de synthèse) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-20 (Conception structure GO) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-21 (Descente de charges préliminaire) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx — T-01 classe les éléments de principe et les éléments à lever |
| B-23 (Exploitation du diagnostic existant) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-24 (Vérification d'éléments existants non) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-25 (Stabilité globale, contreventement, joints) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-30 (Calage sur dxf/dwg source) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-31 (Preuve de superposition) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-32 (Vue nettoyée par livrable) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-33 (Vérification croisée) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-34 (Synthèse des réservations) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-40 (Fondations superficielles) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-41 (Fondations profondes) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-42 (Verticaux BA) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-43 (Planchers et dallages) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-44 (Charpente bois) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-45 (Structure métallique) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-46 (Maçonnerie : vérification) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-47 (Escaliers) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-48 (Prédalles et planchers préfabriqués) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-49 (Linteaux et seuils) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-50 (Assemblages et ancrages) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-60 (Plans d'exécution) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-62 (Nomenclature et façonnage) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-64 (Notice de synthèse) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-70 (Auto-contrôle déclaré de synthèse) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-71 (Indiçage et supersession documentaire) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| B-72 (Journal de clôture) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les éléments à lever classés « à surveiller » — ils deviennent des réserves R-xx |
| T-02 (Prompt de recadrage) | Le verdict « non sincère » — T-02 diagnostique la cause et corrige la méthode |
| T-03 (Prompt de méta-amélioration) | Les éléments à lever récurrents — T-03 propose des corrections au carnet |

Variables consommées

| Code | Libellé | Statut dans T-01 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| Toutes les variables citées dans le livrable | Selon le livrable | BLOQUANTE (chaque variable doit être classée) |

Variables produites
T-01 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (tableau de sincérité) qui alimente T-02, T-03 et B-03.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-01, vous devez valider le verdict de sincérité — c'est votre appréciation qui fait foi, pas la seule liste. Un élément classé « à surveiller » par le modèle peut être en réalité « à lever avant transmission » — c'est votre jugement d'ingénieur qui décide.
Cas particulier — livrable avec 0 élément à lever : si tous les éléments sont certains ou de principe, le verdict est « sincère ». C'est le cas idéal — mais il est rare. Un livrable avec 0 élément à lever peut être parfaitement sincère, ou peut être le signe que le test a été mal fait. Vérifiez que le tableau est exhaustif (tous les éléments sont listés) et que les déclarations de principe sont bien présentes dans le livrable.
Cas particulier — livrable avec beaucoup d'éléments à lever : si le livrable a beaucoup d'éléments à lever (par exemple, plus de 5), c'est le signe que le livrable a été produit sur des bases fragiles. Vous pouvez :
   * soit lever les éléments un par un (par exemple, en ajoutant les sources manquantes) ;
   * soit requalifier le livrable en mode PARTIEL-DÉCLARÉ (les éléments à lever deviennent des éléments de principe déclarés) ;
   * soit suspendre le livrable et reprendre la production à la brique amont.
Chaque choix a des conséquences — c'est votre décision.
Cas particulier — élément à lever de gravité bloquante : si un élément à lever est de gravité bloquante (par exemple, une section de poutre non sourcée), le livrable ne doit pas être diffusé. L'élément doit être levé avant diffusion — soit par une source, soit par une déclaration explicite (hypothèse H-xx).
Cas particulier — test sur un livrable en mode PARAMÉTRIQUE : si le livrable est en mode PARAMÉTRIQUE (par exemple, un plan de fondations avec q_adm manquante), les éléments dépendant de la donnée manquante sont « de principe » (déclarés comme tels, avec la mention « sous hypothèse H-xx — à confirmer »). Ils ne sont pas « à lever » — ils sont déclarés. Mais les éléments qui ne devraient pas dépendre de la donnée manquante et qui sont pourtant non sourcés sont « à lever ».
Cas particulier — test sur un livrable en mode PARTIEL-DÉCLARÉ : si le livrable est en mode PARTIEL-DÉCLARÉ (valeur déclarée au RDR), les éléments utilisant la valeur déclarée sont « de principe » (déclarés comme tels, avec la référence à la décision RDR). Ils ne sont pas « à lever ».
Format de sortie attendu : tableau détaillé (chaque élément, sa catégorie, sa justification), verdict de sincérité (sincère / non sincère), recommandations (cause probable, brique CARNAC, échéance).
Consignation : le test T-01 est consigné au RDL (avec le code du livrable testé, la date, le verdict). En cas de verdict « non sincère », les éléments à lever sont inscrits au RDR comme réserves (R-xx) avec leur échéance.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).