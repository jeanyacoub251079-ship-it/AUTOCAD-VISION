#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-50 — ASSEMBLAGES ET ANCRAGES — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13) — EC2 §8.4 / EC3-1-8 / EC5 §8.2 / NF EN 1992-4.

Sorties : _rendus/b50_assemblages.txt / .json + _plans/FLORA_B50_ASSEMBLAGES_IndA.{dxf,png,pdf}
Aucune capacité de connecteur inventée : les boulons sont calculés par l'EC3-1-8
(§3.6) à partir de leur classe, les assemblages bois par l'EC5 (§8.2, Johansen).
Les scellements dans la maçonnerie et les sabots exigeraient des fiches
techniques (DOC-09) : la FDC les exclut (prédalles). Ils sont donc traités en
PARAMÉTRIQUE DÉCLARÉ, avec une réserve — pas avec une valeur inventée.
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_rendus")
PLANS = os.path.join(ROOT, "_plans")
BASE = os.path.join(PLANS, "FLORA_B50_ASSEMBLAGES_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


# ============================================================== DONNÉES
# --- béton / armatures (EC2, NA)
FCK = 25.0
FCTK_005 = 1.8
GAMMA_C = 1.5
FYK = 500.0
GAMMA_S = 1.15
FYD = FYK / GAMMA_S
FCTD = FCTK_005 / GAMMA_C
PHI = 12.0
N_P2 = 159.0          # kN, B-42 Ind. B
M_P2 = 9.4            # kN.m, B-42 Ind. B
AS_P2 = 6 * math.pi * PHI ** 2 / 4.0

# --- acier de structure et boulonnerie
FY = 275.0            # S275 — MAT-05f
FU = 430.0
GAMMA_M0 = 1.0
GAMMA_M2 = 1.25
BOLT_CLASS = "8.8"
FUB = 800.0
FVB = 640.0

# ============================================================== EN-TÊTE
titre("=" * 78)
log("B-50 — ASSEMBLAGES ET ANCRAGES — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13) — EC2 §8.4/§6.7 · EC3-1-8 · EC5 §8.2")
log("Famille : TOUS — ancrages BA, assemblages métalliques, assemblages bois,")
log("          scellements maçonnerie. Mode : PARTIEL-DÉCLARÉ (DOC-09 exclue).")
log("=" * 78)

titre("[1] INVENTAIRE — CHAQUE ASSEMBLAGE ET SON ÉMETTEUR D'EFFORTS")
INVENTAIRE = [
    ("A1", "Ancrage des 6 HA12 de P2 dans SF1", "B-42 Ind. B", "N 159,0 kN · M 9,4 kN·m", "EC2 §8.4.4"),
    ("A2", "Boulonnage du moisage R1 (2 × UPE 200 / bois 20×15)", "B-45 Ind. A", "V 77,4 kN · M 74,5 kN·m", "EC5 §8.2 + EC3-1-8 §3.6"),
    ("A3", "Platine d'appui R3 sur R2 + reprise de torsion", "B-45 Ind. A", "V 23,1 kN · Mt 1,85 kN·m", "EC3-1-8 §6.2"),
    ("A4", "Scellement des entretoises Stab1 dans le voutain", "B-45 Ind. A", "F 5,8 kN par file", "EC6 §8 / NF EN 1992-4"),
    ("A5", "Platine de pied P1 sur SF1 (4 tiges)", "B-45 Ind. A", "N 100,3 kN", "EC2 §6.7 + EC3-1-8 §3.6"),
    ("A6", "Appuis F1 à R3 sur maçonnerie (8 appuis)", "B-45 Ind. A", "44,6 à 77,4 kN", "EC6 §8 — RENVOI B-46"),
]
log("  %-4s %-52s %-14s %-26s %s" % ("REF", "ASSEMBLAGE", "ÉMETTEUR", "EFFORTS", "RÉFÉRENTIEL"))
for r in INVENTAIRE:
    log("  %-4s %-52s %-14s %-26s %s" % r)

# ============================================================== A1
titre("[2] A1 — ANCRAGE DES 6 HA12 DE P2 DANS SF1 (EC2 § 8.4)")
eta1, eta2 = 1.0, 1.0
f_bd = 2.25 * eta1 * eta2 * FCTD
log("  f_ctd = %.2f / %.1f = %.3f MPa" % (FCTK_005, GAMMA_C, FCTD))
log("  f_bd = 2,25 x n1 x n2 x f_ctd = 2,25 x 1,0 x 1,0 x %.3f = %.2f MPa (EC2 8.4.2)"
    % (FCTD, f_bd))
log("  n1 = 1,0 (bonnes conditions d'adhérence, barres verticales coulées en fond")
log("       de coffrage) · n2 = 1,0 (phi = 12 <= 32 mm)")
log("")
log("  sigma_sd = f_yd = 500 / 1,15 = %.1f MPa  (cas enveloppe)" % FYD)
l_b_rqd = (PHI / 4.0) * (FYD / f_bd)
log("  l_b,rqd = (phi/4) (sigma_sd/f_bd) = (12/4) x (%.1f/%.2f) = %.0f mm" % (FYD, f_bd, l_b_rqd))
# coefficients
a1 = 0.7   # barre courbée (équerre)
a2 = 0.7   # enrobage 50 mm > 3 phi (36 mm)
a3 = 0.7   # confinement par cadres HA8 e150
l_bd = a1 * a2 * a3 * l_b_rqd
l_b_min = max(0.3 * l_b_rqd, 10 * PHI, 100.0)
log("  a1 = 0,70 (équerre, tab. 8.2) · a2 = 0,70 (c_nom 50 >= 3 phi) · a3 = 0,70 (cadres)")
log("  l_bd = a1 a2 a3 l_b,rqd = 0,70^3 x %.0f = %.0f mm" % (l_b_rqd, l_bd))
log("  l_b,min = max(0,3 l_b,rqd ; 10 phi ; 100) = max(%.0f ; %.0f ; 100) = %.0f mm"
    % (0.3 * l_b_rqd, 10 * PHI, l_b_min))
dispo = 250.0 - 50.0          # hauteur SF1 25 cm - enrobage 50 mm
log("")
log("  Longueur disponible dans SF1 : h 250 - c_nom 50 = %.0f mm" % dispo)
log("  l_bd = %.0f mm <= %.0f mm  ->  %s" % (l_bd, dispo, "OK" if l_bd <= dispo else "NON"))
log("  Marge = %.0f mm (%.0f %% de la longueur requise)"
    % (dispo - l_bd, 100 * (dispo - l_bd) / l_bd))
log("")
log("  CONTRÔLE CROISÉ (pièce 4) : le logement de SF1 (25 cm, c_nom 50) accepte")
log("  l'ancrage à condition que les TROIS réductions soient effectives :")
log("    - équerre en pied obligatoire (a1) : sinon l_bd = %.0f mm > %.0f mm  -> NON" % (a2 * a3 * l_b_rqd, dispo))
log("    - enrobage 50 mm tenu sur les 4 faces (a2)")
log("    - cadres HA8 e150 jusqu'en pied de semelle (a3)")
log("  Si une seule tombe, l'ancrage ne rentre plus : B-40 doit augmenter h.")
log("  -> Réserve R-50-1 : condition de validité, pas un écart constaté.")
log("")
log("  Recouvrement avec le treillis de SF1 : non nécessaire (barres d'attente")
log("  continues depuis la semelle), mais la jonction est prescrite en équerre")
log("  posée sur le lit inférieur (voir planche, détail 1).")

# ============================================================== A2
titre("[3] A2 — BOULONNAGE DU MOISAGE R1 (EC5 § 8.2, Johansen)")
D = 16.0
T1 = 200.0            # épaisseur de bois traversée = largeur de la poutre 20x15
RHO_K = 350.0         # kg/m3 — résineux structural, valeur enveloppe C18/C24
FU_K = 400.0          # MPa — résistance ultime de la tige (EC5 8.5.1.1)
KMOD = 0.8            # classe de service 2, charge de moyenne durée
GM_CONN = 1.3
f_h0k = 0.082 * (1 - 0.01 * D) * RHO_K
My_Rk = 0.3 * FU_K * D ** 2.6
log("  Bois : rho_k = %.0f kg/m3 · t1 = %.0f mm (largeur de poutre) · d = %.0f mm"
    % (RHO_K, T1, D))
log("  f_h,0,k = 0,082 (1 - 0,01 d) rho_k = %.2f MPa (EC5 8.5.1.1)" % f_h0k)
log("  M_y,Rk = 0,3 f_u,k d^2,6 = %.0f N.mm = %.1f N.m (EC5 8.5.1.1)" % (My_Rk, My_Rk / 1e3))
a_ = f_h0k * T1 * D
b_ = f_h0k * T1 * D * (math.sqrt(2 + 4 * My_Rk / (f_h0k * D * T1 ** 2)) - 1)
c_ = 2.3 * math.sqrt(My_Rk * f_h0k * D)
Fv_Rk = min(a_, b_, c_)
log("  Double cisaillement, plaques acier extérieures (2 x UPE) :")
log("    a) f_h t1 d ....................... = %.0f N" % a_)
log("    b) f_h t1 d [sqrt(2+4My/(fh d t1^2)) - 1] = %.0f N" % b_)
log("    c) 2,3 sqrt(My f_h d) ............. = %.0f N" % c_)
log("  F_v,Rk = min = %.1f kN par boulon (la ruine est le BROCHAGE du bois)" % (Fv_Rk / 1e3))
Fv_Rd_bois = KMOD * Fv_Rk / 1e3 / GM_CONN
log("  F_v,Rd = k_mod F_v,Rk / gM,conn = 0,80 x %.1f / 1,3 = %.2f kN"
    % (Fv_Rk / 1e3, Fv_Rd_bois))

# côté acier
A_S_M16 = 157.0
Fv_Rd_acier = 0.6 * FUB * A_S_M16 / GAMMA_M2 / 1e3
log("  Côté acier M16 8.8 : F_v,Rd = 0,6 x 800 x 157 / 1,25 = %.1f kN par plan de"
    % Fv_Rd_acier)
log("  cisaillement -> %.1f kN en double cisaillement. LE BOIS GOUVERNE (%.1f kN)."
    % (2 * Fv_Rd_acier, Fv_Rd_bois))
V_R1 = 77.4
n_req = V_R1 / Fv_Rd_bois
log("")
log("  V_Ed (R1) = %.1f kN -> n >= %.1f boulons" % (V_R1, n_req))
N_BOULONS = 10
log("  RETENU : %d boulons M16 8.8 par face, soit 5 rangées de 2" % N_BOULONS)
log("  Capacité = %d x %.2f = %.1f kN pour %.1f kN demandés -> taux %.3f"
    % (N_BOULONS, Fv_Rd_bois, N_BOULONS * Fv_Rd_bois, V_R1, V_R1 / (N_BOULONS * Fv_Rd_bois)))
# pression diamétrale dans le bois et espacements
log("  Espacements EC5 8.2.2 : e1 >= 4d = 64 mm · e2 >= 4d = 64 mm ·")
log("  e3 >= max(7d ; 80) = 112 mm · e4 >= 3d = 48 mm")
log("  Sur 3,85 m de poutre, 5 rangées à 700 mm d'entraxe : e1 = 700 mm >> 112 mm.")
log("  Hauteur 150 mm : 2 boulons par rangée à 50 mm du nu -> e2 = 90 mm > 64 mm.")
log("  CONDITION DE MAINTIEN LATÉRAL (R-45-2) : les UPE sont boulonnés de part et")
log("  d'autre, l'effort de stabilisation %.1f kN est repris par le même boulonnage."
    % 5.83)

# ============================================================== A3
titre("[4] A3 — LINTEAU R3 : TORSION DE LA SECTION OUVERTE (EC3 § 6.2.7)")
MT = 1.85e6                 # N.mm
IT_UPE200 = 9.6e4           # mm4
TF = 11.5                   # mm
tau_t = MT * TF / IT_UPE200
tau_Rd = FY / (math.sqrt(3) * GAMMA_M0)
log("  M_t = P x e = 46,2 x 0,040 = %.2f kN.m (excentrement de l'axe de cisaillement)"
    % (MT / 1e6))
log("  Torsion de Saint-Venant : tau_t = M_t t / I_T")
log("  I_T (UPE 200) = %.0f mm4 · t = t_f = %.1f mm" % (IT_UPE200, TF))
log("  tau_t = %.2e x %.1f / %.0f = %.1f MPa" % (MT, TF, IT_UPE200, tau_t))
log("  tau_Rd = f_y / (sqrt(3) gM0) = %.1f MPa" % tau_Rd)
log("  TAUX DE TORSION = %.3f  ->  %s" % (tau_t / tau_Rd, "NON" if tau_t > tau_Rd else "OK"))
log("")
log("  LA TORSION SEULE DÉPASSE LA RÉSISTANCE DE CISAILLEMENT : le UPE 200 ne peut")
log("  pas reprendre son excentrement, même avant d'ajouter la flexion.")
log("  -> La vérification de flexion de B-45 (0,291) est donc INSUFFISANTE seule :")
log("     elle ignore un effet qui vaut %.0f %% de la résistance." % (100 * tau_t / tau_Rd))
log("")
log("  PRESCRIPTION RETENUE (une seule, et elle est constructive) :")
log("    REMPLISSAGE BÉTON C25/30 ENTRE LES AILES DU UPE, SUR TOUTE LA LONGUEUR.")
log("    Le U devient une section fermée : I_T passe de 9,6e4 à l'ordre de 1e7 mm4")
log("    (évaluation d'ordre de grandeur, NON contractuelle), et la torsion n'est")
log("    plus un critère. Sans ce remplissage, le linteau est non conforme.")
log("    Variante possible : platine de répartition soudée en continu (B-60).")
log("  -> Réserve R-50-2 : prescription constructive à porter sur le plan coté.")

# ============================================================== A4
titre("[5] A4 — SCELLEMENT DES ENTRETOISES Stab1 DANS LE VOUTAIN — PARAMÉTRIQUE")
log("  Effort transmis par B-45 : F = 5,8 kN par file (enveloppe, portée 5,40 m).")
log("  Support : voutain de briques creuses 7 cm — MAÇONNERIE, pas béton.")
log("  Référentiel : EC6 § 8 et NF EN 1992-4 pour les ancrages chimiques.")
log("")
log("  CE QUI MANQUE, ET QUI N'EST PAS INVENTÉ :")
log("    - la fiche technique du scellement (DOC-09) : la FDC l'exclut explicitement")
log("      (D-05 : DOC-09 = fiches de prédalles, NON NÉCESSAIRE — B-48 sans objet) ;")
log("    - la résistance f_k de la maçonnerie (MAT-07, R-15) : non mesurée.")
log("  Sans ces deux données, AUCUNE capacité de scellement n'est calculable.")
log("")
log("  CE QUI EST PRESCRIT SANS CAPACITÉ CHIFFRÉE (et déclaré comme tel) :")
log("    - 2 tiges M12 par file, entraxe >= 100 mm, entraxe aux bords >= 150 mm ;")
log("    - scellement chimique à résine, profondeur >= 80 mm dans la brique pleine")
log("      (jamais dans une alvéole creuse) ;")
log("    - reprise de l'effort par BUTÉE sur le hourdis en plus du scellement :")
log("      l'entretoise ne travaille pas en traction pure, elle est en appui.");
log("  -> Réserve R-50-3 : capacité de scellement à justifier par fiche + essai")
log("     d'arrachement sur 1 file sur 4 avant généralisation.")

# ============================================================== A5
titre("[6] A5 — PLATINE DE PIED DE P1 SUR SF1")
N_P1 = 100.3
A_C0 = 200.0 * 200.0
F_CD = 0.85 * FCK / GAMMA_C
F_RDU = 1.5 * F_CD * A_C0 / 1e3
log("  N_Ed = %.1f kN · platine 200 x 200 mm · A_c0 = %.0f cm2" % (N_P1, A_C0 / 100))
log("  f_cd = 0,85 x 25 / 1,5 = %.2f MPa · F_Rdu = 1,5 f_cd A_c0 = %.0f kN"
    % (F_CD, F_RDU))
log("  Pression diamétrale (EC2 6.7) : taux = %.3f  -> OK" % (N_P1 / F_RDU))
Fv_Rd_M16 = 0.6 * FUB * A_S_M16 / GAMMA_M2 / 1e3
log("  4 tiges M16 8.8 : cisaillement = 4 x %.1f = %.1f kN" % (Fv_Rd_M16, 4 * Fv_Rd_M16))
log("  Effort tranchant à la base de P1 : NON fourni par B-45 (poteau comprimé,")
log("  vent non traité — CHG-06 non applicable, stabilité horizontale par la")
log("  maçonnerie, D-29). Les 4 tiges sont donc dimensionnées par le MINIMUM")
log("  constructif, pas par un effort : c'est écrit, pas sous-entendu.")
log("  -> Réserve R-50-4 : si un effort horizontal apparaît (vent, choc), le")
log("     nombre de tiges se recalcule. Aucune valeur n'est supposée ici.")

# ============================================================== A6
titre("[7] A6 — APPUIS MÉTALLIQUES SUR MAÇONNERIE : RENVOI À B-46, SANS CALCUL")
log("  8 appuis (F1a/b/c, F2, F3, F4, R1, R2-N/S, R3-N/S) reposent sur de la")
log("  maçonnerie en moellons. La contrainte d'appui vaut sigma = V_Ed / (a x b).")
log("  La résistance correspondante est f_k — MAT-07, NON MESURÉE (R-15).")
log("  D-34 fixe f_k = 1,5 MPa comme HYPOTHÈSE, pas comme mesure.")
log("  B-50 ne calcule donc PAS ces appuis : il transmet les réactions et renvoie")
log("  à B-46, qui porte la maçonnerie. C'est la règle de circulation de la fiche.")
log("  -> Réserve R-50-5 : appuis sur maçonnerie à vérifier en B-46 avec f_k")

# ============================================================== CONTRÔLE CROISÉ
titre("[8] CONTRÔLE CROISÉ — PIÈCE 4 (obligatoire)")
CROISE = [
    ("A1", "6 HA12 de P2", "SF1 80x80x25, c_nom 50", "l_bd 166 mm <= 200 mm", "OK sous 3 conditions", "-"),
    ("A2", "10 M16 8.8 par face", "poutre 20x15, 3,85 m", "e1 700 / e2 90 mm",
     "OK", "-"),
    ("A3", "torsion 1,85 kN.m", "UPE 200 ouvert", "tau 222 > 159 MPa", "NON",
     "B-60 (plan) — remplissage béton"),
    ("A4", "5,8 kN par file", "voutain brique 7 cm", "capacité inconnue", "NON CALCULABLE",
     "DOC-09 exclue + MAT-07"),
    ("A5", "4 M16 8.8", "SF1 80x80, platine 200x200", "sigma 2,51 MPa", "OK", "-"),
    ("A6", "8 appuis sur maçonnerie", "moellons, f_k non mesuré", "sigma non calculable",
     "RENVOI", "B-46"),
]
log("  %-4s %-24s %-28s %-26s %-16s %s"
    % ("REF", "ANCRAGE CALCULÉ", "LOGEMENT / SUPPORT", "CONTRÔLE", "VERDICT", "RENVOI"))
for r in CROISE:
    log("  %-4s %-24s %-28s %-26s %-16s %s" % r)
log("")
log("  RÈGLE APPLIQUÉE : B-50 ne corrige AUCUN écart à la place des briques.")
log("  Les deux écarts constatés (A3, A4) sont signalés, identifiés et renvoyés.")
log("  Aucune valeur n'est réduite, aucune capacité n'est inventée.")

# ============================================================== NOMENCLATURE
titre("[9] NOMENCLATURE DES CONNECTEURS")
NOMEN = [
    ("Boulon M16 8.8 + écrou + 2 rondelles", "20 u", "Moisage R1 (10 par face)"),
    ("Tige M16 8.8 à scellement chimique", "8 u", "Platine de pied P1 (4 par poteau)"),
    ("Tige M12 à scellement chimique", "8 u", "Stab1 (2 par file, 4 files)"),
    ("Platine 200 x 200 x 15", "2 u", "Pied de P1-N et P1-S"),
    ("Platine d'about 160 x 160 x 12", "18 u", "Appuis F1 à R3 sur maçonnerie"),
    ("Béton C25/30 de remplissage", "—", "Remplissage des UPE 200 de R3"),
]
log("  %-46s %-6s %s" % ("DÉSIGNATION", "QTÉ", "EMPLOI"))
for r in NOMEN:
    log("  %-46s %-6s %s" % r)

# ============================================================== JSON
res = dict(
    mode="PARTIEL-DÉCLARÉ",
    a1=dict(f_bd=round(f_bd, 2), l_b_rqd=round(l_b_rqd), l_bd=round(l_bd),
            l_b_min=round(l_b_min), dispo=200, ok=True),
    a2=dict(Fv_Rk_kN=round(Fv_Rk / 1e3, 1), Fv_Rd_bois=round(Fv_Rd_bois, 2),
            n=10, taux=round(V_R1 / (10 * Fv_Rd_bois), 3)),
    a3=dict(tau=round(tau_t, 1), tau_Rd=round(tau_Rd, 1),
            taux=round(tau_t / tau_Rd, 3), verdict="NON"),
    a5=dict(taux_pression=round(N_P1 / F_RDU, 3)),
    ecarts=2, renvois=2,
)

# ============================================================== PLANCHE
import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

doc = ezdxf.new("R2018", setup=True)
msp = doc.modelspace()
for nom, coul in (("ASSEMBLAGE-AXES", 1), ("ASSEMBLAGE-DETAILS", 5),
                  ("ASSEMBLAGE-NOMENCLATURE", 3), ("ASSEMBLAGE-HABILLAGE-TEXTE", 7),
                  ("ASSEMBLAGE-COTATION", 8), ("ASSEMBLAGE-CARTOUCHE", 7)):
    doc.layers.add(nom, color=coul)


def txt(x, y, t, ht=2.4, layer="ASSEMBLAGE-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))


def rect(x0, y0, x1, y1, layer="ASSEMBLAGE-DETAILS"):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})


def ligne(x0, y0, x1, y1, layer="ASSEMBLAGE-DETAILS"):
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})


rect(8, 8, 412, 289, "ASSEMBLAGE-CARTOUCHE")
txt(14, 279, "CROISSY-FLORA — B-50 — ASSEMBLAGES ET ANCRAGES", 3.8, "ASSEMBLAGE-AXES")
txt(14, 272.5, "Indice A — 21/10/2026 — Mode PARTIEL-DÉCLARÉ — NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 2.4, "ASSEMBLAGE-AXES")
txt(14, 267, "Protection au feu des assemblages NON dimensionnée — hors lot GO.", 2.3)

# --- D1 : ancrage HA12 dans SF1
txt(14, 257, "1. A1 — ANCRAGE DES 6 HA12 DE P2 DANS SF1 — COUPE", 2.5, "ASSEMBLAGE-AXES")
x0, y0 = 26, 214
rect(x0, y0, x0 + 40, y0 + 12.5, "ASSEMBLAGE-DETAILS")          # SF1 80x25 -> 40x12.5
rect(x0 + 12.5, y0 + 12.5, x0 + 20, y0 + 30, "ASSEMBLAGE-DETAILS")  # P2 15x25 -> 7.5x?
for xb in (x0 + 3, x0 + 13.5, x0 + 18.5, x0 + 7.5):
    ligne(xb, y0 + 2.5, xb, y0 + 27, "ASSEMBLAGE-AXES")
ligne(x0 + 2, y0 + 2.5, x0 + 38, y0 + 2.5, "ASSEMBLAGE-AXES")
txt(x0 + 41, y0 + 18, "P2 — 15 x 25 — 6 HA12", 2.0, "ASSEMBLAGE-AXES")
txt(x0 + 41, y0 + 13.5, "l_bd = %d mm (équerre + enrobage + cadres)" % l_bd, 2.0, "ASSEMBLAGE-AXES")
txt(x0 + 41, y0 + 9, "Disponible : 250 − 50 = 200 mm", 2.0)
txt(x0 + 41, y0 + 4.5, "Marge 34 mm — les 3 réductions sont OBLIGATOIRES", 2.0, "ASSEMBLAGE-AXES")
txt(x0 + 2, y0 - 6, "SF1 80 x 80 x 25 — c_nom 50 — HA8 e150 (B-40)", 2.0)
txt(x0 + 44, y0 + 21, "Équerre en pied, cadres jusqu'en pied", 1.9, "ASSEMBLAGE-COTATION")

# --- D2 : moisage R1 boulonné
txt(14, 194, "2. A2 — BOULONNAGE DU MOISAGE R1 — 10 M16 8.8 PAR FACE", 2.5, "ASSEMBLAGE-AXES")
xb2, yb2 = 26, 170
rect(xb2, yb2, xb2 + 20, yb2 + 15, "ASSEMBLAGE-DETAILS")
for signe in (-1, 1):
    xa = xb2 + (0 if signe < 0 else 20)
    ligne(xa + signe * 0.65, yb2 - 2, xa + signe * 0.65, yb2 + 17, "ASSEMBLAGE-DETAILS")
    ligne(xa + signe * 0.65, yb2 - 2, xa + signe * 8.65, yb2 - 2, "ASSEMBLAGE-DETAILS")
    ligne(xa + signe * 0.65, yb2 + 17, xa + signe * 8.65, yb2 + 17, "ASSEMBLAGE-DETAILS")
for yb in (yb2 + 4, yb2 + 7.5, yb2 + 11):
    ligne(xb2 - 6, yb, xb2 + 26, yb, "ASSEMBLAGE-AXES")
txt(xb2 - 6, yb2 + 19.5, "2 × UPE 200 (S275) — moisage", 2.0, "ASSEMBLAGE-AXES")
txt(xb2 + 30, yb2 + 11, "5 rangées × 2 boulons, e1 = 700 mm", 2.0)
txt(xb2 + 30, yb2 + 6.5, "F_v,Rd = %.1f kN/boulon — le BOIS gouverne" % Fv_Rd_bois, 2.0, "ASSEMBLAGE-AXES")
txt(xb2 + 30, yb2 + 2, "Taux = %.2f pour 77,4 kN" % (V_R1 / (10 * Fv_Rd_bois)), 2.0)
txt(xb2 + 30, yb2 - 2.5, "Rondelles larges — harnais proscrit sur bois sec", 2.0)

# --- D3 : R3 torsion
txt(14, 152, "3. A3 — R3 : TORSION NON REPRISE PAR LE UPE SEUL", 2.5, "ASSEMBLAGE-AXES")
xc, yc = 26, 128
ligne(xc, yc, xc + 31, yc, "ASSEMBLAGE-DETAILS")
ligne(xc, yc + 20, xc + 31, yc + 20, "ASSEMBLAGE-DETAILS")
ligne(xc, yc, xc, yc + 20, "ASSEMBLAGE-DETAILS")
ligne(xc + 31, yc, xc + 31, yc + 20, "ASSEMBLAGE-DETAILS")
for k in range(1, 6):
    ligne(xc + k * 5, yc + 1, xc + k * 5, yc + 19, "ASSEMBLAGE-NOMENCLATURE")
txt(xc + 34, yc + 15, "tau_t = %.0f MPa pour %.0f MPa admis" % (tau_t, tau_Rd), 2.0, "ASSEMBLAGE-AXES")
txt(xc + 34, yc + 10.5, "TAUX = %.2f — NON conforme" % (tau_t / tau_Rd), 2.0, "ASSEMBLAGE-AXES")
txt(xc + 34, yc + 6, "→ remplissage béton C25/30 entre ailes", 2.0)
txt(xc + 34, yc + 1.5, "→ section fermée : torsion supprimée", 2.0)
txt(xc + 2, yc - 6, "UPE 200 — remplissage béton (hachures)", 2.0, "ASSEMBLAGE-NOMENCLATURE")

# --- D4 : Stab1
txt(14, 112, "4. A4 — Stab1 : SCELLEMENT DANS LE VOUTAIN", 2.5, "ASSEMBLAGE-AXES")
xd, yd = 26, 88
rect(xd, yd, xd + 60, yd + 6, "ASSEMBLAGE-DETAILS")
for k in range(4):
    xk = xd + 8 + k * 14
    ligne(xk, yd - 6, xk, yd + 6, "ASSEMBLAGE-AXES")
    msp.add_circle((xk, yd - 3), 0.8, dxfattribs={"layer": "ASSEMBLAGE-COTATION"})
txt(xd, yd + 8, "2 tiges M12 par file · profondeur >= 80 mm · jamais en alvéole creuse", 2.0)
txt(xd, yd - 9, "F = 5,8 kN par file — capacité NON calculable (DOC-09 exclue)", 1.9, "ASSEMBLAGE-AXES")

# --- tableau de contrôle croisé
tx0, ty0, tx1, ty1 = 150, 108, 405, 258
rect(tx0, ty0, tx1, ty1, "ASSEMBLAGE-CARTOUCHE")
txt(tx0 + 3, 253, "CONTRÔLE CROISÉ — PIÈCE 4 (amont / logement / verdict / renvoi)", 2.6, "ASSEMBLAGE-AXES")
cols = (tx0 + 3, tx0 + 20, tx0 + 88, tx0 + 166, tx0 + 236)
for c, t in zip(cols, ("RÉF", "ANCRAGE / EFFORT", "LOGEMENT VÉRIFIÉ", "CONTRÔLE", "VERDICT")):
    txt(c, 245, t, 2.0, "ASSEMBLAGE-AXES")
lignes_c = [
    ("A1", "6 HA12 — N 159,0 kN", "SF1 80×80×25 — c 50", "l_bd 166 ≤ 200", "OK (3 cond.)"),
    ("A2", "10 M16 8.8 — V 77,4 kN", "poutre 20×15 — 3,85 m", "e1 700 / e2 90", "OK — 0,69"),
    ("A3", "Mt 1,85 kN·m", "UPE 200 — section ouverte", "τ 222 > 159 MPa", "NON (R-50-2)"),
    ("A4", "F 5,8 kN / file", "voutain brique 7 cm", "capacité inconnue", "À JUSTIFIER"),
    ("A5", "4 M16 — N 100,3 kN", "SF1 — platine 200×200", "σc 2,51 MPa", "OK — 0,12"),
    ("A6", "8 appuis 23 à 77 kN", "moellons — f_k non mesuré", "σ non calculable", "RENVOI B-46"),
]
for k, l in enumerate(lignes_c):
    y = 237 - k * 7.0
    for c, v in zip(cols, l):
        txt(c, y, v, 1.95, "ASSEMBLAGE-AXES" if k == 2 else "ASSEMBLAGE-HABILLAGE-TEXTE")
txt(tx0 + 3, 186, "RÈGLE : B-50 ne corrige aucun écart — il signale, identifie et renvoie.", 2.1, "ASSEMBLAGE-AXES")
txt(tx0 + 3, 180, "2 écarts constatés (A3, A4) — 2 renvois (B-60, B-46). Aucune capacité inventée.", 2.1)

# --- nomenclature
txt(tx0 + 3, 170, "NOMENCLATURE DES CONNECTEURS", 2.6, "ASSEMBLAGE-AXES")
nom_l = [
    ("Boulon M16 8.8 + écrou + 2 rondelles", "20 u", "Moisage R1"),
    ("Tige M16 8.8 — scellement chimique", "8 u", "Pied de P1 (4/poteau)"),
    ("Tige M12 — scellement chimique", "8 u", "Stab1 (2/file)"),
    ("Platine 200×200×15", "2 u", "Pied P1"),
    ("Platine d'about 160×160×12", "18 u", "Appuis F1 à R3"),
    ("Béton C25/30 de remplissage", "—", "UPE 200 de R3"),
]
txt(tx0 + 3, 162, "DÉSIGNATION", 2.0, "ASSEMBLAGE-AXES")
txt(tx0 + 150, 162, "QTÉ", 2.0, "ASSEMBLAGE-AXES")
txt(tx0 + 180, 162, "EMPLOI", 2.0, "ASSEMBLAGE-AXES")
for k, (a, b, c_) in enumerate(nom_l):
    y = 155 - k * 5.4
    txt(tx0 + 3, y, a, 1.95)
    txt(tx0 + 150, y, b, 1.95)
    txt(tx0 + 180, y, c_, 1.95)

# --- notes opposables (espace libre sous A4)
n0 = 150
txt(n0, 103, "NOTES OPPOSABLES", 2.4, "ASSEMBLAGE-AXES")
notes = [
    "1. A1 : équerre + enrobage 50 + cadres HA8 = les 3 réductions sont OBLIGATOIRES.",
    "2. A2 : 10 M16 par face — le BOIS gouverne (11,2 kN), pas l'acier (120,6 kN).",
    "3. A3 : UPE 200 NON conforme en torsion → remplissage béton C25/30 entre ailes.",
    "4. A4 : capacité de scellement NON calculée (DOC-09 exclue, f_k non mesuré).",
    "5. A5 : 4 tiges = minimum constructif, aucun effort horizontal transmis.",
    "6. A6 : appuis sur maçonnerie renvoyés à B-46 (f_k, D-34, R-15).",
    "7. Protection au feu des assemblages NON dimensionnée — hors lot GO.",
]
for k, t in enumerate(notes):
    col, row = (0, k) if k < 4 else (1, k - 4)
    txt(n0 + col * 130, 97 - row * 5.0, t, 1.85)

# --- cartouche
rect(14, 10, 405, 55, "ASSEMBLAGE-CARTOUCHE")
txt(18, 47, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 3.2, "ASSEMBLAGE-AXES")
txt(18, 39, "B-50 — ASSEMBLAGES ET ANCRAGES", 2.5)
txt(18, 32, "Brique B-50 · Indice A · 21/10/2026 · Mode PARTIEL-DÉCLARÉ · Unités DXF : mm · schémas sans échelle", 2.1)
txt(18, 25, "EC2 §8.4 / §6.7 · EC3-1-8 §3.6 / §6.2.7 · EC5 §8.2 · CARNAC v3.0", 2.1)
txt(18, 14, "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 4.0, "ASSEMBLAGE-AXES")

chemin = BASE + ".dxf"
doc.saveas(chemin)
audit = doc.audit()
log("")
log("  écrit : %s (%d o) — audit %d erreur(s)"
    % (chemin, os.path.getsize(chemin), len(audit.errors)))

fig = plt.figure(figsize=(16.54, 11.69))
ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
cfg = Configuration(background_policy=BackgroundPolicy.WHITE)
Frontend(RenderContext(doc), MatplotlibBackend(ax), config=cfg).draw_layout(msp, finalize=False)
ax.set_xlim(0, 420)
ax.set_ylim(0, 297)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")
fig.savefig(BASE + ".png", dpi=200, facecolor="white")
fig.savefig(BASE + ".pdf", facecolor="white")
plt.close(fig)
log("  rendus : %s.png / .pdf" % BASE)

with open(os.path.join(OUT, "b50_assemblages.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b50_assemblages.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)

log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b50_assemblages.txt"),
                             os.path.getsize(os.path.join(OUT, "b50_assemblages.txt"))))
log("JSON    : %s (%d o)" % (os.path.join(OUT, "b50_assemblages.json"),
                             os.path.getsize(os.path.join(OUT, "b50_assemblages.json"))))
