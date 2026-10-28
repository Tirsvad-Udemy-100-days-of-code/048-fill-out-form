# MIL-003 Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the project is explained well enough for course participants and GitHub viewers: a README with screenshots and a wiki in three languages describing what each lecture step teaches.

## Deliverable

Branch `mil-003-documentation` with the finished `README.md` showing the screenshots, and the wiki in `docs/wiki/` in English, Danish and Bahasa Malaysia with the same page set and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README shows one screenshot per lecture step and `check-readme.sh` passes | Both | Either fails |
| 2 | Every English wiki page has a `-da` and a `-ms` twin | Same page set in 3 languages | A page is missing |
| 3 | Each language line links to the other two languages | All links present | Any missing |
| 4 | Each wiki page explains what was gained in its lecture step | One section per step | Any missing |
| 5 | The review record of the wiki against the rules of `framework/process/wiki.md` is `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Needs the working code and the screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 4 | [BC-001] |
| Success criteria 2, 3 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-04 — the last day of the one-week window of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Finish README with screenshots | Add the three lecture-step screenshots, the run and test instructions and the appendix of project documents to `README.md` (CN-004, CN-007). | No | |
| 2 | Write English wiki | Write `Home`, one page per lecture step ("Link click", "Search", "Form") and `_Sidebar` in `docs/wiki/`, each explaining what was gained and showing the screenshot (CN-007). | No | |
| 3 | Write Danish wiki | Translate every English wiki page into Danish as `<Page>-da.md`, keeping code, commands and file names in English (CN-007). | No | |
| 4 | Write Bahasa Malaysia wiki | Translate every English wiki page into Bahasa Malaysia as `<Page>-ms.md`, keeping code, commands and file names in English (CN-007). | No | |
| 5 | Review wiki against the wiki rules | Review the three wiki languages against `framework/process/wiki.md` (no checklist exists for a wiki) and record the `RC-*` before the pull request. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-form-automation.md
