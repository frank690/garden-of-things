"""
This module holds the logging configuration
"""

__all__ = [
    "get_logger",
]

import logging
from logging.handlers import TimedRotatingFileHandler

from garden.config.common import LOG_PATH


def get_logger(name: str) -> logging.Logger:
    """
    Deliver a custom logger to whoever calls this functions with a desired logger name.
    :param name: Name of logger that should be created.
    :return: Logger
    """
    logger = logging.getLogger(name=name)
    LOG_PATH.joinpath(f"{name}").mkdir(exist_ok=True)

    handler = TimedRotatingFileHandler(
        filename=LOG_PATH.joinpath(f"{name}/{name}.log").resolve(),
        when="W0",
        interval=1,
        backupCount=26,
    )

    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(log_format)

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
