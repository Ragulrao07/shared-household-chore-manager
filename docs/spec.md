# Product Specification & Acceptance Criteria

### Core User Journeys
1. **Chore Listing & Filtering**
   - Acceptance Criteria: Users can view all active household chores ordered by creation date and completion status.
2. **Chore Creation**
   - Acceptance Criteria: Validates required title/name; assigns default frequency (`daily`); increments `chores_created_total`.
3. **Chore Completion State**
   - Acceptance Criteria: Toggling status persists immediately in PostgreSQL and decrements `chores_active_total`.
4. **Observability & Error Handling**
   - Acceptance Criteria: 4xx and 5xx responses increment `chore_creation_failures_total` with appropriate labels.

### Task Tracker Evidence
Tasks and acceptance criteria are mapped to public issues at:
https://github.com/Ragulrao07/shared-household-chore-manager/issues
