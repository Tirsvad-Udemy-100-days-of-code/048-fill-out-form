from typing import Any


class FakeElement:
    """Records the interactions with one element in a shared event list."""

    def __init__(self, events: list[tuple[Any, ...]], locator: tuple[str, str]) -> None:
        self._events = events
        self.locator = locator

    def click(self) -> None:
        self._events.append(("click", self.locator))

    def send_keys(self, *value: str) -> None:
        self._events.append(("send_keys", self.locator, value))


class FakeBrowser:
    """Records every call in order, without any browser."""

    def __init__(self) -> None:
        self.events: list[tuple[Any, ...]] = []
        self.screenshots: list[str] = []

    def get(self, url: str) -> None:
        self.events.append(("get", url))

    def find_element(self, by: str, value: str) -> FakeElement:
        self.events.append(("find_element", by, value))
        return FakeElement(self.events, (by, value))

    def save_screenshot(self, filename: str) -> bool:
        self.screenshots.append(filename)
        self.events.append(("save_screenshot", filename))
        return True

    def quit(self) -> None:
        self.events.append(("quit",))
