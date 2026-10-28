"""Command line entry point.

@file cli.py
@brief Parse the arguments, build the driver and run the lecture.
"""

import argparse
import logging
from collections.abc import Sequence
from pathlib import Path

from fill_out_form.application.run_lecture import run_lecture
from fill_out_form.constants import FORM_URL
from fill_out_form.domain.form_data import FormData, default_form_data
from fill_out_form.infrastructure.driver import create_driver


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser.

    @brief Define the command line options.
    @return The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="fill-out-form",
        description="Run the Day 48 Selenium lecture steps.",
    )
    parser.add_argument(
        "--headless", action="store_true", help="run Chrome without a window"
    )
    parser.add_argument(
        "--screenshots",
        type=Path,
        metavar="DIR",
        default=None,
        help="save one screenshot per step in DIR",
    )
    parser.add_argument(
        "--form-url", default=FORM_URL, help="address of the sign-up form"
    )
    defaults = default_form_data()
    parser.add_argument(
        "--first-name", default=defaults.first_name, help="first name to type"
    )
    parser.add_argument(
        "--last-name", default=defaults.last_name, help="last name to type"
    )
    parser.add_argument("--email", default=defaults.email, help="email to type")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the lecture from the command line.

    @brief Create the driver, run the lecture and always quit the browser.
    @param argv The arguments; the process arguments when omitted.
    @return The process exit code.
    """
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.INFO)
    browser = create_driver(headless=args.headless)
    try:
        run_lecture(
            browser,
            form_url=args.form_url,
            screenshot_dir=args.screenshots,
            form_data=FormData(args.first_name, args.last_name, args.email),
        )
    finally:
        browser.quit()
    return 0
