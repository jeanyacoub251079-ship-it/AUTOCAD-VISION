# DANIEL LEON — Gujan‑Mestras (33) — Retranscription DXF d'une planche de permis de construire

**Objet** : « Construction d'une résidence principale » — planche *PLAN / COUPE / SURFACES*,
échelle d'origine **0.02 P.M. = 1/50**, Entreprise GRAND (Le Canon, 33151), dessin J. GRAND,
juin 1975. Maître d'ouvrage : Monsieur et Madame DANIEL LEON, lotissement **CHANTE CIGALE L.T 77**,
**Gujan‑Mestras**, Gironde.

**Livrable** : `01_PLAN/DANIEL_LEON_PC1975_PLAN_COUPE_SURFACES_v2.dxf`
(+ `_A1.pdf` au 1/50 et `_apercu.png` de contrôle).

---

## 1. Source et méthode

| Étape | Outil | Détail |
|---|---|---|
| Source | reproduction photographique 1554 × 2048 px (document plié) | conservée en `00_SUPPORTS/00_SOURCE/` |
| Lecture | vision (zoom, rehaussement de contraste) | relevé des cotes, textes, cartouche, surfaces |
| Mesure | OpenCV : profils d'encre, morphologie | positions des faces de murs en pixels |
| Calage | 2 cotes d'ensemble | 15.00 m (largeur), 7.00 m (profondeur) → ≈ 68 px/m |
| Reconstruction | géométrie paramétrique | réseau de murs à 0.17 m / 0.07 m d'épaisseur |
| Écriture | ezdxf | DXF **AC1027 (R2013)**, unités **mm**, calques normalisés |
| Contrôle | `controle_dxf.py` + rendu | audit ezdxf OK, 14 calques, 51 cotes |

Aucun service externe n'est appelé : tout est calculé localement (Python, OpenCV, ezdxf).

---

## 2. Chaîne de cotes reconstituée (mur nord, en cm)

```
17 | 300 | 17 | 350 | 7 | 60 | 7 | 85 | 7 | 200 | 7 | 418 | 25   = 1500
```

* 17 cm = murs extérieurs ; 7 cm = cloisons ; **60** = rangement de la chambre 1 ;
  **85** = W.C. ; **200** = bains ; **418** = séjour (partie haute).
* Profondeur : **7.00 m hors‑œuvre / 6.66 m intérieur** (deux murs de 17 cm).
* Largeur intérieure : 14.66 m — cohérente avec les cotes de faitage (3.41 / 5.59) du document.

## 3. Verrouillage par les surfaces du cartouche

Surfaces **retrouvées exactement** par la géométrie reconstruite :

| Pièce | Dimensions | Calculé | Cartouche |
|---|---|---|---|
| GARAGE | 3.00 × 6.66 | **19.98** | 19.98 |
| CHAMBRE 1 | 3.50 × 3.38 | **11.83** | 11.83 |
| CUISINE | 3.50 × 3.00 | **10.50** | 10.50 |
| PLACARD (chambre 1) | 0.60 × 1.60 | **0.96** | 0.96 |
| W.C. | 0.85 × 1.60 | **1.36** | 1.36 |
| ENTREE | 2.75 × 3.24 | **8.91** | 8.91 |
| ESCALIER | 0.90 × 2.70 | **2.43** | 2.43 |
| TERRASSE (L : 2.00 m sud + 1.30 m est) | — | **28.60** | 28.60 |

Écarts résiduels, explicités dans le DXF :

* **SEJOUR** : 30.69 calculé / 30.17 au cartouche (0.5 m²) — la limite « poutre bois » n'est pas
  cotée sur la photo.
* **BAINS** : 5.61 / 7.14 — la cloison côté séjour (cote **2.69** lue) n'est pas traçable
  avec certitude sur la reproduction.

Ces deux points sont signalés comme **à vérifier sur l'original**.

## 4. Contenu du DXF

* **Plan du rez‑de‑chaussée** : murs extérieurs 0.17 m et cloisons 0.07 m hachurés, 15 baies
  (portes, fenêtres, porte‑fenêtre, porte de garage basculante, porte de service), escalier
  14 marches, équipements sanitaires, cheminée « coin de feu », conduit de fumée, terrasse en L.
* **Cotation** : chaîne haute complète (13 tronçons), chaîne basse des baies sud, chaînes
  gauche (profondeur) et droite (baies est), cotes d'ensemble 15.00 × 7.00 m, cotes de terrasse.
* **Coupe A‑B** : terrasse couverte sur poteaux, dallage, semelles filantes, murs, plancher du
  grenier, charpente deux pans (pente 0.30 p.m.), chevrons, conduit de fumée, escalier,
  hauteurs cotées (2.10 / 2.35 / 4.40 / 6.00 m — **estimées**, non cotées sur l'original).
* **Cartouche** d'origine reconstitué (maître d'ouvrage, objet, entreprise, échelle, date).
* **Tableaux** : surfaces (original / dessin), menuiseries extérieures, légende des calques,
  contrôle du calage dimensionnel, échelle graphique.
* **Calques** (couleur / épaisseur) : `MURS_EXT`, `CLOISONS`, `HACHURES`, `OUVERTURES`,
  `MENUISERIES`, `ESCALIER`, `SANITAIRES`, `TERRASSE`, `COTES`, `TEXTES`, `AXES`, `COUPE`,
  `CARTOUCHE`, `TABLEAU`. Cotes associatives (style `ARCH50`), unités mm.
* **Mise en page** : `A1-1_50` (841 × 594 mm), fenêtre au 1/50 ; cadre de feuille 42.00 × 29.70 m
  = A1 au 1/50.

## 5. Réserves (à lire avant usage)

1. Document source : **photographie d'un tirage plié et jauni** — les cotes de détail inférieures
   à 10 cm (épaisseurs, recouvrements) et les hauteurs de coupe ne sont pas garanties.
2. Les **dimensions de menuiseries** (tableau) sont des largeurs déduites des baies dessinées et
   des hauteurs usuelles de 1975 : à confirmer.
3. La planche ne comporte **que le rez‑de‑chaussée** ; le niveau « combles » (chambres 2 et 3)
   n'est connu que par le tableau de surfaces, non redessiné ici.
4. Retranscription **sans portée contractuelle** : à faire valider par un architecte / homme de
   l'art avant tout usage (permis, travaux, expertise).

## 6. Reproduction

```bash
cd affaires/DANIEL_LEON/00_SUPPORTS
python build_daniel_leon_dxf.py            # -> ../01_PLAN/*_v2.dxf
python controle_dxf.py ../01_PLAN/*_v2.dxf # audit
python export_pdf.py ../01_PLAN/*_v2.dxf   # -> PDF A1 1/50 + PNG
python render_dxf.py ../01_PLAN/*_v2.dxf apercu.png
```

Dépendances : `ezdxf`, `matplotlib` (rendu/PDF), `opencv-python-headless` et `pillow`
(analyse de la photo, non nécessaires à la génération du DXF).
