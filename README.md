# Garuda

Garuda is a local-first Venture Intelligence Platform focused on Indian AI startups.

The platform is designed for an individual investor who wants to discover promising AI startups, track funding rounds, research founders, build investment portfolios, record investment theses, score companies using a structured framework, and monitor venture signals such as hiring, product launches, partnerships, and funding activity.

The long-term vision is to evolve Garuda into a professional-grade AI-powered venture research system.

## MVP Goal

Build a local research workspace where an investor can maintain a structured database of Indian AI startups, evaluate them with a repeatable scoring framework, and write durable investment theses.

The first usable milestone is:

> Add 20 Indian AI startups, research founders, record signals, score each company, and maintain a clear investment thesis for the watchlist.

## Core Capabilities

- Discover and manage Indian AI startup profiles.
- Track founders, funding rounds, sources, and market signals.
- Build watchlists and portfolio views.
- Record investment theses and diligence notes.
- Score companies with a structured 1-5 framework.
- Review dashboard summaries, filtered tables, and research status.

## Tech Stack

Backend:

- Python 3.12
- FastAPI
- SQLModel
- Pydantic
- APScheduler

Frontend:

- React
- Vite
- TypeScript
- Tailwind CSS
- shadcn/ui
- Zustand
- TanStack Table
- Apache ECharts

Database:

- SQLite for MVP
- Markdown files for long-form research notes

Testing:

- pytest
- Playwright

## Architecture

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

Garuda is intentionally local-first. The MVP does not use Kubernetes, microservices, Redis, Kafka, RabbitMQ, or cloud deployment.

## Folder Structure

```text
docs/        Product, architecture, database, API, UX, sprint, and framework docs
standards/   Durable engineering and operating standards
prompts/     Reusable prompts and agent interaction patterns
templates/   Reusable project, research, and document templates
seed/        Seed data, bootstrap fixtures, and sample startup records
src/         Application source code
packages/    Shared internal modules when reuse becomes real
scripts/     Automation, setup, migration, and utility scripts
tests/       Test suites, fixtures, and test support utilities
```

Expected implementation shape:

```text
src/
  backend/
  frontend/

packages/
  shared/
```

## Documentation

Project documentation lives in `docs/`:

- `vision.md`
- `product-requirements.md`
- `architecture.md`
- `database-design.md`
- `api-specifications.md`
- `ui-ux-design-system.md`
- `sprint-planning.md`
- `investment-framework.md`

Engineering standards live in `standards/`:

- `engineering-standards.md`
- `coding-guidelines.md`
- `security-guidelines.md`

## Current Status

Garuda is in the foundation stage. The product vision, MVP direction, architecture constraints, technology stack, and documentation structure are defined. The next phase is implementation scaffolding.

## Roadmap

1. Finalize documentation and engineering standards.
2. Scaffold FastAPI backend and React frontend.
3. Add SQLite, SQLModel models, and repository boundaries.
4. Build startup CRUD flows.
5. Add founder, funding, signal, thesis, and scorecard workflows.
6. Build dashboard, tables, and portfolio views.
7. Add pytest backend coverage.
8. Add Playwright smoke tests.
