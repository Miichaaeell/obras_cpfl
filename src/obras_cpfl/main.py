from time import sleep

from obras_cpfl.services.textmebot_client import TextMeBot
from obras_cpfl.services.cpfl_client import CPFLWorksClient

from obras_cpfl.settings import SEND_NUMBERS, log


def main():
    cpfl_cliet = CPFLWorksClient()
    msg = cpfl_cliet.works_week()
    send_numbers: list[str] = [number for number in str(SEND_NUMBERS).split(",")]
    bot = TextMeBot()
    print(msg)
    log.info(msg)
    for number in send_numbers:
        res = bot.notification(number, msg)
        log.info(res)
        sleep(6)


if __name__ == "__main__":
    main()
