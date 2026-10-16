"""Point d'entrée : `python -m structai` (et start.sh).

- démarre uvicorn sur le port 8000 (si occupé : port suivant, §2.4.3) ;
- purge les anciens snapshots au lancement (§5.10.2) ;
- ouvre le navigateur (sauf STRUCTAI_NO_BROWSER=1 ou STRUCTAI_HOST défini).
"""
from __future__ import annotations

import argparse
import os
import socket
import threading
import time
import webbrowser


def _free_port(start: int, host: str) -> int:
    for port in range(start, start + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind((host, port))
                return port
            except OSError:
                continue
    return start


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="structai", description="StructAI — serveur local")
    ap.add_argument("--host", default=os.environ.get("STRUCTAI_HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("STRUCTAI_PORT", "8000")))
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--dev", action="store_true", help="rechargement à chaud")
    args = ap.parse_args(argv)

    from .config import ensure_dirs
    from .logging_setup import setup_logging
    ensure_dirs()
    setup_logging()

    from .db import get_db
    with get_db() as db:  # crée/migre la base
        db.execute("SELECT 1")

    from .projects import purge_old_snapshots
    from .config import load_settings
    try:
        n = purge_old_snapshots(int(load_settings()["retention"]["snapshots_jours"]))
        if n:
            print(f"[StructAI] purge de maintenance : {n} snapshot(s) expiré(s) supprimé(s).")
    except Exception as exc:
        print(f"[StructAI] purge au lancement ignorée : {exc}")

    port = _free_port(args.port, args.host)
    url = f"http://{'localhost' if args.host in ('0.0.0.0', '127.0.0.1') else args.host}:{port}"
    print(f"\n  StructAI — {url}   (Ctrl+C pour quitter)\n")

    if not args.no_browser and not os.environ.get("STRUCTAI_NO_BROWSER"):
        def _open():
            time.sleep(1.4)
            try:
                webbrowser.open(url)
            except Exception:
                pass
        threading.Thread(target=_open, daemon=True).start()

    import uvicorn
    from .api import create_app
    app = create_app()
    from .api import mount_frontend
    mount_frontend(app)
    uvicorn.run(app, host=args.host, port=port, log_level="warning",
                reload=args.dev)


if __name__ == "__main__":
    main()
