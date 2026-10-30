from fastapi.testclient import TestClient
from backend.main import app
from backend.database import get_db
from backend.services.registration_service import register_student


def test_student_dashboard_contains_only_own_registration_data(db, seeded):
    section = seeded["make_section"]()
    register_student(db, seeded["student"], section.id)
    def override_db():
        yield db
    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as client:
            client.post("/api/auth/login", json={
                "email": "student@example.com", "password": "Student123!"
            })
            response = client.get("/api/student/dashboard")
            assert response.status_code == 200
            data = response.json()
            assert data["confirmed_registration_count"] == 1
            assert data["registrations"][0]["course_code"] == "SE101"
    finally:
        app.dependency_overrides.clear()
