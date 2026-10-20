# CROISSY-FLORA — INDEX DE L'ESPACE DE TRAVAIL

> **Mis à jour le 20/10/2026** — **`B-25` en indice E** : `D-29` consignée (le contreventement est assuré par la maçonnerie existante seule ; aucun renfort encastré ni triangulé) ; `B-25` ne porte plus aucun point ouvert. **`B-23` livrée en indice A** : les 9 désordres du diagnostic sont classés et les séquences de phasage `P-1` à `P-7` établies. **`B-03` en indice U** : 34 décisions.

---

## 1. RÉPONSE DIRECTE — CE QUI EXISTE ET CE QUI RESTE À PRODUIRE

**À la date du 20/10/2026 : 21 notes documentaires CARNAC, 6 preuves de calage/superposition, et 21 fichiers de plans (`7 DXF + 7 PDF + 7 PNG = 27 Mo`) — tous purgés à 100 % des cloisons et complexes d'isolation (`0 entité` sur `020_cloi` / `020_cloisons`).**

| Ce qui est produit et synchronisé sur Google Drive (`LIVRABLES_ARENA`) | Emplacement workspace |
|---|---|
| Cadrage `B-00 → B-04` (dont `B-03` **Ind. U**, 34 décisions + Articles `P1 à P8`), analyse `B-10 → B-15` | `01_CADRAGE/` · `02_ANALYSE/` |
| Calage `B-30 Ind. C`, superposition `B-31 Ind. C`, **Vues nettoyées structurelles `B-32 Ind. D`** (zéro cloison, zéro isolation) | `03_CALAGE/` + `_plans/` + `_calage/` |
| **Synthèse structurelle & prédimensionnement `B-20 Ind. B`** : 3 planches A3 Paysage (`PH RDC`, `PB RDC / PLS`, `R+1 Charpente + Coupes A-A / B-B + Cheminement`) | `02_CONCEPTION/` + `_plans/` |
| **Fondations superficielles & implantation `B-40 Ind. E`** : plan combiné `PLS` + détails d'exécution `SF1` (`60×60×30 BA`, `HA8 e150`, gros béton `D-09`) | `06_CALCULS/` + `_plans/` |
| **Stabilité globale `B-25 Ind. E`** : contreventement par la maçonnerie existante seule (`D-29`), torsion, régularité, joints + planche `FLORA_B25_CONTREVENTEMENT_IndE`. Sismique et stabilité provisoire **hors mission** (`D-26`, `D-27`) · **`D-28`** : aucun joint, constaté | `02_CONCEPTION/` + `_plans/` + `_rendus/` |

| Ce qui reste séquencé pour la suite de la chaîne CARNAC | Motif |
|---|---|
| **`B-24`** (Existant non sondé) | Brique suivante de Phase 3 — hérite des **5 zones hors relevé** identifiées par `B-23` ; prête à démarrer sur `GO` |
| **`B-42` (Poteaux & jambages BA : `P2, P3, J1`) · `B-44` (Charpente) · `B-45` (Profilés métalliques `F1–F4, R1–R3, P1, Stab1`) · `B-46` (Maçonnerie existante) · `B-50` (Assemblages & ancrages)** | Calculs fins d'exécution EC2 / EC3 / EC5 séquencés après validation de `B-20 Ind. B` |
| **`B-60 / B-62`** (Plans d'exécution cotés coffrage/ferraillage & nomenclatures — `D-17`) | Séquencés après les calculs d'exécution `B-40 à B-50` |

---

## 2. CHAÎNE DES BRIQUES — ÉTAT AU 20/10/2026

| Brique | Fichier | Indice | Date | État |
|---|---|---|---|---|
| **B-00** | `01_CADRAGE/B-00_Inventaire.md` | **C** | 19/10/2026 | ✅ Livrée — corpus D1 à D5 inventorié |
| **B-01** | `01_CADRAGE/B-01_MPD.md` | **B** | 19/10/2026 | ✅ Livrée — validée par D-05 |
| **B-02** | `01_CADRAGE/B-02_FDC.md` | **F** | 19/10/2026 | ✅ Livrée — prescription `ENC v3` (12 alinéas) |
| **B-03** | `01_CADRAGE/B-03_RDR.md` | **U** | **20/10/2026** | ✅ **34 décisions (`D-01` à `D-24`, `D-26` à `D-34` + `D-29` — `D-25` inexistant) · `D-28` joints · `D-30` `SF1` 80×80 · `D-31` cat. C4 · `D-32` 2,50 kN/m²** |
| **B-03 annexe** | `01_CADRAGE/B-03_Annexe_Hypotheses.md` | **H** | **20/10/2026** | ✅ **30 hypothèses actives** (`H-01` à `H-30`) — `H-28` à `H-30` **notifiées**, `H-31` promue `D-31` |
| **B-04** | `01_CADRAGE/B-04_PTD.md` | **C** | 19/10/2026 | ✅ Plan de travail dégradé actif |
| **B-10 à B-15** | `02_ANALYSE/B-10..B-15*.md` | **A / B** | 19/10/2026 | ✅ Phase 1 Analyse complète et close |
| **B-30** | `03_CALAGE/B-30_Calage.md` | **C** | 19/10/2026 | ✅ Calage `1,7 mm` · surfaces RDC `111,15 m²` / R+1 `106,92 m²` · `0,00 RELATIF` (`D-21`) |
| **B-31** | `03_CALAGE/B-31_Preuve_Superposition.md` | **C** | 19/10/2026 | ✅ Fidélité `0,6 mm` · translation `R+1 → RDC` (`D-23`) |
| **B-32** | `03_CALAGE/B-32_Vue_Nettoyee.md` | **D** | **20/10/2026** | ✅ **CONFORME** — cloisons & isolation 100 % supprimées (`0 entité` sur `020_cloi`/`020_cloisons`), audit `0 erreur` |
| **B-20** | `02_CONCEPTION/B-20_Conception_GO.md` | **B** | **20/10/2026** | ✅ **CONFORME** — synthèse intégrale `D1+D2+D3+D4+D5`, calage vectoriel `1/80` (`21,0 mm`), 100 % des ouvrages implantés, 3 planches + 2 coupes `A-A / B-B` |
| **B-40** | `06_CALCULS/B-40_Fondations.md` | **E** | **20/10/2026** | ✅ **CONFORME EN PARTIEL-DÉCLARÉ** — plan combiné `PLS` implanté + ferraillage `HA8 e150` + note `D-09` + justification `D-24 / R-36` |
| **B-21** | `02_CONCEPTION/B-21_DDC_Preliminaire.md` | **B** | **20/10/2026** | ✅ **CONFORME 7/7** — `1 766 kN` ELU sur le R+1 · `F3` **+109 %** et `R1` **+126 %** vs `B-20` · **`D-30` `SF1` 80 × 80** · `H-27` vérifiée |
| **B-22** | `02_CONCEPTION/B-22_Note_Hypotheses.md` | **B** | **20/10/2026** | ✅ **CONFORME 6/6** — **30 hypothèses** · **`D-33`** : 9 en régime `LECTURE` (aucune relance) · `H-27` vérifiée par `B-21` · famille Matériaux vide (assumée) |
| **B-23** | `02_CONCEPTION/B-23_Exploitation_Diagnostic.md` | **A** | **20/10/2026** | ✅ **CONFORME 6/6** — 9 désordres classés (3 renforcement, 1 sous condition, 3 phasage, 3 coordination lot, 1 sans impact) · 5 zones hors relevé · 9 appuis · séquences `P-2` purge avant renfort et `P-3` flambement avant charge **nouvelles** |
| **B-25** | `02_CONCEPTION/B-25_Stabilite_Globale.md` | **E** | **20/10/2026** | ✅ **CONFORME 6/6 applicables** — contreventement = maçonnerie seule, `ΣK = 1,21/1,64 GN/m`, torsion `τ/f_vk ≤ 0,028`, aucun joint. **Sismique retirée (`D-26`)** · **stabilité provisoire retirée, MOE (`D-27`)** |

---

## 3. LIVRABLES PRINCIPAUX RÉVISÉS LE 20/10/2026 (TAILLES VÉRIFIÉES)

### 3.1 Notes principales

| Fichier | Taille exacte | Contenu |
|---|---|---|
| `01_CADRAGE/B-03_RDR.md` | `68 858 o · 459 l.` | Registre vivant **Ind. U** : `D-01` à `D-34` + `D-29`, Articles `P1–P8`, registre des nuages `D-19` |
| `01_CADRAGE/B-03_Annexe_Hypotheses.md` | `37 653 o · 252 l.` | **Annexe hypothèses notifiées Ind. H** : 30 hypothèses, clause `D-34` (maçonnerie) mot pour mot, `D-33` régime `LECTURE` |
| `02_CONCEPTION/B-20_Conception_GO.md` | `30 101 o · 206 l.` | Synthèse structurelle & prédimensionnement GO Ind. B (rectificatifs + 13 postes + rattachement `B-11`) |
| `06_CALCULS/B-40_Fondations.md` | `10 836 o · 108 l.` | Note de calcul & implantation « PLS » des fondations Ind. E (note `D-09` en tête) |
| `03_CALAGE/B-32_Vue_Nettoyee.md` | `6 412 o · 73 l.` | Rapport de nettoyage structurel strict Ind. D (purge totale cloisons & isolation) |
| `02_CONCEPTION/B-23_Exploitation_Diagnostic.md` | `23 128 o · 198 l.` | **Exploitation du diagnostic Ind. A** : 4 tableaux, 9 désordres, 5 zones hors relevé, 7 séquences de phasage |
| `02_CONCEPTION/B-22_Note_Hypotheses.md` | `31 676 o · 279 l.` | **Note d'hypothèses Ind. B** : 30 hypothèses, 5 régimes de confirmation (`D-33`), historique des révisions |
| `02_CONCEPTION/B-21_DDC_Preliminaire.md` | `32 812 o · 410 l.` | DDC PRÉLIMINAIRE — CONCEPTION **Ind. B** : 5 tableaux, 8 porteurs surfaciques, 14 porteurs linéaires, contrôle `B-20`, `D-30` |
| `02_CONCEPTION/B-25_Stabilite_Globale.md` | `40 749 o · 399 l.` | Note de stabilité globale **Ind. E** (contreventement, torsion, régularité, joints — `D-29` consignée) — exclusions `D-26` (sismique) et `D-27` (stabilité provisoire → MOE) — journal `_rendus/b25_stabilite.txt` |

### 3.2 Planches graphiques actives dans `_plans/` (21 fichiers — 27 Mo — audit `0 erreur` sur les 7 DXF)

| Famille | DXF (AutoCAD AC1032) | PDF vectoriel | PNG (200–220 dpi) |
|---|---|---|---|
| **B-20 Planche 1 — Synthèse PH RDC** | `FLORA_B20_PH-RDC_PRINCIPE-STRUCTUREL_IndB.dxf` (`2 790 594 o`) | `922 524 o` | `922 258 o` |
| **B-20 Planche 2 — Implantation Fondations PB RDC (`PLS`)** | `FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB.dxf` (`2 767 496 o`) | `946 375 o` | `907 137 o` |
| **B-20 Planche 3 — R+1 Charpente, Coupes `A-A / B-B` & Cheminement** | `FLORA_B20_CHARPENTE_COUPES_SCHEMA_IndB.dxf` (`2 729 761 o`) | `612 780 o` | `624 524 o` |
| **B-40 Ind. E — Plan combiné `PLS` + Ferraillage Type Semelles** | `FLORA_FONDATIONS_TYPE_IndE.dxf` (`2 770 072 o`) | `523 324 o` | `648 530 o` |
| **B-32 Ind. D — Vue nettoyée structurelle RDC** | `FLORA_RDC_VUE-NETTOYEE_IndD.dxf` (`2 719 320 o`) | `80 712 o` | `280 106 o` |
| **B-32 Ind. D — Vue nettoyée structurelle R+1** | `FLORA_R1_VUE-NETTOYEE_IndD.dxf` (`2 672 677 o`) | `78 372 o` | `278 171 o` |
| **B-25 Ind. E — Contreventement, torsion, régularité (`D-29`, `D-28`)** | `FLORA_B25_CONTREVENTEMENT_IndE.dxf` (`2 760 613 o`) | `901 519 o` | `1 075 802 o` |

---

## 4. GLOSSAIRE DES CODES (pour lire ce dossier sans ouvrir une autre pièce)

| Code | Objet en clair |
|---|---|
| `B-xx` | Brique de la chaîne CARNAC (un livrable = une brique). Ex. `B-23` = exploitation du diagnostic, `B-25` = stabilité globale. |
| **Ind. A → V** | Indice de révision du livrable. Un indice neuf à chaque correction ; l'indice antérieur est retiré de la diffusion. |
| `D-xx` | Décision tranchée par le maître d'ouvrage, enregistrée au registre `B-03`. Ex. `D-29` = contreventement assuré par la maçonnerie existante. |
| `H-xx` | Hypothèse de conception, enregistrée à l'annexe `B-03` ; devient `D-xx` quand elle est tranchée. |
| `PA-xx` | Point à lever : information manquante, à obtenir du maître d'ouvrage ou d'un tiers. **Aucune valeur n'est inventée à la place.** |
| `T-xx` | Transmission à un tiers (ici `T-04` → maîtrise d'œuvre structure de conception). |
| `ENC` | Existant non qualifié : ouvrage réel mais non sondé ; il n'est **jamais** compté comme porteur sans réserve. |
| `ZONE NON RELEVEE` | Emprise du bâtiment dont la géométrie n'a pas été relevée (`D2` feuille 02) : hors de toute hypothèse chiffrée. |
| Nuage `D-19` | Nuage de révision apposé sur une planche pour marquer une hypothèse à valider par l'entreprise. |
| `RDR` | Registre des décisions et réserves (`B-03`). |
| `DDC` | Descente de charges (`B-21`). |
| `PLS` | Plan de localisation des semelles (implantation des fondations, `B-40`). |
| `F1a/F1b/F1c`, `F2`, `F3`, `F4` | Frangements acier neufs sous charpente (`2×HEA 200`, `HEB 200`, `HEB 160`, `IPE 200`). |
| `R1`, `R2-N/S`, `R3-N/S` | Renforts de plancher neufs (`2×UPE 200`, `HEB 160`, `UPE 200`) — **ouvrages neufs à exécuter**, jamais « exécutés ». |
| `P1-N/S`, `P2`, `P3` | Poteaux neufs : `P1` tube carré `140×140`, `P2` BA `15×25`, `P3` BA `50×40`. |
| `J1` | Jambage BA `24×50` (ouvrage neuf). |
| `SF1` | Semelle isolée type `80×80×25` BA (`D-30`). |
| `Stab1` | Entretoise de stabilisation dans les voutains briques (4 files). |
| `ELU` / `ELS` | États limites ultimes / de service (Eurocodes). |
| `f_k` / `f_vk0` | Résistance caractéristique de la maçonnerie en compression / en cisaillement initial (`D-34` : `1,5 MPa` / `0,15 MPa`, **à confirmer par essais hors mission**). |
| `TN` | Terrain naturel. Arase de référence : `−1,00 m / TN MINIMUM` (`D-09`). |
| `JD` | Joint de dilatation. **Aucun joint dans ce projet** (`D-28`) : l'absence est constatée, jamais démontrée, et la question n'est jamais reposée. |
| `0,00 RELATIF` | Niveau de référence altimétrique du projet (`D-21`), origine `P1`. |

---

## 5. POINTS OUVERTS (à la date du 20/10/2026)

| Réf. | Objet | Statut |
|---|---|---|
| `T-04` | Stabilité des ouvrages provisoires (étaiement, phases) | Transmise à la MOE structure de conception (`D-27`) |
| `PA-01` / `PA-02` | Reconnaissance du soubassement sous `P2` | En attente — aucune valeur de portance inventée ; `SF1 80×80` retenue sur l'hypothèse déclarée |
| Interface façades | Qui traite la fissuration `F5` relevée au pignon ? | À trancher (lot façades) |
| Interface zinguerie | Reprise des `P-4` (zinguerie avant pose) | À trancher (lot couverture) |
| Interface second œuvre | Séquence de dépose/repose des doublages en zone de renfort | À trancher (lot second œuvre) |
