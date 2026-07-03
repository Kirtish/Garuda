# CODEX

Codex-specific workflow notes for Garuda.

## Default Workflow

1. Inspect the repository state with `git status --short`.
2. Read the files most relevant to the requested change.
3. Make narrowly scoped edits.
4. Run the most relevant checks available.
5. Summarize changes and verification clearly.

## Product Context

Garuda is a local-first Venture Intelligence Platform for Indian AI startups. The MVP supports startup discovery, founder research, funding tracking, signal monitoring, thesis writing, scoring, and portfolio/watchlist workflows.

## Architecture Rules

- React UI calls FastAPI.
- FastAPI routes stay thin.
- Business Services own product workflows.
- Repositories isolate SQLite and Markdown persistence.
- SQLite stores structured data.
- Markdown Research Files store long-form research notes and investment theses.

## Explicit Constraints

Do not add Kubernetes, microservices, Redis, Kafka, RabbitMQ, or cloud deployment for the MVP.

## Editing Guidelines

- Preserve user changes.
- Use `src/backend/` for backend source.
- Use `src/frontend/` for frontend source.
- Keep shared code in `packages/` only when reuse is real.
- Add or update documentation when creating workflows, standards, or public behavior.
- Keep generated or placeholder content minimal.
- Favor local-first, portable data over hosted assumptions.
- Follow `standards/coding-guidelines.md` and `standards/security-guidelines.md`.

## Verification

Use pytest for backend tests and Playwright for end-to-end UI tests once the app scaffold exists. Until then, verification may be limited to filesystem checks, Git status, and direct file inspection.
