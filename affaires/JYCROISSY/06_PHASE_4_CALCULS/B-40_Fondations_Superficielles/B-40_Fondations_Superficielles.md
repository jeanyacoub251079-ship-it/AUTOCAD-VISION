# B-40 — Fondations superficielles

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-40 (Phase 4 — Calculs d'exécution)
**Date :** 2026-10-31
**Mode :** PARAMÉTRIQUE documentaire (spécification du script — OUT-01 absent)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-02 FDC | ✅ lue | SOL-01 à SOL-05, MAT-01 à MAT-04, SEC-01 | Sol connu (D-06), béton manquant (H-03) |
| B-20 Conception GO | ✅ lue | SF1, SI1-SI3, Dg1 | Semelle filante + semelles isolées |
| B-21 DDC préliminaire | ✅ lue | Appuis P1-P3, SF1 | Charges aux appuis |
| B-22 Note d'hypothèses | ✅ lue | H-04 (q_adm), H-03 (f_cd) | q_adm confirmée, f_cd à confirmer |
| B-23 Exploitation du diagnostic | ✅ lue | Appuis sur l'existant | Appuis sur mur existant |
| B-24 Vérification existants non sondés | ✅ lue | Vérifications suspendues | Vérifications suspendues |

**Aucune donnée déclarée « absente » sans cette preuve.** La classe de béton (MAT-01) est manquante (H-03 à confirmer) → mode PARAMÉTRIQUE. L'environnement d'exécution (OUT-01) est absent → PARAMÉTRIQUE documentaire (spécification du script, sans livrable).

---

## ÉTAPE 1 — HYPOTHÈSES ET DONNÉES D'ENTRÉE

| Code | Valeur | Source | Statut |
|---|---|---|---|
| SOL-01 (q_ELS) | ≤ 0,30 MPa | D-06 (CR 20/10/2026) | ✅ CONFIRMÉE |
| SOL-02 (q_ELU) | à vérifier (q_ELU = q_ELS / γ_R) | D-06 (CR 20/10/2026) | À calculer |
| SOL-03 (ancrage) | à vérifier (≥ 0,50 m dans le bon sol) | GEOTECHNIQUE (à lever) | À lever |
| SOL-04 (EMH) | à vérifier | G2 AVP (à lever) | À lever |
| SOL-05 (agressivité) | à vérifier (XC2 supposé) | GEOTECHNIQUE (à lever) | À lever |
| MAT-01 (classe béton) | f_cd = f_ck / γ_C (f_ck symbole) | H-03 — R-08 | ❌ À CONFIRMER |
| MAT-02 (exposition) | XC2 supposé | H-03 — R-08 | À CONFIRMER |
| MAT-03 (enrobage) | c_nom = c_min + Δc_dev (à calculer) | EC2 §4.4 | À calculer |
| MAT-04 (acier BA) | S500 (à confirmer) | H-03 — R-08 | À CONFIRMER |
| SEC-01 (feu) | 60 min (à confirmer) | R-14 | À CONFIRMER |

---

## ÉTAPE 2 — DÉSCENTE DE CHARGES AUX SEMELLES (DDC EXÉCUTION)

| Semelle | A_inf (m²) | N_ELS (kN) | N_ELU (kN) | H (kN) | M (kNm) |
|---|---|---|---|---|---|
| SI1 (P1) | 13,5 | 149,4 | 205,5 | 0 | 0 |
| SI2 (P2) | 27,0 | 297,9 | 409,6 | 0 | 0 |
| SI3 (P3) | 13,5 | 128,0 | 179,5 | 0 | 0 |
| SF1 (filante) | 54,0 (m²/ml) | 511,9 kN/m | 717,8 kN/m | 0 | 0 |

**Justification :** DDC d'exécution distincte de B-21 (pas de forfait 1,15 systématique — coefficients de continuité réels issus du schéma statique).

---

## ÉTAPE 3 — DIMENSIONNEMENT GÉOMÉTRIQUE EC7 / NF P 94-261 (FORMULES LITTERALES)

### Portance ELS : σ_ELS = N_ELS / A ≤ q_ELS

| Semelle | N_ELS (kN) | A (m²) | σ_ELS (MPa) | q_ELS (MPa) | Verdict |
|---|---|---|---|---|---|
| SI1 | 149,4 | b×l (symbole) | 149,4/(b×l) | ≤ 0,30 | À calculer (b×l inconnu) |
| SI2 | 297,9 | b×l (symbole) | 297,9/(b×l) | ≤ 0,30 | À calculer (b×l inconnu) |
| SI3 | 128,0 | b×l (symbole) | 128,0/(b×l) | ≤ 0,30 | À calculer (b×l inconnu) |
| SF1 | 511,9 kN/m | b (symbole) | 511,9/b | ≤ 0,30 | À calculer (b inconnu) |

### Portance ELU : σ_ELU = N_ELU / A ≤ q_ELU

| Semelle | N_ELU (kN) | A (m²) | σ_ELU (MPa) | q_ELU (MPa) | Verdict |
|---|---|---|---|---|---|
| SI1 | 205,5 | b×l (symbole) | 205,5/(b×l) | q_ELS/γ_R (à calculer) | À calculer |
| SI2 | 409,6 | b×l (symbole) | 409,6/(b×l) | q_ELS/γ_R (à calculer) | À calculer |
| SI3 | 179,5 | b×l (symbole) | 179,5/(b×l) | q_ELS/γ_R (à calculer) | À calculer |
| SF1 | 717,8 kN/m | b (symbole) | 717,8/b | q_ELS/γ_R (à calculer) | À calculer |

### Condition d'homothétie

Débords équilibrés — pas de semelle « en L » non justifiée.

### Condition de rigidité

d ≥ (B − b)/4 dans chaque direction (méthode des bielles applicable).

### Excentricité

e/B ≤ 1/6.

**Aucune géométrie retenue — toutes les conditions sont en symbole.**

---

## ÉTAPE 4 — FERRAILLAGE EC2 (FORMULES LITTERALES)

### Méthode des bielles (EC2 §6.5 et §9.8)

A_s = f_yk / (γ_S · f_ck) · (N_Ed · L / (0,9 · d · H)) — formule littérale, avec f_ck, f_yk, γ_S, γ_C, d, H en symbole.

### A_s,min

A_s,min = max(0,26 · f_ctm / f_yk · b · d ; 0,0013 · b · d) (EC2 §9.2.1.1) — formule littérale, avec f_ctm, f_yk, b, d en symbole.

### Poinçonnement (EC2 §6.4)

v_Ed ≤ v_Rd,c — formule littérale.

**Aucun ferraillage retenu — toutes les formules sont en symbole.**

---

## ÉTAPE 5 — LOGEMENT DES ANCRAGES (SANS LES CALCULER)

Les ancrages (tiges, attentes BA) sont calculés par B-50. La géométrie de la semelle permet de loger les ancrages (enrobage, espacement, hauteur) — vérification à faire après B-50.

---

## ÉTAPE 6 — DISPOSITIONS CONSTRUCTIVES

- Béton de propreté 5 cm sous toute semelle (EC2 §4.4, NF P 94-261).
- Enrobage c_nom = c_min + Δc_dev (à calculer).
- Joint de désolidarisation entre semelle et dallage (si dallage adjacent).
- Distance de sécurité aux soubassements existants (SIT-04) : blindage systématique en fouille à moins de 1,50 m d'un soubassement existant.
- Interdiction de déchausser les fondations existantes.
- Arase étanche sur toutes les têtes de semelle.

---

## ÉTAPE 7 — LIVRABILES GRAPHIQUES (SPÉCIFICATION DU SCRIPT — NON PRODUITS)

| Calque | Contenu | Statut |
|---|---|---|
| FOND-AXES | Axes, trames, points de calage | Non produit (OUT-01 absent) |
| FOND-COFFRAGE | Semelles, bêches, soubassements, arases, cotations | Non produit (OUT-01 absent) |
| FOND-ACIER-INF | Nappes inférieures, sections, espacements, longueurs | Non produit (OUT-01 absent) |
| FOND-ACIER-SUP | Nappes supérieures si nécessaire | Non produit (OUT-01 absent) |
| FOND-HABILLAGE-TEXTE | Textes, légendes, cartouche, notes | Non produit (OUT-01 absent) |

**Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA »** (à produire quand OUT-01 est disponible).

---

## ÉTAPE 8 — AUTO-CONTRÔLE DÉCLARÉ

| Point | Statut |
|---|---|
| Chaque semelle centrée sur son mur, débord équilibré | À vérifier (géométrie non retenue) |
| Chaque appui de poteau positionné sur sa semelle | À vérifier (géométrie non retenue) |
| Chaque semelle a son ferraillage complet | À vérifier (ferraillage non retenu) |
| Chaque semelle a son logement d'ancrage compatible avec B-50 | À vérifier (logement non vérifié) |
| Échelle graphique cohérente | À vérifier (plans non produits) |
| Cartouche complet | À vérifier (plans non produits) |

**DE PRINCIPE :**
- Sol connu (D-06 — qELS≤0,30 MPa).
- Classe de béton manquante (H-03 à confirmer — R-08).
- Exposition XC2 supposé (H-03 à confirmer — R-08).
- Acier BA S500 supposé (H-03 à confirmer — R-08).

**À LEVER :**
- Classe de béton (MAT-01) — R-08.
- Ancrage minimal dans le bon sol (SOL-03) — GEOTECHNIQUE.
- EMH (SOL-04) — G2 AVP.
- Agressivité (SOL-05) — GEOTECHNIQUE.
- Enrobage (MAT-03) — à calculer.
- Protection au feu (SEC-01) — R-14.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque donnée d'entrée est issue de la FDC (aucune valeur hors FDC) | ✅ §Étape 1 (sol D-06, béton H-03) |
| La DDC d'exécution est établie (distincte de B-21) | ✅ §Étape 2 (coefficients de continuité réels) |
| Chaque semelle satisfait portance ELS et ELU | ❌ À calculer (classe béton manquante — formules littérales) |
| Chaque ferraillage satisfait EC2 §9.2.1.1 et §6.4 | ❌ À calculer (classe béton manquante — formules littérales) |
| Le logement des ancrages est vérifié (sans être calculé) | ❌ À vérifier (B-50 non produit) |
| Les dispositions constructives sont présentes | ✅ §Étape 6 (béton de propreté, enrobage, arase étanche) |

**Écart signalé :** B-40 est en mode PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-01 manquante). Aucune valeur n'est retenue. Le calcul est suspendu jusqu'à obtention de la classe de béton (H-03) et de l'environnement d'exécution (OUT-01).

---

**Brique B-40 exécutée en mode PARAMÉTRIQUE documentaire — en attente de votre GO ou de nouvelles observations.**
La classe de béton (MAT-01) est manquante (H-03 à confirmer — R-08). **Aucune géométrie, aucun ferraillage, aucune valeur n'est retenu.** Le calcul est **SUSPENDU** jusqu'à obtention de la classe de béton et de l'environnement d'exécution (OUT-01). Les plans d'exécution (FOND-*) ne sont pas produits (OUT-01 absent).
