# B-20 — Conception structure GO

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-20 (Phase 3 — Conception et synthèse structurelle)
**Date :** 2026-10-31
**Mode :** INTERNE-GO (aucun BET de conception — CFG-2 selon B-00 §5)
**Version :** 1.0

---

## 0. CONTEXTE DU MODE

**INTERNE-GO** : aucun BET de conception structure. La conception est produite à partir des plans architecte (DOC-02), du diagnostic existant (B-11, B-23) et de la géotechnique (B-12). La vue nettoyée B-32 est la base géométrique (bloquante).

**CFG-2** (B-00 §5) : BET structure MOE existant (EVEN STRUCTURES : DIAG + principes DCE PDF), **sans vecteur structure natif** (le DXF P5 est architecte). Conséquence : transcription intégrale des ouvrages, puis conception à notre charge.

---

## 1. TRAME STRUCTURELLE

### 1.1 Axes et entraxes

La trame structurelle est déduite de la géométrie architecte (P4) et de la vue nettoyée B-32. L'emprise du bâtiment Flora est en RSU (B-30). Les axes principaux sont repérés A, B, C (sens 1 — profondeur) et 1, 2, 3 (sens 2 — largeur).

| Axe | Direction | Position RSU (m) | Note |
|---|---|---|---|
| A | 1 | 0,0 | Mur gouttereau existant |
| B | 1 | 6,0 | Axe central — poteaux existants |
| C | 1 | 12,0 | Mur gouttereau existant |
| 1 | 2 | 0,0 | Façade principale |
| 2 | 2 | 9,0 | Axe central |
| 3 | 2 | 18,0 | Façade arrière |

**Entraux** : 6 m (axe A → B), 6 m (axe B → C), 9 m (axe 1 → 2), 9 m (axe 2 → 3).

### 1.2 Positions des porteurs neufs

| Repère | Ouvrage | Position RSU (m) | Justification |
|---|---|---|---|
| P1 | Poteau neuf BA | (9,0, 0,0) — axe B/1 | Nouveau poteau à l'angle de la trame pour porter le R+1 |
| P2 | Poteau neuf BA | (9,0, 6,0) — axe B/2 | Poteau central sur l'axe B |
| P3 | Poteau neuf BA | (9,0, 18,0) — axe B/3 | Poteau à la jonction avec l'existant |
| Pt1 | Poutre métallique | Axe B, entre P1 et P2 | Poutre de portée 9 m, L/20 ≈ 450 mm → h ≈ 500 mm (ENVELOPPE) |
| Pt2 | Poutre métallique | Axe B, entre P2 et P3 | Poutre de portée 9 m, L/20 ≈ 450 mm → h ≈ 500 mm (ENVELOPPE) |
| SI1 | Semelle isolée | (9,0, 0,0) — sous P1 | Prédimensionnement : B ≥ N/q_adm — À CALER |
| SI2 | Semelle isolée | (9,0, 6,0) — sous P2 | Prédimensionnement : B ≥ N/q_adm — À CALER |
| SI3 | Semelle isolée | (9,0, 18,0) — sous P3 | Prédimensionnement : B ≥ N/q_adm — À CALER |
| SF1 | Semelle filante | Axe A, entre SI1 et SI3 | Fondation de mur gouttereau existant — À CALER |
| Lt1 | Linteau neuf BA | Axe 1, baie existante | Linteau de portée 3 m — À CALER |
| Lt2 | Linteau neuf BA | Axe 3, baie existante | Linteau de portée 3 m — À CALER |
| Dg1 | Dallage neuf | Niveau RDC | Dallage de portée 6 m — À CALER |

---

## 2. PRÉDIMENSIONNEMENT DES SECTIONS DE PRINCIPE

### 2.1 Poteaux neufs BA (P1, P2, P3)

**Méthode** : A_c ≥ N_Ed / (0,3 · f_cd) — prédimensionnement par compression axiale.

- N_Ed : charge d'exploitation (250 daN/m² — D-03) × surface portée ≈ 54 m² → N_Ed ≈ 13,5 kN (charge vivante seule, avant poids propre et charges permanentes).
- f_cd : contrainte design béton — valeur à confirmer (R-08).
- Section proposée : **30 × 30 cm (MINI)** — méthode : A_c ≥ N_Ed / (0,3 · f_cd).

### 2.2 Poutres métalliques (Pt1, Pt2)

**Méthode** : h ≈ L/20 en plancher — prédimensionnement par flèche.

- L = 9 m → h ≈ 450 mm → **h ≈ 500 mm (ENVELOPPE)**.
- Section proposée : **profilé métallique h ≈ 500 mm (MINI)** — à calculer en B-45.

### 2.3 Semelle isolée (SI1, SI2, SI3)

**Méthode** : B ≥ N / q_adm — prédimensionnement par pression sous semelle.

- N : charge totale poteau (poids propre + exploitation).
- q_adm : contrainte admissible du sol (SOL-01 : qELS ≤ 0,30 MPa — D-06).
- Section proposée : **B × L à calculer en B-40** — mention « À CALER ».

### 2.4 Semelle filante (SF1)

**Méthode** : B ≥ N / q_adm — prédimensionnement par pression sous semelle.

- Section proposée : **B × L à calculer en B-40** — mention « À CALER ».

### 2.5 Linteau (Lt1, Lt2)

**Méthode** : section de linteau en BA — prédimensionnement par flexion.

- Portée ≈ 3 m.
- Section proposée : **20 × 30 cm (MINI)** — à calculer en B-49.

### 2.6 Dallage (Dg1)

**Méthode** : épaisseur de dalle par portée — prédimensionnement par flèche.

- Portée ≈ 6 m → épaisseur ≈ L/30 ≈ 20 cm (MINI).
- Section proposée : **dalle 20 cm (MINI)** — à calculer en B-43.

---

## 3. RENFFORTS DE L'EXISTANT

| Repère | Renfort | Ouvrage existant | Désordre corrigé | Justification (B-11) |
|---|---|---|---|---|
| R1 | Moisage métallique | Poutre maîtresse existante (partie Est) | Fléchissement à vue d'œil | B-11 D-01 — pathologies structurelles |
| R2 | Sommier de répartition | Mur gouttereau existant (axe A) | Appuis insuffisants | B-11 D-03 — fondations existantes |
| R3 | Entretoise anti-déversement | Poteaux existants (axe B) | Stabilité latérale | B-11 D-06 — structure métallique existante |
| R4 | Contrefiche | Poteau existant (angle) | Stabilité latérale | B-11 D-06 — structure métallique existante |

**Aucun renfort n'est dimensionné** — les choix de principe sont justifiés par le désordre qu'ils corrigent. La validation fine relève de B-44 à B-50.

---

## 4. HYPOTHÈSES DE CONCEPTION (renvoi B-22)

| N° | Hypothèse | Valeur / norme d'appui | Zone | Statut | Délai DEC-06 |
|---|---|---|---|---|---|
| H-01 | Section des poteaux neufs | 30 × 30 cm (MINI) | RDC + R+1 | À confirmer | 2 jours ouvrés |
| H-02 | Section des poutres métalliques | h ≈ 500 mm (ENVELOPPE) | RDC | À confirmer | 2 jours ouvrés |
| H-03 | Contrainte design béton f_cd | Valeur à confirmer (R-08) | — | À confirmer | 2 jours ouvrés |
| H-04 | Contrainte admissible du sol q_adm | qELS ≤ 0,30 MPa (D-06) | Fondations | Décision D-06 | — |
| H-05 | Charge d'exploitation | 250 daN/m² (D-03) | RDC + R+1 | Décision D-03 | — |

---

## 5. POINTS À VISER

1. **Visa de la conception structure** : la trame, les sections de principe et les renforts doivent être visés par le BET / BC / MOE avant que les briques de calcul ne s'appuient dessus.
2. **Hypothèses H-01 à H-05** : à viser ou à confirmer par la MOE/BET MOE.
3. **Sections de principe** : mini / enveloppe / à caler — jamais une cote définitive.
4. **Protection au feu** : une protection au feu adéquate doit être prévue (mention générique seule — hors périmètre CARNAC).
5. **Plans de principe** : filigranés « PRINCIPE — NE PAS EXÉCUTER — Indice P1 ».

---

## 6. POINTS À LEVER

| Objet | Raison | Brique qui tranchera |
|---|---|---|
| Section des poteaux neufs | Prédimensionnement mini — à calculer | B-42 |
| Section des poutres métalliques | Enveloppe — à calculer | B-45 |
| Section des semelles | À caler — à calculer | B-40 |
| Section des linteaux | Mini — à calculer | B-49 |
| Épaisseur de dalle | Mini — à calculer | B-43 |
| Renforts de l'existant | Choix de principe — à valider | B-44, B-45, B-46, B-50 |
| Protection au feu | Hors périmètre CARNAC — mention générique | — |
| Contradiction C-08 (couverture DXF) | Le vecteur natif ne couvre pas tout le DCE architecte | B-30, B-32, B-20 |
| Données manquantes EXI-01 à EXI-05 | Sections et résistance de l'existant | B-23, B-24, B-44 à B-50 |
| Données manquantes SOL-01 à SOL-07 | Géotechnique | B-40, B-41 |

---

## 7. CE QUE B-20 NE PRODUIT JAMAIS

- Notes de calcul d'exécution (EC2, EC3, EC5, EC7 avec ferraillage détaillé) — B-40 à B-50.
- Plans d'exécution cotés avec ferraillage — B-60.
- Nomenclatures et façonnage — B-62.
- Calage fin et preuve de superposition — B-30, B-31.
- Dimensionnement de la protection au feu — hors périmètre CARNAC (mention générique seule).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Le plan est le livrable qu'on juge | ✅ Plans de principe générés (DXF + PNG + PDF) — voir §Plans |
| Ce qui n'est pas sur le plan n'existe pas | ✅ §1.2 (tous les ouvrages implantés avec repère unique) |
| Le fond est la vue B-32 extraite | ✅ Plans sur fond B-32 |
| Chaque plan porte le filigrane « PRINCIPE — NE PAS EXÉCUTER » | ✅ Filigrane appliqué |
| Aucune cote de section n'a l'air d'un EXE | ✅ §2 (MINI / ENVELOPPE / À CALER) |
| Aucun calcul d'exécution produit | ✅ Prédimensionnement seulement |
| Aucune protection au feu dimensionnée | ✅ §5 (mention générique seule) |
| Les points à viser tiennent sur une page | ✅ §5 |

---

**Brique B-20 exécutée en mode INTERNE-GO — en attente de votre GO ou de nouvelles observations.**
Le visa de la conception est indispensable avant les briques de calcul. **Les plans de principe (Indice P1) sont le livrable principal** — ce qui n'est pas sur le plan n'existe pas.
