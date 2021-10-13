import utils.global_variables as gv
from tkinter import Button, LabelFrame
from functools import partial
from gui.gui_functions import toggle_zannus_settings

def zannus_settings_button():
    zannus_settings_container = LabelFrame(gv.root)
    zannus_settings_container.grid(row=4, columnspan=4, padx=(10, 0), pady=(15, 0))
    zannus_settings_button = Button(zannus_settings_container, text = "Zannus Settings", font=18)
    zannus_settings_button.configure(command = partial(toggle_zannus_settings, zannus_settings_button))
    zannus_settings_button.grid(row=0, column=0)
