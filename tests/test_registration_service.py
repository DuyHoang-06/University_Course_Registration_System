from datetime import time
import pytest
from fastapi import HTTPException
from sqlalchemy import select, func
from backend.models import CourseSection, Registration, Notification
from backend.services.registration_service import overlaps, register_student, cancel_registration

def test_overlap_boundary_rule():
    assert overlaps(time(8), time(10), time(9), time(11))
    assert not overlaps(time(8), time(10), time(10), time(12))

def test_success_updates_registration_count_and_notification(db, seeded):
    s=seeded["make_section"]()
    reg=register_student(db, seeded["student"], s.id)
    assert reg.status == "confirmed"
    assert db.get(CourseSection, s.id).enrolled_count == 1
    assert db.scalar(select(func.count(Notification.id))) == 1

def test_duplicate_registration_rejected(db, seeded):
    s=seeded["make_section"]()
    register_student(db, seeded["student"], s.id)
    with pytest.raises(HTTPException) as exc:
        register_student(db, seeded["student"], s.id)
    assert exc.value.status_code == 409
    assert db.scalar(select(func.count(Registration.id))) == 1

def test_full_section_rejected_without_partial_write(db, seeded):
    s=seeded["make_section"](capacity=1, enrolled=1)
    with pytest.raises(HTTPException):
        register_student(db, seeded["student"], s.id)
    assert db.scalar(select(func.count(Registration.id))) == 0
    assert db.get(CourseSection, s.id).enrolled_count == 1
    assert db.scalar(select(func.count(Notification.id))) == 0

def test_closed_section_rejected(db, seeded):
    s=seeded["make_section"](status="closed")
    with pytest.raises(HTTPException):
        register_student(db, seeded["student"], s.id)
    assert db.scalar(select(func.count(Registration.id))) == 0

def test_program_eligibility_rejected(db, seeded):
    s=seeded["make_section"](course_obj=seeded["other_course"])
    with pytest.raises(HTTPException) as exc:
        register_student(db, seeded["student"], s.id)
    assert exc.value.status_code == 403

def test_schedule_overlap_rejected(db, seeded):
    first=seeded["make_section"]()
    register_student(db, seeded["student"], first.id)
    second=seeded["make_section"](day=0, start=time(9), end=time(11))
    with pytest.raises(HTTPException) as exc:
        register_student(db, seeded["student"], second.id)
    assert exc.value.status_code == 409
    assert db.get(CourseSection, second.id).enrolled_count == 0

def test_adjacent_schedule_allowed(db, seeded):
    first=seeded["make_section"]()
    register_student(db, seeded["student"], first.id)
    second=seeded["make_section"](day=0, start=time(10), end=time(12))
    reg=register_student(db, seeded["student"], second.id)
    assert reg.status == "confirmed"

def test_registration_persists_after_query(db, seeded):
    s=seeded["make_section"]()
    reg=register_student(db, seeded["student"], s.id)
    found=db.get(Registration, reg.id)
    assert found is not None and found.student_id == seeded["student"].id

def test_student_can_cancel_own_registration_and_release_seat(db, seeded):
    s=seeded["make_section"]()
    reg=register_student(db, seeded["student"], s.id)
    cancelled=cancel_registration(db, seeded["student"], reg.id)
    assert cancelled.status == "cancelled"
    assert db.get(CourseSection, s.id).enrolled_count == 0

def test_student_cannot_cancel_another_students_registration(db, seeded):
    s=seeded["make_section"]()
    reg=register_student(db, seeded["student"], s.id)
    with pytest.raises(HTTPException) as exc:
        cancel_registration(db, seeded["other_student"], reg.id)
    assert exc.value.status_code == 404
