"""Deterministic Architecture Process reference implementation."""

from .contracts import (
    FRAMEWORK_VERSION,
    SCHEMA_VERSION,
    RUBRIC_VERSION,
    ContractError,
    validate_config,
    validate_records,
)
from .persistence import (
    ConcurrentRevisionError,
    atomic_write_json,
    load_checkpoint,
    save_checkpoint,
)
from .scoring import evaluate_project, score_checks

__all__ = [
    "FRAMEWORK_VERSION", "SCHEMA_VERSION", "RUBRIC_VERSION",
    "ContractError", "validate_config", "validate_records",
    "ConcurrentRevisionError", "atomic_write_json", "load_checkpoint", "save_checkpoint",
    "evaluate_project", "score_checks",
]

