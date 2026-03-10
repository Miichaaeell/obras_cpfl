from requests import post, get

from obras_cpfl.settings import log, TINY_TOKEN


class TinyUrl:
    def __init__(self):
        self.__url = "https://api.tinyurl.com/"
        self.__token = TINY_TOKEN
        self.__headers = {
            "Authorization": f"Bearer {self.__token}",
            "Content-Type": "application/json",
        }

    def create(self, url: str, tes_number: str) -> str | None:
        base_url = f"{self.__url}create"
        payload = {
            "url": url,
            "domain": "tinyurl.com",
            "alias": str(f"TES-{tes_number}"),
            "description": "string",
        }
        response = post(url=base_url, json=payload, headers=self.__headers)
        if response.status_code == 200:
            return response.json()["data"]["tiny_url"]
        else:
            log.info(response.status_code)
            log.info(response.json())
            return None

    def search(self, tes_number: str) -> str | None:
        base_url = f"{self.__url}alias/tinyurl.com/TES-{tes_number}"
        response = get(url=base_url, headers=self.__headers)

        return (
            response.json()["data"]["tiny_url"] if response.status_code == 200 else None
        )
