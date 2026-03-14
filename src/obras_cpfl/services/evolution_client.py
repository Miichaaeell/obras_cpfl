from requests import post
from obras_cpfl.settings import EVO_API_KEY, EVO_URL, INSTANCE


class EvolutinClient:
    def __init__(self):
        self.__api_key = EVO_API_KEY
        self.__base_url = EVO_URL
        self.__instance = INSTANCE
        self.__headers = {"Content-Type": "application/json", "apikey": self.__api_key}

    def notification(self, number: str, msg: str):
        payload = {"number": f"{number}", "text": msg, "delay": 5}
        res = post(
            url=f"{self.__base_url}message/sendText/{self.__instance}",
            headers=self.__headers,
            json=payload,
            timeout=10,
        )
        return res
