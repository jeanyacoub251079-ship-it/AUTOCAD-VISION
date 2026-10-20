Fichier 06_PHASE_4_CALCULS/B-48_Predalles.md — CARNAC v3.0
________________


B-48 — PRÉDALLES ET PLANCHERS PRÉFABRIQUÉS
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-01 à MAT-04, SEC-01, DOC-09 fiches techniques prédalles disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante) · PARAMÉTRIQUE (SEC-01 manquante ou fiche technique prédalle manquante) · SANS OBJET (pas de prédalles dans le périmètre) |
| Paramètre d'appel | {{phase}} = phase provisoire / phase finale / les deux (votre choix au tronçon 7d) |
| Entrées lues | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-08, NIV-02, NIV-06, GEO-01, DOC-09 (fiches techniques), B-20, B-22, B-40/B-42/B-43 (appuis), B-50 (assemblages) |
| Sortie unique | Note de calcul prédalles (phase provisoire + phase finale) + plans + coupes + nomenclature + export DXF à calques PREDALLE-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte des prédalles ou planchers préfabriqués à calculer. En mode SANS OBJET (pas de prédalles dans le périmètre), B-48 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (matériaux, coupe-feu, charges, épaisseurs), la note d'hypothèses (B-22), la conception de B-20 (porteurs prédimensionnés), la DDC préliminaire (B-21), les fiches techniques des prédalles (DOC-09), les appuis sur les poutres et voiles (B-42, B-43). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{phase}}.
Ce que vous validez à la sortie :
   * la phase provisoire (décoffrage, levage, pose, étaiement, flèche de décoffrage) ;
   * la phase finale (dalle de compression, connexion, flexion, effort tranchant, poinçonnement, flèche finale) ;
   * les efforts aux appuis et connexions transmis à B-50 ;
   * les dispositions constructives (étaiement, joints, réservations) ;
   * l'auto-contrôle zone par zone, phase par phase.
Le périmètre exact de B-48 (votre choix au tronçon 7d — deux phases) :
Phase provisoire (comportement de la prédalle seule, avant coulage de la dalle de compression) :
   * Décoffrage : quand la prédalle peut-elle être décintrée ?
   * Levage : efforts de levage, points d'élingue, contraintes.
   * Pose : étaiement provisoire (nombre, espacement, portée).
   * Flèche de décoffrage : flèche admissible de la prédalle sous son poids propre.
   * Vérifications EC2 en phase provisoire : flexion, effort tranchant, flèche.
Phase finale (comportement du plancher collaborant — prédalle + dalle de compression) :
   * Dalle collaborante : épaisseur, ferraillage complémentaire, connexion.
   * Vérifications EC2 en phase finale : flexion, effort tranchant, poinçonnement, flèche.
   * Si le plancher est mixte (prédalle béton + poutre métallique) : connexion → B-45/B-50.
Ce que B-48 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des connexions (boulons, soudures, armatures de connexion) | B-50 |
| Calcul des poutres de charpente | B-44 |
| Calcul des profilés métalliques de plancher | B-45 |
| Vérification de l'existant | B-46 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |
| Note de calcul du fabricant de prédalle (si fournie) | B-48 en PARTIEL-DÉCLARÉ — contrôle, pas recalcul |

L'articulation avec B-50 (option C) :

| Brique | Rôle sur les connexions |
| --- | --- |
| B-48 | Calcule les phases provisoire et finale et fournit à B-50 les efforts aux appuis et aux connexions (N_Ed, V_Ed, M_Ed, nature de la connexion). Ne calcule pas les connexions. |
| B-50 | Calcule les connexions (armatures de connexion, boulons, soudures) et fait le contrôle croisé avec les efforts fournis par B-48 et les logements prévus. |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution des prédalles et planchers préfabriqués de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour {{phase}} (phase provisoire / phase finale / les deux). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1) : charges d'exploitation.
- EC2 (NF EN 1992-1-1/NA) : §6.1 (flexion), §6.2 (effort tranchant), §6.4 (poinçonnement), §7.4 (flèches), §9.3 (dispositions dalles).
- NF EN 13747 (prédalles), NF EN 15037 (planchers à poutrelles), NF EN 1992-1-1/NA pour la phase provisoire.
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
- matériaux (MAT-01 à MAT-04), enrobage (MAT-03), SEC-01 ;
- charges d'exploitation (CHG-01, CHG-02) ;
- géométrie : portée, largeur, épaisseur de prédalle, épaisseur de dalle de compression (NIV-06) ;
- fiche technique de la prédalle (DOC-09) : section, armatures, poids, flèche admissible de décoffrage ;
- appuis : sur poutres, voiles ou murs (B-40, B-42, B-43).
Aucune valeur hors FDC. Applique le mode {{mode}}.


Étape 2 — Phase provisoire (si {{phase}} = provisoire ou les deux)
- charges : poids propre de la prédalle + charge de chantier (ouvriers, matériel, coffrage) ;
- étaiement : nombre et espacement des étais, portée entre étais ;
- flexion : M_Ed en phase provisoire, contrainte σ ≤ f_ctm (ou f_ctk,0,05 si justifié) ;
- effort tranchant : V_Ed ≤ V_Rd,c ;
- flèche de décoffrage : w ≤ w_admissible de la fiche technique ;
- levage : points d'élingue, efforts, vérification des sections aux points de levage (renvoi à la fiche technique, contrôle de cohérence) ;
- si la fiche technique manque : mode PARAMÉTRIQUE, calcul littéral, suspension de la phase provisoire.


Étape 3 — Phase finale (si {{phase}} = finale ou les deux)
- dalle de compression : épaisseur, ferraillage complémentaire (treillis soudé, A_min) ;
- charges : poids propre prédalle + dalle + revêtement + exploitation ;
- flexion : M_Ed en phase finale, ferraillage total (armatures de la prédalle + complémentaires) ;
- effort tranchant : V_Ed ≤ V_Rd,c (attention : en phase finale, la section est plus épaisse, mais la prédalle peut être critique en phase provisoire) ;
- poinçonnement : si charge ponctuelle (poteau, équipement lourd) ;
- flèche finale : flèche totale (instantanée + différée).


Étape 4 — Vérifications de synthèse
- la prédalle est-elle critique en phase provisoire ou en phase finale ? Justifier ;
- si la phase provisoire est critique : l'étaiement doit être suffisant, et la fiche technique doit le confirmer ;
- si la phase finale est critique : la dalle de compression doit être ferraillée en conséquence.


Étape 5 — Dispositions constructives
- étaiement provisoire : nombre, espacement, portée, maintien jusqu'à décoffrage ;
- connexion prédalle / dalle de compression : rugosité, armatures de connexion ;
- appuis : longueur d'appui sur les poutres ou voiles, ancrage des armatures ;
- joints entre prédalles : clavetage, continuité des armatures ;
- réservations et trémies : compatibles avec les armatures.


Étape 6 — Efforts aux appuis et connexions (transmis à B-50)
Pour chaque appui et chaque connexion : N_Ed, V_Ed, M_Ed, nature de la connexion.


Étape 7 — Livrables graphiques
- PREDALLE-AXES : axes, trames, points de calage ;
- PREDALLE-COFFRAGE : contours, épaisseurs, cotations, réservations, joints, plan d'étaiement ;
- PREDALLE-ACIER-INF : armatures de la prédalle et complémentaires, sections, espacements ;
- PREDALLE-ACIER-SUP : nappe supérieure, chapeaux, renforts ;
- PREDALLE-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plan de pose, coupes, nomenclature ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention générique de protection au feu.


Étape 8 — Auto-contrôle déclaré
Zone par zone, phase par phase : charges / vérifications / étaiement / connexion / flèche / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne calcule AUCUNE connexion (boulons, soudures, armatures de connexion) : c'est B-50.
- N'invente aucune valeur hors FDC.
- Ne confonds pas phase provisoire et phase finale : ce sont deux états distincts, avec des sections résistantes différentes.
- Ne déclare pas COMPLET si DOC-09 (fiche technique prédalle) manque pour la phase provisoire.
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu.
- N'utilise aucune valeur « par expérience ».
- Ne néglige pas la phase provisoire : c'est souvent elle qui gouverne le dimensionnement.


SORTIE
Pièce 1 — Note de calcul (sections 1 à 8, avec phase provisoire et/ou finale).
Pièce 2 — Plans d'exécution + DXF PREDALLE-*.
Pièce 3 — Auto-contrôle déclaré.


CRITÈRE D'ACCEPTATION
- chaque donnée d'entrée est issue de la FDC ;
- la phase provisoire (si demandée) est vérifiée : flexion, effort tranchant, flèche de décoffrage, levage ;
- l'étaiement provisoire est dimensionné et justifié ;
- la phase finale (si demandée) est vérifiée : flexion, effort tranchant, poinçonnement, flèche finale ;
- la connexion prédalle / dalle de compression est décrite ;
- chaque appui et connexion a ses efforts transmis à B-50 ;
- les plans portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque zone et chaque phase ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{phase}} (par phase provisoire, phase finale ou les deux). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Brique dédiée (votre choix au tronçon 1) | La prédalle a deux phases (provisoire et finale) avec des sections résistantes différentes. Une brique « plancher » classique ne distingue pas les deux, et sous-dimensionne la phase provisoire |
| Deux phases explicites | La phase provisoire est souvent critique : la prédalle seule, sans dalle de compression, reprend les efforts de levage et de décoffrage. Si on ne la vérifie pas, on peut avoir une prédalle qui casse au levage alors qu'elle serait largement suffisante en phase finale |
| Flèche de décoffrage | Une prédalle qui fléchit trop au décoffrage fissure la dalle de compression. La flèche admissible de la fiche technique est un critère de qualité, pas seulement de sécurité |
| Étaiement provisoire | L'étaiement n'est pas « accessoire » : il reprend les efforts de la prédalle en phase provisoire. Un étaiement insuffisant fissure la prédalle avant même le coulage |
| « Ne néglige pas la phase provisoire » | C'est la clause qui distingue B-48 d'une dalle BA : sans elle, un modèle « oublie » la phase provisoire et produit une note qui semble complète mais qui est fausse en phase chantier |
| DOC-09 (fiche technique) bloquante pour la phase provisoire | La fiche technique de la prédalle est la seule source des caractéristiques de la prédalle (section, armatures, flèche admissible). Sans elle, on ne peut pas vérifier la phase provisoire |
| « Ne calcule aucune connexion » | Option C — B-48 calcule les phases, B-50 calcule les connexions. B-48 ne peut pas calculer des connexions dont il ne connaît pas les caractéristiques (armatures de connexion, rugosité) |
| « Ne déclare pas COMPLET si DOC-09 manque » | Verrou V12 — une prédalle sans fiche technique est une prédalle dont on ne connaît pas les armatures. Le mode doit refléter cette réalité |
| Filigrane + mention mode | Un plan de prédalle exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les deux phases — précision utile :

| Phase | Objet | Vérifications principales |
| --- | --- | --- |
| Ce qui gouverne | Provisoire | Comportement de la prédalle seule, avant coulage |
| Flexion, effort tranchant, flèche de décoffrage, levage | Souvent la flèche de décoffrage (critère de qualité) | Finale |
| Comportement du plancher collaborant | Flexion, effort tranchant, poinçonnement, flèche finale | Souvent la flexion ou la flèche finale (critère de sécurité) |

Le piège de la phase provisoire : un modèle qui reçoit une prédalle a tendance à ne calculer que la phase finale (le plancher collaborant). C'est insuffisant :
   * la prédalle seule, avant coulage, doit reprendre son poids propre + les charges de chantier (ouvriers, matériel, coffrage) ;
   * la flèche de décoffrage doit être ≤ la flèche admissible de la fiche technique — sinon, la prédalle fissure au décoffrage ;
   * l'étaiement provisoire doit être dimensionné pour la portée réelle entre étais.
Un modèle qui ignore la phase provisoire produit une note qui semble complète, mais qui est fausse en phase chantier. La prédalle peut casser au levage ou au décoffrage — c'est un accident grave.
Le piège de la fiche technique : une prédalle est un produit industriel — le fabricant fournit une fiche technique avec :
   * la section (épaisseur, largeur) ;
   * les armatures (nombre, diamètre, position) ;
   * le poids ;
   * la flèche admissible de décoffrage ;
   * les conditions de levage (points d'élingue).
Sans fiche technique (DOC-09), on ne peut pas vérifier la phase provisoire — c'est pourquoi B-48 s'appelle en mode PARAMÉTRIQUE si DOC-09 manque.
Le piège de la connexion : la connexion entre la prédalle et la dalle de compression est critique :
   * la rugosité de la surface de la prédalle doit être suffisante (EC2 §6.2.5) ;
   * les armatures de connexion (généralement des treillis ou des barres en attente) doivent reprendre l'effort de cisaillement à l'interface ;
   * si la connexion est insuffisante, la dalle de compression se sépare de la prédalle — c'est un désordre grave.
B-48 décrit la connexion, fournit les efforts à B-50, mais ne calcule pas les armatures de connexion — c'est B-50.
Le piège du poinçonnement : si une prédalle reçoit une charge ponctuelle (par exemple, un poteau ou un équipement lourd), il faut vérifier le poinçonnement (EC2 §6.4). C'est souvent oublié — mais c'est une vérification rapide et indispensable.
Le piège de l'étaiement : l'étaiement provisoire est souvent traité comme une « disposition de chantier » — c'est faux :
   * le nombre et l'espacement des étais déterminent la portée réelle de la prédalle en phase provisoire ;
   * un étaiement insuffisant (ou mal positionné) fissure la prédalle ;
   * l'étaiement doit être maintenu jusqu'au décoffrage (délai à respecter).
B-48 dimensionne l'étaiement et le mentionne sur les plans (plan d'étaiement).
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
| B-42 (Verticaux BA) | Les voiles qui reçoivent les appuis de la prédalle |
| B-43 (Planchers et dallages) | Les poutres ou dalles qui reçoivent les appuis de la prédalle |
| B-50 (Assemblages et ancrages) | Aucune donnée en amont — B-48 fournit les efforts, B-50 calcule les connexions |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-34 (Synthèse des réservations) | Les limites de percement admissibles en prédalle |
| B-50 (Assemblages et ancrages) | Les efforts aux appuis et aux connexions (N_Ed, V_Ed, M_Ed) — B-50 calcule les connexions |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (prédalles, armatures de connexion) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-48 — B-70 vérifie que chaque zone et chaque phase ont leur verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-48 |
| --- | --- | --- |
| MAT-01 à MAT-04 | Matériaux BA | BLOQUANTE |
| SEC-01 | Degré coupe-feu | BLOQUANTE (interdit le mode COMPLET si absente) |
| CHG-01, CHG-02 | Usage et surcharges | BLOQUANTE |
| CHG-03 | Poids propres des complexes de plancher | BLOQUANTE |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | BLOQUANTE (pour le poinçonnement) |
| NIV-02, NIV-06 | Niveaux de plancher, épaisseurs de plancher | BLOQUANTE |
| GEO-01 | Emprise / contour du bâtiment | BLOQUANTE |
| DOC-09 | Fiches techniques des prédalles | BLOQUANTE (pour la phase provisoire) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | NON BLOQUANTE (à défaut : PA-xx) |

Variables produites
B-48 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-08, NIV-02, NIV-06, GEO-01, DOC-09, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques PREDALLE-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-48, vous devez valider le nombre et l'espacement des étais — c'est une décision de chantier qui engage la responsabilité de l'entreprise. Un étaiement insuffisant (ou mal positionné) fissure la prédalle avant même le coulage. Le modèle propose, vous décidez (en coordination avec le chef de chantier).
Cas particulier — mode PARAMÉTRIQUE (DOC-09 manquante) : si la fiche technique de la prédalle n'est pas fournie (par exemple, la prédalle est commandée mais la fiche technique n'est pas encore arrivée), B-48 s'appelle en mode PARAMÉTRIQUE pour la phase provisoire :
   * les vérifications de la phase provisoire sont menées en littéral (avec la section et les armatures en symbole) ;
   * un tableau de sensibilité est produit sur les sections plausibles — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE DOC-09 » et suffixé _P ;
   * aucun plan exécutable n'est produit pour la phase provisoire.
La phase finale peut être en mode COMPLET si MAT-01 à MAT-04 et SEC-01 sont disponibles — les deux phases ont des modes indépendants.
Cas particulier — mode PARTIEL-DÉCLARÉ (SEC-01 manquante) : si SEC-01 (coupe-feu) n'est pas fournie pour une prédalle, B-48 s'appelle en mode PARAMÉTRIQUE (ou PARTIEL-DÉCLARÉ si une décision RDR a accepté une valeur). Le mode reflète la réalité : sans coupe-feu, l'enrobage n'est pas justifié.
Cas particulier — phase provisoire critique : si la phase provisoire gouverne le dimensionnement (ce qui est fréquent), B-48 le signale dans sa note. C'est important pour le chantier : la prédalle doit être étayée jusqu'au décoffrage (délai à respecter), et l'étaiement doit être conforme au plan d'étaiement.
Cas particulier — phase finale critique : si la phase finale gouverne le dimensionnement, la dalle de compression doit être ferraillée en conséquence (ferraillage complémentaire, treillis soudé). B-48 le signale dans sa note et sur les plans.
Cas particulier — prédalle sur poutres métalliques (plancher mixte) : si la prédalle repose sur des poutres métalliques, le plancher est mixte (prédalle béton + poutre métallique). B-48 traite la phase finale en EC4 (NF EN 1994-1-1/NA), et les connecteurs (goujons, cornières) relèvent de B-50. B-48 fournit les efforts de cisaillement aux connecteurs, B-50 calcule les connecteurs.
Cas particulier — prédalle sur voiles BA : si la prédalle repose sur des voiles BA (B-42), la connexion est assurée par des armatures en attente dans le voile, ou par un simple appui. B-48 vérifie la longueur d'appui et fournit les efforts à B-50 — le calcul des armatures de connexion relève de B-50.
Cas particulier — réservations et trémies : si la prédalle comporte des trémies (escaliers, gaines, fourreaux), B-48 :
   * vérifie que les trémies sont compatibles avec les armatures de la prédalle (ne coupent pas les barres principales) ;
   * prévoit des renforts autour des trémies (barres de renfort, chapeaux) ;
   * mentionne les trémies sur les plans avec cotes et positions.
Une trémie mal positionnée dans une prédalle coupe des barres — et une prédalle est un produit industriel qui ne se répare pas facilement sur chantier.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ». Le plan d'étaiement est obligatoire si la phase provisoire est traitée.
Consignation : la note B-48 est annexée au RDR (B-03) — elle documente le calcul des prédalles et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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