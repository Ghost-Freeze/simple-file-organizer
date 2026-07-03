from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ScannedFile:
    path: Path
    size: int


def scan_directory(root: Path, recursive: bool = False) -> list[ScannedFile]:
    """Return all files directly inside `root` (or recursively, if requested)."""
    root = Path(root)
    if not root.is_dir():
        raise NotADirectoryError(f"{root} is not a directory")

    # Pick pathlib method based on recursive flag
    pattern_iter = root.rglob("*") if recursive else root.glob("*")

    files = []
    for entry in pattern_iter:
        # Skip hidden files/folders
        if any(part.startswith(".") for part in entry.relative_to(root).parts):
            continue
        # Only files, no folders
        if entry.is_file():
            files.append(ScannedFile(path=entry, size=entry.stat().st_size))
    return files