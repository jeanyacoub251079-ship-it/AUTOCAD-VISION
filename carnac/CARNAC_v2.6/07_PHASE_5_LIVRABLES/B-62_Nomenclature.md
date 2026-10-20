Fichier 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md — CARNAC v2.6
________________


B-62 — NOMENCLATURE ET FAÇONNAGE
1. EN-TÊTE
Champ
	Valeur
	Version
	2.6
	Dernière révision
	v2.6 — consolidation des corrections issues des relectures externes (voir Journal des modifications, entrée v2.6) ; fond de la fiche inchangé depuis sa dernière révision de fond
	Phase
	5 — Livrables
	Brique précédente
	B-60 (Plans d'exécution)
	Brique suivante
	B-64 (Notice de synthèse), B-70 (Auto-contrôle de synthèse), B-71 (Indiçage)
	Fréquence
	À chaque livrable graphique produit par B-60
	Modes d'appel
	COMPLET (B-60 produit en mode COMPLET) · PARTIEL-DÉCLARÉ (B-60 produit sous réserve) · PARAMÉTRIQUE (B-60 en mode PARAMÉTRIQUE : nomenclature partielle, non exécutable)
	Paramètre d'appel
	{{type_livrable}} = même paramètre que B-60 (FOND / VERT / PLANCHER / CHARPENTE / METAL / MACON / ESCALIER / PREDALLE / LINTEAU / ASSEMBLAGE)
	Entrées lues
	Plans B-60 (plan + coupes + détails + nomenclature graphique), note de calcul de la brique amont
	Sortie unique
	Nomenclature détaillée par élément + plan de façonnage des aciers (si BA) + tableau récapitulatif par calque + export tableur (CSV ou XLSX) pour la commande
	Critère d'acceptation
	Voir section 2 (dernier bloc du prompt)
	Quand appeler cette brique : après B-60, quand les plans sont produits. B-62 est la brique qui transforme les plans en liste de commande — elle extrait les éléments dessinés, les quantifie, et produit le document qui permet au fournisseur de livrer les barres, profilés ou connecteurs.
Ce que vous fournissez à l'IA : les plans produits par B-60 (plan général, coupes, détails, nomenclature graphique) et la note de calcul de la brique amont. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}}.
Ce que vous validez à la sortie :
   * la nomenclature détaillée (repère, désignation, section, longueur, quantité) ;
   * le plan de façonnage des aciers BA (formes, cotes, longueurs développées) ;
   * le tableau récapitulatif par calque (longueurs cumulées, poids, quantités) ;
   * l'export tableur (CSV ou XLSX) ;
   * le rapport de cohérence (éléments dessinés vs éléments nommés).
Ce que B-62 produit — le périmètre exact :
Élément
	Nature
	Nomenclature détaillée par élément
	Repère, désignation, section ou diamètre, longueur ou quantité, calque source
	Plan de façonnage (aciers BA)
	Formes des barres, cotes de façonnage, longueurs développées, recouvrements
	Tableau récapitulatif par calque
	Total par calque : longueurs cumulées, poids, quantités
	Export tableur
	CSV ou XLSX, prêt pour commande auprès du fournisseur
	Vérification de cohérence
	Chaque élément dessiné sur B-60 figure dans la nomenclature, et réciproquement
	Ce que B-62 ne produit jamais :
Exclu
	Renvoyé à
	Devis ou estimation financière
	Hors périmètre CARNAC
	Commande fournisseur
	Hors périmètre CARNAC
	Plans (déjà produits par B-60)
	B-60
	Notice de synthèse
	B-64
	Vérification de la cohérence plan ↔ plan
	B-33 (déjà fait)
	________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la nomenclature détaillée et le façonnage du livrable {{type_livrable}} de l'opération {{ID-01}} — {{ID-02}}, à partir des plans B-60 et de la note de calcul de la brique amont. Produire l'export tableur correspondant.


MÉTHODE — DANS CET ORDRE


Étape 1 — Vérification des entrées
- Plans B-60 disponibles (plan général, coupes, détails) ?
- Note de calcul de la brique amont disponible ?
- Nomenclature graphique intégrée aux plans disponible ?
Si une entrée manque, tu ne produis pas la nomenclature — tu signales et tu t'arrêtes.


Étape 2 — Extraction élément par élément
Pour chaque élément dessiné sur le plan (repères F1, S1, P1, etc.) :
- identifie sa nature (semelle, poteau, profilé, barre, etc.) ;
- identifie sa section ou son diamètre ;
- identifie sa longueur ou sa quantité ;
- identifie le calque source (FOND-ACIER-INF, VERT-ACIER-LONG, etc.).


Étape 3 — Nomenclature détaillée
Tableau par élément, puis tableau consolidé :
- repère (issu du plan) ;
- désignation (barre HA12, profilé HEB200, etc.) ;
- section ou diamètre ;
- longueur unitaire (mm) ou quantité ;
- nombre d'occurrences ;
- longueur totale (mm) ou quantité totale ;
- poids total (kg) si acier ;
- calque source.


Étape 4 — Plan de façonnage (aciers BA uniquement)
Pour chaque type de barre :
- forme (droite, équerre, U, cadre, épingle) ;
- cotes de façonnage (longueurs de chaque segment, angles) ;
- longueur développée ;
- longueur de recouvrement (si applicable) ;
- diamètre de mandrin (si cintrage) ;
- repère et quantité.


Étape 5 — Tableau récapitulatif par calque
Pour chaque calque (FOND-ACIER-INF, VERT-ACIER-LONG, etc.) :
- longueur cumulée ;
- poids cumulé (acier) ou volume (béton) ;
- quantité d'éléments.


Étape 6 — Vérification de cohérence
- Chaque élément dessiné sur B-60 figure dans la nomenclature.
- Chaque élément de la nomenclature figure sur B-60.
- Les quantités totales correspondent entre la nomenclature détaillée et le tableau récapitulatif.
Tout écart doit être signalé, pas corrigé par toi.


Étape 7 — Export tableur
- Format CSV (séparateur point-virgule, encodage UTF-8) ou XLSX.
- Colonnes : repère, désignation, section/diamètre, longueur unitaire, nombre, longueur totale, poids total, calque source.
- Une feuille par type (barres, profilés, connecteurs, etc.).


INTERDICTIONS
- Ne produis AUCUN devis ni estimation financière : hors périmètre CARNAC.
- Ne produis AUCUNE commande fournisseur : hors périmètre CARNAC.
- Ne redessine AUCUN élément : tu extrais des plans B-60.
- Ne fusionne pas plusieurs éléments dans une seule ligne : un repère = une ligne.
- Ne produis pas de nomenclature sans plan de façonnage (aciers BA) : les deux sont indissociables.
- Ne corrige pas un écart de cohérence : tu le signales, tu identifies la brique responsable (B-60 ou toi-même), tu renvoies.
- Ne produis pas de nomenclature exécutable si B-60 est en PARAMÉTRIQUE : nomenclature partielle et non exécutable, avec filigrane.


SORTIE
Pièce 1 — Nomenclature détaillée par élément.
Pièce 2 — Plan de façonnage (aciers BA).
Pièce 3 — Tableau récapitulatif par calque.
Pièce 4 — Export tableur (CSV ou XLSX).
Pièce 5 — Rapport de cohérence (éléments dessinés vs éléments nommés).


CRITÈRE D'ACCEPTATION
La nomenclature est acceptée si :
- chaque élément dessiné sur B-60 figure dans la nomenclature ;
- chaque élément de la nomenclature figure sur B-60 ;
- chaque ligne a un repère, une désignation, une section ou un diamètre, une longueur ou une quantité ;
- le plan de façonnage (aciers BA) est produit avec formes, cotes et longueurs développées ;
- le tableau récapitulatif par calque est produit ;
- l'export tableur est produit ;
- le rapport de cohérence est produit et ne présente aucun écart non signalé ;
- si B-60 est PARAMÉTRIQUE : nomenclature partielle, filigranée, non exécutable.
Si un seul de ces huit points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{type_livrable}} et {{mode}} (par COMPLET, PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
Clause
	Pourquoi
	Nomenclature + façonnage indissociables
	Une nomenclature sans façonnage est inutilisable en atelier. Le façonnage est le livrable qui permet au ferrailleur de plier les barres. Les séparer conduit à des allers-retours entre bureau et atelier
	Un repère = une ligne
	Un regroupement « HA12 : toutes les barres » ne permet pas de commander. Chaque repère est une ligne de commande potentielle — le fournisseur doit pouvoir identifier chaque type de barre
	Plan de façonnage avec longueur développée
	Un ferrailleur ne peut pas plier une barre sans sa longueur développée. La cote de façonnage et la longueur développée sont les deux données indispensables — sans elles, le ferrailleur improvise, et les barres ne rentrent pas dans le coffrage
	Vérification de cohérence obligatoire
	Un élément dessiné mais non nommé est un élément non commandé. Un élément nommé mais non dessiné est un élément en trop. Les deux sont des erreurs de production — et les deux se voient à l'exécution (barres manquantes ou en trop)
	Export tableur
	Sans export, la nomenclature est un tableau dans un PDF — inutilisable pour la commande. Le CSV/XLSX est le format d'échange avec le fournisseur
	« Ne corrige pas un écart de cohérence »
	Si le plan B-60 et la nomenclature divergent, c'est B-60 qui est faux (ou la nomenclature, mais c'est plus rare). C'est à la brique responsable de corriger — sinon on ne sait plus quel document fait foi
	Nomenclature non exécutable si B-60 PARAMÉTRIQUE
	Une nomenclature partielle qui ne porte pas de filigrane est une nomenclature qui sera commandée — et les barres seront coupées avant que la donnée manquante n'arrive. Le filigrane est la seule protection
	« Ne produis aucun devis ni commande »
	La nomenclature est un document technique, pas un document commercial. Le devis et la commande relèvent de l'économiste et du service achats — pas du bureau d'études
	Rapport de cohérence
	Le rapport est le document qui prouve que la vérification a été faite. Sans lui, la cohérence est une affirmation — et les erreurs ne sont pas détectées
	Les éléments de la nomenclature — précision utile :
Élément
	Unité
	Exemple
	Repère
	—
	F1, S1, P1, HA12-01
	Désignation
	—
	Semelle filante, poteau BA, barre HA12, HEB200
	Section / diamètre
	mm
	HA12, HEB200, 140×140×8
	Longueur unitaire
	mm
	3200, 4500
	Nombre
	—
	4, 12, 28
	Longueur totale
	mm
	12800, 54000
	Poids
	kg
	45,3, 320,7
	Calque source
	—
	FOND-ACIER-INF, VERT-ACIER-LONG
	Le piège du façonnage : un modèle qui reçoit un plan de ferraillage a tendance à produire une nomenclature sans façonnage (juste les barres, sans les formes). C'est insuffisant :
   * le ferrailleur ne peut pas plier une barre sans sa forme (droite, équerre, U, cadre, épingle) ;
   * il ne peut pas plier sans la longueur développée (longueur totale dépliée) ;
   * il ne peut pas plier sans le diamètre de mandrin (si cintrage).
Une nomenclature sans façonnage est une nomenclature qui oblige le ferrailleur à interpréter le plan — et qui produit des barres fausses.
Le piège de la cohérence : un modèle qui reçoit un plan de ferraillage et une note de calcul a tendance à :
   * soit recopier le plan sans vérifier la cohérence avec la note (le plan peut être faux) ;
   * soit corriger le plan (ce qui est le rôle de B-60, pas de B-62).
Les deux sont faux :
   * recopier sans vérifier, c'est produire une nomenclature qui peut être fausse ;
   * corriger le plan, c'est produire une nomenclature qui ne correspond plus au plan.
La seule réponse correcte est : vérifier la cohérence, signaler les écarts, renvoyer à B-60 pour correction.
Le piège du mode PARAMÉTRIQUE : si B-60 a produit un plan PARAMÉTRIQUE (par exemple, un plan de verticaux avec SEC-01 manquante), B-62 produit une nomenclature partielle :
   * les éléments dont les dimensions sont connues sont nommés ;
   * les éléments dont les dimensions dépendent de la donnée manquante sont omis ou marqués « EN ATTENTE » ;
   * la nomenclature porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * elle ne peut pas être commandée — les barres manquantes seront commandées quand la donnée arrivera.
Une nomenclature PARAMÉTRIQUE qui ne porte pas de filigrane est une nomenclature qui sera commandée — et les barres seront coupées avant que la donnée n'arrive.
________________


4. RÉFÉRENCES
Briques amont
Brique
	Ce qu'elle fournit à B-62
	B-60 (Plans d'exécution)
	Les plans produits (plan, coupes, détails, nomenclature graphique) — B-62 en extrait la nomenclature détaillée
	B-30 (Calage)
	Le fichier recalé — B-62 utilise le calage pour identifier les positions si nécessaire
	B-32 (Vue nettoyée)
	La vue nettoyée — B-62 s'appuie sur cette vue pour vérifier la cohérence
	Brique de calcul (B-40 à B-50)
	La note de calcul — B-62 vérifie la cohérence entre les quantités du plan et celles de la note
	Briques aval
Brique
	Ce qu'elle consomme de B-62
	B-64 (Notice de synthèse)
	La nomenclature — B-64 la cite dans la notice
	B-70 (Auto-contrôle de synthèse)
	Le rapport de cohérence — B-70 vérifie que la cohérence a été faite
	B-71 (Indiçage)
	La nomenclature produite — B-71 l'indice et gère la supersession
	Service achats (hors CARNAC)
	L'export tableur — le service achats l'utilise pour la commande
	Variables consommées
Code
	Libellé
	Statut dans B-62
	MAT-01 à MAT-04
	Matériaux BA
	BLOQUANTE (pour nomenclature BA)
	MAT-05
	Nuance d'acier métallique
	BLOQUANTE (pour nomenclature métallique)
	MAT-06
	Classe de bois
	BLOQUANTE (pour nomenclature bois)
	MAT-09 à MAT-11
	Maçonnerie (blocs, mortier)
	BLOQUANTE (pour nomenclature maçonnerie)
	ID-01
	Code projet
	BLOQUANTE
	ID-02
	Intitulé de l'opération
	BLOQUANTE
	Variables produites
B-62 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (nomenclature + façonnage + export tableur + rapport de cohérence) qui alimente B-64, B-70, B-71 et le service achats.
Documents de référence
Document
	Contenu
	Fichier
	Document maître
	Principes, verrous, modes
	00_MASTER.md
	Dictionnaire de variables
	MAT-01 à MAT-11, ID-01, ID-02
	01_DICTIONNAIRE/CARNAC_v2.6_variables.csv
	Conventions de livrables
	Nomenclature type, unités, formats
	10_ANNEXES/A_Conventions_Livrables.md
	Journal des modifications
	Modifications depuis v1.0
	11_HISTORIQUE/Journal_des_modifications.md
	Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-62, vous devez valider la nomenclature avant transmission au fournisseur. Une erreur de quantité commandée coûte cher — soit en sur-commande (coût), soit en sous-commande (retard de chantier). Le modèle propose, vous validez.
Cas particulier — mode PARAMÉTRIQUE : si B-60 est en mode PARAMÉTRIQUE, B-62 produit une nomenclature partielle :
   * les éléments dont les dimensions sont connues sont nommés ;
   * les éléments dont les dimensions dépendent de la donnée manquante sont marqués « EN ATTENTE DE [donnée] » ;
   * la nomenclature porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
   * elle ne peut pas être commandée.
Le chef de chantier doit être informé que la nomenclature n'est pas complète — et que les barres manquantes seront commandées quand la donnée arrivera.
Cas particulier — nomenclature d'aciers BA : la nomenclature d'aciers BA comporte :
   * la liste des barres par diamètre et par repère ;
   * le plan de façonnage (formes, cotes, longueurs développées) ;
   * le tableau récapitulatif par calque (longueurs cumulées, poids).
Le plan de façonnage est indissociable de la nomenclature — c'est le document qui permet au ferrailleur de plier les barres.
Cas particulier — nomenclature de profilés métalliques : la nomenclature de profilés métalliques comporte :
   * la liste des profilés par type (HEA, HEB, IPE, UPE, tubes) ;
   * les longueurs et quantités ;
   * les poids cumulés ;
   * les connecteurs (boulons, soudures, platines) — renvoi à B-50 pour le calcul, B-62 pour la nomenclature.
La nomenclature métallique est souvent plus courte que la nomenclature BA — mais elle est aussi importante pour la commande.
Cas particulier — nomenclature de maçonnerie : la nomenclature de maçonnerie comporte :
   * les blocs (classe, dimensions, quantités) ;
   * le mortier (classe, volume) ;
   * les chaînages (section, longueur) ;
   * les raidisseurs (section, longueur) ;
   * les armatures de maçonnerie armée (ratios, longueurs).
La nomenclature de maçonnerie est souvent moins détaillée que la nomenclature BA — mais elle doit être complète pour la commande.
Cas particulier — écart entre plan et note : si un écart existe entre le plan B-60 et la note de calcul (par exemple, une section de barre différente), B-62 le signale dans son rapport de cohérence. C'est B-60 ou la brique amont qui doit corriger — pas B-62 qui doit arbitrer.
Cas particulier — export tableur : l'export tableur (CSV ou XLSX) comporte une feuille par type d'élément (barres, profilés, connecteurs, blocs). Chaque feuille est triée par repère, avec les colonnes standardisées. Le service achats peut utiliser directement cet export pour la commande.
Format de sortie attendu : cinq pièces distinctes (nomenclature détaillée, plan de façonnage, tableau récapitulatif, export tableur, rapport de cohérence). La nomenclature porte le filigrane si B-60 est en mode PARAMÉTRIQUE.
Consignation : la nomenclature B-62 est annexée au RDL (Registre des Livrables) — elle documente les quantités produites et permet la mise à jour incrémentale en cas de modification de source.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. Sans environnement d'exécution (OUT-01), elle ne peut pas être déclarée COMPLET ; elle est suspendue ou exécutée en PARAMÉTRIQUE documentaire (spécification du script, sans livrable). Toute mention d'un contrôle « simulé » est une non-conformité V13.
