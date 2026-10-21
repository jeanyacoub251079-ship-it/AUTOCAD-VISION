# NOTE DE CALCUL — CHARPENTE BOIS NEUVE

**EHPAD La Roseraie — Pavillon Flora — Croissy-sur-Seine**  
Indice **B** — 21/10/2026 — présentation (chiffres = B-44 Ind. A)  
Bois **C24** · service **2**  
**NE PAS EXÉCUTER SANS VISA.**

---

## §0  Hypothèses à valider

| n° | Objet | Valeur |
|---|---|---|
| H1 | Charge permanente toiture | **G = 0,95 kN/m²** |
| H2 | Neige | s_k = 0,45 kN/m² zone A1 — μ₁ non réduit |
| H3 | Classe | **C24** = spécification d'approvisionnement (comme S275) |
| H4 | Demi-fermes | **Désolidarisées du plancher** — chargent les murs A et C, pas E-07 |
| H5 | Zones non relevées ZN1 / ZN2 | Hors calcul — relevé avant taille |
| H6 | Contreventement de toiture | **Absent** des pièces — non inventé |

Le programme (CCTP + EVEN) prescrit les **bois neufs** ci-dessous. Il ne prescrit **aucune** intervention de vérification sur les bois existants (ferme tradi, pannes existantes, abouts). Pas d'arrêté termites, pas d'état des abouts à demander pour cette note.

---

## §1  Matériaux

C24, service 2. k_mod / k_def selon EC5 service 2, moyenne durée.

---

## §2  Charges

p_ELU toiture = **1,958 kN/m²** (G + neige). Soulèvement de contrôle −0,425 kN/m².

---

## §3  Géométrie

| Repère | Section | L | Rôle |
|---|---|---|---|
| PN1 / PN2 / PN3 | 75 × 200 | 3,20 m | Pannes neuves |
| DF — arbalétrier | 100 × 200 | 3,62 m | Demi-ferme, 2 u |
| DF — entrait | 75 × 200 | 3,20 m | Demi-ferme, 2 u |
| CF | 75 × 225 | 2,62 m | Contrefiches, après purge ferme Ouest |

Potelets existants E-04 : **supprimés** par les demi-fermes. Ferme tradi E-05 et pannes E-06 : existant, hors calcul.

---

## §4  Vérifications EC5

| | Taux max | Verdict |
|---|---|---|
| Pannes 75×200 | **0,830** (flèche) | OK |
| Arbalétrier 100×200 | **0,626** (flambement) | OK |
| Entrait 75×200 | 0,108 | OK |
| Contrefiches 75×225 | **0,940** (flambement) | OK |

Réaction d'appui demi-ferme : **14,89 kN**. Effort panne : **5,11 kN**. Sabots : **non catalogués, non inventés**.

---

## §5  Points à lever

ZN1 / ZN2 : relevé avant taille. Sabots : fiche ou choix MOE. Contreventement de toiture : absent — non inventé. E-07 non chargé ; le sondage du plancher haut n'est requis **que si** l'on charge ce plancher.

*Annexe — B-44 Ind. A, plan CHARPENTE Ind. B.*
