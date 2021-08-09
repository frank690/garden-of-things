"""This module contains tests for logging.py"""

from logging import Logger

import pytest

from garden.auxiliary.logging import get_logger


@pytest.mark.parametrize(
    "name",
    [
        "some_logger_name",
    ],
)
def test_parse_timedelta_to_str(name):
    logger_instance = get_logger(name=name)
    assert isinstance(logger_instance, Logger)
