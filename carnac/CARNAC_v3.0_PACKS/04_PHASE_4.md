<!-- PACK CARNAC v3.0 — PACK 04 — PHASE 4 : CALCULS D'EXÉCUTION (B-40 à B-50) -->

# PACK 04 — PHASE 4 : CALCULS D'EXÉCUTION (B-40 à B-50)

**Quand coller ce pack** : Quand la conception et la stabilité globale sont visées.

**Ce qu'il contient** : Onze fiches de calcul : fondations superficielles et profondes, verticaux BA, planchers et dallages, charpente bois, structure métallique, maçonnerie, escaliers, prédalles, linteaux et seuils, assemblages et ancrages.

**Note d'usage** : Pack le plus lourd (~97 000 tokens). Si votre contexte est limité, deux coupures possibles sont matérialisées dans le fichier : `B-40` à `B-45`, puis `B-46` à `B-50`.

**Prérequis** : le pack `00_SOCLE.md` doit être collé avant celui-ci, dans la même discussion.

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
**[Début du fichier : 06_PHASE_4_CALCULS/B-40_Fondations_Superficielles.md]**

Fichier 06_PHASE_4_CALCULS/B-40_Fondations_Superficielles.md — CARNAC v3.0
________________


B-40 — FONDATIONS SUPERFICIELLES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (SOL-01 à SOL-05, MAT-01 à MAT-04, SEC-01 disponibles) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante) · PARAMÉTRIQUE (SOL-01 ou SOL-02 manquante : calcul littéral + tableau de sensibilité non contractuel) · SANS OBJET (MPD a statué que les fondations ne sont ni modifiées ni sollicitées) |
| Entrées lues | SOL-01 à SOL-07, MAT-01 à MAT-04, CHG-01 à CHG-03, CHG-07, GEO-01 à GEO-05, NIV-01 à NIV-04, SIT-04, SIT-05, EXI-05, B-20 (conception), B-21 (DDC préliminaire), B-22 (hypothèses), B-50 (ancrages — en aval) |
| Sortie unique | Note de calcul de fondations superficielles + plans d'exécution cotés + coupes + nomenclature + export DXF à calques FOND-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Brique | Rôle sur les ancrages |
| --- | --- |
| B-40 | Vérifie que la géométrie de la semelle permet de loger les ancrages calculés par B-50 (enrobage, espacement, hauteur). Ne calcule pas les ancrages eux-mêmes |
| B-42 / B-45 | Fournissent à B-50 les efforts à ancrer (N_Ed, M_Ed, section des barres, tiges) |
| B-50 | Calcule les ancrages (longueurs de scellement, tiges, platines, retours) et fait le contrôle croisé avec les logements vérifiés par B-40 |

Règle de circulation : si un ancrage ne rentre pas dans la semelle, c'est B-40 qui s'agrandit — pas B-50 qui réduit ses ancrages, pas B-42 qui réduit ses barres.
Ce que B-40 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des ancrages (longueurs de scellement, tiges, platines) | B-50 |
| Calcul des poteaux et de leurs attentes | B-42 |
| Vérification des éléments existants sous semelle | B-46 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |
| Étude géotechnique | Hors périmètre CARNAC (audit B-12, recommandation de mission) |

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

| Clause | Pourquoi |
| --- | --- |
| DDC d'exécution distincte de B-21 | La DDC préliminaire sert à choisir les sections en conception ; la DDC d'exécution est cumulative et exacte. Les confondre conduit à des sections fausses en EXE — c'est exactement l'erreur qui menace toute étude |
| « Aucune valeur hors FDC » | Verrou V3 — une valeur « par expérience » dans une note de calcul n'est pas défendable en réunion de chantier. Chaque valeur vient d'une pièce citée ou d'un calcul tracé |
| « Ne calcule aucun ancrage : c'est B-50 » | Option C — l'ancrage est calculé par la brique qui connaît les efforts à ancrer (B-42 pour les attentes de poteaux BA, B-45 pour les tiges de poteaux métalliques), et le logement est vérifié par B-40. B-40 ne peut pas calculer des ancrages dont il ne connaît pas les efforts |
| « Tu vérifies seulement que la géométrie permet de les loger » | La nuance est capitale : B-40 ne calcule pas les ancrages, mais il doit s'assurer qu'ils rentrent. Si la semelle ne permet pas de loger les ancrages de B-50, c'est B-40 qui doit s'agrandir — pas B-50 qui doit réduire ses ancrages |
| « Ne déclare pas COMPLET si une donnée bloquante manque » | Verrou V12 — une note de calcul COMPLET sans q_adm est une note fausse. Le mode doit refléter la réalité |
| ELS et ELU distincts | Les combinaisons ELS et ELU ne se mélangent pas : une note de calcul qui présente un seul tableau « N » sans préciser ELS ou ELU est illisible pour un vérificateur |
| « Ne recopie pas la DDC préliminaire » | Une DDC préliminaire recopiée en DDC d'exécution est une DDC d'exécution qui n'a pas été vérifiée — c'est exactement le type d'erreur qui ne se voit pas |
| Auto-contrôle par semelle | Un auto-contrôle global ne détecte pas une semelle mal centrée ou un ferraillage manquant sur une semelle. L'auto-contrôle par semelle est le seul qui prouve que chaque élément a été vérifié |
| Filigrane + mention mode | Un plan de fondations exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté. La mention du mode est une protection |
| « Ne dimensionne pas la protection au feu » | Exclusion CARNAC explicite. La mention générique est autorisée, le dimensionnement ne l'est pas |

Le mode PARAMÉTRIQUE en pratique — précision utile :

| Situation | Ce que B-40 produit | Ce qu'elle ne produit pas |
| --- | --- | --- |
| COMPLET | Note complète, plans cotés, DXF, auto-contrôle | — |
| PARTIEL-DÉCLARÉ | Note avec valeur déclarée au RDR, mention de l'auteur et de la date, plans portant la mention « sous hypothèse H-xx » | Une valeur choisie par le modèle |
| PARAMÉTRIQUE | Formules littérales avec q_adm en symbole, tableau de sensibilité non contractuel, note filigranée « EN ATTENTE DE SOL-01 » | Aucune valeur retenue, aucun plan exécutable, aucun DXF à diffuser |
| SANS OBJET | Ligne de justification (« fondations existantes non sollicitées, motif : travaux de superstructure ») | Aucun calcul, aucun plan |

Le piège de la valeur « provisoire » : un modèle qui reçoit un projet avec q_adm absent a tendance à proposer une valeur « provisoire » (par exemple, 0,25 MPa) pour « faire avancer le projet ». C'est exactement ce qu'il faut interdire :
   * la valeur provisoire n'est pas sourcée — elle ne peut pas être défendue ;
   * elle devient implicitement la valeur de calcul — et les semelles dimensionnées sur cette base sont fausses ;
   * elle masque le besoin d'une mission G3 — et la MOA ne commande pas la mission complémentaire.
Le mode PARAMÉTRIQUE est la seule réponse correcte : on produit les formules littérales, on identifie le besoin (G3), et on laisse la décision à la MOA.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-12 (Audit des pièces géotechniques) | Les valeurs exploitables (SOL-01, SOL-02, SOL-03, SOL-05) — B-40 ne peut pas s'exécuter en COMPLET si ces valeurs sont insuffisantes ou ambiguës |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-25 (Stabilité globale, contreventement, joints) | Les efforts horizontaux et moments d'ensemble transmis au sol d'assise |
| B-42 (Verticaux BA) | Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement |
| B-45 (Structure métallique) | Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement |
| B-50 (Assemblages et ancrages) | Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-41 (Fondations profondes) | Les efforts aux semelles — B-41 vérifie la cohérence si les pieux reprennent une partie des charges |
| B-42 (Verticaux BA) | La géométrie des semelles (dimensions, positions) — B-42 vérifie que les attentes peuvent être logées |
| B-43 (Planchers et dallages) | Les appuis du dallage sur les semelles (positions) — B-43 prévoit les joints de désolidarisation |
| B-45 (Structure métallique) | Les appuis des poteaux métalliques sur les semelles |
| B-46 (Maçonnerie : vérification) | Les appuis des murs sur les semelles |
| B-50 (Assemblages et ancrages) | Le logement vérifié — B-50 fait le contrôle croisé et renvoie la correction si l'ancrage ne rentre pas |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-40 — B-70 vérifie que chaque semelle a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-40 |
| --- | --- | --- |
| SOL-01 | Contrainte admissible ELS | BLOQUANTE |
| SOL-02 | Contrainte admissible ELU | BLOQUANTE |
| SOL-03 | Profondeur de bon sol / ancrage minimal | BLOQUANTE |
| SOL-05 | Classe d'agressivité du sol (XA) | BLOQUANTE (pour l'enrobage et le ciment) |
| SOL-06 | Nappe, hydrologie, drainage | NON BLOQUANTE (si absente, mention de vérification à faire) |
| SOL-07 | Tassements admissibles / différentiels | NON BLOQUANTE (si absente, mention de vérification à faire) |
| MAT-01 | Classe de résistance du béton | BLOQUANTE |
| MAT-02 | Classe d'exposition | BLOQUANTE |
| MAT-03 | Enrobage nominal | BLOQUANTE |
| MAT-04 | Nuance d'acier BA | BLOQUANTE |
| NIV-01, NIV-04 | Niveau de terrain naturel, niveau d'assise | BLOQUANTE |
| SIT-04, SIT-05 | Distance aux soubassements, emprise en fouille | BLOQUANTE (pour les dispositions constructives) |
| GEO-01 à GEO-05 | Géométrie et positions | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | BLOQUANTE si sous-sol ou soutènement |

Variables produites
B-40 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | SOL-01 à SOL-07, MAT-01 à MAT-04, NIV-01, NIV-04, SIT-04, SIT-05, GEO-01 à GEO-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques FOND-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 06_PHASE_4_CALCULS/B-40_Fondations_Superficielles.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-41_Fondations_Profondes.md]**

Fichier 06_PHASE_4_CALCULS/B-41_Fondations_Profondes.md — CARNAC v3.0
________________


B-41 — FONDATIONS PROFONDES (VÉRIFICATION EN MODE DÉGRADÉ)
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-12 (Audit Géotechnique) |
| Brique suivante | B-50 (Assemblages et ancrages), B-60 (Plans d'exécution) |
| Modes d'appel | PARAMÉTRIQUE (mode par défaut : les données de pieux sont rarement complètes, et nous ne concevons pas de pieux) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante) · SANS OBJET (MPD a statué qu'il n'y a pas de fondations profondes dans le périmètre) |
| Note sur le mode | B-41 est une brique de vérification, pas de conception : la conception de fondations profondes est hors de notre cœur de métier et relève d'une mission géotechnique spécifique. Les modes d'appel de B-41 sont donc, par construction : PARAMÉTRIQUE (par défaut), PARTIEL-DÉCLARÉ, SANS OBJET. |
| Entrées lues | SOL-01 à SOL-07, DOC-06 (rapport géotechnique), B-12 (audit géotechnique), B-20 (conception), B-21 (DDC préliminaire), données de pieux existants (EXI-04) ou prescrits par un spécialiste |
| Sortie unique | Note de vérification des fondations profondes : hypothèses contrôlées, données manquantes, risques, recommandation de mission G3/G4 — pas de plan de pieux |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-12 (audit géotechnique) et B-20 (conception), quand le projet comporte des fondations profondes (pieux existants à vérifier, pieux prescrits par un spécialiste, micropieux). En mode SANS OBJET (pas de fondations profondes dans le périmètre), B-41 produit une ligne de justification.
Ce que vous fournissez à l'IA : le rapport géotechnique (DOC-06), l'audit B-12, la conception B-20 (si des pieux sont prévus), les données de pieux existants (EXI-04) ou prescrits par un spécialiste, la DDC préliminaire B-21. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * les hypothèses de pieux (cohérence avec la DDC, la stratigraphie, la géométrie) ;
   * les données manquantes (essais, sondages, reconnaissance) ;
   * les recommandations de mission (G3, G4, essais complémentaires) ;
   * les points à faire valider par le spécialiste.
Le périmètre exact de B-41 :

| Ce que B-41 produit | Ce que B-41 ne produit pas |
| --- | --- |
| Contrôle des hypothèses de pieux (frottement, pointe, groupe, tassement) | Calcul de pieux (capacité portante, tassement, groupe) |
| Signalement des données manquantes | Plans de pieux |
| Vérification de la cohérence avec la DDC | Choix de la technique de pieux (battus, forés, micropieux) |
| Recommandation de mission G3/G4 | Calcul des ancrages de pieux (B-50) |
| Liste des points à faire valider par le spécialiste | Dimensionnement de la protection au feu (hors CARNAC) |

La règle la plus importante : B-41 contrôle les hypothèses, elle ne recalculle pas la capacité portante. La nuance est capitale : contrôler la cohérence entre la capacité portante annoncée et les charges transmises est à notre portée ; recalculer la capacité portante ne l'est pas — c'est le métier du géotechnicien.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de VÉRIFICATION des fondations profondes de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}. Tu ne conçois AUCUN pieu : tu contrôles les hypothèses, tu signales les manques, tu recommandes les essais nécessaires.


RÈGLES NORMATIVES
- EC7 (NF EN 1997-1) et NF P 94-262 : fondations profondes.
- NF P 94-500 : missions géotechniques (G1 à G5).
- Pour chaque contrôle, tu cites la référence normative.


MÉTHODE


Étape 1 — Inventaire des données disponibles
Identifie la nature des fondations profondes concernées :
- pieux existants à vérifier (bâtiment existant) ;
- pieux prescrits par un spécialiste (bureau d'études géotechniques, BET structure) ;
- micropieux prescrits.
Pour chaque, cite la source (rapport géotechnique, plan de pieux, note de calcul du spécialiste) et son indice.


Étape 2 — Contrôle des hypothèses
Pour chaque donnée de pieu fournie, contrôle :
- la cohérence entre la capacité portante annoncée et les charges transmises (DDC B-21 ou B-40) ;
- la cohérence entre la longueur de pieu et la stratigraphie du rapport géotechnique ;
- la cohérence entre le nombre de pieux et la géométrie de la fondation (B-20) ;
- la présence ou l'absence de vérification du groupe de pieux ;
- la présence ou l'absence de vérification du tassement.
Tu ne recalculés PAS la capacité portante : tu contrôles sa cohérence avec les autres données.


Étape 3 — Signalement des données manquantes
Identifie ce qui manque pour que la vérification soit complète :
- essais de chargement (statique, dynamique) ;
- essais pressiométriques ou pénétrométriques complémentaires ;
- reconnaissance de la stratigraphie sous la pointe ;
- vérification du groupe ;
- vérification du tassement.
Chaque donnée manquante est rattachée à son code CARNAC (SOL-xx) et à sa brique (B-41).


Étape 4 — Recommandation de mission
Si les données sont insuffisantes, recommande une mission :
- G3 (mission géotechnique d'exécution) si le suivi de chantier est nécessaire ;
- G4 (mission géotechnique de supervision) si la conception doit être revue ;
- essais complémentaires (essais de chargement, essais pressiométriques).
Chaque recommandation cite sa base normative (NF P 94-500) et la conséquence de sa non-commande (briques suspendues, réserves à porter).


Étape 5 — Points à faire valider par le spécialiste
Liste les points que nous ne pouvons pas vérifier nous-mêmes et qui doivent être validés par un spécialiste :
- capacité portante des pieux ;
- tassement du groupe ;
- interaction sol-structure ;
- choix de la technique de pieux.


INTERDICTIONS
- Ne conçois AUCUN pieu : pas de choix de section, de longueur, de technique, de ferraillage.
- Ne calcule AUCUNE capacité portante, AUCUN tassement, AUCUNE vérification de groupe.
- Ne produis AUCUN plan de pieux.
- Ne sors pas des trois modes d'appel de la fiche : PARAMÉTRIQUE (par défaut), PARTIEL-DÉCLARÉ, SANS OBJET.
- Ne retiens aucune valeur sans la rattacher à une source citée.
- Ne propose aucune valeur de repli : la décision de fonder sur une valeur déclarée est une décision RDR (PARTIEL-DÉCLARÉ).
- Ne dimensionne PAS la protection au feu.


SORTIE
Pièce 1 — Inventaire des données
Tableau : type de fondation profonde | source (réf. exacte) | données fournies | données manquantes.


Pièce 2 — Contrôle des hypothèses
Tableau : hypothèse | source (réf.) | contrôle effectué | cohérence (oui / non / à vérifier) | conséquence si incohérence.


Pièce 3 — Données manquantes
Tableau : code CARNAC | libellé | impact sur notre vérification | voie d'obtention.


Pièce 4 — Recommandation de mission
Tableau : mission recommandée (G3 / G4 / essais) | base normative | justification | conséquence si non commandée.


Pièce 5 — Points à faire valider par le spécialiste
Tableau : point | nature (capacité / tassement / groupe / technique) | spécialiste pressenti.


Pièce 6 — Synthèse
6 lignes maximum : nombre de pieux / micropieux concernés | nombre d'hypothèses contrôlées | nombre de données manquantes | nombre de points à valider par le spécialiste | recommandation de mission (oui / non) | niveau de risque (faible / moyen / élevé).


CRITÈRE D'ACCEPTATION
La note est acceptée si :
- chaque donnée de pieu est rattachée à une source citée ;
- chaque hypothèse est contrôlée (cohérence avec DDC, stratigraphie, géométrie) ;
- chaque donnée manquante est rattachée à son code CARNAC et à sa voie d'obtention ;
- chaque recommandation de mission cite sa base normative et la conséquence de sa non-commande ;
- chaque point à valider par le spécialiste est identifié ;
- aucun pieu n'a été conçu, calculé, ou dessiné ;
- la synthèse tient en 6 lignes.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}} (par PARAMÉTRIQUE, PARTIEL-DÉCLARÉ ou SANS OBJET). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Trois modes d'appel seulement | B-41 n'est pas une brique de conception : conclure sur la capacité portante en toute autonomie n'est ni notre métier ni notre mission. Le mode par défaut est PARAMÉTRIQUE — par construction |
| « Tu ne conçois AUCUN pieu » | La conception de pieux est une mission géotechnique spécifique (G3/G4) qui engage la responsabilité du spécialiste. Notre rôle est de vérifier les données et de signaler les manques — pas de nous substituer au spécialiste |
| « Tu contrôles, tu ne recalculles pas » | La nuance est capitale : contrôler la cohérence entre la capacité portante annoncée et les charges transmises est à notre portée ; recalculer la capacité portante ne l'est pas. Le contrôle de cohérence détecte les erreurs de transmission, pas les erreurs de conception |
| Recommandation de mission G3/G4 | C'est le livrable principal de B-41 : si les données sont insuffisantes, la recommandation de mission est la seule action utile. Sans elle, la note se limite à un constat stérile |
| « Conséquence si non commandée » | Comme pour B-12, c'est ce qui vous protège en cas de litige : si la MOA ne commande pas la mission, vous avez documenté ce qui restera suspendu |
| Points à faire valider par le spécialiste | Certains points ne sont pas de notre compétence : les nommer explicitement évite de les traiter par défaut (et de commettre une erreur grave) |
| Pas de plan de pieux | Un plan de pieux sans calcul de pieux est un plan qui engage notre responsabilité sur une conception que nous n'avons pas faite. B-41 ne produit pas de plan — le plan de pieux vient du spécialiste |
| Synthèse en 6 lignes | B-41 est une note courte : elle ne se substitue pas au rapport géotechnique, elle le complète par le contrôle de cohérence |

Les trois modes de B-41 — précision utile :

| Mode | Situation | Livrable |
| --- | --- | --- |
| PARAMÉTRIQUE (par défaut) | Données de pieux incomplètes (ce qui est le cas le plus fréquent) | Note de vérification suspendue, avec liste des essais nécessaires et recommandation de mission |
| PARTIEL-DÉCLARÉ | Une décision RDR a accepté une valeur déclarée pour une donnée manquante | Note avec valeur déclarée, mention de l'auteur et de la date, et réserves sur les conséquences |
| SANS OBJET | MPD a statué qu'il n'y a pas de fondations profondes dans le périmètre | Ligne de justification |

Les deux pièges de B-41 — précision utile :
Piège 1 — Recalculer la capacité portante : un modèle qui reçoit un rapport géotechnique a tendance à recalculer la capacité portante annoncée. C'est exactement ce qu'il faut interdire :
   * le recalcul peut aboutir à une valeur différente de celle du géotechnicien ;
   * si la valeur du recalcul est plus favorable, elle masque un risque ;
   * si elle est plus défavorable, elle crée un conflit avec le géotechnicien.
La seule action légitime est de contrôler la cohérence : la capacité portante annoncée est-elle compatible avec les charges transmises, la stratigraphie, la géométrie ?
Piège 2 — Proposer une valeur de repli : si les données de pieux sont insuffisantes, un modèle a tendance à proposer une valeur de repli (par exemple, « capacité portante estimée à 500 kN par pieu ») pour « faire avancer le projet ». C'est exactement ce qu'il faut interdire :
   * la valeur de repli n'est pas sourcée — elle ne peut pas être défendue ;
   * elle devient implicitement la valeur de calcul — et les pieux dimensionnés sur cette base sont faux ;
   * elle masque le besoin d'une mission G3/G4 — et la MOA ne commande pas la mission complémentaire.
Le mode PARAMÉTRIQUE est la seule réponse correcte : on produit les contrôles de cohérence, on identifie les essais nécessaires, et on laisse la décision à la MOA.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-12 (Audit des pièces géotechniques) | Les valeurs relatives aux pieux — B-41 les contrôle et recommande une mission G3/G4 si nécessaire |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-25 (Stabilité globale, contreventement, joints) | Idem, avec les combinaisons sismiques |
| B-40 (Fondations superficielles) | Les efforts aux semelles — B-41 vérifie la cohérence si les pieux reprennent une partie des charges |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Le livrable à vérifier et les positions prévues |
| B-33 (Vérification croisée) | Le livrable et les positions prévues — B-33 les compare aux autres livrables |
| B-50 (Assemblages et ancrages) | Les efforts aux têtes de pieux (si des ancrages sont prévus) |
| B-60 (Plans d'exécution) | Les plans de fondations — B-60 reprend les pieux existants (pas les pieux neufs, qui relèvent du spécialiste) |
| B-62 (Nomenclature et façonnage) | La note de calcul — B-62 vérifie la cohérence entre les quantités du plan et celles de la note |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | Le verdict de B-41 — B-70 vérifie que les fondations profondes sont traitées |
| B-72 (Journal de clôture) | Les recommandations de mission — B-72 liste les points ouverts |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les recommandations de mission — T-04 les transforme en demande formelle à la MOA |

Variables consommées

| Code | Libellé | Statut dans B-41 |
| --- | --- | --- |
| SOL-01 à SOL-07 | Géotechnique | BLOQUANTE (chaque valeur doit être citée avec sa source) |
| SOL-04 | Nature et succession des couches | BLOQUANTE (pour la cohérence avec la longueur de pieu) |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | BLOQUANTE (détermine la suffisance des données) |
| DOC-06 | Rapport géotechnique | BLOQUANTE |
| EXI-04 | Résultats de sondages (pieux existants) | BLOQUANTE (si pieux existants à vérifier) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | BLOQUANTE si sous-sol ou soutènement |

Variables produites
B-41 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de vérification) qui alimente B-50, B-60, B-70, B-72 et T-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | SOL-01 à SOL-08, DOC-06, EXI-04, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-41, vous devez décider si la mission complémentaire doit être commandée. C'est une décision MOA, mais c'est vous qui documentez la conséquence de la non-commande. Un contrôle de cohérence qui recommande une G3 sans documenter la conséquence ne vous protège pas en cas de litige.
Cas particulier — pieux existants à vérifier : si le projet comporte des pieux existants à vérifier (par exemple, une extension sur des pieux anciens), B-41 s'appuie sur les résultats de sondages (EXI-04) pour contrôler les hypothèses. Si les sondages sont absents, B-41 recommande une inspection vidéo ou un essai de chargement — c'est la seule façon de vérifier la capacité portante d'un pieu existant.
Cas particulier — pieux prescrits par un spécialiste : si un spécialiste (BET structure, géotechnicien) a prescrit des pieux avec une note de calcul, B-41 contrôle cette note :
   * cohérence capacité portante / charges transmises ;
   * cohérence longueur de pieu / stratigraphie ;
   * cohérence nombre de pieux / géométrie de fondation ;
   * vérification du groupe et du tassement.
B-41 ne recalcule pas la note du spécialiste — elle vérifie qu'elle est cohérente avec les autres données du projet. Si une incohérence est détectée, elle est signalée et le spécialiste est consulté.
Cas particulier — micropieux : si le projet comporte des micropieux (par exemple, pour des reprises en sous-œuvre), B-41 les traite comme des fondations profondes au sens large — avec les mêmes contrôles de cohérence. La technique de micropieu est du ressort du spécialiste, pas de B-41.
Cas particulier — absence de données de pieux : si aucune donnée de pieu n'est fournie mais que le projet comporte des fondations profondes (par exemple, parce que le rapport géotechnique recommande des pieux), B-41 s'appelle en mode PARAMÉTRIQUE et :
   * signale l'absence totale de données ;
   * recommande une mission G3/G4 ;
   * liste les essais nécessaires (essais de chargement, reconnaissance complémentaire) ;
   * ne propose aucune valeur de repli.
Cas particulier — recommandation G4 : si les données sont suffisantes pour la conception mais que le suivi d'exécution est nécessaire (par exemple, pour des pieux de grande longueur, ou dans un sol hétérogène), B-41 recommande une G4 (mission géotechnique de supervision) plutôt qu'une G3. La G4 couvre le suivi de l'exécution, pas seulement la conception.
Cas particulier — mode SANS OBJET : si la MPD a statué qu'il n'y a pas de fondations profondes dans le périmètre (par exemple, travaux de superstructure sans fondations profondes), B-41 s'appelle en mode SANS OBJET et produit une ligne de justification. Elle ne calcule rien, ne vérifie rien, ne recommande aucune mission.
Format de sortie attendu : six pièces distinctes (inventaire, contrôle, données manquantes, recommandation, points à faire valider par le spécialiste, synthèse). La note est courte (3 à 5 pages) — elle ne se substitue pas au rapport géotechnique, elle le complète.
Consignation : la note B-41 est annexée au RDR (B-03) — elle documente le contrôle de cohérence et alimente les réserves (R-xx) pour les recommandations de mission.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** pour ses contrôles chiffrés (vérification des hypothèses et des capacités portantes) : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. B-41 étant une brique de contrôle dont les seuls modes d'appel sont PARAMÉTRIQUE, PARTIEL-DÉCLARÉ et SANS OBJET, le régime outillé conditionne la déclaration d'exécution de ses contrôles : sans environnement d'exécution (OUT-01), ils ne peuvent pas être déclarés exécutés ; la brique est suspendue ou limitée à l'analyse documentaire déclarée. Toute mention d'un contrôle « simulé » est une non-conformité V13.


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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 06_PHASE_4_CALCULS/B-41_Fondations_Profondes.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-42_Verticaux_BA.md]**

Fichier 06_PHASE_4_CALCULS/B-42_Verticaux_BA.md — CARNAC v3.0
________________


B-42 — VERTICAUX BA (POTEAUX, JAMBAGES, VOILES)
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-01 à MAT-04 et SEC-01 disponibles) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante, notamment SEC-01) · PARAMÉTRIQUE (SEC-01 manquante : enrobage littéral + note d'attente de la donnée) · SANS OBJET (MPD a statué qu'il n'y a pas de verticaux BA neufs dans le périmètre) |
| Paramètre d'appel | {{élément}} = poteau / jambage / voile (trois valeurs, une par appel) |
| Entrées lues | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-07, NIV-02, NIV-03, GEO-02, GEO-04, GEO-05, B-20 (conception), B-21 (DDC préliminaire), B-22 (hypothèses), B-40 (géométrie des semelles en aval), B-50 (ancrages) |
| Sortie unique | Note de calcul des verticaux BA + plans d'exécution cotés + coupes + nomenclature + export DXF à calques VERT-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Brique | Rôle sur les ancrages |
| --- | --- |
| B-42 | Calcule le vertical et fournit à B-50 les efforts à ancrer (N_Ed, M_Ed, section des barres à ancrer). Vérifie que le vertical peut descendre ses barres jusqu'à la semelle (logement compatible avec B-40). Ne calcule pas les attentes elles-mêmes. |
| B-40 | Vérifie que la géométrie de la semelle permet de loger les attentes calculées par B-50 (enrobage, espacement, hauteur). |
| B-50 | Calcule les attentes (longueur de scellement l_bd, retour d'équerre, dépassement) et fait le contrôle croisé entre ce que B-42 a fourni comme efforts et ce que B-40 a prévu comme logement. |

Règle de circulation : si un ancrage ne rentre pas dans la semelle, c'est B-40 qui s'agrandit — pas B-42 qui réduit ses barres, pas B-50 qui réduit ses ancrages.
Ce que B-42 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des attentes (longueurs, retours, tiges) | B-50 |
| Calcul des semelles qui reçoivent les verticaux | B-40 |
| Calcul des planchers qui s'appuient sur les verticaux | B-43 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |
| Vérification des verticaux existants à conserver | B-46 |

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

| Clause | Pourquoi |
| --- | --- |
| Paramètre {{élément}} = poteau / jambage / voile | Les vérifications EC2 (compression, flambement, second ordre, N-M, biaxial) sont identiques pour les trois. Seules les dispositions constructives (Blocs A, B, C) changent. Un seul prompt évite la répétition de 80 % du contenu et facilite la maintenance du carnet |
| Trois blocs de dispositions constructives | Poteau = cadres. Jambage = liaisonnement à la maçonnerie. Voile = armatures réparties + ferraillage de peau. Chaque bloc est autonome dans le prompt, mais la structure de la note est commune |
| « Ne calcule aucune attente : c'est B-50 » | Option C — B-42 calcule les efforts à ancrer (étape 7), B-50 calcule les attentes (étape de B-50). C'est l'articulation qui évite les doublons |
| « Ne réduis pas les barres pour faire rentrer les attentes dans la semelle » | Point critique : si le logement d'attentes ne rentre pas dans la semelle, la tentation est de réduire les barres du poteau. C'est faux — c'est la semelle qui s'agrandit (B-40). Cette clause protège l'intégrité de la conception |
| « Ne déclare pas COMPLET si SEC-01 manque » | SEC-01 est la donnée manquante la plus coûteuse du projet Flora (40 mm d'enrobage retenus « au titre des exigences de tenue au feu » sans que ces exigences existent). Cette clause impose le mode PARAMÉTRIQUE ou une décision RDR explicite |
| Enrobage satisfaisant à la fois durabilité et SEC-01 | L'enrobage n'est pas déterminé par une seule contrainte : il doit satisfaire la classe d'exposition (durabilité, MAT-02) et la tenue au feu (SEC-01). Le plus défavorable gouverne |
| « Ne recopie pas la DDC préliminaire » | Une DDC préliminaire recopiée n'a pas été vérifiée pour l'exécution. C'est l'erreur qui ne se voit pas |
| Auto-contrôle par vertical | Un auto-contrôle global ne détecte pas un vertical mal ferraillé. L'auto-contrôle par élément est le seul qui prouve chaque élément |
| Mention « protection au feu adéquate à prévoir (hors lot GO) » | Formulation imposée par votre décision de périmètre. Elle figure sur les plans sans autre précision |
| « Ne déclare pas COMPLET si une donnée bloquante manque » | Verrou V12 — un vertical BA sans SEC-01 est un vertical dont l'enrobage n'est pas justifié. Le mode doit refléter cette réalité |

Les trois blocs de dispositions constructives — précision utile :

| Élément | Dispositions principales | Vérifications spécifiques |
| --- | --- | --- |
| Poteau | Cadres HA6 avec espacement réduit aux extrémités (zone critique) et aux recouvrements | Flambement dans les deux directions, interaction N-M, flexion biaxiale |
| Jambage | Cadres HA6 + liaisonnement à la maçonnerie existante (scellements résine) | Flambement hors plan (le jambage est moins raidi dans son épaisseur), vérification du linteau (B-49) |
| Voile | Armatures réparties verticales et horizontales, ferraillage de peau si h > 30 cm, pas de cadres | Flambement hors plan (élancement du voile), dispositions aux ouvertures |

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

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-25 (Stabilité globale, contreventement, joints) | Les efforts tranchants et moments de torsion par élément de contreventement |
| B-40 (Fondations superficielles) | La géométrie des semelles (dimensions, positions) — B-42 vérifie que les attentes peuvent être logées |
| B-50 (Assemblages et ancrages) | Aucune donnée en amont — B-42 fournit les efforts à ancrer, B-50 calcule les attentes |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-34 (Synthèse des réservations) | Les voiles et poteaux concernés, avec leur ferraillage |
| B-40 (Fondations superficielles) | Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement |
| B-43 (Planchers et dallages) | Les appuis des poteaux sur le plancher — B-43 transmet les efforts à B-50 |
| B-45 (Structure métallique) | Les appuis des poutres métalliques sur les poteaux BA |
| B-46 (Maçonnerie : vérification) | Les appuis des planchers sur les murs |
| B-47 (Escaliers) | Les voiles ou poteaux qui reçoivent les efforts horizontaux |
| B-48 (Prédalles et planchers préfabriqués) | Les voiles qui reçoivent les appuis de la prédalle |
| B-49 (Linteaux et seuils) | Les jambages BA qui reçoivent les appuis du linteau |
| B-50 (Assemblages et ancrages) | Les efforts à ancrer (N_Ed, M_Ed, section des barres) — B-50 calcule les attentes |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (barres, cadres) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-42 — B-70 vérifie que chaque vertical a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-42 |
| --- | --- | --- |
| MAT-01 | Classe de résistance du béton | BLOQUANTE |
| MAT-02 | Classe d'exposition | BLOQUANTE |
| MAT-03 | Enrobage nominal | BLOQUANTE |
| MAT-04 | Nuance d'acier BA | BLOQUANTE |
| SEC-01 | Degré coupe-feu exigé par élément | BLOQUANTE (interdit le mode COMPLET si absente) |
| CHG-01, CHG-02, CHG-03 | Usage, surcharges, poids propres | BLOQUANTE |
| CHG-07 | Sismique (si applicable) | NON BLOQUANTE (renvoi à EC8 si présent) |
| NIV-02, NIV-03 | Niveaux de plancher, hauteurs libres | BLOQUANTE |
| GEO-02, GEO-04, GEO-05 | Axes, positions des verticaux, baies | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE en neuf et restructuration |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | BLOQUANTE si sous-sol ou soutènement |
| STR-03 | Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur) | NON BLOQUANTE (à défaut : PA-xx) |

Variables produites
B-42 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-07, NIV-02, NIV-03, GEO-02, GEO-04, GEO-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques VERT-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 06_PHASE_4_CALCULS/B-42_Verticaux_BA.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-43_Planchers_Dallages.md]**

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
**[Fin de 06_PHASE_4_CALCULS/B-43_Planchers_Dallages.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-44_Charpente_Bois.md]**

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
**[Fin de 06_PHASE_4_CALCULS/B-44_Charpente_Bois.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-45_Structure_Metallique.md]**

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
**[Fin de 06_PHASE_4_CALCULS/B-45_Structure_Metallique.md]**

---


<!-- ================= COUPURE POSSIBLE ================= -->
> **Coupure de confort (facultative)** : si votre fenêtre de contexte est limitée, vous pouvez arrêter le collage ici et coller la suite (`B-46` à `B-50`) dans une seconde discussion. Aucune règle du carnet ne dépend de la continuité de ce pack.

**[Début du fichier : 06_PHASE_4_CALCULS/B-46_Maconnerie.md]**

Fichier 06_PHASE_4_CALCULS/B-46_Maconnerie.md — CARNAC v3.0
________________


B-46 — MAÇONNERIE : VÉRIFICATION ET CONCEPTION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-23 (Exploitation du diagnostic), B-24 (Existant non sondé) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | Bloc A : COMPLET / PARAMÉTRIQUE (existant non sondé) · Bloc B : COMPLET (MAT-09 à MAT-11 disponibles) / PARTIEL-DÉCLARÉ (valeur RDR) · SANS OBJET (MPD a statué : pas de maçonnerie dans le périmètre) |
| Paramètre d'appel | {{bloc}} = A (vérification existant) / B (conception maçonnerie) / A+B (les deux) |
| Entrées lues | Bloc A : EXI-01, EXI-03, EXI-05, MAT-07, MAT-12, CHG-07 · Bloc B : MAT-07, MAT-09, MAT-10, MAT-11, MAT-01, MAT-04, CHG-07, GEO-03, GEO-05, B-20, B-22, B-40/B-42/B-43/B-44/B-45 (appuis) |
| Sortie unique | Note de calcul maçonnerie (vérification et/ou conception) + plans + coupes + nomenclature + export DXF à calques MACON-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, B-23 et B-24, quand le projet comporte de la maçonnerie à vérifier (existant) ou à concevoir (neuve, renforcement). En mode SANS OBJET (pas de maçonnerie dans le périmètre), B-46 produit une ligne de justification.
Ce que vous fournissez à l'IA : les données de la FDC (maçonnerie existante ou neuve), la note d'hypothèses (B-22), la conception de B-20 (trame et renforcements prévus), les contraintes du diagnostic (B-23), les vérifications suspendues de l'existant non sondé (B-24), les appuis sur les autres ouvrages. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{bloc}}.
Ce que vous validez à la sortie :
   * les contraintes transmises aux maçonneries existantes (Bloc A) ;
   * les vérifications EC6 (compression, flambement, cisaillement, contraintes localisées) ;
   * les orientations de renforcement (Bloc B) — chaînages, raidisseurs, armatures ;
   * les dispositions parasismiques (EC8) si CHG-07 le justifie ;
   * les efforts aux scellements transmis à B-50 ;
   * l'auto-contrôle par zone.
Le périmètre exact de B-46 (votre choix au tronçon 7c — deux blocs) :
Bloc A — Vérification de l'existant :
   * Contraintes transmises par nos ouvrages aux maçonneries existantes ;
   * Compression centrée et excentrée (EC6 §6.1) ;
   * Cisaillement (EC6 §6.2) ;
   * Flambement (EC6 §5.5) ;
   * Contraintes localisées sous les appuis (EC6 §6.1.3) ;
   * Linteaux existants sous nos appuis (renvoi B-49 si linteau BA/métal, B-46 si linteau maçonnerie).
Bloc B — Conception de maçonnerie :
   * Choix des blocs (NF EN 771-3), mortier, type de maçonnerie ;
   * Chaînages horizontaux et verticaux, raidisseurs (EC6 §8) ;
   * Armatures de maçonnerie armée (EC6 §9) si applicable ;
   * Linteaux de maçonnerie (renvoi B-49 si linteau BA/métal) ;
   * Dispositions parasismiques (EC8) si CHG-07 le justifie ;
   * Renforcement de maçonnerie existante par chaînage rapporté ou raidisseur.
Ce que B-46 ne produit jamais (frontières avec les spécialistes) :

| Exclu | Renvoi |
| --- | --- |
| Injection de résine dans maçonneries fissurées | Spécialiste (hors périmètre CARNAC) |
| Tirants actifs, précontrainte | Spécialiste (hors périmètre CARNAC) |
| Reprise en sous-œuvre par passes alternées | B-40 (fondations) + phasage (B-23) |
| Diagnostic parasitaire | Spécialiste (hors périmètre CARNAC) |
| Calcul des scellements (longueurs, diamètres, résine) | B-50 (option C) |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

L'articulation avec B-50 (option C) :

| Brique | Rôle sur les scellements |
| --- | --- |
| B-46 | Calcule la maçonnerie et fournit à B-50 les efforts aux scellements (N_Ed, V_Ed, M_Ed des chaînages et raidisseurs). Ne calcule pas les scellements. |
| B-50 | Calcule les scellements (résine, longueur, diamètre) et fait le contrôle croisé avec les efforts fournis par B-46 et la contrainte admissible de la maçonnerie. |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de calcul d'exécution de la maçonnerie de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}, pour le bloc {{bloc}} :
- Bloc A = vérification des maçonneries et éléments existants sous les contraintes transmises par nos ouvrages ;
- Bloc B = conception des maçonneries neuves et des renforcements de maçonnerie existante ;
- A+B = les deux.
Produire les livrables graphiques associés.


RÈGLES NORMATIVES
- EC0 (NF EN 1990) : combinaisons.
- EC1 (NF EN 1991-1-1) : charges.
- EC6 (NF EN 1996-1-1/NA) : maçonnerie — §5.5 (flambement), §6.1 (compression), §6.2 (cisaillement), §8 (dispositions constructives), §9 (maçonnerie armée).
- EC8 (NF EN 1998-1/NA) si CHG-07 l'exige.
- EC2 (NF EN 1992-1-1/NA) pour les chaînages BA.
- NF EN 771-3 (blocs béton), NF EN 998-2 (mortiers), NF DTU 20.1 (maçonnerie de petits éléments).
- Pour chaque formule, tu cites la référence exacte.


BLOC A — VÉRIFICATION DE L'EXISTANT


Étape A1 — Données d'entrée
- nature et résistance de la maçonnerie existante (MAT-07) ;
- sections et épaisseurs (EXI-01, GEO-03) ;
- présence et nature des chaînages existants (MAT-12) ;
- contraintes transmises par nos ouvrages (EXI-05, issues de B-40, B-42, B-43, B-44, B-45).
Si EXI-01 ou EXI-03 manque, le mode est PARAMÉTRIQUE (vérification littérale, cf. B-24).


Étape A2 — Vérifications EC6
- compression centrée : N_Ed/(Φ·t·L) ≤ f_d (EC6 §6.1.2.1) ;
- compression excentrée : N_Ed/(Φ·t·L) ≤ Φ_m·f_d (EC6 §6.1.2.2) ;
- flambement des murs : élancement, Φ (EC6 §5.5) ;
- cisaillement : V_Ed ≤ f_vd·t·L (EC6 §6.2) ;
- appuis de nos ouvrages : contrainte localisée à l'appui ≤ f_d local ;
- linteaux existants sous nos appuis : vérification de la flexion et de la longueur d'appui (renvoi B-49).


Étape A3 — Conclusions et renvois
- maçonnerie admissible : verdict par zone ;
- maçonnerie non admissible : signalement, renvoi au Bloc B (renforcement) ou au spécialiste (injection, reprise).


BLOC B — CONCEPTION DE MAÇONNERIE


Étape B1 — Données d'entrée
- classe de bloc (MAT-09), classe de mortier (MAT-10), type de maçonnerie (MAT-11) ;
- charges (CHG-01 à CHG-03, CHG-08) ;
- géométrie des murs (GEO-03, GEO-05) ;
- sismique (CHG-07) ;
- appuis sur nos ouvrages (B-40, B-42, B-43, B-44, B-45).


Étape B2 — Dimensionnement de la maçonnerie neuve
- résistance caractéristique f_k de la maçonnerie (EC6 §3.6, selon blocs et mortier) ;
- compression centrée et excentrée (EC6 §6.1) ;
- cisaillement (EC6 §6.2) ;
- flambement (EC6 §5.5) ;
- linteaux de maçonnerie : vérification ou renvoi B-49 ;
- dispositions parasismiques (EC8) si CHG-07 le justifie : chaînages, raidisseurs, ratios d'armatures.


Étape B3 — Chaînages, raidisseurs, armatures
- chaînages horizontaux (EC6 §8.5) : section minimale, continuité aux angles et aux intersections, ancrage ;
- chaînages verticaux (raidisseurs) : section minimale, espacement, liaison aux planchers et aux fondations ;
- armatures de maçonnerie armée (EC6 §9) si MAT-11 = armée : ratios, enrobage, recouvrements ;
- béton et acier des chaînages : MAT-01, MAT-04.


Étape B4 — Renforcement de maçonnerie existante
- chaînage rapporté : ancrage dans la maçonnerie existante, scellement (efforts fournis à B-50) ;
- raidisseur rapporté : section, fixation, effort repris ;
- si le renforcement dépasse le cadre du chaînage/raidisseur : renvoi explicite au spécialiste (injection, tirants, reprise).


Étape B5 — Dispositions constructives
- joints, épaisseurs, appareillage ;
- ventilation, protection contre l'humidité ;
- chaînages continus, liaison aux planchers et aux fondations ;
- appuis des ouvrages porteurs (linteaux, poutres) : longueur d'appui, contrainte localisée.


Étape B6 — Efforts aux assemblages (transmis à B-50)
Pour chaque ancrage de chaînage, chaque scellement de raidisseur, chaque appui : N_Ed, V_Ed, M_Ed si excentrement.


Étape — Livrables graphiques (Bloc A et B)
- MACON-AXES : axes, trames, points de calage ;
- MACON-COFFRAGE : murs, chaînages, raidisseurs, cotations ;
- MACON-ARMATURES : chaînages, maçonnerie armée ;
- MACON-EXISTANT : éléments existants à conserver ;
- MACON-HABILLAGE-TEXTE : légendes, cartouche, notes, tableaux ;
- plans, coupes, élévations, nomenclature ;
- filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », indice, mode, mention générique de protection au feu.


Étape — Auto-contrôle déclaré
Zone par zone : contraintes / vérifications EC6 / dispositions / efforts aux assemblages / verdict. Points DE PRINCIPE et À LEVER.


INTERDICTIONS
- Ne conçois PAS les techniques de spécialiste (injection, tirants actifs, précontrainte, reprise en sous-œuvre) : tu les signales comme relevant d'un spécialiste.
- Ne calcule AUCUN ancrage ou scellement (longueur, diamètre, résine) : c'est B-50.
- N'invente aucune valeur hors FDC.
- Ne déclare pas COMPLET si une donnée bloquante manque (V12).
- Ne produis aucun livrable exécutable en PARAMÉTRIQUE.
- Ne dimensionne PAS la protection au feu : mention générique seule.
- Ne confonds pas vérification (Bloc A) et conception (Bloc B) : ce sont deux blocs distincts dans la note.
- Ne réduis pas les contraintes transmises pour « faire passer » l'existant : c'est l'existant qui doit être renforcé, ou B-40/B-42/B-43/B-44/B-45 qui doivent être revus.


SORTIE
Pièce 1 — Note de calcul (Bloc A et/ou Bloc B selon {{bloc}}), sections A1 à A3 et/ou B1 à B6.
Pièce 2 — Plans d'exécution + DXF MACON-*.
Pièce 3 — Auto-contrôle déclaré.


CRITÈRE D'ACCEPTATION
- chaque donnée d'entrée est issue de la FDC ;
- Bloc A : chaque zone de maçonnerie existante a ses vérifications EC6 (compression, flambement, cisaillement) ;
- Bloc A : chaque appui de nos ouvrages sur l'existant a sa contrainte localisée vérifiée ;
- Bloc B : chaque maçonnerie neuve a ses vérifications EC6 et ses dispositions EC8 si applicable ;
- Bloc B : chaînages horizontaux et verticaux, raidisseurs, armatures sont dimensionnés ;
- Bloc B : le renforcement de l'existant par chaînage/raidisseur est dimensionné ;
- chaque ancrage et scellement a ses efforts transmis à B-50 ;
- les techniques de spécialiste sont signalées (jamais conçues) ;
- les plans portent le filigrane, l'indice, le mode, la mention générique de protection au feu ;
- l'auto-contrôle déclare chaque zone ;
- aucune protection au feu dimensionnée ;
- aucune valeur hors FDC.
Si un seul de ces points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{mode}} et {{bloc}} (par A, B ou A+B). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Deux blocs distincts A / B | Vérifier un existant et concevoir du neuf sont deux opérations différentes, avec des entrées différentes (EXI-xx vs MAT-09 à MAT-11). Les séparer évite qu'un modèle « conçoive » sans vérifier l'existant, ou « vérifie » sans dimensionner le neuf |
| f_k selon EC6 §3.6 | La résistance caractéristique de la maçonnerie dépend du couple bloc/mortier. Un calcul qui prend une valeur « courante » ignore cette dépendance — et sous-estime ou surestime la résistance |
| Flambement des murs EC6 §5.5 | Le flambement d'un mur n'est pas le flambement d'un poteau. La méthode EC6 (Φ, élancement) diffère — la confondre avec EC2 conduit à des murs sous-dimensionnés |
| Chaînages horizontaux et verticaux | Ce sont les dispositions qui reprennent les efforts de traction, les tassements différentiels et le sismique. Un mur sans chaînage est un mur fragile — même s'il passe en compression |
| Dispositions EC8 si CHG-07 le justifie | En zone 1 (faible), l'EC8 impose des dispositions minimales pour la maçonnerie : chaînages, raidisseurs, ratios. Les ignorer est une erreur réglementaire |
| Frontières spécialiste explicites | Injection de résine, tirants actifs, précontrainte : ces techniques relèvent d'un spécialiste (et d'une mission G5). Les nommer comme « à traiter par spécialiste » évite qu'un modèle les conçoive sans compétence |
| « Ne réduis pas les contraintes pour faire passer l'existant » | La tentation est de réduire la charge transmise pour éviter de renforcer l'existant. C'est faux — c'est l'existant qui se renforce, ou les ouvrages amont qui se revoient |
| Renvois aux briques amont | Un appui de B-42 sur une maçonnerie existante non vérifiée est un appui non vérifié. Le renvoi aux briques amont est la seule protection contre les vérifications en silo |
| « Ne calcule aucun scellement » | Option C — B-46 calcule la maçonnerie et fournit les efforts, B-50 calcule les scellements. B-46 ne peut pas calculer des scellements dont il ne connaît pas les caractéristiques (résine, longueur) |
| Filigrane + mention mode | Un plan de maçonnerie exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les deux blocs — précision utile :

| Bloc | Objet |
| --- | --- |
| Entrées principales | Sortie |
| Bloc A | Vérifier la maçonnerie existante sous les contraintes transmises |
| EXI-01, EXI-03, MAT-07, MAT-12, EXI-05, CHG-07 | Verdict par zone : admissible / à renforcer / à traiter par spécialiste |
| Bloc B | Concevoir la maçonnerie neuve et les renforcements |
| MAT-07, MAT-09 à MAT-11, MAT-01, MAT-04, CHG-07, appuis | Dimensionnement, ferraillage, dispositions constructives |

Le piège de la maçonnerie existante non sondée : si les caractéristiques de la maçonnerie existante ne sont pas connues (par exemple, un mur ancien en moellons dont la résistance n'a pas été testée), B-46 s'appelle en mode PARAMÉTRIQUE (via B-24) :
   * les vérifications EC6 sont menées en littéral (avec la résistance en symbole) ;
   * un tableau de sensibilité est produit sur les résistances plausibles — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE [résistance] » et suffixé _P ;
   * aucun plan exécutable n'est produit.
Le piège du chaînage : un modèle qui reçoit un mur de maçonnerie a tendance à vérifier la compression, mais à oublier les chaînages. C'est faux :
   * un mur sans chaînage est un mur qui peut fissurer sous tassement différentiel, sous sismique, ou sous dilatation thermique ;
   * les chaînages horizontaux (en tête de mur, en pied de mur, aux intersections) et verticaux (raidisseurs) sont obligatoires (EC6 §8.5) ;
   * l'EC8 impose des dispositions supplémentaires en zone sismique — même en zone 1.
Le piège du spécialiste : un modèle qui reçoit une maçonnerie fissurée a tendance à proposer une injection de résine — c'est une technique de spécialiste (mission G5). B-46 doit :
   * signaler la fissuration (Bloc A) ;
   * renvoyer au spécialiste pour l'injection ;
   * ne pas concevoir l'injection elle-même.
La même règle s'applique aux tirants actifs, à la précontrainte, et à la reprise en sous-œuvre par passes alternées (qui relève de B-40 + phasage).
Le piège de la réduction des contraintes : si la maçonnerie existante n'est pas admissible sous les contraintes transmises, un modèle a tendance à « réduire » les contraintes pour éviter de renforcer. C'est faux :
   * les contraintes transmises sont calculées par les briques amont (B-42, B-43, B-44, B-45) — elles ne se réduisent pas arbitrairement ;
   * c'est l'existant qui doit être renforcé (Bloc B) ;
   * ou les ouvrages amont qui doivent être revus (par exemple, ajouter un poteau pour réduire la portée).
B-46 signale le problème et renvoie la correction — elle ne réduit pas les contraintes.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-11 (Audit du diagnostic structure) | Les désordres de maçonnerie existante (si applicable) — B-46 les cite |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-23 (Exploitation du diagnostic existant) | Les appuis sur l'existant — B-46 vérifie la contrainte transmise aux maçonneries existantes |
| B-24 (Vérification d'éléments existants non) | Les vérifications suspendues des maçonneries existantes — B-46 les ferme si le sondage est disponible |
| B-25 (Stabilité globale, contreventement, joints) | Le rôle interdit ou limité des remplissages dans le contreventement |
| B-40 (Fondations superficielles) | Les appuis des murs sur les semelles |
| B-42 (Verticaux BA) | Les appuis des planchers sur les murs |
| B-43 (Planchers et dallages) | Les appuis des planchers sur les murs |
| B-44 (Charpente bois) | Les appuis de la charpente sur les murs |
| B-45 (Structure métallique) | Les appuis des profilés sur les murs |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-43 (Planchers et dallages) | Les appuis du plancher sur l'existant — B-43 vérifie la contrainte transmise |
| B-49 (Linteaux et seuils) | Les murs qui reçoivent les appuis du linteau (vérification du mur au-dessus) |
| B-50 (Assemblages et ancrages) | Les efforts aux scellements (chaînages, raidisseurs) — B-50 calcule les scellements |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (blocs, barres, raidisseurs) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-46 — B-70 vérifie que chaque zone a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-46 |
| --- | --- | --- |
| MAT-01 | Classe de résistance du béton (pour chaînages) | BLOQUANTE (Bloc B) |
| MAT-04 | Nuance d'acier BA (pour chaînages) | BLOQUANTE (Bloc B) |
| MAT-07 | Nature et résistance de la maçonnerie existante | BLOQUANTE (Bloc A) |
| MAT-09 | Classe de bloc de maçonnerie neuve | BLOQUANTE (Bloc B) |
| MAT-10 | Classe de mortier | BLOQUANTE (Bloc B) |
| MAT-11 | Type de maçonnerie (chaînée / armée / non armée) | BLOQUANTE (Bloc B) |
| MAT-12 | Présence et nature des chaînages existants | BLOQUANTE (Bloc A) |
| CHG-07 | Sismique (zone, catégorie d'importance) | BLOQUANTE (pour les dispositions EC8) |
| EXI-01, EXI-03 | Sections et résistance de l'existant | BLOQUANTE (Bloc A) — sinon mode PARAMÉTRIQUE |
| EXI-05 | Contrainte admissible transmise à l'existant | BLOQUANTE (Bloc A) |
| GEO-03, GEO-05 | Épaisseurs de murs, baies et ouvertures | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE en neuf et restructuration |

Variables produites
B-46 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01, MAT-04, MAT-07, MAT-09 à MAT-12, CHG-07, EXI-01, EXI-03, EXI-05, GEO-03, GEO-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques MACON-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE), en particulier C-01 (ajout MAT-09 à MAT-12) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-46, vous devez valider la frontière avec le spécialiste. Une injection de résine relève-t-elle du spécialiste ou de votre lot ? C'est votre décision — et elle dépend du contexte contractuel (le CCTP peut attribuer l'injection au lot GO, ou la réserver à un spécialiste). Le modèle propose, vous décidez.
Cas particulier — mode PARAMÉTRIQUE (Bloc A, maçonnerie existante non sondée) : si les caractéristiques de la maçonnerie existante ne sont pas connues (par exemple, un mur ancien en moellons dont la résistance n'a pas été testée), B-46 s'appelle en mode PARAMÉTRIQUE pour le Bloc A :
   * les vérifications EC6 sont menées en littéral (avec la résistance en symbole) ;
   * un tableau de sensibilité est produit sur les résistances plausibles — clairement identifié comme non contractuel ;
   * le livrable est filigrané « PROVISOIRE — EN ATTENTE DE [résistance] » et suffixé _P ;
   * aucun plan exécutable n'est produit pour le Bloc A.
Le Bloc B (si applicable) peut être en mode COMPLET si MAT-09 à MAT-11 sont disponibles — les deux blocs ont des modes indépendants.
Cas particulier — maçonnerie ancienne en moellons : si la maçonnerie existante est ancienne (moellons, briques anciennes), les valeurs de résistance EC6 sont généralement faibles (f_k de l'ordre de 1 à 2 MPa). B-46 s'appuie sur les valeurs de MAT-07 si elles existent (essais, sondages), ou sur des valeurs de la littérature (NF DTU 20.1, annexe nationale EC6) — déclarées comme hypothèses H-xx.
Cas particulier — maçonnerie existante non admissible : si la maçonnerie existante n'est pas admissible sous les contraintes transmises (Bloc A), B-46 :
   * signale le dépassement ;
   * propose un renforcement (Bloc B) — chaînage rapporté, raidisseur, ou renvoi au spécialiste ;
   * ne réduit pas les contraintes transmises (ce serait aux briques amont de revoir leur conception).
Cas particulier — sismique en zone 1 : en zone 1 (sismicité très faible), l'EC8 impose des dispositions minimales pour la maçonnerie :
   * chaînages horizontaux et verticaux ;
   * ratios d'armatures minimaux en maçonnerie armée ;
   * dispositions aux ouvertures.
Même en zone 1, les dispositions EC8 sont obligatoires pour les bâtiments neufs. Les ignorer est une erreur réglementaire — B-46 les prévoit systématiquement si CHG-07 est fournie.
Cas particulier — maçonnerie armée : si MAT-11 = armée, la maçonnerie comporte des armatures (verticales et horizontales) qui reprennent les efforts de traction et améliorent la ductilité. B-46 dimensionne :
   * les ratios minimaux (EC6 §9.2) ;
   * les armatures verticales (poteaux BA noyés dans la maçonnerie) ;
   * les armatures horizontales (lits armés tous les N rangs) ;
   * l'enrobage et les recouvrements.
Une maçonnerie armée mal ferraillée est plus dangereuse qu'une maçonnerie non armée — la ductilité attendue n'est pas au rendez-vous.
Cas particulier — chaînage rapporté sur existant : si un chaînage est rapporté sur une maçonnerie existante (renforcement), B-46 prévoit :
   * la section du chaînage (béton + acier) ;
   * les scellements dans la maçonnerie existante (efforts fournis à B-50) ;
   * la continuité aux angles et aux intersections ;
   * la liaison avec les planchers et les fondations.
Le scellement lui-même est calculé par B-50 — B-46 fournit les efforts, B-50 calcule la longueur et le diamètre.
Cas particulier — ouverture dans un mur porteur existant : si une ouverture est créée dans un mur porteur existant, B-46 prévoit :
   * un linteau (renvoi B-49 pour le calcul du linteau) ;
   * des jambages (renvoi B-42 pour les jambages BA) ;
   * des renforts de maçonnerie autour de l'ouverture (chaînages, raidisseurs) ;
   * la vérification de la stabilité du mur au-dessus de l'ouverture.
Une ouverture dans un mur porteur sans renforts est un désordre structurel — c'est une erreur grave.
Format de sortie attendu : trois pièces distinctes (note de calcul, plans d'exécution, auto-contrôle déclaré). La note comporte deux blocs distincts (A et B) si {{bloc}} = A+B — les deux blocs sont séparés, avec leurs propres sections. Les plans portent tous le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA », le cartouche complet, la mention du mode, et la mention « protection au feu adéquate à prévoir (hors lot GO) ».
Consignation : la note B-46 est annexée au RDR (B-03) — elle documente la vérification et la conception de la maçonnerie, et alimente les décisions (D-xx) et les réserves (R-xx) pour les données manquantes.
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
**[Fin de 06_PHASE_4_CALCULS/B-46_Maconnerie.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-47_Escaliers.md]**

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
**[Fin de 06_PHASE_4_CALCULS/B-47_Escaliers.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-48_Predalles.md]**

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
**[Fin de 06_PHASE_4_CALCULS/B-48_Predalles.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md]**

Fichier 06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md — CARNAC v3.0
________________


B-49 — LINTEAUX ET SEUILS
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-21 (DDC préliminaire), B-22 (Note d'hypothèses), B-46 (Maçonnerie — si le linteau repose sur maçonnerie) |
| Brique suivante | B-50 (Assemblages et ancrages — contrôle croisé), B-60 (Plans d'exécution) |
| Modes d'appel | COMPLET (MAT-01 à MAT-04, SEC-01, GEO-05 disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante) · PARAMÉTRIQUE (SEC-01 manquante ou linteau existant non sondé) · SANS OBJET (pas de linteaux ni seuils dans le périmètre) |
| Paramètre d'appel | {{type}} = linteau BA / linteau métallique / linteau maçonnerie / seuil BA (quatre valeurs, une par appel) |
| Entrées lues | MAT-01 à MAT-04, MAT-07, SEC-01, CHG-01 à CHG-03, GEO-03, GEO-05, EXI-01, EXI-03, B-20, B-22, B-40/B-42/B-46 (appuis), B-50 (assemblages) |
| Sortie unique | Note de calcul linteaux et seuils + plans + coupes + nomenclature + export DXF à calques LINTEAU-* |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

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

| Ce que B-49 produit | Ce que B-49 ne produit pas |
| --- | --- |
| DDC sur le linteau (mur au-dessus, plancher, toiture) | Calcul des ancrages (longueurs de scellement) — B-50 |
| Vérification EC2 / EC3 / EC6 selon le type | Vérification du mur au-dessus du linteau — B-46 |
| Charge triangulaire pour linteaux courts | Vérification de l'existant non sondé — B-24 |
| Longueur d'appui et contrainte localisée | Dimensionnement de la protection au feu — hors CARNAC |
| Dispositions constructives (enrobage, ferraillage) | — |
| Plans d'exécution (LINTEAU-*) | — |

Le périmètre de chaque type :

| Type | Méthode | Vérifications spécifiques |
| --- | --- | --- |
| Linteau BA | EC2 §6.1 (flexion), §6.2.2 (effort tranchant), §9.3 (dispositions) | V_Rd,max pour éléments courts, longueur d'appui |
| Linteau métallique | EC3 §6.2.5 (flexion), §6.2.6 (cisaillement), §6.3 (flambement/déversement) | Pression diamétrale sur le béton ou la maçonnerie, protection anticorrosion |
| Linteau maçonnerie | EC6 §6.1 (compression), §6.2 (cisaillement), §8 (dispositions) | Longueur d'appui, chaînage |
| Seuil BA | EC2 §6.1 (flexion), §6.2 (effort tranchant), §9.3 (dispositions) | Liaison au dallage, joint de désolidarisation |

Ce que B-49 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Calcul des ancrages (longueurs de scellement) | B-50 |
| Vérification du mur au-dessus du linteau | B-46 |
| Vérification de l'existant non sondé | B-24 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

L'articulation avec B-50 (option C) :

| Brique | Rôle sur les ancrages |
| --- | --- |
| B-49 | Calcule le linteau et fournit à B-50 les efforts aux appuis et aux ancrages (N_Ed, V_Ed, M_Ed). Ne calcule pas les longueurs de scellement. |
| B-50 | Calcule les ancrages (longueurs de scellement, boulons, platines) et fait le contrôle croisé avec les efforts fournis par B-49 et les logements prévus par les briques amont. |

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

| Clause | Pourquoi |
| --- | --- |
| Brique dédiée (votre choix au tronçon 1) | Un linteau est un élément court, avec effort tranchant dominant et charge triangulaire. Une poutre longue traitée comme un linteau court (ou l'inverse) est fausse. La brique dédiée force la méthode spécifique |
| Quatre types (BA / métallique / maçonnerie / seuil) | Chaque type a sa méthode de vérification (EC2, EC3, EC6). Le paramètre force à choisir la bonne — sans lui, un modèle traite tous les linteaux comme du BA, ce qui est faux pour les linteaux métalliques et maçonnerie |
| Charge triangulaire pour les linteaux courts | La charge du mur au-dessus d'un linteau court est triangulaire, pas linéique. C'est une erreur classique de traiter la charge comme linéique — elle sous-estime le moment de 20 à 30 % |
| V_Rd,max pour les éléments courts | Un linteau court casse par effort tranchant, pas par flexion. Vérifier seulement V_Rd,c (qui correspond à la ruine par traction diagonale) sans vérifier V_Rd,max (ruine par écrasement de la bielle) est une erreur grave — c'est la ruine fragile, qui se produit sans signe préalable |
| Longueur d'appui | Un linteau avec une longueur d'appui insuffisante peut glisser ou écraser l'appui. La longueur d'appui est aussi importante que le ferraillage — c'est la vérification qui garantit que le linteau « tient » sur ses appuis |
| « Ne réduis pas la charge du mur pour faire passer » | La tentation de réduire la charge pour éviter un linteau plus grand est une faute grave. C'est le linteau qui s'adapte, pas la charge — réduire la charge d'un mur porteur conduit à un linteau sous-dimensionné, et à un effondrement |
| « Ne vérifie pas le mur au-dessus » | La vérification du mur au-dessus du linteau relève de B-46 (maçonnerie). B-49 calcule le linteau, B-46 calcule le mur — les deux sont complémentaires, pas redondants |
| « Ne calcule aucun ancrage » | Option C — B-49 fournit les efforts, B-50 calcule les longueurs de scellement. B-49 ne peut pas calculer des ancrages dont il ne connaît pas les caractéristiques (type de scellement, résine) |
| Filigrane + mention mode | Un plan de linteau exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les quatre types de linteaux — vérifications spécifiques :

| Type | Vérifications principales | Vérifications spécifiques |
| --- | --- | --- |
| Linteau BA | Flexion, effort tranchant, A_min | V_Rd,max pour linteaux courts, longueur d'appui, ferraillage d'effort tranchant |
| Linteau métallique | Flexion, cisaillement, déversement | Pression diamétrale sur béton ou maçonnerie, protection anticorrosion |
| Linteau maçonnerie | Compression, cisaillement, flambement | Longueur d'appui, chaînage, renvoi au spécialiste si insuffisant |
| Seuil BA | Flexion, effort tranchant, A_min | Liaison au dallage, joint de désolidarisation |

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
| B-24 (Vérification d'éléments existants non) | Les vérifications suspendues des linteaux existants — B-49 les ferme si le sondage est disponible |
| B-42 (Verticaux BA) | Les jambages BA qui reçoivent les appuis du linteau |
| B-46 (Maçonnerie : vérification) | Les murs qui reçoivent les appuis du linteau (vérification du mur au-dessus) |
| B-50 (Assemblages et ancrages) | Aucune donnée en amont — B-49 fournit les efforts, B-50 calcule les ancrages |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-50 (Assemblages et ancrages) | Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les ancrages |
| B-60 (Plans d'exécution) | La note et les plans produits — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (barres, profilés) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | L'auto-contrôle B-49 — B-70 vérifie que chaque linteau a son verdict |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-49 |
| --- | --- | --- |
| MAT-01 à MAT-04 | Matériaux BA | BLOQUANTE (pour linteau BA et seuil BA) |
| MAT-05 | Nuance d'acier métallique | BLOQUANTE (pour linteau métallique) |
| MAT-07 | Nature et résistance de la maçonnerie | BLOQUANTE (pour linteau maçonnerie) |
| SEC-01 | Degré coupe-feu | BLOQUANTE (interdit le mode COMPLET si absente) |
| CHG-01 à CHG-03 | Usage, surcharges, poids propres | BLOQUANTE |
| GEO-03, GEO-05 | Épaisseurs de murs, baies et ouvertures | BLOQUANTE |
| EXI-01, EXI-03 | Sections et résistance de l'existant | BLOQUANTE (si linteau existant) — sinon mode PARAMÉTRIQUE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |

Variables produites
B-49 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans + auto-contrôle) qui alimente B-50, B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-05, MAT-07, SEC-01, CHG-01 à CHG-03, GEO-03, GEO-05, EXI-01, EXI-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques LINTEAU-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 06_PHASE_4_CALCULS/B-49_Linteaux_Seuils.md]**

---

**[Début du fichier : 06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md]**

Fichier 06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md — CARNAC v3.0
________________


B-50 — ASSEMBLAGES ET ANCRAGES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | Toutes les briques de calcul (B-40 à B-49) — B-50 est la brique aval qui consomme les efforts de toutes les briques amont |
| Brique suivante | B-60 (Plans d'exécution), B-70 (Auto-contrôle de synthèse) |
| Modes d'appel | COMPLET (DOC-09 fiches techniques connecteurs disponibles) · PARTIEL-DÉCLARÉ (valeur RDR pour une donnée manquante) · PARAMÉTRIQUE (fiche technique manquante) · SANS OBJET (MPD a statué : pas d'assemblages ni d'ancrages dans le périmètre) |
| Paramètre d'appel | {{famille}} = ancrages BA / assemblages métalliques / assemblages bois / scellements maçonnerie / tous (cinq valeurs) |
| Entrées lues | MAT-01 à MAT-12, DOC-09 (fiches techniques connecteurs, résines, boulons), les efforts transmis par toutes les briques amont (B-40, B-42, B-43, B-44, B-45, B-46, B-47, B-48, B-49), et les logements vérifiés par les briques aval |
| Sortie unique | Note de calcul des assemblages et ancrages + plans de détail + nomenclature + export DXF à calques ASSEMBLAGE-* + rapport de contrôle croisé entre amont et aval |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après toutes les briques de calcul (B-40 à B-49), quand le projet comporte des assemblages et ancrages à calculer. En mode SANS OBJET (pas d'assemblages ni d'ancrages dans le périmètre), B-50 produit une ligne de justification.
Ce que vous fournissez à l'IA : les efforts transmis par les briques amont (N_Ed, V_Ed, M_Ed aux nœuds), les logements vérifiés par les briques aval, les fiches techniques des connecteurs (DOC-09 : boulons, soudures, résines, sabots), les données de la FDC (matériaux). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{mode}} et {{famille}}.
Ce que vous validez à la sortie :
   * les calculs d'assemblages (boulons, soudures, platines, tiges, sabots, équerres, scellements) ;
   * le contrôle croisé entre les ancrages calculés et les logements vérifiés par les briques amont ;
   * les écarts identifiés et les briques responsables ;
   * le rapport de contrôle croisé ;
   * l'auto-contrôle assemblage par assemblage.
B-50 est la brique pivot de l'option C (votre choix au tronçon 6) :

| Brique | Rôle sur les ancrages |
| --- | --- |
| B-42 (poteaux) | Calcule le poteau et fournit à B-50 les efforts à ancrer (N_Ed, M_Ed, section des barres). Vérifie que le poteau peut descendre ses barres jusqu'à la semelle |
| B-45 (métal) | Calcule le profilé et fournit à B-50 les efforts aux nœuds (N_Ed, V_Ed, M_Ed, nature de l'assemblage). Vérifie la pression diamétrale sur le béton |
| B-44 (bois) | Calcule l'élément bois et fournit à B-50 les efforts aux assemblages. Vérifie la compression perpendiculaire aux appuis |
| B-46 (maçonnerie) | Calcule la maçonnerie et fournit à B-50 les efforts aux scellements. Vérifie la contrainte dans la maçonnerie |
| B-40 (fondations) | Vérifie que la géométrie de la semelle permet de loger les ancrages calculés par B-50 (enrobage, espacement, hauteur) |
| B-50 | Calcule les ancrages et assemblages et fait le contrôle croisé entre ce que l'amont a fourni comme efforts et ce que l'aval a prévu comme logement. Ne corrige jamais à la place des briques — il signale, identifie la brique responsable, et renvoie. |

Règle de circulation : si un ancrage ne rentre pas dans la semelle, c'est B-40 qui s'agrandit — pas B-50 qui réduit ses ancrages, pas B-42 qui réduit ses barres.
Ce que B-50 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Vérification des éléments porteurs eux-mêmes (poteaux, poutres, semelles) | B-40 à B-49 (chaque brique vérifie son élément) |
| Dimensionnement des semelles, poteaux, planchers | B-40, B-42, B-43 |
| Protection au feu des assemblages | Hors périmètre CARNAC (mention générique seule) |
| Choix des connecteurs pour les techniques de spécialiste (injection, précontrainte) | Spécialiste (hors périmètre CARNAC) |

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

| Clause | Pourquoi |
| --- | --- |
| Brique dédiée (option C, votre choix) | Les ancrages concernent plusieurs briques à la fois : l'amont qui connaît les efforts, l'aval qui connaît les logements. Une brique dédiée centralise le calcul et le contrôle croisé, sans dupliquer les calculs dans chaque brique |
| Quatre familles (BA, métallique, bois, maçonnerie) | Chaque famille a sa méthode de calcul (EC2, EC3-1-8, EC5, EC6/NF EN 1992-4). Le paramètre force à choisir la bonne — sans lui, un modèle traite tous les ancrages comme du BA, ce qui est faux pour les autres familles |
| Contrôle croisé obligatoire (étape 6) | C'est le cœur de l'option C : vérifier que ce qui est calculé par l'amont tient dans ce qui est vérifié par l'aval. Sans ce contrôle, l'option C n'apporte rien de plus que les briques amont |
| « Ne corrige aucun écart à la place des briques » | La tentation de B-50 est de « réduire l'ancrage pour qu'il rentre » — c'est faux. Si l'ancrage ne rentre pas, c'est l'élément aval qui s'agrandit, ou l'effort amont qui est revu. B-50 ne tranche pas |
| Fiche technique DOC-09 obligatoire | Une capacité de connecteur ne s'invente pas : elle vient de la fiche technique du fabricant. Sans elle, la note n'est pas opposable |
| Écart de contrôle croisé jamais « acceptable » sans justification | Un écart de contrôle croisé non justifié est une erreur qui passe. La tolérance doit être justifiée, pas implicitement acceptée |
| Rapport de contrôle croisé (pièce 4) | C'est le livrable qui prouve que le contrôle a été fait. Sans lui, le contrôle croisé est une affirmation, pas une preuve |
| « Ne vérifie pas les éléments porteurs » | B-50 calcule les assemblages, pas les éléments assemblés. Un boulon peut tenir alors que la poutre flambe — chaque brique a son périmètre |
| « Ne produis aucun assemblage sans fiche technique » | Un assemblage sans fiche technique est un assemblage qui n'est pas opposable — les caractéristiques du connecteur (capacité, classe) sont inconnues. Le mode PARAMÉTRIQUE est la seule réponse correcte |
| Filigrane + mention mode | Un plan d'assemblage exécutable qui porte le mode PARAMÉTRIQUE sans filigrane est un plan qui finit par être exécuté — alors qu'il n'est pas exécutable |

Les quatre familles d'assemblages — méthodes de calcul :

| Famille | Méthode | Exemples |
| --- | --- | --- |
| Ancrages BA | EC2 §8.4 (ancrage des armatures), EC2 §8.7 (recouvrement) | Attentes de poteaux BA, ancrages de dalles dans les voiles, ancrages de linteaux |
| Assemblages métalliques | EC3-1-8 (boulons, soudures, platines), NF EN 1992-4 (tiges d'ancrage) | Platines de pied de poteau, assemblages poutre-poteau, sabots métalliques |
| Assemblages bois | EC5 §8 (Johansen, sabots, équerres, boulons, entailles) | Sabots de pannes sur fermes, équerres anti-soulèvement, boulons d'assemblage |
| Scellements maçonnerie | EC6 §8 (ancrages maçonnerie), NF EN 1992-4 (ancrages chimiques) | Scellements de chaînages rapportés, de raidisseurs, de garde-corps, de linteaux métalliques |

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

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses sur la résistance des connecteurs, des résines, des nuances |
| B-23 (Exploitation du diagnostic existant) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-40 (Fondations superficielles) | Le logement vérifié — B-50 fait le contrôle croisé et renvoie la correction si l'ancrage ne rentre pas |
| B-41 (Fondations profondes) | Les efforts aux têtes de pieux (si des ancrages sont prévus) |
| B-42 (Verticaux BA) | Les efforts à ancrer (N_Ed, M_Ed, section des barres) — B-50 calcule les attentes |
| B-43 (Planchers et dallages) | Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les assemblages |
| B-44 (Charpente bois) | Les efforts aux assemblages (N_Ed, V_Ed, M_Ed, nature de l'assemblage) — B-50 calcule les assemblages |
| B-45 (Structure métallique) | Les efforts aux nœuds (N_Ed, V_Ed, M_Ed, nature de l'assemblage) — B-50 calcule les assemblages |
| B-46 (Maçonnerie : vérification) | Les efforts aux scellements (chaînages, raidisseurs) — B-50 calcule les scellements |
| B-47 (Escaliers) | Les efforts aux appuis et aux scellements (N_Ed, V_Ed, M_Ed) — B-50 calcule les scellements |
| B-48 (Prédalles et planchers préfabriqués) | Les efforts aux appuis et aux connexions (N_Ed, V_Ed, M_Ed) — B-50 calcule les connexions |
| B-49 (Linteaux et seuils) | Les efforts aux appuis (N_Ed, V_Ed, M_Ed) — B-50 calcule les ancrages |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Les plans produits — B-31 vérifie la cohérence avec le fichier source calé |
| B-33 (Vérification croisée) | Les plans produits — B-33 vérifie la cohérence avec les autres livrables |
| B-34 (Synthèse des réservations) | Les attentes et scellements dimensionnés |
| B-40 (Fondations superficielles) | Les efforts à ancrer (N_Ed, M_Ed, sections des barres, tiges) — pour la vérification du logement |
| B-42 (Verticaux BA) | Aucune donnée en amont — B-42 fournit les efforts à ancrer, B-50 calcule les attentes |
| B-47 (Escaliers) | Aucune donnée en amont — B-47 fournit les efforts, B-50 calcule les scellements |
| B-48 (Prédalles et planchers préfabriqués) | Aucune donnée en amont — B-48 fournit les efforts, B-50 calcule les connexions |
| B-49 (Linteaux et seuils) | Aucune donnée en amont — B-49 fournit les efforts, B-50 calcule les ancrages |
| B-60 (Plans d'exécution) | La note et les plans de détail — B-60 les reprend et les indice |
| B-62 (Nomenclature et façonnage) | Les plans — B-62 en extrait la nomenclature détaillée (boulons, soudures, tiges, résines) |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | Le rapport de contrôle croisé — B-70 vérifie que tous les écarts ont été traités |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-50 |
| --- | --- | --- |
| MAT-01 à MAT-04 | Matériaux BA | BLOQUANTE (pour ancrages BA) |
| MAT-05 | Nuance d'acier métallique | BLOQUANTE (pour assemblages métalliques) |
| MAT-06 | Classe de bois | BLOQUANTE (pour assemblages bois) |
| MAT-07 | Nature et résistance de la maçonnerie existante | BLOQUANTE (pour scellements maçonnerie) |
| MAT-09 à MAT-11 | Classe de bloc, mortier, type de maçonnerie | BLOQUANTE (pour scellements maçonnerie) |
| DOC-09 | Fiches techniques produits (connecteurs, résines, boulons) | BLOQUANTE (interdit le mode COMPLET si absente) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |

Variables produites
B-50 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de calcul + plans de détail + auto-contrôle + rapport de contrôle croisé) qui alimente B-60, B-62 et B-70.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | MAT-01 à MAT-11, DOC-09, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques ASSEMBLAGE-*, échelles, formats, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE), en particulier C-04 (B-50 pas B-48) et D-06 (option C) | 11_HISTORIQUE/Journal_des_modifications.md |

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

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 06_PHASE_4_CALCULS/B-50_Assemblages_Ancrages.md]**

<!-- FIN DU PACK — CARNAC v3.0 -->
