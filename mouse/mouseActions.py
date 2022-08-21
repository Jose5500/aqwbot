import time

import pyautogui


def clickPosition(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(0.5)
    pyautogui.leftClick()