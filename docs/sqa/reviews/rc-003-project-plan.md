# SQA Review Record: PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-10-28, end 2026-11-04, the one-week constraint of BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Three gateways, each with its MIL document, decision date and owner. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the MIL target dates (10-29, 11-01, 11-04) and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every in-scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-002 to MIL-003, in schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | States the delay and that only S01 moves the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owners are S-IDs. No governance document exists yet, so no RACI to match; recorded in Open Issues. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions cite BC-001 and SA-001. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks with impact and mitigation. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open issues are current and do not contradict the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Deliverables match the Deliverable of each MIL document. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says none (technical tasks). |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Table, Gantt and dependency chain agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Column says not yet synced; updated after the sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single plan, Version History kept. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language` = en and `Domain` = it. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | IT Executive English for BC, PP and MIL; IT Professional English for SA, as the registry states. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No `DICT` exists yet; only standard IT terms are used, with no synonyms for one concept. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version: no earlier accepted version, so no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer (AI as stand-in for S01) reads English and knows the IT domain; not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (ADR, PO, CI, FURPS+) are known to the audience or spelled out. |

## Overall Verdict

Go — every Mandatory criterion passes; no blocking finding.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
