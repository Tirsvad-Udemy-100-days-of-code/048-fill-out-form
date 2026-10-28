"""The three lecture steps.

@file steps.py
@brief Click a link by its text, search for a term, fill out the form.
"""

import logging
from collections.abc import Callable

from fill_out_form.application.ports import BrowserPort
from fill_out_form.constants import (
    BY_CSS_SELECTOR,
    BY_LINK_TEXT,
    BY_NAME,
    EMAIL_SELECTOR,
    FIRST_NAME_SELECTOR,
    KEY_ENTER,
    LAST_NAME_SELECTOR,
    LINK_TEXT_CONTENT_PORTALS,
    SEARCH_INPUT_NAME,
    SEARCH_TERM,
    SIGN_UP_BUTTON_SELECTOR,
)
from fill_out_form.domain.form_data import FormData, default_form_data

logger = logging.getLogger(__name__)


def click_link_by_text(
    browser: BrowserPort, link_text: str = LINK_TEXT_CONTENT_PORTALS
) -> None:
    """Click the link with the given text.

    @brief Find a link by its visible text and click it.
    @param browser The browser showing the page.
    @param link_text The visible text of the link.
    """
    logger.info("Clicking link %r", link_text)
    browser.find_element(BY_LINK_TEXT, link_text).click()


def search_for(browser: BrowserPort, term: str = SEARCH_TERM) -> None:
    """Type a term into the search input and press Enter.

    @brief Search the page for a term.
    @param browser The browser showing the page.
    @param term The text to search for.
    """
    logger.info("Searching for %r", term)
    search_input = browser.find_element(BY_NAME, SEARCH_INPUT_NAME)
    search_input.send_keys(term)
    search_input.send_keys(KEY_ENTER)


def fill_out_form(
    browser: BrowserPort,
    form_data: FormData | None = None,
    before_submit: Callable[[], None] | None = None,
) -> None:
    """Fill out the sign-up form and submit it.

    @brief Type the three values, run the hook, then click the sign-up button.
    @param browser The browser showing the form.
    @param form_data The values to type; the defaults when omitted.
    @param before_submit A hook called after typing and before the click.
    """
    data = form_data if form_data is not None else default_form_data()
    logger.info("Filling out the form for %s", data.email)
    browser.find_element(BY_CSS_SELECTOR, FIRST_NAME_SELECTOR).send_keys(
        data.first_name
    )
    browser.find_element(BY_CSS_SELECTOR, LAST_NAME_SELECTOR).send_keys(data.last_name)
    browser.find_element(BY_CSS_SELECTOR, EMAIL_SELECTOR).send_keys(data.email)
    if before_submit is not None:
        before_submit()
    browser.find_element(BY_CSS_SELECTOR, SIGN_UP_BUTTON_SELECTOR).click()
