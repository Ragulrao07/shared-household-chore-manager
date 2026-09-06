# Shared Household Chore Manager — MVP Scope

## 1. Project Goal

Build a simple tool for managing shared household chores for roommates/shared apartments.

The MVP should focus on one core workflow:

**Create household → Invite roommates → Add chores → System rotates chores → Today's chores appear → Reminder → Tap Done → History updated → Next rotation**

The goal is to keep the first version focused and avoid unnecessary features.

---

## 2. Decisions Made During Brainstorming

| Area | MVP Decision |
|---|---|
| Users | Roommates/shared apartments |
| Chore assignment | Automatic rotation |
| Rotation | Weekly by default; customizable frequency |
| Reminders | Dashboard + notifications |
| Completion | One-tap “Done” |
| History | Basic completion history |
| Joining a household | Account + invite code |
| Chore management | Any roommate can create/manage chores |
| Missed chore | Mark overdue + notify + automatically move to next roommate |
| Chore swapping | Requires the other roommate's approval |
| Main dashboard | Today's chores only |

---

## 3. Detailed Decisions and Rationale

### 3.1 Target Users

**Decision:** Roommates/shared apartments.

**Why:**
- Gives the product a clear target audience.
- Shared chores are a common problem in roommate situations.
- Keeps the MVP focused instead of trying to support every type of household.

**Other options considered:**
- A single household/family
- Multiple households
- Any type of household

These could be supported later if needed.

---

### 3.2 Chore Assignment

**Decision:** Automatic rotation.

**Why:**
- Makes responsibility fairer between roommates.
- Reduces the need for someone to manually assign chores.
- Creates a predictable workflow.

**Other options considered:**
- Fixed assignment
- Self-claiming chores
- Combination of assignment methods

For the MVP, automatic rotation is the clearest core feature.

---

### 3.3 Rotation Frequency

**Decision:** Weekly by default, with a customizable frequency.

**Why:**
- Weekly rotation is easy to understand and works well for common household chores.
- Different chores may need different frequencies, so flexibility is useful.
- A default prevents configuration from becoming complicated.

**Other options considered:**
- Daily rotation
- Fixed weekly rotation only
- Different frequency for every chore

The MVP should allow customization without making the setup complicated.

---

### 3.4 Reminders and Notifications

**Decision:** Dashboard + notifications.

The MVP should provide:
- Reminder before a chore is due
- Overdue notification
- Notification when a chore is assigned to a roommate

**Why:**
- A dashboard tells users what they need to do.
- Notifications prevent users from forgetting.
- These directly support the core purpose of the tool.

**Other options considered:**
- Dashboard only
- Notifications only
- Daily summaries
- Weekly reports
- Motivational notifications

Extra notification types can be added later.

---

### 3.5 Completing a Chore

**Decision:** One-tap “Done” button.

**Why:**
- Extremely simple.
- Low friction encourages people to actually use the tool.
- No unnecessary verification process.

**Other options considered:**
- Done + photo proof
- Done + roommate verification
- Combination of verification methods

Photo proof and verification could make sense in specific households, but they are unnecessary for the MVP.

---

### 3.6 Completion History

**Decision:** Basic history.

Track:
- Chore
- Person who completed it
- Date/time of completion

**Why:**
- Provides accountability.
- Allows roommates to see whether chores are being completed.
- Gives useful information without introducing gamification.

**Other options considered:**
- No history
- History + statistics
- History + leaderboard
- History + statistics without leaderboard

For the MVP, basic history is enough.

---

### 3.7 Joining a Household

**Decision:** Account + invite code.

Basic flow:

1. User creates an account.
2. One roommate creates a household.
3. The household has an invite code.
4. Other roommates enter the code to join.

**Why:**
- Simple onboarding.
- Easy to implement.
- Suitable for a shared apartment.

**Other options considered:**
- Invitation link
- Invite code + invitation link
- No accounts, just names

Invitation links can be added later.

---

### 3.8 Chore Management Permissions

**Decision:** Any roommate can create and manage chores.

**Why:**
- Avoids unnecessary hierarchy.
- All roommates share responsibility for the household.
- Keeps the permission system simple.

**Other options considered:**
- One household admin
- Admin creates chores while roommates can suggest them
- Admin manages everything

Admin roles may become useful later for larger groups.

---

### 3.9 Missed Chores

**Decision:** Mark the chore overdue, notify the responsible roommate, and automatically move it to the next roommate.

**Why:**
- The missed chore should not disappear.
- The responsible person should know that it is overdue.
- Automatic reassignment prevents household work from getting stuck.

**Other options considered:**
- Only mark as overdue
- Automatically move it to the next roommate
- Leave it overdue without reassignment

The chosen approach balances accountability and keeping the household running.

---

### 3.10 Chore Swapping

**Decision:** Allow swaps, but require approval from the other roommate.

**Why:**
- Roommates sometimes have schedule conflicts.
- Requiring approval prevents someone from unilaterally changing another person's responsibility.
- Keeps the rotation system flexible without removing accountability.

**Other options considered:**
- No swaps
- Swaps without approval
- Only the household creator can approve swaps

The approval-based approach is the best balance for the MVP.

---

### 3.11 Main Dashboard

**Decision:** Show today's chores only.

The dashboard should primarily show:
- Today's chores
- Who is responsible
- Due status
- Done button
- Overdue status when applicable

**Why:**
- Users mainly need to know: “What do I need to do today?”
- Keeps the interface simple.
- Prevents the MVP from becoming a complicated calendar/task-management application.

**Other options considered:**
- This week's chores
- Everyone's chores + overdue + upcoming chores
- Fully customizable dashboard

Those views can be added later.

---

## 4. Chore Creation Fields

For the MVP, each chore should have:

- **Chore name** — required
- **Description** — optional
- **Frequency** — required
- **Due date/time** — required
- **Participants** — required

### Why these fields?

They are enough to make the rotation system work without overwhelming users.

### Fields deliberately excluded from MVP

- Priority
- Estimated completion time
- Category
- Difficulty
- Attachments
- Location

These may be useful later, but they are not essential to the core workflow.

---

## 5. Authentication

**Decision:** Email + password.

**Why:**
- Simple and familiar.
- Enough for an MVP.
- Avoids additional complexity.

**Other options considered:**
- Google login
- Apple login
- Phone OTP
- Social login

These can be added later if convenience becomes important.

---

## 6. Household Structure

**Decision:** One household per user initially.

A user joins one household using an invite code.

**Why:**
- Simplifies the database and permissions model.
- Matches the main use case.
- Avoids unnecessary complexity in the first version.

**Other option considered:**
- Users belonging to multiple households.

Multi-household support can be considered for a future version.

---

## 7. Chore Deletion

**Decision:** Use soft deletion.

When a chore is removed, its previous completion history should remain available.

**Why:**
- Prevents historical records from being accidentally destroyed.
- Keeps completion history accurate.
- Makes future reporting easier.

**Other option considered:**
- Permanent deletion.

Permanent deletion is simpler conceptually but can destroy useful historical information.

---

## 8. Features Explicitly OUT of the MVP

The following should NOT be built initially:

- Leaderboards
- Points/rewards
- Photo proof
- AI chore suggestions
- Expense/bill splitting
- Shopping lists
- Calendar integration
- Multiple households per user
- Advanced analytics
- Chat
- Complex roles/permissions
- Motivational/gamification systems
- Advanced reporting

These can become potential V2 features after validating the core product.

---

## 9. MVP Product Definition

### Target

Roommates living together who need a simple way to share household chores fairly.

### Core Problem

Roommates often forget chores, have unclear responsibilities, or feel that chores are not being distributed fairly.

### Core Solution

Automatically rotate chores between roommates, remind the responsible person, allow them to mark the chore as done, and maintain a basic completion history.

### Core User Experience

1. Create an account.
2. Create or join a household.
3. Share the household invite code.
4. Roommates join.
5. Any roommate creates chores.
6. Set the chore frequency.
7. The system automatically assigns/rotates the chore.
8. Each roommate sees today's chores.
9. The system sends reminders.
10. The roommate taps **Done**.
11. Completion is recorded in history.
12. If the chore is missed, it becomes overdue and the next roommate receives the chore according to the rotation rules.
13. Roommates can request chore swaps, subject to the other roommate's approval.

---

## 10. MVP Philosophy

The MVP should answer one question:

> **Can a group of roommates easily divide, complete, and rotate household chores without needing someone to manually manage everything?**

Everything that does not directly help answer that question should generally be postponed.

The product should prioritize:

**Simple → Fair → Automatic → Accountable**

rather than:

**Complex → Feature-heavy → Highly customizable**

---

## 11. Potential V2 Features

Once the MVP is working, potential additions include:

- Weekly chore overview
- Advanced statistics
- Leaderboards
- Points and rewards
- Photo proof
- Calendar integration
- Multiple households per account
- Invitation links
- Google/Apple login
- Chore categories
- Priority levels
- Estimated chore duration
- AI-powered chore suggestions
- Bill/expense splitting
- Household chat
- Advanced admin roles
- Weekly summary notifications
