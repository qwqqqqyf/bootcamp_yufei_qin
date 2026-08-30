import os
from pathlib import Path


def project_root() -> Path:
    """Return the project root, allowing an explicit PROJECT_ROOT override."""
    return Path(os.getenv("PROJECT_ROOT", Path(__file__).resolve().parents[1]))


def data_path(kind: str = "raw") -> Path:
    """Return and create a project data directory."""
    if kind not in {"raw", "processed"}:
        raise ValueError("kind must be 'raw' or 'processed'")
    path = project_root() / "data" / kind
    path.mkdir(parents=True, exist_ok=True)
    return path
