import dataclasses

import pytest

from fill_out_form import constants
from fill_out_form.domain.form_data import FormData, default_form_data


def test_default_form_data_uses_constants() -> None:
    data = default_form_data()

    assert data.first_name == constants.DEFAULT_FIRST_NAME
    assert data.last_name == constants.DEFAULT_LAST_NAME
    assert data.email == constants.DEFAULT_EMAIL


def test_form_data_is_immutable() -> None:
    data = FormData("A", "B", "a@b.c")

    with pytest.raises(dataclasses.FrozenInstanceError):
        data.email = "x"  # type: ignore[misc]
