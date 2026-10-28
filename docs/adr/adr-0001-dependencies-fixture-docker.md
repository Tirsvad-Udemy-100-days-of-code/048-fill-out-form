# ADR-0001 Dependencies, form page and browser environment

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e1a3d8d] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The project drives a browser with Selenium (the lecture's subject). S03 wants no runtime dependencies beyond the necessary (CN-006). The lecture's form challenge uses a public demo page that is online today but is not under our control. The framework forbids testing a GUI on the host desktop (`framework/process/gui-testing.md`). Options considered: (a) add helper libraries such as `python-dotenv` or `webdriver-manager`; (b) run only against the live demo page; (c) a local HTML fixture for unit tests plus a Docker browser run for screenshots.

## Decision

Selenium is the only runtime dependency (pytest, ruff and mypy are `dev` extras). Unit tests use a fake browser and a local HTML fixture, never the network; the live pages are used only by the Docker browser run that produces the screenshots. Any browser run happens in a Docker container, never on the host desktop. The `.env` file is never read by the project.

## Consequences

**Positive:**

- The installation is one dependency; Selenium Manager finds the driver, so no driver helper is needed.
- Unit tests are fast, offline and independent of a third-party site.
- The user's desktop is never taken over by a browser.

**Negative:**

- Screenshots need Docker.
- The fixture can drift from the live demo page; the Docker run is the check.

## Affected Artifacts

- [BC-001] — realises success criterion 4 (one runtime dependency) and the risk about the demo page

---

[BC-001]: ../business-case.md
[e1a3d8d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/e1a3d8d304d4b6ece1a3f95ee02b597e30a97520
