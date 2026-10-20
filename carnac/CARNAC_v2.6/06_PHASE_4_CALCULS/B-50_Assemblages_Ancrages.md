Fichier 06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md — CARNAC v2.6
________________


B-50 — ASSEMBLAGES ET ANCRAGES
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
	Toutes les briques de calcul (B-40 à B-49) — B-50 est la brique aval qui consomme les efforts de toutes les briques amont
	Brique suivante
	B-60 (Plans d'exécution), B-70 (Auto-contrôle de synthèse)
	Modes d'appel
	COMPLET (DOC-09 fiches techniques connecteurs disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante) · PARAMÉTRIQUE (fiche technique manquante) · SANS OBJET (MPD a statué : pas d'assemblages ni d'ancrages dans le périmètre)
	Paramètre d'appel
	{{famille}} = ancrages BA / assemblages métalliques / assemblages bois / scellements maçonnerie / tous (cinq valeurs)
	Entrées lues
	MAT-01 à MAT-12, DOC-09 (fiches techniques connecteurs, résines, boulons), les efforts transmis par toutes les briques amont (B-40, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49), et les logements vérifiés par les briques aval
	Sortie unique
	Note de calcul des assemblages et ancrages + plans de détail + nomenclature + export DXF à calques ASSEMBLAGE-* + rapport de contrôle croisé entre amont et aval
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après toutes les briques de calcul (B-40 à B-49), quand le projet comporte des assemblages et ancrages à calculer. En mode SANS OBJET (pas d'assemblages ni d'ancrages dans le périmètre), B-50 produit une ligne de justification.
Ce que vous fournissez à l'IA : les efforts transmis par les briques amont (N_Ed, V_Ed, M_Ed aux nœuds), les logements vérifiés par les briques aval, les fiches techniques des connecteurs (DOC-09 : boulons, soudures, résines, sabots), les données de la FDC (matériaux). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{famille}}.
Ce que vous validez à la sortie :
   * les calculs d'assemblages (boulons, soudures, platines, tiges, sabots, équerres, scellements) ;
   * le contrôle croisé entre les ancrages calculés et les logements vérifiés par les briques amont ;
   * les écarts identifiés et les briques responsables ;
   * le rapport de contrôle croisé ;
   * l'auto-contrôle assemblage par assemblage.
B-50 est la brique pivot de l'option C (votre choix au tronçon 6) :
Brique
	Rôle sur les ancrages
	B-42 (poteaux)
	Calcule le poteau et fournit à B-50 les efforts à ancrer (N_Ed, M_Ed, section des barres). Vérifie que le poteau peut descendre ses barres jusqu'à la semelle
	B-45 (métal)
	Calcule le profilé et fournit à B-50 les efforts aux nœuds (N_Ed, V_Ed, M_Ed, nature de l'assemblage). Vérifie la pression diamétrale sur le béton
	B-44 (bois)
	Calcule l'élément bois et fournit à B-50 les efforts aux assemblages. Vérifie la compression perpendiculaire aux appuis
	B-46 (maçonnerie)
	Calcule la maçonnerie et fournit à B-50 les efforts aux scellements. Vérifie la contrainte dans la maçonnerie
	B-40 (fondations)
	Vérifie que la géométrie de la semelle permet de loger les ancrages calculés par B-50 (enrobage, espacement, hauteur)
	B-50
	Calcule les ancrages et assemblages et fait le contrôle croisé entre ce que l'amont a fourni comme efforts et ce que l'aval a prévu comme logement. Ne corrige jamais à la place des briques — il signale, identifie la brique responsable, et renvoie.
	Règle de circulation : si un ancrage ne rentre pas dans la semelle, c'est B-40 qui s'agrandit — pas B-50 qui réduit ses ancrages, pas B-42 qui réduit ses barres.
Ce que B-50 ne produit jamais :
Exclu
	Renvoyé à
	Vérification des éléments porteurs eux-mêmes (poteaux, poutres, semelles)
	B-40 à B-49 (chaque brique vérifie son élément)
	Dimensionnement des semelles, poteaux, planchers
	B-40, B-42, B-43
	Protection au feu des assemblages
	Hors périmètre CARNAC (mention générique seule)
	Choix des connecteurs pour les techniques de spécialiste (injection, précontrainte)
	Spécialiste (hors périmètre CARNAC)
	________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul des assemblages et ancrages de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour la famille {{famille}} (ancrages BA / assemblages métalliques / assemblages bois / scellements maçonnerie / tous). Tu produis :
1. Le calcul des ancrages et assemblages à partir des efforts transmis par les briques amont.
2. Le contrôle croisé avec les logements vérifiés par les briques aval.
3. Les plans de détail des assemblages.
4. Le rapport de contrôle croisé (pièce 4).


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC2 (NF EN 1992-1-1/NA) : §8.4 (ancrage des armatures), §6.7 (compression localisée), §6.4 (poinçonnement).
- EC3 (NF EN 1993-1-1/NA et NF EN 1993-1-8) : §3 (boulons), §4 (soudures), §6 (assemblages), §7 (platine).
- EC5 (NF EN 1995-1-1/NA) : §8 (assemblages bois — Johansen), §8.7 (boulons), §8.9 (sabots).
- EC6 (NF EN 1996-1-1/NA) : §8 (ancrages dans la maçonnerie).
- NF EN 1992-4 (ancrages dans le béton) pour les tiges d'ancrage et scellements.
- Fiches techniques des connecteurs (DOC-09) : capacités, classes, résistances.
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Inventaire des assemblages et ancrages du projet
Liste tous les assemblages et ancrages nécessaires :
- ancrages de poteaux BA (fournis par B-42) ;
- ancrages de dalles dans les voiles (fournis par B-43) ;
- ancrages de linteaux dans les appuis (fournis par B-49) ;
- assemblages métalliques (fournis par B-45) ;
- assemblages bois (fournis par B-44) ;
- scellements de maçonnerie (fournis par B-46) ;
- scellements de garde-corps (fournis par B-47) ;
- connexions prédalles (fournies par B-48).
Pour chaque, cite la brique amont qui a transmis les efforts.


Étape 2 — Calcul des ancrages BA (si famille = ancrages BA ou tous)
Pour chaque attente ou ancrage :
- diamètre et section des barres à ancrer (fournis par la brique amont) ;
- contrainte d'adhérence : f_bd = 2,25·η₁·η₂·f_ctd (EC2 §8.4.2) ;
- longueur d'ancrage de référence : l_b,rqd = (Φ/4)·(σ_sd/f_bd) ;
- longueur d'ancrage de calcul : l_bd = α₁·α₂·α₃·α₄·α₅·l_b,rqd (EC2 §8.4.4) ;
- en équerre : α₁ = 0,7 ;
- dépassement au-dessus de l'arase (recouvrement avec la barre du poteau : EC2 §8.7) ;
- vérification de la longueur d'ancrage minimale : l_b,min = max(0,3·l_b,rqd ; 10·Φ ; 100 mm) (EC2 §8.4.4).


Étape 3 — Calcul des assemblages métalliques (si famille = métallique ou tous)
- boulons :
  - cisaillement : F_v,Rd = α_v·f_ub·A_s/γ_M2 (EC3-1-8 §3.6) ;
  - pression diamétrale : F_b,Rd = k₁·α_b·f_u·d·t/γ_M2 ;
  - traction : F_t,Rd = k₂·f_ub·A_s/γ_M2 ;
  - interaction cisaillement + traction (EC3-1-8 §3.6.1) si applicable ;
- soudures :
  - gorge : a ≤ 0,7·t_min ;
  - contrainte : σ ⊥, τ ⊥, τ // selon EC3-1-8 §4.5 ;
  - longueur efficace : l_eff = L − 2·a ;
- platines :
  - épaisseur selon moments locaux (console, méthode de Yield Line ou méthode simplifiée) ;
  - nombre et diamètre des boulons ;
- tiges d'ancrage :
  - traction et cisaillement selon NF EN 1992-4 ;
  - longueur de scellement selon la résine (fiche technique DOC-09) ;
  - diamètre du trou et profondeur.


Étape 4 — Calcul des assemblages bois (si famille = bois ou tous)
- capacité selon Johansen (EC5 §8.2) : F_v,Rk = f_h,k·t₁·d·[√(2 + 4·M_y,Rk/(f_h,k·d·t₁²)) − 1] (assemblage simple) ;
- sabots : capacité selon fiche technique (DOC-09) et vérifications EC5 §8.9 ;
- équerres : capacité selon fiche technique et vérifications EC5 ;
- boulons : capacité selon EC5 §8.7 (cisaillement + pression diamétrale) ;
- entailles : vérification de la section nette et de la pression diamétrale.


Étape 5 — Calcul des scellements maçonnerie (si famille = maçonnerie ou tous)
- ancrages chimiques (résine) : capacité selon fiche technique, longueur de scellement, vérification de l'entraînement ;
- ancrages mécaniques : capacité selon fiche technique ;
- vérification de la contrainte dans la maçonnerie à l'emplacement du scellement (EC6 §8) ;
- distance aux bords et entraxes minimaux.


Étape 6 — Contrôle croisé (obligatoire pour toutes les familles)
Pour chaque ancrage calculé, contrôle la cohérence avec le logement vérifié par la brique aval :
- l'ancrage calculé tient-il dans le logement vérifié (enrobage, espacement, hauteur) ?
- si non : identifier la brique responsable (aval qui n'a pas assez de place, ou amont qui a sous-estimé les efforts) ;
- si l'écart est aval (B-40, B-42, B-43, B-46, B-49) : l'élément aval s'agrandit ;
- si l'écart est amont (B-44, B-45, B-47, B-48) : les efforts transmis doivent être revus ;
- B-50 ne corrige JAMAIS à la place des briques : il signale, identifie la brique responsable, et renvoie.


Étape 7 — Livrables graphiques
- ASSEMBLAGE-AXES : axes, trames, points de calage ;
- ASSEMBLAGE-DETAILS : détails à grande échelle (1/20, 1/10, 1/5) des assemblages et ancrages ;
- ASSEMBLAGE-NOMENCLATURE : nomenclature des connecteurs (boulons, soudures, tiges, résines) ;
- ASSEMBLAGE-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plans de détail à l'échelle 1/20, 1/10 ou 1/5 selon complexité ;
- coupes, élévations, nomenclature des connecteurs ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention générique de protection au feu.


Étape 8 — Auto-contrôle déclaré
Assemblage par assemblage : efforts / calcul / logement / contrôle croisé / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne vérifie PAS les éléments porteurs eux-mêmes (poteaux, poutres, semelles) : c'est le rôle de B-40 à B-49.
- Ne corrige AUCUN écart à la place des briques amont ou aval : tu signales, tu identifies la brique responsable, tu renvoies.
- Ne produis aucun assemblage sans fiche technique DOC-09 : si elle manque, mode PARAMÉTRIQUE.
- N'invente aucune capacité de connecteur : chaque capacité vient de la fiche technique.
- Ne déclare pas COMPLET si une fiche technique de connecteur manque (V12).
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu des assemblages.
- N'utilise aucune valeur « par expérience ».
- Ne fusionne pas les familles si le paramètre est restreint.
- Ne considère pas un écart de contrôle croisé comme « acceptable » : soit il est dans la tolérance justifiée, soit il est signalé et renvoyé.


SORTIE
Pièce 1 — Note de calcul des assemblages et ancrages (sections 1 à 8, avec le bloc correspondant à la famille).
Pièce 2 — Plans de détail + DXF ASSEMBLAGE-*.
Pièce 3 — Auto-contrôle déclaré (assemblage par assemblage).
Pièce 4 — Rapport de contrôle croisé
Tableau : ancrage / assemblage | effort transmis (brique amont) | calcul B-50 | logement vérifié (brique aval) | cohérence (oui / non) | si non : brique responsable, action à renvoyer.


CRITÈRE D'ACCEPTATION
- chaque assemblage et ancrage est rattaché à une brique amont qui a transmis les efforts ;
- chaque capacité de connecteur vient de la fiche technique DOC-09 ;
- les longueurs d'ancrage BA sont calculées selon EC2 §8.4 ;
- les assemblages métalliques sont calculés selon EC3-1-8 ;
- les assemblages bois sont calculés selon EC5 §8 ;
- les scellements maçonnerie sont calculés selon EC6 §8 et NF EN 1992-4 ;
- le contrôle croisé est fait pour tous les ancrages, avec identification de la brique responsable en cas d'écart ;
- B-50 n'a corrigé aucun écart à la place des briques ;
- les plans de détail portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque assemblage ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{famille}} (par ancrages BA, assemblages métalliques, assemblages bois, scellements maçonnerie ou tous). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Brique dédiée (option C, votre choix)
	Les ancrages concernent plusieurs briques à la fois : l'amont qui connaît les efforts, l'aval qui connaît les logements. Une brique dédiée centralise le calcul et le contrôle croisé, sans dupliquer les calculs dans chaque brique
	Quatre familles (BA, métallique, bois, maçonnerie)
	Chaque famille a sa méthode de calcul (EC2, EC3-1-8, EC5, EC6/NF EN 1992-4). Le paramètre force à choisir la bonne — sans lui, un modèle traite tous les ancrages comme du BA, ce qui est faux pour les autres familles
	Contrôle croisé obligatoire (étape 6)
	C'est le cœur de l'option C : vérifier que ce qui est calculé par l'amont tient dans ce qui est vérifié par l'aval. Sans ce contrôle, l'option C n'apporte rien de plus que les briques amont
	« Ne corrige aucun écart à la place des briques »
	La tentation de B-50 est de « réduire l'ancrage pour qu'il rentre » — c'est faux. Si l'ancrage ne rentre pas, c'est l'élément aval qui s'agrandit, ou l'effort amont qui est revu. B-50 ne tranche pas
	Fiche technique DOC-09 obligatoire
	Une capacité de connecteur ne s'invente pas : elle vient de la fiche technique du fabricant. Sans elle, la note n'est pas opposable
	Écart de contrôle croisé jamais « acceptable » sans justification
	Un écart de contrôle croisé non justifié est une erreur qui passe. La tolérance doit être justifiée, pas implicitement acceptée
	Rapport de contrôle croisé (pièce 4)
	C'est le livrable qui prouve que le contrôle a été fait. Sans lui, le contrôle croisé est une affirmation, pas une preuve
	« Ne vérifie pas les éléments porteurs »
	B-50 calcule les assemblages, pas les éléments assemblés. Un boulon peut tenir alors que la poutre flambe — chaque brique a son périmètre
	« Ne produis aucun assemblage sans fiche technique »
	Un assemblage sans fiche technique est un assemblage qui n'est pas opposable — les caractéristiques du connecteur (capacité, classe) sont inconnues. Le mode PARAMÉTRIQUE est la seule réponse correcte
	Filigrane + mention mode
	Un plan d'assemblage exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable
	Les quatre familles d'assemblages — méthodes de calcul :
Famille
	Méthode
	Exemples
	Ancrages BA
	EC2 §8.4 (ancrage des armatures), EC2 §8.7 (recouvrement)
	Attentes de poteaux BA, ancrages de dalles dans les voiles, ancrages de linteaux
	Assemblages métalliques
	EC3-1-8 (boulons, soudures, platines), NF EN 1992-4 (tiges d'ancrage)
	Platines de pied de poteau, assemblages poutre-poteau, sabots métalliques
	Assemblages bois
	EC5 §8 (Johansen, sabots, équerres, boulons, entailles)
	Sabots de pannes sur fermes, équerres anti-soulèvement, boulons d'assemblage
	Scellements maçonnerie
	EC6 §8 (ancrages maçonnerie), NF EN 1992-4 (ancrages chimiques)
	Scellements de chaînages rapportés, de raidisseurs, de garde-corps, de linteaux métalliques
	Le piège de la capacité de connecteur : un modèle qui reçoit un assemblage a tendance à inventer une capacité de connecteur (par exemple, « un boulon M12 tient 30 kN »). C'est faux :
   * la capacité d'un boulon dépend de sa classe (8.8, 10.9), de son diamètre, de son mode de sollicitation (cisaillement, traction), et des pièces assemblées (épaisseur, nuance) ;
   * elle est donnée par la fiche technique du fabricant (DOC-09) ;
   * sans fiche technique, la capacité est inconnue — et l'assemblage n'est pas opposable.
Un modèle qui invente une capacité produit un assemblage qui peut être sous-dimensionné (rupture) ou surdimensionné (coût).
Le piège du contrôle croisé : un modèle qui reçoit des efforts à ancrer et un logement vérifié a tendance à :
   * soit accepter l'écart (par exemple, « 5 cm de débord, c'est acceptable ») ;
   * soit corriger en réduisant l'ancrage (par exemple, « on réduit la longueur de scellement pour que ça rentre »).
Les deux sont faux :
   * un écart non justifié est une erreur qui se propage — l'ancrage ne rentre pas, il ne tiendra pas ;
   * une réduction d'ancrage non justifiée est une réduction de capacité — l'ancrage ne tiendra pas.
La seule réponse correcte est : signaler, identifier la brique responsable, renvoyer. B-50 ne corrige pas — il rend le problème visible et actionnable.
Le piège de l'interaction boulon : pour un boulon sollicité simultanément en cisaillement et en traction (par exemple, une platine de pied de poteau sous moment), il faut vérifier l'interaction (EC3-1-8 §3.6.1) :
   * F_v,Ed/F_v,Rd + F_t,Ed/(1,4·F_t,Rd) ≤ 1 ;
   * si l'interaction n'est pas vérifiée, le boulon peut casser en traction alors qu'il tient en cisaillement, ou inversement.
L'interaction est souvent oubliée — c'est une erreur qui n'apparaît pas dans les vérifications individuelles.
Le piège du groupe de boulons : pour un groupe de boulons (par exemple, 4 boulons sur une platine), la répartition des efforts n'est pas uniforme :
   * les boulons les plus éloignés du centre de gravité reprennent plus d'effort (effet de levier) ;
   * la vérification doit porter sur le boulon le plus sollicité, pas sur la moyenne ;
   * pour les platines fléchies, la méthode de Yield Line (ou une méthode simplifiée justifiée) donne la répartition.
Un calcul qui divise l'effort par le nombre de boulons sous-estime la sollicitation du boulon le plus chargé.
Le piège du scellement dans la maçonnerie : un scellement dans la maçonnerie est différent d'un scellement dans le béton :
   * la maçonnerie est hétérogène (blocs + mortier) — la résistance est plus faible au mortier ;
   * la contrainte transmise à la maçonnerie doit être vérifiée (EC6 §8) ;
   * la distance aux bords (angles, ouvertures) doit être suffisante ;
   * les entraxes minimaux doivent être respectés.
Un scellement dans la maçonnerie sans vérification de la contrainte locale est un scellement qui peut faire éclater le bloc — et tomber.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-50
	B-40 (Fondations superficielles)
	Le logement des ancrages (enrobage, espacement, hauteur) — B-50 vérifie que les ancrages y rentrent
	B-42 (Verticaux BA)
	Les efforts à ancrer (N_Ed, M_Ed, section des barres) — B-50 calcule les attentes
	B-43 (Planchers et dallages)
	Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les ancrages
	B-44 (Charpente bois)
	Les efforts aux assemblages (N_Ed, V_Ed, M_Ed, nature de l'assemblage) — B-50 calcule les sabots, équerres, boulons
	B-45 (Structure métallique)
	Les efforts aux nœuds (N_Ed, V_Ed, M_Ed, nature de l'assemblage) — B-50 calcule les boulons, soudures, platines
	B-46 (Maçonnerie)
	Les efforts aux scellements (N_Ed, V_Ed, M_Ed) — B-50 calcule les scellements
	B-47 (Escaliers)
	Les efforts aux scellements de garde-corps — B-50 calcule les scellements
	B-48 (Prédalles)
	Les efforts aux appuis et connexions — B-50 calcule les connexions
	B-49 (Linteaux et seuils)
	Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les ancrages
	B-02 (FDC)
	Les valeurs MAT-01 à MAT-12, DOC-09, avec leur fiabilité
	Briques aval
Brique
	Ce qu'elle consomme de B-50
	B-60 (Plans d'exécution)
	La note et les plans de détail — B-60 les reprend et les indice
	B-62 (Nomenclature)
	Les plans — B-62 en extrait la nomenclature détaillée (boulons, soudures, tiges, résines)
	B-70 (Auto-contrôle de synthèse)
	Le rapport de contrôle croisé — B-70 vérifie que tous les écarts ont été traités
	B-31 (Preuve de superposition)
	Les plans produits — B-31 vérifie la cohérence avec le fichier source calé
	B-33 (Vérification croisée)
	Les plans produits — B-33 vérifie la cohérence avec les autres livrables
	Variables consommées
Code
	Libellé
	Statut dans B-50
	MAT-01 à MAT-04
	Matériaux BA
	BLOQUANTE (pour ancrages BA)
	MAT-05
	Nuance d'acier métallique
	BLOQUANTE (pour assemblages métalliques)
	MAT-06
	Classe de bois
	BLOQUANTE (pour assemblages bois)
	MAT-07
	Nature et résistance de la maçonnerie existante
	BLOQUANTE (pour scellements maçonnerie)
	MAT-09 à MAT-11
	Classe de bloc, mortier, type de maçonnerie
	BLOQUANTE (pour scellements maçonnerie)
	DOC-09
	Fiches techniques produits (connecteurs, résines, boulons)
	BLOQUANTE (interdit le mode COMPLET si absente)
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-50 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans de détail + auto-contrôle + rapport de contrôle croisé) qui alimente B-60, B-62 et B-70.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	MAT-01 à MAT-11, DOC-09, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Calques ASSEMBLAGE-*, échelles, formats, cartouche
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0, en particulier C-04 (B-50 pas B-48) et D-06 (option C)
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-50, vous devez valider le rapport de contrôle croisé. C'est vous qui décidez quelle brique corrige — l'aval qui s'agrandit, ou l'amont qui revoit ses efforts. Un écart de contrôle croisé non justifié est une erreur qui passe — et qui se voit à l'exécution (ancrage qui ne tient pas, assemblage qui casse).
Cas particulier — mode PARAMÉTRIQUE (DOC-09 manquante) : si une fiche technique de connecteur n'est pas fournie (par exemple, un boulon dont on connaît la classe et le diamètre, mais pas la capacité), B-50 s'appelle en mode PARAMÉTRIQUE pour l'assemblage concerné :
   * les vérifications sont menées en littéral (avec la capacité en symbole) ;
   * un tableau de sensibilité est produit sur les capacités plausibles — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE DOC-09 » et suffixé _P ;
   * aucun plan exécutable n'est produit pour cet assemblage.
Les autres assemblages (dont la fiche technique est disponible) peuvent être en mode COMPLET — les modes sont indépendants par assemblage.
Cas particulier — mode PARTIEL-DÉCLARÉ : si une décision RDR a accepté une capacité déclarée pour un connecteur (par exemple, « capacité de 50 kN par boulon M16 8.8 retenue par décision D-07 »), B-50 s'appelle en mode PARTIEL-DÉCLARÉ — les vérifications sont complètes, mais la décision est citée avec son auteur, sa date et sa justification.
Cas particulier — ancrages BA : les ancrages BA (attentes de poteaux, ancrages de dalles) sont calculés selon EC2 §8.4. Les points sensibles :
   * la longueur d'ancrage de calcul (l_bd) dépend des conditions de mise en œuvre (α₁ à α₅) ;
   * la longueur d'ancrage minimale (l_b,min) est un plancher — un ancrage plus court n'est pas acceptable, même si le calcul le permet ;
   * le dépassement au-dessus de l'arase (recouvrement avec la barre du poteau) doit être suffisant (EC2 §8.7).
Un ancrage BA trop court est un ancrage qui glisse sous charge — c'est une ruine fragile.
Cas particulier — assemblages métalliques : les assemblages métalliques (boulons, soudures, platines) sont calculés selon EC3-1-8. Les points sensibles :
   * l'interaction cisaillement + traction (pour les boulons) ;
   * la pression diamétrale (pour les boulons sur pièces minces) ;
   * la longueur efficace des soudures (l_eff = L − 2·a) ;
   * la méthode de Yield Line pour les platines fléchies.
Un assemblage métallique sous-dimensionné est un assemblage qui casse brutalement — c'est une ruine fragile.
Cas particulier — assemblages bois : les assemblages bois (sabots, équerres, boulons, entailles) sont calculés selon EC5 §8. Les points sensibles :
   * la capacité Johansen (F_v,Rk) dépend de la densité du bois, du diamètre du boulon, de l'épaisseur des pièces ;
   * les sabots et équerres ont des capacités directionnelles (arrachement, cisaillement) — la fiche technique donne les valeurs pour chaque direction ;
   * les entailles doivent être vérifiées en section nette (pression diamétrale, cisaillement).
Un assemblage bois sous-dimensionné est un assemblage qui arrache ou qui cisaille — c'est souvent un désordre après quelques années (fatigue, humidité).
Cas particulier — scellements maçonnerie : les scellements dans la maçonnerie (chaînages rapportés, raidisseurs, garde-corps, linteaux métalliques) sont calculés selon EC6 §8 et NF EN 1992-4. Les points sensibles :
   * la résistance de la maçonnerie au droit du scellement (EC6 §8) ;
   * la distance aux bords (angles, ouvertures) ;
   * les entraxes minimaux ;
   * la longueur de scellement (résine) selon la fiche technique.
Un scellement dans la maçonnerie sans vérification de la contrainte locale est un scellement qui peut faire éclater le bloc — et tomber. C'est un désordre qui apparaît parfois plusieurs années après la pose, quand la maçonnerie se fatigue.
Cas particulier — plusieurs familles dans le même projet : si le projet comporte plusieurs familles d'assemblages (par exemple, ancrages BA + assemblages métalliques), B-50 peut être appelée en mode {{famille}} = tous — mais chaque famille garde sa propre section dans la note. Les méthodes de calcul ne se mélangent pas.
Cas particulier — rapport de contrôle croisé : le rapport de contrôle croisé (pièce 4) est le livrable le plus important de B-50. Il documente :
   * chaque ancrage calculé ;
   * l'effort transmis par la brique amont ;
   * le logement vérifié par la brique aval ;
   * la cohérence (oui / non) ;
   * en cas d'écart : la brique responsable et l'action à renvoyer.
Sans ce rapport, le contrôle croisé est une affirmation, pas une preuve. C'est le rapport qui permet à B-70 de vérifier que tous les écarts ont été traités.
Format de sortie attendu : quatre pièces distinctes (note de calcul, plans de détail, auto-contrôle déclaré, rapport de contrôle croisé). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-50 est annexée au RDR (B-03) — elle documente le calcul des assemblages et ancrages, et le rapport de contrôle croisé alimente les décisions (D-xx) et les réserves (R-xx) pour les écarts.
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
