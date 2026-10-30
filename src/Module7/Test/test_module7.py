"""Focused tests for UniCourse MOD-07 – Notification Management."""
from src.Module7.module7_service import create_notification, get_user_notifications

def test_notification_list_is_recipient_scoped(seeded, db):
    create_notification(db, user_id=seeded["student"].id, title="Hello", message="For student")
    create_notification(db, user_id=seeded["other_student"].id, title="Other", message="For other")
    rows = get_user_notifications(db, seeded["student"])
    assert len(rows) == 1
    assert rows[0].title == "Hello"

def test_create_notification_persists_record(seeded, db):
    item = create_notification(db, user_id=seeded["student"].id,
        title="Registration successful", message="You are registered.")
    assert item.id is not None
    assert item.user_id == seeded["student"].id
