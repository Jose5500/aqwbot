import time
import cv2
import mss
import numpy
import pytesseract
import pyautogui

import attack
import drops
import farms
import mouseActions
import mousePositions
import questsMethods
import revenant
import utilities


def first():
    while True:
        time.sleep(3)
        pyautogui.moveTo(650, 650)
        pyautogui.leftClick()
        time.sleep(3)
        pyautogui.moveTo(20, 380)
        pyautogui.leftClick()
        time.sleep(3)
        pyautogui.moveTo(680, 760)
        pyautogui.leftClick()


def getItemText():
    mon = {'top': 370, 'left': 500, 'width': 450, 'height': 175}

    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)
        return text


if __name__ == '__main__':
    time.sleep(2)
    while True:
        attack.attack()


