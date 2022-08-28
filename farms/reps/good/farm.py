import datetime
import time

from attack import attack
from quests import questsMethods


def farm():
    while True:
        times_to_submit_quest = 1
        questsMethods.submit_nth_quest_xth_times(4, times_to_submit_quest)
        time.sleep(2)
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()