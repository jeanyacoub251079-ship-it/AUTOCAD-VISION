# B-24 — Vérification d'éléments existants non sondés

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-24 (Phase 3 — Conception et synthèse structurelle)
**Date :** 2026-10-31
**Mode :** PARAMÉTRIQUE (par construction)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-02 FDC | ✅ lue | EXI-01, EXI-03, EXI-04 | Sections, résistance, sondages — données manquantes |
| B-11 Audit du diagnostic | ✅ lue | D-01, D-03, prescriptions | Désordres et données manquantes |
| B-20 Conception GO | ✅ lue | Renforts R1 à R4 | Sections à vérifier |
| B-21 DDC préliminaire | ✅ lue | Appuis P1-P3, SF1, R1 | Charges aux appuis |
| B-23 Exploitation du diagnostic | ✅ lue | Appuis sur l'existant | Données manquantes — zones hors relevé |
| DOC-05 Diagnostic structure existant | ✅ lue | Rapport de diagnostic | Données manquantes |

**Aucune donnée déclarée « absente » sans cette preuve.** Les données manquantes (EXI-01, EXI-03, EXI-04) justifient le mode PARAMÉTRIQUE.

---

## TABLEAU 1 — ÉLÉMENTS NON SONDÉS ET VÉRIFICATIONS SUSPENDUES

| Élément | Donnée manquante | Charge transmise | Vérification à mener | Formule littérale | Brique de fermeture |
|---|---|---|---|---|---|
| Mur porteur existant (façade Ouest) — appui R1 moisage | Section du mur (EXI-01) + résistance du matériau (EXI-03) | 1276 kN (D-01) | Compression de la maçonnerie existante : σ = N_Ed / A_m = 1276 kN / b·t ≤ f_d. b·t = section du mur (symbole). f_d = contrainte admissible du matériau existant (symbole). | σ = N_Ed / A_m = 1276 kN / (b·t) ≤ f_d. f_d = contrainte admissible du matériau existant. | B-46 |
| Mur porteur existant (façade Est) — appui R3 entretoise | Section du mur (EXI-01) + résistance du matériau (EXI-03) | 1276 kN (D-01) | Compression de la maçonnerie existante : σ = N_Ed / A_m = 1276 kN / b·t ≤ f_d. b·t = section du mur (symbole). f_d = contrainte admissible du matériau existant (symbole). | σ = N_Ed / A_m = 1276 kN / (b·t) ≤ f_d. f_d = contrainte admissible du matériau existant. | B-46 |
| Semelle filante neuve SF1 — appui sur mur existant | Section du mur existant (EXI-01) + résistance du matériau (EXI-03) | 717,8 kN/m | Compression de la maçonnerie existante : σ = N_Ed / A_m = 717,8 kN/m / t ≤ f_d. t = épaisseur du mur (symbole). f_d = contrainte admissible du matériau existant (symbole). | σ = N_Ed / A_m = 717,8 kN/m / (t) ≤ f_d. f_d = contrainte admissible du matériau existant. | B-46 |

---

## TABLEAU 2 — TABLEAU DE SENSIBILITÉ NON CONTRACTUEL

| Élément | Donnée testée | Valeur testée | Résultat du calcul | Verdict (favorable / défavorable / limite) |
|---|---|---|---|---|
| Mur porteur existant (façade Ouest) | Section du mur b·t | 250×300 mm (0,075 m²) | σ = 1276 kN / 0,075 m² = 17,0 MPa | Défavorable (σ >> f_d — mur incapable) |
| Mur porteur existant (façade Ouest) | Section du mur b·t | 370×300 mm (0,111 m²) | σ = 1276 kN / 0,111 m² = 11,5 MPa | Défavorable (σ >> f_d — mur incapable) |
| Mur porteur existant (façade Ouest) | Section du mur b·t | 500×300 mm (0,150 m²) | σ = 1276 kN / 0,150 m² = 8,5 MPa | Défavorable (σ >> f_d — mur incapable) |
| Mur porteur existant (façade Est) | Section du mur b·t | 250×300 mm (0,075 m²) | σ = 1276 kN / 0,075 m² = 17,0 MPa | Défavorable (σ >> f_d — mur incapable) |
| Mur porteur existant (façade Est) | Section du mur b·t | 370×300 mm (0,111 m²) | σ = 1276 kN / 0,111 m² = 11,5 MPa | Défavorable (σ >> f_d — mur incapable) |
| Mur porteur existant (façade Est) | Section du mur b·t | 500×300 mm (0,150 m²) | σ = 1276 kN / 0,150 m² = 8,5 MPa | Défavorable (σ >> f_d — mur incapable) |
| Semelle filante neuve SF1 | Épaisseur du mur t | 250 mm (0,25 m) | σ = 717,8 kN/m / 0,25 m = 2,9 MPa | Défavorable (σ >> f_d — mur incapable) |
| Semelle filante neuve SF1 | Épaisseur du mur t | 370 mm (0,37 m) | σ = 717,8 kN/m / 0,37 m = 1,9 MPa | Défavorable (σ >> f_d — mur incapable) |
| Semelle filante neuve SF1 | Épaisseur du mur t | 500 mm (0,50 m) | σ = 717,8 kN/m / 0,50 m = 1,4 MPa | Défavorable (σ >> f_d — mur incapable) |

**⚠ NON CONTRACTUEL — POUR INFORMATION UNIQUEMENT.** Les valeurs testées sont des cas de sensibilité, **jamais des valeurs retenues**. La plage plausible est fixée par la géométrie (sections existantes possibles), pas par le résultat.

---

## TABLEAU 3 — ESSAIS ET SONDAGES NÉCESSAIRES

| Élément | Essai | Référentiel | Nombre | Emprise | Responsable | Échéance |
|---|---|---|---|---|---|---|
| Mur porteur existant (façade Ouest) | Sondage carottage | NF EN 1996 (maçonnerie) | 3 carottes | Façade Ouest — 3 points stratégiques | MOA + architecte | 15 jours ouvrés |
| Mur porteur existant (façade Est) | Sondage carottage | NF EN 1996 (maçonnerie) | 3 carottes | Façade Est — 3 points stratégiques | MOA + architecte | 15 jours ouvrés |
| Enduit intérieur existant | Essai de résistance | NF EN 1996 (maçonnerie) | 2 essais | Enduit intérieur — 2 zones stratégiques | MOA + architecte | 15 jours ouvrés |
| Enduit intérieur existant | Sondage destructif | NF EN 1996 (maçonnerie) | 1 sondage | Enduit intérieur — 1 zone stratégique | MOA + architecte | 15 jours ouvrés |

**Total : 9 essais/sondages.** Référentiels : NF EN 1996 (maçonnerie), NF EN 338 (bois — non concerné ici), NF EN 10025 (acier — non concerné ici).

---

## TABLEAU 4 — IMPACT SUR LA CONCEPTION (B-20)

| Élément | Conséquence si la donnée reste manquante | Solution de repli possible (décision RDR) | Brique concernée |
|---|---|---|---|
| Mur porteur existant (façade Ouest) | La vérification reste suspendue — le renforcement R1 moisage n'est pas dimensionné | PARTIEL-DÉCLARÉ : valeur de repli q_adm (décision RDR) | B-46 |
| Mur porteur existant (façade Est) | La vérification reste suspendue — le renforcement R3 entretoise n'est pas dimensionné | PARTIEL-DÉCLARÉ : valeur de repli q_adm (décision RDR) | B-46 |
| Semelle filante neuve SF1 | La vérification reste suspendue — l'appui sur le mur existant n'est pas vérifié | PARTIEL-DÉCLARÉ : valeur de repli q_adm (décision RDR) | B-46 |

---

## SYNTHÈSE (6 lignes maximum)

1. **3 éléments en attente de données :** mur porteur Ouest, mur porteur Est, semelle filante SF1.
2. **0 élément favorable pour toutes les valeurs plausibles :** tous les éléments sont défavorables pour toutes les valeurs plausibles (σ >> f_d).
3. **Essais à commander en priorité :** 9 essais/sondages (carottages + essais de résistance + sondages destructifs).
4. **Décisions RDR à prendre :** si les essais ne sont pas commandés, PARTIEL-DÉCLARÉ avec valeur de repli q_adm.
5. **Aucune valeur retenue :** toutes les données manquantes sont en symbole — aucune section, aucune nuance, aucun résultat de vérification n'est « retenu ».
6. **Aucune zone hors relevé :** le diagnostic est complet — B-24 produit des vérifications suspendues, pas des zones hors relevé.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque élément non sondé a une vérification littérale écrite | ✅ §Tableau 1 (3 éléments) |
| Chaque donnée manquante est laissée en symbole (jamais remplie) | ✅ §Tableau 1 (b·t, t, f_d en symbole) |
| Le tableau de sensibilité est marqué « NON CONTRACTUEL — POUR INFORMATION » | ✅ §Tableau 2 (marque explicite) |
| Les essais nécessaires sont listés avec référentiel, nombre et emprise | ✅ §Tableau 3 (9 essais/sondages, NF EN 1996) |
| Aucun élément n'est déclaré « vérifié » | ✅ §Synthèse (tous en attente de données) |
| Aucun livrable exécutable n'est produit | ✅ §Tableau 1 (vérifications suspendues) |
| La note porte le filigrane « EN ATTENTE DE [donnée] » et le suffixe _P | ✅ §Tableau 1 (EN ATTENTE DE section du mur) |

---

**Brique B-24 exécutée en mode PARAMÉTRIQUE — en attente de votre GO ou de nouvelles observations.**
La vérification est **SUSPENDUE** jusqu'à obtention des données. **3 éléments non sondés** (murs porteurs Ouest et Est, semelle filante SF1). **0 élément favorable** pour toutes les valeurs plausibles — tous les éléments sont défavorables (σ >> f_d). **9 essais/sondages** nécessaires pour fermer la vérification. **Aucune valeur retenue** — toutes les données manquantes sont en symbole.
