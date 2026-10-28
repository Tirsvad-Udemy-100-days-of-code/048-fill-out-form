from fill_out_form import constants
from fill_out_form.application.ports import BrowserPort
from fill_out_form.application.steps import (
    click_link_by_text,
    fill_out_form,
    search_for,
)
from fill_out_form.domain.form_data import FormData
from tests.unit.fakes import FakeBrowser


def test_click_link_by_text_clicks_default_link() -> None:
    browser = FakeBrowser()

    click_link_by_text(browser)

    link = (constants.BY_LINK_TEXT, constants.LINK_TEXT_CONTENT_PORTALS)
    assert browser.events == [("find_element", *link), ("click", link)]


def test_click_link_by_text_uses_given_text() -> None:
    browser = FakeBrowser()

    click_link_by_text(browser, "Other")

    assert browser.events[0] == ("find_element", constants.BY_LINK_TEXT, "Other")


def test_search_for_types_term_then_enter() -> None:
    browser = FakeBrowser()

    search_for(browser, "Selenium")

    locator = (constants.BY_NAME, constants.SEARCH_INPUT_NAME)
    assert browser.events == [
        ("find_element", *locator),
        ("send_keys", locator, ("Selenium",)),
        ("send_keys", locator, (constants.KEY_ENTER,)),
    ]


def test_search_for_uses_default_term() -> None:
    browser = FakeBrowser()

    search_for(browser)

    assert (
        "send_keys",
        (constants.BY_NAME, constants.SEARCH_INPUT_NAME),
        (constants.SEARCH_TERM,),
    ) in browser.events


def test_fill_out_form_types_fields_then_clicks_in_order() -> None:
    browser = FakeBrowser()
    data = FormData("Ada", "Lovelace", "ada@example.com")

    fill_out_form(browser, data)

    css = constants.BY_CSS_SELECTOR
    actions = [e for e in browser.events if e[0] in ("send_keys", "click")]
    assert actions == [
        ("send_keys", (css, constants.FIRST_NAME_SELECTOR), ("Ada",)),
        ("send_keys", (css, constants.LAST_NAME_SELECTOR), ("Lovelace",)),
        ("send_keys", (css, constants.EMAIL_SELECTOR), ("ada@example.com",)),
        ("click", (css, constants.SIGN_UP_BUTTON_SELECTOR)),
    ]


def test_fill_out_form_uses_default_data() -> None:
    browser = FakeBrowser()

    fill_out_form(browser)

    typed = [e[2][0] for e in browser.events if e[0] == "send_keys"]
    assert typed == [
        constants.DEFAULT_FIRST_NAME,
        constants.DEFAULT_LAST_NAME,
        constants.DEFAULT_EMAIL,
    ]


def test_fill_out_form_calls_before_submit_before_click() -> None:
    browser = FakeBrowser()

    fill_out_form(browser, before_submit=lambda: browser.events.append(("hook",)))

    names = [e[0] for e in browser.events if e[0] in ("send_keys", "hook", "click")]
    assert names == ["send_keys"] * 3 + ["hook", "click"]


def test_fake_browser_satisfies_browser_port() -> None:
    browser: BrowserPort = FakeBrowser()

    assert browser is not None
