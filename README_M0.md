# Module M0 - Vision IA pour Coffrage

Ce module constitue l'œil IA de la pipeline de transformation DXF architecte vers fond de plan de coffrage.

## Fonctionnement

M0 analyse visuellement le plan (soit via le DXF rasterisé, soit via un PDF/image externe) pour produire un masque de segmentation identifiant les masses structurelles (murs et poteaux).

### Modes
1. **Mode Heuristique (Fallback)** : Utilise OpenCV pour détecter les masses par morphologie mathématique.
2. **Mode IA (Recommandé)** : Utilise un modèle de deep learning (U-Net) pour une reconnaissance sémantique des objets. Supporte PyTorch (`.pth`) et ONNX (`.onnx`).

## Installation

### Installation de base (Heuristique)
```bash
pip install ezdxf shapely loguru numpy matplotlib
```

### Installation complète (Vision IA + PDF)
```bash
pip install pymupdf opencv-python torch segmentation-models-pytorch onnxruntime
```

## Utilisation

```bash
python coffrage_m0_vision_filter.py plan_archi.dxf -o plan_filtre.dxf --model weights/model.pth --vision plan.pdf
```

### Paramètres clés
- `--model` : Chemin vers les poids du modèle.
- `--vision` : Source visuelle externe (PDF/PNG) pour plus de fidélité.
- `--only-structure` : Supprime les éléments non structurels (ARCHI_FOND) du DXF de sortie.
- `--audit-dir` : Dossier pour les rapports et masques de diagnostic.

## Configuration IA (`model_config.json`)

Un fichier sidecar peut être placé à côté du modèle pour configurer ses paramètres :
- `input_size` : Taille d'entrée du modèle (ex: [512, 512]).
- `normalization` : Moyenne et écart-type (ImageNet par défaut).
- `classes` : Nombre de classes (fond, mur, poteau).

## Diagnostic

Consultez le dossier d'audit pour visualiser `m0_overlay.png` (superposition IA sur le plan) et `m0_report.json` pour les statistiques détaillées.
