import time

import mss
import numpy
import pyautogui
from pytesseract import pytesseract

import mouseActions
import mousePositions


def openInventory():
    mouseActions.clickPosition(1400,820)


def closeInventory():
    mouseActions.clickPosition(1400,820)

def clickItemSearchBar():
    search_bar_x, search_bar_y = mousePositions.ITEM_SEARCH_BAR
    mouseActions.clickPosition(search_bar_x, search_bar_y)


def searchItem(item):
    pyautogui.typewrite(item)
    pyautogui.press('enter')


def clickNthItem(nth):
    item_x, item_y = mousePositions.FIRST_ITEM_POSITION
    item_y += mousePositions.ITEM_SPACING * (nth - 1)
    mouseActions.clickPosition(item_x,item_y)


def checkItemMaxedOut(item):
    openInventory()
    time.sleep(0.5)
    clickItemSearchBar()
    time.sleep(0.5)
    searchItem(item)
    time.sleep(0.5)
    clickNthItem(1)
    time.sleep(1)
    currAmount, capacity = getCurrItemAmountAndCapacity()
    time.sleep(0.5)
    closeInventory()
    return int(currAmount) == int(capacity)


def getCurrAmountOfStacks(item):
    openInventory()
    time.sleep(0.5)
    clickItemSearchBar()
    time.sleep(0.5)
    searchItem(item)
    time.sleep(0.5)
    clickNthItem(1)
    time.sleep(1)
    currAmount, _ = getCurrItemAmountAndCapacity()
    closeInventory()
    return int(currAmount)


def getItemText():
    mon = {'top': 370, 'left': 500, 'width': 450, 'height': 175}

    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)
        return text


def getCurrItemAmountAndCapacity():
    item_text = getItemText()
    split_text = item_text.split()
    currItemAmount = ""
    for text in split_text:
        if '/' in text:
            currItemAmount = text
    currItemAmount = currItemAmount.split('/')
    currAmount, max = currItemAmount
    return [currAmount, max]


def equipItem(item):
    openInventory()
    clickItemSearchBar()
    searchItem(item)
    time.sleep(1)
    clickNthItem(1)
    time.sleep(1)
    mouseActions.clickPosition(800, 740)
    time.sleep(1)
    closeInventory()
