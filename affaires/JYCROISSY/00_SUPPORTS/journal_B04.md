# Journal d'exécution — B-04 PTD JYCROISSY (preuve d'exécution, verrous V3/V11/V14)

## 1. Chaîne de production (reproductible)

1. **Entrées** : MPD B-01 Ind B (validée), FDC B-02 (17 VERROU), RDR B-03
   (V-01…V-17, R-01…R-10), graphe de dépendances (briques consommatrices
   par variable — colonne « Bloque » du dictionnaire).
2. **Classification** : chaque brique du graphe est placée dans l'un des trois
   tableaux (suspendue / exécutable / PARAMÉTRIQUE) ou statuée SANS OBJET par
   la MPD.
3. **Exécution** : `python3 affaires/JYCROISSY/00_SUPPORTS/build_b04.py`
   (stdlib uniquement) → `PTD_JYCROISSY.md` + `PTD_jycroissy.csv`.

## 2. Validations automatiques (toutes passes)

* Aucune brique répétée dans le PTD (unicité sur l'ensemble des 39 briques).
* Chaque brique suspendue cite une donnée bloquante et une voie d'obtention.
* Chaque brique exécutable porte un mode valide (COMPLET / PARTIEL-DÉCLARÉ /
  INTERNE-GO) et un motif.
* Chaque PARAMÉTRIQUE précise la forme littérale et ce qui ne sera pas produit.
* Zéro placeholder `{{...}}` (V7).

## 3. Décompte final (39 briques)

| Statut | Nb |
|---|---:|
| Produites (phase 0) | 5 |
| Suspendues | 7 |
| Exécutables immédiatement | 23 |
| Exécutables en PARAMÉTRIQUE | 2 |
| SANS OBJET (fixé par la MPD) | 2 |
| **Total** | **39** |

## 4. Points de jugement majeurs (tracés)

* **Blocage local, jamais global (V11)** : 7 briques suspendues, 23 exécutables
  immédiatement — le projet continue.
* **INTERNE-GO ≠ suspendue** : B-30/B-31/B-32 (calage/recalage/nettoyage),
  B-22 (hypothèses H-xx), B-23/B-46 (contrainte existant), B-60 (conventions),
  B-71 (supersession) produisent eux-mêmes les données manquantes : exécutables
  en mode conception.
* **SANS OBJET réservé à la MPD** : B-41 (D-11) et B-48 (D-09) ; le PTD ne statue
  pas.
* **PARAMÉTRIQUE filigrané** : B-43/B-44 (livrables `_P`, non exécutables).
* **Aucune valeur de repli** : chaque blocage est résolu par production interne
  (INTERNE-GO) ou donnée externe (réserves R-xx), jamais par une valeur supposée.

## 5. Limites déclarées

* Le PTD est un instantané à l'ouverture de la phase 1 ; il est régénéré à chaque
  blocage (V12 : requalification NON BLOQUANTE → BLOQUANTE entraîne une nouvelle
  édition).
* Le classement des briques calculs (B-42…B-50) en COMPLET / PARTIEL-DÉCLARÉ
  repose sur le statut MPD des variables consommées (FOURNIE / Décision /
  À confirmer) ; une valeur « À confirmer » n'est pas une donnée manquante.

## 6. Porte suivante

La phase 1 est exécutable dès maintenant (B-30 → B-32 → B-31). Un **GO** explicite
déclenche la prochaine brique exécutable selon le PTD (par défaut B-10 audit CCTP
ou B-30 calage).
