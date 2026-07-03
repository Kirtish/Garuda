# AGENTS

This file defines expectations for AI agents working in Garuda.

## Project Intent

Garuda is a local-first Venture Intelligence Platform focused on Indian AI startups. Agents should help build a professional research system for an individual investor to discover startups, research founders, track funding and signals, score companies, and maintain investment theses.

## Architecture Boundary

Follow this architecture:

```text
React UI -> FastAPI -> Business Services -> Repositories -> SQLite -> Markdown Research Files
```

Keep FastAPI routes thin. Put product logic in services. Put SQLite and Markdown persistence behind repositories.

## Non-Architecture

Do not introduce Kubernetes, microservices, Redis, Kafka, RabbitMQ, or cloud deployment for the MVP.

## Working Principles

- Read the relevant files before making changes.
- Keep edits focused and consistent with the surrounding project structure.
- Do not overwrite user work or unrelated changes.
- Prefer small, verifiable changes with clear reasoning.
- Update documentation when changing workflows, structure, or public behavior.
- Avoid adding dependencies, frameworks, infrastructure, or abstractions before the project needs them.
- Preserve the local-first principle: user research data should remain portable and inspectable.
- Follow `standards/coding-guidelines.md` and `standards/security-guidelines.md`.

## Directory Guidance

- Use `src/backend/` for FastAPI backend code.
- Use `src/frontend/` for React frontend code.
- Use `packages/` only for shared modules with real reuse.
- Use `docs/` for product, architecture, API, database, UX, sprint, and investment framework docs.
- Use `standards/` for durable engineering and operating standards.
- Use `prompts/` for reusable prompt assets.
- Use `templates/` for reusable scaffolds and document structures.
- Use `seed/` for sample startup data, fixtures, and bootstrap records.
- Use `scripts/` for repeatable automation.
- Use `tests/` for cross-cutting tests and test support files.

## Change Workflow

1. Inspect the repository state.
2. Identify the smallest useful change.
3. Make the change without disturbing unrelated files.
4. Run the most relevant available checks.
5. Report what changed, what was verified, and any remaining risk.
