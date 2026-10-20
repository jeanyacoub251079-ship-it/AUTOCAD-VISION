# B-32 — VUE NETTOYÉE STRUCTURELLE PAR LIVRABLE

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-32** — Vue nettoyée par livrable |
| Phase | **3 — Calage et vérification** |
| Mode d'appel | **COMPLET** — fichier source vectoriel AC1032 exploitable |
| Régime | **OUTILLÉ (V13)** — script exécuté, journal consigné, audit `0 erreur`, relecture visuelle des PNG |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Fichier source `DOC-02` | `google_drive/208_FLORA_Plans_DCE_IndC.dxf` — AC1032, 4 399 016 o, `$INSUNITS = 5` (cm) |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b32_vue_nettoyee.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b32_vue_nettoyee.txt` |
| **Livrables produits** | `_plans/FLORA_RDC_VUE-NETTOYEE_IndD.dxf` · `.pdf` · `.png` et `_plans/FLORA_R1_VUE-NETTOYEE_IndD.dxf` · `.pdf` · `.png` |
| **Indice** | **D** *(remplace et annule l'indice C du 19/10/2026 — suppression intégrale des cloisons et de l'isolation)* |
| Date | **20/10/2026** |
| Briques alimentées | **B-20 Ind. B** (synthèse structurelle) · **B-40 Ind. E** (implantation des fondations) · **B-60** (plans d'exécution) |

---

## 1. MOTIF DE LA RÉVISION INDICE D — DOCTRINE STRUCTURELLE STRICTE

Lors de la revue des plans sur Google Drive le 20/10/2026, le client a relevé à juste titre que **toutes les planches issues de l'indice C laissaient encore apparaître les cloisons de distribution et les complexes d'isolation thermique périphérique**.

**Diagnostic technique exact de l'anomalie dans `208_FLORA_Plans_DCE_IndC.dxf` :**
1. Les cloisons légères ET l'intégralité des blocs dynamiques d'isolant thermique / doublage (`*U40` à `*U1219`, 133 entités au RDC et 102 au R+1) sont portés par les calques **`020_cloi`** et **`020_cloisons`** ;
2. Piège interne au DXF architecte : dans certains cadres, la référence `INSERT` du bloc de fond des murs porteurs (`Murs porteurs selon geometre projet` / `R+1 Projet`) était elle-même affectée au calque `'0'` ou `'020_cloi'`, tandis que les murs porteurs à l'intérieur du bloc sont sur **`010_mur`**. Supprimer `020_cloi` sans reclasser au préalable cet `INSERT` aurait détruit les murs porteurs ; conserver `020_cloi` polluait tout le plan ;
3. En outre, `030_menuiserie` portait 26 portes intérieures de cloisons au RDC (12 au R+1), `070_trait-fin` portait des équipements de kitchenette (`evier petit`, `Range-Oven`), et `075_cotation` portait 47 cotes de cloisons au RDC (32 au R+1) qui flottaient au milieu des plateaux une fois les cloisons retirées.

**Correction exécutée en Indice D (`b32_vue_nettoyee.py`) :**
- Reclassement préalable des références `INSERT` de `Murs porteurs selon geometre projet` (RDC) et `R+1 Projet` (R+1) sur `010_mur` ;
- **Purge intégrale (`0 entité` restante, vérifiée par assertion automatique)** de **`020_cloi`** et **`020_cloisons`** tant en espace objet qu'à l'intérieur des blocs ;
- Filtrage géométrique exact (`distance au plus proche segment 010_mur ≤ 22 cm`) sur **`030_menuiserie`** (seules les fenêtres/baies dans les murs porteurs subsistent ; **toutes** les portes intérieures de cloisons disparaissent) et sur **`075_cotation`** (seules les vraies portées nu-à-nu entre murs porteurs subsistent : `496, 512, 354, 484, 482, 361, 234 cm`) ;
- Découpe propre du mur de clôture parcellaire hors bâtiment tout en conservant au Nord l'amorce de la **passerelle château** (`D2 Folio 04`).

---

## 2. TABLEAU DE NETTOYAGE CONSOLIDÉ (INDICE D)

| Calque | Décision Indice D | Justification d'ingénieur structure |
|---|---|---|
| **`010_mur`** | **CONSERVÉ** *(recadré bâti)* | Murs porteurs existants en moellons et briques (relevé géomètre) — contours et hachures intacts |
| **`030_menuiserie`** | **FILTRÉ (`d ≤ 22 cm` de `010_mur`)** | Conserve uniquement les baies dans les murs porteurs (indispensables aux linteaux `R3`, `P1`, `P2`) ; élimine 100 % des portes de cloisons |
| **`070_trait-fin`** | **FILTRÉ *(escalier, seuils, Nord, passerelle)*** | Conserve la trémie et les volées d'escalier (`1..20`) + la flèche Nord ; élimine éviers, cuisinières et symboles PMR |
| **`075_cotation`** | **FILTRÉ *(2 attaches sur `010_mur`, `≥ 160 cm`)*** | Conserve uniquement les portées structurelles entre murs porteurs ; zéro cote flottante de cloison |
| **`020_cloi` · `020_cloisons`** | **SUPPRIMÉ (`0 entité`)** | Cloisons de distribution et complexes d'isolation thermique / doublage — non porteurs, polluants |
| **`102_demol`** | **SUPPRIMÉ du fond muet** *(projeté à part sur `B-20`)* | Retiré de la vue nettoyée de base ; projeté en calque dédié `ARCHI-DEMOL` sur la Planche 1 de `B-20 Ind. B` |
| **Tous autres calques (16)** | **SUPPRIMÉS (`0 entité`)** | Mobilier (`040`), sols (`050`), faux-plafonds (`051`), textes pièces/finitions (`077–079`), CVC/plomberie (`080`), surfaces (`091–092`), PMR (`100`), sanitaires (`31`) |

---

## 3. COMPTAGES VÉRIFIÉS PAR EXÉCUTION (`b32_vue_nettoyee.txt`)

| Métrique | RDC (`Ind. D`) | R+1 (`Ind. D`) |
|---|---|---|
| Fichier DXF généré | `FLORA_RDC_VUE-NETTOYEE_IndD.dxf` (2 719 320 o) | `FLORA_R1_VUE-NETTOYEE_IndD.dxf` (2 672 677 o) |
| Audit `ezdxf` | **0 erreur** | **0 erreur** |
| Entités initiales dans le cadre | 775 | 550 |
| Bloc porteur nettoyé en interne | **85 conservées** / 258 initiales (173 purgées) | **97 conservées** / 472 initiales (375 purgées) |
| `010_mur` (hors bloc + bloc) | 29 + bloc porteur | 4 + bloc porteur |
| `030_menuiserie` (baies porteuses seules) | **26** *(26 portes de cloisons purgées)* | **3** *(12 portes de cloisons purgées)* |
| `070_trait-fin` (escalier, seuils, Nord) | **35** | **38** |
| `075_cotation` (portées nu-à-nu seules) | **17** *(47 cotes de cloisons purgées)* | **8** *(40 cotes de cloisons purgées)* |
| **Contrôle `020_cloi` + `020_cloisons`** | **0 entité (100 % purgé)** | **0 entité (100 % purgé)** |

---

## 4. VERDICT & STATUT

**Statut : ✅ CONFORME — INDICE D LIVRÉ ET DÉPLOYÉ COMME FOND UNIQUE DE `B-20 IND. B` ET `B-40 IND. E`.**

Les anciens fichiers `_IndC` comportant cloisons et isolation ont été retirés de `_plans/` et mis à la corbeille sur Google Drive afin qu'aucun fond pollué ne subsiste dans le dossier.
