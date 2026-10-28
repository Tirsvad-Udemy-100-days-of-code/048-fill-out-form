from html.parser import HTMLParser
from pathlib import Path

from fill_out_form import constants

FIXTURE = Path(__file__).parent.parent / "fixtures" / "signup_form.html"


class _Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.inputs: list[dict[str, str | None]] = []
        self.in_form = False
        self.button_in_form = False
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "form":
            self.in_form = True
        elif tag == "input":
            self.inputs.append(dict(attrs))
        elif tag == "button" and self.in_form:
            self.button_in_form = True
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def _parse() -> _Collector:
    collector = _Collector()
    collector.feed(FIXTURE.read_text(encoding="utf-8"))
    return collector


def _name_from_selector(selector: str) -> str:
    return selector.split("='")[1].rstrip("']")


def test_fixture_inputs_match_constants_selectors() -> None:
    names = {i.get("name") for i in _parse().inputs}

    for selector in (
        constants.FIRST_NAME_SELECTOR,
        constants.LAST_NAME_SELECTOR,
        constants.EMAIL_SELECTOR,
    ):
        assert _name_from_selector(selector) in names


def test_fixture_has_button_inside_form() -> None:
    assert constants.SIGN_UP_BUTTON_SELECTOR == "form button"
    assert _parse().button_in_form


def test_fixture_title() -> None:
    assert _parse().title == "App Brewery Newsletter"
