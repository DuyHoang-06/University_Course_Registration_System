import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from backend.database import Base
from backend.models import Faculty, Program, User, Course, CourseSection
from backend.security import hash_password
from datetime import time

@pytest.fixture()
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    TestingSession = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    session = TestingSession()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
        engine.dispose()

@pytest.fixture()
def seeded(db):
    faculty = Faculty(name="Faculty of IT", code="FIT")
    db.add(faculty); db.flush()
    program = Program(name="Software Engineering", code="SE", faculty_id=faculty.id)
    other_program = Program(name="Business Administration", code="BA", faculty_id=faculty.id)
    db.add_all([program, other_program]); db.flush()
    student = User(email="student@example.com", password_hash=hash_password("Student123!"),
                   first_name="Test", last_name="Student", student_code="S001",
                   role="student", program_id=program.id)
    other_student = User(email="other@example.com", password_hash=hash_password("Student123!"),
                         first_name="Other", last_name="Student", student_code="S002",
                         role="student", program_id=program.id)
    lecturer = User(email="lecturer@example.com", password_hash=hash_password("Lecturer123!"),
                    first_name="Test", last_name="Lecturer", role="lecturer", program_id=program.id)
    admin = User(email="admin@example.com", password_hash=hash_password("Admin123!"),
                 first_name="Test", last_name="Admin", role="administrator")
    db.add_all([student, other_student, lecturer, admin]); db.flush()
    course = Course(code="SE101", name="Intro to SE", credits=3, fee=100, program_id=program.id)
    other_course = Course(code="BA101", name="Intro to BA", credits=3, fee=100, program_id=other_program.id)
    db.add_all([course, other_course]); db.flush()
    def make_section(course_obj=course, *, day=0, start=time(8,0), end=time(10,0),
                     capacity=40, enrolled=0, status="open"):
        section = CourseSection(course_id=course_obj.id, lecturer_id=lecturer.id,
            room="A101", day_of_week=day, start_time=start, end_time=end,
            capacity=capacity, enrolled_count=enrolled, status=status, semester="2026-1")
        db.add(section); db.commit(); db.refresh(section); return section
    db.commit()
    return {"student":student, "other_student":other_student, "lecturer":lecturer,
            "admin":admin, "course":course, "other_course":other_course,
            "make_section":make_section}
