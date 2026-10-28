"""The whole lecture as one use case.

@file run_lecture.py
@brief Run the three lecture steps in order, with optional screenshots.
"""

import logging
import time
from collections.abc import Callable
from pathlib import Path

from fill_out_form.application.ports import BrowserPort
from fill_out_form.application.steps import (
    click_link_by_text,
    fill_out_form,
    search_for,
)
from fill_out_form.constants import (
    FORM_URL,
    PAUSE_SECONDS,
    SCREENSHOT_STEP_1,
    SCREENSHOT_STEP_2,
    SCREENSHOT_STEP_3_FILLED,
    SCREENSHOT_STEP_3_SIGNED_UP,
    WIKIPEDIA_URL,
)
from fill_out_form.domain.form_data import FormData

logger = logging.getLogger(__name__)


def _screenshot(browser: BrowserPort, screenshot_dir: Path | None, name: str) -> None:
    """Save a screenshot when a directory is given."""
    if screenshot_dir is None:
        return
    path = screenshot_dir / name
    logger.info("Saving screenshot %s", path)
    if not browser.save_screenshot(str(path)):
        logger.warning("Screenshot %s was not written", path)


def run_lecture(
    browser: BrowserPort,
    form_url: str = FORM_URL,
    screenshot_dir: Path | None = None,
    pause: Callable[[float], None] = time.sleep,
    form_data: FormData | None = None,
) -> None:
    """Run the three lecture steps in order.

    @brief Click a link, search, then fill out the form, with screenshots.
    @param browser The browser to drive.
    @param form_url The address of the sign-up form.
    @param screenshot_dir Directory for one screenshot per step; none when omitted.
    @param pause Called with the seconds to wait so a viewer can see the result.
    @param form_data The values to type into the form; the defaults when omitted.
    """
    if screenshot_dir is not None:
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Step 1: click a link by its text")
    browser.get(WIKIPEDIA_URL)
    click_link_by_text(browser)
    pause(PAUSE_SECONDS)
    _screenshot(browser, screenshot_dir, SCREENSHOT_STEP_1)

    logger.info("Step 2: search")
    browser.get(WIKIPEDIA_URL)
    search_for(browser)
    pause(PAUSE_SECONDS)
    _screenshot(browser, screenshot_dir, SCREENSHOT_STEP_2)

    logger.info("Step 3: fill out the form")
    browser.get(form_url)
    fill_out_form(
        browser,
        form_data,
        before_submit=lambda: _screenshot(
            browser, screenshot_dir, SCREENSHOT_STEP_3_FILLED
        ),
    )
    pause(PAUSE_SECONDS)
    _screenshot(browser, screenshot_dir, SCREENSHOT_STEP_3_SIGNED_UP)
