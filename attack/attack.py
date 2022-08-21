import datetime
import time

import pyautogui


def attack():
    time.sleep(1)
    pyautogui.press('2')

    time.sleep(1)
    pyautogui.press('3')

    time.sleep(1)
    pyautogui.press('4')

    time.sleep(1)
    pyautogui.press('5')

def attack_for_x_minutes(minutes):
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    while True:
        if datetime.datetime.now() >= endTime:
            break
        attack()