import os
import logging

from dotenv import load_dotenv

from .logging_settings import console

load_dotenv()
console = console
log = logging.getLogger("cpfl")

TINY_TOKEN = os.getenv("TINY_TOKEN", "")
SEND_NUMBERS = os.getenv("SEND_NUMBERS", [])

EVO_API_KEY = os.getenv("EVO_API_KEY", "")
EVO_URL = os.getenv("EVO_URL", "")
INSTANCE = os.getenv("INSTANCE", "")
