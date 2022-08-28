import time

from mouse import constants, mouseActions


def open_pinned_quests():
    mouseActions.clickPosition(constants.PINNED_QUESTS_POS)

def click_nth_quest(n):
    quest_x,quest_y = constants.FIRST_QUEST_POS
    quest_y += (n-1) * constants.QUEST_SPACING
    mouseActions.clickPosition((quest_x,quest_y))

def accept_quest():
    mouseActions.clickPosition(constants.ACCEPT_QUEST_BUTTON_POS)

def submit_quest():
    mouseActions.clickPosition(constants.TURN_IN_QUEST_BUTTON_POS)

def submit_nth_quest_xth_times(n,x):
    open_pinned_quests()
    time.sleep(2)
    for i in range(x):
        click_nth_quest(n)
        time.sleep(2)
        submit_quest()
        time.sleep(2)
    open_pinned_quests()

