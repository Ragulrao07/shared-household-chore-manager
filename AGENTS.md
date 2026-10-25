# AGENTS.md — Autonomous Agent System Guidelines

## Project Overview
Shared Household Chore Manager is an AI-native full-stack application built using Django, PostgreSQL, and React. 
This document defines operational protocols, task execution guidelines, and agent role definitions.

## Agent Team Structure
1. **Architect Agent**: Defines data contracts, REST API specifications, and database models.
2. **Backend Engineer Agent**: Implements Django REST endpoints, ORM models, and business logic.
3. **Frontend Engineer Agent**: Implements UI state, responsive views, and API client integration.
4. **QA / Test Engineer Agent**: Writes and maintains unit, frontend, and end-to-end integration tests.
5. **On-Call SRE Agent**: Listens for Prometheus alert signals and performs automated remediation.

## Modular Documentation
- [System Architecture](docs/architecture.md)
- [Agent Collaboration Process](docs/process.md)
- [Task Tracking & Acceptance Criteria](docs/spec.md)

## Coding & Operational Standards
- **Python**: 3.12, PEP8 compliance.
- **Testing**: Every endpoint must be covered by Django test runners before merging.
- **Telemetry**: Key endpoints must increment Prometheus metrics and propagate OpenTelemetry trace contexts.
