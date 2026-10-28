# SQA Review Record: wiki and README (MIL-003)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9565ebe] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: none exists for a wiki; the rules of `framework/process/wiki.md` and the Go/No-Go criteria of [MIL-003] are used
- Scope: full review of `docs/wiki/` and `README.md`
- Language and domain: en, da and ms wiki; `n/a` (a wiki is not an artifact with Language and Domain rows)
- Language reviewer: none; the reviewer is not a native speaker of Danish or Bahasa Malaysia, so the translations are not independently verified (see Action Items)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | English is the authoritative text and each translation follows it page by page | Pass | The da and ms pages have the same sections in the same order as the English page. |
| 2 | Every English page exists in the PO language and in the added languages, with the same page set | Pass | Home, Step-1-Link-Click, Step-2-Search and Step-3-Form exist as `.md`, `-da.md` and `-ms.md`; the PO language is English, so da and ms are additions (checked with ls). |
| 3 | Each page starts with the language line, and `_Sidebar.md` lists every language | Pass | All 12 pages start with the language line linking the other two languages; `_Sidebar.md` lists English, Dansk and Bahasa Malaysia. |
| 4 | Code blocks, commands, file names and IDs stay in English | Pass | Code, commands and `constants.py` names are unchanged in all languages. |
| 5 | The PO language is the one in the registry; the wiki does not decide it | Pass | Registry PO language is en; no wiki page changes it. |
| 6 | Each page explains what was gained in its lecture step and shows the screenshot (MIL-003 criteria 3 and 4) | Pass | Each step page has the sections lecture, code, what the browser shows (image) and what we gained, in three languages. |
| 7 | The README shows one screenshot per lecture step and `check-readme.sh` passes (MIL-003 criterion 1) | Pass | README has a screenshots table with four images (step 3 twice); `check-readme.sh` reports only a finding about the framework README, not the project README. |
| 8 | Internal links resolve | Pass | A script checked every page link against the files; none are broken. Image URLs point to the raw files of `main` and work once this branch is merged. |

## Overall Verdict

Go — all criteria pass. The translations follow the English text but a native speaker has not read them.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the Danish and Bahasa Malaysia pages and correct wording | S01 | 2026-11-04 |

---

[MIL-003]: ../../milestones/mil-003-documentation.md
[9565ebe]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/commit/9565ebe66d995894437376af631ad3ebc5cc7a15
