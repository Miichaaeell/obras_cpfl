from requests import post

from obras_cpfl.settings import TEXTMEBOT_TOKEN


class TextMeBot:
    def __init__(self):
        self.__api_key = TEXTMEBOT_TOKEN
        self.__base_url = "http://api.textmebot.com/send.php"

    def notification(self, number: str, msg: str):
        res = post(
            self.__base_url,
            params={"recipient": f"+{number}", "apikey": self.__api_key, "text": msg},
            timeout=30,
        )

        return res.json()
