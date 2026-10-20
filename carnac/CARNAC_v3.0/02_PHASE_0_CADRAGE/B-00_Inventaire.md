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