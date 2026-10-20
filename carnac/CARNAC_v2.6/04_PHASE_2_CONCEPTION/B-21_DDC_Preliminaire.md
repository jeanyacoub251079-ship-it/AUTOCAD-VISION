Fichier 04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md — CARNAC v2.6
________________


B-21 — DESCENTE DE CHARGES PRÉLIMINAIRE
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	2 — Conception
	Brique précédente
	B-20 (Conception GO)
	Brique suivante
	B-22 (Note d'hypothèses)
	Modes d'appel
	COMPLET (CHG-01 à CHG-04 disponibles) · PARTIEL-DÉCLARÉ (usage ou poids propre déclaré par décision RDR) · PARAMÉTRIQUE (une charge d'exploitation manque mais les autres sont disponibles)
	Entrées lues
	CHG-01 à CHG-08, B-20 (conception, pour les porteurs à charger), DOC-02 (géométrie)
	Sortie unique
	Tableau de descente de charges préliminaire aux appuis (ELS et ELU) + surfaces d'influence + coefficients de continuité
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-20, avant B-22. B-21 est la DDC préliminaire — elle sert à choisir les sections en phase conception, pas à vérifier les sections (ce qui relève de B-40 à B-50).
Ce que vous fournissez à l'IA : les charges d'exploitation par usage (CHG-01, CHG-02), les poids propres des complexes de plancher (CHG-03) et de toiture (CHG-04), la géométrie (DOC-02), et les porteurs définis par B-20. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * les catégories d'usage EC1 par zone ;
   * les cloisons forfaitaires (NF EN 1991-1-1 §6.3.1.2) ;
   * les coefficients de continuité (1,15 sur appuis intermédiaires, 1,00 sur appuis de rive) ;
   * les tableaux ELS et ELU (distincts).
Ce que B-21 apporte de spécifique — la distinction préliminaire / exécution :
Aspect
	B-21 (DDC préliminaire)
	DDC d'exécution (intégrée à B-40 à B-50)
	Objet
	Choisir les sections en conception
	Vérifier les sections en exécution
	Méthode
	Surfaces d'influence rectangulaires, coefficients de continuité forfaitaires
	Surfaces d'influence exactes, coefficients de continuité issus du schéma statique réel
	Précision
	Approximative, mais justifiée
	Exacte, cumulative
	Usage
	Alimenter B-20 (choix de sections)
	Alimenter B-40 à B-50 (vérifications EC2/EC3/EC5/EC7)
	Règle de non-redondance : B-21 ne peut pas servir de DDC d'exécution. Elle est un outil de conception — elle est remplacée par les DDC détaillées des briques de calcul. Un livrable B-21 porte le titre « DDC PRÉLIMINAIRE — CONCEPTION ».
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la descente de charges PRÉLIMINAIRE de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}. Cette DDC sert à la conception (choix de sections, dimensionnement de principe). Elle NE REMPLACE PAS les DDC d'exécution des briques de calcul B-40 à B-50.


MÉTHODE
1. Pour chaque porteur (poteau, voile, semelle filante, profilé, ferme), établis la surface d'influence :
   - poteau : L_t × l_t (demi-portée adjacente dans chaque direction) ;
   - voile ou mur : largeur tributaire = somme des demi-portées des travées adjacentes, ramenée au mètre linéaire ;
   - profilé isolé : largeur tributaire = demi-entraxe de part et d'autre.
2. Décompose les charges par couche (G) et par usage (Q) :
   - charges permanentes : poids propres par couche (revêtement, chape, plancher, isolation, plafond, équipements) ;
   - charges d'exploitation : par catégorie d'usage EC1, avec cloisons forfaitaires (NF EN 1991-1-1 §6.3.1.2) ;
   - charges climatiques : neige, vent, si applicable.
3. Applique les coefficients de continuité forfaitaires :
   - 1,15 sur les charges de plancher transmises aux appuis intermédiaires (refend, transversaux, poteaux intermédiaires) ;
   - 1,00 aux appuis de rive (façades, poteaux de rive).
   Justifie le classement « appui de rive » / « appui intermédiaire » pour chaque porteur.
4. Combine selon EC0 :
   - ELS caractéristique : N_ELS = ΣG_k + Q_k,1 + Σψ₀,i·Q_k,i ;
   - ELU fondamentale : N_ELU = 1,35·ΣG_k + 1,5·Q_k,1 + 1,5·Σψ₀,i·Q_k,i.
5. Présente les résultats par porteur, en kN (poteaux) ou kN/m (murs, filantes).


INTERDICTIONS
- Ne produis AUCUNE vérification de section : c'est B-40 à B-50.
- Ne produis AUCUN ferraillage : c'est B-42, B-43, etc.
- N'utilise aucune charge « par expérience » : chaque charge est rattachée à une couche (poids propre) ou à une catégorie d'usage EC1 (exploitation).
- Ne confonds pas DDC préliminaire et DDC d'exécution : ta sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION ».
- Ne mélange pas ELS et ELU dans le même tableau : deux tableaux distincts.
- N'invente aucun coefficient de continuité : tu appliques 1,15 ou 1,00, avec justification du classement.


SORTIE
Tableau 1 — Surfaces d'influence
Porteur | L_t (m) | l_t (m) | A_inf (m²) | Justification (demi-portées adjacentes)


Tableau 2 — Charges permanentes par couche (par zone d'usage)
Zone | Couche | Épaisseur | Poids volumique | g (kN/m²) | Source (pièce ou hypothèse H-xx)


Tableau 3 — Charges d'exploitation par zone
Zone | Usage (catégorie EC1) | q_k (kN/m²) | Cloisons (kN/m²) | Total (kN/m²) | Source


Tableau 4 — Descente de charges par porteur (ELS)
Porteur | A_inf (m²) | G (kN) | Q (kN) | Coefficient de continuité | N_ELS (kN ou kN/m)


Tableau 5 — Descente de charges par porteur (ELU)
Porteur | A_inf (m²) | 1,35·G | 1,5·Q | Coefficient de continuité | N_ELU (kN ou kN/m)


Puis une synthèse de 8 lignes maximum :
- le porteur le plus chargé (en N_ELU) ;
- le porteur qui présente le plus fort ratio N/A_inf ;
- les zones où la charge d'exploitation est la plus pénalisante ;
- les hypothèses prises qui devront être confirmées en EXE.


CRITÈRE D'ACCEPTATION
La DDC préliminaire est acceptée si :
- chaque porteur a une surface d'influence justifiée ;
- chaque charge permanente est rattachée à une couche et à un poids volumique ;
- chaque charge d'exploitation est rattachée à une catégorie EC1 ;
- chaque coefficient de continuité est justifié ;
- les tableaux ELS et ELU sont distincts ;
- la sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION » ;
- aucune vérification de section ni aucun ferraillage n'a été produit.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	« DDC PRÉLIMINAIRE — CONCEPTION »
	Empêche la confusion avec les DDC d'exécution des briques de calcul. Sans ce titre, une DDC préliminaire peut être prise pour une DDC d'exécution — et les sections dimensionnées sur cette base seraient fausses
	Tableaux ELS et ELU distincts
	Un modèle a tendance à mélanger les deux dans un seul tableau « pour faire court » — ce qui rend la vérification impossible et les erreurs de combinaison invisibles. Deux tableaux forcent la rigueur
	Coefficients de continuité justifiés
	Le 1,15 forfaitaire n'a de sens que si le classement rive/intermédiaire est justifié. Un modèle qui applique 1,15 partout obtient une DDC fausse de 15 % — et une DDC fausse de 15 % produit des sections surdimensionnées ou sous-dimensionnées
	« Aucune charge par expérience »
	Une charge d'exploitation « à 2,5 kN/m² comme d'usage » est une charge non défendable. Chaque charge est rattachée à EC1 — et chaque poids propre à une couche
	Tableau 2 avec source « pièce ou hypothèse H-xx »
	Les poids propres sont souvent absents du DCE : ils doivent être déclarés comme hypothèses (H-xx dans B-22) et non présentés comme des données. Sans cette colonne, on ne sait pas si la charge est sourcée ou estimée
	« Ne mélange pas ELS et ELU »
	Une DDC qui présente un seul tableau « N » sans préciser ELS ou ELU est illisible pour un vérificateur. Les combinaisons ELS et ELU ne se mélangent pas
	Tableaux par porteur (poteau / voile / filante)
	Une DDC globale sans distinction par porteur ne permet pas de dimensionner les sections. Chaque porteur a son N_ELS et son N_ELU — c'est ce qui permet à B-20 de prédimensionner
	Synthèse en 8 lignes
	La DDC préliminaire sert à orienter la conception — pas à être lue intégralement en réunion. Les 8 lignes identifient le porteur le plus chargé et les zones pénalisantes
	« Ne produis aucune vérification de section »
	Frontière B-21 / B-40 à B-50 : la DDC préliminaire calcule les charges, pas les résistances. Une note qui vérifie les sections en B-21 est une note qui se substitue à B-40 — et qui n'a pas la rigueur de B-40
	Les coefficients de continuité — précision utile :
Type d'appui
	Coefficient
	Justification
	Appui de rive
	1,00
	La charge de plancher n'est pas continue au-delà de l'appui — le moment d'encastrement est nul
	Appui intermédiaire
	1,15
	La continuité du plancher au-delà de l'appui transmet une charge supplémentaire (moment d'encastrement) — le forfait 1,15 couvre cet effet
	Le piège du 1,15 : le coefficient de continuité est forfaitaire en phase conception. Il est exact en phase exécution (calculé par le schéma statique réel). Un modèle qui applique 1,15 partout (y compris aux appuis de rive) produit une DDC majorée de 15 % sur les rives — pas grave en conception, mais faux en exécution. C'est pourquoi la DDC préliminaire est remplacée par la DDC d'exécution dans B-40 à B-50.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-21
	B-20 (Conception GO)
	La trame et les porteurs — B-21 calcule les surfaces d'influence sur cette base
	B-00 (Inventaire)
	La référence exacte des pièces (usage des locaux, complexes de plancher)
	B-01 (MPD validée)
	Le statut de CHG-01 à CHG-08 (FOURNIE / PARTIELLE / BLOQUANTE / À PRODUIRE PAR GO)
	Briques aval
Brique
	Ce qu'elle consomme de B-21
	B-22 (Note d'hypothèses)
	Les hypothèses de charges — B-22 les consigne et les numérote
	B-20 (Conception GO)
	Les N_ELS et N_ELU par porteur — B-20 les utilise pour prédimensionner les sections
	B-40 à B-50 (Calculs)
	Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence
	Variables consommées
Code
	Libellé
	Statut dans B-21
	CHG-01
	Usage des locaux par zone (catégories EC1)
	BLOQUANTE
	CHG-02
	Surcharges d'exploitation par zone
	BLOQUANTE
	CHG-03
	Poids propres des complexes de plancher
	BLOQUANTE
	CHG-04
	Poids propres de toiture
	BLOQUANTE (si toiture dans le périmètre)
	CHG-05
	Neige
	BLOQUANTE (si toiture)
	CHG-06
	Vent
	NON BLOQUANTE (B-21 n'intègre pas le vent — c'est B-44/B-45)
	CHG-08
	Cloisons, équipements lourds, charges ponctuelles
	BLOQUANTE
	GEO-01 à GEO-04
	Géométrie et positions
	BLOQUANTE (pour les surfaces d'influence)
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-21 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (DDC préliminaire) qui alimente B-22 et B-40 à B-50.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	CHG-01 à CHG-08, GEO-01 à GEO-04, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-21, vous devez valider les catégories d'usage EC1 et les cloisons forfaitaires. C'est votre appréciation qui fait foi — un plateau technique kiné peut être classé C3 (activité) ou C4 (activité physique intense) selon l'usage réel. Le choix a un impact direct sur les sections.
Cas particulier — pas d'usage renseigné : si l'usage des locaux n'est pas clairement renseigné dans les pièces, B-21 s'appelle en mode PARTIEL-DÉCLARÉ (si une décision RDR a fixé un usage de travail) ou PARAMÉTRIQUE (si aucune décision n'a été prise). Dans les deux cas, l'usage retenu est explicitement déclaré.
Cas particulier — poids propres absents : si les complexes de plancher et de toiture ne sont pas détaillés dans le DCE, B-21 déclare des hypothèses H-xx (dans B-22) avec :
   * la couche (revêtement, chape, isolation, plafond) ;
   * l'épaisseur retenue ;
   * le poids volumique ;
   * la source (DTU, fiche technique, valeur usuelle — justifiée).
Ces hypothèses sont numérotées et tracées — elles seront reprises dans la DDC d'exécution.
Cas particulier — toiture (neige et vent) : si le projet comporte une toiture, B-21 intègre la neige dans les charges de toiture, mais pas le vent (le vent est traité par B-44 charpente bois et B-45 métal). Les combinaisons EC0 avec la neige comme action variable principale sont appliquées.
Cas particulier — charges ponctuelles : si des équipements lourds (chaudière, groupe de VMC, etc.) sont identifiés (CHG-08), ils sont traités comme des charges ponctuelles, avec la surface d'influence réduite au droit de l'équipement.
Format de sortie attendu : cinq tableaux distincts (surfaces d'influence, charges permanentes, charges d'exploitation, ELS, ELU), suivis d'une synthèse en 8 lignes maximum. Les tableaux ELS et ELU sont impérativement distincts.
Consignation : la DDC préliminaire B-21 est annexée au RDR (B-03) — elle alimente les hypothèses H-xx de B-22 et les discussions de choix de sections en B-20.
________________

