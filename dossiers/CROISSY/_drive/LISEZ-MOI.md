# 00 — LISEZ-MOI — LIVRABLES CROISSY-FLORA (état du 20/10/2026)

Ce dossier est la **diffusion unique** des livrables produits pour le projet **CROISSY**. Toutes les pièces portent le **filigrane `PRINCIPE — NE PAS EXÉCUTER`** : ce sont des documents de conception, pas des plans d'exécution.

**Ce qui a changé le 20/10/2026** : `B-25` passe en **indice E** (décision `D-29` consignée : le contreventement est assuré par la maçonnerie existante seule), `B-23` est **livrée en indice A** (exploitation du diagnostic), `B-03` passe en **indice U** (34 décisions). Les pièces antérieures sont à la corbeille : il ne doit circuler qu'un seul indice par note.

---

## 1. COMMENT LIRE CE DOSSIER SANS OUVRIR D'AUTRE PIÈCE

Chaque note commence par un **glossaire des codes** qu'elle emploie : un code (`D-29`, `H-27`, `SF1`…) n'apparaît jamais seul, il est toujours suivi de son objet en clair. Les renvois sont donnés sous la forme « `B-25` § 3 » (brique + paragraphe), jamais par un simple numéro de page.

- **`B-xx`** = brique de la chaîne CARNAC, c'est-à-dire un livrable.
- **`Ind. X`** = indice de révision ; un indice neuf à chaque correction.
- **`D-xx`** = décision tranchée par le maître d'ouvrage (registre `B-03`).
- **`H-xx`** = hypothèse de conception, non encore tranchée (annexe `B-03`).
- **`PA-xx`** = point à lever : information manquante. Aucune valeur n'est inventée à sa place.
- **`ENC`** = existant non qualifié : ouvrage réel mais non sondé, jamais compté porteur sans réserve.
- **`ZONE NON RELEVEE`** = emprise non relevée (plan `D2` feuille 02) : hors de toute hypothèse chiffrée.

Le **glossaire complet** (matériaux, ouvrages neufs `F1` à `F4`, `R1` à `R3`, `P1` à `P3`, `J1`, `SF1`, `Stab1`, `ELU`/`ELS`, `f_k`, `f_vk0`, `TN`, `JD`) est en **§ 4 de `00 — Index`**, et les **points ouverts** en **§ 5 du même index**.

---

## 2. CE QUE DIT LE DOSSIER, EN CLAIR

1. **Le bâtiment tient par ses murs.** Quand le vent pousse sur le pignon, ce sont les murs en maçonnerie existants qui reprennent l'effort, pas les poutres neuves (`D-29`). Conséquence directe : **aucun renfort neuf n'a besoin d'être encastré ni triangulé**, ce qui allège les assemblages (`B-50` à venir).
2. **Aucun joint de dilatation.** Le bâtiment mesure `17,5 m` de long ; l'allongement thermique calculé est de `5,2 mm`. L'absence de joint est **constatée** sur les planches, elle n'est pas « démontrée » et la question n'est plus posée (`D-28`).
3. **Aucune vérification sismique.** Le projet est en **zone de sismicité 1** : les règles parasismiques ne s'appliquent pas (`D-26`). Aucun calcul sismique n'a été conduit, et aucun n'est attendu.
4. **La stabilité en phase provisoire n'est pas de notre mission** (`D-27`) : elle relève de la maîtrise d'œuvre structure de conception (transmission `T-04`). Les séquences de phasage de `B-23` (étaiement, purge, renfort) sont prescrites, mais leur stabilité n'est pas vérifiée ici.
5. **La maçonnerie est prise à `f_k = 1,5 MPa` et `f_vk0 = 0,15 MPa`** (`D-34`). Ces valeurs sont des **hypothèses à confirmer par essais, hors mission**. Si les essais ne confirment pas, une **reprise d'étude chiffrée** est due, et l'hypothèse doit être fournie **avant** démarrage. La clause figure sur la planche et dans les notes de calcul.
6. **Les renforts `R1`, `R2-N/S`, `R3-N/S` et `J1` sont des ouvrages neufs à exécuter sur nos plans** : ils ne sont **jamais** décrits comme « exécutés ». Seules les solives `8×18` relèvent de la réhabilitation existante (`D3` page 18).
7. **Les hypothèses notifiées à l'entreprise ne recevront pas de réponse formelle** (`D-33`) : elles sont en régime **`LECTURE`** — pas d'attente, pas de relance. Les nuages `D-19` restent portés sur les planches pour la traçabilité.

---

## 3. ARBORESCENCE

### `01_Notes` — 10 Google Docs natifs

| Note | Indice | Objet |
|---|---|---|
| `00 — Index` | 20/10/2026 | Point d'entrée : état de la chaîne, tailles, glossaire, points ouverts |
| `B-03 — Registre des décisions et réserves` | **U** | **34 décisions** (`D-01` à `D-24`, `D-26` à `D-34`, dont `D-29`), Articles `P1` à `P8` |
| `B-03 — Annexe hypothèses notifiées` | **H** | 30 hypothèses `H-01` à `H-30`, clause `D-34` mot pour mot |
| `B-20 — Synthèse structurelle & conception GO` | B | Implantation de tous les ouvrages neufs, 3 planches, coupes `A-A` / `B-B` |
| `B-21 — Descente de charges préliminaire` | B | Charges par zone, `F3` **+109 %** et `R1` **+126 %** vs `B-20` |
| `B-22 — Note d'hypothèses de conception` | B | 30 hypothèses, 5 régimes de confirmation |
| `B-23 — Exploitation du diagnostic` | **A** | **9 désordres classés**, 5 zones hors relevé, 9 appuis, séquences `P-1` à `P-7` |
| `B-25 — Stabilité globale, contreventement & joints` | **E** | `D-29` consignée, torsion, régularité, `D-28`. **Aucun point ouvert** |
| `B-32 — Vue nettoyée structurelle RDC & R+1` | D | `0 entité` sur les calques cloisons et isolation |
| `B-40 — Fondations superficielles & implantation PLS` | E | `SF1 80×80×25` (`D-30`), note `D-09` intégrale |

### `02_Plans_PDF` — 10 planches PDF vectorielles

| Planche | Indice |
|---|---|
| B-20 Planche 1 — Synthèse structurelle `PH RDC` | B |
| B-20 Planche 2 — Implantation des fondations `PB RDC / PLS` | B |
| B-20 Planche 3 — `R+1` Charpente, coupes `A-A` / `B-B` et cheminement | B |
| B-40 — Fondations `PLS` : implantation et ferraillage type | E |
| B-32 — Vue nettoyée structurelle RDC | D |
| B-32 — Vue nettoyée structurelle `R+1` | D |
| **B-25 — Contreventement, torsion, régularité** | **E** |
| Preuves de calage B-30, B-31 A, B-31 B | 3 pièces |

### `03_DXF` — 7 fichiers AutoCAD `AC1032` (`audit = 0 erreur`)

Les mêmes sept familles de planches, en DXF : B-20 planches 1 à 3 (ind. B), B-40 (ind. E), B-32 RDC et `R+1` (ind. D), **B-25 (ind. E)**.

---

## 4. CE QUI EST EXCLU DE LA MISSION, ET POURQUOI

| Exclusion | Motif |
|---|---|
| Vérification sismique | Zone de sismicité 1 — `D-26` |
| Stabilité des ouvrages provisoires | Relève de la MOE structure de conception — `D-27`, `T-04` |
| Étude de tassements, recherche de nappe | Hors mission — voir `B-40` § 2 |
| Calculs fins d'exécution (`B-42` à `B-50`) | Séquencés, non démarrés : ils attendent un `GO` explicite |
| Protection incendie dimensionnée | Hors mission — voir `B-22` |
| Plans de coffrage | Aucun DXF de coffrage n'est produit — décision ferme, ne pas redemander |

---

## 5. SUITE DE LA CHAÎNE

La brique suivante est **`B-24` — Existant non sondé** : elle hérite directement des **5 zones hors relevé** identifiées par `B-23` (deux emprises non cotées sur `D2` feuille 02, les combles, les fondations, les planchers). Viendront ensuite `B-43` (plancher haut), `B-42` / `B-44` (charpente), `B-45` (profilés — priorité `F3` et `R1`), `B-40`, `B-46`, `B-50`, puis `B-60` / `B-62`.

Chaque brique ne démarre que sur un **`GO` explicite** portant son nom.
