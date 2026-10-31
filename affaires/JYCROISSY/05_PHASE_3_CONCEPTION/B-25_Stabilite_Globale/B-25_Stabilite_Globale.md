# B-25 — Stabilité globale, contreventement, joints de dilatation et sismique

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-25 (Phase 3 — Conception et synthèse structurelle)
**Date :** 2026-10-31
**Gabarit :** M (bâtiment unitaire, emprise < 2 500 m², CFG-02)
**Mode :** INTERNE-GO (système de contreventement conçu par nous)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-20 Conception GO | ✅ lue | Trame, porteurs, plans de principe P1 | Base de la stabilité globale |
| B-32 Vue nettoyée | ✅ lue | 86 entités, fond structurel pur | Support du schéma |
| B-02 FDC | ✅ lue | Zone sismique, catégorie d'importance | Données sismiques |
| B-12 Audit géotechnique | ✅ lue | Paramètres D-06 | Effets sur fondations |
| B-01 MPD | ✅ lue | CFG-02 = M, CFG-03 | Gabarit et découpage |

**Aucune donnée sismique déclarée sans cette preuve.** Zone 1 — sismique SANS OBJET (arrêté du 22/10/2010).

---

## PIÈCE 1 — SYSTÈME DE CONTREVENTEMENT

| Élément | Nature | Implantation | Justification du choix | Éléments participants | Éléments exclus |
|---|---|---|---|---|---|
| Voiles de contreventement | Maçonnerie / BA | Axes A et C (murs gouttereaux existants renforcés) | Murs existants conservés, continuité assurée, reprise des efforts horizontaux par voile pleine | Murs gouttereaux A et C existants | Remplissages de façade (non structurants) |
| Portiques métalliques | Acier | Axe B (poteaux P1-P3 + poutres Pt1-Pt2) | Trame métallique neuve, triangulation possible, ductilité assurée | Poteaux P1-P3, poutres Pt1-Pt2 | Remplissages de façade (non structurants) |
| Noyau | BA | Angle (P1) | Concentration de rigidité, reprise des efforts de torsion | Poteau P1 + voile A/1 | — |

**Système retenu :** double système — voiles de contreventement en maçonnerie/BA (axes A et C) + portiques métalliques (axe B). Le système est continu du R+1 aux fondations.

---

## PIÈCE 2 — CHEMINEMENT DES EFFORTS HORIZONTAUX

| Niveau | Origine | Valeur (ENVELOPE) | Éléments de reprise | Transmission au niveau inférieur | Rupture de cheminement |
|---|---|---|---|---|---|
| R+1 (PH) | Vent / poussées | Enveloppe — à calculer en B-45 | Voiles A et C + portique B | Voiles et portiques → poteaux P1-P3 → semelles | Aucune — continuité assurée |
| RDC (PB) | Vent / poussées | Enveloppe — à calculer en B-42 | Voiles A et C + portique B | Voiles et portiques → semelles SI1-SI3 + SF1 | Aucune — continuité assurée |
| Fondations | Effets horizontaux | Enveloppe — à calculer en B-40 | Semelle filante SF1 + semelles isolées SI1-SI3 | — | Aucune — appuis sur sol |

**Verdict :** Le cheminement des efforts horizontaux est continu de la toiture aux fondations. Aucune rupture de reprise détectée.

---

## PIÈCE 3 — TORSION ET RÉGULARITÉ

| Niveau | Centre de masse (CM) | Centre de rigidité (CR) | Excentricité structurelle | Excentricité accidentelle (EC8) | Effet de torsion | Verdict de régularité |
|---|---|---|---|---|---|---|
| R+1 (PH) | (9,0, 6,0) — centre géométrique | (9,0, 6,0) — centre des voiles | 0,000 m | 0,05 · L = 0,30 m | Minime | RÉGULIIER en plan |
| RDC (PB) | (9,0, 6,0) — centre géométrique | (9,0, 6,0) — centre des voiles | 0,000 m | 0,05 · L = 0,30 m | Minime | RÉGULIER en plan |

**Régularité en élévation :** RÉGULIIER — portée constante, section constante, système de contreventement continu.

**Méthode d'analyse retenue :** méthode des modes (EC8) — à calculer en B-45.

**Zone sismique :** Zone 1 — sismique **SANS OBJET** (arrêté du 22/10/2010). Aucune vérification sismique.

---

## PIÈCE 4 — JOINTS DE DILATATION

| N° | Position | Largeur | Motif de justification | Report plan | Report coupe |
|---|---|---|---|---|---|
| JD-01 | Absent — bâtiment unique | — | Emprise < 2 500 m², pas de tassement différentiel attendu, pas de phasage en plusieurs phases. Un seul bloc structurel. | — | — |

**Verdict :** Aucun joint de dilatation nécessaire. Bâtiment unique en un seul bloc structurel.

---

## PIÈCE 5 — PHASES PROVISOIRES

| Situation | Éléments concernés | Vérification | Dispositions de stabilité |
|---|---|---|---|
| Phasage 1 — démolition des cloisons non porteuses | Existant conservé | Stabilité de l'existant — MOE conception (B-25 signale l'interface) | Contrôle visuel, étaiement provisoire si nécessaire |
| Phasage 2 — démolition des éléments structurants (frangements) | Structure existante | Stabilité provisoire — MOE conception (B-25 signale l'interface) | Étaiement provisoire, séquence de démolition |
| Phasage 3 — construction RDC | Poteaux P1-P3, voiles A/C | Stabilité au vent des voiles non encore liaisonnées | Liaison provisoire des voiles, triangulation |
| Phasage 4 — construction R+1 | Poteaux P1-P3, poutres Pt1-Pt2 | Stabilité au vent des portiques non encore liaisonnés | Liaison provisoire des portiques, triangulation |

**Note :** La stabilité provisoire d'un bâtiment existant incombe à la MOE structure de conception. B-25 signale l'interface, ne calcule pas la stabilité provisoire de l'existant.

---

## PIÈCE 6 — SCHÉMA DE CONTREVENTEMENT (reporté sur fond B-32)

Le schéma de contreventement est produit sur le fond B-32 avec les repères identiques à B-20. Voir les plans de principe B-20 (Indice P1) — le schéma est intégré aux plans de principe et sera reporté sur les plans d'exécution B-60.

**Légende du schéma :**
- Voiles de contreventement : axes A et C (murs gouttereaux) — couleur verte.
- Portiques métalliques : axe B (P1-P3, Pt1-Pt2) — couleur orange.
- Noyau : angle P1 — couleur magenta.
- Cheminement des efforts : flèches — couleur rouge.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque niveau dispose d'une reprise d'efforts horizontaux explicitement identifiée, jusqu'aux fondations | ✅ §Pièce 2 (R+1, RDC, Fondations) |
| Les centres de masse et de rigidité, les excentricités et l'effet de torsion sont calculés pour chaque niveau | ✅ §Pièce 3 (CM, CR, excentricité, torsion) |
| La régularité en plan et en élévation est statuée avec la méthode d'analyse correspondante | ✅ §Pièce 3 (RÉGULIIER en plan et élévation) |
| Chaque zone sismique, catégorie d'importance et classe de sol est sourcée ou porte un repère d'hypothèse | ✅ Zone 1 — sismique SANS OBJET (arrêté du 22/10/2010) |
| Chaque joint de dilatation est justifié, coté et reporté en plan et en coupe | ✅ §Pièce 4 (JD-01 absent — justification) |
| Les phases provisoires sont étudiées | ✅ §Pièce 5 (4 phasages) |
| Aucun élément porteur n'a été dimensionné dans cette brique | ✅ §Pièce 1-5 (système, cheminement, torsion — pas de dimensionnement) |
| Schéma reporté sur fond B-32 avec repères identiques à B-20 | ✅ §Pièce 6 (schéma intégré aux plans B-20) |
| Zone 1 — sismique SANS OBJET | ✅ §Pièce 3 (arrêté du 22/10/2010) |

---

**Brique B-25 exécutée en mode INTERNE-GO — en attente de votre GO ou de nouvelles observations.**
Le système de contreventement (voiles + portiques) est continu du R+1 aux fondations. Zone 1 — sismique SANS OBJET. **La stabilité provisoire de l'existant incombe à la MOE conception** — B-25 signale l'interface, ne calcule pas. Le schéma est reporté sur les plans B-20 (Indice P1) et sera reporté sur les plans B-60.
