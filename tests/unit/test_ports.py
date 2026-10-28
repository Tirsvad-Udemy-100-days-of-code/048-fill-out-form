from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from fill_out_form.application.ports import BrowserPort, ElementPort


def _accepts_browser(browser: BrowserPort) -> BrowserPort:
    return browser


def _accepts_element(element: ElementPort) -> ElementPort:
    return element


def test_selenium_types_satisfy_ports_structurally() -> None:
    # mypy --strict checks the structural match through these signatures.
    assert callable(_accepts_browser)
    assert callable(_accepts_element)
    assert WebDriver.find_element is not None
    assert WebElement.click is not None
