import datetime
import time

from attack import attack
from inventory import inventoryMethods
from mouse import mouseActions
from quests import questsMethods


def farm_void_auras():
    while True:
        is_maxed_out = False
        try:
            is_maxed_out = inventoryMethods.checkItemMaxedOut("undead essence")
        except:
            pass
        if is_maxed_out:
            mouseActions.clickPosition((1400, 750))
            time.sleep(2)
            times_to_submit_undead_essence = (inventoryMethods.getCurrAmountOfStacks("undead essence") // 25) - 1
            questsMethods.submit_nth_quest_xth_times(7, times_to_submit_undead_essence)
            times_to_submit_bone_dust = (inventoryMethods.getCurrAmountOfStacks("bone dust") // 40) - 1
            questsMethods.submit_nth_quest_xth_times(8, times_to_submit_bone_dust)
            mouseActions.clickPosition((350, 85))
            time.sleep(2)
        mouseActions.clickPosition((1050, 705))
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()


def farm_finding_fragments_quest():
    while True:
        is_maxed_out = False
        try:
            is_maxed_out = inventoryMethods.checkItemMaxedOut("blinding light fragments")
        except:
            pass
        if is_maxed_out:
            mouseActions.clickPosition((1400, 750))
            time.sleep(2)
            times_to_submit_undead_essence = (
                                                     inventoryMethods.getCurrAmountOfStacks(
                                                         "blinding light fragments") // 10) - 1
            questsMethods.submit_nth_quest_xth_times(1, times_to_submit_undead_essence)
            mouseActions.clickPosition((350, 85))
            time.sleep(2)
        mouseActions.clickPosition((1050, 705))
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()
