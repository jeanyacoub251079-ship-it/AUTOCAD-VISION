"""
Niveaux NGF retenus pour l'affaire GARENNE — source unique de vérité.

Le nivellement du DXF (`geometrie_dxf.json`, clé `niveaux_ngf`) donne, aux
points levés sur les planches P08a/P08b :

    41,11  terrain extérieur (jardin, seuils)
    41,30  sol fini RDC — point bas mesuré
    41,35  sol fini RDC — point haut mesuré
    41,56  sol fini RDC — point singulier (seuil, emmarchement)
    47,47  gouttière
    49,54  faîtage

Le **parti de nivellement retenu** est le suivant : le sol fini du RDC est pris
à **NGF 41,46**, valeur de référence des coupes du maître d'œuvre (P09b, P10b,
P11b), qui correspond au nu de référence des plans de coupe. L'écart avec les
points levés sur les plans de repérage (41,30 à 41,56) est de l'ordre de
± 15 cm, ce qui reste dans la tolérance d'un relevé sur planche papier.

Tous les documents (DOC-01, DOC-02, DOC-03) et tous les plans d'exécution
doivent importer ces valeurs depuis ce module : aucun niveau ne doit être
ressaisi à la main.
"""

# Niveau de référence du sol fini RDC, en m NGF.
NGF_SOL_RDC = 41.46

# Niveau de l'arase supérieure des fondations existantes (assise des puits).
NGF_FONDATION = 39.02

# Niveau du sol fini du sous-sol.
NGF_SSOL = 39.26

# Niveaux de plancher haut.
NGF_PH_RDC = 44.08
NGF_PH_R1 = 44.32

# Niveaux de toiture et d'acrotère.
NGF_ACROTERE = 44.75
NGF_GOUTTIERE = 47.47
NGF_FAITAGE = 50.16
NGF_VERRIERE_HEAD = 45.90

# Niveaux de la poutre-acrotère (fonction mixte poutre + acrotère).
NGF_POUTRE_BAS = NGF_PH_RDC          # 44,08 — sous-face, au nu du plancher haut RDC
NGF_POUTRE_HAUT = NGF_ACROTERE       # 44,75 — arase supérieure de la poutre-acrotère
NGF_ACROTERE_ARASE = NGF_ACROTERE    # 44,75 — arase de référence (couverture sous révélateur)

# Position de l'axe du poteau BA 25 x 25 de la verrière, mesurée depuis le nu
# extérieur de la façade existante. Valeur contractuelle issue de l'arbitrage
# E-01 du 11/11/2026 (poteau repositionné sous la poutre, à ~2,00 m).
POS_POTEAU_FAÇADE = 2.00

# Largeur de l'extension et portées de la poutre-acrotère.
L_EXTENSION = 8.03
TRAVEE_1 = POS_POTEAU_FAÇADE                  # 2,00 m — travée côté façade
TRAVEE_2 = L_EXTENSION - POS_POTEAU_FAÇADE    # 6,03 m — travée vers le voile mitoyen

# Terrain extérieur.
NGF_TERRAIN = 41.11


def tableau_niveaux():
    """Retourne les lignes du tableau des niveaux, prêtes pour common_doc."""
    return [
        ["Terrain extérieur (jardin, seuils)", f"{NGF_TERRAIN:.2f}", "Relevé DXF"],
        ["Sol fini RDC — référence retenue", f"{NGF_SOL_RDC:.2f}",
         "Coupes MOE + parti de nivellement"],
        ["Sol fini RDC — plage des points levés", "41,30 à 41,56",
         "Relevé DXF (écart ± 15 cm)"],
        ["Sol fini sous-sol", f"{NGF_SSOL:.2f}", "Coupe P09b"],
        ["Arase supérieure des fondations", f"{NGF_FONDATION:.2f}",
         "Fond de fouille constaté"],
        ["Sous-face du plancher haut RDC / arase poutre", f"{NGF_PH_RDC:.2f}",
         "Coupe P10b"],
        ["Sous-face du plancher haut R+1", f"{NGF_PH_R1:.2f}", "Coupe P10b"],
        ["Arase de l'acrotère de la terrasse", f"{NGF_ACROTERE:.2f}",
         "Coupe P10b"],
        ["Tête de la verrière", f"{NGF_VERRIERE_HEAD:.2f}", "Coupe P10b"],
        ["Gouttière", f"{NGF_GOUTTIERE:.2f}", "Coupe P09b"],
        ["Faîtage", f"{NGF_FAITAGE:.2f}", "Coupe P09b"],
    ]
