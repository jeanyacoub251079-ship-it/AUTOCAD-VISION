Fichier 05_PHASE_3_CALAGE/B-30_Calage.md — CARNAC v2.6
________________


B-30 — CALAGE SUR DXF/DWG SOURCE
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	3 — Calage et vérification
	Brique précédente
	B-24 (Existant non sondé) — ou la première brique exécutable selon le PTD
	Brique suivante
	B-31 (Preuve de superposition), B-32 (Vue nettoyée), B-33 (Vérification croisée)
	Fréquence
	Une fois par projet — donnée de projet, réutilisée par toutes les briques graphiques
	Modes d'appel
	COMPLET (fichier vectoriel exploitable) · PARTIEL-DÉCLARÉ (fichier image ou PDF non vectoriel : on signale l'impossibilité de calage exact et on passe en calage manuel déclaré) · SANS OBJET (aucun fond de plan nécessaire)
	Entrées lues
	DOC-02 (plans archi vectoriels), GEO-06 (unités), GEO-07 (transformation), GEO-08 (points de calage)
	Sortie unique
	Paramètres de calage validés (transformation, points de calage, résidu) + preuve de calage initiale + fichier recalé indicé
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : au début de la phase 3, avant toute production graphique (B-31, B-32, B-60). B-30 est la brique qui établit le calage entre le fichier source et notre repère de travail. Sans elle, aucune brique graphique ne peut garantir que ses ajouts tombent sur les positions réelles.
Ce que vous fournissez à l'IA : les plans architecte vectoriels (DOC-02, DXF ou DWG), les unités déclarées, et les points de calage identifiables (angles de murs, intersections d'axes). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * les points de calage (au moins 3 non alignés, avec coordonnées dans les deux repères) ;
   * la transformation (translation, rotation, échelle) ;
   * le résidu sur les points témoins (≤ 1 cm à l'échelle du bâtiment) ;
   * la preuve de superposition initiale ;
   * le fichier recalé (nommé et indicé).
Ce que B-30 apporte de spécifique — le calage comme donnée de projet :
Aspect
	B-30 (une fois par projet)
	B-31 / B-32 / B-33 (à chaque livrable)
	Objet
	Caler le fichier source sur notre repère
	Vérifier / nettoyer / croiser chaque livrable produit
	Fréquence
	Une fois
	À chaque livrable
	Sortie
	Paramètres + fichier recalé
	Preuve / vue / rapport
	Réutilisation
	Le fichier recalé alimente toutes les briques graphiques
	Chaque brique graphique s'appuie sur le fichier recalé
	La règle la plus importante : B-30 ne calcule JAMAIS une transformation par ajustement visuel. Le calage se fait par les coordonnées vectorielles du fichier source, avec au moins 3 points non alignés et une mesure de résidu sur des points témoins. C'est ce qui garantit que le calage est reproductible — deux ingénieurs doivent aboutir au même résultat.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir le calage géométrique entre le fichier source (DXF/DWG ou PDF vectoriel) de l'opération {{ID-01}} — {{ID-02}} et le repère de travail que nous utiliserons dans tous nos livrables. Le calage est UNE FOIS établi pour le projet, puis réutilisé par toutes les briques graphiques.


MÉTHODE
1. Identifie le fichier source : nom, format, unités déclarées (GEO-06), orientation (rotation éventuelle), échelle déclarée.
2. Identifie au moins TROIS points de calage NON ALIGNÉS : angles de murs, intersections d'axes, points singuliers stables. Pour chaque point, cite les coordonnées dans le fichier source et dans le repère de travail.
3. Calcule la transformation : translation, rotation, échelle (facteur uniforme, sauf justification d'une anisotropie).
4. Vérifie le résidu de calage sur des points de contrôle NON utilisés pour le calage (points témoins). Résidu acceptable : ≤ seuil projet GEO-12 (défaut : 1 cm ouvrage neuf, 2 cm existant régulier ; au-delà, valeur déclarée au RDR — voir document maître §5). Si le résidu dépasse, tu changes de méthode (recherche d'erreur dans les points de calage ou dans les unités) — tu ne « déplaces pas à l'œil ».
5. Produis la preuve de calage : superposition du fichier source recalé sur un fond de contrôle, avec les points de calage annotés.
6. Consigne les paramètres dans le RDL : fichier source, version, transformation, résidu.


INTERDICTIONS
- Ne calcule JAMAIS une transformation par « ajustement visuel » ou « proportion d'image » : tu utilises les coordonnées vectorielles.
- N'utilise pas moins de TROIS points de calage non alignés.
- Ne valide pas un calage sans résidu mesuré sur des points témoins.
- Ne déplace aucun point pour « faire coller » : si le résidu est élevé, tu diagnostiques la cause (unités, rotation, points de calage mal choisis) et tu recalcules.
- Ne mélange pas calage et nettoyage des vues : le calage est une donnée, le nettoyage est B-32.
- Ne produis aucun plan : tu produis des paramètres de calage et une preuve.


SORTIE
Pièce 1 — Paramètres de calage
Fichier source | Format | Unités déclarées | Rotation déclarée | Transformation calculée (translation, rotation, échelle) | Points de calage utilisés | Résidu maximal sur points témoins | Résidu acceptable (Oui / Non)


Pièce 2 — Preuve de calage
Une superposition annotée : fichier source recalé + points de calage + points témoins + résidus. Format PDF + PNG.


Pièce 3 — Dossier de calage
Le fichier DXF/DWG recalé, nommé explicitement « calé » avec indice, prêt à être utilisé par B-32.


CRITÈRE D'ACCEPTATION
Le calage est accepté si :
- au moins TROIS points de calage non alignés sont identifiés avec leurs coordonnées dans les deux repères ;
- la transformation (translation, rotation, échelle) est calculée et justifiée ;
- le résidu sur points témoins est mesuré et comparé au seuil projet GEO-12 (document maître §5) ;
- la preuve de superposition est fournie en PDF et PNG ;
- le fichier recalé est nommé et indicé ;
- aucun ajustement visuel n'a été utilisé.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou SANS OBJET). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Une fois par projet, réutilisé
	Le calage est une donnée de projet : la transformation entre le DXF et notre repère ne change pas d'un livrable à l'autre. La refaire à chaque livrable est une source d'erreur — deux calages successifs peuvent différer légèrement, et les livrables ne seraient plus cohérents entre eux
	Trois points non alignés
	Deux points ne définissent qu'une droite ; trois non alignés définissent une similitude complète (translation + rotation + échelle). En dessous de trois, le calage n'est pas déterminé — et un calage non déterminé est un calage faux
	Points témoins non utilisés au calage
	Un point utilisé au calage ne prouve rien : il est forcément juste (il a servi à déterminer la transformation). Les points témoins seuls mesurent la qualité du calage — c'est le seul contrôle qui garantit que la transformation est valide partout, pas seulement aux points de calage
	« Ne déplace pas à l'œil »
	Verrou V4 — c'est la réponse directe au décalage du projet Flora. Un calage qui ne colle pas se diagnostique (unités ? rotation ? points de calage mal choisis ?), il ne se retouche pas. La retouche visuelle produit un livrable faux pour une autre raison
	Résidu ≤ 1 cm
	À l'échelle d'un bâtiment, 1 cm est la tolérance au-delà de laquelle une cote devient fausse. En dessous, l'écart est négligeable (à l'échelle 1/50, 1 cm réel = 0,2 mm papier — invisible)
	Fichier « calé » nommé et indicé
	Le fichier recalé devient une donnée de projet, pas un fichier temporaire qui se perd. Il est réutilisé par B-32 (vue nettoyée), B-31 (preuve de superposition) et B-60 (plans d'exécution). S'il est perdu, toutes les briques graphiques doivent être refaites
	Consignation au RDL
	Le RDL (Registre des Livrables) enregistre le calage comme donnée de référence. En cas de modification de source, le RDL identifie les livrables impactés — c'est ce qui permet la mise à jour incrémentale (B-32) sans tout refaire
	« Ne mélange pas calage et nettoyage »
	Le calage est une transformation géométrique (donnée) ; le nettoyage est un filtrage des calques (production). Ce sont deux opérations distinctes — les mélanger conduit à un fichier « calé-netoyé » qui n'est ni l'un ni l'autre, et qui ne peut pas être réutilisé pour un autre livrable
	Le piège du calage visuel : un modèle qui reçoit un décalage visible a tendance à déplacer les points pour les faire coïncider. C'est exactement ce qu'il faut interdire :
   * le déplacement visuel corrige le décalage à un endroit, mais ne corrige pas la cause (unités, rotation, points mal choisis) ;
   * la cause persiste, et le décalage réapparaît ailleurs — souvent de manière plus insidieuse ;
   * le résultat est un fichier qui « a l'air calé » aux points de contrôle, mais qui est faux partout ailleurs.
La règle « diagnostic avant correction » est la seule qui garantit un calage valide.
Le cas du fichier non vectoriel : si le fichier source est une image (PDF rasterisé, scan, JPEG), B-30 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité de calage exact. Le calage manuel est déclaré comme tel — il porte une incertitude qui doit être reportée sur les livrables :
   * les plans produits en mode PARTIEL-DÉCLARÉ portent la mention « calage manuel — incertitude non mesurée » ;
   * les cotes de position sont arrondies (pas de précision au mm) ;
   * les livrables exécutables sont différés jusqu'à obtention d'un fichier vectoriel.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-30
	B-00 (Inventaire)
	La référence exacte du fichier source (DOC-02), son format, ses unités déclarées
	B-01 (MPD validée)
	Le statut de DOC-02 (FOURNIE, PARTIELLE, BLOQUANTE) et de GEO-06 à GEO-08
	B-20 (Conception GO)
	La trame de référence — B-30 calcule la transformation vers cette trame
	Briques aval
Brique
	Ce qu'elle consomme de B-30
	B-31 (Preuve de superposition)
	Le fichier recalé — chaque preuve de superposition se fait sur le fichier calé, pas sur le fichier source brut
	B-32 (Vue nettoyée)
	Le fichier recalé — chaque vue nettoyée est extraite du fichier calé
	B-33 (Vérification croisée)
	Les paramètres de calage — pour vérifier la cohérence plan ↔ source
	B-60 (Plans d'exécution)
	Le fichier recalé — les plans d'exécution s'appuient sur la vue nettoyée (elle-même issue du fichier calé)
	B-71 (Indiçage)
	Le fichier recalé et son indice — consignés au RDL
	Variables consommées
Code
	Libellé
	Statut dans B-30
	DOC-02
	Plans architecte vectoriels
	BLOQUANTE
	GEO-06
	Unités du fichier source (cm/m/mm)
	BLOQUANTE
	GEO-07
	Transformation du fichier (rotation, translation, échelle)
	BLOQUANTE
	GEO-08
	Points de calage identifiés (≥ 3 non alignés)
	BLOQUANTE
	GEO-12
	Seuils géométriques du projet (document maître §5)
	BLOQUANTE (donnée FDC)
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-30 ne produit pas de variable au sens du dictionnaire : sa sortie est un dossier de calage (paramètres + preuve + fichier recalé) qui alimente toutes les briques graphiques de la phase 3 et de la phase 5.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	DOC-02, GEO-06, GEO-07, GEO-08, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Nommage, indiçage
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-30, vous devez valider le résidu de calage. Le critère objectif est le seuil projet GEO-12 (document maître §5) : 1 cm en neuf, 2 cm en existant régulier, valeur déclarée au RDR en existant irrégulier. Vous seul savez dans quelle colonne le bâtiment se situe ; un résidu supérieur au seuil mais expliqué par l'ouvrage est classé « écart justifié » et tracé au RDR — jamais retouché à l'œil.
Cas particulier — fichier source pivoté : si le fichier source est pivoté (par exemple, un plan orienté à 45° par rapport au nord), B-30 identifie la rotation déclarée (GEO-07) et la corrige dans la transformation. La preuve de calage montre le fichier source dans son orientation d'origine et dans l'orientation corrigée — pour que le lecteur puisse vérifier que la rotation a bien été appliquée.
Cas particulier — fichier source multi-calques : si le fichier DXF contient plusieurs calques (murs, cloisons, mobilier, cotations), B-30 identifie les calques utiles pour le calage (généralement les calques de murs) et ignore les autres. Le fichier recalé conserve tous les calques — c'est B-32 qui fera le filtrage.
Cas particulier — fichier source avec unités incohérentes : si le fichier DXF déclare des unités en cm mais que les cotes sont en mm, B-30 le signale et corrige la transformation en conséquence. La preuve de calage montre l'écart avant et après correction — pour que le lecteur comprenne que l'unité a été détectée et corrigée.
Cas particulier — fichier source partiel : si le fichier ne couvre qu'une partie du bâtiment (par exemple, seulement le RDC sans le R+1), B-30 le signale et limite le calage à la zone couverte. Les zones non couvertes ne peuvent pas être calées — elles sont déclarées comme telles, et les livrables qui en dépendent sont suspendus.
Cas particulier — recalage en cours de projet : si une nouvelle version du fichier source arrive (par exemple, un DXF Ind D), B-30 est rappelée pour recalculer le calage sur la nouvelle version. Les paramètres précédents sont conservés (traçabilité), et la nouvelle version est consignée au RDL avec son indice. Les livrables produits sur l'ancienne version sont impactés — B-32 (mise à jour incrémentale) les régénère.
Cas particulier — fichier source absent : si le fichier source vectoriel est absent (par exemple, seuls des PDF rasterisés sont fournis), B-30 s'appelle en mode PARTIEL-DÉCLARÉ et signale l'impossibilité de calage exact. Le calage manuel est déclaré, avec les limitations qui en découlent. Si aucun fichier source n'est disponible (ni vectoriel ni raster), B-30 s'appelle en mode SANS OBJET — et aucune brique graphique ne peut être produite.
Format de sortie attendu : trois pièces distinctes (paramètres de calage, preuve de calage, fichier recalé indicé). La preuve de calage est fournie en PDF et PNG — le PDF pour l'archivage, le PNG pour l'insertion dans les comptes rendus.
Consignation : le dossier B-30 est annexé au RDL (Registre des Livrables) — il documente le calage pour toutes les briques graphiques et permet la mise à jour incrémentale en cas de modification de source.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.
