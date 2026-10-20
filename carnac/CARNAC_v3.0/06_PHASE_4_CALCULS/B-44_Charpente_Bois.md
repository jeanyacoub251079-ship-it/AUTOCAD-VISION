Fichier 06_PHASE_4_CALCULS/B-44_Charpente_Bois.md — CARNAC v3.0
________________


B-44 — CHARPENTE BOIS
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses), B-23 (Exploitation du diagnostic) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-06, MAT-08, CHG-04 à CHG-06 disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante, notamment une section d'existant non sondée) · PARAMÉTRIQUE (section de l'existant non sondée : vérification littérale) · SANS OBJET (MPD a statué : pas de charpente bois dans le périmètre) |
| Paramètre d'appel | {{élément}} = panne / ferme / arbalétrier / contrefiche / chevron / poutre (six valeurs, une par appel) |
| Entrées lues | MAT-06, MAT-08, CHG-04 à CHG-06, EXI-01, EXI-03, GEO-01, B-11, B-23, B-20, B-22, B-50 (assemblages) |
| Sortie unique | Note de calcul charpente bois + plans d'exécution + coupes + nomenclature + export DXF à calques CHARPENTE-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, B-21, B-22 et B-23, quand le projet comporte une charpente bois à calculer (pannes, fermes, arbalétriers, contrefiches, chevrons, poutres). En mode SANS OBJET (pas de charpente bois dans le périmètre), B-44 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (bois, classe de service, charges de toiture, neige, vent), la note d'hypothèses (B-22), la conception de B-20 (sections prédimensionnées), la DDC préliminaire (B-21), les contraintes du diagnostic (B-23). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{élément}}.
Ce que vous validez à la sortie :
   * la DDC d'exécution aux éléments de charpente (distincte de B-21) ;
   * les vérifications EC5 (flexion, cisaillement, compression, flambement, déversement, flèche différée) ;
   * les coefficients k_mod, k_def, k_cr, k_h justifiés ;
   * les dispositions constructives (contreventement, ancrage anti-soulèvement, ventilation) ;
   * les efforts aux appuis et assemblages transmis à B-50 ;
   * l'auto-contrôle par élément.
L'articulation avec B-50 (option C) :

| Brique | Rôle sur les assemblages |
| --- | --- |
| B-44 | Calcule l'élément bois et fournit à B-50 les efforts aux assemblages (N_Ed, V_Ed, M_Ed, nature de l'assemblage : sabot, équerre, boulonné, entaillé). Ne calcule pas les assemblages. |
| B-50 | Calcule les assemblages (capacité Johansen EC5 §8, sabots, équerres, boulons, entailles) et fait le contrôle croisé avec les efforts fournis par B-44 et les logements prévus par les briques amont. |

Ce que B-44 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des assemblages (sabots, boulons, équerres, entailles) | B-50 |
| Calcul des planchers bois (usage intérieur) | B-43 |
| Vérification de l'existant non sondé (sections inconnues) | B-24 (mode PARAMÉTRIQUE), puis B-44 en mode COMPLET si le sondage est disponible |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |
| Étude des couvertures et zingueries | Hors périmètre CARNAC (lot couverture) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution de la charpente bois de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour l'élément {{élément}} (panne / ferme / arbalétrier / contrefiche / chevron / poutre). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1, -1-3, -1-4 et Annexes Nationales) : poids propres, neige, vent.
- EC5 (NF EN 1995-1-1/NA) : §6.1 (flexion), §6.1.5 (compression perpendiculaire), §6.1.7 (cisaillement), §6.2 (traction), §6.3.2 (flambement), §6.3.3 (déversement), §7.2 (flèches différées), §8 (assemblages).
- NF EN 338 (classes de résistance du bois), NF EN 14081 (classement visuel).
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
- classe de bois (MAT-06), classe de service (MAT-08) ;
- poids propres de toiture par couche (CHG-04) ;
- neige (CHG-05), vent (CHG-06) ;
- sections et état de l'existant (EXI-01, EXI-03) si l'élément est existant.
Aucune valeur hors FDC. Si une donnée manque, applique le mode {{mode}}.


Étape 2 — Descente de charges
- surfaces tributaires par élément (entraxes, portées) ;
- charges permanentes décomposées par couche (couverture, voligeage, chevrons, pannes, isolation, plafond) ;
- neige : s = μ₁·s_k (EC1-1-3), avec μ₁ justifié par la pente ;
- vent : pression et dépression selon EC1-1-4, avec coefficients de forme justifiés ;
- combinaisons EC0 : fondamentale, accidentelle si applicable, ELS caractéristique pour les flèches.
Tableau ELS et tableau ELU distincts.


Étape 3 — Vérifications EC5
Pour chaque élément, avec les coefficients k_mod, k_def, k_h, k_cr justifiés :
- flexion : σ_m,d = M_Ed/W ≤ f_m,d ;
- cisaillement : τ_d = 1,5·V_Ed/(b·h·k_cr) ≤ f_v,d ;
- compression parallèle avec flambement (EC5 §6.3.2) : λ_rel, k_c, N_c,Rd ;
- compression perpendiculaire aux appuis (EC5 §6.1.5) ;
- déversement (EC5 §6.3.3) si la semelle comprimée n'est pas maintenue : k_crit, λ_rel,m ;
- flèche instantanée et flèche finale (EC5 §7.2) : w_fin = w_inst,G(1+k_def) + w_inst,Q(1+ψ₂·k_def) ;
- flèche limite : L/300, L/200 ou L/400 selon l'usage (à justifier).
Chaque formule littérale AVANT application numérique.


Étape 4 — Dispositions constructives
- contreventement (croix de Saint-André, diaphragme de toiture, pannes bloquées) ;
- ancrage anti-soulèvement (équerres, sabots — efforts fournis à B-50) ;
- ventilation de la sous-face (lame d'air, chatières) ;
- protection contre l'humidité (classe de service, barrière d'étanchéité) ;
- assemblages : efforts transmis à B-50 (pas de calcul ici).


Étape 5 — Efforts aux appuis et aux assemblages (transmis à B-50)
Pour chaque appui et chaque assemblage : N_Ed, V_Ed, M_Ed, nature de l'assemblage (sabot, équerre, boulonné, entaillé).


Étape 6 — Livrables graphiques
- CHARPENTE-AXES : axes, trames, points de calage ;
- CHARPENTE-COFFRAGE : sections, positions, portées, contreventements ;
- CHARPENTE-EXISTANT : éléments existants à conserver ;
- CHARPENTE-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plan de charpente, coupes, élévations, nomenclature ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention « protection au feu adéquate à prévoir (hors lot GO) ».


Étape 7 — Auto-contrôle déclaré
Élément par élément : charges / vérifications EC5 / flèches / dispositions / efforts aux assemblages / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne calcule AUCUN assemblage (sabots, boulons, équerres) : c'est B-50.
- N'invente aucune valeur hors FDC.
- Ne confonds pas charpente bois (B-44) et plancher bois (B-43).
- Ne déclare pas COMPLET si une donnée bloquante manque (V12).
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu : mention générique seule.
- N'utilise aucune valeur « par expérience ».
- Ne réduis pas les sections pour faire rentrer les assemblages dans l'existant : c'est B-50 qui adapte, et B-46 qui vérifie l'existant.


SORTIE
Pièce 1 — Note de calcul (sections 1 à 7, avec formules littérales avant application numérique).
Pièce 2 — Plans d'exécution + DXF CHARPENTE-*.
Pièce 3 — Auto-contrôle déclaré.


CRITÈRE D'ACCEPTATION
- chaque donnée d'entrée est issue de la FDC ;
- chaque élément satisfait flexion, cisaillement, compression, flèche différée, déversement si applicable ;
- k_mod, k_def, k_h, k_cr sont justifiés ;
- chaque appui et assemblage a ses efforts transmis à B-50 ;
- les dispositions constructives sont présentes (contreventement, ancrage, ventilation) ;
- les plans portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque élément ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{élément}} (par panne, ferme, arbalétrier, contrefiche, chevron ou poutre). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Paramètre {{élément}} = six valeurs | Six types d'éléments, avec des vérifications EC5 communes (flexion, cisaillement, flèche) et des vérifications spécifiques (flambement pour les compressions, déversement pour les flexions non maintenues, compression perpendiculaire pour les appuis). Un prompt unique avec un paramètre évite la répétition de 80 % du contenu et garde les spécificités visibles |
| k_mod, k_def, k_cr justifiés | Ce sont les trois coefficients qui distinguent EC5 d'EC2/EC3. Un calcul EC5 sans k_def est un calcul qui ignore le fluage du bois — donc faux à long terme. Un calcul sans k_mod est un calcul qui ne tient pas compte de la durée de charge (neige vs poids propre) |
| Flèche finale, pas seulement instantanée | La flèche différée gouverne souvent le dimensionnement d'une panne. Un calcul qui ne vérifie que w_inst est un calcul qui sous-dimensionne. C'est la vérification qui distingue EC5 d'EC2/EC3 |
| Déversement conditionné au maintien | χ_LT = 1 (ou k_crit = 1) suppose que la semelle comprimée est maintenue. Sur un plancher, les solives et le hourdis maintiennent ; sur une panne isolée, non. La condition de maintien doit être justifiée, pas supposée |
| Vent : pression ET dépression | La dépression soulève la couverture. Un calcul qui ne vérifie que la pression descendante est un calcul incomplet. La dépression gouverne souvent les ancrages anti-soulèvement |
| « Ne confonds pas charpente et plancher » | Les charges diffèrent (neige/vent vs usage intérieur), les flèches limites aussi. La confusion produit des sections fausses — un plancher traité comme une charpente est surdimensionné (coût), une charpente traitée comme un plancher est sous-dimensionnée (sécurité) |
| Ancrage anti-soulèvement | Le vent en dépression soulève la charpente. L'ancrage est une disposition indispensable — les efforts sont fournis à B-50, qui calcule les équerres et les sabots |
| Ventilation de la sous-face | Une charpente bois non ventilée pourrit. La disposition constructive est aussi importante que le calcul — un calcul juste sur une charpente qui pourrit ne sert à rien |
| « Ne réduis pas les sections pour faire rentrer les assemblages » | La tentation est de réduire une section pour qu'elle rentre dans un assemblage existant. C'est faux — c'est l'assemblage qui s'adapte (B-50), ou l'existant qui est vérifié (B-46). La section de l'élément est déterminée par les vérifications EC5, pas par les contraintes d'assemblage |
| Filigrane + mention mode | Un plan de charpente exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les six types d'éléments — vérifications spécifiques :

| Élément | Vérifications principales | Vérifications spécifiques |
| --- | --- | --- |
| Panne | Flexion, cisaillement, flèche différée | Déversement si non maintenue, compression perpendiculaire aux appuis |
| Ferme | Flexion des arbalétriers, traction des entraits, compression des poinçons | Flambement des éléments comprimés, assemblages (renvoi B-50) |
| Arbalétrier | Flexion composée, compression | Flambement, déversement, interaction |
| Contrefiche | Compression | Flambement (c'est la vérification critique) |
| Chevron | Flexion, cisaillement | Flèche différée (les chevrons fléchissent dans le temps) |
| Poutre | Flexion, cisaillement | Déversement, flèche différée |

Le piège de la flèche différée : un modèle qui reçoit un calcul EC5 a tendance à ne vérifier que la flèche instantanée (w_inst). C'est insuffisant :
   * le bois flue sous charge permanente (k_def = 0,8 en classe de service 2) ;
   * la flèche finale (w_fin) est souvent 1,8 fois la flèche instantanée ;
   * c'est la flèche finale qui gouverne le dimensionnement (L/300 ou L/200).
Un calcul qui ne vérifie que w_inst produit des sections sous-dimensionnées en flèche — le plancher ou la toiture fléchit dans le temps, et l'utilisateur se plaint (plancher qui « rebondit », toiture qui « travaille »).
Le piège du déversement : un modèle qui reçoit un calcul EC5 a tendance à supposer que la semelle comprimée est maintenue (χ_LT = 1), sans justifier le maintien. C'est faux :
   * sur un plancher, le maintien est assuré par les solives et le hourdis — c'est justifié ;
   * sur une panne isolée, le maintien n'est pas assuré — χ_LT < 1, et le déversement gouverne le dimensionnement.
La condition de maintien doit être justifiée explicitement — pas supposée parce que « c'est comme d'usage ».
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-11 (Audit du diagnostic structure) | Les désordres de charpente existante (si applicable) — B-44 les cite |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-23 (Exploitation du diagnostic existant) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-24 (Vérification d'éléments existants non) | Les vérifications suspendues de l'existant bois — B-44 les ferme si le sondage est disponible, sinon les reprend en mode PARAMÉTRIQUE |
| B-25 (Stabilité globale, contreventement, joints) | Les efforts horizontaux repris par les palées et triangulations |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-46 (Maçonnerie : vérification) | Les appuis de la charpente sur les murs |
| B-50 (Assemblages et ancrages) | Les efforts aux assemblages (N_Ed, V_Ed, M_Ed, nature de l'assemblage) — B-50 calcule les assemblages |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (sections, boulons, sabots) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-44 — B-70 vérifie que chaque élément a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-44 |
| --- | --- | --- |
| MAT-06 | Classe de bois | BLOQUANTE |
| MAT-08 | Classe de service et durée de charge | BLOQUANTE |
| CHG-04 | Poids propres de toiture | BLOQUANTE |
| CHG-05 | Neige (zone, s_k) | BLOQUANTE |
| CHG-06 | Vent (zone, v_b, catégorie de terrain) | BLOQUANTE |
| EXI-01 | Sections des éléments existants | BLOQUANTE (si élément existant — sinon mode PARAMÉTRIQUE) |
| EXI-03 | Résistance des matériaux existants | BLOQUANTE (si élément existant) |
| GEO-01 | Emprise / contour du bâtiment | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE en neuf et restructuration |

Variables produites
B-44 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-06, MAT-08, CHG-04 à CHG-06, EXI-01, EXI-03, GEO-01, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques CHARPENTE-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-44, vous devez valider les classes de service et la ventilation. Un bois en classe de service 3 (extérieur, humidité fréquente) mal ventilé pourrit, quel que soit le calcul. C'est votre appréciation des conditions réelles (ventilation de la sous-face, étanchéité de la couverture) qui fait foi.
Cas particulier — mode PARAMÉTRIQUE (section de l'existant non sondée) : si l'élément existant n'a pas de section connue (par exemple, une panne ancienne), B-44 s'appelle en mode PARAMÉTRIQUE :
   * les vérifications EC5 sont menées en littéral (avec la section en symbole) ;
   * un tableau de sensibilité est produit sur les sections plausibles — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE [section] » et suffixé _P ;
   * aucun plan exécutable n'est produit.
C'est B-24 qui est la brique dédiée à ce cas — B-44 ferme la vérification quand la section est disponible.
Cas particulier — élément existant à renforcer : si un élément existant est à renforcer (par exemple, une panne qui fléchit), B-44 traite le renforcement :
   * soit par moisage (ajout de profilés métalliques) — B-44 fournit les efforts, B-45 calcule le métal, B-50 calcule l'assemblage ;
   * soit par doublage bois (ajout d'une panne sœur) — B-44 calcule la section doublée ;
   * soit par ajout d'un appui (contrefiche, étai) — B-44 calcule la contrefiche et l'appui, B-46 vérifie l'existant.
B-44 ne décide pas de la méthode de renforcement — c'est B-23 (exploitation du diagnostic) qui l'oriente, B-20 (conception) qui la décide.
Cas particulier — contrefiche : une contrefiche est un élément comprimé — la vérification critique est le flambement, pas la flexion. Un modèle qui reçoit une contrefiche a tendance à appliquer la méthode de flexion (comme pour une poutre) — c'est faux :
   * la contrefiche travaille en compression ;
   * la vérification est N_Ed/(k_c·A·f_c,0,d) ≤ 1 (EC5 §6.3.2) ;
   * k_c dépend de l'élancement (λ_rel) et de la classe de bois.
La section d'une contrefiche est souvent surdimensionnée — c'est la robustesse de l'assemblage qui gouverne, pas le calcul. Mais le calcul doit être fait.
Cas particulier — ferme : une ferme est un assemblage d'éléments (arbalétriers, entrait, poinçon, contrefiches) — chaque élément a ses vérifications propres. Un modèle qui reçoit une ferme doit :
   * traiter chaque élément séparément (arbalétrier en flexion composée, entrait en traction, poinçon en compression, contrefiche en compression/flambement) ;
   * calculer les efforts aux nœuds (transmis à B-50 pour les assemblages) ;
   * vérifier la stabilité globale (contreventement).
Traiter une ferme comme une seule poutre est une erreur de méthode — la ferme est un treillis, pas une poutre.
Cas particulier — vent en dépression : sur une toiture à faible pente, la dépression due au vent peut soulever la couverture. B-44 calcule la dépression et transmet les efforts à B-50 (ancrages anti-soulèvement). Sans cette vérification, la couverture peut être arrachée lors d'une tempête — c'est un désordre fréquent sur les toitures mal ancrées.
Cas particulier — pente de toiture : la pente de toiture détermine :
   * le coefficient de forme de la neige (μ₁) ;
   * le coefficient de forme du vent (c_pe) ;
   * les efforts de flambement des arbalétriers.
Si la pente n'est pas cotée au dossier, B-44 la relève (par exemple, sur le plan de coupe) et la déclare dans sa note. Une pente supposée fausse produit des charges de neige et de vent fausses.
Cas particulier — ventilation de la sous-face : une charpente bois doit être ventilée (lame d'air entre l'isolation et la couverture, chatières en about). Sans ventilation, l'humidité s'accumule et le bois pourrit. B-44 prévoit les dispositions de ventilation et les mentionne sur les plans.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-44 est annexée au RDR (B-03) — elle documente le calcul de la charpente et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).