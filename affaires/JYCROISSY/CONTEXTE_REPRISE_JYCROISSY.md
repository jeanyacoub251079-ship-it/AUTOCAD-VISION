# CONTEXTE DE REPRISE — JYCROISSY / AUTOCAD-VISION
**Document aide-mémoire — à consulter en priorité au début de chaque session**
Date de création : 2026-10-31
Dernière mise à jour : session de dépôt Drive (commit `a8d0eb2`)

---

## 0. IDENTITÉ DU PROJET

- **Projet** : JYCROISSY — *de Croissy Flora* (opération immobilière, gros œuvre / structures).
- **Carnet d'ordres** : **CARNAC** (§0 et briques B-00 à B-50). **CARNAC est FROIDÉ — NE LE MODIFIER PLUS.** Il reste un artifact dans le repo.
- **Repo** : `https://github.com/jeanyacoub251079-ship-it/AUTOCAD-VISION.git`
- **Branche de travail** : `arena/cc8aea0e-autocad-vision` (fixe — ne pas renommer/switcher).
- **Clone local** : `/home/user/AUTOCAD-VISION` (racine du repo, git inclus).
- **Règle session** : tout le travail sur `arena/cc8aea0e-autocad-vision` ; push uniquement vers cette branche ; PR depuis cette branche.

---

## 1. ÉTAT GÉNÉRAL — PHASES 0 à 4 = **COMPLÉTES**

| Phase | Briques | Statut |
|---|---|---|
| Phase 0 — Cadrage | B-00, B-01, B-02, PTD, RDR, RDL | ✅ Livrée |
| Phase 1 — Socle | B-30 → B-32 → B-31 | ✅ Terminée |
| Phase 2 — Analyse | B-13/B-33, B-14, B-15, B-10, B-11, B-12 | ✅ Livrée |
| Phase 3 — Conception | B-20, B-25, B-21, B-22, B-23, B-24 | ✅ Complète |
| Phase 4 — Calculs | B-40 … B-50 (11 briques) | ✅ **COMPLÈTE** |

**B-50** (Assemblages et ancrages) : livrable en mode **PARAMÉTRIQUE documentaire** —
OUT-01 absente + DOC-09 manquante → calcul **suspendu**, aucune valeur retenue, aucun plan
produit. B-50 signale, n'arbitre pas.

**Sains objet** : B-41, B-44, B-47, B-48, B-49 (et Bloc B de B-46).
**PARAMÉTRIQUE documentaire** : B-40, B-42, B-43, B-45, B-46 (Bloc A), B-50.

---

## 2. OÙ SONT LES LIVRABLES (double stockage)

### 2.1 GitHub (source de vérité, code + artifacts)
- `affaires/JYCROISSY/` — dossier du projet.
  - `00_SUPPORTS/` — scripts de build (build_b01.py … build_b32.py), extracteurs, diagnoseurs DXF.
  - `02_PHASE_0_CADRAGE/` — RDR_JYCROISSY.md, RDL_JYCROISSY.md, B-00/B-01/B-02, PTD.
  - `03_PHASE_1_SOCLE/` — B-30, B-31, B-32 (DXF/PNG/PDF/md).
  - `04_PHASE_2_ANALYSE/` — B-10, B-11, B-12, B-13, B-14, B-15.
  - `05_PHASE_3_CALAGE/B-33_Verification_CROISEE/` — B-33.
  - `05_PHASE_3_CONCEPTION/` — B-20 (avec build_b20.py, DXF/PNG/PDF), B-21 à B-25.
  - `06_PHASE_4_CALCULS/` — B-40 à B-50.
  - `journal_deploiement_drive.md` — journal du dépôt Drive.

### 2.2 Google Drive (distribution des documents de production)
- **Dossier JYCROISSY** : `1X_hSPVvEVMDr3ZsV-5hhpUgjXegrUBUk` (parent `0AHJGUvUVsvY2Uk9PVA`).
- Contient les sous-dossiers `02_PHASE_0_CADRAGE`, `03_PHASE_1_SOCLE`,
  `04_PHASE_2_ANALYSE`, `05_PHASE_3_CONCEPTION`, `06_PHASE_4_CALCULS`
  (+ pièces FLORA/CCTP/CARNAC). **67 fichiers** déployés.
- **Règle** : les documents de production → Drive ; GitHub → code uniquement.

---

## 3. RÈGLES PERMANENTES (ne pas transgresser)

1. **GO strictement lexical** : exécuter exactement ce que le user demande, dans l'ordre donné.
2. **Pas d'arbitrage de contradiction par le modèle** : si deux pièces contradictoires, on
   signale, on ne tranche pas.
3. **Pas de valeur de repli / « pratique courante »** : chaque valeur porte **source + fiabilité**
   ou **VERROU**. Aucune valeur supposée.
4. **Ressources modèle** : utiliser EXCLUSIVEMENT « Claude Opus (Anthropic) » ou
   « ChatGPT ASTR (OpenAI) » ; les valeurs sont sourcées aux **pièces**, jamais à des
   suppositions de modèle.
5. **Une brique à la fois** : arrêt et attente du **GO** du user à chaque porte.
6. **NE TENTE PLUS DE MODIFIER CARNAC** — laisser comme artifact.
7. **Réduire le temps perdu en corrections** : rigueur sur la qualité dès la première production.

---

## 4. PIÈCES DE RENTRÉE (référence)

- `208_FLORA_DIAG structure.pdf` — diagnostic structure.
- `208_FLORA_Plans_DCE_IndC.dxf` — plans DCE (DXF).
- `208_FLORA_DCE_Pièces graphiques_IndC.pdf` — pièces graphiques.
- `24.09.356E DCE indice C FLORA 16.03.2026.pdf` — DCE indice C.
- `CCTP LOT 01 GROS OEUVRE - STRUCTURES ... .pdf` — CCTP.
- CARNAC v3.0.2 (document compilé source .md).

---

## 5. ANCRAGES TECHNIQUES — PIÈCES À NE PAS OUBLIER (prévenir les bugs)

### 5.1 Environment Python (`.venv`)
Le `.venv` est **nettoyé entre sessions** → **recréer systématiquement au reprendre** :

```bash
python3 -m venv /home/user/.venv && pip install ezdxf==1.4.5 matplotlib pypdf pdfminer.six
```

### 5.2 ezdxf 1.4.5 — pièges connus (déjà résolus, ne pas retenter)
- `dxf.alignment` pour **TEXT** → `DXFAttributeError`. **SOLUTION** : ne PAS set
  `alignment` sur TEXT.
- `add_text` doit être appelé sur **`msp`** (modelspace), **pas** sur `Drawing`.
- `add_rectangle` **n'existe pas**. **SOLUTION** : `add_lwpolyline` avec 4 points +
  `close=True`.

### 5.3 Autres
- PDF/PNG/DXF : **ne pas s'embêter à réparer** (consigne utilisateur) — produire directement.

---

## 6. PROCHAINES ÉTAPES (à valider par le user au reprendre)

Les Phases 0 à 4 sont terminées. **Rien n'est en attente technique** :
- B-50 reste suspendu jusqu'à réception de **OUT-01** et **DOC-09**.
- Les phases suivantes (Phase 5+) sont **à définir** — besoin d'un **GO** du user.

**À demander au user au reprendre** :
1. Confirmer la branche / la session.
2. Quel est le prochain GO (brique/phase suivante) ?
3. Donner le prompt de reprise (si fourni).

---

## 7. PROMPT DE REPRISE (à fournir au user)

Voir section « PROMPT DE REPRISE » à copier-coller au début de la prochaine session.

---

## 8. HISTORIQUE DES COMMITS RÉCENTS (branch `arena/cc8aea0e-autocad-vision`)

```
a8d0eb2  docs(JYCROISSY): journal du dépôt des livrables Phase 0 à 4 sur Google Drive
5e350ad  B-50 — Assemblages Ancrages
fa2d8bd  B-49 — Linteaux Seuils
76f1af1  B-48 — Predalles
8638863  B-47 — Escaliers
453c628  B-46 — Maconnerie
c9867ac  B-45 — Structure Metallique
c63c510  B-44 — Charpente Bois
9b83f94  B-43 — Planchers Dallages
acc3c3d  B-42 — Verticaux BA
0484a79  B-41 — Fondations Profondes
c12944e  B-40 — Fondations Superficielles
```

*(les commits antérieurs : B-20…B-33, Phase 0/1/2/3)*
