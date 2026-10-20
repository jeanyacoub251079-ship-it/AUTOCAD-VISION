<!-- PACK CARNAC v3.0 — PACK 01 — PHASE 0 : CADRAGE (B-00 à B-04) -->

# PACK 01 — PHASE 0 : CADRAGE (B-00 à B-04)

**Quand coller ce pack** : Après le socle, au démarrage de l'affaire.

**Ce qu'il contient** : B-00 inventaire et qualification `CFG-01` · B-01 MPD, gabarit `CFG-02`, découpage `CFG-03` · B-02 FDC et table `NIV-07` · B-03 RDR à quatre registres · B-04 PTD.

**Note d'usage** : À la sortie de ce pack, vous devez avoir validé : la configuration MOE, le gabarit, la MPD ligne à ligne et la table des niveaux.

**Prérequis** : le pack `00_SOCLE.md` doit être collé avant celui-ci, dans la même discussion.

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
**[Début du fichier : 02_PHASE_0_CADRAGE/B-00_Inventaire.md]**

Fichier 02_PHASE_0_CADRAGE/B-00_Inventaire.md — CARNAC v3.0
________________


B-00 — INVENTAIRE DES PIÈCES ET ÉNONCÉ DE MISSION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 0 — Cadrage et qualification |
| Brique précédente | Aucune (première brique du carnet) |
| Brique suivante | B-01 (Proposition de MPD) |
| Modes d'appel | COMPLET (mode normal) · PARTIEL-DÉCLARÉ (si une pièce est illisible : on la cite sans la commenter) |
| Entrées lues | Toutes les pièces fournies par le client (DOC-01), l'énoncé de mission du client |
| Sortie unique | Inventaire structuré + liste des contradictions + énoncé de mission reformulé (5 lignes max) |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : au démarrage de chaque projet, avant toute autre brique. B-00 est la première brique de la chaîne ; sans elle, B-01 ne peut pas proposer de MPD valide.
Ce que vous fournissez à l'IA : les pièces du projet (PDF, DXF, DWG, etc.) et l'énoncé de mission du client. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}} par les valeurs du projet.
Ce que vous validez à la sortie : l'inventaire des pièces, la liste des contradictions (non résolues), la reformulation de mission en 5 lignes.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir l'inventaire complet des pièces reçues pour l'opération {{ID-01}} — {{ID-02}}, et reformuler l'énoncé de mission. Tu ne dessines rien, tu ne calcules rien, tu ne conclus rien.


ÉTAPE 1 — Inventaire des pièces
Pour chaque fichier reçu, liste :
- nom du fichier et format (PDF vectoriel / PDF image / DXF / DWG / autre) ;
- pages ou folios utiles, avec leur objet ;
- indice et date de la pièce ;
- échelle (si cotée) ;
- orientation (si plan) ;
- pièces inexploitables : image illisible, fichier corrompu, calques vides — tu le dis explicitement.


ÉTAPE 2 — Éléments structurants extraits
Liste les éléments structurants cités dans les pièces, en rattachant CHACUN à sa source (fichier + folio/page + indice) :
- murs, refends, poteaux, profilés, sommiers, fondations ;
- niveaux, hauteurs, épaisseurs ;
- usages et surcharges annoncées ;
- contraintes de site (occupation, voisinage, accès).


ÉTAPE 3 — Contradictions détectées
Liste TOUTES les contradictions entre pièces, SANS LES TRANCHER :
- donnée concernée | pièce A (référence) | pièce B (référence) | nature de l'écart.
Ne propose aucune résolution — c'est moi qui décide.


ÉTAPE 4 — Énoncé de mission reformulé
En 5 lignes maximum :
- objet de la mission ;
- périmètre du lot ;
- livrables attendus ;
- exclusions explicites (désamiantage, déplombage, curage/démolition, espaces verts, dimensionnement de la protection au feu, fluides/CVC/électricité/VRD).


INTERDICTIONS
- Ne dessine rien.
- Ne calcule rien.
- N'invente aucune pièce : tout élément cité est rattaché à un fichier et un folio.
- Ne tranche aucune contradiction.
- Si une pièce est illisible, tu le dis — tu ne la commentes pas de mémoire.
- Aucun placeholder ne doit subsister dans ta sortie.


CRITÈRE D'ACCEPTATION
L'inventaire est accepté si :
- chaque pièce reçue figure avec son indice et ses folios utiles ;
- chaque élément structurant est rattaché à une source citée ;
- chaque contradiction est listée sans être résolue ;
- l'énoncé de mission tient en 5 lignes et cite les exclusions.
Si un seul de ces quatre points n'est pas satisfait, tu signales l'écart et tu t'arrêtes — tu ne produis pas une version partielle.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} (code projet) et {{ID-02}} (intitulé de l'opération) par les valeurs du projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Tu ne dessines rien, tu ne calcules rien, tu ne conclus rien » | Empêche la contamination de l'inventaire par une production prématurée — c'est la cause directe des plans génériques produits dans la conversation d'origine (prompts 2 et 5) |
| « rattachés à sa source (fichier + folio + indice) » | Verrou V2 — tout élément cité doit être traçable. Un élément structurant sans source est un élément qui ne peut pas être vérifié |
| « sans les trancher — c'est moi qui décide » | Verrou V1 — les contradictions sont signalées, pas arbitrées par le modèle. Un modèle qui tranche une contradiction en B-00 fausse toute la chaîne aval |
| « Si une pièce est illisible, tu le dis — tu ne la commentes pas de mémoire » | Anti-hallucination — la pièce illisible est l'endroit exact où un modèle comble avec du plausible. Cette clause l'oblige à déclarer l'illisibilité |
| « Aucun placeholder ne doit subsister dans ta sortie » | Verrou V7 — un placeholder résiduel est une invitation pour le modèle à combler le vide à votre place |
| « Si un seul des quatre points n'est pas satisfait, tu signales l'écart et tu t'arrêtes » | Verrou V4 — pas de livraison partielle silencieuse. Un inventaire partiel présenté comme complet est plus dangereux qu'un inventaire absent |

________________


4. RÉFÉRENCES
Briques amont
Aucune — B-00 est la première brique de la chaîne.
Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-01 (Proposition de la matrice) | L'inventaire des pièces et l'énoncé de mission reformulé — sans eux, B-01 ne peut pas proposer de MPD valide |
| B-02 (Fiche de données) | La référence exacte des pièces (fichier + folio + indice) |
| B-10 (Audit critique du CCTP) | L'inventaire des pièces, la référence exacte du CCTP (fichier + folio + indice), l'énoncé de mission reformulé |
| B-11 (Audit du diagnostic structure) | La référence exacte du diagnostic (fichier + folio + indice), les plans de récolement/DOE |
| B-12 (Audit des pièces géotechniques) | La référence exacte du rapport géotechnique (fichier + folio + indice) |
| B-13 (Détection et qualification) | La liste des contradictions détectées à chaud par B-00 — B-13 les reprend pour les qualifier (gravité × nature) et les rattacher aux briques |
| B-14 (Clarification du périmètre) | L'énoncé de mission reformulé et les exclusions citées — B-14 s'appuie dessus pour construire la matrice INCLUS/EXCLU/À TRANCHER |
| B-20 (Conception structure GO) | L'énoncé de mission, les exclusions |
| B-21 (Descente de charges préliminaire) | La référence exacte des pièces (usage des locaux, complexes de plancher) |
| B-30 (Calage sur dxf/dwg source) | La référence exacte du fichier source (DOC-02), son format, ses unités déclarées |
| B-32 (Vue nettoyée par livrable) | La référence exacte du fichier source (DOC-02), ses calques ou entités |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-00 |
| --- | --- | --- |
| DOC-01 | Inventaire des pièces (fichier, folio, indice, échelle) | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| ID-02 | Intitulé de l'opération | BLOQUANTE (pour l'en-tête de sortie) |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | BLOQUANTE (dès B-00) |

Variables produites
B-00 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (inventaire + contradictions + mission reformulée) qui alimente B-01, B-13 et B-14, mais qui n'est pas une valeur unique stockée en FDC.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-01, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain : à la sortie de B-00, vous devez vérifier que chaque pièce reçue figure dans l'inventaire, et que les contradictions listées sont bien non résolues. Si le modèle a proposé une résolution, c'est une anomalie — vous la signalez et vous demandez une reprise.
Cas particulier — pièce illisible : si une pièce est illisible (image corrompue, PDF sans couche texte, calques vides dans le DXF), B-00 la cite avec la mention « pièce inexploitable » et son motif. Elle ne la commente pas de mémoire. Vous pouvez alors soit la remplacer, soit l'inscrire au RDR (B-03) comme réserve.
Cas particulier — absence de pièce : si une pièce attendue est absente (pas de CCTP, pas de diagnostic, pas de géotechnique), B-00 ne la cite pas dans l'inventaire (elle n'a pas été reçue). C'est B-01 qui statuera son statut (FOURNIE / NON NÉCESSAIRE / À PRODUIRE PAR GO / BLOQUANTE / PARTIELLE). B-00 ne prend pas cette décision.
Format de sortie attendu : quatre tableaux ou sections distinctes — (1) inventaire des pièces, (2) éléments structurants, (3) contradictions, (4) énoncé de mission reformulé. Chaque section est identifiée par son titre.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Qualification `CFG-01` obligatoire.** B-00 qualifie la configuration de maturité MOE dès l'inventaire : `CFG-1` (aucun BET structure MOE), `CFG-2` (BET structure MOE en PDF ou principe DCE, sans DWG de coffrage), `CFG-3` (BET structure MOE vectoriel complet : DWG/DXF/IFC PRO-DCE + notes) ou `CFG-4` (mission partielle localisée). Cette qualification conditionne toute la suite : elle détermine qui conçoit, ce que nous transcrivons, et ce que nous ne demandons jamais.

**Interdiction de réclamer un livrable inexistant.** En `CFG-2` et `CFG-4`, il est **interdit** de demander un « DXF de coffrage MOE » : ce livrable n'existe pas dans ces configurations. La transcription vectorielle des ouvrages MOE et de leurs interfaces est notre production (`B-32` → `B-20`). En `CFG-1`, l'absence de BET structure MOE est un fait de mission, pas un blocage : la conception est produite en `INTERNE-GO` avec alerte contractuelle.

**Inventaire vectoriel exhaustif.** Pour chaque pièce, B-00 qualifie le mode d'exploitation : vecteur natif (DXF/DWG), PDF vectoriel (extraction des tracés et des textes), PDF raster (relevé déclaré, incertitude portée), IFC. Une pièce non vectorielle n'est jamais déclarée inexploitable sans avoir tenté l'extraction vectorielle et la reconnaissance de texte.
**[Fin de 02_PHASE_0_CADRAGE/B-00_Inventaire.md]**

---

**[Début du fichier : 02_PHASE_0_CADRAGE/B-01_MPD.md]**

Fichier 02_PHASE_0_CADRAGE/B-01_MPD.md — CARNAC v3.0
________________


B-01 — PROPOSITION DE LA MATRICE DE PÉRIMÈTRE ET DE DISPONIBILITÉ
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 0 — Cadrage et qualification |
| Brique précédente | B-00 (Inventaire) |
| Brique suivante | B-02 (Fiche de Données de Conception) |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | Sortie de B-00 (inventaire + mission reformulée), énoncé de mission, dictionnaire de variables CARNAC (01_DICTIONNAIRE/CARNAC_v3.0_variables.csv) |
| Sortie unique | MPD complète (tableau à 8 colonnes) + synthèse des variables bloquantes, à produire, et non nécessaires (pour validation ligne par ligne) |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-00, avant toute autre brique. B-01 est le pivot de tout le carnet : c'est elle qui active ou désactive les briques en aval, et qui fixe le mode de chacune.
Ce que vous fournissez à l'IA : la sortie complète de B-00 (inventaire, éléments structurants, contradictions, mission reformulée) et le dictionnaire de variables CARNAC. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} par le code projet.
Ce que vous validez à la sortie : ligne par ligne, chaque statut NON NÉCESSAIRE (périmètre). C'est votre décision, pas celle du modèle. Un NON NÉCESSAIRE mal validé désactive une brique qui aurait dû s'exécuter ; un BLOQUANTE mal validé suspend inutilement une brique qui aurait pu tourner.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : proposer la Matrice de Périmètre et de Disponibilité (MPD) de l'opération {{ID-01}}, à partir de l'inventaire B-00, de l'énoncé de mission et du dictionnaire de variables CARNAC. Tu PROPOSES, je VALIDE. Aucun statut n'est définitif avant ma validation.


RÈGLES DE STATUT
Chaque variable lue par au moins une brique du dictionnaire reçoit UN SEUL des cinq statuts suivants :
- FOURNIE — la pièce existe et contient la donnée.
- NON NÉCESSAIRE (périmètre) — la donnée n'est pas utile au périmètre de la mission. MOTIF DE PÉRIMÈTRE OBLIGATOIRE.
- À PRODUIRE PAR GO — la donnée doit être produite par nous (cas type : aucun BET structure de conception, diagnostic + plans de principe seulement).
- BLOQUANTE — la donnée est nécessaire à une brique activée mais absente ou inexploitable.
- PARTIELLE — la donnée existe mais incomplète ou ambiguë.


INTERDICTIONS
- Tu ne décides jamais SANS OBJET : c'est moi qui valide les NON NÉCESSAIRE, ligne par ligne.
- Tu ne proposes aucun mode COMPLET sur une variable BLOQUANTE.
- Tu ne retiens aucune valeur de repli.
- Tu ne proposes PAS NON NÉCESSAIRE pour une donnée au seul motif qu'elle n'est pas fournie : le statut NON NÉCESSAIRE se justifie par le périmètre, jamais par la disponibilité.
- Tu cites pour chaque ligne : la pièce source (fichier + folio + indice) OU la raison de l'absence.


SORTIE
Tableau à huit colonnes :
Famille | Code | Libellé | Statut | Motif (si NON NÉCESSAIRE ou À PRODUIRE) | Source ou raison d'absence | Brique(s) consommatrice(s) | Mode induit


Puis une synthèse en trois paragraphes :
- liste des variables BLOQUANTES, avec les briques suspendues correspondantes ;
- liste des variables À PRODUIRE PAR GO, avec la brique INTERNE-GO qui les produira ;
- liste des variables NON NÉCESSAIRE, avec leur motif de périmètre — pour validation ligne par ligne.


CRITÈRE D'ACCEPTATION
La MPD est acceptée si :
- toute variable lue par une brique activée y figure ;
- tout NON NÉCESSAIRE porte un motif de périmètre (pas un simple « pas dispo ») ;
- tout BLOQUANTE est rattaché à une brique identifiée du dictionnaire ;
- tout À PRODUIRE PAR GO identifie la brique INTERNE-GO qui produira la donnée ;
- aucune décision SANS OBJET n'a été prise sans ma validation explicite.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} par le code projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Tu PROPOSES, je VALIDE » | Le « NON NÉCESSAIRE » reste votre décision, jamais celle du modèle — c'est la règle que vous avez explicitement demandée. Un modèle qui décide seul du NON NÉCESSAIRE peut désactiver une brique essentielle sans que personne ne s'en aperçoive |
| « MOTIF DE PÉRIMÈTRE OBLIGATOIRE » + « jamais par la disponibilité » | Distingue deux absences qui n'ont rien à voir : superstructure sans fondations (motif = périmètre, SANS OBJET) vs. G2 non commandée (statut = BLOQUANTE). Sans cette clause, un modèle peut déclarer « non nécessaire » une donnée juste parce qu'elle manque — et désactiver une brique qui aurait dû être bloquante |
| « Tu ne décides jamais SANS OBJET » | Verrou V11 — le SANS OBJET découle de la MPD validée, pas du modèle. Un SANS OBJET non validé est une brique silencieusement supprimée |
| « aucun mode COMPLET sur une variable BLOQUANTE » | Cohérence mode/statut — le mode proposé est cohérent avec le statut. Un COMPLET sur une donnée bloquante est une faute (V12) |
| « tu signales l'écart et tu t'arrêtes » | Empêche la MPD partielle silencieuse. Une MPD incomplète présentée comme complète est plus dangereuse qu'une MPD absente |

Le piège à éviter : la tentation la plus fréquente d'un modèle sur B-01 est de déclarer NON NÉCESSAIRE toute donnée non fournie, pour « faire avancer le projet ». C'est exactement ce que la clause « jamais par la disponibilité » interdit. Une donnée non fournie est BLOQUANTE, pas NON NÉCESSAIRE — sauf si le périmètre de la mission justifie qu'elle n'est pas nécessaire.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | L'inventaire des pièces et l'énoncé de mission reformulé — sans eux, B-01 ne peut pas proposer de MPD valide |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-02 (Fiche de données) | La MPD validée — B-02 ne remplit que les variables que B-01 a statuées FOURNIE, PARTIELLE, BLOQUANTE ou À PRODUIRE PAR GO |
| B-03 (Registre des décisions) | Les décisions de périmètre (les NON NÉCESSAIRE validés) sont inscrites au RDR comme décisions D-xx, avec auteur et date |
| B-04 (Plan de travail dégradé) | Les variables BLOQUANTE et les briques suspendues — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-10 (Audit critique du CCTP) | Le statut de DOC-04 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) |
| B-11 (Audit du diagnostic structure) | Le statut de DOC-05 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) |
| B-12 (Audit des pièces géotechniques) | Le statut de DOC-06 (FOURNIE, PARTIELLE, BLOQUANTE, SANS OBJET) et des variables SOL-01 à SOL-08 |
| B-13 (Détection et qualification) | Les décisions de périmètre — elles permettent de savoir si une contradiction est dans notre périmètre ou hors périmètre |
| B-14 (Clarification du périmètre) | Les décisions de périmètre (les NON NÉCESSAIRE validés) |
| B-20 (Conception structure GO) | Le statut de AC-03 (BET structure de conception) et DOC-03 (plans BET) — INTERNE-GO si AC-03 est À PRODUIRE PAR GO |
| B-21 (Descente de charges préliminaire) | Le statut de CHG-01 à CHG-08 (FOURNIE / PARTIELLE / BLOQUANTE / À PRODUIRE PAR GO) |
| B-30 (Calage sur dxf/dwg source) | Le statut de DOC-02 (FOURNIE, PARTIELLE, BLOQUANTE) et de GEO-06 à GEO-08 |
| B-40 (Fondations superficielles) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-41 (Fondations profondes) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-42 (Verticaux BA) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-43 (Planchers et dallages) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-44 (Charpente bois) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-45 (Structure métallique) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-46 (Maçonnerie : vérification) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-47 (Escaliers) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-48 (Prédalles et planchers préfabriqués) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-49 (Linteaux et seuils) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-50 (Assemblages et ancrages) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-01 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| DOC-01 | Inventaire des pièces (sortie de B-00) | BLOQUANTE (B-01 ne peut pas proposer de MPD sans inventaire) |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | BLOQUANTE (dès B-00) |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | BLOQUANTE (dès B-01) |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE si L / XL ou R+n |

Variables produites (indirectement)
B-01 ne produit pas une variable au sens du dictionnaire : sa sortie est la MPD elle-même, qui statue sur le statut de toutes les autres variables. La MPD est un document, pas une variable.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | Les 106 variables, avec « Bloque » et « Mentionnée » | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique du carnet : à la sortie de B-01, vous devez valider ligne par ligne les NON NÉCESSAIRE. C'est le seul moment où vous pouvez empêcher une brique de s'exécuter à tort, ou au contraire l'activer alors qu'elle aurait été silencieusement désactivée. Cette validation doit être explicite et écrite — un « ok » global ne suffit pas, car il ne permet pas de tracer quelle ligne a été validée et pourquoi.
Cas particulier — pas de BET de conception : si AC-03 (BET structure de conception) est absente, le statut est À PRODUIRE PAR GO avec motif « aucun BET de conception ». Le mode induit pour B-20 est INTERNE-GO. La MPD ne doit pas déclarer AC-03 NON NÉCESSAIRE — ce serait une erreur de périmètre : la conception est nécessaire, elle est simplement à produire par nous.
Cas particulier — pas de géotechnique : si le projet est une superstructure sans impact sur les fondations, les variables SOL-01 à SOL-07 peuvent être déclarées NON NÉCESSAIRE (périmètre) avec motif « travaux de superstructure, fondations existantes non sollicitées ni modifiées ». Les briques B-40 et B-41 passent alors en SANS OBJET. Les variables SOL-xx n'apparaissent pas en FDC.
Cas particulier — pièce fournie mais partielle : si une pièce existe mais est incomplète (par exemple, un G2 AVP sans G3), le statut est PARTIELLE, avec mention de ce qui manque. Le mode induit est PARTIEL-DÉCLARÉ si vous inscrivez une décision RDR, PARAMÉTRIQUE sinon.
Format de sortie attendu : un tableau principal à 8 colonnes (Famille, Code, Libellé, Statut, Motif, Source, Brique(s) consommatrice(s), Mode induit), suivi de trois paragraphes de synthèse (bloquantes, à produire, non nécessaires). Les NON NÉCESSAIRE doivent être listés un par un, avec leur motif, pour permettre une validation ligne par ligne.
Consignation : la MPD validée est annexée au RDR (B-03) comme décision D-xx (« validation de la MPD en date du … »). Elle ne se modifie plus sans une nouvelle décision datée.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Choix du gabarit `CFG-02` et découpage `CFG-03`.** B-01 statue le gabarit d'opération : `S` (1 à 5 porteurs, < 100 m² ou ouvrage unique, avec ou sans BET MOE), `M` (100 à 2 500 m², un bloc unitaire) ou `L-XL` (> 2 500 m², joints de dilatation, niveaux-types, sous-sols, préfabrication). En `L-XL`, B-01 impose le découpage en blocs structurels `JD` et en niveaux-types (`CFG-03`) et active obligatoirement `B-25` (stabilité globale, contreventement, sismique) et `B-34` (synthèse des réservations).

**Voie compacte du gabarit `S`.** En gabarit `S`, la MPD est produite en trois portes seulement : `Porte 1` cadrage + calage et vue nettoyée + hypothèses `H-xx` ; `Porte 2` schéma mécanique `AVANT/APRÈS` + descente de charges + note de calcul ; `Porte 3` plan d'exécution tout-en-un (implantation, coupes, ferraillage ou assemblages, Points d'Arrêt, auto-contrôle). La voie compacte supprime des validations intermédiaires redondantes ; elle ne supprime aucune sortie ni aucun verrou.

**Preuve d'épuisement avant tout `BLOQUANTE`.** Une variable ne peut être déclarée `BLOQUANTE` qu'après la preuve d'épuisement `V14` de la totalité des pièces reçues. Le statut `NON NÉCESSAIRE` reste une décision humaine ligne à ligne et ne se justifie jamais par la disponibilité.
**[Fin de 02_PHASE_0_CADRAGE/B-01_MPD.md]**

---

**[Début du fichier : 02_PHASE_0_CADRAGE/B-02_FDC.md]**

Fichier 02_PHASE_0_CADRAGE/B-02_FDC.md — CARNAC v3.0
________________


B-02 — FICHE DE DONNÉES DE CONCEPTION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 0 — Cadrage et qualification |
| Brique précédente | B-01 (MPD validée) |
| Brique suivante | B-03 (RDR) |
| Modes d'appel | COMPLET (valeurs disponibles) · PARTIEL-DÉCLARÉ (décision RDR déclarée pour une valeur) · PARAMÉTRIQUE (variable restant en symbole) |
| Entrées lues | MPD validée (B-01), toutes les pièces du projet, décisions RDR déjà inscrites (le cas échéant) |
| Sortie unique | FDC complète (tableau valeurs + sources + fiabilité) + tableau des verrous en fin de fiche |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après validation de la MPD par vous. B-02 transforme la MPD en document exploitable : elle rassemble les valeurs effectivement lues par les briques, avec leurs sources et leur niveau de fiabilité.
Ce que vous fournissez à l'IA : la MPD validée, les pièces du projet, les décisions RDR déjà prises (s'il y en a). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} par le code projet.
Ce que vous validez à la sortie :
* chaque valeur et sa source ;
* le niveau de fiabilité (Contractuelle / Décision / À confirmer) ;
* la liste des verrous (variables BLOQUANTE qui n'ont pas de valeur).
Principe clé de la FDC : la FDC porte les valeurs et leur source, pas seulement des renvois. Un lecteur de note de calcul doit pouvoir lire la FDC sans ouvrir le CCTP. C'est ce qui garantit qu'une note de calcul reste opposable — chaque valeur qui y figure est traçable jusqu'à sa source.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la Fiche de Données de Conception (FDC) de l'opération {{ID-01}}, à partir de la MPD validée et des pièces du projet. La FDC porte les VALEURS et leur SOURCE — elle doit pouvoir être lue sans ouvrir le CCTP.


RÈGLES
1. Seules les variables lues par au moins une brique activée figurent en FDC. Une variable non lue n'apparaît pas.
2. Chaque ligne porte : code, libellé, valeur, unité, source (fichier + folio/page + indice) OU mention « VERROU » si la valeur est absente.
3. Niveau de fiabilité obligatoire pour chaque valeur :
   - Contractuelle — valeur issue d'une pièce du marché ;
   - Décision — valeur issue du RDR (numéro, auteur, date cités) ;
   - À confirmer — valeur de travail, non validée.
4. Aucune valeur de repli n'est proposée. Aucune « pratique courante » n'est invoquée comme source.
5. Les variables VERROU sont listées en fin de FDC avec la brique suspendue et la voie d'obtention.
6. Les conflits entre pièces (deux valeurs incompatibles pour le même code) ne sont PAS arbitrés : ils sont listés comme VERROU et inscrits au RDR (B-03).


INTERDICTIONS
- Ne remplis aucun champ sans source citée.
- Ne retiens aucune valeur sur la base d'une pratique courante, d'un ordre de grandeur ou d'une « valeur usuelle ».
- Ne tranche aucune contradiction entre pièces.
- Ne propose aucune décision qui appartient au RDR.


SORTIE
Tableau 1 : Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) consommatrice(s)
Tableau 2 (fin de fiche) : Code VERROU | Brique suspendue | Voie d'obtention proposée (relevé / essai / mission G / décision MOA) | Responsable pressenti


CRITÈRE D'ACCEPTATION
La FDC est acceptée si :
- chaque ligne a une source citée ou est marquée VERROU ;
- aucun champ n'est renseigné sans niveau de fiabilité ;
- les VERROU sont en fin de fiche avec voie d'obtention ;
- aucune contradiction n'a été tranchée silencieusement ;
- aucune variable non lue par une brique n'est présente en FDC.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} par le code projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « lisible sans ouvrir le CCTP » | La FDC est la référence des notes de calcul. Si elle ne porte pas les valeurs, chaque vérificateur (BC, BET, MOE) doit ouvrir le CCTP pour vérifier une note de calcul — ce qui est ingérable en pratique. La FDC porteuse des valeurs et de leurs sources est la seule forme opposable |
| « Aucune valeur de repli… aucune pratique courante » | C'est la faille la plus coûteuse de la conversation d'origine : 40 mm d'enrobage « au titre des exigences de tenue au feu du projet » ont été retenus sans que ces exigences existent. Cette clause interdit ce type de valeur non sourcée |
| « deux valeurs incompatibles → VERROU + RDR » | Traitement explicite de la contradiction XC2/35 mm vs XA3/50 mm du projet Flora : l'arbitrage est une décision RDR, pas une décision du modèle. Sans cette clause, un modèle peut « choisir » la valeur la plus favorable |
| « aucune variable non lue n'apparaît » | Évite la FDC « pour faire complet » qui vous obligeait à remplir des champs inutiles. Une FDC courte et exacte est plus utile qu'une FDC longue et remplie de champs vides |
| « tu signales l'écart et tu t'arrêtes » | Pas de FDC partielle silencieuse. Une FDC partielle présentée comme complète est une FDC qui sera lue comme complète — et les notes de calcul qui s'appuient dessus seront fausses |
| Niveau de fiabilité obligatoire | Un vérificateur doit pouvoir distinguer d'un coup d'œil une valeur contractuelle (que personne ne peut contester) d'une valeur de travail (qui peut être révisée). Sans cette distinction, toutes les valeurs sont traitées au même niveau — ce qui est faux |

Les trois niveaux de fiabilité — précision utile :

| Niveau | Signification | Conséquence en cas de désaccord |
| --- | --- | --- |
| Contractuelle | Issue d'une pièce du marché (CCTP, plan, marché) | Ne se conteste pas unilatéralement ; doit passer par un avenant ou une décision MOA |
| Décision | Issue d'un arbitrage inscrit au RDR (auteur, date, justification) | Peut être révisée par une nouvelle décision RDR, avec traçabilité |
| À confirmer | Hypothèse de travail, non validée | Doit être confirmée avant exécution ; le livrable qui l'utilise porte une réserve |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte des pièces (fichier + folio + indice) |
| B-01 (Proposition de la matrice) | La MPD validée — B-02 ne remplit que les variables que B-01 a statuées FOURNIE, PARTIELLE, BLOQUANTE ou À PRODUIRE PAR GO |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les VERROU listés en fin de FDC — B-03 les inscrit au Registre des Verrous (section 3) |
| B-04 (Plan de travail dégradé) | Les VERROU et les briques suspendues — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-22 (Note d'hypothèses de conception) | Les valeurs et leur fiabilité — les valeurs À confirmer deviennent des hypothèses H-xx |
| B-24 (Vérification d'éléments existants non) | Les données disponibles sur l'existant (EXI-01 à EXI-04) — B-24 les cite, mais ne les complète pas |
| B-25 (Stabilité globale, contreventement, joints) | La zone sismique, la catégorie d'importance, la classe de sol et les coefficients |
| B-40 (Fondations superficielles) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-41 (Fondations profondes) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-42 (Verticaux BA) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-43 (Planchers et dallages) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-44 (Charpente bois) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-45 (Structure métallique) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-46 (Maçonnerie : vérification) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-47 (Escaliers) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-48 (Prédalles et planchers préfabriqués) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-49 (Linteaux et seuils) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-50 (Assemblages et ancrages) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-60 (Plans d'exécution) | Les valeurs utilisées dans les plans (matériaux, niveaux, positions) |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les variables BLOQUANTE — T-04 les cite comme objets de demande |

Variables consommées

| Code | Libellé | Statut dans B-02 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| Toutes les variables statuées FOURNIE, PARTIELLE, BLOQUANTE ou À PRODUIRE PAR GO par B-01 | Selon la variable | Selon le statut |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |

Variables produites
B-02 ne produit pas une variable au sens du dictionnaire : sa sortie est la FDC, qui contient les valeurs de toutes les variables retenues. La FDC est un document, pas une variable.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | Les 106 variables, avec leur nature (bloque/mentionnée) | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| MPD (sortie B-01) | Statut de chaque variable pour le projet en cours | Document de projet |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus important de cette brique : à la sortie de B-02, vous devez valider chaque valeur et valider son niveau de fiabilité. C'est le moment où vous décidez ce qui est contractuel, ce qui est votre décision, et ce qui est votre hypothèse de travail. Un modèle qui remplit la FDC avec des valeurs non sourcées produit une FDC qui ne vaut rien.
Cas particulier — valeur déclarée en mode PARTIEL-DÉCLARÉ : si vous avez déjà pris une décision RDR (par exemple, retenir XA3 en lieu et place de XC2), la FDC porte la valeur (XA3), la source (« Décision D-01 du 17/10/2026 ») et la fiabilité (« Décision »). La valeur XC2 du CCTP n'est pas effacée : elle est listée en VERROU (« contradiction XC2 vs XA3 »), et la décision RDR est citée dans la ligne.
Cas particulier — variable À PRODUIRE PAR GO : si AC-03 (BET structure de conception) est À PRODUIRE PAR GO, la FDC ne porte pas de valeur pour cette variable — elle est listée en VERROU avec la brique B-20 en mode INTERNE-GO comme producteur. La sortie de B-20 deviendra l'entrée des briques de calcul, sans passer par une nouvelle FDC (B-20 produit son propre dossier de conception).
Cas particulier — conflit entre deux pièces : si le CCTP dit XA4 et la décision RDR dit XA3, la FDC porte XA3 en valeur, Décision D-xx en fiabilité, et XA4 (CCTP, réf.) en VERROU. Le conflit n'est pas tranché en silence : il est tracé.
Format de sortie attendu : deux tableaux distincts — tableau 1 (variables résolues avec valeur, source, fiabilité), tableau 2 (VERROU avec brique suspendue et voie d'obtention). Chaque ligne du tableau 1 a impérativement une source citée.
Consignation : la FDC validée est annexée au RDR (B-03) comme décision D-xx (« validation de la FDC en date du … »). Elle est mise à jour à chaque nouvelle décision RDR qui modifie une valeur.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 02_PHASE_0_CADRAGE/B-02_FDC.md]**

---

**[Début du fichier : 02_PHASE_0_CADRAGE/B-03_RDR.md]**

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
**[Fin de 02_PHASE_0_CADRAGE/B-03_RDR.md]**

---

**[Début du fichier : 02_PHASE_0_CADRAGE/B-04_PTD.md]**

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
**[Fin de 02_PHASE_0_CADRAGE/B-04_PTD.md]**

<!-- FIN DU PACK — CARNAC v3.0 -->
