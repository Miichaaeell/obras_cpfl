from time import sleep
from rich.panel import Panel
from rich import print

from obras_cpfl.services.evolution_client import EvolutinClient
from obras_cpfl.services.cpfl_client import CPFLWorksClient

from obras_cpfl.settings import SEND_NUMBERS, console, log


def main():
    try:
        with console.status("Script iniciado...", spinner="aesthetic"):
            cpfl_client = CPFLWorksClient()
            msg = cpfl_client.works_week()
        with console.status("Enviando mensagem no whatsapp", spinner="dots12"):
            send_numbers: list[str] = [
                number.strip()
                for number in str(SEND_NUMBERS).split(",")
                if number.strip()
            ]
            bot = EvolutinClient()
            for number in send_numbers:
                res = bot.notification(number, msg)
                log.info(res)
                if len(send_numbers) > 1:
                    sleep(6)
        print(
            Panel(
                msg,
                title="Obras CPFL",
                title_align="center",
            )
        )
    except Exception as e:
        log.exception(e)


if __name__ == "__main__":
    log.info("Iniciando busca das obras CPFL")
    main()
