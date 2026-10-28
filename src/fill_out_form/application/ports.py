"""Ports the use cases need from a browser.

@file ports.py
@brief Narrow structural interfaces for a web element and a browser.
"""

from typing import Protocol


class ElementPort(Protocol):
    """Describe the web element operations the steps use.

    @brief A clickable, typeable element.
    """

    def click(self) -> None:
        """Click the element.

        @brief Click the element.
        """
        ...

    def send_keys(self, *value: str) -> None:
        """Type text or keys into the element.

        @brief Type the given values into the element.
        @param value The text or special keys to type.
        """
        ...


class BrowserPort(Protocol):
    """Describe the browser operations the steps use.

    @brief A browser that opens pages, finds elements and takes screenshots.
    """

    def get(self, url: str) -> None:
        """Open a page.

        @brief Navigate to the url.
        @param url The address to open.
        """
        ...

    def find_element(self, by: str, value: str) -> ElementPort:
        """Find one element.

        @brief Find the first element matching the locator.
        @param by The locator strategy.
        @param value The locator value.
        @return The element found.
        """
        ...

    def save_screenshot(self, filename: str) -> bool:
        """Save a screenshot of the page.

        @brief Write a PNG screenshot to a file.
        @param filename The path of the PNG file.
        @return True when the file was written.
        """
        ...

    def quit(self) -> None:
        """Close the browser.

        @brief Quit the browser and end the session.
        """
        ...
