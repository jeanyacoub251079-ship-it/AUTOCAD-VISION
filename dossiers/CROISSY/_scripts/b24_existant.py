#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-24 — EXISTANT NON SONDÉ — CROISSY-FLORA (mode PARAMÉTRIQUE)
=============================================================
Produit la vérification littérale des éléments existants dont les données
manquent, le tableau de sensibilité NON CONTRACTUEL, la liste des essais, et
contrôle les 7 points du critère d'acceptation de la fiche B-24.

Interdictions vérifiées par le script :
  - aucune valeur retenue : chaque donnée manquante reste en symbole ;
  - aucun élément déclaré « vérifié » ;
  - le tableau de sensibilité est marqué NON CONTRACTUEL ;
  - aucun livrable exécutable (suffixe _P, filigrane).

Les seules valeurs numériques employées sont :
  * des EFFETS DE CHARGE repris de B-21 (p_ELU, N_ELU, g, q) ;
  * des valeurs de SENSIBILITÉ, explicitement non contractuelles.

Sorties : _rendus/b24_existant.txt + _rendus/b24_existant.json
"""
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_TXT = os.path.join(ROOT, "_rendus", "b24_existant.txt")
OUT_JSON = os.path.join(ROOT, "_rendus", "b24_existant.json")
NOTE = os.path.join(ROOT, "02_CONCEPTION", "B-24_Existant_Non_Sonde_P.md")

LOG = []


def log(s=""):
    LOG.append(s)
    print(s)


def table(rows, widths):
    for r in rows:
        line = "    "
        for cell, w in zip(r, widths):
            line += str(cell)[:w].ljust(w) + "  "
        log(line.rstrip())


# ---------------------------------------------------------------------------
# 1. CONSTANTES REPRISES DE B-21 (effets de charge — pas des résistances)
# ---------------------------------------------------------------------------
G_PLANCHER_A = 5.10      # kN/m²  — B-21 tableau 1
G_PLANCHER_B = 8.01      # kN/m²  — B-21, recharge de sol D4 comprise
Q_EXPLOIT = 2.50         # kN/m²  — D-32
G_TOITURE = 0.95         # kN/m²  — H-29
Q_NEIGE = 0.45           # kN/m²  — zone A1, contractuel
MUR_MOELLONS = 22.0      # kN/m³  — B-21 § 5 (mur porté en sous-œuvre)
GAMMA_ELU_G, GAMMA_ELU_Q = 1.35, 1.50
P_ELU = {"F1a": 76.5, "F1b": 76.5, "F1c": 76.5, "F2": 63.1, "F3": 46.1,
         "F4": 4.7, "R1": 57.9, "R2-N": 34.8, "R2-S": 27.1}
SIGMA_APPUI_P1 = 177.1 / 1000.0   # MPa — B-21 : 177,1 kN/m² sous P1-N/P1-S

# ---------------------------------------------------------------------------
# 2. MATÉRIAUX — valeurs de SENSIBILITÉ (classes plausibles), jamais retenues
# ---------------------------------------------------------------------------
BOIS = {"C18": {"f_mk": 18.0, "f_c0k": 18.0, "E005": 6000.0},
        "C24": {"f_mk": 24.0, "f_c0k": 21.0, "E005": 7400.0}}
K_MOD = 0.80        # classe de service 2, charge de longue durée
GAMMA_BOIS = 1.30
GAMMA_MAC = 2.50    # H-26 / D-34
FK_MAC = (0.5, 1.0, 1.5, 2.0, 2.5)   # plage plausible moellons, MPa


def fm_d(cls):
    return K_MOD * BOIS[cls]["f_mk"] / GAMMA_BOIS


def fc0_d(cls):
    return K_MOD * BOIS[cls]["f_c0k"] / GAMMA_BOIS


def kc_flambement(cls, b_mm, h_mm, lc_mm):
    """EC5 § 6.3.2 — coefficient de flambement, section rectangulaire."""
    a = BOIS[cls]
    i = min(b_mm, h_mm) / math.sqrt(12.0)
    lam = lc_mm / i
    lam_rel = lam / math.pi * math.sqrt(a["f_c0k"] / a["E005"])
    k = 0.5 * (1 + 0.2 * (lam_rel - 0.3) + lam_rel ** 2)
    disc = k * k - lam_rel ** 2
    return 1.0 / (k + math.sqrt(disc)) if disc > 0 else 1.0 / (2 * k), lam_rel


def ratio(ed, rd):
    return ed / rd


# ---------------------------------------------------------------------------
# 3. ÉLÉMENTS NON SONDÉS — E-01 à E-08
#    Chaque élément : (id, nom, donnée manquante, charge, vérification,
#                      formule littérale, plage, brique de fermeture)
# ---------------------------------------------------------------------------
ELEMENTS = [
    dict(id="E-01", nom="Murs de moellons porteurs (façades et refends)",
         manque="f_k (résistance), épaisseur réelle, présence de chaînages",
         charge="sigma = 0,177 MPa sous P1-N/P1-S (B-21) ; 0,094 MPa moyenne voiles",
         verif="Compression verticale",
         formule="sigma_d = N_Ed / A_inf  <=  f_d = f_k / gamma_M",
         plage="f_k = 0,5 à 2,5 MPa",
         fermeture="B-46"),
    dict(id="E-02", nom="Poutre maîtresse bois (désordre 3)",
         manque="section b x h, classe de bois (MAT-06), continuité, état",
         charge="p_ELU = 57,9 kN/m (R1, B-21) ; L = 4,3 m (B-11)",
         verif="Flexion simple + cisaillement + flèche ELS",
         formule="sigma_m,d = M_Ed / (b h^2 / 6)  <=  f_m,d ;  M_Ed = p_ELU L^2 / 8",
         plage="b x h = 0,15x0,20 à 0,20x0,30 m ; C18 à C24",
         fermeture="B-44 (avec R1 : B-45)"),
    dict(id="E-04", nom="Potelets de charpente (désordre 8)",
         manque="section, hauteur libre, classe, excentrement, contreventement",
         charge="N_Ed = (1,35 G + 1,5 Q) x e x L_trib = 1,96 kN/m² x surface reprise",
         verif="Compression + flambement",
         formule="N_Ed / (k_c A f_c,0,d)  <=  1  avec lambda = L_cr / i",
         plage="section 0,08x0,08 à 0,10x0,10 m ; L_cr 2,20 m ; e x L_trib 3,75 à 12,00 m²",
         fermeture="B-44"),
    dict(id="E-05", nom="Ferme de charpente altérée (désordre 6)",
         manque="sections des arbalétriers et de l'entrait, classe, section "
                "résiduelle après purge, entraxe des fermes, contreventement",
         charge="p = 1,96 kN/m² x entraxe des fermes ; portée 9,90 m (D2 f. 02)",
         verif="Flexion de l'arbalétrier (borne) + compression + flambement",
         formule="sigma_m,d = p L^2 / 8 / (b h^2 / 6)  <=  f_m,d  ;  "
                 "puis N_Ed / (k_c A f_c,0,d) <= 1",
         plage="arbalétrier 0,08x0,18 à 0,12x0,24 m ; entraxe 2,5 à 3,5 m ; C18 à C24",
         fermeture="B-44"),
    dict(id="E-06", nom="Pannes de couverture",
         manque="section, portée entre fermes, entraxe, classe",
         charge="p = 1,96 kN/m² x entraxe des pannes",
         verif="Flexion biaise + flèche ELS",
         formule="sigma_m,d = p L^2 / 8 / (b h^2 / 6)  <=  f_m,d",
         plage="section 0,08x0,12 à 0,12x0,18 m ; entraxe 1,75 à 2,25 m ; L = 3,20 m",
         fermeture="B-44"),
    dict(id="E-07", nom="Plancher haut portant la charpente par potelets (désordre 5)",
         manque="NATURE du plancher (bois / BA / hourdis), épaisseur, sens "
                "porteur, portée, sections et entraxes (EXI-04 absent)",
         charge="Réactions des potelets de charpente, augmentées par nos renforts B-44",
         verif="Flexion du solivage + réaction d'appui — non formulable en l'état",
         formule="Indéterminée : la nature du support conditionne la formule "
                 "(EC5 si bois, EC2 si BA)",
         plage="NON DÉFINISSABLE — aucune borne ne peut être posée sans connaître la nature",
         fermeture="B-43"),
    dict(id="E-08", nom="Linteaux existants au-dessus des baies (désordre 1)",
         manque="section, matériau, portée libre, longueur d'appui, état",
         charge="p = 22 x h + bande de plancher (B-21 § 5)",
         verif="Flexion + cisaillement + appui",
         formule="sigma_m,d = M_Ed / (b h^2 / 6)  <=  f_m,d  ;  R / (a b) <= f_d",
         plage="section 0,20x0,20 à 0,25x0,25 m ; h de maçonnerie portée 0,80 à 2,00 m",
         fermeture="B-49"),
]

# ---------------------------------------------------------------------------
# 3 bis. ÉLÉMENT SORTI DU CHAMP EN INDICE B — E-03
#   Les données existent : D3 p. 10 (EXI-01a, EXI-01b, EXI-01e) donnent
#   solives 8x18 @ 0,50 m, portée 2,77 m, poutre 20x15 portée 4,34 m,
#   complexe lambourde + parquet + lattis. La fiche B-24 n'a donc plus lieu
#   d'être : le calcul devient possible et relève de B-43.
#   Seule reste ouverte la question du PÉRIMÈTRE de la recharge de sol 15 cm
#   (D4 p. 5 et 14) : planchers hauts ou sol du RDC seulement ?
# ---------------------------------------------------------------------------
E03 = dict(id="E-03", nom="Solives de plancher bois 8x18 @ 0,50 m (plancher A)",
           b=80.0, h=180.0, e=500.0, L=2770.0,
           source="D3 p. 10 (EXI-01a) : 8x18 @ 0,50 m, portée 2,77 m, C18 (EXI-03, hypothèse)")

# g du plancher A : 1,00 (D3) + 0,80 cloisons (H-30) = 1,80 ; + 3,30 recharge (H-28)
G_A_SANS_RECHARGE = 1.80
G_A_AVEC_RECHARGE = 5.10
Q_A = 2.50

# Zones sans plage plausible (cas particulier de la fiche)
ZONES_SANS_PLAGE = [
    ("ZONE NON RELEVEE n° 1", "emprise non cotée sur D2 f. 02",
     "Inspection visuelle + relevé de charpente avant toute vérification"),
    ("ZONE NON RELEVEE n° 2", "emprise non cotée sur D2 f. 02",
     "Inspection visuelle + relevé de charpente avant toute vérification"),
]


# ---------------------------------------------------------------------------
# 4. TABLEAU DE SENSIBILITÉ — NON CONTRACTUEL — POUR INFORMATION
# ---------------------------------------------------------------------------
def sensibilite():
    """Grille complète sur la plage plausible. Chaque ligne = un cas, jamais
    une valeur retenue."""
    cas = []

    # E-01 — maçonnerie en compression
    for fk in FK_MAC:
        fd = fk / GAMMA_MAC
        r = ratio(SIGMA_APPUI_P1, fd)
        cas.append(("E-01", "f_k = %.1f MPa" % fk, r))

    # E-02 — poutre maîtresse 20x15 (flexion)
    M = P_ELU["R1"] * 4.3 ** 2 / 8.0          # kN.m
    for b, h in ((0.15, 0.20), (0.20, 0.22), (0.20, 0.30)):
        W = (b * 1000) * (h * 1000) ** 2 / 6.0   # mm3
        sd = M * 1e6 / W                          # N/mm2 = MPa
        for cls in ("C18", "C24"):
            cas.append(("E-02", "%dx%d mm, %s" % (b * 1000, h * 1000, cls),
                        ratio(sd, fm_d(cls))))

    # E-04 — potelets (flambement)
    for b in (0.08, 0.10):
        kc, lam_rel = kc_flambement("C18", b * 1000, b * 1000, 2200.0)
        nrd = kc * (b * 1000) ** 2 * fc0_d("C18") / 1000.0   # kN
        for surf in (3.75, 6.00, 12.00):
            ned = (GAMMA_ELU_G * G_TOITURE + GAMMA_ELU_Q * Q_NEIGE) * surf
            cas.append(("E-04", "%dx%d mm, surface reprise %.2f m², C18" % (b * 1000, b * 1000, surf),
                        ratio(ned, nrd)))
        log("        E-04 : %dx%d mm -> k_c = %.3f (lambda_rel = %.2f), N_b,Rd = %.1f kN"
            % (b * 1000, b * 1000, kc, lam_rel, nrd))

    # E-05 — ferme (flexion de l'arbalétrier, borne)
    for e in (2.5, 3.0, 3.5):
        p = (GAMMA_ELU_G * G_TOITURE + GAMMA_ELU_Q * Q_NEIGE) * e
        M = p * 9.90 ** 2 / 8.0
        for b, h in ((0.08, 0.18), (0.10, 0.20), (0.12, 0.24)):
            W = (b * 1000) * (h * 1000) ** 2 / 6.0
            sd = M * 1e6 / W
            for cls in ("C18", "C24"):
                cas.append(("E-05", "arb. %dx%d mm, e = %.1f m, %s"
                            % (b * 1000, h * 1000, e, cls), ratio(sd, fm_d(cls))))

    # E-06 — pannes (flexion)
    for e in (1.75, 2.25):
        p = (GAMMA_ELU_G * G_TOITURE + GAMMA_ELU_Q * Q_NEIGE) * e
        M = p * 3.20 ** 2 / 8.0
        for b, h in ((0.08, 0.12), (0.10, 0.15), (0.12, 0.18)):
            W = (b * 1000) * (h * 1000) ** 2 / 6.0
            sd = M * 1e6 / W
            for cls in ("C18", "C24"):
                cas.append(("E-06", "%dx%d mm, e = %.2f m, %s"
                            % (b * 1000, h * 1000, e, cls), ratio(sd, fm_d(cls))))

    # E-08 — linteaux existants (flexion)
    for h in (0.80, 1.50, 2.00):
        for L in (0.85, 1.00, 1.55):
            p = MUR_MOELLONS * h + 10.51
            M = p * L ** 2 / 8.0
            for b, hh in ((0.20, 0.20), (0.25, 0.25)):
                W = (b * 1000) * (hh * 1000) ** 2 / 6.0
                sd = M * 1e6 / W
                for cls in ("C18", "C24"):
                    cas.append(("E-08", "%dx%d mm, h = %.2f m, L = %.2f m, %s"
                                % (b * 1000, hh * 1000, h, L, cls),
                                ratio(sd, fm_d(cls))))
    return cas


def e03_scenarios():
    """E-03 avec ses données réelles. Le périmètre de la recharge de 15 cm est
    tranché par D-35 (recharge = dallage seul) : le cas « sans recharge » est
    RETENU ; le cas « avec recharge » est conservé pour mémoire."""
    b, h = E03["b"], E03["h"]
    W = b * h ** 2 / 6.0
    I = b * h ** 3 / 12.0
    out = []
    for g, lab in ((G_A_SANS_RECHARGE, "sans recharge (RDC seul)"),
                   (G_A_AVEC_RECHARGE, "avec recharge 15 cm")):
        p = (E03["e"] / 1000.0) * (GAMMA_ELU_G * g + GAMMA_ELU_Q * Q_A)
        M = p * (E03["L"] / 1000.0) ** 2 / 8.0
        sd = M * 1e6 / W
        pser = (E03["e"] / 1000.0) * (g + Q_A)
        w = 5 * pser * E03["L"] ** 4 / (384 * 9000.0 * I)
        out.append((lab, p, M, sd, w))
    return out


def verdict(ratios):
    """Favorable : satisfaisant pour TOUTE la plage. Limite : une partie.
    Défavorable : insuffisant pour toute la plage."""
    if max(ratios) <= 1.0:
        return "FAVORABLE"
    if min(ratios) > 1.0:
        return "DEFAVORABLE"
    return "LIMITE"


# ---------------------------------------------------------------------------
# 5. ESSAIS ET SONDAGES (tableau 3)
# ---------------------------------------------------------------------------
ESSAIS = [
    ("E-01", "Essais de compression sur maçonnerie de moellons (carottages)",
     "NF EN 1996-1-1 + NF EN 1052-1", "6 carottes (2 murs x 3 points)",
     "Façade Ouest et refend central, sur 2,00 m de haut", "MOA (D-34 : hors mission)", "avant B-46"),
    ("E-01", "Essais de cisaillement (cohésion initiale f_vk0)",
     "NF EN 1052-3 / NF EN 1052-4", "3 éprouvettes",
     "Même emprise que les carottages", "MOA (D-34 : hors mission)", "avant B-46"),
    ("E-02/E-05/E-06", "Relevé de charpente au mètre et au calibre (sections, classes, état)",
     "NF EN 338 (classement visuel) + NF EN 1995-1-1", "2 zones non relevées + combles",
     "Intégralité des combles, plan de repérage", "MOA / bureau mandaté", "avant B-44"),
    ("E-07", "Sondage destructif du plancher haut (composition, sens porteur, portée)",
     "NF EN 338 / NF EN 1992 / NF EN 15037 selon la nature", "3 ouvertures de 0,50 x 0,50 m",
     "Plancher haut, un point par file de potelets", "MOA / bureau mandaté",
     "AVANT B-43 — priorité 1"),
    ("E-01", "Ouverture de fouilles au droit des appuis neufs",
     "NF EN 1997-2", "5 fouilles (P1-N, P1-S, P2, P3, J1)",
     "Au droit de chaque appui, jusqu'au niveau d'assise", "MOA (point d'arrêt H-15)", "avant B-40"),
]


# ---------------------------------------------------------------------------
# 6. CONTRÔLE DES 7 POINTS DU CRITÈRE D'ACCEPTATION
# ---------------------------------------------------------------------------
def controle(note_txt, cas):
    crit = []
    par_el = {}
    for cid, label, r in cas:
        par_el.setdefault(cid, []).append(r)
    verdicts = {cid: verdict(v) for cid, v in par_el.items()}
    verdicts["E-07"] = "SANS PLAGE"

    # 1. Chaque élément non sondé a une vérification littérale écrite
    ok1 = all(e["formule"] and e["verif"] for e in ELEMENTS) and \
        all(e["id"] in note_txt for e in ELEMENTS) and "E-03" in note_txt
    crit.append(("1. Vérification littérale écrite pour les %d éléments en attente"
                 % len(ELEMENTS), ok1))

    # 2. Chaque donnée manquante reste en symbole (jamais remplie)
    ok2 = all(e["manque"] for e in ELEMENTS) and \
        all(("f_k" in e["formule"] or "b" in e["formule"] or "NON DÉFINISSABLE" in e["formule"])
            for e in ELEMENTS)
    crit.append(("2. Donnée manquante laissée en symbole (%d éléments)" % len(ELEMENTS), ok2))

    # 3. Tableau de sensibilité marqué NON CONTRACTUEL
    ok3 = "NON CONTRACTUEL" in note_txt and note_txt.count("NON CONTRACTUEL") >= 3
    crit.append(("3. Sensibilité marquée NON CONTRACTUEL (%d occurrences)"
                 % note_txt.count("NON CONTRACTUEL"), ok3))

    # 4. Essais listés avec référentiel, nombre et emprise
    ok4 = all(e[2] and e[3] and e[4] for e in ESSAIS) and "NF EN 338" in note_txt
    ok4 = ok4 and "E-03" not in " ".join(a for a, _, _, _, _, _, _ in ESSAIS)
    crit.append(("4. Essais : référentiel + nombre + emprise (E-03 sorti)", ok4))

    # 5. Aucun élément déclaré « vérifié »
    interdits = re.findall(r"\bvérifié(?:e|s|es)?\b", note_txt, flags=re.I)
    # autorisé : « non vérifié », « à vérifier » n'est pas « vérifié »
    ok5 = len(interdits) == 0
    crit.append(("5. Aucun élément déclaré « vérifié » (%d occurrence(s))"
                 % len(interdits), ok5))

    # 6. Aucun livrable exécutable : suffixe _P + filigrane
    ok6 = os.path.basename(NOTE).endswith("_P.md") and "NE PAS EXÉCUTER" in note_txt \
        and "EN ATTENTE DE" in note_txt
    crit.append(("6. Suffixe _P + filigrane « EN ATTENTE DE »", ok6))

    # 7. Aucune valeur de repli proposée (les replis sont renvoyés à une décision RDR)
    ok7 = "décision `RDR`" in note_txt and "Aucune valeur de repli" in note_txt
    crit.append(("7. Aucune valeur de repli proposée (renvoi RDR)", ok7))

    return crit, verdicts


# ---------------------------------------------------------------------------
def main():
    log("=" * 78)
    log("B-24 — EXISTANT NON SONDÉ — CROISSY-FLORA — INDICE C")
    log("=" * 78)
    log("")
    log("Aucune valeur n'est retenue. Les charges sont des effets de charge")
    log("repris de B-21 ; les résistances sont des valeurs de SENSIBILITÉ.")
    log("")

    log("--- TABLEAU 1 : ÉLÉMENTS NON SONDÉS -------------------------------")
    table([("ID", "ÉLÉMENT", "DONNÉE MANQUANTE", "FERMETURE")] +
          [(e["id"], e["nom"], e["manque"][:58], e["fermeture"]) for e in ELEMENTS],
          (6, 46, 60, 16))
    log("")

    log("--- PARAMÈTRES DE SENSIBILITÉ (non contractuels) ------------------")
    log("    k_mod = %.2f  ·  gamma_M bois = %.2f  ·  gamma_M maçonnerie = %.2f (H-26)"
        % (K_MOD, GAMMA_BOIS, GAMMA_MAC))
    for cls in ("C18", "C24"):
        log("    %s : f_m,d = %.2f MPa  ·  f_c,0,d = %.2f MPa"
            % (cls, fm_d(cls), fc0_d(cls)))
    log("")

    cas = sensibilite()
    log("")
    log("--- TABLEAU 2 : SENSIBILITÉ — NON CONTRACTUEL — POUR INFORMATION --")
    par_el = {}
    for cid, label, r in cas:
        par_el.setdefault(cid, []).append((label, r))

    verdicts = {}
    log("    %-6s %-58s %-9s %-9s %s"
        % ("ID", "CAS LE PLUS DÉFAVORABLE DE LA PLAGE", "ratio min", "ratio max", "VERDICT"))
    for e in ELEMENTS:
        cid = e["id"]
        if cid not in par_el:
            verdicts[cid] = "SANS PLAGE"
            log("    %-6s %-58s %-9s %-9s %s"
                % (cid, "aucune borne posable sans connaître la nature", "-", "-", "SANS PLAGE"))
            continue
        v = par_el[cid]
        rmin = min(r for _, r in v)
        rmax = max(r for _, r in v)
        pire = max(v, key=lambda t: t[1])
        verdicts[cid] = verdict([r for _, r in v])
        log("    %-6s %-58s %-9.3f %-9.3f %s"
            % (cid, pire[0][:58], rmin, rmax, verdicts[cid]))
    log("")
    log("    Grille complète : %d cas testés, tous dans la plage plausible."
        % len(cas))
    log("")

    log("--- E-03 SORTI DU CHAMP EN INDICE B (données D3 p. 10) -----------")
    log("    %s" % E03["source"])
    log("    Périmètre de la recharge TRANCHÉ par D-35 (20/10/2026) : recharge =")
    log("    dallage seul (D4 p. 5 et 14) → le cas SANS RECHARGE est RETENU.")
    log("    %-24s %-8s %-9s %-9s %-9s %s"
        % ("CAS", "p_ELU", "M_Ed", "sigma_m,d", "sigma/f_m,d", "w_ELS (C18)"))
    for lab, p_, m_, sd_, w_ in e03_scenarios():
        tag = "  <-- RETENU (D-35)" if lab.startswith("sans recharge") else ""
        log("    %-24s %-8.2f %-9.2f %-9.2f %-9.3f %.1f mm%s"
            % (lab, p_, m_, sd_, sd_ / fm_d("C18"), w_, tag))
    log("    f_m,d (C18) = %.2f MPa · flèche ELS à E_mean = 9 000 MPa (court terme),"
        % fm_d("C18"))
    log("    limite L/300 = %.1f mm · à long terme (k_def = 0,6) la flèche est majorée."
        % (E03["L"] / 300.0))
    log("    Le cas retenu passe : sigma/f_m,d = 0,619 (marge 38 %) et 4,7 mm")
    log("    pour 9,2 mm admis (court terme). Reste R-24-B2 : état des abouts.")
    log("    La vérification de section reste du ressort de B-43.")
    log("")

    log("--- TABLEAU 3 : ESSAIS ET SONDAGES NÉCESSAIRES --------------------")
    table([("ÉLÉMENT", "ESSAI", "RÉFÉRENTIEL", "NOMBRE", "ÉCHÉANCE")] +
          [(a, b[:52], c[:40], d[:34], g) for a, b, c, d, _, _, g in ESSAIS],
          (14, 54, 42, 36, 14))
    log("")

    # contrôle de la note
    if not os.path.exists(NOTE):
        log("!! Note absente : %s" % NOTE)
        return 2
    with open(NOTE, encoding="utf-8") as f:
        note_txt = f.read()

    crit, _ = controle(note_txt, cas)
    log("--- CRITÈRE D'ACCEPTATION (7 POINTS) ------------------------------")
    for lib, ok in crit:
        log("    [%s] %s" % ("OK" if ok else "KO", lib))
    conformes = sum(1 for _, ok in crit if ok)
    log("")
    log("RÉSULTAT : %d/%d CONFORME" % (conformes, len(crit)))

    # synthèse
    compte = {"FAVORABLE": [], "LIMITE": [], "DEFAVORABLE": [], "SANS PLAGE": []}
    for cid, v in verdicts.items():
        compte[v].append(cid)
    log("")
    log("SYNTHÈSE : %d éléments en attente de données · %d favorable(s) pour toute "
        "la plage · %d limite(s) · %d défavorable(s) pour toute la plage · "
        "%d sans plage plausible · 1 élément SORTI du champ (E-03)"
        % (len(ELEMENTS), len(compte["FAVORABLE"]), len(compte["LIMITE"]),
           len(compte["DEFAVORABLE"]), len(compte["SANS PLAGE"])))
    log("")

    os.makedirs(os.path.dirname(OUT_TXT), exist_ok=True)
    with open(OUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")

    data = {
        "brique": "B-24", "indice": "A", "mode": "PARAMETRIQUE",
        "date": "20/10/2026", "note": os.path.basename(NOTE),
        "elements": [dict(id=e["id"], nom=e["nom"], manque=e["manque"],
                          charge=e["charge"], verif=e["verif"],
                          formule=e["formule"], plage=e["plage"],
                          fermeture=e["fermeture"],
                          verdict=verdicts[e["id"]]) for e in ELEMENTS],
        "zones_sans_plage": [dict(zone=z[0], emprise=z[1], action=z[2])
                             for z in ZONES_SANS_PLAGE],
        "sensibilite": [dict(element=c, cas=l, ratio=round(r, 3)) for c, l, r in cas],
        "essais": [dict(element=a, essai=b, referentiel=c, nombre=d,
                        emprise=e, responsable=f, echeance=g)
                   for a, b, c, d, e, f, g in ESSAIS],
        "elements_sortis": [dict(id=E03["id"], nom=E03["nom"],
                                 source=E03["source"],
                                 scenarios=[dict(cas=l, p_ELU=round(p_, 2),
                                                 M_Ed=round(m_, 2),
                                                 sigma=round(sd_, 2),
                                                 ratio_C18=round(sd_ / fm_d("C18"), 3),
                                                 w_ELS_mm=round(w_, 1))
                                            for l, p_, m_, sd_, w_ in e03_scenarios()])],
        "comptes": {k: v for k, v in compte.items()},
        "verdict_7_criteres": conformes,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\nJournal : %s" % os.path.relpath(OUT_TXT, os.path.dirname(ROOT)))
    print("JSON    : %s" % os.path.relpath(OUT_JSON, os.path.dirname(ROOT)))
    print("TXT     : %s o · JSON : %s o" % (os.path.getsize(OUT_TXT), os.path.getsize(OUT_JSON)))
    return 0 if conformes == 7 else 1


if __name__ == "__main__":
    sys.exit(main())
