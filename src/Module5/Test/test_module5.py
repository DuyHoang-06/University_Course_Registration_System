"""Focused tests for UniCourse MOD-05 – Lecturer Workspace."""
from src.Module5.module5_service import get_assigned_teaching_sections

def test_lecturer_sees_only_assigned_sections(seeded, db):
    own = seeded["make_section"]()
    other_lecturer = __import__("backend.models", fromlist=["User"]).User(
        email="lecturer2@example.com", password_hash="x", first_name="Second",
        last_name="Lecturer", role="lecturer", program_id=seeded["student"].program_id)
    db.add(other_lecturer); db.commit(); db.refresh(other_lecturer)
    from backend.models import CourseSection
    other = CourseSection(course_id=seeded["course"].id, lecturer_id=other_lecturer.id,
        room="B202", day_of_week=1, start_time=__import__("datetime").time(8,0),
        end_time=__import__("datetime").time(10,0), capacity=30, enrolled_count=0,
        semester="2026-1", status="open")
    db.add(other); db.commit()
    rows = get_assigned_teaching_sections(db, seeded["lecturer"])
    assert [row.id for row in rows] == [own.id]
