import datetime
import time

from attack import attack
from quests import questsMethods


def farm_legion_tokens():
    while True:
        times_to_submit_quest = 5
        questsMethods.submit_nth_quest_xth_times(3, times_to_submit_quest)
        time.sleep(2)
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=2)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()