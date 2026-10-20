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