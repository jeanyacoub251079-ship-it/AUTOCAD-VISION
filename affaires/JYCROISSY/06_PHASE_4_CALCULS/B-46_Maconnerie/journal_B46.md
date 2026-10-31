# Journal B-46 — Maçonnerie : vérification et conception

**Date :** 2026-10-31
**Brique :** B-46 (Phase 4 — Calculs d'exécution)
**Bloc A (vérification existant) :** PARAMÉTRIQUE (existant non sondé — B-24)
**Bloc B (conception neuve) :** SANS OBJET (pas de maçonnerie neuve)

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-02 FDC | ✅ lue | MAT-07, MAT-09 à MAT-12, CHG-07 |
| B-20 Conception GO | ✅ lue | Murs porteurs existants |
| B-23 Exploitation du diagnostic | ✅ lue | Appuis sur l'existant |
| B-24 Vérification existants non sondés | ✅ lue | Vérifications suspendues |
| B-40 Fondations superficielles | ✅ lue | Semelles |
| B-42 Verticaux BA | ✅ lue | Poteaux P1-P3 |
| B-43 Planchers et dallages | ✅ lue | Dalles BA |
| B-45 Structure métallique | ✅ lue | Poutres métalliques |

## 2. Traitement

- Bloc A : 3 zones vérifiées (mur Ouest, mur Est, semelle filante SF1).
- Résistance de la maçonnerie existante manquante (B-24 — PARAMÉTRIQUE).
- Contrainte transmise N_Ed = 1276 kN (D-01 — connue).
- Formules littérales (compression, flambement, cisaillement, contraintes localisées) — aucune valeur retenue.
- Bloc B : SANS OBJET (pas de maçonnerie neuve).
- Vérification suspendue jusqu'à obtention des données (B-24).

## 3. Résultat

Livrable `B-46_Maconnerie.md` produit. B-46 est **complète** (Bloc A PARAMÉTRIQUE, Bloc B SANS OBJET).

## 4. Non-régression

Aucune brique modifiée. B-20, B-21, B-22, B-23, B-24, B-40, B-42, B-43, B-45 intacts.

## 5. Point de contrôle humain

Valider la résistance de la maçonnerie existante (B-24 — PARAMÉTRIQUE). Valider l'environnement d'exécution (OUT-01). La vérification est suspendue jusqu'à obtention des données (B-24).
