Fichier 04_PHASE_2_CONCEPTION/B-25_Stabilite_Globale.md — CARNAC v3.0
________________


B-25 — STABILITÉ GLOBALE, CONTREVENTEMENT, JOINTS DE DILATATION ET SISMIQUE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — création de la brique (voir Journal des modifications, entrée v3.0) |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-20 (Conception ou synthèse structurelle) |
| Brique suivante | B-21 (DDC préliminaire), puis B-40 à B-50 |
| Modes d'appel | COMPLET (système de contreventement et géométrie d'ensemble établis) · HYPOTHÈSE-NOTIFIÉE (zone sismique, catégorie d'importance ou classe de sol non fournies mais bornables) · INTERNE-GO (le système de contreventement n'existe pas : nous le concevons) · SANS OBJET (aucune action horizontale à reprendre : ouvrage enterré contrebuté sur quatre faces, décision `D-xx`) |
| Entrées lues | Sortie de B-20, DDC de B-21, MPD validée (B-01), FDC (B-02), rapport géotechnique (B-12), vue nettoyée et différentielle (B-32) |
| Sortie unique | Note de stabilité globale : système de contreventement, cheminement des efforts horizontaux, excentricités et torsion, découpage `JD`, vérification sismique, stabilité des phases provisoires, schéma reporté sur les plans |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20 et avant toute brique de calcul, pour tout bâtiment de plus d'un niveau, tout ouvrage contreventé par voiles, portiques ou palées, tout bâtiment avec joints de dilatation, et systématiquement en gabarit `L-XL` (`CFG-02`). En gabarit `S`, B-25 est appelée en version abrégée si l'ouvrage ne comporte qu'un niveau et aucun contreventement dédié.

Ce que vous fournissez à l'IA : la sortie de B-20 (trame, porteurs, planches de synthèse), la DDC de B-21, la FDC (zone sismique, catégorie d'importance, classe de sol, coefficients), la vue nettoyée B-32 et le découpage `JD` (`CFG-03`). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{gabarit}} et {{mode}}.

Ce que vous validez à la sortie : le système de contreventement retenu (et son adéquation au gabarit de l'ouvrage), les excentricités et la torsion, le découpage en blocs `JD`, la position sismique et la catégorie d'importance, la stabilité des phases provisoires, et le report graphique du schéma de contreventement.

Ce que B-25 apporte de spécifique — la stabilité n'est pas un sous-produit du calcul élément par élément :
| Aspect | Sans B-25 | Avec B-25 |
| --- | --- | --- |
| Cheminement horizontal | Supposé par chaque brique locale | Explicite, continu, justifié niveau par niveau |
| Torsion | Découverte au calcul ou jamais | Calculée (excentricité structurale et accidentelle) avant les calculs locaux |
| Joints de dilatation | Subis, découverts sur plan | Décidés, dimensionnés, reportés en plan et en coupe |
| Phases provisoires | Oubliées | Vérifiées (stabilité des voiles et poteaux en phase transitoire) |
| Sismique | Mention générique | Position `EC8` explicite : zone, catégorie, classe de sol, méthode d'analyse |
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.

MISSION : établir la note de stabilité globale de l'opération {{ID-01}} — {{ID-02}}, de gabarit {{gabarit}}, à partir de la conception ou de la synthèse structurelle B-20, de la descente de charges B-21 et du découpage en blocs structurels. Tu ne dimensionnes aucun élément : tu établis le système qui reprend et transmet les efforts horizontaux, et tu vérifies que ce système est continu, stable et compatible avec la géométrie différentielle du projet.

DONNÉES D'ENTRÉE À QUALIFIER AVANT CALCUL
- Zone sismique, catégorie d'importance, classe de sol, coefficient de comportement : valeur, source et norme d'appui (EC8 et arrêté national en vigueur).
- Actions du vent : site, catégorie de terrain, hauteur de référence, coefficients (EC1-1-4).
- Découpage en blocs et joints de dilatation : nombre, position, largeur, justification du découpage.
- Descente de charges horizontales et verticales par niveau et par bloc (B-21).

MÉTHODE
1. Identifie et décris le système de contreventement réellement disponible dans la géométrie du projet : voiles, portiques, noyaux, palées, triangulations, murs existants conservés, remplissages participatifs (avec la prudence requise). Si la conception B-20 ne comporte aucun système explicite, tu le conçois et tu le signales.
2. Trace le cheminement des efforts horizontaux : origine (vent, séisme, poussées, effets de second ordre), traversée de chaque niveau, reprise par les éléments verticaux, transmission aux fondations. Chaque niveau doit avoir une reprise identifiée ; toute rupture de cheminement est un défaut bloquant.
3. Calcule les centres de masse et de rigidité par niveau, l'excentricité structurale, l'excentricité accidentelle réglementaire, et l'effet de torsion associé. Vérifie les déplacements différentiels entre éléments de contreventement.
4. Vérifie la régularité (en plan et en élévation) au sens de l'EC8 ; en cas d'irrégularité, adapte la méthode d'analyse et les coefficients.
5. Décide et justifie le découpage en blocs `JD` : longueur maximale sans joint, effets de la température, retrait, tassements différentiels, phases de construction. Chaque joint est coté et reporté en plan et en coupe.
6. Vérifie la stabilité des phases provisoires : voiles ou poteaux non encore liaisonnés, planchers non coulés, stabilité au vent des éléments élancés en cours de montage, stabilité des fouilles et des talus de travail.
7. Vérifie les effets globaux du second ordre (amplification des efforts horizontaux) et la sensibilité aux déplacements.
8. Produis le schéma de contreventement et les coupes de principe, avec repères cohérents avec B-20 et report explicite sur le fond B-32.

INTERDICTIONS
- Ne dimensionne aucun élément porteur : les sections, ferraillages et assemblages relèvent de B-40 à B-50.
- Ne suppose aucune zone sismique, aucune catégorie d'importance et aucune classe de sol : chaque valeur est sourcée ou porte un repère {{DEC-05}} avec norme d'appui.
- Ne déclare jamais un bâtiment « régulier » sans avoir mesuré les excentricités.
- Ne crée aucun joint de dilatation sans justification écrite (longueur, température, retrait, tassement, phasage).
- Ne conserve pas un contreventement implicite : un remplissage en maçonnerie n'est jamais compté comme système de contreventement sans justification et sans dispositif de ductilité.
- Ne produis aucun schéma sans repères identiques à ceux de B-20.
- Ne laisse aucune discontinuité de cheminement non traitée : soit elle est reprise par un ouvrage identifié, soit elle est déclarée bloquante.

SORTIE
Pièce 1 — Système de contreventement : nature, implantation, justification du choix, éléments participants et éléments exclus.
Pièce 2 — Cheminement des efforts : tableau par niveau (origine, valeur, éléments de reprise, transmission au niveau inférieur), avec détection des ruptures.
Pièce 3 — Torsion et régularité : centres de masse et de rigidité, excentricités, effet de torsion, verdict de régularité, méthode d'analyse retenue.
Pièce 4 — Joints de dilatation : tableau des blocs `JD` (position, largeur, motif, report plan et coupe).
Pièce 5 — Phases provisoires : situations étudiées, vérifications, dispositions de stabilité.
Pièce 6 — Schéma de contreventement reporté sur le fond B-32, avec légende et renvois.

CRITÈRE D'ACCEPTATION
La note est acceptée si :
- chaque niveau dispose d'une reprise d'efforts horizontaux explicitement identifiée, jusqu'aux fondations ;
- les centres de masse et de rigidité, les excentricités et l'effet de torsion sont calculés pour chaque niveau ;
- la régularité en plan et en élévation est statuée avec la méthode d'analyse correspondante ;
- chaque zone sismique, catégorie d'importance et classe de sol est sourcée ou porte un repère d'hypothèse avec norme d'appui ;
- chaque joint de dilatation est justifié, coté et reporté en plan et en coupe ;
- les phases provisoires sont étudiées ;
- aucun élément porteur n'a été dimensionné dans cette brique.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{gabarit}} et {{mode}}, ainsi que tout repère d'hypothèse {{DEC-05}} par sa valeur ou son renvoi. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
| Clause | Pourquoi |
| --- | --- |
| Brique distincte et non intégrée à B-20 | La conception décide de la géométrie, la stabilité globale décide du cheminement des efforts. Mélanger les deux conduit à des trames dessinées sans système de reprise, et à des calculs locaux fondés sur des hypothèses de contreventement jamais explicitées |
| « Tu ne dimensionnes aucun élément » | Frontière nette avec B-40 à B-50 (V11 et séquence bloquante). Une brique de stabilité qui dimensionne empiète sur les notes de calcul et crée des valeurs non tracées |
| Cheminement niveau par niveau | C'est le seul contrôle qui détecte une rupture de reprise : un plancher qui ne transmet pas, un voile qui s'arrête au R+1, une façade qui ne redescend pas. Sans ce tableau, la rupture n'apparaît qu'au calcul, ou jamais |
| Excentricités mesurées, jamais supposées | Un bâtiment déclaré « régulier » sans mesure est un bâtiment dont la torsion est ignorée. La mesure des centres de masse et de rigidité est la seule preuve de régularité opposable |
| Joints de dilatation justifiés | Un joint mal placé crée deux bâtiments qui se poussent ; un joint absent crée des fissures attribuées à la structure. Le joint est une décision de conception, pas un constat de chantier |
| Phases provisoires | Les effondrements de structure neuve surviennent presque toujours en phase provisoire. La stabilité au vent d'un voile non liaisonné n'est justifiée par aucun calcul d'exploitation |
| Report graphique avec repères identiques | Un schéma de contreventement qui ne partage pas les repères de B-20 est inutilisable sur chantier, et invérifiable par B-31 et B-33 |
| Sismique explicite | La mention « structure conforme » ne vaut rien. Seule compte la chaîne complète : zone, catégorie, classe de sol, régularité, méthode, coefficient de comportement |
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | La zone sismique, la catégorie d'importance, la classe de sol et les coefficients |
| B-20 (Conception structure GO) | La trame, les porteurs et les planches de synthèse |
| B-21 (Descente de charges préliminaire) | Les charges verticales et horizontales par niveau et par bloc |
| B-30 (Calage sur dxf/dwg source) | Le repère de référence dans lequel le schéma est établi |
| B-32 (Vue nettoyée par livrable) | Le fond structurel pur, support du schéma de contreventement |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-34 (Synthèse des réservations) | Les éléments de contreventement et les zones où tout percement est interdit |
| B-40 (Fondations superficielles) | Les efforts horizontaux et moments d'ensemble transmis au sol d'assise |
| B-41 (Fondations profondes) | Idem, avec les combinaisons sismiques |
| B-42 (Verticaux BA) | Les efforts tranchants et moments de torsion par élément de contreventement |
| B-44 (Charpente bois) | Les efforts horizontaux repris par les palées et triangulations |
| B-45 (Structure métallique) | Idem, avec les dispositions de ductilité |
| B-46 (Maçonnerie : vérification) | Le rôle interdit ou limité des remplissages dans le contreventement |
| B-60 (Plans d'exécution) | Le schéma de contreventement, les joints de dilatation et les dispositions parasismiques à reporter |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-25 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | BLOQUANTE |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | NON BLOQUANTE (BLOQUANTE si sous-sol) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| SEC-01 | Exigences de résistance au feu (degré, durée, source) | NON BLOQUANTE |

Variables produites
B-25 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de stabilité globale) et un schéma reporté sur les plans, qui alimentent B-21, B-40 à B-50 et B-60.

Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | CFG-02, CFG-03, STR-01, STR-02, DEC-05 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques, échelles, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain : à la sortie de B-25, vous validez le système de contreventement et le découpage en blocs. C'est votre décision d'ingénieur : le modèle propose un système compatible avec la géométrie, vous décidez s'il est constructible avec les moyens de l'entreprise et compatible avec le phasage.

Cas particulier — bâtiment sans système de contreventement explicite : B-25 s'appelle en INTERNE-GO et conçoit le système (voiles de contreventement, palées, triangulations), avec alerte sur les conséquences contractuelles si la conception n'est pas dans la mission.

Cas particulier — **zone de sismicité 1 (très faible)** (v3.0.1) : **aucune vérification sismique**. Arrêté du 22/10/2010. B-25 mentionne « Zone 1 — sismique SANS OBJET » et **s'arrête** sur ce volet. Interdit : spectre, catégorie d'importance demandée pour un calcul sismique, `H-xx` sismique, relance MOA.

Cas particulier — données sismiques absentes **hors zone 1** : si la zone n'est pas 1 et que la catégorie d'importance n'est pas fournie, B-25 s'appelle en HYPOTHÈSE-NOTIFIÉE : elle retient l'enveloppe la plus défavorable compatible avec la localisation connue, cite l'article d'appui, reporte l'hypothèse sous nuage et la soumet au délai DEC-06. Une donnée sismique n'est jamais « supposée conforme ».

Cas particulier — **stabilité provisoire d'un bâtiment existant** (v3.0.1) : la vérification du contreventement en phase provisoire **incombe à la MOE structure de conception**. B-25 **signale** l'interface (dépose de refend, charge de chantier). Elle **ne calcule pas** la stabilité provisoire de l'existant. Elle **ne produit pas** de `T-04` bloquant à ce titre.

Cas particulier — bâtiment existant conservé : le contreventement de l'existant est qualifié avant d'être compté (continuité, liaisons, état). Un existant non qualifié n'est jamais compté comme système de reprise ; il est porté en PA-xx avec prescription ENC.

Format de sortie attendu : six pièces distinctes (système, cheminement, torsion et régularité, joints, phases provisoires, schéma reporté). Le schéma est produit sur le fond B-32 avec les repères de B-20.

Consignation : la note B-25 est annexée au RDL et le schéma reporté au jeu de plans B-60.
________________

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce.

**V15 — Différentiel temporel et continuité mécanique descendante.** Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Brique nouvelle v3.0.** B-25 est la seule brique habilitée à statuer sur la stabilité d'ensemble. Aucune brique de calcul ne peut la contourner en supposant un contreventement implicite. En gabarit `L-XL`, son exécution est obligatoire et son schéma est reporté sur chaque plan d'exécution.