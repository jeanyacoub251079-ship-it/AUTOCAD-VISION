# Journal B-40 — Fondations superficielles

**Date :** 2026-10-31
**Brique :** B-40 (Phase 4 — Calculs d'exécution)
**Mode :** PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-01 manquante)

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-02 FDC | ✅ lue | SOL-01 à SOL-05, MAT-01 à MAT-04, SEC-01 |
| B-20 Conception GO | ✅ lue | SF1, SI1-SI3, Dg1 |
| B-21 DDC préliminaire | ✅ lue | Appuis P1-P3, SF1 |
| B-22 Note d'hypothèses | ✅ lue | H-04 (q_adm), H-03 (f_cd) |
| B-23 Exploitation du diagnostic | ✅ lue | Appuis sur l'existant |
| B-24 Vérification existants non sondés | ✅ lue | Vérifications suspendues |

## 2. Traitement

- Sol connu (D-06 — qELS≤0,30 MPa).
- Classe de béton manquante (H-03 à confirmer — R-08).
- DDC d'exécution établie (distincte de B-21 — coefficients de continuité réels).
- 4 semelles chargées (SI1, SI2, SI3, SF1).
- Formules littérales (portance, ferraillage) — aucune valeur retenue.
- Plans d'exécution non produits (OUT-01 absent).
- Calcul suspendu jusqu'à obtention de la classe de béton et de OUT-01.

## 3. Résultat

Livrable `B-40_Fondations_Superficielles.md` produit. B-40 est **complète** (mode PARAMÉTRIQUE documentaire).

## 4. Non-régression

Aucune brique modifiée. B-20, B-21, B-22, B-23, B-24 intacts.

## 5. Point de contrôle humain

Valider la classe de béton (H-03 à confirmer — R-08). Valider l'environnement d'exécution (OUT-01). Le calcul est suspendu jusqu'à obtention de ces données.
