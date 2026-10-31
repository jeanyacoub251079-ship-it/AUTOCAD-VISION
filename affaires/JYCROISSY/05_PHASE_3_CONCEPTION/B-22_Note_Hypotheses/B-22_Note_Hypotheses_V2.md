# B-22 V2 — Note d'hypothèses de conception

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-22 (Phase 3 — Conception et synthèse structurelle)
**Date :** 2026-10-31
**Mode :** COMPLET
**Version :** 2.0 (géométrie B-20 V2 — PROJET zone)
**Supersède :** B-22 V1 (géométrie B-20 V1 — EXISTANT zone)

---

## SECTION 1 — INDEX DES HYPOTHÈSES ACTIVES

| N° | Famille | Valeur | Brique introduisant | Brique impactée | Statut |
|---|---|---|---|---|---|
| H-01 | Matériaux | Section poteaux neufs 30×30 cm (MINI) | B-20 | B-42 | À CONFIRMER |
| H-02 | Matériaux | Section poutres métalliques h≈500 mm (ENVELOPPE) | B-20 | B-45 | À CONFIRMER |
| H-03 | Matériaux | Contrainte design béton f_cd (valeur à confirmer R-08) | B-20 | B-40, B-42, B-43 | À CONFIRMER |
| H-04 | Sol | q_adm ≤ 0,30 MPa (D-06) | B-20 | B-40 | CONFIRMÉE (D-06) |
| H-05 | Charges | Charge d'exploitation 250 daN/m² (D-03) | B-20 | B-21, B-42, B-43 | CONFIRMÉE (D-03) |
| H-06 | Charges | Dallage béton armé 20 cm (MINI) | B-21 | B-43 | À CONFIRMER |
| H-07 | Charges | Chape et revêtement 5 cm | B-21 | B-43 | À CONFIRMER |
| H-08 | Charges | Isolation 5 cm | B-21 | B-43 | À CONFIRMER |

---

## SECTION 2 — DÉTAIL PAR HYPOTHÈSE

### H-01 — Section poteaux neufs

| Champ | Valeur |
|---|---|
| Objet | Section des poteaux neufs P1, P2, P3 |
| Valeur retenue | 30 × 30 cm (MINI) |
| Justification | Prédimensionnement par compression axiale : A_c ≥ N_Ed / (0,3 · f_cd). Section MINI pour poteau de telle portée — la vérification définitive se fera en B-42. |
| Source | Hypothèse de travail GO — méthode de prédimensionnement B-20 V2 §2.1 |
| Statut | À CONFIRMER |
| Brique introduisant | B-20 |
| Brique impactée | B-42 (verticaux BA) |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 (V2) |

### H-02 — Section poutres métalliques

| Champ | Valeur |
|---|---|
| Objet | Section des poutres métalliques Pt1, Pt2 |
| Valeur retenue | h ≈ 500 mm (ENVELOPPE) |
| Justification | Prédimensionnement par flèche : h ≈ L/20 en plancher. **L = 9,68 m** (bay 1-2 ou 2-3, B-20 V2) → h ≈ 484 mm → h ≈ 500 mm (ENVELOPPE). |
| Source | Hypothèse de travail GO — méthode de prédimensionnement B-20 V2 §2.2 |
| Statut | À CONFIRMER |
| Brique introduisant | B-20 |
| Brique impactée | B-45 (structure métallique) |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 (V2) |

### H-03 — Contrainte design béton f_cd

| Champ | Valeur |
|---|---|
| Objet | Contrainte design du béton f_cd |
| Valeur retenue | Valeur à confirmer (R-08 — 36 variables « À confirmer » de la FDC) |
| Justification | La FDC ne fournit pas f_cd. Classe de béton à confirmer (C25/30 supposé, mais à valider). |
| Source | R-08 — validation des valeurs « À confirmer » de la FDC |
| Statut | À CONFIRMER |
| Brique introduisant | B-20 |
| Brique impactée | B-40, B-42, B-43 |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 |

### H-04 — Contrainte admissible du sol q_adm

| Champ | Valeur |
|---|---|
| Objet | Contrainte admissible du sol q_adm |
| Valeur retenue | q_adm ≤ 0,30 MPa (qELS) |
| Justification | Paramètres G2 AVP GEOEXPERTS transmis via CR 20/10/2026 — D-06 officiels. |
| Source | D-06 — paramètres G2 AVP GEOEXPERTS n° 25.13646/ES/GIF |
| Statut | CONFIRMÉE |
| Brique introduisant | B-20 |
| Brique impactée | B-40 (fondations superficielles) |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 |
| Date de confirmation | 2026-10-20 (CR 20/10/2026) |

### H-05 — Charge d'exploitation

| Champ | Valeur |
|---|---|
| Objet | Charge d'exploitation des planchers |
| Valeur retenue | 250 daN/m² (2,5 kN/m²) |
| Justification | Décision D-03 — charge d'exploitation officielle pour le cabinet paramédical/bureaux. |
| Source | D-03 — CR 20/10/2026 |
| Statut | CONFIRMÉE |
| Brique introduisant | B-20 |
| Brique impactée | B-21, B-42, B-43 |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 |
| Date de confirmation | 2026-10-20 (CR 20/10/2026) |

### H-06 — Dallage béton armé

| Champ | Valeur |
|---|---|
| Objet | Épaisseur du dallage béton armé neuf Dg1 |
| Valeur retenue | 20 cm (MINI) |
| Justification | Prédimensionnement par flèche : épaisseur ≈ L/30. **L = 5,64 m** (portée courte entre axes A-B ou B-C, B-20 V2) → épaisseur ≈ 19 cm → 20 cm (MINI). |
| Source | Hypothèse de travail GO — méthode de prédimensionnement B-21 V2 §2 |
| Statut | À CONFIRMER |
| Brique introduisant | B-21 |
| Brique impactée | B-43 (planchers et dallages) |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 (V2) |

### H-07 — Chape et revêtement

| Champ | Valeur |
|---|---|
| Objet | Poids propre de la couche chape et revêtement |
| Valeur retenue | 5 cm, 22 kN/m³ |
| Justification | Valeur usuelle pour chape et revêtement — pas de détail dans le DCE. |
| Source | Hypothèse de travail GO — DTU — valeur usuelle |
| Statut | À CONFIRMER |
| Brique introduisant | B-21 |
| Brique impactée | B-43 |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 |

### H-08 — Isolation

| Champ | Valeur |
|---|---|
| Objet | Poids propre de la couche isolation |
| Valeur retenue | 5 cm, 0,15 kN/m³ |
| Justification | Valeur usuelle pour isolation — pas de détail dans le DCE. |
| Source | Hypothèse de travail GO — DTU — valeur usuelle |
| Statut | À CONFIRMER |
| Brique introduisant | B-21 |
| Brique impactée | B-43 |
| Date d'introduction | 2026-10-31 |
| Date de dernière révision | 2026-10-31 |

---

## SECTION 3 — HISTORIQUE DES RÉVISIONS

| Date | Hypothèse (H-xx) | Nature de la révision | Auteur | Motif |
|---|---|---|---|---|
| 2026-10-20 | H-04 | Confirmation (À CONFIRMER → CONFIRMÉE) | CR 20/10/2026 (MOA + architecte) | Paramètres G2 AVP GEOEXPERTS transmis via CR |
| 2026-10-20 | H-05 | Confirmation (À CONFIRMER → CONFIRMÉE) | CR 20/10/2026 (MOA + architecte) | Charge d'exploitation officielle pour cabinet paramédical |
| 2026-10-31 | H-01 | Introduction (nouvelle hypothèse) | B-20 (MOE) | Prédimensionnement poteaux neufs — section MINI |
| 2026-10-31 | H-02 | Introduction (nouvelle hypothèse) | B-20 (MOE) | Prédimensionnement poutres métalliques — enveloppe |
| 2026-10-31 | H-03 | Introduction (nouvelle hypothèse) | B-20 (MOE) | Contrainte design béton f_cd — valeur à confirmer R-08 |
| 2026-10-31 | H-06 | Introduction (nouvelle hypothèse) | B-21 (MOE) | Poids propre dallage — épaisseur MINI |
| 2026-10-31 | H-07 | Introduction (nouvelle hypothèse) | B-21 (MOE) | Poids propre chape et revêtement — valeur usuelle |
| 2026-10-31 | H-08 | Introduction (nouvelle hypothèse) | B-21 (MOE) | Poids propre isolation — valeur usuelle |
| 2026-10-31 | H-02 | Révision V1→V2 (L = 9 m → 9,68 m) | B-20 V2 (MOE) | Géométrie PROJECT : bay 1-2 = 9,68 m |
| 2026-10-31 | H-06 | Révision V1→V2 (L = 6 m → 5,64 m) | B-20 V2 (MOE) | Géométrie PROJECT : portée courte A-B/B-C = 5,64 m |
| 2026-10-31 | H-01 | Révision V1→V2 (justification adaptée) | B-20 V2 (MOE) | Géométrie PROJECT : section MINI inchangée |

---

## ÉCART V1 → V2

| Hypothèse | V1 (EXISTANT) | V2 (PROJECT) |
|---|---|---|
| H-02 — L poutres | 9 m | **9,68 m** (bay 1-2/2-3) |
| H-02 — h calculée | 450 mm | **484 mm** → 500 mm (enveloppe) |
| H-06 — L dallage | 6 m | **5,64 m** (A-B/B-C) |
| H-06 — épaisseur | 20 cm | **19 cm** → 20 cm (MINI) |
| H-01 — section poteaux | 30×30 cm | **30×30 cm** (inchangée) |
| H-04, H-05 | CONFIRMÉE | CONFIRMÉE (inchangée) |

**Conclusion** : les 8 hypothèses conservent leurs valeurs — les portées modifiées (V1→V2) conduisent aux mêmes arrondis aux dimensions nominales.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque hypothèse a un numéro unique et stable | ✅ H-01 à H-08 (numéros stables) |
| Chaque hypothèse a une justification | ✅ §Section 2 (justification pour chaque hypothèse) |
| Chaque hypothèse a un statut | ✅ §Section 1 (À CONFIRMER / CONFIRMÉE) |
| Aucune hypothèse n'a été supprimée | ✅ §Section 3 (historique complet) |
| L'historique des révisions est tenu | ✅ §Section 3 (11 révisions) |
| L'index en section 1 est cohérent avec le détail en section 2 | ✅ §Section 1 ↔ §Section 2 |
| Géométrie rattachée à B-20 V2 (PROJECT zone) | ✅ §Écart V1→V2 |

---

**Brique B-22 V2 exécutée en mode COMPLET — en attente de votre GO ou de nouvelles observations.**
La note d'hypothèses est **unique** — une seule note par projet. **6 hypothèses À CONFIRMER** (H-01, H-02, H-03, H-06, H-07, H-08) doivent être confirmées avant les briques de calcul B-40 à B-50. **2 hypothèses CONFIRMÉES** (H-04, H-05) par décisions D-06 et D-03.
