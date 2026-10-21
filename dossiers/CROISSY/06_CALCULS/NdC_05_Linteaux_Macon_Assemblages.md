# NOTE DE CALCUL — LINTEAUX, APPUIS MAÇONNERIE, ASSEMBLAGES

**EHPAD La Roseraie — Pavillon Flora — Croissy-sur-Seine**  
Indice **B** — 21/10/2026 — présentation (chiffres = B-49 A · B-46 A · B-50 A)  
**NE PAS EXÉCUTER SANS VISA.**  **NE PAS COMMANDER SANS VISA.**

---

## §0  Hypothèses à valider

| n° | Objet | Valeur |
|---|---|---|
| H1 | Maçonnerie | f_k = 1,5 MPa · essais **hors mission** · reprise chiffrée si non concluant |
| H2 | Remplissage R3 | UPE 200 **rempli C25/30** — condition de pose |
| H3 | Coussins | w_b ≥ **300 mm** sous R1, F2, F3 |
| H4 | A4 Stab1 | Capacité M12 **absente** — 8 tiges non commandables |
| H5 | Seuils BA | Sans objet |

---

## §1  Linteaux

Cinq linteaux **neufs**, S275. Aucun linteau BA, aucun seuil BA. Bois existants **non calculés** (non prescrits).

| Repère | Profil | L | Taux |
|---|---|---|---|
| F1a / F1b / F1c | 2 × HEA 200 | 1,00 / 0,90 / 0,85 m | triangle 0,010 · enveloppe 0,059 |
| R3-N / R3-S | UPE 200 + béton | 1,55 m | flexion 0,291 · torsion **close** avec béton |

Sans béton dans le U : τ = 222 / 159 MPa = **1,40** — non posable.  
E-08 (linteaux bois façade Est) : **court-circuités** par R3. Sommiers S1 sur **abouts de mur**, hors bois.

---

## §2  Appuis sur maçonnerie — coussins

Huit appuis F1→R3 vérifiés EC6 § 6.1.3. Cinq passent sans majoration. **R1 (77,4 kN), F2 (62,4), F3 (61,6)** exigent un coussin w_b = 300 mm : verdict alors **inconditionnel**.

Six coussins C25/30, h = 200 mm, 4 HA8. Ce **ne sont pas** des linteaux. F1/R3 : S1 200 mm suffisent. R2/F4 : OK sans coussin.

Voiles : 12/12 OK, taux max 0,290.

---

## §3  Assemblages

| | Assemblage | Verdict |
|---|---|---|
| A1 | 6 HA12 de P2 dans SF1 | OK — l_bd = 166 ≤ 200 mm |
| A2 | Moisage R1 — 10 M16 8.8 / face | OK — 0,69 · **le bois gouverne** |
| A3 | Torsion UPE R3 | Close par le remplissage béton |
| **A4** | Scellement Stab1 | **Non chiffré** — fiche absente |
| A5 | Platine P1 200 × 200 | OK — 0,12 |
| A6 | Appuis maçonnerie | → coussins |

Sabots demi-fermes / pannes : efforts 14,89 / 5,11 kN, **fiche non inventée**.

---

## §4  Points à lever

A4 : 8 tiges non commandables. Écart P2 HA12 équerre (plan fondations) vs droite (note poteaux) : 6 barres non commandables tant que non tranché. Forages du remplissage R3 : non inventés.

*Annexe — B-46, B-49, B-50 Ind. A · plans LINTEAU, MACON, ASSEMBLAGE Ind. B.*
