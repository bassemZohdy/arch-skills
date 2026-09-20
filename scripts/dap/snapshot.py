"""Explicit byte snapshots; evaluation never rereads mutable inputs mid-calculation."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from .contracts import ContractError, FILES, FRAMEWORK
from .persistence import content_hash

BEGIN = "<!-- DAP EVALUATION BEGIN -->"
END = "<!-- DAP EVALUATION END -->"
REQUIRED = set(FILES.values()) | {"architecture.md", "process/config.json", "process/state.json",
    "process/reviews.json", "process/assessment.json", "process/history.jsonl"}


def normalized(path, data):
    if path == "architecture.md":
        text = data.decode("utf-8")
        if text.count(BEGIN) != text.count(END) or text.count(BEGIN) > 1:
            raise ContractError("invalid generated appendix markers")
        if BEGIN in text:
            if text.index(END) < text.index(BEGIN):
                raise ContractError("reversed appendix markers")
            text = re.sub(re.escape(BEGIN) + r"[\s\S]*?" + re.escape(END), "", text)
        return text.rstrip().encode("utf-8") + b"\n"
    return data


def local_path(root, name):
    if not isinstance(name, str) or not name or "\\" in name or Path(name).is_absolute() or ".." in Path(name).parts:
        raise ContractError(f"unsafe relative artifact path: {name}")
    if Path(name).as_posix() != name or name == '.':
        raise ContractError(f'noncanonical artifact path: {name}')
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ContractError(f"artifact escapes root: {name}")
    resolved = path.relative_to(root.resolve())
    if not resolved.parts or resolved.parts[0] == 'evaluations' or resolved.name.endswith('.lock'):
        raise ContractError(f"generated/lock artifact cannot be assessed: {name}")
    return path


class Snapshot:
    def __init__(self, root, config_path=None):
        self.root = Path(root).resolve()
        self.external_config = Path(config_path).resolve() if config_path else None
        control = local_path(self.root, "process/manifest.json")
        manifest_bytes = control.read_bytes()
        try:
            specification = json.loads(manifest_bytes)
            names = specification["files"]
        except (ValueError, KeyError, TypeError) as exc:
            raise ContractError("manifest must contain an explicit files array") from exc
        if not isinstance(names, list) or any(not isinstance(x, str) for x in names) or len(set(names)) != len(names):
            raise ContractError("manifest files must be unique strings")
        if not REQUIRED.issubset(names):
            raise ContractError(f"manifest missing required files: {sorted(REQUIRED - set(names))}")
        self.data = {name: local_path(self.root, name).read_bytes() for name in names}
        self.data["process/manifest.json"] = manifest_bytes
        self.data["@rubric"] = (FRAMEWORK / "criteria-catalog.json").read_bytes()
        self.data["@schema"] = (FRAMEWORK / "project-schema.json").read_bytes()
        if self.external_config:
            self.data["@config"] = self.external_config.read_bytes()
        self.manifest = self._manifest()

    def _manifest(self):
        files = [{"path": name, "sha256": hashlib.sha256(normalized(name, data)).hexdigest(), "bytes": len(normalized(name, data))}
                 for name, data in sorted(self.data.items())]
        result = {"normalization": "raw bytes; architecture excludes one DAP appendix and normalizes trailing whitespace",
                  "files": files, "sha256": content_hash(files)}
        if self.external_config:
            result["external_config"] = str(self.external_config)
        return result

    def json(self, name):
        try:
            return json.loads(self.data[name], parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
        except (KeyError, ValueError) as exc:
            raise ContractError(f"invalid/missing assessed JSON {name}: {exc}") from exc

    def evidence(self, locator):
        """Resolve local, frozen evidence; remote citations need a captured source record."""
        if not isinstance(locator, str):
            return False
        name, _, fragment = locator.partition("#")
        if name not in self.data or name.startswith("@"):
            return False
        body = normalized(name, self.data[name]).decode("utf-8", errors="replace")
        if not body.strip():
            return False
        if fragment.startswith("/"):
            try:
                item = json.loads(body)
                for part in fragment[1:].split("/"):
                    if re.search(r'~(?![01])', part):
                        return False
                    part = part.replace("~1", "/").replace("~0", "~")
                    if isinstance(item, list):
                        if not re.fullmatch(r'0|[1-9][0-9]*', part):
                            return False
                        item = item[int(part)]
                    else:
                        item = item[part]
                return item is not None and item != ""
            except (ValueError, KeyError, TypeError, IndexError):
                return False
        return not fragment or fragment in body

    def subject_hash(self):
        # Approval/checkpoint/assessment records bind this subject without a self-reference.
        excluded = {"process/reviews.json", "process/assessment.json", "process/state.json", "process/history.jsonl",
                    "process/exceptions.json", "process/manifest.json"}
        return content_hash([x for x in self.manifest["files"] if x["path"] not in excluded])

    def unchanged(self):
        try:
            return Snapshot(self.root, self.external_config).manifest["sha256"] == self.manifest["sha256"]
        except (OSError, ValueError):
            return False


def report_is_stale(root, report):
    try:
        config = report["input_manifest"].get("external_config")
        return Snapshot(root, config).manifest["sha256"] != report["input_manifest"]["sha256"]
    except (KeyError, OSError, ValueError):
        return True
