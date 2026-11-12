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

# ---------------------------------------------------------------------------
# GÉOMÉTRIE DE L'EXTENSION — RECTIFICATION DU 11/11/2026 (arbitrage E-02)
# ---------------------------------------------------------------------------
# Le schéma structurel retenu est le suivant (croquis MOE du 11/11/2026) :
#
#   * la terrasse mesure 8,03 m de long sur **2,00 m de large, poutre-
#     acrotère comprise** ;
#   * la poutre-acrotère de 8,03 m est **en limite de dalle, à 2,00 m de la
#     façade** ; elle est **isostatique** (travée unique) ;
#   * elle s'appuie à droite sur un **voile BA à créer**, fondé sur une
#     **semelle filante à créer**, en limite de propriété, dans le
#     prolongement du mur pignon ;
#   * elle s'appuie à gauche sur l'**extrémité en console** d'une poutre-
#     acrotère **perpendiculaire à la façade**, qui s'appuie sur le poteau
#     BA et se poursuit en **porte-à-faux de 0,70 m** ;
#   * le poteau BA est implanté à **1,30 m du nu de la façade**, à
#     l'extrémité gauche des 8,03 m.
#
# La version antérieure (poteau à 2,00 m sous une poutre de 8,03 m appuyée
# sur ce seul poteau et sur le voile mitoyen) est ABANDONNÉE.

# Largeur totale de la terrasse, poutre-acrotère comprise (m).
LARGEUR_TERRASSE = 2.00

# Position de l'axe du poteau BA, depuis le nu extérieur de la façade (m).
POS_POTEAU_FAÇADE = 1.30

# Longueur (portée) de la poutre-acrotère isostatique, le long de la façade.
L_EXTENSION = 8.03

# Porte-à-faux de la poutre perpendiculaire au-delà du poteau (m).
PORTE_A_FAUX = LARGEUR_TERRASSE - POS_POTEAU_FAÇADE      # 0,70 m
CONSOLE_DALLE = LARGEUR_TERRASSE - 0.30                   # 1,70 m (nu int. poutre)

# Travée de la poutre perpendiculaire entre la façade et le poteau (m).
TRAVEE_PERPENDICULAIRE = POS_POTEAU_FAÇADE               # 1,30 m

# Épaisseur de la poutre-acrotère et largeur du voile de rive (m).
B_POUTRE = 0.30
EP_VOILE = 0.20

# Axe de la poutre de 8,03 m : nu extérieur à 2,00 m, largeur 0,30 m.
AXE_POUTRE_8M = LARGEUR_TERRASSE - B_POUTRE / 2.0        # 1,85 m

# Bande de dalle reprise par la poutre de 8,03 m (la dalle porte dans le
# sens de la largeur : une demi-largeur pour la façade, une pour la poutre).
BANDE_POUTRE_8M = LARGEUR_TERRASSE / 2.0                 # 1,00 m

# Longueur du voile de rive à créer (limite de propriété).
L_VOILE_RIVE = L_EXTENSION

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
