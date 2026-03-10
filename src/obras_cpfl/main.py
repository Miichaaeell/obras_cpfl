from time import sleep

from services import textmebot, cpfl

cpfl_workers = cpfl.GetWorks()
bot = textmebot.TextMeBot()


msg = cpfl_workers.return_works()
numbers: list[str] = ["120363324345011236@g.us"]
print(msg)
for number in numbers:
    res = bot.notification(number, msg)
    print(res)
    sleep(6)
