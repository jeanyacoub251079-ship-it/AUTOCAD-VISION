# NOTE DE CALCUL — DALLAGE ET PLANCHERS

**EHPAD La Roseraie — Pavillon Flora — Croissy-sur-Seine**  
Indice **B** — 21/10/2026 — présentation (chiffres = B-43 Ind. B)  
**NE PAS EXÉCUTER SANS VISA.**

---

## §0  Hypothèses à valider

| n° | Objet | Valeur |
|---|---|---|
| H1 | Emprise dallage | **111,15 m²** — non remesurée |
| H2 | Recharge | 15 cm sur **100 %** de l'emprise |
| H3 | Solives aile Est | 80 × 180 mm @ 0,50 m, portée 2,77 m, **C18** (hypothèse du diagnostic) |
| H4 | Plancher haut d'étage | **Nature inconnue** — aucun calcul |
| H5 | Termites sous dallage | Prescription **déjà au CCTP** (entreprise) — pas une donnée manquante |

---

## §1  Matériaux

Dallage C25/30, c_nom = 30 mm, treillis **ST25C** (Ø7 e150, 257 mm²/m).  
Solives existantes : C18, k_mod = 0,80, k_def = 0,60, service 2.

---

## §2  Charges

| Zone | g | q | p_ELS | p_ELU |
|---|---|---|---|---|
| A — solives bois | 1,80 | 2,50 | — | — |
| B — plancher mixte (renvoi métal) | 4,71 | 2,50 | — | 7,28 kN/m par solive |
| D — dallage + recharge 15 cm | **7,75** | 2,50 | 10,25 | **14,21 kN/m²** |

---

## §3  Géométrie

**Zone D — dallage**, RDC BAS, 111,15 m², ép. 130 mm sur fond de forme 400 mm. Coulé **à même** les semelles, désolidarisé 20 mm, **jamais** sur leur débord.  
**Zone A — solives 8×18**, aile Est, existant.  
**Zone B — IPE 160 @ 0,72 m + hourdis + IPE 330**, existant / renforts → note métal.  
**Zone C — plancher haut**, non sondé.

Joints de **retrait** du dallage e ≤ 4,50 m. Ce **ne sont pas** des joints de dilatation (aucun dans le bâtiment).

---

## §4  Vérifications

### Solives 8×18 — EC5 (cinq vérifications)

| | Taux |
|---|---|
| Flexion | **0,619** |
| Cisaillement | 0,362 |
| Compression d'appui | 0,316 |
| Flèche instantanée | 0,510 |
| Flèche finale | **0,576** |

### Dallage

Portance : 14,2 kPa / 490 kPa = **2,9 %** — le sol n'est pas le sujet.  
A_s,min EC2 = 122 mm²/m · ST25C = 257 mm²/m (**2,10 ×**).  
Fissuration et désolidarisation gouvernent, pas la flexion.

---

## §5  Points à lever

Plancher haut E-07 : **aucun calcul possible**. La charpente neuve est **désolidarisée** et ne le charge pas. Le point d'arrêt (sondage) **tombe si la charpente sort du programme**.  
Abouts de solives sous R1 : constat avant moisage (condition de pose, pas une étude bois).

*Annexe — B-43 Ind. B, plan PLANCHER Ind. B.*
