#!/usr/bin/env python3
"""Construction de l'arborescence CARNAC v3.0 depuis la baseline v2.6 (Étapes 3 et 4)."""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
SRC = BASE / "CARNAC_v2.6"
DST = BASE / "CARNAC_v3.0"

sys.path.insert(0, str(BASE / "_tools"))
from table_normalizer import normalize_tables_in_markdown  # noqa: E402

PHASE_BY_PREFIX = {
    "B-00": "0 — Cadrage et qualification",
    "B-01": "0 — Cadrage et qualification",
    "B-02": "0 — Cadrage et qualification",
    "B-03": "0 — Cadrage et qualification",
    "B-04": "0 — Cadrage et qualification",
    "B-10": "2 — Audit croisé multi-pièces",
    "B-11": "2 — Audit croisé multi-pièces",
    "B-12": "2 — Audit croisé multi-pièces",
    "B-13": "2 — Audit croisé multi-pièces",
    "B-14": "2 — Audit croisé multi-pièces",
    "B-15": "2 — Audit croisé multi-pièces",
    "B-20": "3 — Conception et synthèse structurelle",
    "B-21": "3 — Conception et synthèse structurelle",
    "B-22": "3 — Conception et synthèse structurelle",
    "B-23": "3 — Conception et synthèse structurelle",
    "B-24": "3 — Conception et synthèse structurelle",
    "B-25": "3 — Conception et synthèse structurelle",
    "B-30": "1 — Socle géométrique et nettoyage",
    "B-31": "1 — Socle géométrique et nettoyage",
    "B-32": "1 — Socle géométrique et nettoyage",
    "B-33": "6 — Vérification croisée et clôture",
    "B-34": "5 — Synthèse et livrables d'exécution",
    "B-60": "5 — Synthèse et livrables d'exécution",
    "B-62": "5 — Synthèse et livrables d'exécution",
    "B-64": "5 — Synthèse et livrables d'exécution",
    "B-70": "6 — Vérification croisée et clôture",
    "B-71": "6 — Vérification croisée et clôture",
    "B-72": "6 — Vérification croisée et clôture",
}


def phase_for(code: str) -> str | None:
    if code in PHASE_BY_PREFIX:
        return PHASE_BY_PREFIX[code]
    if code.startswith("B-4") or code.startswith("B-50"):
        return "4 — Calculs d'exécution"
    if code.startswith("T-"):
        return "Transverse — à tout moment"
    return None


VAR_INJECT: dict[str, list[str]] = {
    "CFG-01": ["B-00", "B-01", "B-20", "B-60"],
    "CFG-02": ["B-01", "B-04", "B-25", "B-34", "B-60"],
    "CFG-03": ["B-01", "B-20", "B-21", "B-25", "B-30", "B-60"],
    "DEC-05": ["B-03", "B-20", "B-22", "B-40", "B-60", "B-64", "B-70"],
    "DEC-06": ["B-03", "B-22", "B-60", "B-64"],
    "DEC-07": ["B-03", "B-24", "B-40", "B-41", "B-44", "B-46", "B-60", "B-64"],
    "GEO-13": ["B-13", "B-20", "B-30", "B-31", "B-32"],
    "GEO-14": ["B-11", "B-13", "B-20", "B-31", "B-32", "B-33"],
    "NIV-07": ["B-02", "B-20", "B-30", "B-32", "B-43", "B-60"],
    "STR-01": ["B-20", "B-21", "B-25", "B-42", "B-44", "B-45", "B-46"],
    "STR-02": ["B-12", "B-25", "B-40", "B-41", "B-42", "B-43"],
    "STR-03": ["B-32", "B-34", "B-42", "B-43", "B-48", "B-60"],
}

VAR_LABELS = {
    "CFG-01": ("Configuration de maturité MOE (CFG-1 à CFG-4)", "BLOQUANTE (dès B-00)"),
    "CFG-02": ("Gabarit d'opération (S / M / L-XL)", "BLOQUANTE (dès B-01)"),
    "CFG-03": ("Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types", "BLOQUANTE si L / XL ou R+n"),
    "DEC-05": ("Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut)", "BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE"),
    "DEC-06": ("Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés)", "BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE"),
    "DEC-07": ("Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx)", "BLOQUANTE si inconnue physique (Classe II)"),
    "GEO-13": ("Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU)", "BLOQUANTE"),
    "GEO-14": ("Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N", "BLOQUANTE en existant et en R+n"),
    "NIV-07": ("Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini", "BLOQUANTE"),
    "STR-01": ("Système global de contreventement, centre de torsion et descente des efforts horizontaux", "BLOQUANTE en neuf et restructuration"),
    "STR-02": ("Poussées des terres, surcharges de remblai et écrans de soutènement", "BLOQUANTE si sous-sol ou soutènement"),
    "STR-03": ("Carnet des réservations et trémies tous corps d'état (CVC / Plomberie / Élec / Ascenseur)", "NON BLOQUANTE (à défaut : PA-xx)"),
}

COMPLEMENT_COMMON = """
---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
"""

COMPLEMENT_BY_CODE = {
    "B-00": """
**Qualification `CFG-01` obligatoire.** B-00 qualifie la configuration de maturité MOE dès l'inventaire : `CFG-1` (aucun BET structure MOE), `CFG-2` (BET structure MOE en PDF ou principe DCE, sans DWG de coffrage), `CFG-3` (BET structure MOE vectoriel complet : DWG/DXF/IFC PRO-DCE + notes) ou `CFG-4` (mission partielle localisée). Cette qualification conditionne toute la suite : elle détermine qui conçoit, ce que nous transcrivons, et ce que nous ne demandons jamais.

**Interdiction de réclamer un livrable inexistant.** En `CFG-2` et `CFG-4`, il est **interdit** de demander un « DXF de coffrage MOE » : ce livrable n'existe pas dans ces configurations. La transcription vectorielle des ouvrages MOE et de leurs interfaces est notre production (`B-32` → `B-20`). En `CFG-1`, l'absence de BET structure MOE est un fait de mission, pas un blocage : la conception est produite en `INTERNE-GO` avec alerte contractuelle.

**Inventaire vectoriel exhaustif.** Pour chaque pièce, B-00 qualifie le mode d'exploitation : vecteur natif (DXF/DWG), PDF vectoriel (extraction des tracés et des textes), PDF raster (relevé déclaré, incertitude portée), IFC. Une pièce non vectorielle n'est jamais déclarée inexploitable sans avoir tenté l'extraction vectorielle et la reconnaissance de texte.
""",
    "B-01": """
**Choix du gabarit `CFG-02` et découpage `CFG-03`.** B-01 statue le gabarit d'opération : `S` (1 à 5 porteurs, < 100 m² ou ouvrage unique, avec ou sans BET MOE), `M` (100 à 2 500 m², un bloc unitaire) ou `L-XL` (> 2 500 m², joints de dilatation, niveaux-types, sous-sols, préfabrication). En `L-XL`, B-01 impose le découpage en blocs structurels `JD` et en niveaux-types (`CFG-03`) et active obligatoirement `B-25` (stabilité globale, contreventement, sismique) et `B-34` (synthèse des réservations).

**Voie compacte du gabarit `S`.** En gabarit `S`, la MPD est produite en trois portes seulement : `Porte 1` cadrage + calage et vue nettoyée + hypothèses `H-xx` ; `Porte 2` schéma mécanique `AVANT/APRÈS` + descente de charges + note de calcul ; `Porte 3` plan d'exécution tout-en-un (implantation, coupes, ferraillage ou assemblages, Points d'Arrêt, auto-contrôle). La voie compacte supprime des validations intermédiaires redondantes ; elle ne supprime aucune sortie ni aucun verrou.

**Preuve d'épuisement avant tout `BLOQUANTE`.** Une variable ne peut être déclarée `BLOQUANTE` qu'après la preuve d'épuisement `V14` de la totalité des pièces reçues. Le statut `NON NÉCESSAIRE` reste une décision humaine ligne à ligne et ne se justifie jamais par la disponibilité.
""",
    "B-03": """
**Registres séparés.** Le RDR tient désormais quatre registres distincts et non interchangeables : `D-xx` (décisions humaines datées et signées), `H-xx` (hypothèses notifiées sous nuage, avec valeur, norme d'appui, zone d'application et statut de visa), `PA-xx` (Points d'Arrêt chantier opposables, avec prescription `ENC` associée) et `V-xx` (verrous de Classe III, seuls bloquants).

**Délai de contradiction.** Chaque hypothèse `H-xx` est notifiée avec le délai contractuel `DEC-06` (2 jours ouvrés par défaut) : à l'expiration, l'hypothèse est réputée acceptée et le titulaire est exonéré des conséquences de l'écart, dans la limite de la norme d'appui citée.
""",
    "B-20": """
**Synthèse indissociable sur fond nettoyé.** B-20 travaille exclusivement sur le fond `B-32` (vue nettoyée : zéro cloison, zéro isolation, zéro doublage, zéro menuiserie de distribution) et produit une **synthèse structurelle complète sur une même vue** superposant `EXISTANT`, `DÉMOLITION` et `PROJET`. Il est interdit de traiter les pièces en silos, d'exclure un ouvrage du périmètre de la vue ou de déclarer un ouvrage « non plaçable ».

**Transcription vectorielle intégrale.** En `CFG-2` et `CFG-3`, les porteurs conçus par le BET MOE sont transcrits vectoriellement à 100 % sur le fond structurel pur, avec leurs interfaces et les ouvrages manquants (reprises, transferts, fondations non dessinées). En `CFG-1`, B-20 conçoit l'ensemble de la structure en `INTERNE-GO` et porte l'alerte contractuelle d'extension de mission et d'assurance.

**Continuité descendante et stabilité globale.** Toute trame produite est justifiée par une descente de charges continue `Toiture → Fondations` (`V15`), un système de contreventement identifié (`STR-01`) et, en `L-XL`, un découpage `JD` explicite. L'absence de fondations MOE n'autorise ni l'impasse ni la reproduction d'un modèle type : les fondations sont conçues ou transcrites, jamais omises.
""",
    "B-30": """
**Calage multi-sources vers le Repère Structurel Unique (`RSU`).** Le calage ne porte plus sur un seul fichier architecte : il intègre toutes les sources vectorielles disponibles et les PDF structure MOE (extraction des tracés), avec une matrice de recalage `GEO-13` consignant pour chaque source la transformation appliquée (translation, rotation, échelle) et le résidu mesuré sur les points témoins.

**Séquence imposée.** Le calage précède désormais l'audit et la conception : il s'exécute en `Phase 1`, immédiatement après le cadrage. Aucun audit de contradiction ni aucune conception ne s'appuie sur un fond non calé.

**Détection des unités et des rotations déclaratives.** Le script de calage vérifie systématiquement la cohérence des unités (mm/cm/m) et l'orientation déclarée avant tout ajustement ; un écart d'unité est corrigé par la transformation, jamais par déplacement de points.
""",
    "B-31": """
**Preuve de superposition multi-étages et multi-sources.** La preuve ne se limite plus au fichier architecte : elle superpose, niveau par niveau, `EXISTANT`, `DÉMOLITION` et `PROJET`, ainsi que la source structure MOE transcrite. Elle détecte les **porteurs non portés** : mur ou poteau interrompu entre deux niveaux sans ouvrage de transfert, ce qui constitue une non-conformité `V15` à corriger avant tout calcul.
""",
    "B-32": """
**Loi d'airain graphique.** La vue nettoyée supprime 100 % des cloisons, doublages, isolants, complexes de finition et menuiseries de distribution. Seuls subsistent : les porteurs (existants, conservés, démolis, neufs), les ouvertures mécaniques (baies, trémies, percements), la trémie et l'escalier, la structure neuve et les réservations techniques.

**Protocole CAO obligatoire en quatre temps.** (1) `INSERT` récursif multi-calques : reconnaissance des blocs imbriqués et reclassement des porteurs sur le calque structurel avant toute purge ; (2) retrait du complexe isolant et des doublages périphériques (décalage d'épaisseur vers le nu porteur) ; (3) purge spatiale des portes, cotes et hachures orphelines par distance aux segments porteurs ; (4) table explicite de correspondance `Plan Archi N ↔ PB/PH` et `nu brut ASB / nu fini` (`NIV-07`).

**Différentiel explicite.** La vue porte trois états graphiques distincts et lisibles (`EXISTANT` gris fin, `DÉMOLITION` pointillé, `PROJET` trait fort) et une légende normalisée. Une vue sans différentiel exploitable est refusée.
""",
    "B-10": """
**Ordre inversé.** L'audit croisé s'exécute désormais **après** le socle géométrique : B-10 lit les plans sur le fond calé et nettoyé (`B-30`, `B-32`), ce qui supprime les contradictions fantômes produites par les cloisons et les doublages.

**Preuve d'épuisement.** Avant d'inscrire une lacune, B-10 produit le journal d'épuisement `V14` : pièces examinées, passages, résultat par pièce. Une lacune non prouvée n'est pas une lacune : c'est une pièce non lue.
""",
    "B-11": """
**Exploitation du différentiel `EXISTANT / DÉMOLITION / PROJET`.** L'audit du diagnostic ne se limite plus aux désordres cités : il confronte chaque désordre à sa localisation réelle sur le fond calé et vérifie que les ouvrages conservés sont bien ceux que le projet sollicite (`GEO-14`).

**Zones non relevées.** Une zone non relevée n'est jamais un blanc : elle est soit couverte par une hypothèse `H-xx`, soit portée par une prescription `ENC` et un Point d'Arrêt `PA-xx` de reconnaissance.
""",
    "B-13": """
**Réconciliation quantitative multi-pièces.** Le tableau de contradictions intègre une matrice de réconciliation `Plans Archi ↔ Plans Structure ↔ CCTP/DPGF ↔ Diagnostic ↔ Géotechnique` : surfaces, linéaires de voiles, nombres d'ouvertures, sections annoncées. Un écart quantitatif est une contradiction au même titre qu'un écart de valeur.

**Recalage commun.** Toute contradiction de position est arbitrée sur le `RSU` (`GEO-13`) : deux cotes divergentes sont comparées après recalage, jamais sur des fonds différents.
""",
    "B-14": """
**Périmètre technique et périmètre de mission.** La matrice `INCLUS / EXCLU / À TRANCHER` distingue explicitement ce qui relève du périmètre de l'entreprise (lot gros œuvre / structure), du périmètre d'intervention d'autres lots (charpente, métallerie, réservations techniques) et du périmètre de mission (études d'exécution, synthèse, OPC).
""",
    "B-15": """
**Pré-Audit Flash d'Exécutabilité obligatoire.** Avant toute production, B-15 contrôle par ratios l'exécutabilité de l'ensemble du dossier, **y compris lorsqu'un BET structure MOE existe** : élancement de flèche sous maçonnerie (`L/h`), portance et dimension minimale des semelles (`q_Ed` vs `q_adm`, `B_min`), élancement des poteaux (`H_0/b`), compression locale sous appuis et sous appareils d'appui. Un ratio hors bornes produit un risque de criticité élevée et une demande de complément `T-04`, jamais un silence.
""",
    "B-21": """
**Descente de charges continue et différentielle.** La DDC préliminaire est établie par niveau et par bloc `JD`, en distinguant les charges de l'existant conservé, des démolitions et du projet neuf. Elle alimente directement `B-25` (stabilité globale) et l'ensemble des briques de calcul.
""",
    "B-22": """
**Note d'hypothèses `H-xx` unique et opposable.** Chaque hypothèse porte : valeur retenue, norme ou DTU d'appui, zone d'application, délai de contradiction (`DEC-06`), mode de report graphique (nuage). Une hypothèse sans norme d'appui n'est pas une hypothèse notifiée : c'est une valeur de repli interdite par le verrou `V3`.
""",
    "B-24": """
**Inconnue physique = Point d'Arrêt, jamais hypothèse silencieuse.** L'existant non sondé est traité par prescription `ENC` (sondage, dépose, fouille, curage) et Point d'Arrêt `PA-xx` (`DEC-07`), avec critère de lever explicite et conséquence chiffrée en cas de découverte défavorable. Le mode `HYPOTHÈSE-NOTIFIÉE` ne s'applique jamais à une inconnue physique mesurable sur site.
""",
    "B-25": """
**Brique nouvelle — stabilité globale et contreventement.** B-25 vérifie la stabilité d'ensemble : système de contreventement, cheminement des efforts horizontaux (vent `EC1`, séisme `EC8` selon zone et catégorie d'importance), centre de torsion et excentricités, joints de dilatation `JD`, effets du second ordre globaux et stabilité des piles en phase provisoire. Elle produit la justification de stabilité globale et le schéma de contreventement reporté sur les plans.
""",
    "B-33": """
**Vérification croisée globale.** B-33 quitte la phase géométrique et devient la vérification finale `Plan ↔ Plan ↔ Note ↔ Nomenclature` : cohérence des repères, des sections, des niveaux, des quantités, des réservations et des Points d'Arrêt. Elle s'exécute après `B-64` et conditionne `B-70`.
""",
    "B-34": """
**Brique nouvelle — synthèse des réservations techniques.** B-34 collecte, vérifie et synthétise l'ensemble des réservations et trémies tous corps d'état (CVC, plomberie, électricité, ascenseur, VRD), contrôle leur compatibilité avec la structure (position, dimension, distance aux rives, renforcement nécessaire) et produit le carnet de réservations unique reporté sur les plans.
""",
    "B-60": """
**Loi d'airain graphique et vérité du titre.** Les plans d'exécution ne contiennent **aucune** cloison, isolation, doublage ni menuiserie de distribution : uniquement les porteurs, les ouvertures mécaniques, la trémie et l'escalier, la structure neuve et les réservations. Le titre d'un plan doit correspondre exactement à son contenu géométrique complet : un plan intitulé « fondations » qui ne porte pas toutes les fondations est refusé.

**Zéro collision de textes.** Chaque plan est contrôlé par script : `0` chevauchement de textes, `0` cote orpheline, `0` entité sur le calque `0`. Un plan non contrôlé n'est pas diffusé.

**Report, jamais redessin.** Le plan reporte la géométrie du fond `B-32` et les éléments calculés ; il ne redessine jamais l'empreinte architecturale et n'invente aucune position.
""",
    "B-62": """
**Nomenclature issue du DXF contrôlé.** La nomenclature est extraite par script des calques normalisés du DXF effectivement produit et relu (`V13`), jamais ressaisie. Toute divergence entre quantités extraites et quantités annoncées dans la note est un écart bloquant.
""",
    "B-64": """
**Notice de synthèse et points d'arrêt.** La notice reprend les hypothèses `H-xx` actives, les prescriptions `ENC`, les Points d'Arrêt `PA-xx`, le mode d'exécution, les réservations `B-34` et les limites de mission. Elle constitue la pièce contractuelle de référence en cas d'écart d'exécution.
""",
    "B-70": """
**Contrôle des hypothèses et des Points d'Arrêt.** L'auto-contrôle de synthèse vérifie : statut et échéance de chaque hypothèse `H-xx` (active, expirée, acceptée, contredite), présence et opposabilité de chaque Point d'Arrêt `PA-xx`, `0` collision de textes sur les plans, adéquation titre ↔ contenu, et absence totale de second œuvre sur les vues structurelles.
""",
    "T-03": """
**Passage obligatoire du compilateur.** Aucune version du carnet n'est publiée sans exécution du compilateur de cohérence (`T1` à `T10`) et sans résultat `10/10 PASS` (zéro erreur, zéro avertissement). Le journal d'exécution est annexé à la version publiée.
""",
}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write(p: Path, t: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(t, encoding="utf-8")


def patch_pipe_row(text: str, key: str, new_value: str) -> str:
    pat = re.compile(r"^\| " + re.escape(key) + r" \| .*? \|$", re.M)
    if pat.search(text):
        return pat.sub(f"| {key} | {new_value} |", text, count=1)
    return text


def transform(path: Path, rel: str) -> str:
    text = read(path)
    text = normalize_tables_in_markdown(text, rel)

    # En-tête de fichier
    text = re.sub(r"^(Fichier .*?) — CARNAC v2\.6$", r"\1 — CARNAC v3.0", text, flags=re.M)
    # Version et révision
    text = patch_pipe_row(text, "Version", "3.0")
    text = patch_pipe_row(
        text,
        "Dernière révision",
        "v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi",
    )
    text = re.sub(r"^> Version du document : 2\.6 \(carnet CARNAC v2\.6\)", "> Version du document : 3.0 (carnet CARNAC v3.0)", text, flags=re.M)
    # Chemins du dictionnaire
    text = text.replace("CARNAC_v2.6_variables", "CARNAC_v3.0_variables")
    text = text.replace("carnet v2.5", "carnet v3.0")
    text = text.replace("Le carnet CARNAC (v1.1)", "Le carnet CARNAC (v3.0)")
    # Mentions historiques non verrouillées
    text = text.replace("Modifications depuis v1.0", "Journal des modifications (11_HISTORIQUE)")
    text = text.replace("12 verrous", "15 verrous")
    text = re.sub(r"\bcinq modes\b", "six modes", text, flags=re.I)
    text = text.replace("LES 5 MODES", "LES 6 MODES")
    text = text.replace("94 variables", "106 variables")
    text = text.replace("les 94 variables", "les 106 variables")
    text = text.replace("13 verrous", "15 verrous")
    text = text.replace("LES 13 VERROUS", "LES 15 VERROUS")

    # Phase d'exécution
    m = re.search(r"/([BT]-\d{2})_", rel)
    if m:
        code = m.group(1)
        ph = phase_for(code)
        if ph:
            text = patch_pipe_row(text, "Phase", ph)

    # Placeholders : garantir l'égalité prompt <-> Rappel V7
    m_sec = re.search(r"2\.\s*PROMPT(.*?)3\.\s*JUSTIFICATION", text, flags=re.S)
    if m_sec:
        sec = m_sec.group(1)
        m_rap = re.search(r"Rappel V7[^\n]*", sec)
        if m_rap:
            body = sec[: m_rap.start()]
            rappel = m_rap.group(0)
            body_ph = set(re.findall(r"\{\{([^{}\.]+)\}\}", body))
            rappel_ph = set(re.findall(r"\{\{([^{}\.]+)\}\}", rappel))
            if body_ph - rappel_ph:
                extra = sorted(body_ph - rappel_ph)
                new_rappel = rappel.rstrip() + " " + " ".join(f"Remplacer aussi {{{{ {p} }}}}." for p in extra)
                text = text.replace(rappel, new_rappel, 1)
            if rappel_ph - body_ph:
                extra = sorted(rappel_ph - body_ph)
                lines = text.splitlines()
                for idx, line in enumerate(lines):
                    if line.strip().startswith("MISSION :"):
                        lines.insert(idx + 1, "")
                        lines.insert(
                            idx + 2,
                            "MODE D'EXÉCUTION APPLIQUÉ : {{" + "}}, {{".join(extra) + "}}.",
                        )
                        break
                text = "\n".join(lines)

    # Complements v3.0 par fiche
    if m:
        code = m.group(1)
        if "### 5. COMPLÉMENT v3.0" not in text:
            text = text.rstrip() + "\n" + COMPLEMENT_COMMON
            if code in COMPLEMENT_BY_CODE:
                text = text.rstrip() + "\n" + COMPLEMENT_BY_CODE[code] + "\n"
            else:
                text = text.rstrip() + "\n"
    return text


def add_variable_rows(text: str, code: str) -> str:
    """Ajoute une ligne dans la table 'Variables consommées' de la fiche."""
    if f"| {code} |" in text:
        return text
    m = re.search(r"^Variables consommées$", text, flags=re.M)
    if not m:
        return text
    start = m.end()
    idx = text.find("\n| Code |", start)
    if idx == -1:
        return text
    end = text.find("\n\n", idx)
    block = text[idx:end]
    label, status = VAR_LABELS[code]
    row = f"\n| {code} | {label} | {status} |"
    return text[:end] + row + text[end:]


def main() -> None:
    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    for p in sorted(DST.rglob("*.md")):
        rel = str(p.relative_to(DST))
        write(p, transform(p, rel))

    # Injection des 12 variables v3.0 dans les fiches consommatrices
    for code, sheets in VAR_INJECT.items():
        for sheet in sheets:
            for p in DST.rglob(f"{sheet}_*.md"):
                write(p, add_variable_rows(read(p), code))

    print(f"Arborescence v3.0 préparée : {len(list(DST.rglob('*.md')))} fichiers Markdown")


if __name__ == "__main__":
    main()
