# Preuves d'extraction — localisation de la « recharge de sol de 15 cm »

**Source unique** : `208_FLORA_DCE_Pièces graphiques_IndC.pdf` (DCE indice C, Truelle Architectes, 13/03/2026), 29 pages — pièces graphiques `D4`.

Méthode : extraction texte par `PyMuPDF` (`search_for`), puis rendu raster et recadrage. **Les coordonnées sont celles du PDF** (page A3 paysage `1191 × 842` pt, rotation 270°). Une annotation n'est retenue que si **la planche qui la porte** est identifiée.

---

## 1. Occurrences de la chaîne « recharg » dans tout le DCE graphique

| Page | Planche (cartouche) | Occurrence | Plan concerné |
|---|---|---|---|
| **5** | `PLANS DE DEMOLITION` — 1/100 | « **Sol à recharger de 15cm** » à `x = 158,1 · y = 232,2` | **RDC FLORA — Projet** (plan de gauche) |
| **14** | `SANITAIRES PMR RDC` — 1/50 | « sol à recharger de 15cm » à `x ≈ 250 · y ≈ 365` | **RDC** — Sanitaire PMR |

**Aucune autre occurrence** sur les 29 pages (recherche insensible à la casse sur `recharg`, `15 cm`, `remblai`, `dallage`). En particulier : **aucune sur les planches de R+1** (`p. 16` à `p. 18`), dont les finitions sont nommées une à une — moquette grand trafic, parquet, sol souple acoustique, carrelage — **sans recharge**.

## 2. Ce que montrent les planches

| Fichier | Page | Ce qu'on y voit |
|---|---|---|
| `D4_p05.png` | 5 | Planche entière : plan RDC (démolition) à gauche, plan R+1 existant à droite |
| `D4_p05_zoom_recharge.png` | 5 | Recadrage : l'annotation « Sol à recharger de 15cm » avec sa ligne de rappel, **au droit de la façade sur rue, à côté du portail à remplacer** — niveau du sol, à l'entrée |
| `D4_p05_entree.png` | 5 | Même zone, plus large : la recharge voisine « Sol à décaisser de 6cm », « mur démoli », « remplacement porte » |
| `D4_p14.png` | 14 | Planche `SANITAIRES PMR RDC` : la recharge apparaît **dans la pièce d'eau**, sous le carrelage |
| `D4_p14_coupeKK.png` | 14 | Détail : « sol à recharger de 15cm » sous la finition carrelage, dans le sanitaire |

## 3. Les quatre preuves que la recharge est au **RDC** et **au sol**

1. **Position sur la planche p. 5** : l'annotation est dans la bande `y = 96 → 440`, avec « dépose des dalles » (`y = 96`), « sol décaissé en pente 10 % h : 16,8 cm » (`y = 321`), « ouverture mur » (`y = 399`) et « Hspo : 2.75 » (`y = 424`) — **toutes des annotations de RDC**. Les annotations de R+1 (« cloisons démolies », repères `Z: 204,42`) sont dans la bande `y = 890 → 1 110`.
2. **Planche p. 14** : cartouche **`SANITAIRES PMR RDC`**, échelle 1/50, avec la recharge sous le carrelage de la pièce d'eau.
3. **Cohérence avec le diagnostic (`D3`)** : EVEN vérifie la solive `8 × 18` à `150 daN/m²` et trouve `w = 7,7 mm` pour `7,0` admis. Une recharge de `3,30 kN/m²` sur ce plancher **triplerait** la flèche (≈ `25 mm`). Le chiffre d'EVEN n'est compatible **qu'avec un plancher non rechargé**.
4. **Nature du plancher bas** : `D2` folio 03 = « Vue en plan **PB RDC** (plancher bas) — **Dallage** / fondations ponctuelles » ; `B-20` retient un **dallage BA désolidarisé `ép. 13 cm` sur forme `40 cm`**. La recharge est donc un **ouvrage de sol en contact avec le terrain**, pas une charge de plancher haut.

## 4. Ce qui reste non établi — et qui ne sera pas inventé

**L'emprise exacte de la recharge n'est pas tracée.** Les deux planches portent **une annotation avec ligne de rappel**, jamais une trame hachurée délimitant une zone. On peut donc affirmer :

- ✅ la recharge est **au RDC**, sur le **sol** (dallage) ;
- ✅ elle **ne charge pas** les planchers bois et hourdis (`A` et `B`) ;
- ❌ son **étendue en plan** (entrée seule ? sanitaires ? tout le RDC ?) **n'est pas établie par le DCE** : c'est une question à la MOE, sans effet sur le calcul des planchers hauts.

## 5. Conséquence sur `B-21`

`B-21` appliquait `+3,30 kN/m²` « **sur toute la surface du plancher B** » — et de fait à `A` comme à `B` (§ 3.5). **Cette localisation est fausse.** Le détail du calcul figure dans `B-21` Ind. C, à produire.
