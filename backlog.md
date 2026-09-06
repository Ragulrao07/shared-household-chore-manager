# Project Backlog: Shared Household Chore Manager

This backlog outlines the sequential tasks required to implement the MVP as defined in `_docs/plan.md`.

## Phase 1: Foundation & Authentication
- [x] **Task 1.1: Project Setup**
    - Initialize Django project and application.
    - Configure database settings and base templates.
- [ ] **Task 1.2: User Authentication**
    - Implement Email + Password registration and login.
    - Create basic profile/account management.

## Phase 2: Household Management
- [ ] **Task 2.1: Household Model & Creation**
    - Create `Household` model.
    - Implement "Create Household" view.
    - Generate unique invite codes for households.
- [ ] **Task 2.2: Joining a Household**
    - Implement "Join Household" via invite code.
    - Enforce the "one household per user" constraint.

## Phase 3: Chore Management
- [ ] **Task 3.1: Chore Model & CRUD**
    - Create `Chore` model with name, description, frequency, and participants.
    - Implement soft deletion for chores.
    - Build views for creating, editing, and listing chores.
- [ ] **Task 3.2: Rotation Logic**
    - Implement the algorithm to determine the next responsible roommate based on frequency and history.

## Phase 4: Dashboard & Completion
- [ ] **Task 4.1: Main Dashboard**
    - Create a view showing "Today's Chores" for the logged-in user.
- [ ] **Task 4.2: Completing Chores**
    - Implement the one-tap "Done" functionality.
    - Create a `ChoreHistory` model to record completions.
- [ ] **Task 4.3: Overdue Handling**
    - Implement logic to detect missed chores.
    - Automatically reassign overdue chores to the next person in the rotation.

## Phase 5: Swapping & Notifications
- [ ] **Task 5.1: Chore Swapping**
    - Build the "Request Swap" workflow.
    - Implement the "Approval" mechanism for the requested roommate.
- [ ] **Task 5.2: Basic Notifications**
    - Set up in-app/dashboard alerts for reminders, overdue status, and assignment changes.

## Phase 6: Final Polish
- [ ] **Task 6.1: Basic History View**
    - Implement a simple history log for roommates to view past completions.
- [ ] **Task 6.2: Final UI/UX Refinement**
    - Ensure "Today's Chores" is the primary focus of the interface.
