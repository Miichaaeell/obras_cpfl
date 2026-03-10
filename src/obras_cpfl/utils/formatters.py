from datetime import datetime
from .scrapper import get_link_pdf


def format_date(date: datetime) -> str:
    return date.strftime("%d/%m/%Y")


def format_message(responses: list[dict]) -> list[dict] | None:
    works: list[dict] = []
    for response in responses:
        if response["Data"]:
            city = response["Data"][0]["NomeMunicipio"]
            for data in response["Data"][0]["Datas"]:
                date = str(data["Data"]).split("T")[0].split("-")
                date_formated = format_date(
                    datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]))
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
                            "Rua": data["Documentos"][indice]["Bairros"][0]["Ruas"][0][
                                "NomeRua"
                            ],
                            "PDF": get_link_pdf(
                                str(
                                    data["Documentos"][indice]["DescricaoDocumento"]
                                    .strip()
                                    .split(" ")[1]
                                )
                            ),
                        }
                    )
    return works if works else []


def format_response(
    list_works: list[dict], start_date: datetime, end_date: datetime
) -> str:
    messages = []
    for work in list_works:
        message: str = ""
        for key, value in work.items():
            message += f"{key}: {value}\n"
        messages.append(message)

    final_msg: str = (
        f"*OBRAS CPFL {format_date(start_date)} - {format_date(end_date)}* \n"
        + "-" * 60
        + "\n"
    )
    for msg in messages:
        final_msg += f"{msg}" + "-" * 60 + "\n"

    return final_msg
