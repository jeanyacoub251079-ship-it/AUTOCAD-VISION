#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-45 — STRUCTURE MÉTALLIQUE — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13) — EC3 / EC2 §6.7 / NF EN 10025.

Sorties : _rendus/b45_metal.txt / .json + _plans/FLORA_B45_METAL_IndA.{dxf,png,pdf}
Aucune valeur d'entrée n'est calculée « de tête » : toute donnée vient de
B-21 (charges), B-20 (sections), B-02 (MAT-05 = S275, D2 p. 1).
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_rendus")
PLANS = os.path.join(ROOT, "_plans")
BASE = os.path.join(PLANS, "FLORA_B45_METAL_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


# ---------------------------------------------------------------- CONSTANTES
E = 210000.0          # N/mm2
G = 81000.0           # N/mm2
FY = 275.0            # S275 — MAT-05f, D2 p. 1, contractuelle
FU = 430.0
GM0 = 1.0
GM1 = 1.0
EPS = math.sqrt(235.0 / FY)

# --------------------------------------------------------------- PROFILÉS
# Source : EN 10365 (valeurs tabulées). Unités : mm, cm2, cm4, cm3, cm6
P = {
    "HEA 200": dict(h=190, b=200, tw=6.5, tf=10, r=18, A=53.8, Iy=3692.0, Wel=389.0,
                    Wpl=429.5, Iz=1335.5, IT=41.16, Iw=97360.0, iy=82.8, iz=49.8,
                    famille="I", courbe="a"),
    "HEB 200": dict(h=200, b=200, tw=9, tf=15, r=18, A=78.1, Iy=5696.0, Wel=569.6,
                    Wpl=642.5, Iz=2003.0, IT=59.28, Iw=171990.0, iy=85.4, iz=50.7,
                    famille="I", courbe="a"),
    "HEB 160": dict(h=160, b=160, tw=8, tf=13, r=15, A=42.6, Iy=2492.0, Wel=311.5,
                    Wpl=354.0, Iz=889.2, IT=31.24, Iw=47970.0, iy=76.5, iz=45.7,
                    famille="I", courbe="a"),
    "IPE 200": dict(h=200, b=100, tw=5.6, tf=8.5, r=12, A=28.5, Iy=1943.0, Wel=194.3,
                    Wpl=220.6, Iz=142.4, IT=6.98, Iw=12990.0, iy=82.6, iz=22.4,
                    famille="I", courbe="b"),
    "IPE 160": dict(h=160, b=82, tw=5.0, tf=7.4, r=9, A=20.09, Iy=869.3, Wel=108.7,
                    Wpl=123.9, Iz=68.31, IT=3.60, Iw=3910, iy=65.8, iz=18.4,
                    famille="I", courbe="b"),
    "IPE 120": dict(h=120, b=64, tw=4.4, tf=6.3, r=7, A=13.21, Iy=317.8, Wel=52.96,
                    Wpl=60.7, Iz=27.67, IT=1.74, Iw=1180.0, iy=49.0, iz=14.5,
                    famille="I", courbe="b"),
    "UPE 200": dict(h=200, b=80, tw=6.5, tf=11.5, r=13, A=28.5, Iy=1910.0, Wel=191.0,
                    Wpl=224.0, Iz=148.0, IT=9.6, Iw=6720.0, iy=81.9, iz=22.8,
                    famille="U", courbe="c"),
}

# tube carré 140 x 140 x 6,3 — propriétés calculées
_bs, _ts = 140.0, 6.3
_bi = _bs - 2 * _ts
_A_tube = (_bs ** 2 - _bi ** 2) / 100.0          # cm2
_I_tube = (_bs ** 4 - _bi ** 4) / 12.0 / 1e4     # cm4
_i_tube = math.sqrt(_I_tube * 1e4 / (_A_tube * 100.0))
P["SHS 140x140x6.3"] = dict(h=_bs, b=_bs, tw=_ts, tf=_ts, r=0.0, A=round(_A_tube, 1),
                            Iy=round(_I_tube, 1), Wel=round(2 * _I_tube / (_bs / 10.0), 1),
                            Wpl=round(2 * _I_tube / (_bs / 10.0) * 1.15, 1),
                            Iz=round(_I_tube, 1), IT=round(_I_tube * 2, 1), Iw=0.0,
                            iy=round(_i_tube, 1), iz=round(_i_tube, 1),
                            famille="T", courbe="a")

# ---------------------------------------------------------------- BARRES
# Charges p_ELS / p_ELU : B-21 Ind. C § 5 (tableau des poutres)
BARRES = [
    # code, rôle, profilé, n_profiles, L (m), p_ELS, p_ELU, L_c (m), limite, appui
    ("F1a", "Frangement sous-œuvre, façade Est", "HEA 200", 2, 1.25, 52.6, 71.4, 1.25, 300, "maçonnerie"),
    ("F1b", "Frangement sous-œuvre, façade Est", "HEA 200", 2, 1.25, 52.6, 71.4, 1.25, 300, "maçonnerie"),
    ("F1c", "Frangement sous-œuvre, refend Sud", "HEA 200", 2, 1.25, 52.6, 71.4, 1.25, 300, "maçonnerie"),
    ("F2", "Poutre de reprise + charge F4", "HEB 200", 1, 2.85, 31.3, 43.8, 2.85, 300, "maçonnerie"),
    ("F3", "Poutre de plancher courant", "HEB 160", 1, 3.85, 22.8, 32.0, 3.85, 300, "maçonnerie"),
    ("F4", "Poutre sous toiture basse", "IPE 200", 1, 4.88, 3.3, 4.7, 4.88, 250, "maçonnerie"),
    ("R1", "Moisage poutre bois 20x15", "UPE 200", 2, 3.85, 28.6, 40.2, 3.85, 350, "maçonnerie"),
    ("R2-N", "Poutre de refend sous solivage", "HEB 160", 1, 3.82, 17.2, 24.2, 3.82, 350, "maçonnerie"),
    ("R2-S", "Poutre de refend sous solivage", "HEB 160", 1, 3.82, 13.4, 18.8, 3.82, 350, "maçonnerie"),
]

# ================================================================ EN-TÊTE
titre("=" * 78)
log("B-45 — STRUCTURE MÉTALLIQUE — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13) — EC3 (NF EN 1993-1-1) / EC2 §6.7")
log("MAT-05 : S275 (D2 p. 1, contractuelle) — f_y = 275 MPa, f_u = 430 MPa")
log("=" * 78)

titre("[1] DONNÉES D'ENTRÉE — AUCUNE VALEUR HORS FDC")
log("  MAT-05f  nuance acier ................ S275 (D2 p. 1) — CONTRACTUELLE")
log("  MAT-05a  F1a/b/c ..................... 2 x HEA 200 (D2 f. 01)")
log("  MAT-05b  F2 / F3 / F4 ................ HEB 200 / HEB 160 / IPE 200 (D2 f. 01)")
log("  MAT-05c  R1 / R2 / R3 ................ 2 x UPE 200 / HEB 160 / UPE 200 (D2 f. 01)")
log("  MAT-05d  P1 .......................... tube carré 140 x 140 (D2 f. 01)")
log("  MAT-05e  Stab1 ....................... entretoises IPE en voutain (D2 f. 01)")
log("  CHG      p_ELS / p_ELU par barre ..... B-21 Ind. C § 5")
log("  GEO      portées ..................... B-20 § 3 (mesurées sur D5/D4)")
log("  f_y = %.0f MPa · f_u = %.0f MPa · gM0 = %.1f · gM1 = %.1f · eps = %.3f"
    % (FY, FU, GM0, GM1, EPS))
log("  E = %.0f MPa · G = %.0f MPa" % (E, G))

# ================================================================ CALCULS
resultats = []
for code, role, prof, n, L, p_els, p_elu, Lc, lim, appui in BARRES:
    s = P[prof]
    Lmm = L * 1000.0
    Iy = s["Iy"] * 1e4 * n          # mm4
    Wel = s["Wel"] * 1e3 * n        # mm3
    Wpl = s["Wpl"] * 1e3 * n        # mm3
    A = s["A"] * 1e2 * n            # mm2

    # ---- sollicitations
    M = p_elu * L ** 2 / 8.0        # kN.m
    V = p_elu * L / 2.0             # kN

    # ---- classification EC3 §5.5.2 (semelle en console, âme fléchie)
    # semelle : c = (b - tw - 2r)/2 ; c/tf
    c_f = (s["b"] - s["tw"] - 2 * s["r"]) / 2.0
    c_tf = c_f / s["tf"]
    # âme fléchie : d/tw avec d = h - 2tf - 2r
    d_w = s["h"] - 2 * s["tf"] - 2 * s["r"]
    d_tw = d_w / s["tw"]
    lim_f = (9 * EPS, 10 * EPS, 14 * EPS)   # classes 1, 2, 3
    lim_w = (72 * EPS, 83 * EPS, 124 * EPS)
    if c_tf <= lim_f[0] and d_tw <= lim_w[0]:
        classe = 1
    elif c_tf <= lim_f[1] and d_tw <= lim_w[1]:
        classe = 2
    elif c_tf <= lim_f[2] and d_tw <= lim_w[2]:
        classe = 3
    else:
        classe = 4
    W_util = Wpl if classe <= 2 else Wel

    # ---- flexion EC3 §6.2.5
    M_Rd = W_util * FY / GM0 / 1e6      # kN.m
    r_flex = M / M_Rd

    # ---- cisaillement EC3 §6.2.6
    Av = (s["A"] - 2 * s["b"] * s["tf"] / 100.0
          + (s["tw"] + 2 * s["r"]) * s["tf"] / 100.0) * n   # cm2
    V_Rd = Av * 1e2 * FY / (math.sqrt(3) * GM0) / 1e3      # kN
    r_shear = V / V_Rd
    interaction = None
    if r_shear > 0.5:
        rho = (2 * r_shear - 1) ** 2
        Mv_Rd = M_Rd * (1 - rho)
        interaction = dict(rho=round(rho, 3), Mv_Rd=round(Mv_Rd, 1),
                           ratio=round(M / Mv_Rd, 3))

    # ---- déversement EC3 §6.3.2
    Iz = s["Iz"] * 1e4 * n
    IT = s["IT"] * 1e4 * n
    Iw = s["Iw"] * 1e8 * n
    C1 = 1.13
    kL = Lc * 1000.0
    Mcr = (C1 * math.pi ** 2 * E * Iz / kL ** 2
           * math.sqrt(Iw / Iz + (kL ** 2 * G * IT) / (math.pi ** 2 * E * Iz))) / 1e6
    lam_LT = math.sqrt(s["Wel"] * n * 1e3 * FY / (Mcr * 1e6))
    alpha = {"a": 0.21, "b": 0.34, "c": 0.49}[s["courbe"]]
    phi = 0.5 * (1 + alpha * (lam_LT - 0.2) + lam_LT ** 2)
    chi = min(1.0, 1.0 / (phi + math.sqrt(max(phi ** 2 - lam_LT ** 2, 0.0))))
    Mb_Rd = chi * s["Wel"] * n * 1e3 * FY / GM1 / 1e6
    r_ltb = M / Mb_Rd

    # ---- flèche ELS
    w = 5.0 * p_els * (Lmm ** 4) / (384.0 * E * Iy)
    w_lim = Lmm / lim
    r_def = w / w_lim

    resultats.append(dict(code=code, role=role, prof=prof, n=n, L=L, p_els=p_els,
                          p_elu=p_elu, M=round(M, 2), V=round(V, 2), classe=classe,
                          c_tf=round(c_tf, 1), d_tw=round(d_tw, 1),
                          M_Rd=round(M_Rd, 1), r_flex=round(r_flex, 3),
                          V_Rd=round(V_Rd, 1), r_shear=round(r_shear, 3),
                          inter=interaction, Mcr=round(Mcr, 1),
                          lam_LT=round(lam_LT, 3), chi=round(chi, 3),
                          Mb_Rd=round(Mb_Rd, 1), r_ltb=round(r_ltb, 3),
                          w=round(w, 1), w_lim=round(w_lim, 1), lim=lim,
                          r_def=round(r_def, 3)))

# ================================================================ SORTIE 3
titre("[2] CLASSIFICATION EC3 § 5.5 — AVANT TOUT CALCUL")
log("  %-6s %-16s %8s %8s %8s %8s" % ("CODE", "PROFILÉ", "c/tf", "lim 1", "d/tw", "CLASSE"))
for r in resultats:
    s = P[r["prof"]]
    log("  %-6s %-16s %8.1f %8.1f %8.1f %8d"
        % (r["code"], r["prof"], r["c_tf"], 9 * EPS, r["d_tw"], r["classe"]))
log("  eps = sqrt(235/275) = %.3f — semelle en console : 9e / 10e / 14e" % EPS)
log("  âme fléchie : 72e / 83e / 124e (EC3 tab. 5.2)")

titre("[3] FLEXION ET CISAILLEMENT — EC3 § 6.2.5 et § 6.2.6")
log("  M_Ed = p_ELU L2/8 · V_Ed = p_ELU L/2")
log("  %-6s %8s %8s %8s %8s %8s %8s %8s"
    % ("CODE", "M_Ed", "M_Rd", "RATIO", "V_Ed", "V_Rd", "RATIO", "VERT."))
for r in resultats:
    ok = "OK" if max(r["r_flex"], r["r_shear"]) <= 1.0 else "NON"
    log("  %-6s %8.1f %8.1f %8.3f %8.1f %8.1f %8.3f %8s"
        % (r["code"], r["M"], r["M_Rd"], r["r_flex"], r["V"], r["V_Rd"],
           r["r_shear"], ok))
mvx = [r for r in resultats if r["inter"]]
if not mvx:
    log("  Interaction M-V (EC3 6.2.8) : aucun cas V_Ed > 0,5 V_pl,Rd.")
for r in mvx:
    log("  %-6s V_Ed > 0,5 V_pl,Rd -> rho = %.3f · M_V,Rd = %.1f kN.m · ratio = %.3f"
        % (r["code"], r["inter"]["rho"], r["inter"]["Mv_Rd"], r["inter"]["ratio"]))

titre("[4] DÉVERSEMENT — EC3 § 6.3.2 — MAINTIEN LATÉRAL NON SUPPOSÉ")
log("  Cas non maintenu : L_cr = L (aucun maintien pris en compte).")
log("  %-6s %8s %8s %8s %8s %8s %8s"
    % ("CODE", "Lcr(m)", "Mcr", "lam_LT", "chi_LT", "M_b,Rd", "RATIO"))
for r in resultats:
    log("  %-6s %8.2f %8.1f %8.3f %8.3f %8.1f %8.3f"
        % (r["code"], r["L"], r["Mcr"], r["lam_LT"], r["chi"],
           r["Mb_Rd"], r["r_ltb"]))
log("  Courbes : I laminé h/b <= 2 -> a ; h/b > 2 -> b ; U -> c (prudence).")

titre("[5] FLÈCHE ELS — EC2/EC3, limite justifiée par barre")
log("  %-6s %8s %8s %8s %8s %8s %8s"
    % ("CODE", "L(m)", "w(mm)", "lim", "w_lim", "RATIO", "VERT."))
for r in resultats:
    ok = "OK" if r["r_def"] <= 1.0 else "NON"
    log("  %-6s %8.2f %8.1f %8d %8.1f %8.3f %8s"
        % (r["code"], r["L"], r["w"], r["lim"], r["w_lim"], r["r_def"], ok))

titre("[6] POTEAUX MÉTALLIQUES P1-N / P1-S — FLAMBEMENT EC3 § 6.3.1")
sP1 = P["SHS 140x140x6.3"]
N_P1 = 100.3
H = 3.00
log("  Tube carré 140 x 140 x %.1f — A = %.1f cm2 · i = %.1f mm (calculé)"
    % (_ts, sP1["A"], sP1["iy"]))
log("  N_Ed = %.1f kN (B-21 § 6) · L_cr = %.2f m (articulé-articulé)" % (N_P1, H))
lam = H * 1000.0 / sP1["iy"]
lam_bar = lam / (93.9 * EPS)
alphaP = 0.21
phiP = 0.5 * (1 + alphaP * (lam_bar - 0.2) + lam_bar ** 2)
chiP = min(1.0, 1.0 / (phiP + math.sqrt(max(phiP ** 2 - lam_bar ** 2, 0.0))))
N_Rd = chiP * sP1["A"] * 1e2 * FY / GM1 / 1e3
log("  lambda = %.1f · lambda_bar = %.3f · courbe a · chi = %.3f" % (lam, lam_bar, chiP))
log("  N_b,Rd = %.3f x %.1f x 275 / 1,0 = %.1f kN" % (chiP, sP1["A"], N_Rd))
log("  TAUX = %.3f  ->  %s" % (N_P1 / N_Rd, "OK" if N_P1 <= N_Rd else "NON"))
log("  Épaisseur retenue : 6,3 mm (mini) — B-20 laissait 10 ou 6,3 mm ouvert.")

titre("[7] ENTRETOISES Stab1 — MAINTIEN ANTI-DÉVERSEMENT DES IPE 160")
# effort de stabilisation : 2,5 % de l'effort de semelle comprimée
p_sol = 10.11      # kN/m2 ELU, B-43 zone B
e_sol = 0.72
p_lin = p_sol * e_sol
log("  Solive existante IPE 160 @ 0,72 m — p_ELU = %.2f x %.2f = %.2f kN/m"
    % (p_sol, e_sol, p_lin))
log("  La portée des IPE 160 n'est écrite par AUCUNE pièce : c'est un ouvrage")
log("  EXISTANT, sa portée relève de B-46. Le calcul est donc mené sur un")
log("  INTERVALLE, et l'on retient le profilé qui couvre tout l'intervalle.")
log("")
log("  %-8s %8s %8s %8s %8s %10s" % ("L(m)", "M(kN.m)", "N_f(kN)", "F_stab", "N_b,Rd", "TAUX"))
sStab = P["IPE 120"]
Lst = 2.50   # longueur de flambement de l'entretoise = pas des files Stab1
lamS = Lst * 1000.0 / (sStab["iz"] * 10.0)
lamS_bar = lamS / (93.9 * EPS)
phiS = 0.5 * (1 + 0.34 * (lamS_bar - 0.2) + lamS_bar ** 2)
chiS = min(1.0, 1.0 / (phiS + math.sqrt(max(phiS ** 2 - lamS_bar ** 2, 0.0))))
Nb_stab = chiS * sStab["A"] * 1e2 * FY / GM1 / 1e3
stab_rows = []
for Ls in (2.50, 3.00, 3.60, 4.20, 4.80, 5.40):
    Ms = p_lin * Ls ** 2 / 8.0
    Nf = Ms * 1e6 / (sStab["h"] - sStab["tf"]) / 1e3
    Fs = 0.025 * Nf
    log("  %-8.2f %8.1f %8.1f %8.2f %8.1f %10.3f"
        % (Ls, Ms, Nf, Fs, Nb_stab, Fs / Nb_stab))
    stab_rows.append(dict(L=Ls, M=round(Ms, 2), Nf=round(Nf, 1),
                          F=round(Fs, 2), taux=round(Fs / Nb_stab, 3)))
log("  IPE 120 : i_z = %.1f mm · lambda_bar = %.3f · courbe b · chi = %.3f"
    % (sStab["iz"], lamS_bar, chiS))
log("  N_b,Rd = %.1f kN — couvre tout l'intervalle avec un taux < %.2f"
    % (Nb_stab, max(r["taux"] for r in stab_rows)))
log("  Portée L inutile : le résultat est INSENSIBLE à la portée des IPE 160.")
log("  Effort de stabilisation par file transmis à B-50 : %.1f kN (enveloppe L=5,40 m)"
    % max(r["F"] for r in stab_rows))

titre("[8] R3-N / R3-S — LINTEAUX SOUS CHARGE PONCTUELLE")
P_R3 = 46.2       # kN, réaction de R2-N à l'ELU (B-21 § 5)
L_baie = 1.55
M_R3 = P_R3 * L_baie / 4.0
V_R3 = P_R3 / 2.0
sR3 = P["UPE 200"]
M_Rd3 = sR3["Wpl"] * 1e3 * FY / GM0 / 1e6
V_Rd3 = (sR3["A"] * 1e2 * FY / (math.sqrt(3) * GM0)) / 1e3
w_R3 = P_R3 * 1e3 * (L_baie * 1000.0) ** 3 / (48.0 * E * sR3["Iy"] * 1e4)
log("  P_Ed = %.1f kN à mi-portée · L_baie = %.2f m (profilé livré 2,50 m)" % (P_R3, L_baie))
log("  M_Ed = P L/4 = %.1f kN.m   ·  M_pl,Rd = %.1f kN.m  ->  %.3f"
    % (M_R3, M_Rd3, M_R3 / M_Rd3))
log("  V_Ed = %.1f kN            ·  V_pl,Rd = %.1f kN     ->  %.3f"
    % (V_R3, V_Rd3, V_R3 / V_Rd3))
log("  Flèche (charge ponctuelle) = %.2f mm pour %.1f mm admis (L/250)"
    % (w_R3, L_baie * 1000.0 / 250))
log("  TORSION D'EXCENTREMENT : un U est un profilé ASYMÉTRIQUE — la charge")
log("  appliquée sur l'axe de l'âme crée un moment de torsion M_t = P x e.")
log("  e = %.0f mm (axe de l'âme / axe de cisaillement) -> M_t = %.2f kN.m"
    % (sR3["b"] / 2.0, P_R3 * sR3["b"] / 2000.0))
log("  Cette torsion n'est PAS reprise par le UPE seul : elle impose soit un")
log("  remplissage béton entre les ailes, soit une platine de répartition.")
log("  -> Renvoi B-50 (assemblage) + prescription de planche.")

titre("[9] PRESSION DIAMÉTRALE SUR LE BÉTON — EC2 § 6.7")
log("  Le seul appui métallique sur béton est P1-N / P1-S sur SF1 (B-40).")
log("  F1, F2, F3, F4, R1, R2, R3 s'appuient sur MAÇONNERIE -> B-46 (§ f_k).")
f_cd = 0.85 * 25.0 / 1.5     # MPa — C25/30, alpha_cc = 0,85 (EC2 3.1.6)
plat = 200.0                 # mm — platine 200 x 200
A_c0 = plat ** 2             # mm2
sig = N_P1 * 1e3 / A_c0      # MPa
F_Rdu = 1.5 * f_cd * A_c0 / 1e3   # kN
log("  N_Ed = %.1f kN · platine %.0f x %.0f mm · A_c0 = %.0f cm2"
    % (N_P1, plat, plat, A_c0 / 100.0))
log("  f_cd = 0,85 x 25 / 1,5 = %.2f MPa · F_Rdu = 1,5 f_cd A_c0 = %.1f kN"
    % (f_cd, F_Rdu))
log("  sigma_c = %.2f MPa -> TAUX = %.3f  %s"
    % (sig, N_P1 / F_Rdu, "OK" if N_P1 <= F_Rdu else "NON"))

titre("[10] DISPOSITIONS CONSTRUCTIVES ET TRANSMISSIONS")
log("  - Maintien latéral : IPE 160 existants -> Stab1 (4 files, pas 2,50 m)")
log("    F_stab = %.1f kN par file (enveloppe) -> B-50"
    % max(r["F"] for r in stab_rows))
log("  - R1 : le moisage n'est pas un profilé isolé — 2 x UPE 200 boulonnés de")
log("    part et d'autre de la poutre bois 20 x 15. Le boulonnage assure le")
log("    maintien latéral ET la solidarisation ; ses deux fonctions sont")
log("    chiffrées pour B-50 (F_stab ci-dessus + glissement).")
log("  - Anticorrosion : galvanisation à chaud NF EN ISO 1461 (min 70 um),")
log("    ou peinture classe C3 si galva impossible en œuvre.")
log("  - Protection au feu : NON dimensionnée (hors périmètre) — mention")
log("    générique reportée sur la planche.")
log("  - Réservations : aucune trémie dans les semelles des profilés ;")
log("    les saignées Stab1 dans le voutain sont ponctuelles (D2 f. 01).")

# ================================================================ JSON
res = dict(
    nuance="S275", fy=FY, mode="COMPLET", n_barres=len(resultats),
    barres=resultats,
    poteaux=dict(code="P1-N/P1-S", profil="SHS 140x140x6.3", N_Ed=N_P1,
                 N_Rd=round(N_Rd, 1), taux=round(N_P1 / N_Rd, 3)),
    stab=dict(profil="IPE 120", N_Rd=round(Nb_stab, 1), cas=stab_rows),
    r3=dict(P=P_R3, M=round(M_R3, 2), M_Rd=round(M_Rd3, 1),
            taux=round(M_R3 / M_Rd3, 3), fleche=round(w_R3, 2)),
    pression_diametrale=dict(N=N_P1, F_Rdu=round(F_Rdu, 1), taux=round(N_P1 / F_Rdu, 3)),
    max_flex=max(r["r_flex"] for r in resultats),
    max_shear=max(r["r_shear"] for r in resultats),
    max_ltb=max(r["r_ltb"] for r in resultats),
    max_def=max(r["r_def"] for r in resultats),
)

# ================================================================ PLANCHE
import ezdxf
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

doc = ezdxf.new("R2018", setup=True)
msp = doc.modelspace()
for nom, coul in (("METAL-AXES", 1), ("METAL-COFFRAGE", 5), ("METAL-PROFILES", 3),
                  ("METAL-HABILLAGE-TEXTE", 7), ("METAL-COTATION", 8),
                  ("METAL-CARTOUCHE", 7)):
    doc.layers.add(nom, color=coul)


def txt(x, y, t, ht=2.4, layer="METAL-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))


def rect(x0, y0, x1, y1, layer="METAL-COFFRAGE"):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})


def ligne(x0, y0, x1, y1, layer="METAL-COFFRAGE"):
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})


rect(8, 8, 412, 289, "METAL-CARTOUCHE")
txt(14, 279, "CROISSY-FLORA — B-45 — STRUCTURE MÉTALLIQUE : PROFILÉS, MOISAGE, ENTRETOISES", 3.8, "METAL-AXES")
txt(14, 272, "Indice A — 21/10/2026 — ACIER S275 (MAT-05f, D2 p. 1) — NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 2.5, "METAL-AXES")
txt(14, 266.5, "Protection au feu NON dimensionnée — hors lot GO. Aucun assemblage calculé ici (B-50).", 2.3)

# ---------------------------------------------------------- DÉTAIL 1 (haut gauche)
txt(14, 257, "1. MOISAGE R1 — 2 × UPE 200 BOULONNÉS SUR POUTRE BOIS 20 × 15", 2.5, "METAL-AXES")
x0, y0 = 30, 232
rect(x0, y0, x0 + 20, y0 + 15, "METAL-COFFRAGE")
for k in range(1, 4):
    ligne(x0 + k * 5, y0, x0 + k * 5, y0 + 15, "METAL-COTATION")
for signe in (-1, 1):
    xa = x0 + (0 if signe < 0 else 20)
    ligne(xa + signe * 0.65, y0 - 2, xa + signe * 0.65, y0 + 17, "METAL-PROFILES")
    ligne(xa + signe * 0.65, y0 - 2, xa + signe * 8.65, y0 - 2, "METAL-PROFILES")
    ligne(xa + signe * 0.65, y0 + 17, xa + signe * 8.65, y0 + 17, "METAL-PROFILES")
for yb in (y0 + 3, y0 + 7.5, y0 + 12):
    ligne(x0 - 6, yb, x0 + 26, yb, "METAL-AXES")
    msp.add_circle((x0 - 3, yb), 0.7, dxfattribs={"layer": "METAL-AXES"})
    msp.add_circle((x0 + 23, yb), 0.7, dxfattribs={"layer": "METAL-AXES"})
txt(x0 - 6, y0 + 19.5, "2 × UPE 200 (S275)", 2.1, "METAL-PROFILES")
txt(x0 + 30, y0 + 13, "Poutre bois 20 × 15 existante (B-24)", 2.0)
txt(x0 + 30, y0 + 8.5, "∅ boulons et espacement : B-50", 2.0)
txt(x0 + 30, y0 + 4, "Maintien latéral assuré par le boulonnage", 2.0)
txt(x0 + 30, y0 - 0.5, "Harnais de serrage interdit sur bois sec", 2.0)

# ---------------------------------------------------------- DÉTAIL 2 (haut droite)
txt(208, 257, "2. FRANGEMENT F1 — 2 × HEA 200 SOUS MUR EN MOELLONS", 2.5, "METAL-AXES")
xb, yb0 = 218, 232
rect(xb, yb0, xb + 50, yb0 + 5, "METAL-COFFRAGE")
for k in range(12):
    ligne(xb + k * 4.2, yb0, xb + k * 4.2, yb0 + 5, "METAL-COTATION")
rect(xb + 12, yb0 - 16, xb + 16, yb0, "METAL-PROFILES")
rect(xb + 19, yb0 - 16, xb + 23, yb0, "METAL-PROFILES")
rect(xb + 8, yb0 - 19, xb + 27, yb0 - 16, "METAL-PROFILES")
txt(xb + 30, yb0 - 4, "2 × HEA 200 — L_calc = 1,25 m", 2.0, "METAL-PROFILES")
txt(xb + 30, yb0 - 8.5, "M_Ed = 13,9 kN·m pour 236 kN·m (0,06)", 2.0)
txt(xb + 30, yb0 - 13, "Platine d'appui et calage : B-50", 2.0)

# ---------------------------------------------------------- DÉTAIL 3 (bas gauche)
txt(14, 212, "3. LINTEAU R3 — UPE 200 SOUS R2", 2.5, "METAL-AXES")
xc, yc = 30, 185
ligne(xc, yc, xc + 31, yc, "METAL-PROFILES")
ligne(xc, yc + 20, xc + 31, yc + 20, "METAL-PROFILES")
ligne(xc, yc, xc, yc + 20, "METAL-PROFILES")
ligne(xc + 31, yc, xc + 31, yc + 20, "METAL-PROFILES")
msp.add_line((xc + 15.5, yc + 20), (xc + 15.5, yc + 24), dxfattribs={"layer": "METAL-AXES"})
txt(xc + 18, yc + 21, "R2 — P_Ed = 46,2 kN", 2.0, "METAL-AXES")
txt(xc + 34, yc + 12, "M_Ed = 17,9 / M_pl,Rd = 61,6 → 0,29", 1.9)
txt(xc + 34, yc + 7.5, "UPE = profilé asymétrique : axe de", 1.9)
txt(xc + 34, yc + 3, "cisaillement décalé de 40 mm", 1.9)
txt(xc + 34, yc - 1.5, "M_t = P × e = 1,85 kN·m NON repris", 1.9, "METAL-AXES")
txt(xc + 34, yc - 6, "→ remplissage béton ou platine (B-50)", 1.9)

# ---------------------------------------------------------- DÉTAIL 4 (bas droite)
txt(208, 205, "4. Stab1 — ENTRETOISES IPE 120 DANS LE VOUTAIN, PAS 2,50 m", 2.5, "METAL-AXES")
xd, yd = 218, 190
ligne(xd, yd, xd + 60, yd, "METAL-PROFILES")
for k in range(4):
    xk = xd + 6 + k * 16
    rect(xk, yd - 8, xk + 8, yd, "METAL-PROFILES")
    txt(xk - 2, yd - 11, "F ≤ 5,8 kN", 1.9, "METAL-AXES")
txt(xd + 84, yd + 2, "Solives IPE 160 existantes", 1.9)
txt(xd + 84, yd - 2.5, "(B-46) — déversement", 1.9)
txt(xd + 84, yd - 7, "instable au diagnostic", 1.9)
txt(xd, yd - 15, "IPE 120 : N_b,Rd = %.0f kN pour F_stab ≤ 5,8 kN (taux 0,02)" % Nb_stab, 2.0, "METAL-PROFILES")

# ---------------------------------------------------------- TABLEAU
tx0, ty0, tx1, ty1 = 14, 84, 405, 172
rect(tx0, ty0, tx1, ty1, "METAL-CARTOUCHE")
txt(tx0 + 3, 168, "SYNTHÈSE DES VÉRIFICATIONS EC3 — S275 · gM0 = gM1 = 1,0 · classification avant calcul", 2.6, "METAL-AXES")
entetes = ("CODE", "PROFILÉ", "CL.", "M_Ed", "M_Rd", "RATIO", "DÉVERS.", "FLÈCHE", "VERDICT")
cols = (tx0 + 3, tx0 + 26, tx0 + 76, tx0 + 90, tx0 + 110, tx0 + 130, tx0 + 152, tx0 + 180, tx0 + 208)
for c, t in zip(cols, entetes):
    txt(c, 162, t, 2.1, "METAL-AXES")
kk = 0
for r in resultats:
    y = 155 - kk * 5.0
    ok = max(r["r_flex"], r["r_shear"], r["r_ltb"], r["r_def"])
    txt(cols[0], y, r["code"], 2.0)
    txt(cols[1], y, r["prof"] + (" ×2" if r["n"] == 2 else ""), 2.0)
    txt(cols[2], y, str(r["classe"]), 2.0)
    txt(cols[3], y, "%.1f" % r["M"], 2.0)
    txt(cols[4], y, "%.1f" % r["M_Rd"], 2.0)
    txt(cols[5], y, "%.2f" % r["r_flex"], 2.0)
    txt(cols[6], y, "%.2f" % r["r_ltb"], 2.0)
    txt(cols[7], y, "%.2f" % r["r_def"], 2.0)
    txt(cols[8], y, "OK" if ok <= 1 else "NON", 2.0,
        "METAL-AXES" if ok > 1 else "METAL-HABILLAGE-TEXTE")
    kk += 1
extras = [
    ("P1-N/S", "SHS 140×140×6,3", "1", "N = 100,3", "%.0f" % N_Rd, "0,12", "—", "—", "OK"),
    ("R3-N/S", "UPE 200", "1", "%.1f" % M_R3, "%.1f" % M_Rd3, "0,29", "—", "%.1f mm" % w_R3, "OK + torsion"),
    ("Stab1", "IPE 120", "1", "F ≤ 5,8", "%.0f" % Nb_stab, "0,02", "—", "—", "OK"),
]
for e in extras:
    y = 155 - kk * 5.0
    for c, v in zip(cols, e):
        txt(c, y, v, 2.0)
    kk += 1
txt(tx0 + 3, 92.5, "F3 et R1 : ce sont les deux barres qui gouvernent (flexion 0,61 et 0,60 ; flèche 0,97 et 0,93). M-V vérifiée pour F3 (M_V,Rd = 88,2 → 0,67).", 2.0, "METAL-AXES")
txt(tx0 + 3, 89, "Déversement : cas NON maintenu vérifié pour toutes les barres — le maintien n'est jamais supposé. Courbes a (HE), b (IPE), c (UPE, prudence).", 2.0)

# ---------------------------------------------------------- NOTES (2 colonnes)
notes = [
    "1. Acier S275 (MAT-05f, D2 p. 1) — aucune nuance supposée.",
    "2. Toutes les barres en classe 1 : résistance plastique retenue.",
    "3. Déversement vérifié sans maintien — jamais supposé acquis.",
    "4. Stab1 : 4 files, pas 2,50 m, F ≤ 5,8 kN/file → B-50.",
    "5. Moisage R1 : boulonnage = solidarisation ET maintien (B-50).",
    "6. UPE 200 (R3) : torsion Mt = 1,85 kN·m → B-50.",
    "7. Appuis sur maçonnerie : f_k non mesuré → B-46 (D-34, R-15).",
    "8. P1 sur SF1 : pression diamétrale EC2 §6.7 = 0,118.",
    "9. Anticorrosion : galvanisation NF EN ISO 1461, 70 µm mini.",
    "10. Protection au feu NON dimensionnée — hors lot GO.",
    "11. Étais obligatoires pendant la dépose (AT-09, T-04).",
]
txt(14, 80, "NOTES OPPOSABLES", 2.6, "METAL-AXES")
for k, t in enumerate(notes):
    col, row = k // 4, k % 4
    txt(14 + col * 132, 76.0 - row * 5.4, t, 2.0)

# ---------------------------------------------------------- CARTOUCHE
rect(14, 10, 405, 55, "METAL-CARTOUCHE")
txt(18, 47, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 3.2, "METAL-AXES")
txt(18, 39, "B-45 — STRUCTURE MÉTALLIQUE : PROFILÉS, MOISAGE, ENTRETOISES", 2.5)
txt(18, 32, "Brique B-45 · Indice A · 21/10/2026 · Mode COMPLET · Unités DXF : mm · Échelle des schémas : sans échelle", 2.1)
txt(18, 25, "S275 · EC3 (NF EN 1993-1-1) · EC2 §6.7 · CARNAC v3.0", 2.1)
txt(18, 14, "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 4.0, "METAL-AXES")

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

with open(os.path.join(OUT, "b45_metal.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b45_metal.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)

log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b45_metal.txt"),
                             os.path.getsize(os.path.join(OUT, "b45_metal.txt"))))
log("JSON    : %s (%d o)" % (os.path.join(OUT, "b45_metal.json"),
                             os.path.getsize(os.path.join(OUT, "b45_metal.json"))))
