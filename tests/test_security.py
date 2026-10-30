from backend.security import hash_password, verify_password
from backend.models import User

def test_password_hash_is_not_plain_text():
    encoded=hash_password("Student123!")
    assert encoded != "Student123!"
    assert verify_password("Student123!", encoded)
    assert not verify_password("wrong", encoded)

def test_role_values_are_explicit(seeded):
    assert seeded["student"].role == "student"
    assert seeded["lecturer"].role == "lecturer"
    assert seeded["admin"].role == "administrator"
