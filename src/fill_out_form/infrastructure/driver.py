"""Chrome driver factory.

@file driver.py
@brief Build a Selenium Chrome driver, headless when requested.
"""

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from fill_out_form.constants import CHROME_BINARY_ENV, HEADLESS_ARGUMENTS, WINDOW_SIZE


def create_driver(headless: bool = False) -> WebDriver:
    """Create a Chrome driver.

    @brief Build a Chrome WebDriver from the options the lecture needs.
    @param headless Run without a window, for a container without a desktop.
    @return The Chrome WebDriver.
    """
    options = Options()
    if headless:
        for argument in HEADLESS_ARGUMENTS:
            options.add_argument(argument)
        options.add_argument(f"--window-size={WINDOW_SIZE}")
    else:
        options.add_experimental_option("detach", False)
    binary = os.environ.get(CHROME_BINARY_ENV)
    if binary:
        options.binary_location = binary
    return webdriver.Chrome(options=options)
