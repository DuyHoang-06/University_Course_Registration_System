"""UniCourse MOD-05 – Lecturer Workspace.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from backend.models import CourseSection

def get_assigned_teaching_sections(db, lecturer):
    """Only return sections assigned to the authenticated lecturer."""
    return db.scalars(select(CourseSection).options(joinedload(CourseSection.course))
        .where(CourseSection.lecturer_id == lecturer.id)
        .order_by(CourseSection.day_of_week, CourseSection.start_time)).unique().all()
