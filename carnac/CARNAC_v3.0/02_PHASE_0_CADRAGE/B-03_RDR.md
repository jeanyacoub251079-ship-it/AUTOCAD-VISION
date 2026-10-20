Fichier 02_PHASE_0_CADRAGE/B-03_RDR.md — CARNAC v3.0
________________


B-03 — REGISTRE DES DÉCISIONS ET RÉSERVES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 0 — Cadrage et qualification |
| Brique précédente | B-02 (FDC) |
| Brique suivante | B-04 (PTD) |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | MPD validée (B-01), FDC (B-02), échanges avec MOA / MOE / BET |
| Sortie unique | RDR complet, daté, avec trois sections numérotées (Décisions / Réserves / Registre des Verrous) |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-02, avant B-04. Le RDR est ouvert en phase 0 et mis à jour à chaque décision, réserve ou verrou pendant toute la durée du projet. Ce n'est pas un document « une fois » — c'est un registre vivant.
Ce que vous fournissez à l'IA : la MPD validée, la FDC, et les échanges déjà intervenus avec la MOA / MOE / BET (décisions prises, réserves demandées, données manquantes signalées). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-05}} et {{ID-07}}.
Ce que vous validez à la sortie :
* chaque décision (auteur, date, effet sur les briques) ;
* chaque réserve (responsable, échéance) ;
* chaque verrou (brique suspendue, briques exécutées malgré tout).
Pourquoi le RDR est le document qui vous protège : en cas de litige sur un délai, une valeur déclarée, ou un livrable partiel, c'est le RDR qui prouve que vous avez :
1. pris les décisions qui vous appartenaient (Section 1) ;
2. demandé les données manquantes dans les délais (Section 2) ;
3. exécuté tout ce qui était faisable malgré les blocages (Section 3 — Registre des Verrous).
Sans le RDR, ces trois preuves n'existent pas. Le RDR n'est pas un document administratif — c'est votre défense.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : ouvrir le Registre des Décisions et Réserves (RDR) de l'opération {{ID-01}}, à partir de la MPD validée, de la FDC et des échanges avec la MOA/MOE/BET. Le RDR est le document qui me protège en cas de litige sur un délai, une valeur déclarée ou un livrable partiel.


TROIS SECTIONS OBLIGATOIRES


Section 1 — Décisions
Tableau : N° | Date | Objet | Décision | Auteur | Effet sur les briques
Numérotation D-01, D-02… Chaque décision est datée, attribuée à un auteur nommé, et son effet sur les modes des briques est explicité (ex. « MAT-02 → B-40, B-42, B-43 en COMPLET »).


Section 2 — Réserves
Tableau : N° | Objet | Statut (Ouverte / Fermée) | Responsable de l'obtention | Date de demande | Échéance
Numérotation R-01, R-02… Une réserve ne se ferme que par une entrée en FDC (valeur + source) ou une décision en Section 1.


Section 3 — Registre des Verrous
Tableau : N° | Donnée (code) | Brique suspendue | Date | Responsable | Briques exécutées malgré tout | Mode de contournement (PARAMÉTRIQUE / PARTIEL-DÉCLARÉ)
Numérotation V-01, V-02…


RÈGLES
1. Une décision sans auteur et sans date n'existe pas.
2. Un verrou ne se ferme que par entrée en FDC ou décision en Section 1.
3. Le Registre des Verrous liste TOUJOURS ce qui a été fait malgré tout : c'est ce qui me protège en cas de litige.
4. Une requalification NON BLOQUANTE → BLOQUANTE est inscrite au registre, avec suspension immédiate. L'inverse est interdit : une donnée BLOQUANTE ne devient jamais NON BLOQUANTE par décision du modèle.


INTERDICTIONS
- Ne prends aucune décision qui relève de moi ou de la MOA.
- Ne ferme aucun verrou sans entrée en FDC ou décision en Section 1.
- Ne crée aucune ligne D-/R-/V- sans justification.


SORTIE
Le RDR complet, daté, avec les trois sections et les numérotations. En tête du document : rappel de l'indice du dossier ({{ID-05}}) et de la date ({{ID-07}}).


CRITÈRE D'ACCEPTATION
Le RDR est accepté si :
- chaque décision a un auteur, une date et un effet identifié ;
- chaque réserve a un responsable et une date de demande ;
- chaque verrou identifie la brique suspendue et les briques exécutées malgré tout ;
- aucune décision n'a été prise à ma place sans source citée.
Si un seul de ces quatre points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} (code projet), {{ID-05}} (indice du dossier en vigueur) et {{ID-07}} (date de l'étude). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « une décision sans auteur et sans date n'existe pas » | Une décision sans auteur ni date n'est pas opposable en cas de litige. Si vous dites « on avait décidé de retenir XA3 », votre interlocuteur peut répondre « quand ? qui ? » — et sans réponse, la décision est nulle. La traçabilité auteur/date est la seule protection |
| « Un verrou ne se ferme que par entrée en FDC ou décision en Section 1 » | Empêche une « fermeture orale » du verrou — c'est la fermeture orale qui fait perdre les litiges. Un verrou fermé oralement (« oui, on a le G2, c'est bon ») n'est pas fermé : il reste ouvert jusqu'à ce que la valeur entre en FDC ou qu'une décision soit inscrite |
| « Le Registre des Verrous liste TOUJOURS ce qui a été fait malgré tout » | C'est le document qui prouve que vous n'avez pas attendu les pieds croisés. En cas de reproche sur un retard, le Registre des Verrous montre que vous avez exécuté toutes les briques qui ne dépendaient pas de la donnée manquante — et que le retard est imputable à l'obtention de la donnée, pas à votre production |
| « requalification NON BLOQUANTE → BLOQUANTE autorisée ; l'inverse interdit » | Verrou V12 — votre validation explicite. Une donnée qui se révèle bloquante en cours de route doit suspendre la brique (et être inscrite au registre). Une donnée bloquante ne peut jamais être débloquée par décision du modèle — seul un acte écrit (entrée FDC ou décision RDR) le permet |
| « Ne prends aucune décision qui relève de moi ou de la MOA » | Une décision MOA (par exemple, « commande du G3 ») n'est pas une décision du modèle. Le modèle peut recommander (dans B-12 par exemple), il ne peut pas décider |
| « Ne crée aucune ligne D-/R-/V- sans justification » | Une ligne sans justification est une ligne qui ne se défend pas. Chaque ligne du RDR doit pouvoir être expliquée — sinon elle devient une ligne « de confort » qui pollue le registre |
| « rappel de l'indice du dossier et de la date » | Un RDR sans indice ni date n'est pas rattachable à une version du dossier. La date et l'indice sont les deux éléments qui permettent de dire « à cette date, avec ce dossier, voilà ce qui avait été décidé » |

Différence entre les trois sections — précision utile :

| Section | Question à laquelle elle répond | Nature |
| --- | --- | --- |
| Décisions (D-xx) | « Qu'a-t-on décidé, quand, qui, et avec quel effet ? » | Actes positifs (on choisit une valeur, on tranche un point) |
| Réserves (R-xx) | « Qu'est-ce qui reste à obtenir, par qui, quand ? » | Actes d'attente (on demande une donnée, on attend une réponse) |
| Verrous (V-xx) | « Qu'est-ce qui est bloqué, et qu'a-t-on fait malgré tout ? » | Actes de contournement (on exécute ce qui est faisable, on suspend le reste) |

Une même situation peut produire les trois : par exemple, un G2 insuffisant produit une réserve R-xx (demande de G3 à la MOA), un verrou V-xx (B-40 suspendue, B-21/B-42/B-43 exécutées malgré tout en PARAMÉTRIQUE), et une décision D-xx si la MOA décide de ne pas commander le G3 (valeur déclarée, avec mention de la conséquence).
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Les décisions de périmètre (les NON NÉCESSAIRE validés) sont inscrites au RDR comme décisions D-xx, avec auteur et date |
| B-02 (Fiche de données) | Les VERROU listés en fin de FDC — B-03 les inscrit au Registre des Verrous (section 3) |
| B-13 (Détection et qualification) | Les propositions d'inscription (V-xx ou R-xx) — B-03 les inscrit dans la section correspondante |
| B-14 (Clarification du périmètre) | Les prestations À TRANCHER — B-03 les inscrit en réserves (R-xx) avec destinataire et échéance |
| B-15 (Fiche de synthèse) | Les risques identifiés — chaque risque de criticité élevée devient une réserve R-xx (ou un verrou V-xx si le risque est déjà bloquant) |
| B-24 (Vérification d'éléments existants non) | Les essais à commander — B-03 les inscrit en réserves (R-xx) avec responsable et échéance |
| T-01 (Prompt de sincérité) | Les éléments à lever classés « à surveiller » — ils deviennent des réserves R-xx |
| T-04 (Prompt de demande) | Les demandes consignées (statut envoyée / en attente / répondue) — le RDR est mis à jour |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-04 (Plan de travail dégradé) | Les verrous (Section 3) et les réserves (Section 2) — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-10 (Audit critique du CCTP) | Les décisions déjà prises (par exemple, une décision de périmètre qui précise ce qui est dans le lot GO) |
| B-11 (Audit du diagnostic structure) | Les décisions déjà prises (par exemple, une décision de périmètre qui précise les lots inclus) |
| B-12 (Audit des pièces géotechniques) | Les décisions déjà prises (par exemple, une décision de périmètre qui précise que les fondations ne sont pas concernées) |
| B-15 (Fiche de synthèse) | Les décisions et verrous déjà inscrits — B-15 en tient compte pour ne pas dupliquer un risque déjà traité |
| B-22 (Note d'hypothèses de conception) | Les décisions déjà prises — les hypothèses peuvent être validées par une décision D-xx |
| B-40 (Fondations superficielles) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-41 (Fondations profondes) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-42 (Verticaux BA) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-43 (Planchers et dallages) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-44 (Charpente bois) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-45 (Structure métallique) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-46 (Maçonnerie : vérification) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-47 (Escaliers) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-48 (Prédalles et planchers préfabriqués) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-49 (Linteaux et seuils) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-50 (Assemblages et ancrages) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-64 (Notice de synthèse) | Les décisions, réserves et verrous — B-64 les intègre dans les points à lever |
| B-70 (Auto-contrôle déclaré de synthèse) | Les décisions et verrous — B-70 vérifie la conformité des modes avec les décisions RDR (verrou V12) |
| B-71 (Indiçage et supersession documentaire) | Les décisions — chaque révision d'un livrable est rattachée à une décision RDR (motif documenté) |
| B-72 (Journal de clôture) | Les réserves et verrous — B-72 liste les points ouverts qui restent à traiter après remise |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les réserves (Section 2) — T-04 transforme les réserves en demande formelle à la MOE / BET / MOA |

Variables consommées

| Code | Libellé | Statut dans B-03 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| ID-05 | Indice du dossier en vigueur | BLOQUANTE (pour la traçabilité du RDR) |
| ID-07 | Date de l'étude | BLOQUANTE (pour la traçabilité du RDR) |
| DEC-02 | Décisions inscrites au RDR (valeur déclarée, auteur, date) | Variable produite par B-03 |
| DEC-03 | Verrous ouverts (donnée, brique suspendue, responsable) | Variable produite par B-03 |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |

Variables produites

| Code | Libellé | Description |
| --- | --- | --- |
| DEC-02 | Décisions inscrites au RDR | Chaque décision D-xx (date, objet, décision, auteur, effet) |
| DEC-03 | Verrous ouverts | Chaque verrou V-xx (donnée, brique suspendue, responsable, briques exécutées malgré tout) |

Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DEC-02, DEC-03, ID-05, ID-07 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique de cette brique : à la sortie de B-03, vous devez valider chaque décision (auteur, date, effet). C'est vous qui êtes l'auteur des décisions qui vous appartiennent ; c'est la MOA qui est l'auteur des décisions qui lui appartiennent. Un modèle qui inscrit une décision « à votre place » produit une décision qui n'est pas opposable (vous ne l'avez pas signée).
Cas particulier — décision MOA non encore obtenue : si une décision est en attente (par exemple, la MOA n'a pas encore répondu sur la commande du G3), elle n'est pas une décision D-xx. Elle est une réserve R-xx (« en attente de décision MOA sur la commande G3 »), avec responsable et échéance. La décision D-xx ne sera inscrite qu'une fois la réponse obtenue.
Cas particulier — décision de périmètre (MPD) : la validation de la MPD par vous (étape B-01) est une décision D-xx : « D-01 : validation de la MPD en date du … — auteur : [vous] — effet : active les briques … ». La MPD validée est annexée au RDR, pas recopiée.
Cas particulier — requalification en cours de route : si une donnée déclarée NON BLOQUANTE se révèle BLOQUANTE (par exemple, une donnée qu'on croyait secondaire devient indispensable à une brique), la requalification est inscrite au registre (Section 3) avec :
* la donnée concernée ;
* la brique suspendue ;
* la date de requalification ;
* la raison (pourquoi elle est devenue bloquante) ;
* les briques exécutées malgré tout.
Cas particulier — fermeture de verrou : un verrou ne se ferme jamais par simple déclaration orale. Il se ferme :
* soit par une entrée en FDC (la valeur manquante arrive avec sa source) ;
* soit par une décision D-xx (valeur déclarée, avec auteur, date et justification).
Une fois le verrou fermé, la brique suspendue peut être relancée (en COMPLET si la valeur est Contractuelle ou Décision, en PARTIEL-DÉCLARÉ si la valeur est une décision de travail).
Cas particulier — livrable partiel : si vous remettez un livrable alors qu'un verrou est encore ouvert, le Registre des Verrous documente exactement ce qui a été exécuté malgré tout. C'est ce qui prouve que le livrable partiel n'est pas un livrable « bâclé » — c'est un livrable qui aurait été complet si la donnée avait été fournie.
Format de sortie attendu : trois sections distinctes (Décisions, Réserves, Verrous), chacune avec un tableau numéroté. En tête du document : code projet, indice du dossier, date.
Consignation : le RDR est le document central du projet — il est référencé par toutes les briques de calcul et par la clôture (B-70 à B-72). Il est mis à jour à chaque décision, réserve ou verrou, et il est daté à chaque mise à jour.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Registres séparés.** Le RDR tient désormais quatre registres distincts et non interchangeables : `D-xx` (décisions humaines datées et signées), `H-xx` (hypothèses notifiées sous nuage, avec valeur, norme d'appui, zone d'application et statut de visa), `PA-xx` (Points d'Arrêt chantier opposables, avec prescription `ENC` associée) et `V-xx` (verrous de Classe III, seuls bloquants).

**Délai de contradiction.** Chaque hypothèse `H-xx` est notifiée avec le délai contractuel `DEC-06` (2 jours ouvrés par défaut) : à l'expiration, l'hypothèse est réputée acceptée et le titulaire est exonéré des conséquences de l'écart, dans la limite de la norme d'appui citée.