# MOD-08 – Security & Data Integrity

## Scope
Defined by the UniCourse requirements workbook.

## Module source
- `module8_service.py`: module-focused service facade / domain operations.
- `Test/test_module8.py`: focused automated tests.

## Shared implementation
The canonical FastAPI / SQLAlchemy implementation remains in `backend/`:
- routers: `backend/routers/`
- shared domain models: `backend/models.py`
- services: `backend/services/`
- authentication and access control: `backend/security.py`

The module source files delegate to the shared backend implementation where applicable. This avoids maintaining duplicated business rules in two places.

## Run module tests
From the project root:
```bash
python -m pytest src/Module8/Test -q
```
