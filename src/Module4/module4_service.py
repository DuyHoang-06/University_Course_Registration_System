"""UniCourse MOD-04 – Student Self-Service.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from backend.models import Registration, CourseSection

def get_student_profile(student):
    return {"id": student.id, "email": student.email, "first_name": student.first_name,
            "last_name": student.last_name, "student_code": student.student_code,
            "program_id": student.program_id}

def get_student_registrations(db, student):
    return db.scalars(select(Registration)
        .options(joinedload(Registration.section).joinedload(CourseSection.course))
        .where(Registration.student_id == student.id)
        .order_by(Registration.registered_at.desc())).unique().all()

def get_student_dashboard(db, student):
    regs = [r for r in get_student_registrations(db, student) if r.status == "confirmed"]
    return {"student": {"id": student.id, "name": f"{student.first_name} {student.last_name}",
            "student_code": student.student_code, "program_id": student.program_id},
            "confirmed_registration_count": len(regs), "registrations": [
            {"registration_id": r.id, "section_id": r.section_id, "course_code": r.section.course.code,
             "course_name": r.section.course.name, "status": r.status} for r in regs]}
