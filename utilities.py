import datetime
import time

import pyautogui

import attack
import drops
import inventoryMethods
import mouseActions


def farm_until_max_stack(item, charPosition):
    is_maxed_out = False
    while True:
        try:
            is_maxed_out = inventoryMethods.checkItemMaxedOut(item)
        except Exception as e:
            print("ayo we broke over here in farm til max stack with an exception of")
            print(e)
            inventoryMethods.closeInventory()
        if is_maxed_out:
            return
        time.sleep(0.5)
        mouseActions.clickPosition(charPosition[0], charPosition[1])
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()

def farm_until_receive_item(item):
    item_in_drops = False
    while True:
        try:
            item_in_drops = drops.is_item_in_drops(item)
        except Exception as e:
            print("ayo we broke over here i farm til receive item with an exception of")
            print(e)
        if item_in_drops:
            time.sleep(2)
            drops.open_drops()
            time.sleep(2)
            drops.accept_drop()
            time.sleep(2)
            drops.close_drops()
            return
        time.sleep(0.5)
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=2)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            attack.attack()

def go_to_location(location):
    mouseActions.clickPosition(250,820)
    time.sleep(2)
    pyautogui.typewrite(location)
    pyautogui.press("enter")


