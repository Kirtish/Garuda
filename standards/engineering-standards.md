# Engineering Standards

Garuda is a local-first Venture Intelligence Platform. Engineering choices should keep the system simple, inspectable, and easy to evolve.

## Architecture Standards

- Follow: React UI -> FastAPI -> Business Services -> Repositories -> SQLite -> Markdown Research Files.
- Keep FastAPI routes thin.
- Put product workflows in services.
- Put persistence behind repositories.
- Store structured data in SQLite.
- Store long-form research in Markdown files.

## MVP Infrastructure Constraints

Do not introduce:

- Kubernetes
- Microservices
- Redis
- Kafka
- RabbitMQ
- Cloud deployment

## Backend Standards

- Use Python 3.12.
- Use FastAPI for the API.
- Use SQLModel for SQLite models.
- Use Pydantic for validation and API schemas.
- Use APScheduler only for local scheduled jobs when a real scheduling workflow exists.
- Keep database access out of route handlers.

## Frontend Standards

- Use React, Vite, and TypeScript.
- Use Tailwind CSS and shadcn/ui for UI.
- Use Zustand for local UI/application state when needed.
- Use TanStack Table for data-heavy tables.
- Use Apache ECharts for charts.
- Keep screens optimized for research, scanning, filtering, and repeated use.

## Testing Standards

- Use pytest for backend tests.
- Use Playwright for end-to-end UI tests.
- Add tests when behavior changes.
- Start with focused smoke coverage and expand around core workflows.

## Data Standards

- Treat investor notes and theses as private research data.
- Keep data portable and inspectable.
- Avoid cloud assumptions in MVP data flows.
- Prefer explicit export/import paths over hidden storage.

## Documentation Standards

- Update documentation when architecture, workflows, or public behavior changes.
- Keep durable standards in `standards/`.
- Keep product and technical documentation in `docs/`.
- Keep documentation concise enough to stay maintained.

## Related Standards

- `standards/coding-guidelines.md`
- `standards/security-guidelines.md`
