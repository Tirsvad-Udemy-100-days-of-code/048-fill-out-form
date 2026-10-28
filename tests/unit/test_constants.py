from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fill_out_form import constants


def test_locator_strategies_equal_selenium_by() -> None:
    assert constants.BY_LINK_TEXT == By.LINK_TEXT
    assert constants.BY_NAME == By.NAME
    assert constants.BY_CSS_SELECTOR == By.CSS_SELECTOR


def test_enter_key_equals_selenium_keys_enter() -> None:
    assert constants.KEY_ENTER == Keys.ENTER


def test_urls_use_https() -> None:
    assert constants.WIKIPEDIA_URL.startswith("https://")
    assert constants.FORM_URL.startswith("https://")
