import utils.global_variables as gv
import random
from utils.config import dict, random_timeout
from time import sleep
from wrappers.win32api_wrapper import *
from wrappers.logging_wrapper import info, debug

def fish_notice():
    notice_timeout = random_timeout(dict['fishing']['timeouts']['notice'])
    debug("Press mouse key for: {} s".format(notice_timeout))
    press_mouse_key()
    sleep(notice_timeout)
    release_mouse_key()

def reel_fish():
    reel_timeout = random_timeout(dict['fishing']['timeouts']['reeling'])
    debug("Press mouse key for: {} s".format(reel_timeout))
    press_mouse_key()
    sleep(reel_timeout)
    release_mouse_key()

def pause():
    pause_timeout = random_timeout(dict['fishing']['timeouts']['pause'])
    debug("Pause for: {} s".format(pause_timeout))
    sleep(pause_timeout)

def cast():
    cast_timeout = random_timeout(dict['fishing']['timeouts']['cast'])
    key_to_press = dict['keybinds']['free_look']
    debug("Pause for: 6 s")
    sleep(6)
    debug("release " + key_to_press)
    release_key(key_to_press)
    debug("Pause for: 1 s")
    sleep(1)
    debug("Pause for: {} s".format(cast_timeout))
    press_mouse_key()
    sleep(cast_timeout)
    release_mouse_key()
    debug("Pause for: 5 s")
    sleep(5)
    debug(key_to_press)
    press_key(key_to_press)

def repairing():
    key_to_press = dict['keybinds']['free_look']
    release_key(key_to_press)
    arm_disarm_timeout = random_timeout(dict['repairing']['timeouts']['arm_disarm'])
    debug("Disarm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(arm_disarm_timeout)

    inventory_timeout = random_timeout(dict['repairing']['timeouts']['inventory'])
    debug("Open inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(inventory_timeout)

    repair_timeout = random_timeout(dict['repairing']['timeouts']['repair'])
    debug("Repair fishing rod. Total time: {} s".format(repair_timeout))
    repair(repair_timeout)

    confirm_timeout = random_timeout(dict['repairing']['timeouts']['confirm'])
    debug("Confirm repair. Total time: {} s".format(confirm_timeout))
    confirm_repair(confirm_timeout)

    debug("Close inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(inventory_timeout)

    debug("Arm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(arm_disarm_timeout)


def breaking_afk():
    release_key(dict['keybinds']['free_look'])
    horizontal_stutter()
    for _ in range(1, random.choice(range(3,7))):
        if random.choice([1,2]) == 1:
            horizontal_stutter()
        else:
            jump()

def horizontal_stutter():
    def go_left(timeout, timeout2):
        key_to_press = dict['keybinds']['strafe_left']
        debug("Pressing and releasing {}".format(key_to_press))
        press_key(key_to_press)
        sleep(timeout2)
        release_key(key_to_press)
        sleep(timeout)

    def go_right(timeout, timeout2):
        key_to_press = dict['keybinds']['strafe_right']
        debug("Pressing and releasing {}".format(key_to_press))
        press_key(key_to_press)
        sleep(timeout2)
        release_key(key_to_press)
        sleep(timeout)

    is_left = random.choice([1,2]) == 1
    info("Strafing {}".format("Right", "Left")[is_left])
    timeout = random_timeout(dict['fishing']['timeouts']['afk'])
    timeout2 = random_timeout(dict['fishing']['timeouts']['afk_strafe_return'])
    if is_left:
        go_left(timeout, timeout2)
        go_right(timeout, timeout2)
    else:
        go_right(timeout, timeout2)
        go_left(timeout, timeout2)
        


def jump():
    timeout = random_timeout(dict['fishing']['timeouts']['afk'])
    key_to_press = dict['keybinds']['jump']
    debug("Pressing and releasing {}".format(key_to_press))
    press_key(key_to_press)
    release_key(key_to_press)
    sleep(timeout)
    

def arm_disarm_fishing_rod(timeout):
    key_to_press = dict['keybinds']['arm_disarm_fishing_rod']
    sleep(timeout)
    press_key(key_to_press)
    release_key(key_to_press)
    sleep(timeout)

def open_close_inventory(timeout):
    key_to_press = dict['keybinds']['open_inventory']
    sleep(timeout)
    press_key(key_to_press)
    release_key(key_to_press)
    sleep(timeout)

def repair(timeout):
    key_to_press = dict['keybinds']['bait']
    sleep(timeout)
    press_key(key_to_press)
    sleep(0.1)
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    sleep(0.1)
    release_key(key_to_press)
    sleep(timeout)

def confirm_repair(timeout):
    key_to_press = dict['keybinds']['interact']
    sleep(timeout)
    press_key(key_to_press)
    sleep(0.1)
    release_key(key_to_press)
    sleep(timeout)

def select_bait():
    release_key(dict['keybinds']['free_look'])

    key_to_press = dict['keybinds']['bait']
    debug("Bait selection.")
    press_key(key_to_press)
    sleep(0.1)
    release_key(key_to_press)

    bait_select_timeout = random_timeout(dict['bait']['timeouts']['select'])
    debug("Bait select. Total time: {} s".format(bait_select_timeout))
    press_on_bait(bait_select_timeout)

    confirm_timeout = random_timeout(dict['bait']['timeouts']['confirm'])
    debug("Confirm bait selection. Total time: {} s".format(confirm_timeout))
    press_equip_bait(confirm_timeout)

def press_on_bait(timeout):
    sleep(timeout)
    click_mouse_with_coordinates(dict['bait']['bait_x'].get(), dict['bait']['bait_y'].get())
    sleep(timeout)

def press_equip_bait(timeout):
    sleep(timeout)
    click_mouse_with_coordinates(dict['bait']['equip_button_x'].get(), dict['bait']['equip_button_y'].get())
    sleep(timeout)
    # waiting for animation to finish
    sleep(1)