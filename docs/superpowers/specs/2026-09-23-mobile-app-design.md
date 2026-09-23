# Mobile App Foundation — Design

Date: 2026-09-23
Status: Approved, pending implementation plan

## Context

`tarot-reader` currently ships a Python library (`src/`), an interactive CLI
(`cli.py`) and an argparse CLI (`src/__main__.py`, installed as the
`tarot-reader` console script), and an optional async FastAPI REST API
(`api/`). All three already exist and are published to PyPI (tagged releases
`v0.0.1`, `v0.0.4`, `v0.0.5`; `pyproject.toml` registers the console script
and the `api` extra).

The next step is a React Native mobile client. This is the first of several
planned efforts that were explicitly decomposed out of a larger ask:

1. **This spec** — mobile app foundation (reading features only)
2. Daily habits & scheduling feature (own spec, later — will need
   accounts/persistence that this spec deliberately defers)
3. A generic random-number-generation API/utility within the package,
   independent of tarot cards (own spec, later)
4. PyPI publishing of the CLI/API — already done, no work needed

This document covers only #1.

## Goal

Ship a React Native (Expo) mobile app with full feature parity with the
existing REST API: single-card, 3-card, and Celtic Cross readings, random
drops, and card search/browse — plus on-device reading history. No accounts,
no server-side persistence, no changes to the existing Python package.

## Non-goals

- Accounts / authentication / server-side persistence — deferred to the
  habits/schedules spec, which is the first feature that actually needs them.
- Habits and scheduling features themselves.
- The generic random-number API.
- App store submission / EAS build & signing configuration.
- Offline reading generation (the app requires a reachable API instance).
- Push notifications.
- Any change to `src/`, `api/`, `cli.py`, or the console script — this
  sub-project is purely additive.

## Architecture

### Repo layout

New top-level `app/` directory, alongside `src/`, `api/`, `cli.py`:

```
app/
  App.tsx
  app.json
  package.json
  tsconfig.json
  .env.example            # EXPO_PUBLIC_API_URL
  assets/
  src/
    api/
      client.ts           # fetch wrapper, reads EXPO_PUBLIC_API_URL
      readings.ts          # single/three/celtic/random calls
      cards.ts              # deck-info/major/minor/suit/search calls
    types/
      card.ts               # TS types hand-mirrored from api/models.py
    navigation/
      RootNavigator.tsx     # stack + tabs (Home / Search / History)
    screens/
      HomeScreen.tsx
      SingleReadingScreen.tsx
      ThreeCardScreen.tsx
      CelticCrossScreen.tsx
      RandomDrawScreen.tsx
      CardSearchScreen.tsx
      HistoryScreen.tsx
    components/
      CardView.tsx
      LoadingState.tsx
      ErrorState.tsx
    storage/
      history.ts             # AsyncStorage read/write wrapper
```

Nothing under `src/`, `api/`, or `cli.py` is modified.

### Data flow

- Expo + TypeScript + React Navigation (native-stack, with a bottom-tab
  layer for Home / Search / History).
- `api/client.ts` is a thin `fetch` wrapper; base URL comes from the
  `EXPO_PUBLIC_API_URL` environment variable (Expo's public env var
  convention), set to a LAN IP or tunnel URL during development.
- Each reading/card screen maps ~1:1 to an existing endpoint
  (`/api/v1/readings/single`, `/three`, `/celtic-cross`, `/random`,
  `/api/v1/cards/*`). Response shapes are hand-mirrored as TypeScript types
  in `src/types/card.ts` from `api/models.py` — no codegen for v1.

### Local history

After a successful reading, the app writes a record
`{ id, spreadType, cards, timestamp, seed }` to AsyncStorage via
`storage/history.ts` (single JSON array under one key is sufficient at this
scale). `HistoryScreen` lists saved readings and lets the user open one to
view its cards again. No sync, no server involvement.

### Error handling

Each screen owns its own loading / error / retry state around its API call.
No global error boundary or centralized error store is needed at this size.

### Dev workflow

```bash
# Backend, reachable on LAN
uvicorn api.main:app --reload --host 0.0.0.0

# App, pointed at that host
EXPO_PUBLIC_API_URL=http://<lan-ip>:8000 npx expo start
```
Test via Expo Go on a physical device or an iOS/Android simulator. CORS is
already wide open (`allow_origins=["*"]` in `api/main.py`), so no backend
changes are needed for local device testing.

### Testing

Jest + `@testing-library/react-native`, focused on:
- `api/*.ts` response parsing/error handling
- `storage/history.ts` read/write behavior

Full UI test coverage is not a goal for v1.

### CI

A new `app` job in `.github/workflows/ci.yml` (or a separate workflow file)
running `npm ci && npm test` inside `app/`, isolated from the existing
Python lint/test/build/docker jobs so a JS failure doesn't block a Python
release and vice versa.

## Open items deferred to later specs

- How habits/schedules' need for accounts and persistence will integrate
  with this app's local-history pattern (likely: introduce accounts +
  backend DB at that point, migrate local history into synced history).
- Whether to adopt OpenAPI-generated TS types once the API surface grows
  beyond what's comfortable to hand-mirror.
