# Security Guidelines

Garuda is local-first, but it still handles sensitive investor research. Security decisions should protect private notes, thesis reasoning, sources, and portfolio data.

## Security Principles

- Treat all investment notes, theses, and portfolio data as private by default.
- Keep user data local for the MVP.
- Avoid hidden network calls.
- Avoid cloud storage assumptions.
- Prefer explicit import/export over automatic sync.
- Minimize the amount of sensitive data written to logs.

## Secrets and Configuration

- Never commit secrets, API keys, tokens, credentials, private data dumps, or `.env` files.
- Keep local configuration in ignored environment files.
- Document required environment variables without including real values.
- Use placeholder values in examples.
- Rotate any secret that is accidentally committed.

## Backend Security

- Validate all API inputs with Pydantic or equivalent request schemas.
- Do not build SQL queries through string concatenation.
- Use SQLModel and parameterized query patterns.
- Validate file names and paths before reading or writing Markdown files.
- Keep Markdown research files inside the configured research data directory.
- Prevent path traversal when accessing local files.
- Return safe error messages that do not leak internal paths, stack traces, or private data.
- Avoid logging full request bodies when they may contain research notes.

## Frontend Security

- Treat rendered Markdown as untrusted content.
- Sanitize Markdown or render it through a safe renderer before displaying HTML.
- Do not use raw HTML rendering unless the content is sanitized.
- Validate URLs before making them clickable.
- Clearly distinguish external links from internal navigation.
- Do not store sensitive notes in browser storage unless that behavior is intentional and documented.

## Local Data Protection

- Store the SQLite database and Markdown research files in predictable local paths.
- Make export/import explicit and user-controlled.
- Avoid silently copying private research data outside the workspace.
- Do not add telemetry, analytics, or remote error reporting in the MVP.
- If future sync is added, require explicit user opt-in.

## Dependency Security

- Add dependencies only when they serve a real workflow.
- Prefer well-maintained libraries with clear ownership and active releases.
- Keep backend and frontend dependencies separated.
- Review new dependencies for transitive risk, licensing, and maintenance status.
- Pin or lock dependencies once package management is introduced.

## Research Source Handling

- Record source URLs and access dates.
- Do not scrape or store private data from sources without a clear legal and ethical basis.
- Avoid storing credentials for third-party research sources in the app.
- Treat founder, company, and funding data as research material that should include source context.

## AI Feature Security

- Do not send private theses, portfolio notes, or unpublished research to external AI services without explicit user approval.
- Keep AI-assisted features optional and transparent.
- Label AI-generated summaries or scores when they are introduced.
- Preserve source links and human notes alongside generated analysis.
