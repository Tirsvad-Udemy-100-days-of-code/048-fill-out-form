# SQA Review Record: code of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e764269] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case functions, PascalCase classes and Protocols, UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`click_link_by_text`, `search_for`, `fill_out_form`, `run_lecture`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` and `ruff format --check .` pass; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes on 25 files; every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; the CLI uses try/finally so the browser is always quit. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults (`form_data: FormData | None = None`); no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files are opened; screenshots go through the driver, directories through pathlib. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a Doxygen docstring; `doxygen Doxyfile` runs without warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging` is used, no `print`; only the test email address is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | N-A: no Design Class Diagram exists; the tasks are plain technical tasks. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 30 offline unit tests with fakes, named for behaviour; the e2e test is deselected by default and passed in Docker (1 passed). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` has no errors and `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `selenium>=4.25,<5` is the only runtime dependency and is used. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | URLs, locators, texts and file names are defined once in `constants.py`; a grep finds none elsewhere under `src/`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` and `application` import no selenium; selenium appears only in `infrastructure` (and the structural check in tests). |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each module has one reason to change; steps depend on narrow Protocols (`ElementPort`, `BrowserPort`). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Source in `domain`, `application`, `infrastructure`, `presentation`; tests in `unit`, `e2e`, `fixtures`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English with allowed characters. |

## Overall Verdict

Go — every Mandatory criterion passes; no blocking finding. Files: src/fill_out_form and tests/ at commit of this milestone. Observation: the live demo form rejects the default example.com address; documented in the README and wiki.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[MIL-002]: ../../milestones/mil-002-form-automation.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[e764269]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/e764269eda7ccba732556b4c59bd8778483a6991
