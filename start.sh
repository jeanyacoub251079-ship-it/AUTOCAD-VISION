#!/usr/bin/env bash
# StructAI — démarrage local : environnement Python, (build frontend si Node
# disponible) puis serveur sur http://localhost:8000 (port suivant si occupé).
set -euo pipefail
cd "$(dirname "$0")"

PY=${PYTHON:-python3}

if [ ! -d .venv ]; then
  echo "[StructAI] création de l'environnement virtuel Python…"
  "$PY" -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
echo "[StructAI] installation des dépendances…"
pip install -q --disable-pip-version-check -r requirements.txt

if [ ! -f web/dist/index.html ]; then
  if command -v npm >/dev/null 2>&1; then
    echo "[StructAI] build de l'interface React…"
    (cd web && npm install --no-audit --no-fund && npm run build) \
      || echo "[StructAI] build web ignoré — backend seul."
  else
    echo "[StructAI] Node/npm absent — backend seul (UI non construite)."
  fi
fi

echo "[StructAI] lancement sur http://localhost:8000 (Ctrl+C pour quitter)"
exec python -m structai "$@"
