# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e1a3d8d] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | [RC-003] |
| [MIL-001] | MIL | en | it | [PP-001] | [MIL-002], [ADR-0001] | [RC-004], [RC-008] (code) |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-010], [RC-009] (code) |
| [MIL-003] | MIL | en | it | [MIL-002] | - | [RC-006] |
| [ADR-0001] | ADR | - | - | [BC-001], [MIL-001] | - | [RC-007] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [PP-001], [MIL-001], [MIL-002], [MIL-003] | - | - | Covered |
| CN-002 | [MIL-002] | - | - | Covered |
| CN-003 | [MIL-001], [MIL-002] | - | - | Covered |
| CN-004 | [MIL-001], [MIL-003] | - | - | Covered |
| CN-005 | [MIL-001] | - | - | Covered |
| CN-006 | [MIL-001] | [ADR-0001] | - | Covered |
| CN-007 | [MIL-002], [MIL-003] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |

## Coverage Notes

- No instance exists yet of the other artifact types (KPI, BMC, BPMN, UCD, US, UC, design artifacts, TP, GOV, DICT); the tasks of all milestones are plain technical tasks.
- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-form-automation.md
[MIL-003]: ../milestones/mil-003-documentation.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-project-setup.md
[RC-005]: ./reviews/rc-005-mil-002-form-automation.md
[RC-006]: ./reviews/rc-006-mil-003-documentation.md
[ADR-0001]: ../adr/adr-0001-dependencies-fixture-docker.md
[RC-007]: ./reviews/rc-007-adr-0001.md
[RC-008]: ./reviews/rc-008-code-mil-001.md
[e1a3d8d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/e1a3d8d304d4b6ece1a3f95ee02b597e30a97520
[RC-009]: ./reviews/rc-009-code-mil-002.md
[RC-010]: ./reviews/rc-010-mil-002-form-automation.md
