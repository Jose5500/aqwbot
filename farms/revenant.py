import time

import pyautogui

from attack import attack
from inventory import inventoryMethods
from mouse import mouseActions
from quests import questsMethods
import utilities


def farm_spellscroll():
    # go to revenant
    utilities.go_to_location("/join revenant")
    time.sleep(5)
    # change class to void highlord
    inventoryMethods.equipItem("Void Highlord")
    time.sleep(1)
    # go to wisps
    mouseActions.clickPosition(1075, 240)
    time.sleep(3)
    # farm wisps until max stack
    utilities.farm_until_max_stack("Tethered Soul", [230, 610])
    time.sleep(2)
    # go to aecus
    mouseActions.clickPosition(650, 170)
    time.sleep(3)
    # change weapon to BLOD
    inventoryMethods.equipItem("Blinding light of destiny")
    time.sleep(3)
    pyautogui.leftClick(530, 685)
    # farm aeacus until max stack
    utilities.farm_until_max_stack("Aeacus Empowered", [530, 685])
    # leave aeacus
    mouseActions.clickPosition(350, 770)
    time.sleep(3)
    # equip BBOA
    inventoryMethods.equipItem("Dual Burning Blades Of Abezeth")
    time.sleep(1)
    # join shadowrealmpast
    utilities.go_to_location("/join shadowrealmpast")
    time.sleep(5)
    # equip farming class
    inventoryMethods.equipItem("Blaze Binder")
    time.sleep(1)
    mouseActions.clickPosition(700, 430)
    # farm shadow people until max stack
    utilities.farm_until_max_stack("Darkened Essence", [700, 430])
    # get out of room
    mouseActions.clickPosition(1230, 500)
    time.sleep(3)
    # go to necrodungeon
    utilities.go_to_location("/join necrodungeon")
    time.sleep(5)
    # get to dracolichs
    get_to_dracolichs()
    time.sleep(2)
    # farm until I get dracolich contract
    # utilities.farm_until_receive_item("Dracolich Contract")
    # time.sleep(2)
    # farm til max stack of dracolich contract
    utilities.farm_until_max_stack("Dracolich Contract", [730, 675])
    time.sleep(2)
    # get out of room
    mouseActions.clickPosition(485, 755)
    time.sleep(2)
    # turn in quest
    questsMethods.submit_nth_quest_xth_times(1, 1)
    time.sleep(2)


def farm_wreath():
    # go to doomvault
    utilities.go_to_location("/join doomvault-6969")
    time.sleep(5)
    # walk to lever
    mouseActions.clickPosition(436, 663)
    time.sleep(2)
    # click lever
    mouseActions.clickPosition(258, 623)
    time.sleep(2)
    # enter door
    mouseActions.clickPosition(745, 626)
    time.sleep(2)
    utilities.farm_until_max_stack("Grim Cohort Conquered", [731, 715])
    time.sleep(1)
    mouseActions.clickPosition(509, 772)
    time.sleep(5)

    # go to mummies
    utilities.go_to_location("/join mummies")
    time.sleep(5)
    utilities.farm_until_max_stack("Ancient Cohort Conquered", [148, 392])
    time.sleep(1)
    mouseActions.clickPosition(1439, 566)
    time.sleep(5)

    # go to wrath
    utilities.go_to_location("/join wrath-6969")
    time.sleep(5)
    mouseActions.clickPosition(1411, 556)
    time.sleep(5)
    mouseActions.clickPosition(1414, 509)
    time.sleep(5)
    mouseActions.clickPosition(1410, 513)
    time.sleep(5)
    utilities.farm_until_max_stack("Pirate Cohort Conquered", [167, 496])
    time.sleep(1)
    mouseActions.clickPosition(0, 475)
    time.sleep(5)

    # go to overworld
    utilities.go_to_location("/join overworld-6969")
    time.sleep(5)
    mouseActions.clickPosition(1403, 750)
    time.sleep(3)
    mouseActions.clickPosition(1422, 483)
    time.sleep(3)
    utilities.farm_until_max_stack("Mirror Cohort Conquered", [234, 477])
    time.sleep(1)
    mouseActions.clickPosition(0, 569)
    time.sleep(5)

    # go to deathpits
    utilities.go_to_location("/join deathpits-6969")
    time.sleep(5)
    mouseActions.clickPosition(0, 527)
    time.sleep(5)
    utilities.farm_until_max_stack("Darkblood Cohort Conquered", [177, 334])
    time.sleep(1)
    mouseActions.clickPosition(80, 44)
    time.sleep(5)

    # go to maxius
    utilities.go_to_location("/join maxius")
    time.sleep(5)
    mouseActions.clickPosition(743, 687)
    time.sleep(3)
    mouseActions.clickPosition(1385, 422)
    time.sleep(3)
    utilities.farm_until_max_stack("Vampire Cohort Conquered", [255, 557])
    time.sleep(1)
    mouseActions.clickPosition(0, 561)
    time.sleep(5)

    # go to cursheshore
    utilities.go_to_location("/join curseshore")
    time.sleep(5)
    utilities.farm_until_max_stack("Spirit Cohort Conquered", [167, 672])
    time.sleep(1)
    mouseActions.clickPosition(1439, 695)
    time.sleep(5)

    # go to dragonbone
    utilities.go_to_location("/join dragonbone-6969")
    time.sleep(5)
    utilities.farm_until_max_stack("Dragon Cohort Conquered", [753, 737])
    time.sleep(1)
    mouseActions.clickPosition(1439, 736)
    time.sleep(5)

    # go to doomwood
    utilities.go_to_location("/join doomwood")
    time.sleep(5)
    mouseActions.clickPosition(0, 615)
    time.sleep(5)
    mouseActions.clickPosition(648, 219)
    time.sleep(3)
    mouseActions.clickPosition(201, 468)
    time.sleep(3)
    utilities.farm_until_max_stack("Doomwood Cohort Conquered", [1285, 636])
    time.sleep(1)
    mouseActions.clickPosition(1439, 609)
    time.sleep(5)

    # go to doomwar
    utilities.go_to_location("/join doomwar-6969")
    time.sleep(5)
    mouseActions.clickPosition(1260, 404)
    time.sleep(5)
    mouseActions.clickPosition(926, 263)
    time.sleep(2)
    utilities.farm_until_max_stack("Battleon Cohort Conquered", [417, 669])
    time.sleep(1)
    mouseActions.clickPosition(476, 772)
    time.sleep(5)

    questsMethods.submit_nth_quest_xth_times(2, 1)
    time.sleep(2)


def farm_diamond_token_of_dage():
    while True:
        # farm makais
        utilities.go_to_location("/house stu")
        time.sleep(5)
        mouseActions.clickPosition(705, 354)
        time.sleep(3)
        mouseActions.clickPosition(705, 354)
        time.sleep(3)
        mouseActions.clickPosition(705, 354)
        time.sleep(3)
        mouseActions.clickPosition(595, 486)
        time.sleep(5)
        mouseActions.clickPosition(576, 618)
        time.sleep(3)
        mouseActions.clickPosition(762, 278)
        time.sleep(3)
        mouseActions.clickPosition(616, 494)
        time.sleep(5)
        mouseActions.clickPosition(492, 292)
        time.sleep(3)
        mouseActions.clickPosition(1333, 551)
        time.sleep(3)
        attack.attack_for_x_minutes(1)
        mouseActions.clickPosition(882, 45)
        time.sleep(3)
        mouseActions.clickPosition(2, 257)
        time.sleep(3)

        # go to carnax
        utilities.go_to_location("/join aqlesson")
        time.sleep(5)
        mouseActions.clickPosition(1160, 410)
        time.sleep(3)
        mouseActions.clickPosition(467, 762)
        time.sleep(3)
        attack.attack_for_x_minutes(0.5)
        mouseActions.clickPosition(1439, 731)
        time.sleep(3)

        # go to squid
        utilities.go_to_location("/join museum")
        time.sleep(5)
        mouseActions.clickPosition(1437, 584)
        time.sleep(3)
        mouseActions.clickPosition(160, 315)
        time.sleep(2)
        mouseActions.clickPosition(611, 504)
        time.sleep(5)
        attack.attack_for_x_minutes(0.5)
        mouseActions.clickPosition(3, 615)
        time.sleep(3)

        # kill red dragon
        utilities.go_to_location("/join underlair")
        time.sleep(5)
        mouseActions.clickPosition(12, 53)
        time.sleep(3)
        mouseActions.clickPosition(595, 485)
        time.sleep(5)
        mouseActions.clickPosition(584, 749)
        time.sleep(5)
        mouseActions.clickPosition(1439, 549)
        time.sleep(5)
        mouseActions.clickPosition(1439, 549)
        time.sleep(5)
        mouseActions.clickPosition(1377, 294)
        time.sleep(5)
        attack.attack_for_x_minutes(1)
        mouseActions.clickPosition(1406, 63)
        time.sleep(3)

        # go to fluffy
        utilities.go_to_location("/join dflesson")
        time.sleep(5)
        mouseActions.clickPosition(466, 635)
        time.sleep(3)
        mouseActions.clickPosition(1225, 548)
        time.sleep(3)
        attack.attack_for_x_minutes(0.5)
        mouseActions.clickPosition(1439, 730)
        time.sleep(3)

        # go to bloodtitan
        utilities.go_to_location("/join bloodtitan")
        time.sleep(5)
        pyautogui.press('3')
        time.sleep(0.75)
        pyautogui.press('1')
        attack.attack_for_x_minutes(1)
        mouseActions.clickPosition(1257, 120)
        time.sleep(3)
        if inventoryMethods.getCurrAmountOfStacks("Defeated Makai") > 25:
            questsMethods.submit_nth_quest_xth_times(6, 1)
        time.sleep(2)


def get_to_dracolichs():
    positions = [[570, 515], [1180, 670], [930, 740], [990, 685], [970, 285], [1050, 385], [1405, 510], [1420, 585],
                 [1390, 505], [990, 670], [885, 335], [1050, 385], [1100, 665], [1280, 390], [1415, 585], [1415, 385],
                 [1100, 670], [1270, 470], [760, 490], [1345, 720], [1350, 430], [1050, 385], [1410, 585], [1410, 585],
                 [1080, 485]]
    for x, y in positions:
        mouseActions.clickPosition(x, y)
        time.sleep(10)
