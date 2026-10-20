# Annexe O — COUCHE OUTILLAGE ET PROTOCOLE CAO (refondue en v3.0)
> Version du document : 3.0 (carnet CARNAC v3.0) — historique des modifications : 11_HISTORIQUE/Journal_des_modifications.md.

## 1. OBJET
Cette annexe définit l'environnement d'exécution et les protocoles qui rendent le verrou V13 applicable. Elle est fonctionnelle et neutre (V10) : elle décrit des capacités, pas des produits. Les exemples d'outils sont interchangeables : bibliothèque de lecture/écriture DXF (type ezdxf), bibliothèque d'extraction vectorielle PDF (type PyMuPDF), moteur de rendu (type matplotlib/CairoSVG), interpréteur de calcul (type Python).

Elle s'applique à toutes les briques en **régime outillé** : B-30, B-31, B-32, B-33, B-40 à B-50 (applications numériques), B-60, B-62.

## 2. ENVIRONNEMENT D'EXÉCUTION (variable OUT-01)
Avant toute brique outillée, l'environnement est déclaré et consigné :
- interpréteur et version majeure ;
- bibliothèques utilisées et leur rôle (lecture DXF, extraction PDF, calcul, rendu, écriture DXF) ;
- capacité d'écriture de fichiers persistants (les livrables et les scripts survivent à la session) ;
- capacité de relecture des fichiers produits.

Si l'environnement n'est pas disponible, la brique outillée ne peut pas être déclarée COMPLET : elle est suspendue (PTD) ou exécutée en PARAMÉTRIQUE documentaire (spécification du script à produire, sans livrable).

## 3. PROTOCOLE SCRIPT (variable OUT-02)
Chaque production outillée suit les cinq temps suivants, sans exception :

1. **Écriture du script.** Le modèle écrit un script complet, lisible, commenté, qui lit les fichiers sources réels (jamais des coordonnées recopiées de mémoire) et produit le livrable.
2. **Exécution.** Le script est exécuté. Toute erreur est diagnostiquée et le script corrigé ; on ne contourne pas une erreur en produisant le résultat « à la main ».
3. **Relecture réelle.** Le fichier produit (DXF, PDF, tableau) est rouvert par un second script ou une seconde passe qui énumère et compte : calques présents, nombre d'entités par calque, cotes lues, positions contrôlées. C'est ce comptage, et lui seul, qui vaut « test de relecture ». Toute mention du type « réouvre le fichier (simulé) » est une non-conformité V13.
4. **Contrôle visuel.** Un rendu du livrable (PNG) est produit et lu. Le contrôle visuel vérifie la plausibilité (pas d'élément dans le vide, pas d'appui manquant, pas de collision de textes) ; il ne remplace ni le comptage ni le calcul.
5. **Journalisation (OUT-03).** Le journal d'exécution est consigné avec le livrable : script (nom, version), fichiers d'entrée (nom, indice, taille), paramètres, comptages de relecture, écarts constatés et leur traitement.

Les scripts sont conservés dans le dossier du livrable et versionnés avec lui : un livrable sans son script n'est pas reproductible, donc pas clos.

## 4. RÈGLES D'EXTRACTION GÉOMÉTRIQUE
Ces règles codifient les échecs rencontrés en pratique ; elles sont impératives en phase 3 et 5.

1. **Vectoriel d'abord.** La géométrie provient des coordonnées vectorielles des fichiers (entités DXF, chemins PDF), jamais d'une image, d'une proportion d'écran ou d'une estimation visuelle.
2. **Rendu pleine page.** Tout rendu de contrôle d'un PDF est produit en pleine page à résolution fixe (300 dpi) puis découpé ; les rendus rognés à la volée introduisent des décalages d'échelle et sont interdits comme base de mesure.
3. **Unités vérifiées, pas déclarées.** L'unité réelle du fichier est vérifiée sur au moins deux cotes connues avant tout calcul de transformation. Une unité déclarée incohérente avec les cotes est signalée et traitée dans la transformation (B-30).
4. **Continuité ≠ identité.** Un segment continu n'est pas forcément un mur ; l'identification d'un élément (mur, limite de terrasse, joint) se fait par convergence d'indices (épaisseur, calque, cotes, annotations), jamais sur la seule géométrie. Pour les parois porteuses, cette convergence est formalisée par le protocole B-32 §R (critères C1 à C6, classes PORTEUR CERTAIN / NON PORTEUR / À LEVER).
5. **Distorsion connue.** Un fond PDF peut être localement distordu par rapport au DXF : le calage est alors local (par zone ou par niveau), avec résidus par zone, plutôt qu'une transformation globale forcée.
6. **Aucun élément sans appui.** Tout élément produit (profilé, poteau, semelle) est rattaché par le script à ses appuis identifiés dans la source ; le journal liste les éléments dont l'appui n'a pas été trouvé — ils ne sont pas dessinés.

## 5. PROTOCOLE CALCUL (briques B-40 à B-50)
1. Chaque application numérique d'une note de calcul est produite par le script de calcul versionné avec la note (OUT-02) ; la note cite le script et ses sorties.
2. Le script expose, pour chaque vérification : les données d'entrée (avec leur code FDC), la formule littérale, la référence normative, le résultat et le taux de travail.
3. Les contrôles de cohérence internes (unités, ordres de grandeur, cas limites) sont codés dans le script ; un résultat aberrant arrête la production, il n'est pas « corrigé » dans le texte de la note.
4. En cas de correction d'une hypothèse (B-22), le script est ré-exécuté intégralement ; les notes ne sont jamais rattrapées par des retouches numériques locales.

## 6. PROTOCOLE DXF
1. Écriture selon l'annexe A (calques normalisés, unités millimètres, aucun élément sur le calque 0, calques de travail supprimés à l'export).
2. Relecture systématique : ouverture du DXF produit, comptage des entités par calque, comparaison aux comptages attendus du script de production. Tout écart est un écart de production, signalé avant diffusion.
3. Le DXF livré et le PDF livré proviennent du même script et de la même exécution ; un DXF régénéré séparément est un nouveau livrable, re-vérifié.

## 7. JOURNAL D'EXÉCUTION (variable OUT-03) — FORMAT MINIMAL
| Champ | Contenu |
|---|---|
| Livrable | Code, indice, brique source, mode |
| Script | Nom, version, date d'exécution |
| Entrées | Fichiers lus (nom, indice, taille), variables FDC consommées |
| Paramètres | Transformation de calage, seuils GEO-12, hypothèses H-xx |
| Relecture | Comptages par calque, cotes contrôlées, résidus mesurés |
| Visuel | Rendu produit et lu (oui/non), anomalies relevées |
| Écarts | Écarts constatés, diagnostic, traitement (correction du script / réserve R-xx) |
| Verdict | Conforme / conforme avec réserves / à reprendre |

## 8. INTERDICTIONS DE LA COUCHE OUTILLAGE
- Interdit de déclarer un contrôle « fait » sans journal OUT-03.
- Interdit de produire un livrable graphique « à la main » dans la conversation (coordonnées inventées ou recopiées d'une image).
- Interdit de masquer une erreur d'exécution en reformulant le résultat attendu.
- Interdit de livrer un DXF dont la relecture comptée n'a pas été comparée aux attendus.
- Interdit de réutiliser un script d'un autre projet sans revalider ses entrées (fichiers, unités, calage).

---

## 9. PROTOCOLE CAO DE NETTOYAGE STRUCTUREL (nouveau en v3.0)

Le nettoyage d'un fond de plan n'est jamais une suppression « au feeling » : c'est une suite de quatre opérations contrôlées, scriptées et journalisées.

### 9.1 Étape 1 — Reconnaissance des blocs et reclassement (`INSERT` récursif)
1. Parcours récursif de toutes les références de blocs (`INSERT`), y compris imbriquées.
2. Pour chaque entité rencontrée, détermination du calque *effectif* (calque du bloc, calque de l'insertion, calque des entités internes) : le calque porteur est celui de l'entité interne, jamais celui de l'insertion.
3. Reclassement des entités porteuses sur le calque structurel normalisé (annexe A §2) **avant** toute purge : une purge réalisée avant reclassement détruit des porteurs.
4. Journal : nombre de blocs parcourus, profondeur maximale, entités reclassées par calque d'origine et de destination.

### 9.2 Étape 2 — Retrait du complexe isolant et des doublages
1. Identification des enveloppes de doublage par épaisseur, position relative au nu porteur et calque d'origine.
2. Suppression de l'enveloppe, conservation du **nu porteur** (le plan de structure cote le nu brut, jamais le nu fini).
3. Report systématique de la correspondance `nu brut ASB / nu fini` et `Plan Archi N / PB / PH` dans la table `NIV-07` (§9.5).
4. Journal : épaisseurs retirées par façade, nu conservé, écarts de niveau induits.

### 9.3 Étape 3 — Purge spatiale des portes, cotes et hachures orphelines
1. Détection des entités non porteuses : portes, fenêtres, mobilier, hachures de revêtement, cotes de second œuvre.
2. Filtrage par distance : une entité est conservée si elle est à moins de 22 cm d'un segment porteur **et** si sa fonction est mécanique (baie, percement, trémie) ; sinon elle est purgée.
3. Contrôle inverse obligatoire : aucune ouverture mécanique réelle ne doit disparaître. Le script compare le nombre d'ouvertures avant/après et exige l'égalité sur les baies et trémies déclarées.
4. Journal : entités purgées par catégorie, ouvertures conservées, écart éventuel justifié.

### 9.4 Étape 4 — Recalage multi-sources vers le Repère Structurel Unique (`RSU`)
1. Pour chaque source vectorielle secondaire (plan structure MOE en PDF vectoriel, DXF de diagnostic, relevé géomètre), extraction des tracés et des textes.
2. Appariement des points homologues avec la source de référence, puis calcul de la transformation (similarité : translation, rotation, échelle ; affinité seulement si anisotropie justifiée).
3. Mesure du résidu sur des points témoins **non utilisés** au calage, avec seuils de l'annexe A et du document maître §5.
4. Consignation dans la matrice `GEO-13` : source, indice, points appariés, transformation, résidu maximal, résidu acceptable, statut.
5. Journal : nombre de sources recalées, résidus, sources refusées et motif.

### 9.5 Table de correspondance des niveaux et des épaisseurs (`NIV-07`)
| Plan architecte | Plancher bas (PB) | Plancher haut (PH) | Nu brut ASB | Nu fini | Épaisseur de complexe |
| --- | --- | --- | --- | --- | --- |
| Niveau `N` | cote `PB_N` | cote `PH_N` | cote `ASB_N` | cote `FINI_N` | `FINI_N − ASB_N` |

Règle : aucune cote de niveau n'est reprise d'un plan architecte sans passer par cette table. Un écart non renseigné est un écart bloquant pour B-43 et B-60.

### 9.6 Contrôle de rendu et anti-collision de textes
1. Extraction de toutes les entités texte et de leurs boîtes englobantes réelles (après rotation).
2. Détection des chevauchements deux à deux ; seuil exigé : `0` chevauchement sur tout plan diffusé.
3. Détection des cotes orphelines (aucune entité cotée à moins de 22 cm) et des entités sur le calque `0`.
4. Détection des entités de second œuvre résiduelles sur les calques de structure.
5. Journal : nombre de textes contrôlés, collisions détectées, collisions corrigées, collisions résiduelles (doit être nulles).
