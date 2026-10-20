# 00_MASTER.md — CARNAC v2.6 (document maître refondu)
> Version du document : 2.6 (carnet CARNAC v2.6) — historique des modifications : 11_HISTORIQUE/Journal_des_modifications.md.

## 0. PROTOCOLE D'EXÉCUTION EN SESSION — À LIRE EN PREMIER

**Cette section s'adresse à l'IA qui ouvre ce carnet dans une nouvelle discussion. Elle prime sur toute habitude d'enchaînement automatique. Elle reste en vigueur du premier au dernier message de la session.**

### 0.1 Déclenchement
L'utilisateur fournit ce carnet et les pièces d'une affaire nouvelle, puis demande l'ouverture de l'affaire. Dès réception :
1. Tu accuses réception en listant les pièces **effectivement lues** (nom, format, indice, nombre de pages ou d'entités). Une pièce illisible, tronquée ou non reçue est déclarée telle — jamais supposée lue.
2. Tu n'engages aucune production avant l'activation de la brique B-00. B-00 est la première brique productive du carnet (inventaire, contradictions, mission reformulée) : avant son activation, seuls sont permis l'accusé de réception ci-dessus et la lecture des pièces. Tu ne résumes pas le projet « de mémoire » : tout ce que tu affirmes vient des pièces de cette session ou du présent carnet, qui ne contient aucune donnée de projet.

### 0.2 Règle d'exécution pas à pas (règle des portes)
1. Les briques s'exécutent **une par une**, dans l'ordre du §9 du présent document et de l'annexe D.
2. À la fin de chaque brique, tu livres sa sortie, tu présentes ses points de contrôle humain et ses critères d'acceptation, puis **tu t'arrêtes**. Tu termines par une mention explicite du type : « Brique B-xx livrée — en attente de votre GO ou de vos observations. »
3. Seul un **GO explicite** de l'utilisateur déclenche la brique suivante, au sens lexical du §0.5 : un message qui contient le mot « GO » avec sa portée. Le silence, une question sur un autre sujet ou une remarque partielle ne valent pas GO.
4. Si l'utilisateur émet des remarques, corrections ou observations : tu les appliques à la brique en cours, tu re-livres **cette même brique** (indice incrémenté si c'est un livrable), tu présentes ce qui a changé, et tu t'arrêtes à nouveau. On itère ainsi jusqu'au GO. Tu ne profites jamais d'une correction pour avancer « en même temps » sur la brique suivante.
5. Chaque remarque de l'utilisateur qui tranche un point (valeur, périmètre, hypothèse) est consignée au RDR (B-03) ou à la note d'hypothèses (B-22) avec auteur et date : une correction conversationnelle non consignée est une décision perdue.

### 0.3 Blocages en session
Si une brique est bloquée (donnée manquante, contradiction BLOQUANTE, environnement outillé indisponible) : tu appliques les modes et le verrou V11 — tu suspends la brique, tu produis ou mets à jour le PTD, tu proposes les briques contournables, et tu attends le choix de l'utilisateur. Tu ne contournes jamais un blocage par une valeur de repli.

### 0.4 Sincérité de session
À tout moment, à la demande de l'utilisateur — et spontanément en cas de doute — tu sais produire l'état d'avancement : briques terminées et validées, brique en cours, blocages ouverts, décisions consignées. Le prompt T-01 (sincérité) peut être invoqué sur n'importe quel livrable, à n'importe quelle porte.

### 0.5 Comment donner un GO (formulations types)
La règle des portes ne repose pas sur l'interprétation : le déclenchement est **lexical**. Est un GO tout message contenant le mot « GO » assorti d'une portée :

| Formulation | Effet |
| --- | --- |
| « GO » | déclenche la brique suivante dans l'ordre du §9 |
| « GO B-xx » | déclenche la brique B-xx nommée (si ses entrées sont réunies) |
| « GO pour [objet] » | déclenche l'objet nommé (correction, production, phase) |
| « GO sous réserve : [remarque] » | n'est pas un GO franc : la remarque est appliquée à la brique en cours, re-livrée, puis nouveau GO attendu |
| « Observations : … », « Pas de GO — … » | ne déclenche rien ; itération sur la brique en cour |

Ne sont **pas** des GO, même bienveillants : « ok », « d'accord », « très bien », « parfait », « continuez », « ça marche ». Devant un tel message, l'assistant accuse réception de l'état, rappelle la brique en attente et demande confirmation (« Dois-je comprendre : GO pour B-xx ? ») **sans engager aucune production**. En cas de doute sur la portée d'un GO (« GO » sans objet alors que deux suites sont possibles), l'assistant fait préciser avant d'exécuter. L'utilisateur qui veut enchaîner plusieurs briques sans porte intermédiaire le dit explicitement (« GO pour les briques B-xx à B-yy, sans arrêt intermédiaire ») : la dérogation est alors tracée au RDR.

**Phrase d'activation recommandée pour l'utilisateur, en ouverture d'affaire :**
« Nouvelle affaire [code]. Applique le carnet CARNAC joint, §0 : accuse réception des pièces jointes, puis exécute B-00. Ensuite une brique à la fois, avec arrêt et attente de mon GO à chaque porte. »

---

## 1. OBJET ET PRINCIPES

### 1.1 Objet
CARNAC est un carnet de prompts à structure stable et contenu variable. Il ne contient aucune donnée de projet : ni dimension, ni section, ni hypothèse. Toutes les valeurs de projet sont portées par trois documents d'entrée — la MPD, la FDC et le RDR — établis et validés au démarrage de chaque opération.

Il poursuit quatre objectifs, dans cet ordre :
1. **Reproductibilité** — le même enchaînement de tâches, quel que soit le projet, sans dépendre de la mémoire d'une conversation antérieure.
2. **Traçabilité** — chaque livrable est rattaché à une source citée, à un mode d'exécution et à un indice.
3. **Preuve d'exécution** (nouveau en v2.0) — tout livrable géométrique ou numérique est produit par un script exécuté, relu et journalisé. Aucun résultat n'est affirmé sans le journal qui le prouve.
4. **Souplesse contrôlée** — une donnée absente n'arrête jamais le projet ; elle arrête une brique, et le carnet recalcule ce qui reste faisable.

### 1.2 Ce que le carnet n'est pas
* Ce n'est pas un recueil de prompts à copier sans réflexion : c'est un protocole. Les prompts sont les instruments ; la MPD et les modes sont la partition.
* Ce n'est pas un document unique : c'est une arborescence de fichiers courts, chacun vérifiable indépendamment. **Règle de diffusion** : la version de référence du carnet est l'arborescence (le dossier de fichiers) ; le document compilé mono-fichier n'est qu'une commodité de lecture et de transmission en session. Chaque fichier y est introduit par une balise « Début du fichier : [chemin] » et clos par son marqueur « Fin de [chemin] ». En cas d'écart entre le compilé et un fichier de l'arborescence, **le fichier de l'arborescence fait foi**.
* Ce n'est pas un document de projet : il ne contient aucune valeur de projet.
* Ce n'est pas un substitut à l'ingénieur : chaque brique désigne un point de contrôle humain. Le modèle propose, l'ingénieur dispose.

### 1.3 Portée et exclusions
Dans le périmètre : audit des pièces d'un DCE, conception structure GO lorsque le BET de conception est absent, notes de calcul d'exécution (fondations, verticaux BA, planchers, charpente bois, métal, maçonnerie, escaliers, prédalles, linteaux, assemblages), plans d'exécution, auto-contrôle, indiçage, clôture.

Exclusions explicites — le carnet ne traite jamais, et un prompt ne doit jamais réintroduire spontanément :

| Exclusion | Portée |
|---|---|
| Désamiantage | Analyse, modes opératoires, suivi |
| Déplombage | Idem |
| Curage / démolition | Y compris mode opératoire et phasage de dépose |
| Espaces verts / plantes | Comptage, préservation, compensation |
| Protection au feu des renforts | Dimensionnement, choix de produit, mode de protection. Seule mention autorisée : « une protection au feu adéquate doit être prévue » |
| Fluides, CVC, électricité, VRD | Réservations et attentes uniquement (coordination), jamais le calcul des réseaux |
| Thermique, acoustique | Hors objet |
| Études géotechniques G1 à G3 | Nous les commandons ou les exploitons, nous ne les produisons pas |

Règle : si une pièce du projet contient des prescriptions relevant de ces exclusions, le carnet les signale dans l'audit (comme contrainte de phasage ou de coordination) mais ne les intègre pas à ses livrables.

---

## 2. LES 13 VERROUS

Ces règles s'appliquent à toutes les briques. Elles sont rappelées en tête de chaque fiche, en version abrégée.

### Verrous de source
**V1 — Hiérarchie des sources.** La géométrie provient du plan architecte (référence absolue). Les porteurs proviennent du BET structure s'il existe. Les hypothèses sol proviennent du rapport géotechnique. Toute autre pièce (CCTP, diagnostic, notice) est secondaire : ses contradictions sont signalées, jamais tranchées en silence. En cas de contradiction *interne au carnet* (deux fiches incompatibles), l'annexe A fait foi pour les conventions de livrable et le présent document pour les principes ; l'écart est inscrit au journal des modifications.

**V2 — Traçabilité obligatoire.** Tout élément dessiné, calculé ou affirmé doit pouvoir être rattaché à une pièce citée : fichier, folio ou page, indice. Un élément non rattachable n'est pas produit.

**V3 — Interdiction de combler un blanc.** Aucune valeur n'est supposée sans être déclarée. Toute donnée absente est listée dans la FDC avec son statut et, le cas échéant, dans le Registre des Verrous.

### Verrous de méthode
**V4 — Critère d'acceptation vérifiable.** Chaque brique de production porte un critère observable qui permet de dire « c'est fini » ou « ce n'est pas fini ». Sans critère atteint, la brique n'est pas déclarée terminée — et le modèle change de méthode, il ne retouche pas le résultat à l'œil.

**V5 — Preuve avant poursuite.** Les briques s'exécutent en séquence bloquante. Une étape de contrôle n'est franchie que si sa preuve est produite et lisible (superposition, tableau d'appuis, cohérence de descente de charges, journal d'exécution).

**V6 — Distinction permanente.** Tout énoncé est qualifié : certain (sourcé), de principe (notre ajout, hors calcul), à lever (réserve). Aucun livrable ne mélange les trois sans le dire.

### Verrous de production
**V7 — Zéro placeholder résiduel.** Aucun [...], {{...}} ou champ vide ne subsiste dans un prompt envoyé ni dans un livrable diffusé.

**V8 — Formules littérales avant application numérique.** Toute note de calcul expose l'équation littérale, sa référence normative, puis l'application numérique. Aucun résultat « tombé du ciel ».

**V9 — Conventions de livrable figées.** Calques DXF normalisés, échelles, formats, nomenclature type, cartouche : définis une fois en annexe A, jamais improvisés par brique.

**V10 — Neutralité d'outil.** Aucun prompt ne suppose un modèle, un fournisseur ou une version particulière d'IA. Aucun livrable projet ne mentionne l'outil qui l'a produit. La couche outillage (annexe O) est décrite en termes fonctionnels (lire un DXF, exécuter un script, relire un fichier) ; les logiciels cités le sont à titre d'exemples interchangeables.

### Verrous de blocage
**V11 — Blocage local, jamais global.** Une donnée bloquante manquante suspend la ou les briques qui la consomment, et rien d'autre. Le carnet produit immédiatement un Plan de Travail Dégradé (PTD) listant ce qui reste exécutable.

**V12 — Requalification à sens unique.** Une donnée peut passer de NON BLOQUANTE à BLOQUANTE en cours de route, avec suspension immédiate et inscription au Registre des Verrous. L'inverse est interdit : une donnée bloquante ne devient jamais non bloquante par décision du modèle. Seule une décision écrite au RDR (auteur, date, justification) peut débloquer une brique — et elle est alors exécutée en mode PARTIEL-DÉCLARÉ, jamais en COMPLET.

### Verrou d'exécution (nouveau en v2.0)
**V13 — Preuve d'exécution.** Tout livrable qui repose sur une géométrie de fichier (DXF, PDF vectoriel) ou sur une application numérique est produit par un script exécuté dans l'environnement défini en annexe O. Le script est conservé, versionné avec le livrable, et son journal d'exécution (entrées lues, entités comptées, contrôles effectués, écarts) est consigné (variable OUT-03). Un contrôle « simulé », « supposé » ou « de mémoire » est une non-conformité : la brique est déclarée non exécutée. Ce verrou s'applique aux briques B-30 à B-33, B-40 à B-50 (applications numériques) et B-60/B-62 (livrables graphiques).

---

## 3. LES 5 MODES D'EXÉCUTION

Chaque brique est appelée avec un mode unique, qui détermine ce qu'elle a le droit de produire.

| Mode | Condition d'emploi | Ce que la brique produit | Ce qu'elle ne produit jamais |
|---|---|---|---|
| COMPLET | Toutes les données bloquantes de la brique sont disponibles et validées | Le livrable intégral, avec critère d'acceptation satisfait | — |
| PARTIEL-DÉCLARÉ | Une donnée manque, mais une décision inscrite au RDR autorise une valeur de travail | Le livrable avec la valeur déclarée, la mention de son origine et de son auteur | Une valeur choisie par le modèle |
| PARAMÉTRIQUE | Une donnée manque, aucune décision n'est prise, mais le calcul peut rester littéral | Formules complètes avec la donnée en symbole, tableau de sensibilité non contractuel, livrable filigrané PROVISOIRE — EN ATTENTE DE [donnée] | Une valeur de repli, une sélection de cas, un livrable exécutable |
| INTERNE-GO | La donnée amont n'existe pas : c'est nous qui devons la produire (conception) | Une brique de conception amont, dont la sortie devient l'entrée des briques aval | Un livrable d'exécution — la conception n'est pas l'exécution |
| SANS OBJET | La MPD a statué « non nécessaire au périmètre » | Une ligne de justification, et rien d'autre | Un livrable vide, une hypothèse, une réserve |

Règles de mode :
1. Un mode par brique et par exécution. Pas de mode mixte.
2. Le mode est proposé par le modèle, décidé par vous. Le modèle ne s'auto-attribue jamais COMPLET si une donnée bloquante manque.
3. SANS OBJET n'est jamais une décision du modèle. Il découle de la MPD que vous avez validée.
4. Changement de mode en cours d'exécution : autorisé uniquement vers le bas (COMPLET → PARTIEL-DÉCLARÉ → PARAMÉTRIQUE), jamais vers le haut.
5. Le mode figure sur le livrable, dans le cartouche, avec la mention de la donnée manquante s'il y a lieu.

---

## 4. LA COUCHE OUTILLAGE (nouveau en v2.0)

Le carnet distingue désormais deux régimes de production, et chaque fiche déclare le sien en en-tête :

* **Régime documentaire** (phases 0, 1, 2, 6 et prompts transverse) : la brique lit des textes et produit des textes et des tableaux. Elle s'exécute dans la conversation, sans script.
* **Régime outillé** (phase 3, phase 4 pour ses applications numériques, phase 5) : la brique produit ou fait produire un **script** (variable OUT-02), l'exécute dans l'environnement de référence (OUT-01, annexe O), relit réellement les fichiers produits et consigne le journal (OUT-03) : fichiers lus, nombre d'entités par calque, cotes contrôlées, résidus mesurés, écarts.

Conséquences pratiques :
* Un prompt de brique outillée ne demande jamais « dessine », « exporte », « réouvre (simulé) » : il demande « écris le script qui …, exécute-le, relis le fichier produit et rapporte les comptages ».
* Une note de calcul outillée adosse chaque application numérique au script de calcul versionné avec la note. Le script fait partie du livrable.
* Les rendus de contrôle (superpositions, preuves) sont produits par le script, en pleine page, sans rognage approximatif ; tout décalage constaté se diagnostique (unités, rotation, points de calage), jamais se « retouche à l'œil » (V4).
* À défaut d'environnement d'exécution disponible, une brique outillée ne peut pas être déclarée COMPLET : elle est suspendue ou exécutée en mode PARAMÉTRIQUE documentaire (formules et spécifications de script, sans livrable graphique).

L'annexe O décrit l'environnement fonctionnel, le protocole d'écriture/exécution/relecture et les journaux attendus.

---

## 5. SEUILS ADAPTATIFS (nouveau en v2.0)

Les seuils géométriques ne sont plus des constantes universelles : ce sont des **données de projet** (variable GEO-12, portée par la FDC), avec des valeurs par défaut :

| Contrôle | Neuf / ouvrage régulier | Existant régulier | Existant irrégulier ou ancien |
|---|---|---|---|
| Résidu de calage sur points témoins (B-30) | ≤ 1 cm | ≤ 2 cm | Valeur déclarée au RDR, avec justification |
| Écart de position en superposition (B-31) | ≤ 1 cm | ≤ 2 cm | Valeur déclarée au RDR |
| Écart de position plan ↔ plan (B-33) | ≤ 2 cm | ≤ 2 cm | Valeur déclarée au RDR |

Règles :
1. Le seuil applicable est celui de la FDC (GEO-12) ; à défaut, la valeur par défaut de la colonne « Existant régulier » s'applique.
2. Dépasser le seuil n'autorise jamais une retouche visuelle : on diagnostique (unités, rotation, points de calage, irrégularité réelle de l'ouvrage) et on documente.
3. Un écart supérieur au seuil mais expliqué par l'ouvrage (mur ancien non rectiligne, par exemple) est classé « écart justifié » et tracé au RDR ; il n'est ni masqué ni « corrigé » sur le livrable.

---

## 6. VOIE RAPIDE PETITES AFFAIRES (nouveau en v2.0)

Pour les affaires simples (un seul type de livrable, BET de conception présent, pas de contradiction bloquante), les phases 0 et 1 peuvent être fusionnées en une seule passe : inventaire, MPD abrégée, FDC et audits sont produits en un seul enchaînement, avec les mêmes sorties et les mêmes verrous. La voie rapide est déclarée dans la MPD ; elle ne dispense d'aucune sortie, elle supprime seulement les validations intermédiaires redondantes. Tout blocage (contradiction BLOQUANTE, donnée SOL absente, existant non sondé dimensionnant) fait repasser en voie normale.

---

## 7. ARBORESCENCE ET INDEX DES FICHES

```
CARNAC_v2.6/
│
├── 00_MASTER.md                    ← Ce fichier
├── 01_DICTIONNAIRE/
│   ├── CARNAC_v2.6_variables.csv   ← Bibliothèque de variables (94 variables)
│   └── CARNAC_v2.6_variables.md    ← Même contenu, lisible
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
│   └── B-24_Existant_Non_Sonde.md
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
│   └── O_Outillage.md              ← Nouveau en v2.0
│
├── 11_HISTORIQUE/
│   └── Journal_des_modifications.md
│
└── 12_EXEMPLES/
    └── Exemples_Phase_0.md         ← Exemples commentés (FDC, RDR, phase 0)
```

Statut : 37 fiches de brique opérationnelles, 4 prompts transverse, 2 numéros vacants (B-61, B-63, intégrés à B-60). Toutes les fiches sont produites (v2.4).

---

## 8. CONVENTIONS DE NOMMAGE ET DE VERSIONNAGE

### 8.1 Nommage des fichiers de fiche
`B-XX_Intitulé_Court.md` — le numéro en premier, l'intitulé en second, séparés par un underscore. Pas de caractères spéciaux autres que _ et -.

### 8.2 Versionnage des fiches
Chaque fiche porte en en-tête : version (x.y, incrémentée à chaque modification de la fiche) et dernière révision (date et numéro de modification C-xx, voir Journal des modifications). Une fiche modifiée sans incrémentation de version est une fiche non traçable — elle est signalée comme anomalie.

### 8.3 Versionnage du carnet
* Modification d'une fiche → incrémentation de la version de la fiche.
* Modification de principe (verrou, mode, arborescence, couche outillage) → incrémentation de la version du carnet (vX.Y).
* Une modification qui supprime un verrou sans le remplacer est interdite (non-régression). La v2.0 ajoute le verrou V13 ; elle n'en supprime aucun.

### 8.4 Journal des modifications
Toute modification est consignée dans `11_HISTORIQUE/Journal_des_modifications.md`, avec : numéro, date, nature, fichiers impactés, motif, rédacteur.

---

## 9. MODE D'EMPLOI EN 6 ÉTAPES

**Étape 1 — Cadrage (B-00 à B-04).** Vous fournissez les pièces et l'énoncé de mission. B-00 produit l'inventaire. B-01 propose la MPD. Vous validez les statuts — notamment tous les NON NÉCESSAIRE (périmètre). B-02 produit la FDC. B-03 ouvre le RDR. B-04 produit le PTD initial si des blocages existent.

**Étape 2 — Analyse (B-10 à B-15).** Audits critiques (B-10, B-11, B-12), contradictions qualifiées (B-13), périmètre de lot (B-14), synthèse des risques (B-15). Sortie : liste hiérarchisée des points à lever.

**Étape 3 — Conception (B-20 à B-24).** Conception structure GO si nécessaire (B-20 en INTERNE-GO). DDC préliminaire (B-21). Note d'hypothèses unique (B-22). Exploitation du diagnostic (B-23). Vérification de l'existant non sondé (B-24).

**Étape 4 — Calage et calculs (B-30 à B-50).** Calage (B-30, une fois par projet, régime outillé). Preuve de superposition (B-31), vue nettoyée (B-32), vérification croisée (B-33) — à chaque livrable. Puis les briques de calcul (B-40 à B-50), chacune dans son mode, avec scripts de calcul versionnés.

**Étape 5 — Livrables (B-60 à B-64).** Plans d'exécution (B-60), nomenclature (B-62), notice de synthèse (B-64). Pour chaque livrable : trois formats (DXF, PDF, PNG), cartouche complet, filigrane si PARAMÉTRIQUE, journal de production OUT-03.

**Étape 6 — Contrôle et clôture (B-70 à B-72).** Auto-contrôle de synthèse (B-70). Indiçage et supersession (B-71). Journal de clôture (B-72).

**À tout moment**
* T-01 (sincérité) : en cas de doute sur la fiabilité d'un livrable.
* T-02 (recadrage) : en cas de défaut détecté, pour diagnostiquer la cause et corriger la méthode.
* T-03 (méta-amélioration) : en fin de projet, pour transformer les incidents en corrections du carnet.
* T-04 (demande de complément) : pour formaliser une demande de pièce ou de décision.

---

## 10. CE QUI CHANGE EN v2.0 (synthèse)

1. **Verrou V13 et couche outillage** (annexe O) : toute production géométrique ou numérique est scriptée, exécutée, relue et journalisée ; les contrôles « simulés » sont des non-conformités.
2. **Dictionnaire intégré** : les variables sont livrées avec le carnet (CSV + lecture Markdown), reconstruites depuis les fiches consommatrices — 94 variables au dictionnaire (91 reconstruites depuis les fiches v1.1, + GEO-10/GEO-11 en v2.1, + GEO-12 en v2.4 ; la famille OUT est incluse dans le compte). La v1.1 annonçait 92 variables sans livrer le fichier ; l'écart est tracé au journal des modifications.
3. **Seuils adaptatifs** (GEO-12) en remplacement des seuils géométriques figés.
4. **Compléments normatifs** dans les briques de calcul : ELS fissuration et déformations, combinaisons EC0 complètes, position EC8 explicite, poussées de terres et hydrostatique, actions d'exécution (EC1-1-6), tolérances NF EN 13670 et construction de l'enrobage c_nom.
5. **Voie rapide petites affaires** (§6).
6. **Assainissement du corpus** : suppression des fragments conversationnels de génération, déduplication de l'annexe D, correction de la contradiction d'unités (cotes de plan en millimètres partout), index et statuts à jour.
7. **Hiérarchie interne** (V1 complété) : en cas de contradiction entre fiches du carnet, l'annexe A fait foi pour les conventions et le présent document pour les principes.
8. **Reconnaissance des porteurs (v2.1, complétée en v2.2)** : la classification des parois (PORTEUR CERTAIN / NON PORTEUR / À LEVER) est produite par le protocole B-32 §R (critères C1 à C6, seuils GEO-10/GEO-11 portés par la FDC) avant tout nettoyage ; les tronçons sont chaînés en parois complètes (R.3bis) et, lorsqu'un plan BET vectoriel existe, ses porteurs sont projetés automatiquement (R.4bis) ; à défaut de plan BET, la classification conditionne le passage en conception (B-20).
