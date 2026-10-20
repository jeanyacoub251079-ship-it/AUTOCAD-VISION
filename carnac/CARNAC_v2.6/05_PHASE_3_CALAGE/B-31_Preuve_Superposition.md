Fichier 05_PHASE_3_CALAGE/B-31_Preuve_Superposition.md — CARNAC v2.6
________________


B-31 — PREUVE DE SUPERPOSITION
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
	B-30 (Calage) — et la brique qui a produit le livrable à vérifier (B-20, B-40 à B-50, B-60)
	Brique suivante
	B-33 (Vérification croisée)
	Fréquence
	À chaque livrable graphique — le livrable repose sur une superposition qui doit être prouvée
	Modes d'appel
	COMPLET (calage B-30 disponible et livrable graphique produit) · PARTIEL-DÉCLARÉ (calage en mode dégradé : la preuve est fournie avec les réserves du calage)
	Entrées lues
	Paramètres de calage B-30, livrable graphique concerné, vue nettoyée B-32 utilisée
	Sortie unique
	Preuve de superposition propre au livrable : image annotée + tableau de contrôle des positions + verdict global
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : à chaque livrable graphique produit — plans d'exécution (B-60), plans de calcul (B-40 à B-50), plans de principe (B-20). La preuve de superposition est la seule démonstration que ce que nous avons ajouté tombe sur les positions réelles.
Ce que vous fournissez à l'IA : le fichier source calé (B-30), le livrable à vérifier, la vue nettoyée (B-32) utilisée pour ce livrable. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{code_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * le tableau de contrôle élément par élément (positions prévue vs mesurée, écart, verdict) ;
   * la superposition annotée au zoom réel du livrable ;
   * les écarts (signalés, non corrigés dans la preuve) ;
   * le verdict global (livrable validé / validé sous réserve / à corriger).
Ce que B-31 apporte de spécifique — la preuve par superposition :
Aspect
	B-30 (calage)
	B-31 (preuve de superposition)
	Objet
	Établir la transformation entre le fichier source et notre repère
	Prouver que chaque ajout du livrable tombe au bon endroit
	Fréquence
	Une fois par projet
	À chaque livrable
	Sortie
	Paramètres de calage + fichier recalé
	Tableau de contrôle + superposition annotée
	Contrôle
	Résidu global sur points témoins
	Vérification élément par élément
	La règle la plus importante : B-31 ne corrige aucun écart dans la preuve. Elle signale l'écart, identifie la cause probable, et renvoie la correction à la brique source (B-20, B-40 à B-50, B-60). Une preuve qui corrige n'est plus une preuve — c'est une version corrigée non tracée.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la preuve de superposition du livrable graphique {{code_livrable}} de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, c'est-à-dire la démonstration que les éléments que nous avons ajoutés (porteurs, renforts, semelles, poteaux) tombent sur les positions réelles du fichier source calé en B-30.


MÉTHODE
1. Reprends le fichier source calé (B-30) et le livrable graphique à vérifier.
2. Superpose-les au même zoom, avec un code couleur lisible : source en gris fin, ajouts en couleur vive.
3. Vérifie les positions élément par élément, selon la nature du livrable :
   - poteaux : le symbole est-il centré sur le mur, le refend ou l'axe de trame ?
   - poutres et profilés : chaque extrémité aboutit-elle sur un appui réel (mur, poteau, sommier) ? Aucun about dans le vide ?
   - semelles : chaque semelle est-elle centrée sur son mur, avec débord de part et d'autre ? Aucune semelle flottante ?
   - ouvertures : les baies et passages sont-ils aux bonnes positions ?
4. Produis un TABLEAU DE CONTRÔLE : chaque élément ajouté, sa position prévue, sa position mesurée sur la superposition, l'écart, le verdict (conforme / écart acceptable / écart à corriger).
5. Si un écart est détecté, tu ne le corriges pas dans la preuve : tu le signales, tu identifies la cause probable (calage, saisie, saisie de la donnée), et tu renvoies la correction à la brique qui a produit le livrable (B-20, B-40 à B-50, B-60).
6. La preuve est annexée au livrable et consignée dans le RDL.


INTERDICTIONS
- Ne produis pas la preuve sur un zoom qui masque les écarts : tu produis au zoom réel du livrable, plus des zooms sur les points singuliers si nécessaire.
- Ne corrige AUCUN écart dans la preuve : tu le signales et tu renvoies la correction à la brique source.
- N'utilise pas le fichier source non calé : la preuve se fait sur le fichier calé B-30.
- Ne valide pas une preuve sans tableau de contrôle élément par élément.
- Ne déclare pas un élément « conforme » sans mesure d'écart.
- Ne produis pas la preuve en mode PARAMÉTRIQUE : soit le calage est disponible, soit le livrable ne peut pas être vérifié (et le livrable est suspendu).


SORTIE
Pièce 1 — Superposition annotée
Image PDF + PNG, au zoom réel, avec code couleur source/ajouts, et zooms sur les points singuliers.


Pièce 2 — Tableau de contrôle
Élément ajouté | Position prévue | Position mesurée | Écart | Verdict | Cause probable si écart | Brique à corriger


Pièce 3 — Synthèse
Nombre d'éléments contrôlés | Nombre conformes | Nombre d'écarts acceptables | Nombre d'écarts à corriger | Livrable validé (Oui / Non) | Si Non, briques à reprendre.


CRITÈRE D'ACCEPTATION
La preuve est acceptée si :
- la superposition est produite au zoom réel du livrable ;
- le tableau de contrôle couvre TOUS les éléments ajoutés ;
- chaque élément a une mesure d'écart (pas un simple « conforme ») ;
- les écarts sont signalés sans être corrigés dans la preuve ;
- la synthèse indique le verdict global et les briques à reprendre ;
- la preuve est annexée au livrable et consignée au RDL.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{code_livrable}} et {{mode}} (par COMPLET ou PARTIEL-DÉCLARÉ). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	À chaque livrable graphique
	Un livrable sans preuve de superposition est un livrable dont on ne sait pas s'il est calé. La preuve est la seule protection contre les erreurs de position — et les erreurs de position sont les plus coûteuses, parce qu'elles sont invisibles sur le livrable lui-même (un poteau dessiné à 10 cm de son mur paraît juste si on ne superpose pas)
	Tableau de contrôle élément par élément
	Une superposition visuelle sans mesure est une impression. Le tableau transforme la preuve en contrôle mesuré, opposable. Sans tableau, on ne peut pas dire « ce poteau est conforme » — on peut seulement dire « il a l'air bien placé »
	« Ne corrige aucun écart dans la preuve »
	Une preuve qui corrige n'est plus une preuve : c'est une version corrigée non tracée. La preuve constate, la brique source corrige. Si la preuve corrige, on ne sait plus quelle version du livrable est la bonne — et la traçabilité est rompue
	« Cause probable si écart »
	Un écart sans diagnostic de cause se reproduit. La cause identifiée (calage ? saisie ? donnée ?) permet de corriger la méthode, pas seulement l'occurrence — et donc d'éviter que le même écart ne réapparaisse sur le livrable suivant
	« Pas de preuve en PARAMÉTRIQUE »
	Un livrable PARAMÉTRIQUE (filigrané, non exécutable) n'a pas à être vérifié en position — il n'est pas exécutable. La preuve ne s'applique qu'aux livrables produits en COMPLET ou PARTIEL-DÉCLARÉ
	Zoom réel du livrable
	Un zoom sur un détail peut masquer des écarts ailleurs. La preuve doit être produite au zoom réel du livrable (celui de la production), plus des zooms sur les points singuliers si nécessaire — mais jamais seulement des zooms
	Consignation au RDL
	La preuve doit être retrouvable quand une modification de source survient — c'est ce qui permet de savoir quels livrables doivent être reprouvés. Sans RDL, la preuve est un document isolé, qui ne sert à rien en cas de modification
	Verdict global explicite
	Un tableau sans verdict est un tableau qui laisse la décision au lecteur. Le verdict global (validé / validé sous réserve / à corriger) est la conclusion de la preuve — sans lui, la preuve n'est pas actionnable
	Synthèse quantitative
	Le nombre d'éléments contrôlés, conformes, en écart acceptable, à corriger, donne une vue d'ensemble que le tableau détaillé ne donne pas. C'est ce qui permet de décider si le livrable est globalement bon ou globalement mauvais
	Les trois verdicts possibles — précision utile :
Verdict
	Définition
	Conséquence
	Conforme
	Écart mesuré ≤ tolérance de position (généralement 2 cm à l'échelle du bâtiment)
	L'élément est validé
	Écart acceptable
	Écart > tolérance, mais justifié par une contrainte (par exemple, un décalage de 5 cm pour éviter une réservation existante)
	L'élément est validé avec mention de l'écart et de sa justification
	Écart à corriger
	Écart > tolérance, non justifié
	L'élément est refusé — la brique source doit corriger
	Les trois causes probables d'écart — précision utile :
Cause
	Définition
	Action
	Calage
	L'écart vient du calage (B-30) — la transformation entre le fichier source et notre repère est fausse
	Recalculer le calage (B-30)
	Saisie
	L'écart vient de la production du livrable — la brique source a mal saisi la position
	Corriger le livrable (brique source)
	Donnée
	L'écart vient de la donnée d'entrée — la position de l'élément dans le fichier source est fausse, ou la contrainte de conception est mal transcrite
	Corriger la donnée (FDC ou B-20), puis régénérer le livrable
	Le piège du « c'est juste à quelques centimètres » : un écart de 5 cm sur un poteau peut paraître négligeable — sauf si ce poteau tombe sur une réservation existante, ou si l'écart cumulé sur plusieurs poteaux crée une trame fausse. La tolérance de position doit être fixée à l'avance (généralement 2 cm), et tout écart au-delà doit être justifié explicitement — pas implicitement accepté.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-31
	B-30 (Calage)
	Le fichier source calé (transformation validée) — la preuve se fait sur ce fichier, jamais sur le fichier source brut
	B-32 (Vue nettoyée)
	La vue nettoyée utilisée par le livrable — B-31 vérifie la cohérence livrable ↔ vue nettoyée
	Brique source du livrable (B-20, B-40 à B-50, B-60)
	Le livrable à vérifier et les positions prévues
	Briques aval
Brique
	Ce qu'elle consomme de B-31
	B-33 (Vérification croisée)
	La preuve de superposition — B-33 vérifie la cohérence plan ↔ source (section 1) en s'appuyant sur la preuve B-31
	B-70 (Auto-contrôle de synthèse)
	Le verdict de la preuve — B-70 vérifie que chaque livrable a sa preuve et que le verdict est favorable
	B-71 (Indiçage)
	La preuve annexée au livrable — chaque livrable est indiçable avec sa preuve
	B-32 (mise à jour incrémentale)
	Le RDL — si une modification de source survient, les livrables avec preuve B-31 sont identifiés pour mise à jour
	Variables consommées
Code
	Libellé
	Statut dans B-31
	DOC-02
	Plans architecte vectoriels
	BLOQUANTE (via B-30)
	GEO-07
	Transformation du fichier
	BLOQUANTE (via B-30)
	GEO-08
	Points de calage identifiés
	BLOQUANTE (via B-30)
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-31 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (preuve de superposition) qui alimente B-33, B-70, B-71 et B-32.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	DOC-02, GEO-07, GEO-08, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Nommage, indiçage, formats (PDF + PNG)
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-31, vous devez valider le verdict global avant de diffuser le livrable. Un livrable avec un verdict « à corriger » ne doit pas être diffusé — il doit être repris par la brique source. Un livrable avec un verdict « validé sous réserve » peut être diffusé, mais les écarts acceptables doivent être justifiés explicitement.
Cas particulier — livrable avec écart de calage : si l'écart vient du calage (B-30), la preuve B-31 est fausse par construction — elle mesure un écart qui n'existe pas dans le livrable. B-31 le signale et renvoie à B-30 pour recalculer le calage. La preuve est alors suspendue jusqu'à ce que le calage soit corrigé.
Cas particulier — livrable avec plusieurs types d'éléments : si le livrable contient plusieurs types d'éléments (semelles + poteaux + profilés), B-31 vérifie chaque type avec les critères qui lui sont propres :
   * semelles : centrage sur le mur, débord équilibré ;
   * poteaux : centrage sur le mur ou sur l'axe de trame ;
   * profilés : about sur un appui réel, pas dans le vide ;
   * ouvertures : position par rapport aux murs.
Chaque type a ses critères — un seul critère global masque les écarts spécifiques.
Cas particulier — livrable avec erreur de saisie détectée : si un écart est détecté et que la cause est une saisie (par exemple, un poteau saisi à 4,50 m au lieu de 4,00 m), B-31 identifie l'écart et le renvoie à la brique source. La correction est faite par la brique source, pas par B-31 — et la preuve est refaite après correction.
Cas particulier — livrable avec erreur de donnée : si l'écart vient d'une donnée fausse (par exemple, une position de poteau mal transcrite dans la FDC), B-31 identifie l'écart, mais la correction ne relève pas de la brique source du livrable — elle relève de la FDC (B-02) ou de B-20 (conception). B-31 le signale avec la brique à corriger appropriée.
Cas particulier — zoom réel vs zoom détail : B-31 exige une preuve au zoom réel du livrable. C'est souvent insuffisant pour voir les écarts faibles (par exemple, un poteau décalé de 2 cm). B-31 produit donc des zooms complémentaires sur les points singuliers :
   * les appuis (about de profilé, sommier, semelle) ;
   * les passages (baies, trémies) ;
   * les angles (coins de murs, intersections de refends).
Les zooms complètent la preuve au zoom réel, ils ne la remplacent pas.
Cas particulier — livrable en cours de production : si le livrable est en cours de production (par exemple, un plan B-60 en cours de finalisation), B-31 n'est pas appelée. La preuve ne s'applique qu'aux livrables terminés — une preuve sur un livrable inachevé est une preuve de l'état courant, pas du livrable final.
Format de sortie attendu : trois pièces distinctes (superposition annotée, tableau de contrôle, synthèse). La superposition est fournie en PDF et PNG — le PDF pour l'archivage, le PNG pour insertion dans les comptes rendus. Le tableau de contrôle couvre tous les éléments ajoutés, sans exception.
Consignation : la preuve B-31 est annexée au livrable (dans le PDF du livrable ou dans un document séparé référencé) et consignée au RDL (avec la date, l'indice du livrable, le verdict).
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.
