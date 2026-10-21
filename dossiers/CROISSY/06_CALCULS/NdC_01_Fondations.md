# NOTE DE CALCUL — FONDATIONS

**EHPAD La Roseraie — Pavillon Flora — Croissy-sur-Seine**  
Indice **B** — 21/10/2026 — présentation (chiffres = note B-40 Ind. F)  
C25/30 · S500B · arase **−1,00 m / TN mini**  
**NE PAS EXÉCUTER SANS VISA.**

---

## §0  Hypothèses à valider

| n° | Objet | Valeur | Source |
|---|---|---|---|
| H1 | Portance | q_ELS ≤ 0,30 MPa · q_ELU ≤ 0,49 MPa | G2 GEOEXPERTS |
| H2 | Arase inférieure | −1,00 m / TN **minimum** — jamais de remontée | Prescription d'exécution |
| H3 | Encastrement | 0,50 m dans les alluvions anciennes | G2 |
| H4 | Semelle mini | 600 × 600 mm | Programme / EVEN |
| H5 | SF1 sous P2 | **800 × 800 × 250 mm** | Calcul (60×60 = 121 % ELS) |
| H6 | Nappe | Non déclarée — venue d'eau = arrêt | G2 |
| H7 | Tassements | Hors mission | — |

---

## §1  Matériaux

- Béton semelles **C25/30** — f_cd = 14,17 MPa  
- Gros béton de rattrapage **C16/20**  
- Acier **S500B** — f_yd = 434,8 MPa  
- Enrobage fondation **c_nom = 50 mm**

---

## §2  Charges

Les fondations reprennent les **planchers hauts**. Le dallage repose sur le sol et **ne charge aucune semelle**.

| Destination | g | q | p_ELS | p_ELU |
|---|---|---|---|---|
| Planchers hauts (fondations) | 4,71 | 2,50 | **7,21** | **10,11 kN/m²** |
| Dallage (recharge 15 cm, 100 %) | 7,75 | 2,50 | 10,25 | 14,21 kN/m² |

---

## §3  Géométrie

| Repère | Ouvrage | Position | Statut |
|---|---|---|---|
| **SF1** | 800 × 800 × 250 sous P2 | X = 95,35 m · Y = 59,29 m | Certain |
| Z-P1N / Z-P1S | Vérif. moellons ou 600 × 600 | Façade Ouest Sud | Fouille |
| Z-P3 / Z-J1 | Appui existant + gros béton | Refends | Fouille |
| Bêche | 200 mm × 2,85 m | Sud-Est | Certain |
| RSO passerelle | Passes ≤ 1,00 m C16/20 | Nord | Certain |

**Égalisation.** Si l'existant est plus profond : descendre et rattraper **sous** la semelle par du gros béton C16/20. Jamais déchausser l'existant.

---

## §4  Vérifications — SF1

N_ELS = **130,5 kN** · N_ELU = **182,9 kN** (descente B-21, continuité 1,15).

| | Valeur | Admissible | Taux |
|---|---|---|---|
| σ_ELS | 0,204 MPa | 0,300 | **68 %** |
| σ_ELU | 0,286 MPa | 0,490 | **58 %** |
| Poinçonnement v_Ed | 0,279 MPa | 0,392 | **71 %** |
| Rigidité d | 192 mm | ≥ 138 mm | OK |
| Flexion | gouvernée par A_s,min | HA8 e150 (335 ≥ 323 mm²/m) | OK |

**Ferraillage.** Lit inf. HA8 e150, 6+6. Attentes P2 : **6 HA12 équerre**, l_bd = 166 mm ≤ 200 mm. Sans équerre : 237 mm — **non conforme**. Cadres HA8 e150 jusqu'au lit. c_nom 50 mm **4 faces**.

Un 60 × 60 sous P2 donnerait σ_ELS = 0,362 MPa (**121 %**) : d'où 80 × 80.

Dallage : 14,2 kPa sur 490 kPa = **2,9 %** du sol — se dimensionne en fissuration (note dallage), pas ici.

---

## §5  Points à lever

Réception contradictoire de fond de fouille **avant coulage**. Nuages Z-P1N/S, Z-P3, Z-J1 ouverts. Écart d'aplomb R+1/RDC 10,1 cm = donnée, non corrigée.

*Annexe — B-40 Ind. F, script b40_fondations.py, plan B-60 FOND Ind. B.*
