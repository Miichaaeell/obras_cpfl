import os
from logging import Logger

from dotenv import load_dotenv

load_dotenv()

log = Logger(__name__, level=os.getenv("LEVEL_LOG", "INFO"))

TEXTMEBOT_TOKEN = os.getenv("TEXTMEBOT_TOKEN")
TINY_TOKEN = os.getenv("TINY_TOKEN")
SEND_NUMBERS = os.getenv("SEND_NUMBERS")
