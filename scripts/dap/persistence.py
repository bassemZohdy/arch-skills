from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any

class ConcurrentRevisionError(RuntimeError):
    pass
def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
def content_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()
def atomic_write_json(path: Path, value: Any) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical_json(value)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    return hashlib.sha256(data).hexdigest()
def load_checkpoint(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"revision": 0, "state": None}
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or not isinstance(document.get("revision"), int):
        raise ValueError("checkpoint must contain an integer revision")
    return document
def save_checkpoint(path: Path, state: dict[str, Any], expected_revision: int | None = None) -> dict[str, Any]:
    current = load_checkpoint(path)
    if expected_revision is not None and current["revision"] != expected_revision:
        raise ConcurrentRevisionError(
            f"checkpoint changed: expected {expected_revision}, found {current['revision']}"
        )
    document = {
        "revision": current["revision"] + 1,
        "state": state,
    }
    document["state_hash"] = content_hash(state)
    atomic_write_json(path, document)
    return document

