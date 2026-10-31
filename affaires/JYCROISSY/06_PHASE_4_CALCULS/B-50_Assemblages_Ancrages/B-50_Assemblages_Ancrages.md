# B-50 — Assemblages et ancrages

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-50 (Phase 4 — Calculs d'exécution)
**Date :** 2026-10-31
**Mode :** PARAMÉTRIQUE documentaire (spécification du script — OUT-01 absent)
**Famille :** tous
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-40 Fondations superficielles | ✅ lue | Efforts transmis (symbole) | Calcul suspendu — PARAMÉTRIQUE |
| B-42 Verticaux BA | ✅ lue | Efforts à ancrer (symbole) | Calcul suspendu — PARAMÉTRIQUE |
| B-43 Planchers et dallages | ✅ lue | Efforts aux appuis (symbole) | Calcul suspendu — PARAMÉTRIQUE |
| B-45 Structure métallique | ✅ lue | Efforts aux assemblages (symbole) | Calcul suspendu — PARAMÉTRIQUE |
| B-46 Maçonnerie | ✅ lue | Efforts aux scellements (symbole) | Calcul suspendu — PARAMÉTRIQUE |
| B-02 FDC | ✅ lue | MAT-01 à MAT-12, DOC-09 | DOC-09 manquant |

**Aucune donnée déclarée « absente » sans cette preuve.** Les efforts transmis par les briques amont sont en symbole (PARAMÉTRIQUE) et DOC-09 (fiches techniques connecteurs) est manquant → mode PARAMÉTRIQUE documentaire. L'environnement d'exécution (OUT-01) est absent → PARAMÉTRIQUE documentaire (spécification du script, sans livrable).

---

## ÉTAPE 1 — INVENTAIRE DES ASSEMBLAGES ET ANCRAGES

| Assemblage / ancrage | Brique amont | Efforts transmis | Statut |
|---|---|---|---|
| Ancrage poteau P1 (attente vers semelle SI1) | B-42 | N_Ed, M_Ed, section des barres (symbole) | PARAMÉTRIQUE |
| Ancrage poteau P2 (attente vers semelle SI2) | B-42 | N_Ed, M_Ed, section des barres (symbole) | PARAMÉTRIQUE |
| Ancrage poteau P3 (attente vers semelle SI3) | B-42 | N_Ed, M_Ed, section des barres (symbole) | PARAMÉTRIQUE |
| Appui Pt1 sur poteau P1 | B-45 | N_Ed, V_Ed, M_Ed (symbole) | PARAMÉTRIQUE |
| Appui Pt2 sur poteau P2 | B-45 | N_Ed, V_Ed, M_Ed (symbole) | PARAMÉTRIQUE |
| Scellement chaînage rapporté mur Ouest | B-46 | N_Ed, V_Ed, M_Ed (symbole) | PARAMÉTRIQUE |
| Scellement chaînage rapporté mur Est | B-46 | N_Ed, V_Ed, M_Ed (symbole) | PARAMÉTRIQUE |

**Aucun assemblage calculé — tous les efforts sont en symbole.**

---

## ÉTAPE 2 — CALCUL DES ANCRAGES BA (FORMULES LITTERALES)

### Contrainte d'adhérence : f_bd = 2,25·η₁·η₂·f_ctd (EC2 §8.4.2)

- f_bd = 2,25·η₁·η₂·f_ctd (symbole).

### Longueur d'ancrage de référence : l_b,rqd = (Φ/4)·(σ_sd/f_bd)

- l_b,rqd = (Φ/4)·(σ_sd/f_bd) (symbole).

### Longueur d'ancrage de calcul : l_bd = α₁·α₂·α₃·α₄·α₅·l_b,rqd (EC2 §8.4.4)

- l_bd = α₁·α₂·α₃·α₄·α₅·l_b,rqd (symbole).

### En équerre : α₁ = 0,7

- α₁ = 0,7 (valeur connue).

### Vérification de la longueur d'ancrage minimale : l_b,min = max(0,3·l_b,rqd ; 10·Φ ; 100 mm) (EC2 §8.4.4)

- l_b,min = max(0,3·l_b,rqd ; 10·Φ ; 100 mm) (symbole).

**Aucune longueur d'ancrage retenue — toutes les formules sont en symbole.**

---

## ÉTAPE 3 — CALCUL DES ASSEMBLAGES MÉTALLIQUES (FORMULES LITTERALES)

### Boulons

- Cisaillement : F_v,Rd = α_v·f_ub·A_s/γ_M2 (EC3-1-8 §3.6) (symbole).
- Pression diamétrale : F_b,Rd = k₁·α_b·f_u·d·t/γ_M2 (symbole).
- Traction : F_t,Rd = k₂·f_ub·A_s/γ_M2 (symbole).
- Interaction cisaillement + traction (EC3-1-8 §3.6.1) (symbole).

### Soudures

- Gorge : a ≤ 0,7·t_min (symbole).
- Contrainte : σ ⊥, τ ⊥, τ // selon EC3-1-8 §4.5 (symbole).
- Longueur efficace : l_eff = L − 2·a (symbole).

**Aucun assemblage métallique calculé — toutes les formules sont en symbole.**

---

## ÉTAPE 4 — CONTRÔLE CROISÉ (OBLIGATOIRE)

Pour chaque ancrage calculé (à calculer), contrôler la cohérence avec le logement vérifié par la brique aval :
- L'ancrage calculé tient-il dans le logement vérifié (enrobage, espacement, hauteur) ?
- Si non : identifier la brique responsable (aval qui n'a pas assez de place, ou amont qui a sous-estimé les efforts).
- Si l'écart est aval (B-40, B-42, B-43, B-46, B-49) : l'élément aval s'agrandit.
- Si l'écart est amont (B-44, B-45, B-47, B-48) : les efforts transmis doivent être revus.

**Aucun contrôle croisé produit — les ancrages ne sont pas calculés (efforts en symbole — PARAMÉTRIQUE).**

---

## ÉTAPE 5 — LIVRABILES GRAPHIQUES (SPÉCIFICATION DU SCRIPT — NON PRODUITS)

| Calque | Contenu | Statut |
|---|---|---|
| ASSEMBLAGE-AXES | Axes, trames, points de calage | Non produit (OUT-01 absent) |
| ASSEMBLAGE-DETAILS | Détails à grande échelle des assemblages et ancrages | Non produit (OUT-01 absent) |
| ASSEMBLAGE-NOMENCLATURE | Nomenclature des connecteurs | Non produit (OUT-01 absent) |
| ASSEMBLAGE-HABILLAGE-TEXTE | Légendes, cartouche, notes, tableaux | Non produit (OUT-01 absent) |

**Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA »** (à produire quand OUT-01 est disponible).

---

## ÉTAPE 6 — RAPPORT DE CONTRÔLE CROISÉ

**Aucun rapport produit — les ancrages ne sont pas calculés (efforts en symbole — PARAMÉTRIQUE).** Le rapport de contrôle croisé sera produit quand les briques amont seront en mode COMPLET (efforts chiffrés) et DOC-09 sera disponible.

---

## ÉTAPE 7 — AUTO-CONTRÔLE DÉCLARÉ

| Point | Statut |
|---|---|
| Inventaire des assemblages et ancrages | ✅ §Étape 1 (7 assemblages/ancrages) |
| Calcul des ancrages BA (EC2 §8.4) | ❌ À calculer (efforts en symbole — PARAMÉTRIQUE) |
| Calcul des assemblages métalliques (EC3-1-8) | ❌ À calculer (efforts en symbole — PARAMÉTRIQUE) |
| Contrôle croisé (ancrage vs logement) | ❌ À calculer (ancrages non calculés) |
| Rapport de contrôle croisé | ❌ À produire (ancrages non calculés) |
| Plans de détail | ❌ À produire (OUT-01 absent) |
| Auto-contrôle assemblage par assemblage | ✅ §Étape 7 (7 assemblages) |

**DE PRINCIPE :**
- Efforts transmis en symbole (briques amont en PARAMÉTRIQUE).
- DOC-09 (fiches techniques connecteurs) manquant.

**À LEVER :**
- Efforts chiffrés (briques amont en COMPLET).
- DOC-09 (fiches techniques connecteurs).
- Environnement d'exécution (OUT-01).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque donnée d'entrée est issue de la FDC | ✅ §Étape 1 (efforts transmis par briques amont) |
| Calcul des ancrages et assemblages à partir des efforts transmis | ❌ À calculer (efforts en symbole — PARAMÉTRIQUE) |
| Contrôle croisé avec les logements vérifiés par les briques aval | ❌ À calculer (ancrages non calculés) |
| Rapport de contrôle croisé (pièce 4) | ❌ À produire (ancrages non calculés) |
| Plans de détail des assemblages | ❌ À produire (OUT-01 absent) |
| Auto-contrôle assemblage par assemblage | ✅ §Étape 7 (7 assemblages) |

**Écart signalé :** B-50 est en mode PARAMÉTRIQUE documentaire (OUT-01 absent + DOC-09 manquante + efforts en symbole). Aucune valeur n'est retenue. Le calcul est suspendu jusqu'à obtention des efforts chiffrés (briques amont en COMPLET), de DOC-09 et de OUT-01.

---

**Brique B-50 exécutée en mode PARAMÉTRIQUE documentaire — en attente de votre GO ou de nouvelles observations.**
Les briques amont (B-40 à B-49) sont en mode PARAMÉTRIQUE (efforts en symbole) et DOC-09 est manquant. **Aucun ancrage, aucun assemblage, aucune valeur n'est retenu.** Le calcul est **SUSPENDU** jusqu'à obtention des efforts chiffrés, de DOC-09 et de l'environnement d'exécution (OUT-01).
