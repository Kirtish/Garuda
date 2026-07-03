# API Specifications

Garuda exposes a local FastAPI API for the React frontend.

## API Principles

- Keep routes thin.
- Validate inputs with Pydantic.
- Delegate product behavior to services.
- Keep persistence behind repositories.
- Return clear errors with useful messages.

## MVP Resources

- Startups
- Founders
- Funding rounds
- Signals
- Theses
- Scorecards
- Portfolio positions
- Sources

## Initial Endpoint Shape

```text
GET    /api/startups
POST   /api/startups
GET    /api/startups/{startup_id}
PATCH  /api/startups/{startup_id}
DELETE /api/startups/{startup_id}

GET    /api/startups/{startup_id}/founders
POST   /api/startups/{startup_id}/founders

GET    /api/startups/{startup_id}/funding-rounds
POST   /api/startups/{startup_id}/funding-rounds

GET    /api/startups/{startup_id}/signals
POST   /api/startups/{startup_id}/signals

GET    /api/startups/{startup_id}/thesis
PUT    /api/startups/{startup_id}/thesis

GET    /api/startups/{startup_id}/scorecard
PUT    /api/startups/{startup_id}/scorecard

GET    /api/dashboard/summary
```

## Error Pattern

Errors should use consistent response shapes:

```json
{
  "detail": "Human-readable error message"
}
```

## API Status

This document defines the initial API direction. Exact request and response schemas should be added when the SQLModel and Pydantic models are implemented.
