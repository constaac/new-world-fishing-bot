from tkinter import LabelFrame, Button, Entry
from utils.config import dict
from functools import partial
from gui.gui_functions import popup_rectangle_window

def keybind_column_show_button(keybind_column):
    keybind_column_show_container = LabelFrame(keybind_column)
    keybind_column_show_container.grid(row=4, column=0, pady=(5, 0))
    keybind_column_show_button = Button(keybind_column_show_container, text = "Show fishing position")
    keybind_column_show_button.configure(command = partial(popup_rectangle_window, keybind_column_show_button, dict['fishing']['x'], dict['fishing']['y'], dict['fishing']['width'], dict['fishing']['height']))
    keybind_column_show_button.grid(row=4, column=0, padx=(34, 34), pady=(2, 4))
