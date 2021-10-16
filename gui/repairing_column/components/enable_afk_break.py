from tkinter import Label, LabelFrame, Button
from utils.config import dict
from functools import partial
from gui.gui_functions import change_afk_break_button_state

def repairing_column_enable_afk_break(repairing_column):
    repairing_column_enable_afk_break_container = LabelFrame(repairing_column)
    repairing_column_enable_afk_break_container.grid(row=5, column=0, pady=(0, 5))
    repairing_column_enable_afk_break_text = Label(repairing_column_enable_afk_break_container, text="Enable AFK Break:")
    repairing_column_enable_afk_break_text.grid(row=0, column=0, padx=(0, 20))
    repairing_column_enable_afk_break_button = Button(repairing_column_enable_afk_break_container)
    change_afk_break_button_state(repairing_column_enable_afk_break_button)
    change_afk_break_button_state(repairing_column_enable_afk_break_button)
    repairing_column_enable_afk_break_button.configure(command = partial(change_afk_break_button_state, repairing_column_enable_afk_break_button))
    repairing_column_enable_afk_break_button.grid(row=0, column=1, padx=(0, 13))
