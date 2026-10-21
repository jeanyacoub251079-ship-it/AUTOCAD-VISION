# A1 — ADDENDUM v3.0.1 — GARDE-FOUS DE LECTURE, DE DEMANDE ET DE PRÉSENTATION

> Version : **3.0.1** (21/10/2026) — complément de CARNAC v3.0, **sans suppression de verrou**.
> Origine : méta-amélioration `T-03` après l'affaire CROISSY-FLORA (frictions de session).
> Classement : **GÉNÉRALE** — s'applique à toutes les affaires futures.
> Non-régression : `V1`–`V15` inchangés. Aucune brique supprimée. Aucun numéro réattribué.

Cet addendum corrige six dérives observées : demander ce que le programme des travaux ne prescrit pas ; oublier un fait déjà dans le dossier ; relancer le maître d'ouvrage sur des prestations **non adressées** au BET d'exécution ; vérifier le séisme en zone 1 ; endosser la stabilité provisoire de l'existant ; produire des plans illisibles (dump DXF + murs de codes).

________________

## 1. LECTURE ADRESSÉE DU DCE (`DEC-08`)

### 1.1 Le DCE n'est pas adressé au BET d'exécution

Un dossier de consultation / dossier marché est **adressé à l'entreprise**. Le CCTP prescrit des prestations **à la charge de l'entreprise** (désamiantage, déplombage, cantonnements, phasage, PGC, PPSPS, etc.).

Le BET d'exécution **lit** le CCTP. Il **retient** les informations qui concernent ses études (charges, matériaux, ouvrages, interfaces). Il **n'attend pas** de réponse formelle sur une prestation qui ne lui est pas adressée. L'absence de PV, d'arrêté, de plan de cantonnement ou de mode opératoire entreprise **n'est pas un verrou** de nos notes.

### 1.2 Programme des travaux = CCTP + plans archi + plans structure (EVEN / BET MOE)

Le diagnostic décrit un état. **Le programme des travaux** est ce que le CCTP et les plans **prescrivent de faire**.

Règle : **on ne demande un document, un essai ou un relevé que s'il est nécessaire à un ouvrage que le programme nous charge de concevoir ou de vérifier.**

| Situation | Traitement |
|---|---|
| CCTP + archi + EVEN **ne prescrivent aucune intervention sur le bois** | Interdit de demander l'arrêté termites, l'état des abouts, un PV de traitement, un classement biologique. Le diagnostic a déjà conclu ; le programme a déjà tranché. |
| Renforts existants **non repris** par nos ouvrages | Interdit de demander les PV de réception de ces renforts. |
| Désamiantage, déplombage, cantonnements, PGC | Constat d'interface en `B-10` (tableau « non adressé »). **Aucune** demande `T-04`. **Aucune** réserve de nos notes. |
| Protection termites **déjà prescrite** au CCTP (ex. sous dallage) | C'est une **prescription d'entreprise**, reportée en note comme contrainte de pose — pas une donnée manquante. |

### 1.3 Ce qui reste une vraie demande

Une demande `T-04` n'est légitime que si **les trois** conditions sont réunies :

1. la donnée manque **après épuisement** du corpus (`V14`) ;
2. elle est **nécessaire** à un calcul ou à un plan **de notre mission** ;
3. le destinataire est **celui à qui la pièce est adressée** (MOE conception, MOA, BET MOE) — jamais « l'entreprise » pour un document qu'elle n'a pas à nous remettre.

Une demande qui échoue au test 1, 2 ou 3 **n'est pas rédigée**. Elle n'entre pas au RDR comme point ouvert.

________________

## 2. CARNET DES FAITS (`DEC-09`) — ANTI-OUBLI

`V14` interdit de déclarer une donnée absente sans épuisement. Il n'interdisait pas **d'oublier une donnée présente**.

Dès `B-00` / `B-10` / `B-11`, l'assistant constitue un **carnet des faits** — tableau unique, sourcé, **consommé** par toutes les briques aval :

| Fait | Exemples | Source |
|---|---|---|
| Nature des planchers par zone | bois `8×18` / hourdis + `IPE` / dallage / non sondé | Diagnostic, plans EVEN, CCTP |
| Niveaux et usages | PB, PH, R+1, cabinet, locaux | Archi, CCTP |
| Matériaux prescrits | `S275`, `C25/30`, `C24` | EVEN, CCTP |
| Ouvrages neufs vs existants | liste `F1`…`PN` vs `E-xx` | EVEN |
| Exclusions de mission | feu, fluides, amiante, curage | CCTP + `B-00` |

**Non-conformité** : une brique aval qui redemande, ignore ou « découvre » un fait déjà porté au carnet. Le carnet est une entrée bloquante de `B-20` à `B-64`.

________________

## 3. SISMIQUE ZONE 1 ET STABILITÉ PROVISOIRE

### 3.1 Zone de sismicité 1 (très faible) — Île-de-France type

Arrêté du 22 octobre 2010 : **aucune règle parasismique** n'est applicable en zone 1. `B-25` **ne produit aucune** vérification sismique, **ne demande aucune** catégorie d'importance pour un spectre, **n'ouvre aucun** `H-xx` sismique.

La mention unique autorisée : « Zone 1 — vérification sismique **sans objet**. »

### 3.2 Stabilité provisoire d'un bâtiment existant

La vérification du contreventement **en phase provisoire** (étaiement, dépose de refend, ouverture de baie, stabilité du bâtiment occupé) **incombe à la maîtrise d'œuvre structure de conception**.

Le BET d'exécution **signale** l'interface (phasage, charge de chantier sur un plancher). Il **ne calcule pas** la stabilité provisoire de l'existant. Il **ne relance pas** la MOA. Destinataire unique si une alerte est utile : **MOE conception**, en information — pas en `T-04` bloquant.

________________

## 4. PRÉSENTATION DES PLANS (`LIV-06`)

### 4.1 Ce qu'un plan d'exécution doit être

Un plan se lit **debout, sur chantier**, en dix secondes : l'ouvrage, les cotes, le matériau.

| Autorisé et attendu | Interdit |
|---|---|
| Fond **blanc** | Dump du DXF `B-32` complet (calques archi, textes, blocs) |
| Existant en **gris léger** (empreinte extraite, pas redessinée) | Murs de codes `D-xx` / `R-xx` / `H-xx` / `ENC` 12 alinéas |
| Ouvrages neufs en **couleur simple** (un type = une couleur) | Croquis de coupe **flottant**, sans plan d'implantation du niveau |
| Cotes en mm (plan) et m 3 déc. (niveaux) | Cartouche-registre (historique d'indices, glossaire CARNAC) |
| Titre **trois lignes** : qui / quoi / indice + matériau | Filigrane qui masque la géométrie |
| Une coupe type **hachurée**, barres dessinées | Fusion de plusieurs types sur un plan EXE |
| Nomenclature graphique **courte** (repère, section, qté) | |

**Report, jamais redessin** (`B-60`) signifie : les **coordonnées** et les **dimensions** viennent de `B-32` / `B-20` / de la note. Cela **n'autorise pas** à coller le fichier `B-32` entier comme fond. L'empreinte est **extraite** (murs porteurs, baies, trémie) et redessinée en trait fin gris.

### 4.2 Implantation obligatoire

Chaque plan `B-60` d'un type comporte **obligatoirement** :

1. **le plan d'implantation du niveau concerné** (RDC BAS, PH, R+1) avec **tous les ouvrages de ce type** figurés à leur place ;
2. **au moins une coupe** ou un détail type à 1/20 ou 1/10.

Un dallage représenté **seulement** en coupe, sans hachure d'emprise sur le RDC BAS, est **refusé**. Un linteau représenté **seulement** en détail, sans baie sur le plan, est **refusé**.

Un type = un plan EXE (**inchangé**). La vue qui montre **tous** les ouvrages neufs ensemble n'est **pas** un plan EXE fusionné : c'est une **vue d'ensemble de lecture** (pièce facultative après le dernier type, filigrane `LECTURE — NE PAS EXÉCUTER`). Elle répond à la question « où est-ce, dans le bâtiment ? ».

### 4.3 Codes CARNAC : la note, pas le dessin

| Sur le plan | Dans la note |
|---|---|
| Repères d'ouvrage (`SF1`, `P2`, `F3`) | Codes `D-xx`, `R-xx`, `H-xx`, `PA-xx` |
| Cotes, niveaux, sections | Historique d'indice, « ce que la brique ne fait pas » |
| **Un** encadré `ENC` de **5 lignes maximum** | Prescription intégrale |
| **Un** nuage `H-xx` ou `D-19` **par zone**, pastille courte | Tableau des hypothèses |
| Filigrane **une ligne** : `NE PAS EXÉCUTER SANS VISA` | Visas, destinataires, échéances |

`A_Conventions` §8.3 et §8.4 (nuage `H-xx`, `ENC` mot pour mot sur le plan) sont **restreints** par le présent addendum : le mot-pour-mot vit **en note** ; le plan porte l'information **opposable et lisible**.

________________

## 5. PRÉSENTATION DES NOTES DE CALCUL (`LIV-07`)

Toute note `B-40` à `B-50` et la notice `B-64` s'ouvrent dans cet ordre, **sans glossaire CARNAC en tête** :

| § | Contenu |
|---|---|
| En-tête | Opération, adresse, indice, date, matériau, mention visa — **cinq lignes** |
| **§0** | **Hypothèses à valider** — tableau `n° / objet / valeur / source / statut` |
| **§1** | Matériaux et normes |
| **§2** | Charges (couche par couche) |
| **§3** | Géométrie et implantation |
| **§4** | Descente de charges |
| **§5** | Vérifications (formule littérale → numérique → taux → verdict) |
| **§6** | Points à lever (critiques / importants / suivi) |
| **Annexe** | Traçabilité CARNAC (`D-xx`, `H-xx`, `PA-xx`, scripts) — **après** le calcul |

Interdit en tête de note : « ce que cette brique fait / ne fait pas », historique d'indices AL/AK/AJ, glossaire de vingt codes. Ces éléments, s'ils sont utiles, vont en **annexe**.

`B-64` reste 2–4 pages. Elle ne recopie pas la note. Elle ne noie pas le lecteur sous les codes.

________________

## 6. FICHES TOUCHÉES

| Fiche | Nature du complément |
|---|---|
| `00_MASTER.md` | §1.5 lecture adressée · §1.6 carnet des faits · §1.7 présentation |
| `B-00` | Étape carnet des faits |
| `B-10` | Tableau 5 « prestations lues, non adressées » |
| `T-04` | Test des trois conditions avant toute demande |
| `B-25` | Zone 1 = SO sismique · stab. prov. = MOE conception |
| `B-60` | Implantation obligatoire · fond simplifié · codes hors dessin |
| `B-64` | Ordre §0 / charges / vérif |
| `A_Conventions` | `LIV-06` / `LIV-07` · ENC court |

________________

## 7. CE QUE CET ADDENDUM NE CHANGE PAS

- Un type `B-60` = un plan EXE.
- Report des **cotes**, jamais invention d'empreinte.
- `V14` épuisement, `V15` continuité mécanique.
- `D-26` (aucune sismique), `D-27` (stab. prov. MOE), `D-28` (aucun joint de dilatation) — déjà décidés ; le présent texte les **généralise**.
- Zéro placeholder, zéro devis, zéro protection incendie dimensionnée.
