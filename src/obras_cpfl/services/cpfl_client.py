from datetime import datetime, timedelta
from requests import get

from obras_cpfl.utils.formatters import format_message, format_response


class CPFLWorksClient:

    def __init__(self):
        self.__start_date: datetime = datetime.now().date()
        self.__end_date: datetime = self.__start_date + timedelta(days=7)
        self.__url = ("https://spir.cpfl.com.br/api/ConsultaDesligamentoProgramado/",)
        self.__url = (
            f"https://spir.cpfl.com.br/api/ConsultaDesligamentoProgramado/Pesquisar?"
            f"PeriodoDesligamentoInicial={self.__start_date}&PeriodoDesligamentoFinal={self.__end_date}&"
            "IdMunicipio={city}&NomeBairro=&NomeRua=&null"
        )
        self.__city: dict = {"Cosmopolis": 59, "Paulinia": 116}

    def search_works(self) -> list[dict]:
        responses: list = []
        for key, value in self.__city.items():
            responses.append(get(url=self.__url.format(city=value)).json())
        return format_message(responses)

    def works_week(self) -> str:
        works = self.search_works()
        return format_response(
            list_works=works, start_date=self.__start_date, end_date=self.__end_date
        )
