import re
from requests import get
from bs4 import BeautifulSoup
from urllib.parse import quote

from obras_cpfl.services.tinyurl_client import TinyUrl
from obras_cpfl.settings import console


def get_link_pdf(tes_number: str) -> str:
    with console.status("Gerando link pdf...", spinner="arrow3"):
        base_url = "http://201.130.20.15:8609"
        response = get(base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        pdf = soup.find(class_=re.compile("bg-green"), href=re.compile(f"{tes_number}"))
        path_pdf = pdf.get("href") if pdf else None
        if path_pdf and " " in path_pdf:
            path_pdf = quote(path_pdf)
        if path_pdf:
            tiny = TinyUrl()
            short_url = tiny.search(tes_number)
            if not short_url:
                short_url = tiny.create(
                    url=f"{base_url}{path_pdf}", tes_number=tes_number
                )
        else:
            short_url = "Não foi possível gerar o link do pdf"
    return short_url
