"""UniCourse MOD-02 – Course Catalogue & Class Information.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from backend.services.section_service import list_open_sections

def get_available_sections(db, student):
    """Return open sections restricted to the authenticated student's program."""
    return list_open_sections(db, student.program_id)
