"""UniCourse MOD-06 – Administration & Class Management.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from backend.services.section_service import create_section, update_section, cancel_section, admin_statistics

def create_course_section(db, payload):
    return create_section(db, payload)

def update_course_section(db, section_id, payload):
    return update_section(db, section_id, payload)

def cancel_course_section(db, section_id):
    return cancel_section(db, section_id)

def get_administration_statistics(db):
    return admin_statistics(db)
