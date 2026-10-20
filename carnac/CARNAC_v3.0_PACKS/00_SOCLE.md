<!-- PACK CARNAC v3.0 — PACK 00 — SOCLE (à coller en premier, toujours) -->

# PACK 00 — SOCLE (à coller en premier, toujours)

**Quand coller ce pack** : À l'ouverture de CHAQUE nouvelle discussion, avant toute pièce de projet.

**Ce qu'il contient** : Document maître (protocole §0, 15 verrous, 6 modes, `CFG-1..4`, gabarits, ordonnancement) · annexe A (livrables, pureté structurelle) · annexe D (mode d'emploi) · annexe O (outillage et protocole CAO) · dictionnaire des 106 variables.

**Note d'usage** : Ce pack suffit à faire comprendre le protocole à une IA. Il ne permet pas encore de produire une brique : il faut y ajouter le pack de la phase concernée.

**Prérequis** : aucun — ce pack se colle en premier, à l'ouverture de la discussion.

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
**[Début du fichier : 00_MASTER.md]**

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

**[Fin de 00_MASTER.md]**

---

**[Début du fichier : 10_ANNEXES/A_Conventions_Livrables.md]**

Fichier 10_ANNEXES/A_Conventions_Livrables.md — CARNAC v3.0
> Version du document : 3.0 (carnet CARNAC v3.0) — historique des modifications : 11_HISTORIQUE/Journal_des_modifications.md.
1. OBJET
Ce document fixe les conventions de production des livrables graphiques du carnet CARNAC. Elles s'appliquent à toutes les briques de production graphique (B-20, B-31, B-32, B-60) et à toutes les briques de calcul qui produisent des plans (B-40 à B-50).
Règle de stabilité : ces conventions sont figées. Une modification passe par une révision de carnet (voir 11_HISTORIQUE/Journal_des_modifications.md), jamais par une décision de brique.
Règle de non-ambiguïté : un élément graphique (cote, ferraillage, profilé, texte) ne peut exister que sur un seul calque. Un élément partagé entre deux calques est une anomalie de production.
________________


2. CALQUES DXF NORMALISÉS
2.1 Structure de nommage
{{TYPE}}-{{FONCTION}}
* {{TYPE}} : préfixe lié au type de livrable (voir §2.2)
* {{FONCTION}} : suffixe lié à la fonction du calque (voir §2.3)
2.2 Préfixes par type de livrable

| Type de livrable | Préfixe | Brique source |
| --- | --- | --- |
| Fondations | FOND- | B-40, B-41 |
| Verticaux BA | VERT- | B-42 |
| Planchers et dallages | PLANCHER- | B-43 |
| Charpente bois | CHARPENTE- | B-44 |
| Structure métallique | METAL- | B-45 |
| Maçonnerie | MACON- | B-46 |
| Escaliers | ESCALIER- | B-47 |
| Prédalles | PREDALLE- | B-48 |
| Linteaux et seuils | LINTEAU- | B-49 |
| Assemblages et ancrages | ASSEMBLAGE- | B-50 |
| Coupes et détails transverses | DETAIL- | B-60 |

2.3 Suffixes par fonction

| Suffixe | Contenu | Présence obligatoire |
| --- | --- | --- |
| -AXES | Axes, trames, points de calage, cotes de référence | Oui |
| -COFFRAGE | Contours, épaisseurs, cotations, réservations, joints | Oui |
| -ACIER-INF | Ferraillage inférieur (nappes, sections, espacements, recouvrements) | Oui si BA |
| -ACIER-SUP | Ferraillage supérieur (nappes, chapeaux, renforts) | Oui si BA |
| -ACIER-LONG | Barres longitudinales (verticaux BA) | Oui si verticaux BA |
| -ACIER-TRANS | Cadres et armatures transversales (verticaux BA) | Oui si verticaux BA |
| -PROFILES | Profilés métalliques (sections, positions, repères) | Oui si métal |
| -EXISTANT | Éléments existants à conserver (gris, trait fin) | Oui (même vide) |
| -DETAILS | Détails à grande échelle (1/20, 1/10, 1/5) | Oui |
| -NOMENCLATURE | Nomenclature des aciers, profilés, connecteurs | Oui |
| -HABILLAGE-TEXTE | Textes, légendes, cartouche, notes, tableaux | Oui |
| -COTATION | Cotations isolées (si volumineuses) | Non (optionnel) |

2.4 Règles d'usage
1. Un élément = un seul calque. Pas de calque fourre-tout, pas d'élément partagé entre deux calques.
2. Les calques -EXISTANT sont toujours présents, même vides. Leur absence est une anomalie de traçabilité.
3. Les calques -HABILLAGE-TEXTE et -NOMENCLATURE sont toujours présents et renseignés.
4. Aucun élément du livrable sur le calque 0 (calque par défaut AutoCAD).
5. Les calques de travail interne (DEFPOINTS, _Construction, _Grille) sont supprimés à l'export.
6. Les calques vides (sauf -EXISTANT) sont supprimés à l'export.
2.5 Exemple complet — Plan de fondations
text
FOND-AXES
FOND-COFFRAGE
FOND-ACIER-INF
FOND-ACIER-SUP
FOND-EXISTANT
FOND-DETAILS
FOND-NOMENCLATURE
FOND-HABILLAGE-TEXTE
________________


3. ÉCHELLES AUTORISÉES

| Échelle | Usage | Exemples |
| --- | --- | --- |
| 1/500 | Vue d'ensemble, plan de situation | Plan masse |
| 1/200 | Vue d'ensemble, plan d'étage | Plan de structure d'ensemble |
| 1/100 | Plans courants | Plan de coffrage d'étage |
| 1/50 | Plans d'exécution courants | Plan de fondations, plan de plancher |
| 1/20 | Détails courants, coupes de principe | Coupe de semelle, coupe de poteau |
| 1/10 | Détails d'assemblage | Détail de platine, détail de sabot |
| 1/5 | Détails singuliers | Ferraillage d'about, ancrage de barre |

Règle : une échelle hors de cette liste doit être justifiée dans le cartouche (mention « échelle exceptionnelle : [motif] »).
Règle de cohérence : sur un même plan, l'échelle du plan général et celles des détails sont indiquées séparément dans le cartouche.
________________


4. FORMATS DE SORTIE
4.1 Trois formats obligatoires
Chaque livrable graphique est produit en trois formats :

| Format | Usage | Nommage |
| --- | --- | --- |
| DXF | Échange avec outils, réutilisation par B-62 et B-64 | {{TYPE}}_EXE_{{indice}}.dxf |
| PDF | Impression, archivage, diffusion officielle | {{TYPE}}_EXE_{{indice}}.pdf |
| PNG | Diffusion rapide, insertion dans comptes rendus | {{TYPE}}_EXE_{{indice}}.png |

4.2 Cas particuliers

| Cas | Suffixe ajouté | Exemple |
| --- | --- | --- |
| Mode PARAMÉTRIQUE | _P | FOND_EXE_A_P.pdf |
| Mode PARTIEL-DÉCLARÉ | _D | FOND_EXE_B_D.pdf |
| Version provisoire (avant clôture B-71) | _PROV | FOND_EXE_A_PROV.pdf |
| Vue nettoyée (B-32) | _NET | FOND_VUE-NETTOYEE_A_NET.pdf |
| Preuve de superposition (B-31) | _SUP | FOND_PREUVE-SUP_A_SUP.pdf |

4.3 Résolution et qualité

| Format | Paramètre |
| --- | --- |
| PDF | Vectoriel, pas de rasterisation sauf pour les images importées |
| PNG | 300 dpi minimum, fond blanc, transparence désactivée |
| DXF | Version AutoCAD 2013 minimum (compatibilité descendante), unités en millimètres |

________________


5. CARTOUCHE TYPE
5.1 Zones du cartouche
Le cartouche comporte sept zones obligatoires :

| Zone | Position | Contenu |
| --- | --- | --- |
| Zone 1 | Haut gauche | Code projet (ID-01) et intitulé (ID-02) |
| Zone 2 | Haut droite | Logo ou nom de l'entreprise GO |
| Zone 3 | Centre | Intitulé du plan, type de livrable, niveau concerné |
| Zone 4 | Bas gauche | Indice, date, échelle, format |
| Zone 5 | Bas centre | Brique source (B-xx), mode d'exécution |
| Zone 6 | Bas droite | Numéro de plan, révision, visas |
| Zone 7 | Bandeau | Mentions obligatoires |

5.2 Contenu des zones
Zone 1 :
text
Code projet : {{ID-01}}
Intitulé : {{ID-02}}
Zone 2 :
text
Logo / nom entreprise GO
Zone 3 :
text
Intitulé : {{intitulé du plan}}
Type : {{type livrable}}
Niveau : {{niveau}}
Zone 4 :
text
Indice : {{A/B/C...}}
Date : {{JJ/MM/AAAA}}
Échelle : {{1/50, 1/20...}}
Format : {{A0/A1/A2/A3/A4}}
Zone 5 :
text
Brique source : {{B-xx}}
Mode : {{COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE / INTERNE-GO}}
Zone 6 :
text
N° plan : {{numéro}}
Révision : {{xx}}
Visas : {{BET / BC / MOE / MOA}}
Zone 7 (bandeau, texte fixe) :
text
NE PAS EXÉCUTER SANS EXE COTÉ ET VISA
Protection au feu adéquate à prévoir (hors lot GO)
[Si PARAMÉTRIQUE] PROVISOIRE — EN ATTENTE DE [donnée]
[Si PARTIEL-DÉCLARÉ] Établi sous hypothèse(s) déclarée(s) — voir RDR
5.3 Mentions fixes
Certaines mentions sont toujours présentes, quelle que soit la brique :

| Mention | Position |
| --- | --- |
| « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » | Zone 7 (bandeau) |
| « Protection au feu adéquate à prévoir (hors lot GO) » | Zone 7 (bandeau) |
| Indice et date | Zone 4 |
| Échelle | Zone 4 |
| Brique source et mode | Zone 5 |

________________


6. NOMENCLATURE TYPE
6.1 Structure de la nomenclature graphique
La nomenclature graphique intégrée au plan (produite par B-60) comporte au minimum les colonnes suivantes :

| Colonne | Contenu | Exemple |
| --- | --- | --- |
| Repère | Identifiant du repère sur le plan | F1, P2, S/P3 |
| Désignation | Nature de l'élément | Semelle filante, Poteau BA, Profilé HEB200 |
| Section / diamètre | Section ou diamètre | HA12, HEB200, 140×140×8 |
| Longueur / quantité | Longueur ou nombre | 3200 mm, 4 |
| Observations | Notes spécifiques | équerre, avec platine |

6.2 Structure de la nomenclature détaillée (B-62)
La nomenclature détaillée produite par B-62 comporte les colonnes suivantes :

| Colonne | Contenu | Unité |
| --- | --- | --- |
| Repère | Identifiant du repère | — |
| Désignation | Nature détaillée | — |
| Section / diamètre | Section ou diamètre | mm |
| Longueur unitaire | Longueur d'une barre ou d'un élément | mm |
| Nombre | Nombre d'occurrences | — |
| Longueur totale | Longueur cumulée | mm |
| Poids | Poids cumulé (acier uniquement) | kg |
| Calque source | Calque du plan B-60 d'où l'élément est extrait | — |

6.3 Nomenclature de façonnage (aciers BA)
Pour chaque type de barre, la nomenclature de façonnage comporte :

| Colonne | Contenu |
| --- | --- |
| Repère | Identifiant |
| Diamètre | HA6, HA8, HA10, HA12, HA14, HA16, HA20, HA25, HA32 |
| Forme | Droite, équerre, U, cadre, épingle, chapeau |
| Cotes de façonnage | Longueurs de chaque segment, angles |
| Longueur développée | Longueur totale dépliée (mm) |
| Longueur de recouvrement | Si applicable (mm) |
| Diamètre de mandrin | Si cintrage (mm) |
| Quantité | Nombre d'occurrences |

________________


7. UNITÉS ET PRÉCISIONS
7.1 Unités par type de valeur

| Type de valeur | Unité | Précision |
| --- | --- | --- |
| Cotes de plan | Millimètres (mm) | Entier |
| Cotes de niveau | Mètres (m) | 3 décimales |
| Sections de barres | Millimètres (mm) | Entier (HA12) |
| Sections de profilés | Millimètres (mm) | Entier (HEB200) |
| Longueurs développées d'acier | Millimètres (mm) | Entier |
| Poids d'acier | Kilogrammes (kg) | 1 décimale |
| Charges linéiques | kN/m | 2 décimales |
| Charges ponctuelles | kN | 2 décimales |
| Moments | kNm | 2 décimales |
| Contraintes | MPa | 1 décimale |
| Résistances | MPa | 1 décimale |
| Niveaux NGF | mètres | 3 décimales |

7.2 Règle de non-ambiguïté
Toute valeur numérique dans un livrable est suivie de son unité, sauf dans les tables où la colonne indique l'unité.
7.3 Arrondis

| Type de valeur | Règle d'arrondi |
| --- | --- |
| Cotes de plan | Arrondi à l'entier (mm) |
| Niveaux | Arrondi au millimètre |
| Sections d'acier | Arrondi à la section commerciale supérieure |
| Résultats de calcul | Arrondi à la précision affichée, jamais d'arrondi intermédiaire |

________________


8. RÈGLES DE NOMMAGE DES FICHIERS LIVRÉS
8.1 Format général
{{TYPE}}_EXE_{{indice}}.{{extension}}
8.2 Exemples

| Fichier | Contenu |
| --- | --- |
| FOND_EXE_A.dxf | Plan de fondations, indice A, DXF |
| FOND_EXE_A.pdf | Plan de fondations, indice A, PDF |
| FOND_EXE_A.png | Plan de fondations, indice A, PNG |
| VERT_EXE_B_P.pdf | Plan de verticaux, indice B, mode PARAMÉTRIQUE |
| PLANCHER_EXE_A_D.pdf | Plan de plancher, indice A, mode PARTIEL-DÉCLARÉ |
| FOND_VUE-NETTOYEE_A_NET.dxf | Vue nettoyée du plan de fondations |
| FOND_PREUVE-SUP_A_SUP.pdf | Preuve de superposition du plan de fondations |

8.3 Règles complémentaires
1. Pas d'espaces dans les noms de fichiers (remplacer par _).
2. Pas d'accents dans les noms de fichiers.
3. Pas de caractères spéciaux autres que _ et -.
4. Indice en majuscule (A, B, C...).
5. Extension en minuscule (dxf, pdf, png).
________________


9. RÈGLES DE VERSIONNAGE DES LIVRABLES
9.1 Indice des livrables
* Indice A : première émission
* Indice B, C, D... : révisions successives
* Un indice ne se saute pas : on ne passe jamais de A à C sans B
9.2 Motifs de révision
Une révision de livrable est justifiée par :
* une correction d'erreur (motif : correction)
* une modification de conception (motif : modification)
* un ajout d'élément (motif : ajout)
* une suppression d'élément (motif : suppression)
* une mise à jour de donnée source (motif : maj_source)
Le motif est consigné dans le RDL (B-71).
9.3 Supersession
Un nouveau livrable remplace et annule l'indice précédent. La mention figure dans le cartouche :
text
Ce livrable remplace et annule l'indice {{précédent}} du {{date}}.
________________


10. GESTION DES RÉSERVES SUR LES LIVRABLES
10.1 Livrables en mode dégradé

| Mode | Marque visuelle | Mention au cartouche |
| --- | --- | --- |
| COMPLET | Aucune | — |
| PARTIEL-DÉCLARÉ | Filigrane jaune | « Établi sous hypothèse(s) déclarée(s) — voir RDR » |
| PARAMÉTRIQUE | Filigrane rouge | « PROVISOIRE — EN ATTENTE DE [donnée] » |
| INTERNE-GO | Aucune (mode de conception, pas d'exécution) | Mention « Étude de conception — ne se substitue pas à l'EXE » |
| SANS OBJET | Pas de livrable | Ligne de justification au RDR |

10.2 Livrables en attente de données
Un livrable en mode PARAMÉTRIQUE :
* porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
* est suffixé _P dans son nom de fichier ;
* mentionne la donnée manquante dans le cartouche (zone 7) ;
* n'est jamais diffusé comme livrable exécutable.
10.3 Livrables en attente de visa
Un livrable dont les visas ne sont pas obtenus porte la mention :
text
VISA EN ATTENTE : [BET / BC / MOE / MOA]
NE PAS EXÉCUTER
________________


11. CAS PARTICULIERS
11.1 Plans de principe (B-20)
Un plan de principe (B-20, mode INTERNE-GO) porte :
* le filigrane « PRINCIPE — NE PAS EXÉCUTER » ;
* un indice P (premier principe, P2, P3... pour les suivants) ;
* la mention « Étude de conception — ne se substitue pas à l'EXE ».
11.2 Vues nettoyées (B-32)
Une vue nettoyée (B-32) porte :
* la mention « Vue nettoyée — fond de plan uniquement » ;
* un nommage {{TYPE}}_VUE-NETTOYEE_{{indice}} ;
* un indice de version de la vue nettoyée, distinct de l'indice du livrable.
11.3 Preuves de superposition (B-31)
Une preuve de superposition (B-31) porte :
* la mention « Preuve de superposition » ;
* la mention du livrable vérifié (code + indice) ;
* la mention du fichier source utilisé (code + indice) ;
* un nommage {{TYPE}}_PREUVE-SUP_{{indice}}.
11.4 Notes de calcul
Une note de calcul (B-40 à B-50) porte :
* en en-tête : code projet, intitulé, indice, date, mode, brique source ;
* en pied : visas requis et mention « NE PAS EXÉCUTER SANS VISA » ;
* en annexe : liste des pièces jointes (plans, nomenclatures, preuves).
________________


12. RÈGLES DE DIFFUSION
12.1 Diffusion interne (GO)
Tous les livrables sont diffusés en interne, y compris les modes dégradés (PARTIEL-DÉCLARÉ, PARAMÉTRIQUE).
12.2 Diffusion externe (MOE, BC, MOA)
Seuls les livrables en mode COMPLET ou PARTIEL-DÉCLARÉ sont diffusés en externe. Les livrables PARAMÉTRIQUE ne sont diffusés qu'à titre informatif, avec mention explicite « provisoire, ne pas exécuter ».
12.3 Diffusion pour exécution (entreprise)
Seuls les livrables visés (BET, BC, MOE, MOA) sont diffusés pour exécution. Un livrable non visé porte la mention « NE PAS EXÉCUTER ».
________________


13. FICHIERS DE RÉFÉRENCE

| Fichier | Contenu |
| --- | --- |
| 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv | Variables, dont LIV-01 à LIV-05 (conventions) |
| 11_HISTORIQUE/Journal_des_modifications.md | Modifications de ces conventions |
| 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md | Brique de production graphique |
| 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md | Brique de nomenclature détaillée |

________________
---

## 11. COMPLÉMENT v2.0 — TOLÉRANCES D'EXÉCUTION ET ENROBAGE
1. Les plans d'exécution sont établis pour la classe d'exécution déclarée en note d'hypothèses (NF EN 13670) ; les tolérances qui affectent le calcul sont celles de cette classe.
2. L'enrobage figuré sur les plans est l'enrobage nominal c_nom = c_min + Δc_dev (EC2 §4.4), avec Δc_dev = 10 mm sauf justification contraire portée en FDC (MAT-03).
3. Les cotes de plan sont en millimètres (entiers) ; les cotes de niveau en mètres (3 décimales). Aucune autre convention d'unités n'est admise sur un livrable (corrige la contradiction d'unités historique entre la présente annexe et la fiche B-60).

---

## 8. PURETÉ STRUCTURELLE, HYPOTHÈSES NOTIFIÉES ET CONTRÔLE DE RENDU (nouveau en v3.0)

### 8.1 Loi d'airain graphique — zéro second œuvre
Sur **tout** plan de structure produit par le carnet (plans de principe, plans de coffrage, plans d'implantation, plans de ferraillage, coupes et détails), sont **interdits** :
* les cloisons, doublages, contre-cloisons et complexes de finition ;
* les isolants thermiques et acoustiques, y compris les complexes isolants périphériques des façades ;
* les menuiseries de distribution intérieure, les revêtements, les faux plafonds et le mobilier.

Sont **autorisés et attendus** : les éléments porteurs (existants, conservés, démolis, neufs), les ouvertures mécaniques (baies, trémies, percements, réservations), la trémie et l'escalier, la structure neuve, les attentes et scellements, les axes et trames, les cotations et les repères.

### 8.2 Différentiel graphique `EXISTANT / DÉMOLITION / PROJET`
Chaque vue structurelle porte trois états graphiques distincts et une légende normalisée :
| État | Calque | Convention graphique |
| --- | --- | --- |
| EXISTANT conservé | `*-EXISTANT` | trait fin, gris |
| EXISTANT démoli | `*-EXISTANT` + suffixe `-DEM` | trait pointillé, gris clair, hachures de démolition |
| PROJET neuf | calques de fonction (`-COFFRAGE`, `-ACIER-*`, `-PROFILES`) | trait fort, noir ou couleur de fonction |

Une vue qui ne permet pas de distinguer les trois états est refusée (V15).

### 8.3 Hypothèses notifiées `H-xx`
Toute valeur issue du mode `HYPOTHÈSE-NOTIFIÉE` est reportée :
1. sur les plans, par un **nuage graphique** fermé entourant la zone concernée, avec le repère `H-xx` en texte lisible ;
2. en tête de note, par un encadré listant valeur, norme d'appui, zone d'application et délai de contradiction (`DEC-06`) ;
3. dans le tableau des hypothèses du livrable, avec le statut (active, expirée, acceptée, contredite).

Une hypothèse sans norme d'appui n'est pas notifiée : c'est une valeur de repli interdite (V3).

### 8.4 Prescriptions chantier `ENC` et Points d'Arrêt `PA-xx`
Toute inconnue physique est portée par un encadré `ENC` (prescription opposable : sondage, dépose, fouille, curage, essai) et par un Point d'Arrêt `PA-xx` (arrêt de production avant poursuite, avec critère de lever et conséquence chiffrée). L'encadré figure **à la fois** sur le plan et en tête de la note, mot pour mot.

### 8.5 Contrôle de rendu obligatoire (`0` collision)
Aucun plan n'est diffusé avant contrôle automatisé, journalisé au format de l'annexe O §7 :
| Contrôle | Seuil |
| --- | --- |
| Chevauchement de textes | 0 |
| Cote orpheline (sans entité cotée à moins de 22 cm) | 0 |
| Entité sur le calque `0` | 0 |
| Entité de second œuvre sur un calque de structure | 0 |
| Titre du plan non couvert par le contenu géométrique | 0 (vérité du titre) |
| Réservation non reportée depuis le carnet B-34 | 0 |

### 8.6 Plan de réservations (B-34)
Le plan de réservations est établi sur le fond structurel pur, avec tableau intégré (repère, niveau, élément porteur, position, dimensions, altitude, lot, statut). Il porte les mêmes axes et les mêmes repères que les plans de coffrage, et il est référencé dans la notice de synthèse.

**[Fin de 10_ANNEXES/A_Conventions_Livrables.md]**

---

**[Début du fichier : 10_ANNEXES/D_Mode_Emploi.md]**

Fichier 10_ANNEXES/D_Mode_Emploi.md — CARNAC v3.0
________________


D — MODE D'EMPLOI DU CARNET
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Nature | Document de référence — annexe D du carnet |
| Objet | Expliquer comment utiliser le carnet CARNAC au quotidien, projet par projet |
| Public | Ingénieur qui pilote la production d'études d'exécution |
| Statut | Document stable — ne change qu'avec une révision du carnet |

Distinction avec le document maître (00_MASTER.md) :
   * le document maître décrit ce qu'est le carnet (principes, verrous, modes, arborescence) ;
   * ce mode d'emploi décrit comment s'en servir (quelle fiche ouvrir, quel prompt copier, dans quel ordre, avec quelles précautions).
________________


2. CE QUE VOUS AVEZ EN MAIN
Le carnet CARNAC se compose de trois types de documents :

| Type | Nature | Usage |
| --- | --- | --- |
| Documents de référence (ce document, document maître, dictionnaire, annexes) | Stables, consultés en permanence | Comprendre le carnet, vérifier une convention, connaître un verrou |
| Fiches de brique (B-xx_Intitulé.md) | Une fiche par tâche | Ouvrir la fiche quand vous devez exécuter la tâche correspondante |
| Prompts transverse (T-xx_Intitulé.md) | Utilisables à tout moment | Ouvrir quand vous avez besoin de contrôler, recadrer, demander un complément |

Chaque fiche de brique contient quatre sections :

| Section | Contenu | À qui s'adresse-t-elle ? |
| --- | --- | --- |
| 1. En-tête | Version, phase, modes d'appel, entrées, sortie, critère d'acceptation | À vous : pour savoir quand et comment appeler la brique |
| 2. Prompt | Le bloc de code entre triples backquotes | À l'IA : c'est le seul texte à copier-coller |
| 3. Justification des clauses clés | Pourquoi chaque clause existe | À vous : pour comprendre et pouvoir modifier |
| 4. Références | Briques amont, briques aval, variables consommées | À vous : pour savoir ce qui alimente et ce qui dépend de la brique |

Ce que vous copiez dans l'IA : uniquement le bloc de code de la section 2. Le reste est de la documentation pour vous.
________________


3. DÉMARRAGE D'UN NOUVEAU PROJET — LES 6 ÉTAPES
Vue d'ensemble
text
Phase 0 (Cadrage) ──► Phase 1 (Analyse) ──► Phase 2 (Conception)
      │                                           │
      │                                           ▼
      └──► Phase 3 (Calage) ──► Phase 4 (Calculs) ──► Phase 5 (Livrables)
                                                                 │
                                                                 ▼
                                                        Phase 6 (Clôture)
Durée indicative par phase (variable selon le projet) :

| Phase | Durée indicative | Livrables principaux |
| --- | --- | --- |
| 0 — Cadrage | 1 à 2 jours | Inventaire, MPD, FDC, RDR, PTD |
| 1 — Analyse | 3 à 5 jours | Audits, contradictions, périmètre, risques |
| 2 — Conception | 2 à 10 jours selon complexité | Conception GO, DDC préliminaire, hypothèses |
| 3 — Calage | 1 à 2 jours | Calage, preuve, vues nettoyées |
| 4 — Calculs | 10 à 30 jours selon volume | Notes de calcul, plans |
| 5 — Livrables | 3 à 5 jours | DXF/PDF/PNG, nomenclatures, notices |
| 6 — Clôture | 1 à 2 jours | Auto-contrôle, indiçage, journal |

________________


Étape 1 — Cadrage (Phase 0)
Objectif : constituer les trois documents d'entrée (MPD, FDC, RDR) et identifier immédiatement ce qui bloque.
Fiches à exécuter, dans l'ordre :

| Ordre | Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- | --- |
| 1 | B-00 Inventaire | Copier le prompt, fournir les pièces du projet | La liste des pièces, la reformulation de mission |
| 2 | B-01 MPD | Copier le prompt, fournir l'inventaire B-00 | Ligne par ligne les NON NÉCESSAIRE (périmètre) |
| 3 | B-02 FDC | Copier le prompt, fournir la MPD validée | Chaque valeur et sa source |
| 4 | B-03 RDR | Copier le prompt, fournir la FDC | Chaque décision (auteur, date) et chaque réserve |
| 5 | B-04 PTD | Copier le prompt, fournir la MPD, la FDC et le RDR | Le PTD : ce qui est suspendu, ce qui est exécutable |

Point de contrôle critique : à l'issue de B-01, vous validez (ou refusez) chaque NON NÉCESSAIRE. C'est votre décision, pas celle du modèle. Un NON NÉCESSAIRE mal validé bloque une brique qui aurait dû s'exécuter.
Si une donnée bloquante manque : B-04 produit un PTD. Vous savez immédiatement ce qui est faisable et ce qui ne l'est pas. T-04 peut être utilisée pour demander le complément.
________________


Étape 2 — Analyse (Phase 1)
Objectif : auditer les pièces, identifier les contradictions, clarifier le périmètre, hiérarchiser les risques.
Fiches à exécuter :

| Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- |
| B-10 Audit CCTP | Copier le prompt, fournir le CCTP | La liste des points à lever avec destinataires |
| B-11 Audit Diagnostic | Copier le prompt, fournir le diagnostic | Chaque [ANALYSE GO] est bien la vôtre |
| B-12 Audit Géotechnique | Copier le prompt, fournir le rapport G2 | La recommandation de mission complémentaire |
| B-13 Contradictions | Copier le prompt, fournir B-10, B-11, B-12 | Le classement gravité × nature |
| B-14 Périmètre de lot | Copier le prompt, fournir B-10, B-11 | Les prestations À TRANCHER |
| B-15 Synthèse des risques | Copier le prompt, indiquer le périmètre | Les risques résiduels acceptés |

Points de contrôle critiques :
   * B-10 : avant transmission à la MOE, valider les destinataires et urgences.
   * B-11 : chaque cellule [ANALYSE GO] doit être votre analyse, pas une reformulation du diagnostic.
   * B-12 : la décision de commander (ou non) une mission G3/G4 est une décision MOA, pas la vôtre.
   * B-14 : une prestation que vous acceptez implicitement devient la vôtre, même si le CCTP ne la prescrit pas.
   * B-15 : valider les risques résiduels acceptés — c'est l'engagement qui vous engage.
________________


Étape 3 — Conception (Phase 2)
Objectif : concevoir la structure GO si le BET de conception est absent, ou compléter ce qu'il n'a pas fourni ; prédimensionner et produire les plans de principe ; poser les hypothèses.
Fiches à exécuter (dans l'ordre) :

| Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- |
| B-20 Conception GO | Copier le prompt, choisir le mode (INTERNE-GO / PARTIEL-DÉCLARÉ / SANS OBJET), fournir la géométrie archi et les contraintes existantes | La trame, les sections de principe, la liste des points à faire valider par un tiers |
| B-21 DDC préliminaire | Copier le prompt, fournir les charges et les usages | Les catégories d'usage EC1 et les cloisons forfaitaires |
| B-22 Note d'hypothèses | Copier le prompt, fournir la FDC | Chaque hypothèse à son introduction (pas après) |
| B-23 Exploitation diagnostic | Copier le prompt, fournir B-11 et B-20 | Les orientations de renforcement ne sont pas des dimensionnements |
| B-24 Existant non sondé | Copier le prompt, fournir EXI-xx | Le tableau de sensibilité est bien marqué « NON CONTRACTUEL » |

Points de contrôle critiques :
   * B-20 : le visa de la conception (par vous, un BET, ou le BC) avant que les briques de calcul ne s'appuient dessus.
   * B-21 : les catégories d'usage sont vos choix, pas ceux du modèle.
   * B-22 : une hypothèse validée trop tard est une hypothèse qui a déjà contaminé les calculs. Validez à l'introduction.
   * B-24 : décider de commander les essais, ou d'inscrire au RDR une valeur déclarée (PARTIEL-DÉCLARÉ).
Cas particulier — pas de BET de conception : B-20 s'appelle en mode INTERNE-GO. La sortie de B-20 (trame, sections de principe, plans de principe filigranés) devient l'entrée de toutes les briques de calcul.
________________


Étape 4 — Calage et calculs (Phases 3 et 4)
Objectif : caler la géométrie sur le fichier source, puis produire les notes de calcul et les plans d'exécution.
4.1 Calage (une fois par projet)

| Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- |
| B-30 Calage | Copier le prompt, fournir le DXF/DWG source | Le résidu de calage (≤ 1 cm) et la preuve de superposition |

B-30 est exécutée une seule fois pour le projet. Le fichier « calé » est une donnée de projet, réutilisée par toutes les briques graphiques.
4.2 Pour chaque livrable graphique (à chaque brique de calcul)

| Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- |
| B-32 Vue nettoyée | Copier le prompt, fournir le fichier calé et le type de livrable | La liste des calques À TRANCHER |
| B-31 Preuve de superposition | Copier le prompt, fournir le livrable produit | Le verdict global sur chaque livrable |
| B-33 Vérification croisée | Copier le prompt, fournir le livrable et le RDL | Les écarts section 2 (plan ↔ plan) avant de relancer la brique source |

4.3 Briques de calcul (phase 4)
Choisir la brique selon le type d'élément :

| Élément à calculer | Fiche |
| --- | --- |
| Fondations superficielles | B-40 |
| Fondations profondes (vérification) | B-41 |
| Poteaux, jambages, voiles | B-42 (paramètre {{élément}}) |
| Planchers, dallages | B-43 (paramètre {{type}}) |
| Charpente bois | B-44 (paramètre {{élément}}) |
| Structure métallique | B-45 (paramètre {{élément}}) |
| Maçonnerie (vérification et conception) | B-46 (paramètre {{bloc}} = A / B / A+B) |
| Escaliers | B-47 (paramètre {{type}}) |
| Prédalles | B-48 (paramètre {{phase}}) |
| Linteaux et seuils | B-49 (paramètre {{type}}) |
| Assemblages et ancrages | B-50 (paramètre {{famille}}) |

Pour chaque brique de calcul :
   1. Ouvrir la fiche.
   2. Lire l'en-tête : mode d'appel, entrées lues, sortie attendue.
   3. Copier le bloc de code.
   4. Remplacer les {{...}} par les valeurs du projet (mode, élément, type).
   5. Fournir les données d'entrée (FDC, DDC, hypothèses, notes amont).
   6. Vérifier l'auto-contrôle produit par la brique.
Points de contrôle critiques :
   * B-40 à B-50 : vérifier que la brique est bien en mode COMPLET si toutes les données sont disponibles, PARAMÉTRIQUE sinon.
   * B-42 : valider le type d'élément (poteau / jambage / voile) pour chaque vertical.
   * B-43 : valider le type de plancher (dalle / dallage / plancher bois).
   * B-46 : valider la frontière avec le spécialiste (injection, tirants).
   * B-47 : valider la méthode de calcul pour escalier balancé ou hélicoïdal.
   * B-49 : valider la méthode de charge pour linteau court (triangulaire vs linéique).
   * B-50 : valider le contrôle croisé — c'est vous qui décidez quelle brique corrige.
Si une donnée bloquante manque : la brique s'appelle en mode PARAMÉTRIQUE. Le livrable est filigrané et suffixé _P. Consulter le PTD (B-04) pour savoir ce qui reste faisable.
________________


Étape 5 — Livrables (Phase 5)
Objectif : produire les plans d'exécution, les nomenclatures et la notice de synthèse.
Fiches à exécuter, dans l'ordre :

| Ordre | Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- | --- |
| 1 | B-60 Plans d'exécution | Copier le prompt, fournir la note de calcul et la vue nettoyée | Le cartouche, l'indice, la structure DXF |
| 2 | B-62 Nomenclature | Copier le prompt, fournir les plans B-60 | La nomenclature avant transmission au fournisseur |
| 3 | B-64 Notice de synthèse | Copier le prompt, fournir la note, les plans, la nomenclature, le RDL et le RDR | Les visas requis |

Points de contrôle critiques :
   * B-60 : c'est vous qui décidez du numéro d'indice (A, B, C) en fonction du cycle de révision.
   * B-60 : validation de la structure DXF avant diffusion — un DXF mal structuré est inutilisable.
   * B-62 : une erreur de quantité commandée coûte cher.
   * B-64 : c'est vous qui savez qui doit viser (BC, BET, MOE) selon le contexte contractuel.
________________


Étape 6 — Clôture (Phase 6)
Objectif : faire l'auto-contrôle de synthèse, indiçer les documents, produire le journal de clôture.
Fiches à exécuter, dans l'ordre :

| Ordre | Fiche | Ce que vous faites | Ce que vous validez |
| --- | --- | --- | --- |
| 1 | B-70 Auto-contrôle de synthèse | Copier le prompt, fournir tous les auto-contrôles des briques | Le verdict global |
| 2 | B-71 Indiçage | Copier le prompt, fournir le RDL et les documents | Les motifs de révision |
| 3 | B-72 Journal de clôture | Copier le prompt, fournir le RDL, le RDR, B-70 et B-71 | Les points ouverts à traiter avant remise |

Points de contrôle critiques :
   * B-70 : votre appréciation de la criticité des incohérences fait foi, pas la seule liste.
   * B-71 : vous seul savez si une révision est justifiée.
   * B-72 : certains points ouverts peuvent être « acceptés » par votre décision, d'autres pas. C'est vous qui décidez lesquels doivent être traités avant remise.
________________


4. UTILISATION DES PROMPTS TRANSVERSE
Ces prompts s'utilisent à tout moment, pas dans une phase particulière.
T-01 — Sincérité
Quand : après chaque production graphique importante, après chaque note de calcul, en cas de doute sur la fiabilité d'un livrable, avant transmission à un tiers.
Ce qu'il fait : classe tous les éléments du livrable en trois catégories (certain / de principe / à lever) et donne un verdict de sincérité.
Ce que vous validez : le verdict et la liste des éléments à lever.
T-02 — Recadrage
Quand : quand un livrable présente un défaut visible, quand une deuxième version ne corrige pas la première, quand un modèle « corrige » sans expliquer.
Ce qu'il fait : diagnostique la cause du défaut dans la méthode, propose une nouvelle méthode reproductible, applique et prouve la correction.
Ce que vous validez : le diagnostic et la preuve de correction.
T-03 — Méta-amélioration
Quand : après chaque projet terminé, après un incident significatif (T-02 déclenché), après l'ajout ou la suppression d'une brique.
Ce qu'il fait : analyse les incidents du projet, propose des corrections au carnet, classe en GÉNÉRALE / PROJET / À ÉTUDIER.
Ce que vous validez : les corrections GÉNÉRALES à intégrer au carnet (c'est vous qui décidez d'une nouvelle version).
T-04 — Demande de complément
Quand : à la fin de la phase 0 (données bloquantes identifiées), à tout moment si une donnée bloquante est découverte, avant remise d'un livrable important.
Ce qu'il fait : rédige une demande formelle à la MOE/BET/MOA, structurée et datée, avec conséquence de non-réponse et échéance.
Ce que vous validez : la forme de la demande et la priorisation (URGENTE / IMPORTANTE / DE SUIVI).
________________


5. LES CINQ PRÉCAUTIONS À PRENDRE
Précaution 1 — Ne copier que le bloc de code
Le prompt est dans la section 2 de la fiche, entre triples backquotes. Les en-têtes et les justifications sont pour vous, pas pour l'IA.
Précaution 2 — Remplacer tous les {{...}} avant envoi
Aucun {{...}} ne doit subsister dans le prompt envoyé. C'est le verrou V7 (zéro placeholder résiduel). Si vous en oubliez un, l'IA peut le combler à votre place — et ce ne sera pas votre choix.
Précaution 3 — Vérifier le mode avant d'appeler une brique
Le mode (COMPLET, PARTIEL-DÉCLARÉ, PARAMÉTRIQUE, INTERNE-GO, SANS OBJET) doit être cohérent avec la disponibilité des données. Un COMPLET sur une donnée bloquante manquante est une faute (V12).
Précaution 4 — Vérifier le critère d'acceptation à la fin
Chaque brique a un critère d'acceptation dans son en-tête. Si le critère n'est pas satisfait, la brique n'est pas terminée — et l'IA doit le signaler.
Précaution 5 — Consigner au RDL et au RDR
Chaque livrable produit est consigné au RDL (registre des livrables). Chaque décision, réserve ou verrou est consigné au RDR. Sans cette consignation, la traçabilité est rompue — et la mise à jour incrémentale (B-32) devient impossible.
________________


6. QUE FAIRE EN CAS DE PROBLÈME

| Problème | Que faire |
| --- | --- |
| Une donnée bloquante manque | B-04 (PTD) vous dit ce qui est faisable. T-04 rédige la demande de complément. |
| Un livrable est défaillant | T-02 diagnostique la cause et corrige la méthode. |
| Un livrable est douteux (sincérité) | T-01 classe les éléments en certain / de principe / à lever. |
| Une incohérence entre briques | B-70 détecte et identifie la brique responsable. |
| Un défaut se répète | T-03 propose une correction générale au carnet. |
| Une donnée change en cours de projet | B-32 met à jour uniquement les livrables impactés (via le RDL). |
| Une décision est à prendre | RDR section 1 : décision avec auteur, date, justification. |
| Une demande de complément est sans réponse | T-04 relance, puis B-72 la cite dans les points ouverts à la clôture. |

________________


7. CE QUE VOUS NE FAITES PAS
   * Vous ne copiez pas les en-têtes et justifications dans l'IA.
   * Vous ne validez pas un NON NÉCESSAIRE sans vérifier qu'il est justifié par le périmètre (pas par la disponibilité).
   * Vous ne validez pas un COMPLET sur une donnée bloquante manquante (V12).
   * Vous ne laissez pas un {{...}} dans un prompt envoyé (V7).
   * Vous ne diffusez pas un livrable PARAMÉTRIQUE sans filigrane et sans mention.
   * Vous n'exécutez pas un livrable sans visa.
   * Vous ne modifiez pas le carnet sans passer par T-03 et une révision de version.
________________


8. CE QUE VOUS FAITES SYSTÉMATIQUEMENT
   * Vous validez ligne par ligne les NON NÉCESSAIRE de la MPD (B-01).
   * Vous validez les valeurs et leur fiabilité à la FDC (B-02).
   * Vous validez les décisions avec auteur, date et effet (B-03).
   * Vous validez les risques résiduels acceptés (B-15).
   * Vous visez la conception avant que les briques de calcul ne s'appuient dessus (B-20).
   * Vous validez le type d'élément pour chaque brique paramétrée (B-42, B-43, B-47, B-48, B-49).
   * Vous validez le rapport de contrôle croisé (B-50).
   * Vous validez l'indice du livrable (B-60, B-71).
   * Vous validez le verdict global de l'auto-contrôle de synthèse (B-70).
   * Vous validez les points ouverts à la clôture (B-72).
________________


9. RENVOIS

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Index, principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | 106 variables | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des révisions | Versions du carnet | 10_ANNEXES/C_Journal_Revisions.md |
| Journal des modifications | Détail des modifications unitaires | 11_HISTORIQUE/Journal_des_modifications.md |

________________


10. RÉSUMÉ EN UNE PAGE
Un projet = 6 phases = 37 briques = 4 prompts transverse.
Ce que vous faites à chaque projet :
   1. Cadrage : B-00 à B-04 — 1 à 2 jours — inventaire, MPD, FDC, RDR, PTD.
   2. Analyse : B-10 à B-15 — 3 à 5 jours — audits, contradictions, périmètre, risques.
   3. Conception : B-20 à B-24 — 2 à 10 jours — conception GO, DDC, hypothèses.
   4. Calage et calculs : B-30 à B-50 — 10 à 30 jours — calage, preuves, vérifications, notes de calcul.
   5. Livrables : B-60, B-62, B-64 — 3 à 5 jours — plans, nomenclatures, notices.
   6. Clôture : B-70 à B-72 — 1 à 2 jours — auto-contrôle, indiçage, journal.
À tout moment : T-01 (sincérité), T-02 (recadrage), T-03 (méta-amélioration), T-04 (demande de complément).
Les trois règles qui gouvernent tout :
   1. Le mode doit être honnête — pas de COMPLET sur une donnée manquante.
   2. Les sources doivent être citées — tout élément est rattaché à une pièce.
   3. La mise à jour est incrémentale — seuls les livrables impactés sont régénérés.
________________


Additif v2.3 — Durées indicatives en voie rapide (document maître §6) : pour une affaire simple (un seul type de livrable, BET de conception présent, aucune contradiction bloquante), les phases 0 et 1 fusionnées en une seule passe représentent indicativement 1 à 3 jours, sans suppression d'aucune sortie ; les durées des phases 2 à 6 du tableau ci-dessus restent inchangées. Tout blocage fait repasser en voie normale.
---

### Additif v2.4 — Ce que les versions v2.x changent à l'usage quotidien
- **Verrou V13 et annexe O** : les briques géométriques et de calcul (phase 3, phase 4, B-60/B-62) travaillent par scripts exécutés et relus ; sans environnement d'exécution, elles ne peuvent pas être déclarées COMPLET.
- **Protocole B-32 §R** : avant tout nettoyage, les parois sont chaînées (R.3bis) puis classées PORTEUR CERTAIN / NON PORTEUR / À LEVER (critères C1 à C6) ; les porteurs BET vectoriels sont projetés (R.4bis). Votre arbitrage porte sur la liste À LEVER, à la porte B-32.
- **Seuils du projet** : GEO-09 = échelle tracé ; GEO-10/GEO-11 = reconnaissance des porteurs ; GEO-12 = seuils géométriques (calage, superposition, position). Ces quatre variables sont des données FDC : vérifiez-les en phase 0.
- **Voie rapide** : phases 0 et 1 fusionnables pour les affaires simples (voir l'additif v2.3 ci-dessus et le document maître §6).

### Additif — Application proportionnée et garde-fous d'usage
Le carnet est un menu, pas un programme obligatoire : le nombre de briques réellement activées est fixé par le PTD (B-04) selon l'affaire, jamais par défaut à 37.
- **Petite affaire** (un livrable, BET de conception présent, pas de contradiction bloquante) : voie rapide — phases 0 et 1 fusionnées, seules les briques du livrable visé sont activées.
- **Affaire moyenne** : phases 0 à 6 dans l'ordre, en n'activant que les briques de calcul et de livrables correspondant au périmètre GO réel.
- **Affaire lourde ou réhabilitation** : parcours complet, protocole B-32 §R et contrôles croisés inclus.
Restent **incompressibles à toute échelle** : le protocole de session (§0, portes et GO), le triptyque MPD/FDC/RDR, et pour tout livrable diffusé les verrous V7 (document propre, sans trace de génération), V11 (aucune invention, blocages déclarés) et V13 (preuve d'exécution des livrables géométriques et numériques). Le risque symétrique — n'appliquer que la partie « promesse » du carnet — se traite ici : avant de diffuser un livrable ou une version du carnet, l'assistant exécute et montre un contrôle anti-fragments (recherche des traces de génération en français et en anglais, lecture des jonctions entre documents) ; aucune mention « complet », « assaini » ou « vérifié » n'est écrite sans la sortie de ce contrôle. Le prompt T-01 (sincérité) peut être invoqué par l'utilisateur à tout moment pour l'exiger.

---

## ORDONNANCEMENT v3.0 — MODE D'EMPLOI EN 6 PHASES (remplace l'ordre v2.x)

> L'ordre historique du présent document (cadrage → analyse → conception → calage → calculs → livrables → clôture) est conservé ci-dessus comme archive de lecture. Il est **remplacé**, pour toute exécution à compter de la v3.0, par l'ordonnancement suivant, qui remonte le socle géométrique en phase 1.

### Phase 0 — Cadrage et qualification (B-00 à B-04)
1. `B-00` : inventaire des pièces, contradictions à chaud, mission reformulée, **qualification `CFG-01`** (aucun BET MOE / PDF MOE / vecteurs MOE / mission partielle) et inventaire vectoriel de chaque pièce.
2. `B-01` : MPD, **gabarit `CFG-02`** (`S` / `M` / `L-XL`) et **découpage `CFG-03`** (blocs, joints de dilatation, niveaux-types).
3. `B-02` : FDC, avec la table `NIV-07` (PB / PH / ASB / Fini / 0,00 relatif).
4. `B-03` : RDR à quatre registres (`D-xx`, `H-xx`, `PA-xx`, `V-xx`).
5. `B-04` : PTD, blocages locaux, briques contournables.

### Phase 1 — Socle géométrique et nettoyage (B-30 → B-32 → B-31)
1. `B-30` : calage multi-sources vers le Repère Structurel Unique, matrice `GEO-13`, résidus sur points témoins.
2. `B-32` : vue nettoyée différentielle, protocole CAO en quatre temps (annexe O §9), `0` cloison et `0` isolant.
3. `B-31` : preuve de superposition multi-étages et multi-sources, détection des porteurs non portés (`V15`).
**Aucune brique des phases 2 à 6 ne s'engage sur un fond non calé et non nettoyé.**

### Phase 2 — Audit croisé multi-pièces (B-10 à B-15)
Audits sur fond calé (`B-10`, `B-11`, `B-12`), contradictions et réconciliation quantitative (`B-13`), périmètre de lot (`B-14`), risques et **Pré-Audit Flash d'Exécutabilité** (`B-15`), avec preuve d'épuisement `V14` avant toute déclaration d'absence.

### Phase 3 — Conception et synthèse structurelle (B-20 → B-25 → B-21 → B-22 → B-23 → B-24)
Synthèse indissociable sur fond nettoyé (`B-20`), stabilité globale et contreventement (`B-25`), descente de charges (`B-21`), hypothèses `H-xx` (`B-22`), exploitation du diagnostic (`B-23`), existant non sondé et `PA-xx` (`B-24`).

### Phase 4 — Calculs d'exécution (B-40 à B-50)
Notes scriptées, hypothèses actives citées, prescriptions `ENC` et `PA-xx` reportées, flèches sous maçonnerie vérifiées, assemblages renvoyés à `B-50`.

### Phase 5 — Synthèse des réservations et livrables (B-34 → B-60 → B-62 → B-64)
Carnet de réservations (`B-34`), plans d'exécution purs (`B-60`), nomenclature extraite du DXF relu (`B-62`), notice de synthèse (`B-64`).

### Phase 6 — Vérification croisée et clôture (B-33 → B-70 → B-71 → B-72)
Vérification croisée globale (`B-33`), auto-contrôle de synthèse (`B-70`), indiçage (`B-71`), journal de clôture (`B-72`).

### Points de contrôle humain par phase
| Phase | Validation humaine obligatoire |
| --- | --- |
| 0 | Qualification `CFG-01`, gabarit `CFG-02`, MPD ligne à ligne, table `NIV-07` |
| 1 | Résidus de calage, périmètre de nettoyage, différentiel `EXISTANT / DÉMOLITION / PROJET` |
| 2 | Classement gravité × nature des contradictions, risques résiduels acceptés |
| 3 | Système de contreventement, hypothèses `H-xx` et leur délai, Points d'Arrêt `PA-xx` |
| 4 | Sections et ferraillages retenus, hypothèses actives citées |
| 5 | Indice des plans, carnet de réservations, titre véridique, `0` collision |
| 6 | Verdict global, supersession, points ouverts à la clôture |

**[Fin de 10_ANNEXES/D_Mode_Emploi.md]**

---

**[Début du fichier : 10_ANNEXES/O_Outillage.md]**

# Annexe O — COUCHE OUTILLAGE ET PROTOCOLE CAO (refondue en v3.0)
> Version du document : 3.0 (carnet CARNAC v3.0) — historique des modifications : 11_HISTORIQUE/Journal_des_modifications.md.

## 1. OBJET
Cette annexe définit l'environnement d'exécution et les protocoles qui rendent le verrou V13 applicable. Elle est fonctionnelle et neutre (V10) : elle décrit des capacités, pas des produits. Les exemples d'outils sont interchangeables : bibliothèque de lecture/écriture DXF (type ezdxf), bibliothèque d'extraction vectorielle PDF (type PyMuPDF), moteur de rendu (type matplotlib/CairoSVG), interpréteur de calcul (type Python).

Elle s'applique à toutes les briques en **régime outillé** : B-30, B-31, B-32, B-33, B-40 à B-50 (applications numériques), B-60, B-62.

## 2. ENVIRONNEMENT D'EXÉCUTION (variable OUT-01)
Avant toute brique outillée, l'environnement est déclaré et consigné :
- interpréteur et version majeure ;
- bibliothèques utilisées et leur rôle (lecture DXF, extraction PDF, calcul, rendu, écriture DXF) ;
- capacité d'écriture de fichiers persistants (les livrables et les scripts survivent à la session) ;
- capacité de relecture des fichiers produits.

Si l'environnement n'est pas disponible, la brique outillée ne peut pas être déclarée COMPLET : elle est suspendue (PTD) ou exécutée en PARAMÉTRIQUE documentaire (spécification du script à produire, sans livrable).

## 3. PROTOCOLE SCRIPT (variable OUT-02)
Chaque production outillée suit les cinq temps suivants, sans exception :

1. **Écriture du script.** Le modèle écrit un script complet, lisible, commenté, qui lit les fichiers sources réels (jamais des coordonnées recopiées de mémoire) et produit le livrable.
2. **Exécution.** Le script est exécuté. Toute erreur est diagnostiquée et le script corrigé ; on ne contourne pas une erreur en produisant le résultat « à la main ».
3. **Relecture réelle.** Le fichier produit (DXF, PDF, tableau) est rouvert par un second script ou une seconde passe qui énumère et compte : calques présents, nombre d'entités par calque, cotes lues, positions contrôlées. C'est ce comptage, et lui seul, qui vaut « test de relecture ». Toute mention du type « réouvre le fichier (simulé) » est une non-conformité V13.
4. **Contrôle visuel.** Un rendu du livrable (PNG) est produit et lu. Le contrôle visuel vérifie la plausibilité (pas d'élément dans le vide, pas d'appui manquant, pas de collision de textes) ; il ne remplace ni le comptage ni le calcul.
5. **Journalisation (OUT-03).** Le journal d'exécution est consigné avec le livrable : script (nom, version), fichiers d'entrée (nom, indice, taille), paramètres, comptages de relecture, écarts constatés et leur traitement.

Les scripts sont conservés dans le dossier du livrable et versionnés avec lui : un livrable sans son script n'est pas reproductible, donc pas clos.

## 4. RÈGLES D'EXTRACTION GÉOMÉTRIQUE
Ces règles codifient les échecs rencontrés en pratique ; elles sont impératives en phase 3 et 5.

1. **Vectoriel d'abord.** La géométrie provient des coordonnées vectorielles des fichiers (entités DXF, chemins PDF), jamais d'une image, d'une proportion d'écran ou d'une estimation visuelle.
2. **Rendu pleine page.** Tout rendu de contrôle d'un PDF est produit en pleine page à résolution fixe (300 dpi) puis découpé ; les rendus rognés à la volée introduisent des décalages d'échelle et sont interdits comme base de mesure.
3. **Unités vérifiées, pas déclarées.** L'unité réelle du fichier est vérifiée sur au moins deux cotes connues avant tout calcul de transformation. Une unité déclarée incohérente avec les cotes est signalée et traitée dans la transformation (B-30).
4. **Continuité ≠ identité.** Un segment continu n'est pas forcément un mur ; l'identification d'un élément (mur, limite de terrasse, joint) se fait par convergence d'indices (épaisseur, calque, cotes, annotations), jamais sur la seule géométrie. Pour les parois porteuses, cette convergence est formalisée par le protocole B-32 §R (critères C1 à C6, classes PORTEUR CERTAIN / NON PORTEUR / À LEVER).
5. **Distorsion connue.** Un fond PDF peut être localement distordu par rapport au DXF : le calage est alors local (par zone ou par niveau), avec résidus par zone, plutôt qu'une transformation globale forcée.
6. **Aucun élément sans appui.** Tout élément produit (profilé, poteau, semelle) est rattaché par le script à ses appuis identifiés dans la source ; le journal liste les éléments dont l'appui n'a pas été trouvé — ils ne sont pas dessinés.

## 5. PROTOCOLE CALCUL (briques B-40 à B-50)
1. Chaque application numérique d'une note de calcul est produite par le script de calcul versionné avec la note (OUT-02) ; la note cite le script et ses sorties.
2. Le script expose, pour chaque vérification : les données d'entrée (avec leur code FDC), la formule littérale, la référence normative, le résultat et le taux de travail.
3. Les contrôles de cohérence internes (unités, ordres de grandeur, cas limites) sont codés dans le script ; un résultat aberrant arrête la production, il n'est pas « corrigé » dans le texte de la note.
4. En cas de correction d'une hypothèse (B-22), le script est ré-exécuté intégralement ; les notes ne sont jamais rattrapées par des retouches numériques locales.

## 6. PROTOCOLE DXF
1. Écriture selon l'annexe A (calques normalisés, unités millimètres, aucun élément sur le calque 0, calques de travail supprimés à l'export).
2. Relecture systématique : ouverture du DXF produit, comptage des entités par calque, comparaison aux comptages attendus du script de production. Tout écart est un écart de production, signalé avant diffusion.
3. Le DXF livré et le PDF livré proviennent du même script et de la même exécution ; un DXF régénéré séparément est un nouveau livrable, re-vérifié.

## 7. JOURNAL D'EXÉCUTION (variable OUT-03) — FORMAT MINIMAL
| Champ | Contenu |
|---|---|
| Livrable | Code, indice, brique source, mode |
| Script | Nom, version, date d'exécution |
| Entrées | Fichiers lus (nom, indice, taille), variables FDC consommées |
| Paramètres | Transformation de calage, seuils GEO-12, hypothèses H-xx |
| Relecture | Comptages par calque, cotes contrôlées, résidus mesurés |
| Visuel | Rendu produit et lu (oui/non), anomalies relevées |
| Écarts | Écarts constatés, diagnostic, traitement (correction du script / réserve R-xx) |
| Verdict | Conforme / conforme avec réserves / à reprendre |

## 8. INTERDICTIONS DE LA COUCHE OUTILLAGE
- Interdit de déclarer un contrôle « fait » sans journal OUT-03.
- Interdit de produire un livrable graphique « à la main » dans la conversation (coordonnées inventées ou recopiées d'une image).
- Interdit de masquer une erreur d'exécution en reformulant le résultat attendu.
- Interdit de livrer un DXF dont la relecture comptée n'a pas été comparée aux attendus.
- Interdit de réutiliser un script d'un autre projet sans revalider ses entrées (fichiers, unités, calage).

---

## 9. PROTOCOLE CAO DE NETTOYAGE STRUCTUREL (nouveau en v3.0)

Le nettoyage d'un fond de plan n'est jamais une suppression « au feeling » : c'est une suite de quatre opérations contrôlées, scriptées et journalisées.

### 9.1 Étape 1 — Reconnaissance des blocs et reclassement (`INSERT` récursif)
1. Parcours récursif de toutes les références de blocs (`INSERT`), y compris imbriquées.
2. Pour chaque entité rencontrée, détermination du calque *effectif* (calque du bloc, calque de l'insertion, calque des entités internes) : le calque porteur est celui de l'entité interne, jamais celui de l'insertion.
3. Reclassement des entités porteuses sur le calque structurel normalisé (annexe A §2) **avant** toute purge : une purge réalisée avant reclassement détruit des porteurs.
4. Journal : nombre de blocs parcourus, profondeur maximale, entités reclassées par calque d'origine et de destination.

### 9.2 Étape 2 — Retrait du complexe isolant et des doublages
1. Identification des enveloppes de doublage par épaisseur, position relative au nu porteur et calque d'origine.
2. Suppression de l'enveloppe, conservation du **nu porteur** (le plan de structure cote le nu brut, jamais le nu fini).
3. Report systématique de la correspondance `nu brut ASB / nu fini` et `Plan Archi N / PB / PH` dans la table `NIV-07` (§9.5).
4. Journal : épaisseurs retirées par façade, nu conservé, écarts de niveau induits.

### 9.3 Étape 3 — Purge spatiale des portes, cotes et hachures orphelines
1. Détection des entités non porteuses : portes, fenêtres, mobilier, hachures de revêtement, cotes de second œuvre.
2. Filtrage par distance : une entité est conservée si elle est à moins de 22 cm d'un segment porteur **et** si sa fonction est mécanique (baie, percement, trémie) ; sinon elle est purgée.
3. Contrôle inverse obligatoire : aucune ouverture mécanique réelle ne doit disparaître. Le script compare le nombre d'ouvertures avant/après et exige l'égalité sur les baies et trémies déclarées.
4. Journal : entités purgées par catégorie, ouvertures conservées, écart éventuel justifié.

### 9.4 Étape 4 — Recalage multi-sources vers le Repère Structurel Unique (`RSU`)
1. Pour chaque source vectorielle secondaire (plan structure MOE en PDF vectoriel, DXF de diagnostic, relevé géomètre), extraction des tracés et des textes.
2. Appariement des points homologues avec la source de référence, puis calcul de la transformation (similarité : translation, rotation, échelle ; affinité seulement si anisotropie justifiée).
3. Mesure du résidu sur des points témoins **non utilisés** au calage, avec seuils de l'annexe A et du document maître §5.
4. Consignation dans la matrice `GEO-13` : source, indice, points appariés, transformation, résidu maximal, résidu acceptable, statut.
5. Journal : nombre de sources recalées, résidus, sources refusées et motif.

### 9.5 Table de correspondance des niveaux et des épaisseurs (`NIV-07`)
| Plan architecte | Plancher bas (PB) | Plancher haut (PH) | Nu brut ASB | Nu fini | Épaisseur de complexe |
| --- | --- | --- | --- | --- | --- |
| Niveau `N` | cote `PB_N` | cote `PH_N` | cote `ASB_N` | cote `FINI_N` | `FINI_N − ASB_N` |

Règle : aucune cote de niveau n'est reprise d'un plan architecte sans passer par cette table. Un écart non renseigné est un écart bloquant pour B-43 et B-60.

### 9.6 Contrôle de rendu et anti-collision de textes
1. Extraction de toutes les entités texte et de leurs boîtes englobantes réelles (après rotation).
2. Détection des chevauchements deux à deux ; seuil exigé : `0` chevauchement sur tout plan diffusé.
3. Détection des cotes orphelines (aucune entité cotée à moins de 22 cm) et des entités sur le calque `0`.
4. Détection des entités de second œuvre résiduelles sur les calques de structure.
5. Journal : nombre de textes contrôlés, collisions détectées, collisions corrigées, collisions résiduelles (doit être nulles).

**[Fin de 10_ANNEXES/O_Outillage.md]**

---

**[Début du fichier : 01_DICTIONNAIRE/CARNAC_v3.0_variables.md]**

Fichier 01_DICTIONNAIRE/CARNAC_v3.0_variables.md — CARNAC v3.0
________________


CARNAC — DICTIONNAIRE DES VARIABLES (v3.0)
1. NOTE DE COMPTE
Le dictionnaire v3.0 compte 106 variables : 94 variables reprises de la version précédente (aucune supprimée), dont deux libellés restaurés (LIV-01 « Conventions de calques DXF » et LIV-03 « Formats de sortie », corrompus en « B-61 » lors de la reconstruction antérieure), et 12 variables nouvelles (CFG-01 à CFG-03, DEC-05 à DEC-07, GEO-13, GEO-14, NIV-07, STR-01 à STR-03).

La colonne « Briques consommatrices » est reconstruite automatiquement, par développement des plages (SOL-01 à SOL-07, GEO-01 à GEO-05, LIV-01 à LIV-05, CHG-01 à CHG-03, etc.), à partir des tables « Variables consommées » des 39 fiches B-xx et des 4 prompts T-xx : elle est donc exacte par construction.

2. TABLE DES VARIABLES

| Code | Libellé | Briques consommatrices |
| --- | --- | --- |
| AC-01 | MOA | — (variable de référence) |
| AC-02 | Architecte | — (variable de référence) |
| AC-03 | BET structure de conception | B-20 |
| AC-06 | Bureau de contrôle | — (variable de référence) |
| CHG-01 | Usage des locaux par zone (catégories EC1) | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-02 | Surcharges d'exploitation par zone | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-03 | Poids propres des complexes de plancher | B-21, B-42, B-43, B-45, B-47, B-48, B-49 |
| CHG-04 | Poids propres de toiture | B-21, B-44 |
| CHG-05 | Neige | B-21, B-44 |
| CHG-06 | Vent | B-21, B-44, B-45 |
| CHG-07 | Sismique (si applicable) | B-42, B-46 |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | B-21, B-43, B-47, B-48 |
| DEC-01 | Mode attribué à chaque brique | B-70 |
| DEC-02 | Décisions inscrites au RDR (valeur déclarée, auteur, date) | B-03, B-64, B-70, B-72, T-03 |
| DEC-03 | Verrous ouverts (donnée, brique suspendue, responsable) | B-03, B-04, B-13, B-15, B-64, B-70, B-72, T-03, T-04 |
| DEC-04 | Documents supersédés (indice, date) | B-71, B-72 |
| DOC-01 | Inventaire des pièces (fichier, folio, indice, échelle) | B-00, B-01 |
| DOC-02 | Plans architecte vectoriels | B-20, B-30, B-31, B-32, B-33, B-60 |
| DOC-03 | Plans BET structure (si disponibles) | B-10, B-11, B-20 |
| DOC-04 | CCTP / pièces contractuelles | B-10, B-14 |
| DOC-05 | Diagnostic structure de l'existant | B-11, B-23, B-24 |
| DOC-06 | Rapport géotechnique | B-12, B-41 |
| DOC-07 | Diagnostic amiante/plomb (cité en exemple v1.1, défini en v2.0) | — (variable de référence) |
| DOC-08 | Plans de récolement / DOE | B-11 |
| DOC-09 | Fiches techniques des prédalles | B-48, B-50 |
| EXI-01 | Sections des éléments existants | B-20, B-23, B-24, B-44, B-46, B-49 |
| EXI-02 | Pathologies relevées | B-23 |
| EXI-03 | Résistance des matériaux existants | B-20, B-24, B-44, B-46, B-49 |
| EXI-04 | Résultats de sondages destructifs ou semi-destructifs | B-24, B-41 |
| EXI-05 | Contrainte admissible transmise à l'existant | B-23, B-46 |
| GEO-01 | Emprise / contour du bâtiment | B-20, B-21, B-23, B-33, B-40, B-43, B-44, B-47, B-48, B-60 |
| GEO-02 | Axes et trames | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 |
| GEO-03 | Épaisseurs murs | B-20, B-21, B-23, B-33, B-40, B-46, B-49, B-60 |
| GEO-04 | Positions poteaux | B-20, B-21, B-23, B-33, B-40, B-42, B-45, B-60 |
| GEO-05 | Baies et ouvertures | B-20, B-23, B-33, B-40, B-42, B-46, B-47, B-49, B-60 |
| GEO-06 | Unités du fichier source (cm/m/mm) | B-30, B-32 |
| GEO-07 | Transformation du fichier (rotation, translation, échelle) | B-30, B-31 |
| GEO-08 | Points de calage identifiés (≥ 3 non alignés) | B-30, B-31 |
| GEO-09 | Échelle tracé | — (variable de référence) |
| ID-01 | Code projet | B-00, B-01, B-02, B-03, B-04, B-10, B-11, B-12, B-13, B-14, B-15, B-20, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-34, B-40, B-41, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-50, B-60, B-62, B-64, B-70, B-71, B-72, T-01, T-02, T-03, T-04 |
| ID-02 | Intitulé de l'opération | B-00, B-10, B-11, B-12, B-13, B-14, B-15, B-20, B-21, B-22, B-23, B-24, B-25, B-30, B-31, B-32, B-33, B-34, B-40, B-41, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49, B-50, B-60, B-62, B-64, B-70, B-71, B-72, T-01, T-02, T-03, T-04 |
| ID-03 | Adresse | — (variable de référence) |
| ID-04 | Nature | — (variable de référence) |
| ID-05 | Indice du dossier en vigueur | B-03, B-64, B-71, B-72 |
| ID-06 | Phase | — (variable de référence) |
| ID-07 | Date de l'étude | B-03 |
| LIV-01 | Conventions de calques DXF (préfixes, suffixes, règles d'usage) | B-60 |
| LIV-02 | Échelles autorisées | B-60 |
| LIV-03 | Formats de sortie (DXF, PDF, PNG) et nommage des fichiers | B-60 |
| LIV-04 | Cartouche | B-60 |
| LIV-05 | Langue et unités | B-60 |
| MAT-01 | Classe de résistance du béton | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 |
| MAT-02 | Classe d'exposition | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 |
| MAT-03 | Enrobage nominal | B-40, B-42, B-43, B-47, B-48, B-49, B-50, B-62 |
| MAT-04 | Nuance d'acier BA | B-40, B-42, B-43, B-46, B-47, B-48, B-49, B-50, B-62 |
| MAT-05 | Nuance d'acier de charpente métallique | B-45, B-49, B-50, B-62 |
| MAT-06 | Classe de bois | B-43, B-44, B-50, B-62 |
| MAT-07 | Nature et résistance de la maçonnerie existante | B-46, B-49, B-50 |
| MAT-08 | Classe de service et durée de charge | B-43, B-44 |
| MAT-09 | Classe de bloc de maçonnerie neuve (NF EN 771-3) | B-46, B-50, B-62 |
| MAT-10 | Classe de mortier (M2,5 à M10) | B-46, B-50, B-62 |
| MAT-11 | Type de maçonnerie (chaînée / armée / non armée) | B-46, B-50, B-62 |
| MAT-12 | Présence et nature des chaînages existants | B-46 |
| NIV-01 | Niveau TN | B-40 |
| NIV-02 | Niveaux planchers | B-42, B-43, B-47, B-48, B-60 |
| NIV-03 | Hauteurs libres | B-42, B-47 |
| NIV-04 | Niveau assise | B-40 |
| NIV-05 | Niveau fini dallage | B-43, B-60 |
| NIV-06 | Épaisseurs plancher | B-43, B-48 |
| OUT-01 | Environnement d'exécution (interpréteur, bibliothèques, persistance) | — (variable de référence) |
| OUT-02 | Script de production ou de calcul versionné avec le livrable | — (variable de référence) |
| OUT-03 | Journal d'exécution et de relecture (comptages, résidus, écarts) | — (variable de référence) |
| OUT-04 | Rendu de contrôle visuel lu (PNG pleine page 300 dpi) | — (variable de référence) |
| SEC-01 | Degré coupe-feu exigé par élément | B-25, B-42, B-43, B-47, B-48, B-49 |
| SEC-02 | Catégorie ERP | — (variable de référence) |
| SEC-03 | Classement termites de la commune | B-43 |
| SEC-04 | Classe structurale | — (variable de référence) |
| SEC-05 | PMR | — (variable de référence) |
| SIT-01 | Site occupé | — (variable de référence) |
| SIT-02 | Contraintes de site (cité en exemple v1.1, défini en v2.0) | — (variable de référence) |
| SIT-03 | Accès | — (variable de référence) |
| SIT-04 | Voisinage | B-40 |
| SIT-05 | Emprise fouille | B-40 |
| SOL-01 | Contrainte admissible ELS | B-12, B-20, B-40, B-41, B-43 |
| SOL-02 | Contrainte admissible ELU | B-20, B-40, B-41 |
| SOL-03 | Profondeur de bon sol / ancrage minimal | B-20, B-40, B-41 |
| SOL-04 | Nature et succession des couches | B-20, B-41 |
| SOL-05 | Classe d'agressivité du sol (XA) | B-20, B-40, B-41, B-43 |
| SOL-06 | Nappe, hydrologie, drainage | B-40, B-41 |
| SOL-07 | Tassements admissibles / différentiels | B-40, B-41 |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | B-12, B-41 |
| GEO-10 | Seuils d'épaisseur de présomption porteuse (seuil bas / seuil haut, par système constructif) | B-32 |
| GEO-11 | Superposition des niveaux : recouvrement minimal et écart maximal d'axe entre niveaux | B-32 |
| GEO-12 | Seuils géométriques du projet (résidu de calage, écarts de superposition et de position) | B-30 |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | B-00, B-01, B-20, B-60 |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | B-01, B-04, B-25, B-34, B-60 |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | B-01, B-20, B-21, B-25, B-30, B-60 |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | B-03, B-20, B-22, B-25, B-34, B-40, B-60, B-64, B-70 |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | B-03, B-22, B-60, B-64 |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | B-03, B-24, B-34, B-40, B-41, B-44, B-46, B-60, B-64 |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | B-13, B-20, B-30, B-31, B-32, B-34 |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | B-11, B-13, B-20, B-31, B-32, B-33 |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | B-02, B-20, B-30, B-32, B-43, B-60 |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | B-20, B-21, B-25, B-42, B-44, B-45, B-46 |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | B-12, B-25, B-40, B-41, B-42, B-43 |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | B-32, B-34, B-42, B-43, B-48, B-60 |

**[Fin de 01_DICTIONNAIRE/CARNAC_v3.0_variables.md]**

<!-- FIN DU PACK — CARNAC v3.0 -->
