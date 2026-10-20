Fichier 04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md — CARNAC v3.0
________________


B-24 — VÉRIFICATION D'ÉLÉMENTS EXISTANTS NON SONDÉS
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-23 (Exploitation du diagnostic) |
| Brique suivante | B-30 (Calage) — ou la première brique de calcul selon le PTD |
| Modes d'appel | PARAMÉTRIQUE uniquement (par construction : l'existant non sondé impose le littéral) |
| Entrées lues | EXI-01 (sections), EXI-03 (résistance), EXI-04 (sondages), B-11, B-23, DOC-05 |
| Sortie unique | Vérification littérale de l'élément existant + tableau de sensibilité non contractuel + liste des essais/sondages nécessaires pour fermer la vérification |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-23, quand des éléments existants sont concernés par nos travaux mais que leurs caractéristiques ne sont pas connues (sections, nuance, résistance). B-24 est la brique qui permet de travailler malgré l'incertitude — elle produit une vérification littérale qui servira dès que le sondage sera disponible.
Ce que vous fournissez à l'IA : les données disponibles sur l'existant (EXI-01 à EXI-04, si partielles), les sorties de B-11 et B-23, le diagnostic (DOC-05). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * le tableau de sensibilité (clairement identifié « NON CONTRACTUEL ») ;
   * la liste des essais (nature, référentiel, nombre, emprise) ;
   * la mention de suspension (vérification suspendue jusqu'à obtention des données).
Ce que B-24 apporte de spécifique — la brique typique du mode PARAMÉTRIQUE :

| Aspect | B-24 (mode PARAMÉTRIQUE) | B-46 (mode COMPLET) |
| --- | --- | --- |
| Données disponibles | Sections, nuances ou résistances inconnues | Sections, nuances et résistances connues |
| Méthode | Vérification littérale + tableau de sensibilité non contractuel | Vérification chiffrée avec les valeurs réelles |
| Valeur retenue | Aucune — la donnée reste en symbole | Valeur(s) issue(s) de la FDC |
| Livrable | Note suspendue, filigranée, suffixée _P | Note d'exécution, exécutable après visa |
| Conclusion | « En attente de [donnée] » | « Vérifié » ou « À renforcer » |

La règle la plus importante : B-24 ne retient aucune valeur. Elle produit des formules littérales, un tableau de sensibilité non contractuel, et la liste des essais nécessaires. C'est exactement le mode PARAMÉTRIQUE que vous avez validé au tronçon 2 : on travaille, on ne conclut pas.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la vérification en mode PARAMÉTRIQUE des éléments existants non sondés de l'opération {{ID-01}} — {{ID-02}}. Tu ne retiens AUCUNE valeur : tu produis des formules littérales, un tableau de sensibilité NON CONTRACTUEL, et la liste des essais nécessaires pour fermer la vérification.


MÉTHODE
1. Pour chaque élément existant non sondé (poutre, solive, panne, ferme, poteau, mur porteur), identifie :
   - la donnée manquante (section ? nuance ? continuité ?) ;
   - la charge transmise par nos ouvrages (issue de B-21 ou B-20) ;
   - la vérification à effectuer (flexion, cisaillement, compression, flambement, déversement, ancrage).
2. Écris la vérification en littéral, avec la donnée manquante laissée en symbole :
   - flexion bois : σ_m,d = M_Ed/W = M_Ed/(b·h²/6) ≤ f_m,d ;
   - flexion métal : M_Ed/M_pl,Rd ≤ 1 avec M_pl,Rd = W_pl·f_y/γ_M0 ;
   - compression bois : N_Ed/(k_c·A·f_c,0,d) ≤ 1 avec k_c fonction de λ ;
   - compression métal : N_Ed/N_b,Rd ≤ 1 avec N_b,Rd = χ·A·f_y/γ_M1 ;
   - cisaillement : τ_d = k·V_Ed/(b·h·k_cr) ≤ f_v,d (bois) ou V_Ed/V_pl,Rd ≤ 1 (métal).
3. Produis un tableau de sensibilité sur une plage de valeurs PLAUSIBLES, clairement identifié comme NON CONTRACTUEL : chaque valeur testée est présentée comme « cas de sensibilité », jamais comme « valeur retenue ».
4. Identifie les essais ou sondages nécessaires pour fermer la vérification : nature de l'essai, référentiel (NF EN 338 pour le bois, NF EN 10025 pour l'acier), nombre, emprise.
5. Rédige la mention de suspension : la vérification est SUSPENDUE jusqu'à obtention des données, la brique reste en mode PARAMÉTRIQUE, le livrable est filigrané.


INTERDICTIONS
- Ne retiens AUCUNE valeur : aucune section, aucune nuance, aucun résultat de vérification n'est « retenu ».
- Ne déclare AUCUN élément « vérifié » : tous sont « en attente de données ».
- Ne présente le tableau de sensibilité comme contractuel : il est TOUJOURS marqué « NON CONTRACTUEL — POUR INFORMATION ».
- N'utilise aucune valeur « par expérience » : toute valeur testée est dans la plage plausible et justifiée comme telle.
- Ne réduis pas la plage plausible pour « faire joli » : si la plage est 100×200 à 200×300, tu la couvres entièrement.
- Ne produis aucun livrable exécutable : la sortie est une note de vérification suspendue, filigranée, avec mention « EN ATTENTE DE [donnée] ».
- Ne propose aucune valeur de repli : la décision de fonder sur une valeur plancher est une décision RDR (PARTIEL-DÉCLARÉ), jamais une initiative de B-24.


SORTIE
Tableau 1 — Éléments non sondés et vérifications suspendues
Élément | Donnée manquante | Charge transmise (kN, kNm) | Vérification à mener | Formule littérale | Brique de fermeture (B-44, B-45, B-46)


Tableau 2 — Tableau de sensibilité NON CONTRACTUEL
Élément | Donnée testée | Valeur testée | Résultat du calcul | Verdict (favorable / défavorable / limite) — pour information uniquement


Tableau 3 — Essais et sondages nécessaires
Élément | Essai | Référentiel | Nombre | Emprise | Responsable | Échéance


Tableau 4 — Impact sur la conception (B-20)
Élément | Conséquence si la donnée reste manquante | Solution de repli possible (décision RDR) | Brique concernée


Puis une synthèse de 6 lignes maximum :
- le nombre d'éléments en attente de données ;
- le nombre d'éléments dont la vérification est favorable pour toutes les valeurs plausibles (bonne nouvelle) ;
- les essais à commander en priorité ;
- les décisions RDR à prendre si les essais ne sont pas commandés.


CRITÈRE D'ACCEPTATION
La vérification est acceptée si :
- chaque élément non sondé a une vérification littérale écrite ;
- chaque donnée manquante est laissée en symbole (jamais remplie) ;
- le tableau de sensibilité est marqué « NON CONTRACTUEL — POUR INFORMATION » ;
- les essais nécessaires sont listés avec référentiel, nombre et emprise ;
- aucun élément n'est déclaré « vérifié » ;
- aucun livrable exécutable n'est produit ;
- la note porte le filigrane « EN ATTENTE DE [donnée] » et le suffixe _P.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Mode PARAMÉTRIQUE par construction | La brique n'a de sens que si la donnée manque. Si elle était disponible, elle relèverait de B-46 (vérification de l'existant) en mode COMPLET. Le mode unique de B-24 est ce qui la distingue de B-46 et garantit qu'elle ne se substitue pas à une vérification réelle |
| « Ne retiens AUCUNE valeur » | La tentation est forte de conclure « avec une section 100×200, ça passe ». C'est exactement ce qu'il faut interdire : une valeur testée n'est pas une valeur retenue. Une valeur retenue par B-24 serait une décision implicite non traçable — et cette décision relève d'une décision RDR (PARTIEL-DÉCLARÉ) |
| Tableau de sensibilité NON CONTRACTUEL | Un tableau de sensibilité mal identifié devient contractuel par usage — quelqu'un finit par l'exécuter. Le marquage explicite « NON CONTRACTUEL — POUR INFORMATION » est la seule protection |
| « Ne réduis pas la plage plausible » | Un modèle a tendance à ne tester que les valeurs qui « passent » — ce qui donne une fausse impression de sécurité. La plage plausible est fixée par la géométrie (sections existantes possibles), pas par le résultat. Si la section existante peut être 100×200 ou 200×300, on teste tout |
| Tableau 3 — Essais et référentiels | Sans référentiel, l'essai n'est pas commandable. NF EN 338 (bois) et NF EN 10025 (acier) sont les référentiels standards. Le nombre et l'emprise rendent l'essai chiffrable |
| « Ne propose aucune valeur de repli » | La valeur de repli est une décision RDR (PARTIEL-DÉCLARÉ), pas une proposition de B-24. C'est le verrou du mode PARAMÉTRIQUE : le modèle peut suggérer une valeur de repli dans B-04 (PTD), mais il ne peut pas l'appliquer sans une décision RDR |
| Filigrane + suffixe _P | Un livrable PARAMÉTRIQUE sans filigrane finit par être exécuté. Le filigrane et le suffixe sont les deux marqueurs qui empêchent la confusion avec un livrable exécutable |
| « Ne déclare aucun élément vérifié » | Un élément « vérifié » suppose une conclusion — et B-24 ne peut pas conclure. Déclarer « vérifié » un élément dont la section est inconnue est une affirmation fausse qui engage la responsabilité |
| Tableau 4 — Impact sur la conception | Une vérification suspendue n'est pas sans conséquence : elle impacte la conception (B-20), les calculs (B-40 à B-50) et le planning. Le tableau 4 documente cette conséquence — c'est ce qui permet à B-04 (PTD) et B-72 (clôture) de traiter les points ouverts |
| Synthèse en 6 lignes | La synthèse identifie les éléments favorables pour toutes les valeurs plausibles — une bonne nouvelle qui permet de fermer certains éléments même sans sondage. Les 6 lignes sont actionnables, pas descriptives |

Les trois verdicts de sensibilité — précision utile :

| Verdict | Définition | Conséquence |
| --- | --- | --- |
| Favorable | Le résultat de la vérification est satisfaisant pour toute la plage de valeurs plausibles | L'élément peut être considéré comme non critique — mais cette conclusion doit être validée par votre jugement (elle reste « pour information ») |
| Limite | Le résultat de la vérification est satisfaisant pour certaines valeurs de la plage, mais pas toutes | L'élément est critique : le sondage est indispensable pour conclure |
| Défavorable | Le résultat de la vérification est insuffisant pour toute la plage de valeurs plausibles | L'élément est à renforcer dans tous les cas — le sondage permettra de dimensionner le renforcement, mais la décision de renforcer est déjà acquise |

La limite de B-24 : même dans le cas « favorable », B-24 ne déclare pas l'élément vérifié — elle signale que toutes les valeurs plausibles sont favorables, ce qui est un indice fort mais qui reste non contractuel. La décision de conclure relève de votre jugement, ou d'une décision RDR.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les données disponibles sur l'existant (EXI-01 à EXI-04) — B-24 les cite, mais ne les complète pas |
| B-11 (Audit du diagnostic structure) | Les données manquantes — B-24 produit une vérification en mode PARAMÉTRIQUE pour les éléments non sondés |
| B-20 (Conception structure GO) | Les sections à vérifier — B-24 produit des vérifications en mode PARAMÉTRIQUE |
| B-21 (Descente de charges préliminaire) | Les charges aux appuis — B-24 les utilise pour les vérifications suspendues |
| B-23 (Exploitation du diagnostic existant) | Les zones hors relevé et les données manquantes — B-24 produit une vérification en mode PARAMÉTRIQUE |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les essais à commander — B-03 les inscrit en réserves (R-xx) avec responsable et échéance |
| B-04 (Plan de travail dégradé) | Les éléments en attente de données et les essais nécessaires — B-04 les intègre dans le plan de travail dégradé |
| B-20 (Conception structure GO) | Les sections inconnues de l'existant — B-20 les prend en compte avec mention |
| B-22 (Note d'hypothèses de conception) | Les hypothèses sur les sections inconnues de l'existant |
| B-44 (Charpente bois) | Les vérifications suspendues de l'existant bois — B-44 les ferme si le sondage est disponible, sinon les reprend en mode PARAMÉTRIQUE |
| B-45 (Structure métallique) | Les vérifications suspendues de l'existant métal — B-45 les ferme si le sondage est disponible |
| B-46 (Maçonnerie : vérification) | Les vérifications suspendues des maçonneries existantes — B-46 les ferme si le sondage est disponible |
| B-49 (Linteaux et seuils) | Les vérifications suspendues des linteaux existants — B-49 les ferme si le sondage est disponible |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les essais à commander — T-04 les transforme en demande formelle à la MOA |

Variables consommées

| Code | Libellé | Statut dans B-24 |
| --- | --- | --- |
| EXI-01 | Sections des éléments existants | BLOQUANTE (si absente, c'est la donnée manquante qui justifie le mode PARAMÉTRIQUE) |
| EXI-03 | Résistance des matériaux existants | BLOQUANTE (idem) |
| EXI-04 | Résultats de sondages destructifs ou semi-destructifs | BLOQUANTE (idem) |
| DOC-05 | Diagnostic structure de l'existant | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |

Variables produites
B-24 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (vérification suspendue) qui alimente B-44, B-45, B-46, B-04 et T-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes (en particulier PARAMÉTRIQUE) | 00_MASTER.md |
| Dictionnaire de variables | EXI-01, EXI-03, EXI-04, DOC-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-24, vous devez vérifier que :
   1. aucune valeur n'est retenue — chaque donnée manquante est en symbole ;
   2. le tableau de sensibilité est bien marqué « NON CONTRACTUEL » ;
   3. les essais sont listés avec référentiel, nombre et emprise ;
   4. les éléments « favorables pour toute la plage » sont bien signalés — c'est la seule bonne nouvelle que B-24 peut produire.
Cas particulier — appel en phase 4 : B-24 peut être appelée en phase 4 (calculs) pour les éléments existants non sondés — c'est la même brique, mais son appel est justifié par un besoin de vérification fine après les calculs d'exécution. Dans ce cas, B-24 reste en mode PARAMÉTRIQUE — elle ne se substitue jamais à B-46 (vérification de l'existant en mode COMPLET) quand les données sont disponibles.
Cas particulier — élément favorable pour toute la plage : si un élément est favorable pour toutes les valeurs plausibles, B-24 le signale dans la synthèse. Vous pouvez alors :
   * soit fermer l'élément (avec votre jugement, mentionné au RDR) ;
   * soit commander le sondage pour confirmation (plus rigoureux, mais plus coûteux) ;
   * soit passer en PARTIEL-DÉCLARÉ avec une valeur de repli (décision RDR).
Cas particulier — élément défavorable pour toute la plage : si un élément est défavorable pour toutes les valeurs plausibles, il est à renforcer dans tous les cas. Le sondage permettra de dimensionner le renforcement (B-44, B-45, B-46 en mode COMPLET), mais la décision de renforcer est déjà acquise — elle remonte dans B-23 (tableau 2, orientations de renforcement).
Cas particulier — élément sans plage plausible : si les données sont tellement manquantes qu'on ne peut même pas définir une plage plausible (par exemple, un élément dont on ne connaît ni la nature ni la fonction), B-24 le signale et recommande une inspection visuelle avant toute tentative de vérification. Ce cas est rare, mais il doit être explicitement traité.
Cas particulier — fermeture de la vérification : une vérification B-24 se ferme :
   * soit par un sondage (la donnée manquante arrive) → la vérification reprend en B-44/B-45/B-46 en mode COMPLET ;
   * soit par une décision RDR (valeur de repli acceptée) → la vérification reprend en mode PARTIEL-DÉCLARÉ ;
   * soit par un jugement de votre part documenté au RDR (élément favorable pour toute la plage — décision d'accepter le risque).
Format de sortie attendu : quatre tableaux distincts (éléments non sondés, sensibilité, essais nécessaires, impact sur la conception), suivis d'une synthèse en 6 lignes maximum. Le tableau de sensibilité est impérativement marqué « NON CONTRACTUEL — POUR INFORMATION ».
Consignation : la note B-24 est annexée au RDR (B-03) — elle documente les vérifications suspendues et alimente les réserves (R-xx) pour les essais à commander.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Inconnue physique = Point d'Arrêt, jamais hypothèse silencieuse.** L'existant non sondé est traité par prescription `ENC` (sondage, dépose, fouille, curage) et Point d'Arrêt `PA-xx` (`DEC-07`), avec critère de lever explicite et conséquence chiffrée en cas de découverte défavorable. Le mode `HYPOTHÈSE-NOTIFIÉE` ne s'applique jamais à une inconnue physique mesurable sur site.