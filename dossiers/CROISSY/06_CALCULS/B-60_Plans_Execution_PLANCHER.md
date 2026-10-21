# B-60 — PLANS D'EXÉCUTION — type `PLANCHER` — CROISSY-FLORA

> **`D-28` — AUCUN JOINT DE DILATATION.** Les joints de **retrait** du dallage ne sont **pas** des joints de dilatation (NF DTU 13.3).
> **`D-35` — recharge `15 cm` sur le dallage à `100 %`, jamais sur les planchers A et B.**
> **`D-09` — dallage coulé à même les semelles, désolidarisé, jamais sur leur débord.**
> **`D-26` — AUCUNE VÉRIFICATION SISMIQUE.** Termites : `D1 § 01.2.1.9.2`.

| Champ | Valeur |
|---|---|
| **Brique** | `B-60` — Plans d'exécution |
| **`{{type_livrable}}`** | **`PLANCHER`** |
| **Indice / date** | **A** — 21/10/2026 |
| **Mode** | **PARTIEL-DÉCLARÉ** |
| **Régime** | **OUTILLÉ** — `_scripts/b60_plancher.py` (`V13`) |
| **Fond** | `B-32` Ind. D — **report, jamais redessin** |
| **Amont** | `B-43` B · `B-21` C · `B-30` · `B-32` D |
| **Aval** | `B-62` · `B-60` `LINTEAU` / `METAL` / `MACON` |
| **`COMPLET`** | **INTERDIT** : `STR-03` absent, `E-07` non sondé, emprise non remesurée |

**Ce que cette note fait.** Elle implante le **dallage** de `B-43` **sur le RDC BAS** (`B-32`) : hachure d'emprise, joints de retrait `e ≤ 4 500 mm`, désolidarisation `20 mm` (périmètre + `P2`/`P3`/`J1`), coupe du complexe, `D-35` / `D-28` / `D-09`. Rien n'est recalculé.

**Ce qu'elle ne fait pas.** Elle ne fusionne aucun autre type. Elle ne transforme **pas** les solives `8 × 18` ni les `IPE 160` en ouvrages neufs. Elle ne calcule **pas** `E-07`. Elle ne remesure **pas** `111,15 m²` (`H-06`). Dalle BA `20 cm` : **écartée**.

---

## 1. GLOSSAIRE

| Code | Objet |
|---|---|
| Zone **D** | Dallage BA `130 mm` `ST25C` — **ce plan** |
| Zone **A** | Solives `8 × 18` @ `0,50 m` — **existant** |
| Zone **B** | `IPE 160` @ `0,72 m` + `IPE 330` — **existant**, `B-45` |
| Zone **C** | Plancher haut `E-07` — **`PA-03`**, hors planche |
| `JR` | Joint de **retrait** scié — ≠ dilatation |
| `ST25C` | Treillis `Ø7 e150` = `257 mm²/m` — partie haute |

---

## 2. IMPLANTATION

| Élément | Disposition | Statut |
|---|---|---|
| Emprise dallage | Hachure sur fond `B-32` | `111,15 m²` **B-43** — non remesurée |
| Joints de retrait | Grille `e ≤ 4 500 mm`, 2 sens | sciés, `43 mm`, treillis continu |
| Désolidarisation | Périmètre + `P2`/`P3`/`J1` | polystyrène `20 mm` + mastic |
| `P2`/`P3`/`J1` | Traversent le dallage | **sans contact** |
| Zone A / B | Étiquettes existant | pas un coffrage neuf |
| Zone C | Mention `PA-03` | hors planche (`R+1`) |

---

## 3. COMPLEXE (cotes mm)

| Couche | Épaisseur | Note |
|---|---|---|
| Revêtement | `20` | hors lot GO |
| Recharge | `150` | **`D-35`**, `100 %` |
| Dallage C25/30 | `130` | `ST25C` partie haute, `c_nom 30` |
| Polyane | `200 µm` | remonté `100 mm` |
| Fond de forme GNT | `400` | `D2` f. 03 |
| Termites | — | **`D1 § 01.2.1.9.2`** |

Portance `14,2 / 490 kPa = 2,9 %` — **non gouvernante**. Gouverne = retrait + désolidarisation.

---

## 4. DXF — VIEWER ET PURGE

Les DXF d'overlay `B-32` (`B-20`, `B-25`, `B-40`, `B-60` FOND/VERT) pèsent `~2,7 Mo` et portent **454 blocs** AutoCAD dont **4 seulement** sont insérés. Le viewer JS de la fenêtre affiche `Maximum call stack size exceeded` : **ce n'est pas un DXF corrompu** (audit ezdxf **0**, PDF/PNG lisibles).

Ce livrable **purge les 443 blocs non référencés** : `971 000 o`, **11 blocs**, audit **0**. Géométrie `B-32` inchangée. Les DXF antérieurs restent valides en AutoCAD ; un re-export purgé n'est pas fait sans GO d'indice neuf.

---

## 5. AUTO-CONTRÔLE (`V13`)

| Contrôle | Résultat |
|---|---|
| Audit | **0** |
| Calques `PLANCHER-*` | **12 / 12** |
| Entités `PLANCHER-*` | **121** |
| Blocs | **11** (purge −443) |
| Trois formats | DXF · PNG · PDF |
| Filigrane | oui |
| Cloisons / isolation | **0** |

Script : `_scripts/b60_plancher.py`. Planche : `_plans/FLORA_B60_PLANCHER_EXE_IndA.{dxf,pdf,png}`.

---

## 6. RDL

| Livrable | Indice | Source | Calage | Vue | Date |
|---|---|---|---|---|---|
| `PLANCHER EXE` | **A** | `B-43` B | `B-30` | `B-32` D | 21/10/2026 |

**Types `B-60` restants :** `LINTEAU` · `MACON` (`D-37`) · `METAL` (`D-36`) · `CHARPENTE` · `ASSEMBLAGE`. `FOND` et `VERT` livrés.
