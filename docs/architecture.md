# Architecture

Garuda uses a simple local-first architecture.

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

## Layers

## React UI

The React frontend provides the research workspace, tables, filters, dashboards, forms, scorecards, and thesis writing experience.

## FastAPI

FastAPI exposes the local API. Routes should be thin and should delegate product behavior to business services.

## Business Services

Services contain product workflows such as startup scoring, signal classification, thesis management, portfolio status updates, and dashboard summaries.

## Repositories

Repositories isolate persistence. They handle SQLite queries, Markdown file reads and writes, and persistence coordination.

## SQLite

SQLite stores structured records such as startups, founders, funding rounds, signals, scorecards, portfolio positions, and sources.

## Markdown Research Files

Markdown files store long-form research such as theses, founder notes, market notes, diligence questions, decision memos, and decision logs.

## Explicit Constraints

The MVP does not use:

- Kubernetes
- Microservices
- Redis
- Kafka
- RabbitMQ
- Cloud deployment

## Backend Shape

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
```

## Frontend Shape

```text
src/frontend/
  src/
    app/
    components/
    features/
    lib/
    routes/
    stores/
    types/
```
