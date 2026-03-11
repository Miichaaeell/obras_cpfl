from datetime import datetime
from .scraper import get_link_pdf
from obras_cpfl.settings import console, log


def format_date(date: datetime) -> str:
    return date.strftime("%d/%m/%Y")


def parse_works_response(responses: list[dict]) -> list[dict] | None:
    works: list[dict] = []
    with console.status("Tratando dados...", spinner="dots12"):
        for response in responses:
            response = response.get("Data") or None
            if response:
                city = response[0].get("NomeMunicipio", "")
                datas = response[0].get("Datas") or None
                if datas:
                    for data in datas:
                        date = data["Data"]
                        if "T" in date:
                            date = str(date).split("T")[0].split("-")
                        try:
                            date_formated = format_date(
                                datetime(
                                    year=int(date[0]),
                                    month=int(date[1]),
                                    day=int(date[2]),
                                )
                            )
                        except Exception as e:
                            log.exception(e)
                        documents = data.get("Documentos") or None
                        if documents:
                            for indice in range(0, len(documents)):
                                with console.status(
                                    "Criando payload de resposta...",
                                    spinner="aesthetic",
                                ):
                                    tes_document = documents[indice].get(
                                        "DescricaoDocumento", ""
                                    )
                                    status = documents[indice].get("Estado", "")
                                    bairros = documents[indice].get("Bairros") or []
                                    bairro = (
                                        bairros[0].get("NomeBairro") if bairros else ""
                                    )
                                    ruas = bairros[0].get("Ruas") or []
                                    rua = ruas[0].get("NomeRua") or ""
                                    hora_inicial = (
                                        documents[indice].get("PeriodoExecucaoInicial")
                                        or ""
                                    )
                                    if hora_inicial.strip():
                                        if "T" in hora_inicial:
                                            hora_inicial = hora_inicial.split("T")[1]
                                    hora_final = (
                                        documents[indice].get(
                                            "PeriodoExecucaoPeriodoFinal"
                                        )
                                        or ""
                                    )
                                    if hora_final.strip():
                                        if "T" in hora_final:
                                            hora_final = hora_final.split("T")[1]
                                    works.append(
                                        {
                                            "Cidade": city,
                                            "Data": date_formated,
                                            "Documento": tes_document,
                                            "Status": status,
                                            "Horario de início": hora_inicial,
                                            "Horario do final": hora_final,
                                            "Bairro": bairro,
                                            "Rua": rua,
                                        }
                                    )
    return works if works else []


def complete_response(responses: list) -> list[dict]:
    workers_list = parse_works_response(responses=responses)
    for worker in workers_list:
        tes_number = worker["Documento"].split(" ")[1]

        worker["PDF"] = get_link_pdf(tes_number=tes_number)
    return workers_list


def format_response(
    list_works: list[dict], start_date: datetime, end_date: datetime
) -> str:
    with console.status("Formatando resposta...", spinner="dots12"):
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
