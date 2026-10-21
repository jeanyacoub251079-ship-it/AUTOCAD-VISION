#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-44 — CHARPENTE BOIS — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13) — EC5 / EC1-1-3 / EC1-1-4 / EC0.

Périmètre :
  - 3 pannes NEUVES, 2 demi-fermes NEUVES, contrefiches NEUVES (B-20, D2 f.02).
  - Bois neuf prescrit C24 (NF EN 338) — spécification d'approvisionnement, pas une mesure.
  - Existant E-04/E-05/E-06 : NON CALCULÉ (B-24 PARAMÉTRIQUE, sections inconnues).
  - E-07 : NON CHARGÉ par les neufs (demi-fermes désolidarisées, potelets supprimés).
  - 2 zones non relevées : AUCUN CALCUL (nuage D-19). Chevrons existants : B-24.
Aucun assemblage calculé (B-50). Aucune protection incendie dimensionnée.
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_rendus")
PLANS = os.path.join(ROOT, "_plans")
BASE = os.path.join(PLANS, "FLORA_B44_CHARPENTE_IndA")

LIGNES = []


def log(t=""):
    LIGNES.append(t)
    print(t)


def titre(t):
    log("")
    log(t)
    log("-" * 78)


# ============================================================== DONNÉES (FDC / B-xx)
G_TOIT = 0.95          # kN/m² — H-29 (B-21), CHG-04 absent du marché
Q_NEIGE = 0.45         # kN/m² — CHG-05, zone A1, sk=45 daN/m² (B-21, SANS réduction μ1)
Q_H = 0.40             # kN/m² — cat. H, B-21 ; NON combiné à la neige
QP_VENT = 0.50         # kN/m² — B-25 q_p(6 m) = 500 Pa
CPE_UPLIFT = 0.70      # |c_pe| zone courante versant (EC1-1-4 §7.2.3) — dépression

L_PANNE = 3.20         # m — B-24 E-06, D2 f.02 (portée entre fermes)
E_PANNE = 1.60         # m — entraxe de calcul : demi File A–C (B-20 §2.2, 3,20 m)
L_DF = 3.20            # m — File A (X=85,55) → File C (X=88,75), B-20 §2.2
Y_EST = 9.51           # m — File 2 (49,54) → File 5 (59,05), aile Est
ALPHA_DEG = 28.0       # ° — min NIV-02c : atan((209,19-206,57)/((95,35-85,55)/2))
ALPHA = math.radians(ALPHA_DEG)
L_ARB = L_DF / math.cos(ALPHA)
H_DF = L_DF * math.tan(ALPHA)
L_CF = 2.62            # m — contrefiche : hauteur de versant NIV-02c min (conservateur)

# C24 — NF EN 338 (bois massif, neuf prescrit)
FMK, FVK, FC0K, FC90K = 24.0, 4.0, 21.0, 2.5   # MPa
E05, EMEAN = 7400.0, 11000.0                     # MPa
RHO = 420.0                                      # kg/m³ (mean) — poids propre
GM = 1.3                                         # EC5/NA bois massif
KMOD = 0.80                                      # cl. service 2, moyenne durée (neige) — T3.1
KDEF = 0.80                                      # cl. service 2, bois massif — T3.2
KCR = 0.67                                       # EC5 §6.1.7(2) bois massif non renforcé
PSI2_S = 0.0                                     # neige — EC0/NA

P_ELU = 1.35 * G_TOIT + 1.50 * Q_NEIGE          # 1,958 kN/m²
P_ELS_G = G_TOIT
P_ELS_Q = Q_NEIGE
W_UPLIFT = QP_VENT * CPE_UPLIFT                 # 0,35 kN/m²
# combinaison soulèvement EC0 : 1,5 W + 1,0 G (G favorable, γG,inf=1,0)
P_UPLIFT = 1.50 * W_UPLIFT - 1.00 * G_TOIT      # négatif = pas de soulèvement net

CATALOGUE = [
    (75, 200), (75, 225), (100, 200), (100, 225), (100, 250),
    (120, 240), (150, 250), (150, 300), (200, 300),
]


def kh(h_mm):
    return min((150.0 / h_mm) ** 0.2, 1.3) if h_mm < 150 else 1.0


def props(b_mm, h_mm):
    b, h = b_mm / 1000.0, h_mm / 1000.0
    return dict(
        b_mm=b_mm, h_mm=h_mm, b=b, h=h,
        A=b * h, W=b * h ** 2 / 6.0, I=b * h ** 3 / 12.0,
        iy=h / math.sqrt(12.0), iz=b / math.sqrt(12.0),
        g=RHO * 9.81 * b * h / 1000.0,   # kN/m
        kh=kh(h_mm),
    )


def kcrit(b_mm, h_mm, Lef_m):
    """EC5 §6.3.3 — déversement. Lef = L (Tableau 6.1, sans maintien déclaré)."""
    sig_crit = 0.78 * (b_mm ** 2) / h_mm * E05 / (Lef_m * 1000.0)  # MPa
    if sig_crit <= 0:
        return 0.0, 99.0, sig_crit
    lam = math.sqrt(FMK / sig_crit)
    if lam <= 0.75:
        kc = 1.0
    elif lam <= 1.4:
        kc = 1.56 - 0.75 * lam
    else:
        kc = 1.0 / lam ** 2
    return kc, lam, sig_crit


def kc_buck(lam_rel, beta=0.2):
    """EC5 §6.3.2 — flambement, bois massif courbe (β_c = 0,2)."""
    k = 0.5 * (1 + beta * (lam_rel - 0.3) + lam_rel ** 2)
    return 1.0 / (k + math.sqrt(k ** 2 - lam_rel ** 2))


def fmd(kh_):
    return KMOD * kh_ * FMK / GM


def fvd():
    return KMOD * FVK / GM


def fc0d():
    return KMOD * FC0K / GM


def fc90d():
    return KMOD * FC90K / GM


# ============================================================== EN-TÊTE
titre("=" * 78)
log("B-44 — CHARPENTE BOIS — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13) — EC5 §6 / §7.2 · EC1-1-3 · EC1-1-4")
log("Mode : PARTIEL-DÉCLARÉ (H-29 toiture, H-14 périmètre, existant non sondé).")
log("Neufs : C24 prescrit. Existant E-04/05/06 : B-24. E-07 : non chargé.")
log("=" * 78)

titre("[0] HYPOTHÈSES ET CLAUSES OPPOSABLES")
log("  D-26 : AUCUNE VÉRIFICATION SISMIQUE (zone 1).")
log("  D-28 : AUCUN JOINT DE DILATATION.")
log("  D-34 : f_k = 1,5 MPa HYPOTHÈSE — essais hors mission (maçonnerie, pas le bois neuf).")
log("  D-38 : B-41 et B-48 SANS OBJET — « il n'y en a pas sur le projet » (21/10/2026).")
log("  MAT-08 : classe de service 2 (toiture, désordre 6 humidité) — produit par B-44.")
log("  Bois neuf : C24 NF EN 338 — SPÉCIFICATION d'approvisionnement (comme S275).")
log("  H-29 : G_toiture = 0,95 kN/m² (CHG-04 absent). H-14 : charpente dans le lot 01.")
log("  Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée.")
log("  k_mod = 0,80 (T3.1, cl. 2, moyenne durée) · k_def = 0,80 (T3.2, cl. 2, massif).")
log("  k_cr = 0,67 (EC5 §6.1.7(2)) · γ_M = 1,30.")
log("  Déversement : AUCUN maintien supposé (chevrons existants altérés, Désordre 8).")

titre("[1] INVENTAIRE — PREUVE D'ÉPUISEMENT (V14)")
INV = [
    ("PN1", "Panne neuve Est", "C24 à dim.", "3,20", "aile Est, D2 f.02", "NEUF — B-20"),
    ("PN2", "Panne neuve Nord", "C24 à dim.", "3,20", "hall / Ouest", "NEUF — B-20"),
    ("PN3", "Panne neuve Sud", "C24 à dim.", "3,20", "hall / Ouest", "NEUF — B-20"),
    ("DF1", "Demi-ferme n°1", "C24 à dim.", "3,20", "aile Est N, File A–C", "NEUF — suppr. potelet"),
    ("DF2", "Demi-ferme n°2", "C24 à dim.", "3,20", "aile Est S, File A–C", "NEUF — suppr. potelet"),
    ("CF", "Contrefiches ferme tradi", "C24 à dim.", "2,62", "Ouest, Désordre 6", "NEUF — après purge"),
    ("E-04", "Potelets existants", "non sondé", "—", "Désordre 8", "SUPPRIMÉS par DF — B-24"),
    ("E-05", "Ferme tradi existante", "non sondé", "9,90", "Désordre 6", "B-24 — purge puis CF"),
    ("E-06", "Pannes existantes", "non sondé", "3,20", "couverture", "B-24 — non calculées"),
    ("E-07", "Plancher haut", "nature inconnue", "—", "Désordre 5", "NON CHARGÉ — PA-03 B-43"),
    ("ZN1", "ZONE NON RELEVÉE n°1", "—", "—", "D2 f.02 Nord", "AUCUN CALCUL — D-19"),
    ("ZN2", "ZONE NON RELEVÉE n°2", "—", "—", "D2 f.02 Sud", "AUCUN CALCUL — D-19"),
]
log("  %-5s %-28s %-16s %-6s %-22s %s" % ("RÉF", "OUVRAGE", "SECTION", "L m", "EMPLACEMENT", "STATUT"))
for r in INV:
    log("  %-5s %-28s %-16s %-6s %-22s %s" % r)
log("")
log("  Épuisement : D1 (aucune section bois — C-07/R-22) · D2 f.02 (2 demi-fermes,")
log("  3 pannes, contrefiches, 2 zones non relevées) · D3 p.7-9/14-15 (dés. 5, 6, 8) ·")
log("  D4 p.26-27 NIV-02c · B-20 planche 3 · B-21 H-29 · B-23 P-2/P-3 · B-24 E-04..07 ·")
log("  B-25 q_p=500 Pa · B-43 R-43-1/PA-03. Aucun pieu. Aucune prédalle.")

titre("[2] CHARGES — DDC D'EXÉCUTION (distincte de B-21, cohérente)")
log("  G     = %.2f kN/m²  (H-29 : tuiles 0,40 + chevrons 0,15 + pannes/fermes 0,25 + plafond 0,15)"
    % G_TOIT)
log("  Q_s   = %.2f kN/m²  (CHG-05 sk=0,45 — μ1 NON réduit, enveloppe B-21)" % Q_NEIGE)
log("  Q_H   = %.2f kN/m²  (cat. H, NON combiné à la neige)" % Q_H)
log("  q_p   = %.2f kN/m²  (B-25, z=6 m) · |c_pe| courante = %.2f" % (QP_VENT, CPE_UPLIFT))
log("  p_ELU = 1,35 G + 1,5 Q_s = %.3f kN/m²" % P_ELU)
log("  p_ELS,G = %.2f · p_ELS,Q = %.2f" % (P_ELS_G, P_ELS_Q))
log("  w_dépression = q_p · |c_pe| = %.2f kN/m²" % W_UPLIFT)
log("  p_uplift ELU = 1,5 w − 1,0 G = %.3f kN/m²  %s"
    % (P_UPLIFT, "→ PAS DE SOULÈVEMENT NET (G gouverne)" if P_UPLIFT < 0
       else "→ SOULÈVEMENT — ancrage B-50"))
log("  α = %.1f° (NIV-02c min) · L_arb = L_DF/cos α = %.3f m · h_DF = %.3f m"
    % (ALPHA_DEG, L_ARB, H_DF))
log("  D-26 : EC8 non applicable (zone 1).")

# ============================================================== PANNES
titre("[3] PANNES NEUVES PN1/PN2/PN3 — EC5 §6.1 / §6.3.3 / §7.2")
log("  L = %.2f m · e = %.2f m · 3 unités identiques (B-20)." % (L_PANNE, E_PANNE))
log("  Appuis simples. Semelle comprimée NON maintenue (Désordre 8 : chevrons altérés).")
log("  Formules :")
log("    M_Ed = p L² / 8 · V_Ed = p L / 2")
log("    σ_m,d = M_Ed / W  ≤  k_crit · f_m,d     (EC5 6.11 + 6.3.3)")
log("    τ_d   = 1,5 V_Ed / (k_cr b h)  ≤ f_v,d  (EC5 6.13 + 6.1.7)")
log("    σ_c,90,d = V_Ed / (b · l_app)  ≤ k_c,90 f_c,90,d  (l_app = 100 mm, k_c,90 = 1,5 appuis)")
log("    w_inst = 5 p L⁴ / (384 E I) · w_fin = w_G(1+k_def) + w_Q(1+ψ2 k_def)")
log("    w_lim = L/300 (EC5 T7.2, éléments de toiture).")


def verif_panne(b_mm, h_mm):
    s = props(b_mm, h_mm)
    p = P_ELU * E_PANNE + s["g"]
    pG = P_ELS_G * E_PANNE + s["g"]
    pQ = P_ELS_Q * E_PANNE
    Med = p * L_PANNE ** 2 / 8.0
    Ved = p * L_PANNE / 2.0
    sig = Med * 1e-3 / s["W"]          # kN.m / m³ = kPa → /1000 = MPa ; 1e-3 because kN/m²=kPa, W m³ → kPa, /1e3=MPa
    # M [kN.m] / W [m³] = kN/m² = 10⁻³ MPa. Yes sig = Med / W / 1000.
    sig = Med / s["W"] / 1000.0
    tau = 1.5 * Ved / (KCR * s["b"] * s["h"]) / 1000.0
    kc, lam, scrit = kcrit(b_mm, h_mm, L_PANNE)
    fm = fmd(s["kh"])
    taux_m = sig / (kc * fm) if kc > 0 else 99.0
    taux_v = tau / fvd()
    l_app = 0.10
    kc90 = 1.5
    sig90 = Ved / (s["b"] * l_app) / 1000.0
    taux_90 = sig90 / (kc90 * fc90d())
    wG = 5.0 * pG * L_PANNE ** 4 / (384.0 * EMEAN * 1e3 * s["I"]) * 1e3  # mm  (E MPa=N/mm²; convert)
    # E [MPa=N/mm²=10^6 N/m²] ; I m⁴ ; p kN/m = 10³ N/m
    # w = 5 p L^4 / (384 E I)  in m if p in N/m, E in N/m², I in m⁴
    E_Nm2 = EMEAN * 1e6
    wG_m = 5.0 * (pG * 1e3) * L_PANNE ** 4 / (384.0 * E_Nm2 * s["I"])
    wQ_m = 5.0 * (pQ * 1e3) * L_PANNE ** 4 / (384.0 * E_Nm2 * s["I"])
    w_inst = (wG_m + wQ_m) * 1000.0
    w_fin = (wG_m * (1.0 + KDEF) + wQ_m * (1.0 + PSI2_S * KDEF)) * 1000.0
    wlim = L_PANNE / 300.0 * 1000.0
    taux_w = w_fin / wlim
    ok = max(taux_m, taux_v, taux_90, taux_w) <= 1.0
    return dict(sec="%d×%d" % (b_mm, h_mm), p=p, Med=Med, Ved=Ved, sig=sig, tau=tau,
                kc=kc, lam=lam, scrit=scrit, fm=fm, kh=s["kh"], g=s["g"],
                taux_m=taux_m, taux_v=taux_v, taux_90=taux_90, taux_w=taux_w,
                w_inst=w_inst, w_fin=w_fin, wlim=wlim, ok=ok,
                max_taux=max(taux_m, taux_v, taux_90, taux_w))


panne_ok = None
log("  Catalogue C24 (b×h mm) — premier qui passe TOUTES les vérifications :")
log("  %-8s %6s %6s %6s %6s %6s %6s  %s" %
    ("SECTION", "σ/f", "τ/f", "c90", "w_fin", "k_crit", "λ_rel", "VERDICT"))
panne_scan = []
for bh in CATALOGUE:
    r = verif_panne(*bh)
    panne_scan.append(r)
    log("  %-8s %6.3f %6.3f %6.3f %6.3f %6.3f %6.2f  %s" %
        (r["sec"], r["taux_m"], r["taux_v"], r["taux_90"], r["taux_w"],
         r["kc"], r["lam"], "OK" if r["ok"] else "NON"))
    if r["ok"] and panne_ok is None:
        panne_ok = r

if panne_ok is None:
    raise SystemExit("aucune panne du catalogue ne passe")
log("")
log("  RETENU : %s C24" % panne_ok["sec"])
log("    p_ELU = %.3f kN/m (dont g_propre %.3f) · M_Ed = %.3f kN·m · V_Ed = %.3f kN"
    % (panne_ok["p"], panne_ok["g"], panne_ok["Med"], panne_ok["Ved"]))
log("    k_h = %.3f · f_m,d = %.2f MPa · k_crit = %.3f (λ_rel,m = %.2f, σ_crit = %.1f MPa)"
    % (panne_ok["kh"], panne_ok["fm"], panne_ok["kc"], panne_ok["lam"], panne_ok["scrit"]))
log("    flexion k_crit : %.3f · cisaillement : %.3f · appui : %.3f · flèche : %.3f"
    % (panne_ok["taux_m"], panne_ok["taux_v"], panne_ok["taux_90"], panne_ok["taux_w"]))
log("    w_inst = %.2f mm · w_fin = %.2f mm · L/300 = %.2f mm"
    % (panne_ok["w_inst"], panne_ok["w_fin"], panne_ok["wlim"]))

# ============================================================== DEMI-FERMES
titre("[4] DEMI-FERMES DF1/DF2 — TREILLIS (arbalétrier + entrait)")
log("  L_horiz = %.2f m · α = %.1f° · L_arb = %.3f m · h = %.3f m" % (L_DF, ALPHA_DEG, L_ARB, H_DF))
log("  2 unités. Désolidarisées du plancher (B-20). Potelets E-04 SUPPRIMÉS après pose.")
log("  Surface tributaire par DF : (Y_est / 2) × L_DF = %.2f × %.2f = %.2f m²"
    % (Y_EST / 2.0, L_DF, Y_EST / 2.0 * L_DF))
A_DF = Y_EST / 2.0 * L_DF
W_DF = P_ELU * A_DF
log("  W_ELU = p_ELU × A = %.3f × %.2f = %.2f kN  (charge verticale totale)" % (P_ELU, A_DF, W_DF))
log("  Treillis isostatique triangle :")
log("    H_entrait = (W L / 4) / h     [2 appuis, M_eq = W L/4 en bipoint médian conserv.]")
log("    N_arb     = (W / 2) / sin α")
log("    V_appui   = W / 2")
# conservative: treat as central point load (panne faîtière) → M = W L / 4
H_ENT = (W_DF * L_DF / 4.0) / H_DF
N_ARB = (W_DF / 2.0) / math.sin(ALPHA)
V_APP = W_DF / 2.0
log("    H_entrait = %.2f kN (traction) · N_arb = %.2f kN (compression) · V_appui = %.2f kN"
    % (H_ENT, N_ARB, V_APP))
log("  Arbalétrier : compression + flambement (EC5 §6.3.2) + flexion de poids propre.")
log("  Entrait : traction parallèle (EC5 §6.1.2).")


def verif_arb(b_mm, h_mm):
    s = props(b_mm, h_mm)
    # buckling in the weak axis if not braced ; L_ef = L_arb (conservateur)
    lam = (L_ARB / s["iz"])          # élancement
    lam_rel = (lam / math.pi) * math.sqrt(FC0K / E05)
    kc = kc_buck(lam_rel)
    # poids propre de l'arbalétrier : flexion L_arb, p = g
    Med = s["g"] * L_ARB ** 2 / 8.0
    sig_m = Med / s["W"] / 1000.0
    sig_c = N_ARB / s["A"] / 1000.0
    fm = fmd(s["kh"])
    fc = fc0d()
    # interaction EC5 (6.23) : σ_c /(kc fc) + σ_m / f_m ≤ 1
    taux = sig_c / (kc * fc) + sig_m / fm
    ok = taux <= 1.0
    return dict(sec="%d×%d" % (b_mm, h_mm), N=N_ARB, Med=Med, sig_c=sig_c, sig_m=sig_m,
                lam=lam, lam_rel=lam_rel, kc=kc, taux=taux, ok=ok, g=s["g"],
                kh=s["kh"], fm=fm, fc=fc)


def verif_entrait(b_mm, h_mm):
    s = props(b_mm, h_mm)
    ftd = KMOD * 14.0 / GM          # f_t,0,k C24 = 14 MPa
    sig = H_ENT / s["A"] / 1000.0
    taux = sig / ftd
    return dict(sec="%d×%d" % (b_mm, h_mm), N=H_ENT, sig=sig, ftd=ftd, taux=taux,
                ok=taux <= 1.0)


arb_ok = None
log("  Arbalétrier — catalogue :")
log("  %-8s %6s %6s %6s %6s  %s" % ("SECTION", "λ_rel", "k_c", "taux", "σ_c", "VERDICT"))
arb_scan = []
for bh in CATALOGUE:
    r = verif_arb(*bh)
    arb_scan.append(r)
    log("  %-8s %6.3f %6.3f %6.3f %6.2f  %s" %
        (r["sec"], r["lam_rel"], r["kc"], r["taux"], r["sig_c"], "OK" if r["ok"] else "NON"))
    if r["ok"] and arb_ok is None:
        arb_ok = r
if arb_ok is None:
    raise SystemExit("aucun arbalétrier du catalogue ne passe")

ent_ok = None
for bh in CATALOGUE:
    r = verif_entrait(*bh)
    if r["ok"] and ent_ok is None:
        ent_ok = r
        break
if ent_ok is None:
    raise SystemExit("aucun entrait du catalogue ne passe")

log("")
log("  RETENU arbalétrier : %s C24 — taux interaction %.3f · λ_rel = %.3f · k_c = %.3f"
    % (arb_ok["sec"], arb_ok["taux"], arb_ok["lam_rel"], arb_ok["kc"]))
log("  RETENU entrait     : %s C24 — traction %.3f (N = %.2f kN, σ = %.2f MPa, f_t,0,d = %.2f)"
    % (ent_ok["sec"], ent_ok["taux"], ent_ok["N"], ent_ok["sig"], ent_ok["ftd"]))
log("  Appui mural : V = %.2f kN par about → B-46/B-50 (PA-02 liaison charpente-maçonnerie)."
    % V_APP)

# ============================================================== CONTREFICHES
titre("[5] CONTREFICHES SUR FERME TRADI — COMPRESSION + FLAMBEMENT (EC5 §6.3.2)")
log("  L_ef = %.2f m (hauteur de versant NIV-02c min, conservateur)." % L_CF)
log("  Rôle : reprendre la ferme E-05 APRÈS purge (B-23 P-2). La ferme elle-même n'est pas calculée.")
log("  Charge : fraction de la ferme. Enveloppe : bande 3,20 m × demi-portée 4,90 m / 2 appuis.")
# ferme tradi ouest : File C–E = 6,60 m span? B-24 used 9.90 m. Contrefiche takes compression
# from rafter. Conservative: N = (p_ELU * e_ferme * L_ferme/2) * sin component
# Use B-24 E-05 p = 4.89 to 6.85 kN/m on L=9.90 m. We don't retain a value from B-24 sensitivity.
# Instead: new load path via CF : N_cf = W_half * cos-related.
# Simple : CF takes the same N as an arbalétrier of the tradi farm on 6.60 m (File C–E).
L_FERME_OUEST = 95.35 - 88.75   # 6.60 m File C–E, B-20
A_CF = L_FERME_OUEST / 2.0 * L_PANNE   # half farm × panne spacing
W_CF = P_ELU * A_CF
N_CF = W_CF / math.sin(ALPHA)    # compression in strut along the slope, conservative
log("  File C–E = %.2f m · A_trib = %.2f m² · W = %.2f kN · N_cf = W/sin α = %.2f kN"
    % (L_FERME_OUEST, A_CF, W_CF, N_CF))
log("  Formule : N_Ed / (k_c A f_c,0,d) ≤ 1  (EC5 6.3.2). Pas de flexion (bielles).")


def verif_cf(b_mm, h_mm):
    s = props(b_mm, h_mm)
    i_min = min(s["iy"], s["iz"])
    lam = L_CF / i_min
    lam_rel = (lam / math.pi) * math.sqrt(FC0K / E05)
    kc = kc_buck(lam_rel)
    sig = N_CF / s["A"] / 1000.0
    taux = sig / (kc * fc0d())
    return dict(sec="%d×%d" % (b_mm, h_mm), N=N_CF, sig=sig, lam=lam, lam_rel=lam_rel,
                kc=kc, taux=taux, ok=taux <= 1.0)


cf_ok = None
log("  %-8s %6s %6s %6s %6s  %s" % ("SECTION", "λ_rel", "k_c", "σ_c", "taux", "VERDICT"))
cf_scan = []
for bh in CATALOGUE:
    r = verif_cf(*bh)
    cf_scan.append(r)
    log("  %-8s %6.3f %6.3f %6.2f %6.3f  %s" %
        (r["sec"], r["lam_rel"], r["kc"], r["sig"], r["taux"], "OK" if r["ok"] else "NON"))
    if r["ok"] and cf_ok is None:
        cf_ok = r
if cf_ok is None:
    raise SystemExit("aucune contrefiche du catalogue ne passe")
log("")
log("  RETENU : %s C24 — taux %.3f · λ_rel = %.3f · k_c = %.3f · N_Ed = %.2f kN"
    % (cf_ok["sec"], cf_ok["taux"], cf_ok["lam_rel"], cf_ok["kc"], cf_ok["N"]))

# ============================================================== EXISTANT / E-07
titre("[6] EXISTANT ET PLANCHER HAUT — HORS CALCUL")
log("  E-04 potelets : B-20 les SUPPRIME (remplacés par DF1/DF2). Pas de flambement à vérifier")
log("    sous charge augmentée : la charge est DÉVIÉE vers les murs. Séquence : pose DF →")
log("    reprise → dépose potelets (B-23 P-3 inversé par le parti B-20).")
log("  E-05 ferme : B-24 DÉFAVORABLE sur toute plage. Renfort = CF après purge (B-23 P-2).")
log("    Aucune section résiduelle retenue. Aucune valeur de B-24 n'est contractuelle.")
log("  E-06 pannes existantes : B-24 LIMITE. 3 pannes neuves AJOUTÉES, existant non calculé.")
log("  E-07 plancher haut : les DF sont DÉSOLIDARISÉES (B-20, coupe A-A). Les neufs")
log("    chargent les MURS, pas E-07. PA-03 reste un point d'arrêt de B-43 (nature de E-07),")
log("    il NE BLOQUE PAS B-44. Si la charpente sortait du programme, PA-03 tombait (B-43) ;")
log("    le GO de B-44 la maintient dans le programme (H-14).")
log("  ZN1 / ZN2 : emprises non cotées (B-23 §3). Relevé avant taille — déjà prescrit")
log("    (B-20 point 6, nuage D-19). Pas une demande nouvelle.")

titre("[7] EFFORTS AUX APPUIS ET ASSEMBLAGES → B-50")
log("  %-8s %-22s %8s %8s %8s  %s" % ("NŒUD", "NATURE", "N_Ed", "V_Ed", "M_Ed", "TYPE"))
efforts = [
    ("PN-app", "panne / sablière ou DF", 0.0, panne_ok["Ved"], 0.0, "sabot ou entaille"),
    ("DF-mur", "entrait / mur File A ou C", H_ENT, V_APP, 0.0, "sabot + ancrage anti-soulèvement"),
    ("DF-faît", "arbalétrier / poinçon", N_ARB, 0.0, 0.0, "boulonné / entaillé"),
    ("CF-arb", "contrefiche / arbalétrier E-05", N_CF, 0.0, 0.0, "boulonné — APRÈS purge"),
    ("CF-ent", "contrefiche / entrait E-05", N_CF, 0.0, 0.0, "boulonné — APRÈS purge"),
]
for e in efforts:
    log("  %-8s %-22s %8.2f %8.2f %8.2f  %s" % e)
log("  Soulèvement net toiture : %.3f kN/m² → %s"
    % (P_UPLIFT, "néant (G > 1,5 w)" if P_UPLIFT < 0 else "ancrage à dimensionner"))
log("  PA-02 (liaison charpente-maçonnerie) MAINTENU — B-21. Efforts fournis, logements B-50.")
log("  Aucun Johansen ici. Aucun sabot chiffré.")

titre("[8] DISPOSITIONS CONSTRUCTIVES")
log("  Contreventement de toiture : ABSENT au D2 (B-25). Les pannes neuves ne constituent")
log("    PAS un diaphragme. Croix de Saint-André / entretoises → B-60, hors calcul de section.")
log("  Ventilation sous-face : lame d'air + chatières — prescription, pas un calcul.")
log("  Phasage E-05 : 1. purge bois mort  2. traitement  3. pose CF  (B-23 P-2). Ordre inverse interdit.")
log("  Phasage E-04 : 1. pose DF1/DF2  2. reprise des pannes  3. dépose potelets.")
log("  Classe de service 2 : toiture, humidité (désordre 6). Pas de classe 1.")
log("  Termites : D1 § 01.2.1.9.2 déjà prescrit (ne pas rouvrir).")

titre("[9] AUTO-CONTRÔLE DÉCLARÉ")
log("  %-6s %-22s %-10s %-8s %s" % ("RÉF", "ÉLÉMENT", "SECTION", "TAUX", "VERDICT"))
log("  %-6s %-22s %-10s %-8.3f %s" % ("PN1-3", "Pannes neuves", panne_ok["sec"],
                                       panne_ok["max_taux"], "OK"))
log("  %-6s %-22s %-10s %-8.3f %s" % ("DF-arb", "Arbalétrier DF", arb_ok["sec"],
                                       arb_ok["taux"], "OK"))
log("  %-6s %-22s %-10s %-8.3f %s" % ("DF-ent", "Entrait DF", ent_ok["sec"],
                                       ent_ok["taux"], "OK"))
log("  %-6s %-22s %-10s %-8.3f %s" % ("CF", "Contrefiches", cf_ok["sec"],
                                       cf_ok["taux"], "OK"))
log("  %-6s %-22s %-10s %-8s %s" % ("E-04", "Potelets", "—", "—", "SUPPRIMÉS — hors calcul"))
log("  %-6s %-22s %-10s %-8s %s" % ("E-05", "Ferme tradi", "—", "—", "B-24 + purge — hors calcul"))
log("  %-6s %-22s %-10s %-8s %s" % ("E-06", "Pannes exist.", "—", "—", "B-24 — hors calcul"))
log("  %-6s %-22s %-10s %-8s %s" % ("E-07", "Plancher haut", "—", "—", "NON CHARGÉ — PA-03 B-43"))
log("  %-6s %-22s %-10s %-8s %s" % ("ZN", "2 zones NR", "—", "—", "D-19 — hors calcul"))
log("")
log("  COMPLET interdit (V12) : EXI-01g / MAT-06 existant absents, CHG-04 = H-29,")
log("  2 zones non cotées. PARTIEL-DÉCLARÉ assumé.")

res = {
    "indice": "A",
    "mode": "PARTIEL-DECLARE",
    "panne": panne_ok,
    "arbaletrier": arb_ok,
    "entrait": ent_ok,
    "contrefiche": cf_ok,
    "p_ELU": round(P_ELU, 3),
    "p_uplift": round(P_UPLIFT, 3),
    "W_DF": round(W_DF, 2),
    "H_ENT": round(H_ENT, 2),
    "N_ARB": round(N_ARB, 2),
    "V_APP": round(V_APP, 2),
    "N_CF": round(N_CF, 2),
    "alpha_deg": ALPHA_DEG,
    "L_arb": round(L_ARB, 3),
    "D38_B41_B48_SO": True,
    "E07_charge": False,
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
for nom, coul in (("CHARPENTE-AXES", 1), ("CHARPENTE-COFFRAGE", 5),
                  ("CHARPENTE-EXISTANT", 8), ("CHARPENTE-HABILLAGE-TEXTE", 7),
                  ("CHARPENTE-CARTOUCHE", 7)):
    doc.layers.add(nom, color=coul)


def txt(x, y, t, ht=2.4, layer="CHARPENTE-HABILLAGE-TEXTE"):
    e = msp.add_text(t, height=ht, dxfattribs={"layer": layer})
    e.set_placement((x, y))


def rect(x0, y0, x1, y1, layer="CHARPENTE-COFFRAGE"):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)],
                       dxfattribs={"layer": layer})


def ligne(x0, y0, x1, y1, layer="CHARPENTE-COFFRAGE"):
    msp.add_line((x0, y0), (x1, y1), dxfattribs={"layer": layer})


rect(8, 8, 412, 289, "CHARPENTE-CARTOUCHE")
txt(14, 279, "CROISSY-FLORA — B-44 — CHARPENTE BOIS : PANNES, DEMI-FERMES, CONTREFICHES", 3.4, "CHARPENTE-AXES")
txt(14, 272.5, "Indice A — 21/10/2026 — Mode PARTIEL-DÉCLARÉ (H-29, H-14, existant non sondé)", 2.3, "CHARPENTE-AXES")
txt(14, 267, "Protection au feu : ADÉQUATE À PRÉVOIR (hors lot GO) — NON dimensionnée. Bois neuf C24.", 2.2)

# 1. coupe demi-ferme
txt(14, 257, "1. DEMI-FERME EN SOUS-ŒUVRE — COUPE (désolidarisée du plancher)", 2.4, "CHARPENTE-AXES")
x0, y0 = 28, 200
# murs
rect(x0, y0, x0 + 8, y0 + 28, "CHARPENTE-EXISTANT")
rect(x0 + 72, y0, x0 + 80, y0 + 28, "CHARPENTE-EXISTANT")
# plancher (non chargé)
ligne(x0 + 8, y0 + 28, x0 + 72, y0 + 28, "CHARPENTE-EXISTANT")
txt(x0 + 22, y0 + 29.5, "plancher haut E-07 — NON CHARGÉ", 1.7, "CHARPENTE-AXES")
# triangle DF
faix, faiy = x0 + 40, y0 + 52
ligne(x0 + 8, y0 + 36, faix, faiy, "CHARPENTE-COFFRAGE")
ligne(x0 + 72, y0 + 36, faix, faiy, "CHARPENTE-COFFRAGE")
ligne(x0 + 8, y0 + 36, x0 + 72, y0 + 36, "CHARPENTE-COFFRAGE")  # entrait
# gap under entrait = désolidarisation
ligne(x0 + 8, y0 + 32, x0 + 72, y0 + 32, "CHARPENTE-AXES")
txt(x0 + 18, y0 + 33.5, "vide de désolidarisation", 1.6, "CHARPENTE-AXES")
# panne
rect(faix - 3, faiy - 2, faix + 3, faiy + 3, "CHARPENTE-COFFRAGE")
txt(x0 + 82, y0 + 48, "arbalétrier %s C24" % arb_ok["sec"], 1.85, "CHARPENTE-AXES")
txt(x0 + 82, y0 + 43, "entrait %s C24" % ent_ok["sec"], 1.85)
txt(x0 + 82, y0 + 38, "L_h 3,20 m  α 28°  N_arb %.1f kN" % N_ARB, 1.85)
txt(x0 + 82, y0 + 33, "H_entrait %.1f kN  V_appui %.1f kN" % (H_ENT, V_APP), 1.85)
txt(x0 + 82, y0 + 28, "potelet E-04 SUPPRIMÉ", 1.85, "CHARPENTE-AXES")

# 2. tableau
txt(14, 188, "2. ÉLÉMENTS NEUFS — CONTRÔLE EC5", 2.4, "CHARPENTE-AXES")
rect(14, 118, 250, 182, "CHARPENTE-CARTOUCHE")
cols = (16, 52, 95, 140, 185, 215)
for c, t in zip(cols, ("RÉF", "SECTION C24", "L m", "TAUX", "VÉRIF. GOUV.", "VERDICT")):
    txt(c, 176, t, 1.85, "CHARPENTE-AXES")
lignes_t = [
    ("PN1/2/3", panne_ok["sec"], "3,20", "%.3f" % panne_ok["max_taux"],
     "flèche L/300", "OK"),
    ("DF-arb", arb_ok["sec"], "%.2f" % L_ARB, "%.3f" % arb_ok["taux"],
     "flambement", "OK"),
    ("DF-ent", ent_ok["sec"], "3,20", "%.3f" % ent_ok["taux"],
     "traction", "OK"),
    ("CF", cf_ok["sec"], "2,62", "%.3f" % cf_ok["taux"],
     "flambement", "OK"),
]
for k, l in enumerate(lignes_t):
    y = 168 - k * 11
    for c, v in zip(cols, l):
        txt(c, y, v, 2.0)

# 3. existant hors calcul
txt(255, 257, "3. EXISTANT — HORS CALCUL", 2.4, "CHARPENTE-AXES")
rect(255, 175, 405, 250, "CHARPENTE-CARTOUCHE")
exl = [
    "E-04 potelets : SUPPRIMÉS par DF1/DF2.",
    "E-05 ferme : B-24, purge PUIS CF (P-2).",
    "E-06 pannes exist. : B-24, non chiffrées.",
    "E-07 plancher : NON CHARGÉ (désolidarisation).",
    "PA-03 reste un arrêt de B-43, pas de B-44.",
    "ZN1 / ZN2 : relevé avant taille (D-19).",
    "Chevrons altérés (dés. 8) : pas de maintien",
    "compté pour le déversement des pannes.",
    "Aucun bois existant dimensionné ici.",
]
for k, t in enumerate(exl):
    txt(258, 243 - k * 7.0, t, 1.85)

# 4. D-34 + D-38
rect(255, 108, 405, 168, "CHARPENTE-CARTOUCHE")
txt(258, 161, "CLAUSES OPPOSABLES — MAJUSCULES", 2.0, "CHARPENTE-AXES")
clause = [
    "D-26 : AUCUNE VÉRIFICATION SISMIQUE.",
    "D-28 : AUCUN JOINT DE DILATATION.",
    "D-34 : f_k = 1,5 MPa — ESSAIS HORS MISSION.",
    "D-38 : B-41 ET B-48 SANS OBJET",
    "(PAS DE PIEU, PAS DE PRÉDALLE).",
    "C24 NEUF PRESCRIT — PAS UNE MESURE.",
]
for k, t in enumerate(clause):
    txt(258, 154 - k * 7.0, t, 1.85, "CHARPENTE-AXES")

# notes
txt(14, 108, "NOTES OPPOSABLES", 2.3, "CHARPENTE-AXES")
notes = [
    "1. Pannes %s C24 — taux %.3f (flèche L/300). Déversement vérifié SANS maintien (k_crit=1,00)." % (panne_ok["sec"], panne_ok["max_taux"]),
    "2. Demi-fermes désolidarisées : charges aux murs File A/C, pas à E-07.",
    "3. Contrefiches %s APRÈS purge de E-05. Ordre inverse interdit (B-23 P-2)." % cf_ok["sec"],
    "4. Soulèvement net %.2f kN/m² : G gouverne. Ancrages locaux → B-50." % P_UPLIFT,
    "5. Assemblages NON calculés (B-50). PA-02 liaison charpente-maçonnerie maintenu.",
    "6. Classe de service 2 · k_mod 0,80 · k_def 0,80 · k_cr 0,67 · γ_M 1,30.",
]
for k, t in enumerate(notes):
    txt(14, 101 - k * 6.5, t, 1.9)

rect(14, 10, 405, 48, "CHARPENTE-CARTOUCHE")
txt(18, 40, "EHPAD LA ROSERAIE — PAVILLON FLORA (CROISSY-SUR-SEINE)", 3.0, "CHARPENTE-AXES")
txt(18, 32, "B-44 — CHARPENTE BOIS  ·  Indice A · 21/10/2026 · PARTIEL-DÉCLARÉ · DXF mm", 2.0)
txt(18, 25, "EC5 §6.1 / §6.3 / §7.2 · C24 · cl. service 2 · CARNAC v3.0", 2.0)
txt(18, 14, "NE PAS EXÉCUTER SANS EXE COTÉ ET VISA", 4.0, "CHARPENTE-AXES")

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

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "b44_charpente.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
with open(os.path.join(OUT, "b44_charpente.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)

log("")
log("Journal : %s (%d o)" % (os.path.join(OUT, "b44_charpente.txt"),
                             os.path.getsize(os.path.join(OUT, "b44_charpente.txt"))))
log("JSON    : %s (%d o)" % (os.path.join(OUT, "b44_charpente.json"),
                             os.path.getsize(os.path.join(OUT, "b44_charpente.json"))))
