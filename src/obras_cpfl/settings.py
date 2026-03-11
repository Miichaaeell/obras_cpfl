import os
import logging

from rich.console import Console
from rich.logging import RichHandler

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(
    level=os.getenv("LEVEL_LOG", "DEBUG"),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)
log = logging.getLogger("rich")

console = Console(color_system="truecolor", force_terminal=True)


TEXTMEBOT_TOKEN = os.getenv("TEXTMEBOT_TOKEN")
TINY_TOKEN = os.getenv("TINY_TOKEN")
SEND_NUMBERS = os.getenv("SEND_NUMBERS")
