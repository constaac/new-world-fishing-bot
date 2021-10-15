from functools import partial
from gui.zannus_settings_button.zannus_settings_button import zannus_settings_button
from gui.save_button.save_button import save_button
from gui.gui_functions import on_closing
from gui.fishing_column.fishing_column import fishing_column
from gui.repairing_column.repairing_column import repairing_column
from gui.bait_column.bait_column import bait_column
from gui.keybind_column.keybind_column import keybind_column
from gui.start_fishing_button.start_fishing_button import start_fishing_button
from gui.zannus_settings_button.zannus_settings_button import zannus_settings_button
import utils.global_variables as gv

def gui_init():
    gv.root.resizable(False, False)
    gv.root.protocol("WM_DELETE_WINDOW", partial(on_closing))
    fishing_column()
    repairing_column()
    bait_column()
    keybind_column()
    start_fishing_button()
    save_button()
    zannus_settings_button()
