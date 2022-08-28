import time
import mss
import numpy
import pytesseract
from farms.nsod.farm import farm




# def first():
#     while True:
#         time.sleep(3)
#         pyautogui.moveTo(650, 650)
#         pyautogui.leftClick()
#         time.sleep(3)
#         pyautogui.moveTo(20, 380)
#         pyautogui.leftClick()
#         time.sleep(3)
#         pyautogui.moveTo(680, 760)
#         pyautogui.leftClick()
#
#
# def getItemText():
#     mon = {'top': 370, 'left': 500, 'width': 450, 'height': 175}
#
#     with mss.mss() as sct:
#         im = numpy.asarray(sct.grab(mon))
#         # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#
#         text = pytesseract.image_to_string(im)
#         return text


if __name__ == '__main__':
    # pyautogui.mouseInfo()
    time.sleep(2)
    farm()

