import datetime
import time

import pyautogui

import attack
import inventoryMethods
import mouseActions
import questsMethods


def farm_void_auras():
    while True:
        is_maxed_out = False
        try:
            is_maxed_out = inventoryMethods.checkItemMaxedOut("undead essence")
        except:
            pass
        if is_maxed_out:
            mouseActions.clickPosition(1400, 750)
            time.sleep(2)
            times_to_submit_undead_essence = (inventoryMethods.getCurrAmountOfStacks("undead essence")//25) - 1
            questsMethods.submit_nth_quest_xth_times(7, times_to_submit_undead_essence)
            times_to_submit_bone_dust = (inventoryMethods.getCurrAmountOfStacks("bone dust")//40) - 1
            questsMethods.submit_nth_quest_xth_times(8, times_to_submit_bone_dust)
            mouseActions.clickPosition(350, 85)
            time.sleep(2)
        mouseActions.clickPosition(1050, 705)
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
            mouseActions.clickPosition(1400, 750)
            time.sleep(2)
            times_to_submit_undead_essence = (inventoryMethods.getCurrAmountOfStacks("blinding light fragments")//10) - 1
            questsMethods.submit_nth_quest_xth_times(1, times_to_submit_undead_essence)
            mouseActions.clickPosition(350, 85)
            time.sleep(2)
        mouseActions.clickPosition(1050, 705)
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()

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

def farm_good_rep():
    while True:
        times_to_submit_quest = 1
        questsMethods.submit_nth_quest_xth_times(4, times_to_submit_quest)
        time.sleep(2)
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()

def farm_dark_tokens():
    while True:
        for i in range(20):
            attack.attack()
        for i in range(10):
            mouseActions.clickPosition(942,143)
            time.sleep(0.5)
            mouseActions.clickPosition(1010,143)
            time.sleep(0.5)
def farm_fishing():
    while True:
        pyautogui.moveTo(700, 650)
        pyautogui.leftClick()
        time.sleep(9)
        pyautogui.moveTo(700, 525)
        for i in range(10):
            pyautogui.leftClick()
