"""UniCourse MOD-01 – Authentication & Account Management.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from sqlalchemy import select
from fastapi import HTTPException
from backend.models import User, Program
from backend.security import hash_password, verify_password

def register_student_account(db, *, email, password, first_name, last_name, student_code, program_id):
    if not db.get(Program, program_id):
        raise HTTPException(404, "Program not found")
    duplicate = db.scalar(select(User).where(User.email == email))
    if duplicate or db.scalar(select(User).where(User.student_code == student_code)):
        raise HTTPException(409, "Email or student code already exists")
    user = User(email=email, password_hash=hash_password(password), first_name=first_name,
                last_name=last_name, student_code=student_code, role="student", program_id=program_id)
    db.add(user); db.commit(); db.refresh(user)
    return user

def authenticate_user(db, *, email, password):
    user = db.scalar(select(User).where(User.email == email))
    if not user or not user.is_active or not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid email or password")
    return user

def logout_session(request):
    request.session.clear()
    return {"message": "Logged out"}
