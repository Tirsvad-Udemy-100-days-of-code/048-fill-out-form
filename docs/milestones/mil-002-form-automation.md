# MIL-002 Form automation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e1a3d8d] |

---

## Purpose

Decide whether the three lecture steps (click a link by its text, search and press Enter, fill out and submit a form) work, are tested, and have screenshots.

## Deliverable

Branch `mil-002-form-automation` with the `fill_out_form` package, a runnable entry point, pytest tests, a local form fixture, and one screenshot per lecture step in `docs/images/`, captured in Docker.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` exits 0 on the host without a browser | Exit 0 | Non-zero |
| 2 | The Docker end-to-end run exits 0 and writes three screenshots | Exit 0 and three PNG files | Otherwise |
| 3 | Every selector, URL and text is defined in `constants.py` | No literal selector or URL elsewhere under `src/` | Any found |
| 4 | Public functions carry Doxygen comments | All public functions | Any missing |
| 5 | The code review record against `QC-PY-001` is `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the project configuration, constants file and tooling |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2 | [BC-001] |
| Success criteria 1 and 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-01 — inside the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement driver factory | Create `create_driver` that returns a Chrome WebDriver, headless when requested, so the same code runs on a desktop-less Docker container (CN-002). | No | |
| 2 | Implement click_link_by_text | Open the Wikipedia main page and click the link whose text is "Content portals" with `By.LINK_TEXT`, as the lecture shows (CN-002, CN-003). | No | |
| 3 | Implement search_for | Find the search input by its `name` attribute, type "Python" and press `Keys.ENTER` (CN-002, CN-003). | No | |
| 4 | Implement fill_out_form | Find first name, last name and email fields with CSS selectors, type the values from `constants.py` and click the sign-up button (CN-002, CN-003). | No | |
| 5 | Add the main entry point | Add `python -m fill_out_form` that runs the three steps in order and optionally saves a screenshot after each step (CN-004, CN-007). | No | |
| 6 | Add local form fixture and unit tests | Add an HTML form fixture with the same field names and pytest tests that use a fake driver for the logic and need no browser (CN-002). | No | |
| 7 | Run end-to-end in Docker and capture screenshots | Run the three steps in a headless Chrome Docker container with a shared results folder (Docker container; never the host desktop) and save one screenshot per step to `docs/images/` (CN-007). | No | |
| 8 | Review code against the Python checklist | Review `src/` and `tests/` against `qc-programming-python` and record the `RC-*` before the pull request. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-project-setup.md
[e1a3d8d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/e1a3d8d304d4b6ece1a3f95ee02b597e30a97520
