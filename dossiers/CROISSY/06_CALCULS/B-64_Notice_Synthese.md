# B-64 — NOTICE DE SYNTHÈSE — CROISSY-FLORA

> **NE PAS EXÉCUTER SANS EXE COTÉ ET VISA.**
> **NE PAS COMMANDER SANS VISA** (`B-62`).
> **Protection au feu adéquate à prévoir (hors lot GO).**
> Livrable établi **sous hypothèses** (`D-19`, `D-34`, `H-xx`) — mode **PARTIEL-DÉCLARÉ**.

| Champ | Valeur |
|---|---|
| **Brique** | `B-64` — Notice de synthèse |
| **Opération** | `CROISSY-FLORA` — EHPAD La Roseraie, pavillon Flora, cabinet paramédical |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** (amont `B-40`…`B-62` tous en PARTIEL-DÉCLARÉ) |
| **Périmètre** | Les **8** types `B-60` + nomenclature `B-62` — **une** notice pour le paquet EXE |
| **`COMPLET`** | **INTERDIT** |
| **Aval** | `B-70` · `B-71` · `B-72` |

---

## 1. PRÉSENTATION DU LIVRABLE

**Objet.** Paquet d'exécution gros œuvre / structure du pavillon Flora : fondations, poteaux BA, dallage, linteaux, coussins, profilés, charpente neuve, assemblages — cotés sur le fond `B-32` Ind. D, jamais redessinés.

**Inclus.** Ouvrages **neufs** `SF1`, `P2`/`P3`/`J1`, dallage zone D, `F1a/b/c`, `R3-N/S`, coussins `D-37`, `F2`/`F3`/`F4`/`R1`/`R2`/`P1`/`Stab1`, `PN`/`DF`/`CF`, connecteurs `A1`–`A6` (portés ou renvoyés).

**Exclu.** Pieux / prédalles / escaliers (`D-38` SO). Solives `8×18` et `IPE 160/330` = **existant**. `E-07` **non chargé**. Contreventement de toiture **absent au `D2`**, non inventé. Feu hors lot. Devis hors CARNAC.

**Pièces du paquet (Ind. A, 21/10/2026) — cohérentes entre elles (relues).**

| Pièce | Fichier | Contrôle |
|---|---|---|
| 8 plans EXE | `FLORA_B60_{FOND,VERT,PLANCHER,LINTEAU,MACON,METAL,CHARPENTE,ASSEMBLAGE}_EXE_IndA` | DXF audit **0** |
| Nomenclature + CSV | `B-62` Ind. A — 62 lignes, 5 écarts **signalés** | `V13` |
| Façonnage BA | `FLORA_B62_FACONNAGE_IndA.{png,pdf}` | `P2` HA12 **non commandable** |
| Notes amont | `B-40` F · `B-42` B · `B-43` B · `B-44` A · `B-45` A · `B-46` A · `B-49` A · `B-50` A | — |
| RDR | `B-03` Ind. AL → **AM** (cette notice) | 38 décisions |

`B-34` (réservations) : **non produite** — `STR-03` absent. Encadrements de trémies **non débitées**.

**Épuisement (`V14`).** 8 notes `B-60` · 8 DXF · `B-62` · `B-22` (30 `H-xx`) · `B-03` · Index §5 · `B-40`…`B-50`. Aucune donnée déclarée absente sans cette lecture.

---

## 2. HYPOTHÈSES RETENUES (`B-22`)

Livrable établi **sous hypothèses à confirmer**. `D-33` : régime `LECTURE` = **aucune relance**.

| `H-xx` | Objet | Statut | Régime | Effet EXE |
|---|---|---|---|---|
| `H-03` | `R1`/`R2`/`R3`/`J1` = **neufs** | À CONFIRMER | LECTURE | Porté sur tous les plans |
| `H-06` | Échelle `D2` = 1/80 · `111,15 m²` = `B-43` | À CONFIRMER | LECTURE | **Jamais scalimètre** |
| `H-10` | Semelles ≥ `60×60` | **CONFIRMÉE** (`D-14`) | — | `SF1` = `80×80` (`D-30`) |
| `H-21` | Déplombage / curage **hors mission** | **CONFIRMÉE** | LECTURE | — |
| `H-22` | Assise `−1,00 m / TN mini` | **CONFIRMÉE** | — | ENC v3 sur FOND |
| `H-23` | `XA1` · `c_nom 30 mm` hors fondation | À CONFIRMER | DOCUMENTAIRE | VERT / dallage |
| `H-25`/`H-26` | `f_k = 1,5` · `f_vk0 = 0,15` MPa | À CONFIRMER | CALCUL → **`D-34`** | Mot pour mot, plan ET note |
| `H-27` | `σ_d` voiles | **CONFIRMÉE** (`0,094`) | CALCUL | — |
| `H-28` | Recharge `15 cm` | À CONFIRMER | CALCUL → **`D-35` 100 %** | Dallage |
| `H-29` | Toiture `0,95 kN/m²` | À CONFIRMER | CALCUL | Charpente |
| `H-24` | Sismique | **ABANDONNÉE** (`D-26`) | — | Aucun calcul sismique |
| Autres `H-01`…`H-20` | Voir `B-22` | 9 LECTURE · 2 RELEVÉ · reste DOCUMENTAIRE | — | Nuages `D-19` |

**`D-34` mot pour mot.** Essais hors mission. Non concluants → reprise **chiffrée**.

---

## 3. POINTS DE PRINCIPE (choix, pas calculs)

| Choix | Pourquoi | Où |
|---|---|---|
| Un type `B-60` = un plan | Fiche : ne pas fusionner | 8 planches |
| Fond `B-32` D reporté, jamais redessiné | Empreinte contractuelle | Tous EXE |
| Contreventement = maçonnerie **seule** | `D-29` | Pas d'encastrement neuf |
| Aucun joint de dilatation | `D-28` constaté | Joints de **retrait** dallage seulement |
| `E-07` non chargé · DF désolidarisées | `PA-03` ouvert | CHARPENTE |
| Remplissage `UPE` `R3` | `D-36` — sinon `τ = 1,40` | METAL, condition de **pose** |
| Coussins `w_b = 300 mm` | `D-37` — verdict inconditionnel | MACON, **pas** un linteau |
| `6 HA12` partout | Espacement max, pas la résistance | VERT |
| Sabots / `A4` **non inventés** | `DOC-09` hors FDC | ASSEMBLAGE / `B-62` |
| `F3` : **aucune charge ajoutée** | Flèche `0,971` de `L/300` | `R-45-1` |

---

## 4. POINTS À LEVER

**Recommandation :** **attendre** pour l'exécution d'ensemble. Commande **partielle** possible (profilés à `L` lue, bois, `ST25C`, `A2`/`A5`) **sous visa**, **hors** les lignes ci-dessous.

### Critiques — bloquent l'EXE ou la commande

| Réf. | Nature | Conséquence | Destinataire | Échéance |
|---|---|---|---|---|
| **Écart `P2` HA12** | ÉQUERRE plan FOND vs DROITE `B-42` | 6 barres **non commandables** | BET (`B-42` C ou `B-60` FOND B) | Avant ferraillage `P2` |
| **`R-50-3` / `A4`** | Capacité `M12` `Stab1` absente (`DOC-09`) | 8 tiges **non commandables** | MOA (fiche) ou essai 1/4 files | Avant pose `Stab1` |
| **`D-19`** | Fouille `P3`/`J1`/`P1` / `SF-T`/`GB` | Semelles types + GB selon constat | Entreprise + BET | **Point d'arrêt** fond de fouille |
| **`PA-03` / `R-43-1`** | `E-07` non sondé | Charpente posée **sans** charger le plancher | MOA / MOE | Avant toute charge sur `E-07` ; **tombe si charpente hors programme** |
| **`R-42-1`** | `H = 2 800 mm` hypothèse | Débits cadres / `L_dev` **indicatifs** | Entreprise (relevé) | Avant façonnage fûts |

### Importants — n'arrêtent pas tout le paquet

| Réf. | Nature | Conséquence | Destinataire |
|---|---|---|---|
| `Stab1` `L` | Portée `IPE 160` inconnue | 4 files `IPE 120` **sans longueur** | Relevé existant |
| Forages `D-36` | Diam. / entraxe absents | Remplissage `R3` sans piquage | `B-60` METAL B — **non inventé** |
| Cadres `SF1` | Qté absente du plan FOND | Nappe `HA8` certaine, cadres non | `B-60` FOND B |
| Sabots `DF`/`PN` | Type non catalogué | Efforts connus (`14,89` / `5,11 kN`), fiche **non inventée** | `DOC-09` ou choix MOE |
| `R-45-1` | `F3` flèche `0,971` | **Aucune charge ajoutée** (y c. C4 sport) | MOE / lots |
| `R-24-B2` | Abouts solives `R1` | Condition de réceptivité du moisage | Constat avant `A2` |

### Suivi — ne bloquent pas l'EXE de ce paquet

| Réf. | Objet | Destinataire |
|---|---|---|
| `T-04` / `D-27` | Stabilité **provisoire** | **MOE structure de conception** — hors notre mission |
| `PA-01` / `PA-02` | Soubassement sous `P2` | Fouille — `SF1 80×80` déjà portée |
| `STR-03` | Trémies | Encadrements non débitées |
| Interfaces | Fissure `F5` · zinguerie `P-4` · doublages | Lots façades / couverture / SO |

**`PA-03`, `R-50-3`, `R-42-1`, `R-45-1` : cette notice ne les clôt pas.**

---

## 5. RÉSERVES ET LIMITES

- **Existant non sondé** (`B-24`) : `E-04` supprimés, `E-05`/`E-06`/`E-07` hors calcul, `IPE 330` existante non calculée.
- **`D-23`** : écart d'aplomb `R+1`/`RDC` `10,1 cm` = **donnée**, non corrigée.
- **`D-15`** tassements hors mission · **`D-16`** nappe absente (venue d'eau = arrêt).
- **`D-26`** aucune sismique · **`D-28`** aucun joint de dilatation.
- **`H-20` vs `D-27` :** `D-27` **gouverne** — stabilité de phase = MOE (`T-04`), pas cette notice.
- Nomenclature **non exécutable en l'état** (`B-62` : 5 écarts, 7 en attente).
- **Protection au feu adéquate à prévoir (hors lot GO).**

---

## 6. VISAS REQUIS

| Visa | Qui | Nature |
|---|---|---|
| Exécution structure | **Bureau de contrôle** | Visa d'exécution sur les 8 planches + `B-62` |
| Conception / cohérence | **MOE structure de conception** | Visa de conception ; `T-04` reste à sa charge |
| Production | **BET d'exécution** (rédacteur) | Auto-contrôle `B-70` aval — **cette notice n'est pas le visa** |
| Hypothèses `D-34` / fouille `D-19` | **MOA** (silence `DEC-06` = 2 j = acceptation) | Contradiction ; essais hors mission |

Aucun autre visa n'est requis par ce paquet. Un visa d'indice antérieur **ne vaut pas** pour l'Ind. A.

**NE PAS EXÉCUTER SANS EXE COTÉ ET VISA.**

---

## 7. INDIÇAGE ET SUPERSESSION

| Livrable | Indice en vigueur | Supersédé |
|---|---|---|
| **Cette notice `B-64`** | **A** — 21/10/2026 | **Aucun** (création) |
| 8 plans `B-60` | **A** | Aucun |
| Nomenclature `B-62` | **A** | Aucun |
| `B-03` | **AM** (cette passe) | AL, AK, … |

Ce livrable **ne remplace aucun indice `B-64` antérieur** : il n'y en a pas.

**Suite :** `B-70` — auto-contrôle déclaré de synthèse. `B-41`/`B-47`/`B-48` **SANS OBJET** (`D-38`).
