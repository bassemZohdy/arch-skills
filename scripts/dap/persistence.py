from __future__ import annotations

import hashlib
import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any

class ConcurrentRevisionError(RuntimeError):
    pass
def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
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
def load_checkpoint(path: Path, project: Path | None = None) -> dict[str, Any]:
    if not path.exists():
        return {"revision": 0, "state": None}
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or type(document.get("revision")) is not int or document["revision"] < 1:
        raise ValueError("checkpoint must contain a positive integer revision")
    if not isinstance(document.get("state"), dict) or document.get("state_hash") != content_hash(document["state"]):
        raise ValueError("checkpoint state hash mismatch or missing state")
    if project is not None:
        from .snapshot import Snapshot
        if document["state"].get("subject_hash") != Snapshot(project).subject_hash():
            raise ValueError("checkpoint references a changed artifact baseline; reconcile before resuming")
    return document
@contextmanager
def exclusive_lock(path: Path):
    """Fail closed on contention; stale locks require explicit operator recovery."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ConcurrentRevisionError(f"operation locked: {path}; inspect interrupted operation before recovery") from exc
    try:
        os.write(fd, str(os.getpid()).encode("ascii"))
        os.close(fd)
        yield
    finally:
        path.unlink()


def save_checkpoint(path: Path, state: dict[str, Any], expected_revision: int | None = None) -> dict[str, Any]:
    if not isinstance(state, dict):
        raise ValueError("checkpoint state must be an object")
    if type(expected_revision) is not int or expected_revision < 0:
        raise ValueError("explicit nonnegative expected_revision required")
    with exclusive_lock(path.with_suffix(path.suffix + ".lock")):
        return _save_checkpoint(path, state, expected_revision)


def _save_checkpoint(path, state, expected_revision):
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

