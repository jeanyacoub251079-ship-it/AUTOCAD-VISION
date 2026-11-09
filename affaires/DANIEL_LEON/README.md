# Affaire DANIEL LEON — Gujan‑Mestras (33)

Retranscription au format **DXF** d'une planche de permis de construire de 1975
(« Construction d'une résidence principale », lotissement Chante Cigale L.T 77),
fournie sous forme de reproduction photographique.

| Dossier | Contenu |
|---|---|
| `00_SUPPORTS/` | scripts de relevé et de génération (`build_daniel_leon_dxf.py`), contrôle (`controle_dxf.py`), export PDF/PNG (`export_pdf.py`, `render_dxf.py`), source photographique (`00_SOURCE/`) |
| `01_PLAN/` | **livrable** : `DANIEL_LEON_PC1975_PLAN_COUPE_SURFACES_v2.dxf` (+ `_A1.pdf` au 1/50, `_apercu.png`) |
| `JOURNAL_RETRANSCRIPTION.md` | méthode, chaîne de cotes, contrôle par les surfaces, réserves |

## Livrable

* DXF **AC1027 (R2013)**, unités **mm**, 14 calques normalisés, cotes associatives (style `ARCH50`),
  cartouche + tableaux (surfaces, menuiseries, légende, contrôle de calage), mise en page
  `A1-1_50` (841 × 594 mm) avec cadre 42.00 × 29.70 m = A1 au 1/50.
* Contenu : **plan du rez‑de‑chaussée** (murs, cloisons, 15 baies, escalier, sanitaires,
  cheminée, terrasse en L) et **coupe A‑B** (fondations, dallage, grenier, charpente 0.30 p.m.,
  conduit de fumée).

```
cd 00_SUPPORTS
python build_daniel_leon_dxf.py           # génère ../01_PLAN/*_v2.dxf
python controle_dxf.py ../01_PLAN/*_v2.dxf
python export_pdf.py ../01_PLAN/*_v2.dxf  # PDF A1 1/50 + PNG
```

Dépendances : `ezdxf`, `matplotlib` ; `opencv-python-headless` + `pillow` pour l'analyse
de la photographie.

> ⚠️ Retranscription établie à partir d'une photographie de tirage plié : **sans portée
> contractuelle**, à vérifier et valider par un homme de l'art. Les réserves et les deux
> écarts de surface (séjour, bains) sont détaillés dans `JOURNAL_RETRANSCRIPTION.md`.
