import time

import mss
import numpy
import pyautogui
from pytesseract import pytesseract

from mouse import constants, mouseActions
from inventory import constants


def openInventory():
    mouseActions.clickPosition(constants.INVENTORY_POS)


def closeInventory():
    mouseActions.clickPosition(constants.INVENTORY_POS)


def clickItemSearchBar():
    mouseActions.clickPosition(constants.ITEM_SEARCH_BAR_POS)


def searchItem(item):
    pyautogui.typewrite(item)
    pyautogui.press('enter')


def clickNthItem(nth):
    item_x, item_y = constants.FIRST_ITEM_POSITION_POS
    item_y += constants.ITEM_SPACING * (nth - 1)
    mouseActions.clickPosition(item_x, item_y)


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
    box_boundaries = constants.ITEM_BOX_BOUNDARIES

    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(box_boundaries))
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
    mouseActions.clickPosition(constants.ITEM_EQUIP_BUTTON_POS)
    time.sleep(1)
    closeInventory()
