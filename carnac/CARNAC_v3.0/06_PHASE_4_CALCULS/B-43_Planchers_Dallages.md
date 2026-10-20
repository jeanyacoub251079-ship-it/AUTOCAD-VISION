Fichier 06_PHASE_4_CALCULS/B-43_Planchers_Dallages.md — CARNAC v3.0
________________


B-43 — PLANCHERS ET DALLAGES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-01 à MAT-04 et SEC-01 disponibles pour les dalles BA ; MAT-06 et MAT-08 disponibles pour les planchers bois) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante) · PARAMÉTRIQUE (SEC-01 manquante pour une dalle BA, ou section d'un existant non sondée) · SANS OBJET (MPD a statué) |
| Paramètre d'appel | {{type}} = dalle BA / dallage sur terre-plein / plancher bois |
| Entrées lues | MAT-01 à MAT-04, MAT-06, MAT-08, SEC-01, SEC-03, CHG-01 à CHG-03, CHG-08, NIV-02, NIV-05, NIV-06, GEO-01, B-20, B-21, B-22, B-40 (appuis sur fondations), B-46 (appuis sur existant), B-50 (assemblages) |
| Sortie unique | Note de calcul du plancher ou du dallage + plans d'exécution cotés + coupes + nomenclature + export DXF à calques PLANCHER-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, B-21 et B-22, quand le projet comporte un plancher ou un dallage à calculer. En mode SANS OBJET (aucun plancher neuf dans le périmètre), B-43 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (matériaux, coupe-feu, charges, usage), la note d'hypothèses (B-22), la conception de B-20 (porteurs prédimensionnés), la DDC préliminaire (B-21), les positions des appuis (B-40, B-42, B-46). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{type}}.
Ce que vous validez à la sortie :
   * la DDC d'exécution aux planchers (distincte de B-21) ;
   * le dimensionnement selon le type (BA, dallage, bois) ;
   * le ferraillage ou les sections bois ;
   * les dispositions constructives (joints, réservations, appuis) ;
   * les efforts aux appuis transmis à B-50 ;
   * l'auto-contrôle par zone.
Le périmètre exact de B-43 :

| Ce que B-43 produit | Ce que B-43 ne produit pas |
| --- | --- |
| DDC aux planchers (surfaces d'influence, charges par couche, exploitation) | Calcul des attentes, connecteurs, ancrages (B-50) |
| Dimensionnement du plancher BA ou du dallage | Calcul des poutres de charpente (B-44) |
| Ferraillage BA (nappes, chapeaux, renforts) | Calcul des profilés métalliques de plancher (B-45) |
| Dimensionnement du plancher bois (flexion, cisaillement, flèche différée) | Prédalles et planchers préfabriqués (B-48) |
| Dispositions constructives (joints, réservations) | Vérification des planchers existants à conserver (B-46) |
| Efforts aux appuis transmis à B-50 | Dimensionnement de la protection au feu (hors CARNAC) |

L'articulation avec B-50 (option C) :

| Brique | Rôle sur les assemblages |
| --- | --- |
| B-43 | Calcule le plancher et fournit à B-50 les efforts aux appuis (N_Ed, V_Ed, M_Ed, efforts de cisaillement aux connecteurs si mixte). Ne calcule pas les assemblages. |
| B-50 | Calcule les assemblages (boulons, soudures, connecteurs, sabots, équerres) et fait le contrôle croisé avec les efforts fournis par B-43 et les logements prévus par les briques amont. |

Ce que B-43 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des assemblages (boulons, sabots, connecteurs, tiges) | B-50 |
| Calcul des poutres de charpente (toiture) | B-44 |
| Calcul des profilés métalliques de plancher | B-45 |
| Prédalles et planchers préfabriqués | B-48 |
| Vérification des planchers existants à conserver | B-46 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution des planchers et dallages de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour le type {{type}} (dalle BA / dallage sur terre-plein / plancher bois). Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1) : charges d'exploitation, cloisons.
- EC2 (NF EN 1992-1-1/NA) : dalles BA, dallage sur terre-plein — §6.1 (flexion), §6.2 (effort tranchant), §6.4 (poinçonnement), §7.4 (flèches), §9.3 (dispositions dalles).
- EC5 (NF EN 1995-1-1/NA) : planchers bois — §6.1 (flexion), §6.1.7 (cisaillement), §6.3.2 (flambement), §7.2 (flèches), §8 (assemblages).
- NF DTU 13.3 (dallages) pour les dispositions constructives du dallage.
- Pour chaque formule, tu cites la référence exacte.


MÉTHODE — DANS CET ORDRE


Étape 1 — Hypothèses et données d'entrée
Reprends de la FDC et de la note d'hypothèses :
- pour BA : MAT-01, MAT-02, MAT-03, MAT-04, SEC-01 ;
- pour bois : MAT-06, classe de service (MAT-08) ;
- pour dallage : classe d'agressivité du sol (SOL-05), classement termites (SEC-03), portance du sol support (SOL-01 si elle est aussi utilisée comme portance du dallage) ;
- niveaux (NIV-02, NIV-05, NIV-06) ;
- usages et charges d'exploitation (CHG-01, CHG-02) ;
- cloisons et équipements lourds (CHG-08).
Tu ne retiens AUCUNE valeur hors FDC. Si une donnée manque, tu appliques le mode {{mode}}.


Étape 2 — Descente de charges aux planchers
Établis la DDC d'exécution aux planchers (et non la DDC préliminaire de B-21) :
- surface d'influence par zone de plancher ;
- charges permanentes décomposées couche par couche (revêtement, chape, dalle ou plancher, isolation, plafond, équipements) ;
- charges d'exploitation par catégorie EC1 ;
- cloisons (EC1 §6.3.1.2) ;
- combinaisons ELS et ELU distinctes.
Présente un tableau par zone.


Étape 3 — Dimensionnement selon le type


BLOC A — DALLE BA
- épaisseur de dalle : prédimensionnement par ratio (L/25 pour dalle portant sur 1 sens, L/30 pour 2 sens), puis vérification ;
- flexion : M_Ed et M_Rd selon EC2 §6.1, avec ferraillage correspondant ;
- effort tranchant : V_Ed ≤ V_Rd,c (EC2 §6.2.2) ;
- poinçonnement : v_Ed ≤ v_Rd,c (EC2 §6.4) aux appuis ponctuels (poteaux) ;
- flèches : si requises par l'usage (EC2 §7.4) ;
- A_s,min = max(0,26·f_ctm/f_yk·b·d ; 0,0013·b·d) (EC2 §9.3.1.1) ;
- ferraillage : nappe inférieure, nappe supérieure si nécessaire, chapeaux aux appuis, renforts ponctuels ;
- dispositions constructives (EC2 §9.3) : enrobage, espacement, recouvrements, longueur d'ancrage aux appuis.


BLOC B — DALLAGE SUR TERRE-PLEIN
- portance du sol support : q_adm (SOL-01), épaisseur du dallage déterminée selon NF DTU 13.3 et les charges ;
- contraintes sous dallage : σ ≤ q_adm du sol support ;
- flexion : dallage sur appuis continus (méthode simplifiée NF DTU 13.3 ou méthode des éléments finis si justifié) ;
- retrait : joints sciés, joints de fractionnement, dispositions contre le retrait ;
- A_s,min et treillis soudé : ST25C ou HA selon calcul ;
- renforts ponctuels : angles, rives, charges roulantes ;
- désolidarisation au droit des poteaux, semelles et ouvrages existants (joints de désolidarisation) ;
- barrière anti-termites si SEC-03 en zone classée ;
- complexe de dallage (couche par couche) : géotextile, GNT, sablage, barrière termites, isolation XPS, film polyane, dallage BA, revêtement.


BLOC C — PLANCHER BOIS
- vérification des solives et poutres : flexion (EC5 §6.1.6), cisaillement (EC5 §6.1.7), flèche différée (EC5 §7.2, k_def) ;
- flèche limite : L/300 ou L/200 selon usage ;
- flambement latéral des poutres (EC5 §6.3.3, déversement) : maintien par le plancher si justifié ;
- appuis : vérification de la compression perpendiculaire aux appuis (EC5 §6.1.5), longueur d'appui ;
- connexions (renvoi B-50 pour le calcul, B-43 pour les efforts) ;
- dispositions constructives : entretoises, contreventement, protection contre l'humidité.


Étape 4 — Efforts aux appuis (transmis à B-50)
Pour chaque appui (poteau, mur, poutre) :
- N_Ed transmis ;
- V_Ed (effort tranchant) ;
- M_Ed si excentrement ;
- efforts de cisaillement aux connecteurs (si plancher mixte) ;
- efforts aux appuis de plancher bois (compression perpendiculaire).
Tu ne calcules PAS les assemblages (boulons, sabots, connecteurs) : c'est B-50.


Étape 5 — Dispositions constructives
Selon le type :
- joints de retrait, joints de fractionnement, joints de désolidarisation ;
- réservations (trémies, gaines, fourreaux) : positions et dimensions compatibles avec le ferraillage ;
- renforts aux angles et aux rives ;
- liaisons avec les verticaux (B-42) et les fondations (B-40) ;
- mention « protection au feu adéquate à prévoir (hors lot GO) ».


Étape 6 — Livrables graphiques
Plans d'exécution cotés + coupes + nomenclature + export DXF à calques normalisés :
- PLANCHER-AXES : axes, trames, points de calage ;
- PLANCHER-COFFRAGE : contours, épaisseurs, cotations, réservations, joints ;
- PLANCHER-ACIER-INF : nappe inférieure, sections, espacements, recouvrements ;
- PLANCHER-ACIER-SUP : nappe supérieure, chapeaux, renforts ;
- PLANCHER-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux.
Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », cartouche avec indice et date, mention du mode {{mode}}, mention « protection au feu adéquate à prévoir (hors lot GO) ».


Étape 7 — Auto-contrôle déclaré
Vérifie et déclare, zone par zone :
- chaque zone a ses charges et ses combinaisons ELS et ELU ;
- chaque zone a son ferraillage ou ses sections bois complètes ;
- chaque zone satisfait A_min et dispositions constructives ;
- chaque appui a ses efforts transmis à B-50 ;
- chaque réservation est compatible avec le ferraillage ;
- les joints de retrait et de désolidarisation sont prévus ;
- l'échelle est cohérente ;
- le cartouche est complet.
Tu déclares aussi ce qui est DE PRINCIPE et ce qui reste À LEVER.


INTERDICTIONS
- Ne calcule AUCUN assemblage (boulons, sabots, connecteurs, tiges) : c'est B-50.
- N'invente aucune valeur hors FDC.
- Ne mélange pas ELS et ELU.
- Ne déclare pas COMPLET si une donnée bloquante manque (verrou V12). Notamment : SEC-01 manquante interdit COMPLET pour une dalle BA.
- Ne produis aucun livrable exécutable si le mode est PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu : mention générique seule.
- N'utilise aucune valeur « par expérience ».
- Ne recopie pas la DDC préliminaire de B-21.
- Ne confonds pas plancher bois (B-43) et charpente bois (B-44) : le plancher porte les charges d'usage intérieur, la charpente porte la toiture.


SORTIE
Pièce 1 — Note de calcul
Sections 1 à 7 comme ci-dessus, avec référence normative pour chaque formule.


Pièce 2 — Plans d'exécution
Plan général coté + coupes + nomenclature + export DXF à calques PLANCHER-*.


Pièce 3 — Auto-contrôle déclaré
Tableau par zone : charges / ferraillage ou sections / appuis / réservations / joints / verdict. Points DE PRINCIPE et À LEVER.


CRITÈRE D'ACCEPTATION
La note et les plans sont acceptés si :
- chaque donnée d'entrée est issue de la FDC ;
- la DDC d'exécution est établie (distincte de B-21) ;
- chaque zone satisfait les vérifications du type {{type}} (flexion, effort tranchant, poinçonnement pour BA ; portance et retrait pour dallage ; flexion, cisaillement, flèche différée pour bois) ;
- chaque zone satisfait A_min et dispositions constructives ;
- chaque appui a ses efforts transmis à B-50 ;
- chaque réservation est compatible avec le ferraillage ;
- les joints sont prévus (retrait, fractionnement, désolidarisation) ;
- les plans portent le filigrane, l'indice, le mode, la mention de protection au feu générique ;
- l'auto-contrôle déclare chaque zone ;
- aucune protection au feu n'a été dimensionnée ;
- aucune valeur hors FDC n'a été utilisée.
Si un seul de ces onze points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{type}} (par dalle BA, dallage sur terre-plein ou plancher bois). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Paramètre {{type}} = dalle BA / dallage / plancher bois | Les trois types de planchers ont des méthodes de vérification radicalement différentes (EC2, NF DTU 13.3, EC5). Un seul prompt avec trois blocs évite la répétition de la structure (DDC, dispositions, auto-contrôle) tout en gardant les spécificités visibles |
| Bloc A — poinçonnement | Un plancher BA sur poteaux sans vérification du poinçonnement est un plancher qui peut poinçonner. C'est la vérification la plus souvent oubliée dans les notes de plancher |
| Bloc B — joints de désolidarisation | Le désordre classique du dallage est le poinçonnement par retrait au droit des ouvrages rigides. La désolidarisation au droit des poteaux, semelles et existants est la disposition qui l'évite |
| Bloc C — flèche différée | Un plancher bois sans vérification de flèche différée (k_def) est un plancher qui fléchit dans le temps. C'est la vérification qui distingue EC5 d'EC2 |
| « Ne confonds pas plancher bois (B-43) et charpente bois (B-44) » | Un plancher bois porte les charges d'usage intérieur (surcharges EC1), une charpente bois porte la toiture (neige, vent). Les méthodes EC5 sont les mêmes, mais les charges et les combinaisons diffèrent. La confusion conduit à des planchers surdimensionnés ou sous-dimensionnés |
| « Ne calcule aucun assemblage : c'est B-50 » | Option C — B-43 calcule les efforts aux appuis (étape 4), B-50 calcule les assemblages. La circulation des efforts est la même que pour B-42 |
| « Ne déclare pas COMPLET si SEC-01 manque » | Même règle que B-42 : la tenue au feu détermine l'enrobage de la dalle BA |
| Réservations compatibles avec le ferraillage | Une trémie mal positionnée coupe des barres. La vérification de compatibilité est indispensable avant exécution |
| Mention générique de protection au feu | Formulation imposée par votre décision de périmètre, rappelée sur les plans |
| « Ne recopie pas la DDC préliminaire de B-21 » | Une DDC préliminaire recopiée n'a pas été vérifiée pour l'exécution. Le plancher est l'élément où cette erreur est la plus fréquente — et la plus coûteuse (les dalles sont les plus gros volumes de béton) |

Les trois blocs de dimensionnement — précision utile :

| Type | Vérifications principales | Dispositions constructives critiques |
| --- | --- | --- |
| Dalle BA | Flexion, effort tranchant, poinçonnement, flèches, A_min | Nappe inférieure, nappe supérieure, chapeaux aux appuis, recouvrements |
| Dallage sur terre-plein | Portance du sol support, flexion, retrait | Joints de retrait, joints de fractionnement, joints de désolidarisation, barrière termites |
| Plancher bois | Flexion, cisaillement, flèche différée, flambement latéral, compression perpendiculaire | Entretoises, contreventement, protection contre l'humidité, ventilation |

Le piège du poinçonnement : un plancher BA qui repose sur des poteaux doit être vérifié au poinçonnement. C'est une vérification que les modèles oublient fréquemment, parce qu'elle n'est pas dans la méthode de flexion classique. Sans elle, une dalle peut se poinçonner brutalement — c'est-à-dire s'effondrer localement autour d'un poteau, sans signe préalable.
Le piège du dallage : un dallage sur terre-plein est souvent traité comme une simple « dalle sur sol », sans vérification de la portance du sol support, ni des joints. C'est faux :
   * la portance du sol support (q_adm) doit être vérifiée — le dallage ne reprend pas les charges d'un plancher, il les transmet au sol ;
   * les joints de retrait sont indispensables — sans eux, le dallage fissure aléatoirement ;
   * les joints de désolidarisation au droit des ouvrages rigides sont indispensables — sans eux, le dallage poinçonne les semelles ou les poteaux.
Le piège du plancher bois : un plancher bois est souvent traité avec les mêmes méthodes qu'une charpente, sans vérification de la flèche différée. C'est faux :
   * la flèche différée (k_def) gouverne souvent le dimensionnement d'un plancher habitable — un plancher qui fléchit trop dans le temps est inconfortable, même s'il est structurellement stable ;
   * la compression perpendiculaire aux appuis est souvent oubliée — un plancher bois sur appuis courts écrase le bois perpendiculairement aux fibres ;
   * le flambement latéral (déversement) est conditionné par le maintien latéral — qui doit être justifié, pas supposé.
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
| B-40 (Fondations superficielles) | Les appuis du dallage sur les semelles (positions) — B-43 prévoit les joints de désolidarisation |
| B-42 (Verticaux BA) | Les appuis des poteaux sur le plancher — B-43 transmet les efforts à B-50 |
| B-46 (Maçonnerie : vérification) | Les appuis du plancher sur l'existant — B-43 vérifie la contrainte transmise |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-34 (Synthèse des réservations) | Les dalles et planchers concernés, avec leurs zones critiques |
| B-45 (Structure métallique) | Les appuis des profilés de plancher sur les dalles |
| B-46 (Maçonnerie : vérification) | Les appuis des planchers sur les murs |
| B-47 (Escaliers) | Les planchers qui reçoivent les appuis de l'escalier |
| B-48 (Prédalles et planchers préfabriqués) | Les poutres ou dalles qui reçoivent les appuis de la prédalle |
| B-50 (Assemblages et ancrages) | Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les assemblages |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (barres, treillis, solives) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-43 — B-70 vérifie que chaque zone a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-43 |
| --- | --- | --- |
| MAT-01 à MAT-04 | Matériaux BA | BLOQUANTE (pour dalle BA et dallage) |
| MAT-06, MAT-08 | Matériaux bois et classe de service | BLOQUANTE (pour plancher bois) |
| SEC-01 | Degré coupe-feu | BLOQUANTE (interdit le mode COMPLET pour une dalle BA) |
| SEC-03 | Classement termites de la commune | BLOQUANTE (pour dallage sur terre-plein) |
| SOL-01 | Contrainte admissible ELS | BLOQUANTE (pour dallage sur terre-plein — portance du sol support) |
| SOL-05 | Classe d'agressivité du sol | BLOQUANTE (pour dallage — protection du béton) |
| CHG-01 à CHG-03 | Usage, surcharges, poids propres | BLOQUANTE |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | BLOQUANTE |
| NIV-02, NIV-05, NIV-06 | Niveaux de plancher, niveau fini du dallage, épaisseurs | BLOQUANTE |
| GEO-01 | Emprise / contour du bâtiment | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | BLOQUANTE si sous-sol ou soutènement |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | NON BLOQUANTE (à défaut : PA-xx) |

Variables produites
B-43 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-04, MAT-06, MAT-08, SEC-01, SEC-03, SOL-01, SOL-05, CHG-01 à CHG-03, CHG-08, NIV-02, NIV-05, NIV-06, GEO-01, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques PLANCHER-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-43, vous devez valider le type de plancher (dalle BA, dallage, plancher bois) pour chaque zone. Un plancher bois traité comme une dalle BA (ou l'inverse) est une erreur de méthode, pas de calcul. C'est votre appréciation qui fait foi.
Cas particulier — mode PARAMÉTRIQUE (SEC-01 manquante pour une dalle BA) : si SEC-01 (coupe-feu) n'est pas fournie pour une dalle BA, B-43 s'appelle en mode PARAMÉTRIQUE :
   * les vérifications EC2 (flexion, effort tranchant, poinçonnement) sont menées normalement ;
   * l'enrobage de tenue au feu est traité en littéral (avec le degré coupe-feu en symbole) ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE SEC-01 » et suffixé _P ;
   * aucun plan exécutable n'est produit.
Cas particulier — dallage sur terre-plein avec SEC-03 : si le projet est situé en zone termitée (SEC-03), B-43 prévoit une barrière anti-termites physico-chimique sous le dallage. La disposition est mentionnée sur le plan et dans la note, avec la référence au classement préfectoral de la commune.
Cas particulier — plancher bois sur existant : si le plancher bois repose sur des appuis existants (murs, poutres), B-43 vérifie :
   * la compression perpendiculaire aux appuis (EC5 §6.1.5) ;
   * la longueur d'appui minimale (généralement ≥ 100 mm pour les poutres, selon EC5 §10) ;
   * la contrainte transmise à l'existant (renvoi à B-46 si la maçonnerie existante n'est pas vérifiée).
B-43 ne vérifie pas l'existant — c'est B-46. B-43 transmet la contrainte, B-46 vérifie qu'elle est admissible.
Cas particulier — dallage sur semelles : si le dallage est en contact avec des semelles existantes (cas Flora), B-43 prévoit :
   * un joint de désolidarisation au droit de chaque semelle (polystyrène + mastic) ;
   * une consigne de coulage (couler à même la semelle, ne pas compacter sur le débord) ;
   * une mention explicite dans la note et sur les plans.
Le non-respect de cette consigne conduit à un tassement différentiel et à des fissures du dallage. C'est une disposition de chantier, pas un calcul — mais c'est une disposition qui doit être prescrite.
Cas particulier — plancher mixte (dalle BA sur poutres métalliques) : si le plancher est mixte (dalle BA collaborante sur poutres métalliques), B-43 traite la dalle BA selon EC4 (NF EN 1994-1-1/NA), et les poutres métalliques relèvent de B-45. Les connecteurs (goujons, cornières) relèvent de B-50 — B-43 fournit les efforts de cisaillement aux connecteurs, B-50 calcule les connecteurs.
Cas particulier — trémies et réservations : si le plancher comporte des trémies (escaliers, gaines, fourreaux), B-43 :
   * vérifie que les trémies sont compatibles avec le ferraillage (ne coupent pas les barres principales) ;
   * prévoit des renforts autour des trémies (barres de renfort, chapeaux) ;
   * mentionne les trémies sur les plans avec cotes et positions.
Une trémie mal positionnée coupe des barres — c'est une erreur de conception qui se voit à l'exécution, mais qui coûte cher.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-43 est annexée au RDR (B-03) — elle documente le calcul des planchers et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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