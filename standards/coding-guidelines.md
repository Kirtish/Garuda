# Coding Guidelines

Garuda code should be boring in the best way: readable, explicit, testable, and easy to change.

## General Guidelines

- Prefer clarity over cleverness.
- Keep functions small and purpose-specific.
- Use descriptive names for modules, functions, variables, and components.
- Avoid premature abstractions. Extract shared code after real repetition appears.
- Keep business rules out of UI components and API route handlers.
- Handle errors deliberately and return useful messages.
- Write code that can be tested without a running full application whenever practical.

## Backend Guidelines

- Use Python 3.12 language features conservatively.
- Use type hints for public functions, service methods, repository methods, and models.
- Keep FastAPI route handlers thin.
- Put product workflows in service modules.
- Put SQLite and Markdown persistence behind repository modules.
- Use SQLModel for database tables and persistence models.
- Use Pydantic schemas for API validation and response contracts when models diverge from persistence.
- Do not let route handlers build raw SQL or perform direct file writes.
- Prefer explicit dependency injection for database sessions and services.
- Keep scheduled jobs idempotent where possible.

## Frontend Guidelines

- Use React with TypeScript for all application code.
- Prefer functional components.
- Keep components focused on presentation and interaction.
- Put feature logic under feature directories.
- Use Zustand only for state that must be shared across views or workflows.
- Keep server state, UI state, and form state conceptually separate.
- Use TanStack Table for data-heavy grids.
- Use Apache ECharts for charting rather than custom chart implementations.
- Keep research workflows dense, scannable, and efficient.

## API Guidelines

- Use resource-oriented REST endpoints.
- Use consistent naming, status codes, and error response shapes.
- Validate all request bodies.
- Return typed response schemas.
- Keep API responses stable once frontend workflows depend on them.
- Do not expose filesystem paths unless the UI genuinely needs them.

## Data Guidelines

- Store structured records in SQLite.
- Store long-form research in Markdown files.
- Use stable IDs for records.
- Track `created_at` and `updated_at` on core entities.
- Avoid deleting user research data silently.
- Prefer explicit archive/status fields for investor workflow decisions.

## Testing Guidelines

- Add pytest coverage for backend services, repositories, and API routes.
- Add Playwright smoke tests for critical investor workflows.
- Test scoring logic separately from UI.
- Test Markdown read/write behavior where research files are created or updated.
- Use fixtures for sample startups, founders, signals, and scorecards.

## Documentation Guidelines

- Update docs when changing architecture, workflows, API behavior, or data models.
- Keep durable rules in `standards/`.
- Keep product and technical explanations in `docs/`.
- Prefer concise examples over long abstract descriptions.
