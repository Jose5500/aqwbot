import time

import pyautogui

from mouse import mouseActions


def farm_fishing():
    while True:
        mouseActions.clickPosition((700,650))
        time.sleep(9)
        for i in range(10):
            mouseActions.clickPosition((700,525))