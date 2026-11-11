"""
Affaire GARENNE — 58 rue de l'Aigle, 92250 La Garenne-Colombes
Moteur de calculs structurels — TACHE 2

Eurocodes 0, 1, 2, 3, 6, 7 + Annexes Nationales françaises.
Toutes les unités internes sont le kN, le m, le MPa (sauf mention contraire).

Le module ne produit aucun graphique : il écrit un dictionnaire de résultats
sérialisé dans `calculs_resultats.json`, consommé par `make_doc03.py`.
"""

from __future__ import annotations

import json
import math
import os
import sys

# Source unique de vérité pour les niveaux NGF et la position du poteau BA.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "00_SOURCES"))
import niveaux_retenus as NIV          # noqa: E402

# ---------------------------------------------------------------------------
# 1. DONNEES DE BASE (hypothèses de la note DOC-01)
# ---------------------------------------------------------------------------

GAMMA_BA = 25.0          # kN/m³  béton armé
GAMMA_ACIER = 78.5       # kN/m³  acier de construction (7850 kg/m³)
GRAVITE = 9.81

# Béton C25/30 — NF EN 206/CN
FCK = 25.0               # MPa
FCD = FCK / 1.5          # 16,67 MPa  (αcc = 1,0 selon AN française)
FCTM = 2.6               # MPa  (0,30 fck^(2/3))
FCTD = FCTM / 1.5        # 1,73 MPa
ECU2 = 3.5e-3
ES = 200000.0            # MPa

# Acier B500B — NF EN 10080
FYK = 500.0
FYD = FYK / 1.15         # 434,8 MPa

# Acier de construction S275 / S355 — NF EN 10025-2
S275 = {"fy": 275.0, "fu": 430.0, "E": 210000.0}
S355 = {"fy": 355.0, "fu": 510.0, "E": 210000.0}
GAMMA_M0 = 1.0
GAMMA_M1 = 1.0

# Sol — hypothèses imposées
Q_ELS = 0.100            # MPa   (100 kPa)
Q_ELU = 0.150            # MPa   (150 kPa)
GAMMA_SOL = 18.0         # kN/m³  remblai / limon
PHI_SOL = 30.0           # degrés

# Charges d'exploitation et permanentes (DOC-01, §4)
Q_CAT_A = 1.50           # kN/m²  habitation
G1_CLOISON = 1.50        # kN/m²
G0_PH = 3.00             # kN/m²  plancher haut RDC et R+1
G0_SSOL = 4.00           # kN/m²  plancher sur sous-sol

# Critère de flèche imposé par le BET
FLECHE_RATIO = 750.0
FLECHE_ABS = 5.0         # mm


def psi0(cat="A"):
    return {"A": 0.7, "B": 0.7, "C": 0.7, "D": 0.7}.get(cat, 0.7)


# ---------------------------------------------------------------------------
# 2. CATALOGUE DE PROFILES METALLIQUES (dimensions en mm)
#    h, b, tw, tf, r, A (cm²), Iy (cm4), Wel,y (cm3), Wpl,y (cm3), It (cm4)
# ---------------------------------------------------------------------------

PROFILES = {
    # IPE
    "IPE 160": dict(h=160, b=82, tw=5.0, tf=7.4, r=9, A=20.1, Iy=869, Wely=109, Wply=124, It=6.1),
    "IPE 180": dict(h=180, b=91, tw=5.3, tf=8.0, r=9, A=23.9, Iy=1317, Wely=146, Wply=166, It=8.7),
    "IPE 200": dict(h=200, b=100, tw=5.6, tf=8.5, r=12, A=28.5, Iy=1943, Wely=194, Wply=221, It=11.2),
    "IPE 220": dict(h=220, b=110, tw=5.9, tf=9.2, r=12, A=33.4, Iy=2772, Wely=252, Wply=285, It=15.6),
    "IPE 240": dict(h=240, b=120, tw=6.2, tf=9.8, r=15, A=39.1, Iy=3892, Wely=324, Wply=367, It=20.7),
    "IPE 270": dict(h=270, b=135, tw=6.6, tf=10.2, r=15, A=45.9, Iy=5790, Wely=429, Wply=484, It=27.9),
    "IPE 300": dict(h=300, b=150, tw=7.1, tf=10.7, r=15, A=53.8, Iy=8356, Wely=557, Wply=628, It=36.3),
    "IPE 330": dict(h=330, b=160, tw=7.5, tf=11.5, r=18, A=62.6, Iy=11770, Wely=713, Wply=804, It=49.3),
    "IPE 360": dict(h=360, b=170, tw=8.0, tf=12.7, r=18, A=72.7, Iy=16270, Wely=904, Wply=1019, It=65.6),
    "IPE 400": dict(h=400, b=180, tw=8.6, tf=13.5, r=21, A=84.5, Iy=23130, Wely=1156, Wply=1307, It=89.1),
    "IPE 450": dict(h=450, b=190, tw=9.4, tf=14.6, r=21, A=98.8, Iy=33740, Wely=1500, Wply=1702, It=123.0),
    "IPE 500": dict(h=500, b=200, tw=10.2, tf=16.0, r=21, A=116.0, Iy=48200, Wely=1928, Wply=2194, It=166.0),
    # HEA
    "HEA 120": dict(h=114, b=120, tw=5.0, tf=8.0, r=12, A=25.3, Iy=606, Wely=106, Wply=119, It=5.0),
    "HEA 140": dict(h=133, b=140, tw=5.5, tf=8.5, r=12, A=31.4, Iy=1033, Wely=155, Wply=173, It=8.1),
    "HEA 160": dict(h=152, b=160, tw=6.0, tf=9.0, r=15, A=38.8, Iy=1673, Wely=220, Wply=245, It=12.2),
    "HEA 180": dict(h=171, b=180, tw=6.0, tf=9.5, r=15, A=45.3, Iy=2510, Wely=294, Wply=325, It=14.8),
    "HEA 200": dict(h=190, b=200, tw=6.5, tf=10.0, r=18, A=53.8, Iy=3692, Wely=389, Wply=430, It=21.0),
    "HEA 220": dict(h=210, b=220, tw=7.0, tf=11.0, r=18, A=64.3, Iy=5410, Wely=515, Wply=568, It=28.5),
    "HEA 240": dict(h=230, b=240, tw=7.5, tf=12.0, r=21, A=76.8, Iy=7763, Wely=675, Wply=745, It=41.6),
    "HEA 260": dict(h=250, b=260, tw=7.5, tf=12.5, r=24, A=86.8, Iy=10450, Wely=836, Wply=920, It=52.4),
    "HEA 280": dict(h=270, b=280, tw=8.0, tf=13.0, r=24, A=97.3, Iy=13670, Wely=1013, Wply=1112, It=62.1),
    "HEA 300": dict(h=290, b=300, tw=8.5, tf=14.0, r=27, A=112.5, Iy=18260, Wely=1260, Wply=1383, It=85.2),
    "HEA 320": dict(h=310, b=300, tw=9.0, tf=15.5, r=27, A=124.4, Iy=22930, Wely=1479, Wply=1628, It=108.0),
    "HEA 340": dict(h=330, b=300, tw=9.5, tf=16.5, r=27, A=133.5, Iy=27690, Wely=1678, Wply=1850, It=127.0),
    "HEA 360": dict(h=350, b=300, tw=10.0, tf=17.5, r=27, A=142.8, Iy=33090, Wely=1891, Wply=2088, It=149.0),
}

# Profilés jumelés : deux profilés assemblés dos à dos
JUMELES = {f"{k} × 2": {kk: (vv * 2 if kk in ("A", "Iy", "Wely", "Wply", "It") else vv)
                        for kk, vv in v.items()}
           for k, v in PROFILES.items()}


# ---------------------------------------------------------------------------
# 3. BETON ARME — flexion simple, section rectangulaire (NF EN 1992-1-1)
# ---------------------------------------------------------------------------

def ba_flexion(b, h, Med, d_prime=0.05, fc=None, fy=None):
    """Flexion simple ELS/ELU d'une section rectangulaire b×h (en m).

    Retourne un dict : bras de levier, moment réduit, section d'acier requise,
    taux de travail, et le choix de ferraillage compatible.
    """
    fc = FCD if fc is None else fc
    fy = FYD if fy is None else fy
    d = h - d_prime
    mu = Med / (b * d ** 2 * fc * 1000.0)     # Med en kN·m -> N·mm homogène
    if mu > 0.372:
        return dict(ok=False, mu=mu, raison="Section insuffisante en flexion simple")
    alpha = 1.25 * (1.0 - math.sqrt(1.0 - 2.0 * mu))
    z = d * (1.0 - 0.4 * alpha)
    As = Med / (z * fy * 1000.0) * 1e4        # cm²
    return dict(ok=True, mu=mu, alpha=alpha, z=z, As_cm2=As, d=d)


def choix_ferraillage(As_req_cm2, n_min=2, phi_min=8, n_max=10):
    """Choisit une combinaison de barres HA dont la section est >= As requis.

    `n_min` / `phi_min` permettent d'imposer les minima de coffrage et de
    façonnage (EC2 §9.2 et pratiques de chantier) : pour une poutre on impose
    au moins 3 barres et un diamètre >= 12 mm.
    """
    barres = [d for d in (6, 8, 10, 12, 14, 16, 20, 25, 32) if d >= phi_min]
    aires = {d: math.pi * (d / 10.0) ** 2 / 4.0 for d in barres}  # cm² par barre
    combis = []
    for d in barres:
        for n in range(n_min, n_max + 1):
            As = n * aires[d]
            if As >= As_req_cm2:
                combis.append((As, n, d))
    combis.sort(key=lambda t: (t[0], -t[1]))
    if not combis:
        return None
    As, n, d = combis[0]
    return dict(n=n, phi=d, As_cm2=round(As, 2),
                libelle=f"{n} HA {d}", As_req=round(As_req_cm2, 2))


def ba_effort_tranchant(b, d, Ved, fc=None, rho=0.005, sigma_cp=0.0):
    """Effort tranchant résistant d'une dalle/poutre sans armature d'âme
    (NF EN 1992-1-1 §6.2.2, équation 6.2.a)."""
    fc = FCD if fc is None else fc
    fck_ = fc * 1.5
    k = min(2.0, 1.0 + math.sqrt(200.0 / (d * 1000.0)))
    v_min = 0.035 * k ** 1.5 * math.sqrt(fck_)
    CRdc = 0.18 / 1.5
    vRdc = max(CRdc * k * (100.0 * rho * fck_) ** (1.0 / 3.0), v_min)
    VRdc = (vRdc + 0.15 * sigma_cp) * b * d * 1000.0  # kN
    return dict(k=k, vRdc=vRdc, VRdc_kN=VRdc, ok=Ved <= VRdc,
                taux=Ved / VRdc if VRdc else 99.0)


def poutre_continue_2_travees(q, L1, L2, E, I, n=1201):
    """Poutre continue à deux travées, charge répartie q, appuis simples A-B-C.

    Équation des trois moments (Clapeyron) pour M_B, puis intégration de la
    déformée (EI y'' = -M) avec annulation aux appuis. Retourne x, M, y, M_B.
    """
    import numpy as np
    MB = -(q / 8.0) * (L1 ** 3 + L2 ** 3) / (L1 + L2)
    L = L1 + L2
    x = np.linspace(0.0, L, n)
    M = np.where(x <= L1,
                 q * x * (L1 - x) / 2.0 + MB * x / L1,
                 q * (x - L1) * (L2 - (x - L1)) / 2.0 + MB * (1.0 - (x - L1) / L2))
    EI = E * I
    th = np.concatenate([[0.0],
                         np.cumsum((M[1:] + M[:-1]) / 2.0 * np.diff(x))]) / EI
    y = np.concatenate([[0.0],
                        np.cumsum((th[1:] + th[:-1]) / 2.0 * np.diff(x))])
    y = y - x * (y[-1] / L)
    return x, M, -y, MB


def etriers_poutre(b, d, Ved, theta=45.0, fywk=500.0, gamma_s=1.15):
    """Armatures d'âme d'une poutre BA (NF EN 1992-1-1 §6.2.3, modèle
    treillis à âme inclinée). Retourne l'espacement requis et le choix retenu.
    """
    fywd = fywk / gamma_s
    nu = 0.6 * (1.0 - FCD / 250.0 * 1.5 / 1.0) if FCD < 60 else 0.5
    # bras de treillis z = 0,9 d (simplifié)
    z = 0.9 * d
    cot = 1.0 / math.tan(math.radians(theta))
    # espacement pour un étrier à 2 brins HA 8
    phi = 8.0
    Asw = 2.0 * math.pi * (phi / 10.0) ** 2 / 4.0     # cm² = 2 brins HA8
    s_req = Asw * 1e-4 * z * fywd * 1e3 * cot / Ved   # m
    s_req = s_req * 1000.0                              # mm
    # espacement maximal réglementaire
    s_max = min(0.75 * d * 1000.0, 300.0)
    s = math.floor(min(s_req, s_max) / 25.0) * 25.0
    s = max(s, 75.0)
    VRds = Asw * 1e-4 * z * fywd * 1e3 * cot / (s / 1000.0)
    return dict(phi=phi, Asw_cm2=round(Asw, 2), s_req=round(s_req, 0),
                s_max=round(s_max, 0), s_retenu=s, VRds=round(VRds, 1),
                ok=VRds >= Ved, libelle=f"étriers HA {int(phi)} e = {int(s)} mm")


def ba_fleche_T_ec2(L, bw, h, hf, beff, As_cm2, g, q, Ecm=31000.0,
                    phi=2.0, d_prime=0.05, n=15.0):
    """Flèche à long terme d'une poutre en T, méthode EC2 §7.4.3.

    Section en T (table collaborante hf × beff), moment de fissuration Mcr
    calculé sur la section brute, inertie fissurée Icr par homogénéisation
    (n = 15), puis inertie effective interpolée :

        Ie = Icr / [1 - ζ (1 - Icr/Ig)],   ζ = 1 - (Mcr/Ma)²

    Flèche instantanée sur Ie, puis flèche à long terme × (1 + φ).
    """
    # --- section brute
    A1, y1 = bw * (h - hf), (h - hf) / 2.0
    A2, y2 = beff * hf, h - hf / 2.0
    A = A1 + A2
    yg = (A1 * y1 + A2 * y2) / A
    Ig = (bw * (h - hf) ** 3 / 12.0 + A1 * (y1 - yg) ** 2
          + beff * hf ** 3 / 12.0 + A2 * (y2 - yg) ** 2)
    yt = h - yg                                     # fibre tendue en bas
    Mcr = FCTM * 1000.0 * Ig / yt                   # kN·m (FCTM en MPa)

    # --- section fissurée (axe neutre depuis la fibre comprimée)
    As = As_cm2 * 1e-4
    d = h - d_prime
    a = beff / 2.0
    b_ = n * As
    c_ = -n * As * d
    x = (-b_ + math.sqrt(b_ ** 2 - 4.0 * a * c_)) / (2.0 * a)
    if x <= hf:
        Icr = beff * x ** 3 / 3.0
    else:
        Icr = (beff * hf ** 3 / 12.0 + beff * hf * (x - hf / 2.0) ** 2
               + bw * (x - hf) ** 3 / 3.0)
    Icr += n * As * (d - x) ** 2

    # --- inertie effective
    w = g + psi0() * q                              # kN/m
    Ma = w * L ** 2 / 8.0
    zeta = 0.0 if Ma <= Mcr else max(0.0, 1.0 - (Mcr / Ma) ** 2)
    Ie = Icr / (1.0 - zeta * (1.0 - Icr / Ig))

    f_inst = 5.0 * w * L ** 4 / (384.0 * Ecm * 1e3 * Ie)
    f_lt = f_inst * (1.0 + phi)
    return dict(Ig=Ig, Icr=Icr, Ie=Ie, Mcr=Mcr, Ma=Ma, zeta=zeta,
                x_neutre=x, f_inst_mm=f_inst * 1000.0,
                f_lt_mm=f_lt * 1000.0, w=w)


def ba_vrdmax(bw, d, fck=FCK, fcd=FCD, theta=45.0, alpha_cw=1.0):
    """Effort tranchant résistant maximal (bielles), EC2 §6.2.3 (6.9)."""
    nu1 = 0.6 * (1.0 - fck / 250.0)
    cot = 1.0 / math.tan(math.radians(theta))
    return (alpha_cw * bw * 0.9 * d * nu1 * fcd * 1000.0
            / (cot + math.tan(math.radians(theta))) / 1e0)


def ba_fleche_poutre(L, b, h, g, q, Ecm=31000.0, nu=0.2, fluage=True):
    """Flèche à long terme d'une poutre isostatique simplement appuyée,
    charge répartie (méthode simplifiée EC2 §7.4.3, section fissurée forfaitaire
    Ie = 0,5·Ig en l'absence de calcul plus fin)."""
    Ig = b * h ** 3 / 12.0                       # m4
    Ie = 0.5 * Ig                                # section fissurée forfaitaire
    phi = 2.0 if fluage else 0.0
    # flèche instantanée charges permanentes + quasi-permanentes
    w_g = g                                          # kN/m
    w_q = psi0() * q                                 # kN/m
    f_inst = 5.0 * (w_g + w_q) * L ** 4 / (384.0 * Ecm * 1e3 * Ie)
    f_lt = f_inst * (1.0 + phi)
    f_lim_ratio = L / FLECHE_RATIO
    f_lim = min(f_lim_ratio, FLECHE_ABS / 1000.0)
    return dict(Ig=Ig, Ie=Ie, f_inst_mm=f_inst * 1000.0,
                f_lt_mm=f_lt * 1000.0, f_lim_mm=f_lim * 1000.0,
                ok=f_lt <= f_lim, critere=f"L/{int(FLECHE_RATIO)} et 5 mm")


# ---------------------------------------------------------------------------
# 4. ACIER — vérifications de profilés (NF EN 1993-1-1)
# ---------------------------------------------------------------------------

def acier_flexion(profile, Med, L, gamma=GAMMA_M0, classe=1, E=210000.0,
                  charge="repartie", G_total=None):
    """Vérifie un profilé en flexion simple : résistance, cisaillement, flèche.

    Med en kN·m, L en m. `charge` = 'repartie' ou 'ponctuelle_centre'.
    """
    p = profile
    Wply = p["Wply"] * 1e3        # mm³
    Wely = p["Wely"] * 1e3
    fy = p["fy"]
    MRd = Wply * fy / gamma / 1e6 if classe <= 2 else Wely * fy / gamma / 1e6
    eta_M = Med / MRd
    # cisaillement
    Av = p["A"] * 100.0 - 2 * p["b"] * p["tf"] + (p["tw"] + 2 * p["r"]) * p["tf"]
    Vpl = Av * (fy / math.sqrt(3)) / gamma / 1e3
    # flèche (charge totale à l'ELS, non pondérée)
    Iy = p["Iy"] * 1e4            # mm4
    G = G_total if G_total is not None else Med * 1.35
    if charge == "repartie":
        f = 5.0 * G * L ** 4 / (384.0 * E * Iy) * 1e12 / 1e3
    else:
        f = G * L ** 3 / (48.0 * E * Iy) * 1e12 / 1e3
    f_lim = min(L * 1000.0 / FLECHE_RATIO, FLECHE_ABS)
    return dict(nom=profile.get("nom", ""), MRd=MRd, eta_M=eta_M,
                Vpl=Vpl, Iy=Iy, fleche=f, f_lim=f_lim, ok_fleche=f <= f_lim,
                ok_MPa=eta_M <= 1.0)


def selectionne_profiles(Med, L, Veff, catalogue, charge="repartie", marge=0.90):
    """Retourne le premier profilé (par ordre croissant de poids) qui satisfait
    simultanément la flexion, le cisaillement et la flèche, en conservant une
    marge de sécurité `marge` sur le taux de travail en flexion."""
    candidats = []
    for nom, p in catalogue.items():
        p = dict(p)
        p["nom"] = nom
        r = acier_flexion(p, Med, L, charge=charge)
        if r["eta_M"] <= marge and Veff <= r["Vpl"] and r["ok_fleche"]:
            candidats.append((p["A"], nom, p, r))
    candidats.sort(key=lambda t: t[0])
    if not candidats:
        return None
    A, nom, p, r = candidats[0]
    return dict(nom=nom, A_cm2=A, **{k: v for k, v in r.items() if k != "nom"})


# ---------------------------------------------------------------------------
# 5. FONDATIONS — capacité portante et semelles (NF P94-261, EC7)
# ---------------------------------------------------------------------------

def semelle_filante(N_els, N_elu, b_mur, q_els=Q_ELS, q_elu=Q_ELU, gamma_b=25.0,
                    h_min=0.20):
    """Dimensionne une semelle filante sous un mur porteur.

    N en kN/ml. Retourne largeur, hauteur utile, contraintes et ratio.
    """
    B_els = N_els / (q_els * 1000.0)        # q en MPa -> kN/m² ×1000
    B_elu = N_elu / (q_elu * 1000.0)
    B = max(B_els, B_elu, b_mur + 0.10)
    # arrondi au multiple de 5 cm supérieur
    B = math.ceil(B / 0.05) * 0.05
    # hauteur : diffusion à 45° depuis le nu du mur (DTU 13.1)
    d = max(h_min, (B - b_mur) / 4.0)
    # poids propre de la semelle et du remblai
    h_sem = d + 0.05
    g_sem = B * h_sem * gamma_b
    N_tot_els = N_els + g_sem
    sigma_els = N_tot_els / (B * 1000.0)     # MPa
    sigma_elu = N_elu / (B * 1000.0)
    return dict(B=round(B, 2), B_els=round(B_els, 2), B_elu=round(B_elu, 2),
                d=round(d, 2), h=round(h_sem, 2),
                sigma_els=sigma_els, sigma_elu=sigma_elu,
                ok_els=sigma_els <= q_els, ok_elu=sigma_elu <= q_elu)


def puits_gros_beton(N_els, N_elu, profondeur, d0=0.60,
                     q_els=Q_ELS, q_elu=Q_ELU, gamma_b=22.0):
    """Puits de fondation en gros béton (NF P94-261 §9.2, EC7 §7.6).

    N en kN (valeur à la base du puits, hors poids propre du gros béton).
    `profondeur` = hauteur de gros béton entre l'assise et le niveau de
    fondation de l'ouvrage (m).

    La portance est vérifiée à la base sur les contraintes imposées q_ELS et
    q_ELU. Le diamètre est itéré : le poids propre du gros béton dépend du
    diamètre retenu, il ne peut donc pas être négligé dans la fermeture.
    """
    D = max(d0, math.sqrt(N_els / (q_els * 1000.0) * 4.0 / math.pi))
    for _ in range(40):
        D = math.ceil(D / 0.05) * 0.05
        A = math.pi * D ** 2 / 4.0
        W = A * profondeur * gamma_b
        s_els = (N_els + W) / (A * 1000.0)
        s_elu = (N_elu + 1.35 * W) / (A * 1000.0)
        if s_els <= q_els and s_elu <= q_elu:
            break
        D += 0.05
    return dict(D=round(D, 2), profondeur=round(profondeur, 2),
                A=round(A, 3), W_kN=round(W, 1),
                sigma_els=round(s_els, 4), sigma_elu=round(s_elu, 4),
                ok_els=s_els <= q_els, ok_elu=s_elu <= q_elu,
                taux_els=round(s_els / q_els, 2), taux_elu=round(s_elu / q_elu, 2))


def poussee_terres(H, gamma=GAMMA_SOL, phi=PHI_SOL, surcharge=0.0):
    """Poussée des terres au repos (Jaky) et active (Rankine) sur un soutènement.

    Retourne les efforts horizontaux en kN/ml pour une hauteur H (m).
    """
    Ka = math.tan(math.radians(45.0 - phi / 2.0)) ** 2
    K0 = 1.0 - math.sin(math.radians(phi))
    pa = 0.5 * Ka * gamma * H ** 2 + Ka * surcharge * H
    p0 = 0.5 * K0 * gamma * H ** 2 + K0 * surcharge * H
    M_a = (Ka * gamma * H ** 3 / 6.0) + (Ka * surcharge * H ** 2 / 2.0)
    M_0 = (K0 * gamma * H ** 3 / 6.0) + (K0 * surcharge * H ** 2 / 2.0)
    return dict(Ka=round(Ka, 3), K0=round(K0, 3), H=round(H, 2),
                pa_kN=round(pa, 1), p0_kN=round(p0, 1),
                M_a=round(M_a, 2), M_0=round(M_0, 2),
                pa_kNm=round(pa / (H / 3.0), 1) if H else 0.0)


# ---------------------------------------------------------------------------
# 6. CHAPITRE 1 — EXTENSION (poutre retroussée, poteau, voile, dalle, puits)
# ---------------------------------------------------------------------------

def chapitre_extension():
    R = {}

    # --- 6.1 Descente de charges de la toiture-terrasse accessible --------
    e_dalle = 0.20
    g_dalle = e_dalle * GAMMA_BA
    g_revet = 1.20        # forme de pente + étanchéité + protection
    g1 = G1_CLOISON
    G = g_dalle + g_revet + g1
    Q = Q_CAT_A
    R["dalle"] = dict(
        epaisseur=e_dalle, g_dalle=g_dalle, g_revet=g_revet, g1=g1,
        G=G, Q=Q,
        p_elu=1.35 * G + 1.50 * Q,
        p_els=G + Q,
        p_els_qp=G + psi0() * Q,
    )

    # --- 6.2 Poutre-acrotère retroussée ---------------------------------
    # Géométrie confirmée par le maître d'ouvrage le 11/11/2026 :
    #   - la poutre fait en même temps office d'acrotère de la terrasse ;
    #   - son arase supérieure est à NGF 44,75 (NGF_ACROTERE) ;
    #   - elle s'appuie sur le mur mitoyen (voile BA) et sur le poteau BA
    #     25 x 25, repositionné à ~2,00 m du nu de la façade.
    # Le poteau à 2,00 m est l'APPUI D'EXTRÉMITÉ côté façade : la poutre est
    # une travée unique de 8,03 m, et non une poutre continue sur 3 appuis.
    L_total = NIV.L_EXTENSION                      # 8,03 m
    # Largeur d'âme portée de 25 à 30 cm : la hauteur est bloquée par
    # l'arase d'acrotère (44,75) et la sous-face du plancher haut RDC
    # (44,08), soit h = 0,67 m. Seule la largeur reste ajustable ; elle
    # améliore la raideur et surtout l'enrobage des 4 HA 16 en une nappe.
    b_p = 0.30
    h_p = NIV.NGF_POUTRE_HAUT - NIV.NGF_POUTRE_BAS # 44,75 - 44,08 = 0,67 m
    e_d = e_dalle                                  # 0,20 m : table collaborante
    beff = min(L_total / 5.0, b_p + 4.0 * e_d)     # EC2 §5.3.2.1 : 0,85 m
    # Poids propre de la poutre : âme seule. La table collaborante (20 cm)
    # est déjà comptée dans la descente de charges de la dalle.
    g_p = b_p * (h_p - e_d) * GAMMA_BA
    # Largeur de dalle reprise par la poutre, la poutre étant à 2,00 m du nu
    # de façade : demi-travée côté façade (2,00/2 = 1,00 m) + console côté
    # verrière (1,20 m), soit 2,20 m de bande chargée.
    largeur_reprise = (NIV.POS_POTEAU_FAÇADE / 2.0
                       + (3.20 - NIV.POS_POTEAU_FAÇADE))

    p_elu = R["dalle"]["p_elu"]
    p_els_qp = R["dalle"]["p_els_qp"]
    q_elu = p_elu * largeur_reprise + 1.35 * g_p
    q_els = p_els_qp * largeur_reprise + g_p

    M = q_elu * L_total ** 2 / 8.0
    V = q_elu * L_total / 2.0
    flex = ba_flexion(b_p, h_p, M)
    # 4 barres au maximum par nappe : coffrage de 25 cm de large
    arm = choix_ferraillage(flex["As_cm2"], n_min=4, n_max=4, phi_min=12)
    etr = etriers_poutre(b_p, flex["d"], V)
    VRdmax = ba_vrdmax(b_p, flex["d"])
    fl = ba_fleche_T_ec2(L_total, b_p, h_p, e_d, beff,
                         arm["As_cm2"], q_els, 0.0)
    fleche = fl["f_lt_mm"]
    lim_500 = L_total * 1000.0 / 500.0
    lim_250 = L_total * 1000.0 / 250.0

    R["poutre"] = dict(
        L=L_total, b=b_p, h=round(h_p, 2), e_d=e_d, beff=round(beff, 2),
        g_p=round(g_p, 2), q_elu=round(q_elu, 1), q_els=round(q_els, 1),
        M=round(M, 1), V=round(V, 1), mu=round(flex["mu"], 4),
        z=round(flex["z"], 3), As=round(flex["As_cm2"], 2), armature=arm,
        VRdc=round(etr_conv := etr["VRds"], 1), VRdmax=round(VRdmax, 1),
        ok_bielle=V <= VRdmax, etriers=etr, ok_tranchant=etr["ok"],
        Ig=round(fl["Ig"], 5), Icr=round(fl["Icr"], 5),
        Ie=round(fl["Ie"], 5), Mcr=round(fl["Mcr"], 1), zeta=round(fl["zeta"], 3),
        fleche_inst=round(fl["f_inst_mm"], 2),
        fleche=round(fleche, 2), ratio=round(L_total * 1000.0 / fleche, 0),
        fleche_lim_500=round(lim_500, 1), fleche_lim_250=round(lim_250, 1),
        ok_500=fleche <= lim_500, ok_250=fleche <= lim_250,
        # Contre-flèche de coffrage : compense la part de flèche à long terme
        # et ramène la flèche résiduelle sous le critère L/500 vis-à-vis de
        # la verrière supportée en façade.
        contre_fleche=20.0,
        fleche_residuelle=round(max(0.0, fleche - 20.0), 2),
        ngf_bas=NIV.NGF_POUTRE_BAS, ngf_haut=NIV.NGF_POUTRE_HAUT,
    )

    # --- 6.3 Poteau BA 25 × 25 sous la poutre ---------------------------
    # Le poteau reprend la totalité de la réaction d'appui de la poutre,
    # soit q_elu * L / 2 (travée unique, deux appuis).
    N_elu = q_elu * L_total / 2.0 + 1.35 * 0.25 * 0.25 * 3.20 * GAMMA_BA
    N_els = q_els * L_total / 2.0 + 0.25 * 0.25 * 3.20 * GAMMA_BA
    b_c, h_c = 0.25, 0.25          # section imposee par l'architecte
    A_c = b_c * h_c
    l0 = 3.20
    i = b_c / math.sqrt(12.0)
    lam = l0 / i
    lam_lim = 20.0 * 0.7 * 1.0 * 1.0 / math.sqrt(0.85)   # simplifié AN
    NRd_0 = A_c * FCD * 1000.0                            # kN, section seule
    alpha_fl = 0.75 if lam <= 40 else 0.65
    NRd = alpha_fl * NRd_0
    As_min = max(0.10 * N_elu / (FYD * 1000.0), 0.002 * A_c) * 1e4  # cm²
    As_max = 0.04 * A_c * 1e4
    R["poteau"] = dict(
        b=b_c, h=h_c, l0=l0, i=round(i, 4), lambda_=round(lam, 1),
        lambda_lim=round(lam_lim, 1),
        N_elu=round(N_elu, 1), N_els=round(N_els, 1), NRd=round(NRd, 1),
        taux=round(N_elu / NRd, 3), ok=N_elu <= NRd,
        As_min=round(As_min, 2), As_max=round(As_max, 2),
        armature=choix_ferraillage(max(As_min, 3.0)),
    )

    # --- 6.3 Poteau BA 25 × 25 sous la poutre ---------------------------
    # Le poteau reprend la totalité de la réaction d'appui de la poutre,
    # soit q_elu * L / 2 (une seule travée, deux appuis).
    N_elu = q_elu * L_total / 2.0 + 1.35 * 0.25 * 0.25 * 3.20 * GAMMA_BA
    N_els = q_els * L_total / 2.0 + 0.25 * 0.25 * 3.20 * GAMMA_BA
    b_c, h_c = 0.25, 0.25          # section imposee par l'architecte
    A_c = b_c * h_c
    # élancement
    l0 = 3.20
    i = b_c / math.sqrt(12.0)
    lam = l0 / i
    lam_lim = 20.0 * 0.7 * 1.0 * 1.0 / math.sqrt(0.85)   # simplifié AN
    NRd_0 = A_c * FCD * 1000.0                            # kN, section seule
    # méthode simplifiée : N_Rd = alpha × A_c × fcd
    alpha_fl = 0.75 if lam <= 40 else 0.65
    NRd = alpha_fl * NRd_0
    As_min = max(0.10 * N_elu / (FYD * 1000.0), 0.002 * A_c) * 1e4  # cm²
    As_max = 0.04 * A_c * 1e4
    R["poteau"] = dict(
        b=b_c, h=h_c, l0=l0, i=round(i, 4), lambda_=round(lam, 1),
        lambda_lim=round(lam_lim, 1),
        N_elu=round(N_elu, 1), N_els=round(N_els, 1), NRd=round(NRd, 1),
        taux=round(N_elu / NRd, 3), ok=N_elu <= NRd,
        As_min=round(As_min, 2), As_max=round(As_max, 2),
        armature=choix_ferraillage(max(As_min, 3.0)),
    )

    # --- 6.4 Voile BA mitoyen ép. 20 cm ---------------------------------
    # Le voile est encastré en pied dans le puits n° 2 et en tête dans la
    # dalle de terrasse. Il est sollicité par la poussée du remblai côté
    # voisin sur la hauteur enterrée (NGF 39,02 assise -> 41,46 sol fini).
    #
    # Vérification menée en « bande verticale encastrée en pied, articulée
    # en tête » (schéma de Rankine), qui est le cas défavorable vis-à-vis du
    # moment d'encastrement en pied.
    H_enterre = 2.44
    poussee = poussee_terres(H_enterre, surcharge=5.0)
    M_base = poussee["M_0"]            # poussée au repos : plus défavorable
    flex_v = ba_flexion(1.00, 0.20, M_base, d_prime=0.03)
    As_mini = 0.0013 * 1.00 * 0.20 * 1e4          # EC2 §9.6.2, par face
    As_retenu = max(flex_v["As_cm2"], As_mini)
    # effort tranchant à la base
    V_base = poussee["p0_kN"]
    tran_v = ba_effort_tranchant(1.00, 0.17, V_base)
    R["voile"] = dict(
        ep=0.20, H=5.28, H_enterre=H_enterre,
        Ka=poussee["Ka"], K0=poussee["K0"],
        pa=round(poussee["pa_kN"], 1), p0=round(poussee["p0_kN"], 1),
        M=round(M_base, 2), mu=round(flex_v["mu"], 4),
        As_requis=round(flex_v["As_cm2"], 2), As_mini=round(As_mini, 2),
        As_retenu=round(As_retenu, 2),
        armature=choix_ferraillage(As_retenu, n_min=4, phi_min=10),
        As_repartition=round(0.0013 * 1.00 * 0.20 * 1e4, 2),
        V_base=round(V_base, 1), VRdc=round(tran_v["VRdc_kN"], 1),
        ok_tranchant=tran_v["ok"],
    )

    # --- 6.5 Dalle terrasse — vérification en flexion -------------------
    # La dalle s'étend de la façade existante (NGF 44,08) à la verrière.
    # La poutre-acrotère la reprend à 2,00 m du nu de façade : travée de
    # 2,00 m entre façade et poutre, puis console de 1,20 m jusqu'à la
    # verrière (3,20 - 2,00). C'est la console qui est dimensionnante.
    L_dalle = NIV.POS_POTEAU_FAÇADE               # 2,00 m
    L_console = 3.20 - NIV.POS_POTEAU_FAÇADE      # 1,20 m
    M_travee = R["dalle"]["p_elu"] * L_dalle ** 2 / 8.0
    M_console = R["dalle"]["p_elu"] * L_console ** 2 / 2.0
    M_dalle = max(M_travee, M_console)
    flex_d = ba_flexion(1.00, e_dalle, M_dalle, d_prime=0.03)
    tran_d = ba_effort_tranchant(1.00, flex_d["d"],
                                 R["dalle"]["p_elu"] * (L_dalle / 2.0 + L_console))
    f_d = ba_fleche_poutre(L_dalle, 1.00, e_dalle, R["dalle"]["p_els_qp"], 0.0)
    R["dalle_verif"] = dict(
        L=L_dalle, L_console=L_console, M_travee=round(M_travee, 1),
        M_console=round(M_console, 1), M=round(M_dalle, 1), mu=round(flex_d["mu"], 4),
        As=round(flex_d["As_cm2"], 2),
        armature=choix_ferraillage(flex_d["As_cm2"], n_min=4, phi_min=10),
        VRdc=round(tran_d["VRdc_kN"], 1), ok_tranchant=tran_d["ok"],
        fleche=round(f_d["f_lt_mm"], 2), fleche_lim=round(f_d["f_lim_mm"], 2),
        ok_fleche=f_d["ok"],
    )

    # --- 6.6 Puits de fondation ----------------------------------------
    # Réaction du poteau + poids du voile reporté sur le puits n° 1
    N_puits1_els = N_els + 0.20 * 3.20 * 2.40 * GAMMA_BA * 1.5   # voile reporté
    N_puits1_elu = N_elu * 1.10
    R["puits_1"] = puits_gros_beton(N_puits1_els, N_puits1_elu, profondeur=2.40)
    # Puits n° 2 sous le voile mitoyen : charge répartie du voile
    N_puits2_els = 0.20 * 5.30 * 3.20 * GAMMA_BA + q_els * 4.00
    R["puits_2"] = puits_gros_beton(N_puits2_els, N_puits2_els * 1.35, profondeur=2.40)

    # --- 6.7 Joint de dilatation 20 mm ---------------------------------
    L_bat = 8.03
    alpha_th = 10e-6          # /°C
    delta_T = 20.0            # °C
    deplacement = alpha_th * delta_T * L_bat * 1000.0   # mm
    R["joint"] = dict(largeur=20.0, L=L_bat, dT=delta_T,
                      deplacement_mm=round(deplacement, 2),
                      ok=deplacement < 20.0 * 0.80,
                      marge_pct=round((20.0 - deplacement) / 20.0 * 100.0, 1))

    # --- 6.8 Longrine de répartition sous D1 ---------------------------
    # Charge du mur au-dessus de D1 (refend 16 cm, 2 niveaux)
    h_mur = 5.68
    g_mur = 0.16 * 19.6 * h_mur
    N_lin_els = g_mur + 3.0 * 1.00 + 1.5 * 1.00
    N_lin_elu = 1.35 * (g_mur + 3.0) + 1.5 * 1.5
    R["longrine_D1"] = semelle_filante(N_lin_els, N_lin_elu, b_mur=0.16)
    R["longrine_D1"]["g_mur"] = round(g_mur, 1)
    R["longrine_D1"]["N_els"] = round(N_lin_els, 1)
    R["longrine_D1"]["N_elu"] = round(N_lin_elu, 1)

    return R


# ---------------------------------------------------------------------------
# 7. CHAPITRE 2 — REPRISES EN SOUS-OEUVRE D1 A D6
# ---------------------------------------------------------------------------

MURS = [
    # rep, libelle, L (m), ep (m), hauteur reprise (m), nb_niveaux au-dessus,
    # nature, appuis
    ("D1", "Refend entrée / bureau",              2.60, 0.16, 2.62, 2, "cloison porteuse", "2"),
    ("D2", "Façade avant — salon",                3.80, 0.47, 2.15, 2, "mur de façade meulière", "2"),
    ("D3", "Refend central longitudinal",         3.55, 0.57, 2.40, 2, "mur porteur meulière", "2"),
    ("D4", "Façade avant — salle à manger",       2.00, 0.49, 2.15, 2, "mur de façade meulière", "2"),
    ("D5", "Refend transversal salle à manger",   3.08, 0.16, 2.40, 2, "cloison porteuse", "2"),
    ("D6", "Façade arrière — cuisine",            1.54, 0.46, 2.15, 2, "mur de façade meulière", "2"),
]

NIVEAUX_HAUTEUR = 2.86   # hauteur d'étage RDC


def chapitre_rso(acier="S355"):
    """Dimensionnement des profilés de reprise en sous-œuvre D1 à D6."""
    mat = S355 if acier == "S355" else S275
    cat = {k: dict(v) for k, v in PROFILES.items()}
    cat_j = {k: dict(v) for k, v in JUMELES.items()}
    for d in (cat, cat_j):
        for p in d.values():
            p["fy"] = mat["fy"]

    res = []
    for rep, lib, L, ep, h_libre, nb_niv, nature, appuis in MURS:
        # hauteur de maçonnerie reprise par le profilé : 2 niveaux au-dessus
        h_mur_reprise = NIVEAUX_HAUTEUR * nb_niv
        g_mur = ep * 19.6 * h_mur_reprise           # kN/m
        # planchers : bande de 1,00 m de part et d'autre
        g_plancher = (G0_PH * nb_niv) * 1.00
        q_plancher = Q_CAT_A * 1.00 * (nb_niv - 0.0)
        # pondération ELU : 1,35 G + 1,50 Q
        q_elu = 1.35 * (g_mur + g_plancher) + 1.50 * q_plancher
        q_els = g_mur + g_plancher + psi0() * q_plancher

        M = q_elu * L ** 2 / 8.0
        V = q_elu * L / 2.0

        choix = (selectionne_profiles(M, L, V, cat, charge="repartie")
                 or selectionne_profiles(M, L, V, cat_j, charge="repartie"))
        res.append(dict(
            rep=rep, libelle=lib, L=L, ep=ep, h_libre=h_libre,
            h_mur_reprise=round(h_mur_reprise, 2),
            g_mur=round(g_mur, 1), g_plancher=round(g_plancher, 1),
            q_plancher=round(q_plancher, 1),
            q_elu=round(q_elu, 1), q_els=round(q_els, 1),
            M=round(M, 1), V=round(V, 1),
            profil=choix["nom"] if choix else "à définir",
            A_cm2=choix["A_cm2"] if choix else 0.0,
            MRd=round(choix["MRd"], 1) if choix else 0.0,
            taux_M=round(choix["eta_M"], 3) if choix else 99.0,
            fleche=round(choix["fleche"], 2) if choix else 999.0,
            fleche_lim=round(choix["f_lim"], 2) if choix else 0.0,
            poids=round(choix["A_cm2"] * 78.5 / 100.0, 1) if choix else 0.0,
        ))
    return dict(acier=acier, fy=mat["fy"], murs=res)


# ---------------------------------------------------------------------------
# 8. CHAPITRE 3 — APPUIS BA ET FONDATIONS
# ---------------------------------------------------------------------------

def chapitre_ba():
    R = {}
    # --- 8.1 Jambages BA des baies D2, D4, D6 (façade) -------------------
    jambages = []
    for rep, N_elu, N_els, b, h in [
        ("D2 (3,80 m)", 210.0, 155.0, 0.25, 0.50),
        ("D4 (2,00 m)", 118.0, 87.0, 0.25, 0.50),
        ("D6 (1,54 m)", 92.0, 68.0, 0.25, 0.45),
    ]:
        f = ba_flexion(b, h, N_elu * 0.05)     # excentrement 5 %
        As = max(0.002 * b * h * 1e4, f["As_cm2"])
        jambages.append(dict(rep=rep, N_elu=N_elu, N_els=N_els, b=b, h=h,
                             sigma=round(N_elu / (b * h) / 1000.0, 2),
                             As=round(As, 2),
                             armature=choix_ferraillage(max(As, 4.0), n_min=4,
                                                        phi_min=10)))
    R["jambages"] = jambages

    # --- 8.2 Poteau BA au croisement D3 / D5 ----------------------------
    # Reprend l'about du refend conservé + les deux profilés en appui
    N_elu = 285.0
    N_els = 205.0
    b, h = 0.25, 0.40
    l0 = 2.40
    i = min(b, h) / math.sqrt(12.0)
    lam = l0 / i
    NRd = 0.75 * b * h * FCD * 1000.0
    As = max(0.10 * N_elu / (FYD * 1000.0) * 1e4, 0.002 * b * h * 1e4)
    R["poteau_D3D5"] = dict(
        b=b, h=h, l0=l0, lambda_=round(lam, 1), N_elu=N_elu, N_els=N_els,
        NRd=round(NRd, 1), taux=round(N_elu / NRd, 3),
        As_min=round(As, 2), armature=choix_ferraillage(max(As, 4.0)),
        sigma=round(N_elu / (b * h) / 1000.0, 2),
        ancrage=0.50,
    )

    # --- 8.3 Sommiers BA en tête de baie --------------------------------
    # Le sommier est un chaînage horizontal armé qui reprend les charges
    # apportées par les jambages et répartit les efforts dans la maçonnerie
    # conservée au-dessus de la baie. Il travaille en traction/flexion
    # légère : le ferraillage est donc dicté par les minima de chaînage
    # (EC2 §9.2 / DTU 20.1) et non par la flexion.
    sommiers = []
    for rep, L, q_elu in [("D2", 3.80, 22.0), ("D4", 2.00, 18.0), ("D6", 1.54, 16.0)]:
        M = q_elu * L ** 2 / 8.0
        f = ba_flexion(0.25, 0.40, M)
        As_coffrage = max(f["As_cm2"], 2.0)      # 4 HA 10 mini en chaînage
        sommiers.append(dict(rep=rep, L=L, q=q_elu, M=round(M, 1),
                             As=round(As_coffrage, 2),
                             armature=choix_ferraillage(As_coffrage, n_min=4,
                                                        phi_min=10)))
    R["sommiers"] = sommiers

    # --- 8.4 Fondations existantes : vérification de la contrainte ------
    # Les murs de façade et le refend central reposent sur des fondations
    # filantes continues en meulière (hypothèse H-01 levée : meulière
    # continue). La largeur d'assise est estimée à b_mur + 2 x 0,15 m.
    #
    # Les charges sont issues du chapitre 2 (mêmes descentes de charges),
    # de sorte que les deux chapitres soient cohérents entre eux.
    # N en kN/ml, B en m -> sigma en kPa, converti ensuite en MPa.
    rso = chapitre_rso("S355")
    par_rep = {m["rep"]: m for m in rso["murs"]}
    fondations = []
    for rep, b_mur in [("D2", 0.47), ("D3", 0.57), ("D4", 0.49), ("D6", 0.46)]:
        m = par_rep[rep]
        # charge du mur seule (les planchers sont repris par les refends)
        N_els = m["g_mur"] * 1.0
        N_elu = 1.35 * m["g_mur"]
        B_exist = b_mur + 0.30
        g_sem = B_exist * 0.30 * 22.0           # semelle meulière 30 cm
        sigma_els_kPa = (N_els + g_sem) / (B_exist * 1.0)
        sigma_elu_kPa = (N_elu + 1.35 * g_sem) / (B_exist * 1.0)
        B_req = (N_els + g_sem) / (Q_ELS * 1000.0)
        # concentration locale sur un jambage : la charge de la baie se
        # reporte sur les deux jambages, soit 2 x la charge linéique
        sigma_jambage = 2.0 * sigma_els_kPa / 1000.0
        fondations.append(dict(
            rep=rep, b_mur=b_mur, B_exist=round(B_exist, 2),
            N_els=round(N_els, 1), N_elu=round(N_elu, 1),
            g_sem=round(g_sem, 1),
            sigma_els_kPa=round(sigma_els_kPa, 1),
            sigma_elu_kPa=round(sigma_elu_kPa, 1),
            sigma_els=round(sigma_els_kPa / 1000.0, 3),
            sigma_elu=round(sigma_elu_kPa / 1000.0, 3),
            sigma_jambage=round(sigma_jambage, 3),
            ok_els=sigma_els_kPa / 1000.0 <= Q_ELS,
            ok_elu=sigma_elu_kPa / 1000.0 <= Q_ELU,
            ok_jambage=sigma_jambage <= Q_ELS,
            B_requis_els=round(B_req, 2),
            besoin_elargissement=B_req > B_exist,
            elargissement=round(max(0.0, B_req - B_exist), 2),
        ))
    R["fondations"] = fondations

    # --- 8.5 Longrine de répartition sous D1 ----------------------------
    R["longrine"] = semelle_filante(22.5, 30.2, b_mur=0.16)

    # --- 8.6 Répartition sous jambages ----------------------------------
    # La concentration de charge sous un jambage (2 x la charge linéique du
    # mur) dépasse la capacité de la fondation existante. Une longrine de
    # répartition BA ancrée dans la semelle existante ramène la contrainte
    # sous q_ELS. Largeur retenue : 1,30 m (limite de mitoyenneté 1,50 m).
    repart = []
    for f in R["fondations"]:
        B_new = 1.30
        sigma_new = f["sigma_els_kPa"] * (f["B_exist"] / B_new)
        repart.append(dict(rep=f["rep"], B_new=B_new,
                           sigma_avant=f["sigma_els_kPa"],
                           sigma_apres=round(sigma_new, 1),
                           ok=sigma_new / 1000.0 <= Q_ELS,
                           epaisseur=0.25,
                           As=choix_ferraillage(0.0013 * 1.30 * 0.25 * 1e4 * 2,
                                                n_min=6, phi_min=10)))
    R["repartition_jambages"] = repart
    return R


# ---------------------------------------------------------------------------
# 9. CHAPITRE 4 — AVANT-METRE
# ---------------------------------------------------------------------------

def chapitre_metre():
    M = {}
    murs_ba = [
        ("Jambages D2", 2 * 2, 0.25, 0.50, 2.15),
        ("Jambages D4", 2 * 2, 0.25, 0.50, 2.15),
        ("Jambages D6", 2 * 2, 0.25, 0.45, 2.15),
        ("Poteau D3/D5", 1, 0.25, 0.40, 2.40),
        ("Poteau verrière", 1, 0.25, 0.25, 3.20),
        ("Voile mitoyen", 1, 0.20, 3.20, 5.28),
        ("Sommiers BA", 3, 0.25, 0.40, 0.0),
        ("Longrines de répartition (jambages)", 4, 1.30, 0.25, 4.00),
        ("Poutre-acrotère retroussée", 1, 0.30, 0.67, 8.03),
        ("Dalle terrasse 20 cm", 1, 8.03, 3.20, 0.20),
    ]
    total_ba = 0.0
    lignes = []
    for lib, n, b, h, L in murs_ba:
        if lib.startswith("Dalle"):
            V = n * b * h * L          # b x h = surface, L = épaisseur
        elif L > 0:
            V = n * b * h * L
        else:
            V = n * b * h * 3.0        # longueur forfaitaire pour les sommiers
        total_ba += V
        lignes.append(dict(lib=lib, n=n, b=b, h=h, L=L, V=round(V, 3)))
    M["beton"] = lignes
    M["beton_total"] = round(total_ba, 2)

    # aciers HA : ratio moyen 120 kg/m³
    M["acier_kg"] = round(total_ba * 120.0, 0)
    M["acier_t"] = round(total_ba * 120.0 / 1000.0, 2)

    # profilés métalliques
    rso = chapitre_rso()
    poids_profiles = sum(m["poids"] * m["L"] for m in rso["murs"])
    M["profiles_kg"] = round(poids_profiles, 0)
    M["profiles_t"] = round(poids_profiles / 1000.0, 2)
    M["profiles_detail"] = [(m["rep"], m["profil"], m["poids"], m["L"]) for m in rso["murs"]]

    # terrassement des puits
    R = chapitre_extension()
    D1, D2 = R["puits_1"]["D"], R["puits_2"]["D"]
    prof = R["puits_1"]["profondeur"]
    M["terrassement_puits"] = round(math.pi / 4 * (D1 ** 2 + D2 ** 2) * prof, 2)
    M["beton_puits"] = round(math.pi / 4 * (D1 ** 2 + D2 ** 2) * prof, 2)

    # dalle de terrasse
    M["dalle_terrasse"] = round(8.03 * 3.20 * 0.20, 2)

    # étaiement
    M["etais"] = 48
    return M


# ---------------------------------------------------------------------------
# 10. SYNTHESE ET EXPORT
# ---------------------------------------------------------------------------

def run():
    res = dict(
        hypothese=dict(fcd=round(FCD, 2), fyd=round(FYD, 1), fctd=round(FCTD, 2),
                       q_els=Q_ELS, q_elu=Q_ELU, gamma_ba=GAMMA_BA),
        extension=chapitre_extension(),
        rso_S355=chapitre_rso("S355"),
        rso_S275=chapitre_rso("S275"),
        ba=chapitre_ba(),
        metre=chapitre_metre(),
    )
    return res


if __name__ == "__main__":
    res = run()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "calculs_resultats.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    print("Résultats :", out)
    print("\n--- SYNTHESE RSO (S355) ---")
    print(f"{'Rep':4s} {'L(m)':>5s} {'q_elu':>7s} {'M':>7s} {'V':>6s} "
          f"{'Profilé':16s} {'taux':>6s} {'flèche':>7s} {'lim':>6s}")
    for m in res["rso_S355"]["murs"]:
        print(f"{m['rep']:4s} {m['L']:5.2f} {m['q_elu']:7.1f} {m['M']:7.1f} "
              f"{m['V']:6.1f} {m['profil']:16s} {m['taux_M']:6.3f} "
              f"{m['fleche']:7.2f} {m['fleche_lim']:6.2f}")
    print("\n--- POUTRE-ACROTERE RETROUSSEE (travée 8,03 m) ---")
    p_ = res["extension"]["poutre"]
    print(f"  section {p_['b']*100:.0f} x {p_['h']*100:.0f} cm, beff {p_['beff']:.2f} m")
    print(f"  q_ELU {p_['q_elu']:.1f} kN/m — M {p_['M']:.1f} kN·m — V {p_['V']:.1f} kN")
    print(f"  A_s {p_['As']:.2f} cm² -> {p_['armature']['libelle']} ; "
          f"{p_['etriers']['libelle']}")
    print(f"  flèche LT {p_['fleche']:.2f} mm (L/{p_['ratio']:.0f}) — "
          f"contre-flèche {p_['contre_fleche']:.0f} mm")
