import os

from dotenv import load_dotenv
from rich.console import Console

from .logging_settings import setup_logging

console = Console(color_system="truecolor", force_terminal=True)

load_dotenv()
log = setup_logging("cpfl")


TINY_TOKEN = os.getenv("TINY_TOKEN", "")
SEND_NUMBERS = os.getenv("SEND_NUMBERS", [])

EVO_API_KEY = os.getenv("EVO_API_KEY", "")
EVO_URL = os.getenv("EVO_URL", "")
INSTANCE = os.getenv("INSTANCE", "")
