from datetime import datetime, timedelta
from requests import get
import re
from urllib.parse import quote

from bs4 import BeautifulSoup

from services.tinyurl import TinyUrl


class GetWorks:
    start_data: datetime = datetime.now().date()
    end_data: datetime = start_data + timedelta(days=7)

    def __init__(self):
        self.__url = (
            f"https://spir.cpfl.com.br/api/ConsultaDesligamentoProgramado/Pesquisar?"
            f"PeriodoDesligamentoInicial={GetWorks.start_data}&PeriodoDesligamentoFinal={GetWorks.end_data}&"
            "IdMunicipio={city}&NomeBairro=&NomeRua=&null"
        )
        self.__city: dict = {"Cosmopolis": 59, "Paulinia": 116}

    def format_date(self, date: datetime) -> str:
        return date.strftime("%d/%m/%Y")

    def search_works(self) -> list[dict]:
        works: list[dict] = []
        responses: list = []
        for key, value in self.__city.items():
            responses.append(
                get(
                    url=self.__url.format(city=value),
                ).json()
            )
        for response in responses:
            if response["Data"]:
                city = response["Data"][0]["NomeMunicipio"]
                for data in response["Data"][0]["Datas"]:
                    date = str(data["Data"]).split("T")[0].split("-")
                    date_formated = self.format_date(
                        datetime(
                            year=int(date[0]), month=int(date[1]), day=int(date[2])
                        )
                    )
                    for indice in range(0, len(data["Documentos"])):
                        works.append(
                            {
                                "Cidade": city,
                                "Data": date_formated,
                                "Documento": data["Documentos"][indice][
                                    "DescricaoDocumento"
                                ],
                                "Status": data["Documentos"][indice]["Estado"],
                                "Horario de início": str(
                                    data["Documentos"][indice]["PeriodoExecucaoInicial"]
                                ).split("T")[1],
                                "Horario do final": str(
                                    data["Documentos"][indice][
                                        "PeriodoExecucaoPeriodoFinal"
                                    ]
                                ).split("T")[1],
                                "Bairro": data["Documentos"][indice]["Bairros"][0][
                                    "NomeBairro"
                                ],
                                "Rua": data["Documentos"][indice]["Bairros"][0]["Ruas"][
                                    0
                                ]["NomeRua"],
                                "PDF": self.get_link_pdf(
                                    str(
                                        data["Documentos"][indice]["DescricaoDocumento"]
                                        .strip()
                                        .split(" ")[1]
                                    )
                                ),
                            }
                        )
        return works if works else []

    def get_link_pdf(self, tes: str) -> str:
        tiny = TinyUrl()
        base_url = "http://201.130.20.15:8609"
        response = get(base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            path_pdf = soup.find(
                class_=re.compile("bg-green"), href=re.compile(f"{tes}")
            ).get("href")
            if " " in path_pdf:
                path_pdf = quote(path_pdf)
        except Exception as e:
            print(e)
            return "Não encontrado link do PDF"
        short_url = tiny.search(tes)
        if not short_url:
            short_url = tiny.create(url=f"{base_url}{path_pdf}", tes=tes)

        return short_url

    def return_works(self) -> str:
        works = self.search_works()
        messages = []
        for work in works:
            message: str = ""
            for key, value in work.items():
                message += f"{key}: {value}\n"
            messages.append(message)

        final_msg: str = (
            f"*OBRAS CPFL {self.format_date(GetWorks.start_data)} - {self.format_date(GetWorks.end_data)}* \n"
            + "-" * 60
            + "\n"
        )
        for msg in messages:
            final_msg += f"{msg}" + "-" * 60 + "\n"

        return final_msg
