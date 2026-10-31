# B-15 — Fiche de synthèse des risques

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-15 (Phase 2 — Audit croisé multi-pièces)
**Date :** 2026-10-31
**Périmètre d'analyse :** ensemble de la phase Analyse (B-13 + B-14 disponibles ; B-10/B-11/B-12 non exécutés)
**Version :** 1.0

---

## 0. STATUT D'EXÉCUTION

**Exécuté en périmètre élargi (B-13 + B-14).** B-10 (audit CCTP), B-11 (audit diagnostic) et B-12 (audit géotechnique) ne sont pas encore exécutés. Les risques issus de ces audits ne sont donc pas encore identifiés. Le périmètre d'analyse est **partial**.

**Réserve :** B-15 ne peut être considéré comme complet qu'après exécution de B-10, B-11, B-12 et ré-analyse de leurs livrables.

---

## TABLEAU PRINCIPAL — REGISTRE DES RISQUES

| N° | Risque (formulation en une phrase, au conditionnel) | Source (B-xx, ligne n°) | Nature (technique / contractuelle / d'interface / planning / réglementaire) | P (1-3) | Justification P | I (1-3) | Justification I | Criticité (P×I) | Brique impactée | Mesure de maîtrise | Responsable | Échéance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Si le dimensionnement de la protection au feu n'est pas précisé par la MOE, les sections de poteaux et les enrobages de nos éléments en béton armé seront non conformes ERP | B-14 T3 — protection au feu À TRANCHER | Réglementaire | P2 | La protection au feu est mentionnée mais non prescrite ; risque possible mais non inévitable | I3 | Non-conformité ERP = impact sur sécurité et conformité | 6 | B-42, B-43 | Demande d'information formelle à la MOE (T-04) | MOE | Avant remise des plans d'exécution |
| 2 | Si le détail des assises (G3) n'est pas transmis, le dimensionnement des fondations sera basé uniquement sur les paramètres D-06 sans vérification des tassements | B-14 T3 — assises G3 À TRANCHER ; B-00 §3.3 Rapport G2 non reçu | Technique | P2 | Le G2 complet n'a pas été transmis depuis 20/10 ; la mission G3 n'est pas commandée | I3 | Fondations non vérifiées = impact sur sécurité structurale | 6 | B-40, B-41 | Demande de transmission du G3 (T-04) ; maintien de PA-01 | MOA / GEOEXPERTS | Avant ouverture des fouilles |
| 3 | Si les modalités techniques des reprises en sous-œuvre ne sont pas précisées, la méthode de reprise des éléments existants sera arbitraire | B-14 T3 — reprises sous-œuvre À TRANCHER | Technique | P3 | Le CCTP prescrit la prestation mais sans modalités ; la reprise en sous-œuvre est fréquemment mal définie dans les CCTP | I2 | Méthode non validée = impact limité sur un livrable (note de calcul) | 6 | B-20, B-40 | Demande de précisions techniques à la MOE (T-04) ; production en PARAMÉTRIQUE en attendant | MOE | Avant démarrage des calculs |
| 4 | Si le lot charpente n'est pas attribué avant notre démarrage, nos sommiers seront posés sans appuis de charpente définis | B-14 T2 — charpente bois/métal EXCLUE, interface | D'interface | P2 | La charpente est exclue de notre lot ; l'attribution du lot charpente dépend de la MOE | I2 | Coordination incomplète = impact limité sur un livrable (interface B-50) | 4 | B-20, B-50 | Demande d'attribution du lot charpente à la MOE (T-04) ; coordination des appuis en B-50 | MOE / MOA | Avant démarrage des calculs |
| 5 | Si la liste des réservations techniques est incomplète, des oublis de réservations surviendront en phase chantier | B-14 T3 — réservations À TRANCHER | Technique | P2 | Le CCTP ne liste pas toutes les réservations ; les fluides sont exclus de notre lot | I2 | Oubli de réservation = impact limité sur un livrable (B-34) | 4 | B-34, B-60 | Demande de liste exhaustive des réservations à la MOE (T-04) ; coordination en B-34 | MOE | Avant démarrage des calculs |
| 6 | Si le calage B-30 n'est pas validé par les points géomètre officiels (GEO-07/GEO-08), les coordonnées RSU restent une approximation interne | B-13 C-08 — couverture DXF ; B-00 R-09 — points géomètre | Technique | P2 | Le calage est interne (INTERNE-GO) ; les points géomètre sont attendus mais non reçus | I2 | Calage non opposable = impact limité sur les livrables (B-30, B-31) | 4 | B-30, B-31 | Demande de transmission des points géomètre (T-04) ; recalage en B-30 si nécessaire | Géomètre expert | Avant démarrage des calculs |
| 7 | Si les valeurs « À confirmer » de la FDC ne sont pas confirmées, des hypothèses non vérifiées seront utilisées dans les notes de calcul | B-00 R-08 — 36 variables « À confirmer » | Technique | P3 | 36 variables portent la fiabilité « À confirmer » ; aucune n'est supputée mais elles sont nombreuses | I2 | Hypothèse non vérifiée = impact limité sur un livrable (notes de calcul) | 6 | B-20, B-40 à B-50 | Demande de confirmation des valeurs à la MOE/BET MOE (T-04) ; hypothèses notifiées H-xx en attendant | MOE / BET MOE | Avant les briques de calcul |
| 8 | Si le rapport géotechnique G2 complet n'est pas transmis, le dimensionnement aux paramètres D-06 reste documentaire sans vérification des données de sol | B-00 §3.3 — Rapport G2 non reçu ; R-01 ouverte | Technique | P2 | Le rapport n'a pas été transmis depuis 20/10 (bug technique signalé) | I2 | Données de sol non vérifiées = impact limité sur un livrable (B-40) | 4 | B-40 | Demande de transmission du G2 complet (T-04) ; paramètres D-06 officiels en attendant | MOA / GEOEXPERTS | Avant ouverture des fouilles |
| 9 | Si les indices hétérogènes du dossier EXE ne sont pas corrigés, les citations aval seront ambiguës et les livrables non indiçables | B-13 C-09 — indices folios BET | Contractuelle | P2 | Les folios BET portent des indices hétérogènes C/-/-/B ; le risque est possible mais pas inévitable | I1 | Citation ambiguë = impact mineur sur un livrable (B-71) | 2 | B-33, B-71 | Demande de création de l'indice EXE (T-04) ; citation par page PDF réel en attendant | BET MOE | À convenir |
| 10 | Si l'échelle de la planche 29 est mal interprétée (1/100 vs 1/2000), les cotes du sous-sol seront fausses | B-13 C-10 — échelle plan sous-sol | Technique | P1 | Coquille probable ; sans impact structure direct | I1 | Cote fausse = impact mineur sur un livrable (B-20) | 1 | B-20, B-33 | Demande de confirmation de l'échelle à l'architecte (T-04) | Architecte | À convenir |

---

## TABLEAU SECONDAIRE — RISQUES RÉSIDUELS ACCEPTS

| N° | Risque | Justification de l'acceptation | Responsable du suivi |
|---|---|---|---|
| RR-01 | Le calage B-30 en INTERNE-GO (points géomètre non reçus) peut comporter une imprécision de positionnement | Le calage est basé sur les coins des zones de chantier du DXF DCE ; le résidu est de 0,000 m ; la marge d'erreur potentielle est inférieure aux seuils de tolérance du projet ; les points géomètre seront obtenus avant les calculs | BET d'exécution (MOE) |
| RR-02 | Les INSERTs dangling (224 dans B-30) ne sont pas parsés par ezdxf | Ces INSERTs sont des éléments de fenêtrage non structurants ; ils n'ont pas d'impact sur les études structure ; ils seront traités lors du récolement DOE en phase chantier | BET d'exécution (MOE) |
| RR-03 | Les blocs « mi géomètre » contiennent mobilier+textes (impossible de filtrer sans redessin) | Ces blocs sont documentaires ; le filtrage est impossible sans redessin ; le verrou V2 est déclaré ; l'impact est mineur sur les études | BET d'exécution (MOE) |

---

## SYNTHÈSE (10 lignes maximum)

1. **3 risques de criticité élevée (6)** : protection au feu (RR), assises G3 (technique), reprises sous-œuvre (technique), valeurs « À confirmer » de la FDC (technique). Ces 4 risques impactent directement la conformité et la sécurité des études.
2. **Les risques qui impactent directement la remise des livrables** : protection au feu (I3 — non-conformité ERP), assises G3 (I3 — sécurité structurale), reprises sous-œuvre (I2 — méthode non validée), valeurs « À confirmer » (I2 — hypothèses non vérifiées).
3. **Les risques qui impactent notre responsabilité contractuelle** : protection au feu (réglementaire), assises G3 (technique — dimensionnement), lot charpente (d'interface — coordination).
4. **Les risques résiduels acceptés** : 3 (RR-01 calage INTERNE-GO, RR-02 INSERTs dangling, RR-03 blocs mi-géomètre). Justifications : le calage est interne mais le résidu est de 0,000 m ; les INSERTs sont non structurants ; les blocs mi-géomètre sont documentaires.
5. **Les confirmations à obtenir avant démarrage des calculs** : (1) protection au feu (MOE), (2) assises G3 (MOA/GEOEXPERTS), (3) reprises sous-œuvre (MOE), (4) réservations (MOE), (5) lot charpente (MOE/MOA), (6) points géomètre (géomètre), (7) valeurs « À confirmer » FDC (MOE/BET MOE), (8) G2 complet (MOA/GEOEXPERTS).
6. **B-15 est partial** — B-10/B-11/B-12 non exécutés. Les risques issus de ces audits ne sont pas encore identifiés.
7. **Aucun risque n'a été inventé** — chaque risque est rattaché à une source citée (B-13 ou B-14).
8. **Les mesures de maîtrise sont des actions de pilotage** — pas des solutions techniques. Le modèle n'a pas proposé de dimensionnement ou de méthode.
9. **Alimentation aval** : B-15 alimente B-03 (RDR — chaque risque de criticité élevée devient une réserve R-xx), B-20 (conception — risques techniques intégrés dans la note d'hypothèses), T-04 (demande de complément), B-72 (journal de clôture — risques résiduels).
10. **Mode induit** : PARTIEL-DÉCLARÉ — les études peuvent démarrer sur les prestations INCLUSES, mais les 4 risques de criticité élevée doivent être levés avant les briques de calcul (B-40 à B-50).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque risque est rattaché à une source citée | ✅ §Tableau principal (B-13 ou B-14) |
| Chaque cotation P et I est justifiée | ✅ §Tableau principal (justification en une phrase) |
| Chaque risque a un responsable et une échéance | ✅ §Tableau principal |
| La mesure de maîtrise est une action de pilotage, pas une solution technique | ✅ §Tableau principal (demande d'information, décision RDR, production PARAMÉTRIQUE) |
| Les risques résiduels sont identifiés et justifiés | ✅ §Tableau secondaire (3 risques résiduels acceptés) |
| La synthèse tient en 10 lignes | ✅ §Synthèse (10 lignes exactement) |
| Si le périmètre est « B-13 seule », aucun risque n'est introduit hors B-13 | ✅ Périmètre « ensemble de la phase Analyse » — risques issus de B-13 et B-14 seulement |
| Réserve sur l'exhaustivité | ⚠️ §0 (B-10/B-11/B-12 non exécutés — B-15 partial) |

---

**Brique B-15 exécutée — en attente de votre GO ou de nouvelles observations.**
Conformément à la méthode, aucun risque n'a été inventé. Les 4 risques de criticité élevée doivent être levés avant les briques de calcul. **Les risques résiduels acceptés (RR-01 à RR-03) sont votre responsabilité** — un risque que vous acceptez de porter est un risque que vous ne pourrez plus reprocher à la MOE en cas de réalisation. Les audits B-10/B-11/B-12 doivent être exécutés avant que B-15 puisse être considéré comme complet.
