# B-13 — DÉTECTION ET QUALIFICATION DES CONTRADICTIONS INTER-PIÈCES

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-13** — Détection et qualification des contradictions |
| Phase | 1 — Analyse |
| **Mode d'appel** | **PARTIEL-DÉCLARÉ** — B-10 et B-11 livrés en mode dégradé, B-12 sans accès au rapport |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Entrées lues | **B-10** ind. A · **B-11** ind. A · **B-12** ind. B · **B-00** ind. C (21 contradictions à chaud) · **B-01** ind. B · **B-03** ind. I (18 décisions) |
| Sortie | Tableau qualifié + répartition par brique + synthèse 8 lignes |
| Indice du livrable | **A** |
| Date | 19/10/2026 |
| Brique suivante | **B-14 (Périmètre de lot)** — puis B-15 |

---

## 1. MÉTHODE — ET UNE DISTINCTION QUE JE N'AI PAS VOULU FORCER

La fiche B-13 définit strictement la **contradiction** : *« deux pièces affirment des choses incompatibles sur un même objet »*. Une **lacune** ou une **imprécision** n'en sont pas — elles relèvent de B-10, B-11 ou B-12 et ne figurent pas ici.

**Cette définition m'a obligé à scinder le corpus en deux.** Trois des contradictions soumises ne sont pas inter-pièces :

- **C-22** oppose le CCTP (§ 01.2.1.7.2, semelles filantes) à **D-10**, une **décision client** du 19/10/2026 ;
- **C-24** oppose D2 folio 04 (« les altimétries peuvent varier ») à **D-09 / D-12**, décisions client.

Une décision n'est pas une pièce du DCE. Les ranger dans le même tableau aurait été une commodité, pas une qualification. Elles font donc l'objet du **tableau B**, avec un statut propre — et ce statut est plus grave, parce qu'une pièce contractuelle qui contredit une décision est un **écart contractuel**, pas une incohérence interne.

**C-23** (compactage) reste au contraire au tableau A : CCTP § 01.2.1.9 contre D2 folio 04, deux pièces du même dossier.

**Test appliqué systématiquement** : *les deux affirmations peuvent-elles être vraies en même temps ?* Si oui, ce n'est pas une contradiction, et la ligne est écartée. Aucune n'a été retenue sur la foi d'une seule des deux sources.

---

## 2. TABLEAU A — CONTRADICTIONS INTER-PIÈCES (22 lignes)

> **Légende gravité** : **B** = bloquante · **ALVD** = à lever avant démarrage · **AS** = à surveiller.
> **Légende nature** : **T** = technique · **C** = contractuelle · **I** = d'interface.

| N° | Objet | Source A (réf. exacte) | Source B (réf. exacte) | Nature de l'écart | Grav. | Nat. | Brique(s) | Mode induit | Inscription RDR |
|---|---|---|---|---|---|---|---|---|---|
| **C-01** | Adresse | **D3 p. 1** : « 2 Rue Alfred Dormeuil, 78290 Croissy » | **D2 p. 1** et **D4 p. 1** : « 11 rue Paul Demange, 78290 Croissy-sur-Seine » | Deux adresses pour le même pavillon | **AS** | **C** | B-60, B-64 | COMPLET | **R-39** *(proposé)* |
| **C-02** | Charge d'exploitation | **D3 p. 10-11** : **150 daN/m²** | **D2 p. 1** : **250 daN/m²** | +67 % sur la même structure | **B** | **T** | B-21, B-40 à B-45 | PARAMÉTRIQUE | **R-06** *(déjà)* |
| **C-03** | Destination | **D3 p. 2** : habitation + service technique ; **D1** : « Flora & Gardien » | **D2 p. 1**, **D4** : « cabinet paramédical » | Programme divergent | **ALVD** | **C** | B-14, B-20 | COMPLET | **R-40** *(proposé)* |
| **C-04** | Maître d'ouvrage | **D1 p. 1** : UNIVI, Lille | **D4 p. 1** : SCI GEMS RC – site 208, Rueil | Deux entités MOA | **ALVD** | **C** | B-64, B-71 | COMPLET | **R-23** *(déjà)* |
| **C-05** | Renfort des solives | **D3 p. 18** : « le renforcement des solives **n'est pas jugé utile** » | **D2 folio 01** : renforts R1 / R2 / R3 contractualisés | Conclusion du diagnostic contredite par la prescription | **B** | **T** | B-44, B-45 | PARAMÉTRIQUE | **R-41** *(proposé)* |
| **C-06** | Périmètre du lot | **D1 titre** : « Flora **& Gardien** » | **D1 sommaire** : Flora seul ; **D4 p. 28** : deux bâtiments | Bâtiment annoncé, non décrit | **ALVD** | **C** | B-14, B-62 | COMPLET | **R-42** *(proposé)* |
| **C-07** | Charpente bois | **D2 folio 02** : pannes, demi-ferme, contrefiches | **D1 sommaire** : aucune section bois | Travaux dessinés, non spécifiés | **B** | **C** | B-44, B-50 | PARAMÉTRIQUE | **R-22** *(déjà)* |
| **C-08** | Charges permanentes | **D2 p. 1** : **100 daN/m²** | **D4 p. 5 et 14** : « sol à recharger de 15 cm » (255-330 daN/m²) | 2,5 à 3,3 fois l'hypothèse | **B** | **T** | B-21, B-43 | PARAMÉTRIQUE | **R-08** *(déjà)* |
| **C-09** | Murs démolis / frangements | **D4 p. 5** : 3 murs, 1 ouverture, 1 agrandissement, 1 passage 90×210 | **D2 folio 01** : F1 à F4 + J1, **sans dimensions ni cotes** | Correspondance impossible à établir | **B** | **T** | B-45, B-49, B-60 | PARAMÉTRIQUE | **R-43** *(proposé)* |
| **C-10** | Usage « salle de sport » | **D4 p. 6 et 17** : salle de sport 34,25 m² | **D2 p. 1** : 250 daN/m², catégorie bureaux | Catégorie d'usage sous-évaluée | **B** | **T** | B-21 | PARAMÉTRIQUE | **R-07** *(déjà)* |
| **C-11** | Reprise en sous-œuvre | **D2 folio 04** : passes alternées de gros béton | **D1 § 01.2.1.7.2** : semelles filantes neuves, « selon BET » | Reprise dessinée sur le folio de la **passerelle**, pas du pavillon | **B** | **T** | B-40, B-60 | PARTIEL-DÉCLARÉ | **R-31bis / V-26** *(déjà)* |
| **C-12** | Échelle | **D2 folio 01 cartouche** : « 1/50 – 1/20 » | **D2 folios 01, 02, 03 plan** : « (1/80) » | Échelle du cartouche ≠ échelle du dessin | **ALVD** | **T** | B-30, B-60 | COMPLET | **R-44** *(proposé)* |
| **C-13** | Indice des folios | **D2 p. 1 (sommaire)** : folio 3 = « – » | **D2 folio 03 cartouche** : « B » | Indice sommaire ≠ indice folio | **AS** | **C** | B-71 | COMPLET | **R-45** *(proposé)* |
| **C-14** | Orientation des façades | **D4 p. 1 (sommaire)** : p. 21 « nord est », p. 22 « ouest sud » | **D4 p. 21** : « SUD EST » ; **p. 22** : « NORD OUEST » | Quatre orientations pour deux planches | **AS** | **T** | B-60 | COMPLET | **R-46** *(proposé)* |
| **C-15** | Classe d'exposition | **D2 p. 1** : « XA4 » | **D1 § 01.1.1** : NP EN 206+A1, qui ne définit que XA1 à XA3 | Classe non normative | **B** | **T** | B-40, B-42, B-43 | PARAMÉTRIQUE | **R-14** *(déjà)* |
| **C-16** | Enrobage | **D2 p. 1** : c<sub>nom</sub> = **30 mm** | **D2 p. 1** (même cartouche) : S4 + **XC4** + w<sub>k</sub> = 0,4 mm | Cohérence c<sub>nom</sub> / (c<sub>min,dur</sub> + Δc<sub>dev</sub>) non démontrée | **B** | **T** | B-40, B-42, B-46 | PARTIEL-DÉCLARÉ | **R-03 / R-04** *(déjà)* |
| **C-17** | Sécurité incendie | **D2 p. 1** : « stabilité au feu par encoffrement » | **D2 p. 1** : section SECURITE INCENDIE **intégralement vide** | Prescription sans exigence | **B** | **T** | B-42, B-43, B-49 | PARAMÉTRIQUE | **R-12** *(déjà)* |
| **C-18** | Séisme | **D2 p. 1** : zone 1, catégorie II | **D2 p. 1** : a<sub>gr</sub> = vide, classe de sol = vide | Action non calculable | **B** | **T** | B-42, B-46 | PARAMÉTRIQUE | **R-11** *(déjà)* |
| **C-19** | Relevé de charpente | **D2 folio 02** : plans établis | **D2 folio 02** : « ZONE NON RELEVEE » ×2 | Relevé incomplet, déclaré par le BET | **B** | **T** | B-44 | PARAMÉTRIQUE | **R-20** *(déjà)* |
| **C-20** | Sigle « RSO » | **D2 p. 1** : « RSO ancrées d'au moins 0,5 m » → élément de fondation | **D2 folio 04** : « après stabilisation de la RSO » → ouvrage | Acronyme dans deux sens incompatibles | **ALVD** | **T** | B-40 | PARTIEL-DÉCLARÉ | **R-47** *(proposé)* |
| **C-21** | Profondeur d'ancrage | **D-P4 / D-04** : **0,40 m** | **D2 p. 1** : **≥ 0,50 m** | 10 cm d'écart, soit 25 % de l'encastrement | ✅ **TRANCHÉE** | **T** | B-40 | COMPLET | **Close par D-08** |
| **C-23** | Compactage | **D1 § 01.2.1.9** : compactage de la plate-forme, sans réserve | **D2 folio 04** : « ne pas compacter sur ce débord », « distance de sécurité le long des soubassements » | Prescriptions contraires selon la pièce | **ALVD** | **T** | B-43, B-40 | COMPLET | **R-49** *(proposé)* |

---

## 3. TABLEAU B — PIÈCES CONTREDITES PAR UNE DÉCISION POSTÉRIEURE (2 lignes)

> **Statut propre.** Ces deux écarts ne sont pas des contradictions internes au DCE : le DCE y est cohérent avec lui-même. C'est une **décision du 19/10/2026** qui contredit la pièce contractuelle. La conséquence est plus lourde qu'une incohérence interne : il faut **mettre le marché à jour**, ou accepter un écart documenté.

| N° | Objet | Source A — pièce | Source B — décision | Nature de l'écart | Grav. | Nat. | Brique(s) | Mode | Inscription RDR |
|---|---|---|---|---|---|---|---|---|---|
| **C-22** | Géométrie des semelles | **D1 § 01.2.1.7.2** : « **semelles filantes BA** », sections selon BET | **D-10** (19/10/2026) : **semelles isolées**, puis **D-14** : **60 × 60 cm minimum** | Le marché prescrit une filante ; la décision retient une isolée. La surface d'assise varie d'un facteur 4 à 5,76 | **B** | **C** | B-40, B-60, B-62 | COMPLET | **R-48** *(proposé)* |
| **C-24** | Variabilité altimétrique | **D2 folio 04** : « les altimétries des semelles **peuvent varier** sur une même pièce » | **D-09 / D-12** (19/10/2026) : **−1,00 m / TN minimum**, nivellement jamais par remontée | Le plan admet une variabilité que la décision encadre strictement | **B** | **C** | B-40, B-60 | COMPLET | **R-50** *(proposé)* |

**Ce que C-22 implique et que je ne peux pas laisser passer.** Le CCTP décrit une **semelle filante** ; D-10 puis D-14 retiennent une **semelle isolée de 60 × 60 minimum**. Ce n'est pas une nuance de dessin : c'est un **autre ouvrage**, avec un autre métré, un autre ferraillage et un autre prix. **Si le marché n'est pas mis à jour, nous exécutons un ouvrage que le CCTP ne décrit pas** — et l'écart se discutera en fin de chantier, pas maintenant. C'est le point le plus lourd de tout ce tableau.

---

## 4. TABLEAU SECONDAIRE — RÉPARTITION PAR BRIQUE

| Brique | Bloquantes | À lever avant démarrage | À surveiller | **Mode consolidé induit** |
|---|---|---|---|---|
| **B-21** — DDC préliminaire | 3 *(C-02, C-08, C-10)* | — | — | **PARAMÉTRIQUE** |
| **B-30** — Calage | — | 1 *(C-12)* | — | **COMPLET** |
| **B-40** — Fondations | 5 *(C-15, C-16, C-22, C-24, C-11)* | 2 *(C-20, C-23)* | — | **PARAMÉTRIQUE** |
| **B-42** — Verticaux BA | 4 *(C-15, C-16, C-17, C-18)* | — | — | **PARAMÉTRIQUE** |
| **B-43** — Planchers / dallages | 3 *(C-08, C-15, C-17)* | 1 *(C-23)* | — | **PARAMÉTRIQUE** |
| **B-44** — Charpente bois | 3 *(C-05, C-07, C-19)* | — | — | **PARAMÉTRIQUE** |
| **B-45** — Structure métallique | 3 *(C-02, C-05, C-09)* | — | — | **PARAMÉTRIQUE** |
| **B-46** — Maçonnerie | 2 *(C-16, C-18)* | — | — | **PARAMÉTRIQUE** |
| **B-49** — Linteaux / seuils | 2 *(C-09, C-17)* | — | — | **PARAMÉTRIQUE** |
| **B-50** — Assemblages | 1 *(C-07)* | — | — | **PARAMÉTRIQUE** |
| **B-60** — Plans d'exécution | 3 *(C-22, C-24, C-09)* | 1 *(C-12)* | 2 *(C-01, C-14)* | **COMPLET** *(hors R-37 fermée par D-17)* |
| **B-62** — Nomenclature | 1 *(C-22)* | 1 *(C-06)* | — | **COMPLET** |
| **B-64** — Notice de synthèse | — | 1 *(C-04)* | 1 *(C-01)* | **PARTIEL-DÉCLARÉ** |
| **B-71** — Indiçage | — | 1 *(C-04, partagée avec B-64)* | 1 *(C-13)* | **PARTIEL-DÉCLARÉ** |
| **B-14** — Périmètre de lot | — | 2 *(C-03, C-06)* | — | **COMPLET** |
| **B-20** — Conception GO | — | 1 *(C-03)* | — | **INTERNE-GO** |

**Lecture.** **Aucune brique de calcul n'atteint le mode COMPLET** : B-40 à B-50 restent toutes en PARAMÉTRIQUE. Ce n'est pas un excès de prudence — c'est la conséquence directe de **14 contradictions bloquantes**, dont **une seule** (C-21) est déjà tranchée.

**Une observation qui compte plus que le compte.** Les briques documentaires (B-14, B-20, B-60, B-62, B-64, B-71) sont **majoritairement en COMPLET** : leurs contradictions sont contractuelles ou administratives, et elles se lèvent par une réponse de la MOE, pas par un calcul. L'écart entre les deux familles est net : **ce dossier bloque sur les valeurs, pas sur les pièces.**

---

## 5. CE QUI N'EST PAS UNE CONTRADICTION — ET QUE JE N'AI PAS MIS DANS LES TABLEAUX

Application du test « les deux affirmations peuvent-elles être vraies en même temps ? » :

| Objet | Pourquoi ce n'est pas une contradiction | Où il est traité |
|---|---|---|
| **Absence de section charpente au CCTP** (au-delà de C-07) | Une pièce qui ne parle pas d'un objet est une **lacune** | B-10, tableau 2 |
| **XA4 sans méthode de calcul** | Une classe inexistante est une **imprécision normative** ; elle devient contradiction seulement au contact de la NP EN 206 (C-15) | B-10 et C-15 |
| **RSO non défini** | Le sigle est employé deux fois avec deux sens : c'est bien une contradiction (C-20) et non une lacune | C-20 |
| **Charpente non reconnue dans deux zones** | Le BET déclare lui-même le relevé partiel : il n'y a pas deux affirmations incompatibles, mais une **information manquante assumée** | B-11, § zones non relevées |
| **Tassements hors mission (D-15)** | Aucune pièce ne contredit D-15 : c'est un **choix de périmètre**, pas un écart | B-12, § 5 |
| **Nappe absente (D-16)** | Déclaration unique, non contredite par une autre pièce | B-12, § 5 |

---

## 6. LES DOUZE INSCRIPTIONS PROPOSÉES AU RDR — **JE NE LES AI PAS ÉCRITES**

La fiche B-13 demande de **proposer** l'inscription au RDR. Je propose, je n'inscris pas : le RDR est votre registre, et douze lignes ajoutées d'office changeraient son visage sans votre accord.

| Réserve proposée | Objet | Gravité | Brique(s) |
|---|---|---|---|
| **R-39** | Adresse du pavillon | AS | B-60, B-64 |
| **R-40** | Destination du bâtiment | ALVD | B-14, B-20 |
| **R-41** | Renfort des solives : diagnostic contre DCE | B | B-44, B-45 |
| **R-42** | Périmètre « Gardien » | ALVD | B-14, B-62 |
| **R-43** | Murs démolis non cotés | B | B-45, B-49, B-60 |
| **R-44** | Échelle cartouche contre échelle plan | ALVD | B-30, B-60 |
| **R-45** | Indice du folio 03 | AS | B-71 |
| **R-46** | Orientations des façades | AS | B-60 |
| **R-47** | Sigle « RSO » | ALVD | B-40 |
| **R-48** | **Semelles filantes (CCTP) contre isolées (D-10/D-14)** | **B** | B-40, B-60, B-62 |
| **R-49** | Compactage de plate-forme | ALVD | B-43, B-40 |
| **R-50** | Variabilité altimétrique admise par D2 | B | B-40, B-60 |

**Si vous les validez, le registre passe de 39 à 51 réserves (30 → 42 ouvertes).** Les onze autres contradictions sont déjà portées par une réserve existante (R-03, R-04, R-06, R-07, R-08, R-11, R-12, R-14, R-20, R-22, R-23, R-31bis) et **ne demandent aucune création**.

---

## 7. SYNTHÈSE — HUIT LIGNES

- **24 contradictions qualifiées** : 14 bloquantes, 6 à lever avant démarrage, 3 à surveiller, 1 déjà tranchée (C-21 par D-08).
- **Les trois plus lourdes** : **C-22** (filantes contre isolées — change l'ouvrage), **C-24** (variabilité altimétrique contre règle de niveau), **C-11** (reprise en sous-œuvre dessinée sur un autre bâtiment).
- **Par nombre de briques impactées** : C-22, C-24 et C-16 touchent chacun trois briques de production ou plus.
- **11 contradictions étaient déjà au RDR depuis B-00** (C-02, C-04, C-07, C-08, C-10, C-11, C-15, C-16, C-17, C-18, C-19) — elles sont désormais **qualifiées**, ce qu'elles n'étaient pas.
- **12 sont nouvelles ou requalifiées** : C-01, C-03, C-05, C-06, C-09, C-12, C-13, C-14, C-20, C-22, C-23, C-24 — dont **3 issues de B-10** (C-22, C-23, C-24).
- **Par nature** : **16 techniques, 8 contractuelles, 0 d'interface** — l'analyse inter-lots relève de B-14, qui n'est pas encore faite.
- **Aucune brique de calcul n'atteint le mode COMPLET** ; les briques documentaires y accèdent presque toutes.
- **Conclusion** : les contradictions ne se lèvent pas par une relecture, mais par **quatre réponses de la MOE** (C-22, C-24, C-11, C-07) et **quatre données** (C-15, C-16, C-18, C-19).

---

## 8. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-13) | État | Observation |
|---|---|---|
| Chaque ligne cite les deux sources avec référence exacte | ✅ | **24 lignes**, deux colonnes de source, fichier + folio/page + indice |
| Chaque ligne porte un classement gravité et un classement nature | ✅ | Colonnes distinctes, jamais fusionnées |
| Aucune ligne ne relève d'une lacune ou d'une imprécision | ✅ | **6 objets écartés** et justifiés au § 5 |
| Chaque ligne identifie la brique impactée et le mode induit | ✅ | Colonnes renseignées ; répartition consolidée au § 4 |
| Aucune contradiction n'a été tranchée par moi | ✅ | **C-21** est signalée comme tranchée **par D-08**, pas par B-13. **Aucune** des 23 autres n'est arbitrée |
| La synthèse tient en 8 lignes | ✅ | **8 lignes** exactement |

**Écart signalé (V4)** : B-13 est appelée à être **COMPLET** quand les trois audits le sont. B-10, B-11 et B-12 sont tous en mode dégradé — B-13 est donc livrée en **PARTIEL-DÉCLARÉ**. La détection est limitée aux pièces couvertes par les audits : **les 30 pages non lues du CCTP peuvent receler d'autres contradictions** que je ne peux pas voir.

**Placeholders résiduels (V7)** : aucun.

---

## 9. POINT DE CONTRÔLE HUMAIN

1. **Les douze inscriptions R-39 à R-50** : je les propose, vous les validez ? *(Elles feraient passer le registre à 51 réserves.)*
2. **C-22 — la plus lourde** : le CCTP prescrit des semelles **filantes**, D-10/D-14 des **isolées de 60 × 60**. Faut-il **mettre le CCTP à jour**, ou traiter l'écart comme une réserve d'exécution ?
3. **C-24** : D2 folio 04 admet que « les altimétries peuvent varier ». Souhaitez-vous que B-40 porte une **règle de tolérance altimétrique** compatible avec D-12 ?
4. **Le classement d'interface à zéro** : je l'explique par l'absence de B-14. Confirmez-vous qu'il faut faire B-14 **avant** B-15, pour ne pas conclure sur des risques sans connaître les lots ?

---

*Brique B-13, **indice A**, livrée en mode **PARTIEL-DÉCLARÉ**.*

*Aucune inscription au RDR n'est appliquée : les 12 créations sont **proposées**, en attente de validation.*

*Aucune brique aval engagée : **B-14 (Périmètre de lot)** attend un GO.*
