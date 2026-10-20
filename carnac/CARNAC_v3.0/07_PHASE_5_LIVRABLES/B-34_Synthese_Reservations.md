Fichier 07_PHASE_5_LIVRABLES/B-34_Synthese_Reservations.md — CARNAC v3.0
________________


B-34 — SYNTHÈSE DES RÉSERVATIONS ET INTERFACES AVEC LES LOTS TECHNIQUES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — création de la brique (voir Journal des modifications, entrée v3.0) |
| Phase | 5 — Synthèse et livrables d'exécution |
| Brique précédente | B-20 (Conception et synthèse), B-25 (Stabilité globale), B-40 à B-50 (calculs) |
| Brique suivante | B-60 (Plans d'exécution), B-62 (Nomenclature), B-64 (Notice de synthèse) |
| Modes d'exécution | COMPLET (plan de réservations de tous les lots fourni et cohérent) · PARTIEL-DÉCLARÉ (plan partiel : les réservations non documentées sont déclarées) · HYPOTHÈSE-NOTIFIÉE (dimensions standard de réservation non fournies mais bornables par DTU ou notice) · INTERNE-GO (aucun plan de réservations n'existe : nous établissons les positions de principe sur la base des pièces disponibles) |
| Entrées lues | Sortie de B-20, vue nettoyée et différentielle (B-32), notes B-40 à B-50, plan de réservations de chaque lot technique s'il existe, CCTP (lot 01 et lots techniques), DOC-09 (fiches techniques) |
| Sortie unique | Carnet unique des réservations : tableau par niveau et par élément porteur, plan de réservations reporté sur le fond B-32, liste des renforcements induits et des Points d'Arrêt |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : en phase 5, avant la production des plans d'exécution (B-60), pour tout ouvrage comportant des trémies, gaines, percements, scellements ou attentes techniques — systématiquement en gabarit `L-XL` (`CFG-02`), et dès qu'un lot technique est attribué.

Ce que vous fournissez à l'IA : la sortie de B-20, la vue nettoyée B-32, les notes de calcul B-40 à B-50, les plans de réservations des lots techniques s'ils existent, et le CCTP. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.

Ce que vous validez à la sortie : la position et la dimension de chaque réservation, le renforcement induit (ou son absence justifiée), les réservations non documentées portées en Points d'Arrêt, et le report graphique sur le plan de réservations.

Ce que B-34 apporte de spécifique — la réservation n'est pas un détail de second œuvre :
| Aspect | Sans B-34 | Avec B-34 |
| --- | --- | --- |
| Percements en voile ou poutre | Découverts sur chantier, après coulage | Listés, positionnés, renforcés ou interdits avant production |
| Trémies de gaines | Positionnées par le lot technique après nos plans | Arbitrées avec la structure, reportées sur nos plans |
| Attentes et scellements | Improvisés en chantier | Dimensionnés avec les efforts transmis (B-50) |
| Interfaces entre lots | Renvois mutuels non tranchés | Matrice des interfaces avec responsable désigné |
| Oublis | Découverts en réception | Détectés par contrôle croisé B-33 et B-70 |
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.

MISSION : établir le carnet unique des réservations et des interfaces techniques de l'opération {{ID-01}} — {{ID-02}}, à partir de la synthèse structurelle B-20, de la vue nettoyée B-32, des notes de calcul B-40 à B-50 et des pièces techniques disponibles. Tu ne calcules aucun réseau, tu ne dimensionnes aucun équipement : tu positionnes, vérifies la compatibilité structurale et renforces lorsque c'est nécessaire.

MÉTHODE
1. Inventorie toutes les réservations demandées par les pièces reçues : trémies de gaines, percements, scellements, attentes, fourreaux, regards, fosses d'ascenseur, réservations de réseaux, passages de câbles, évacuations. Pour chacune, cite la pièce source (fichier, folio, indice) et le lot demandeur.
2. Recense les réservations manquantes au regard de la destination réelle du bâtiment : une pièce qui ne demande rien ne prouve pas l'absence de besoin. Toute réservation prévisible mais non documentée est portée en Point d'Arrêt avec prescription de confirmation.
3. Positionne chaque réservation sur la vue nettoyée B-32 : niveau, élément porteur concerné, cote depuis les axes du Repère Structurel Unique, dimensions, forme, altitude.
4. Vérifie la compatibilité structurale de chaque réservation : zone interdite (about de poutre, nœud, zone d'ancrage, membrure tendue), distance minimale aux rives, pourcentage de section retirée, incidence sur le ferraillage ou sur le profilé.
5. Pour chaque réservation incompatible ou significative, prescris le renforcement induit (armatures de renfort, cadre, chevêtre, renfort de membrure, platine) et renvoie le dimensionnement à la brique de calcul compétente, sans jamais l'inventer.
6. Construis la matrice des interfaces entre lots : réservation, lot demandeur, lot réalisateur, lot bénéficiaire, responsable de la cote, échéance de confirmation, Point d'Arrêt éventuel.
7. Produis le plan de réservations reporté sur le fond B-32, avec tableau intégré, repères cohérents avec B-20 et renvois aux coupes.
8. Contrôle par script l'absence de collision entre réservations, entre réservation et ferraillage, et entre réservation et appui.

INTERDICTIONS
- Ne dimensionne aucun réseau, aucune gaine, aucun équipement : tu positionnes et tu vérifies la compatibilité structurale.
- Ne positionne aucune réservation « de mémoire » ou par symétrie supposée : chaque position vient d'une pièce ou d'un calcul cité.
- Ne crée aucune réservation dans une zone interdite sans renforcement prescrit ou refus motivé.
- Ne déclare jamais une réservation « à définir par le lot technique » sans Point d'Arrêt associé, responsable et échéance.
- Ne produis aucun plan sans tableau de réservations intégré et sans repères identiques à B-20.
- N'ajoute aucun élément de second œuvre sur la vue : seules les réservations et attentes structurelles y figurent.

SORTIE
Pièce 1 — Tableau des réservations : repère, niveau, élément porteur, position, dimensions, altitude, lot demandeur, pièce source, compatibilité, renforcement prescrit, statut.
Pièce 2 — Réservations non documentées : repère, besoin constaté, motif, Point d'Arrêt proposé, responsable, échéance.
Pièce 3 — Matrice des interfaces entre lots : réservation, demandeur, réalisateur, bénéficiaire, responsable de la cote, échéance.
Pièce 4 — Plan de réservations reporté sur le fond B-32, avec tableau intégré et renvois.
Pièce 5 — Journal du contrôle de collisions : nombre de réservations contrôlées, collisions détectées, collisions résolues, collisions résiduelles.

CRITÈRE D'ACCEPTATION
Le carnet est accepté si :
- chaque réservation est rattachée à une pièce source ou à un Point d'Arrêt avec responsable et échéance ;
- chaque réservation est positionnée par rapport aux axes du Repère Structurel Unique, avec niveau et altitude ;
- la compatibilité structurale est statuée pour chaque réservation, avec renforcement prescrit ou refus motivé ;
- la matrice des interfaces désigne un responsable de cote pour chaque réservation ;
- le plan de réservations est produit sur le fond B-32, avec tableau intégré et repères cohérents avec B-20 ;
- le contrôle de collisions est exécuté par script et journalisé.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
| Clause | Pourquoi |
| --- | --- |
| Brique distincte, en amont de B-60 | Les réservations décidées après la production des plans obligent à reprendre les plans, les notes et la nomenclature. Les traiter en amont supprime la principale source de reprises en phase EXE |
| « Tu ne calcules aucun réseau » | Frontière de mission : nous sommes bureau d'études structure. Positionner et renforcer relève de notre lot ; dimensionner une gaine ou un débit relève du lot technique |
| Réservations non documentées portées en Point d'Arrêt | L'absence de demande n'est pas l'absence de besoin. Un Point d'Arrêt avec responsable et échéance est la seule protection contre l'oubli, et il est opposable |
| Zone interdite et pourcentage de section retirée | Une trémie dans un nœud ou dans un about de poutre met en cause la sécurité structurale. Le contrôle de zone est plus efficace qu'un renforcement systématique |
| Renforcement renvoyé à la brique compétente | Un renforcement inventé dans une brique de synthèse est une valeur non tracée, donc non opposable. Le renvoi maintient la chaîne de preuve |
| Matrice des interfaces avec responsable de cote | La cause la plus fréquente d'une réservation manquée est l'absence de responsable de la cote. La matrice désigne ce responsable une fois pour toutes |
| Contrôle de collisions par script | Les collisions entre réservations et ferraillage sont invisibles à l'œil sur un plan chargé. Seul un contrôle automatisé les détecte de manière exhaustive |
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-20 (Conception structure GO) | La trame, les porteurs et les zones sensibles |
| B-25 (Stabilité globale, contreventement, joints) | Les éléments de contreventement et les zones où tout percement est interdit |
| B-32 (Vue nettoyée par livrable) | Le fond structurel pur sur lequel les réservations sont positionnées |
| B-42 (Verticaux BA) | Les voiles et poteaux concernés, avec leur ferraillage |
| B-43 (Planchers et dallages) | Les dalles et planchers concernés, avec leurs zones critiques |
| B-48 (Prédalles et planchers préfabriqués) | Les limites de percement admissibles en prédalle |
| B-50 (Assemblages et ancrages) | Les attentes et scellements dimensionnés |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-33 (Vérification croisée) | La matrice des interfaces, contrôlée contre les plans et les notes |
| B-60 (Plans d'exécution) | Le plan de réservations et les renforcements à reporter |
| B-64 (Notice de synthèse) | La liste des réservations et des Points d'Arrêt |
| B-70 (Auto-contrôle déclaré de synthèse) | Le statut des Points d'Arrêt et l'exhaustivité des réservations |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-34 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | BLOQUANTE |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | NON BLOQUANTE |

Variables produites
B-34 ne produit pas de variable au sens du dictionnaire : sa sortie est un carnet de réservations et un plan reporté, qui alimentent B-60, B-33, B-64 et B-70.

Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | STR-03, DEC-07, GEO-13, CFG-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques, échelles, cartouche, plan de réservations | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain : à la sortie de B-34, vous validez la liste des réservations non documentées et les Points d'Arrêt proposés. C'est votre décision : une réservation portée en Point d'Arrêt engage l'entreprise sur un arrêt de production, une réservation acceptée sans preuve engage sa responsabilité.

Cas particulier — plans de réservations des lots techniques absents : B-34 s'appelle en INTERNE-GO et produit un plan de principe fondé sur la destination du bâtiment et sur les pièces disponibles, avec toutes les réservations non documentées portées en Points d'Arrêt.

Cas particulier — réservation demandée dans une zone interdite : B-34 refuse la position, propose une position alternative compatible et documente le refus. Il ne déplace jamais silencieusement une réservation demandée par un autre lot.

Cas particulier — réservation dimensionnante pour la structure : le renforcement est prescrit, renvoyé à la brique de calcul compétente, et le plan de réservations n'est diffusé qu'après retour du calcul.

Format de sortie attendu : cinq pièces distinctes (tableau, réservations non documentées, matrice des interfaces, plan reporté, journal de collisions). Le plan est produit sur le fond B-32.

Consignation : le carnet B-34 est annexé au RDL ; le plan de réservations est reporté au jeu de plans B-60 et référencé dans la notice B-64.
________________

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Cette fiche ne peut jamais déclarer une réservation « non demandée » avant d'avoir consommé 100 % des pièces reçues, y compris les notes générales et les cartouches des plans techniques.

**V15 — Différentiel temporel et continuité mécanique descendante.** Chaque réservation est rattachée au différentiel `EXISTANT − DÉMOLITION + PROJET` et vérifiée sur l'élément porteur réellement conservé ou neuf.

**Brique nouvelle v3.0.** B-34 est obligatoire en gabarit `L-XL` et pour tout ouvrage comportant des trémies en voile ou en poutre. Son plan de réservations est une pièce du dossier d'exécution, pas une annexe facultative.