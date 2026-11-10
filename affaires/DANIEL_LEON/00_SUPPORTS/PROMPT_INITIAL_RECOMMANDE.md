# Prompt initial recommandé — Retranscription DXF d'une planche de permis de construire

> Document de méthode. Il décrit **le prompt qui aurait produit directement le livrable**
> `DANIEL_LEON_PC1975_PLAN_COUPE_SURFACES_v2.dxf`, et pourquoi chaque bloc est nécessaire.
> À réutiliser tel quel pour toute nouvelle planche (remplacer les champs `[entre crochets]`).

---

## 0. Version courte (prompt express, ~12 lignes)

```text
RÔLE : Projecteur / dessinateur projeteur bâtiment, spécialiste DAO (DXF) et relevé de plans anciens.

OBJECTIF : retranscrire en DXF la planche scannée jointe ([affaire], [commune], [date estimée]),
échelle d'origine [0.02 P.M. = 1/50], comprenant [plan RDC] + [coupe A-B] + [tableau de surfaces].

LIVRABLES : affaires/[AFFAIRE]/01_PLAN/[AFFAIRE]_PLAN_COUPE_SURFACES_v1.dxf
            + contrôle (rapport texte) + PDF A1 au 1/50 + PNG d'aperçu
            + journal de relevé (méthode, hypothèses, réserves).

CONTRAINTES : travail 100 % local (Python + ezdxf, OpenCV pour la mesure) — aucun service
de conversion en ligne. Unités mm, DXF R2013 (AC1027), calques normalisés, cotes associatives.
Ne jamais inventer une cote : ce qui n'est pas lisible est marqué comme hypothèse.

MÉTHODE IMPOSÉE : caler l'échelle sur 2 cotes d'ensemble, relever les faces de murs par
profils d'encre, reconstruire un réseau de murs dont les surfaces recalculées retrouvent
celles du cartouche, puis contrôler automatiquement et itérer jusqu'à l'écart nul.

ACCEPTATION : chaîne de cotes qui se referme exactement, ≥ 5 surfaces exactes au cm²,
audit DXF sans erreur, aucun texte vide, planche lisible A1.

RÉPONSE : montrer le rendu PNG, lister les écarts chiffrés et les réserves, indiquer les
fichiers produits et la commande de régénération.
```

Le reste du document détaille chaque bloc : c'est la version « longue » à utiliser pour un
livrable professionnel.

---

# PROMPT DÉTAILLÉ (version longue)

## 1. Rôle et posture

```text
Tu es projeteur / dessinateur bâtiment (20 ans de pratique, plans d'architecte et plans
d'exécution), expert DAO (AutoCAD/DXF) et relevé de plans anciens (permis de construire
des années 1950-1980, tirages papier pliés, photographiés au téléphone).

Tu travailles comme dans un bureau d'études : tu mesures avant de dessiner, tu chiffres tes
incertitudes, tu livres des fichiers propres, nommés et reproductibles.
Tu es en droit de dire « cette cote est illisible » — tu ne complètes jamais au hasard.
```

*Pourquoi* : sans rôle explicite, un agent produit un « joli dessin » ; avec le rôle, il
produit un **document technique** avec des réserves.

## 2. Objet et pièce jointe

```text
Pièce jointe : [nom_fichier].jpeg — reproduction photographique d'une planche de permis de
construire, [format px], document plié (2 plis visibles), papier jauni, encre bleue/noire.

Identification relevée sur le document (à confirmer / corriger si je me trompe) :
- Maître d'ouvrage : [M. et Mme X]
- Localisation : [commune, département], lotissement [nom + n° de lot]
- Objet : [construction d'une résidence principale]
- Échelle : [0.02 P.M. = 1/50] — cartouche [entreprise, dessinateur, date]
- Contenu de la planche : [plan RDC] + [coupe A-B] + [tableau de surfaces RDC et combles]

Si une information du cartouche est illisible, écris-le dans les réserves au lieu de l'inventer.
```

*Pourquoi* : l'identification sert de **garde-fou de calage** (échelle déclarée) et évite les
erreurs de contexte (bonne commune, bonne affaire, bon dossier).

## 3. Livrables attendus (chemins et noms imposés)

```text
Arborescence imposée (respecte les conventions du dépôt) :
affaires/[AFFAIRE]/
├── 00_SUPPORTS/
│   ├── 00_SOURCE/[source].jpeg          (copie de la pièce jointe)
│   ├── build_[affaire]_dxf.py           (générateur paramétrique, rejouable)
│   ├── controle_dxf.py                  (contrôle automatique)
│   ├── export_pdf.py / render_dxf.py    (PDF A1 1/50 + PNG d'aperçu)
│   └── PROMPT_INITIAL_RECOMMANDE.md
├── 01_PLAN/
│   ├── [AFFAIRE]_PLAN_COUPE_SURFACES_v1.dxf   ← LIVRABLE PRINCIPAL
│   ├── ..._A1.pdf                             (planche au 1/50)
│   └── ..._apercu.png                         (contrôle visuel)
├── JOURNAL_RETRANSCRIPTION.md          (méthode, calculs, réserves)
└── README.md                           (résumé de l'affaire)

Exigences de forme :
- scripts exécutables en une commande, sans argument obligatoire (chemins par défaut) ;
- aucune dépendance payante ; lister les dépendances dans le README ;
- le DXF doit être reproductible à l'identique (géométrie paramétrée, pas de « dessin à la main ») ;
- versionner les livrables, jamais les fichiers temporaires ni les rendus intermédiaires.
```

*Pourquoi* : c'est le bloc qui fait la différence entre « un DXF » et « un livrable déposé dans
une affaire ». Il fixe aussi la **traçabilité** (le script EST la note de calcul).

## 4. Spécifications techniques du DXF

```text
- Version : AC1027 (AutoCAD 2013) ; ouverture testée sans avertissement.
- Unités : millimètres réels ($INSUNITS = 4), 1 unité = 1 mm.
- Calques nommés, colorés, avec épaisseurs de trait :
    MURS_EXT (0.50) · CLOISONS (0.35) · HACHURES (0.13) · OUVERTURES (0.25)
    MENUISERIES (0.25) · ESCALIER (0.25) · SANITAIRES (0.18) · TERRASSE (0.18)
    COTES (0.18) · TEXTES (0.18) · AXES (0.13) · COUPE (0.35)
    CARTOUCHE (0.25) · TABLEAU (0.18)
- Cotation : cotes **associatives** (entités DIMENSION, style dédié, texte en mètres, 2 décimales),
  pas de texte « posé » à côté d'un trait.
- Murs : polylignes fermées + hachures pleines dans l'épaisseur (rendu lisible sans AutoCAD).
- Textes : hauteurs cohérentes (0.10 à 0.30 m) ; aucun texte vide ; pas de superposition.
- Mise en page : feuille A1 (841 × 594 mm), fenêtre au 1/50 ; cadre de feuille tracé dans
  l'espace objet à l'échelle réelle (42.00 × 29.70 m).
- Le fichier doit rester lisible : titre de planche, légende des calques, échelle graphique,
  cartouche complet, tableaux, repère Nord.
```

*Pourquoi* : « fais un DXF » laisse l'agent choisir des unités en mètres, des calques
`Layer1`, des textes non cotés. Ces 8 lignes suppriment 90 % des reprises.

## 5. Contenu graphique exigé

```text
PLAN DU REZ-DE-CHAUSSEE
- murs extérieurs et cloisons à leur épaisseur réelle (relevée ou déduite des cotes) ;
- toutes les baies : portes, portes-fenêtres, fenêtres, porte de garage, porte de service,
  avec tableaux, ébrasements, vantaux et arcs de débattement ;
- escalier : nombre de marches, sens de montée, largeur d'emmarchement ;
- équipements figurés sur l'original (sanitaires, évier, baignoire, cheminée, conduit de fumée) ;
- terrasses / auvents / débords, avec leur surface ;
- noms des pièces + surface de chaque pièce ;
- cotation : chaîne complète du document, cotes d'ensemble, cotes des baies, cotes de terrasse ;
- trait de coupe A-B, repère Nord.

COUPE A-B
- sol naturel + remblai, dallage, semelles filantes, murs coupés hachurés, plancher, charpente ;
- pentes et abouts de toiture, débords, conduit de fumée, escalier ;
- cotes de hauteur (sol, sous-plafond, égout, faîtage, hauteur totale) ;
- textes de matériaux (couverture, pente).

CARTOUCHE ET ANNEXES
- cartouche reconstitué à l'identique (maître d'ouvrage, objet, entreprise, échelle, date) ;
- tableau des surfaces : valeurs du document **et** valeurs recalculées, colonne d'écart ;
- tableau des menuiseries (repère, désignation, L × H, façade) ;
- légende des calques, échelle graphique, note de contrôle dimensionnel.
```

*Pourquoi* : c'est la **liste de contrôle d'omission** — sans elle, on oublie systématiquement
les ébrasements, les arcs de porte, la légende ou le repère Nord.

## 6. Méthode de relevé imposée (le cœur du travail)

```text
1. CALAGE : identifie deux cotes d'ensemble sur le document et calcule le facteur pixel -> mètre
   (ici 15.00 m en largeur, 7.00 m en profondeur). Vérifie la cohérence de l'échelle dans les
   deux directions (document éventuellement déformé : facteurs X et Y séparés).

2. MESURE : relève les positions des faces de murs par analyse d'image (profils d'encre,
   morphologie), pas « à l'œil ». Documente les positions en pixels puis en mètres.

3. RECONSTRUCTION : construis un réseau de murs **fermé et cohérent** (épaisseurs constantes) ;
   la géométrie doit respecter simultanément la chaîne de cotes et les surfaces.

4. VERROUILLAGE PAR LES SURFACES : recalcule toutes les surfaces et compare-les au cartouche.
   Objectif : écart nul sur un maximum de pièces (c'est la meilleure preuve du calage).
   N'ajuste une cote que si elle reste compatible avec la chaîne de cotes.

5. ÉCARTS ASSUMÉS : si une pièce ne tombe pas juste, ne force pas la géométrie en silence :
   signale l'écart, explique la cause (cloison non cotée, cote illisible), propose la vérification.

6. CONTRÔLE : audit automatique du DXF (intégrité, calques attendus, présence de cotes et de
   textes, étendue), rendu PNG de la planche entière + zooms, correction, itération.

7. TRACE : journal listant source, calage, chaîne de cotes, table des surfaces, hypothèses,
   réserves, commandes de reproduction.
```

*Pourquoi* : c'est ce qui distingue une **retranscription** (fidèle, vérifiable) d'une
**reproduction approximative**. La règle « verrouiller par les surfaces » est l'astuce
décisive : elle transforme une lecture subjective en contrôle chiffré.

## 7. Ce qu'il est interdit de faire

```text
- inventer une cote, une hauteur, une épaisseur ou une dimension de menuiserie sans le dire ;
- « lisser » ou déplacer un mur pour faire tomber une surface juste sans le signaler ;
- utiliser un service en ligne de conversion image -> DXF, ou un convertisseur automatique
  non contrôlé (vecteurs en escalier, illisibles) ;
- livrer un DXF en mètres si les mm sont demandés, ou avec des calques génériques ;
- livrer sans les réserves ni la liste des points à vérifier sur l'original.
```

*Pourquoi* : le risque métier n'est pas l'imprécision, c'est **l'imprécision silencieuse**.

## 8. Critères d'acceptation (à vérifier avant de rendre)

```text
[ ] La chaîne de cotes du document se referme EXACTEMENT (ex. : total = 1500 cm).
[ ] Au moins 5 surfaces recalculées = surfaces du cartouche, au cm² près.
[ ] Écarts restants documentés et expliqués (pas de correction silencieuse).
[ ] Audit DXF : 0 erreur ; 14 calques attendus présents ; aucune entité orpheline.
[ ] Aucun texte vide, aucun texte superposé (contrôle sur rendu PNG).
[ ] Planche lisible en A1 au 1/50 ; cartouche complet ; légende et échelle graphique présentes.
[ ] PDF + PNG de contrôle fournis ; jeu de scripts rejouable en une commande.
[ ] Journal des réserves : au moins les points illisibles et les hauteurs estimées.
```

## 9. Format de la réponse finale attendue

```text
1. Identification du document (affaire, commune, objet, échelle, date).
2. Ce qui a été produit (chemins des fichiers, formats, nombre d'entités/calques).
3. Preuve du calage : chaîne de cotes + tableau surfaces (document / calculé / écart).
4. Rendu de la planche (image).
5. Réserves et points à vérifier sur l'original (liste courte, hiérarchisée).
6. Commande de régénération.
```

## 10. Rappel sur la contrainte « fournisseur / modèles »

Si l'intention est de restreindre les modèles utilisés (Claude Opus, GPT…), formule-la comme une
**contrainte opérationnelle**, pas comme un nom :

```text
Contraintes d'environnement :
- exécution locale (Python, OpenCV, ezdxf, matplotlib) — pas de service cloud de conversion ;
- ne transmettre à un service externe aucune donnée identifiante (nom du client, adresse) ;
- si un service externe est utilisé, indiquer lequel et pour quelle étape.
```

*Pourquoi* : « utilise exclusivement Claude Opus » ne change pas la qualité du livrable et empêche
l'agent de choisir l'outil adapté (par ex. calcul géométrique déterministe plutôt que génération).
Ce qui compte pour un plan, c'est la **méthode mesurable** et l'**absence de sortie du poste**.

---

## Tableau : bloc de prompt → problème évité

| Bloc | Sans lui, on obtient… | Avec lui, on obtient… |
|---|---|---|
| Rôle | un dessin décoratif | un document technique |
| Pièce jointe identifiée | contresens sur l'affaire ou l'échelle | calage guidé par l'échelle déclarée |
| Livrables nommés | fichiers `plan.dxf`, `output(1).pdf` | dépôt propre dans l'affaire |
| Spécifications DXF | mètres, calque `0`, textes non cotés | mm, 14 calques, cotes associatives |
| Liste du contenu | oublis (ébrasements, Nord, légende) | planche complète |
| Méthode imposée | « à peu près » | calage chiffré, écart nul prouvé |
| Interdits | corrections silencieuses | hypothèses explicites |
| Critères d'acceptation | livraison non vérifiée | contrôle automatique avant envoi |
| Format de réponse | résultat brut | résultat + preuves + réserves |

---

## Bonus : les 6 questions à poser *avant* de lancer

1. Format et version DXF souhaités (R2013 ? mm ? échelle papier ?).
2. Faut-il le niveau combles (souvent non fourni) ou seulement le RDC ?
3. Les surfaces du cartouche font-elles foi, ou le relevé graphique prime-t-il en cas d'écart ?
4. Faut-il les hauteurs réelles (relevé sur site) ou les hauteurs estimées suffisent-elles ?
5. Nommage / arborescence imposés par le bureau (norme interne, calques de charte) ?
6. Diffusion : interne, client, ou dépôt (impact sur les mentions de réserve) ?
