"""Focused tests for UniCourse MOD-06 – Administration & Class Management."""
import pytest
from fastapi import HTTPException
from backend.schemas import SectionUpdate
from src.Module6.module6_service import cancel_course_section, get_administration_statistics, update_course_section

def test_admin_statistics_counts_core_records(seeded, db):
    seeded["make_section"]()
    stats = get_administration_statistics(db)
    assert stats["users"] == 4
    assert stats["courses"] == 2
    assert stats["sections"] == 1

def test_cancel_section_creates_notifications_for_registered_students(seeded, db):
    from src.Module3.module3_service import register_for_class
    section = seeded["make_section"]()
    register_for_class(db, seeded["student"], section.id)
    result = cancel_course_section(db, section.id)
    assert result["notified_students"] == 1
    assert section.status == "cancelled"

def test_update_section_rejects_capacity_below_enrollment(seeded, db):
    section = seeded["make_section"](capacity=10, enrolled=5)
    payload = SectionUpdate(course_id=section.course_id, lecturer_id=section.lecturer_id,
        room=section.room, day_of_week=section.day_of_week, start_time=section.start_time,
        end_time=section.end_time, capacity=4, semester=section.semester, status="open")
    with pytest.raises(HTTPException) as error:
        update_course_section(db, section.id, payload)
    assert error.value.status_code == 409
