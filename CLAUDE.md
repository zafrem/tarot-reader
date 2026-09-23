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

- `src/deck.py` — static data only: `MAJOR_ARCANA` and minor arcana lists (78 cards total), each a dict with `name`, `upright`, `reversed`, and `number` (Major Arcana only). `get_all_cards()` concatenates and returns a fresh list. All card content lives here; reading logic never hardcodes card data.
- `src/core.py` — drawing logic. `_draw_cards(num_cards, personal_seed)` is the shared primitive behind `draw_single`, `draw_three`, `celtic_cross`. Two distinct randomness strategies:
  - Seeded path (`personal_seed` given): `_create_personal_seed()` hashes `lowercase(seed) + current_time_microseconds` with MD5 to produce an int seed — so results still change run-to-run even with the same seed, by design (time component is intentional, not a bug).
  - Unseeded path: `random_drop()` uses `_create_time_seed()` and reshuffles 3-7 times; orientation is derived from `time.time()` microseconds rather than `random.choice`.
  - Orientation strings from `core.py` are `"Upright"`/`"Reversed"` (capitalized) — the API layer (`api/routers/readings.py::_format_card_response`) lowercases them to match the Pydantic `Literal["upright", "reversed"]` models. Keep that lowercasing in mind if touching either layer — it's a real, load-bearing conversion, not dead code.
  - `random.seed()` is reset at the end of seeded calls to avoid leaking a deterministic global seed into subsequent unrelated calls.
- `src/search.py` — `search_cards(query)` supports name substring, Major Arcana number, and short aliases (suit letter + rank, e.g. `s1` = Ace of Swords, `wk` = King of Wands). Alias tables (`suit_aliases`, `court_aliases`) are defined inline in this function.
- `src/text_formatter.py` — turns the dict/list structures from `core.py` into the emoji-decorated terminal strings shown by both CLIs.
- `src/__init__.py` — the public library surface (`__all__`); `api/` and `cli.py` both import from here rather than reaching into `core`/`search`/`text_formatter` directly.
- `api/main.py` — FastAPI app setup, CORS (wide open, `allow_origins=["*"]` — flagged in README as needing tightening for production), custom 404/500 handlers, `/health`.
- `api/routers/readings.py` and `api/routers/cards.py` — thin wrappers around `src` functions; conversion between internal dicts and `api/models.py` Pydantic response models happens here, not in `src`.
- `api/models.py` — all request/response Pydantic models.

## Versioning

`__version__` is duplicated in three places and must be kept in sync manually: `pyproject.toml` (`[project].version`), `src/__init__.py`, and the hardcoded strings in `api/main.py` (FastAPI `version=`, root endpoint response, `HealthCheckResponse`).

## CI/CD (`.github/workflows/ci.yml`)

Push/PR to `main`/`develop` runs lint (ruff, black --check, mypy) → tests (matrix across OS × Python 3.8-3.12) → build → docker build. Tag pushes matching `v*.*.*` additionally run the full release pipeline: publish to TestPyPI → install-and-smoke-test from TestPyPI → publish to PyPI → GitHub release → push Docker image to Docker Hub. `.github/workflows/publish.yml` is a separate, simpler manual/tag-triggered TestPyPI-only publish workflow.
