<!-- PACK CARNAC v3.0 — PACK 05 — PHASES 5 ET 6 : RÉSERVATIONS, LIVRABLES, VÉRIFICATION ET CLÔTURE (B-34, B-60 à B-64, B-33, B-70 à B-72) -->

# PACK 05 — PHASES 5 ET 6 : RÉSERVATIONS, LIVRABLES, VÉRIFICATION ET CLÔTURE (B-34, B-60 à B-64, B-33, B-70 à B-72)

**Quand coller ce pack** : Quand les notes de calcul sont visées.

**Ce qu'il contient** : B-34 réservations tous corps d'état · B-60 plans d'exécution purs · B-62 nomenclature · B-64 notice · B-33 vérification croisée globale · B-70 auto-contrôle · B-71 indiçage · B-72 clôture. En annexe, les quatre prompts transverse T-01 à T-04.

**Note d'usage** : L'annexe transverse est séparée par un repère de coupure : vous ne la collez que si vous invoquez T-01, T-02, T-03 ou T-04.

**Prérequis** : le pack `00_SOCLE.md` doit être collé avant celui-ci, dans la même discussion.

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
**[Début du fichier : 07_PHASE_5_LIVRABLES/B-34_Synthese_Reservations.md]**

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
**[Fin de 07_PHASE_5_LIVRABLES/B-34_Synthese_Reservations.md]**

---

**[Début du fichier : 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md]**

Fichier 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md — CARNAC v3.0
________________


B-60 — PLANS D'EXÉCUTION (PLANS COTÉS + COUPES + DÉTAILS + EXPORT DXF)
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 5 — Synthèse et livrables d'exécution |
| Brique précédente | La brique de calcul qui a produit la note (B-40 à B-50), ou B-20 pour un plan de principe |
| Brique suivante | B-62 (Nomenclature), B-64 (Notice de synthèse), B-31 (Preuve de superposition), B-33 (Vérification croisée) |
| Fréquence | À chaque livrable graphique produit par une brique de calcul (B-40 à B-50) ou de conception (B-20) |
| Modes d'appel | COMPLET (brique amont en mode COMPLET ou PARTIEL-DÉCLARÉ) · PARAMÉTRIQUE (brique amont en mode PARAMÉTRIQUE : le plan est filigrané et suffixé _P) |
| Paramètre d'appel | {{type_livrable}} = FOND / VERT / PLANCHER / CHARPENTE / METAL / MACON / ESCALIER / PREDALLE / LINTEAU / ASSEMBLAGE |
| Entrées lues | Note de calcul de la brique amont, vue nettoyée (B-32), calage (B-30), conventions de calques (annexe A), RDL, cartouche modèle |
| Sortie unique | Dossier graphique complet : plans cotés + coupes + détails + nomenclature graphique + export DXF + PNG + PDF, tous indicés, filigranés si PARAMÉTRIQUE, consignés au RDL |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : à chaque livrable graphique produit par une brique de calcul (B-40 à B-50) ou par B-20 (plan de principe). B-60 est la brique qui transforme les calculs en plans d'exécution — c'est le livrable final qui sera diffusé à l'entreprise.
Ce que vous fournissez à l'IA : la note de calcul de la brique amont, la vue nettoyée (B-32) du livrable concerné, le fichier calé (B-30), le cartouche modèle, et la convention de calques (annexe A). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * le plan général coté (positions, dimensions, réservations) ;
   * les coupes (niveaux, cotes, ferraillages ou profilés) ;
   * les détails (points singuliers, appuis, assemblages) ;
   * la nomenclature graphique (repères, désignations, quantités) ;
   * l'export DXF (structure à calques normalisés) ;
   * les trois formats (DXF, PNG, PDF) ;
   * le cartouche (code projet, indice, date, échelle, mode, mentions obligatoires) ;
   * la consignation au RDL.
Ce que B-60 produit — le périmètre exact :

| Élément | Nature |
| --- | --- |
| Plan général coté | Vue en plan du livrable, avec cotations complètes, repères des éléments |
| Coupes | Coupes longitudinale et transversale à l'échelle 1/50 ou 1/20, selon complexité |
| Détails | Détails à grande échelle (1/20, 1/10, 1/5) : appuis, ferraillages singuliers, assemblages |
| Nomenclature graphique | Tableau de nomenclature intégré au plan (renvoi à B-62 pour la nomenclature détaillée) |
| Export DXF | Fichier DXF à calques normalisés (annexe A), prêt à être utilisé par un outil aval |
| Export PNG et PDF | Versions image et document |
| Cartouche et indiçage | Cartouche complet, indice, date, mode, filigrane |

Ce que B-60 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Nomenclature détaillée et façonnage | B-62 |
| Notice de synthèse du livrable | B-64 |
| Vérification de la cohérence plan ↔ plan | B-33 (vérification croisée, déjà faite en amont) |
| Vérification des positions par superposition | B-31 (preuve de superposition, déjà faite en amont) |
| Note de calcul | Brique amont (B-40 à B-50) |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire le dossier graphique d'exécution {{type_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir de la note de calcul de la brique amont et de la vue nettoyée (B-32). Le dossier comprend : plans cotés + coupes + détails + export DXF + PNG + PDF, tous indicés et consignés au RDL.


RÈGLES NORMATIVES ET CONVENTIONS
- Convention de calques DXF : voir annexe A du carnet CARNAC — préfixe {{type_livrable}}- et fonctions standard (AXES, COFFRAGE, ACIER-INF, ACIER-SUP, ACIER-LONG, ACIER-TRANS, PROFILES, EXISTANT, DETAILS, NOMENCLATURE, HABILLAGE-TEXTE).
- Échelles autorisées : 1/200 (vue d'ensemble), 1/100, 1/50 (plans courants), 1/20, 1/10, 1/5 (détails).
- Cartouche normalisé : code projet, intitulé, indice, date, échelle, mode, brique source, numéro de plan, mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », mention « protection au feu adéquate à prévoir (hors lot GO) ».
- Unités : millimètres pour toutes les cotes (plan, sections, ferraillages) — voir annexe A §7. Les cotes de niveau sont en mètres avec 3 décimales.


MÉTHODE — DANS CET ORDRE


Étape 1 — Vérification des entrées
- La note de calcul de la brique amont est-elle disponible et complète ?
- La vue nettoyée (B-32) est-elle disponible et versionnée avec le livrable ?
- Le calage (B-30) est-il disponible ?
- Le cartouche modèle est-il disponible ?
Si une entrée manque, tu ne produis pas le plan — tu signales et tu t'arrêtes.


Étape 2 — Plan général coté
- Reprends la vue nettoyée (B-32) comme fond, sans redessiner l'empreinte.
- Reporte les éléments du livrable : semelles, poteaux, profilés, planchers, etc., selon {{type_livrable}}.
- Cote TOUS les éléments : positions, dimensions, entraxes, réservations.
- Numérote les éléments (F1, S1, P1, etc.) selon la nomenclature de la note de calcul.
- Cote les axes et trames, avec les points de calage (B-30).


Étape 3 — Coupes
- Coupe longitudinale et coupe transversale, à l'échelle 1/50 ou 1/20 selon complexité.
- Reprends les niveaux (NIV-02, NIV-03, NIV-05) et les épaisseurs.
- Représente les ferraillages ou les profilés de manière schématique mais juste (positions, sections).
- Cote les hauteurs, les enrobages, les positions des barres ou des profilés.


Étape 4 — Détails
- Détails à 1/20, 1/10 ou 1/5 sur les points singuliers : appuis, ferraillages singuliers, assemblages, jonctions.
- Chaque détail porte un titre, une échelle, une cote complète.
- Les détails renvoient aux repères du plan général.


Étape 5 — Nomenclature graphique
- Tableau intégré au plan : repère, désignation, section ou diamètre, longueur ou quantité, calque.
- Nomenclature détaillée et façonnage → B-62.


Étape 6 — Export DXF
- Structure le DXF avec les calques normalisés (annexe A) — un élément = un calque, pas de calque fourre-tout.
- Vérifie que l'export conserve : positions, cotations, textes, calques, échelles.
- Le DXF est nommé : {{type_livrable}}_EXE_{{indice}}.dxf.
- Test de relecture du DXF (obligatoire, verrou V13 et annexe O §6) : le fichier produit est RÉELLEMENT rouvert, les entités sont comptées par calque et comparées aux attendus du script de production ; les comptages sont consignés au journal OUT-03. Un test non exécuté ou « simulé » est une non-conformité : le livrable n'est pas produit.


Étape 7 — Export PNG et PDF
- PNG haute résolution pour diffusion rapide.
- PDF pour impression et archivage, avec cartouche et mentions.


Étape 8 — Indiçage et filigrane
- Indice du livrable : {{indice}} (A, B, C...), cohérent avec le RDL.
- Filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » sur tous les plans.
- Si la brique amont est en mode PARAMÉTRIQUE : filigrane supplémentaire « PROVISOIRE — EN ATTENTE DE [donnée] » et suffixe _P dans le nom de fichier.
- Mention du mode {{mode}} dans le cartouche.


Étape 9 — Consignation au RDL
- Ligne du RDL : livrable, indice, brique source, source utilisée, version du calage B-30, version de la vue nettoyée B-32, preuve de superposition B-31, vérification croisée B-33, date.


INTERDICTIONS
- Ne redessine AUCUN élément : tu reportes la géométrie et les éléments calculés par la brique amont sur la vue nettoyée (B-32). Tu ne réinventes rien.
- Ne produis aucun plan sans les trois formats (DXF, PNG, PDF) — un plan sans DXF est un plan qui devra être réexporté plus tard.
- Ne produis aucun plan sans cartouche complet : code projet, indice, date, échelle, mode, brique source, mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA ».
- Ne regroupe pas plusieurs éléments sur un seul calque : un élément = un calque normalisé.
- Ne produis pas un plan si une entrée manque (note de calcul, vue nettoyée, calage, cartouche).
- Ne produis pas un plan exécutable si la brique amont est PARAMÉTRIQUE : le plan est filigrané et suffixé _P.
- Ne dimensionne PAS la protection au feu : mention générique seule.
- Ne fusionne pas plusieurs livrables dans un seul plan : un plan = un type de livrable.
- N'utilise pas d'échelle hors convention (1/200, 1/100, 1/50, 1/20, 1/10, 1/5) sans justification.
- Ne produis pas un plan sans nomenclature graphique intégrée.


SORTIE
Pièce 1 — Plan général coté (PDF + PNG + DXF).
Pièce 2 — Coupes (PDF + PNG + DXF).
Pièce 3 — Détails (PDF + PNG + DXF).
Pièce 4 — Nomenclature graphique intégrée aux plans.
Pièce 5 — Fichiers DXF structurés (un par plan, nommés selon convention).
Pièce 6 — Consignation RDL (ligne du RDL complétée).


CRITÈRE D'ACCEPTATION
Le dossier graphique est accepté si :
- toutes les entrées (note de calcul, vue nettoyée B-32, calage B-30, cartouche) sont disponibles ;
- le plan général est coté (positions, dimensions, entraxes, réservations) ;
- les coupes sont produites avec niveaux et cotes ;
- les détails sont produits sur les points singuliers ;
- la nomenclature graphique est intégrée ;
- l'export DXF est structuré à calques normalisés (un élément = un calque) ;
- l'export DXF est testé (tous les calques attendus sont présents) ;
- les trois formats (DXF, PNG, PDF) sont produits ;
- le cartouche est complet : code projet, indice, date, échelle, mode, brique source, mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », mention « protection au feu adéquate à prévoir (hors lot GO) » ;
- si la brique amont est PARAMÉTRIQUE : filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » et suffixe _P ;
- le RDL est consigné.
Si un seul de ces onze points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}} (par COMPLET ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister. Remplacer aussi {{indice}}.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Brique unique (votre choix au tronçon 6) | Séparer plan et coupes conduit à des incohérences (une cote de plan qui ne correspond pas à la coupe). Une brique unique produit plan, coupes et détails ensemble, avec cohérence garantie |
| Export DXF intégré (votre choix au tronçon 6) | Un DXF exporté plus tard se désynchronise du plan. L'export au moment de la production garantit que DXF et plan sont identiques |
| « Ne redessine aucun élément » | Verrou V2 — le plan d'exécution est le report de la géométrie et des éléments calculés, pas un redessin. Un redessin introduit des erreurs invisibles : un mur dessiné légèrement décalé, une cote arrondie, une intersection mal recopiée |
| Convention de calques fixe (annexe A) | Sans convention, chaque plan invente ses calques. La convention permet à B-62 (nomenclature) et à un vérificateur externe de lire le DXF de manière prévisible |
| Trois formats (DXF, PNG, PDF) | Le DXF pour les outils, le PNG pour la diffusion rapide, le PDF pour l'archivage. Un seul format est toujours insuffisant |
| Cartouche avec mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » | Un plan sans cette mention finit par être exécuté sans visa. C'est la seule protection |
| Filigrane + suffixe _P si PARAMÉTRIQUE | Un plan PARAMÉTRIQUE sans filigrane est un plan qui sera exécuté — alors qu'il n'est pas exécutable |
| Test de relecture du DXF | Un DXF produit sans vérification peut manquer de calques ou d'éléments. Le test de relecture garantit que le DXF est utilisable |
| Nomenclature graphique intégrée | Un plan sans nomenclature oblige à ouvrir B-62 pour comprendre. La nomenclature graphique rend le plan autoportant |
| Consignation RDL | Sans RDL, un plan produit ne se retrouve pas dans le registre. C'est le RDL qui permet la mise à jour incrémentale (B-32) |
| « Ne fusionne pas plusieurs livrables » | Un plan qui contient plusieurs livrables (fondations + plancher) est un plan illisible et difficile à mettre à jour. Un plan = un type de livrable, c'est la règle de base |

Les trois types de plans produits — précision utile :

| Élément | Échelle | Contenu |
| --- | --- | --- |
| Plan général coté | 1/50 ou 1/100 | Vue en plan, cotations complètes, repères des éléments, réservations |
| Coupes | 1/50 ou 1/20 | Coupe longitudinale + transversale, niveaux, hauteurs, ferraillages ou profilés |
| Détails | 1/20, 1/10, 1/5 | Points singuliers : appuis, ferraillages singuliers, assemblages, jonctions |

Le piège du redessin : un modèle qui reçoit une note de calcul et une vue nettoyée a tendance à redessiner les éléments sur un fond vierge. C'est exactement ce qu'il faut interdire :
   * le redessin réintroduit des erreurs de position (le modèle place les éléments à des positions approximatives) ;
   * il perd le bénéfice du calage (B-30) et de la vue nettoyée (B-32) ;
   * il crée un décalage entre le plan et la source — que B-31 (preuve de superposition) et B-33 (vérification croisée) vont devoir détecter.
La règle « report, jamais redessin » est la seule qui garantit que le plan est fidèle à la source.
Le piège du cartouche : un modèle qui reçoit une note de calcul et une vue nettoyée a tendance à produire un plan sans cartouche complet, ou avec un cartouche générique. C'est exactement ce qu'il faut interdire :
   * sans cartouche complet, le plan n'est pas opposable (pas d'indice, pas de date, pas de mode) ;
   * sans mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le plan peut être exécuté sans visa ;
   * sans la mention du mode, un plan PARAMÉTRIQUE peut être exécuté alors qu'il n'est pas exécutable.
Le cartouche est la carte d'identité du plan — il doit être complet et exact.
Le piège du DXF : un modèle qui reçoit une note de calcul a tendance à produire un DXF avec un seul calque « 0 » (calque par défaut) qui contient tous les éléments. C'est exactement ce qu'il faut interdire :
   * un DXF avec un seul calque est inutilisable pour un outil aval (B-62 ne peut pas extraire la nomenclature par calque) ;
   * les éléments sont mélangés (murs, ferraillage, cotations) — impossibles à filtrer ;
   * le DXF n'est pas réutilisable pour une autre production (un plan de fondations et un plan de plancher ne peuvent pas être extraits du même DXF).
La convention de calques (annexe A) est la seule qui rend le DXF utilisable.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les valeurs utilisées dans les plans (matériaux, niveaux, positions) |
| B-20 (Conception structure GO) | Les plans de principe — B-60 les transforme en plans d'exécution cotés |
| B-25 (Stabilité globale, contreventement, joints) | Le schéma de contreventement, les joints de dilatation et les dispositions parasismiques à reporter |
| B-30 (Calage sur dxf/dwg source) | Le fichier recalé — les plans d'exécution s'appuient sur la vue nettoyée (elle-même issue du fichier calé) |
| B-32 (Vue nettoyée par livrable) | La vue nettoyée — B-60 produit le plan sur ce fond de plan |
| B-33 (Vérification croisée) | Le verdict de la vérification — B-60 ne produit le plan définitif qu'après un verdict favorable |
| B-34 (Synthèse des réservations) | Le plan de réservations et les renforcements à reporter |
| B-40 (Fondations superficielles) | La note et les plans produits — B-60 les reprend et les indice |
| B-41 (Fondations profondes) | Les plans de fondations — B-60 reprend les pieux existants (pas les pieux neufs, qui relèvent du spécialiste) |
| B-42 (Verticaux BA) | La note et les plans produits — B-60 les reprend et les indice |
| B-43 (Planchers et dallages) | La note et les plans produits — B-60 les reprend et les indice |
| B-44 (Charpente bois) | La note et les plans produits — B-60 les reprend et les indice |
| B-45 (Structure métallique) | La note et les plans produits — B-60 les reprend et les indice |
| B-46 (Maçonnerie : vérification) | La note et les plans produits — B-60 les reprend et les indice |
| B-47 (Escaliers) | La note et les plans produits — B-60 les reprend et les indice |
| B-48 (Prédalles et planchers préfabriqués) | La note et les plans produits — B-60 les reprend et les indice |
| B-49 (Linteaux et seuils) | La note et les plans produits — B-60 les reprend et les indice |
| B-50 (Assemblages et ancrages) | La note et les plans de détail — B-60 les reprend et les indice |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée et le façonnage |
| B-64 (Notice de synthèse) | Les plans produits — B-64 les cite dans la notice |
| B-70 (Auto-contrôle déclaré de synthèse) | Les plans produits — B-70 vérifie que chaque livrable a son plan |
| B-71 (Indiçage et supersession documentaire) | Les plans produits — B-71 les indice et gère la supersession |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-60 |
| --- | --- | --- |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE (via B-30) |
| GEO-01 à GEO-05 | Géométrie (emprise, axes, murs, poteaux, baies) | BLOQUANTE |
| NIV-02, NIV-05 | Niveaux de plancher, niveau fini du dallage | BLOQUANTE |
| LIV-01 à LIV-05 | Conventions de livrables (calques, échelles, formats, cartouche, unités) | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | BLOQUANTE (dès B-00) |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | BLOQUANTE (dès B-01) |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE si L / XL ou R+n |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | NON BLOQUANTE (à défaut : PA-xx) |

Variables produites
B-60 ne produit pas de variable au sens du dictionnaire : sa sortie est un dossier graphique (plans, coupes, détails, DXF, PNG, PDF) qui alimente B-62, B-64, B-31, B-33 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-02, GEO-01 à GEO-05, NIV-02, NIV-05, LIV-01 à LIV-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques DXF, échelles, formats, cartouche, unités | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE), en particulier C-02 (fusion B-61) et C-03 (intégration B-63) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-60, vous devez valider le cartouche et l'indice — c'est vous qui décidez du numéro d'indice (A, B, C) en fonction du cycle de révision. Un indice A est une première émission, un indice B est une révision, un indice C est une nouvelle révision. Le modèle propose, vous décidez.
Cas particulier — mode PARAMÉTRIQUE : si la brique amont est en mode PARAMÉTRIQUE (par exemple, SEC-01 manquante pour un plan de verticaux), B-60 s'appelle en mode PARAMÉTRIQUE :
   * le plan porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * le nom du fichier est suffixé _P ;
   * le plan n'est pas exécutable — il ne peut pas être diffusé à l'entreprise pour exécution ;
   * il peut être diffusé à la MOE/BC à titre informatif, avec mention explicite « provisoire, ne pas exécuter ».
Cas particulier — mode COMPLET : si la brique amont est en mode COMPLET, B-60 produit un plan exécutable — mais qui porte toujours la mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA ». Le plan n'est exécutable qu'après visa du BET, du BC, de la MOE ou de la MOA selon le contexte contractuel.
Cas particulier — plusieurs livrables du même type : si le projet comporte plusieurs livrables du même type (par exemple, deux plans de fondations pour deux zones différentes), B-60 produit un plan par livrable — pas un plan qui regroupe plusieurs zones. Chaque plan porte son propre numéro et son propre indice.
Cas particulier — plan de principe : si B-60 produit un plan de principe (à partir de B-20), le plan porte :
   * le filigrane « PRINCIPE — NE PAS EXÉCUTER » (au lieu de « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA ») ;
   * un indice P (P1, P2, P3... pour les versions successives) ;
   * la mention « Étude de conception — ne se substitue pas à l'EXE ».
Cas particulier — plan de détail d'assemblage : si B-60 produit un plan de détail d'assemblage (à partir de B-50), le plan porte :
   * les calques ASSEMBLAGE-DETAILS (détails à 1/20, 1/10, 1/5) ;
   * les calques ASSEMBLAGE-NOMENCLATURE (boulons, soudures, tiges, résines) ;
   * les renvois aux plans de coffrage et d'armatures des éléments assemblés.
Cas particulier — export DXF défaillant : si l'export DXF ne contient pas tous les calques attendus (par exemple, le calque -ACIER-INF est vide alors qu'il devrait contenir le ferraillage), B-60 le signale et s'arrête. Un DXF partiel est un DXF inutilisable pour B-62.
Cas particulier — échelle hors convention : si un plan nécessite une échelle hors convention (par exemple, 1/75 pour un détail), B-60 le signale dans le cartouche avec la mention « échelle exceptionnelle : [motif] ». L'échelle doit être justifiée, pas choisie par défaut.
Format de sortie attendu : six pièces distinctes (plan général, coupes, détails, nomenclature graphique, DXF, PNG + PDF). Les plans portent tous le filigrane, le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : le dossier B-60 est annexé au RDL (Registre des Livrables) — il documente la production du plan et permet la mise à jour incrémentale en cas de modification de source.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Loi d'airain graphique et vérité du titre.** Les plans d'exécution ne contiennent **aucune** cloison, isolation, doublage ni menuiserie de distribution : uniquement les porteurs, les ouvertures mécaniques, la trémie et l'escalier, la structure neuve et les réservations. Le titre d'un plan doit correspondre exactement à son contenu géométrique complet : un plan intitulé « fondations » qui ne porte pas toutes les fondations est refusé.

**Zéro collision de textes.** Chaque plan est contrôlé par script : `0` chevauchement de textes, `0` cote orpheline, `0` entité sur le calque `0`. Un plan non contrôlé n'est pas diffusé.

**Report, jamais redessin.** Le plan reporte la géométrie du fond `B-32` et les éléments calculés ; il ne redessine jamais l'empreinte architecturale et n'invente aucune position.
**[Fin de 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md]**

---

**[Début du fichier : 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md]**

Fichier 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md — CARNAC v3.0
________________


B-62 — NOMENCLATURE ET FAÇONNAGE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 5 — Synthèse et livrables d'exécution |
| Brique précédente | B-60 (Plans d'exécution) |
| Brique suivante | B-64 (Notice de synthèse), B-70 (Auto-contrôle de synthèse), B-71 (Indiçage) |
| Fréquence | À chaque livrable graphique produit par B-60 |
| Modes d'appel | COMPLET (B-60 produit en mode COMPLET) · PARTIEL-DÉCLARÉ (B-60 produit sous réserve) · PARAMÉTRIQUE (B-60 en mode PARAMÉTRIQUE : nomenclature partielle, non exécutable) |
| Paramètre d'appel | {{type_livrable}} = même paramètre que B-60 (FOND / VERT / PLANCHER / CHARPENTE / METAL / MACON / ESCALIER / PREDALLE / LINTEAU / ASSEMBLAGE) |
| Entrées lues | Plans B-60 (plan + coupes + détails + nomenclature graphique), note de calcul de la brique amont |
| Sortie unique | Nomenclature détaillée par élément + plan de façonnage des aciers (si BA) + tableau récapitulatif par calque + export tableur (CSV ou XLSX) pour la commande |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-60, quand les plans sont produits. B-62 est la brique qui transforme les plans en liste de commande — elle extrait les éléments dessinés, les quantifie, et produit le document qui permet au fournisseur de livrer les barres, profilés ou connecteurs.
Ce que vous fournissez à l'IA : les plans produits par B-60 (plan général, coupes, détails, nomenclature graphique) et la note de calcul de la brique amont. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * la nomenclature détaillée (repère, désignation, section, longueur, quantité) ;
   * le plan de façonnage des aciers BA (formes, cotes, longueurs développées) ;
   * le tableau récapitulatif par calque (longueurs cumulées, poids, quantités) ;
   * l'export tableur (CSV ou XLSX) ;
   * le rapport de cohérence (éléments dessinés vs éléments nommés).
Ce que B-62 produit — le périmètre exact :

| Élément | Nature |
| --- | --- |
| Nomenclature détaillée par élément | Repère, désignation, section ou diamètre, longueur ou quantité, calque source |
| Plan de façonnage (aciers BA) | Formes des barres, cotes de façonnage, longueurs développées, recouvrements |
| Tableau récapitulatif par calque | Total par calque : longueurs cumulées, poids, quantités |
| Export tableur | CSV ou XLSX, prêt pour commande auprès du fournisseur |
| Vérification de cohérence | Chaque élément dessiné sur B-60 figure dans la nomenclature, et réciproquement |

Ce que B-62 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Devis ou estimation financière | Hors périmètre CARNAC |
| Commande fournisseur | Hors périmètre CARNAC |
| Plans (déjà produits par B-60) | B-60 |
| Notice de synthèse | B-64 |
| Vérification de la cohérence plan ↔ plan | B-33 (déjà fait) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la nomenclature détaillée et le façonnage du livrable {{type_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir des plans B-60 et de la note de calcul de la brique amont. Produire l'export tableur correspondant.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


MÉTHODE — DANS CET ORDRE


Étape 1 — Vérification des entrées
- Plans B-60 disponibles (plan général, coupes, détails) ?
- Note de calcul de la brique amont disponible ?
- Nomenclature graphique intégrée aux plans disponible ?
Si une entrée manque, tu ne produis pas la nomenclature — tu signales et tu t'arrêtes.


Étape 2 — Extraction élément par élément
Pour chaque élément dessiné sur le plan (repères F1, S1, P1, etc.) :
- identifie sa nature (semelle, poteau, profilé, barre, etc.) ;
- identifie sa section ou son diamètre ;
- identifie sa longueur ou sa quantité ;
- identifie le calque source (FOND-ACIER-INF, VERT-ACIER-LONG, etc.).


Étape 3 — Nomenclature détaillée
Tableau par élément, puis tableau consolidé :
- repère (issu du plan) ;
- désignation (barre HA12, profilé HEB200, etc.) ;
- section ou diamètre ;
- longueur unitaire (mm) ou quantité ;
- nombre d'occurrences ;
- longueur totale (mm) ou quantité totale ;
- poids total (kg) si acier ;
- calque source.


Étape 4 — Plan de façonnage (aciers BA uniquement)
Pour chaque type de barre :
- forme (droite, équerre, U, cadre, épingle) ;
- cotes de façonnage (longueurs de chaque segment, angles) ;
- longueur développée ;
- longueur de recouvrement (si applicable) ;
- diamètre de mandrin (si cintrage) ;
- repère et quantité.


Étape 5 — Tableau récapitulatif par calque
Pour chaque calque (FOND-ACIER-INF, VERT-ACIER-LONG, etc.) :
- longueur cumulée ;
- poids cumulé (acier) ou volume (béton) ;
- quantité d'éléments.


Étape 6 — Vérification de cohérence
- Chaque élément dessiné sur B-60 figure dans la nomenclature.
- Chaque élément de la nomenclature figure sur B-60.
- Les quantités totales correspondent entre la nomenclature détaillée et le tableau récapitulatif.
Tout écart doit être signalé, pas corrigé par toi.


Étape 7 — Export tableur
- Format CSV (séparateur point-virgule, encodage UTF-8) ou XLSX.
- Colonnes : repère, désignation, section/diamètre, longueur unitaire, nombre, longueur totale, poids total, calque source.
- Une feuille par type (barres, profilés, connecteurs, etc.).


INTERDICTIONS
- Ne produis AUCUN devis ni estimation financière : hors périmètre CARNAC.
- Ne produis AUCUNE commande fournisseur : hors périmètre CARNAC.
- Ne redessine AUCUN élément : tu extrais des plans B-60.
- Ne fusionne pas plusieurs éléments dans une seule ligne : un repère = une ligne.
- Ne produis pas de nomenclature sans plan de façonnage (aciers BA) : les deux sont indissociables.
- Ne corrige pas un écart de cohérence : tu le signales, tu identifies la brique responsable (B-60 ou toi-même), tu renvoies.
- Ne produis pas de nomenclature exécutable si B-60 est en PARAMÉTRIQUE : nomenclature partielle et non exécutable, avec filigrane.


SORTIE
Pièce 1 — Nomenclature détaillée par élément.
Pièce 2 — Plan de façonnage (aciers BA).
Pièce 3 — Tableau récapitulatif par calque.
Pièce 4 — Export tableur (CSV ou XLSX).
Pièce 5 — Rapport de cohérence (éléments dessinés vs éléments nommés).


CRITÈRE D'ACCEPTATION
La nomenclature est acceptée si :
- chaque élément dessiné sur B-60 figure dans la nomenclature ;
- chaque élément de la nomenclature figure sur B-60 ;
- chaque ligne a un repère, une désignation, une section ou un diamètre, une longueur ou une quantité ;
- le plan de façonnage (aciers BA) est produit avec formes, cotes et longueurs développées ;
- le tableau récapitulatif par calque est produit ;
- l'export tableur est produit ;
- le rapport de cohérence est produit et ne présente aucun écart non signalé ;
- si B-60 est PARAMÉTRIQUE : nomenclature partielle, filigranée, non exécutable.
Si un seul de ces huit points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Nomenclature + façonnage indissociables | Une nomenclature sans façonnage est inutilisable en atelier. Le façonnage est le livrable qui permet au ferrailleur de plier les barres. Les séparer conduit à des allers-retours entre bureau et atelier |
| Un repère = une ligne | Un regroupement « HA12 : toutes les barres » ne permet pas de commander. Chaque repère est une ligne de commande potentielle — le fournisseur doit pouvoir identifier chaque type de barre |
| Plan de façonnage avec longueur développée | Un ferrailleur ne peut pas plier une barre sans sa longueur développée. La cote de façonnage et la longueur développée sont les deux données indispensables — sans elles, le ferrailleur improvise, et les barres ne rentrent pas dans le coffrage |
| Vérification de cohérence obligatoire | Un élément dessiné mais non nommé est un élément non commandé. Un élément nommé mais non dessiné est un élément en trop. Les deux sont des erreurs de production — et les deux se voient à l'exécution (barres manquantes ou en trop) |
| Export tableur | Sans export, la nomenclature est un tableau dans un PDF — inutilisable pour la commande. Le CSV/XLSX est le format d'échange avec le fournisseur |
| « Ne corrige pas un écart de cohérence » | Si le plan B-60 et la nomenclature divergent, c'est B-60 qui est faux (ou la nomenclature, mais c'est plus rare). C'est à la brique responsable de corriger — sinon on ne sait plus quel document fait foi |
| Nomenclature non exécutable si B-60 PARAMÉTRIQUE | Une nomenclature partielle qui ne porte pas de filigrane est une nomenclature qui sera commandée — et les barres seront coupées avant que la donnée manquante n'arrive. Le filigrane est la seule protection |
| « Ne produis aucun devis ni commande » | La nomenclature est un document technique, pas un document commercial. Le devis et la commande relèvent de l'économiste et du service achats — pas du bureau d'études |
| Rapport de cohérence | Le rapport est le document qui prouve que la vérification a été faite. Sans lui, la cohérence est une affirmation — et les erreurs ne sont pas détectées |

Les éléments de la nomenclature — précision utile :

| Élément | Unité | Exemple |
| --- | --- | --- |
| Repère | — | F1, S1, P1, HA12-01 |
| Désignation | — | Semelle filante, poteau BA, barre HA12, HEB200 |
| Section / diamètre | mm | HA12, HEB200, 140×140×8 |
| Longueur unitaire | mm | 3200, 4500 |
| Nombre | — | 4, 12, 28 |
| Longueur totale | mm | 12800, 54000 |
| Poids | kg | 45,3, 320,7 |
| Calque source | — | FOND-ACIER-INF, VERT-ACIER-LONG |

Le piège du façonnage : un modèle qui reçoit un plan de ferraillage a tendance à produire une nomenclature sans façonnage (juste les barres, sans les formes). C'est insuffisant :
   * le ferrailleur ne peut pas plier une barre sans sa forme (droite, équerre, U, cadre, épingle) ;
   * il ne peut pas plier sans la longueur développée (longueur totale dépliée) ;
   * il ne peut pas plier sans le diamètre de mandrin (si cintrage).
Une nomenclature sans façonnage est une nomenclature qui oblige le ferrailleur à interpréter le plan — et qui produit des barres fausses.
Le piège de la cohérence : un modèle qui reçoit un plan de ferraillage et une note de calcul a tendance à :
   * soit recopier le plan sans vérifier la cohérence avec la note (le plan peut être faux) ;
   * soit corriger le plan (ce qui est le rôle de B-60, pas de B-62).
Les deux sont faux :
   * recopier sans vérifier, c'est produire une nomenclature qui peut être fausse ;
   * corriger le plan, c'est produire une nomenclature qui ne correspond plus au plan.
La seule réponse correcte est : vérifier la cohérence, signaler les écarts, renvoyer à B-60 pour correction.
Le piège du mode PARAMÉTRIQUE : si B-60 a produit un plan PARAMÉTRIQUE (par exemple, un plan de verticaux avec SEC-01 manquante), B-62 produit une nomenclature partielle :
   * les éléments dont les dimensions sont connues sont nommés ;
   * les éléments dont les dimensions dépendent de la donnée manquante sont omis ou marqués « EN ATTENTE » ;
   * la nomenclature porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * elle ne peut pas être commandée — les barres manquantes seront commandées quand la donnée arrivera.
Une nomenclature PARAMÉTRIQUE qui ne porte pas de filigrane est une nomenclature qui sera commandée — et les barres seront coupées avant que la donnée n'arrive.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-30 (Calage sur dxf/dwg source) | Le fichier recalé — B-62 utilise le calage pour identifier les positions si nécessaire |
| B-32 (Vue nettoyée par livrable) | La vue nettoyée — B-62 s'appuie sur cette vue pour vérifier la cohérence |
| B-40 (Fondations superficielles) | Les plans — B-62 en extrait la nomenclature détaillée |
| B-41 (Fondations profondes) | La note de calcul — B-62 vérifie la cohérence entre les quantités du plan et celles de la note |
| B-42 (Verticaux BA) | Les plans — B-62 en extrait la nomenclature détaillée (barres, cadres) |
| B-43 (Planchers et dallages) | Les plans — B-62 en extrait la nomenclature détaillée (barres, treillis, solives) |
| B-44 (Charpente bois) | Les plans — B-62 en extrait la nomenclature détaillée (sections, boulons, sabots) |
| B-45 (Structure métallique) | Les plans — B-62 en extrait la nomenclature détaillée (profilés, platines) |
| B-46 (Maçonnerie : vérification) | Les plans — B-62 en extrait la nomenclature détaillée (blocs, barres, raidisseurs) |
| B-47 (Escaliers) | Les plans — B-62 en extrait la nomenclature détaillée (barres, chapeaux, renforts) |
| B-48 (Prédalles et planchers préfabriqués) | Les plans — B-62 en extrait la nomenclature détaillée (prédalles, armatures de connexion) |
| B-49 (Linteaux et seuils) | Les plans — B-62 en extrait la nomenclature détaillée (barres, profilés) |
| B-50 (Assemblages et ancrages) | Les plans — B-62 en extrait la nomenclature détaillée (boulons, soudures, tiges, résines) |
| B-60 (Plans d'exécution) | Les plans — B-62 en extrait la nomenclature détaillée et le façonnage |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-64 (Notice de synthèse) | La nomenclature — B-64 la cite dans la notice |
| B-70 (Auto-contrôle déclaré de synthèse) | Le rapport de cohérence — B-70 vérifie que la cohérence a été faite |
| B-71 (Indiçage et supersession documentaire) | La nomenclature produite — B-71 l'indice et gère la supersession |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-62 |
| --- | --- | --- |
| MAT-01 à MAT-04 | Matériaux BA | BLOQUANTE (pour nomenclature BA) |
| MAT-05 | Nuance d'acier métallique | BLOQUANTE (pour nomenclature métallique) |
| MAT-06 | Classe de bois | BLOQUANTE (pour nomenclature bois) |
| MAT-09 à MAT-11 | Maçonnerie (blocs, mortier) | BLOQUANTE (pour nomenclature maçonnerie) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |

Variables produites
B-62 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (nomenclature + façonnage + export tableur + rapport de cohérence) qui alimente B-64, B-70, B-71 et le service achats.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-11, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nomenclature type, unités, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-62, vous devez valider la nomenclature avant transmission au fournisseur. Une erreur de quantité commandée coûte cher — soit en sur-commande (coût), soit en sous-commande (retard de chantier). Le modèle propose, vous validez.
Cas particulier — mode PARAMÉTRIQUE : si B-60 est en mode PARAMÉTRIQUE, B-62 produit une nomenclature partielle :
   * les éléments dont les dimensions sont connues sont nommés ;
   * les éléments dont les dimensions dépendent de la donnée manquante sont marqués « EN ATTENTE DE [donnée] » ;
   * la nomenclature porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * elle ne peut pas être commandée.
Le chef de chantier doit être informé que la nomenclature n'est pas complète — et que les barres manquantes seront commandées quand la donnée arrivera.
Cas particulier — nomenclature d'aciers BA : la nomenclature d'aciers BA comporte :
   * la liste des barres par diamètre et par repère ;
   * le plan de façonnage (formes, cotes, longueurs développées) ;
   * le tableau récapitulatif par calque (longueurs cumulées, poids).
Le plan de façonnage est indissociable de la nomenclature — c'est le document qui permet au ferrailleur de plier les barres.
Cas particulier — nomenclature de profilés métalliques : la nomenclature de profilés métalliques comporte :
   * la liste des profilés par type (HEA, HEB, IPE, UPE, tubes) ;
   * les longueurs et quantités ;
   * les poids cumulés ;
   * les connecteurs (boulons, soudures, platines) — renvoi à B-50 pour le calcul, B-62 pour la nomenclature.
La nomenclature métallique est souvent plus courte que la nomenclature BA — mais elle est aussi importante pour la commande.
Cas particulier — nomenclature de maçonnerie : la nomenclature de maçonnerie comporte :
   * les blocs (classe, dimensions, quantités) ;
   * le mortier (classe, volume) ;
   * les chaînages (section, longueur) ;
   * les raidisseurs (section, longueur) ;
   * les armatures de maçonnerie armée (ratios, longueurs).
La nomenclature de maçonnerie est souvent moins détaillée que la nomenclature BA — mais elle doit être complète pour la commande.
Cas particulier — écart entre plan et note : si un écart existe entre le plan B-60 et la note de calcul (par exemple, une section de barre différente), B-62 le signale dans son rapport de cohérence. C'est B-60 ou la brique amont qui doit corriger — pas B-62 qui doit arbitrer.
Cas particulier — export tableur : l'export tableur (CSV ou XLSX) comporte une feuille par type d'élément (barres, profilés, connecteurs, blocs). Chaque feuille est triée par repère, avec les colonnes standardisées. Le service achats peut utiliser directement cet export pour la commande.
Format de sortie attendu : cinq pièces distinctes (nomenclature détaillée, plan de façonnage, tableau récapitulatif, export tableur, rapport de cohérence). La nomenclature porte le filigrane si B-60 est en mode PARAMÉTRIQUE.
Consignation : la nomenclature B-62 est annexée au RDL (Registre des Livrables) — elle documente les quantités produites et permet la mise à jour incrémentale en cas de modification de source.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Nomenclature issue du DXF contrôlé.** La nomenclature est extraite par script des calques normalisés du DXF effectivement produit et relu (`V13`), jamais ressaisie. Toute divergence entre quantités extraites et quantités annoncées dans la note est un écart bloquant.
**[Fin de 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md]**

---

**[Début du fichier : 07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md]**

Fichier 07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md — CARNAC v3.0
________________


B-64 — NOTICE DE SYNTHÈSE DU LIVRABLE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 5 — Synthèse et livrables d'exécution |
| Brique précédente | B-60 (Plans d'exécution), B-62 (Nomenclature) |
| Brique suivante | B-70 (Auto-contrôle de synthèse), B-71 (Indiçage) |
| Fréquence | Une fois par livrable complet (à la fin de la chaîne : après B-60 et B-62) |
| Modes d'appel | COMPLET (toutes les briques amont en COMPLET) · PARTIEL-DÉCLARÉ (briques amont en modes dégradés, déclarées) · PARAMÉTRIQUE (briques amont en PARAMÉTRIQUE : la notice est filigranée) |
| Paramètre d'appel | {{type_livrable}} = même paramètre que B-60 (FOND / VERT / PLANCHER / CHARPENTE / METAL / MACON / ESCALIER / PREDALLE / LINTEAU / ASSEMBLAGE) |
| Entrées lues | Note de calcul de la brique amont, plans B-60, nomenclature B-62, RDL, RDR (décisions et verrous) |
| Sortie unique | Notice de synthèse (2 à 4 pages max) : présentation du livrable, hypothèses retenues, points de principe, points à lever, réserves, visas requis, indiçage |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-60 et B-62, quand les plans et la nomenclature sont produits. B-64 est la brique qui transforme les documents techniques en document de synthèse lisible — elle est destinée à un lecteur (MOE, BC, entreprise) qui doit comprendre le livrable sans ouvrir la note de calcul complète.
Ce que vous fournissez à l'IA : la note de calcul de la brique amont, les plans B-60, la nomenclature B-62, le RDL (registre des livrables), le RDR (décisions et verrous). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * la présentation du livrable (objet, périmètre, pièces jointes) ;
   * les hypothèses retenues (H-xx actives, avec statut) ;
   * les points de principe (ce qui relève d'un choix de conception) ;
   * les points à lever (données manquantes, décisions à prendre, réserves) ;
   * les réserves et limites ;
   * les visas requis ;
   * l'indiçage et la supersession.
Ce que B-64 produit — le périmètre exact :

| Élément | Nature |
| --- | --- |
| Présentation du livrable | Objet, périmètre, pièces jointes |
| Hypothèses retenues | Liste des hypothèses H-xx actives et de leur statut |
| Points de principe | Ce qui relève d'un choix de conception, non d'un calcul |
| Points à lever | Ce qui reste à confirmer ou à décider (verrous, réserves) |
| Réserves et limites | Limites de la note de calcul, points hors périmètre |
| Visas requis | Qui doit viser le livrable avant exécution |
| Indiçage et supersession | Indice du livrable, documents supersédés |

Ce que B-64 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Note de calcul | Brique amont (B-40 à B-50) |
| Plans | B-60 |
| Nomenclature | B-62 |
| Auto-contrôle déclaré | Brique amont (chaque fiche de calcul contient son propre auto-contrôle) |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

La raison d'être de B-64 : sans notice de synthèse, un lecteur (MOE, BC) doit ouvrir toutes les pièces du livrable pour comprendre :
   * ce que couvre le livrable ;
   * quelles hypothèses sont prises ;
   * quels points restent à lever ;
   * quels visas sont requis.
La notice de synthèse est le document d'entrée du livrable — elle permet au lecteur de décider s'il doit approfondir, ou si le livrable est suffisamment clair.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : rédiger la notice de synthèse du livrable {{type_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir de la note de calcul de la brique amont, des plans B-60, de la nomenclature B-62, du RDL et du RDR. La notice tient en 2 à 4 pages maximum et permet à un lecteur de comprendre le livrable sans ouvrir la note de calcul.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


MÉTHODE — DANS CET ORDRE


Étape 1 — Présentation du livrable
- Objet : ce que le livrable couvre (fondations / verticaux / plancher / charpente / etc.) ;
- Périmètre : ce qui est inclus dans le livrable ;
- Pièces jointes : liste des notes de calcul, plans, nomenclatures associés ;
- Brique source et indice du livrable ;
- Date.


Étape 2 — Hypothèses retenues
- Liste des hypothèses H-xx actives (issues de B-22) ;
- Statut de chaque hypothèse (À CONFIRMER / CONFIRMÉE) ;
- Si des hypothèses sont À CONFIRMER, mention explicite : « livrable établi sous hypothèses H-xx à confirmer ».


Étape 3 — Points de principe
- Ce qui relève d'un choix de conception et non d'un calcul ;
- Justification de chaque choix en une phrase ;
- Renvoi aux documents qui détaillent (B-20 pour la conception, note de calcul pour les calculs).


Étape 4 — Points à lever
- Liste des points ouverts (issus du RDR) : données manquantes, décisions à prendre, réserves ;
- Pour chaque point : nature, conséquence sur le livrable, destinataire, échéance.


Étape 5 — Réserves et limites
- Limites de la note de calcul (ce qui n'est pas couvert : existant non sondé, données manquantes, éléments hors périmètre) ;
- Réserves sur les hypothèses ;
- Mention « protection au feu adéquate à prévoir (hors lot GO) ».


Étape 6 — Visas requis
- Qui doit viser le livrable avant exécution : BET structure, bureau de contrôle, MOE, MOA ;
- Nature du visa (visa de conception, visa d'exécution, visa de conformité) ;
- Mention obligatoire : « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA ».


Étape 7 — Indiçage et supersession
- Indice du livrable (A, B, C...) ;
- Documents supersédés (le cas échéant) : indice précédent, date, motif de révision ;
- Mention « ce livrable remplace et annule l'indice précédent ».


INTERDICTIONS
- Ne produis pas une notice de plus de 4 pages : c'est une synthèse, pas une duplication de la note de calcul.
- Ne recopie pas la note de calcul : tu synthétises.
- N'omets aucun point à lever : un point à lever omis est un point qui sera oublié à l'exécution.
- Ne mentionne pas de visas non requis : seuls les visas effectivement nécessaires sont listés.
- Ne produis pas une notice qui ne correspond pas aux plans et nomenclatures produits (cohérence obligatoire).
- Ne produis pas de notice exécutable si le livrable est en mode PARAMÉTRIQUE : la notice est filigranée et suffixée _P.


SORTIE
Pièce unique — Notice de synthèse (2 à 4 pages), structurée en sections 1 à 7.


CRITÈRE D'ACCEPTATION
La notice est acceptée si :
- toutes les entrées (note de calcul, plans, nomenclature, RDL, RDR) sont disponibles et cohérentes ;
- la présentation du livrable identifie l'objet, le périmètre et les pièces jointes ;
- les hypothèses actives sont listées avec leur statut ;
- les points de principe sont identifiés avec justification ;
- les points à lever sont listés avec destinataire et échéance ;
- les limites et réserves sont explicites ;
- les visas requis sont identifiés ;
- l'indiçage et la supersession sont documentés ;
- la mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » figure en tête ;
- la mention « protection au feu adéquate à prévoir (hors lot GO) » figure ;
- la notice tient en 4 pages maximum ;
- si le livrable est PARAMÉTRIQUE : notice filigranée et suffixée _P.
Si un seul de ces douze points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| 4 pages maximum | Une notice de synthèse qui dépasse 4 pages n'est plus une synthèse — c'est une duplication de la note de calcul. Le lecteur (MOE, BC) ne la lit plus — et la notice perd sa fonction |
| Hypothèses avec statut | Une hypothèse « confirmée » et une hypothèse « à confirmer » n'ont pas le même poids. Le statut doit figurer dans la notice — sinon le lecteur croit que tout est confirmé |
| Points à lever avec destinataire et échéance | Un point à lever sans destinataire ne se lève jamais. Sans échéance, il se lève trop tard. La notice est le document qui rend les points à lever actionnables |
| Visas requis explicites | Un livrable sans visa explicite finit par être exécuté sans visa. La notice est le document qui rappelle les visas nécessaires — et qui vous protège si l'exécution commence sans visa |
| Indiçage et supersession | Un livrable indice C qui ne dit pas qu'il remplace l'indice B crée de la confusion (quel document est en vigueur ?). La supersession est indispensable pour la gestion documentaire |
| Mention « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » | La notice est le dernier document lu avant exécution. C'est là que la mention a le plus d'impact |
| Filigrane si PARAMÉTRIQUE | Une notice qui accompagne un livrable PARAMÉTRIQUE sans filigrane donne l'impression que le livrable est exécutable. Le filigrane protège |
| Cohérence avec plans et nomenclature | Une notice qui cite des plans ou des nomenclatures qui ne correspondent pas (parce que B-60 ou B-62 ont été modifiés entre-temps) est une notice fausse. La cohérence est vérifiée à l'étape 1 |
| « Ne recopie pas la note de calcul » | Une notice qui recopie la note de calcul est une notice inutile — elle ne fait que dupliquer un document qui existe déjà. La notice doit synthétiser, pas dupliquer |
| « N'omets aucun point à lever » | Un point à lever omis est un point qui sera oublié à l'exécution. La notice est le document qui rassemble tous les points à lever en un seul endroit lisible — c'est sa fonction principale |
| « Ne mentionne pas de visas non requis » | Une notice qui liste des visas non requis crée de la confusion (qui doit viser ?). Seuls les visas effectivement nécessaires doivent être listés — c'est votre appréciation du contexte contractuel qui fait foi |
| Filigrane + suffixe _P | Une notice PARAMÉTRIQUE qui accompagne un livrable PARAMÉTRIQUE doit porter le filigrane — sinon elle est diffusée comme une notice normale, et le lecteur croit que le livrable est exécutable |

Les sept sections de la notice — précision utile :

| Section | Objet | Lecteur cible |
| --- | --- | --- |
| 1. Présentation du livrable | Objet, périmètre, pièces jointes, indice | Tous |
| 2. Hypothèses retenues | H-xx actives, statut | MOE, BET, BC |
| 3. Points de principe | Choix de conception, justification | MOE, BET |
| 4. Points à lever | Données manquantes, décisions à prendre | MOE, MOA, BET |
| 5. Réserves et limites | Ce qui n'est pas couvert, ce qui reste à confirmer | Tous |
| 6. Visas requis | Qui doit viser, nature du visa | MOE, BC, BET |
| 7. Indiçage et supersession | Indice, documents supersédés | Tous |

Le piège de la notice trop longue : un modèle qui reçoit une note de calcul, des plans et une nomenclature a tendance à produire une notice qui récapitule tout. C'est exactement ce qu'il faut interdire :
   * une notice trop longue n'est plus lue ;
   * elle duplique les documents existants (note, plans, nomenclature) ;
   * elle ajoute du volume sans apporter d'information nouvelle.
La notice doit synthétiser — c'est-à-dire extraire l'essentiel (hypothèses, points de principe, points à lever, visas) pour permettre au lecteur de décider s'il doit approfondir.
Le piège des points à lever : un modèle a tendance à minimiser les points à lever (par exemple, « quelques points mineurs à lever ») pour présenter un livrable « propre ». C'est exactement ce qu'il faut interdire :
   * un point à lever omis est un point qui sera oublié à l'exécution ;
   * la notice est le document qui rassemble les points à lever en un seul endroit lisible ;
   * c'est ce qui permet à la MOE/BC de décider si le livrable est suffisamment mûr pour être exécuté.
La notice doit lister les points à lever, pas les minimiser.
Le piège de la cohérence : un modèle a tendance à produire la notice sans vérifier que les plans et nomenclatures cités sont bien ceux qui ont été produits. C'est faux :
   * si B-60 a été modifié après B-62 (par exemple, une correction de plan), la nomenclature ne correspond plus ;
   * si B-62 a été modifié après B-60 (par exemple, une correction de quantité), la notice doit en tenir compte ;
   * la notice doit vérifier que les documents cités sont cohérents entre eux — c'est la première vérification de la notice (étape 1).
Une notice incohérente est une notice qui trompe le lecteur — et qui vous engage.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions, réserves et verrous — B-64 les intègre dans les points à lever |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — B-64 les liste avec leur statut |
| B-34 (Synthèse des réservations) | La liste des réservations et des Points d'Arrêt |
| B-40 (Fondations superficielles) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-41 (Fondations profondes) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-42 (Verticaux BA) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-43 (Planchers et dallages) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-44 (Charpente bois) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-45 (Structure métallique) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-46 (Maçonnerie : vérification) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-47 (Escaliers) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-48 (Prédalles et planchers préfabriqués) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-49 (Linteaux et seuils) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-50 (Assemblages et ancrages) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-60 (Plans d'exécution) | Les plans produits — B-64 les cite dans la notice |
| B-62 (Nomenclature et façonnage) | La nomenclature — B-64 la cite dans la notice |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-70 (Auto-contrôle déclaré de synthèse) | La notice — B-70 vérifie que chaque livrable a sa notice |
| B-71 (Indiçage et supersession documentaire) | La notice — B-71 l'indice avec le livrable |
| B-72 (Journal de clôture) | La notice — B-72 la cite dans la liste des livrables produits |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-64 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| ID-05 | Indice du dossier en vigueur | BLOQUANTE (pour l'indiçage et la supersession) |
| DEC-02 | Décisions inscrites au RDR | BLOQUANTE (pour les visas requis et les décisions appliquées) |
| DEC-03 | Verrous ouverts | BLOQUANTE (pour les points à lever) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |

Variables produites
B-64 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (notice de synthèse) qui alimente B-70, B-71, B-72 et les destinataires externes.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, ID-05, DEC-02, DEC-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-64, vous devez valider les visas requis — c'est vous qui savez qui doit viser (BC, BET, MOE) selon le contexte contractuel. Un livrable qui n'est pas visé par le bon tiers peut être refusé à la réception — ou engager votre responsabilité en cas de problème.
Cas particulier — mode PARAMÉTRIQUE : si le livrable est en mode PARAMÉTRIQUE (par exemple, SEC-01 manquante pour un livrable de verticaux), la notice porte :
   * le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * le nom du fichier est suffixé _P ;
   * la mention « livrable provisoire, ne pas exécuter » en tête de notice ;
   * les points à lever sont exhaustifs — y compris la donnée manquante qui bloque l'exécution.
La notice PARAMÉTRIQUE peut être diffusée à la MOE/BC à titre informatif, avec mention explicite « provisoire, ne pas exécuter ».
Cas particulier — livrable avec plusieurs indices : si le livrable a plusieurs indices successifs (par exemple, A → B → C), la notice porte :
   * l'indice en vigueur (C) ;
   * les indices supersédés (A, B) avec leurs dates ;
   * le motif des révisions (correction d'erreur, modification de conception, etc.) ;
   * la mention « ce livrable remplace et annule les indices A et B ».
Sans cette traçabilité, l'entreprise peut exécuter sur un indice périmé — c'est un risque majeur.
Cas particulier — points à lever nombreux : si le livrable a beaucoup de points à lever (par exemple, 10 ou plus), la notice doit :
   * les hiérarchiser (critiques / importants / de suivi) ;
   * identifier les plus critiques (ceux qui bloquent l'exécution) ;
   * recommander une décision (attendre, exécuter partiellement, exécuter sous réserve).
La notice n'est pas seulement un constat — c'est un outil de décision pour la MOE/BC.
Cas particulier — visas déjà obtenus : si le livrable a déjà été visé (par exemple, le BC a visé une version antérieure), la notice porte :
   * les visas déjà obtenus (avec date) ;
   * les visas restant à obtenir ;
   * la mention « les visas de la version antérieure ne valent pas pour l'indice actuel ».
Un visa antérieur ne vaut pas pour un nouvel indice — c'est une règle de gestion documentaire qui évite les confusions.
Cas particulier — livrable d'exécution vs livrable de principe : si le livrable est un plan de principe (produit par B-20), la notice porte :
   * la mention « Étude de conception — ne se substitue pas à l'EXE » ;
   * les points à faire valider par un tiers (BET, BC) avant de passer à l'exécution ;
   * les visas requis (visa de conception, pas visa d'exécution).
Un plan de principe n'est pas un plan d'exécution — la notice doit le préciser.
Cas particulier — livrable avec écart de contrôle croisé : si B-50 (assemblages) a identifié un écart de contrôle croisé (par exemple, un ancrage qui ne rentre pas dans la semelle), la notice porte :
   * l'écart identifié ;
   * la brique responsable (B-40 qui doit s'agrandir, ou B-42 qui doit revoir ses barres) ;
   * l'action en cours (correction de B-40 en cours, décision en attente).
Un livrable avec écart de contrôle croisé non traité n'est pas exécutable — la notice doit le signaler.
Format de sortie attendu : notice unique (2 à 4 pages), structurée en sections 1 à 7, avec les mentions obligatoires. La notice porte le filigrane si le livrable est en mode PARAMÉTRIQUE.
Consignation : la notice B-64 est annexée au livrable et consignée au RDL — elle fait partie du dossier de livraison, avec les plans et la nomenclature.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Notice de synthèse et points d'arrêt.** La notice reprend les hypothèses `H-xx` actives, les prescriptions `ENC`, les Points d'Arrêt `PA-xx`, le mode d'exécution, les réservations `B-34` et les limites de mission. Elle constitue la pièce contractuelle de référence en cas d'écart d'exécution.
**[Fin de 07_PHASE_5_LIVRABLES/B-64_Notice_Synthese.md]**

---

**[Début du fichier : 05_PHASE_3_CALAGE/B-33_Verification_Croisee.md]**

Fichier 05_PHASE_3_CALAGE/B-33_Verification_Croisee.md — CARNAC v3.0
________________


B-33 — VÉRIFICATION CROISÉE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 6 — Vérification croisée et clôture |
| Brique précédente | B-31 (Preuve de superposition), B-32 (Vue nettoyée) |
| Brique suivante | B-60 (Plans d'exécution), B-70 (Auto-contrôle de synthèse) |
| Fréquence | À chaque livrable graphique + en fin de projet (élargissement à l'ensemble des livrables) |
| Modes d'appel | COMPLET uniquement (la vérification est un contrôle, elle ne se fait pas en mode dégradé) |
| Entrées lues | Livrable graphique produit, fichier source calé (B-30), vue nettoyée (B-32), autres livrables déjà produits (via le RDL) |
| Sortie unique | Rapport de vérification en deux sections distinctes : (1) plan ↔ source, (2) plan ↔ plan |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * à chaque livrable graphique produit, après B-31 et B-32 ;
   * en fin de projet, avec élargissement de la section 2 à l'ensemble des livrables.
Ce que vous fournissez à l'IA : le livrable produit, le fichier source calé (B-30), la vue nettoyée (B-32), et la liste des livrables déjà produits (via le RDL). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{code_livrable}}.
Ce que vous validez à la sortie :
   * les écarts section 1 (plan ↔ source) ;
   * les écarts section 2 (plan ↔ plan) ;
   * la brique à corriger pour chaque écart ;
   * le verdict global du livrable (validé / validé sous réserve / à corriger).
Ce que B-33 apporte de spécifique — les deux sections :

| Section | Objet | Ce qu'elle détecte |
| --- | --- | --- |
| Section 1 — Plan ↔ source | Le livrable est-il cohérent avec le fichier source calé (B-30) et avec la vue nettoyée (B-32) ? | Décalage résiduel, cote fausse, élément omis, position erronée par rapport au fond |
| Section 2 — Plan ↔ plan | Le livrable est-il cohérent avec les autres livrables déjà produits ? | Poteau qui bouge d'un plan à l'autre, baie figurée sur un livrable mais absente sur l'autre, profilé dessiné sur le PH mais sans appui sur le plan de fondations |

La règle la plus importante : B-33 ne corrige aucun écart. Elle signale, identifie la brique à corriger, et renvoie la correction. Une vérification qui corrige n'est plus une vérification — c'est une correction non tracée.
Pourquoi deux sections et pas une : la cohérence verticale (plan ↔ source) et la cohérence horizontale (plan ↔ plan) ont des causes différentes et des remèdes différents. Les fusionner brouille le diagnostic :
   * un écart vertical (plan ↔ source) vient d'une erreur de production sur le livrable, ou d'un calage faux ;
   * un écart horizontal (plan ↔ plan) vient d'une incohérence entre deux livrables — par exemple, un poteau a été déplacé sur un livrable mais pas sur l'autre, ou une baie a été oubliée sur un livrable. Seule une vérification croisée détecte cette catégorie d'erreur.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire le rapport de vérification croisée du livrable graphique {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}, en DEUX sections distinctes :
- Section 1 : cohérence plan ↔ source (le livrable est-il conforme au fichier source calé et à la vue nettoyée ?) ;
- Section 2 : cohérence plan ↔ plan (le livrable est-il cohérent avec les autres livrables déjà produits ?).


SECTION 1 — PLAN ↔ SOURCE
1. Compare le livrable et le fichier source calé (B-30) sur : positions des appuis, cotes, ouvertures, épaisseurs de murs, axes et trames.
2. Compare le livrable et la vue nettoyée (B-32) sur : les éléments conservés dans la vue sont-ils bien représentés sur le livrable ? Les éléments ajoutés sont-ils sur les bons appuis ?
3. Produis un tableau : élément | valeur source | valeur livrable | écart | verdict.


SECTION 2 — PLAN ↔ PLAN
1. Liste les livrables déjà produits et consignés au RDL (hors celui-ci).
2. Pour chaque livrable antérieur, compare avec le livrable actuel sur les éléments communs :
   - positions des poteaux, profilés, semelles ;
   - niveaux et hauteurs ;
   - ouvertures et trémies ;
   - axes et trames.
3. Produis un tableau : élément commun | valeur dans le livrable antérieur | valeur dans le livrable actuel | écart | verdict | brique à corriger.
4. En fin de projet (appel de clôture), élargis la section 2 à l'ensemble des livrables et produis une synthèse globale de cohérence.


INTERDICTIONS
- Ne produis pas une seule section : les deux sont obligatoires (sauf en clôture, où la section 2 est élargie).
- Ne compare pas le livrable à une source non calée ou à une vue nettoyée d'un autre livrable.
- Ne corrige AUCUN écart dans la vérification : tu le signales, tu identifies la brique à corriger.
- Ne déclare pas un livrable « cohérent » sans comparaison chiffrée élément par élément.
- Ne fusionne pas les deux sections : une cohérence plan ↔ source (verticale) et une cohérence plan ↔ plan (horizontale) sont deux contrôles distincts, avec des causes distinctes.


SORTIE
Pièce 1 — Rapport section 1 (plan ↔ source)
Tableau de vérification élément par élément + verdict global : conforme / conforme avec réserves / à corriger.


Pièce 2 — Rapport section 2 (plan ↔ plan)
Tableau de vérification élément par élément + verdict global : cohérent / cohérent avec réserves / incohérent.


Pièce 3 — Synthèse
Nombre d'écarts section 1 | Nombre d'écarts section 2 | Verdict global du livrable (validé / validé sous réserve / à corriger) | Brique(s) à reprendre | Inscription au RDL.


CRITÈRE D'ACCEPTATION
La vérification est acceptée si :
- les deux sections sont produites (sauf clôture, section 2 élargie) ;
- chaque élément a une comparaison chiffrée (pas un simple « conforme ») ;
- les écarts sont signalés sans être corrigés ;
- la synthèse identifie la brique à reprendre pour chaque écart ;
- le RDL est mis à jour avec le verdict global.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{code_livrable}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Deux sections distinctes | Votre choix — la cohérence verticale (plan ↔ source) et la cohérence horizontale (plan ↔ plan) ont des causes différentes et des remèdes différents. Les fusionner brouille le diagnostic : on ne sait plus si l'écart vient du livrable (vertical) ou d'une incohérence entre livrables (horizontal) |
| Section 2 obligatoire à chaque livrable | C'est la cohérence inter-livrables qui détecte les poteaux qui « bougent » d'un plan à l'autre, les baies oubliées, les profilés sans appui. Une vérification brique par brique ne peut pas la détecter — chaque brique vérifie son périmètre, pas les interfaces avec les autres briques |
| RDL comme source des livrables à comparer | Sans RDL, la section 2 ne sait pas quels livrables existent, et compare au hasard. Le RDL est la seule liste fiable des livrables produits, avec leur indice et leur date |
| « Ne corrige aucun écart » | Une vérification qui corrige n'est plus une vérification. L'écart remonte à la brique source, qui corrige et re-déclenche B-33. La traçabilité est préservée : on sait quel écart a été détecté, à quelle date, et quelle correction a été apportée |
| Élargissement en clôture | La cohérence globale inter-livrables est un contrôle de fin de projet, pas seulement de fin de brique. En clôture, B-33 compare tous les livrables entre eux — c'est le seul moment où l'on peut détecter une incohérence entre deux livrables produits à des moments différents |
| « Ne compare pas à une source non calée » | Un livrable comparé à un fichier non calé donne des écarts faux (dus au calage, pas au livrable). Le calage B-30 est obligatoire pour toute vérification — sans lui, la section 1 est inutilisable |
| « Ne compare pas à une vue nettoyée d'un autre livrable » | La vue nettoyée d'un livrable est propre à ce livrable. La comparer avec un autre livrable produit des écarts faux (dus aux éléments conservés dans la vue, pas au livrable lui-même) |
| Verdict global explicite | Un tableau sans verdict laisse la décision au lecteur. Le verdict global (validé / validé sous réserve / à corriger) est la conclusion de la vérification — sans lui, la vérification n'est pas actionnable |
| Synthèse quantitative | Le nombre d'écarts section 1 et section 2, plus le verdict global, donne une vue d'ensemble que les tableaux détaillés ne donnent pas. C'est ce qui permet de décider si le livrable est globalement bon ou globalement mauvais |
| Consignation au RDL | La vérification doit être retrouvable quand une modification survient. Le RDL enregistre le verdict global et l'indice du livrable — c'est ce qui permet de savoir si un livrable a été vérifié, et avec quel résultat |

Les trois verdicts possibles — précision utile :

| Verdict | Définition | Conséquence |
| --- | --- | --- |
| Validé | Aucun écart (ou seulement des écarts acceptables justifiés) | Le livrable est prêt à être diffusé |
| Validé sous réserve | Des écarts acceptables justifiés existent (par exemple, un décalage de 2 cm pour éviter une réservation existante) | Le livrable peut être diffusé, avec les écarts mentionnés |
| À corriger | Un ou plusieurs écarts non justifiés existent | Le livrable ne doit pas être diffusé — la brique source doit corriger |

Les trois causes d'écart (section 2) — précision utile :

| Cause | Définition |
| --- | --- |
| Action | Production divergente |
| Deux livrables produits à des moments différents ont des positions différentes (par exemple, un poteau déplacé dans un livrable mais pas dans l'autre) | Corriger le livrable le plus récent (ou vérifier lequel est le bon) |
| Élément omis | Un élément présent sur un livrable est absent sur l'autre (par exemple, une baie figurée sur le plan de plancher mais oubliée sur le plan de fondations) |
| Ajouter l'élément manquant sur le livrable qui l'omet | Élément mal transcrit |
| Un élément est présent sur les deux livrables, mais avec des positions différentes (par exemple, un sommier dont la longueur est différente sur les deux plans) | Corriger l'un des deux livrables (le plus récent, ou celui qui diverge de la source) |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-20 (Conception structure GO) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-30 (Calage sur dxf/dwg source) | Les paramètres de calage — pour vérifier la cohérence plan ↔ source |
| B-31 (Preuve de superposition) | La preuve de superposition — B-33 vérifie la cohérence plan ↔ source (section 1) en s'appuyant sur la preuve B-31 |
| B-32 (Vue nettoyée par livrable) | La vue nettoyée — B-33 compare le livrable à la vue nettoyée (section 1) |
| B-34 (Synthèse des réservations) | La matrice des interfaces, contrôlée contre les plans et les notes |
| B-40 (Fondations superficielles) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-41 (Fondations profondes) | Le livrable et les positions prévues — B-33 les compare aux autres livrables |
| B-42 (Verticaux BA) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-43 (Planchers et dallages) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-44 (Charpente bois) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-45 (Structure métallique) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-46 (Maçonnerie : vérification) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-47 (Escaliers) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-48 (Prédalles et planchers préfabriqués) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-49 (Linteaux et seuils) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-50 (Assemblages et ancrages) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-60 (Plans d'exécution) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| T-02 (Prompt de recadrage) | La vérification de non-régression — B-33 vérifie que la correction n'a pas introduit de nouveaux défauts |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-32 (Vue nettoyée par livrable) | Le RDL — si une modification de source survient, les livrables avec vérification favorable sont identifiés pour mise à jour |
| B-60 (Plans d'exécution) | Le verdict de la vérification — B-60 ne produit le plan définitif qu'après un verdict favorable |
| B-70 (Auto-contrôle déclaré de synthèse) | Les verdicts de tous les livrables — B-70 vérifie que chaque livrable a une vérification croisée favorable |
| B-71 (Indiçage et supersession documentaire) | La vérification annexée au livrable — chaque livrable est indiçable avec sa vérification |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-33 |
| --- | --- | --- |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE (via B-30) |
| GEO-01 à GEO-05 | Géométrie (emprise, axes, murs, poteaux, baies) | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |

Variables produites
B-33 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (rapport de vérification croisée) qui alimente B-60, B-70 et B-71.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-02, GEO-01 à GEO-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-33, vous devez valider les écarts section 2 avant de relancer la brique source en correction. Un écart section 2 peut révéler une incohérence entre deux livrables — et le choix de la brique à corriger (celle qui est fausse, ou celle qui a été produite en premier et qui doit être reprise) est votre décision, pas celle du modèle.
Cas particulier — plusieurs livrables produits : si plusieurs livrables ont été produits (fondations, verticaux, plancher), B-33 compare le livrable courant avec chacun des livrables antérieurs. Chaque comparaison produit sa propre ligne dans le tableau section 2. Les écarts récurrents (le même élément diverge avec plusieurs livrables) signalent un problème de production plus grave qu'un écart isolé.
Cas particulier — livrable sans élément commun : si le livrable courant n'a aucun élément commun avec les livrables antérieurs (par exemple, un plan de charpente qui ne partage aucun élément avec un plan de fondations), la section 2 est vide — mais elle doit être produite quand même, avec la mention « aucun élément commun avec les livrables antérieurs ». Une section 2 vide sans justification est une anomalie.
Cas particulier — écart entre deux livrables du même indice : si un écart existe entre deux livrables du même indice (par exemple, un plan de fondations et un plan de verticaux à l'indice A), c'est anormal — ils devraient être cohérents, puisqu'ils ont été produits au même moment. B-33 le signale avec une criticité élevée.
Cas particulier — écart entre deux livrables d'indices différents : si un écart existe entre deux livrables d'indices différents (par exemple, un plan de fondations à l'indice B et un plan de verticaux à l'indice A), l'écart peut être légitime — le livrable à l'indice B a peut-être été corrigé depuis. B-33 le signale, et la brique à corriger dépend de l'indice : c'est le livrable le plus ancien qui doit être mis à jour (avec un nouvel indice), pas le plus récent.
Cas particulier — appel en clôture : si B-33 est appelée en clôture, la section 2 est élargie à l'ensemble des livrables. La vérification prend plus de temps, mais elle est indispensable — c'est le seul moment où l'on peut détecter une incohérence entre deux livrables produits à des moments différents, qui n'ont jamais été comparés directement.
Cas particulier — livrable déjà vérifié : si un livrable a déjà fait l'objet d'une vérification B-33, et qu'il est représenté sans modification, B-33 ne le re-vérifie pas — elle cite la vérification précédente (référence, date, verdict). La re-vérification n'est nécessaire qu'en cas de nouvel indice ou de nouvelle source.
Format de sortie attendu : trois pièces distinctes (rapport section 1, rapport section 2, synthèse). Les deux sections sont impérativement distinctes — les fusionner brouille le diagnostic. Le verdict global est explicite, avec les briques à corriger.
Consignation : le rapport B-33 est annexé au livrable et consigné au RDL (verdict global, indice du livrable, date). C'est ce qui permet de savoir si un livrable a été vérifié, et avec quel résultat.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Vérification croisée globale.** B-33 quitte la phase géométrique et devient la vérification finale `Plan ↔ Plan ↔ Note ↔ Nomenclature` : cohérence des repères, des sections, des niveaux, des quantités, des réservations et des Points d'Arrêt. Elle s'exécute après `B-64` et conditionne `B-70`.
**[Fin de 05_PHASE_3_CALAGE/B-33_Verification_Croisee.md]**

---

**[Début du fichier : 08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md]**

Fichier 08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md — CARNAC v3.0
________________


B-70 — AUTO-CONTRÔLE DÉCLARÉ DE SYNTHÈSE ET DE COHÉRENCE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 6 — Vérification croisée et clôture |
| Brique précédente | B-60, B-62, B-64 (livrables produits) — ou toute brique de calcul pour un contrôle intermédiaire |
| Brique suivante | B-71 (Indiçage), B-72 (Journal de clôture) |
| Fréquence | En fin de production de chaque livrable complet (après B-60, B-62, B-64) et une fois en clôture du projet |
| Modes d'appel | COMPLET (toutes les briques amont en COMPLET ou PARTIEL-DÉCLARÉ) · PARTIEL-DÉCLARÉ (certaines briques en modes dégradés : les incohérences liées à ces briques sont signalées et non résolues) · PARAMÉTRIQUE (briques suspendues : B-70 produit un auto-contrôle partiel, filigrané) |
| Paramètre d'appel | {{périmètre}} = livrable (un seul livrable) / projet (l'ensemble des livrables du projet) |
| Entrées lues | Auto-contrôles de toutes les briques exécutées (B-40 à B-50), contrôles croisés de B-50, RDR (décisions, réserves, verrous), RDL (livrables produits), B-31 (preuves de superposition), B-33 (vérifications croisées) |
| Sortie unique | Auto-contrôle de synthèse : tableau agrégé + tableau des incohérences inter-briques + tableau des interfaces + vérification des modes + verdict global |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * en fin de production de chaque livrable complet (après B-60, B-62, B-64) — pour vérifier que le livrable est cohérent ;
   * une fois en clôture du projet (avant B-71 et B-72) — pour vérifier que l'ensemble des livrables est cohérent.
Ce que vous fournissez à l'IA : les auto-contrôles de toutes les briques exécutées (B-40 à B-50), les contrôles croisés de B-50, le RDR (décisions, réserves, verrous), le RDL (livrables produits), les preuves de superposition (B-31) et les vérifications croisées (B-33). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{périmètre}} et {{mode}}.
Ce que vous validez à la sortie :
   * l'inventaire des auto-contrôles disponibles (et des manquants) ;
   * le tableau agrégé des éléments (verdict par élément) ;
   * les incohérences inter-briques (avec brique responsable) ;
   * les interfaces vérifiées ou non vérifiées ;
   * la conformité des modes (verrou V12) ;
   * le verdict global (cohérent / cohérent avec réserves / incohérent).
Ce que B-70 apporte de spécifique — la vue d'ensemble :

| Aspect | Auto-contrôle d'une brique (B-40 à B-50) | Auto-contrôle de synthèse (B-70) |
| --- | --- | --- |
| Périmètre | Une brique (fondations, verticaux, planchers, etc.) | Toutes les briques du livrable ou du projet |
| Objet | Vérifier que chaque élément de la brique est conforme | Vérifier que les éléments sont cohérents entre eux |
| Détection | Erreurs dans la brique | Incohérences entre briques |
| Interfaces | Non traitées (chaque brique ignore les autres) | Explicites (B-42→B-40, B-50→toutes, etc.) |
| Verdict | Conforme pour la brique | Cohérent pour le livrable ou le projet |

Le rôle critique de B-70 : chaque brique de calcul est individuellement correcte (elle vérifie ses éléments), mais l'ensemble peut être incohérent. Exemple :
   * B-42 (verticaux) déclare que le poteau P2 est conforme à ses vérifications EC2 ;
   * B-40 (fondations) déclare que la semelle S/P2 n'a pas été vérifiée en logement d'ancrage ;
   * chacune est individuellement correcte, mais l'ensemble est incohérent — le poteau ne pourra pas descendre ses barres dans la semelle.
Seule B-70 peut détecter ce type d'incohérence — c'est sa fonction principale.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire l'auto-contrôle déclaré de synthèse et de cohérence du {{périmètre}} (livrable / projet) {{ID-01}} — {{ID-02}}, à partir des auto-contrôles produits par toutes les briques exécutées. Tu ne refais aucun auto-contrôle : tu agrèges, tu contrôles la cohérence entre eux, et tu détectes les interfaces non couvertes.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


MÉTHODE — DANS CET ORDRE


Étape 1 — Inventaire des auto-contrôles disponibles
Liste toutes les briques exécutées pour ce périmètre :
- brique | mode d'exécution | auto-contrôle produit (oui / non) | raison si non (suspendue, SANS OBJET, mode PARAMÉTRIQUE).
Si une brique a produit un livrable mais pas son auto-contrôle, tu le signales : c'est une anomalie de production.


Étape 2 — Tableau agrégé par élément
Pour chaque élément produit (semelle, poteau, profilé, plancher, linteau, assemblage, etc.) :
- repère ;
- brique source ;
- verdict de l'auto-contrôle de la brique (conforme / conforme avec réserves / à corriger) ;
- réserves déclarées par la brique.


Étape 3 — Détection des incohérences inter-briques
Compare les déclarations des briques sur les éléments partagés :
- une brique amont déclare un effort transmis, une brique aval déclare ne pas avoir reçu cet effort : incohérence ;
- une brique amont déclare un élément conforme, une brique aval déclare que l'appui de cet élément n'est pas vérifié : incohérence ;
- une brique déclare un élément en mode PARTIEL-DÉCLARÉ sans que la décision RDR correspondante existe : incohérence ;
- une brique déclare un élément conforme sur la base d'une hypothèse H-xx, une autre brique déclare H-xx abandonnée : incohérence.
Pour chaque incohérence : nature, briques concernées, élément concerné, gravité (bloquante / à lever / à surveiller), brique responsable de la correction (amont ou aval).


Étape 4 — Vérification des interfaces
Pour chaque interface identifiée dans le carnet :
- B-42 → B-40 : les efforts à ancrer fournis par B-42 ont-ils été vérifiés en logement par B-40 ?
- B-42 → B-50 : les efforts à ancrer fournis par B-42 ont-ils été calculés par B-50 ?
- B-43 → B-50 : les efforts aux appuis fournis par B-43 ont-ils été calculés par B-50 ?
- B-44 → B-50 : les efforts aux assemblages fournis par B-44 ont-ils été calculés par B-50 ?
- B-45 → B-50 : les efforts aux nœuds fournis par B-45 ont-ils été calculés par B-50 ?
- B-46 → B-50 : les efforts des chaînages fournis par B-46 ont-ils été calculés par B-50 ?
- B-47/B-48/B-49 → B-50 : idem.
Pour chaque interface : vérifiée (oui / non / partiellement) | brique responsable en cas de non-vérification.


Étape 5 — Vérification des modes
- Aucune brique n'est passée de PARAMÉTRIQUE à COMPLET sans décision RDR ?
- Aucune brique n'est passée de BLOQUANTE à NON BLOQUANTE (verrou V12) ?
- Toutes les décisions RDR sont citées avec auteur et date ?


Étape 6 — Verdict global
- Nombre de briques exécutées | nombre d'auto-contrôles disponibles | nombre d'incohérences | nombre d'interfaces non vérifiées | nombre de modes non conformes.
- Verdict : cohérent / cohérent avec réserves / incohérent.
- Si incohérent : liste des briques à reprendre et des points à lever avant clôture.


INTERDICTIONS
- Ne refais AUCUN auto-contrôle brique par brique : tu agrèges, tu contrôles la cohérence, tu ne recommences pas les vérifications.
- Ne corrige AUCUNE incohérence : tu la signales, tu identifies la brique responsable, tu renvoies.
- Ne déclare pas une interface « vérifiée » sans avoir trouvé la trace de sa vérification dans la brique aval.
- Ne tolère aucun écart entre modes et décisions RDR : un mode PARTIEL-DÉCLARÉ sans décision RDR est une anomalie bloquante.
- Ne produis pas d'auto-contrôle de synthèse COMPLET si une seule brique est en PARAMÉTRIQUE : le mode global est PARTIEL-DÉCLARÉ minimum.
- Ne déclare pas le livrable ou le projet cohérent tant qu'une incohérence bloquante subsiste.


SORTIE
Pièce 1 — Inventaire des auto-contrôles.
Pièce 2 — Tableau agrégé par élément.
Pièce 3 — Tableau des incohérences inter-briques.
Pièce 4 — Tableau des interfaces vérifiées / non vérifiées.
Pièce 5 — Vérification des modes (conformité RDR et verrou V12).
Pièce 6 — Verdict global et liste des briques à reprendre.


CRITÈRE D'ACCEPTATION
L'auto-contrôle de synthèse est accepté si :
- toutes les briques exécutées figurent dans l'inventaire avec leur mode ;
- chaque élément produit figure dans le tableau agrégé avec son verdict ;
- toutes les incohérences inter-briques sont listées, avec brique responsable ;
- toutes les interfaces sont vérifiées, avec la trace de vérification citée ;
- la conformité des modes avec les décisions RDR est vérifiée (verrou V12) ;
- le verdict global est explicite ;
- si le mode global est PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE, la mention et le filigrane correspondants figurent.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{périmètre}} (par livrable ou projet) et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Tu agrèges, tu ne refais pas » | Refaire les auto-contrôles brique par brique est une perte de temps et une source d'erreur. Le rôle de B-70 est la vue d'ensemble — les vérifications détaillées existent déjà dans chaque brique |
| Détection des incohérences inter-briques | C'est la valeur ajoutée de B-70 : chaque brique est individuellement correcte, mais l'ensemble peut être incohérent (poteau conforme mais semelle non vérifiée). Seule cette brique peut le voir |
| Vérification des interfaces | Les interfaces (B-42→B-40, B-50→toutes) sont les points où les erreurs se glissent, parce qu'aucune brique seule ne les voit de bout en bout. B-70 les vérifie explicitement |
| Contrôle du mode et du verrou V12 | Une brique qui a « discrètement » changé de mode est une brique non fiable. La vérification du mode est une vérification de la méthode, pas du résultat |
| « Ne déclare pas cohérent tant qu'une incohérence bloquante subsiste » | Une incohérence bloquante non résolue rend le livrable non opposable. Le verdict « cohérent » est une signature, pas un constat |
| Pas de COMPLET si une brique est PARAMÉTRIQUE | Le mode global est celui de la brique la plus dégradée. Un livrable qui contient une brique PARAMÉTRIQUE ne peut pas être déclaré COMPLET |
| Inventaire des auto-contrôles manquants | Une brique qui a produit un livrable mais pas son auto-contrôle est une anomalie de production. B-70 doit la signaler — sinon, on croit que tout est vérifié alors que rien ne l'est |
| Verdict global explicite | Un tableau sans verdict laisse la décision au lecteur. Le verdict global (cohérent / cohérent avec réserves / incohérent) est la conclusion de l'auto-contrôle — sans lui, l'auto-contrôle n'est pas actionnable |
| Liste des briques à reprendre | Une incohérence détectée mais non attribuée à une brique est une incohérence qui n'est pas traitée. La liste des briques à reprendre rend l'auto-contrôle actionnable |
| Filigrane si PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE | Un auto-contrôle de synthèse qui ne porte pas le filigrane est un auto-contrôle qui est lu comme COMPLET — alors qu'il ne l'est pas |

Les trois niveaux de verdict — précision utile :

| Verdict | Définition | Conséquence |
| --- | --- | --- |
| Cohérent | Aucune incohérence bloquante, toutes les interfaces sont vérifiées | Le livrable ou le projet est validé |
| Cohérent avec réserves | Des incohérences non bloquantes subsistent (par exemple, une incohérence à surveiller), toutes les interfaces sont vérifiées | Le livrable ou le projet peut être diffusé, avec mention des réserves |
| Incohérent | Une ou plusieurs incohérences bloquantes subsistent, ou des interfaces ne sont pas vérifiées | Le livrable ou le projet ne doit pas être diffusé — les briques responsables doivent corriger |

Le piège de la « fausse cohérence » : un modèle qui reçoit les auto-contrôles de toutes les briques a tendance à :
   * soit recopier les verdicts individuels sans vérifier la cohérence entre eux ;
   * soit conclure que le livrable est cohérent parce que chaque brique est individuellement conforme.
Les deux sont faux :
   * recopier sans vérifier, c'est ne pas faire le travail de B-70 (la cohérence inter-briques n'est pas vérifiée) ;
   * conclure que c'est cohérent parce que chaque brique est conforme, c'est ignorer les incohérences entre briques (par exemple, un poteau conforme mais dont la semelle n'est pas vérifiée).
La règle est : vérifier explicitement les incohérences et les interfaces — pas les supposer.
Le piège de l'interface non vérifiée : une interface (par exemple, B-42→B-40 sur les ancrages) peut être non vérifiée même si les deux briques sont individuellement conformes :
   * B-42 calcule le poteau et fournit les efforts à ancrer ;
   * B-40 calcule la semelle mais ne vérifie pas le logement des ancrages (parce qu'elle attend les efforts de B-50) ;
   * B-50 calcule les ancrages mais ne vérifie pas qu'ils rentrent dans la semelle (parce qu'il attend le logement de B-40).
Dans ce cas, aucune brique n'a vérifié l'interface — et B-70 est la seule à pouvoir le détecter. C'est exactement pour cela que B-70 est indispensable.
Le piège du mode « discret » : une brique qui a changé de mode sans décision RDR est une brique non fiable :
   * elle est passée de PARAMÉTRIQUE à COMPLET sans que la donnée manquante soit arrivée — c'est une violation du verrou V12 ;
   * elle est passée de BLOQUANTE à NON BLOQUANTE — c'est une violation du sens unique de la requalification (V12) ;
   * la décision RDR correspondante n'existe pas — c'est une décision implicite du modèle.
B-70 vérifie explicitement la conformité des modes avec les décisions RDR — c'est ce qui rend le système fiable.
Le piège de l'auto-contrôle manquant : une brique qui a produit un livrable mais pas son auto-contrôle est une anomalie de production :
   * soit l'auto-contrôle a été oublié (le livrable est peut-être bon, mais non vérifié) ;
   * soit la brique a été exécutée en mode PARAMÉTRIQUE et l'auto-contrôle n'a pas été produit (le livrable est provisoire).
B-70 signale ces anomalies — elles sont aussi graves qu'une incohérence, parce qu'elles masquent un défaut de production.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions et verrous — B-70 vérifie la conformité des modes avec les décisions RDR (verrou V12) |
| B-22 (Note d'hypothèses de conception) | Les hypothèses non confirmées — B-70 vérifie que chaque hypothèse est tracée |
| B-31 (Preuve de superposition) | Le verdict de la preuve — B-70 vérifie que chaque livrable a sa preuve et que le verdict est favorable |
| B-33 (Vérification croisée) | Les verdicts de tous les livrables — B-70 vérifie que chaque livrable a une vérification croisée favorable |
| B-34 (Synthèse des réservations) | Le statut des Points d'Arrêt et l'exhaustivité des réservations |
| B-40 (Fondations superficielles) | L'auto-contrôle B-40 — B-70 vérifie que chaque semelle a son verdict |
| B-41 (Fondations profondes) | Le verdict de B-41 — B-70 vérifie que les fondations profondes sont traitées |
| B-42 (Verticaux BA) | L'auto-contrôle B-42 — B-70 vérifie que chaque vertical a son verdict |
| B-43 (Planchers et dallages) | L'auto-contrôle B-43 — B-70 vérifie que chaque zone a son verdict |
| B-44 (Charpente bois) | L'auto-contrôle B-44 — B-70 vérifie que chaque élément a son verdict |
| B-45 (Structure métallique) | L'auto-contrôle B-45 — B-70 vérifie que chaque profilé a son verdict |
| B-46 (Maçonnerie : vérification) | L'auto-contrôle B-46 — B-70 vérifie que chaque zone a son verdict |
| B-47 (Escaliers) | L'auto-contrôle B-47 — B-70 vérifie que chaque volée a son verdict |
| B-48 (Prédalles et planchers préfabriqués) | L'auto-contrôle B-48 — B-70 vérifie que chaque zone et chaque phase ont leur verdict |
| B-49 (Linteaux et seuils) | L'auto-contrôle B-49 — B-70 vérifie que chaque linteau a son verdict |
| B-50 (Assemblages et ancrages) | Le rapport de contrôle croisé — B-70 vérifie que tous les écarts ont été traités |
| B-60 (Plans d'exécution) | Les plans produits — B-70 vérifie que chaque livrable a son plan |
| B-62 (Nomenclature et façonnage) | Le rapport de cohérence — B-70 vérifie que la cohérence a été faite |
| B-64 (Notice de synthèse) | La notice — B-70 vérifie que chaque livrable a sa notice |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-71 (Indiçage et supersession documentaire) | Le verdict de B-70 — l'indiçage ne se fait que si le verdict est favorable |
| B-72 (Journal de clôture) | Le verdict de B-70 — B-72 liste les points ouverts à traiter avant remise |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-70 |
| --- | --- | --- |
| DEC-01 | Mode attribué à chaque brique | BLOQUANTE |
| DEC-02 | Décisions inscrites au RDR | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |

Variables produites
B-70 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (auto-contrôle de synthèse) qui alimente B-71, B-72 et les destinataires externes.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes (en particulier V11 et V12) | 00_MASTER.md |
| Dictionnaire de variables | DEC-01, DEC-02, DEC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-70, vous devez valider le verdict global — c'est votre appréciation de la criticité des incohérences qui fait foi, pas la seule liste. Une incohérence classée « à surveiller » par le modèle peut être en réalité « bloquante » — c'est votre jugement d'ingénieur qui décide.
Cas particulier — périmètre « livrable » : si B-70 est appelée pour un seul livrable (par exemple, le livrable de fondations), elle agrège uniquement les auto-contrôles des briques qui ont contribué à ce livrable (B-40, B-50 pour les ancrages). Elle ne vérifie pas les incohérences avec les livrables non encore produits.
Cas particulier — périmètre « projet » : si B-70 est appelée pour l'ensemble du projet (en clôture), elle agrège tous les auto-contrôles. C'est la vérification globale — la plus importante.
Cas particulier — auto-contrôle manquant : si une brique a produit un livrable mais pas son auto-contrôle, B-70 le signale dans l'inventaire. C'est une anomalie de production qui doit être corrigée avant clôture.
Cas particulier — incohérence inter-briques : si deux briques déclarent des choses incompatibles (par exemple, B-42 déclare le poteau P2 conforme, B-40 déclare la semelle S/P2 non vérifiée en logement), B-70 :
   * identifie l'incohérence ;
   * identifie les briques concernées ;
   * identifie l'élément concerné ;
   * classe la gravité (bloquante / à lever / à surveiller) ;
   * identifie la brique responsable de la correction (amont ou aval).
C'est votre décision de choisir quelle brique corrige — le modèle propose, vous décidez.
Cas particulier — interface non vérifiée : si une interface (par exemple, B-42→B-40 sur les ancrages) n'a pas été vérifiée (parce qu'aucune des deux briques ne l'a traitée explicitement), B-70 :
   * signale l'interface non vérifiée ;
   * identifie la brique qui devrait la vérifier (généralement B-40 pour le logement, ou B-50 pour le calcul croisé) ;
   * recommande l'action (exécuter B-40 en mode COMPLET si le logement n'a pas été vérifié).
Cas particulier — mode non conforme : si une brique a changé de mode sans décision RDR (violation du verrou V12), B-70 :
   * signale l'anomalie ;
   * identifie la brique concernée ;
   * identifie le mode actuel et le mode attendu (selon RDR) ;
   * recommande l'action (retour au mode attendu, ou décision RDR de validation).
Un mode non conforme est une anomalie bloquante — le livrable ne peut pas être diffusé tant que ce n'est pas résolu.
Cas particulier — verdict « cohérent avec réserves » : si le verdict est « cohérent avec réserves », le livrable peut être diffusé — mais les réserves doivent être explicites dans le livrable (mention dans la notice B-64, mention dans le cartouche). Le lecteur doit savoir qu'il y a des réserves.
Cas particulier — verdict « incohérent » : si le verdict est « incohérent », le livrable ne doit pas être diffusé — les briques responsables doivent corriger, puis B-70 est rappelée pour re-vérifier. Le livrable n'est diffusé qu'avec un verdict « cohérent » ou « cohérent avec réserves ».
Format de sortie attendu : six pièces distinctes (inventaire, tableau agrégé, incohérences, interfaces, modes, verdict). Le verdict global est explicite, avec la liste des briques à reprendre.
Consignation : l'auto-contrôle de synthèse B-70 est annexé au livrable et consigné au RDL — il fait partie du dossier de livraison, avec les plans, la nomenclature et la notice.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Contrôle des hypothèses et des Points d'Arrêt.** L'auto-contrôle de synthèse vérifie : statut et échéance de chaque hypothèse `H-xx` (active, expirée, acceptée, contredite), présence et opposabilité de chaque Point d'Arrêt `PA-xx`, `0` collision de textes sur les plans, adéquation titre ↔ contenu, et absence totale de second œuvre sur les vues structurelles.
**[Fin de 08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md]**

---

**[Début du fichier : 08_PHASE_6_CLOTURE/B-71_Indicage.md]**

Fichier 08_PHASE_6_CLOTURE/B-71_Indicage.md — CARNAC v3.0
________________


B-71 — INDIÇAGE ET SUPERSESSION DOCUMENTAIRE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 6 — Vérification croisée et clôture |
| Brique précédente | B-70 (Auto-contrôle de synthèse) |
| Brique suivante | B-72 (Journal de clôture) |
| Fréquence | À chaque révision d'un livrable (nouvel indice) et en fin de projet (état documentaire final) |
| Modes d'appel | COMPLET uniquement (l'indiçage est un acte administratif, pas une production) |
| Paramètre d'appel | {{périmètre}} = livrable (révision d'un livrable) / projet (état documentaire complet) |
| Entrées lues | RDL (Registre des Livrables), B-70 (verdict de cohérence), RDR (décisions et réserves), les livrables eux-mêmes (indices actuels) |
| Sortie unique | Tableau d'indiçage complet + tableau de supersession + RDL mis à jour + liste des documents en vigueur + rapport des orphelins |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * à chaque révision d'un livrable (nouvel indice) — après B-70, quand un livrable est corrigé et prêt à être réindicé ;
   * en fin de projet (état documentaire final) — avant B-72, pour figer l'état documentaire.
Ce que vous fournissez à l'IA : le RDL (Registre des Livrables), le verdict de cohérence (B-70), le RDR (décisions et réserves), et les livrables eux-mêmes (indices actuels). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{périmètre}}.
Ce que vous validez à la sortie :
   * le tableau d'indiçage (chaque document, son indice, sa date, son statut) ;
   * le tableau de supersession (révisions documentées, avec motif et auteur) ;
   * le RDL mis à jour (ligne par ligne) ;
   * la liste des documents en vigueur (indice en cours à un instant donné) ;
   * le rapport des orphelins (documents dont l'indice n'est ni en vigueur ni superseded ni annulé).
Ce que B-71 apporte de spécifique — l'administration documentaire :

| Aspect | Brique de production (B-60, B-62, B-64) | Brique d'indiçage (B-71) |
| --- | --- | --- |
| Objet | Produire le document | Administrer son état (indice, supersession) |
| Action | Créer, modifier | Figer, indiçer, superséder |
| Sortie | Le document lui-même | Le tableau d'indiçage et la liste en vigueur |
| Contenu | Technique | Administratif |
| Responsable | Ingénieur qui produit | Ingénieur qui administre |

La règle la plus importante : B-71 administre les documents, elle ne les modifie pas. Un document qui change d'indice sans motif documenté est une anomalie — c'est B-71 qui la détecte.
La notion de supersession : un document est superseded quand il est remplacé par une version plus récente. Un document en vigueur est celui qui doit être utilisé à un instant donné. Un document annulé est celui qui est retiré sans être remplacé. Ces trois statuts sont les seuls possibles — il n'y a pas de statut « provisoire » ou « ancien » dans le registre.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir l'indiçage et la supersession documentaire du {{périmètre}} (livrable / projet) {{ID-01}} — {{ID-02}}, à partir du RDL, de l'auto-contrôle B-70, du RDR et des livrables eux-mêmes. Tu ne modifies AUCUN document : tu administres leur état.


MÉTHODE — DANS CET ORDRE


Étape 1 — Inventaire des documents produits
Liste tous les documents produits pour ce périmètre :
- code du document (ex. Plan_fondations_FLORA, Note_verticaux_FLORA, Nomenclature_fondations_FLORA) ;
- intitulé ;
- indice actuel (A, B, C...) ;
- date de production ;
- brique source (B-40, B-60, B-62, B-64...) ;
- statut actuel (en vigueur / superseded / annulé).


Étape 2 — Vérification de l'indice
- Chaque document a-t-il un indice attribué ?
- L'indice est-il cohérent avec l'historique (une première émission est A, une révision est B, etc.) ?
- Aucun indice n'est sauté sans raison documentée.


Étape 3 — Supersession
Pour chaque révision :
- document concerné ;
- indice précédent (superseded) ;
- indice nouveau (en vigueur) ;
- motif de la révision (correction, modification, ajout) ;
- date de la révision ;
- auteur de la révision ;
- référence à la décision RDR ou à la brique qui a produit la révision.
Une révision sans motif documenté est une révision non traçable : tu la signales.


Étape 4 — Mise à jour du RDL
Pour chaque ligne du RDL concernée :
- code livrable ;
- nouvel indice ;
- nouvelle date ;
- nouvelle version de la vue nettoyée B-32 (si applicable) ;
- nouvelle version de la preuve B-31 (si applicable) ;
- nouvelle version de la vérification B-33 (si applicable).
Le RDL est mis à jour ligne par ligne, pas remplacé en bloc.


Étape 5 — Documents en vigueur
Vue synthétique : pour chaque type de document (plans, notes, nomenclatures, notices), quel est l'indice en vigueur. C'est la liste que l'entreprise doit utiliser pour l'exécution.


Étape 6 — Détection des orphelins
- Documents dont l'indice n'est ni en vigueur, ni superseded, ni annulé : anomalie.
- Documents produits mais absents du RDL : anomalie.
- Lignes du RDL qui pointent vers un document non produit : anomalie.
Chaque anomalie est signalée avec identification de la cause probable (oubli de saisie RDL, document produit hors chaîne, etc.).


INTERDICTIONS
- Ne modifie AUCUN document : tu administres leur état, tu ne les révises pas.
- Ne change pas un indice sans motif documenté : un indice « qui a changé tout seul » est une anomalie.
- Ne remplace pas le RDL en bloc : tu le mets à jour ligne par ligne.
- Ne déclare pas un document « en vigueur » sans date : un document sans date n'est pas opposable.
- Ne fusionne pas la liste des documents en vigueur et la liste complète : ce sont deux sorties distinctes.
- Ne tolère aucun orphelin : tout document a un statut explicite, ou il est signalé.


SORTIE
Pièce 1 — Tableau d'indiçage (documents avec indice, date, statut).
Pièce 2 — Tableau de supersession (révisions documentées).
Pièce 3 — RDL mis à jour (ligne par ligne).
Pièce 4 — Liste des documents en vigueur.
Pièce 5 — Rapport des orphelins (avec cause probable).


CRITÈRE D'ACCEPTATION
L'indiçage est accepté si :
- chaque document a un indice attribué et une date ;
- chaque révision a un motif documenté (brique ou décision RDR) ;
- le RDL est mis à jour ligne par ligne (pas remplacé) ;
- la liste des documents en vigueur est produite ;
- tous les orphelins sont détectés et signalés avec leur cause probable ;
- aucun document n'est déclaré en vigueur sans date.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{périmètre}} (par livrable ou projet). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Administrer, pas modifier | B-71 est une brique d'administration documentaire, pas de production. Confondre les deux conduit à des révisions faites « en passant » qui ne sont pas traçables — et à des documents qui changent sans que personne ne s'en aperçoive |
| Indice cohérent avec l'historique | Une première émission est A. Une révision est B. Un indice sauté (A → C) sans raison est une anomalie de traçabilité — c'est souvent le signe qu'une révision a été faite sans passer par B-71 |
| Supersession avec motif et auteur | Un document qui change d'indice sans motif documenté n'est pas opposable en cas de litige. Le motif (brique source ou décision RDR) est la protection — il permet de dire « ce document a été révisé parce que B-40 a corrigé une erreur, ou parce que D-05 a modifié une valeur » |
| RDL mis à jour ligne par ligne | Un RDL remplacé en bloc perd l'historique. Un RDL mis à jour ligne par ligne conserve la traçabilité des versions — et permet de savoir quand un document a été modifié, par qui, et pourquoi |
| Liste des documents en vigueur | C'est le livrable opérationnel : l'entreprise doit savoir quel document utiliser à un instant donné. Sans cette liste, elle risque d'utiliser un indice périmé — c'est un risque majeur |
| Détection des orphelins | Un document dont l'indice n'est ni en vigueur, ni superseded, ni annulé est un document qui échappe au contrôle. Il doit être signalé, jamais ignoré |
| « Ne déclare pas en vigueur sans date » | Un document en vigueur sans date n'est pas datable, donc pas opposable. La date est un élément de validité, pas un ornement |
| Trois statuts seulement (en vigueur / superseded / annulé) | Sans cette limite, un modèle produit des statuts « provisoire », « ancien », « à réviser » — qui ne sont pas des statuts mais des états intermédiaires non définis. Trois statuts forcent la clarté |
| « Ne fusionne pas la liste en vigueur et la liste complète » | La liste en vigueur est ce que l'entreprise doit utiliser ; la liste complète est l'historique. Les fusionner rend la lecture ambiguë — on ne sait plus quel document est en vigueur |
| Rapport des orphelins | Le rapport des orphelins est la preuve que la vérification a été faite. Sans lui, l'indiçage est une affirmation — et les anomalies de traçabilité ne sont pas détectées |

Les trois statuts d'un document — précision utile :

| Statut | Définition | Utilisation |
| --- | --- | --- |
| En vigueur | Le document est la version actuelle — celle qui doit être utilisée pour l'exécution | L'entreprise utilise cette version |
| Superseded | Le document a été remplacé par une version plus récente — il est conservé pour traçabilité | Personne ne l'utilise, mais il est conservé |
| Annulé | Le document est retiré sans être remplacé — il ne doit pas être utilisé | Personne ne l'utilise, et il est marqué comme obsolète |

Le piège du « faux nouveau » : un modèle qui reçoit une révision de livrable a tendance à :
   * soit créer un nouveau document (par exemple, « Plan_fondations_FLORA_v2 ») au lieu de réviser l'indice ;
   * soit modifier le document existant sans changer l'indice.
Les deux sont faux :
   * créer un nouveau document casse la traçabilité (on ne sait plus quel document est en vigueur) ;
   * modifier sans changer l'indice trompe l'entreprise (elle croit utiliser l'indice A alors qu'il a été modifié).
La règle est : un document = un code = un indice qui évolue. Le code reste le même, l'indice change (A → B → C). C'est la convention qui garantit la traçabilité.
Le piège de l'orphelin : un document orphelin est un document qui n'a pas de statut clair :
   * il n'est pas en vigueur (personne ne l'utilise) ;
   * il n'est pas superseded (aucune version ne le remplace) ;
   * il n'est pas annulé (personne ne l'a retiré).
C'est un document « flottant » — qui peut être utilisé par erreur, ou qui peut être perdu. B-71 doit le détecter et le signaler :
   * soit c'est un document qui devrait être en vigueur (le statut n'a pas été mis à jour) ;
   * soit c'est un document qui devrait être superseded (une version plus récente existe mais la supersession n'a pas été enregistrée) ;
   * soit c'est un document qui devrait être annulé (il est obsolète mais le statut n'a pas été mis à jour) ;
   * soit c'est un document qui devrait être dans le RDL mais qui n'y est pas (oubli de saisie).
Chaque orphelin est une anomalie de traçabilité — qui peut avoir des conséquences graves (utilisation d'un document périmé, perte d'un document valide).
Le piège du motif de révision : une révision sans motif documenté est une révision non traçable. Un modèle a tendance à :
   * soit inventer un motif (par exemple, « révision pour amélioration ») ;
   * soit omettre le motif (par exemple, « indice B » sans explication).
Les deux sont faux :
   * inventer un motif crée une fausse traçabilité (on croit savoir pourquoi le document a été révisé, mais c'est faux) ;
   * omettre le motif rend la révision non opposable (on ne sait pas pourquoi le document a changé).
La règle est : une révision = un motif documenté = un auteur = une date. C'est ce qui rend la révision défendable en cas de litige.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions — chaque révision d'un livrable est rattachée à une décision RDR (motif documenté) |
| B-30 (Calage sur dxf/dwg source) | Le fichier recalé et son indice — consignés au RDL |
| B-31 (Preuve de superposition) | La preuve annexée au livrable — chaque livrable est indiçable avec sa preuve |
| B-32 (Vue nettoyée par livrable) | La vue nettoyée et son indice — consignés au RDL |
| B-33 (Vérification croisée) | La vérification annexée au livrable — chaque livrable est indiçable avec sa vérification |
| B-60 (Plans d'exécution) | Les plans produits — B-71 les indice et gère la supersession |
| B-62 (Nomenclature et façonnage) | La nomenclature produite — B-71 l'indice et gère la supersession |
| B-64 (Notice de synthèse) | La notice — B-71 l'indice avec le livrable |
| B-70 (Auto-contrôle déclaré de synthèse) | Le verdict de B-70 — l'indiçage ne se fait que si le verdict est favorable |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-72 (Journal de clôture) | La liste des documents en vigueur — B-72 la cite dans le journal |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-71 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| ID-05 | Indice du dossier en vigueur | BLOQUANTE |
| DEC-04 | Documents supersédés (indice, date) | BLOQUANTE |

Variables produites

| Code | Libellé |
| --- | --- |
| Description | DEC-04 |
| Documents supersédés | Chaque document avec son indice, sa date, son statut (en vigueur / superseded / annulé) |

Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, ID-05, DEC-04 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-71, vous devez valider les motifs de révision — c'est vous qui savez si une révision est justifiée. Un modèle qui invente un motif crée une fausse traçabilité — qui peut vous être reprochée en cas de litige.
Cas particulier — première émission : si le document est une première émission, l'indice est A. La date est la date de production. Le statut est en vigueur. Il n'y a pas de supersession (aucune version antérieure).
Cas particulier — révision : si le document est une révision, l'indice est B, C, D.... La date est la date de révision. Le statut est en vigueur (le nouvel indice remplace l'ancien). L'ancien indice passe en superseded. Le motif de révision est documenté (brique source ou décision RDR).
Cas particulier — annulation : si le document est retiré sans être remplacé (par exemple, un plan qui n'est plus nécessaire), le statut est annulé. La date et le motif d'annulation sont documentés.
Cas particulier — plusieurs révisions successives : si un document a plusieurs indices successifs (par exemple, A → B → C), chaque indice a son statut :
   * A : superseded (remplacé par B) ;
   * B : superseded (remplacé par C) ;
   * C : en vigueur (version actuelle).
Le RDL conserve toutes les versions (pour traçabilité), mais la liste des documents en vigueur ne cite que C.
Cas particulier — document orphelin : si un document est orphelin (indice sans statut clair), B-71 le signale dans son rapport des orphelins. Vous devez alors :
   * soit compléter le statut (en vigueur, superseded, annulé) ;
   * soit retirer le document (s'il n'a pas lieu d'être).
Un document orphelin ne peut pas rester dans le RDL sans statut — c'est une anomalie qui doit être corrigée.
Cas particulier — document produit mais absent du RDL : si un document a été produit (par exemple, un plan B-60) mais n'est pas dans le RDL, B-71 le signale. Vous devez :
   * soit ajouter la ligne du RDL (avec l'indice, la date, le statut) ;
   * soit identifier l'oubli (le document a été produit hors chaîne, ou la saisie RDL a été omise).
Un document produit hors RDL est un document non traçable — c'est une anomalie de production.
Cas particulier — document dans le RDL mais non produit : si le RDL cite un document qui n'a pas été produit (par exemple, une ligne « Plan_fondations_B » alors que B-60 n'a produit que l'indice A), B-71 le signale. Vous devez :
   * soit corriger la ligne du RDL (indice erroné) ;
   * soit produire le document (B-60 en mode COMPLET).
Un document cité mais non produit est un document qui n'existe pas — c'est une anomalie de traçabilité.
Format de sortie attendu : cinq pièces distinctes (tableau d'indiçage, tableau de supersession, RDL mis à jour, liste des documents en vigueur, rapport des orphelins). La liste des documents en vigueur est la sortie opérationnelle — c'est ce que l'entreprise utilisera pour l'exécution.
Consignation : l'indiçage B-71 est consigné au RDL (ligne par ligne, pour chaque document concerné) — il fait partie du dossier de livraison.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 08_PHASE_6_CLOTURE/B-71_Indicage.md]**

---

**[Début du fichier : 08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md]**

Fichier 08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md — CARNAC v3.0
________________


B-72 — JOURNAL DE CLÔTURE DU PROJET
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 6 — Vérification croisée et clôture |
| Brique précédente | B-70 (Auto-contrôle de synthèse), B-71 (Indiçage) |
| Brique suivante | Aucune — B-72 clôt la production. Les points ouverts sont traités par T-04, les incidents par T-03 |
| Fréquence | Une fois en fin de projet (après B-70 et B-71 pour l'ensemble du projet) |
| Modes d'appel | COMPLET uniquement (le journal de clôture est un document formel) |
| Entrées lues | RDL (registre des livrables), RDR (décisions, réserves, verrous), B-70 (verdicts de cohérence par livrable), B-71 (état documentaire), toutes les briques exécutées et leurs modes |
| Sortie unique | Journal de clôture en trois sections : (1) livrables produits, (2) points ouverts, (3) synthèse et recommandations |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : une seule fois en fin de projet, après B-70 (tous les livrables sont cohérents) et B-71 (tous les documents sont indicés). C'est le document qui clôt la production — il liste ce qui a été fait, ce qui reste à faire, et il récapitule les points ouverts à traiter.
Ce que vous fournissez à l'IA : le RDL, le RDR, les verdicts B-70 pour chaque livrable, l'état documentaire B-71, et la liste des briques exécutées (avec leur mode). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * la section 1 (livrables produits, avec mode d'exécution) ;
   * la section 2 (points ouverts, en quatre sous-sections : verrous, réserves, décisions en attente, hypothèses à confirmer) ;
   * la section 3 (synthèse, points de vigilance, recommandations) ;
   * la mention finale (les points ouverts restent à traiter).
Ce que B-72 produit — le périmètre exact :

| Section | Contenu | Fonction |
| --- | --- | --- |
| Section 1 — Livrables produits | Liste exhaustive : code, intitulé, indice, date, brique source, mode d'exécution, statut | Ce qui a été remis |
| Section 2 — Points ouverts | Quatre sous-sections : verrous V-xx, réserves R-xx, décisions en attente, hypothèses à confirmer | Ce qui reste à traiter |
| Section 3 — Synthèse | Bilan de la production, points de vigilance pour l'exécution, recommandations | Ce qui est à retenir |

Ce que B-72 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Révision des documents | Brique responsable |
| Indiçage et supersession | B-71 |
| Auto-contrôle de cohérence | B-70 |
| Suivi de l'exécution des travaux | Hors périmètre CARNAC |
| Nouvelle analyse du projet | Hors périmètre de B-72 (B-72 clôt, il ne réouvre pas) |

La règle la plus importante : B-72 clôt la production formelle — les études sont remises. Il ne clôt pas substantiellement le projet : les points ouverts (verrous, réserves, décisions en attente, hypothèses à confirmer) restent à traiter. C'est cette distinction qui vous protège en cas de litige — elle prouve que vous avez remis les études et signalé les réserves.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir le journal de clôture du projet {{ID-01}} — {{ID-02}}, à partir du RDL, du RDR, des verdicts B-70 et de l'état documentaire B-71. Le journal comporte trois sections distinctes : livrables produits, points ouverts, synthèse et recommandations.


MÉTHODE — DANS CET ORDRE


SECTION 1 — LIVRABLES PRODUITS
Tableau : code | intitulé | indice | date | brique source | mode d'exécution | statut (en vigueur / superseded / annulé).
Regroupe par famille : notes de calcul, plans, nomenclatures, notices, auto-contrôles.
Pour chaque famille, une ligne de total (nombre de documents émis).
Signale les documents émis en mode PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE : ce sont les documents qui portent une réserve intrinsèque.


SECTION 2 — POINTS OUVERTS
Quatre sous-sections obligatoires, aucune ne peut être vide sans justification.


2.1 — Verrous (V-xx)
Tableau : n° verrou | donnée manquante | brique suspendue | responsable de l'obtention | échéance | briques exécutées malgré tout.


2.2 — Réserves (R-xx)
Tableau : n° réserve | objet | statut (ouverte / fermée) | responsable | échéance.


2.3 — Décisions en attente
Tableau : objet de la décision | brique concernée | destinataire (MOE / MOA / BET / BC) | conséquence de la décision sur les livrables.


2.4 — Hypothèses à confirmer (H-xx)
Tableau : n° hypothèse | valeur retenue | brique impactée | voie de confirmation (essai / décision / relevé).


SECTION 3 — SYNTHÈSE ET RECOMMANDATIONS
- Bilan de la production : nombre de livrables, nombre de briques exécutées, modes d'exécution respectés ou non.
- Points de vigilance pour l'exécution : ce que l'entreprise doit savoir avant de commencer (hypothèses actives, réserves, points de principe).
- Recommandations pour la suite : essais à commander, visas à obtenir, décisions à prendre, missions complémentaires à recommander.
- Mention finale : « Le présent journal clôture la production des études d'exécution. Il ne clôt pas le projet : les points ouverts en section 2 restent à traiter. »


INTERDICTIONS
- Ne produis pas un journal sans les trois sections : une section vide sans justification est une anomalie.
- N'omets aucun point ouvert : un point ouvert omis est un point qui sera oublié.
- Ne mets pas une section 2 vide « parce qu'il n'y a pas de verrou » : même sans verrou, tu écris « aucun verrou ouvert à la date de clôture ».
- Ne déclare pas le projet clos si des points ouverts restent à traiter : la clôture est formelle, pas substantielle.
- Ne mentionne pas de visas non requis : seuls les visas effectivement nécessaires sont listés.
- Ne fusionne pas les livrables et les points ouverts dans une seule section : ce sont deux vues distinctes de l'état du projet.


SORTIE
Pièce unique — Journal de clôture, structuré en sections 1, 2 et 3, avec tableaux et mention finale.


CRITÈRE D'ACCEPTATION
Le journal est accepté si :
- la section 1 liste tous les livrables avec indice, date, brique source, mode et statut ;
- les livrables en mode PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE sont signalés ;
- la section 2 comporte les quatre sous-sections (verrous, réserves, décisions en attente, hypothèses à confirmer), chacune renseignée ou explicitement vide ;
- chaque point ouvert a un responsable et une échéance ;
- la section 3 contient le bilan, les points de vigilance et les recommandations ;
- la mention finale figure et rappelle que les points ouverts restent à traiter ;
- le journal ne déclare pas le projet clos substantiellement tant que des points ouverts subsistent.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Trois sections distinctes | Votre choix — un journal qui ne liste que les livrables émis omet les points ouverts, alors que ce sont précisément ces points qui conditionnent la suite (exécution, réception) |
| Section 2 divisée en quatre sous-sections | Verrous, réserves, décisions en attente, hypothèses à confirmer : quatre natures différentes, avec quatre interlocuteurs différents. Les fusionner conduit à des oublis |
| Signalement des modes PARTIEL-DÉCLARÉ et PARAMÉTRIQUE | Un livrable en mode dégradé porte une réserve intrinsèque qui doit être vue en clôture. Sinon, l'entreprise reçoit un livrable qu'elle croit ferme alors qu'il ne l'est pas |
| Chaque point ouvert avec responsable et échéance | Un point ouvert sans responsable ne se traite jamais. Sans échéance, il se traite trop tard |
| « Ne déclare pas le projet clos si des points ouverts subsistent » | La clôture est formelle (les études sont remises), pas substantielle (les points ouverts restent). Confondre les deux est la principale source de litige en fin de projet |
| Mention finale explicite | La mention qui rappelle que les points ouverts restent à traiter est la protection de l'entreprise : elle prouve qu'elle a remis les études et signalé les réserves |
| « Ne fusionne pas livrables et points ouverts » | Ce sont deux vues distinctes : ce qui est remis, et ce qui reste à traiter. Les fusionner brouille la lecture en réunion de clôture |
| « Ne produis pas un journal sans les trois sections » | Une section vide sans justification est une anomalie — elle masque un défaut de production. Le journal doit couvrir les trois sections, même si l'une est explicitement vide |
| « Ne mets pas une section 2 vide parce qu'il n'y a pas de verrou » | Même sans verrou, la section 2 doit être renseignée avec la mention « aucun verrou ouvert à la date de clôture ». C'est la preuve que la vérification a été faite |
| « Ne déclare pas le projet clos substantiellement » | La clôture formelle (remise des études) n'est pas la clôture substantielle (tous les points ouverts traités). Le journal doit refléter cette distinction — sinon, il engage votre responsabilité sur des points non traités |

Les quatre sous-sections de la section 2 — précision utile :

| Sous-section | Nature | Interlocuteur habituel |
| --- | --- | --- |
| Verrous (V-xx) | Données manquantes qui suspendent des briques | Responsable de l'obtention (MOA, BET, GO) |
| Réserves (R-xx) | Objets à lever, avec statut ouvert/fermé | Responsable de l'obtention |
| Décisions en attente | Décisions à prendre (auteur, conséquence) | MOE, MOA, BET, BC |
| Hypothèses à confirmer (H-xx) | Hypothèses de travail non encore validées | Voie de confirmation (essai, décision, relevé) |

Le piège de la clôture substantielle : un modèle qui reçoit le RDL et le RDR a tendance à déclarer le projet clos parce que tous les livrables ont été produits. C'est exactement ce qu'il faut interdire :
   * les livrables ont été produits, mais les points ouverts (verrous, réserves, décisions, hypothèses) restent à traiter ;
   * la clôture est formelle (les études sont remises) — pas substantielle (tous les points sont traités) ;
   * déclarer le projet clos substantiellement engage votre responsabilité sur des points qui ne sont pas traités.
La mention finale est la protection : elle prouve que vous avez remis les études et signalé les réserves.
Le piège du mode PARAMÉTRIQUE : si un livrable est en mode PARAMÉTRIQUE (par exemple, un plan de fondations avec q_adm manquante), le journal doit explicitement le signaler dans la section 1. L'entreprise doit savoir que ce livrable n'est pas exécutable en l'état — sinon, elle risque de l'exécuter et de commettre une erreur grave.
Le piège de l'omission des points ouverts : un modèle a tendance à minimiser les points ouverts (par exemple, « quelques points à traiter ») pour présenter un projet « propre ». C'est exactement ce qu'il faut interdire :
   * chaque point ouvert omis est un point qui sera oublié à l'exécution ;
   * le journal est le document qui rassemble tous les points ouverts en un seul endroit lisible ;
   * c'est ce qui permet à la MOA de décider si le projet est suffisamment mûr pour être exécuté.
Le journal doit lister tous les points ouverts, pas les minimiser.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les réserves et verrous — B-72 liste les points ouverts qui restent à traiter après remise |
| B-04 (Plan de travail dégradé) | L'historique des PTD — B-72 liste les points ouverts qui restent à traiter après remise |
| B-15 (Fiche de synthèse) | Les risques résiduels — B-72 les intègre dans la section « points ouverts » |
| B-22 (Note d'hypothèses de conception) | Les hypothèses non confirmées — B-72 les liste dans les points ouverts |
| B-41 (Fondations profondes) | Les recommandations de mission — B-72 liste les points ouverts |
| B-64 (Notice de synthèse) | La notice — B-72 la cite dans la liste des livrables produits |
| B-70 (Auto-contrôle déclaré de synthèse) | Le verdict de B-70 — B-72 liste les points ouverts à traiter avant remise |
| B-71 (Indiçage et supersession documentaire) | La liste des documents en vigueur — B-72 la cite dans le journal |
| T-04 (Prompt de demande) | Les demandes non répondues à la date de clôture — B-72 les cite dans les points ouverts |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-03 (Prompt de méta-amélioration) | Le journal de clôture — T-03 s'appuie dessus pour proposer des corrections au carnet |
| T-04 (Prompt de demande) | Les points ouverts (verrous, réserves, décisions en attente) — T-04 les transforme en demandes formelles à la MOE/BET/MOA |

Variables consommées

| Code | Libellé | Statut dans B-72 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| ID-05 | Indice du dossier en vigueur | BLOQUANTE |
| DEC-02 | Décisions inscrites au RDR | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE |
| DEC-04 | Documents supersédés | BLOQUANTE |

Variables produites
B-72 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (journal de clôture) qui alimente T-04, T-03 et les destinataires externes.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, ID-05, DEC-02, DEC-03, DEC-04 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-72, vous devez valider la liste des points ouverts avant transmission à la MOA. Certains points peuvent être acceptés par votre décision (par exemple, un verrou dont la donnée est arrivée après la production du journal), d'autres non. C'est votre appréciation qui fait foi — et c'est vous qui décidez quels points doivent être traités avant la remise.
Cas particulier — aucun point ouvert : si le projet n'a aucun point ouvert (ce qui est rare, mais possible), la section 2 est renseignée avec la mention « aucun verrou ouvert, aucune réserve ouverte, aucune décision en attente, aucune hypothèse à confirmer à la date de clôture ». Ce n'est pas une section vide — c'est une section explicitement sans point ouvert.
Cas particulier — livrables en mode dégradé : si des livrables ont été émis en mode PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE, la section 1 les signale explicitement, et la section 2 les reprend (hypothèses à confirmer, décisions en attente). Un livrable PARAMÉTRIQUE qui n'apparaît pas dans la section 2 est une anomalie — il porte une réserve intrinsèque qui doit être tracée.
Cas particulier — plusieurs livrables du même type : si le projet comporte plusieurs livrables du même type (par exemple, plusieurs plans de fondations pour des zones différentes), la section 1 les liste tous, avec leur code et leur indice. Un livrable regroupé (par exemple, « plans de fondations : 3 plans ») est une anomalie — chaque livrable doit être identifiable.
Cas particulier — projet multi-lots : si le projet comporte plusieurs lots (par exemple, lot GO et lot charpente), le journal de clôture est propre au lot GO — il ne couvre pas les autres lots. Les interfaces avec les autres lots sont mentionnées dans les points ouverts (section 2.3 — décisions en attente), mais le journal ne clôt pas les autres lots.
Cas particulier — clôture partielle : si le projet est clôturé par phases (par exemple, phase 1 : fondations, phase 2 : superstructure), chaque phase a son propre journal de clôture. Le journal de la phase 1 liste les points ouverts pour la phase 1 — et les interfaces avec la phase 2. Le journal de clôture final agrège les journaux des phases.
Format de sortie attendu : journal unique (5 à 10 pages), structuré en sections 1, 2 (avec 4 sous-sections), 3, et mention finale. Le journal porte le filigrane si un ou plusieurs livrables sont en mode PARAMÉTRIQUE.
Consignation : le journal de clôture B-72 est consigné au RDL (comme document de clôture) et transmis aux destinataires (MOA, MOE, BC, BET). C'est le document qui prouve que les études ont été remises et que les réserves ont été signalées.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md]**

---

<!-- ================= COUPURE ================= -->

# ANNEXE AU PACK 05 — PROMPTS TRANSVERSE (T-01 à T-04), à coller seulement si nécessaire

---

**[Début du fichier : 09_TRANSVERSE/T-01_Sincerite.md]**

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
**[Fin de 09_TRANSVERSE/T-01_Sincerite.md]**

---

**[Début du fichier : 09_TRANSVERSE/T-02_Recadrage.md]**

Fichier 09_TRANSVERSE/T-02_Recadrage.md — CARNAC v3.0
________________


T-02 — PROMPT DE RECADRAGE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | Transverse — à tout moment |
| Brique précédente | T-01 (sincérité) — ou détection directe d'un défaut par vous |
| Brique suivante | Retour à la brique source du livrable (B-40 à B-50, B-60) pour correction |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | Le livrable défaillant, la description du défaut (fournie par vous) |
| Sortie unique | Diagnostic de cause + méthode de correction + preuve de correction + vérification de non-régression |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * quand un livrable présente un défaut visible (calage faux, poteaux flottants, axes mal ancrés, sections incohérentes, ferraillage manquant) ;
   * quand une deuxième version ne corrige pas le défaut de la première ;
   * quand un modèle « corrige » sans expliquer ce qu'il a corrigé.
Ce que vous fournissez à l'IA : le livrable défaillant et la description du défaut (en termes observables : « les axes ajoutés ne tombent pas sur les murs du fond », « deux poteaux sont dessinés au milieu de pièces », « un profilé n'a pas d'appui à son extrémité Est »). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{code_livrable}} et {{description_du_defaut}}.
Ce que vous validez à la sortie :
   * la reformulation du défaut en termes observables ;
   * le diagnostic de méthode (la cause dans la méthode de production, pas dans le résultat) ;
   * la nouvelle méthode (reproductible, qui évite la cause) ;
   * la preuve de correction (au même zoom que le livrable initial, plus zooms sur les points singuliers) ;
   * la vérification de non-régression (la correction n'a pas introduit de nouveaux défauts).
Ce que T-02 apporte de spécifique — le recadrage par diagnostic :

| Aspect | Correction visuelle (interdite) | Recadrage T-02 (autorisé) |
| --- | --- | --- |
| Objet | Déplacer les points pour les faire coïncider | Diagnostiquer la cause dans la méthode, puis corriger |
| Méthode | Retouche à l'œil | Nouvelle méthode reproductible |
| Cause | Non identifiée | Identifiée précisément |
| Correction | Ponctuelle | Systémique |
| Preuve | Absente | Preuve de correction au même zoom |
| Non-régression | Non vérifiée | Vérifiée |

T-02 est la brique qui a transformé « chef, regarde le décalage » en un diagnostic reproductible. Dans la conversation d'origine, c'est cette formulation qui a fonctionné — elle a forcé le modèle à changer de méthode au lieu de retoucher le dessin. Sans elle, un modèle réajuste à l'œil et produit une nouvelle version fausse pour une autre raison.
La règle la plus importante : T-02 diagnostique la cause dans la méthode, pas dans le résultat. Un défaut de résultat est un symptôme — la cause est toujours dans la méthode (mauvaise extraction, mauvaise transformation, mauvaise lecture). Corriger le symptôme sans corriger la cause reproduit le défaut.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : recadrer la production du livrable {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}. Le livrable présente le défaut suivant : {{description_du_defaut}}. Tu ne corriges PAS le livrable « à l'œil » : tu diagnostiques la cause de la méthode, tu changes de méthode, tu prouves la correction.


MÉTHODE


Étape 1 — Reformulation du défaut
Reformule le défaut en termes observables : « les axes ajoutés ne tombent pas sur les murs du fond », « deux poteaux sont dessinés au milieu de pièces », « un profilé n'a pas d'appui à son extrémité Est ». Si le défaut ne peut pas être reformulé en termes observables, tu le signales et tu demandes une précision.


Étape 2 — Diagnostic de méthode
Identifie la cause probable du défaut dans la méthode de production, pas dans le résultat :
- méthode d'extraction de la géométrie (coordonnées vectorielles vs fraction d'image) ?
- transformation de calage (translation, rotation, échelle) ?
- lecture des calques (mauvais calque lu, calque vide) ?
- interprétation des données BET (confusion sections / positions) ?
- méthode de report sur le livrable (report manuel vs extraction) ?
Tu cites la cause précise et la brique ou l'étape où elle s'est produite.


Étape 3 — Proposition de nouvelle méthode
Propose une méthode différente qui évite la cause :
- « j'extrais les coordonnées vectorielles du DXF source, je calcule une transformation par 3 points non alignés, je vérifie le résidu sur 2 points témoins » ;
- « je lis le calque 010_mur du DXF archi, j'extrais les faces de murs, je superpose les axes calculés sur les faces extraites » ;
- « je vérifie chaque extrémité d'élément par rapport aux faces de murs mesurées ».
La méthode doit être reproductible : elle doit pouvoir être réappliquée si le défaut revient.


Étape 4 — Application de la nouvelle méthode
Applique la nouvelle méthode et produis une version corrigée du livrable.


Étape 5 — Preuve de correction
Produis une preuve que la correction est effective :
- superposition annotée (si graphique) ;
- tableau de contrôle élément par élément (si calcul) ;
- test de reproductibilité (si méthode).
La preuve est fournie au même zoom que le livrable initial, plus des zooms sur les points singuliers si nécessaire.


Étape 6 — Vérification de non-régression
Vérifie que la correction n'a pas introduit de nouveaux défauts ailleurs :
- les éléments corrigés sont-ils cohérents avec le reste du livrable ?
- les éléments non corrigés sont-ils inchangés ?
- les cotes, sections, positions qui n'étaient pas concernées par le défaut sont-elles toujours justes ?


INTERDICTIONS
- Ne corrige pas « à l'œil » : ne déplace aucun point sans avoir diagnostiqué la cause.
- Ne propose pas une correction sans changer de méthode : « je vais faire plus attention » n'est pas une méthode.
- Ne produis pas de version corrigée sans preuve de correction : la preuve est aussi importante que le livrable.
- Ne corrige pas un défaut en en introduisant un autre : la vérification de non-régression est obligatoire.
- Ne minimise pas le défaut : « ce n'est qu'un décalage de quelques millimètres » est un diagnostic, pas une excuse.


SORTIE
Pièce 1 — Reformulation du défaut.
Pièce 2 — Diagnostic de méthode.
Pièce 3 — Proposition de nouvelle méthode.
Pièce 4 — Version corrigée du livrable.
Pièce 5 — Preuve de correction.
Pièce 6 — Vérification de non-régression.


CRITÈRE D'ACCEPTATION
Le recadrage est accepté si :
- le défaut est reformulé en termes observables ;
- le diagnostic identifie une cause précise dans la méthode ;
- la nouvelle méthode est reproductible (elle peut être décrite et réappliquée) ;
- la version corrigée est produite avec la nouvelle méthode ;
- la preuve de correction est produite au même zoom que le livrable initial ;
- la vérification de non-régression est faite.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{code_livrable}} et {{description_du_defaut}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Diagnostique la cause, ne déplace pas à l'œil » | C'est la formulation exacte qui a fonctionné sur le projet Flora. La correction visuelle produit un livrable faux pour une autre raison — et le cycle recommence |
| Diagnostic dans la méthode, pas dans le résultat | Un défaut de résultat est un symptôme. La cause est toujours dans la méthode (mauvaise extraction, mauvaise transformation, mauvaise lecture). Corriger le symptôme sans corriger la cause reproduit le défaut |
| Reformulation en termes observables | Un défaut mal décrit (« le plan est faux ») ne peut pas être diagnostiqué. La reformulation en termes observables (« les axes ne tombent pas sur les murs du fond ») permet d'identifier la cause |
| Méthode reproductible | « Je ferai plus attention » n'est pas une méthode. La nouvelle méthode doit pouvoir être décrite et réappliquée — c'est ce qui garantit la non-régression |
| Preuve de correction | Une version corrigée sans preuve est une version corrigée sur parole. La preuve est la seule garantie que la correction est effective — et qu'elle n'est pas juste une nouvelle version « qui a l'air mieux » |
| Vérification de non-régression | Une correction qui introduit un autre défaut est une correction ratée. La vérification de non-régression est la seule protection contre les corrections qui déplacent le problème |
| « Ne minimise pas le défaut » | La tentation est de minimiser (« ce n'est qu'un décalage de quelques millimètres ») pour éviter la correction. C'est faux — un décalage de quelques millimètres peut être critique (par exemple, un poteau qui tombe sur une réservation existante) |
| Preuve au même zoom que le livrable initial | Une preuve à un zoom différent peut masquer des écarts ailleurs. La preuve doit être produite au même zoom, plus des zooms sur les points singuliers — c'est la seule façon de vérifier que la correction est complète |
| Diagnostic avec brique ou étape | Un diagnostic sans identification de la brique ou de l'étape est un diagnostic vague — il ne permet pas de corriger la méthode. La brique ou l'étape identifiée rend le diagnostic actionnable |

Les trois causes fréquentes — précision utile :

| Cause | Définition | Exemple |
| --- | --- | --- |
| Extraction | La géométrie a été mal extraite (coordonnées vectorielles non utilisées, calque non lu, etc.) | Un modèle a dessiné les murs à partir d'une fraction d'image au lieu des coordonnées vectorielles du DXF |
| Transformation | La transformation de calage est fausse (translation, rotation, échelle) | Le calage a été fait par 2 points au lieu de 3, et l'échelle est fausse |
| Interprétation | Les données BET ont été mal interprétées (confusion sections/positions, etc.) | Une section de poutre a été confondue avec la position d'un poteau |

Le piège du « je vais faire plus attention » : un modèle a tendance à proposer une correction « en faisant plus attention » — c'est-à-dire en retouchant le résultat. C'est exactement ce qu'il faut interdire :
   * « faire plus attention » n'est pas une méthode ;
   * la correction visuelle produit un livrable faux pour une autre raison ;
   * le cycle recommence (le défaut réapparaît ailleurs).
La seule réponse correcte est : changer de méthode. La nouvelle méthode doit être reproductible — c'est ce qui garantit la non-régression.
Le piège de la minimisation : un modèle a tendance à minimiser le défaut (« ce n'est qu'un décalage de quelques millimètres ») pour éviter la correction. C'est exactement ce qu'il faut interdire :
   * un décalage de quelques millimètres peut être critique (un poteau qui tombe sur une réservation existante, un ferraillage qui ne rentre pas dans le coffrage) ;
   * la minimisation est un diagnostic (le défaut est effectivement mineur) — pas une excuse pour ne pas corriger ;
   * même un défaut mineur doit être corrigé si le livrable est exécutable.
Le piège de la « correction par déplacement » : un modèle a tendance à déplacer les points pour les faire coïncider (par exemple, déplacer un axe pour qu'il tombe sur un mur). C'est exactement ce qu'il faut interdire :
   * le déplacement corrige le décalage à un endroit, mais ne corrige pas la cause (unités, rotation, points mal choisis) ;
   * la cause persiste, et le décalage réapparaît ailleurs — souvent de manière plus insidieuse ;
   * le résultat est un fichier qui « a l'air calé » aux points de contrôle, mais qui est faux partout ailleurs.
La règle « diagnostic avant correction » est la seule qui garantit un livrable valide.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| T-01 (Prompt de sincérité) | Le verdict « non sincère » — T-02 diagnostique la cause et corrige la méthode |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-31 (Preuve de superposition) | La preuve de correction — B-31 vérifie que la correction est effective |
| B-33 (Vérification croisée) | La vérification de non-régression — B-33 vérifie que la correction n'a pas introduit de nouveaux défauts |
| B-40 (Fondations superficielles) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-41 (Fondations profondes) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-42 (Verticaux BA) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-43 (Planchers et dallages) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-44 (Charpente bois) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-45 (Structure métallique) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-46 (Maçonnerie : vérification) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-47 (Escaliers) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-48 (Prédalles et planchers préfabriqués) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-49 (Linteaux et seuils) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-50 (Assemblages et ancrages) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| B-60 (Plans d'exécution) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-03 (Prompt de méta-amélioration) | Le diagnostic et la nouvelle méthode — T-03 propose des corrections au carnet si le défaut est récurrent |

Variables consommées

| Code | Libellé | Statut dans T-02 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| Toutes les variables citées dans le livrable | Selon le livrable | BLOQUANTE |

Variables produites
T-02 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (diagnostic + méthode + preuve) qui alimente la brique source du livrable, B-31, B-33 et T-03.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-02, vous devez valider le diagnostic — c'est votre appréciation qui fait foi, pas la seule liste. Un diagnostic qui identifie la mauvaise cause conduit à une correction qui ne résout pas le problème — c'est votre jugement d'ingénieur qui décide.
Cas particulier — diagnostic incertain : si le modèle n'arrive pas à identifier la cause du défaut (par exemple, il n'y a pas de cause évidente dans la méthode), le diagnostic doit le dire. Vous pouvez alors :
   * soit produire une nouvelle version avec une méthode radicalement différente (par exemple, repartir du DXF source au lieu du PDF) ;
   * soit suspendre le livrable et recommencer la production à la brique amont.
Un diagnostic incertain est un diagnostic honnête — un faux diagnostic est plus dangereux qu'une absence de diagnostic.
Cas particulier — plusieurs défauts : si le livrable présente plusieurs défauts (par exemple, décalage + poteaux flottants + sections incohérentes), T-02 traite chaque défaut séparément :
   * un diagnostic par défaut ;
   * une méthode par défaut ;
   * une preuve par défaut.
Un diagnostic global (« le livrable est faux ») ne permet pas de corriger — il faut identifier chaque cause.
Cas particulier — défaut récurrent : si le défaut se reproduit après la correction (par exemple, le décalage réapparaît sur une nouvelle version), c'est le signe que le diagnostic est faux — la cause n'a pas été identifiée. Vous devez :
   * soit reprendre le diagnostic (chercher une autre cause) ;
   * soit changer radicalement de méthode (par exemple, repartir du DXF source au lieu du PDF) ;
   * soit faire appel à un tiers (BET, BC) pour un diagnostic externe.
Un défaut récurrent est le signe qu'il faut changer d'approche — pas retoucher encore.
Cas particulier — preuve de correction : la preuve de correction doit être au même zoom que le livrable initial, plus des zooms sur les points singuliers. Une preuve à un zoom différent peut masquer des écarts ailleurs — c'est la règle de B-31 (preuve de superposition), appliquée à T-02.
Cas particulier — non-régression : la vérification de non-régression doit être explicite — pas une simple déclaration « la correction n'a pas introduit de nouveaux défauts ». Elle doit vérifier :
   * les éléments corrigés (sont-ils cohérents avec le reste du livrable ?) ;
   * les éléments non corrigés (sont-ils inchangés ?) ;
   * les cotes, sections, positions non concernées par le défaut (sont-elles toujours justes ?).
Sans cette vérification, une correction peut introduire un nouveau défaut — plus insidieux que le premier.
Format de sortie attendu : six pièces distinctes (reformulation, diagnostic, méthode, version corrigée, preuve, non-régression). Chaque pièce est explicite — pas de déclaration vague.
Consignation : le recadrage T-02 est consigné au RDL (avec le code du livrable, la date, le défaut identifié, la méthode appliquée). En cas de défaut récurrent, T-03 propose des corrections au carnet.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 09_TRANSVERSE/T-02_Recadrage.md]**

---

**[Début du fichier : 09_TRANSVERSE/T-03_Meta_Amelioration.md]**

Fichier 09_TRANSVERSE/T-03_Meta_Amelioration.md — CARNAC v3.0
________________


T-03 — PROMPT DE MÉTA-AMÉLIORATION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | Transverse — à tout moment |
| Brique précédente | B-72 (Journal de clôture) — ou T-02 (Recadrage) en cas d'incident significatif |
| Brique suivante | Nouvelle version du carnet CARNAC (v3.x) — voir Annexe C |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | Le carnet CARNAC (v3.0), le journal de clôture du projet (B-72), les corrections effectuées (T-02), les points ouverts (RDR) |
| Sortie unique | Proposition de correction au carnet : brique(s) concernée(s), nature de la correction, justification, impact, classement GÉNÉRALE / PROJET / À ÉTUDIER |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * après chaque projet terminé — pour transformer les incidents en améliorations ;
   * après un incident significatif (T-02 déclenché) — pour éviter que l'incident se reproduise sur un autre projet ;
   * après l'ajout ou la suppression d'une brique — pour maintenir la cohérence du carnet.
Ce que vous fournissez à l'IA : le carnet CARNAC (version en vigueur), le journal de clôture du projet (B-72), les corrections effectuées (T-02), les points ouverts (RDR). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * l'inventaire des incidents et corrections ;
   * l'analyse de chaque incident (brique concernée, nature du problème, conséquence) ;
   * les propositions de correction (brique, clause, justification, impact) ;
   * le tri en trois catégories : GÉNÉRALE (à intégrer au carnet), PROJET (reste dans le RDR du projet), À ÉTUDIER (nécessite validation) ;
   * la proposition de version (si des corrections générales sont retenues).
Ce que T-03 apporte de spécifique — la boucle d'apprentissage :

| Aspect | Correction de projet (T-02) | Méta-amélioration (T-03) |
| --- | --- | --- |
| Objet | Corriger un livrable défaillant | Améliorer le carnet qui a produit le livrable |
| Périmètre | Un livrable, un projet | Tous les projets futurs |
| Sortie | Version corrigée du livrable | Proposition de correction au carnet |
| Effet | Résout le problème actuel | Évite que le problème se reproduise |
| Boucle | Fermée (le livrable est corrigé) | Ouverte (le carnet évolue) |

T-03 est la brique qui transforme un incident en amélioration générale. C'est la boucle d'apprentissage qui fait progresser CARNAC d'une version à l'autre, par incréments de version mineure puis majeure.
La règle la plus importante : une correction n'entre au carnet que si elle est générale. Une correction propre à un projet reste dans le RDR de ce projet — elle ne pollue pas le carnet.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : analyser le projet {{ID-01}} — {{ID-02}} terminé (ou l'incident survenu) et proposer les corrections à apporter au carnet CARNAC. Tu ne modifies pas le carnet : tu proposes des corrections, à valider par l'utilisateur.


MÉTHODE


Étape 1 — Inventaire des incidents et corrections
Liste tous les incidents survenus pendant le projet :
- défauts de livrable (T-02 déclenchés) ;
- points ouverts qui n'auraient pas dû l'être (données non demandées, données demandées inutilement) ;
- blocages non anticipés (données manquantes non identifiées à la MPD) ;
- corrections manuelles effectuées (où le carnet n'a pas couvert un besoin).


Étape 2 — Analyse de chaque incident
Pour chaque incident :
- brique concernée (B-xx, T-xx) ;
- nature du problème (méthode, données, clause manquante, clause mal formulée) ;
- conséquence sur le livrable.


Étape 3 — Proposition de correction
Pour chaque incident, propose une correction générale (applicable à tous les projets) :
- brique(s) à modifier (version actuelle → version proposée) ;
- clause à ajouter, à modifier ou à supprimer ;
- justification (en quoi la correction évite la reproduction de l'incident) ;
- impact sur les autres briques (une correction à B-40 peut avoir un impact sur B-42 ou B-50).


Étape 4 — Tri des corrections
Classe les corrections en trois catégories :
- GÉNÉRALE : la correction s'applique à tous les projets, elle entre au carnet.
- PROJET : la correction est propre à ce projet, elle reste dans le RDR.
- À ÉTUDIER : la correction semble générale mais nécessite une validation ou un test avant d'entrer au carnet.


Étape 5 — Proposition de version
Si des corrections GÉNÉRALES sont retenues, propose une nouvelle version du carnet :
- numéro de version (vX.Y) ;
- liste des corrections intégrées ;
- entrée au journal des révisions (annexe C) ;
- impact sur les fiches existantes.


INTERDICTIONS
- Ne propose aucune correction propre à un seul projet comme correction générale.
- Ne propose aucune correction sans justification (en quoi elle évite la reproduction de l'incident).
- Ne propose pas de correction qui supprime un verrou sans le remplacer : la règle de non-régression (document maître §9) interdit la suppression sans remplacement.
- Ne modifie pas le carnet : tu proposes, l'utilisateur valide.
- Ne fusionne pas corrections GÉNÉRALE et corrections PROJET : ce sont deux destins différents.


SORTIE
Pièce 1 — Inventaire des incidents.
Pièce 2 — Analyse par incident.
Pièce 3 — Propositions de correction.
Pièce 4 — Tri GÉNÉRALE / PROJET / À ÉTUDIER.
Pièce 5 — Proposition de version (si corrections générales).


CRITÈRE D'ACCEPTATION
La proposition est acceptée si :
- chaque incident est listé et analysé ;
- chaque correction est justifiée ;
- chaque correction est classée en GÉNÉRALE / PROJET / À ÉTUDIER ;
- aucune correction projet n'est présentée comme générale ;
- aucune correction ne supprime un verrou sans remplacement ;
- la proposition de version est cohérente avec les corrections retenues.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Ne modifie pas le carnet » | T-03 propose, l'utilisateur décide. Un modèle qui modifie son propre carnet est un modèle qui dérive — il peut introduire des corrections non validées, ou supprimer des clauses qui le gênent |
| Tri GÉNÉRALE / PROJET / À ÉTUDIER | La distinction est cruciale : une correction spécifique à un projet ne doit pas polluer le carnet. Sans ce tri, le carnet se remplit de cas particuliers et perd sa généralité — il devient inutilisable |
| Justification obligatoire | Une correction sans justification est une modification arbitraire. La justification (« en quoi elle évite la reproduction de l'incident ») est la seule protection contre les corrections « cosmétiques » |
| Non-suppression de verrou sans remplacement | La règle de non-régression protège le carnet contre les régressions. Une correction qui supprime un verrou sans le remplacer est une régression déguisée — elle peut sembler améliorer le carnet, mais elle le fragilise |
| Inventaire des points ouverts « qui n'auraient pas dû l'être » | Certains points ouverts sont légitimes (données manquantes réelles), d'autres sont des défauts du carnet (données non demandées, données demandées inutilement). C'est la distinction qui permet d'améliorer le carnet |
| Inventaire des corrections manuelles | Les corrections manuelles (où le carnet n'a pas couvert un besoin) sont les meilleurs indicateurs de lacunes du carnet. Elles révèlent ce que le carnet aurait dû faire mais n'a pas fait |
| Impact sur les autres briques | Une correction à B-40 peut avoir un impact sur B-42 ou B-50 (par exemple, si B-40 change la façon de calculer les semelles, B-50 doit être cohérent). L'impact doit être identifié pour éviter les incohérences |
| Proposition de version | Une correction générale sans proposition de version est une correction qui ne sera jamais intégrée. La proposition de version (vX.Y) est le mécanisme qui permet d'intégrer les corrections au carnet |
| « Ne fusionne pas GÉNÉRALE et PROJET » | Les deux catégories ont des destins différents : GÉNÉRALE entre au carnet, PROJET reste dans le RDR. Les fusionner conduit à des corrections qui entrent au carnet sans justification (ou qui restent dans le RDR alors qu'elles devraient être générales) |
| « Ne propose pas de correction qui supprime un verrou » | Les 15 verrous sont la protection du carnet contre les dérives. Une correction qui supprime un verrou est une régression — même si elle semble simplifier le carnet |

Les trois catégories de corrections — précision utile :

| Catégorie | Définition |
| --- | --- |
| Destin | GÉNÉRALE |
| La correction s'applique à tous les projets, elle corrige une lacune du carnet | Entre au carnet dans la prochaine version (vX.Y) |
| PROJET | La correction est propre à ce projet (par exemple, une donnée spécifique, une contrainte de site particulière) |
| Reste dans le RDR du projet | À ÉTUDIER |
| La correction semble générale, mais elle doit être testée ou validée avant d'entrer au carnet | Entre au carnet après validation (ou après un projet de test) |

Le piège de la « correction spécifique » : un modèle qui reçoit un incident de projet a tendance à proposer une correction spécifique (par exemple, « ajouter une clause pour le cas où le fichier DXF a des calques non nommés ») comme correction générale. C'est exactement ce qu'il faut interdire :
   * une correction spécifique à un projet pollue le carnet (elle ajoute une clause qui ne s'appliquera jamais ailleurs) ;
   * elle rend le carnet plus complexe sans le rendre plus utile ;
   * elle peut même être contradictoire avec d'autres clauses.
La règle est : une correction n'entre au carnet que si elle est générale — c'est-à-dire si elle s'applique à tous les projets, pas seulement à celui qui a révélé l'incident.
Le piège de la suppression de verrou : un modèle a tendance à proposer de supprimer un verrou qui le gêne (par exemple, « supprimer le verrou V7 sur les placeholders pour simplifier la rédaction »). C'est exactement ce qu'il faut interdire :
   * les 15 verrous sont la protection du carnet contre les dérives ;
   * supprimer un verrou, c'est supprimer une protection — c'est une régression ;
   * si un verrou est problématique, il doit être remplacé (par une clause équivalente ou meilleure), pas supprimé.
La règle de non-régression est la seule protection contre les corrections qui fragilisent le carnet.
Le piège de la « correction cosmétique » : un modèle a tendance à proposer des corrections cosmétiques (par exemple, « reformuler la clause X pour la rendre plus claire ») sans justification réelle. C'est exactement ce qu'il faut interdire :
   * une correction cosmétique sans justification est une modification arbitraire ;
   * elle peut introduire des ambiguïtés (la reformulation peut changer le sens) ;
   * elle ne résout aucun problème réel.
La règle est : une correction doit être justifiée — elle doit résoudre un problème identifié dans l'inventaire.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-72 (Journal de clôture) | Le journal de clôture — T-03 s'appuie dessus pour proposer des corrections au carnet |
| T-01 (Prompt de sincérité) | Les éléments à lever récurrents — T-03 propose des corrections au carnet |
| T-02 (Prompt de recadrage) | Le diagnostic et la nouvelle méthode — T-03 propose des corrections au carnet si le défaut est récurrent |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| Aucune — dernière brique de la chaîne | — |

Variables consommées

| Code | Libellé | Statut dans T-03 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-02 | Décisions inscrites au RDR | NON BLOQUANTE (si absentes, T-03 fonctionne sur les incidents seuls) |
| DEC-03 | Verrous ouverts | NON BLOQUANTE (si absents, T-03 fonctionne sur les incidents seuls) |

Variables produites
T-03 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (proposition de correction) qui alimente la nouvelle version du carnet et l'annexe C.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, DEC-02, DEC-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des révisions | Versions du carnet | 10_ANNEXES/C_Journal_Revisions.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-03, vous devez valider les corrections GÉNÉRALES à intégrer au carnet. C'est vous qui décidez si une correction est générale (elle entre au carnet) ou spécifique (elle reste dans le RDR du projet). Un modèle qui classe une correction spécifique en GÉNÉRALE pollue le carnet.
Cas particulier — plusieurs projets : si T-03 est appelée après plusieurs projets (par exemple, après trois projets avec la même version en vigueur), elle peut proposer une correction globale (v3.x) qui intègre les corrections récurrentes. La règle est : une correction qui apparaît dans plusieurs projets est probablement générale — elle doit entrer au carnet.
Cas particulier — incident isolé : si un incident apparaît dans un seul projet, il peut être :
   * soit spécifique au projet (correction PROJET) ;
   * soit général (correction GÉNÉRALE) — dans ce cas, il doit être testé sur un autre projet avant d'entrer au carnet (classification À ÉTUDIER).
La règle est : un incident isolé est À ÉTUDIER avant d'être intégré au carnet — sauf s'il est manifestement général (par exemple, un défaut de méthode qui se reproduira sur tous les projets).
Cas particulier — correction qui supprime un verrou : si une correction proposée supprime un verrou (par exemple, « supprimer le verrou V7 sur les placeholders »), elle doit être refusée — sauf si elle est remplacée par une clause équivalente. La règle de non-régression est absolue.
Cas particulier — correction qui ajoute une brique : si une correction propose d'ajouter une nouvelle brique (par exemple, « ajouter une brique B-51 pour les ancrages de garde-corps »), elle doit être étudiée :
   * la nouvelle brique est-elle vraiment nécessaire ? (une brique existante peut-elle couvrir le besoin ?)
   * son numéro est-il disponible ? (la numérotation doit être stable)
   * son intégration dans la chaîne est-elle cohérente ?
Une nouvelle brique est une modification majeure — elle doit être justifiée et validée.
Cas particulier — correction qui supprime une brique : si une correction propose de supprimer une brique (par exemple, « supprimer B-41 fondations profondes car jamais utilisée »), elle doit être étudiée :
   * la brique est-elle vraiment inutile ? (peut-elle être nécessaire sur un projet futur ?)
   * son numéro doit-il rester vacant ? (la règle de stabilité de numérotation)
   * l'impact sur les autres briques est-il nul ?
La suppression d'une brique est une modification majeure — elle doit être justifiée et validée.
Cas particulier — correction qui modifie un mode : si une correction propose de modifier un mode (par exemple, « ajouter un mode VALIDÉ PAR TIERS »), elle doit être étudiée :
   * le mode existant ne suffit-il pas ? (les 6 modes sont COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE / INTERNE-GO / SANS OBJET)
   * le nouveau mode est-il vraiment distinct ? (ou peut-il être traité par une décision RDR ?)
   * l'impact sur les briques existantes est-il nul ?
Un nouveau mode est une modification majeure — elle doit être justifiée et validée.
Format de sortie attendu : cinq pièces distinctes (inventaire, analyse, propositions, tri, version). Chaque pièce est explicite — pas de déclaration vague.
Consignation : la proposition T-03 est consignée au journal des révisions (annexe C) comme proposition de nouvelle version. Si la nouvelle version est validée par vous, elle est intégrée au carnet et le journal est mis à jour.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Passage obligatoire du compilateur.** Aucune version du carnet n'est publiée sans exécution du compilateur de cohérence (`T1` à `T10`) et sans résultat `10/10 PASS` (zéro erreur, zéro avertissement). Le journal d'exécution est annexé à la version publiée.
**[Fin de 09_TRANSVERSE/T-03_Meta_Amelioration.md]**

---

**[Début du fichier : 09_TRANSVERSE/T-04_Demande_Complement.md]**

Fichier 09_TRANSVERSE/T-04_Demande_Complement.md — CARNAC v3.0
________________


T-04 — PROMPT DE DEMANDE DE COMPLÉMENT
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | Transverse — à tout moment |
| Brique précédente | B-04 (PTD) — ou toute brique qui identifie une donnée bloquante manquante |
| Brique suivante | Retour à la brique concernée (B-40 à B-50) une fois la réponse obtenue |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | RDR (points ouverts), briques suspendues, MPD (variables bloquantes) |
| Sortie unique | Demande de complément formelle à la MOE / au BET / au MOA, structurée et datée, avec échéance et conséquence de non-réponse, + mise à jour du RDR |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * à la fin de la phase 0 (cadrage) — pour les données bloquantes identifiées à la MPD ;
   * à tout moment si une donnée bloquante est découverte en cours de production ;
   * avant remise d'une offre ou d'un livrable important.
Ce que vous fournissez à l'IA : le RDR (points ouverts, verrous), la liste des briques suspendues, la MPD (variables bloquantes) et le destinataire (MOE / BET / MOA / BC). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{destinataire}}.
Ce que vous validez à la sortie :
   * la liste des demandes (une par point ouvert) ;
   * la conséquence de non-réponse pour chaque demande ;
   * l'échéance pour chaque demande ;
   * la priorisation (URGENTE / IMPORTANTE / DE SUIVI) ;
   * la forme de la demande (courrier formel) ;
   * la consignation au RDR (section 2 et 3).
Ce que T-04 apporte de spécifique — la demande formelle :

| Aspect | Point ouvert au RDR (B-03) | Demande de complément (T-04) |
| --- | --- | --- |
| Objet | Constater un point ouvert | Le transformer en demande formelle à un destinataire |
| Forme | Ligne de tableau | Courrier structuré et daté |
| Destinataire | Mentionné | Explicitement adressé |
| Échéance | Mentionnée | Explicite et opposable |
| Conséquence | Implicite | Explicite (« si non-réponse, alors… ») |
| Traçabilité | Au RDR | Au RDR + courrier envoyé |

T-04 est la brique qui transforme un point ouvert en demande opposable. Un point ouvert au RDR est un constat interne — il ne déclenche pas d'action. Une demande formelle est un acte administratif — elle déclenche une réponse, ou elle documente l'absence de réponse (ce qui vous protège en cas de litige).
La règle la plus importante : T-04 ne rédige aucune demande sans conséquence de non-réponse et sans échéance. Une demande sans conséquence est une demande qui ne se traite pas — elle reste dans la pile du destinataire.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : rédiger la demande de complément formelle de l'opération {{ID-01}} — {{ID-02}} à destination de {{destinataire}} (MOE / BET / MOA / BC), à partir des points ouverts du RDR et des briques suspendues. La demande doit être structurée, datée, et opposer à chaque point une conséquence de non-réponse.


MÉTHODE


Étape 1 — Inventaire des points ouverts
Reprends du RDR et du Registre des Verrous :
- les variables BLOQUANTES manquantes (FDC) ;
- les briques suspendues et leurs conséquences ;
- les décisions en attente (RDR section 1) ;
- les hypothèses à confirmer (RDR section 4).


Étape 2 — Structuration de la demande
Chaque demande comporte obligatoirement :
- numéro de demande (D-xx ou R-xx, cohérent avec le RDR) ;
- objet de la demande (donnée manquante, décision à prendre, confirmation d'hypothèse) ;
- brique(s) concernée(s) ;
- conséquence de non-réponse : quelle(s) brique(s) reste(nt) suspendue(s), quel(s) livrable(s) ne peu(ven)t pas être émis, quel impact sur le planning ;
- échéance souhaitée ;
- destinataire.


Étape 3 — Priorisation
Classe les demandes en trois catégories :
- URGENTES : bloquent la remise d'un livrable majeur ou l'engagement de la phase suivante.
- IMPORTANTES : bloquent une partie de la production mais n'empêchent pas les autres briques.
- DE SUIVI : à traiter avant l'exécution, mais pas avant la remise des études.


Étape 4 — Rédaction formelle
Rédige la demande en respectant les formes :
- en-tête : projet, date, destinataire, objet ;
- corps : liste numérotée des demandes, structurée comme à l'étape 2 ;
- clôture : demande d'accusé de réception et de réponse écrite dans les délais ;
- signature : nom et fonction de l'expéditeur (à remplir).


Étape 5 — Traçabilité
Chaque demande est consignée au RDR (section 2 ou 3) :
- numéro de demande ;
- date d'envoi ;
- destinataire ;
- échéance ;
- statut (envoyée / en attente / répondue).


INTERDICTIONS
- Ne rédige aucune demande sans conséquence de non-réponse : une demande sans conséquence est une demande qui ne se traite pas.
- Ne rédige aucune demande sans échéance : une demande sans échéance est une demande sans priorité.
- Ne mélange pas les demandes URGENTES et les demandes de suivi : elles n'ont pas le même traitement.
- Ne rédige pas de demande vague (« fournir les données manquantes ») : chaque demande porte sur une donnée précise, avec sa référence au RDR.
- N'oublie aucun point ouvert : chaque point du RDR doit avoir sa demande correspondante.
- Ne produis pas de demande sans consignation au RDR : une demande non consignée n'est pas opposable.


SORTIE
Pièce 1 — Demande formelle (courrier).
Pièce 2 — Tableau de synthèse des demandes (numéro, objet, brique, échéance, destinataire, conséquence de non-réponse).
Pièce 3 — Mise à jour du RDR (section 2 et 3).


CRITÈRE D'ACCEPTATION
La demande est acceptée si :
- chaque point ouvert du RDR a sa demande correspondante ;
- chaque demande a une conséquence de non-réponse explicite ;
- chaque demande a une échéance ;
- chaque demande est classée en URGENTE / IMPORTANTE / DE SUIVI ;
- la forme est respectée (en-tête, corps, clôture, signature) ;
- chaque demande est consignée au RDR.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{destinataire}} (par MOE, BET, MOA ou BC). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Conséquence de non-réponse obligatoire | Une demande sans conséquence (« merci de fournir le G2 ») est une demande qui ne se traite pas. La conséquence (« la brique B-40 reste suspendue, le livrable de fondations ne peut pas être émis ») est ce qui déclenche la réponse — elle rend le destinataire responsable du retard |
| Échéance obligatoire | Une demande sans échéance se traite quand le destinataire a le temps — c'est-à-dire tard. L'échéance rend la demande prioritaire |
| Priorisation URGENTE / IMPORTANTE / DE SUIVI | Sans priorisation, toutes les demandes sont traitées au même niveau, ce qui revient à traiter les urgentes trop tard. La priorisation permet au destinataire de savoir ce qui bloque et ce qui peut attendre |
| Consignation au RDR | Une demande orale ou par mail non consignée n'est pas opposable. La consignation au RDR transforme la demande en trace formelle — c'est ce qui vous protège en cas de litige |
| Chaque point du RDR = une demande | Un point du RDR sans demande est un point qui reste ouvert indéfiniment. La correspondance stricte point ↔ demande garantit que rien n'est oublié |
| Demande précise (pas vague) | Une demande vague (« fournir les données manquantes ») ne permet pas au destinataire de savoir quoi fournir. Une demande précise (« fournir q_adm ELS selon NF P 94-261, référence SOL-01 du RDR ») permet une réponse rapide |
| Forme respectée (en-tête, corps, clôture, signature) | Un courrier sans forme n'est pas un courrier — c'est un message. La forme (en-tête, date, destinataire, signature) rend la demande officielle — elle peut être produite en justice si nécessaire |
| Clôture avec accusé de réception | L'accusé de réception est la preuve que la demande a été reçue. Sans lui, le destinataire peut nier avoir reçu la demande — l'accusé est votre protection |
| « Ne mélange pas URGENTES et DE SUIVI » | Un courrier qui mélange les urgentes et les demandes de suivi dilue les urgentes — le destinataire traite tout au même niveau, et les urgentes ne sont pas traitées en priorité. Les séparer rend la demande lisible |
| « Ne produis pas de demande sans consignation au RDR » | Une demande sans consignation est une demande « dans le vide » — elle n'est pas traçable, elle ne peut pas être suivie, elle ne peut pas être opposée en cas de litige |

Les trois niveaux de priorité — précision utile :

| Priorité | Définition | Exemple |
| --- | --- | --- |
| URGENTE | Bloque la remise d'un livrable majeur ou l'engagement de la phase suivante | q_adm manquante — bloque le livrable de fondations |
| IMPORTANTE | Bloque une partie de la production mais n'empêche pas les autres briques | Section d'une panne existante non sondée — bloque la vérification de la charpente, mais les autres briques tournent |
| DE SUIVI | À traiter avant l'exécution, mais pas avant la remise des études | Niveau d'assise exact des fondations — à préciser à l'ouverture des fouilles, pas avant |

Le piège de la demande vague : un modèle a tendance à produire des demandes vagues (« fournir les données manquantes », « confirmer les hypothèses »). C'est exactement ce qu'il faut interdire :
   * une demande vague ne permet pas au destinataire de savoir quoi fournir ;
   * elle ne permet pas de savoir quand la réponse est attendue ;
   * elle n'a pas de conséquence de non-réponse claire — donc elle ne déclenche rien.
La règle est : une demande = une donnée précise = un code RDR. C'est la seule forme qui déclenche une réponse.
Le piège de la « conséquence vague » : un modèle a tendance à produire des conséquences vagues (« retard sur le planning », « impact sur les livrables »). C'est exactement ce qu'il faut interdire :
   * une conséquence vague ne permet pas de mesurer l'impact réel ;
   * elle ne permet pas de décider si le retard est critique ou non ;
   * elle ne permet pas d'opposer la demande en cas de litige.
La règle est : une conséquence précise = une brique suspendue = un livrable non émis. C'est la seule forme qui a du poids.
Le piège du courrier unique : un modèle a tendance à produire un seul courrier qui regroupe toutes les demandes. C'est acceptable si les demandes sont de même priorité et au même destinataire — sinon, il faut séparer :
   * courrier urgent (destinataire MOA) — pour les données qui bloquent la remise ;
   * courrier important (destinataire BET) — pour les données qui bloquent une partie de la production ;
   * courrier de suivi (destinataire MOE) — pour les données à préciser avant l'exécution.
Séparer les courriers permet au destinataire de traiter par priorité — et rend la traçabilité plus claire.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les variables BLOQUANTE — T-04 les cite comme objets de demande |
| B-03 (Registre des décisions) | Les réserves (Section 2) — T-04 transforme les réserves en demande formelle à la MOE / BET / MOA |
| B-04 (Plan de travail dégradé) | Les briques suspendues et les voies d'obtention — T-04 transforme ces informations en demande formelle à la MOE / BET / MOA |
| B-10 (Audit critique du CCTP) | Les points à lever avec destinataire — T-04 transforme ces points en demande formelle à la MOE / BET / MOA |
| B-11 (Audit du diagnostic structure) | Les points à lever avec destinataire — T-04 transforme ces points en demande formelle |
| B-12 (Audit des pièces géotechniques) | La recommandation de mission — T-04 transforme cette recommandation en demande formelle à la MOA |
| B-14 (Clarification du périmètre) | Les prestations À TRANCHER avec destinataire — T-04 les transforme en demande formelle |
| B-15 (Fiche de synthèse) | Les risques avec responsable et échéance — T-04 les transforme en demande formelle à la MOE / BET / MOA |
| B-24 (Vérification d'éléments existants non) | Les essais à commander — T-04 les transforme en demande formelle à la MOA |
| B-41 (Fondations profondes) | Les recommandations de mission — T-04 les transforme en demande formelle à la MOA |
| B-72 (Journal de clôture) | Les points ouverts (verrous, réserves, décisions en attente) — T-04 les transforme en demandes formelles à la MOE/BET/MOA |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les demandes consignées (statut envoyée / en attente / répondue) — le RDR est mis à jour |
| B-40 (Fondations superficielles) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-41 (Fondations profondes) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-42 (Verticaux BA) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-43 (Planchers et dallages) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-44 (Charpente bois) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-45 (Structure métallique) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-46 (Maçonnerie : vérification) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-47 (Escaliers) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-48 (Prédalles et planchers préfabriqués) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-49 (Linteaux et seuils) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-50 (Assemblages et ancrages) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |
| B-72 (Journal de clôture) | Les demandes non répondues à la date de clôture — B-72 les cite dans les points ouverts |

Variables consommées

| Code | Libellé | Statut dans T-04 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE (T-04 ne peut pas produire de demande sans la liste des verrous) |
| Toutes les variables BLOQUANTE de la FDC | Selon la variable | BLOQUANTE (chaque variable bloquante doit être l'objet d'une demande) |

Variables produites
T-04 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (demande formelle + tableau de synthèse + RDR mis à jour) qui alimente le RDR, la brique concernée et B-72.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, DEC-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-04, vous devez valider les conséquences de non-réponse — c'est votre appréciation de la criticité qui fait foi. Une conséquence « retard sur le livrable de fondations de 2 semaines » est votre engagement — elle doit être réaliste et défendable.
Cas particulier — demandes à plusieurs destinataires : si les demandes concernent plusieurs destinataires (par exemple, une donnée MOA et une donnée BET), T-04 produit un courrier par destinataire — pas un courrier unique. Chaque destinataire reçoit uniquement les demandes qui le concernent.
Cas particulier — demandes de priorités différentes : si les demandes ont des priorités différentes (par exemple, deux urgentes et trois de suivi), T-04 peut produire :
   * un courrier urgent (destinataire concerné) — pour les demandes qui bloquent la remise ;
   * un courrier de suivi (destinataire concerné) — pour les demandes à traiter avant l'exécution.
Le courrier urgent est envoyé immédiatement ; le courrier de suivi peut être envoyé dans un délai plus long.
Cas particulier — demande déjà envoyée : si une demande a déjà été envoyée (par exemple, dans un courrier antérieur), T-04 ne la reproduit pas — elle est relancée (rappel avec la date du premier envoi et la date de relance). Le RDR est mis à jour avec le statut « relancée ».
Cas particulier — demande répondue : si une demande a été répondue, T-04 ne la reproduit pas — elle est clôturée au RDR (statut « répondue », avec la date de réponse et la référence à la pièce reçue). La brique concernée est relancée en mode COMPLET (ou PARTIEL-DÉCLARÉ si la réponse est partielle).
Cas particulier — demande refusée : si une demande est refusée par le destinataire (par exemple, la MOA refuse de commander un G3), T-04 ne la reproduit pas — elle est clôturée au RDR (statut « refusée », avec la date et le motif du refus). La brique concernée est relancée en mode PARTIEL-DÉCLARÉ (avec la décision de repli) ou reste suspendue (avec la mention « refusée »).
Cas particulier — demande sans réponse à la clôture : si une demande est sans réponse à la date de clôture, T-04 la cite dans le journal de clôture (B-72) comme point ouvert — avec la date d'envoi, l'échéance, et la conséquence de non-réponse. C'est ce qui vous protège en cas de litige : la demande a été envoyée, la réponse n'est pas venue, et vous avez documenté la conséquence.
Format de sortie attendu : trois pièces distinctes (demande formelle, tableau de synthèse, RDR mis à jour). La demande formelle est rédigée au format courrier — en-tête, corps, clôture, signature.
Consignation : la demande T-04 est consignée au RDR (section 2 pour les réserves, section 3 pour les verrous) — elle fait partie de la traçabilité du projet.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 09_TRANSVERSE/T-04_Demande_Complement.md]**

<!-- FIN DU PACK — CARNAC v3.0 -->
