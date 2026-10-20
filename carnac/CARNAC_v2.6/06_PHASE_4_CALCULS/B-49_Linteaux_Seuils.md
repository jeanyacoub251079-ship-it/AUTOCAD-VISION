Fichier 06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md — CARNAC v2.6
________________


B-49 — LINTEAUX ET SEUILS
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	4 — Calculs d'exécution
	Brique précédente
	B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses), B-46 (Maçonnerie — si le linteau repose sur maçonnerie)
	Brique suivante
	B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution)
	Modes d'appel
	COMPLET (MAT-01 à MAT-04, SEC-01, GEO-05 disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante) · PARAMÉTRIQUE (SEC-01 manquante ou linteau existant non sondé) · SANS OBJET (pas de linteaux ni seuils dans le périmètre)
	Paramètre d'appel
	{{type}} = linteau BA / linteau métallique / linteau maçonnerie / seuil BA (quatre valeurs, une par appel)
	Entrées lues
	MAT-01 à MAT-04, MAT-07, SEC-01, CHG-01 à CHG-03, GEO-03, GEO-05, EXI-01, EXI-03, B-20, B-22, B-40/B-42/B-46 (appuis), B-50 (assemblages)
	Sortie unique
	Note de calcul linteaux et seuils + plans + coupes + nomenclature + export DXF à calques LINTEAU-*
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte des linteaux (BA, métalliques ou maçonnerie) ou des seuils BA à calculer. En mode SANS OBJET (pas de linteaux ni seuils dans le périmètre), B-49 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (matériaux, coupe-feu, charges, géométrie des baies), la note d'hypothèses (B-22), la conception de B-20 (linteaux prédimensionnés), la DDC préliminaire (B-21), les appuis sur les murs, poteaux ou jambages (B-42, B-46). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{type}}.
Ce que vous validez à la sortie :
   * la DDC sur le linteau (mur au-dessus, plancher, toiture) ;
   * les vérifications selon le type (EC2, EC3, EC6) ;
   * la charge triangulaire pour les linteaux courts ;
   * la longueur d'appui et la contrainte localisée ;
   * les efforts aux appuis transmis à B-50 ;
   * l'auto-contrôle par linteau.
Le périmètre exact de B-49 :
Ce que B-49 produit
	Ce que B-49 ne produit pas
	DDC sur le linteau (mur au-dessus, plancher, toiture)
	Calcul des ancrages (longueurs de scellement) — B-50
	Vérification EC2 / EC3 / EC6 selon le type
	Vérification du mur au-dessus du linteau — B-46
	Charge triangulaire pour linteaux courts
	Vérification de l'existant non sondé — B-24
	Longueur d'appui et contrainte localisée
	Dimensionnement de la protection au feu — hors CARNAC
	Dispositions constructives (enrobage, ferraillage)
	—
	Plans d'exécution (LINTEAU-*)
	—
	Le périmètre de chaque type :
Type
	Méthode
	Vérifications spécifiques
	Linteau BA
	EC2 §6.1 (flexion), §6.2.2 (effort tranchant), §9.3 (dispositions)
	V_Rd,max pour éléments courts, longueur d'appui
	Linteau métallique
	EC3 §6.2.5 (flexion), §6.2.6 (cisaillement), §6.3 (flambement/déversement)
	Pression diamétrale sur le béton ou la maçonnerie, protection anticorrosion
	Linteau maçonnerie
	EC6 §6.1 (compression), §6.2 (cisaillement), §8 (dispositions)
	Longueur d'appui, chaînage
	Seuil BA
	EC2 §6.1 (flexion), §6.2 (effort tranchant), §9.3 (dispositions)
	Liaison au dallage, joint de désolidarisation
	Ce que B-49 ne produit jamais :
Exclu
	Renvoyé à
	Calcul des ancrages (longueurs de scellement)
	B-50
	Vérification du mur au-dessus du linteau
	B-46
	Vérification de l'existant non sondé
	B-24
	Dimensionnement de la protection au feu
	Hors périmètre CARNAC (mention générique seule)
	L'articulation avec B-50 (option C) :
Brique
	Rôle sur les ancrages
	B-49
	Calcule le linteau et fournit à B-50 les efforts aux appuis et aux ancrages (N_Ed, V_Ed, M_Ed). Ne calcule pas les longueurs de scellement.
	B-50
	Calcule les ancrages (longueurs de scellement, boulons, platines) et fait le contrôle croisé avec les efforts fournis par B-49 et les logements prévus par les briques amont.
	________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution des linteaux et seuils de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour le type {{type}} (linteau BA / linteau métallique / linteau maçonnerie / seuil BA). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1) : charges.
- EC2 (NF EN 1992-1-1/NA) : §6.1 (flexion), §6.2.2 (effort tranchant — attention aux éléments courts), §9.3 (dispositions), §8.4 (ancrages).
- EC3 (NF EN 1993-1-1/NA) : §6.2.5 (flexion), §6.2.6 (cisaillement), §6.3 (flambement/déversement).
- EC6 (NF EN 1996-1-1/NA) : §6.1 (compression), §6.2 (cisaillement), §8 (dispositions linteaux maçonnerie).
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
- matériaux selon type (MAT-01 à MAT-04, MAT-07) ;
- enrobage (MAT-03), SEC-01 ;
- géométrie : portée du linteau, hauteur du mur au-dessus (GEO-03, GEO-05) ;
- existant si linteau à conserver (EXI-01, EXI-03) ;
- appuis : murs, poteaux, jambages (B-42, B-46).


Étape 2 — Descente de charges sur le linteau
- charges du mur au-dessus : poids propre × hauteur × taux d'ouvertures, décomposition par couche si mur composite ;
- charges du plancher ou de la toiture qui s'appuie sur le mur au-dessus ;
- charges concentrées éventuelles (poutres, équipements) ;
- combinaisons ELS et ELU distinctes ;
- attention : la charge du mur au-dessus n'est pas toujours linéique — pour les linteaux courts, la charge est triangulaire (méthode du triangle de charge).


Étape 3 — Vérifications selon type


BLOC A — LINTEAU BA
- flexion : M_Ed selon schéma statique (poutre sur deux appuis, éventuellement console) ;
- effort tranchant : V_Ed — attention aux linteaux courts : V_Ed est dominant, vérifier V_Ed ≤ V_Rd,max (EC2 §6.2.3) et pas seulement V_Rd,c ;
- A_s : ferraillage longitudinal, A_s,min ;
- armatures d'effort tranchant si V_Ed > V_Rd,c ;
- longueur d'appui : ancrage des barres dans les appuis, longueur d'appui ≥ 20 cm ou selon EC2 §9.3 ;
- dispositions : enrobage, espacement, cadres.


BLOC B — LINTEAU MÉTALLIQUE
- flexion : M_Ed, M_c,Rd = W_pl·f_y/γ_M0 ;
- cisaillement : V_Ed, V_pl,Rd ;
- déversement si la semelle comprimée n'est pas maintenue ;
- flèche si requise ;
- longueur d'appui : pression diamétrale sur le béton ou la maçonnerie, longueur d'appui minimale ;
- protection anticorrosion.


BLOC C — LINTEAU MAÇONNERIE
- vérification EC6 : compression, cisaillement, flambement ;
- si maçonnerie armée : ratios d'armatures ;
- longueur d'appui : ≥ 20 cm ou selon EC6 §8 ;
- dispositions : chaînage, raidisseur si nécessaire ;
- si linteau maçonnerie insuffisant : signaler et renvoyer à B-46 pour renforcement ou remplacement.


BLOC D — SEUIL BA
- flexion : seuil sur appuis, charge du mur au-dessus si applicable ;
- effort tranchant ;
- A_min et ferraillage ;
- longueur d'appui ;
- dispositions : liaison au dallage, joint de désolidarisation.


Étape 4 — Longueur d'appui et contraintes localisées
Pour chaque appui :
- longueur d'appui effective ;
- contrainte localisée à l'appui (EC2 §6.7 ou EC6 §6.1.3) ;
- si contrainte > admissible : renforcement de l'appui ou augmentation de la longueur.


Étape 5 — Dispositions constructives
- enrobage compatible avec SEC-01 ;
- ferraillage : barres principales, cadres, chapeaux ;
- ancrages dans les appuis (B-50 pour les longueurs de scellement) ;
- joints de désolidarisation avec les ouvrages adjacents si nécessaire ;
- si linteau existant à conserver : vérification EXI, renvoi B-46.


Étape 6 — Efforts aux appuis (transmis à B-50)
Pour chaque appui et chaque ancrage : N_Ed, V_Ed, M_Ed, nature de l'ancrage.


Étape 7 — Livrables graphiques
- LINTEAU-AXES : axes, trames, points de calage ;
- LINTEAU-COFFRAGE : contours, épaisseurs, cotations, longueurs d'appui ;
- LINTEAU-ACIER : ferraillage (pour linteau BA et seuil BA) ou profilé (pour linteau métallique) ;
- LINTEAU-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plans, coupes, élévations, nomenclature ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention générique de protection au feu.


Étape 8 — Auto-contrôle déclaré
Linteau par linteau : charges / vérifications / longueur d'appui / ferraillage ou section / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne calcule AUCUN ancrage (longueur de scellement) : c'est B-50.
- N'invente aucune valeur hors FDC.
- Ne traite pas un linteau court comme une poutre longue : pour un linteau court, l'effort tranchant est dominant et la charge du mur au-dessus est triangulaire (méthode du triangle de charge).
- Ne déclare pas COMPLET si SEC-01 manque (V12).
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu.
- N'utilise aucune valeur « par expérience ».
- Ne vérifie pas le mur au-dessus du linteau (c'est B-46).
- Ne réduis pas la charge du mur au-dessus « pour faire passer » le linteau.


SORTIE
Pièce 1 — Note de calcul (sections 1 à 8, avec le bloc correspondant au type).
Pièce 2 — Plans d'exécution + DXF LINTEAU-*.
Pièce 3 — Auto-contrôle déclaré.


CRITÈRE D'ACCEPTATION
- chaque donnée d'entrée est issue de la FDC ;
- la charge du mur au-dessus est calculée correctement (linéique ou triangulaire selon le cas) ;
- chaque linteau satisfait flexion, effort tranchant (V_Rd,max si court), A_min ;
- la longueur d'appui est vérifiée avec contrainte localisée ;
- chaque appui a ses efforts transmis à B-50 ;
- les plans portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque linteau ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{type}} (par linteau BA, linteau métallique, linteau maçonnerie ou seuil BA). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Brique dédiée (votre choix au tronçon 1)
	Un linteau est un élément court, avec effort tranchant dominant et charge triangulaire. Une poutre longue traitée comme un linteau court (ou l'inverse) est fausse. La brique dédiée force la méthode spécifique
	Quatre types (BA / métallique / maçonnerie / seuil)
	Chaque type a sa méthode de vérification (EC2, EC3, EC6). Le paramètre force à choisir la bonne — sans lui, un modèle traite tous les linteaux comme du BA, ce qui est faux pour les linteaux métalliques et maçonnerie
	Charge triangulaire pour les linteaux courts
	La charge du mur au-dessus d'un linteau court est triangulaire, pas linéique. C'est une erreur classique de traiter la charge comme linéique — elle sous-estime le moment de 20 à 30 %
	V_Rd,max pour les éléments courts
	Un linteau court casse par effort tranchant, pas par flexion. Vérifier seulement V_Rd,c (qui correspond à la ruine par traction diagonale) sans vérifier V_Rd,max (ruine par écrasement de la bielle) est une erreur grave — c'est la ruine fragile, qui se produit sans signe préalable
	Longueur d'appui
	Un linteau avec une longueur d'appui insuffisante peut glisser ou écraser l'appui. La longueur d'appui est aussi importante que le ferraillage — c'est la vérification qui garantit que le linteau « tient » sur ses appuis
	« Ne réduis pas la charge du mur pour faire passer »
	La tentation de réduire la charge pour éviter un linteau plus grand est une faute grave. C'est le linteau qui s'adapte, pas la charge — réduire la charge d'un mur porteur conduit à un linteau sous-dimensionné, et à un effondrement
	« Ne vérifie pas le mur au-dessus »
	La vérification du mur au-dessus du linteau relève de B-46 (maçonnerie). B-49 calcule le linteau, B-46 calcule le mur — les deux sont complémentaires, pas redondants
	« Ne calcule aucun ancrage »
	Option C — B-49 fournit les efforts, B-50 calcule les longueurs de scellement. B-49 ne peut pas calculer des ancrages dont il ne connaît pas les caractéristiques (type de scellement, résine)
	Filigrane + mention mode
	Un plan de linteau exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable
	Les quatre types de linteaux — vérifications spécifiques :
Type
	Vérifications principales
	Vérifications spécifiques
	Linteau BA
	Flexion, effort tranchant, A_min
	V_Rd,max pour linteaux courts, longueur d'appui, ferraillage d'effort tranchant
	Linteau métallique
	Flexion, cisaillement, déversement
	Pression diamétrale sur béton ou maçonnerie, protection anticorrosion
	Linteau maçonnerie
	Compression, cisaillement, flambement
	Longueur d'appui, chaînage, renvoi au spécialiste si insuffisant
	Seuil BA
	Flexion, effort tranchant, A_min
	Liaison au dallage, joint de désolidarisation
	Le piège de la charge triangulaire : un modèle qui reçoit un linteau a tendance à traiter la charge du mur au-dessus comme linéique (uniformément répartie). C'est faux pour les linteaux courts :
   * un linteau court (portée < 1,5 × hauteur du mur au-dessus) ne reprend qu'une charge triangulaire — le mur au-dessus forme un « triangle de charge » qui se reporte sur le linteau ;
   * le moment maximal n'est pas au même endroit (au centre pour une charge linéique, mais décalé vers les appuis pour une charge triangulaire) ;
   * l'effort tranchant est plus élevé aux appuis pour une charge triangulaire.
Traiter la charge comme linéique sous-estime le moment de 20 à 30 % — et sous-estime l'effort tranchant aux appuis de 10 à 20 %. C'est l'erreur la plus fréquente sur les linteaux.
Le piège de V_Rd,max : un linteau court casse par effort tranchant, pas par flexion. La vérification V_Ed ≤ V_Rd,c (EC2 §6.2.2) vérifie la ruine par traction diagonale (ruine ductile, avec fissuration préalable). La vérification V_Ed ≤ V_Rd,max (EC2 §6.2.3) vérifie la ruine par écrasement de la bielle (ruine fragile, sans signe préalable). Pour un linteau court, c'est V_Rd,max qui gouverne — et l'ignorer conduit à un linteau qui casse brutalement.
Le piège de la longueur d'appui : un linteau avec une longueur d'appui insuffisante peut :
   * glisser (si l'effort tranchant dépasse le frottement) ;
   * écraser l'appui (si la contrainte localisée dépasse la résistance du béton ou de la maçonnerie) ;
   * fissurer l'appui (si la longueur d'appui est trop faible pour répartir la contrainte).
La longueur d'appui est aussi importante que le ferraillage — un linteau parfaitement ferraillé mais mal appuyé est un linteau qui casse.
Le piège du linteau existant à conserver : si un linteau existant est à conserver, B-49 doit :
   * vérifier le linteau sous les charges réelles (via EXI-01, EXI-03) ;
   * si la vérification est insuffisante (section ou résistance non connue), s'appeler en mode PARAMÉTRIQUE (via B-24) ;
   * si le linteau est insuffisant, signaler et renvoyer à B-46 (renforcement) ou B-20 (remplacement).
B-49 ne peut pas supposer un linteau existant admissible — elle le vérifie ou elle suspend la vérification.
Le piège du seuil BA : un seuil BA est souvent traité comme une petite dalle — c'est faux :
   * le seuil reprend la charge du mur au-dessus (si le mur est porté par le seuil) ;
   * la liaison au dallage doit être désolidarisée (joint) pour éviter les fissures ;
   * la longueur d'appui doit être suffisante (≥ 20 cm ou selon EC2 §9.3).
Un seuil BA mal dimensionné fissure au contact du dallage, ou s'affaisse sous la charge du mur.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-49
	B-02 (FDC)
	Les valeurs MAT-01 à MAT-04, MAT-07, SEC-01, CHG-01 à CHG-03, GEO-03, GEO-05, avec leur fiabilité
	B-03 (RDR)
	Les décisions de périmètre (le SANS OBJET éventuel) et les décisions de valeur déclarée (PARTIEL-DÉCLARÉ)
	B-20 (Conception GO)
	La trame et les linteaux prédimensionnés
	B-21 (DDC préliminaire)
	Les ordres de grandeur des charges — B-49 refait la DDC d'exécution
	B-22 (Note d'hypothèses)
	Les hypothèses de charges et de matériaux
	B-24 (Existant non sondé)
	Les vérifications suspendues des linteaux existants — B-49 les ferme si le sondage est disponible
	B-42 (Verticaux BA)
	Les jambages BA qui reçoivent les appuis du linteau
	B-46 (Maçonnerie)
	Les murs qui reçoivent les appuis du linteau (vérification du mur au-dessus)
	B-50 (Assemblages — aval)
	Aucune donnée en amont — B-49 fournit les efforts, B-50 calcule les ancrages
	Briques aval
Brique
	Ce qu'elle consomme de B-49
	B-50 (Assemblages et ancrages)
	Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les ancrages
	B-60 (Plans d'exécution)
	La note et les plans produits — B-60 les reprend et les indice
	B-31 (Preuve de superposition)
	Les plans produits — B-31 vérifie la cohérence avec le fichier source calé
	B-33 (Vérification croisée)
	Les plans produits — B-33 vérifie la cohérence avec les autres livrables
	B-62 (Nomenclature)
	Les plans — B-62 en extrait la nomenclature détaillée (barres, profilés)
	B-70 (Auto-contrôle de synthèse)
	L'auto-contrôle B-49 — B-70 vérifie que chaque linteau a son verdict
	Variables consommées
Code
	Libellé
	Statut dans B-49
	MAT-01 à MAT-04
	Matériaux BA
	BLOQUANTE (pour linteau BA et seuil BA)
	MAT-05
	Nuance d'acier métallique
	BLOQUANTE (pour linteau métallique)
	MAT-07
	Nature et résistance de la maçonnerie
	BLOQUANTE (pour linteau maçonnerie)
	SEC-01
	Degré coupe-feu
	BLOQUANTE (interdit le mode COMPLET si absente)
	CHG-01 à CHG-03
	Usage, surcharges, poids propres
	BLOQUANTE
	GEO-03, GEO-05
	Épaisseurs de murs, baies et ouvertures
	BLOQUANTE
	EXI-01, EXI-03
	Sections et résistance de l'existant
	BLOQUANTE (si linteau existant) — sinon mode PARAMÉTRIQUE
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-49 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	MAT-01 à MAT-05, MAT-07, SEC-01, CHG-01 à CHG-03, GEO-03, GEO-05, EXI-01, EXI-03, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Calques LINTEAU-*, échelles, formats, cartouche
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-49, vous devez valider la méthode de charge (triangulaire vs linéique) pour les linteaux courts. C'est la source d'erreur la plus fréquente — et la plus coûteuse, parce qu'elle n'apparaît pas dans le résultat (le linteau « passe » avec une charge linéique, mais casse avec la charge réelle). Le modèle propose, vous décidez.
Cas particulier — mode PARAMÉTRIQUE (SEC-01 manquante ou linteau existant non sondé) : si SEC-01 (coupe-feu) n'est pas fournie pour un linteau BA, ou si un linteau existant n'a pas de section connue, B-49 s'appelle en mode PARAMÉTRIQUE :
   * les vérifications sont menées en littéral (avec la donnée manquante en symbole) ;
   * un tableau de sensibilité est produit sur les valeurs plausibles — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE [donnée] » et suffixé _P ;
   * aucun plan exécutable n'est produit.
Cas particulier — linteau court : un linteau est court si sa portée est inférieure à environ 1,5 fois la hauteur du mur au-dessus (critère variable selon les guides, à justifier). Pour un linteau court :
   * la charge du mur au-dessus est triangulaire ;
   * l'effort tranchant est dominant ;
   * V_Rd,max gouverne (pas V_Rd,c) ;
   * le ferraillage d'effort tranchant est souvent nécessaire.
Un modèle qui traite un linteau court comme une poutre longue sous-estime l'effort tranchant et sous-dimensionne le ferraillage d'âme — c'est la cause d'effondrement de nombreux linteaux anciens.
Cas particulier — linteau métallique : un linteau métallique est souvent utilisé en réhabilitation, pour renforcer une ouverture existante. Les vérifications sont :
   * flexion (EC3 §6.2.5) ;
   * cisaillement (EC3 §6.2.6) ;
   * déversement (EC3 §6.3.2) — si la semelle comprimée n'est pas maintenue ;
   * pression diamétrale sur le béton ou la maçonnerie (EC2 §6.7 ou EC6 §6.1.3) ;
   * protection anticorrosion.
La pression diamétrale est souvent oubliée — c'est la vérification qui garantit que le linteau métallique ne poinçonne pas son appui.
Cas particulier — linteau maçonnerie : un linteau maçonnerie est constitué de blocs (béton, briques) ou de pierres, avec éventuellement des armatures. Les vérifications EC6 sont :
   * compression (EC6 §6.1) ;
   * cisaillement (EC6 §6.2) ;
   * flambement (EC6 §5.5) — rare pour un linteau, mais possible si le linteau est très élancé.
Si le linteau maçonnerie est insuffisant, B-49 le signale et renvoie à B-46 (renforcement par chaînage ou raidisseur) ou à B-20 (remplacement par un linteau BA ou métallique).
Cas particulier — seuil BA : un seuil BA est un élément court, souvent sous une porte ou une fenêtre. Ses vérifications sont :
   * flexion (si le seuil porte un mur au-dessus) ;
   * effort tranchant ;
   * A_min ;
   * liaison au dallage (joint de désolidarisation) ;
   * longueur d'appui.
Un seuil BA qui n'est pas désolidarisé du dallage fissure au contact — c'est un désordre esthétique fréquent, mais qui peut aussi indiquer un problème structurel (mouvement différentiel).
Cas particulier — plusieurs linteaux identiques : si le projet comporte plusieurs linteaux identiques (même portée, même charge, même section), B-49 les traite ensemble dans la même note — mais chaque linteau a sa propre ligne dans l'auto-contrôle. Un auto-contrôle global ne détecte pas un linteau isolé mal positionné ou mal appuyé.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-49 est annexée au RDR (B-03) — elle documente le calcul des linteaux et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.


---

### COMPLÉMENT v2.0 — CALCULS, ELS ET TOLÉRANCES
1. **Adossage script (V13, annexe O §5)** : chaque application numérique de la note est produite par le script de calcul versionné avec la note (OUT-02) ; la note cite le script, ses entrées (codes FDC) et ses sorties. Aucun nombre n'est calculé « de tête » dans le texte.
2. **Combinaisons EC0 complètes** : ELU (fondamentale, accidentelle le cas échéant), ELS caractéristique, fréquente et quasi-permanente sont distinguées ; les coefficients ψ sont cités. Les vérifications de déformation et de fissuration utilisent les combinaisons ELS adaptées (quasi-permanente pour les déformations différées, caractéristique ou fréquente pour la fissuration selon le cas).
3. **Position EC8 explicite** : la note déclare, dans ses hypothèses, si l'EC8 s'applique (zone, catégorie d'importance, régularité) ou non — et pourquoi. « Non applicable » est une conclusion motivée, pas un silence.
4. **Tolérances d'exécution (NF EN 13670)** : la classe d'exécution est déclarée ; les tolérances qui conditionnent le calcul (position des armatures, Δc_dev) sont cohérentes avec l'enrobage retenu.
5. **Enrobage construit, pas seulement lu** : c_nom = c_min + Δc_dev, avec c_min = max(c_min,b ; c_min,dur ; 10 mm) selon l'EC2 §4.4, confronté à l'exigence de tenue au feu lorsqu'elle relève du lot (SEC-01). MAT-03 est la valeur résultante portée en FDC, pas une valeur devinée.

6. **Fissuration (EC2 §7.3)** : pour chaque élément BA, la note vérifie l'ouverture de fissures w_k ≤ w_max (classe d'exposition, tableau 7.1N) ou applique les règles indirectes (diamètres/espacements maximaux) en le déclarant. Une note BA sans position sur la fissuration est incomplète.
7. **Déformations (EC2 §7.4)** : flèches et rotations sont vérifiées lorsque l'élément y est sensible, avec les inerties fissurées ou les rapports portée/hauteur selon la méthode déclarée.
