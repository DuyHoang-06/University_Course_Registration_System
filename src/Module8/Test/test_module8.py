"""Focused tests for UniCourse MOD-08 – Security & Data Integrity."""
import pytest
from src.Module8.module8_service import hash_password, verify_password, atomic_operation

def test_password_hash_is_salted_and_verifiable():
    encoded = hash_password("UniCourse-Pass123!")
    assert encoded != "UniCourse-Pass123!"
    assert verify_password("UniCourse-Pass123!", encoded)
    assert not verify_password("wrong-password", encoded)

def test_atomic_operation_rolls_back_on_exception(seeded, db):
    from backend.models import Notification
    with pytest.raises(RuntimeError):
        with atomic_operation(db):
            db.add(Notification(user_id=seeded["student"].id, title="Temp", message="Rollback me"))
            raise RuntimeError("simulate failure")
    assert db.query(Notification).count() == 0
