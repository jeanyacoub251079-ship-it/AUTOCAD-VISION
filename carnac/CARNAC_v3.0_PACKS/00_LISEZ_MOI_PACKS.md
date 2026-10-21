# `CARNAC v3.0` — PACKS PRÊTS À COLLER DANS UNE DISCUSSION

**But** : permettre d'utiliser le carnet dans n'importe quelle discussion d'IA, sans jamais coller les 348 000 tokens du document compilé complet.

**Principe** : on colle **un socle de règles** une fois, puis **un seul pack de phase** au moment où l'on y arrive.

---

## 1. Les six packs

| Ordre | Fichier | Contenu | Poids |
|---|---|---|---|
| **1** | `00_SOCLE.md` | Document maître + annexes A, **A1 v3.0.1**, D, O + dictionnaire des 106 variables | **≈ 33 300 tokens** |
| 2 | `01_PHASE_0.md` | `B-00` à `B-04` — inventaire, `CFG-01`, MPD, `CFG-02`, FDC, `NIV-07`, RDR, PTD | ≈ 23 200 tokens |
| 3 | `02_PHASES_1-2.md` | `B-30`, `B-32`, `B-31` (calage, nettoyage, preuve) puis `B-10` à `B-15` (audits, contradictions, risques) | ≈ 54 200 tokens |
| 4 | `03_PHASE_3.md` | `B-20`, `B-25`, `B-21`, `B-22`, `B-23`, `B-24` — synthèse, stabilité globale, DDC, hypothèses | ≈ 35 400 tokens |
| 5 | `04_PHASE_4.md` | `B-40` à `B-50` — les onze notes de calcul d'exécution | ≈ 97 100 tokens |
| 6 | `05_PHASES_5-6.md` | `B-34`, `B-60`, `B-62`, `B-64`, `B-33`, `B-70` à `B-72` + annexe transverse `T-01` à `T-04` | ≈ 75 300 tokens |

**Total des six packs** : ≈ 320 000 tokens — mais vous n'en collez jamais plus de deux à la fois (socle + une phase), soit **de 56 000 à 130 000 tokens**.

---

## 2. Mode d'emploi en trois gestes

1. **Ouvrir la discussion** : coller `00_SOCLE.md` intégralement, puis écrire :
   > « Applique le carnet CARNAC joint, §0. Nouvelle affaire [code]. Accuse réception des pièces, puis exécute B-00 et arrête-toi. »
2. **Coller les pièces du projet** (PDF, DXF, CCTP…).
3. **À chaque changement de phase**, coller le pack correspondant — inutile de le coller avant.

> Le carnet fonctionne **une brique à la fois** (§0.2). L'IA n'a besoin que des règles et de la fiche en cours : coller toutes les fiches d'avance nuit à la tenue du protocole.

---

## 3. Deux coupures de confort

* **Pack `04_PHASE_4`** : un repère `COUPURE POSSIBLE` sépare `B-40`–`B-45` de `B-46`–`B-50`. Si votre contexte est limité, collez la première moitié, puis la seconde dans une autre discussion. Aucune règle ne dépend de la continuité du pack.
* **Pack `05_PHASES_5-6`** : un repère `COUPURE` isole l'annexe transverse `T-01` à `T-04`. Ne la collez que si vous invoquez l'un de ces prompts (sincérité, recadrage, méta-amélioration, demande de complément).

---

## 4. Ce que les packs ne contiennent pas — et pourquoi

| Fichier exclu | Raison |
|---|---|
| `10_ANNEXES/C_Journal_Revisions.md` | Historique des versions du carnet : utile pour la maintenance, inutile à la production |
| `11_HISTORIQUE/Journal_des_modifications.md` | Archive de traçabilité (entrées `v1.0` à `v3.0`) : aucun rôle opérationnel |
| `12_EXEMPLES/Exemples_Phase_0.md` | Exemples pédagogiques de la version `v1.1` : lecture de formation, pas d'exécution |

Ces trois fichiers restent disponibles dans l'arborescence (`08 — .zip`) et dans le document compilé complet (`07 — .md`).

---

## 5. Preuve d'intégrité

Les fichiers contenus dans les packs sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0`. Contrôle exécuté :

```text
Fichiers vérifiés : 49 · identiques : 49 · écarts : 0
Couverture : 49/52 fichiers Markdown de l'arborescence
Cohérence manifeste : 49 fichiers déclarés / 49 retrouvés
```

Le détail (`octets` + `SHA-256` par fichier) est dans **`PACKS_MANIFEST.json`**. Si vous modifiez une fiche source, régénérez les packs (`carnac/_tools/build_packs.py`) puis revérifiez (`carnac/_tools/verify_packs.py`) : ne corrigez jamais un pack à la main.

---

## 6. Règle d'or

> **Le pack est un véhicule, la fiche est la loi.** Entre les balises `**[Début du fichier : …]**` et `**[Fin de …]**`, le texte est celui du carnet. Toute correction se fait dans l'arborescence, jamais dans le pack.
