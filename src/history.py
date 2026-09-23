"""
Local persistence for Daily Tarot readings.

The core library and CLI are otherwise stateless; this is the only module
that touches disk. Storage is a single JSON file, written atomically.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from .core import daily_reading


def _default_history_path() -> Path:
    """Resolve the default history file path, honoring TAROT_READER_HOME.

    Read at call time (not import time) so it can be overridden per-call,
    e.g. in tests.
    """
    home = os.environ.get("TAROT_READER_HOME", str(Path.home() / ".tarot-reader"))
    return Path(home) / "history.json"


def _load(path: Path) -> Dict[str, Dict[str, Any]]:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _save(path: Path, history: Dict[str, Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(".tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
    os.replace(tmp_path, path)


def record_daily_reading(
    personal_seed: Optional[str] = None, path: Optional[Path] = None
) -> Dict[str, Any]:
    """
    Compute today's daily reading and persist it to the local history file.

    Safe to call repeatedly on the same day: daily_reading() is
    deterministic, so each call overwrites today's entry with the same
    value rather than creating duplicates or conflicting entries.

    Args:
        personal_seed: Optional personal information for a personalized
                      daily card
        path: Optional override for the history file location (defaults
              to TAROT_READER_HOME/history.json or ~/.tarot-reader/history.json)

    Returns:
        The reading dict that was saved (see core.daily_reading)
    """
    resolved_path = Path(path) if path else _default_history_path()
    reading = daily_reading(personal_seed)

    history = _load(resolved_path)
    history[reading["date"]] = reading
    _save(resolved_path, history)

    return reading


def get_daily_history(path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """
    Return all saved daily readings, sorted oldest to newest by date.

    Args:
        path: Optional override for the history file location
    """
    resolved_path = Path(path) if path else _default_history_path()
    history = _load(resolved_path)
    return [history[d] for d in sorted(history.keys())]
