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