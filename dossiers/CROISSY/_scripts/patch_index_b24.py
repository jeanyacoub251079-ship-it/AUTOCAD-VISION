# -*- coding: utf-8 -*-
"""Mise à jour de 00_INDEX.md après livraison de B-24 (Ind. A, mode PARAMÉTRIQUE).

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
    "> **Mis à jour le 20/10/2026** — **`B-25` en indice E** : `D-29` consignée (le contreventement est assuré par la maçonnerie existante seule ; aucun renfort encastré ni triangulé) ; `B-25` ne porte plus aucun point ouvert. **`B-23` livrée en indice A** : les 9 désordres du diagnostic sont classés et les séquences de phasage `P-1` à `P-7` établies. **`B-03` en indice U** : 34 décisions.",
    "> **Mis à jour le 20/10/2026** — **`B-24` livrée en indice A** (mode PARAMÉTRIQUE, suffixe `_P`) : les **8 éléments existants non sondés** ont leur vérification littérale, `101` cas de sensibilité balayés, `6` campagnes d'essais listées. **La phase 3 est close.** **`B-25` en indice E** (`D-29` consignée, aucun point ouvert) · **`B-23` en indice A** (9 désordres classés) · **`B-03` en indice U** (34 décisions).",
)

# 2. § 1 — compteurs
rep(
    "**À la date du 20/10/2026 : 21 notes documentaires CARNAC, 6 preuves de calage/superposition, et 21 fichiers de plans (`7 DXF + 7 PDF + 7 PNG = 27 Mo`)",
    "**À la date du 20/10/2026 : 22 notes documentaires CARNAC (dont `B-24` en mode PARAMÉTRIQUE, suffixe `_P`), 6 preuves de calage/superposition, et 21 fichiers de plans (`7 DXF + 7 PDF + 7 PNG = 27 Mo`)",
)

# 3. § 1 — ligne B-24 produite
rep(
    "| **Stabilité globale `B-25 Ind. E`**",
    "| **Existant non sondé `B-24 Ind. A (_P)`** : 8 éléments en vérification littérale suspendue + 101 cas de sensibilité **non contractuels** + 6 campagnes d'essais. **Aucun élément conclu** | `02_CONCEPTION/` + `_rendus/` |\n"
    "| **Stabilité globale `B-25 Ind. E`**",
)

# 4. § 1 — ce qui reste
rep(
    "| **`B-24`** (Existant non sondé) | Brique suivante de Phase 3 — hérite des **5 zones hors relevé** identifiées par `B-23` ; prête à démarrer sur `GO` |\n"
    "| **`B-42` (Poteaux & jambages BA : `P2, P3, J1`) · `B-44` (Charpente) · `B-45` (Profilés métalliques `F1–F4, R1–R3, P1, Stab1`) · `B-46` (Maçonnerie existante) · `B-50` (Assemblages & ancrages)** | Calculs fins d'exécution EC2 / EC3 / EC5 séquencés après validation de `B-20 Ind. B` |\n",
    "| **`B-42`** (poteaux et jambages BA) · **`B-43`** (planchers et plancher haut) · **`B-44`** (charpente) · **`B-45`** (profilés métalliques) · **`B-46`** (maçonnerie existante) · **`B-47`/`B-49`** (escaliers, linteaux) · **`B-50`** (assemblages et ancrages) | **Phase 4 — notes de calcul d'exécution.** Premières notes opposables, sur `GO` ; `B-41` (fondations profondes) et `B-48` (prédalles) à déclarer `SANS OBJET` s'il n'y a ni pieu ni prédalle |\n",
)

# 5. § 2 — ligne B-24 dans la chaîne
rep(
    "| **B-25** | `02_CONCEPTION/B-25_Stabilite_Globale.md` | **E** |",
    "| **B-24** | `02_CONCEPTION/B-24_Existant_Non_Sonde_P.md` | **A (`_P`)** | **20/10/2026** | ✅ **CONFORME 7/7** — **8 éléments non sondés** · `101` cas de sensibilité **NON CONTRACTUEL** · **1 favorable** (`E-01` maçonnerie), **4 limites**, **2 défavorables** (`E-02`, `E-05`), **1 sans plage** (`E-07`) · **0 élément conclu** · 6 campagnes d'essais |\n"
    "| **B-25** | `02_CONCEPTION/B-25_Stabilite_Globale.md` | **E** |",
)

# 6. § 3.1 — ligne B-24 (après B-23)
rep(
    "| `02_CONCEPTION/B-23_Exploitation_Diagnostic.md` | `23 128 o · 198 l.` |",
    "| `02_CONCEPTION/B-24_Existant_Non_Sonde_P.md` | `21 832 o · 210 l.` | **Existant non sondé Ind. A (`_P`)** : 4 tableaux, 8 éléments, 101 cas de sensibilité, 6 essais — **note suspendue, non exécutable** |\n"
    "| `02_CONCEPTION/B-23_Exploitation_Diagnostic.md` | `23 128 o · 198 l.` |",
)

assert src != orig
io.open(P, "w", encoding="utf-8").write(src)
print("OK — %d o (avant %d)" % (len(src.encode("utf-8")), len(orig.encode("utf-8"))))
