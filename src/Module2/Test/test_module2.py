"""Focused tests for UniCourse MOD-02 – Course Catalogue & Class Information."""
from src.Module2.module2_service import get_available_sections

def test_catalogue_returns_only_open_sections_in_student_program(seeded, db):
    make = seeded["make_section"]
    open_section = make()
    make(status="closed")
    make(course_obj=seeded["other_course"])
    rows = get_available_sections(db, seeded["student"])
    assert [row.id for row in rows] == [open_section.id]
