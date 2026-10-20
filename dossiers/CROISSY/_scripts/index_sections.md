
---

## 4. GLOSSAIRE DES CODES (pour lire ce dossier sans ouvrir une autre pièce)

| Code | Objet en clair |
|---|---|
| `B-xx` | Brique de la chaîne CARNAC (un livrable = une brique). Ex. `B-23` = exploitation du diagnostic, `B-25` = stabilité globale. |
| **Ind. A → V** | Indice de révision du livrable. Un indice neuf à chaque correction ; l'indice antérieur est retiré de la diffusion. |
| `D-xx` | Décision tranchée par le maître d'ouvrage, enregistrée au registre `B-03`. Ex. `D-29` = contreventement assuré par la maçonnerie existante. |
| `H-xx` | Hypothèse de conception, enregistrée à l'annexe `B-03` ; devient `D-xx` quand elle est tranchée. |
| `PA-xx` | Point à lever : information manquante, à obtenir du maître d'ouvrage ou d'un tiers. **Aucune valeur n'est inventée à la place.** |
| `T-xx` | Transmission à un tiers (ici `T-04` → maîtrise d'œuvre structure de conception). |
| `ENC` | Existant non qualifié : ouvrage réel mais non sondé ; il n'est **jamais** compté comme porteur sans réserve. |
| `ZONE NON RELEVEE` | Emprise du bâtiment dont la géométrie n'a pas été relevée (`D2` feuille 02) : hors de toute hypothèse chiffrée. |
| Nuage `D-19` | Nuage de révision apposé sur une planche pour marquer une hypothèse à valider par l'entreprise. |
| `RDR` | Registre des décisions et réserves (`B-03`). |
| `DDC` | Descente de charges (`B-21`). |
| `PLS` | Plan de localisation des semelles (implantation des fondations, `B-40`). |
| `F1a/F1b/F1c`, `F2`, `F3`, `F4` | Frangements acier neufs sous charpente (`2×HEA 200`, `HEB 200`, `HEB 160`, `IPE 200`). |
| `R1`, `R2-N/S`, `R3-N/S` | Renforts de plancher neufs (`2×UPE 200`, `HEB 160`, `UPE 200`) — **ouvrages neufs à exécuter**, jamais « exécutés ». |
| `P1-N/S`, `P2`, `P3` | Poteaux neufs : `P1` tube carré `140×140`, `P2` BA `15×25`, `P3` BA `50×40`. |
| `J1` | Jambage BA `24×50` (ouvrage neuf). |
| `SF1` | Semelle isolée type `80×80×25` BA (`D-30`). |
| `Stab1` | Entretoise de stabilisation dans les voutains briques (4 files). |
| `ELU` / `ELS` | États limites ultimes / de service (Eurocodes). |
| `f_k` / `f_vk0` | Résistance caractéristique de la maçonnerie en compression / en cisaillement initial (`D-34` : `1,5 MPa` / `0,15 MPa`, **à confirmer par essais hors mission**). |
| `TN` | Terrain naturel. Arase de référence : `−1,00 m / TN MINIMUM` (`D-09`). |
| `JD` | Joint de dilatation. **Aucun joint dans ce projet** (`D-28`) : l'absence est constatée, jamais démontrée, et la question n'est jamais reposée. |
| `0,00 RELATIF` | Niveau de référence altimétrique du projet (`D-21`), origine `P1`. |

---

## 5. POINTS OUVERTS (à la date du 20/10/2026)

| Réf. | Objet | Statut |
|---|---|---|
| `T-04` | Stabilité des ouvrages provisoires (étaiement, phases) | Transmise à la MOE structure de conception (`D-27`) |
| `PA-01` / `PA-02` | Reconnaissance du soubassement sous `P2` | En attente — aucune valeur de portance inventée ; `SF1 80×80` retenue sur l'hypothèse déclarée |
| Interface façades | Qui traite la fissuration `F5` relevée au pignon ? | À trancher (lot façades) |
| Interface zinguerie | Reprise des `P-4` (zinguerie avant pose) | À trancher (lot couverture) |
| Interface second œuvre | Séquence de dépose/repose des doublages en zone de renfort | À trancher (lot second œuvre) |
