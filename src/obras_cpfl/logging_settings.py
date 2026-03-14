import logging.config
from typing import Any


LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(message)s",
            "datefmt": "%d-%m-%Y %H:%M",
        },
    },
    "handlers": {
        "rich": {
            "()": "rich.logging.RichHandler",
            "formatter": "default",
            "level": "INFO",
            "rich_tracebacks": True,
        },
    },
    "root": {"handlers": ["rich"], "level": "INFO"},
    "loggers": {
        "cpfl": {
            "level": "INFO",
        }
    },
}


def setup_logging(logger_name: str) -> logging.Logger:
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger(logger_name)
