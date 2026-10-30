# API reference

All routes exchange JSON unless noted. Authentication uses a session cookie; retain the cookie returned by login/register for subsequent requests.

| Method | Endpoint | Role | Purpose |
|---|---|---|---|
| POST | `/api/auth/register` | Public | Create a student account |
| POST | `/api/auth/login` | Public | Authenticate |
| POST | `/api/auth/logout` | Authenticated session | End session |
| GET | `/api/auth/me` | Any authenticated | Current user |
| GET | `/api/student/sections` | Student | Open eligible sections |
| POST | `/api/student/registrations/{section_id}` | Student | Register |
| GET | `/api/student/registrations` | Student | Own registrations |
| POST | `/api/student/registrations/{registration_id}/cancel` | Student | Cancel own registration |
| GET | `/api/student/profile` | Student | Own profile |\n| GET | `/api/student/dashboard` | Student | Own profile summary and own confirmed registrations |
| GET | `/api/notifications` | Any authenticated | Own notifications |
| GET | `/api/student/notifications` | Student | Student notification list (compatibility route) |
| GET | `/api/lecturer/sections` | Lecturer | Assigned teaching sections |
| GET | `/api/admin/statistics` | Administrator | Current statistics |
| POST | `/api/admin/sections` | Administrator | Create section |
| PUT | `/api/admin/sections/{section_id}` | Administrator | Edit section |
| POST | `/api/admin/sections/{section_id}/cancel` | Administrator | Cancel section and notify enrolled students |

Interactive OpenAPI documentation is available at `/docs` when the API server is running. No browser frontend is included.
