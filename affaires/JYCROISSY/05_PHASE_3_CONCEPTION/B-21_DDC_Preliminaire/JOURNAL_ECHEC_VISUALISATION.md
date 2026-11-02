# Journal d'échec — Visualisation géométrique impossible

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Phase :** Phase 3 — Conception et synthèse structurelle
**Briques impactées :** B-20 V2, B-21 V2, B-22 V2
**Date :** 2026-10-31
**Statut :** ÉCHEC DOCUMENTÉ — Livrables invalidés

---

## 1. CHRONOLOGIE DE L'ÉCHEC

| Date | Événement | Conséquence |
|---|---|---|
| 2026-10-31 | B-20 V2 produit — trame posée sur géométrie interprétée | Géométrie non vérifiée — axes, travées et murs erronés |
| 2026-10-31 | B-21 V2 produit — DDC calculée sur B-20 V2 | Charges gonflées — murs existants ignorés |
| 2026-10-31 | B-22 V2 produit — hypothèses sur B-20 V2 | Portées erronées propagées |
| 2026-10-31 | User détecte l'erreur : « ta DDC est erronée » | Début de la correction |
| 2026-10-31 | Analyse DXF B-32 V3 — géométrie réelle identifiée | Bâtiment ~226 m², murs porteurs existants |
| 2026-10-31 | User confirme : « tu as mal compris le projet » | Erreur fondamentale confirmée |
| 2026-10-31 | User : « tout est à jeter » | Arrêt du travail — livrables invalidés |

---

## 2. RAISON FONDAMENTALE DE L'ÉCHEC

**L'IA n'avait pas la capacité de visualiser les plans DXF.**

L'IA a parsing les fichiers DXF textuellement (extraction de coordonnées, entités, blocs), mais **n'a pas pu vérifier visuellement** que ses interprétations correspondaient à la réalité du projet.

**Conséquence :**
- Les coordonnées extraites ont été utilisées pour définir la géométrie du bâtiment.
- La géométrie défini était **interprétée**, non **vérifiée**.
- Aucun des livrables n'était valide.

---

## 3. ERREURS COMMISEES

### 3.1. B-20 V2 — Trame de principe

**Erreur :** Géométrie interprétée incorrectement.

| Élément | Ce qui a été produit | Ce qui aurait été nécessaire |
|---|---|---|
| Bâtiment FLORA | X[145,70 — 156,98] Y[40,86 — 60,22] = 11,28 m × 19,36 m | Bâtiment ~226 m² avec murs porteurs existants |
| Axes A/B/C | X = 145,70 / 151,34 / 156,98 | Vérifier visuellement les axes réels |
| Axes 1/2/3 | Y = 40,86 / 50,54 / 60,22 | Vérifier visuellement les axes réels |
| Murs existants | Non identifiés | Murs porteurs existants identifiés et positionnés |
| Trame neuve | Sur zone PROJECT (X > 115,64) | Trame réelle avec murs existants + renforts |

### 3.2. B-21 V2 — DDC préliminaire

**Erreur :** DDC calculée sur géométrie erronée, murs existants ignorés.

| Porteur | N_ELU (produit) | Problème |
|---|---|---|
| P1 | 362,9 kN | Surface tributaire erronée |
| P2 | 834,6 kN | Surface tributaire de 54,60 m² — trop grande |
| P3 | 362,9 kN | Surface tributaire erronée |
| SF1 | 725,7 kN/m | Erreur d'unité (54,60 m²/ml au lieu de 2,82 m²/ml) + murs existants ignorés |

**Erreur fondamentale :** Tous les appuis du bâtiment ont été considérés comme étant les éléments neufs (P1-P3, SF1). Les murs porteurs existants ont été ignorés.

### 3.3. B-22 V2 — Note hypothèses

**Erreur :** Portées erronées héritées de B-20 V2.

| Hypothèse | Portée V2 (erronée) | Problème |
|---|---|---|
| H-02 — poutres | L = 9,68 m | Portée non vérifiée |
| H-06 — dallage | L = 5,64 m | Portée non vérifiée |

---

## 4. PROBLÈMES MAJEURS DÉTECTÉS

### 4.1. Erreur d'unité — SF1

**SF1 (semelle filante)** — surface d'influence calculée comme :

```
B-21 V2 : A_inf(SF1) = 19,36 m × 2,82 m = 54,60 m²/ml  ← ERREUR
Correct : A_inf(SF1) = 2,82 m²/ml  (largeur tributaire seule)
```

Pour une **semelle filante** (charge linéique en kN/m), la surface tributaire **par mètre linéaire** est uniquement la largeur tributaire, pas la largeur × longueur.

**Conséquence :** N_ELS(SF1) et N_ELU(SF1) gonflés d'un facteur ~19.

### 4.2. Coefficient de continuité non standard — P2/SI2

**Coefficient 1,15** appliqué à P2 et SI2 (appuis intermédiaires). Ce coefficient est **non standard en Eurocode**. La méthode des surfaces tributaires **déjà tient compte** de la position des appuis. Appliquer 1,15 au-dessus est un double comptage.

### 4.3. Murs existants ignorés

**Erreur fondamentale :** La DDC a été calculée en considérant que les éléments neufs (P1-P3, SF1) étaient les seuls appuis. Or, le bâtiment FLORA contient des **murs porteurs existants** qui sont les appuis principaux.

**Conséquence :** Toutes les charges du bâtiment ont été réparties sur seulement 4 appuis, ce qui a gonflé artificiellement les charges sur chaque élément neuf.

---

## 5. CE QUI AURAIT DÛ ÊTRE FAIT

### 5.1. Début de session

**Avant toute production :**

1. **Poser les questions de capacités à l'IA** (voir `QUESTIONNAIRE_SESSION_IA.md`)
2. **Vérifier si l'IA peut visualiser les plans**
3. **Si non : demander des informations géométriques explicites**

### 5.2. Production de B-20 V2

**Au lieu de :**
- Parsing le DXF et interpréter les coordonnées
- Produire la trame sur cette base

**Il aurait fallu :**
- Demander à l'utilisateur les coordonnées explicites des murs, axes, travées
- Vérifier visuellement la géométrie avant de produire
- Documenter les incertitudes

### 5.3. Production de B-21 V2

**Au lieu de :**
- Calculer la DDC sur les éléments neufs seuls
- Ignor les murs existants

**Il aurait fallu :**
- Identifier tous les appuis (murs existants + éléments neufs)
- Répartir les charges sur tous les appuis
- Vérifier l'équilibre des charges

---

## 6. LIVRABILES INVALIDÉS

| Brique | Statut | Action |
|---|---|---|
| B-20 V2 | **INVALIDE** | À jeter — géométrie erronée |
| B-21 V2 | **INVALIDE** | À jeter — DDC sur géométrie erronée |
| B-22 V2 | **INVALIDE** | À jeter — hypothèses sur géométrie erronée |

**Recommandation :** Ne pas utiliser ces livrables pour les briques aval (B-23 à B-50).

---

## 7. LEÇONS TIRÉES

1. **Toujours vérifier les capacités de l'IA en début de session.**
2. **Ne jamais produire un livrable sans s'assurer que la géométrie est correcte.**
3. **Communiquer explicitement les incertitudes.**
4. **Arrêter immédiatement si l'IA ne peut pas travailler correctement.**
5. **Ne pas propager les erreurs : chaque brique doit être vérifiée avant la suivante.**

---

## 8. DOCUMENTS CONNEXES

| Document | Chemin |
|---|---|
| Questionnaire capacités IA | `QUESTIONNAIRE_SESSION_IA.md` |
| B-20 V2 (invalide) | `B-20_Conception_GO/B-20_Plan_Principe_P1_V2.{dxf,png,pdf}` |
| B-21 V2 (invalide) | `B-21_DDC_Preliminaire/B-21_DDC_Preliminaire_V2.md` |
| B-22 V2 (invalide) | `B-22_Note_Hypotheses/B-22_Note_Hypotheses_V2.md` |
| B-32 V3 (fond — géométrie réelle) | `03_PHASE_1_SOCLE/B-32_Vue_Nettoyee/SOCLE-GEOS_VUE-NETTOYEE_V3.dxf` |

---

**Journal documenté — 2026-10-31.**
**Usage :** À lire en début de toute nouvelle session sur ce projet.
