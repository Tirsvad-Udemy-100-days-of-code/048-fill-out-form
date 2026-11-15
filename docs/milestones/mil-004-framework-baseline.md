# MIL-004 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [PP-001], [MIL-003] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [90ad973] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added task 6 and criterion 9 (the container of `docker/Dockerfile` runs as a user without root rights, so the OpenGrep scan passes without a suppression); reviewed in autonomous mode, not independent | pending |

---

## Purpose

This gate decides whether Fill Out Form has the baseline of the framework: the adopted framework release, the wiki in English, Danish and Bahasa Malaysia in the framework's shape (sidebar with the title, one list of the English pages and the Languages section last, every page starting with its language line), the README in the framework template with an appendix that lists only the documents of the repository, complete licence and project URL metadata, a passing test suite and reviewed documents, merged to the default branch with a green build. One behaviour-neutral change of the container set-up is part of it, so that the OpenGrep scan of the pull request passes without a suppression. The work is delivered on the branch `mil-004-framework-baseline` and one pull request. It changes no behaviour of the program.

## Deliverable

A merged pull request that holds: the updated Business Case, Project Plan, Artifact Registry and Traceability Matrix, this milestone and their review records; the wiki sidebar in the framework's shape and the review record of the wiki; the README without the private framework files in its appendix; `pyproject.toml` with the project URLs and a build requirement that reads the licence expression; `.editorconfig` and `.env.example` of the framework baseline (the settings of the program are kept in it as comments); and the framework release adopted by the project. The program (`src/`) and the tests (`tests/`) do not change; `docker/Dockerfile` gets a user without root rights.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, PP-001 and MIL-004 each have an `Accepted` Version History row and a review record, and the wiki has a review record | Verdict `Go` (the wiki `Go-with-conditions` until it is checked on the host) | Any missing or `No-Go` |
| 2 | `python -m pytest` runs (the unit tests use fakes and a local copy of the form and need no browser and no network) and `git diff origin/main --stat -- src tests` lists no file | Exit code 0 and an empty diff | Any failure or any change |
| 3 | `docs/wiki/` has `_Sidebar.md` and the four pages Home, Step-1-Link-Click, Step-2-Search and Step-3-Form in en, da and ms (12 pages), directly in the folder, each starting with the language line, and the sidebar has the title, one list of the English pages and the Languages section last, with no Related section | 12 pages and the sidebar | A page or language missing, a page without the language line first, a subfolder, or a sidebar of another shape |
| 4 | `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license` (a licence expression), `license-files` and the project URLs for the repository, the documentation and the issue tracker, and requires a setuptools version that reads the licence expression | All set | Any missing |
| 6 | `.env.example` is tracked and holds empty placeholders for the framework tokens and, as comments, the settings of the program (`CHROME_BIN`, `RESULTS_DIR`); `.env` is not tracked | Present, no real value | Missing, a real value present or `.env` tracked |
| 7 | All CI checks of the pull request | Green | Red or pending |
| 8 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |
| 9 | `docker/Dockerfile` sets a `USER` that is not `root` before its `CMD`, and the OpenGrep check of the pull request passes without a suppression | Both | Either fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted | Baselines the finished program, its tests, its README and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 5 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| Objective 6 | Criteria 1, 3, 4, 5, 6, 8 and 9 (documents, wiki, README, licence, environment template, issues and container user) |
| Success criterion 7 | Criteria 1, 2, 3, 4, 7 and 9 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint for this milestone requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules` (lowercase repository URL), install the skills and hooks, add `.editorconfig`, bring `.env.example` to the framework's template and keep the settings of the program in it, so the project follows the same rules as the other projects of the portfolio. | No | BC-001 objective 6 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case, Project Plan and Traceability Matrix, set the domain of the changed documents to education, bring the Artifact Registry up to date and review each changed document against its QC checklist, so the plan-first gate is met. | No | BC-001 objective 6 |
| 3 | Bring the wiki sidebar to the framework's shape | Give the sidebar the wiki title, one list of the English pages and the Languages section last, check the page sets and the flat folder against the wiki checklist, and add a review record for the wiki. | No | BC-001 objectives 4 and 6 |
| 4 | Bring the README to the framework template | Keep the text of the README, describe the framework files in the repository layout, name the licence expression and give the appendix only the documents that are in the repository, so the README is complete and checkable. | No | BC-001 objective 6 |
| 5 | Complete the package metadata | Add the project URLs to `pyproject.toml` and raise the build requirement to the setuptools version that reads a licence expression, so package tools can read them. | No | BC-001 objective 6 |
| 6 | Run the container as a user without root rights | Add a user with the id 1000 that owns `/results`, and a `USER` line before the `CMD` in `docker/Dockerfile`, so that the OpenGrep rule `missing-user` no longer matches. The scan is not suppressed. The program, its options and the folder of the screenshots are unchanged. The image is not built or run in this milestone (that needs Docker and a browser); on Linux the folder given as `results/` must be writable by the user id 1000. | No | BC-001 objective 6 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-documentation.md
[90ad973]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/90ad973aec2f4c57daaa1ec1dbc194932214cce0
