Fichier 05_PHASE_3_CALAGE/B-32_Vue_Nettoyee.md — CARNAC v3.0
________________


B-32 — VUE NETTOYÉE PAR LIVRABLE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 1 — Socle géométrique et nettoyage |
| Brique précédente | B-30 (Calage) |
| Brique suivante | B-31 (Preuve de superposition) — ou directement la brique de production du livrable |
| Fréquence | À chaque livrable graphique, versionnée avec lui. Mise à jour incrémentale en cas de modification de source. |
| Modes d'appel | COMPLET (fichier vectoriel exploitable) · PARTIEL-DÉCLARÉ (fichier image : nettoyage manuel déclaré, réserves notées) |
| Entrées lues | Fichier source calé (B-30), livrable concerné, liste des calques ou éléments à conserver/supprimer |
| Sortie unique | Vue nettoyée propre au livrable, versionnée, consignée au RDL |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : à chaque livrable graphique produit. La vue nettoyée est le fond de plan utilisé par la brique de production (B-60) — elle est versionnée avec le livrable, et régénérée en cas de modification de source.
Ce que vous fournissez à l'IA : le fichier source calé (B-30), le livrable concerné (type et indice), et la liste des calques ou entités à conserver/supprimer (selon le livrable). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{indice_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * la liste des calques (conservés / supprimés / à trancher) avec justification ;
   * le nom de la vue nettoyée (convention) ;
   * la consignation au RDL (ligne complétée) ;
   * en cas de mise à jour incrémentale : les livrables impactés identifiés via le RDL.
Ce que B-32 apporte de spécifique — la vue nettoyée par livrable :

| Aspect | Vue nettoyée unique (par projet) | Vue nettoyée par livrable (B-32) |
| --- | --- | --- |
| Fond de plan | Un seul fond pour tous les livrables | Un fond adapté à chaque livrable |
| Éléments conservés | Tous les éléments utiles au livrable le plus exigeant | Seuls les éléments utiles au livrable concerné |
| Mise à jour | Tout le projet est à refaire | Seuls les livrables impactés sont à refaire |
| Traçabilité | Un seul fond, un seul indice | Un fond par livrable, indicé avec le livrable |

Votre règle (validée au tronçon 6) : une vue nettoyée par livrable, versionnée avec lui. En cas de modification de source, seuls les livrables impactés sont régénérés — pas tout le projet.
La règle la plus importante : B-32 ne redessine aucun élément. La vue nettoyée est une extraction filtrée du fichier source calé — pas un redessin. Un redessin introduit des erreurs invisibles, et rend la vue incohérente avec le fichier source.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la vue nettoyée du livrable graphique {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir du fichier source calé (B-30), et en conservant uniquement les éléments nécessaires au livrable concerné.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


RÈGLES DE NETTOYAGE
Selon le livrable à produire, conserve :
- Livrable FONDATIONS : murs porteurs, refends, poteaux, semelles existantes, axes, cotations de position des appuis. Supprime : cloisons, menuiseries intérieures, revêtements, mobilier, fluides.
- Livrable PLANCHER : murs porteurs, poteaux, profilés, appuis, axes, trémies et réservations. Supprime : tout élément du second œuvre, y compris les menuiseries extérieures si le plancher ne les concerne pas.
- Livrable CHERPENTE : murs d'appui, pignons, fermes existantes, pannes, chevrons. Supprime : tout élément sous toiture sauf les appuis.
- Livrable VERTICAUX : murs, poteaux, axes, ouvertures (baies et passages), attentes de fondations. Supprime : tout le second œuvre.
- Livrable PLAN DE PRINCIPE : murs porteurs, axes, trames. Supprime : tout ce qui n'est pas porteur ou repère.


MÉTHODE
1. Reprends le fichier source calé (B-30).
2. AVANT tout classement par calque : applique le §R (protocole de reconnaissance des porteurs, en fin de fiche) — inventaire des entités, reconstruction des parois et mesure des épaisseurs, critères C1 à C6 (source BET souveraine, épaisseur vs GEO-10, superposition des niveaux vs GEO-11, schéma statique, position, indices graphiques). Les tronçons sont d'abord chaînés en parois complètes (R.3bis : segmentation aux intersections, regroupement des colinéaires, appariement des faces — on ne classe jamais un tronçon isolé). Si un plan BET vectoriel existe (DOC-03), ses porteurs sont projetés automatiquement sur les parois par recalage et recouvrement (R.4bis) : c'est cette projection qui vaut critère C1, et ses écarts sont signalés, jamais appariés de force. Chaque paroi reçoit une classe : PORTEUR CERTAIN, NON PORTEUR ou À LEVER, justifiée dans le tableau de reconnaissance. Si les calques du fichier séparent déjà explicitement les porteurs (sémantique vérifiée), le §R se réduit aux temps R.2, R.6 et R.7.
3. Identifie les calques (layers) du DXF ou les entités du PDF vectoriel, et pour chacun : CONSERVER, SUPPRIMER, ou À TRANCHER — en cohérence avec les classes du §R : un élément classé PORTEUR CERTAIN n'est jamais supprimé ; un élément À LEVER non arbitré est conservé en gris (calque EXISTANT).
4. Pour les calques À TRANCHER, applique la règle du livrable concerné : conserver si l'élément est structurant pour le livrable, supprimer sinon.
5. Extrais les entités conservées. NE REDESSINE AUCUN élément : la vue nettoyée est une extraction filtrée du fichier source, pas un redessin.
6. Nomme la vue nettoyée selon la convention : {{code_livrable}}_VUE-NETTOYEE_{{indice_livrable}}.dxf (ou .pdf, .png).
7. Consigne au RDL : livrable, source utilisée, calque de nettoyage, version. Consigne au journal OUT-03 les comptages par classe (PORTEUR CERTAIN / NON PORTEUR / À LEVER), les seuils GEO-10/GEO-11 utilisés et les arbitrages reçus.


MISE À JOUR INCRÉMENTALE (cas de modification)
Si une modification est découverte (source corrigée, calage corrigé, livrable corrigé) :
1. Consulte le RDL pour identifier les livrables impactés.
2. Pour chaque livrable impacté, régénère la vue nettoyée depuis le fichier source mis à jour.
3. Ne régénère JAMAIS les vues nettoyées des livrables non impactés.
4. Consigne la mise à jour au RDL (indice précédent, indice nouveau, motif, date).


INTERDICTIONS
- Ne redessine AUCUN élément : la vue nettoyée est une extraction filtrée du fichier source, jamais un redessin.
- Ne conserve pas un calque « au cas où » : si l'élément n'est pas nécessaire au livrable, il est supprimé.
- N'utilise jamais une vue nettoyée d'un livrable pour un autre livrable : chaque livrable a la sienne.
- Ne régénère pas toutes les vues nettoyées du projet sur une modification ponctuelle : tu identifies d'abord les livrables impactés via le RDL.
- Ne nomme pas les vues nettoyées de façon libre : tu utilises la convention {{code_livrable}}_VUE-NETTOYEE_{{indice_livrable}}.
- Ne mélange pas la vue nettoyée et le livrable : la vue nettoyée est un fond de plan, pas un plan d'exécution.


SORTIE
Pièce 1 — Vue nettoyée
Fichier DXF ou PDF + PNG, nommé selon la convention, avec la liste des calques conservés/supprimés/à trancher.


Pièce 2 — Tableau de nettoyage
Calque ou entité | Statut (conservé / supprimé / à trancher) | Justification | Livrable concerné


Pièce 3 — Consignation RDL
Ligne du RDL pour ce livrable : source utilisée (fichier + indice), version du calage B-30, version de la vue nettoyée, indice du livrable, date.


CRITÈRE D'ACCEPTATION
La vue nettoyée est acceptée si :
- la vue est une extraction filtrée du fichier source calé, sans redessin ;
- chaque calque ou entité a un statut explicite et une justification ;
- le nom respecte la convention ;
- la vue est propre au livrable (pas réutilisée d'un autre livrable) ;
- le RDL est mis à jour avec la ligne correspondante ;
- en cas de mise à jour incrémentale, seuls les livrables impactés ont été régénérés.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{code_livrable}}, {{indice_livrable}} et {{mode}} (par COMPLET ou PARTIEL-DÉCLARÉ). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Vue nettoyée par livrable | Votre choix — chaque livrable a ses propres besoins de fond de plan. Une vue unique oblige à conserver des éléments inutiles pour certains livrables (par exemple, les menuiseries sur un plan de fondations), et ne permet pas la mise à jour ciblée. La vue par livrable est plus légère (moins d'éléments) et plus maintenable (mise à jour ciblée) |
| Règles de nettoyage par livrable | Sans règles fixées, un modèle invente le nettoyage : il conserve les menuiseries sur un plan de fondations (parce que « c'est dans le DXF »), ou supprime des éléments structurants (parce qu'« ils ne sont pas porteurs »). Les règles écrites rendent le nettoyage reproductible — deux ingénieurs doivent aboutir au même résultat |
| « À TRANCHER » | Certains calques ne sont ni à conserver ni à supprimer dans l'absolu : la décision dépend du livrable. Par exemple, les trémies sont structurantes sur un plan de plancher, mais inutiles sur un plan de fondations. Les nommer explicitement évite les décisions implicites |
| « Extraction filtrée, jamais redessin » | Verrou V2 — la vue nettoyée n'invente rien, elle filtre. Un redessin introduit des erreurs invisibles : un mur dessiné légèrement décalé, une cote arrondie, une intersection mal recopiée. Ces erreurs sont indétectables sur la vue nettoyée — et se propagent au livrable |
| Mise à jour incrémentale + RDL | Votre règle : si on découvre une modification, on met à jour les livrables impactés, pas tout. Le RDL identifie les livrables impactés — sans lui, la règle est inapplicable, et la seule solution est de tout refaire |
| « Ne régénère jamais les vues non impactées » | Un modèle qui ne maîtrise pas la mise à jour incrémentale régénère tout — ce qui réintroduit des erreurs dans les livrables qui étaient bons (les paramètres de calage ont pu changer, ou le fichier source a été corrigé entre-temps, mais pas pour ce livrable). C'est l'inverse du résultat cherché |
| Convention de nommage | Le livrable et sa vue nettoyée doivent se retrouver par leur nom. Une convention libre casse la traçabilité — on ne sait plus quelle vue correspond à quel livrable |
| Consignation au RDL | La vue nettoyée doit être retrouvable quand une modification de source survient. Le RDL est ce qui permet de savoir quelle vue a été produite, à partir de quelle source, et à quelle version du calage |
| Tableau de nettoyage avec justification | Un calque « supprimé » sans justification est un calque qui peut être supprimé par erreur. La justification force le modèle à expliciter pourquoi un élément est conservé ou supprimé — et permet à un tiers de vérifier que la décision est correcte |

Les règles de nettoyage par livrable — précision utile :

| Livrable | Éléments conservés | Éléments supprimés |
| --- | --- | --- |
| FONDATIONS | Murs porteurs, refends, poteaux, semelles existantes, axes, cotations de position des appuis | Cloisons, menuiseries, revêtements, mobilier, fluides |
| PLANCHER | Murs porteurs, poteaux, profilés, appuis, axes, trémies et réservations | Tout élément du second œuvre (y compris menuiseries extérieures si non concernées) |
| CHARPENTE | Murs d'appui, pignons, fermes existantes, pannes, chevrons | Tout élément sous toiture sauf les appuis |
| VERTICAUX | Murs, poteaux, axes, ouvertures (baies et passages), attentes de fondations | Tout le second œuvre |
| PLAN DE PRINCIPE | Murs porteurs, axes, trames | Tout ce qui n'est pas porteur ou repère |

Le piège du « au cas où » : un modèle a tendance à conserver un calque « au cas où il serait utile ». C'est faux :
   * un calque conservé en trop encombre la vue, et masque les éléments essentiels ;
   * un calque conservé en trop perd son statut : on ne sait plus s'il est structurant ou non ;
   * un calque conservé en trop oblige à le supprimer plus tard — ce qui est un travail supplémentaire, et une source d'erreur.
La règle est simple : si l'élément n'est pas nécessaire au livrable, il est supprimé.
Le cas du PDF non vectoriel : si le fichier source est une image (PDF rasterisé, scan, JPEG), B-32 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité d'extraction filtrée. Le nettoyage est fait manuellement (par découpe des zones inutiles dans l'image), avec les limitations qui en découlent :
   * perte de la vectorisation (les cotes ne sont plus des objets, mais des pixels) ;
   * impossibilité de filtrer par calque ;
   * incertitude sur les positions (le calage est lui-même manuel).
La vue nettoyée en mode PARTIEL-DÉCLARÉ porte la mention « nettoyage manuel — calage partiel ».
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte du fichier source (DOC-02), ses calques ou entités |
| B-20 (Conception structure GO) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-30 (Calage sur dxf/dwg source) | Le fichier recalé — chaque vue nettoyée est extraite du fichier calé |
| B-31 (Preuve de superposition) | Le RDL — si une modification de source survient, les livrables avec preuve B-31 sont identifiés pour mise à jour |
| B-33 (Vérification croisée) | Le RDL — si une modification de source survient, les livrables avec vérification favorable sont identifiés pour mise à jour |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-25 (Stabilité globale, contreventement, joints) | Le fond structurel pur, support du schéma de contreventement |
| B-31 (Preuve de superposition) | La vue nettoyée — B-31 vérifie la cohérence livrable ↔ vue nettoyée |
| B-33 (Vérification croisée) | La vue nettoyée — B-33 compare le livrable à la vue nettoyée (section 1) |
| B-34 (Synthèse des réservations) | Le fond structurel pur sur lequel les réservations sont positionnées |
| B-60 (Plans d'exécution) | La vue nettoyée — B-60 produit le plan sur ce fond de plan |
| B-62 (Nomenclature et façonnage) | La vue nettoyée — B-62 s'appuie sur cette vue pour vérifier la cohérence |
| B-71 (Indiçage et supersession documentaire) | La vue nettoyée et son indice — consignés au RDL |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-32 |
| --- | --- | --- |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE (via B-30) |
| GEO-06 | Unités du fichier source | BLOQUANTE (via B-30) |
| GEO-10 | Seuils d'épaisseur de présomption porteuse (§R) | BLOQUANTE pour le §R (donnée FDC) |
| GEO-11 | Superposition des niveaux : recouvrement et écart d'axe (§R) | BLOQUANTE pour le §R (donnée FDC) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | NON BLOQUANTE (à défaut : PA-xx) |

Variables produites
B-32 ne produit pas de variable au sens du dictionnaire : sa sortie est un fichier (vue nettoyée) qui alimente B-60, B-31, B-33 et B-71.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-02, GEO-06, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Nommage, indiçage, formats | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-32, vous devez valider la liste des calques À TRANCHER. C'est votre appréciation de la nature du livrable qui fait foi — un élément peut être structurant sur un livrable et inutile sur un autre. Le modèle propose, vous décidez.
Cas particulier — plusieurs vues nettoyées pour un même livrable : si un livrable nécessite plusieurs vues nettoyées (par exemple, un plan de fondations qui s'étend sur plusieurs planches), chaque vue nettoyée est nommée avec un suffixe de planche : {{code_livrable}}_VUE-NETTOYEE_{{indice_livrable}}_{{num_planche}}.dxf. La règle de non-réutilisation reste la même : chaque vue nettoyée est propre à sa planche.
Cas particulier — calque À TRANCHER non résolu : si un calque reste À TRANCHER après la validation, il est conservé par défaut dans la vue nettoyée. Il sera tranché ultérieurement (par une nouvelle version de B-32, ou par une décision explicite). La conservation par défaut évite de supprimer un élément qui pourrait être structurant — c'est l'erreur la plus coûteuse.
Cas particulier — mise à jour incrémentale : si une modification est découverte (par exemple, le fichier source passe de l'indice B à l'indice C), B-32 est rappelée avec les mêmes paramètres. Elle consulte le RDL pour identifier les livrables impactés, puis :
   1. régénère uniquement les vues nettoyées des livrables impactés ;
   2. conserve les vues nettoyées des livrables non impactés ;
   3. consigne la mise à jour au RDL (indice précédent, indice nouveau, motif, date).
Cas particulier — modification de calage : si le calage (B-30) est modifié (par exemple, un recalage sur une nouvelle version du fichier source), toutes les vues nettoyées sont impactées — parce qu'elles sont toutes extraites du fichier calé. B-32 le signale et régénère toutes les vues nettoyées. C'est le seul cas où la mise à jour incrémentale est globale — et c'est pour cela que le calage est fait une fois (B-30), pas à chaque livrable.
Cas particulier — fichier source non vectoriel : si le fichier source est un PDF rasterisé (image), B-32 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité d'extraction filtrée. Le nettoyage est manuel, la vue nettoyée porte la mention « nettoyage manuel — calage partiel ».
Cas particulier — vue nettoyée pour la preuve de superposition (B-31) : si la vue nettoyée est produite spécifiquement pour la preuve de superposition B-31, elle peut inclure des éléments supplémentaires (par exemple, les cotes des éléments existants, pour mesurer l'écart). Dans ce cas, le nommage est : {{code_livrable}}_VUE-NETTOYEE-PREUVE_{{indice_livrable}}.dxf. La distinction permet de ne pas confondre la vue nettoyée « production » et la vue nettoyée « preuve ».
Format de sortie attendu : trois pièces distinctes (vue nettoyée, tableau de nettoyage, consignation RDL). La vue nettoyée est fournie en DXF et PDF + PNG — le DXF pour les outils, le PDF pour l'archivage, le PNG pour insertion.
Consignation : la vue nettoyée est versionnée avec le livrable et consignée au RDL (source utilisée, version du calage, indice de la vue, date). C'est cette consignation qui permet la mise à jour incrémentale en cas de modification.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.

---

## COMPLÉMENT v2.1 — §R. PROTOCOLE DE RECONNAISSANCE DES PORTEURS (obligatoire avant tout nettoyage B-32)

### R.1 Objet et champ d'application
Le nettoyage B-32 filtre un fichier ; il ne sait pas, à lui seul, distinguer un porteur d'une cloison lorsque le fichier source ne les sépare pas. Le présent protocole produit, **avant** le filtrage, la classification des parois et poteaux du fichier calé (B-30) en trois classes — PORTEUR CERTAIN, NON PORTEUR, À LEVER — qui devient l'entrée du nettoyage.
Il est **obligatoire** dès que l'une de ces conditions est remplie : les calques du fichier mélangent parois porteuses et cloisons ; la sémantique des calques est absente, incohérente ou invérifiable ; aucun plan BET ne désigne les porteurs. Si le fichier sépare déjà explicitement les porteurs (calques dédiés dont la sémantique est vérifiée sur les cotes et les annotations), le protocole se réduit aux temps R.2, R.6 et R.7 (contrôle et consignation).

### R.2 Temps 1 — Inventaire des entités (script, annexe O)
Le script (OUT-02) énumère, par niveau : entités par calque et par type (lignes, polylignes ouvertes/fermées, hachures, blocs éclatés virtuellement), épaisseurs de trait, textes et annotations. Il produit le tableau d'inventaire (OUT-03) : calque | type | nombre | rôle supposé | indices de sémantique (nom de calque, annotations rencontrées). Aucune classification n'est faite à ce stade.

### R.3 Temps 2 — Reconstruction des parois
Le script reconstruit les parois élémentaires : appariement des lignes parallèles et des polylignes fermées, mesure de l'**épaisseur** de chaque tronçon (distance entre faces), segmentation aux intersections et aux ouvertures. Chaque paroi reçoit un identifiant (niveau, repère, position, longueur, épaisseur mesurée). Les poteaux sont détectés comme rectangles fermés de faible développement, pleins ou hachurés, notamment aux intersections de parois.

### R.3bis Chaînage des tronçons en parois (obligatoire — enseignement v2.2)
La classification ne porte jamais sur des tronçons isolés : elle porte sur des **parois chaînées**. Avant les critères (R.4), le script chaîne les tronçons :
1. **Segmentation** : les tronçons sont coupés à chaque intersection (croisement, jonction en T, angle) et à chaque ouverture détectée.
2. **Regroupement** : les tronçons colinéaires ou quasi colinéaires (écart angulaire ≤ 2°, écart d'axe ≤ 2 cm) séparés par moins de 5 cm sont fusionnés en un même alignement.
3. **Appariement des faces** : les alignements parallèles distants de l'épaisseur mesurée (moins de 5 % d'écart sur la longueur commune) sont appariés comme les deux faces d'une même paroi ; l'épaisseur de la paroi est la médiane des distances mesurées, et non une valeur par tronçon.
4. **Objet paroi** : chaque paroi reçoit un identifiant unique (niveau, repère), sa longueur cumulée, son épaisseur médiane, ses faces, ses ouvertures et ses éléments associés (jambages aux extrémités des baies, poteaux incorporés détectés en R.3). Une paroi interrompue par une baie est une seule paroi avec ouverture, pas trois tronçons.
5. **Cas non chaînables** : un tronçon qui ne peut être ni regroupé ni apparié (géométrie dégradée, arc, tracé libre) reste un élément isolé, classé au plus À LEVER, et signalé dans le journal OUT-03.
C'est l'objet paroi — pas le tronçon — qui est évalué par les critères C1 à C6, porté au tableau de reconnaissance et rendu sur le plan de contrôle.



### R.4 Temps 3 — Critères de reconnaissance (convergence obligatoire)
Chaque paroi est évaluée sur les critères suivants. **Aucun critère seul ne classe.**

| N° | Critère | Mesure (script) | Signal porteur | Signal non porteur |
|---|---|---|---|---|
| C1 | Source BET | Le plan structure (DOC-03) désigne-t-il cette paroi ? | Désignée : critère souverain (V1) | — |
| C2 | Épaisseur | Épaisseur mesurée vs seuils GEO-10 | ≥ seuil haut de présomption | ≤ seuil bas (cloison) |
| C3 | Superposition des niveaux | Recouvrement de l'empreinte entre niveaux successifs (longueur commune / longueur, écart maximal) vs GEO-11 | Paroi retrouvée aux niveaux adjacents dans la tolérance | Paroi propre à un seul niveau |
| C4 | Schéma statique | Continuité vers le bas (paroi, poteau, semelle au niveau inférieur), alignement avec fondations/poutres, portées résultantes | Chaîne d'appuis complète, portées plausibles au regard du plancher | Paroi « en l'air », portée résultante incohérente |
| C5 | Position et fonction | Façade, refend, noyau (escalier, ascenseur, gaines structurantes), mitoyenneté | Position structurante | Division intérieure d'un local |
| C6 | Indices graphiques | Hachure (pleine/dense = matériau structurel), épaisseur de trait, calque, annotations (« refend », « voile », « porteur »), baies avec jambages | Indices concordants | Cloison légère, doublage, menuiserie |

Seuils de projet (FDC, jamais des constantes du carnet) :
- **GEO-10** — seuils d'épaisseur de présomption : seuil bas (au plus : cloison présumée) et seuil haut (à partir de : porteur présumé), fixés selon l'époque et le système constructif (à titre de repère à valider par projet : cloison ≤ 10 cm ; zone indéterminée 10–18 cm ; présomption porteuse ≥ 18 cm ; murs anciens : seuils spécifiques déclarés).
- **GEO-11** — superposition : recouvrement minimal (repère : 80 % de la longueur) et écart maximal d'axe entre niveaux (repère : 5 cm en régulier ; valeur déclarée en existant irrégulier).
Entre le seuil bas et le seuil haut de GEO-10, le critère C2 est neutre : la classification repose sur C3, C4, C5, C6.


### R.4bis Projection automatique des porteurs BET (critère C1 — enseignement v2.2)
Lorsqu'un plan de structure existe (DOC-03) sous forme vectorielle (DXF/DWG ou PDF vectoriel), le critère C1 n'est pas apprécié « à l'œil » : il est **projeté géométriquement**.
1. **Extraction** : le script extrait du plan BET la géométrie de ses porteurs (calques structure, traits forts, hachures béton, symboles de poteaux/jambages) selon la même méthode d'inventaire que R.2.
2. **Recalage** : la géométrie BET est recalée sur le repère du fichier calé (B-30) par la transformation du plan BET s'il en existe une, sinon par au moins trois points communs identifiés (angles, axes) avec résidu consigné ; à défaut de recalage fiable, la projection est déclarée impossible et C1 repasse en appréciation humaine tracée.
3. **Appariement** : chaque paroi chaînée (R.3bis) est appariée aux porteurs BET par recouvrement (distance d'axe ≤ tolérance GEO-11, recouvrement de longueur ≥ 50 %). Une paroi appariée reçoit C1 positif → PORTEUR CERTAIN (sauf contradiction majeure signalée).
4. **Écarts obligatoirement signalés** : tout porteur BET sans paroi archi correspondante, et toute paroi archi épaisse et superposée (C2/C3 favorables) non désignée par le BET, sont listés comme **écarts de projection** dans le tableau de reconnaissance et renvoyés à B-13/B-33 — jamais appariés de force.
5. **Cas non vectoriel** : si le plan BET n'existe qu'en raster, la projection est manuelle et déclarée (mode PARTIEL-DÉCLARÉ) ; les porteurs reportés sont qualifiés « de principe » jusqu'à validation humaine à la porte B-32.

### R.5 Temps 4 — Règle de classification
- **PORTEUR CERTAIN** : C1 positif ; ou convergence d'au moins trois critères favorables dont C3 ou C4.
- **NON PORTEUR** : C2 bas **et** C3 négatif **et** C4 sans fonction d'appui ; aucun indice contraire (C5, C6).
- **À LEVER** : tout le reste — signaux contradictoires, données insuffisantes, paroi épaisse non superposée, paroi mince en position d'appui, poteau isolé sans chaîne d'appuis lisible.
La classification est produite paroi par paroi dans le **tableau de reconnaissance** : repère | niveau | épaisseur mesurée | superposition (C3) | appui (C4) | autres indices | classe | justification. Un **plan de contrôle** rend les trois classes dans trois couleurs, superposé au fichier source.

### R.6 Temps 5 — Porte humaine et traitement des À LEVER
La liste À LEVER est soumise à l'utilisateur à la porte B-32, élément par élément, avec les signaux contradictoires. L'arbitrage est consigné (RDR ou note d'hypothèses B-22). Tant qu'un élément À LEVER n'est pas arbitré, il est **conservé** dans la vue nettoyée, en gris sur le calque EXISTANT : on ne supprime jamais un porteur possible. Si l'arbitrage est impossible sur pièces et que l'élément est dimensionnant, la brique renvoie à B-24 (existant non sondé) ou à un sondage — elle ne tranche pas.

### R.7 Temps 6 — Nettoyage et consignation
Le filtrage B-32 proprement dit s'applique alors aux classes : PORTEUR CERTAIN conservé ; NON PORTEUR supprimé selon la règle du livrable ; À LEVER conservé en EXISTANT. Le journal OUT-03 consigne les comptages par classe et par calque, les seuils GEO-10/GEO-11 utilisés et les arbitrages. B-31 vérifie ensuite qu'aucun PORTEUR CERTAIN ne manque à la vue nettoyée ; B-33 la confronte aux livrables voisins.

### R.8 Cas dégradés et interdictions
- Fichier non vectoriel (raster) : pas de reconnaissance automatique ; mode PARTIEL-DÉCLARÉ, nettoyage manuel déclaré, mention portée sur la vue.
- Il est interdit de classer sur la seule continuité géométrique d'un segment (annexe O §4.4), sur la seule sémantique d'un nom de calque non vérifiée, ou sur un seuil d'épaisseur importé d'un autre projet.
- Il est interdit de supprimer un élément À LEVER non arbitré, et de présenter le plan de contrôle des classes comme un plan de structure : c'est une pièce de travail, pas un livrable BET.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Loi d'airain graphique.** La vue nettoyée supprime 100 % des cloisons, doublages, isolants, complexes de finition et menuiseries de distribution. Seuls subsistent : les porteurs (existants, conservés, démolis, neufs), les ouvertures mécaniques (baies, trémies, percements), la trémie et l'escalier, la structure neuve et les réservations techniques.

**Protocole CAO obligatoire en quatre temps.** (1) `INSERT` récursif multi-calques : reconnaissance des blocs imbriqués et reclassement des porteurs sur le calque structurel avant toute purge ; (2) retrait du complexe isolant et des doublages périphériques (décalage d'épaisseur vers le nu porteur) ; (3) purge spatiale des portes, cotes et hachures orphelines par distance aux segments porteurs ; (4) table explicite de correspondance `Plan Archi N ↔ PB/PH` et `nu brut ASB / nu fini` (`NIV-07`).

**Différentiel explicite.** La vue porte trois états graphiques distincts et lisibles (`EXISTANT` gris fin, `DÉMOLITION` pointillé, `PROJET` trait fort) et une légende normalisée. Une vue sans différentiel exploitable est refusée.