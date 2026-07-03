# Contributing

Thanks for contributing to Garuda.

Garuda is a local-first Venture Intelligence Platform for Indian AI startups. Contributions should make the product clearer, easier to run, easier to test, or easier to extend.

## Getting Started

1. Create a focused branch for your change.
2. Read `README.md`, `AGENTS.md`, `CODEX.md`, and relevant files under `docs/` or `standards/`.
3. Keep changes scoped to a single concern.
4. Add or update tests when behavior changes.
5. Update documentation when workflows, conventions, or public interfaces change.

## Quality Bar

- Code should be readable, maintainable, and consistent with local patterns.
- Documentation should be useful and close to the workflow it describes.
- Changes should be easy to review.
- Automated checks should pass before merging once checks exist.
- User research data should remain portable, inspectable, and local-first.
- Coding and security standards should be followed for all implementation changes.

## Repository Conventions

- Backend source belongs in `src/backend/`.
- Frontend source belongs in `src/frontend/`.
- Shared reusable code belongs in `packages/`.
- Product and technical documentation belongs in `docs/`.
- Durable engineering standards belong in `standards/`.
- Reusable prompts belong in `prompts/`.
- Reusable scaffolds belong in `templates/`.
- Seed data and fixtures belong in `seed/`.
- Automation belongs in `scripts/`.
- Tests belong in `tests/`.

## Architecture Expectations

Follow this flow:

```text
React UI -> FastAPI -> Business Services -> Repositories -> SQLite -> Markdown Research Files
```

Avoid distributed infrastructure in the MVP. Do not introduce Kubernetes, microservices, Redis, Kafka, RabbitMQ, or cloud deployment.

## Review Expectations

Before opening or merging a change, confirm that:

- The change is intentionally scoped.
- Related documentation is updated.
- New behavior has appropriate tests or a clear reason tests are not yet available.
- The repository remains easy for a new contributor or agent to understand.
