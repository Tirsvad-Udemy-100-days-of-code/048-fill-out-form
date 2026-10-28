# SQA Review Record: SA-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [e1a3d8d] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | S01, S02, S03 all have power, interest and quadrant. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | Stable IDs S01-S03. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Role, organisation, power and interest in the summary table. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Communication table C-01 to C-03 maps to milestones. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Two conflicts, each with a mitigation. |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | Traceability table cites BC-001 objectives. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Concern register maps each concern to a FURPS+ attribute. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Short entries in plain language. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | CN-001 to CN-007, each with the stakeholder who raised it. |

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

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[e1a3d8d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/e1a3d8d304d4b6ece1a3f95ee02b597e30a97520
