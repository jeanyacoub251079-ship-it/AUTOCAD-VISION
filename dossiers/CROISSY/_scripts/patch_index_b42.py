# -*- coding: utf-8 -*-
"""Mise à jour de 00_INDEX.md après livraison de B-42 (Ind. A) — Phase 4 ouverte.

À exécuter UNE SEULE FOIS : relancé sur un index déjà patché, il s'arrête sur
assert avant toute écriture.
"""
import io

P = "00_INDEX.md"
src = io.open(P, encoding="utf-8").read()
orig = src


def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, "occurrences %d (attendu %d) pour : %r" % (c, n, old[:70])
    src = src.replace(old, new)


# 1. En-tête
rep(
    "> **Mis à jour le 20/10/2026** — **`B-24` livrée en indice A** (mode PARAMÉTRIQUE, suffixe `_P`) : les **8 éléments existants non sondés** ont leur vérification littérale, `101` cas de sensibilité balayés, `6` campagnes d'essais listées. **La phase 3 est close.**",
    "> **Mis à jour le 20/10/2026** — **`B-42` livrée en indice A** : **première note de calcul d'exécution** (`P2`, `P3`, `J1` en béton armé), diagramme d'interaction `N-M` + flambement EC2, **8/8 CONFORME**. **La phase 4 est ouverte.** **`B-24` livrée en indice A** (mode PARAMÉTRIQUE, suffixe `_P`) : 8 éléments non sondés, `101` cas de sensibilité, 6 campagnes d'essais. **La phase 3 est close.**",
)

# 2. § 1 — compteurs
rep(
    "**À la date du 20/10/2026 : 22 notes documentaires CARNAC",
    "**À la date du 20/10/2026 : 23 notes documentaires CARNAC",
)

# 3. § 1 — ligne B-42 produite (en tête du tableau des productions)
rep(
    "| Cadrage `B-00 → B-04`",
    "| **Verticaux BA `B-42 Ind. A`** : `P2` `15 × 25` (`M_Ed/M_Rd = 0,400`), `P3` `50 × 40` et `J1` `24 × 50` (minimum réglementaire) — **6 HA12** partout, cadres `HA8 e150/e200`, débits `83,8 kg`. Réserves `R-42-1` à `R-42-5` | `06_CALCULS/` + `_rendus/` |\n"
    "| Cadrage `B-00 → B-04`",
)

# 4. § 1 — ce qui reste
rep(
    "| **`B-42`** (poteaux et jambages BA) · **`B-43`** (planchers et plancher haut) · **`B-44`** (charpente) · **`B-45`** (profilés métalliques) · **`B-46`** (maçonnerie existante) · **`B-47`/`B-49`** (escaliers, linteaux) · **`B-50`** (assemblages et ancrages) | **Phase 4 — notes de calcul d'exécution.** Premières notes opposables, sur `GO` ; `B-41` (fondations profondes) et `B-48` (prédalles) à déclarer `SANS OBJET` s'il n'y a ni pieu ni prédalle |",
    "| **`B-43`** (planchers et plancher haut) · **`B-44`** (charpente) · **`B-45`** (profilés métalliques) · **`B-46`** (maçonnerie existante) · **`B-47`/`B-49`** (escaliers, linteaux) · **`B-50`** (assemblages et ancrages) | **Phase 4 en cours** — `B-42` livrée. `B-41` (fondations profondes) et `B-48` (prédalles) à déclarer `SANS OBJET` s'il n'y a ni pieu ni prédalle |",
)

# 5. § 2 — ligne B-42 dans la chaîne
rep(
    "| **B-25** | `02_CONCEPTION/B-25_Stabilite_Globale.md` | **E** | **20/10/2026** | ✅ **CONFORME 6/6 applicables**",
    "| **B-42** | `06_CALCULS/B-42_Verticaux_BA.md` | **A** | **20/10/2026** | ✅ **CONFORME 8/8** — `P2` `15×25` seul porteur élancé (`lambda = 64,7`), `M_Ed/M_Rd = 0,400` · `P3` `0,014` · `J1` `0,016` · **6 HA12** partout · point dur : appui de `J1` sur maçonnerie (`0,62` à `f_k = 1,5 MPa`, `1,85` à `0,5`) |\n"
    "| **B-25** | `02_CONCEPTION/B-25_Stabilite_Globale.md` | **E** | **20/10/2026** | ✅ **CONFORME 6/6 applicables**",
)

# 6. § 3.1 — ligne B-42 (en tête des notes de calcul)
rep(
    "| `01_CADRAGE/B-03_RDR.md` | `68 858 o · 459 l.` |",
    "| `06_CALCULS/B-42_Verticaux_BA.md` | `18 080 o · 263 l.` | **Verticaux BA Ind. A** : diagramme d'interaction `N-M`, flambement EC2 § 5.8, ferraillage 6 HA12, débits, 5 réserves |\n"
    "| `01_CADRAGE/B-03_RDR.md` | `68 858 o · 459 l.` |",
)

assert src != orig
io.open(P, "w", encoding="utf-8").write(src)
print("OK — %d o (avant %d)" % (len(src.encode("utf-8")), len(orig.encode("utf-8"))))
