"""Values typed into the sign-up form.

@file form_data.py
@brief The form values as an immutable value object, and their defaults.
"""

from dataclasses import dataclass

from fill_out_form.constants import (
    DEFAULT_EMAIL,
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
)


@dataclass(frozen=True, slots=True)
class FormData:
    """Hold the three values the sign-up form asks for.

    @brief Immutable first name, last name and email of the sign-up form.
    @param first_name The first name to type.
    @param last_name The last name to type.
    @param email The email address to type.
    """

    first_name: str
    last_name: str
    email: str


def default_form_data() -> FormData:
    """Return the form values defined in the constants.

    @brief Build a FormData from the DEFAULT_* constants.
    @return The default form data.
    """
    return FormData(
        first_name=DEFAULT_FIRST_NAME,
        last_name=DEFAULT_LAST_NAME,
        email=DEFAULT_EMAIL,
    )
