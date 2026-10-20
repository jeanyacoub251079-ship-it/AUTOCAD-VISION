Fichier 06_PHASE_4_CALCULS/B-45_Structure_Metallique.md — CARNAC v3.0
________________


B-45 — STRUCTURE MÉTALLIQUE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-05, CHG-02, CHG-06 disponibles) · PARTIEL-DÉCLARÉ (nuance supposée avec décision RDR) · PARAMÉTRIQUE (nuance non confirmée : calcul littéral en f_y) · SANS OBJET (MPD a statué : pas de structure métallique dans le périmètre) |
| Paramètre d'appel | {{élément}} = profilé de plancher / poteau métallique / poutre métallique / entretoise (quatre valeurs, une par appel) |
| Entrées lues | MAT-05, CHG-01 à CHG-03, CHG-06, GEO-02, GEO-04, B-20, B-21, B-22, B-40/B-42/B-43 (appuis), B-50 (assemblages) |
| Sortie unique | Note de calcul structure métallique + plans d'exécution + coupes + nomenclature + export DXF à calques METAL-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte des éléments métalliques à calculer (profilés de plancher, poteaux métalliques, poutres métalliques, entretoises). En mode SANS OBJET (pas de structure métallique dans le périmètre), B-45 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (nuance d'acier, charges, vent), la note d'hypothèses (B-22), la conception de B-20 (sections et positions prédimensionnées), la DDC préliminaire (B-21), les appuis sur les autres ouvrages (B-40, B-42, B-43). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{élément}}.
Ce que vous validez à la sortie :
   * la classification de section (EC3 §5.5) avant tout calcul ;
   * les vérifications EC3 (flexion, cisaillement, interaction M-V, flambement, déversement, flèches) ;
   * le maintien latéral justifié (condition du déversement) ;
   * les efforts aux nœuds transmis à B-50 ;
   * la pression diamétrale sur le béton (EC2 §6.7) ;
   * l'auto-contrôle par profilé.
L'articulation avec B-50 (option C) :

| Brique | Rôle sur les assemblages |
| --- | --- |
| B-45 | Calcule le profilé et fournit à B-50 les efforts aux nœuds et appuis (N_Ed, V_Ed, M_Ed, nature de l'assemblage). Vérifie la pression diamétrale sur le béton (EC2 §6.7). Ne calcule pas les assemblages. |
| B-50 | Calcule les assemblages (boulons, soudures, platines, tiges d'ancrage) et fait le contrôle croisé avec les efforts fournis par B-45 et les logements prévus par les briques amont. |

Ce que B-45 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des assemblages (boulons, soudures, platines, tiges) | B-50 |
| Calcul des profilés de charpente bois | B-44 |
| Calcul des planchers bois (usage intérieur) | B-43 |
| Vérification de l'existant métallique non sondé | B-24 (mode PARAMÉTRIQUE), puis B-46 si le sondage est disponible |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution de la structure métallique de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour l'élément {{élément}} (profilé de plancher / poteau métallique / poutre métallique / entretoise). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1, -1-4) : charges, vent.
- EC3 (NF EN 1993-1-1/NA) : §5.5 (classification), §6.2.5 (flexion), §6.2.6 (cisaillement), §6.2.8 (interaction M-V), §6.3.1 (flambement), §6.3.2 (déversement).
- EC3-1-8 (NF EN 1993-1-8) : assemblages (renvoi B-50).
- EC2 (NF EN 1992-1-1/NA) : §6.7 (pression diamétrale sur le béton).
- NF EN 10025 (nuances d'acier), NF EN 1090 (exécution).
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
- nuance d'acier (MAT-05) : f_y, f_u, γ_M0, γ_M1, γ_M2 ;
- charges (CHG-01 à CHG-03, CHG-06) ;
- positions (GEO-02, GEO-04) ;
- appuis sur les autres ouvrages (B-40, B-42, B-43).
Aucune valeur hors FDC. Si MAT-05 manque, applique le mode {{mode}} — pas de nuance « par défaut ».


Étape 2 — Descente de charges
- surfaces tributaires par profilé ;
- charges permanentes et d'exploitation, vent si applicable ;
- combinaisons ELS et ELU distinctes.
Tableau par profilé : w_ELS, w_ELU, N_Ed, V_Ed, M_Ed.


Étape 3 — Classification de section (EC3 §5.5)
Pour chaque profilé : classe 1, 2, 3 ou 4 selon les rapports c/t et la sollicitation. La classe détermine la résistance utilisable (plastique pour 1 et 2, élastique pour 3, efficace pour 4). Tu cites la classe et tu justifies.


Étape 4 — Vérifications EC3
- flexion : M_Ed ≤ M_c,Rd = W_pl·f_y/γ_M0 (classe 1/2) ou W_el·f_y/γ_M0 (classe 3) ;
- cisaillement : V_Ed ≤ V_pl,Rd = A_v·f_y/(√3·γ_M0) ;
- interaction M-V (EC3 §6.2.8) si V_Ed > 0,5·V_pl,Rd ;
- flambement (EC3 §6.3.1) pour les éléments comprimés : λ̄, courbe, χ, N_b,Rd ;
- déversement (EC3 §6.3.2) si la semelle comprimée n'est pas maintenue : λ̄_LT, χ_LT, M_b,Rd ;
- flèche ELS : δ ≤ L/250 ou L/300 (à justifier).
Chaque formule littérale AVANT application numérique.


Étape 5 — Dispositions constructives
- maintien latéral des semelles comprimées (entretoises, plancher collaborant, solives) : condition du déversement ;
- entretoises anti-déversement si nécessaire (efforts fournis à B-50) ;
- protection anticorrosion (galvanisation à chaud NF EN ISO 1461, peinture) ;
- réservations et trémies : positions compatibles avec les semelles ;
- appuis : vérification de la pression diamétrale sur le béton (EC2 §6.7) — effort transmis à B-50.


Étape 6 — Efforts aux assemblages (transmis à B-50)
Pour chaque nœud et chaque appui : N_Ed, V_Ed, M_Ed, nature de l'assemblage (platine boulonnée, soudé, sabot).


Étape 7 — Livrables graphiques
- METAL-AXES : axes, trames, points de calage ;
- METAL-COFFRAGE : sections, positions, portées, réservations ;
- METAL-PROFILES : désignation des profilés, positions, repères ;
- METAL-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plans, coupes, nomenclature des profilés ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention générique de protection au feu.


Étape 8 — Auto-contrôle déclaré
Profilé par profilé : charges / classification / vérifications EC3 / flèche / dispositions / efforts aux assemblages / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne calcule AUCUN assemblage (boulons, soudures, platines) : c'est B-50.
- N'invente aucune nuance d'acier : si MAT-05 manque, PARAMÉTRIQUE ou décision RDR.
- Ne déclare pas COMPLET si MAT-05 n'est pas confirmée (une nuance « supposée S235 » interdit COMPLET — V12).
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu : mention générique seule.
- Ne confonds pas déversement (EC3 §6.3.2) et flambement (EC3 §6.3.1).
- Ne suppose pas le maintien latéral sans le justifier.


SORTIE
Pièce 1 — Note de calcul (sections 1 à 8, avec formules littérales avant application numérique).
Pièce 2 — Plans d'exécution + DXF METAL-*.
Pièce 3 — Auto-contrôle déclaré.


CRITÈRE D'ACCEPTATION
- chaque donnée d'entrée est issue de la FDC ;
- chaque profilé a sa classification EC3 §5.5 ;
- chaque profilé satisfait flexion, cisaillement, interaction M-V, flambement et déversement si applicable, flèche ;
- le maintien latéral est justifié (condition du déversement) ;
- chaque nœud et appui a ses efforts transmis à B-50 ;
- les plans portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque profilé ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{élément}} (par profilé de plancher, poteau métallique, poutre métallique ou entretoise). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Classification EC3 §5.5 avant tout calcul | La classe de section détermine la résistance utilisable (plastique, élastique, efficace). Un calcul qui ignore la classe utilise W_pl pour une section de classe 3 — et surestime la résistance. C'est une erreur qui ne se voit pas sur le résultat (le taux de travail est sous-estimé) |
| Déversement conditionné au maintien | χ_LT = 1 suppose que la semelle comprimée est maintenue. Sur un plancher, les solives et le hourdis maintiennent ; sur une panne isolée, non. La condition doit être justifiée, pas supposée. Un déversement non vérifié est un risque de ruine latérale |
| Interaction M-V | Pour les profilés courts et fortement cisaillés, l'interaction M-V réduit la résistance en flexion. Un calcul qui l'ignore surestime la capacité — c'est souvent le cas des poutres courtes ou des profilés de rive |
| « Ne confonds pas déversement et flambement » | Ce sont deux vérifications distinctes : flambement pour les éléments comprimés (N), déversement pour les éléments fléchis (M). Confondre les deux conduit à des erreurs de méthode — un poteau vérifié au déversement est un poteau non vérifié au flambement |
| « Ne déclare pas COMPLET si MAT-05 non confirmée » | Une nuance « supposée S235 » est un cas Flora classique. Si la nuance n'est pas confirmée, la note n'est pas opposable — elle reste PARAMÉTRIQUE ou PARTIEL-DÉCLARÉ. C'est la même règle que SEC-01 pour le BA |
| Pression diamétrale sur le béton | Un profilé métallique sur un appui béton transmet une pression localisée. La vérification EC2 §6.7 est souvent oubliée — elle est indispensable. Sans elle, le béton peut éclater localement sous la platine |
| Protection anticorrosion | Un profilé non protégé rouille en quelques années. La disposition constructive est aussi importante que le calcul — un profilé calculé juste mais qui rouille ne sert à rien |
| « Ne réduis pas les sections pour faire rentrer les assemblages » | La tentation est de réduire une section pour qu'elle rentre dans un assemblage existant. C'est faux — c'est l'assemblage qui s'adapte (B-50), ou l'existant qui est vérifié (B-46). La section du profilé est déterminée par les vérifications EC3 |
| Filigrane + mention mode | Un plan métallique exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les quatre types d'éléments — vérifications spécifiques :

| Élément | Vérifications principales | Vérifications spécifiques |
| --- | --- | --- |
| Profilé de plancher | Flexion, cisaillement, flèche | Maintien latéral par le plancher (déversement), interaction M-V |
| Poteau métallique | Compression, flambement | Élancement dans les deux directions, courbe de flambement |
| Poutre métallique | Flexion, cisaillement, flèche | Déversement, interaction M-V, maintien latéral |
| Entretoise | Compression ou traction | Flambement si comprimée, traction si tendue |

Le piège de la classification : un modèle qui reçoit un profilé a tendance à utiliser directement W_pl (résistance plastique) sans vérifier la classe. C'est faux :
   * une section de classe 1 ou 2 utilise W_pl — c'est justifié ;
   * une section de classe 3 utilise W_el — la résistance est plus faible que W_pl ;
   * une section de classe 4 utilise une section efficace — la résistance est encore plus faible.
La classification n'est pas un détail — c'est ce qui détermine la résistance utilisable. Un calcul qui utilise W_pl sur une section de classe 3 surestime la résistance de 10 à 20 %.
Le piège du déversement : un modèle qui reçoit un calcul EC3 a tendance à supposer que la semelle comprimée est maintenue (χ_LT = 1), sans justifier le maintien. C'est faux :
   * sur un plancher, le maintien est assuré par les solives et le hourdis — c'est justifié ;
   * sur une poutre isolée, le maintien n'est pas assuré — χ_LT < 1, et le déversement gouverne le dimensionnement ;
   * sur une poutre de rive, le maintien est partiel — il faut le justifier.
La condition de maintien doit être justifiée explicitement — pas supposée parce que « c'est comme d'usage ».
Le piège de la pression diamétrale : un modèle qui reçoit un profilé sur un appui béton a tendance à vérifier la flexion et le cisaillement, mais pas la pression diamétrale. C'est faux :
   * la platine d'appui transmet une pression localisée au béton ;
   * si la pression dépasse la résistance du béton (EC2 §6.7), le béton éclate localement — c'est un désordre qui apparaît après quelques années (fissuration de la platine, éclatement du béton) ;
   * la vérification est rapide et peu coûteuse — l'oublier est une erreur grave.
Le piège de la protection anticorrosion : un modèle qui reçoit un profilé métallique a tendance à oublier la protection anticorrosion. C'est faux :
   * un profilé en acier non protégé rouille en quelques années (surtout en ambiance humide) ;
   * la protection est spécifiée (galvanisation à chaud NF EN ISO 1461, peinture) ;
   * la disposition est aussi importante que le calcul — un profilé calculé juste mais qui rouille ne sert à rien.
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
| B-24 (Vérification d'éléments existants non) | Les vérifications suspendues de l'existant métal — B-45 les ferme si le sondage est disponible |
| B-25 (Stabilité globale, contreventement, joints) | Idem, avec les dispositions de ductilité |
| B-40 (Fondations superficielles) | Les appuis des poteaux métalliques sur les semelles |
| B-42 (Verticaux BA) | Les appuis des poutres métalliques sur les poteaux BA |
| B-43 (Planchers et dallages) | Les appuis des profilés de plancher sur les dalles |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-40 (Fondations superficielles) | Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement |
| B-46 (Maçonnerie : vérification) | Les appuis des profilés sur les murs |
| B-50 (Assemblages et ancrages) | Les efforts aux nœuds (N_Ed, V_Ed, M_Ed, nature de l'assemblage) — B-50 calcule les assemblages |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (profilés, platines) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-45 — B-70 vérifie que chaque profilé a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-45 |
| --- | --- | --- |
| MAT-05 | Nuance d'acier de charpente métallique | BLOQUANTE (interdit le mode COMPLET si non confirmée) |
| CHG-01 à CHG-03 | Usage, surcharges, poids propres | BLOQUANTE |
| CHG-06 | Vent (zone, v_b, catégorie de terrain) | BLOQUANTE (si applicable) |
| GEO-02, GEO-04 | Axes et positions des porteurs | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE en neuf et restructuration |

Variables produites
B-45 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-05, CHG-01 à CHG-03, CHG-06, GEO-02, GEO-04, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques METAL-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-45, vous devez valider la nuance d'acier (MAT-05). Une nuance « supposée » n'est pas une nuance — c'est une hypothèse. Si la nuance n'est pas confirmée (par exemple, un profilé Even sans nuance précisée), B-45 s'appelle en mode PARAMÉTRIQUE ou PARTIEL-DÉCLARÉ (décision RDR).
Cas particulier — mode PARAMÉTRIQUE (MAT-05 non confirmée) : si la nuance n'est pas confirmée, B-45 s'appelle en mode PARAMÉTRIQUE :
   * les vérifications EC3 sont menées en littéral (avec f_y en symbole) ;
   * un tableau de sensibilité est produit sur les nuances plausibles (S235, S275, S355) — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE MAT-05 » et suffixé _P ;
   * aucun plan exécutable n'est produit.
Cas particulier — mode PARTIEL-DÉCLARÉ (nuance déclarée par RDR) : si la nuance est déclarée par une décision RDR (par exemple, « S235 retenu par décision D-06 »), B-45 s'appelle en mode PARTIEL-DÉCLARÉ — les vérifications sont complètes, mais la décision est citée avec son auteur, sa date et sa justification. Le livrable porte la mention « sous hypothèse MAT-05 — décision D-06 ».
Cas particulier — profilé existant à renforcer : si un profilé existant est à renforcer, B-45 traite le renforcement :
   * soit par moisage (ajout de profilés complémentaires) — B-45 calcule le profilé renforcé ;
   * soit par ajout d'appui (étai, contrefiche) — B-45 calcule la nouvelle trame, B-46 vérifie l'existant ;
   * soit par remplacement — B-45 calcule le nouveau profilé, la dépose relève de B-11 (diagnostic) et B-23 (exploitation).
B-45 ne décide pas de la méthode de renforcement — c'est B-23 qui l'oriente, B-20 qui la décide.
Cas particulier — poteau métallique : un poteau métallique travaille en compression — les vérifications critiques sont :
   * le flambement (EC3 §6.3.1) : λ̄, courbe (a, b, c, d selon le type de section), χ, N_b,Rd ;
   * l'élancement (rapport entre la longueur de flambement et le rayon de giration) — un poteau trop élancé flambe avant d'atteindre sa limite élastique ;
   * les deux directions : un poteau rectangulaire a deux rayons de giration (i_y, i_z) et deux élancements — les deux doivent être vérifiés.
Un modèle qui reçoit un poteau a tendance à ne vérifier qu'une direction — c'est faux. Le flambement dans la direction la plus défavorable gouverne.
Cas particulier — entretoise anti-déversement : une entretoise est un élément de maintien latéral — elle ne reprend pas de charges verticales, mais elle empêche les profilés de flamber latéralement. Sa vérification est :
   * compression ou traction selon le cas ;
   * flambement si comprimée ;
   * effort forfaitaire de stabilisation (généralement 2,5 % de l'effort de semelle, selon EC3).
Un modèle qui reçoit une entretoise a tendance à la traiter comme une poutre — c'est faux. L'entretoise est un maintien, pas un porteur.
Cas particulier — pression diamétrale : la pression diamétrale sur le béton (EC2 §6.7) est vérifiée pour chaque appui métallique sur béton (platine d'about, platine de pied de poteau). Si la contrainte dépasse la résistance du béton, il faut :
   * soit augmenter la surface d'appui (platine plus grande) ;
   * soit augmenter la classe de béton ;
   * soit ajouter une armature de frettage (EC2 §6.7).
Cette vérification est rapide — mais elle est souvent oubliée sur les projets où les profilés sont posés sur des dalles ou des poteaux BA.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-45 est annexée au RDR (B-03) — elle documente le calcul de la structure métallique et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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