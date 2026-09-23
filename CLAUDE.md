# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A lightweight Python tarot reading library (`src/`), a text-based CLI, and an optional async FastAPI REST API (`api/`). Core library has zero dependencies; the API is an optional extra (`pip install tarot-reader[api]`).

## Commands

```bash
# Install in editable mode with dev extras
pip install -e ".[dev]"

# Run all tests
python -m unittest discover tests
# or
pytest

# Run a single test file / test case
pytest tests/test_core.py
pytest tests/test_core.py::TestCore::test_draw_single_returns_dict

# Lint / format / type-check (as run in CI)
ruff check src/ tests/
black --check src/ tests/
mypy src/

# Run the interactive CLI (top-level script, imports from src)
python3 cli.py

# Run the argparse-based CLI entry point (installed as `tarot-reader`)
python -m src --type three --seed "INFP"
python -m src --type daily --seed "INFP"   # deterministic per calendar day, saved to local history

# Override where Daily Tarot history is saved (default: ~/.tarot-reader/history.json)
export TAROT_READER_HOME=/path/to/dir

# Run the REST API locally
pip install -e ".[api]"
uvicorn api.main:app --reload
# Docs at /docs (Swagger) and /redoc

# Docker
docker-compose up api          # production-style API container
docker-compose --profile dev up api-dev   # hot-reload dev container on :8001
```

There are two separate CLIs: `cli.py` at the repo root (interactive menu, search + full reading walkthrough, imports `from src import *`) and `src/__main__.py` (argparse-based, installed as the `tarot-reader` console script via `pyproject.toml`). Don't conflate them when asked to change "the CLI."

## Architecture

- `src/data/deck.json` — the canonical, portable card dataset (78 entries: `name`, `arcana`, `number`/`suit`, `upright`, `reversed`, `image`), with no Python dependency. `src/data/images/` holds the accompanying public-domain Rider-Waite-Smith card art (see `src/data/CREDITS.md`); both ship inside the built package (`pyproject.toml` `[tool.setuptools.package-data]` + `MANIFEST.in`). A future native client (mobile, Obsidian plugin, etc.) can read this JSON and its images directly without any Python involvement.
- `src/deck.py` — loads `deck.json` at import time and reconstructs `MAJOR_ARCANA` (list) and `MINOR_ARCANA` (dict of suit → list) in their original shapes, each card dict carrying `name`, `upright`, `reversed`, `image` (+ `number` for Major Arcana only — deliberately *absent*, not `None`, on Minor Arcana cards, since `core.py`/`search.py` check `"number" in card`). `get_all_cards()` concatenates and returns a fresh list. `get_card_image_path(card)` resolves a card's image to an absolute filesystem path. All card content lives here; reading logic never hardcodes card data.
- `src/core.py` — drawing logic. `_draw_cards(num_cards, personal_seed)` is the shared primitive behind `draw_single`, `draw_three`, `celtic_cross`. Three distinct randomness strategies:
  - Seeded path (`personal_seed` given): `_create_personal_seed()` hashes `lowercase(seed) + current_time_microseconds` with MD5 to produce an int seed — so results still change run-to-run even with the same seed, by design (time component is intentional, not a bug).
  - Unseeded path: `random_drop()` uses `_create_time_seed()` and reshuffles 3-7 times; orientation is derived from `time.time()` microseconds rather than `random.choice`.
  - Daily path: `daily_reading(personal_seed=None, date=None)` is the opposite of the above — deterministic, no time component. `_create_daily_seed()` hashes only the date (+ personal_seed), so repeated calls on the same date return the same card. Uses a local `random.Random(seed)` instance rather than the global `random` module, so it never needs a reset-after-use step the way the seeded/time-seeded paths do.
  - Orientation strings from `core.py` are `"Upright"`/`"Reversed"` (capitalized) — the API layer (`api/routers/*.py::_format_*_response`) lowercases them to match the Pydantic `Literal["upright", "reversed"]` models. Keep that lowercasing in mind if touching either layer — it's a real, load-bearing conversion, not dead code.
  - `random.seed()` is reset at the end of seeded calls to avoid leaking a deterministic global seed into subsequent unrelated calls.
- `src/history.py` — the only module that touches disk. Local JSON-file persistence for Daily Tarot: `record_daily_reading()` computes via `core.daily_reading()` and atomically overwrites today's entry (temp file + `os.replace`); safe to call repeatedly per day since the computation is deterministic. `get_daily_history()` reads entries back, sorted by date. Storage path defaults to `~/.tarot-reader/history.json`, overridable via the `TAROT_READER_HOME` env var — the path is resolved at call time (not import time) specifically so tests/callers can override it without reloading the module.
- `src/search.py` — `search_cards(query)` supports name substring, Major Arcana number, and short aliases (suit letter + rank, e.g. `s1` = Ace of Swords, `wk` = King of Wands). Alias tables (`suit_aliases`, `court_aliases`) are defined inline in this function.
- `src/text_formatter.py` — turns the dict/list structures from `core.py` into the emoji-decorated terminal strings shown by both CLIs. Stays pure/no I/O: `get_daily_reading_text(reading)` formats an already-computed reading dict rather than computing (and saving) one itself — callers (CLI, `src/__main__.py`) are responsible for calling `history.record_daily_reading()` first.
- `src/__init__.py` — the public library surface (`__all__`); `api/` and `cli.py` both import from here rather than reaching into `core`/`search`/`text_formatter`/`history` directly.
- `api/main.py` — FastAPI app setup, CORS (wide open, `allow_origins=["*"]` — flagged in README as needing tightening for production), custom 404/500 handlers, `/health`.
- `api/routers/readings.py`, `api/routers/cards.py`, `api/routers/daily.py` — thin wrappers around `src` functions; conversion between internal dicts and `api/models.py` Pydantic response models happens here, not in `src`. `daily.py` has a deliberate asymmetry driven by the API having no accounts: `GET /api/v1/daily` without `?seed=` is the one shared "card of the day" and gets persisted server-side (via `history.record_daily_reading()`) into the public history log; with `?seed=`, the personalized card is computed via `core.daily_reading()` directly and returned but *not* saved server-side (there's no per-user scope to save it under) — a client is expected to persist its own personalized readings locally, same as the mobile app design's local-history approach.
- `api/models.py` — all request/response Pydantic models.

## Versioning

`__version__` is duplicated in three places and must be kept in sync manually: `pyproject.toml` (`[project].version`), `src/__init__.py`, and the hardcoded strings in `api/main.py` (FastAPI `version=`, root endpoint response, `HealthCheckResponse`).

## CI/CD (`.github/workflows/ci.yml`)

Push/PR to `main`/`develop` runs lint (ruff, black --check, mypy — scoped to `src/ tests/`, not `api/` or `cli.py`) → tests (matrix across OS × Python 3.8-3.12; installs `.[test,api]` so the fastapi-dependent tests in `tests/test_daily_api.py` actually run) → build → docker build. Tag pushes matching `v*.*.*` additionally run the full release pipeline: publish to TestPyPI → install-and-smoke-test from TestPyPI → publish to PyPI → GitHub release → push Docker image to Docker Hub. `.github/workflows/publish.yml` is a separate, simpler manual/tag-triggered TestPyPI-only publish workflow.
