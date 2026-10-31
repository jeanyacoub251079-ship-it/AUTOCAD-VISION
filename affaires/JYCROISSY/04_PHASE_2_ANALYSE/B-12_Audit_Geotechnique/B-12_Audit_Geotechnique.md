# B-12 — Audit des pièces géotechniques

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-12 (Phase 2 — Audit croisé multi-pièces)
**Date :** 2026-10-31
**Mode :** PARTIEL-DÉCLARÉ (paramètres G2 AVP transmis via D-06, mais G2 complet non reçu — R-01 ouverte)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| Rapport G2 AVP GEOEXPERTS n° 25.13646/ES/GIF (paramètres) | ✅ transmis via CR 20/10/2026 | Paramètres de dimensionnement : qELS ≤ 0,30 MPa ; qELU ≤ 0,49 MPa ; fondations ancrées de 50 cm dans les alluvions anciennes | Paramètres D-06 officiels |
| Rapport G2 complet (22/01/2026) | ❌ non reçu | — | R-01 ouverte (bug technique signalé par le client) |
| B-00 — Énoncé de mission | ✅ lue | §1 à §6 | Mission reformulée |
| B-01 — MPD | ✅ lue | SOL-01 à SOL-08 statuts | SOL-01 FOURNIE (D-06), SOL-04/06/07 NON NÉCESSAIRE (D-12) |
| B-03 — RDR | ✅ lue | D-06, D-12, PA-01 | Décisions déjà prises |
| B-10 — Audit CCTP | ✅ lue | Lacunes CCTP | Points à lever |
| B-11 — Audit diagnostic | ✅ lue | Données manquantes | Données EXI/GEO manquantes |

**Aucune donnée manquante inscrite sans cette preuve.** Chaque donnée manquante ci-dessous est rattaché à une pièce examinée ou à une décision RDR.

---

## TABLEAU 1 — DONNEES DISPONIBLES ET ADÉQUATION

| Code CARNAC | Libellé | Valeur citée | Unité | Référence rapport (§, tableau, page) | Adéquation (exploitable / insuffisante / ambiguë) |
|---|---|---|---|---|---|
| SOL-01 | Contrainte admissible ELS (qELS) | ≤ 0,30 | MPa | CR 20/10/2026 — paramètres G2 AVP GEOEXPERTS n° 25.13646/ES/GIF | Exploitable (paramètres D-06 officiels) |
| SOL-02 | Contrainte admissible ELU (qELU) | ≤ 0,49 | MPa | CR 20/10/2026 — paramètres G2 AVP GEOEXPERTS n° 25.13646/ES/GIF | Exploitable (paramètres D-06 officiels) |
| SOL-03 | Fondations ancrées dans les alluvions anciennes | ≥ 0,50 m | m | CR 20/10/2026 — paramètres G2 AVP ; D-01 | Exploitable (D-01/D-06) |
| SOL-08 | Mission géotechnique disponible | G2 AVP | — | CR 20/10/2026 ; D-12 | Insuffisante — G2 AVP ne suffit pas pour des calculs EXE ; G3 nécessaire |
| NIV-01 | Niveau TN précis | Variable (P1 p14) ; altimétrie Z ≈ 201 m | m | P1 p14 — diagnostic | Ambiguë — TN variable, altimétrie seule connue |
| STR-02 | Poussées des terres / écrans de soutènement | SANS OBJET | — | D-10 — périmètre = bâtiment Flora uniquement | SANS OBJET (D-10) |

---

## TABLEAU 2 — DONNEES MANQUANTES ET IMPACT

| Code CARNAC | Libellé | Impact sur nos calculs | Brique suspendue | Voie d'obtention proposée (essai / mission complémentaire / décision MOA) |
|---|---|---|---|---|
| SOL-01 | Contrainte admissible ELS (fourchette) | Calculs de fondations — dimensionnement des semelles | B-40 | Transmission du G2 complet (R-01) ou G3 (recommandation Tableau 3) |
| SOL-02 | Contrainte admissible ELU (fourchette) | Calculs de fondations — vérification ULTIME | B-40 | Transmission du G2 complet (R-01) ou G3 |
| SOL-04 | Géologie et stratigraphie détaillée | Vérification des assises — PA-01 | B-40, B-41 | Transmission du G2 complet ou G3 |
| SOL-05 | Essais in-situ / laboratoire | Vérification des paramètres de sol | B-40 | Essais complémentaires ou G3 |
| SOL-06 | Calcul de tassement | Vérification des fondations — D-12 : tassement délégué au géotechnicien | B-40 (délégué) | Mission G3 ou G4 |
| SOL-07 | Nappe phréatique | Aucune nappe phréatique confirmée — pas d'impact | — | Confirmation écrite du géotechnicien |
| NIV-01 | Niveau TN précis | Calculs des fondations — assises | B-40 | Géomètre expert (R-10) |
| STR-01 | Poussées des terres | SANT OBJET — périmètre = Flora uniquement (D-10) | — | SANS OBJET (D-10) |

---

## TABLEAU 3 — RECOMMANDATION DE MISSION

| Mission proposée | Base normative (NF P 94-500 et références) | Justification | Conséquence si non commandée (briques suspendues, réserves à porter) |
|---|---|---|---|
| G2 PRO (géotechnique pour exécution) | NF P 94-500 — mission de géotechnique pour exécution (G2 PRO) | Le G2 AVP fourni (paramètres D-06) ne suffit pas pour des calculs d'exécution ; un G2 PRO couvre la phase PRO/EXE | B-40 suspendu en COMPLET ; production en PARTIEL-DÉCLARÉ (paramètres D-06) ; PA-01 maintenu ; R-01 ouverte |
| G3 (géotechnique pour fondations) | NF P 94-500 — mission G3 (fondations) | La mission G3 couvre le dimensionnement des fondations et les assises ; le G2 AVP ne couvre pas cette phase | B-40 suspendu en COMPLET ; dimensionnement aux paramètres D-06 seulement ; PA-01 maintenu ; R-02 ouverte |
| Essais complémentaires (si G3 non commandée) | NF P 94-500 — essais in-situ et laboratoire | Si la MOA ne commande pas la G3, des essais complémentaires permettent de lever les inconnues géotechniques | B-40 suspendu en COMPLET ; paramètres D-06 seulement ; PA-01 maintenu |

---

## SYNTHÈSE (8 lignes maximum)

1. **Niveau de mission actuel** : G2 AVP (GEOEXPERTS n° 25.13646/ES/GIF) — paramètres transmis via CR 20/10/2026 (D-06). **Suffisance** : insuffisante pour des calculs d'exécution (EXE). Un G2 PRO ou G3 est nécessaire.
2. **Les trois données dont l'absence bloque le plus nos calculs** : (1) SOL-01/SOL-02 fourchette (qELS/qELU) — G2 complet non reçu (R-01) ; (2) SOL-04 stratigraphie détaillée — assises (PA-01) ; (3) SOL-06 calcul de tassement — délégué au géotechnicien (D-12).
3. **Recommandation de mission complémentaire** : G2 PRO ou G3 (NF P 94-500). **Impact planning** : si non commandée, B-40 reste en PARTIEL-DÉCLARÉ ; dimensionnement aux paramètres D-06 seulement ; PA-01 maintenu ; R-01/R-02 ouvertes.
4. **Paramètres D-06 officiels** : qELS ≤ 0,30 MPa ; qELU ≤ 0,49 MPa ; fondations ancrées de 50 cm dans les alluvions anciennes. Ces paramètres sont exploitables pour un dimensionnement documentaire (PARTIEL-DÉCLARÉ).
5. **Aucune valeur de calcul retenue** — B-12 cite ce que dit le rapport (paramètres D-06), jamais une valeur « retenue » par le modèle.
6. **SOL-04/SOL-06/SOL-07 NON NÉCESSAIRE** (D-12) — mission CARNAC = dimensionnement aux contraintes D-06 seulement, sans calcul de tassement ; tassement/assise délégués au géotechnicien.
7. **STR-01/STR-02 SANS OBJET** (D-10) — périmètre = bâtiment Flora uniquement ; Gardien/Bagatelle hors périmètre ; pas de sous-sol ni de soutènement.
8. **Alimentation aval** : B-12 alimente B-13 (contradictions), B-15 (synthèse des risques), B-40 (fondations), T-04 (demande de complément — recommandation de mission G2 PRO/G3).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Le niveau de mission est identifié avec sa référence normative | ✅ §Tableau 1 (G2 AVP, NF P 94-500) |
| Chaque donnée citée est rattachée à un paragraphe ou tableau du rapport | ✅ §Tableau 1 (CR 20/10/2026 — paramètres G2 AVP GEOEXPERTS) |
| Chaque donnée manquante est rattachée à son code CARNAC et à sa brique suspendue | ✅ §Tableau 2 (code CARNAC + brique suspendue) |
| La recommandation de mission cite sa base normative et la conséquence de sa non-commande | ✅ §Tableau 3 (NF P 94-500 + conséquence) |
| Aucune valeur de calcul n'a été retenue par toi | ✅ §Synthèse (citation des paramètres D-06, pas de valeur « retenue ») |
| La synthèse tient en 8 lignes | ✅ §Synthèse (8 lignes exactement) |
| Preuve d'épuisement produite | ✅ §0 (pièces lues, passages, résultat par pièce) |

---

**Brique B-12 exécutée en mode PARTIEL-DÉCLARÉ — en attente de votre GO ou de nouvelles observations.**
Conformément à la méthode, aucune valeur de calcul n'a été retenue par le modèle. **La recommandation de mission G2 PRO ou G3 doit être portée à la MOA** (T-04). Si la mission n'est pas commandée, B-40 reste en PARTIEL-DÉCLARÉ avec les paramètres D-06, et PA-01 est maintenu.
