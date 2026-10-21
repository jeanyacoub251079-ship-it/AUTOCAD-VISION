# NOTE DE CALCUL — POTEAUX BA ET PROFILÉS

**EHPAD La Roseraie — Pavillon Flora — Croissy-sur-Seine**  
Indice **B** — 21/10/2026 — présentation (chiffres = B-42 Ind. B + B-45 Ind. A)  
C25/30 · S500B · **S275**  
**NE PAS EXÉCUTER SANS VISA.**

---

## §0  Hypothèses à valider

| n° | Objet | Valeur |
|---|---|---|
| H1 | Hauteur de fût | **2 800 mm** — à relever avant façonnage |
| H2 | Appuis | Rotulés pied et tête (l0 = H) |
| H3 | Nuance acier | **S275** — contractuelle (EVEN) |
| H4 | F3 | **Aucune charge ajoutée** (y c. local sport C4) |
| H5 | IPE 330 | Existant — hors cette note |
| H6 | Sismique | Zone 1 — sans objet |

---

## §1  Matériaux

Béton C25/30, f_cd = 14,17 MPa. Acier BA S500B, f_yd = 434,8 MPa, c_nom = 30 mm.  
Acier de construction **S275**, f_y = 275 MPa, γ_M0 = γ_M1 = 1,00. Toutes les barres en **classe 1**.

---

## §2  Charges (ELU)

| Repère | N_Ed ou V_Ed | Source |
|---|---|---|
| P2 | N = **159,0 kN** | Descente planchers, sans recharge dallage |
| P3 | N = 35,8 kN | |
| J1 | N = 39,8 kN | |
| P1-N/S | N = 100,3 kN | |
| R1 | V = 77,4 kN · M = 74,5 kN·m | |
| F3 | M = 59,3 kN·m | Gouvernant flèche |

---

## §3  Géométrie

P2 150 × 250 sous F2, façade Ouest Nord, sur SF1.  
P3 400 × 500 au refend hall.  
J1 240 × 500 au refend central, sous F1a.  
Profilés implantés : F2 HEB 200 (2,85 m), F3 HEB 160 (3,85 m), F4 IPE 200 (4,88 m), R1 2×UPE 200 (3,85 m), R2-N/S HEB 160 (3,82 m), P1 SHS 140×140×6,3, Stab1 IPE 120 (4 files).

---

## §4  Vérifications

### Poteaux BA — interaction N-M + flambement EC2 § 5.8

| | P2 | P3 | J1 |
|---|---|---|---|
| λ / λ_lim | 64,7 / 19,7 → **2ᵉ ordre** | 24,2 / 95,9 | 40,4 / 70,5 |
| M_Ed / M_Rd | **0,305** | 0,013 | 0,015 |
| Ferraillage | **6 HA12** (679 mm²) | 6 HA12 | 6 HA12 |
| Cadres | HA8 e150 | HA8 e200 | HA8 e200 |

6 HA12 est imposé par l'**espacement maximal** sur les faces étroites, pas par A_s,min.  
Appui de J1 sur la maçonnerie : 0,332 MPa → 55 % à f_k = 1,5 MPa ; 83 % à 1,0 ; **non satisfait à 0,5**.

### Profilés — EC3 (déversement **sans maintien supposé**)

| Repère | Flexion | Flèche / L/300 | Déversement |
|---|---|---|---|
| F1a/b/c 2×HEA 200 | 0,059 | 0,026 | 0,065 |
| F2 HEB 200 | 0,252 | 0,237 | — |
| **F3 HEB 160** | 0,609 | **0,971** | — |
| F4 IPE 200 | 0,231 | 0,306 | — |
| **R1 2×UPE 200** | 0,605 | 0,927 | **0,880** |
| P1 SHS 140 | flambement 0,123 | — | — |

**F3 : 12,5 mm pour 12,8 mm admis.** Conforme, sans marge. Toute charge ajoutée sort la barre.

R3 (UPE 200) : flexion 0,291 OK ; **torsion non conforme** sans remplissage béton (taux 1,40) — le remplissage C25/30 est une **condition de pose**.

---

## §5  Points à lever

H = 2 800 mm à relever. F3 : consigne opposable « aucune charge ajoutée ». Stab1 : longueurs selon relevé des IPE 160. A4 scellement Stab1 : non chiffré (fiche absente).

*Annexe — B-42 Ind. B, B-45 Ind. A, plans VERT et METAL Ind. B.*
