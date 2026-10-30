# Requirements baseline – UniCourse

The implementation is aligned with the supplied workbook `course_registration_system(2).xlsx`.

## Modules
1. Authentication & Account Management
2. Course Catalogue & Class Information
3. Registration & Validation
4. Student Self-Service
5. Lecturer Workspace
6. Administration & Class Management
7. Notification Management
8. Security & Data Integrity

## Registration invariants
- Section must exist and be open.
- Enrolled count must be lower than capacity.
- Student must not already have a confirmed registration for the section.
- Course program must match the student's program.
- Existing confirmed registrations on the same day must not overlap.
- Adjacent intervals are allowed: `[08:00, 10:00)` and `[10:00, 12:00)` do not overlap.
- A successful transaction creates a registration, increments the section count once and creates a notification.
- A rejected transaction must not leave partial writes.

## Roles
- Student: catalogue, own profile, own registrations and notifications.
- Lecturer: assigned teaching sections only.
- Administrator: section management and statistics.
- Database/notification components: persistence and event notification responsibilities.

## Non-functional targets from workbook
- NFR-001: 95th percentile interactive response time ≤ 2 seconds.
- NFR-002: ≥ 500 concurrent active users.
- NFR-003: ≥ 99% availability during registration window.
- NFR-004/NFR-005: zero successful unauthorized accesses.
- NFR-006: zero inconsistent committed registration transactions.
- NFR-007: zero invalid mandatory inputs persisted.
- NFR-008: actionable and understandable critical messages.
- NFR-009: ≥ 80% target coverage for critical registration service rules.
- NFR-010: 100% traceability of critical administrative operations when audit logging is enabled.

These are acceptance targets; they are not all demonstrated by the included local test suite.
