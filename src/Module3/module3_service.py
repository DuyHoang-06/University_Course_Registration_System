"""UniCourse MOD-03 – Registration & Validation.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from backend.services.registration_service import register_student, cancel_registration, overlaps

def register_for_class(db, student, section_id):
    return register_student(db, student, section_id)

def cancel_class_registration(db, student, registration_id):
    return cancel_registration(db, student, registration_id)
