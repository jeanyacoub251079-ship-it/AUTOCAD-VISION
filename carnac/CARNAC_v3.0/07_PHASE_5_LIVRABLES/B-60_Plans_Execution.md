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

---

### 6. COMPLÉMENT v3.0.1 — IMPLANTATION LISIBLE (addendum A1)

**Fond simplifié, pas dump.** « Report, jamais redessin » porte sur les **coordonnées et dimensions**. Interdit de coller le DXF `B-32` entier (calques, blocs, textes). L'existant est **extrait** (murs porteurs, baies, trémie) et figuré en **gris léger** sur fond **blanc**.

**Implantation obligatoire.** Chaque type comporte (1) le **plan du niveau** avec **tous** les ouvrages de ce type à leur place, (2) au moins une coupe ou un détail type. Un croquis de coupe **sans** plan d'implantation (dallage, linteau, semelle) est **refusé**.

**Codes hors dessin.** Sur le plan : repères d'ouvrage, cotes, un encadré `ENC` ≤ 5 lignes, pastilles `H-xx`/`D-19` courtes, filigrane une ligne. Les codes `D-xx`/`R-xx`, l'historique d'indice et « ce que la brique ne fait pas » vont **en note**.

**Vue d'ensemble de lecture.** Après le dernier type, une pièce facultative peut superposer tous les ouvrages neufs. Filigrane `LECTURE — NE PAS EXÉCUTER`. Ce n'est **pas** un plan EXE fusionné (la règle un type = un plan EXE reste).

**Titre trois lignes.** Qui / quoi / indice + matériau. Cartouche visuellement court. Couleurs : un type = une couleur. Coupe hachurée, barres dessinées.

---

### 7. COMPLÉMENT v3.0.2 — SUBSTITUTION DES REPÈRES B-20 (C-27)

`B-60` **n'est pas** le plan de principe. Le principe est `B-20`, après `B-32`, avant les calculs.

`B-60` (EXE) **reprend les mêmes repères** (`P2` reste `P2`, `Lt1` reste `Lt1`) et substitue l'enveloppe par la section calculée. Interdit d'inventer un nouveau système de repères en EXE. Interdit d'appeler `B-60` pour produire un principe.