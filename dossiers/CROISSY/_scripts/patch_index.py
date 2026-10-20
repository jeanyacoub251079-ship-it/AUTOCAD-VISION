# -*- coding: utf-8 -*-
"""Mise en cohérence de 00_INDEX.md — état au 20/10/2026 (4e passe).

Aucune écriture si un remplacement ne tombe pas exactement une fois (assert).
À exécuter UNE SEULE FOIS : relancé sur un index déjà patché, il s'arrête sur
assert avant toute écriture.
"""
import io
import sys

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
    "> **Mis à jour le 20/10/2026** — **`B-25` en indice B** : `D-26` (aucune vérification sismique, zone 1) et `D-27` (stabilité en phase provisoire → MOE structure de conception) ; puis validation de la décision **D-25 (Articles P1 à P8 — Synthèse structurelle du dossier)** et à la refonte intégrale des vues nettoyées (`B-32 Ind. D`), de la synthèse structurelle (`B-20 Ind. B`) et de l'implantation des fondations (`B-40 Ind. E`).",
    "> **Mis à jour le 20/10/2026** — **`B-25` en indice E** : `D-29` consignée (le contreventement est assuré par la maçonnerie existante seule ; aucun renfort encastré ni triangulé) ; `B-25` ne porte plus aucun point ouvert. **`B-23` livrée en indice A** : les 9 désordres du diagnostic sont classés et les séquences de phasage `P-1` à `P-7` établies. **`B-03` en indice U** : 34 décisions.",
)

# 2. § 1 — compteurs
rep(
    "**À la date du 20/10/2026 : 18 notes documentaires CARNAC, 6 preuves de calage/superposition, et 18 fichiers de plans (`6 DXF + 6 PDF + 6 PNG = 22,2 Mo`)",
    "**À la date du 20/10/2026 : 21 notes documentaires CARNAC, 6 preuves de calage/superposition, et 21 fichiers de plans (`7 DXF + 7 PDF + 7 PNG = 27 Mo`)",
)

# 3. § 1 — indice du RDR
rep(
    "(dont `B-03` **Ind. P**, 25 décisions + Articles `P1 à P8`)",
    "(dont `B-03` **Ind. U**, 34 décisions + Articles `P1 à P8`)",
)

# 4. § 1 — ligne B-25
rep(
    "| **Stabilité globale `B-25 Ind. C`** : contreventement, torsion, régularité, joints + planche `FLORA_B25_CONTREVENTEMENT_IndE`. Sismique et stabilité provisoire **hors mission** (`D-26`, `D-27`) · **`D-28`** : aucun joint, consigné |",
    "| **Stabilité globale `B-25 Ind. E`** : contreventement par la maçonnerie existante seule (`D-29`), torsion, régularité, joints + planche `FLORA_B25_CONTREVENTEMENT_IndE`. Sismique et stabilité provisoire **hors mission** (`D-26`, `D-27`) · **`D-28`** : aucun joint, constaté |",
)

# 5. § 1 — briques restantes
rep(
    "| **`B-23`** (Exploitation du diagnostic) puis **`B-24`** (Existant non sondé) | Briques suivantes de Phase 3 — prêtes à démarrer sur `GO` |",
    "| **`B-24`** (Existant non sondé) | Brique suivante de Phase 3 — hérite des **5 zones hors relevé** identifiées par `B-23` ; prête à démarrer sur `GO` |",
)

# 6. § 3.1 — indice B-22
rep(
    "| **Note d'hypothèses Ind. A** : 30 hypothèses",
    "| **Note d'hypothèses Ind. B** : 30 hypothèses",
)

# 7. § 3.1 — indice B-25
rep(
    "Note de stabilité globale **Ind. C** (contreventement, torsion, régularité, joints)",
    "Note de stabilité globale **Ind. E** (contreventement, torsion, régularité, joints — `D-29` consignée)",
)

# 8. § 3.1 — ajout de l'annexe B-03 en tête de tableau (ordre des indices)
rep(
    "| `01_CADRAGE/B-03_RDR.md` | `68 858 o · 459 l.` | Registre vivant **Ind. U** : `D-01` à `D-34` + `D-29`, Articles `P1–P8`, registre des nuages `D-19` |\n",
    "| `01_CADRAGE/B-03_RDR.md` | `68 858 o · 459 l.` | Registre vivant **Ind. U** : `D-01` à `D-34` + `D-29`, Articles `P1–P8`, registre des nuages `D-19` |\n"
    "| `01_CADRAGE/B-03_Annexe_Hypotheses.md` | `37 653 o · 252 l.` | **Annexe hypothèses notifiées Ind. H** : 30 hypothèses, clause `D-34` (maçonnerie) mot pour mot, `D-33` régime `LECTURE` |\n",
)

# 9. § 3.2 — en-tête
rep(
    "### 3.2 Planches graphiques actives dans `_plans/` (18 fichiers — 22,2 Mo — audit `0 erreur` sur les 6 DXF)",
    "### 3.2 Planches graphiques actives dans `_plans/` (21 fichiers — 27 Mo — audit `0 erreur` sur les 7 DXF)",
)

# 10. § 3.2 — ligne B-25
rep(
    "| **B-32 Ind. D — Vue nettoyée structurelle R+1** | `FLORA_R1_VUE-NETTOYEE_IndD.dxf` (`2 672 677 o`) | `78 372 o` | `278 171 o` |\n",
    "| **B-32 Ind. D — Vue nettoyée structurelle R+1** | `FLORA_R1_VUE-NETTOYEE_IndD.dxf` (`2 672 677 o`) | `78 372 o` | `278 171 o` |\n"
    "| **B-25 Ind. E — Contreventement, torsion, régularité (`D-29`, `D-28`)** | `FLORA_B25_CONTREVENTEMENT_IndE.dxf` (`2 760 613 o`) | `901 519 o` | `1 075 802 o` |\n",
)

# 11. Sections de clôture : glossaire + points ouverts
if "## 4. GLOSSAIRE DES CODES" not in src:
    src = src.rstrip("\n") + "\n" + io.open(
        "_scripts/index_sections.md", encoding="utf-8"
    ).read()

assert src != orig
io.open(P, "w", encoding="utf-8").write(src)
print("OK — %d o (avant %d)" % (len(src.encode("utf-8")), len(orig.encode("utf-8"))))
