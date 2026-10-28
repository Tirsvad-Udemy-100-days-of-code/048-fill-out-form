import os
from pathlib import Path

import pytest

from fill_out_form import constants
from fill_out_form.application.run_lecture import run_lecture
from fill_out_form.infrastructure.driver import create_driver


@pytest.mark.e2e
def test_lecture_runs_against_real_sites() -> None:
    results = Path(os.environ.get("RESULTS_DIR", "results"))
    browser = create_driver(headless=True)
    try:
        run_lecture(browser, screenshot_dir=results)
    finally:
        browser.quit()

    for name in (
        constants.SCREENSHOT_STEP_1,
        constants.SCREENSHOT_STEP_2,
        constants.SCREENSHOT_STEP_3_FILLED,
        constants.SCREENSHOT_STEP_3_SIGNED_UP,
    ):
        assert (results / name).is_file()
