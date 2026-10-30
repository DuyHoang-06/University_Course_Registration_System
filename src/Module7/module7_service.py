"""UniCourse MOD-07 – Notification Management.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from sqlalchemy import select
from backend.models import Notification

def get_user_notifications(db, user):
    return db.scalars(select(Notification).where(Notification.user_id == user.id)
        .order_by(Notification.created_at.desc())).all()

def create_notification(db, *, user_id, title, message):
    item = Notification(user_id=user_id, title=title, message=message)
    db.add(item); db.commit(); db.refresh(item)
    return item
