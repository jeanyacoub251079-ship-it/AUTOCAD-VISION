#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-46 — MAÇONNERIE : VÉRIFICATION ET CONCEPTION — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13) — EC6 (NF EN 1996-1-1) §5.5 / §6.1 / §6.2 / §8.

Sorties : _rendus/b46_maconnerie.txt / .json + _plans/FLORA_B46_MACONNERIE_IndA.{dxf,png,pdf}

Règles du dossier :
- f_k = 1,5 MPa et f_vk0 = 0,15 MPa sont les HYPOTHÈSES NOTIFIÉES H-25 / H-26
  (décision D-34) — jamais des mesures (MAT-07 n'est pas mesurée).
- Les 8 appuis viennent de B-45 Ind. A §11 (efforts transmis) ; les sommiers
  S1/S2 de B-20 (D2 Folio 01) ; la géométrie des voiles de B-25 §2.3 (D5).
- Aucun scellement n'est calculé (c'est B-50). Aucune valeur hors FDC.
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_rendus")
PLANS = os.path.join(ROOT, "_plans")
BASE = os.path.join(PLANS, "FLORA_B46_MACONNERIE_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


# ============================================================== DONNÉES
# --- maçonnerie existante : hypothèses notifiées (H-25, H-26 — D-34)
FK = 1.5            # MPa — HYPOTHÈSE (D-34), non mesurée (MAT-07)
E_MOD = 1500.0      # MPa — E = 1000 f_k (EC6 §3.7.2, H-25)
FVK0 = 0.15         # MPa — H-26
GAMMA_M = 2.5       # maçonnerie non contrôlée (H-26, usage B-25)
FD = FK / GAMMA_M   # 0,60 MPa
SIGMA_D = 0.069     # MPa — contrainte moyenne voiles RDC (B-21 C §7)
SIGMA_D_LOC = 0.159  # MPa — max N/A_inf sous P1 (B-21 C §6.2)
H = 3000.0          # mm — hauteur RDC 0,00 → 3,00 (B-25)
S_PRE = (H / 2.0) * math.tan(math.radians(30.0))   # dispersion 60° jusqu'à mi-hauteur

# --- les 8 appuis transmis par B-45 Ind. A §11, supportés par sommiers S1/S2 (B-20)
# w_b = longueur d'appui le long du mur, t = épaisseur du mur au droit de l'appui
APPUIS = [
    ("F1a/b/c", 44.6, "S2 20x50x20", 200.0, 500.0),
    ("F2", 62.4, "S1 20x40x20", 200.0, 400.0),
    ("F3", 61.6, "S1 20x40x20", 200.0, 400.0),
    ("F4", 11.5, "S1 20x40x20", 200.0, 400.0),
    ("R1", 77.4, "S2 20x50x20", 200.0, 500.0),
    ("R2-N", 46.2, "S2 20x50x20", 200.0, 500.0),
    ("R2-S", 35.9, "S2 20x50x20", 200.0, 500.0),
    ("R3-N/S", 23.1, "S1 20x40x20", 200.0, 400.0),
]
A1_SERIE = (0.0, 500.0, 1000.0, 2000.0)   # mm — distance au bout de mur (inconnue : plage)

# --- voiles RDC (B-25 §2.3 — t_eq = A/L issus des blocs D5)
VOILES = [
    ("M01", 0.31), ("M02", 0.39), ("M03", 0.88), ("M04", 0.57),
    ("M05", 0.15), ("M06", 0.24), ("M07", 0.21), ("M08", 0.36),
    ("M09", 0.85), ("M10", 0.48), ("M11", 0.60), ("M12", 0.37),
]

# --- appuis des neufs sur soubassement moellons (B-21 C, B-40 F)
SEMELLE = 600.0   # mm — semelle type 60x60 (D-14) si soubassement insuffisant (D-19)
NEUFS = [("P1-N", 100.3), ("P1-S", 100.3), ("P3", 35.8), ("J1", 39.8)]


def beta_ec6(a1, w_b, t):
    """EC6 §6.1.3 (6.10)-(6.11) — facteur de majoration pour charge concentrée."""
    l_efm = min(a1, S_PRE) + w_b + S_PRE       # dispersion 60° vers mi-hauteur, bornée
    A_b = w_b * t
    A_ef = l_efm * t
    r = min(A_b / A_ef, 0.45)                  # Ab/Aef plafonné à 0,45 (fig. 6.2)
    brut = (1.0 + 0.3 * a1 / H) * (1.5 - 1.1 * r)
    beta = min(max(brut, 1.0), 1.5, 1.25 + a1 / (2.0 * H))
    return beta, l_efm, A_b, A_ef, r


def n_rdc(a1, w_b, t, fk):
    beta, l_efm, A_b, A_ef, r = beta_ec6(a1, w_b, t)
    return beta * A_b * (fk / GAMMA_M) / 1000.0   # kN


def a1_critique(v_ed, w_b, t, fk):
    """Plus petite distance au bout de mur rendant l'appui admissible (µm : 10 mm)."""
    for a1 in range(0, 5001, 10):
        if n_rdc(float(a1), w_b, t, fk) >= v_ed:
            return float(a1)
    return None


# ============================================================== EN-TÊTE
titre("=" * 78)
log("B-46 — MAÇONNERIE : VÉRIFICATION ET CONCEPTION — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13) — EC6 (NF EN 1996-1-1) §5.5/§6.1/§6.2/§8")
log("Famille : MACONNERIE — bloc A (vérification existant) + orientations bloc B.")
log("Mode : PARTIEL-DÉCLARÉ (hypothèses notifiées H-25/H-26 sous D-34).")
log("COMPLET INTERDIT : MAT-07 non mesurée, EXI-05 verrou, GEO-03 non relevé,")
log("MAT-09 à MAT-12 bloquantes.")
log("=" * 78)

titre("[0] HYPOTHÈSES NOTIFIÉES — CLAUSE D-34 (à reporter en majuscules)")
log("  f_k  = 1,5 MPa (H-25) — HYPOTHÈSE D'ÉTUDE À CONFIRMER PAR ESSAIS.")
log("  E    = 1 500 MPa (E = 1000 f_k, EC6 §3.7.2).")
log("  f_vk0 = 0,15 MPa (H-26). gamma_M = 2,5 → f_d = 0,60 MPa.")
log("  NOS ÉTUDES SONT RÉALISÉES AVEC CES HYPOTHÈSES. LA CONFIRMATION PAR ESSAIS")
log("  EST HORS DE NOTRE MISSION ET À LA CHARGE DU MAÎTRE D'OUVRAGE. SI LES ESSAIS")
log("  NE SONT PAS CONCLUANTS, LA REPRISE DE NOS ÉTUDES FAIT L'OBJET D'UNE")
log("  PRESTATION COMPLÉMENTAIRE CHIFFRÉE.")
log("  Sismique : SANS OBJET (D-26, zone de sismicité 1) — AUCUNE VÉRIFICATION.")
log("  Joints : AUCUN JOINT DE DILATATION (D-28).")
log("  D-09 : ARASE −1,00 M / TN MINIMUM ; ÉGALISATION GROS BÉTON SI ÉCART.")

# ============================================================== A1
titre("[1] A1 — DONNÉES D'ENTRÉE ET PREUVE D'ÉPUISEMENT")
ENTREES = [
    ("MAT-07", "résistance maçonnerie", "NON MESURÉE → H-25 (D-34)", "D2 f.03 · D4 p.19"),
    ("EXI-05", "contrainte admissible", "VERROU — valeurs « à la limite »", "D3 p.17"),
    ("GEO-03", "épaisseurs murs", "NON RELEVÉES → t_eq D5 (B-25)", "B-25 §2.3 · PA-01"),
    ("MAT-09", "classe de bloc NF EN 771-3", "BLOQUANTE (« pleins ou semi-pleins »)", "D1 §01.2.1.7.5"),
    ("MAT-10", "classe de mortier", "BLOQUANTE (« hydrofugé »)", "D1 §01.2.1.7.5"),
    ("MAT-11", "type (chaînée/armée)", "BLOQUANTE", "D1 §01.2.1.7.5"),
    ("MAT-12", "chaînages existants", "AUCUN RELEVÉ", "D2 · D3 · PA-01"),
    ("CHG-07", "sismique", "SANS OBJET (D-26)", "D2 p.1"),
]
log("  %-8s %-32s %-42s %s" % ("CODE", "OBJET", "STATUT", "SOURCE"))
for r in ENTREES:
    log("  %-8s %-32s %-42s %s" % r)
log("")
log("  Épuisement (V14) : D2 f.03 (soubassement moellons, semelle 25×25) · D3 p.10-17")
log("  (planchers, pieds « à la limite ») · D4 p.19 (mur moellons apparents) · D5 blocs")
log("  (géométrie des voiles, B-25) · B-20 §4-5 (sommiers S1/S2, implantation) ·")
log("  B-21 §6-7 (N_ELU par porteur) · B-24 §2 (E-01 murs) · B-25 §2-3 (voiles, vent) ·")
log("  B-45 §10-11 (8 réactions) · B-50 §8 (A6, R-50-5). Aucune donnée absente non cherchée.")

# ============================================================== A2 — Z1 voiles
titre("[2] Z1 — VOILES PORTEURS EXISTANTS : COMPRESSION ET FLAMBEMENT (EC6 §6.1.2, §5.5)")
log("  Formule (EC6 §6.1.2) : N_Ed/(Phi · t · L) ≤ f_d = f_k/gamma_M = %.2f MPa" % FD)
log("  Flambement (EC6 §5.5) : lambda = h_ef/t_ef ≤ 27 · e_init = h_ef/450")
log("  h_ef = 1,00 h = %.0f mm (planchers bois/mixtes : rho2 = 1,0 — prudent)" % H)
log("")
log("  %-6s %-8s %-8s %-8s %-10s %-10s %s" % ("VOILE", "t_eq(m)", "lambda", "Phi_i", "sigma_d", "taux", "VERDICT"))
voiles_res = []
for nom, t in VOILES:
    te = t * 1000.0
    lam = H / te
    e_init = H / 450.0
    phi = 1.0 - 2.0 * e_init / te
    taux = SIGMA_D_LOC / (phi * FD)
    ok = lam <= 27.0 and taux <= 1.0
    voiles_res.append({"voile": nom, "t_eq": t, "lambda": round(lam, 1),
                       "phi_i": round(phi, 3), "taux": round(taux, 3),
                       "ok": ok})
    log("  %-6s %-8.2f %-8.1f %-8.3f %-10.3f %-10.3f %s"
        % (nom, t, lam, phi, SIGMA_D_LOC, taux, "OK" if ok else "NON"))
log("")
log("  Contrainte moyenne (B-21 C §7) : %.3f MPa — taux global %.3f" % (SIGMA_D, SIGMA_D / (FD)))
log("  Contrainte locale retenue : %.3f MPa (max N/A_inf, B-21 C §6.2 — sous P1)" % SIGMA_D_LOC)
log("  Cisaillement : renvoi B-25 (tau/f_vk ≤ 0,043 — vent, H-27) — f_vk = f_vk0+0,4*sigma_d")
f_vk = FVK0 + 0.4 * SIGMA_D
log("  f_vk(sigma_d=%.3f) = %.3f MPa → f_vd = %.3f MPa (gamma_M=2,5)" % (SIGMA_D, f_vk, f_vk / GAMMA_M))

# ============================================================== A2 — Z2 appuis
titre("[3] Z2 — LES 8 APPUIS SUR MAÇONNERIE (EC6 §6.1.3) — RÉPONSE À R-50-5")
log("  Charge concentrée (EC6 §6.1.3) : N_Edc ≤ N_Rdc = beta · A_b · f_d  (6.10)")
log("  beta = (1+0,3 a1/h_c)·(1,5−1,1 A_b/A_ef) — (6.11)")
log("  Plafonds : beta = min(beta ; 1,5 ; 1,25+a1/(2 h_c)) · plancher 1,0 · A_b/A_ef ≤ 0,45")
log("  l_efm = min(a1;s) + w_b + min(a2;s), s = (h_c/2)·tan30 = %.0f mm (fig. 6.2)" % S_PRE)
log("  A_b = aire du sommier (B-20) — appui mini 90 mm (EC6 §8.1.6) — e ≤ t/4 (6.1.3(4))")
log("  a1 = distance au bout de mur : NON RELEVÉE → plage déclarée 0 / 0,50 / 1,00 / 2,00 m")
log("")
log("  %-9s %-7s %-13s %-9s %-9s %-9s %-9s %s"
    % ("APPUIS", "V_Ed", "SOMMIER", "N(β=1)", "N(a1=0)", "N(a1=2m)", "a1 crit.", "VERDICT"))
appuis_res = []
for nom, v, som, w_b, t in APPUIS:
    n_beta1 = w_b * t * FD / 1000.0
    n0 = n_rdc(0.0, w_b, t, FK)
    n2 = n_rdc(2000.0, w_b, t, FK)
    ac = a1_critique(v, w_b, t, FK)
    ok_partout = v <= n0
    ok_reserve = (not ok_partout) and (ac is not None)
    if ok_partout:
        verdict = "OK"
    elif ok_reserve:
        verdict = "OK si a1≥%.2f" % (ac / 1000.0)
    else:
        verdict = "NON"
    appuis_res.append({
        "appui": nom, "V_kN": v, "sommier": som, "A_b_mm2": w_b * t,
        "N_beta1_kN": round(n_beta1, 1), "N_a1_0_kN": round(n0, 1),
        "N_a1_2m_kN": round(n2, 1), "a1_crit_mm": ac, "verdict": verdict,
    })
    log("  %-9s %-7.1f %-13s %-9.1f %-9.1f %-9.1f %-9s %s"
        % (nom, v, som, n_beta1, n0, n2,
           ("%.2f m" % (ac / 1000.0)) if ac is not None else "> 5 m", verdict))
log("")
log("  Lecture : 5 appuis sont admissibles MÊME sans majoration (beta = 1).")
log("  R1 (77,4), F2 (62,4) et F3 (61,6) exigent la majoration EC6 §6.1.3 ET")
log("  a1 ≥ ~0,25 m : ils sont NON admissibles en borne basse a1 = 0.")
log("  En beta = 1 (unités groupe 2/3/4 — EC6 §6.1.3(3)) : R1, F2, F3 NON conformes.")

# ============================================================== A2 — Z3
titre("[4] Z3 — APPUIS DES NEUFS SUR SOUBASSEMENT MOELLONS (B-21 C / B-40 F)")
log("  Semelle type 60×60 (D-14) ou appui vérifié en fouille — nuages D-19 (B-40).")
log("  sigma = N_ELU / A ≤ f_d = %.2f MPa" % FD)
log("")
for nom, n in NEUFS:
    sig = n * 1000.0 / (SEMELLE * SEMELLE)
    log("  %-6s N_ELU %5.1f kN — A = %.2f m² — sigma = %.3f MPa — taux %.3f %s"
        % (nom, n, (SEMELLE / 1000.0) ** 2, sig, sig / FD,
           "OK" if sig <= FD else "NON"))
log("  Sous réserve de la reconnaissance du soubassement en fouille (D-19, H-15).")

# ============================================================== sensibilité
titre("[5] SENSIBILITÉ f_k — NON CONTRACTUEL (méthode B-24)")
log("  Plage f_k plausible pour maçonnerie de moellons : 0,5 à 2,0 MPa.")
log("  Taux = V_Ed / N_Rdc(a1 = 2,00 m — borne favorable).")
log("")
log("  %-9s %s" % ("APPUIS", "  ".join("f_k=%.1f" % f for f in (0.5, 1.0, 1.5, 2.0))))
sens = {}
for nom, v, som, w_b, t in APPUIS:
    vals = []
    for fk in (0.5, 1.0, 1.5, 2.0):
        vals.append(round(v / n_rdc(2000.0, w_b, t, fk), 3))
    sens[nom] = vals
    log("  %-9s %s" % (nom, "  ".join("%9.3f" % x for x in vals)))
log("")
log("  R1, F2 et F3 dépassent 1,0 dès f_k ≤ 1,2 MPa environ, même en a1 favorable :")
log("  leur admissibilité REPOSE sur l'hypothèse f_k = 1,5 MPa (D-34).")

# ============================================================== Bloc B
titre("[6] BLOC B — ORIENTATIONS DE RENFORCEMENT (MAT-09 à MAT-12 bloquantes)")
log("  1. R1/F2/F3 — si a1 < 0,25 m (about de mur) : coussin de répartition ou")
log("     sommier élargi (w_b 200 → 300 mm min) — orientation, dimensionnement")
log("     définitif reporté (classe de bloc/mortier/type bloquantes).")
log("  2. Chaînages (EC6 §8.5) : AUCUN chaînage existant relevé (MAT-12).")
log("     Prescription de chaînage horizontal en tête de mur, liaison planchers/murs")
log("     et fondations — orientation, à porter en B-60. Aucun scellement calculé ici")
log("     (c'est B-50). Aucun effort de scellement transmis : aucun chaînage")
log("     rapporté n'est dimensionné dans cette note.")
log("  3. Sismique : AUCUNE disposition EC8 (D-26) — les chaînages ci-dessus relèvent")
log("     des dispositions constructives EC6 §8.5, pas d'une vérification sismique.")
log("  4. Protection au feu : mention générique seule (hors lot GO) — NON dimensionnée.")
log("  5. Spécialiste : injection, tirants actifs, précontrainte, reprise en sous-œuvre")
log("     = HORS périmètre (B-40 + phasage pour la reprise ; spécialiste pour le reste).")

# ============================================================== auto-contrôle
titre("[7] AUTO-CONTRÔLE DÉCLARÉ — ZONE PAR ZONE")
AC = [
    ("Z1 voiles", "compression %.3f/%.3f + lambda≤27" % (SIGMA_D_LOC, FD), "OK", "Φ_i min 0,911 (M05)"),
    ("Z2 appuis", "8 appuis EC6 §6.1.3", "5 OK / 3 sous réserve", "R-46-1 (a1), R-46-2 (groupe)"),
    ("Z3 soubassement", "4 appuis neufs (D-19)", "OK sous fouille", "reconnaissance ENC"),
    ("Z4 linteaux E-08", "capacité inconnue", "RENVOI B-49", "R-46-4"),
    ("Cisaillement", "tau/f_vk (B-25)", "OK (0,043)", "renvoi B-25 — H-27"),
    ("Chaînages EC6 §8.5", "MAT-12 non relevé", "ORIENTATION", "R-46-3 — B-60"),
]
for z, c, v, p in AC:
    log("  %-18s %-36s %-22s %s" % (z, c, v, p))
log("")
log("  Points DE PRINCIPE : aucune capacité inventée ; aucune contrainte transmise")
log("  réduite ; f_k reste une hypothèse (D-34) ; aucun scellement calculé.")
log("  Points À LEVER : a1 réel (R-46-1) ; groupe des unités (R-46-2) ; épaisseurs")
log("  réelles et chaînages (R-46-3, PA-01) ; linteaux E-08 (R-46-4 → B-49).")

# ============================================================== JSON
res = {
    "mode": "PARTIEL-DÉCLARÉ",
    "fk_MPa": FK,
    "fd_MPa": FD,
    "gamma_M": GAMMA_M,
    "z1_voiles": voiles_res,
    "z2_appuis": appuis_res,
    "sensibilite_fk": sens,
    "z3_neufs": [{"ref": n, "N_kN": v, "sigma_MPa": round(v * 1000.0 / (SEMELLE ** 2), 3)}
                 for n, v in NEUFS],
    "ecarts": 3,
    "renvois": 2,
}

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
for nom, coul in (("MACON-AXES", 1), ("MACON-COFFRAGE", 5), ("MACON-ARMATURES", 3),
                  ("MACON-EXISTANT", 8), ("MACON-HABILLAGE-TEXTE", 7),
                  ("MACON-CARTOUCHE", 7)):
    doc.layers.add(nom, color=coul)


def txt(x, y, t, ht=2.4, layer="MACON-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))


def rect(x0, y0, x1, y1, layer="MACON-COFFRAGE"):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})


def ligne(x0, y0, x1, y1, layer="MACON-COFFRAGE"):
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})


rect(8, 8, 412, 289, "MACON-CARTOUCHE")
txt(14, 279, "CROISSY-FLORA — B-46 — MAÇONNERIE : VÉRIFICATION DES APPUIS", 3.8, "MACON-AXES")
txt(14, 272.5, "Indice A — 21/10/2026 — Mode PARTIEL-DÉCLARÉ (H-25/H-26, D-34)", 2.4, "MACON-AXES")
txt(14, 267, "Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée.", 2.3)

# --- D1 : coupe d'appui type sur sommier
txt(14, 257, "1. APPUI TYPE SUR SOMMIER S1/S2 — COUPE (EC6 §6.1.3)", 2.5, "MACON-AXES")
x0, y0 = 26, 214
rect(x0, y0, x0 + 10, y0 + 26, "MACON-EXISTANT")           # mur 50 cm (5 mm = 25 cm éch.)
rect(x0 + 2, y0 + 26, x0 + 8, y0 + 30, "MACON-COFFRAGE")   # sommier S2
rect(x0 + 3, y0 + 30, x0 + 7, y0 + 42, "MACON-COFFRAGE")   # poutre
for k in range(5):
    ligne(x0, y0 + 4 + k * 5, x0 + 10, y0 + 4 + k * 5, "MACON-EXISTANT")
ligne(x0 + 2, y0 + 25, x0 - 6, y0 + 8, "MACON-AXES")       # dispersion 60°
ligne(x0 + 8, y0 + 25, x0 + 16, y0 + 8, "MACON-AXES")
txt(x0 + 17, y0 + 20, "Sommier BA (S1 : 20x40x20 / S2 : 20x50x20)", 2.0, "MACON-AXES")
txt(x0 + 17, y0 + 15.5, "N_Rdc = beta · A_b · f_d — EC6 (6.10)", 2.0)
txt(x0 + 17, y0 + 11, "f_d = f_k/gamma_M = 0,60 MPa (H-25, D-34)", 2.0, "MACON-AXES")
txt(x0 + 17, y0 + 6.5, "Dispersion 60° vers mi-hauteur (fig. 6.2)", 2.0)
txt(x0 + 17, y0 + 2, "e <= t/4 — sommier CENTRÉ en épaisseur", 2.0, "MACON-AXES")
txt(x0 - 6, y0 - 6, "Appui mini 90 mm (EC6 §8.1.6) — w_b = 200 mm", 1.9)

# --- D2 : tableau des 8 appuis
txt(14, 196, "2. LES 8 APPUIS — B-45 Ind. A → B-46 (réponse à R-50-5)", 2.5, "MACON-AXES")
tx0, ty0 = 14, 118
rect(tx0, ty0, 250, 189, "MACON-CARTOUCHE")
cols = (tx0 + 2, tx0 + 30, tx0 + 52, tx0 + 86, tx0 + 110, tx0 + 134, tx0 + 158, tx0 + 186)
for c, t in zip(cols, ("APPUI", "V_Ed", "SOMMIER", "N(β=1)", "N(a1=0)", "N(a1=2)", "a1 crit", "VERDICT")):
    txt(c, 183, t, 1.9, "MACON-AXES")
for k, a in enumerate(appuis_res):
    y = 176 - k * 7.0
    ac = a["a1_crit_mm"]
    vals = (a["appui"], "%.1f kN" % a["V_kN"], a["sommier"], "%.1f" % a["N_beta1_kN"],
            "%.1f" % a["N_a1_0_kN"], "%.1f" % a["N_a1_2m_kN"],
            ("%.2f m" % (ac / 1000.0)) if ac is not None else ">5m", a["verdict"])
    colr = "MACON-AXES" if a["verdict"] != "OK" else "MACON-HABILLAGE-TEXTE"
    for c, v in zip(cols, vals):
        txt(c, y, v, 1.85, colr)
txt(tx0 + 2, 121, "N en kN — a1 = distance au bout de mur (NON RELEVÉE : R-46-1)", 1.9, "MACON-AXES")

# --- D3 : voiles Z1
txt(255, 257, "3. Z1 — VOILES RDC : COMPRESSION + FLAMBEMENT", 2.5, "MACON-AXES")
rect(255, 189, 405, 250, "MACON-CARTOUCHE")
txt(258, 243, "sigma_d max = 0,159 MPa (B-21 C) — f_d = 0,60 MPa", 2.0, "MACON-AXES")
txt(258, 238.5, "12 voiles RDC — t_eq 0,15 à 0,88 m (D5, B-25)", 2.0)
txt(258, 234, "lambda = h_ef/t = 3,4 à 20,0 ≤ 27 (EC6 §5.5)", 2.0)
txt(258, 229.5, "Phi_i = 1 - 2 e_init/t ≥ 0,911 (M05) — e_init = h/450", 2.0)
txt(258, 225, "Taux max = 0,290 (M05) — TOUT OK", 2.0, "MACON-AXES")
txt(258, 219, "Cisaillement : renvoi B-25 (tau/f_vk ≤ 0,043)", 2.0)
txt(258, 214.5, "f_vk = f_vk0 + 0,4 sigma_d = 0,178 MPa", 2.0)
txt(258, 210, "f_vd = 0,071 MPa (gamma_M = 2,5)", 2.0)
txt(258, 204, "Z3 — NEUFS SUR SOUBASSEMENT (semelle 60x60)", 2.0, "MACON-AXES")
txt(258, 199.5, "P1-N/S 100,3 kN — 0,279 MPa — taux 0,46 OK", 2.0)
txt(258, 195, "P3 35,8 · J1 39,8 — OK — sous fouille (D-19)", 2.0)

# --- D4 : sensibilité
txt(255, 178, "4. SENSIBILITÉ f_k — NON CONTRACTUELLE", 2.5, "MACON-AXES")
rect(255, 128, 405, 171, "MACON-CARTOUCHE")
txt(258, 164, "Taux = V/N_Rdc(a1=2 m) selon f_k (MPa)", 1.95, "MACON-AXES")
txt(258, 159.5, "APPUI    0,5    1,0    1,5    2,0", 1.9)
for k, (nom, vals) in enumerate(sens.items()):
    y = 155 - k * 3.6
    txt(258, y, "%-8s %5.2f %6.2f %6.2f %6.2f" % (nom, vals[0], vals[1], vals[2], vals[3]), 1.8)
txt(258, 122, "R1, F2, F3 > 1 si f_k ≤ 1,2 — D-34 gouverne", 1.95, "MACON-AXES")

# --- clause D-34 intégrale (majuscules) — exigence « sur les plans ET les notes »
rect(14, 58, 148, 112, "MACON-CARTOUCHE")
txt(18, 105, "CLAUSE D-34 — MAJUSCULES (OPPOSABLE)", 2.2, "MACON-AXES")
clause = [
    "NOS ÉTUDES SONT RÉALISÉES AVEC LES HYPOTHÈSES",
    "f_k = 1,5 MPa · E = 1 500 MPa · f_vk0 = 0,15 MPa.",
    "LA CONFIRMATION PAR ESSAIS EST HORS DE NOTRE",
    "MISSION ET À LA CHARGE DU MAÎTRE D'OUVRAGE.",
    "SI LES ESSAIS NE SONT PAS CONCLUANTS, LA REPRISE",
    "DE NOS ÉTUDES FAIT L'OBJET D'UNE PRESTATION",
    "COMPLÉMENTAIRE CHIFFRÉE (D-34, 20/10/2026).",
]
for k, t in enumerate(clause):
    txt(18, 98 - k * 5.2, t, 1.95, "MACON-AXES")

# --- notes opposables (2 colonnes sous D2)
n0 = 150
txt(n0, 112, "NOTES OPPOSABLES", 2.4, "MACON-AXES")
notes = [
    "1. f_k = 1,5 MPa : HYPOTHÈSE (D-34) à confirmer par essais, HORS mission.",
    "2. Essais non concluants => REPRISE D'ÉTUDE CHIFFRÉE (D-34).",
    "3. R1, F2, F3 : coussin de répartition si a1 < 0,25 m (orientation B-60).",
    "4. Sommiers S1 (x10) et S2 (x6) : CONSERVER — centrés en épaisseur (e ≤ t/4).",
    "5. AUCUN JOINT DE DILATATION (D-28).",
    "6. D-09 : ARASE -1,00 M / TN MINIMUM — ÉGALISATION GROS BÉTON SI ÉCART.",
    "7. Aucun scellement calculé ici (B-50). Aucune protection incendie dimensionnée.",
    "8. Sismique : AUCUNE VÉRIFICATION (D-26, zone de sismicité 1).",
]
for k, t in enumerate(notes):
    col, row = (0, k) if k < 4 else (1, k - 4)
    txt(n0 + col * 130, 106 - row * 5.0, t, 1.85)

# --- cartouche
rect(14, 10, 405, 55, "MACON-CARTOUCHE")
txt(18, 47, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 3.2, "MACON-AXES")
txt(18, 39, "B-46 — MAÇONNERIE : VÉRIFICATION ET CONCEPTION", 2.5)
txt(18, 32, "Brique B-46 · Indice A · 21/10/2026 · Mode PARTIEL-DÉCLARÉ · DXF mm · schémas sans échelle", 2.1)
txt(18, 25, "EC6 §5.5 / §6.1 / §6.2 / §8 · Hypothèses H-25 / H-26 (D-34) · CARNAC v3.0", 2.1)
txt(18, 14, "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 4.0, "MACON-AXES")

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

with open(os.path.join(OUT, "b46_maconnerie.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b46_maconnerie.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)

log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b46_maconnerie.txt"),
                             os.path.getsize(os.path.join(OUT, "b46_maconnerie.txt"))))
log("JSON    : %s (%d o)" % (os.path.join(OUT, "b46_maconnerie.json"),
                             os.path.getsize(os.path.join(OUT, "b46_maconnerie.json"))))
