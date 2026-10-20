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