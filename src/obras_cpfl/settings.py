import os
import logging

from rich.console import Console

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(
    level=os.getenv("LEVEL_LOG", "INFO"),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
log = logging.getLogger(__name__)

console = Console(color_system="truecolor", force_terminal=True)


TEXTMEBOT_TOKEN = os.getenv("TEXTMEBOT_TOKEN")
TINY_TOKEN = os.getenv("TINY_TOKEN")
SEND_NUMBERS = os.getenv("SEND_NUMBERS")
