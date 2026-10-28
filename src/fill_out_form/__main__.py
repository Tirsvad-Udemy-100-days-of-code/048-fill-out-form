"""Module entry point.

@file __main__.py
@brief Run the lecture with `python -m fill_out_form`.
"""

import sys

from fill_out_form.presentation.cli import main

if __name__ == "__main__":
    sys.exit(main())
