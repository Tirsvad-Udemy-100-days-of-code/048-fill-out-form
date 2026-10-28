# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This analysis names the people who care about the project, so that owners, reviewers and concerns can be cited by ID. It uses the power/interest grid and maps each concern to a FURPS+ attribute. It supports [BC-001].

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Private | HIGH | HIGH | Manage Closely | A tidy, correct and well documented solution for the course portfolio |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Monitor | A clear repository description, topics and README, and no unnecessary runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact.
- **Keep Informed (S02):** cannot change the project, but whether they can run the code decides whether it is useful. They get the README and the wiki.
- **Monitor (S03):** casual visitors, served by the repository metadata and the README.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every change is planned, reviewed and traceable by pull request | Supportability |
| CN-002 | S01 | The code is correct for all three lecture steps and tested | Functionality |
| CN-003 | S02 | The code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | The README tells how to create the venv, run the code and run the tests | Usability |
| CN-005 | S03 | The repository has a description, topics and a clear README | Usability |
| CN-006 | S03 | No runtime dependency except the one that is necessary | Supportability |
| CN-007 | S01 | Each lecture step has a screenshot and a wiki text in three languages | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| C-01 | Chat with S01 | At plan acceptance and at the end of the run | Plan; run summary | All |
| C-02 | Pull request | One per milestone | Changes and review records | MIL-001, MIL-002, MIL-003 |
| C-03 | README and wiki | At each milestone that changes them | Instructions, screenshots, explanations | MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's names; clean code conventions may prefer others | S01, S02 | Public functions keep the lecture's names; internals follow the conventions |
| S01 wants documentation in three languages; S03 wants brevity | S01, S03 | The README stays short and links to the wiki for detail |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 and 2 |
| S01 | CN-007 | [BC-001] objectives 3 and 4 |
| S02 | CN-003, CN-004 | [BC-001] objectives 1 and 3 |
| S03 | CN-005, CN-006 | [BC-001] objective 5 |

## Sign-Off

Pending review. In autonomous mode the AI stands in for S01 as reviewer; the review record says "not independent".

---

[BC-001]: ./business-case.md
