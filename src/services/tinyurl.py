import os
from rich import print
from requests import post, get


class TinyUrl:
    def __init__(self):
        self.__url = "https://api.tinyurl.com/"
        self.__token = os.getenv(
            "tiny_token", "3yoWtTEXGw3O7ZlgWkuIuEdny93Pgx3FmtPIuuWvHAaEmDCeD30LtrGURKr7"
        )
        self.__headers = {
            "Authorization": f"Bearer {self.__token}",
            "Content-Type": "application/json",
        }

    def create(self, url: str, tes: str) -> str | None:
        base_url = f"{self.__url}create"
        payload = {
            "url": url,
            "domain": "tinyurl.com",
            "alias": str(f"TES-{tes}"),
            "description": "string",
        }
        response = post(url=base_url, json=payload, headers=self.__headers)
        if response.status_code == 200:
            return response.json()["data"]["tiny_url"]
        else:
            print(response.status_code)
            print(response.json())
            return None

    def search(self, tes: str) -> str | None:
        base_url = f"{self.__url}alias/tinyurl.com/TES-{tes}"
        response = get(url=base_url, headers=self.__headers)

        return (
            response.json()["data"]["tiny_url"] if response.status_code == 200 else None
        )
