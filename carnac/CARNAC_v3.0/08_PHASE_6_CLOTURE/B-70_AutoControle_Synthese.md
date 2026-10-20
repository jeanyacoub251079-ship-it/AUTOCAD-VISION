Fichier 08_PHASE_6_CLOTURE/B-70_AutoControle_Synthese.md — CARNAC v3.0
________________


B-70 — AUTO-CONTRÔLE DÉCLARÉ DE SYNTHÈSE ET DE COHÉRENCE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 6 — Vérification croisée et clôture |
| Brique précédente | B-60, B-62, B-64 (livrables produits) — ou toute brique de calcul pour un contrôle intermédiaire |
| Brique suivante | B-71 (Indiçage), B-72 (Journal de clôture) |
| Fréquence | En fin de production de chaque livrable complet (après B-60, B-62, B-64) et une fois en clôture du projet |
| Modes d'appel | COMPLET (toutes les briques amont en COMPLET ou PARTIEL-DÉCLARÉ) · PARTIEL-DÉCLARÉ (certaines briques en modes dégradés : les incohérences liées à ces briques sont signalées et non résolues) · PARAMÉTRIQUE (briques suspendues : B-70 produit un auto-contrôle partiel, filigrané) |
| Paramètre d'appel | {{périmètre}} = livrable (un seul livrable) / projet (l'ensemble des livrables du projet) |
| Entrées lues | Auto-contrôles de toutes les briques exécutées (B-40 à B-50), contrôles croisés de B-50, RDR (décisions, réserves, verrous), RDL (livrables produits), B-31 (preuves de superposition), B-33 (vérifications croisées) |
| Sortie unique | Auto-contrôle de synthèse : tableau agrégé + tableau des incohérences inter-briques + tableau des interfaces + vérification des modes + verdict global |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * en fin de production de chaque livrable complet (après B-60, B-62, B-64) — pour vérifier que le livrable est cohérent ;
   * une fois en clôture du projet (avant B-71 et B-72) — pour vérifier que l'ensemble des livrables est cohérent.
Ce que vous fournissez à l'IA : les auto-contrôles de toutes les briques exécutées (B-40 à B-50), les contrôles croisés de B-50, le RDR (décisions, réserves, verrous), le RDL (livrables produits), les preuves de superposition (B-31) et les vérifications croisées (B-33). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{périmètre}} et {{mode}}.
Ce que vous validez à la sortie :
   * l'inventaire des auto-contrôles disponibles (et des manquants) ;
   * le tableau agrégé des éléments (verdict par élément) ;
   * les incohérences inter-briques (avec brique responsable) ;
   * les interfaces vérifiées ou non vérifiées ;
   * la conformité des modes (verrou V12) ;
   * le verdict global (cohérent / cohérent avec réserves / incohérent).
Ce que B-70 apporte de spécifique — la vue d'ensemble :

| Aspect | Auto-contrôle d'une brique (B-40 à B-50) | Auto-contrôle de synthèse (B-70) |
| --- | --- | --- |
| Périmètre | Une brique (fondations, verticaux, planchers, etc.) | Toutes les briques du livrable ou du projet |
| Objet | Vérifier que chaque élément de la brique est conforme | Vérifier que les éléments sont cohérents entre eux |
| Détection | Erreurs dans la brique | Incohérences entre briques |
| Interfaces | Non traitées (chaque brique ignore les autres) | Explicites (B-42→B-40, B-50→toutes, etc.) |
| Verdict | Conforme pour la brique | Cohérent pour le livrable ou le projet |

Le rôle critique de B-70 : chaque brique de calcul est individuellement correcte (elle vérifie ses éléments), mais l'ensemble peut être incohérent. Exemple :
   * B-42 (verticaux) déclare que le poteau P2 est conforme à ses vérifications EC2 ;
   * B-40 (fondations) déclare que la semelle S/P2 n'a pas été vérifiée en logement d'ancrage ;
   * chacune est individuellement correcte, mais l'ensemble est incohérent — le poteau ne pourra pas descendre ses barres dans la semelle.
Seule B-70 peut détecter ce type d'incohérence — c'est sa fonction principale.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire l'auto-contrôle déclaré de synthèse et de cohérence du {{périmètre}} (livrable / projet) {{ID-01}} — {{ID-02}}, à partir des auto-contrôles produits par toutes les briques exécutées. Tu ne refais aucun auto-contrôle : tu agrèges, tu contrôles la cohérence entre eux, et tu détectes les interfaces non couvertes.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.


MÉTHODE — DANS CET ORDRE


Étape 1 — Inventaire des auto-contrôles disponibles
Liste toutes les briques exécutées pour ce périmètre :
- brique | mode d'exécution | auto-contrôle produit (oui / non) | raison si non (suspendue, SANS OBJET, mode PARAMÉTRIQUE).
Si une brique a produit un livrable mais pas son auto-contrôle, tu le signales : c'est une anomalie de production.


Étape 2 — Tableau agrégé par élément
Pour chaque élément produit (semelle, poteau, profilé, plancher, linteau, assemblage, etc.) :
- repère ;
- brique source ;
- verdict de l'auto-contrôle de la brique (conforme / conforme avec réserves / à corriger) ;
- réserves déclarées par la brique.


Étape 3 — Détection des incohérences inter-briques
Compare les déclarations des briques sur les éléments partagés :
- une brique amont déclare un effort transmis, une brique aval déclare ne pas avoir reçu cet effort : incohérence ;
- une brique amont déclare un élément conforme, une brique aval déclare que l'appui de cet élément n'est pas vérifié : incohérence ;
- une brique déclare un élément en mode PARTIEL-DÉCLARÉ sans que la décision RDR correspondante existe : incohérence ;
- une brique déclare un élément conforme sur la base d'une hypothèse H-xx, une autre brique déclare H-xx abandonnée : incohérence.
Pour chaque incohérence : nature, briques concernées, élément concerné, gravité (bloquante / à lever / à surveiller), brique responsable de la correction (amont ou aval).


Étape 4 — Vérification des interfaces
Pour chaque interface identifiée dans le carnet :
- B-42 → B-40 : les efforts à ancrer fournis par B-42 ont-ils été vérifiés en logement par B-40 ?
- B-42 → B-50 : les efforts à ancrer fournis par B-42 ont-ils été calculés par B-50 ?
- B-43 → B-50 : les efforts aux appuis fournis par B-43 ont-ils été calculés par B-50 ?
- B-44 → B-50 : les efforts aux assemblages fournis par B-44 ont-ils été calculés par B-50 ?
- B-45 → B-50 : les efforts aux nœuds fournis par B-45 ont-ils été calculés par B-50 ?
- B-46 → B-50 : les efforts des chaînages fournis par B-46 ont-ils été calculés par B-50 ?
- B-47/B-48/B-49 → B-50 : idem.
Pour chaque interface : vérifiée (oui / non / partiellement) | brique responsable en cas de non-vérification.


Étape 5 — Vérification des modes
- Aucune brique n'est passée de PARAMÉTRIQUE à COMPLET sans décision RDR ?
- Aucune brique n'est passée de BLOQUANTE à NON BLOQUANTE (verrou V12) ?
- Toutes les décisions RDR sont citées avec auteur et date ?


Étape 6 — Verdict global
- Nombre de briques exécutées | nombre d'auto-contrôles disponibles | nombre d'incohérences | nombre d'interfaces non vérifiées | nombre de modes non conformes.
- Verdict : cohérent / cohérent avec réserves / incohérent.
- Si incohérent : liste des briques à reprendre et des points à lever avant clôture.


INTERDICTIONS
- Ne refais AUCUN auto-contrôle brique par brique : tu agrèges, tu contrôles la cohérence, tu ne recommences pas les vérifications.
- Ne corrige AUCUNE incohérence : tu la signales, tu identifies la brique responsable, tu renvoies.
- Ne déclare pas une interface « vérifiée » sans avoir trouvé la trace de sa vérification dans la brique aval.
- Ne tolère aucun écart entre modes et décisions RDR : un mode PARTIEL-DÉCLARÉ sans décision RDR est une anomalie bloquante.
- Ne produis pas d'auto-contrôle de synthèse COMPLET si une seule brique est en PARAMÉTRIQUE : le mode global est PARTIEL-DÉCLARÉ minimum.
- Ne déclare pas le livrable ou le projet cohérent tant qu'une incohérence bloquante subsiste.


SORTIE
Pièce 1 — Inventaire des auto-contrôles.
Pièce 2 — Tableau agrégé par élément.
Pièce 3 — Tableau des incohérences inter-briques.
Pièce 4 — Tableau des interfaces vérifiées / non vérifiées.
Pièce 5 — Vérification des modes (conformité RDR et verrou V12).
Pièce 6 — Verdict global et liste des briques à reprendre.


CRITÈRE D'ACCEPTATION
L'auto-contrôle de synthèse est accepté si :
- toutes les briques exécutées figurent dans l'inventaire avec leur mode ;
- chaque élément produit figure dans le tableau agrégé avec son verdict ;
- toutes les incohérences inter-briques sont listées, avec brique responsable ;
- toutes les interfaces sont vérifiées, avec la trace de vérification citée ;
- la conformité des modes avec les décisions RDR est vérifiée (verrou V12) ;
- le verdict global est explicite ;
- si le mode global est PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE, la mention et le filigrane correspondants figurent.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{périmètre}} (par livrable ou projet) et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Tu agrèges, tu ne refais pas » | Refaire les auto-contrôles brique par brique est une perte de temps et une source d'erreur. Le rôle de B-70 est la vue d'ensemble — les vérifications détaillées existent déjà dans chaque brique |
| Détection des incohérences inter-briques | C'est la valeur ajoutée de B-70 : chaque brique est individuellement correcte, mais l'ensemble peut être incohérent (poteau conforme mais semelle non vérifiée). Seule cette brique peut le voir |
| Vérification des interfaces | Les interfaces (B-42→B-40, B-50→toutes) sont les points où les erreurs se glissent, parce qu'aucune brique seule ne les voit de bout en bout. B-70 les vérifie explicitement |
| Contrôle du mode et du verrou V12 | Une brique qui a « discrètement » changé de mode est une brique non fiable. La vérification du mode est une vérification de la méthode, pas du résultat |
| « Ne déclare pas cohérent tant qu'une incohérence bloquante subsiste » | Une incohérence bloquante non résolue rend le livrable non opposable. Le verdict « cohérent » est une signature, pas un constat |
| Pas de COMPLET si une brique est PARAMÉTRIQUE | Le mode global est celui de la brique la plus dégradée. Un livrable qui contient une brique PARAMÉTRIQUE ne peut pas être déclaré COMPLET |
| Inventaire des auto-contrôles manquants | Une brique qui a produit un livrable mais pas son auto-contrôle est une anomalie de production. B-70 doit la signaler — sinon, on croit que tout est vérifié alors que rien ne l'est |
| Verdict global explicite | Un tableau sans verdict laisse la décision au lecteur. Le verdict global (cohérent / cohérent avec réserves / incohérent) est la conclusion de l'auto-contrôle — sans lui, l'auto-contrôle n'est pas actionnable |
| Liste des briques à reprendre | Une incohérence détectée mais non attribuée à une brique est une incohérence qui n'est pas traitée. La liste des briques à reprendre rend l'auto-contrôle actionnable |
| Filigrane si PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE | Un auto-contrôle de synthèse qui ne porte pas le filigrane est un auto-contrôle qui est lu comme COMPLET — alors qu'il ne l'est pas |

Les trois niveaux de verdict — précision utile :

| Verdict | Définition | Conséquence |
| --- | --- | --- |
| Cohérent | Aucune incohérence bloquante, toutes les interfaces sont vérifiées | Le livrable ou le projet est validé |
| Cohérent avec réserves | Des incohérences non bloquantes subsistent (par exemple, une incohérence à surveiller), toutes les interfaces sont vérifiées | Le livrable ou le projet peut être diffusé, avec mention des réserves |
| Incohérent | Une ou plusieurs incohérences bloquantes subsistent, ou des interfaces ne sont pas vérifiées | Le livrable ou le projet ne doit pas être diffusé — les briques responsables doivent corriger |

Le piège de la « fausse cohérence » : un modèle qui reçoit les auto-contrôles de toutes les briques a tendance à :
   * soit recopier les verdicts individuels sans vérifier la cohérence entre eux ;
   * soit conclure que le livrable est cohérent parce que chaque brique est individuellement conforme.
Les deux sont faux :
   * recopier sans vérifier, c'est ne pas faire le travail de B-70 (la cohérence inter-briques n'est pas vérifiée) ;
   * conclure que c'est cohérent parce que chaque brique est conforme, c'est ignorer les incohérences entre briques (par exemple, un poteau conforme mais dont la semelle n'est pas vérifiée).
La règle est : vérifier explicitement les incohérences et les interfaces — pas les supposer.
Le piège de l'interface non vérifiée : une interface (par exemple, B-42→B-40 sur les ancrages) peut être non vérifiée même si les deux briques sont individuellement conformes :
   * B-42 calcule le poteau et fournit les efforts à ancrer ;
   * B-40 calcule la semelle mais ne vérifie pas le logement des ancrages (parce qu'elle attend les efforts de B-50) ;
   * B-50 calcule les ancrages mais ne vérifie pas qu'ils rentrent dans la semelle (parce qu'il attend le logement de B-40).
Dans ce cas, aucune brique n'a vérifié l'interface — et B-70 est la seule à pouvoir le détecter. C'est exactement pour cela que B-70 est indispensable.
Le piège du mode « discret » : une brique qui a changé de mode sans décision RDR est une brique non fiable :
   * elle est passée de PARAMÉTRIQUE à COMPLET sans que la donnée manquante soit arrivée — c'est une violation du verrou V12 ;
   * elle est passée de BLOQUANTE à NON BLOQUANTE — c'est une violation du sens unique de la requalification (V12) ;
   * la décision RDR correspondante n'existe pas — c'est une décision implicite du modèle.
B-70 vérifie explicitement la conformité des modes avec les décisions RDR — c'est ce qui rend le système fiable.
Le piège de l'auto-contrôle manquant : une brique qui a produit un livrable mais pas son auto-contrôle est une anomalie de production :
   * soit l'auto-contrôle a été oublié (le livrable est peut-être bon, mais non vérifié) ;
   * soit la brique a été exécutée en mode PARAMÉTRIQUE et l'auto-contrôle n'a pas été produit (le livrable est provisoire).
B-70 signale ces anomalies — elles sont aussi graves qu'une incohérence, parce qu'elles masquent un défaut de production.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions et verrous — B-70 vérifie la conformité des modes avec les décisions RDR (verrou V12) |
| B-22 (Note d'hypothèses de conception) | Les hypothèses non confirmées — B-70 vérifie que chaque hypothèse est tracée |
| B-31 (Preuve de superposition) | Le verdict de la preuve — B-70 vérifie que chaque livrable a sa preuve et que le verdict est favorable |
| B-33 (Vérification croisée) | Les verdicts de tous les livrables — B-70 vérifie que chaque livrable a une vérification croisée favorable |
| B-34 (Synthèse des réservations) | Le statut des Points d'Arrêt et l'exhaustivité des réservations |
| B-40 (Fondations superficielles) | L'auto-contrôle B-40 — B-70 vérifie que chaque semelle a son verdict |
| B-41 (Fondations profondes) | Le verdict de B-41 — B-70 vérifie que les fondations profondes sont traitées |
| B-42 (Verticaux BA) | L'auto-contrôle B-42 — B-70 vérifie que chaque vertical a son verdict |
| B-43 (Planchers et dallages) | L'auto-contrôle B-43 — B-70 vérifie que chaque zone a son verdict |
| B-44 (Charpente bois) | L'auto-contrôle B-44 — B-70 vérifie que chaque élément a son verdict |
| B-45 (Structure métallique) | L'auto-contrôle B-45 — B-70 vérifie que chaque profilé a son verdict |
| B-46 (Maçonnerie : vérification) | L'auto-contrôle B-46 — B-70 vérifie que chaque zone a son verdict |
| B-47 (Escaliers) | L'auto-contrôle B-47 — B-70 vérifie que chaque volée a son verdict |
| B-48 (Prédalles et planchers préfabriqués) | L'auto-contrôle B-48 — B-70 vérifie que chaque zone et chaque phase ont leur verdict |
| B-49 (Linteaux et seuils) | L'auto-contrôle B-49 — B-70 vérifie que chaque linteau a son verdict |
| B-50 (Assemblages et ancrages) | Le rapport de contrôle croisé — B-70 vérifie que tous les écarts ont été traités |
| B-60 (Plans d'exécution) | Les plans produits — B-70 vérifie que chaque livrable a son plan |
| B-62 (Nomenclature et façonnage) | Le rapport de cohérence — B-70 vérifie que la cohérence a été faite |
| B-64 (Notice de synthèse) | La notice — B-70 vérifie que chaque livrable a sa notice |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-71 (Indiçage et supersession documentaire) | Le verdict de B-70 — l'indiçage ne se fait que si le verdict est favorable |
| B-72 (Journal de clôture) | Le verdict de B-70 — B-72 liste les points ouverts à traiter avant remise |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-70 |
| --- | --- | --- |
| DEC-01 | Mode attribué à chaque brique | BLOQUANTE |
| DEC-02 | Décisions inscrites au RDR | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |

Variables produites
B-70 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (auto-contrôle de synthèse) qui alimente B-71, B-72 et les destinataires externes.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes (en particulier V11 et V12) | 00_MASTER.md |
| Dictionnaire de variables | DEC-01, DEC-02, DEC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-70, vous devez valider le verdict global — c'est votre appréciation de la criticité des incohérences qui fait foi, pas la seule liste. Une incohérence classée « à surveiller » par le modèle peut être en réalité « bloquante » — c'est votre jugement d'ingénieur qui décide.
Cas particulier — périmètre « livrable » : si B-70 est appelée pour un seul livrable (par exemple, le livrable de fondations), elle agrège uniquement les auto-contrôles des briques qui ont contribué à ce livrable (B-40, B-50 pour les ancrages). Elle ne vérifie pas les incohérences avec les livrables non encore produits.
Cas particulier — périmètre « projet » : si B-70 est appelée pour l'ensemble du projet (en clôture), elle agrège tous les auto-contrôles. C'est la vérification globale — la plus importante.
Cas particulier — auto-contrôle manquant : si une brique a produit un livrable mais pas son auto-contrôle, B-70 le signale dans l'inventaire. C'est une anomalie de production qui doit être corrigée avant clôture.
Cas particulier — incohérence inter-briques : si deux briques déclarent des choses incompatibles (par exemple, B-42 déclare le poteau P2 conforme, B-40 déclare la semelle S/P2 non vérifiée en logement), B-70 :
   * identifie l'incohérence ;
   * identifie les briques concernées ;
   * identifie l'élément concerné ;
   * classe la gravité (bloquante / à lever / à surveiller) ;
   * identifie la brique responsable de la correction (amont ou aval).
C'est votre décision de choisir quelle brique corrige — le modèle propose, vous décidez.
Cas particulier — interface non vérifiée : si une interface (par exemple, B-42→B-40 sur les ancrages) n'a pas été vérifiée (parce qu'aucune des deux briques ne l'a traitée explicitement), B-70 :
   * signale l'interface non vérifiée ;
   * identifie la brique qui devrait la vérifier (généralement B-40 pour le logement, ou B-50 pour le calcul croisé) ;
   * recommande l'action (exécuter B-40 en mode COMPLET si le logement n'a pas été vérifié).
Cas particulier — mode non conforme : si une brique a changé de mode sans décision RDR (violation du verrou V12), B-70 :
   * signale l'anomalie ;
   * identifie la brique concernée ;
   * identifie le mode actuel et le mode attendu (selon RDR) ;
   * recommande l'action (retour au mode attendu, ou décision RDR de validation).
Un mode non conforme est une anomalie bloquante — le livrable ne peut pas être diffusé tant que ce n'est pas résolu.
Cas particulier — verdict « cohérent avec réserves » : si le verdict est « cohérent avec réserves », le livrable peut être diffusé — mais les réserves doivent être explicites dans le livrable (mention dans la notice B-64, mention dans le cartouche). Le lecteur doit savoir qu'il y a des réserves.
Cas particulier — verdict « incohérent » : si le verdict est « incohérent », le livrable ne doit pas être diffusé — les briques responsables doivent corriger, puis B-70 est rappelée pour re-vérifier. Le livrable n'est diffusé qu'avec un verdict « cohérent » ou « cohérent avec réserves ».
Format de sortie attendu : six pièces distinctes (inventaire, tableau agrégé, incohérences, interfaces, modes, verdict). Le verdict global est explicite, avec la liste des briques à reprendre.
Consignation : l'auto-contrôle de synthèse B-70 est annexé au livrable et consigné au RDL — il fait partie du dossier de livraison, avec les plans, la nomenclature et la notice.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Contrôle des hypothèses et des Points d'Arrêt.** L'auto-contrôle de synthèse vérifie : statut et échéance de chaque hypothèse `H-xx` (active, expirée, acceptée, contredite), présence et opposabilité de chaque Point d'Arrêt `PA-xx`, `0` collision de textes sur les plans, adéquation titre ↔ contenu, et absence totale de second œuvre sur les vues structurelles.