Fichier 06_PHASE_4_CALCULS/B-42_Verticaux_BA.md — CARNAC v2.6
________________


B-42 — VERTICAUX BA (POTEAUX, JAMBAGES, VOILES)
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
	B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses)
	Brique suivante
	B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution)
	Modes d'appel
	COMPLET (MAT-01 à MAT-04 et SEC-01 disponibles) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante, notamment SEC-01) · PARAMÉTRIQUE (SEC-01 manquante : enrobage littéral + note d'attente de la donnée) · SANS OBJET (MPD a statué qu'il n'y a pas de verticaux BA neufs dans le périmètre)
	Paramètre d'appel
	{{élément}} = poteau / jambage / voile (trois valeurs, une par appel)
	Entrées lues
	MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-07, NIV-02, NIV-03, GEO-02, GEO-04, GEO-05, B-20 (conception), B-21 (DDC préliminaire), B-22 (hypothèses), B-40 (géométrie des semelles en aval), B-50 (ancrages)
	Sortie unique
	Note de calcul des verticaux BA + plans d'exécution cotés + coupes + nomenclature + export DXF à calques VERT-*
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte des verticaux en béton armé à calculer. En mode SANS OBJET (aucun vertical BA neuf dans le périmètre), B-42 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (matériaux, coupe-feu, charges), la note d'hypothèses (B-22), la conception de B-20 (sections et positions prédimensionnées), la DDC préliminaire (B-21), les positions des semelles (B-40) pour la vérification du logement des attentes. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{élément}}.
Ce que vous validez à la sortie :
   * la DDC d'exécution aux pieds des verticaux (distincte de B-21) ;
   * le dimensionnement EC2 (flambement, second ordre, N-M, biaxial) ;
   * le ferraillage EC2 (A_s, A_min, cadres ou armatures réparties) ;
   * l'enrobage compatible avec SEC-01 (coupe-feu) et MAT-02 (exposition) ;
   * les efforts à ancrer transmis à B-50 ;
   * le logement des attentes vérifié avec B-40 ;
   * l'auto-contrôle par vertical.
L'articulation avec B-50 (option C) :
Brique
	Rôle sur les ancrages
	B-42
	Calcule le vertical et fournit à B-50 les efforts à ancrer (N_Ed, M_Ed, section des barres à ancrer). Vérifie que le vertical peut descendre ses barres jusqu'à la semelle (logement compatible avec B-40). Ne calcule pas les attentes elles-mêmes.
	B-40
	Vérifie que la géométrie de la semelle permet de loger les attentes calculées par B-50 (enrobage, espacement, hauteur).
	B-50
	Calcule les attentes (longueur de scellement l_bd, retour d'équerre, dépassement) et fait le contrôle croisé entre ce que B-42 a fourni comme efforts et ce que B-40 a prévu comme logement.
	Règle de circulation : si un ancrage ne rentre pas dans la semelle, c'est B-40 qui s'agrandit — pas B-42 qui réduit ses barres, pas B-50 qui réduit ses ancrages.
Ce que B-42 ne produit jamais :
Exclu
	Renvoyé à
	Calcul des attentes (longueurs, retours, tiges)
	B-50
	Calcul des semelles qui reçoivent les verticaux
	B-40
	Calcul des planchers qui s'appuient sur les verticaux
	B-43
	Dimensionnement de la protection au feu
	Hors périmètre CARNAC (mention générique seule)
	Vérification des verticaux existants à conserver
	B-46
	________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution des verticaux en béton armé de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour l'élément {{élément}} (poteau / jambage / voile). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1) : charges d'exploitation.
- EC2 (NF EN 1992-1-1/NA) : béton armé — §5.8 (flambement), §6.1 (flexion composée), §9.5 (dispositions poteaux), §9.6 (dispositions voiles).
- Pour chaque formule, tu cites la référence exacte (EC2 §5.8.3, §5.8.8, §6.1, §9.5.2, etc.).


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
Reprends de la FDC et de la note d'hypothèses :
- classe de béton (MAT-01), classe d'exposition (MAT-02), enrobage c_nom (MAT-03), nuance d'acier (MAT-04) ;
- degré coupe-feu (SEC-01) : l'enrobage doit satisfaire à la fois la durabilité et la tenue au feu ;
- hauteur libre (NIV-03), niveaux de plancher (NIV-02) ;
- positions des verticaux (GEO-04), baies et passages (GEO-05).
Tu ne retiens AUCUNE valeur hors FDC. Si une donnée est manquante, tu appliques le mode {{mode}}.


Étape 2 — Descente de charges aux pieds des verticaux
Établis la DDC d'exécution aux pieds de chaque vertical (et non la DDC préliminaire de B-21) :
- surface d'influence par vertical (longueur tributaire × largeur tributaire) ;
- charges permanentes décomposées par couche ;
- charges d'exploitation par catégorie EC1 ;
- charges climatiques si applicable ;
- coefficients de continuité réels issus du schéma statique.
Présente un tableau par vertical : N_ELS, N_ELU, H, M au pied (excentrement éventuel).


Étape 3 — Dimensionnement EC2 — compression et flambement
Pour chaque vertical, dans chaque direction de flambement :
- élancement : λ = l₀/i, avec i = h/√12 (rectangulaire) et l₀ = k·L (k à justifier selon les liaisons) ;
- élancement limite : λ_lim = 20·A·B·C/√n (EC2 §5.8.3.1) ;
- si λ ≤ λ_lim : effets du second ordre négligeables ;
- si λ > λ_lim : second ordre par la méthode de la courbure nominale (EC2 §5.8.8) : e₂ = (1/r)·l₀²/c, avec 1/r = K_r·K_φ·(1/r₀) ;
- excentricités : e₀ = max(h/30 ; 20 mm) (EC2 §6.1(4)) ; imperfections e_i = l₀/400 (EC2 §5.8.3.2) ;
- moment de calcul : M_Ed = N_Ed·(e₀ + e_i + e₂).
Présente chaque formule littérale AVANT application numérique.


Étape 4 — Vérification de la capacité portante
Pour chaque vertical, dans chaque direction :
- diagramme d'interaction N-M par bloc rectangulaire (EC2 §6.1) ;
- M_Rd calculé à N_Ed donné ;
- taux de travail = M_Ed/M_Rd ;
- flexion biaxiale (EC2 §5.8.9) : (M_Ed,z/M_Rd,z)^a + (M_Ed,y/M_Rd,y)^a ≤ 1, exposant a interpolé.
Tu ne valides le vertical que si TOUS les taux de travail sont ≤ 1.


Étape 5 — Ferraillage EC2
- A_s,min = max(0,10·N_Ed/f_yd ; 0,002·A_c) (EC2 §9.5.2) ;
- A_s,max = 0,04·A_c (EC2 §9.5.2) ;
- choix des barres : nombre, diamètre, disposition (angles et intermédiaires) ;
- cadres (poteaux et jambages, EC2 §9.5.3) : Ø ≥ max(6 mm ; Ø_l,max/4), espacement ≤ min(20·Ø_l,min ; plus petite dimension ; 400 mm), réduit aux nœuds et aux recouvrements ;
- voiles (EC2 §9.6) : armatures réparties verticales et horizontales, ratio minimal, ferraillage de peau si h > 30 cm, pas de cadres sauf cas particulier.
Présente chaque formule et chaque choix de barres.


Étape 6 — Dispositions constructives par type d'élément
Applique le bloc correspondant à {{élément}}.


BLOC A — POTEAU
- cadres HA6 (ou diamètre selon §9.5.3) avec espacement réduit aux extrémités (zone critique) et aux recouvrements ;
- recouvrement des barres longitudinales (EC2 §8.7) : longueur l_0 = α·l_b,rqd, justifiée ;
- attentes vers le bas : effort transmis à B-50 (voir étape 7) ;
- enrobage c_nom (MAT-03) satisfaisant à la fois la durabilité et SEC-01 ;
- si le poteau reçoit un profilé métallique ou une platine, réservations prévues.


BLOC B — JAMBAGE (poteau de baie)
- cadres HA6 avec espacement réduit aux nœuds ;
- liaisonnement à la maçonnerie existante (cadres en attente dans la maçonnerie, scellement résine) : nombre et espacement des scellements ;
- attentes vers le bas : effort transmis à B-50 ;
- vérification du linteau qui repose sur le jambage : renvoi à B-49 (linteaux) ;
- enrobage compatible avec SEC-01.


BLOC C — VOILE
- armatures réparties verticales et horizontales (ratio minimal EC2 §9.6.2) ;
- ferraillage de peau si h > 30 cm ;
- pas de cadres sauf cas particulier (raidisseurs, abouts) ;
- attentes verticales en pied : effort transmis à B-50 ;
- attentes horizontales en rive si le voile est liaisonné à un autre voile ou à un plancher ;
- dispositions aux ouvertures (renforts de linteaux et de trumeaux).


Étape 7 — Efforts à ancrer (transmis à B-50)
Pour chaque vertical, fournis à B-50 les données nécessaires au calcul des attentes :
- N_Ed au pied ;
- M_Ed au pied (si excentrement) ;
- section des barres longitudinales à ancrer ;
- nombre et diamètre des barres à ancrer ;
- dépassement au-dessus de l'arase de la semelle (recouvrement avec la barre du poteau : EC2 §8.7).
Tu ne calcules PAS les longueurs d'ancrage : c'est B-50.


Étape 8 — Vérification du logement des attentes (sans les calculer)
Vérifie que le poteau peut descendre ses barres jusqu'à la semelle (B-40) :
- la section du poteau permet-elle de loger les barres avec l'enrobage et l'espacement requis ?
- l'about des barres dans la semelle est-il possible (longueur de scellement issue de B-50) ?
Si le logement n'est pas possible, tu signales et tu renvoies à B-40 (la semelle s'agrandit, le poteau ne se réduit pas).


Étape 9 — Livrables graphiques
Plans d'exécution cotés + coupes + nomenclature + export DXF à calques normalisés :
- VERT-AXES : axes, trames, points de calage ;
- VERT-COFFRAGE : sections, cotations, positions ;
- VERT-ACIER-LONG : barres longitudinales, sections, recouvrements ;
- VERT-ACIER-TRANS : cadres (poteaux et jambages), armatures réparties (voiles) ;
- VERT-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux de ferraillage.
Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche avec indice et date, la mention du mode {{mode}}, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».


Étape 10 — Auto-contrôle déclaré
Vérifie et déclare, élément par élément :
- chaque vertical a ses efforts N, H, M au pied ;
- chaque vertical a ses ferraillages longitudinaux et transversaux ;
- chaque vertical satisfait A_min et A_max ;
- chaque vertical satisfait la tenue au feu (SEC-01) par l'enrobage ;
- chaque vertical a ses efforts à ancrer fournis à B-50 ;
- chaque vertical a son logement d'attentes vérifié avec B-40 ;
- l'échelle graphique est cohérente ;
- le cartouche est complet.
Tu déclares aussi ce qui est DE PRINCIPE (hypothèses, valeurs à confirmer) et ce qui reste À LEVER.


INTERDICTIONS
- Ne calcule AUCUNE attente (longueur de scellement, retour d'équerre, tige, platine) : c'est B-50 (option C).
- N'invente aucune valeur hors FDC : si une donnée manque, tu appliques le mode {{mode}} et tu le déclares.
- Ne mélange pas ELS et ELU : deux tableaux distincts par vertical.
- Ne déclare pas COMPLET si une donnée bloquante manque (verrou V12). Notamment : SEC-01 manquante interdit COMPLET pour un élément BA.
- Ne produis aucun livrable exécutable si le mode est PARAMÉTRIQUE : livrable filigrané et suffixé _P.
- Ne dimensionne PAS la protection au feu : mention générique seule.
- N'utilise aucune valeur « par expérience » : chaque valeur vient de la FDC ou d'un calcul tracé.
- Ne recopie pas la DDC préliminaire de B-21 : tu établis la DDC d'exécution.
- Ne réduis pas les barres longitudinales pour « faire rentrer » les attentes dans la semelle : c'est B-40 qui s'agrandit.


SORTIE
Pièce 1 — Note de calcul (document texte, équations littérales avant application numérique)
Sections 1 à 10 comme ci-dessus, avec référence normative pour chaque formule.


Pièce 2 — Plans d'exécution
Plan général coté + coupes + nomenclature + export DXF à calques VERT-*. Filigrane, cartouche, indice, mention mode, mention protection au feu générique.


Pièce 3 — Auto-contrôle déclaré
Tableau par vertical : efforts / ferraillage / tenue au feu / efforts à ancrer / logement d'attentes / verdict. Points DE PRINCIPE et À LEVER.


CRITÈRE D'ACCEPTATION
La note et les plans sont acceptés si :
- chaque donnée d'entrée est issue de la FDC (aucune valeur hors FDC) ;
- la DDC d'exécution est établie (distincte de B-21) ;
- chaque vertical satisfait λ_lim et, le cas échéant, le second ordre (courbure nominale) ;
- chaque vertical satisfait l'interaction N-M et la flexion biaxiale si applicable ;
- chaque vertical satisfait A_min, A_max et les dispositions de cadres/armatures réparties selon son type ;
- chaque vertical a son enrobage compatible avec SEC-01 ;
- chaque vertical a ses efforts à ancrer fournis à B-50 ;
- chaque vertical a son logement d'attentes vérifié avec B-40 ;
- les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », l'indice, le mode et la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque vertical (verdict par vertical) ;
- aucune protection au feu n'a été dimensionnée ;
- aucune valeur hors FDC n'a été utilisée.
Si un seul de ces douze points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{élément}} (par poteau, jambage ou voile). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Paramètre {{élément}} = poteau / jambage / voile
	Les vérifications EC2 (compression, flambement, second ordre, N-M, biaxial) sont identiques pour les trois. Seules les dispositions constructives (Blocs A, B, C) changent. Un seul prompt évite la répétition de 80 % du contenu et facilite la maintenance du carnet
	Trois blocs de dispositions constructives
	Poteau = cadres. Jambage = liaisonnement à la maçonnerie. Voile = armatures réparties + ferraillage de peau. Chaque bloc est autonome dans le prompt, mais la structure de la note est commune
	« Ne calcule aucune attente : c'est B-50 »
	Option C — B-42 calcule les efforts à ancrer (étape 7), B-50 calcule les attentes (étape de B-50). C'est l'articulation qui évite les doublons
	« Ne réduis pas les barres pour faire rentrer les attentes dans la semelle »
	Point critique : si le logement d'attentes ne rentre pas dans la semelle, la tentation est de réduire les barres du poteau. C'est faux — c'est la semelle qui s'agrandit (B-40). Cette clause protège l'intégrité de la conception
	« Ne déclare pas COMPLET si SEC-01 manque »
	SEC-01 est la donnée manquante la plus coûteuse du projet Flora (40 mm d'enrobage retenus « au titre des exigences de tenue au feu » sans que ces exigences existent). Cette clause impose le mode PARAMÉTRIQUE ou une décision RDR explicite
	Enrobage satisfaisant à la fois durabilité et SEC-01
	L'enrobage n'est pas déterminé par une seule contrainte : il doit satisfaire la classe d'exposition (durabilité, MAT-02) et la tenue au feu (SEC-01). Le plus défavorable gouverne
	« Ne recopie pas la DDC préliminaire »
	Une DDC préliminaire recopiée n'a pas été vérifiée pour l'exécution. C'est l'erreur qui ne se voit pas
	Auto-contrôle par vertical
	Un auto-contrôle global ne détecte pas un vertical mal ferraillé. L'auto-contrôle par élément est le seul qui prouve chaque élément
	Mention « protection au feu adéquate à prévoir (hors lot GO) »
	Formulation imposée par votre décision de périmètre. Elle figure sur les plans sans autre précision
	« Ne déclare pas COMPLET si une donnée bloquante manque »
	Verrou V12 — un vertical BA sans SEC-01 est un vertical dont l'enrobage n'est pas justifié. Le mode doit refléter cette réalité
	Les trois blocs de dispositions constructives — précision utile :
Élément
	Dispositions principales
	Vérifications spécifiques
	Poteau
	Cadres HA6 avec espacement réduit aux extrémités (zone critique) et aux recouvrements
	Flambement dans les deux directions, interaction N-M, flexion biaxiale
	Jambage
	Cadres HA6 + liaisonnement à la maçonnerie existante (scellements résine)
	Flambement hors plan (le jambage est moins raidi dans son épaisseur), vérification du linteau (B-49)
	Voile
	Armatures réparties verticales et horizontales, ferraillage de peau si h > 30 cm, pas de cadres
	Flambement hors plan (élancement du voile), dispositions aux ouvertures
	Le piège de l'enrobage : un modèle qui reçoit SEC-01 a tendance à retenir l'enrobage minimal de durabilité, et à ignorer la tenue au feu. C'est exactement ce qu'il faut interdire :
   * l'enrobage de durabilité (MAT-02) est calculé selon EC2 §4.4.1 ;
   * l'enrobage de tenue au feu (SEC-01) est calculé selon l'EC2 partie 1-2 (structures en situation d'incendie) ;
   * le plus défavorable gouverne — et il est reporté dans la note et sur les plans.
Sur un ERP recevant du public, SEC-01 est un paramètre de conception, pas un détail. Sans SEC-01, l'enrobage n'est pas justifié — et le mode PARAMÉTRIQUE est obligatoire.
Le piège de la réduction des barres : si le logement des attentes ne rentre pas dans la semelle, un modèle a tendance à réduire les barres longitudinales du poteau — ce qui résout le problème de logement, mais affaiblit le poteau. C'est exactement ce qu'il faut interdire :
   * les barres du poteau sont dimensionnées par les vérifications EC2 (N-M, biaxial) — les réduire, c'est réduire la capacité portante ;
   * c'est la semelle qui s'agrandit (B-40) — c'est la seule solution qui préserve l'intégrité des deux éléments ;
   * cette clause force le modèle à renvoyer la correction à B-40, pas à la prendre en charge lui-même.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-42
	B-02 (FDC)
	Les valeurs MAT-01 à MAT-04, SEC-01, avec leur fiabilité
	B-03 (RDR)
	Les décisions de périmètre (le SANS OBJET éventuel) et les décisions de valeur déclarée (PARTIEL-DÉCLARÉ)
	B-20 (Conception GO)
	Les sections et positions prédimensionnées des verticaux
	B-21 (DDC préliminaire)
	Les ordres de grandeur des charges — B-42 refait la DDC d'exécution
	B-22 (Note d'hypothèses)
	Les hypothèses de charges et de matériaux
	B-40 (Fondations superficielles)
	La géométrie des semelles (dimensions, positions) — B-42 vérifie que les attentes peuvent être logées
	B-50 (Assemblages — aval)
	Aucune donnée en amont — B-42 fournit les efforts à ancrer, B-50 calcule les attentes
	Briques aval
Brique
	Ce qu'elle consomme de B-42
	B-50 (Assemblages et ancrages)
	Les efforts à ancrer (N_Ed, M_Ed, section des barres) — B-50 calcule les attentes
	B-60 (Plans d'exécution)
	La note et les plans produits — B-60 les reprend et les indice
	B-31 (Preuve de superposition)
	Les plans produits — B-31 vérifie la cohérence avec le fichier source calé
	B-33 (Vérification croisée)
	Les plans produits — B-33 vérifie la cohérence avec les autres livrables
	B-62 (Nomenclature)
	Les plans — B-62 en extrait la nomenclature détaillée (barres, cadres)
	B-70 (Auto-contrôle de synthèse)
	L'auto-contrôle B-42 — B-70 vérifie que chaque vertical a son verdict
	Variables consommées
Code
	Libellé
	Statut dans B-42
	MAT-01
	Classe de résistance du béton
	BLOQUANTE
	MAT-02
	Classe d'exposition
	BLOQUANTE
	MAT-03
	Enrobage nominal
	BLOQUANTE
	MAT-04
	Nuance d'acier BA
	BLOQUANTE
	SEC-01
	Degré coupe-feu exigé par élément
	BLOQUANTE (interdit le mode COMPLET si absente)
	CHG-01, CHG-02, CHG-03
	Usage, surcharges, poids propres
	BLOQUANTE
	CHG-07
	Sismique (si applicable)
	NON BLOQUANTE (renvoi à EC8 si présent)
	NIV-02, NIV-03
	Niveaux de plancher, hauteurs libres
	BLOQUANTE
	GEO-02, GEO-04, GEO-05
	Axes, positions des verticaux, baies
	BLOQUANTE
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-42 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-07, NIV-02, NIV-03, GEO-02, GEO-04, GEO-05, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Calques VERT-*, échelles, formats, cartouche
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-42, vous devez valider le type d'élément pour chaque vertical. Un jambage traité comme un poteau (ou l'inverse) conduit à des dispositions constructives fausses :
   * un jambage traité comme un poteau n'a pas ses cadres liaisonnés à la maçonnerie — il n'est pas solidaire du mur ;
   * un poteau traité comme un jambage a des cadres liaisonnés à une maçonnerie qui n'existe pas — il est mal ferraillé.
C'est votre appréciation qui fait foi, pas la classification du modèle.
Cas particulier — mode PARAMÉTRIQUE (SEC-01 manquante) : si SEC-01 (coupe-feu) n'est pas fournie, B-42 s'appelle en mode PARAMÉTRIQUE :
   * les vérifications EC2 (flambement, N-M, biaxial) sont menées normalement ;
   * l'enrobage de tenue au feu est traité en littéral (avec le degré coupe-feu en symbole) ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE SEC-01 » et suffixé _P ;
   * aucun plan exécutable n'est produit.
Cas particulier — SEC-01 fournie par une décision RDR : si SEC-01 est fournie par une décision RDR (par exemple, « coupe-feu 1/2 h retenu par décision D-05 »), B-42 s'appelle en mode PARTIEL-DÉCLARÉ — les vérifications sont complètes, mais la décision est citée avec son auteur, sa date et sa justification. Le livrable porte la mention « sous hypothèse SEC-01 — décision D-05 ».
Cas particulier — plusieurs verticaux du même type : si le projet comporte plusieurs poteaux, plusieurs jambages ou plusieurs voiles, B-42 traite chacun séparément :
   * un tableau de DDC par vertical ;
   * un tableau de dimensionnement par vertical ;
   * un tableau de ferraillage par vertical ;
   * un auto-contrôle par vertical.
L'auto-contrôle par vertical est indispensable — un auto-contrôle global ne détecte pas un poteau isolé mal ferraillé.
Cas particulier — vertical recevant un profilé métallique : si un vertical reçoit un profilé métallique (par exemple, un poteau BA qui reçoit une platine d'about de poutre métallique), B-42 prévoit une réservation pour la platine et les tiges d'ancrage. La vérification de la pression diamétrale sur le béton relève de B-45 (EC2 §6.7 — compression localisée), pas de B-42. B-42 prévoit le logement, B-45 vérifie la contrainte.
Cas particulier — jambage sur maçonnerie existante : si le jambage est liaisonné à une maçonnerie existante (cas Flora), B-42 prévoit :
   * le nombre et l'espacement des scellements (cadres en attente dans la maçonnerie) ;
   * la nature du scellement (résine, par exemple) ;
   * la vérification de la contrainte dans la maçonnerie à l'emplacement du scellement — qui relève de B-46 (vérification de l'existant).
B-42 ne conçoit pas le scellement dans la maçonnerie — c'est B-50 (option C) qui calcule les scellements. B-42 fournit les efforts, B-50 calcule les ancrages, B-46 vérifie la contrainte dans la maçonnerie.
Cas particulier — voile avec ouvertures : si un voile comporte des ouvertures (baies, passages), B-42 prévoit :
   * les renforts de linteaux (renvoi à B-49) ;
   * les renforts de trumeaux (armatures verticales supplémentaires) ;
   * les dispositions aux angles des ouvertures.
Un voile avec ouvertures non renforcées est un voile qui fissure aux angles — c'est une erreur qui ne se voit qu'après le coulage.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-42 est annexée au RDR (B-03) — elle documente le calcul des verticaux et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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
