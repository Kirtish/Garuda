# Database Design

Garuda uses SQLite for structured MVP data and Markdown files for long-form research.

## Storage Responsibilities

SQLite stores structured records that need filtering, sorting, relationships, and dashboard summaries.

Markdown files store long-form research that benefits from readable, portable text files.

## Core Entities

- Startup
- Founder
- FundingRound
- Signal
- Thesis
- Scorecard
- PortfolioPosition
- Source

## Startup

Represents an Indian AI startup under research.

Suggested fields:

- id
- name
- website
- sector
- ai_focus_area
- location
- founded_year
- stage
- description
- status
- created_at
- updated_at

## Founder

Represents a founder associated with a startup.

Suggested fields:

- id
- startup_id
- name
- role
- linkedin_url
- profile_url
- background_summary
- prior_companies
- education
- notable_achievements

## FundingRound

Represents a funding event.

Suggested fields:

- id
- startup_id
- round_type
- amount
- currency
- announced_date
- investors
- source_id
- notes

## Signal

Represents an observed company signal.

Suggested fields:

- id
- startup_id
- signal_type
- signal_date
- summary
- source_id
- confidence
- notes

## Thesis

Represents the structured metadata for an investment thesis. The long-form body should live in Markdown.

Suggested fields:

- id
- startup_id
- markdown_path
- thesis_status
- last_reviewed_at
- created_at
- updated_at

## Scorecard

Represents a structured company score.

Suggested fields:

- id
- startup_id
- market_opportunity
- founder_quality
- product_strength
- ai_defensibility
- traction
- distribution
- funding_signal
- strategic_fit
- risk_level
- overall_score
- notes
- scored_at

## PortfolioPosition

Represents the investor's relationship to a company.

Suggested fields:

- id
- startup_id
- status
- invested_amount
- currency
- entry_date
- ownership_notes
- next_action

## Source

Represents a research source.

Suggested fields:

- id
- title
- url
- publisher
- published_at
- accessed_at
- source_type
- notes

## Markdown Linkage

SQLite records should store paths to Markdown files where needed. Markdown files should remain readable outside the application.
