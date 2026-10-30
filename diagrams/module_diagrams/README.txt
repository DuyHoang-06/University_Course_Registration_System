UNICOURSE – MODULE DIAGRAMS

Structure: module_diagrams/MOD-01 ... MOD-08/
Each module folder contains six PNG diagrams:
01_use_case.png
02_requirement_dependency.png
03_activity.png
04_sequence.png
05_domain_class.png
06_component.png

Source basis: course_registration_system(2).xlsx sheets modules, requirements, use_cases, actors, system_overview, data_dictionary, storage_design and traceability.
All diagrams are PNG. The Graphviz source files are intentionally not included in module folders.

Important source-data note:
- MOD-08 has no standalone use-case row in the workbook. Its use-case view therefore shows the three cross-cutting behaviors described by REQ-013, REQ-015 and REQ-018, without inventing UC identifiers.
- REQ-011 (Cancel Class) is referenced in UC-05, REQ-012 and traceability, but the requirements sheet has no REQ-011 row. MOD-06 dependency diagram marks it as provisional / missing from the requirements sheet.
- REQ-001 lists itself as a dependency; the meaningless self-loop is omitted.
- Class/domain diagrams show selected conceptual attributes from the data dictionary, not a complete physical database schema.
- Sequence and component diagrams are logical views inferred from the workbook's stated interfaces, storage and use-case flows; they are not claims that every component has already been implemented.