# Shared Household Chore Manager

Production-grade, AI-native full-stack application built for managing shared household chores with automated CI/CD, observability, and autonomous incident remediation.

## Problem Description
In shared living arrangements, chore delegation often leads to friction, missing accountability, and uneven task distribution. The Shared Household Chore Manager provides an accessible, real-time board for household members to create, schedule, track, and complete recurring chores with zero deployment overhead.

## Architecture & Tech Stack
- **Frontend**: Responsive React UI / Django template interface
- **Backend**: Django 4.2+ (Python 3.12) REST API
- **Database**: PostgreSQL 16
- **DevOps**: Multi-stage Docker, Docker Compose, GitHub Actions (ghcr.io)
- **Observability**: OpenTelemetry, Prometheus (/metrics), Grafana, Alertmanager
- **Incident Response**: Autonomous AI on-call engineer via headless agent scripts

## Quickstart (Single-Command Run)

### Local Docker Stack
`ash
docker compose up -d --build
`
- Web Application: http://localhost:8000
- Prometheus Metrics: http://localhost:8000/metrics

### Observability Stack
`ash
cd observability
docker compose up -d
`
- Prometheus UI: http://localhost:9090
- Grafana: http://localhost:3000

## Running Tests
Run all unit and integration tests with a single command:
`ash
python manage.py test
`

## Agent Team & Specifications
- Agent Team Specifications: [AGENTS.md](AGENTS.md)
- Product Specifications: [docs/spec.md](docs/spec.md)
- Public Task Tracker: [GitHub Issues](https://github.com/Ragulrao07/shared-household-chore-manager/issues)
