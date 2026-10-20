# RECETTE DU CARNET `CARNAC v3.0` — CHECK-LIST DE LECTURE CIBLÉE

| Champ | Valeur |
|---|---|
| **Objet** | Valider les **deux seules fiches entièrement nouvelles** de `v3.0` : `B-25` (stabilité globale) et `B-34` (réservations) — les 37 autres fiches sont des fiches existantes enrichies, à faible risque |
| **Durée** | **20 minutes** (10 points × 2 minutes) |
| **Documents à ouvrir** | `04_PHASE_2_CONCEPTION/B-25_Stabilite_Globale.md` · `07_PHASE_5_LIVRABLES/B-34_Synthese_Reservations.md` |
| **Ce que vous cherchez** | Non pas « est-ce bien écrit », mais : **« est-ce que je signerais un livrable produit selon cette fiche ? »** |
| **Ce que vous ne jugez pas** | Les 37 autres fiches, les annexes, le dictionnaire, l'historique : déjà contrôlés par script (`10/10 PASS`, `0` erreur, `0` avertissement) |

---

## 0. Comment répondre — trois formulations, trois effets

| Vous répondez | Effet |
|---|---|
| **« GO recette v3.0 »** | Le carnet est réputé reçu. Aucune modification. Il devient la version en vigueur sans réserve. |
| **« GO recette v3.0, sous réserve du point n° X : … »** | Je corrige le point, je re-livre la fiche à un indice neuf, je vous présente le `avant / après`. Les 49 autres fichiers ne bougent pas. |
| **« Pas de GO — point n° X : je veux plutôt … »** | Idem, mais la correction porte sur la doctrine, pas sur la forme : je réécris le passage, je passe le carnet en **`v3.1`**, et je consigne la modification en `C-22` (ou suivante) au journal. |

> **Aucun verrou n'est supprimé, aucune brique n'est retirée, quel que soit votre retour.** Une correction `v3.1` ajoute ou précise ; elle ne retire jamais.

---

## A. `B-25` — STABILITÉ GLOBALE (5 points)

### Point n° 1 — La frontière de mission
**Où** : `B-25` §2, interdiction *« Ne dimensionne aucun élément porteur »*.
**Ce que vous devez pouvoir dire OUI à** : « B-25 établit le système qui reprend les efforts horizontaux, mais ne calcule aucune section — les sections restent dans `B-40` à `B-50`. »
**Si non** : *« Point n° 1 : je veux que B-25 aille jusqu'à [préciser : le prédimensionnement des voiles / le ferraillage / autre], parce que … »*

### Point n° 2 — Le système de contreventement est celui que vous construisez
**Où** : §2 méthode 1 et interdiction *« Ne conserve pas un contreventement implicite »*.
**Ce que vous devez pouvoir dire OUI à** : « La fiche m'oblige à nommer le système réel (voiles, portiques, palées, noyaux) et m'interdit de compter les remplissages en maçonnerie comme contreventement sans justification. »
**Si non** : *« Point n° 2 : chez nous, les remplissages sont pris en compte de la façon suivante … »* → je modifie la clause.

### Point n° 3 — Le cheminement des efforts est continu jusqu'aux fondations
**Où** : §2 méthode 2 et critère d'acceptation, 1ᵉʳ point.
**Ce que vous devez pouvoir dire OUI à** : « Chaque niveau doit avoir une reprise identifiée, et toute rupture (voile qui s'arrête, plancher qui ne transmet pas) est un défaut bloquant — pas une note de bas de page. »
**Si non** : *« Point n° 3 : je veux que la rupture soit traitée ainsi … »*

### Point n° 4 — La torsion et la régularité `EC8`
**Où** : §2 méthode 3 et 4 (centres de masse et de rigidité, excentricités, régularité en plan et en élévation).
**Ce que vous devez pouvoir dire OUI à** : « Aucun bâtiment n'est déclaré régulier sans mesure des excentricités, et la méthode d'analyse découle de cette mesure. C'est la pratique de mon BET. »
**Si non** : *« Point n° 4 : la méthode d'analyse que j'utilise est … , il faut la citer explicitement. »*

### Point n° 5 — Joints de dilatation et phases provisoires
**Où** : §2 méthode 5 et 6 (justification `JD` : longueur, température, retrait, tassement, phasage ; stabilité des voiles non liaisonnés).
**Ce que vous devez pouvoir dire OUI à** : « Un joint n'est jamais posé par défaut, il est justifié et coté ; la stabilité en phase provisoire est vérifiée, pas supposée. »
**Si non** : *« Point n° 5 : sur mes chantiers, le phasage provisoire se traite plutôt comme … »*

---

## B. `B-34` — RÉSERVATIONS (5 points)

### Point n° 6 — La frontière de mission
**Où** : `B-34` §2, interdiction *« Ne dimensionne aucun réseau »*.
**Ce que vous devez pouvoir dire OUI à** : « B-34 positionne, vérifie la compatibilité structurale et prescrit le renforcement — il ne dimensionne ni gaine, ni débit, ni équipement. »
**Si non** : *« Point n° 6 : je veux que B-34 aille jusqu'à … »*

### Point n° 7 — Ce qui n'est pas documenté devient un Point d'Arrêt
**Où** : §2 méthode 2 et pièce 2 (réservations non documentées → `PA-xx`, avec responsable et échéance).
**Ce que vous devez pouvoir dire OUI à** : « Une réservation prévisible mais non demandée par un lot est portée en Point d'Arrêt, opposable, avec un responsable nommé et une échéance. Je ne la laisse pas passer en silence. »
**Si non** : *« Point n° 7 : un Point d'Arrêt sur ce type de réservation me pose problème contractuellement, je préfère … »* — **c'est le point le plus sensible** : il engage l'entreprise sur un arrêt de production.

### Point n° 8 — Zones interdites et renforcements
**Où** : §2 méthode 4 et 5 (zone interdite : about de poutre, nœud, zone d'ancrage, membrure tendue ; renforcement renvoyé à la brique de calcul compétente).
**Ce que vous devez pouvoir dire OUI à** : « Une trémie dans un nœud est refusée, une trémie significative déclenche un renforcement calculé par `B-42` ou `B-43` — jamais inventé dans la fiche de synthèse. »
**Si non** : *« Point n° 8 : mes zones interdites sont définies comme … »*

### Point n° 9 — La matrice des interfaces désigne UN responsable de cote
**Où** : §2 méthode 6 et pièce 3 (réservation, lot demandeur, lot réalisateur, bénéficiaire, **responsable de la cote**, échéance).
**Ce que vous devez pouvoir dire OUI à** : « Pour chaque réservation, une seule personne est responsable de la cote. C'est ce qui évite le trou de 40 cm découvert après coulage. »
**Si non** : *« Point n° 9 : la répartition des responsabilités chez nous est … »*

### Point n° 10 — Le contrôle automatique et le plan de réservations
**Où** : §2 méthode 8 et pièce 5 (contrôle de collisions par script, journalisé) + pièce 4 (plan sur fond `B-32`, repères identiques à `B-20`).
**Ce que vous devez pouvoir dire OUI à** : « Le plan de réservations est une pièce du dossier d'exécution, contrôlée par script (collisions avec ferraillage et appuis), et non une annexe facultative. »
**Si non** : *« Point n° 10 : je veux que le plan de réservations soit / ne soit pas une pièce du dossier, parce que … »*

---

## C. Ce que je fais de votre réponse

| Votre réponse | Ce que je produis |
|---|---|
| GO franc | Rien à produire. Le carnet reste en `v3.0`, version en vigueur. |
| GO sous réserve (1 à 3 points) | Les fiches concernées re-livrées à indice neuf + tableau `avant / après` + contrôle `T1..T10` re-passé |
| Pas de GO / refonte d'un point | Le passage réécrit, carnet en **`v3.1`**, entrée `C-22` au journal, `10/10 PASS` re-prouvé |

> **Une seule chose ne changera pas** : les quinze verrous et les six modes validés à l'Étape 2. Une recette porte sur la **doctrine des deux fiches nouvelles**, pas sur l'architecture du carnet que vous avez déjà arbitrée par « GO ».
