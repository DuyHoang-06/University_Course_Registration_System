"""Focused tests for UniCourse MOD-01 – Authentication & Account Management."""
import pytest
from fastapi import HTTPException
from src.Module1.module1_service import register_student_account, authenticate_user

def test_authenticate_active_user(seeded, db):
    user = authenticate_user(db, email="student@example.com", password="Student123!")
    assert user.id == seeded["student"].id
    assert user.role == "student"

def test_authenticate_rejects_wrong_password(db, seeded):
    with pytest.raises(HTTPException) as error:
        authenticate_user(db, email="student@example.com", password="wrong")
    assert error.value.status_code == 401

def test_register_student_account(seeded, db):
    user = register_student_account(db, email="new@example.com", password="Password123!",
        first_name="New", last_name="Student", student_code="S003",
        program_id=seeded["student"].program_id)
    assert user.email == "new@example.com"
    assert user.role == "student"

def test_register_rejects_duplicate_email(seeded, db):
    with pytest.raises(HTTPException) as error:
        register_student_account(db, email="student@example.com", password="Password123!",
            first_name="New", last_name="Student", student_code="S004",
            program_id=seeded["student"].program_id)
    assert error.value.status_code == 409
