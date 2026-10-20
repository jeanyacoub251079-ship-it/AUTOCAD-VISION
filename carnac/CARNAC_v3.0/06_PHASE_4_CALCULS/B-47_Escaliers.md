Fichier 06_PHASE_4_CALCULS/B-47_Escaliers.md — CARNAC v3.0
________________


B-47 — ESCALIERS
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-01 à MAT-04, SEC-01 disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante) · PARAMÉTRIQUE (SEC-01 manquante) · SANS OBJET (pas d'escalier dans le périmètre) |
| Paramètre d'appel | {{type}} = escalier droit / escalier balancé / escalier hélicoïdal (trois valeurs, une par appel) |
| Entrées lues | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-08, GEO-01, GEO-05, NIV-02, NIV-03, B-20, B-22, B-40/B-42/B-43 (appuis), B-50 (assemblages) |
| Sortie unique | Note de calcul escalier BA + plans + coupes + nomenclature + export DXF à calques ESCALIER-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte un escalier BA à calculer. En mode SANS OBJET (pas d'escalier dans le périmètre), B-47 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (matériaux, coupe-feu, charges, usage), la note d'hypothèses (B-22), la conception de B-20 (géométrie de l'escalier), les appuis sur les planchers et voiles (B-42, B-43). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{type}}.
Ce que vous validez à la sortie :
   * la DDC sur l'escalier (charges permanentes et d'exploitation) ;
   * le dimensionnement de la paillasse (flexion, effort tranchant, A_min) ;
   * les efforts horizontaux à la cage ;
   * la vérification vibratoire (fréquence propre) ;
   * les efforts aux appuis et scellements transmis à B-50 ;
   * l'auto-contrôle par volée.
Le périmètre exact de B-47 :

| Ce que B-47 produit | Ce que B-47 ne produit pas |
| --- | --- |
| DDC sur l'escalier (charges permanentes par couche, exploitation selon usage) | Calcul des garde-corps et main courante (hors CARNAC — lot serrurerie) |
| Dimensionnement de la paillasse (volée et palier) | Calcul des scellements de garde-corps (B-50) |
| Efforts horizontaux à la cage (poussée) | Vérification de l'existant de la cage (B-46) |
| Vérification vibratoire (fréquence propre) | Dimensionnement de la protection au feu (hors CARNAC) |
| Dispositions constructives (enrobage, ferraillage, appuis) | — |
| Plans d'exécution (ESCALIER-*) | — |

L'articulation avec B-50 (option C) :

| Brique | Rôle sur les assemblages |
| --- | --- |
| B-47 | Calcule l'escalier et fournit à B-50 les efforts aux appuis (N_Ed, V_Ed, M_Ed) et aux scellements (garde-corps). Ne calcule pas les scellements. |
| B-50 | Calcule les scellements (garde-corps, ancrages dans les appuis) et fait le contrôle croisé avec les efforts fournis par B-47. |

Ce que B-47 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des scellements de garde-corps | B-50 |
| Calcul des planchers d'appui | B-43 |
| Calcul des voiles d'appui | B-42 |
| Vérification de la cage existante (maçonnerie) | B-46 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution de l'escalier de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour le type {{type}} (escalier droit / escalier balancé / escalier hélicoïdal). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1) : charges d'exploitation des escaliers (catégorie A, B ou C selon usage).
- EC2 (NF EN 1992-1-1/NA) : §6.1 (flexion), §6.2.2 (effort tranchant), §9.3 (dispositions dalles), §7.4 (flèches).
- Vibrations : EC2 §7.4.2 ou guide technique de vibration des escaliers (fréquence propre ≥ 3 Hz ou 5 Hz selon usage).
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
- matériaux (MAT-01 à MAT-04), enrobage (MAT-03), SEC-01 (tenue au feu) ;
- charges d'exploitation selon usage (CHG-01, CHG-02) ;
- géométrie : volée, palier, largeur, giron, hauteur d'étage (NIV-02, NIV-03) ;
- appuis : sur plancher bas (B-43), sur plancher haut (B-43), sur voile ou poteau (B-42).
Aucune valeur hors FDC. Applique le mode {{mode}}.


Étape 2 — Descente de charges
- charges permanentes décomposées (marches, paillasse, revêtement, garde-corps forfaitaire) ;
- charges d'exploitation selon EC1 (usage) ;
- combinaisons ELS et ELU distinctes ;
- pour escalier balancé : répartition des charges selon la géométrie (méthode des lignes de rupture ou méthode simplifiée justifiée) ;
- pour escalier hélicoïdal : méthode des éléments finis ou méthode simplifiée justifiée (limites, torsion).


Étape 3 — Dimensionnement de la paillasse
- épaisseur de paillasse : prédimensionnement (L/25 à L/30 selon portée développée), puis vérification ;
- flexion : M_Ed selon le schéma statique (poutre droite pour escalier droit, poutre courbe pour hélicoïdal, méthode des lignes de rupture pour balancé) ;
- effort tranchant : V_Ed ≤ V_Rd,c (EC2 §6.2.2) ;
- flèche : si requise par l'usage ;
- A_s,min = max(0,26·f_ctm/f_yk·b·d ; 0,0013·b·d) (EC2 §9.3.1.1).


Étape 4 — Efforts horizontaux
- poussée horizontale à la cage d'escalier (effort H à chaque palier) : H = M_appui/h ou méthode justifiée ;
- renvoi des efforts horizontaux aux voiles ou aux poteaux adjacents (B-42) ;
- si la cage n'a pas d'appui horizontal suffisant, signaler.


Étape 5 — Vérification vibratoire
- fréquence propre fondamentale f₁ = (π/2)·√(EI/(m·L⁴)) ou formule approchée pour poutre simplement appuyée ;
- fréquence minimale : 5 Hz pour escalier d'habitation ou ERP (usage normal), 3 Hz pour usage exceptionnel — à justifier selon l'usage ;
- si f₁ < limite : augmenter l'épaisseur ou ajouter une masse, justifier.


Étape 6 — Dispositions constructives
- enrobage compatible avec SEC-01 ;
- ferraillage : nappe inférieure principale, nappe supérieure si console, chapeaux aux appuis ;
- dispositions aux appuis : ancrage des barres dans les planchers ou voiles ;
- marches et contremarches : dispositions selon type ;
- garde-corps : réservations ou scellements (efforts fournis à B-50 si scellement) ;
- joints de désolidarisation si l'escalier est adjacent à un ouvrage rigide.


Étape 7 — Efforts aux appuis et scellements (transmis à B-50)
Pour chaque appui et chaque scellement : N_Ed, V_Ed, M_Ed, nature du scellement.


Étape 8 — Livrables graphiques
- ESCALIER-AXES : axes, trames, points de calage ;
- ESCALIER-COFFRAGE : contours, épaisseurs, cotations, marches, contremarches ;
- ESCALIER-ACIER-INF : nappe inférieure, sections, espacements, recouvrements ;
- ESCALIER-ACIER-SUP : nappe supérieure, chapeaux, renforts ;
- ESCALIER-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plan, coupes longitudinale et transversale, élévation, nomenclature ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention générique de protection au feu.


Étape 9 — Auto-contrôle déclaré
Volée par volée : charges / ferraillage / efforts horizontaux / vibration / dispositions / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne calcule AUCUN scellement de garde-corps : c'est B-50.
- N'invente aucune valeur hors FDC.
- Ne confonds pas escalier BA (B-47) et dalle BA (B-43) : l'escalier a des marches, des contremarches, une géométrie inclinée, des efforts horizontaux.
- Ne déclare pas COMPLET si SEC-01 manque (V12).
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu.
- N'utilise aucune valeur « par expérience ».
- Ne passe pas sous silence la vérification vibratoire : c'est la vérification la plus souvent oubliée sur les escaliers.


SORTIE
Pièce 1 — Note de calcul (sections 1 à 9).
Pièce 2 — Plans d'exécution + DXF ESCALIER-*.
Pièce 3 — Auto-contrôle déclaré.


CRITÈRE D'ACCEPTATION
- chaque donnée d'entrée est issue de la FDC ;
- chaque volée a ses charges et ses combinaisons ;
- chaque volée satisfait flexion, effort tranchant, A_min, dispositions ;
- les efforts horizontaux sont calculés et renvoyés aux appuis ;
- la vérification vibratoire est faite avec fréquence minimale justifiée ;
- chaque appui et scellement a ses efforts transmis à B-50 ;
- les plans portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque volée ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{type}} (par escalier droit, escalier balancé ou escalier hélicoïdal). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Brique dédiée (votre choix au tronçon 1) | L'escalier a une méthode de calcul propre (paillasse inclinée, efforts horizontaux, vibration) qui n'a rien à voir avec une dalle. Une brique dédiée évite de « plaquer » la méthode dalle sur l'escalier — et de produire un ferraillage faux |
| Trois types (droit / balancé / hélicoïdal) | Chaque type a une méthode de calcul différente : poutre droite, lignes de rupture, éléments finis. Le paramètre force à choisir la méthode — sans lui, un modèle traite tous les escaliers comme des poutres droites, ce qui est faux pour les escaliers balancés et hélicoïdaux |
| Efforts horizontaux à la cage | Un escalier transmet une poussée horizontale à la cage. Si cette poussée n'est pas reprise, la cage peut se déformer. C'est souvent oublié — et c'est un désordre qui apparaît après quelques années (fissures aux angles de la cage) |
| Vérification vibratoire obligatoire | Un escalier qui vibre est un escalier inconfortable, même s'il est structurellement stable. La fréquence minimale (5 Hz ou 3 Hz selon usage) est un critère de confort, pas de sécurité — mais il est réglementaire, et il est souvent oublié |
| « Ne confonds pas escalier BA et dalle BA » | Un escalier a des marches, des contremarches, une inclinaison, des efforts horizontaux. La méthode « dalle » appliquée à un escalier produit des ferraillages faux — et un escalier qui fissure aux angles ou qui vibre |
| Scellements de garde-corps → B-50 | Les scellements de garde-corps transmettent des efforts horizontaux importants (1 kN/m selon NF P 01-012). Le calcul relève de B-50 (option C), pas de B-47 |
| « Ne passe pas sous silence la vérification vibratoire » | C'est la vérification la plus souvent oubliée sur les escaliers — parce qu'elle n'est pas dans la méthode de flexion classique. Un modèle qui l'oublie produit un escalier structurellement stable mais inconfortable |
| Filigrane + mention mode | Un plan d'escalier exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les trois types d'escaliers — méthodes de calcul :

| Type | Méthode de calcul | Vérifications spécifiques |
| --- | --- | --- |
| Escalier droit | Poutre droite inclinée (paillasse), avec ou sans palier | Flexion, effort tranchant, vibration, efforts horizontaux |
| Escalier balancé | Méthode des lignes de rupture (ou méthode simplifiée justifiée) | Répartition des charges selon la géométrie, torsion locale, vibration |
| Escalier hélicoïdal | Éléments finis (ou méthode simplifiée justifiée avec limites) | Torsion, flexion composée, vibration, efforts horizontaux importants |

Le piège de la méthode : un modèle qui reçoit un escalier balancé a tendance à le traiter comme un escalier droit — c'est faux :
   * un escalier balancé a des marches qui tournent, et la paillasse est courbe (ou brisée) ;
   * la répartition des charges n'est pas uniforme — elle est concentrée à l'extérieur du virage ;
   * le moment fléchissant est plus élevé que dans un escalier droit de même portée développée.
La méthode des lignes de rupture (ou une méthode simplifiée justifiée) est obligatoire pour les escaliers balancés. Un calcul en poutre droite sous-estime le moment de 20 à 40 %.
Le piège de la vibration : un modèle qui reçoit un escalier a tendance à ne vérifier que la flexion et l'effort tranchant. C'est insuffisant :
   * un escalier qui vibre (fréquence propre < 5 Hz) est inconfortable, même s'il est structurellement stable ;
   * la fréquence propre dépend de la raideur (EI) et de la masse (m) — une paillasse trop mince vibre ;
   * c'est souvent la vérification qui gouverne l'épaisseur de la paillasse (plus que la flexion).
Un escalier qui vibre est un escalier qui « rebondit » sous le pas — c'est un désordre qui n'apparaît pas dans les calculs de résistance, mais qui est immédiatement perceptible par l'utilisateur.
Le piège des efforts horizontaux : un escalier qui monte d'un étage à l'autre transmet une poussée horizontale à la cage (effort H à chaque palier). C'est un effet de « arc-boutant » — la paillasse inclinée pousse horizontalement sur ses appuis. Un modèle qui l'ignore produit un escalier qui « pousse » sur la cage — et une cage qui n'est pas dimensionnée pour cela fissure aux angles.
L'effort horizontal est généralement faible (quelques kN), mais il doit être explicitement transmis aux voiles ou aux poteaux adjacents (B-42). Si la cage n'a pas d'appui horizontal suffisant, c'est un problème de conception à signaler.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-23 (Exploitation du diagnostic existant) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-42 (Verticaux BA) | Les voiles ou poteaux qui reçoivent les efforts horizontaux |
| B-43 (Planchers et dallages) | Les planchers qui reçoivent les appuis de l'escalier |
| B-50 (Assemblages et ancrages) | Aucune donnée en amont — B-47 fournit les efforts, B-50 calcule les scellements |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-50 (Assemblages et ancrages) | Les efforts aux appuis et aux scellements (N_Ed, V_Ed, M_Ed) — B-50 calcule les scellements |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (barres, chapeaux, renforts) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-47 — B-70 vérifie que chaque volée a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-47 |
| --- | --- | --- |
| MAT-01 | Classe de résistance du béton | BLOQUANTE |
| MAT-02 | Classe d'exposition | BLOQUANTE |
| MAT-03 | Enrobage nominal | BLOQUANTE |
| MAT-04 | Nuance d'acier BA | BLOQUANTE |
| SEC-01 | Degré coupe-feu | BLOQUANTE (interdit le mode COMPLET si absente) |
| CHG-01, CHG-02 | Usage et surcharges | BLOQUANTE |
| CHG-03 | Poids propres des complexes de plancher | BLOQUANTE |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | NON BLOQUANTE (si absente, aucune charge ponctuelle considérée) |
| NIV-02, NIV-03 | Niveaux de plancher, hauteurs libres | BLOQUANTE |
| GEO-01, GEO-05 | Emprise, baies et ouvertures | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |

Variables produites
B-47 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-08, NIV-02, NIV-03, GEO-01, GEO-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques ESCALIER-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-47, vous devez valider la méthode de calcul pour un escalier balancé ou hélicoïdal. Les méthodes simplifiées (lignes de rupture, formules approchées) doivent être justifiées — pas choisies par défaut. Un escalier balancé calculé en poutre droite est un escalier sous-dimensionné de 20 à 40 %.
Cas particulier — mode PARAMÉTRIQUE (SEC-01 manquante) : si SEC-01 (coupe-feu) n'est pas fournie, B-47 s'appelle en mode PARAMÉTRIQUE :
   * les vérifications EC2 (flexion, effort tranchant, vibration) sont menées normalement ;
   * l'enrobage de tenue au feu est traité en littéral (avec le degré coupe-feu en symbole) ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE SEC-01 » et suffixé _P ;
   * aucun plan exécutable n'est produit.
Cas particulier — escalier balancé : si l'escalier est balancé, B-47 utilise la méthode des lignes de rupture (ou une méthode simplifiée justifiée). La méthode des lignes de rupture est plus complexe qu'une poutre droite, mais elle donne le moment réel dans la paillasse courbe. Une méthode simplifiée peut être acceptable si :
   * elle est explicitement justifiée (référence à un guide technique) ;
   * elle est conservative (elle surestime le moment) ;
   * elle est validée par votre jugement.
Un escalier balancé calculé en poutre droite sous-estime le moment — et produit une paillasse qui fissure au virage.
Cas particulier — escalier hélicoïdal : si l'escalier est hélicoïdal, B-47 utilise la méthode des éléments finis (ou une méthode simplifiée justifiée avec limites). Un escalier hélicoïdal a :
   * une torsion importante (la paillasse tourne autour de l'axe) ;
   * une flexion composée (flexion + compression ou traction) ;
   * des efforts horizontaux importants à la cage.
C'est l'escalier le plus difficile à calculer — et le plus sensible aux erreurs. Si les données ne permettent pas un calcul fiable, B-47 le signale et recommande un calcul par un spécialiste (BET structure).
Cas particulier — vérification vibratoire : la fréquence propre minimale est :
   * 5 Hz pour les escaliers d'habitation ou d'ERP (usage normal) ;
   * 3 Hz pour les usages exceptionnels (escaliers de secours peu fréquentés, escaliers techniques).
La fréquence propre dépend de la raideur (EI) et de la masse (m). Une paillasse trop mince vibre — c'est souvent la vérification qui gouverne l'épaisseur de la paillasse. Un escalier qui vibre à 3 Hz est immédiatement perceptible par l'utilisateur.
Cas particulier — efforts horizontaux à la cage : l'effort horizontal transmis à la cage est généralement faible (quelques kN), mais il doit être explicitement transmis :
   * si la cage a des voiles ou des poteaux adjacents (B-42), l'effort y est renvoyé ;
   * si la cage n'a pas d'appui horizontal suffisant (par exemple, une cage ouverte sur un côté), B-47 le signale — c'est un problème de conception qui doit être résolu par B-20 (ajout d'un voile, modification de la cage).
Un escalier qui « pousse » sur une cage sans appui horizontal fissure les angles de la cage après quelques années.
Cas particulier — scellements de garde-corps : les scellements de garde-corps transmettent des efforts horizontaux importants (1 kN/m selon NF P 01-012). B-47 les mentionne sur les plans (réservations ou scellements), et fournit les efforts à B-50. Le calcul du scellement lui-même relève de B-50.
Cas particulier — escalier adjacent à un ouvrage rigide : si l'escalier est adjacent à un ouvrage rigide (par exemple, un voile BA), B-47 prévoit un joint de désolidarisation (polystyrène + mastic) pour éviter les fissures dues aux mouvements différentiels. Sans ce joint, l'escalier fissure au contact du voile.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-47 est annexée au RDR (B-03) — elle documente le calcul de l'escalier et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).