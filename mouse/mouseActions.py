import time

import pyautogui


def clickPosition(position):
    x, y = position
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.leftClick()
