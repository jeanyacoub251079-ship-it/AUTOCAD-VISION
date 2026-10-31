# B-14 — Clarification du périmètre de lot

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-14 (Phase 2 — Audit croisé multi-pièces)
**Date :** 2026-10-31
**Mode :** PARTIEL-DÉCLARÉ
**Version :** 1.0

---

## 0. STATUT D'EXÉCUTION

**Exécuté en mode PARTIEL-DÉCLARÉ.** B-14 requiert B-10 (audit CCTP) et B-11 (audit diagnostic) comme entrées amont. Ces briques **ne sont pas encore exécutées**. La matrice est construite à partir de B-00 (énoncé de mission), B-01 (MPD validée), B-13 (contradictions qualifiées) et du CCTP directement. Les constats d'audit B-10/B-11 ne sont pas encore disponibles — certaines attributions peuvent comporter des ambiguïtés non encore levées.

**Réserve :** B-14 ne peut être considéré comme complet qu'après exécution de B-10 et B-11, et ré-analyse de leurs livrables.

---

## TABLEAU 1 — PRESTATIONS INCLUSES dans notre lot

| Prestation | Article CCTP (réf. exacte) | Ce que cela implique techniquement | Brique CARNAC qui validera | Points à lever (si prescription incomplète) |
|---|---|---|---|---|
| Démolitions structurelles représentées (reprises, frangements, percements, rebouchages) | CCTP §01.2.1 — périmètre gros œuvre | Transcription graphique des reprise en sous-œuvre, frangements de poteaux, percements de murs porteurs, rebouchages | B-20, B-60 | — |
| Renforts métalliques (tubes carrés, profilés) | CCTP §01.2.1 — périmètre gros œuvre ; P1 p23 (poteau P1, section 14×14 cm — D-02) | Renforts de poteaux et linteaux en structure métallique, ferraillage des appuis | B-45, B-50 | — |
| Réalisation en béton armé (semelles, poteaux, linteaux, dalles) | CCTP §01.2.1 — périmètre gros œuvre | Coffrage, ferraillage, coulage de tous les éléments en béton armé du gros œuvre | B-40, B-42, B-43, B-49 | — |
| Fondations superficielles (ancrage ≥ 0,50 m — D-01/D-06) | CCTP §01.2.1 ; P1 p13 | Semelles filantes et semelles isolées, ancrage dans les alluvions anciennes | B-40 | — |
| Dallages et planchers (réfection, renforcement) | CCTP §01.2.1 — périmètre gros œuvre | Dallages existants repris ou renforcés ; planchers existants re-vérifiés sous 250 daN/m² (D-03) | B-43, B-21 | — |
| Élévations maçonnerie et béton armé (RDC + R+1) | CCTP §01.2.1 — périmètre gros œuvre | Murs et poteaux en maçonnerie et BA, élévation du R+1 | B-42, B-46 | — |
| Réservations pour coordination (fluides, CVC, électricité) | CCTP §01.2.1 — périmètre gros œuvre | Réservations dans les éléments en béton armé pour passage des fluides techniques | B-34, B-60 | — |
| Linteaux et seuils | CCTP §01.2.1 — périmètre gros œuvre | Linteaux en béton armé et en maçonnerie, seuils de portes et fenêtres | B-49 | — |
| Escaliers (réfection, adaptation) | CCTP §01.2.1 — périmètre gros œuvre | Escaliers existants repris ou adaptés | B-47 | — |
| Auto-contrôle et récolement DOE (DXF/DWG) | CCTP §01.2.1.1.6 — mission EXE/PAC | Auto-contrôle des études, récolement des plans en DXF/DWG | B-70, B-72 | — |

---

## TABLEAU 2 — PRESTATIONS EXCLUES de notre lot

| Prestation | Pièce qui l'attribue à un autre lot (réf.) | Lot pressenti | Interface éventuelle avec notre lot |
|---|---|---|---|
| Charpente bois (existante et neuve) | B-00 §4 — exclusion explicite : « charpente bois » non inclus dans le périmètre | Lot charpente | Appuis de charpente sur nos sommiers (interface B-50) |
| Charpente métallique (neuve) | B-00 §4 — exclusion explicite | Lot charpente métallique | Appuis de charpente métallique sur nos éléments (interface B-50) |
| Second œuvre de distribution (cloisons, doublages) | CARNAC — loi d'airain graphique : zéro cloison, zéro isolant | Lot second œuvre | Réservations dans nos éléments pour fixations (interface B-34) |
| Thermique et acoustique | B-00 §4 — exclusion explicite | Lot isolation | Épaisseurs de murs pour isolation (interface B-46) |
| Fluides (CVC, électricité, plomberie) | B-00 §4 — exclusion explicite | Lots techniques | Réservations dans nos éléments en béton (interface B-34) |
| VRD ( voirie, réseaux divers) | B-00 §4 — exclusion explicite | Lot VRD | Emprise au sol, ancrages extérieurs (interface B-40) |
| Étanchéité toiture | B-00 §4 — exclusion explicite | Lot étanchéité | Appuis sur murs gouttereaux (interface B-46) |
| Menuiseries (portes, fenêtres) | CARNAC — loi d'airain graphique : zéro menuiserie de distribution | Lot menuiserie | Pose dans les baies et les seuils (interface B-49) |

---

## TABLEAU 3 — PRESTATIONS À TRANCHER

| Prestation | Pièce(s) en cause (réf.) | Nature de l'ambiguïté | Lot pressenti | Conséquence pour nos études | Destinataire pour trancher |
|---|---|---|---|---|---|
| Périmètre Gardien/Bagatelle | B-13 C-07 — fermée par D-10 | — | — | Aucune — C-07 fermée par D-10 (Gardien/Bagatelle hors périmètre CARNAC) | — |
| Protection au feu (dimensionnement) | B-00 §4 — exclusion explicite, mais mention seule | Silence — CCTP mentionne mais ne prescrit pas | Lot GO ou spécialisé | Si la protection au feu doit être dimensionnée, cela impacte les sections et les enrobages | MOE |
| Assises des fondations (détail G3) | B-00 §3.3 — Rapport G2 non reçu ; R-01 ouverte | Silence — le G2 complet n'a pas été transmis | Géotechnicien | Détail des assises non borné ; dimensionnement aux paramètres D-06 seulement | MOA / GEOEXPERTS |
| Reprises en sous-œuvre (modalités techniques) | CCTP §01.2.1 — périmètre gros œuvre, mais modalités non détaillées | Silence — CCTP prescrit mais sans modalités techniques | Lot GO | Modalités de reprise inconnues (passes alternées ? fases ?) | MOE |
| Réservations techniques (liste exhaustive) | CCTP §01.2.1 — périmètre gros œuvre, mais liste non exhaustive | Silence — CCTP ne liste pas toutes les réservations | Lots techniques / Lot GO | Liste des réservations incomplète — risque d'oubli en phase chantier | MOE |

---

## TABLEAU 4 — Hors périmètre CARNAC (à titre documentaire)

| Prestation | Motif de l'exclusion (référence aux exclusions du carnet) |
|---|---|
| Désamiantage | B-00 §4 — exclusion explicite ; DOC-07 SANS OBJET (D-08) |
| Déplombage | B-00 §4 — exclusion explicite |
| Curage / démolition (mode opératoire et phasage) | B-00 §4 — exclusion explicite |
| Espaces verts | B-00 §4 — exclusion explicite |
| Dimensionnement protection au feu | B-00 §4 — exclusion explicite (mention seule) |
| Fluides / CVC / électricité / VRD | B-00 §4 — exclusion explicite (réservations/attentes seules) |
| Thermique et acoustique | B-00 §4 — exclusion explicite |
| Études géotechniques G1 à G3 | B-00 §4 — exclusion explicite |

---

## SYNTHÈSE (10 lignes maximum)

1. **10 prestations INCLUSES** dans notre lot gros œuvre/structure, prescrites par le CCTP §01.2.1 — la plus engageante est la réalisation en béton armé (semelles, poteaux, linteaux, dalles) qui conditionne toute la chaîne de calcul B-40 à B-43.
2. **8 prestations EXCLUES** — la charpente bois et la charpente métallique sont les plus critiques en termes d'interface : leurs appuis sur nos sommiers doivent être coordonnés (B-50).
3. **5 prestations À TRANCHER** — la plus critique est la protection au feu : si le CCTP impose un dimensionnement, cela impacte les sections et les enrobages de tous nos éléments en béton armé (B-42, B-43).
4. **0 prestation bloquante** — C-07 (Gardien/Bagatelle) est fermée par D-10. Aucune attribution n'est bloquante pour le démarrage des études.
5. **5 confirmations à obtenir avant démarrage des études** : (1) dimensionnement protection au feu (MOE), (2) détail des assises G3 (MOA/GEOEXPERTS), (3) modalités des reprises en sous-œuvre (MOE), (4) liste exhaustive des réservations (MOE), (5) confirmation des interfaces charpente (lot charpente).
6. **B-14 est partial** — B-10 et B-11 ne sont pas encore exécutés. Les constats d'audit CCTP et de diagnostic ne sont pas encore disponibles.
7. **Les prestations hors périmètre CARNAC** (désamiantage, déplombage, curage, espaces verts, protection au feu, fluides, VRD, thermique, acoustique, géotechnique) sont listées en tableau séparé — leur attribution à un lot est une décision MOE.
8. **Aucune attribution n'a été tranchée** par le modèle — toutes les incertitudes sont listées en À TRANCHER avec destinataire.
9. **Alimentation aval** : B-14 alimente B-15 (synthèse des risques), B-03 (RDR — les prestations À TRANCHER deviennent des réserves R-xx), T-04 (demande de complément).
10. **Mode induit** : PARTIEL-DÉCLARÉ — les études peuvent démarrer sur les prestations INCLUSES, mais les prestations À TRANCHER doivent être levées avant les briques de calcul (B-40 à B-50).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque prestation INCLUSE cite l'article du CCTP qui la prescrit | ✅ §Tableau 1 (CCTP §01.2.1) |
| Chaque prestation EXCLUE cite la pièce qui l'attribue à un autre lot | ✅ §Tableau 2 (B-00 §4, CARNAC loi d'airain) |
| Chaque prestation À TRANCHER identifie la nature de l'ambiguïté et un destinataire | ✅ §Tableau 3 (nature + destinataire) |
| Aucune attribution n'a été tranchée par le modèle | ✅ §Tableaux 1-3 (les incertitudes sont listées, jamais résolues) |
| Les prestations hors périmètre CARNAC sont dans un tableau séparé | ✅ §Tableau 4 |
| La synthèse tient en 10 lignes | ✅ §Synthèse (10 lignes exactement) |
| Réserve sur l'exhaustivité | ⚠️ §0 (B-10/B-11 non exécutés — B-14 partial) |

---

**Brique B-14 exécutée en mode PARTIEL-DÉCLARÉ — en attente de votre GO ou de nouvelles observations.**
Conformément à la méthode, aucune attribution n'a été tranchée. Les 5 prestations À TRANCHER doivent être levées avant les briques de calcul. **La confirmation des interfaces charpente est la plus critique** — les appuis de charpente sur nos sommiers doivent être coordonnés dès la conception (B-20, B-50). Les audits B-10 et B-11 doivent être exécutés avant que B-14 puisse être considéré comme complet.
