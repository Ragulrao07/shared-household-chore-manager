# Agent Team Collaboration Process

## Workflow Lifecycle
1. **Requirement Definition**: Architect Agent converts user stories into strict acceptance criteria recorded in GitHub Issues.
2. **Implementation**:
   - Backend Agent scaffolds migrations and endpoints.
   - Frontend Agent integrates UI components.
3. **Quality Gate**: QA Agent runs `python manage.py test` and integration test suites.
4. **Deployment Gate**: GitHub Actions runs CI, builds multi-stage Docker images to GHCR, and deploys to DEV.
5. **Monitoring & Healing**: SRE Agent monitors `/metrics`, detects 5xx spikes via Prometheus, and patches regressions autonomously.
