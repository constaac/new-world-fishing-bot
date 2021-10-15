import utils.global_variables as gv
from tkinter import Button, LabelFrame
from functools import partial
from gui.gui_functions import save


def save_button():
    save_container = LabelFrame(gv.root)
    save_container.grid(row=5, columnspan=6, padx=(10, 0), pady=(15, 15))
    save_button = Button(save_container, text = "Save", font=18)
    save_button.configure(command = partial(save))
    save_button.grid(row=0, column=0)
