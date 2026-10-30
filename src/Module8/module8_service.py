"""UniCourse MOD-08 – Security & Data Integrity.

Module-focused service facade; business logic is shared with the canonical backend package.
"""
from contextlib import contextmanager
from backend.security import hash_password, verify_password, get_current_user, require_roles

@contextmanager
def atomic_operation(db):
    """Provide a transaction boundary and rollback if the operation raises."""
    try:
        yield
        db.commit()
    except Exception:
        db.rollback()
        raise

__all__ = ["hash_password", "verify_password", "get_current_user", "require_roles", "atomic_operation"]
