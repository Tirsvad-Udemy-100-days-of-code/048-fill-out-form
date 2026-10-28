from pathlib import Path

from fill_out_form import constants
from fill_out_form.application.run_lecture import run_lecture
from fill_out_form.domain.form_data import FormData
from tests.unit.fakes import FakeBrowser


def test_run_lecture_visits_pages_in_order() -> None:
    browser = FakeBrowser()

    run_lecture(browser, form_url="https://form.test/", pause=lambda _: None)

    urls = [e[1] for e in browser.events if e[0] == "get"]
    assert urls == [
        constants.WIKIPEDIA_URL,
        constants.WIKIPEDIA_URL,
        "https://form.test/",
    ]


def test_run_lecture_pauses_after_each_step() -> None:
    browser = FakeBrowser()
    pauses: list[float] = []

    run_lecture(browser, pause=pauses.append)

    assert pauses == [constants.PAUSE_SECONDS] * 3


def test_run_lecture_saves_screenshots_in_step_order(tmp_path: Path) -> None:
    browser = FakeBrowser()
    target = tmp_path / "nested" / "results"

    run_lecture(browser, screenshot_dir=target, pause=lambda _: None)

    assert target.is_dir()
    assert browser.screenshots == [
        str(target / name)
        for name in (
            constants.SCREENSHOT_STEP_1,
            constants.SCREENSHOT_STEP_2,
            constants.SCREENSHOT_STEP_3_FILLED,
            constants.SCREENSHOT_STEP_3_SIGNED_UP,
        )
    ]


def test_run_lecture_filled_screenshot_is_taken_before_sign_up_click(
    tmp_path: Path,
) -> None:
    browser = FakeBrowser()

    run_lecture(browser, screenshot_dir=tmp_path, pause=lambda _: None)

    names = [e[0] for e in browser.events]
    filled = browser.events.index(
        ("save_screenshot", str(tmp_path / constants.SCREENSHOT_STEP_3_FILLED))
    )
    click = names.index("click", filled)
    assert names[filled] == "save_screenshot"
    assert browser.events[click][1] == (
        constants.BY_CSS_SELECTOR,
        constants.SIGN_UP_BUTTON_SELECTOR,
    )


def test_run_lecture_types_given_form_data() -> None:
    browser = FakeBrowser()

    run_lecture(
        browser,
        pause=lambda _: None,
        form_data=FormData("Ada", "Lovelace", "ada@example.test"),
    )

    typed = [e[2][0] for e in browser.events if e[0] == "send_keys"][-3:]
    assert typed == ["Ada", "Lovelace", "ada@example.test"]


def test_run_lecture_without_directory_takes_no_screenshots() -> None:
    browser = FakeBrowser()

    run_lecture(browser, pause=lambda _: None)

    assert browser.screenshots == []
