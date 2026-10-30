from fastapi.testclient import TestClient
from backend.main import app
from backend.database import get_db
from backend.models import Notification


def test_notifications_endpoint_is_scoped_to_authenticated_user(db, seeded):
    db.add_all([
        Notification(user_id=seeded["student"].id, title="For student", message="Hello"),
        Notification(user_id=seeded["other_student"].id, title="Private", message="Not yours"),
    ])
    db.commit()
    def override_db():
        yield db
    app.dependency_overrides[get_db] = override_db
    try:
        with TestClient(app) as client:
            client.post("/api/auth/login", json={
                "email": "student@example.com", "password": "Student123!"
            })
            response = client.get("/api/notifications")
            assert response.status_code == 200
            assert [item["title"] for item in response.json()] == ["For student"]
    finally:
        app.dependency_overrides.clear()
