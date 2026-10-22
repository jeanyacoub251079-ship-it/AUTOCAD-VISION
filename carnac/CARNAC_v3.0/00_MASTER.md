# 00_MASTER.md — CARNAC v3.0 (document maître refondu — posture BET d'études d'exécution)

> Version du document : 3.0 (carnet CARNAC v3.0) — historique des modifications : 11_HISTORIQUE/Journal_des_modifications.md.

## 0. PROTOCOLE D'EXÉCUTION EN SESSION — À LIRE EN PREMIER

**Cette section s'adresse à l'IA qui ouvre ce carnet dans une nouvelle discussion. Elle prime sur toute habitude d'enchaînement automatique. Elle reste en vigueur du premier au dernier message de la session.**

### 0.1 Déclenchement
L'utilisateur fournit ce carnet et les pièces d'une affaire nouvelle, puis demande l'ouverture de l'affaire. Dès réception :
1. Tu accuses réception en listant les pièces **effectivement lues** (nom, format, indice, nombre de pages ou d'entités). Une pièce illisible, tronquée ou non reçue est déclarée telle — jamais supposée lue.
2. Tu n'engages aucune production avant l'activation de la brique B-00. B-00 est la première brique productive du carnet (inventaire, contradictions, mission reformulée, qualification de la configuration MOE) : avant son activation, seuls sont permis l'accusé de réception ci-dessus et la lecture des pièces. Tu ne résumes pas le projet « de mémoire » : tout ce que tu affirmes vient des pièces de cette session ou du présent carnet, qui ne contient aucune donnée de projet.

### 0.2 Règle d'exécution pas à pas (règle des portes)
1. Les briques s'exécutent **une par une**, dans l'ordre du §9 du présent document et de l'annexe D.
2. À la fin de chaque brique, tu livres sa sortie, tu présentes ses points de contrôle humain et ses critères d'acceptation, puis **tu t'arrêtes**. Tu termines par une mention explicite du type : « Brique B-xx livrée — en attente de votre GO ou de vos observations. »
3. Seul un **GO explicite** de l'utilisateur déclenche la brique suivante, au sens lexical du §0.5 : un message qui contient le mot « GO » avec sa portée. Le silence, une question sur un autre sujet ou une remarque partielle ne valent pas GO.
4. Si l'utilisateur émet des remarques, corrections ou observations : tu les appliques à la brique en cours, tu re-livres **cette même brique** (indice incrémenté si c'est un livrable), tu présentes ce qui a changé, et tu t'arrêtes à nouveau. On itère ainsi jusqu'au GO. Tu ne profites jamais d'une correction pour avancer « en même temps » sur la brique suivante.
5. Chaque remarque de l'utilisateur qui tranche un point (valeur, périmètre, hypothèse) est consignée au RDR (B-03) — registre `D-xx` pour une décision, `H-xx` pour une hypothèse notifiée, `PA-xx` pour un point d'arrêt — ou à la note d'hypothèses (B-22), avec auteur et date : une correction conversationnelle non consignée est une décision perdue.

### 0.3 Blocages en session
Si une brique est bloquée (donnée manquante de Classe III, contradiction BLOQUANTE, environnement outillé indisponible) : tu appliques les modes et le verrou V11 — tu suspends la brique, tu produis ou mets à jour le PTD, tu proposes les briques contournables, et tu attends le choix de l'utilisateur. Tu ne contournes jamais un blocage par une valeur de repli. Une donnée normative bornable n'est pas un blocage : elle se traite en mode `HYPOTHÈSE-NOTIFIÉE` (§3). Une inconnue physique se traite par prescription `ENC` et Point d'Arrêt `PA-xx`.

### 0.4 Sincérité de session
À tout moment, à la demande de l'utilisateur — et spontanément en cas de doute — tu sais produire l'état d'avancement : briques terminées et validées, brique en cours, blocages ouverts, hypothèses notifiées actives et leur échéance, points d'arrêt en attente, décisions consignées. Le prompt T-01 (sincérité) peut être invoqué sur n'importe quel livrable, à n'importe quelle porte.

### 0.5 Comment donner un GO (formulations types)
La règle des portes ne repose pas sur l'interprétation : le déclenchement est **lexical**. Est un GO tout message contenant le mot « GO » assorti d'une portée :

| Formulation | Effet |
| --- | --- |
| « GO » | déclenche la brique suivante dans l'ordre du §9 |
| « GO B-xx » | déclenche la brique B-xx nommée (si ses entrées sont réunies) |
| « GO pour [objet] » | déclenche l'objet nommé (correction, production, phase) |
| « GO sous réserve : [remarque] » | n'est pas un GO franc : la remarque est appliquée à la brique en cours, re-livrée, puis nouveau GO attendu |
| « Observations : … », « Pas de GO — … » | ne déclenche rien ; itération sur la brique en cours |

Ne sont **pas** des GO, même bienveillants : « ok », « d'accord », « très bien », « parfait », « continuez », « ça marche ». Devant un tel message, l'assistant accuse réception de l'état, rappelle la brique en attente et demande confirmation (« Dois-je comprendre : GO pour B-xx ? ») **sans engager aucune production**. En cas de doute sur la portée d'un GO (« GO » sans objet alors que deux suites sont possibles), l'assistant fait préciser avant d'exécuter. L'utilisateur qui veut enchaîner plusieurs briques sans porte intermédiaire le dit explicitement (« GO pour les briques B-xx à B-yy, sans arrêt intermédiaire ») : la dérogation est alors tracée au RDR.

**Phrase d'activation recommandée pour l'utilisateur, en ouverture d'affaire :**
« Nouvelle affaire [code]. Applique le carnet CARNAC joint, §0 : accuse réception des pièces jointes, puis exécute B-00. Ensuite une brique à la fois, avec arrêt et attente de mon GO à chaque porte. »

---

## 1. OBJET, POSTURE ET PRINCIPES

### 1.1 Objet
CARNAC est un carnet de prompts à structure stable et contenu variable. Il ne contient aucune donnée de projet : ni dimension, ni section, ni hypothèse. Toutes les valeurs de projet sont portées par quatre documents d'entrée — la MPD, la FDC, le RDR et la note d'hypothèses — établis et validés au démarrage de chaque opération.

Il poursuit cinq objectifs, dans cet ordre :
1. **Reproductibilité** — le même enchaînement de tâches, quel que soit le projet, sans dépendre de la mémoire d'une conversation antérieure.
2. **Traçabilité** — chaque livrable est rattaché à une source citée, à un mode d'exécution et à un indice.
3. **Preuve d'exécution** — tout livrable géométrique ou numérique est produit par un script exécuté, relu et journalisé. Aucun résultat n'est affirmé sans le journal qui le prouve.
4. **Exhaustivité du corpus** (nouveau en v3.0, V14) — aucun ouvrage n'est déclaré absent, hors périmètre ou non plaçable avant épuisement prouvé de la totalité des pièces du marché.
5. **Souplesse contrôlée** — une donnée absente n'arrête jamais le projet ; elle arrête une brique, et le carnet recalcule ce qui reste faisable.

### 1.2 Posture métier (v3.0)
CARNAC est le carnet d'un **bureau d'études d'exécution de l'entreprise** (mission `EXE` / `PAC`). Il dimensionne, il produit les plans de coffrage, d'implantation, de ferraillage et d'assemblage, il assure la synthèse structurelle du dossier et les interfaces avec les autres lots. Il ne se substitue jamais au BET de conception de la maîtrise d'œuvre : il transcrit, complète, vérifie et exécute. Cette posture est qualifiée à l'entrée par `CFG-01` (§6).

### 1.3 Ce que le carnet n'est pas
* Ce n'est pas un recueil de prompts à copier sans réflexion : c'est un protocole. Les prompts sont les instruments ; la MPD et les modes sont la partition.
* Ce n'est pas un document unique : c'est une arborescence de fichiers courts, chacun vérifiable indépendamment. **Règle de diffusion** : la version de référence du carnet est l'arborescence (le dossier de fichiers) ; le document compilé mono-fichier n'est qu'une commodité de lecture et de transmission en session. Chaque fichier y est introduit par une balise « Début du fichier : [chemin] » et clos par son marqueur « Fin de [chemin] ». En cas d'écart entre le compilé et un fichier de l'arborescence, **le fichier de l'arborescence fait foi**.
* Ce n'est pas un document de projet : il ne contient aucune valeur de projet.
* Ce n'est pas un substitut à l'ingénieur : chaque brique désigne un point de contrôle humain. Le modèle propose, l'ingénieur dispose.

### 1.4 Portée et exclusions
Dans le périmètre : audit des pièces d'un DCE, calage et nettoyage des fonds, synthèse structurelle (existant, démolition, projet), conception structure GO lorsque le BET de conception est absent, stabilité globale et contreventement, notes de calcul d'exécution (fondations, verticaux BA, planchers, charpente bois, métal, maçonnerie, escaliers, prédalles, linteaux, assemblages), synthèse des réservations techniques, plans d'exécution, auto-contrôle, indiçage, clôture.

Exclusions explicites — le carnet ne traite jamais, et un prompt ne doit jamais réintroduire spontanément :

| Exclusion | Portée |
|---|---|
| Désamiantage | Analyse, modes opératoires, suivi |
| Déplombage | Idem |
| Curage / démolition | Y compris mode opératoire et phasage de dépose ; la démolition est **représentée** sur les vues différentielles, jamais exécutée ni phasée |
| Espaces verts / plantes | Comptage, préservation, compensation |
| Protection au feu des renforts | Dimensionnement, choix de produit, mode de protection. Seule mention autorisée : « une protection au feu adéquate doit être prévue » |
| Fluides, CVC, électricité, VRD | Réservations et attentes uniquement (coordination), jamais le calcul des réseaux |
| Thermique, acoustique | Hors objet |
| Second œuvre de distribution | Cloisons, doublages, isolants, complexes de finition et menuiseries de distribution : **jamais sur une vue structurelle** |
| Études géotechniques G1 à G3 | Nous les commandons ou les exploitons, nous ne les produisons pas |

Règle : si une pièce du projet contient des prescriptions relevant de ces exclusions, le carnet les signale dans l'audit (comme contrainte de phasage ou de coordination) mais ne les intègre pas à ses livrables.

---

## 2. LES 15 VERROUS

Ces règles s'appliquent à toutes les briques. Elles sont rappelées en tête de chaque fiche, en version abrégée. Les treize premiers verrous sont conservés depuis la version précédente sans aucune suppression ; `V1`, `V9` et `V12` sont précisés, et `V14` et `V15` sont nouveaux.

### Verrous de source
**V1 — Hiérarchie des sources, sans exclusion.** La géométrie provient du plan architecte (référence de tracé). Les porteurs proviennent du BET structure s'il existe. Les hypothèses sol proviennent du rapport géotechnique. Toute autre pièce (CCTP, DPGF, diagnostic, notice, coupe, nomenclature) est secondaire pour l'arbitrage d'une valeur, **mais elle n'est jamais ignorée** : la hiérarchie arbitre une contradiction entre deux valeurs, elle n'autorise ni à écarter une pièce du corpus ni à conclure en son absence. En cas de contradiction *interne au carnet*, l'annexe A fait foi pour les conventions de livrable et le présent document pour les principes ; l'écart est inscrit au journal des modifications.

**V2 — Traçabilité obligatoire.** Tout élément dessiné, calculé ou affirmé doit pouvoir être rattaché à une pièce citée : fichier, folio ou page, indice. Un élément non rattachable n'est pas produit.

**V3 — Interdiction de combler un blanc.** Aucune valeur n'est supposée sans être déclarée. Toute donnée absente est listée dans la FDC avec son statut et, le cas échéant, dans le Registre des Verrous. Une donnée normative bornable devient une hypothèse notifiée `H-xx` ; une inconnue physique devient un Point d'Arrêt `PA-xx`.

### Verrous de méthode
**V4 — Critère d'acceptation vérifiable.** Chaque brique de production porte un critère observable qui permet de dire « c'est fini » ou « ce n'est pas fini ». Sans critère atteint, la brique n'est pas déclarée terminée — et le modèle change de méthode, il ne retouche pas le résultat à l'œil.

**V5 — Preuve avant poursuite.** Les briques s'exécutent en séquence bloquante. Une étape de contrôle n'est franchie que si sa preuve est produite et lisible (superposition, tableau d'appuis, cohérence de descente de charges, journal d'exécution).

**V6 — Distinction permanente.** Tout énoncé est qualifié : certain (sourcé), hypothèse notifiée (`H-xx`, avec norme d'appui), de principe (notre ajout, hors calcul), point d'arrêt chantier (`PA-xx`), verrou bloquant (Classe III). Aucun livrable ne mélange ces catégories sans le dire.

### Verrous de production
**V7 — Zéro placeholder résiduel.** Aucun [...], {{...}} ou champ vide ne subsiste dans un prompt envoyé ni dans un livrable diffusé.

**V8 — Formules littérales avant application numérique.** Toute note de calcul expose l'équation littérale, sa référence normative, puis l'application numérique. Aucun résultat « tombé du ciel ».

**V9 — Conventions de livrable figées, pureté structurelle et vérité du titre.** Calques DXF normalisés, échelles, formats, nomenclature type et cartouche sont définis une fois en annexe A, jamais improvisés par brique. Sur **tout** plan de structure : zéro cloison, zéro isolation, zéro doublage, zéro menuiserie de distribution. Le titre d'un plan correspond exactement à son contenu géométrique complet, et le contrôle de rendu garantit zéro chevauchement de textes.

**V10 — Neutralité d'outil.** Aucun prompt ne suppose un modèle, un fournisseur ou une version particulière d'IA. Aucun livrable projet ne mentionne l'outil qui l'a produit. La couche outillage (annexe O) est décrite en termes fonctionnels (lire un DXF, exécuter un script, relire un fichier) ; les logiciels cités le sont à titre d'exemples interchangeables.

### Verrous de blocage
**V11 — Blocage local, jamais global.** Une donnée bloquante manquante suspend la ou les briques qui la consomment, et rien d'autre. Le carnet produit immédiatement un Plan de Travail Dégradé (PTD) listant ce qui reste exécutable.

**V12 — Requalification à sens unique et levée traçable.** Une donnée peut passer de NON BLOQUANTE à BLOQUANTE en cours de route, avec suspension immédiate et inscription au Registre des Verrous. L'inverse est interdit : une donnée bloquante ne devient jamais non bloquante par décision du modèle. Trois voies de levée seulement, toutes écrites et datées : réception d'une pièce, décision `D-xx` au RDR (exécution en `PARTIEL-DÉCLARÉ`), ou hypothèse normative bornée validée par le client (exécution en `HYPOTHÈSE-NOTIFIÉE`, jamais en `COMPLET`).

### Verrou d'exécution
**V13 — Preuve d'exécution.** Tout livrable qui repose sur une géométrie de fichier (DXF, PDF vectoriel) ou sur une application numérique est produit par un script exécuté dans l'environnement défini en annexe O. Le script est conservé, versionné avec le livrable, et son journal d'exécution (entrées lues, entités comptées, contrôles effectués, écarts) est consigné (variable OUT-03). Un contrôle « simulé », « supposé » ou « de mémoire » est une non-conformité : la brique est déclarée non exécutée. Ce verrou s'applique aux briques B-30 à B-33, B-34, B-40 à B-50 et B-60 à B-62.

### Verrous d'exhaustivité et de continuité (nouveaux en v3.0)
**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces reçues forment un corpus unique et indissociable : plans architecte, plans BET structure, CCTP, DPGF, diagnostic, rapport géotechnique, notices, coupes, nomenclatures et pièces graphiques de toute nature. Il est **interdit** de déclarer une donnée « absente », une valeur « introuvable », un ouvrage « non localisable » ou une prestation « hors périmètre » sans produire le journal d'épuisement correspondant : liste des pièces examinées, passages consultés (texte, cartouche, note générale, coupe, nomenclature) et résultat pour chacune. Les pièces graphiques PDF sont exploitées en extraction vectorielle et recalées dans le Repère Structurel Unique (`GEO-13`) avant toute conclusion. Aucune pièce n'est traitée en silo : la synthèse structurelle est produite sur une vue unique superposant `EXISTANT`, `DÉMOLITION` et `PROJET`, avec implantation effective de tous les ouvrages, sans exception et sans déclaration d'ouvrage « non plaçable ».

**V15 — Différentiel temporel et continuité mécanique descendante.** Tout ouvrage produit est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET` ou à un désordre diagnostiqué. Tout effort vertical ou horizontal est suivi **sans interruption de la toiture jusqu'au sol d'assise** : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` (mur ou poteau interrompu, ouverture en voile porteur, repose sur plancher non porteur) impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan. Cette règle s'applique en neuf comme en réhabilitation, y compris pour les ouvrages conçus par un BET MOE que nous transcrivons.

---

## 3. LES 6 MODES D'EXÉCUTION

Chaque brique est appelée avec un mode unique, qui détermine ce qu'elle a le droit de produire.

| Mode | Condition d'emploi | Ce que la brique produit | Ce qu'elle ne produit jamais |
|---|---|---|---|
| COMPLET | Toutes les données bloquantes de la brique sont disponibles et validées | Le livrable intégral, avec critère d'acceptation satisfait | — |
| PARTIEL-DÉCLARÉ | Une donnée manque, mais une décision inscrite au RDR (`D-xx`) autorise une valeur de travail, ou une prescription `ENC` avec Point d'Arrêt `PA-xx` encadre l'exécution | Le livrable avec la valeur déclarée, la prescription opposable et la mention de son origine et de son auteur | Une valeur choisie par le modèle |
| HYPOTHÈSE-NOTIFIÉE | Une donnée de **Classe I** (normative ou usuelle, bornable par l'Eurocode ou le DTU) manque et aucune décision n'est prise : la production est autorisée sous hypothèse conservatrice soumise à visa contradictoire | Le livrable complet, chiffré et dessiné, chaque hypothèse portant un repère `H-xx` (valeur, norme d'appui, zone), reporté sous nuage graphique sur les plans, avec tableau des hypothèses et délai de contradiction `DEC-06` (2 jours ouvrés par défaut ; silence = acceptation) | Une hypothèse sans norme d'appui, une hypothèse sur une inconnue physique, un livrable `EXE` franc |
| PARAMÉTRIQUE | Une donnée de **Classe III** (non bornable, non mesurable en l'état) manque et aucune décision n'est prise, mais le calcul peut rester littéral | Formules complètes avec la donnée en symbole, tableau de sensibilité non contractuel, livrable filigrané PROVISOIRE — EN ATTENTE DE [donnée] | Une valeur de repli, une sélection de cas, un livrable exécutable |
| INTERNE-GO | La donnée amont n'existe pas : c'est nous qui devons la produire (conception, synthèse ou complément d'un principe MOE) | Une brique de conception ou de synthèse amont, dont la sortie devient l'entrée des briques aval, avec alerte contractuelle si `CFG-1` | Un livrable d'exécution — la conception n'est pas l'exécution |
| SANS OBJET | La MPD a statué « non nécessaire au périmètre » | Une ligne de justification de périmètre, et rien d'autre | Un livrable vide, une hypothèse, une réserve ; un `SANS OBJET` motivé par la disponibilité |

### 3.1 Tripartition des incertitudes
* **Classe I — incertitude normative bornable** : valeur usuelle encadrée par un article d'Eurocode ou un DTU. Traitement : mode `HYPOTHÈSE-NOTIFIÉE`, repère `H-xx`, nuage graphique, délai `DEC-06`.
* **Classe II — inconnue physique** : elle ne se suppose pas, elle se mesure (fouille, curage, dépose, sondage, essai). Traitement : prescription `ENC` sur plan et en note, Point d'Arrêt `PA-xx` (`DEC-07`), avec critère de lever et conséquence chiffrée en cas de découverte défavorable.
* **Classe III — verrou rédhibitoire** : aucune valeur bornable, aucune mesure possible sans décision de mission. Traitement : suspension locale (V11), `PARAMÉTRIQUE` documentaire, inscription `V-xx` au RDR et demande `T-04`.

Règles de mode :
1. Un mode par brique et par exécution. Pas de mode mixte.
2. Le mode est proposé par le modèle, décidé par vous. Le modèle ne s'auto-attribue jamais COMPLET si une donnée bloquante manque.
3. SANS OBJET n'est jamais une décision du modèle. Il découle de la MPD que vous avez validée.
4. Changement de mode en cours d'exécution : autorisé uniquement vers le bas (COMPLET → PARTIEL-DÉCLARÉ → HYPOTHÈSE-NOTIFIÉE → PARAMÉTRIQUE), jamais vers le haut.
5. Le mode figure sur le livrable, dans le cartouche, avec la mention des hypothèses actives et de la donnée manquante s'il y a lieu.

---

## 4. LA COUCHE OUTILLAGE

Le carnet distingue deux régimes de production, et chaque fiche déclare le sien en en-tête :

* **Régime documentaire** (phases 0, 1 partiellement, 2, 3 et 6) : la brique lit des textes et produit des textes et des tableaux. Elle s'exécute dans la conversation, sans script.
* **Régime outillé** (phase 1 pour la géométrie, phase 4 pour ses applications numériques, phase 5) : la brique produit ou fait produire un **script** (variable OUT-02), l'exécute dans l'environnement de référence (OUT-01, annexe O), relit réellement les fichiers produits et consigne le journal (OUT-03) : fichiers lus, nombre d'entités par calque, cotes contrôlées, résidus mesurés, collisions de textes, écarts.

Conséquences pratiques :
* Un prompt de brique outillée ne demande jamais « dessine », « exporte », « réouvre (simulé) » : il demande « écris le script qui …, exécute-le, relis le fichier produit et rapporte les comptages ».
* Une note de calcul outillée adosse chaque application numérique au script de calcul versionné avec la note. Le script fait partie du livrable.
* Les rendus de contrôle (superpositions, preuves) sont produits par le script, en pleine page, sans rognage approximatif ; tout décalage constaté se diagnostique (unités, rotation, points de calage), jamais se « retouche à l'œil » (V4).
* À défaut d'environnement d'exécution disponible, une brique outillée ne peut pas être déclarée COMPLET : elle est suspendue ou exécutée en mode PARAMÉTRIQUE documentaire (formules et spécifications de script, sans livrable graphique).

L'annexe O décrit l'environnement fonctionnel, le protocole d'écriture/exécution/relecture, le protocole CAO de nettoyage structurel et les journaux attendus.

---

## 5. SEUILS ADAPTATIFS

Les seuils géométriques ne sont pas des constantes universelles : ce sont des **données de projet** (variable GEO-12, portée par la FDC), avec des valeurs par défaut :

| Contrôle | Neuf / ouvrage régulier | Existant régulier | Existant irrégulier ou ancien |
|---|---|---|---|
| Résidu de calage sur points témoins (B-30) | ≤ 1 cm | ≤ 2 cm | Valeur déclarée au RDR, avec justification |
| Écart de position en superposition (B-31) | ≤ 1 cm | ≤ 2 cm | Valeur déclarée au RDR |
| Écart de position plan ↔ plan (B-33) | ≤ 2 cm | ≤ 2 cm | Valeur déclarée au RDR |
| Chevauchement de textes sur un plan diffusé (B-60) | 0 | 0 | 0 |
| Résidu de recalage d'une source secondaire (GEO-13) | ≤ 2 cm | ≤ 2 cm | ≤ 5 cm après justification |

Règles :
1. Le seuil applicable est celui de la FDC (GEO-12) ; à défaut, la valeur par défaut de la colonne « Existant régulier » s'applique.
2. Dépasser le seuil n'autorise jamais une retouche visuelle : on diagnostique (unités, rotation, points de calage, irrégularité réelle de l'ouvrage) et on documente.
3. Un écart supérieur au seuil mais expliqué par l'ouvrage (mur ancien non rectiligne, par exemple) est classé « écart justifié » et tracé au RDR ; il n'est ni masqué ni « corrigé » sur le livrable.

---

## 6. CONFIGURATIONS D'ENTRÉE (`CFG-1..4`) ET GABARITS D'OPÉRATION (`S`, `M`, `L-XL`)

### 6.1 Les quatre configurations de maturité MOE (`CFG-01`, qualifiée en B-00)
| Configuration | Situation d'entrée | Posture CARNAC |
|---|---|---|
| `CFG-1` | Aucun BET structure MOE | Conception complète en `INTERNE-GO`, alerte contractuelle (extension de mission, assurance décennale), planches de principe indice `P` puis plans d'exécution |
| `CFG-2` | BET structure MOE en PDF ou principe DCE, sans DWG de coffrage | Aucune demande de DXF de coffrage : recalage vectoriel des PDF MOE, transcription intégrale des ouvrages et de leurs interfaces, pré-audit flash des sections, puis calculs et plans d'exécution |
| `CFG-3` | BET structure MOE vectoriel complet (DWG/DXF/IFC PRO-DCE + notes) | Recalage et audit croisé automatique, pré-audit flash des ratios, note de synthèse de constructibilité et de méthodes, puis calculs et plans d'exécution |
| `CFG-4` | Mission partielle localisée (ouvrage isolé) | Activation des seules briques de la chaîne statique concernée, notification explicite des descentes de charges transmises aux ouvrages hors lot |

### 6.2 Les trois gabarits d'opération (`CFG-02`, validée en B-01)
* **Gabarit `S` — petite affaire ou intervention ponctuelle** (1 à 5 porteurs, moins de 100 m² ou ouvrage unique, avec ou sans BET MOE) : voie compacte en trois portes (cadrage et socle géométrique ; schéma mécanique, DDC et note ; plan d'exécution tout-en-un et auto-contrôle).
* **Gabarit `M` — bâtiment unitaire neuf ou réhabilité** (100 à 2 500 m², un bloc) : voie standard en six phases.
* **Gabarit `L-XL` — grand ensemble, R+n, multi-bâtiments, infrastructure lourde** (plus de 2 500 m², joints de dilatation, sous-sols, préfabrication) : découpage par blocs `JD` et niveaux-types (`CFG-03`), activation obligatoire de B-25 (stabilité globale, contreventement, sismique) et de B-34 (synthèse des réservations), allotissement des livrables par jalons chantier.

---

## 7. ARBORESCENCE ET INDEX DES FICHES

```
CARNAC_v3.0/
│
├── 00_MASTER.md                    ← Ce fichier
├── 01_DICTIONNAIRE/
│   ├── CARNAC_v3.0_variables.csv   ← Bibliothèque de variables (106 variables)
│   └── CARNAC_v3.0_variables.md    ← Même contenu, lisible
│
├── 02_PHASE_0_CADRAGE/
│   ├── B-00_Inventaire.md
│   ├── B-01_MPD.md
│   ├── B-02_FDC.md
│   ├── B-03_RDR.md
│   └── B-04_PTD.md
│
├── 03_PHASE_1_ANALYSE/
│   ├── B-10_Audit_CCTP.md
│   ├── B-11_Audit_Diagnostic.md
│   ├── B-12_Audit_Geotechnique.md
│   ├── B-13_Contradictions.md
│   ├── B-14_Perimetre_Lot.md
│   └── B-15_Synthese_Risques.md
│
├── 04_PHASE_2_CONCEPTION/
│   ├── B-20_Conception_GO.md
│   ├── B-21_DDC_Preliminaire.md
│   ├── B-22_Note_Hypotheses.md
│   ├── B-23_Exploitation_Diagnostic.md
│   ├── B-24_Existant_Non_Sonde.md
│   └── B-25_Stabilite_Globale.md   ← Nouveau en v3.0
│
├── 05_PHASE_3_CALAGE/
│   ├── B-30_Calage.md
│   ├── B-31_Preuve_Superposition.md
│   ├── B-32_Vue_Nettoyee.md
│   └── B-33_Verification_Croisee.md
│
├── 06_PHASE_4_CALCULS/
│   ├── B-40_Fondations_Superficielles.md
│   ├── B-41_Fondations_Profondes.md
│   ├── B-42_Verticaux_BA.md
│   ├── B-43_Planchers_Dallages.md
│   ├── B-44_Charpente_Bois.md
│   ├── B-45_Structure_Metallique.md
│   ├── B-46_Maconnerie.md
│   ├── B-47_Escaliers.md
│   ├── B-48_Predalles.md
│   ├── B-49_Linteaux_Seuils.md
│   └── B-50_Assemblages_Ancrages.md
│
├── 07_PHASE_5_LIVRABLES/
│   ├── B-34_Synthese_Reservations.md ← Nouveau en v3.0
│   ├── B-60_Plans_Execution.md
│   ├── B-62_Nomenclature.md
│   └── B-64_Notice_Synthese.md
│
├── 08_PHASE_6_CLOTURE/
│   ├── B-70_AutoControle_Synthese.md
│   ├── B-71_Indicage.md
│   └── B-72_Journal_Cloture.md
│
├── 09_TRANSVERSE/
│   ├── T-01_Sincerite.md
│   ├── T-02_Recadrage.md
│   ├── T-03_Meta_Amelioration.md
│   └── T-04_Demande_Complement.md
│
├── 10_ANNEXES/
│   ├── A_Conventions_Livrables.md
│   ├── C_Journal_Revisions.md
│   ├── D_Mode_Emploi.md
│   └── O_Outillage.md
│
├── 11_HISTORIQUE/
│   └── Journal_des_modifications.md
│
└── 12_EXEMPLES/
    └── Exemples_Phase_0.md         ← Exemples commentés (conservés comme archive de référence)
```

Statut : 39 fiches de brique opérationnelles, 4 prompts transverse, 2 numéros vacants (B-61, B-63, fusionnés dans B-60). Les 52 fichiers de l'arborescence sont produits et contrôlés (v3.0).

---

## 8. CONVENTIONS DE NOMMAGE ET DE VERSIONNAGE

### 8.1 Nommage des fichiers de fiche
`B-XX_Intitulé_Court.md` — le numéro en premier, l'intitulé en second, séparés par un underscore. Pas de caractères spéciaux autres que _ et -. L'emplacement dans l'arborescence suit la **phase d'exécution v3.0** (§9), pas l'ordre historique de numérotation.

### 8.2 Versionnage des fiches
Chaque fiche porte en en-tête : version (x.y, incrémentée à chaque modification de la fiche) et dernière révision (date et numéro de modification C-xx, voir Journal des modifications). Une fiche modifiée sans incrémentation de version est une fiche non traçable — elle est signalée comme anomalie. Les fiches v3.0 portent toutes `Version : 3.0`.

### 8.3 Versionnage du carnet
* Modification d'une fiche → incrémentation de la version de la fiche.
* Modification de principe (verrou, mode, arborescence, ordonnancement, couche outillage) → incrémentation de la version du carnet (vX.Y).
* Une modification qui supprime un verrou sans le remplacer est interdite (non-régression). La v3.0 conserve les verrous V1 à V13 et ajoute V14 et V15 ; elle ne supprime aucune brique existante et ajoute B-25 et B-34.

### 8.4 Journal des modifications
Toute modification est consignée dans `11_HISTORIQUE/Journal_des_modifications.md`, avec : numéro, date, nature, fichiers impactés, motif, rédacteur.

### 8.5 Contrôle automatique de cohérence
Aucune version du carnet n'est publiée sans exécution du compilateur de cohérence formelle (`T1` à `T10`) sur l'arborescence complète, avec résultat **10/10 PASS, zéro erreur et zéro avertissement**. Le journal d'exécution est joint à la version publiée.

---

## 9. ORDONNANCEMENT UNIVERSEL EN 6 PHASES

**Phase 0 — Cadrage et qualification (B-00 à B-04).** Inventaire et qualification `CFG-01` (B-00). Proposition de MPD, gabarit `CFG-02`, découpage `CFG-03` (B-01). Fiche de données de conception, avec table `NIV-07` (B-02). Ouverture du RDR à quatre registres `D-xx` / `H-xx` / `PA-xx` / `V-xx` (B-03). Plan de travail dégradé (B-04).

**Phase 1 — Socle géométrique et nettoyage (B-30 → B-32 → B-31).** Calage multi-sources vers le Repère Structurel Unique (B-30). Vue nettoyée et différentielle `EXISTANT / DÉMOLITION / PROJET`, zéro cloison et zéro isolant (B-32). Preuve de superposition multi-étages et détection des porteurs non portés (B-31). **Aucune analyse ni production ne s'engage sur un fond non calé et non nettoyé.**

**Phase 2 — Audit croisé multi-pièces (B-10 à B-15).** Audits CCTP, diagnostic et géotechnique sur fond calé (B-10, B-11, B-12). Contradictions qualifiées et réconciliation quantitative (B-13). Périmètre de lot (B-14). Synthèse des risques et Pré-Audit Flash d'Exécutabilité sur 100 % des sections (B-15).

**Phase 3 — Conception et synthèse structurelle (B-20 → B-25 → B-21 → B-22 → B-23 → B-24).** Conception ou synthèse indissociable sur fond nettoyé (B-20). Stabilité globale, contreventement, joints de dilatation et sismique (B-25). Descente de charges (B-21). Note d'hypothèses `H-xx` (B-22). Exploitation du diagnostic (B-23). Existant non sondé et Points d'Arrêt `PA-xx` (B-24).

**Phase 4 — Calculs d'exécution (B-40 à B-50).** Fondations superficielles et profondes, verticaux BA, planchers et dallages, charpente bois, structure métallique, maçonnerie, escaliers, prédalles, linteaux et seuils, assemblages et ancrages. Chaque brique en régime outillé, hypothèses `H-xx` actives citées, prescriptions `ENC` et `PA-xx` reportées.

**Phase 5 — Synthèse des réservations et livrables d'exécution (B-34 → B-60 → B-62 → B-64).** Carnet unique des réservations tous corps d'état (B-34). Plans de coffrage, d'implantation et de ferraillage, zéro cloisons et zéro isolants, titre véridique, zéro collision de textes (B-60). Nomenclature extraite du DXF relu (B-62). Notice de synthèse (B-64).

**Phase 6 — Vérification croisée et clôture (B-33 → B-70 → B-71 → B-72).** Vérification croisée globale `Plan ↔ Plan ↔ Note ↔ Nomenclature` (B-33). Auto-contrôle de synthèse, contrôle des hypothèses et des Points d'Arrêt (B-70). Indiçage et supersession (B-71). Journal de clôture (B-72).

**À tout moment**
* T-01 (sincérité) : en cas de doute sur la fiabilité d'un livrable.
* T-02 (recadrage) : en cas de défaut détecté, pour diagnostiquer la cause et corriger la méthode.
* T-03 (méta-amélioration) : en fin de projet, pour transformer les incidents en corrections du carnet.
* T-04 (demande de complément) : pour formaliser une demande de pièce ou de décision.

---

## 10. CE QUI CHANGE EN v3.0 (synthèse)

1. **Posture métier explicite** : bureau d'études d'exécution de l'entreprise, qualifiée par `CFG-01` (quatre configurations), avec interdiction de réclamer un livrable MOE inexistant et obligation de transcrire les ouvrages du BET MOE.
2. **Deux verrous nouveaux** : `V14` (indissociabilité du corpus et preuve d'épuisement) et `V15` (différentiel `EXISTANT / DÉMOLITION / PROJET` et continuité mécanique descendante jusqu'aux fondations).
3. **Sixième mode `HYPOTHÈSE-NOTIFIÉE`** et tripartition des incertitudes en trois classes, avec prescriptions `ENC` et Points d'Arrêt `PA-xx`.
4. **Ordonnancement inversé** : le socle géométrique (B-30, B-32, B-31) passe en phase 1, avant tout audit et toute conception ; B-33 devient la vérification croisée finale.
5. **Deux briques nouvelles** : B-25 (stabilité globale, contreventement, joints de dilatation, sismique) et B-34 (synthèse des réservations et interfaces techniques).
6. **Gabarits d'opération** `S` / `M` / `L-XL` avec voie compacte en trois portes pour les petites affaires, y compris sans BET MOE.
7. **Loi d'airain graphique** : zéro cloison, zéro isolation, zéro doublage, zéro menuiserie de distribution sur tout plan de structure ; vérité du titre ; zéro collision de textes.
8. **Dictionnaire porté à 106 variables** : restauration des libellés corrompus `LIV-01` (conventions de calques) et `LIV-03` (formats de sortie), développement des plages de consommation, et douze variables nouvelles (`CFG-01` à `CFG-03`, `DEC-05` à `DEC-07`, `GEO-13`, `GEO-14`, `NIV-07`, `STR-01` à `STR-03`).
9. **Assainissement formel complet** : tableaux convertis en tables Markdown normalisées, mentions de version alignées, compteurs de verrous et de modes corrigés, placeholders alignés entre prompt et rappel, symétrie intégrale du graphe amont/aval, archives historiques protégées.
10. **Contrôle automatique obligatoire** : `10/10 PASS` (zéro erreur, zéro avertissement) exigé avant toute publication d'une version du carnet.

---

## 11. COMPLÉMENT v3.0.1 — LECTURE ADRESSÉE, CARNET DES FAITS, PRÉSENTATION

Voir `10_ANNEXES/A1_Addendum_v3.0.1.md` (texte opposable). Synthèse :

### 1.5 Lecture adressée du DCE
Le DCE / CCTP est **adressé à l'entreprise**. Le BET d'exécution en **extrait** ce qui concerne ses études. Il n'attend aucune réponse formelle sur une prestation qui ne lui est pas adressée (désamiantage, déplombage, cantonnements, PGC). Il ne demande un document que s'il est **nécessaire à un ouvrage prescrit** par le programme des travaux (CCTP + plans archi + EVEN). Diagnostic ≠ programme.

### 1.6 Carnet des faits
Dès `B-00`, un tableau sourcé (natures de planchers, niveaux, matériaux, neufs vs existants) est **consommé** par toutes les briques aval. Oublier un fait déjà au dossier est une non-conformité — distincte de `V14` (déclarer absent sans épuisement).

### 1.7 Présentation
Plans : fond blanc, existant gris léger **extrait** (pas dump `B-32`), ouvrages neufs en couleur, implantation **obligatoire** sur le niveau, codes CARNAC **en note**. Notes : §0 hypothèses → matériaux → charges → géométrie → DDC → vérifs → points à lever ; codes en annexe.

### 1.8 Sismique zone 1 · stabilité provisoire
Zone 1 : **aucune** vérification sismique (`B-25` SANS OBJET sur ce volet). Stabilité provisoire d'un existant : **MOE conception**, pas BET EXE.

### 1.9 Plan de principe `B-20` (v3.0.2)
Après le nettoyage `B-32`, **avant** les calculs : le livrable de conception que l'humain vise est **le plan** (repères `P` / `Pt` / `SI` / `SF` / `Lt` / `Dg`…), pas une liste. Filigrane `PRINCIPE — NE PAS EXÉCUTER`. `B-60` (EXE) reprend les mêmes repères. Sans étude de conception, ce plan est obligatoire.
