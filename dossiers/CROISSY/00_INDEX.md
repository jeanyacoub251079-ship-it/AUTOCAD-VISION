# CROISSY-FLORA — INDEX DE L'ESPACE DE TRAVAIL

> **Mis à jour le 20/10/2026** — **`B-25` en indice B** : `D-26` (aucune vérification sismique, zone 1) et `D-27` (stabilité en phase provisoire → MOE structure de conception) ; puis validation de la décision **D-25 (Articles P1 à P8 — Synthèse structurelle du dossier)** et à la refonte intégrale des vues nettoyées (`B-32 Ind. D`), de la synthèse structurelle (`B-20 Ind. B`) et de l'implantation des fondations (`B-40 Ind. E`).

---

## 1. RÉPONSE DIRECTE — CE QUI EXISTE ET CE QUI RESTE À PRODUIRE

**À la date du 20/10/2026 : 18 notes documentaires CARNAC, 6 preuves de calage/superposition, et 18 fichiers de plans (`6 DXF + 6 PDF + 6 PNG = 22,2 Mo`) — tous purgés à 100 % des cloisons et complexes d'isolation (`0 entité` sur `020_cloi` / `020_cloisons`).**

| Ce qui est produit et synchronisé sur Google Drive (`LIVRABLES_ARENA`) | Emplacement workspace |
|---|---|
| Cadrage `B-00 → B-04` (dont `B-03` **Ind. P**, 25 décisions + Articles `P1 à P8`), analyse `B-10 → B-15` | `01_CADRAGE/` · `02_ANALYSE/` |
| Calage `B-30 Ind. C`, superposition `B-31 Ind. C`, **Vues nettoyées structurelles `B-32 Ind. D`** (zéro cloison, zéro isolation) | `03_CALAGE/` + `_plans/` + `_calage/` |
| **Synthèse structurelle & prédimensionnement `B-20 Ind. B`** : 3 planches A3 Paysage (`PH RDC`, `PB RDC / PLS`, `R+1 Charpente + Coupes A-A / B-B + Cheminement`) | `02_CONCEPTION/` + `_plans/` |
| **Fondations superficielles & implantation `B-40 Ind. E`** : plan combiné `PLS` + détails d'exécution `SF1` (`60×60×30 BA`, `HA8 e150`, gros béton `D-09`) | `06_CALCULS/` + `_plans/` |
| **Stabilité globale `B-25 Ind. B`** : système de contreventement, torsion, régularité, joints + planche `FLORA_B25_CONTREVENTEMENT_IndB`. Sismique et stabilité provisoire **hors mission** (`D-26`, `D-27`) | `02_CONCEPTION/` + `_plans/` + `_rendus/` |

| Ce qui reste séquencé pour la suite de la chaîne CARNAC | Motif |
|---|---|
| **`B-21 / B-22`** (DDC préliminaire globale & Note d'hypothèses consolidée `D-19`) | Briques suivantes de Phase 2 — prêtes à démarrer sur `GO` |
| **`B-42` (Poteaux & jambages BA : `P2, P3, J1`) · `B-44` (Charpente) · `B-45` (Profilés métalliques `F1–F4, R1–R3, P1, Stab1`) · `B-46` (Maçonnerie existante) · `B-50` (Assemblages & ancrages)** | Calculs fins d'exécution EC2 / EC3 / EC5 séquencés après validation de `B-20 Ind. B` |
| **`B-60 / B-62`** (Plans d'exécution cotés coffrage/ferraillage & nomenclatures — `D-17`) | Séquencés après les calculs d'exécution `B-40 à B-50` |

---

## 2. CHAÎNE DES BRIQUES — ÉTAT AU 20/10/2026

| Brique | Fichier | Indice | Date | État |
|---|---|---|---|---|
| **B-00** | `01_CADRAGE/B-00_Inventaire.md` | **C** | 19/10/2026 | ✅ Livrée — corpus D1 à D5 inventorié |
| **B-01** | `01_CADRAGE/B-01_MPD.md` | **B** | 19/10/2026 | ✅ Livrée — validée par D-05 |
| **B-02** | `01_CADRAGE/B-02_FDC.md` | **F** | 19/10/2026 | ✅ Livrée — prescription `ENC v3` (12 alinéas) |
| **B-03** | `01_CADRAGE/B-03_RDR.md` | **P** | **20/10/2026** | ✅ **25 décisions (`D-01` à `D-25`) · Articles `P1 à P8` · Registre des nuages `D-19`** |
| **B-03 annexe** | `01_CADRAGE/B-03_Annexe_Hypotheses.md` | **B** | 19/10/2026 | ✅ 24 hypothèses validées (`H-01` à `H-24`) |
| **B-04** | `01_CADRAGE/B-04_PTD.md` | **C** | 19/10/2026 | ✅ Plan de travail dégradé actif |
| **B-10 à B-15** | `02_ANALYSE/B-10..B-15*.md` | **A / B** | 19/10/2026 | ✅ Phase 1 Analyse complète et close |
| **B-30** | `03_CALAGE/B-30_Calage.md` | **C** | 19/10/2026 | ✅ Calage `1,7 mm` · surfaces RDC `111,15 m²` / R+1 `106,92 m²` · `0,00 RELATIF` (`D-21`) |
| **B-31** | `03_CALAGE/B-31_Preuve_Superposition.md` | **C** | 19/10/2026 | ✅ Fidélité `0,6 mm` · translation `R+1 → RDC` (`D-23`) |
| **B-32** | `03_CALAGE/B-32_Vue_Nettoyee.md` | **D** | **20/10/2026** | ✅ **CONFORME** — cloisons & isolation 100 % supprimées (`0 entité` sur `020_cloi`/`020_cloisons`), audit `0 erreur` |
| **B-20** | `02_CONCEPTION/B-20_Conception_GO.md` | **B** | **20/10/2026** | ✅ **CONFORME** — synthèse intégrale `D1+D2+D3+D4+D5`, calage vectoriel `1/80` (`21,0 mm`), 100 % des ouvrages implantés, 3 planches + 2 coupes `A-A / B-B` |
| **B-40** | `06_CALCULS/B-40_Fondations.md` | **E** | **20/10/2026** | ✅ **CONFORME EN PARTIEL-DÉCLARÉ** — plan combiné `PLS` implanté + ferraillage `HA8 e150` + note `D-09` + justification `D-24 / R-36` |
| **B-25** | `02_CONCEPTION/B-25_Stabilite_Globale.md` | **B** | **20/10/2026** | ✅ **CONFORME 6/6 applicables** — contreventement = maçonnerie seule, `ΣK = 1,21/1,64 GN/m`, torsion `τ/f_vk ≤ 0,028`, aucun joint. **Sismique retirée (`D-26`)** · **stabilité provisoire retirée, MOE (`D-27`)** |

---

## 3. LIVRABLES PRINCIPAUX RÉVISÉS LE 20/10/2026 (TAILLES VÉRIFIÉES)

### 3.1 Notes principales

| Fichier | Taille exacte | Contenu |
|---|---|---|
| `01_CADRAGE/B-03_RDR.md` | `57 322 o · 433 l.` | Registre vivant Ind. P : `D-01` à `D-25`, Articles `P1–P8`, registre des nuages `D-19` |
| `02_CONCEPTION/B-20_Conception_GO.md` | `30 101 o · 206 l.` | Synthèse structurelle & prédimensionnement GO Ind. B (rectificatifs + 13 postes + rattachement `B-11`) |
| `06_CALCULS/B-40_Fondations.md` | `10 836 o · 108 l.` | Note de calcul & implantation « PLS » des fondations Ind. E (note `D-09` en tête) |
| `03_CALAGE/B-32_Vue_Nettoyee.md` | `6 412 o · 73 l.` | Rapport de nettoyage structurel strict Ind. D (purge totale cloisons & isolation) |
| `02_CONCEPTION/B-25_Stabilite_Globale.md` | `45 802 o · 419 l.` | Note de stabilité globale **Ind. B** (contreventement, torsion, régularité, joints) — exclusions `D-26` (sismique) et `D-27` (stabilité provisoire → MOE) — journal `_rendus/b25_stabilite.txt` |

### 3.2 Planches graphiques actives dans `_plans/` (18 fichiers — 22,2 Mo — audit `0 erreur` sur les 6 DXF)

| Famille | DXF (AutoCAD AC1032) | PDF vectoriel | PNG (200–220 dpi) |
|---|---|---|---|
| **B-20 Planche 1 — Synthèse PH RDC** | `FLORA_B20_PH-RDC_PRINCIPE-STRUCTUREL_IndB.dxf` (`2 790 594 o`) | `922 524 o` | `922 258 o` |
| **B-20 Planche 2 — Implantation Fondations PB RDC (`PLS`)** | `FLORA_B20_PB-RDC_IMPLANTATION-FONDATIONS_IndB.dxf` (`2 767 496 o`) | `946 375 o` | `907 137 o` |
| **B-20 Planche 3 — R+1 Charpente, Coupes `A-A / B-B` & Cheminement** | `FLORA_B20_CHARPENTE_COUPES_SCHEMA_IndB.dxf` (`2 729 761 o`) | `612 780 o` | `624 524 o` |
| **B-40 Ind. E — Plan combiné `PLS` + Ferraillage Type Semelles** | `FLORA_FONDATIONS_TYPE_IndE.dxf` (`2 770 072 o`) | `523 324 o` | `648 530 o` |
| **B-32 Ind. D — Vue nettoyée structurelle RDC** | `FLORA_RDC_VUE-NETTOYEE_IndD.dxf` (`2 719 320 o`) | `80 712 o` | `280 106 o` |
| **B-32 Ind. D — Vue nettoyée structurelle R+1** | `FLORA_R1_VUE-NETTOYEE_IndD.dxf` (`2 672 677 o`) | `78 372 o` | `278 171 o` |
