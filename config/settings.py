import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def staticFiles(folder: str, filename: str) -> str:
    return os.path.join(BASE_DIR, "static", folder, filename)
