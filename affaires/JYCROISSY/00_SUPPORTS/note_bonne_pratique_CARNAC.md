# Note de bonne pratique — Persistance des artifacts et gestion des données en session

**Statut** : proposition d'amélioration du cahier des charges CARNAC (à valider par l'utilisateur avant insertion).
**Date** : 2026-10-23.
**Contexte** : le CARNAC s'exécute dans un environnement de session. Certains artifacts ne sont garantis que pendant la durée de la session.

---

## Contexte

Le CARNAC s'exécute dans un environnement de session (une session = un échange continu avec l'utilisateur). Certains artifacts ne sont garantis que pendant la durée de la session :

- L'**environnement technique** (outils, bibliothèques de lecture/calcul) ;
- Les **données brutes** (PDF, DXF, etc.) ;
- Les **fichiers intermédiaires** (tableaux de variables, journaux techniques, scripts).

À chaque nouvelle session, ces artifacts peuvent avoir disparu.

## Règles

1. **Les livrables validés sont la source de vérité.** Une fois qu'un livrable est validé par l'utilisateur, il est pérenne et fait foi. Il ne doit jamais être supprimé ou modifié sans une nouvelle décision datée.
2. **Les données brutes sont des entrées externes.** Elles doivent être re-fournies au début de chaque session si elles ont disparu. Le verrou V14 (preuve d'épuisement) s'applique à chaque nouvelle exploitation.
3. **Les fichiers intermédiaires doivent être versionnés avec les livrables.** Si un fichier intermédiaire disparaît, il doit être **reconstruit à partir des livrables validés** — jamais supposé, jamais comblé par une valeur de repli (verrou V3).
4. **L'environnement technique doit être recréé au début de chaque session.** La persistance de l'environnement n'est garantie qu'à l'intérieur d'une session.
5. **Toute reconstruction d'un artifact perdu doit être traçable.** Le journal d'exécution doit mentionner l'origine de la reconstruction (quel livrable validé a été utilisé comme source).

## Implémentation

- Variables concernées : OUT-01 (environnement d'exécution), OUT-02 (script versionné), OUT-03 (journal d'exécution), OUT-04 (rendu de contrôle), DOC-01 à DOC-09 (données).
- Les livrables validés sont annexés au RDR (B-03) et constituent la source de vérité persistante.
- Toute reconstruction est consignée dans le journal d'exécution (OUT-03).

## Emplacement dans le cahier des charges

**Recommandé** : `10_ANNEXES/O_Outillage.md`, dans la section sur l'outillage et l'environnement (ajouter une sous-section « Persistance des artifacts et reconstruction »).

**Alternative** : `10_ANNEXES/D_Mode_Emploi.md`, section sur la gestion des données en session.

**Pourquoi `O_Outillage.md`** : les variables d'outillage (OUT-01 à OUT-04) sont définies dans ce fichier ; la note sur la persistance de l'environnement et des artifacts s'y rattache naturellement. Un lien vers `D_Mode_Emploi.md` permet de renvoyer au mode d'emploi.
