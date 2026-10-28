# 🚀 048-fill-out-form

Udemy "100 Days of Code: The Complete Python Pro Bootcamp", Day 48: automate a browser with Selenium — click a link by its text, type into a search box, send the Enter key and fill out a sign-up form. For course participants who want to compare solutions and for anyone who wants a small, tested Selenium example.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The code automates the three steps of the lecture:

1. `click_link_by_text` — click the "Content portals" link on the Wikipedia main page.
2. `search_for` — type "Python" into the search box and press Enter.
3. `fill_out_form` — type a first name, last name and email into the sign-up form and click the button.

| Part | What it is for |
| --- | --- |
| `src/fill_out_form/` | The package: `constants.py` holds every URL, locator and text; the layers `domain`, `application`, `infrastructure` and `presentation` hold the code |
| `tests/` | pytest tests (`unit/`), the browser run (`e2e/`) and a local copy of the form (`fixtures/`) |
| `docs/` | Project documents, screenshots and the wiki in English, Danish and Bahasa Malaysia |
| `Doxyfile` | Configuration for the Doxygen API documentation |

### Screenshots of the lecture steps

Taken in a Docker container with headless Chromium.

| Step | Screenshot |
| --- | --- |
| 1. Click the link "Content portals" | ![Step 1][img-step-1] |
| 2. Search for "Python" and press Enter | ![Step 2][img-step-2] |
| 3. Fill out the form, before Sign Up | ![Step 3, filled][img-step-3-filled] |
| 3. After Sign Up (the demo page rejects the default example.com address; pass your own with `--email`) | ![Step 3, signed up][img-step-3-signed-up] |

What each step teaches is explained in the wiki: [English][wiki-en], [Dansk][wiki-da], [Bahasa Malaysia][wiki-ms].

## 📋 Requirements

- Python 3.13 or newer, with `venv` — the language and the isolated environment.
- Google Chrome or Chromium — the browser that Selenium drives (Selenium 4 finds the driver itself).
- Docker — only to run the browser in a container and take the screenshots.
- Doxygen — only to build the API documentation (optional).

The only runtime dependency is `selenium`; `pytest`, `ruff` and `mypy` are development extras.

## 🛠️ Setup

Create and use a local virtual environment in `.venv`:

```bash
python -m venv .venv
```

Activate it (Linux, macOS, Git Bash):

```bash
source .venv/bin/activate
```

Activate it (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Upgrade pip and install the project with the development extras:

```bash
python -m pip install --upgrade pip
```

```bash
python -m pip install -e ".[dev]"
```

## ▶️ Run

Run the three lecture steps in a visible Chrome window:

```bash
python -m fill_out_form
```

Useful options: `--headless` (no window), `--screenshots DIR` (save one picture per step), `--form-url URL` (use another form page) and `--first-name`, `--last-name`, `--email` (the values typed into the form; the demo page rejects the default `example.com` address, so use your own to see the success page). See `python -m fill_out_form --help`.

Run the steps in Docker (headless, screenshots in `results/`), which never touches your desktop:

```bash
docker build -t fill-out-form -f docker/Dockerfile .
```

```bash
docker run --rm -v "$(pwd)/results:/results" fill-out-form
```

## 🧪 Tests

The unit tests need no browser and no network:

```bash
python -m pytest
```

Build the API documentation with Doxygen (output in `docs/doxygen/`):

```bash
doxygen Doxyfile
```

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Wiki pages (docs/wiki)][wiki-dir] | The lecture steps explained, in three languages |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/wiki
[wiki-en]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/wiki/Home
[wiki-da]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/wiki/Home-da
[wiki-ms]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/wiki/Home-ms
[img-step-1]: ./docs/images/step-1-click-link.png
[img-step-2]: ./docs/images/step-2-search.png
[img-step-3-filled]: ./docs/images/step-3-form-filled.png
[img-step-3-signed-up]: ./docs/images/step-3-form-signed-up.png
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-fill-out-form/issues
[license]: ./LICENSE
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[wiki-dir]: ./docs/wiki/
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
