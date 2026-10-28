**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Day 48: Fill out a form with Selenium

This project solves the Day 48 lecture of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". The lecture shows how Selenium WebDriver interacts with a page: clicking elements, typing into inputs, sending special keys and filling out a form.

## What each lecture step gives you

| Step | Lecture topic | Function | What you gain |
| --- | --- | --- | --- |
| 1 | Click a link, find it by its text | `click_link_by_text` | Navigate without the mouse |
| 2 | Type into an input and send the Enter key | `search_for` | Fill an input and submit with a special key |
| 3 | Challenge: fill out a form and click the button | `fill_out_form` | Combine selectors, typing and clicking |

- [Step 1: Click a link](Step-1-Link-Click)
- [Step 2: Search](Step-2-Search)
- [Step 3: The form](Step-3-Form)

## Run it

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m fill_out_form
```

The README of the repository has the full instructions, the tests and the Docker run that never touches your desktop.
