# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e1a3d8d] |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 6, success criterion 7, a scope item, an out-of-scope item, a risk and constraints for the baseline milestone MIL-004; set the domain to education; reviewed in autonomous mode, not independent | [90ad973] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Scope wording: the baseline milestone includes one behaviour-neutral change of `docker/Dockerfile` (a user without root rights) so the OpenGrep scan passes; reviewed in autonomous mode, not independent | [087f57a] |

---

## Executive Summary

Day 48 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" teaches Selenium WebDriver: clicking links, typing into inputs, sending special keys and filling out a sign-up form. This project turns that assignment into a small, readable, runnable Python repository with tests, documentation, a screenshot for every lecture step and a three-language wiki. It is a learning and portfolio project with one person doing the work.

## Methodological and Standards Foundation

- The SQA and QC framework mounted at `framework/` governs documents, reviews and the plan-first gate.
- Quality characteristics follow ISO/IEC 25010:2023.
- Code follows the `coding-conventions` skill (Python) and the layering of the `clean-architecture` skill.
- Docs-as-code: every change reaches `main` by a pull request, one pull request per milestone.

## Problem Statement

- The course assignment is normally solved as one throw-away script. The author's earlier solution (the day-48 folder of a monolithic course repository) is a scratch file that does not follow the lecture, has no tests and no documentation.
- Other course participants cannot easily compare solutions or see what each lecture step produces.
- A repository without a description, topics and a README is neither found nor understood by GitHub viewers.

## Business Opportunity

A clean reference solution for the lecture lets the author keep a tidy portfolio, lets course participants compare solutions, and shows a repeatable project structure (src, tests, docs, wiki) for the remaining days of the course.

## Objectives

1. Deliver Python code that automates the lecture steps with Selenium: click a link by its text, search for "Python" and press Enter, and fill out a form (first name, last name, email) and click the sign-up button.
2. Deliver pytest tests for all logic that needs no browser.
3. Deliver a screenshot for each lecture step, shown in the README and the wiki.
4. Deliver a wiki in English, Danish and Bahasa Malaysia that explains what was gained in each lecture step.
5. Configure the repository: description, topics, Python `.gitignore`, `pyproject.toml`, Doxyfile, and instructions for a local `.venv`.
6. Bring the finished project to the common baseline of the framework: the adopted framework release, a wiki sidebar that follows the framework's shape, licence and project URL metadata, a README that lists only the documents of the repository, the editor and environment templates, and review records for every changed document ([MIL-004]).

## Scope

### In Scope

- Python 3.13 or newer package under `src/`, tests under `tests/`, documents under `docs/`.
- Constants in `constants.py`; Doxygen comments in the source and a `Doxyfile`.
- `pyproject.toml`, venv instructions (`python -m pip install --upgrade pip`), Python `.gitignore`.
- README from the framework template, with run and test instructions and screenshots.
- Wiki pages in English, Danish and Bahasa Malaysia (`docs/wiki/`), with the same screenshots.
- Repository description and topics on the git host.
- The baseline milestone [MIL-004]: the framework release, the wiki sidebar in the framework's shape, the README without the private framework files in its appendix, licence and project URL metadata, `.editorconfig`, `.env.example`, review records and the update of the traceability matrix. It changes no behaviour of the program; its only other change is one `USER` line with its user set-up in `docker/Dockerfile` so the OpenGrep scan passes (task 6).

### Out of Scope

- Running the browser automation on the host desktop (it runs in Docker, see `framework/process/gui-testing.md`).
- Later days of the course and the final project.
- Packaging for PyPI, a graphical front end, and a web service.
- Reading, testing or importing the personal tokens in `.env`.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-004]; its only change of a runtime file is the user set-up in `docker/Dockerfile` (task 6). That milestone opens no live web page, submits no form and runs no browser; the tests use fakes and a local copy of the form.

## Expected Benefits

### Tangible Benefits

- A runnable reference solution with passing tests.
- One screenshot per lecture step (at least three).
- Three language versions of the wiki.

### Intangible Benefits

- A reusable project layout for the other course days.
- Practice with Selenium, pytest and docs-as-code.
- A repository others can read and learn from.

## Strategic Alignment

The project supports the author's goal of completing the course with a documented, reviewable portfolio, and the framework's goal of showing the plan-first workflow on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100 % of pytest tests pass on Python 3.13 | `pytest` exit code 0 |
| 2 | Lecture steps covered | 3 of 3 steps (link click, search, form) implemented and shown by a screenshot | Files in `docs/images/` |
| 3 | Wiki languages | 3 of 3 languages with the same page set | Files in `docs/wiki/` |
| 4 | Runtime dependencies | Exactly 1 (selenium) | `dependencies` in `pyproject.toml` |
| 5 | Repository metadata | Description set and at least 5 topics | Git host API response |
| 6 | Quality gate | Every document and the code have an `RC-*` with verdict Go | `docs/sqa/reviews/` |
| 7 | The baseline milestone is done (objective 6) | The wiki sidebar has the framework's shape, `framework/scripts/check-readme.sh`, `check-languages.sh` and `check-editorconfig.sh` exit with code 0, `python -m pytest` passes, 100 % of the continuous integration (CI) checks of the pull request of [MIL-004] pass | Files in `docs/`, the script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The assignment's form page (a Heroku demo) is offline | The form step cannot be shown against the original site | A local HTML fixture with the same field names serves tests and screenshots; the original URL is a constant |
| Docker or the browser image is unavailable | No screenshots | Stop and report (gui-testing rule 5); never fall back to the host desktop |
| Wikipedia changes its page layout | Selectors break | Selectors live in `constants.py`; screenshots record the state on the capture date |
| Danish or Bahasa Malaysia text contains errors | Misleading text | English is authoritative; translations follow page by page; the author can correct them |
| Tokens in `.env` leak | Account compromise | `.env` is in `.gitignore` and is never read by project code or tests |
| The documents of the baseline milestone [MIL-004] change documents that were accepted earlier, and the AI stand-in for S01 reviews them | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, `src/` and `tests/` are not changed, the tests run before and after, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- S01 is Product Owner, developer and reviewer; in autonomous mode the AI stands in for the reviewer, recorded as not independent.
- Docker is installed on the author's machine.
- The git host accepts the token in `.env` for repository and issue operations.
- "Python greater than 3.13" is read as 3.13 or newer (`requires-python = ">=3.13"`).

## Constraints

- Duration: one week, 2026-10-28 to 2026-11-04.
- The baseline milestone [MIL-004] starts 2026-11-16 and is finished within one week, by 2026-11-23. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.
- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Only runtime dependency: selenium.
- The Product Owner (PO) language is English and the PO domain is education (it was IT until [MIL-004]; the documents that [MIL-004] does not change keep the domain `it`, see the Open Issues of [PP-001]).

## Cost–Benefit Assessment

Qualitative, because the project is unpaid learning work with no revenue.

| Costs | Benefits |
| --- | --- |
| About one week of the author's time and AI usage | A reference solution, documentation in three languages and a reusable project layout |
| A Docker image download | Safe, reproducible browser runs |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants a tidy portfolio piece (CN-001, CN-002, CN-007) |
| S02 | Wants readable, runnable code with the assignment's function names and run instructions (CN-003, CN-004) |
| S03 | Wants a clear repository description, topics and README, and no unnecessary runtime dependencies (CN-005, CN-006) |

## Recommendation

Proceed — the scope is small, the risks are mitigated and the outcome is a reusable reference.

---

[SA-001]: ./stakeholder-analysis.md
[e1a3d8d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/e1a3d8d304d4b6ece1a3f95ee02b597e30a97520
[PP-001]: ./project-plan.md
[MIL-004]: ./milestones/mil-004-framework-baseline.md
[90ad973]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/90ad973aec2f4c57daaa1ec1dbc194932214cce0
[087f57a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/087f57a2ec5fc058e25a1f37bc26a6d664e437dc
