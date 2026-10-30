"""Focused tests for UniCourse MOD-03 – Registration & Validation."""
import pytest
from fastapi import HTTPException
from src.Module3.module3_service import register_for_class, cancel_class_registration, overlaps

def test_registration_creates_record_and_confirmation(seeded, db):
    section = seeded["make_section"]()
    registration = register_for_class(db, seeded["student"], section.id)
    assert registration.status == "confirmed"
    assert section.enrolled_count == 1

def test_registration_rejects_full_section(seeded, db):
    section = seeded["make_section"](capacity=1, enrolled=1)
    with pytest.raises(HTTPException) as error:
        register_for_class(db, seeded["student"], section.id)
    assert error.value.status_code == 409

def test_cancel_registration_decrements_enrollment(seeded, db):
    section = seeded["make_section"]()
    registration = register_for_class(db, seeded["student"], section.id)
    cancelled = cancel_class_registration(db, seeded["student"], registration.id)
    assert cancelled.status == "cancelled"
    assert section.enrolled_count == 0

def test_adjacent_class_intervals_do_not_overlap():
    from datetime import time
    assert overlaps(time(8,0), time(10,0), time(9,59), time(11,0))
    assert not overlaps(time(8,0), time(10,0), time(10,0), time(12,0))
