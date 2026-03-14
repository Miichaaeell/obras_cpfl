import logging.config
from typing import Any
from rich.console import Console

console = Console(color_system="truecolor", force_terminal=True)


LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[cpfl]|%(message)s",
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
    "root": {"handlers": ["rich"]},
    "loggers": {
        "cpfl": {
            "level": "INFO",
        }
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
