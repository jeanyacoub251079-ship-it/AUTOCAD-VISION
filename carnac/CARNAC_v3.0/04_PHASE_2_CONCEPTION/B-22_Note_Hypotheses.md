Fichier 04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md — CARNAC v3.0
________________


B-22 — NOTE D'HYPOTHÈSES DE CONCEPTION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-21 (DDC préliminaire) |
| Brique suivante | B-23 (Exploitation du diagnostic), B-24 (Existant non sondé) |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | FDC (B-02), RDR (B-03), toutes les briques de la phase 2, puis toutes les briques de calcul qui introduisent une hypothèse (B-40 à B-50) |
| Sortie unique | Note d'hypothèses unique du projet, annexée à la FDC, mise à jour à chaque introduction |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * une première fois après B-21, pour consigner les hypothèses de conception (charges, matériaux, existant, sol) ;
   * à chaque fois qu'une brique introduit, modifie ou retire une hypothèse, en phases 2, 3 et 4.
Ce que vous fournissez à l'IA : la FDC (B-02), le RDR (B-03), les sorties des briques qui ont introduit des hypothèses (B-20, B-21, B-24, B-40 à B-50), et les hypothèses déjà consignées. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * chaque hypothèse H-xx (valeur, source, justification, statut) ;
   * la cohérence entre les hypothèses d'un même projet ;
   * les hypothèses abandonnées (jamais supprimées).
Ce que B-22 apporte de spécifique — la note unique :

| Aspect | Note unique B-22 | Notes éclatées (N notes) |
| --- | --- | --- |
| Cohérence | Les hypothèses se lisent ensemble — les interactions sont visibles | Les hypothèses sont isolées — les incohérences passent inaperçues |
| Vérification | Un tiers ouvre un seul document pour valider toutes les hypothèses | Un tiers doit ouvrir N documents pour valider une seule note de calcul |
| Traçabilité | Un numéro H-xx est stable dans toute la chaîne | Chaque note a ses propres numéros — les références croisées sont fragiles |
| Opposabilité | La note unique est la pièce opposable en cas de litige | Les notes éclatées rendent la défense difficile |

Règle stricte : une seule note d'hypothèses par projet — pas une par brique. Les hypothèses d'un même projet se lisent ensemble : une hypothèse de charge et une hypothèse de matériau interagissent, et leur cohérence ne se vérifie qu'en les lisant côte à côte.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : tenir à jour la note d'hypothèses UNIQUE de l'opération {{ID-01}} — {{ID-02}}. Cette note est annexée à la FDC et couvre l'ensemble du projet. Elle est mise à jour à chaque fois qu'une brique introduit, modifie ou retire une hypothèse.


RÈGLES
1. Chaque hypothèse porte un numéro unique H-xx (H-01, H-02…) et ne change plus de numéro, même si son contenu évolue. Une hypothèse révisée porte « H-xx (rév. n) ».
2. Chaque hypothèse porte :
   - la valeur retenue ;
   - la brique qui l'introduit (B-xx) ;
   - la justification (pourquoi cette valeur ?) ;
   - la source (pièce, ou « hypothèse de travail GO ») ;
   - le statut : À CONFIRMER / CONFIRMÉE / ABANDONNÉE ;
   - la brique impactée (celle qui utilise cette hypothèse).
3. Les hypothèses sont classées par famille : charges, matériaux, géométrie, existant, sol, autres.
4. Toute hypothèse non confirmée figure en filigrane sur les livrables qui l'utilisent : mention « sous hypothèse H-xx — à confirmer ».
5. Toute hypothèse abandonnée n'est jamais supprimée : elle est marquée ABANDONNÉE avec la raison, pour préserver la traçabilité.


INTERDICTIONS
- Ne crée aucune hypothèse sans justification : « valeur courante » n'est pas une justification.
- Ne supprime aucune hypothèse : tu la marques ABANDONNÉE.
- Ne fusionne jamais deux hypothèses distinctes en une seule.
- N'utilise aucune hypothèse qui ne soit pas dans la note.
- Ne recopie pas une hypothèse sans son numéro H-xx : un livrable qui cite une hypothèse doit citer son numéro.


SORTIE
Section 1 — Index des hypothèses actives
N° | Famille | Valeur | Brique introduisant | Brique impactée | Statut


Section 2 — Détail par hypothèse
Pour chaque hypothèse : H-xx, objet, valeur retenue, justification, source, statut, brique introduisant, brique impactée, date d'introduction, date de dernière révision.


Section 3 — Historique des révisions
Date | Hypothèse (H-xx) | Nature de la révision | Auteur | Motif


CRITÈRE D'ACCEPTATION
La note est acceptée si :
- chaque hypothèse a un numéro unique et stable ;
- chaque hypothèse a une justification (pas seulement une valeur) ;
- chaque hypothèse a un statut (À CONFIRMER / CONFIRMÉE / ABANDONNÉE) ;
- aucune hypothèse n'a été supprimée (les abandonnées sont conservées) ;
- l'historique des révisions est tenu ;
- l'index en section 1 est cohérent avec le détail en section 2.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Note unique par projet » | Votre choix — la cohérence des hypothèses ne se vérifie qu'en les lisant ensemble. Un éclatement en N notes rend impossible la vérification par un tiers (BC, BET, MOE) qui devrait ouvrir N documents pour valider une seule note de calcul |
| « H-xx stable, jamais renuméroté » | Un livrable cite « sous H-03 ». Si H-03 devient H-07 en cours de projet, le livrable devient faux sans que personne ne s'en aperçoive. La stabilité du numéro est la garantie de la traçabilité |
| « Toute hypothèse abandonnée est conservée » | La traçabilité est la protection en cas de litige : « pourquoi H-03 a-t-elle été abandonnée ? » doit avoir une réponse datée. Une hypothèse supprimée est une hypothèse qui ne peut plus être expliquée |
| « Ne recopie pas une hypothèse sans son numéro » | Une hypothèse non numérotée n'est pas traçable — et un livrable qui la cite sans numéro n'est pas opposable. C'est le verrou V2 (traçabilité) appliqué aux hypothèses |
| « Aucune hypothèse sans justification » | Une hypothèse « valeur courante » est indéfendable ; une hypothèse justifiée (« pas de G3 disponible, valeur plancher de la fourchette G2 ») est défendable. La justification est ce qui distingue une hypothèse de travail d'une valeur inventée |
| « Ne fusionne jamais deux hypothèses distinctes » | Une fusion d'hypothèses rend la traçabilité impossible — si l'hypothèse fusionnée est infirmée, on ne sait plus quelle partie de la valeur est fausse |
| « Toute hypothèse non confirmée figure en filigrane sur les livrables » | Un livrable qui utilise une hypothèse sans le mentionner est un livrable qui paraît certain alors qu'il est incertain. Le filigrane est la seule protection |
| « Ne supprime aucune hypothèse » | Une hypothèse supprimée est une hypothèse qui ne peut plus être expliquée en cas de litige. La conservation, même avec statut ABANDONNÉE, garantit la traçabilité |
| Section 3 — Historique des révisions | L'historique permet de savoir quand une hypothèse a changé, pourquoi, et par qui. C'est ce qui permet de comprendre une décision en cas de contestation |

Les trois statuts d'hypothèse — précision utile :

| Statut | Définition | Conséquence |
| --- | --- | --- |
| À CONFIRMER | Hypothèse de travail, non validée | Le livrable qui l'utilise porte le filigrane « sous hypothèse H-xx — à confirmer » |
| CONFIRMÉE | Hypothèse validée (par une décision RDR, une donnée reçue, ou une validation BET/BC) | Le livrable peut être en mode COMPLET (si l'hypothèse est explicitement citée) |
| ABANDONNÉE | Hypothèse qui n'est plus utilisée | Conservée pour traçabilité — le livrable qui l'utilisait doit être révisé |

Les six familles d'hypothèses — précision utile :

| Famille | Contenu | Exemples |
| --- | --- | --- |
| Charges | Poids propres, surcharges, cloisons | Poids propre d'un complexe de plancher non détaillé au CCTP |
| Matériaux | Classes de béton, nuances d'acier, classes de bois | Nuance d'acier d'un profilé Even non précisée (S235 supposé) |
| Géométrie | Sections de l'existant, épaisseurs de murs, hauteurs | Section d'une panne existante non sondée |
| Existant | Résistance des matériaux existants, état parasitaire | Résistance d'une maçonnerie ancienne non testée |
| Sol | q_adm, agressivité, ancrage | Valeur plancher de q_adm en attente du G3 |
| Autres | Classe de service, durée de vie, conditions de chantier | Durée de vie de projet non précisée |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — les valeurs À confirmer deviennent des hypothèses H-xx |
| B-03 (Registre des décisions) | Les décisions déjà prises — les hypothèses peuvent être validées par une décision D-xx |
| B-20 (Conception structure GO) | Les hypothèses de conception — B-22 les consigne et les numérote |
| B-21 (Descente de charges préliminaire) | Les hypothèses de charges — B-22 les consigne et les numérote |
| B-24 (Vérification d'éléments existants non) | Les hypothèses sur les sections inconnues de l'existant |
| B-40 (Fondations superficielles) | Les hypothèses introduites par chaque brique de calcul |
| B-41 (Fondations profondes) | Les hypothèses introduites par chaque brique de calcul |
| B-42 (Verticaux BA) | Les hypothèses introduites par chaque brique de calcul |
| B-43 (Planchers et dallages) | Les hypothèses introduites par chaque brique de calcul |
| B-44 (Charpente bois) | Les hypothèses introduites par chaque brique de calcul |
| B-45 (Structure métallique) | Les hypothèses introduites par chaque brique de calcul |
| B-46 (Maçonnerie : vérification) | Les hypothèses introduites par chaque brique de calcul |
| B-47 (Escaliers) | Les hypothèses introduites par chaque brique de calcul |
| B-48 (Prédalles et planchers préfabriqués) | Les hypothèses introduites par chaque brique de calcul |
| B-49 (Linteaux et seuils) | Les hypothèses introduites par chaque brique de calcul |
| B-50 (Assemblages et ancrages) | Les hypothèses introduites par chaque brique de calcul |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-40 (Fondations superficielles) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-41 (Fondations profondes) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-42 (Verticaux BA) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-43 (Planchers et dallages) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-44 (Charpente bois) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-45 (Structure métallique) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-46 (Maçonnerie : vérification) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-47 (Escaliers) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-48 (Prédalles et planchers préfabriqués) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-49 (Linteaux et seuils) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-50 (Assemblages et ancrages) | Les hypothèses sur la résistance des connecteurs, des résines, des nuances |
| B-64 (Notice de synthèse) | Les hypothèses H-xx actives — B-64 les liste avec leur statut |
| B-70 (Auto-contrôle déclaré de synthèse) | Les hypothèses non confirmées — B-70 vérifie que chaque hypothèse est tracée |
| B-72 (Journal de clôture) | Les hypothèses non confirmées — B-72 les liste dans les points ouverts |
| T-01 (Prompt de sincérité) | Les hypothèses H-xx — T-01 classe les éléments de principe et les éléments à lever |

Variables consommées

| Code | Libellé | Statut dans B-22 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| Toutes les variables À confirmer de la FDC | Selon la variable | BLOQUANTE (chaque valeur À confirmer doit être une hypothèse H-xx) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |

Variables produites
B-22 ne produit pas de variable au sens du dictionnaire : sa sortie est la note d'hypothèses (document unique, annexé à la FDC), qui référence toutes les hypothèses H-xx du projet.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| FDC (B-02) | Valeurs et fiabilité — les valeurs À confirmer deviennent des hypothèses | Document de projet |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-22, vous devez valider chaque hypothèse à son introduction. Une hypothèse validée trop tard est une hypothèse qui a déjà contaminé les calculs. La validation à l'introduction est la seule qui garantit que les calculs reposent sur des hypothèses connues et acceptées.
Cas particulier — hypothèse introduite par une brique de calcul : si une brique de calcul (par exemple B-42) introduit une hypothèse (par exemple, « section P1 supposée 140×140×8 »), elle est consignée en B-22 avec :
   * le numéro H-xx ;
   * la brique introduisant (B-42) ;
   * la brique impactée (B-42 elle-même, et B-50 pour les ancrages) ;
   * le statut À CONFIRMER.
La note est mise à jour à chaque introduction — pas en fin de projet.
Cas particulier — hypothèse confirmée : si une hypothèse est confirmée (par exemple, par une décision RDR D-05, ou par une donnée reçue), elle change de statut (À CONFIRMER → CONFIRMÉE), avec :
   * la date de confirmation ;
   * la source de la confirmation (décision RDR, donnée reçue, validation BET/BC).
L'historique des révisions (section 3) enregistre ce changement.
Cas particulier — hypothèse abandonnée : si une hypothèse n'est plus utilisée (par exemple, une hypothèse de charge devenue sans objet), elle est marquée ABANDONNÉE (pas supprimée), avec :
   * la raison de l'abandon ;
   * la date ;
   * la brique qui a rendu l'hypothèse obsolète.
Les livrables qui utilisaient cette hypothèse doivent être révisés (par le biais de B-32 — mise à jour incrémentale).
Cas particulier — hypothèse en conflit avec une décision RDR : si une hypothèse H-xx est en conflit avec une décision RDR (par exemple, H-03 dit « XC2 supposé » et D-05 dit « XA3 retenu »), l'hypothèse est abandonnée et remplacée par la décision RDR. La note documente ce remplacement.
Cas particulier — hypothèse liée à une donnée manquante : si l'hypothèse est liée à une donnée manquante (par exemple, « q_adm non disponible — on suppose 0,25 MPa »), elle est statuée À CONFIRMER, et elle est co-déclarée avec le verrou correspondant au RDR (V-xx). La note et le RDR se renvoient mutuellement.
Format de sortie attendu : trois sections distinctes (index, détail, historique des révisions). L'index est la vue rapide ; le détail est la vue complète ; l'historique est la vue chronologique.
Consignation : la note d'hypothèses B-22 est annexée à la FDC (B-02) — elle est la référence unique pour toutes les hypothèses du projet. Toute hypothèse utilisée dans une brique de calcul doit être présente dans cette note.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Note d'hypothèses `H-xx` unique et opposable.** Chaque hypothèse porte : valeur retenue, norme ou DTU d'appui, zone d'application, délai de contradiction (`DEC-06`), mode de report graphique (nuage). Une hypothèse sans norme d'appui n'est pas une hypothèse notifiée : c'est une valeur de repli interdite par le verrou `V3`.