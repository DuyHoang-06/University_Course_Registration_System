# MOD-03 – Registration & Validation

## Scope
Defined by the UniCourse requirements workbook.

## Module source
- `module3_service.py`: module-focused service facade / domain operations.
- `Test/test_module3.py`: focused automated tests.

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
python -m pytest src/Module3/Test -q
```
