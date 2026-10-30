"""Focused tests for UniCourse MOD-04 – Student Self-Service."""
from src.Module3.module3_service import register_for_class
from src.Module4.module4_service import get_student_profile, get_student_registrations, get_student_dashboard

def test_student_profile_is_scoped_to_given_student(seeded):
    profile = get_student_profile(seeded["student"])
    assert profile["student_code"] == "S001"
    assert profile["email"] == "student@example.com"

def test_student_registration_list_and_dashboard(seeded, db):
    section = seeded["make_section"]()
    register_for_class(db, seeded["student"], section.id)
    rows = get_student_registrations(db, seeded["student"])
    dashboard = get_student_dashboard(db, seeded["student"])
    assert len(rows) == 1
    assert dashboard["confirmed_registration_count"] == 1
    assert dashboard["registrations"][0]["course_code"] == "SE101"
