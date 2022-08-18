import time

import mouseActions
import mss
import numpy
import pytesseract


def accept_drop():
    mouseActions.clickPosition(830, 740)


def reject_drop():
    mouseActions.clickPosition(860,740)

def get_curr_lowest_drop():
    mon = {'top': 726, 'left': 570, 'width': 240, 'height': 25}

    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        return text
def is_item_in_drops(item):
    open_drops()
    while True:
        time.sleep(2)
        curr_lowest_drop = get_curr_lowest_drop()
        if curr_lowest_drop == "":
            close_drops()
            return False
        print(curr_lowest_drop)
        if item in curr_lowest_drop:
            close_drops()
            return True
        else:
            reject_drop()
def open_drops():
    mouseActions.clickPosition(720,765)

def close_drops():
    mouseActions.clickPosition(720, 765)

