# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e1a3d8d] |

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

## Scope

### In Scope

- Python 3.13 or newer package under `src/`, tests under `tests/`, documents under `docs/`.
- Constants in `constants.py`; Doxygen comments in the source and a `Doxyfile`.
- `pyproject.toml`, venv instructions (`python -m pip install --upgrade pip`), Python `.gitignore`.
- README from the framework template, with run and test instructions and screenshots.
- Wiki pages in English, Danish and Bahasa Malaysia (`docs/wiki/`), with the same screenshots.
- Repository description and topics on the git host.

### Out of Scope

- Running the browser automation on the host desktop (it runs in Docker, see `framework/process/gui-testing.md`).
- Later days of the course and the final project.
- Packaging for PyPI, a graphical front end, and a web service.
- Reading, testing or importing the personal tokens in `.env`.

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

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The assignment's form page (a Heroku demo) is offline | The form step cannot be shown against the original site | A local HTML fixture with the same field names serves tests and screenshots; the original URL is a constant |
| Docker or the browser image is unavailable | No screenshots | Stop and report (gui-testing rule 5); never fall back to the host desktop |
| Wikipedia changes its page layout | Selectors break | Selectors live in `constants.py`; screenshots record the state on the capture date |
| Danish or Bahasa Malaysia text contains errors | Misleading text | English is authoritative; translations follow page by page; the author can correct them |
| Tokens in `.env` leak | Account compromise | `.env` is in `.gitignore` and is never read by project code or tests |

## Assumptions

- S01 is Product Owner, developer and reviewer; in autonomous mode the AI stands in for the reviewer, recorded as not independent.
- Docker is installed on the author's machine.
- The git host accepts the token in `.env` for repository and issue operations.
- "Python greater than 3.13" is read as 3.13 or newer (`requires-python = ">=3.13"`).

## Constraints

- Duration: one week, 2026-10-28 to 2026-11-04.
- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Only runtime dependency: selenium.
- Product Owner domain: IT; language: English.

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
