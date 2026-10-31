# Journal d'exécution — B-03 RDR JYCROISSY (preuve d'exécution, verrous V3/V12/V14)

## 1. Chaîne de production (reproductible)

1. **Entrées** : MPD B-01 Ind B (validée), FDC B-02 (17 VERROU), pré-RDR
   (`../02_PHASE_0_CADRAGE/RDR_provisoire_en_attente_B03.md`, D-01…D-13, PA-01).
2. **Ouverture du RDR** à quatre registres (D-xx / H-xx / PA-xx / V-xx), avec
   reprise intégrale du pré-RDR **sans renumérotation** (consigné dans D-16).
3. **Exécution** : `python3 affaires/JYCROISSY/00_SUPPORTS/build_b03.py`
   (stdlib uniquement) → `RDR_JYCROISSY.md` + `RDR_jycroissy.csv`.

## 2. Validations automatiques (toutes passes)

* Unicité des numéros D-xx, R-xx, V-xx (assertions sur ensembles).
* Chaque D-xx a un auteur et une date ; chaque R-xx a un responsable et une date.
* Le registre V-xx reprend exactement les 17 VERROU de la FDC B-02.
* Chaque D-xx porte un effet sur les briques (sans effet → assertion).
* Zéro placeholder `{{...}}` (V7).

## 3. Décompte final

| Registre | Nb | Explication |
|---|---:|---|
| D-xx — Décisions | 16 | D-01…D-13 (CR 20/10/2026 + validation B-01) ; D-14 (MPD), D-15 (FDC), D-16 (ouverture RDR) |
| R-xx — Réserves | 10 | Actes d'attente (données à obtenir d'un tiers) |
| V-xx — Verrous | 17 | Les 17 VERROU de la FDC B-02 |
| H-xx — Hypothèses notifiées | 0 | Aucune (toutes les inconnues tranchées sont D-xx / PA-xx) |
| PA-xx — Points d'arrêt | 1 | PA-01 (contrôle d'arase de fouille) |

## 4. Points de jugement majeurs (tracés)

* **Aucune décision MOA/MOE prise à sa place** : la commande du G3 est une
  réserve R-02, non une décision. Seuls D-01…D-06 (CR officiel 20/10/2026) et
  D-07…D-16 (BET d'exécution / utilisateur) figurent en Section 1.
* **Un verrou ne se ferme que par entrée FDC ou décision Section 1** : V-17
  (NIV-07) est partiellement fermé (correspondance PB/PH entrée en FDC, D-13) ;
  les 16 autres restent ouverts.
* **Le registre des verrous liste ce qui a été fait malgré tout** : B-00, B-01,
  B-02, B-03 (cadrage) figurent comme briques exécutées malgré l'ouverture des
  verrous.
* **Registres séparés non interchangeables** (V3.0) : D-xx (décisions signées),
  H-xx (hypothèses sous nuage), PA-xx (arrêts chantier), V-xx (verrous).

## 5. Limites déclarées

* Le pré-RDR est un document de transition (B-00 Ind B) ; B-03 en reprend les
  lignes sans renumérotation. Toute décision future est appendue au RDR et datée.
* Les auteurs des décisions D-01…D-06 sont le CR officiel ; le modèle n'est
  jamais signataire d'une décision humaine.

## 6. Porte suivante

Un **GO B-04** explicite déclenche le Plan de travail dégradé (PTD), qui consume
les verrous (Section 3) et les réserves (Section 2) de ce RDR.
