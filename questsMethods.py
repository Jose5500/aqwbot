import time

import mouseActions
import mousePositions


def open_pinned_quests():
    pinned_quest_x,pinned_quest_y = mousePositions.PINNED_QUESTS
    mouseActions.clickPosition(pinned_quest_x,pinned_quest_y)

def click_nth_quest(n):
    quest_x,quest_y = mousePositions.FIRST_QUEST_POSITION
    quest_y += (n-1) * mousePositions.QUEST_SPACING
    mouseActions.clickPosition(quest_x,quest_y)

def accept_quest():
    button_x,button_y = mousePositions.ACCEPT_QUEST_BUTTON
    mouseActions.clickPosition(button_x,button_y)

def submit_quest():
    button_x, button_y = mousePositions.TURN_IN_QUEST_BUTTON
    mouseActions.clickPosition(button_x,button_y)

def submit_nth_quest_xth_times(n,x):
    open_pinned_quests()
    time.sleep(2)
    for i in range(x):
        click_nth_quest(n)
        time.sleep(2)
        submit_quest()
        time.sleep(2)
    open_pinned_quests()

