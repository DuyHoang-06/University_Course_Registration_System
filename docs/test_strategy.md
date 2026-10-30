# Verification and test strategy

## Levels
- Unit: time overlap, validation and password hashing.
- Service integration: registration persistence, capacity updates, notification creation and cancellation.
- API/security: authentication, role-protected endpoint behavior, ownership scope, and administration operations.
- Manual API review: inspect request/response behavior through OpenAPI documentation and verify role-specific workflows.
- Non-functional: load, availability, usability, security review and maintainability coverage.

## Local execution
`python -m pytest -v`

## Test data isolation
Automated service tests create a fresh in-memory SQLite database for each test using SQLAlchemy metadata and a fixture. This database is test-only and does not imply a production database selection.

## Acceptance boundaries
The local suite verifies business behavior in a controlled environment. It does not verify 500 concurrent users, 99% availability, browser compatibility, production DB locking semantics or third-party integrations. These require a deployed test environment. The current deliverable is a backend/API package and does not include a browser frontend.
