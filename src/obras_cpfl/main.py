from time import sleep

from obras_cpfl.services.textmebot_client import TextMeBot
from obras_cpfl.services.cpfl_client import CPFLWorksClient

from obras_cpfl.settings import SEND_NUMBERS, console


def main():
    cpfl_client = CPFLWorksClient()
    msg = cpfl_client.works_week()
    send_numbers: list[str] = [
        number.strip() for number in str(SEND_NUMBERS).split(",") if number.strip()
    ]
    bot = TextMeBot()
    console.log(f"\n{msg}", style="green")
    for number in send_numbers:
        res = bot.notification(number, msg)
        console.log(res)
        sleep(6)


if __name__ == "__main__":
    main()
