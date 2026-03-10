from requests import post

from obras_cpfl.settings import TEXTMEBOT_TOKEN


class TextMeBot:
    def __init__(self):
        self.__api_key = TEXTMEBOT_TOKEN
        self.__base_url = (
            "http://api.textmebot.com/send.php?recipient=+{number}&"
            "apikey={api_key}&text={msg}"
        )

    def notification(self, number: str, msg: str):
        res = post(
            self.__base_url.format(number=number, api_key=self.__api_key, msg=msg)
        )

        return res.json()
