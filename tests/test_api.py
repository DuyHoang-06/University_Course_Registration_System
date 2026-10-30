from fastapi.testclient import TestClient
from backend.main import app
from backend.database import get_db
from backend.models import User, CourseSection
from sqlalchemy import select

def test_health_endpoint():
    with TestClient(app) as client:
        assert client.get("/health").json()["status"] == "ok"

def test_student_login_and_role_protected_endpoint(db, seeded):
    def override_db():
        yield db
    app.dependency_overrides[get_db]=override_db
    try:
        with TestClient(app) as client:
            response=client.post("/api/auth/login", json={"email":"student@example.com","password":"Student123!"})
            assert response.status_code == 200
            assert client.get("/api/student/profile").status_code == 200
            assert client.get("/api/admin/statistics").status_code == 403
    finally:
        app.dependency_overrides.clear()

def test_anonymous_cannot_access_student_endpoint(db):
    def override_db():
        yield db
    app.dependency_overrides[get_db]=override_db
    try:
        with TestClient(app) as client:
            assert client.get("/api/student/sections").status_code == 401
    finally:
        app.dependency_overrides.clear()


def test_student_registrations_endpoint_and_lecturer_scope(db, seeded):
    section = seeded["make_section"]()
    def override_db():
        yield db
    app.dependency_overrides[get_db]=override_db
    try:
        with TestClient(app) as client:
            client.post("/api/auth/login", json={"email":"student@example.com","password":"Student123!"})
            assert client.get("/api/student/registrations").status_code == 200
            client.post("/api/auth/logout")
            client.post("/api/auth/login", json={"email":"lecturer@example.com","password":"Lecturer123!"})
            response = client.get("/api/lecturer/sections")
            assert response.status_code == 200
            assert [item["id"] for item in response.json()] == [section.id]
    finally:
        app.dependency_overrides.clear()
