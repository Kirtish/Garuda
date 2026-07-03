# Backend Scaffolding

## Goal

Define the FastAPI backend scaffold for Garuda before implementation.

This document captures the agreed backend development approach for Issue 002. It should be used as the reference before creating backend source files, installing dependencies, or adding tests.

## Backend Role

The backend is Garuda's local API layer. It connects the React UI to business workflows, structured SQLite data, and Markdown research files.

## Architecture Position

```text
React UI
   |
   v
FastAPI
   |
   v
Business Services
   |
   v
Repositories
   |
   v
SQLite
   |
   v
Markdown Research Files
```

FastAPI routes should stay thin. Business Services should own product workflows. Repositories should isolate SQLite and Markdown persistence.

## Dependency Management

Decision: use `uv`.

Expected backend project files:

- `pyproject.toml`
- `uv.lock`

Expected virtual environment location:

- `src/backend/.venv/`

The virtual environment must remain uncommitted.

## Backend Directory Structure

```text
src/backend/
  app/
    api/
    core/
    db/
    models/
    schemas/
    services/
    repositories/
    research/
    jobs/
    main.py
  tests/
  pyproject.toml
  uv.lock
```

## Application Entrypoint

Use:

```text
app.main:app
```

The initial FastAPI application should be created in:

```text
src/backend/app/main.py
```

## Initial Dependencies

Runtime dependencies:

- `fastapi`
- `uvicorn`
- `sqlmodel`
- `pydantic`
- `pydantic-settings`
- `apscheduler`

Development and test dependencies:

- `pytest`
- `httpx`
- `ruff`

## Initial Commands

Run these commands later during implementation, not during planning:

```powershell
cd src/backend
uv init
uv add fastapi uvicorn sqlmodel pydantic pydantic-settings apscheduler
uv add --dev pytest httpx ruff
```

## Configuration Approach

Use:

```text
src/backend/app/core/config.py
```

Configuration should use Pydantic Settings.

Local environment files such as `.env` must remain ignored. Add `.env.example` later when real configuration keys exist.

## Database Plan

Use SQLite for the MVP.

Database setup should live under:

```text
src/backend/app/db/
```

The default database path should be configurable.

Do not add Alembic initially. Add migrations later only if schema change management becomes necessary.

## Research Files Plan

Markdown research file utilities should live under:

```text
src/backend/app/research/
```

Repositories should coordinate Markdown reads and writes.

Security requirements:

- Keep research files inside the configured research data directory.
- Prevent path traversal.
- Do not expose private local filesystem paths unless the UI genuinely needs them.

## Initial API Shape

Start with:

```text
GET /health
```

Later MVP API areas:

- Startup CRUD
- Founders
- Funding rounds
- Signals
- Thesis read/write
- Scorecard read/write
- Dashboard summary

## Testing Plan

Use pytest for backend tests.

Initial test location:

```text
src/backend/tests/test_health.py
```

Use `httpx` or FastAPI's test client for API tests.

## Security Notes

- Validate all inputs.
- Avoid direct database or file access inside route handlers.
- Avoid logging private research notes or thesis content.
- Return safe error messages that do not leak internal paths or private data.
- Keep local data private by default.

## Acceptance Criteria

- Backend dependency manager is selected as `uv`.
- Backend folder structure is agreed.
- Application entrypoint is agreed as `app.main:app`.
- Initial runtime and development dependencies are listed.
- Configuration, database, research file, and testing approach are documented.
- Backend implementation can begin from this document without additional architectural decisions.
