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