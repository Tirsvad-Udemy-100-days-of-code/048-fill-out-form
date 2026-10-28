# MIL-001 Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the repository is configured well enough to start writing the Selenium code: project configuration, folder structure, constants, tooling, documentation skeleton and repository metadata.

## Deliverable

A repository on branch `mil-001-project-setup` with `pyproject.toml`, the `src/` and `tests/` skeleton, `constants.py`, a Python `.gitignore`, a `Doxyfile`, the README with venv instructions, ADR-0001, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `python -m pip install --upgrade pip` and `pip install -e ".[dev]"` succeed on Python 3.13 | All three succeed | Any fails |
| 2 | `pytest` runs and exits 0 on the skeleton | Exit 0 | Non-zero |
| 3 | `[project] dependencies` lists only selenium | Only selenium | Any other runtime dependency |
| 4 | The git host shows a description and at least 5 topics | Both present | Either missing |
| 5 | `.env` is ignored and is not read by any file under `src/` or `tests/` | `git check-ignore .env` succeeds; no match for `.env` in code | Otherwise |
| 6 | The code review record against `QC-PY-001` is `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; the Business Case, Stakeholder Analysis and Project Plan are accepted before it starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5 (repository configuration) | [BC-001] |
| Success criteria 4 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-29 — inside the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a short description and topics (python, selenium, udemy, 100-days-of-code, web-automation, pytest) on the git host through its API. The token is read from the shell environment loaded from `.env` by the operator and is never printed, committed, tested or imported by the project (CN-005). | No | |
| 2 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.venv/`, `.env`, build output, caches and generated Doxygen output so that no secret or artifact is committed (CN-005). | No | |
| 3 | Create pyproject.toml and package layout | Configure the project in `pyproject.toml` with `requires-python = ">=3.13"`, selenium as the only runtime dependency, pytest as a `dev` extra, and the `src/fill_out_form/` and `tests/` folders (CN-006). | No | |
| 4 | Create constants.py | Put every URL, selector, link text, search term, field value and timeout in `constants.py` so the logic has no magic values (CN-003). | No | |
| 5 | Add Doxyfile | Add a `Doxyfile` configured for Python sources in `src/` and write Doxygen-style comments in the skeleton (CN-003). | No | |
| 6 | Write README with venv and test instructions | Create `README.md` from the framework template with how to create a local `.venv`, run `python -m pip install --upgrade pip`, install, run and test (CN-004). | No | |
| 7 | Record dependency and fixture decisions as ADR-0001 | Record that selenium is the only runtime dependency, that the form step has a local HTML fixture because the original demo site may be offline, and that browser runs happen in Docker (CN-006). | No | |

---

[BC-001]: ../business-case.md
