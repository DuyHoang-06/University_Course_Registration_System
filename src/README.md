# UniCourse source modules

This folder mirrors the reference repository's module-oriented structure and expands it to all eight UniCourse modules.

```text
src/
├── Module1/
│   ├── module1_service.py
│   └── Test/test_module1.py
...
└── Module8/
    ├── module8_service.py
    └── Test/test_module8.py
```

Each module contains its own service facade, README and focused tests. The canonical integrated implementation is shared in the project-level `backend/` package so that the module folders do not maintain conflicting copies of API and domain logic.

Run all module tests from the project root:
```bash
python -m pytest src -q
```

Run one module:
```bash
python -m pytest src/Module3/Test -q
```
