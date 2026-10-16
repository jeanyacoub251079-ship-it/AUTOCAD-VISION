"""Données normatives Eurocodes + Annexes Nationales Françaises.

Sources (valeurs par défaut, paramétrables projet par projet — l'utilisateur
garde la main, cf. §1.2/§1.8) :
- EC0 NF EN 1990 + NA : γG=1.35/1.0, γQ=1.5, combinaisons ELU/ELS.
- EC1-1-1 NA : charges d'exploitation par catégorie de local.
- EC1-1-3 NA : zones de neige A1..E, sk0 (<200 m), S_Ad, ψ0 neige.
- EC1-1-4 NA : zones de vent, vb0 = 22/24/26/28 m/s, ρ=1.25 kg/m³.
- EC8 (arrêté du 22/10/2010 + NA) : agr par zone sismique, spectre type 1,
  γI par classe d'importance, T1 estimé.
TOUTES ces valeurs sont vérifiables/éditables — l'application produit des
PROPOSITIONS à valider par l'ingénieur, jamais un livrable signable.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

G_ACC = 9.81  # m/s²
RHO_AIR = 1.25  # kg/m³ (EC1-1-4 NA)
GAMMA_CONCRETE = 25.0  # kN/m³ béton armé
GAMMA_STEEL = 78.5  # kN/m³

# --- EC0 + NA France --------------------------------------------------------
GAMMA_G_INFAVORABLE = 1.35
GAMMA_G_FAVORABLE = 1.0  # choix national FR
GAMMA_Q = 1.5

# --- EC1-1-1 (charges d'exploitation, kN/m²) — NA France, AN.2.3 ----------
LIVE_LOADS: dict[str, dict[str, float]] = {
    "habitation": {"q": 1.5, "psi0": 0.5, "psi1": 0.4, "psi2": 0.3,
                   "libelle": "Locaux d'habitation (cat. A, NA FR AN.2.3)"},
    "bureau": {"q": 2.5, "psi0": 0.5, "psi1": 0.3, "psi2": 0.3,
               "libelle": "Bureaux (cat. B1)"},
    "commerce": {"q": 4.0, "psi0": 0.5, "psi1": 0.3, "psi2": 0.3,
                 "libelle": "Surfaces commerciales (cat. C1)"},
    "mixte": {"q": 1.5, "psi0": 0.5, "psi1": 0.4, "psi2": 0.3,
              "libelle": "Usage mixte — dominé habitation"},
    "escalier_prive": {"q": 2.5, "psi0": 0.5, "psi1": 0.4, "psi2": 0.3,
                      "libelle": "Escaliers privés"},
    "balcon": {"q": 2.5, "psi0": 1.0, "psi1": 0.6, "psi2": 0.5,
               "libelle": "Balcons et loggias (NA FR)"},
}

# Charges d'enveloppe habituelles (kN/m²)
FINISHES_KPA = 1.0      # revêtements + chape + cloisons légères
PARTITIONS_KPA = 0.8    # cloisons distributives (NA FR 150 daN/m² paroi/m² sol?)
CEILING_KPA = 0.25

# --- EC1-1-3 Neige — NA France AN.2/AN.4 -----------------------------------
SNOW_ZONES: dict[str, dict[str, float | str]] = {
    "A1": {"sk0": 0.45, "sAd": 0.00, "psi0": 0.0, "seuil_alt": 150.0, "grad_per100": 0.15},
    "A2": {"sk0": 0.45, "sAd": 1.00, "psi0": 0.0, "seuil_alt": 150.0, "grad_per100": 0.15},
    "B1": {"sk0": 0.55, "sAd": 1.00, "psi0": 0.0, "seuil_alt": 200.0, "grad_per100": 0.15},
    "B2": {"sk0": 0.55, "sAd": 1.35, "psi0": 0.0, "seuil_alt": 200.0, "grad_per100": 0.15},
    "C1": {"sk0": 0.65, "sAd": 0.00, "psi0": 0.5, "seuil_alt": 600.0, "grad_per100": 0.35},
    "C2": {"sk0": 0.65, "sAd": 1.35, "psi0": 0.5, "seuil_alt": 600.0, "grad_per100": 0.35},
    "D":  {"sk0": 0.90, "sAd": 1.80, "psi0": 1.0, "seuil_alt": 200.0, "grad_per100": 0.15},
    "E":  {"sk0": 1.40, "sAd": 0.00, "psi0": 1.0, "seuil_alt": 200.0, "grad_per100": 0.30},
}
SNOW_MU_FLAT = 0.8     # μ1 toiture-terrasse (pente < 30°)

def snow_load_sk(zone: str, altitude_m: float) -> tuple[float, str]:
    z = SNOW_ZONES.get(zone) or SNOW_ZONES["A2"]
    sk0 = float(z["sk0"])
    seuil = float(z["seuil_alt"])
    grad = float(z["grad_per100"])
    if altitude_m < seuil:
        # Zones A1/A2/B1/B2 : sous le seuil d'altitude, la neige est traditionnellement
        # négligée ; le NA fournit sk0 « à < 200 m » par défaut conservateur.
        return sk0, f"sk0 zone {zone} (altitude {altitude_m:.0f} m < seuil {seuil:.0f} m)"
    delta = grad * (altitude_m - 200.0) / 100.0
    return round(sk0 + max(0.0, delta), 3), f"sk0 + loi d'altitude (Δ={delta:.2f}) zone {zone}"


# --- EC1-1-4 Vent — NA France AN.2.3 ---------------------------------------
WIND_ZONES = {1: 22.0, 2: 24.0, 3: 26.0, 4: 28.0}

def wind_reference_pressure(zone: int) -> dict[str, float]:
    vb0 = WIND_ZONES.get(int(zone), 24.0)
    qb = 0.5 * RHO_AIR * vb0 * vb0 / 1000.0  # kPa
    return {"vb0_ms": vb0, "qb_kpa": round(qb, 3)}


# --- EC8 — agr par zone (arrêté 2010) + γI + spectre ------------------------
SEISME_AGR = {1: 0.4, 2: 0.7, 3: 1.1, 4: 1.6, 5: 3.0}
IMPORTANCE_GAMMA_I = {"I": 0.8, "II": 1.0, "III": 1.2, "IV": 1.4}
# Spectre élastique type 1, bâtiment (EC8 §3.2.2.2) — valeurs par défaut,
# l'AN FR modifie certains paramètres (sol B/C notamment) : à confirmer.
SOIL_TYPES = {
    "A": {"S": 1.00, "TB": 0.05, "TC": 0.10, "TD": 0.40},
    "B": {"S": 1.35, "TB": 0.10, "TC": 0.30, "TD": 2.00},
    "C": {"S": 1.50, "TB": 0.20, "TC": 0.60, "TD": 2.00},
    "D": {"S": 1.60, "TB": 0.20, "TC": 0.80, "TD": 2.00},
    "E": {"S": 1.40, "TB": 0.15, "TC": 1.00, "TD": 2.00},
}
BEHAVIOR_FACTORS = {
    "portique": {"DCV": {"q": 2.0}, "DCM": {"q": 3.0}, "DCH": {"q": 4.0}},
    "voiles": {"DCV": {"q": 2.0}, "DCM": {"q": 4.0}, "DCH": {"q": 5.3}},
    "double_systeme": {"DCV": {"q": 2.0}, "DCM": {"q": 3.0}, "DCH": {"q": 4.4}},
}


def seismic_spectral_acceleration(T: float, ag: float, soil: dict, importance: float,
                                   q: float, ductility_class: str = "DCM") -> dict:
    """Ordonnée du spectre Sd(T) = S·[η + 2.5(1−S)]·ag·β / q, η=1 primaire.

    β = 1.2 (DCH), 1.0 (DCM), 0.8 (DCV) — EC8 §3.2.2.5(3)N.
    """
    beta = {"DCV": 0.8, "DCM": 1.0, "DCH": 1.2}.get(ductility_class, 1.0)
    S, Tb, Tc, Td = soil["S"], soil["TB"], soil["TC"], soil["TD"]
    if T <= Tb:
        shape = 1.0 + (T / Tb) * (2.5 * (1 - S) - 1.0)
    elif T <= Tc:
        shape = 2.5
    elif T <= Td:
        shape = 2.5 * (Tc / T)
    else:
        shape = 2.5 * (Tc * Td / T ** 2) * (0.4 + 0.6 * S)
    Se = shape * ag * importance * S
    Sd = Se * beta / q
    return {"T": T, "Se_m_s2": round(Se, 3), "Sd_m_s2": round(Sd, 3), "beta": beta}


def estimate_fundamental_period(niveaux: int, system: str) -> float:
    """T1 estimé (écarts acceptables en conception préliminaire).

    AN FR NF EN 1998-1 §4.3.4 : portiques béton T1 = 0.15·n ;
    voiles T1 = 0.05·n ; systèmes doubles T1 = 0.10·n.
    """
    n = max(1, int(niveaux))
    if system == "voiles":
        return 0.05 * n
    if system == "double_systeme":
        return 0.10 * n
    return 0.15 * n


# --- Matériaux EC2 (Tableau 3.1/3.2) ----------------------------------------
CONCRETE: dict[str, dict[str, float]] = {
    "C20/25": {"fck": 20.0, "fck_cube": 25.0, "fctm": 2.2, "Ecm": 29000.0},
    "C25/30": {"fck": 25.0, "fck_cube": 30.0, "fctm": 2.6, "Ecm": 31000.0},
    "C30/37": {"fck": 30.0, "fck_cube": 37.0, "fctm": 2.9, "Ecm": 33000.0},
    "C35/45": {"fck": 35.0, "fck_cube": 45.0, "fctm": 3.2, "Ecm": 34000.0},
    "C40/50": {"fck": 40.0, "fck_cube": 50.0, "fctm": 3.5, "Ecm": 35000.0},
}
ALPHA_CC = 0.85  # choix national FR
GAMMA_C = 1.50
GAMMA_S = 1.15
STEEL_REBAR = {"classe": "B500B", "fyk": 500.0, "Es": 200000.0}

def concrete_props(classe: str) -> dict:
    c = dict(CONCRETE.get(classe) or CONCRETE["C25/30"])
    c["fcd"] = ALPHA_CC * c["fck"] / GAMMA_C
    c["fctd"] = c["fctm"] / 1.5
    c["Ecd"] = c["Ecm"] / GAMMA_C
    return c


def steel_props() -> dict:
    s = dict(STEEL_REBAR)
    s["fyd"] = s["fyk"] / GAMMA_S
    return s


# --- Enrobage (EC2 4.4.1.2, NA FR — valeur nominale, durée de vie 50 ans) ---
NOMINAL_COVER = {"X0": 10, "XC1": 15, "XC2": 20, "XC3": 20, "XC4": 25,
                 "XF1": 20, "XF3": 25, "XF4": 30, "XD1": 25, "XD2": 30,
                 "XS1": 25, "XS2": 30, "XS3": 35}
FONDATION_COVER = 50  # sous-face sur béton de propreté, semelle courante


def design_cover(classe_exposition: str, element: str) -> float:
    c = float(NOMINAL_COVER.get(classe_exposition, 20))
    if element in ("semelle", "radier", "fondation"):
        c = max(c, FONDATION_COVER - 20)
    if element in ("voile", "mur"):
        c += 5
    return c


# --- Combinaisons EC0 + AN FR (bâtiments) ----------------------------------

@dataclass
class LoadCases:
    G: float = 0.0          # permanent volumique sur l'élément (kN/m ou kPa)
    Q: float = 0.0          # exploitation
    S: float = 0.0          # neige
    W: float = 0.0          # vent
    psi0_Q: float = 0.5
    psi0_S: float = 0.0
    psi0_W: float = 0.5
    psi1_Q: float = 0.4
    psi2_Q: float = 0.3
    psi2_S: float = 0.2
    has_snow: bool = False
    has_wind: bool = False

    def combinations(self) -> list[dict]:
        combos: list[dict] = []

        def push(cid, ctype, expr, g, q=0.0, s=0.0, w=0.0):
            combos.append({"id": cid, "type": ctype, "expression": expr,
                           "coeff": {"G": g, "Q": q, "S": s, "W": w}})

        gU, gF, gQ = GAMMA_G_INFAVORABLE, GAMMA_G_FAVORABLE, GAMMA_Q
        # ELU 1.35G + 1.5Q1 (+1.5ψ0·Qi)
        push("ELU-1", "ELU", f"{gU}·G + {gQ}·Q", gU, gQ)
        if self.has_snow:
            push("ELU-2", "ELU", f"{gU}·G + {gQ}·S", gU, 0.0, gQ)
        if self.has_wind:
            push("ELU-3", "ELU", f"{gU}·G + {gQ}·W + {gQ}·ψ0Q·Q", gU, gQ * self.psi0_Q, 0.0, gQ)
            if self.Q > 0 and not self.has_snow:
                push("ELU-4", "ELU", f"{gU}·G + {gQ}·Q + {gQ}·ψ0W·W", gU, gQ, 0.0, gQ * self.psi0_W)
            elif self.has_snow and self.psi0_S > 0:
                push("ELU-5", "ELU", f"{gU}·G + {gQ}·Q + {gQ}·ψ0S·S", gU, gQ, gQ * self.psi0_S, 0.0)
        elif self.Q > 0:
            # pas de réduction en France hors tête de combinaison : ELU-1 suffit
            pass
        # ELS
        push("ELS-car", "ELS", "G + Q", 1.0, 1.0)
        if self.has_snow:
            push("ELS-car-N", "ELS", "G + S", 1.0, 0.0, 1.0)
        push("ELS-freq", "ELS", "G + ψ1·Q", 1.0, self.psi1_Q)
        push("ELS-qp", "ELS", "G + ψ2·Q", 1.0, self.psi2_Q)
        # ELU accidentel séisme : γ=1 sur G, ψ2 sur variables (EC8 §3.4.3, pratique FR :
        # G nominale + ψ2Q + Ad)
        push("ELU-acc-E", "ELU-acc", "G + ψ2·Q + E", 1.0, self.psi2_Q)
        return combos

    def design_forces(self) -> list[tuple[str, float]]:
        out = []
        for c in self.combinations():
            k = c["coeff"]
            val = (k["G"] * self.G + k["Q"] * self.Q + k["S"] * self.S + k["W"] * self.W)
            out.append((c["id"], round(val, 3)))
        return out


# --- Dispositions constructives EC8 (sélection automatique DCV→DCM) --------
EC8_CONSTRUCTIVE_RULES: dict[str, list[dict[str, Any]]] = {
    "colonne": [
        {"code": "5.4.1.2(3)", "regle": "Dimension minimale ≥ 250 mm (DCM, section composée)",
         "check": lambda d: min(d) >= 0.25},
        {"code": "5.4.1.2(4)", "regle": "Rapport des dimensions de section ≤ 3",
         "check": lambda d: max(d) / max(min(d), 1e-9) <= 3.0},
        {"code": "5.4.1.2(5)", "regle": "Élançement ≤ 15 (portique DCM)",
         "check": lambda extra: extra.get("elancement", 0) <= 15.0},
    ],
    "poutre": [
        {"code": "5.4.2.1(2)", "regle": "Largeur de semelle ≥ 200 mm et h/b ≤ 3",
         "check": lambda d: d[0] >= 0.20 and d[1] / max(d[0], 1e-9) <= 3.0},
        {"code": "5.4.2.3(1)", "regle": "Armatures mini 2 barres haut et bas",
         "check": lambda extra: extra.get("nbarres_min", 2) >= 2},
    ],
    "voile": [
        {"code": "5.4.1", "regle": "Épaisseur ≥ 150 mm et élancement ≤ 30",
         "check": lambda d: d[0] >= 0.15},
    ],
}
