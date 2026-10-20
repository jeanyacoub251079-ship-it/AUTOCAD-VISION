Fichier 06_PHASE_4_CALCULS/B-40_Fondations_Superficielles.md — CARNAC v2.6
________________


B-40 — FONDATIONS SUPERFICIELLES
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
	COMPLET (SOL-01 à SOL-05, MAT-01 à MAT-04, SEC-01 disponibles) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante) · PARAMÉTRIQUE (SOL-01 ou SOL-02 manquante : calcul littéral + tableau de sensibilité non contractuel) · SANS OBJET (MPD a statué que les fondations ne sont ni modifiées ni sollicitées)
	Entrées lues
	SOL-01 à SOL-07, MAT-01 à MAT-04, CHG-01 à CHG-03, CHG-07, GEO-01 à GEO-05, NIV-01 à NIV-04, SIT-04, SIT-05, EXI-05, B-20 (conception), B-21 (DDC préliminaire), B-22 (hypothèses), B-50 (ancrages — en aval)
	Sortie unique
	Note de calcul de fondations superficielles + plans d'exécution cotés + coupes + nomenclature + export DXF à calques FOND-*
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte des fondations superficielles à concevoir ou à vérifier. En mode SANS OBJET (fondations existantes non modifiées), B-40 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (sol, matériaux, charges), la note d'hypothèses (B-22), la conception de B-20 (semelles prédimensionnées), la DDC préliminaire (B-21), les efforts à ancrer de B-42 et B-45 (via B-50 — option C). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * la DDC d'exécution (distincte de B-21) ;
   * le dimensionnement EC7 (portance, homothétie, rigidité, excentricité) ;
   * le ferraillage EC2 (A_s, A_min, poinçonnement, dispositions) ;
   * le logement des ancrages (sans les calculer — c'est B-50) ;
   * les dispositions constructives (béton de propreté, enrobage, arase, distance de sécurité) ;
   * l'auto-contrôle par semelle.
L'articulation avec B-50 (option C) :
Brique
	Rôle sur les ancrages
	B-40
	Vérifie que la géométrie de la semelle permet de loger les ancrages calculés par B-50 (enrobage, espacement, hauteur). Ne calcule pas les ancrages eux-mêmes
	B-42 / B-45
	Fournissent à B-50 les efforts à ancrer (N_Ed, M_Ed, section des barres, tiges)
	B-50
	Calcule les ancrages (longueurs de scellement, tiges, platines, retours) et fait le contrôle croisé avec les logements vérifiés par B-40
	Règle de circulation : si un ancrage ne rentre pas dans la semelle, c'est B-40 qui s'agrandit — pas B-50 qui réduit ses ancrages, pas B-42 qui réduit ses barres.
Ce que B-40 ne produit jamais :
Exclu
	Renvoyé à
	Calcul des ancrages (longueurs de scellement, tiges, platines)
	B-50
	Calcul des poteaux et de leurs attentes
	B-42
	Vérification des éléments existants sous semelle
	B-46
	Dimensionnement de la protection au feu
	Hors périmètre CARNAC (mention générique seule)
	Étude géotechnique
	Hors périmètre CARNAC (audit B-12, recommandation de mission)
	________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution des fondations superficielles de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, et produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) et son Annexe Nationale : combinaisons.
- EC1 (NF EN 1991-1-1) : charges d'exploitation.
- EC2 (NF EN 1992-1-1/NA) : béton armé.
- EC7 (NF EN 1997-1) et NF P 94-261 : fondations superficielles.
- Pour chaque formule, tu cites la référence normative exacte (EC2 §6.5, EC7 §6.5.2, NF P 94-261 §…).


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
Reprends les données de la FDC (B-02) et de la note d'hypothèses (B-22) :
- q_ELS, q_ELU (SOL-01, SOL-02) ;
- ancrage minimal dans le bon sol (SOL-03) ;
- classe d'agressivité du sol (SOL-05) ;
- classe de béton, classe d'exposition, enrobage (MAT-01, MAT-02, MAT-03) ;
- nuance d'acier BA (MAT-04).
Tu ne retiens AUCUNE valeur hors FDC. Si une donnée est manquante, tu appliques le mode {{mode}}.


Étape 2 — Descente de charges aux semelles
Établis la DDC d'exécution aux semelles (et non la DDC préliminaire de B-21) :
- surfaces d'influence par semelle, justifiées par la géométrie B-20 ;
- charges permanentes décomposées couche par couche ;
- charges d'exploitation par catégorie EC1 ;
- coefficients de continuité réels issus du schéma statique (pas de forfait 1,15 systématique) ;
- combinaisons ELS et ELU distinctes.
Présente un tableau par semelle : N_ELS, N_ELU, H, M (si excentrement).


Étape 3 — Dimensionnement géométrique EC7 / NF P 94-261
Pour chaque semelle (isolée et filante) :
- vérification de portance ELS : σ_ELS = N_ELS/A ≤ q_ELS ;
- vérification de portance ELU : σ_ELU = N_ELU/A ≤ q_ELU ;
- condition d'homothétie : débords équilibrés, pas de semelle « en L » non justifiée ;
- condition de rigidité : d ≥ (B − b)/4 dans chaque direction (méthode des bielles applicable) ;
- excentricité : e/B ≤ 1/6.
Tu ne retiens la géométrie que si TOUTES les conditions sont satisfaites. Sinon tu dimensionnes plus grand.


Étape 4 — Ferraillage EC2
- Méthode des bielles (EC2 §6.5 et §9.8) si la semelle est rigide ;
- Méthode de flexion (EC2 §6.1) si la semelle est souple ;
- A_s calculé par la formule correspondante ;
- A_s,min = max(0,26·f_ctm/f_yk·b·d ; 0,0013·b·d) (EC2 §9.2.1.1) ;
- vérification du poinçonnement (EC2 §6.4) : v_Ed ≤ v_Rd,c ;
- dispositions constructives (EC2 §9.8.3) : enrobage, espacement, courbure des barres.
Présente chaque formule littérale AVANT l'application numérique.


Étape 5 — Vérification du logement des ancrages (sans les calculer)
Les ancrages (tiges, attentes BA) sont calculés par B-50. Tu vérifies seulement que la géométrie de la semelle permet de les loger :
- enrobage suffisant pour les tiges d'ancrage ou les attentes ;
- espacement suffisant entre ancrages ;
- hauteur de semelle suffisante pour le scellement des attentes (longueur de scellement l_bd issue de B-50).
Si la géométrie ne permet pas de loger les ancrages calculés par B-50, tu modifies la semelle et tu le signales.


Étape 6 — Dispositions constructives
- béton de propreté 5 cm sous toute semelle ;
- enrobage c_nom (MAT-03) ;
- joint de désolidarisation entre semelle et dallage (si dallage adjacent) ;
- distance de sécurité aux soubassements existants (SIT-04) : blindage systématique en fouille à moins de 1,50 m d'un soubassement existant ;
- interdiction de déchausser les fondations existantes ;
- arase étanche sur toutes les têtes de semelle.


Étape 7 — Livrables graphiques
Plans d'exécution cotés + coupes + nomenclature + export DXF à calques normalisés :
- FOND-AXES : axes, trames, points de calage ;
- FOND-COFFRAGE : semelles, bêches, soubassements, arases, cotations ;
- FOND-ACIER-INF : nappes inférieures, sections, espacements, longueurs ;
- FOND-ACIER-SUP : nappes supérieures si nécessaire ;
- FOND-HABILLAGE-TEXTE : textes, légendes, cartouche, notes.
Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche avec indice et date, et la mention du mode {{mode}}.


Étape 8 — Auto-contrôle déclaré
Vérifie et déclare :
- chaque semelle est centrée sur son mur, avec débord équilibré ;
- chaque appui de poteau est positionné sur sa semelle ;
- chaque semelle a son ferraillage complet (nappes, attentes, recouvrements) ;
- chaque semelle a son logement d'ancrage compatible avec B-50 ;
- l'échelle graphique est cohérente ;
- le cartouche est complet.
Tu déclares aussi ce qui est DE PRINCIPE (hypothèses, valeurs à confirmer) et ce qui reste À LEVER.


INTERDICTIONS
- Ne calcule AUCUN ancrage (tige, platine, longueur de scellement) : c'est B-50 (option C).
- N'invente aucune valeur hors FDC : si une donnée manque, tu appliques le mode {{mode}} et tu le déclares.
- Ne mélange pas ELS et ELU : deux tableaux distincts par semelle.
- Ne déclare pas un mode COMPLET si une donnée bloquante manque (verrou V12).
- Ne produis aucun livrable exécutable si le mode est PARAMÉTRIQUE : le livrable est filigrané « PROVISOIRE — EN ATTENTE DE [donnée] » et suffixé _P.
- Ne dimensionne PAS la protection au feu : tu mentionnes « une protection au feu adéquate doit être prévue » sans autre précision.
- N'utilise aucune valeur « par expérience » : chaque valeur vient de la FDC ou d'un calcul tracé.
- Ne recopie pas la DDC préliminaire de B-21 : tu établis la DDC d'exécution.


SORTIE
Pièce 1 — Note de calcul (document texte, avec équations littérales avant application numérique)
Sections 1 à 8 comme ci-dessus. Chaque formule littérale est suivie de son application numérique, avec la référence normative.


Pièce 2 — Plans d'exécution
Plan général coté + coupes + nomenclature + export DXF à calques FOND-*. Filigrane, cartouche, indice.


Pièce 3 — Auto-contrôle déclaré
Tableau par semelle : extrémité / appui / logement d'ancrage / ferraillage / verdict. Points DE PRINCIPE et À LEVER.


CRITÈRE D'ACCEPTATION
La note et les plans sont acceptés si :
- chaque donnée d'entrée est issue de la FDC (aucune valeur hors FDC) ;
- la DDC d'exécution est établie (distincte de la DDC préliminaire B-21) ;
- chaque semelle satisfait portance ELS et ELU, homothétie, rigidité, excentricité ;
- chaque ferraillage satisfait EC2 §9.2.1.1 (A_min) et §6.4 (poinçonnement) ;
- le logement des ancrages est vérifié (sans être calculé) ;
- les dispositions constructives sont présentes (béton de propreté, enrobage, joint, arase, distance de sécurité) ;
- les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » et l'indice ;
- l'auto-contrôle déclare chaque semelle (verdict par semelle) ;
- aucune protection au feu n'a été dimensionnée ;
- aucune valeur hors FDC n'a été utilisée.
Si un seul de ces dix points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ, PARAMÉTRIQUE ou SANS OBJET). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	DDC d'exécution distincte de B-21
	La DDC préliminaire sert à choisir les sections en conception ; la DDC d'exécution est cumulative et exacte. Les confondre conduit à des sections fausses en EXE — c'est exactement l'erreur qui menace toute étude
	« Aucune valeur hors FDC »
	Verrou V3 — une valeur « par expérience » dans une note de calcul n'est pas défendable en réunion de chantier. Chaque valeur vient d'une pièce citée ou d'un calcul tracé
	« Ne calcule aucun ancrage : c'est B-50 »
	Option C — l'ancrage est calculé par la brique qui connaît les efforts à ancrer (B-42 pour les attentes de poteaux BA, B-45 pour les tiges de poteaux métalliques), et le logement est vérifié par B-40. B-40 ne peut pas calculer des ancrages dont il ne connaît pas les efforts
	« Tu vérifies seulement que la géométrie permet de les loger »
	La nuance est capitale : B-40 ne calcule pas les ancrages, mais il doit s'assurer qu'ils rentrent. Si la semelle ne permet pas de loger les ancrages de B-50, c'est B-40 qui doit s'agrandir — pas B-50 qui doit réduire ses ancrages
	« Ne déclare pas COMPLET si une donnée bloquante manque »
	Verrou V12 — une note de calcul COMPLET sans q_adm est une note fausse. Le mode doit refléter la réalité
	ELS et ELU distincts
	Les combinaisons ELS et ELU ne se mélangent pas : une note de calcul qui présente un seul tableau « N » sans préciser ELS ou ELU est illisible pour un vérificateur
	« Ne recopie pas la DDC préliminaire »
	Une DDC préliminaire recopiée en DDC d'exécution est une DDC d'exécution qui n'a pas été vérifiée — c'est exactement le type d'erreur qui ne se voit pas
	Auto-contrôle par semelle
	Un auto-contrôle global ne détecte pas une semelle mal centrée ou un ferraillage manquant sur une semelle. L'auto-contrôle par semelle est le seul qui prouve que chaque élément a été vérifié
	Filigrane + mention mode
	Un plan de fondations exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté. La mention du mode est une protection
	« Ne dimensionne pas la protection au feu »
	Exclusion CARNAC explicite. La mention générique est autorisée, le dimensionnement ne l'est pas
	Le mode PARAMÉTRIQUE en pratique — précision utile :
Situation
	Ce que B-40 produit
	Ce qu'elle ne produit pas
	COMPLET
	Note complète, plans cotés, DXF, auto-contrôle
	—
	PARTIEL-DÉCLARÉ
	Note avec valeur déclarée au RDR, mention de l'auteur et de la date, plans portant la mention « sous hypothèse H-xx »
	Une valeur choisie par le modèle
	PARAMÉTRIQUE
	Formules littérales avec q_adm en symbole, tableau de sensibilité non contractuel, note filigranée « EN ATTENTE DE SOL-01 »
	Aucune valeur retenue, aucun plan exécutable, aucun DXF à diffuser
	SANS OBJET
	Ligne de justification (« fondations existantes non sollicitées, motif : travaux de superstructure »)
	Aucun calcul, aucun plan
	Le piège de la valeur « provisoire » : un modèle qui reçoit un projet avec q_adm absent a tendance à proposer une valeur « provisoire » (par exemple, 0,25 MPa) pour « faire avancer le projet ». C'est exactement ce qu'il faut interdire :
   * la valeur provisoire n'est pas sourcée — elle ne peut pas être défendue ;
   * elle devient implicitement la valeur de calcul — et les semelles dimensionnées sur cette base sont fausses ;
   * elle masque le besoin d'une mission G3 — et la MOA ne commande pas la mission complémentaire.
Le mode PARAMÉTRIQUE est la seule réponse correcte : on produit les formules littérales, on identifie le besoin (G3), et on laisse la décision à la MOA.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-40
	B-02 (FDC)
	Les valeurs SOL-01 à SOL-07, MAT-01 à MAT-04, avec leur fiabilité
	B-03 (RDR)
	Les décisions de périmètre (le SANS OBJET éventuel) et les décisions de valeur déclarée (PARTIEL-DÉCLARÉ)
	B-20 (Conception GO)
	Les semelles prédimensionnées et la trame de fondations
	B-21 (DDC préliminaire)
	Les ordres de grandeur des charges — B-40 refait la DDC d'exécution, mais peut vérifier la cohérence
	B-22 (Note d'hypothèses)
	Les hypothèses de charges (poids propres, cloisons) et les hypothèses de matériaux
	B-42 / B-45 (via B-50)
	Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement
	B-12 (Audit Géotechnique)
	L'adéquation du rapport géotechnique à nos besoins, la recommandation de mission G3
	Briques aval
Brique
	Ce qu'elle consomme de B-40
	B-50 (Assemblages et ancrages)
	Le logement vérifié — B-50 fait le contrôle croisé et renvoie la correction si l'ancrage ne rentre pas
	B-60 (Plans d'exécution)
	La note et les plans produits — B-60 les reprend et les indice
	B-31 (Preuve de superposition)
	Les plans produits — B-31 vérifie la cohérence avec le fichier source calé
	B-33 (Vérification croisée)
	Les plans produits — B-33 vérifie la cohérence avec les autres livrables
	B-62 (Nomenclature)
	Les plans — B-62 en extrait la nomenclature détaillée
	B-70 (Auto-contrôle de synthèse)
	L'auto-contrôle B-40 — B-70 vérifie que chaque semelle a son verdict
	Variables consommées
Code
	Libellé
	Statut dans B-40
	SOL-01
	Contrainte admissible ELS
	BLOQUANTE
	SOL-02
	Contrainte admissible ELU
	BLOQUANTE
	SOL-03
	Profondeur de bon sol / ancrage minimal
	BLOQUANTE
	SOL-05
	Classe d'agressivité du sol (XA)
	BLOQUANTE (pour l'enrobage et le ciment)
	SOL-06
	Nappe, hydrologie, drainage
	NON BLOQUANTE (si absente, mention de vérification à faire)
	SOL-07
	Tassements admissibles / différentiels
	NON BLOQUANTE (si absente, mention de vérification à faire)
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
	NIV-01, NIV-04
	Niveau de terrain naturel, niveau d'assise
	BLOQUANTE
	SIT-04, SIT-05
	Distance aux soubassements, emprise en fouille
	BLOQUANTE (pour les dispositions constructives)
	GEO-01 à GEO-05
	Géométrie et positions
	BLOQUANTE
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-40 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	SOL-01 à SOL-07, MAT-01 à MAT-04, NIV-01, NIV-04, SIT-04, SIT-05, GEO-01 à GEO-05, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Calques FOND-*, échelles, formats, cartouche
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-40, vous devez valider la géométrie des semelles après le dimensionnement EC7. C'est votre appréciation de la constructibilité (accès aux fouilles, blindage nécessaire, distance aux existants, emprise disponible) qui fait foi — pas seulement le calcul. Une semelle qui passe en portance mais qui n'est pas constructible doit être modifiée.
Cas particulier — mode SANS OBJET : si la MPD a statué que les fondations ne sont ni modifiées ni sollicitées (par exemple, travaux de superstructure sans impact sur les fondations), B-40 s'appelle en mode SANS OBJET et produit une ligne de justification. Elle ne calcule rien, ne dessine rien, ne signale aucune donnée manquante. Ce sont B-46 (vérification de l'existant) et B-24 (existant non sondé) qui couvrent alors la vérification des appuis sur l'existant.
Cas particulier — q_adm absente : si SOL-01 (q_adm ELS) est BLOQUANTE (G2 AVP insuffisant, G3 non commandé), B-40 s'appelle en mode PARAMÉTRIQUE :
   * les formules sont écrites en littéral (B ≥ N/q_adm) ;
   * un tableau de sensibilité est produit pour q_adm = 0,20 / 0,25 / 0,30 / 0,35 MPa — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE SOL-01 » et suffixé _P ;
   * aucune valeur n'est retenue.
Cas particulier — conflit entre deux valeurs : si la FDC contient deux valeurs incompatibles pour un même code (par exemple, XC2 du CCTP et XA3 de la décision RDR), B-40 le signale et s'arrête. C'est au RDR de trancher (décision D-xx), et B-40 reprend ensuite.
Cas particulier — logement des ancrages non compatible : si les ancrages calculés par B-50 ne rentrent pas dans la semelle dimensionnée par B-40, B-40 s'agrandit et le signale dans son auto-contrôle. Elle ne réduit jamais les ancrages (ce serait à B-50 de le faire, et B-50 ne le fait pas — c'est B-40 qui s'adapte).
Cas particulier — plusieurs semelles : si le projet comporte plusieurs semelles (semelles filantes + semelles isolées), B-40 les traite toutes dans la même note, avec :
   * un tableau de DDC par semelle ;
   * un tableau de dimensionnement par semelle ;
   * un tableau de ferraillage par semelle ;
   * un auto-contrôle par semelle.
L'auto-contrôle par semelle est indispensable — un auto-contrôle global ne détecte pas une semelle isolée mal centrée.
Cas particulier — semelle filante sur sol hétérogène : si le sol est hétérogène (par exemple, remblai sur une partie de l'emprise, alluvions sur l'autre), B-40 traite chaque tronçon de semelle filante séparément, avec les valeurs q_adm correspondantes. Une semelle filante dimensionnée uniformément sur un sol hétérogène est une semelle fausse sur au moins un tronçon.
Cas particulier — béton de propreté : B-40 prévoit systématiquement 5 cm de béton de propreté sous toute semelle. Ce n'est pas une option — c'est une exigence normative (EC2 §4.4 pour l'enrobage, NF P 94-261 pour la mise en œuvre). Le béton de propreté est mentionné dans les plans et dans la note.
Cas particulier — arase étanche : B-40 prévoit systématiquement une arase étanche sur toutes les têtes de semelle (feutre bitumineux entre deux chapes de ciment hydrofugé). Cette disposition est indispensable pour éviter les remontées capillaires — elle est mentionnée dans les coupes et dans la note.
Cas particulier — distance aux existants : si une semelle est à moins de 1,50 m d'un soubassement existant (SIT-04), B-40 prévoit un blindage systématique en fouille et interdit de déchausser les fondations existantes. Toute reprise en sous-œuvre consécutive est à la charge de l'entreprise — c'est une clause contractuelle qui doit être rappelée dans la note.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, et la mention du mode.
Consignation : la note B-40 est annexée au RDR (B-03) — elle documente le calcul des fondations et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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

8. **Poussées et eau** : si une semelle, une bêche ou un soubassement retient des terres ou est sous nappe (SOL-06), la poussée des terres et la poussée hydrostatique sont introduites dans les combinaisons, ou leur absence est motivée.
9. **Actions d'exécution (EC1-1-6)** : les phases provisoires dimensionnantes (fouilles ouvertes, blindage, reprise en sous-œuvre, étaiement) sont identifiées ; la situation provisoire ne doit pas être plus défavorable que la situation définitive sans être vérifiée.
