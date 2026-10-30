from datetime import time
from fastapi.testclient import TestClient
from backend.main import app
from backend.database import get_db
from backend.models import CourseSection


def test_admin_can_update_section_and_capacity_cannot_underflow(db, seeded):
    section = seeded["make_section"](capacity=40)
    def override_db():
        yield db
    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as client:
            client.post("/api/auth/login", json={
                "email": "admin@example.com", "password": "Admin123!"
            })
            response = client.put(f"/api/admin/sections/{section.id}", json={
                "course_id": seeded["course"].id,
                "lecturer_id": seeded["lecturer"].id,
                "room": "B202",
                "day_of_week": 1,
                "start_time": "09:00:00",
                "end_time": "11:00:00",
                "capacity": 30,
                "semester": "2026-1",
                "status": "open"
            })
            assert response.status_code == 200
            db.refresh(section)
            assert section.room == "B202"
            assert section.capacity == 30
    finally:
        app.dependency_overrides.clear()


def test_non_admin_cannot_update_section(db, seeded):
    section = seeded["make_section"]()
    def override_db():
        yield db
    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as client:
            client.post("/api/auth/login", json={
                "email": "student@example.com", "password": "Student123!"
            })
            response = client.put(f"/api/admin/sections/{section.id}", json={
                "course_id": seeded["course"].id,
                "lecturer_id": seeded["lecturer"].id,
                "room": "B202",
                "day_of_week": 1,
                "start_time": "09:00:00",
                "end_time": "11:00:00",
                "capacity": 30,
                "semester": "2026-1",
                "status": "open"
            })
            assert response.status_code == 403
    finally:
        app.dependency_overrides.clear()


def test_admin_cannot_reduce_capacity_below_enrollment(db, seeded):
    section = seeded["make_section"](capacity=5, enrolled=3)
    def override_db():
        yield db
    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as client:
            client.post("/api/auth/login", json={
                "email": "admin@example.com", "password": "Admin123!"
            })
            response = client.put(f"/api/admin/sections/{section.id}", json={
                "course_id": seeded["course"].id,
                "lecturer_id": seeded["lecturer"].id,
                "room": "B202",
                "day_of_week": 1,
                "start_time": "09:00:00",
                "end_time": "11:00:00",
                "capacity": 2,
                "semester": "2026-1",
                "status": "open"
            })
            assert response.status_code == 409
            db.refresh(section)
            assert section.capacity == 5
    finally:
        app.dependency_overrides.clear()
