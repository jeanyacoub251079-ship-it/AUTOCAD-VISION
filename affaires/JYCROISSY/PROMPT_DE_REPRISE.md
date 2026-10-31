# PROMPT DE REPRISE — à copier-coller au début de la prochaine session

---

Reprends la session JYCROISSY / AUTOCAD-VISION.

**Branche** : `arena/cc8aea0e-autocad-vision` (fixe — ne pas renommer/switcher).
**Clone** : `/home/user/AUTOCAD-VISION`.

**PRIME** : lis en priorité ces deux documents (ils contiennent tout le contexte) :
- `affaires/JYCROISSY/CONTEXTE_REPRISE_JYCROISSY.md`
- `affaires/JYCROISSY/journal_deploiement_drive.md`

**État** : Phases 0 à 4 = **COMPLÈTES** (B-00 à B-50). Rien n'est en attente technique.

**À faire immédiatement en réveil** :
1. Recréer le `.venv` :
   `python3 -m venv /home/user/.venv && pip install ezdxf==1.4.5 matplotlib pypdf pdfminer.six`
2. Vérifier `git status` / `git log --oneline -5` sur la branche.
3. Relire le `CONTEXTE_REPRISE_JYCROISSY.md` (règles, ancrages, pièges ezdxf).

**Règles permanentes (ne pas transgresser)** :
- GO **strictement lexical** ; une brique à la fois ; arrêt et attente de mon **GO** à chaque porte.
- **Pas** d'arbitrage de contradiction par le modèle — on signale, on ne tranche pas.
- **Pas** de valeur de repli / « pratique courante » : chaque valeur porte **source + fiabilité** ou **VERROU**.
- Ressources modèle : EXCLUSIVEMENT « Claude Opus (Anthropic) » ou « ChatGPT ASTR (OpenAI) » ; valeurs sourcées aux **pièces**, jamais à des suppositions.
- **NE TENTE PLUS DE MODIFIER CARNAC** (froidé, laisser comme artifact).
- Docs de production → **Google Drive** (sous-dossier JYCROISSY `1X_hSPVvEVMDr3ZsV-5hhpUgjXegrUBUk`) ; GitHub → code uniquement.

**Pièges ezdxf 1.4.5 (déjà connus)** : ne PAS set `alignment` sur TEXT ; `add_text` sur `msp` (modelspace) pas `Drawing` ; `add_rectangle` n'existe → `add_lwpolyline(..., close=True)`.

**Pièces** : 208_FLORA_DIAG structure.pdf, 208_FLORA_Plans_DCE_IndC.dxf, 208_FLORA_DCE_Pièces graphiques_IndC.pdf, 24.09.356E DCE indice C FLORA 16.03.2026.pdf, CCTP LOT 01 GROS OEUVRE - STRUCTURES, CARNAC v3.0.2.

**Demande au user au reprendre** : le prochain GO (brique/phase suivante) — ou confirmation qu'il n'y a rien de pending.
