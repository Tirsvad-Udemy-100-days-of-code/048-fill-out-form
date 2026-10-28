from pathlib import Path
from typing import Any

import pytest

from fill_out_form import constants
from fill_out_form.application.ports import BrowserPort
from fill_out_form.domain.form_data import FormData, default_form_data
from fill_out_form.presentation import cli
from tests.unit.fakes import FakeBrowser


def test_parser_defaults() -> None:
    args = cli.build_parser().parse_args([])

    assert args.headless is False
    assert args.screenshots is None
    assert args.form_url == constants.FORM_URL


def test_parser_reads_all_options() -> None:
    args = cli.build_parser().parse_args(
        ["--headless", "--screenshots", "out", "--form-url", "http://x/"]
    )

    assert args.headless is True
    assert args.screenshots == Path("out")
    assert args.form_url == "http://x/"


def test_main_runs_lecture_and_quits(monkeypatch: pytest.MonkeyPatch) -> None:
    browser = FakeBrowser()
    created: list[bool] = []
    calls: list[dict[str, Any]] = []

    def fake_create(headless: bool = False) -> FakeBrowser:
        created.append(headless)
        return browser

    def fake_run(b: BrowserPort, **kwargs: Any) -> None:
        calls.append({"browser": b, **kwargs})

    monkeypatch.setattr(cli, "create_driver", fake_create)
    monkeypatch.setattr(cli, "run_lecture", fake_run)

    code = cli.main(["--headless", "--screenshots", "shots"])

    assert code == 0
    assert created == [True]
    assert calls == [
        {
            "browser": browser,
            "form_url": constants.FORM_URL,
            "screenshot_dir": Path("shots"),
            "form_data": default_form_data(),
        }
    ]
    assert ("quit",) in browser.events


def test_parser_form_data_defaults_come_from_constants() -> None:
    args = cli.build_parser().parse_args([])

    assert FormData(args.first_name, args.last_name, args.email) == (
        default_form_data()
    )


def test_parser_reads_form_data_options() -> None:
    args = cli.build_parser().parse_args(
        ["--first-name", "Ada", "--last-name", "Lovelace", "--email", "a@example.test"]
    )

    assert (args.first_name, args.last_name, args.email) == (
        "Ada",
        "Lovelace",
        "a@example.test",
    )


def test_main_forwards_form_data_to_run_lecture(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    received: list[FormData | None] = []

    def fake_run(b: BrowserPort, **kwargs: Any) -> None:
        received.append(kwargs["form_data"])

    monkeypatch.setattr(cli, "create_driver", lambda headless=False: FakeBrowser())
    monkeypatch.setattr(cli, "run_lecture", fake_run)

    cli.main(["--first-name", "Ada", "--last-name", "L", "--email", "a@example.test"])

    assert received == [FormData("Ada", "L", "a@example.test")]


def test_main_quits_browser_when_lecture_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    browser = FakeBrowser()

    def failing_run(b: BrowserPort, **kwargs: Any) -> None:
        raise RuntimeError("boom")

    monkeypatch.setattr(cli, "create_driver", lambda headless=False: browser)
    monkeypatch.setattr(cli, "run_lecture", failing_run)

    with pytest.raises(RuntimeError, match="boom"):
        cli.main([])

    assert ("quit",) in browser.events
