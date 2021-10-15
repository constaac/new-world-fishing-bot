from gui.keybind_column.components.fields import keybind_column_fields
import utils.global_variables as gv
from tkinter import Label, LabelFrame

def keybind_column():
    keybind_column_header = Label(gv.root, text = "Keybinds")
    keybind_column_header.grid(row=0, column=4, pady=(3, 0))
    keybind_column = LabelFrame(gv.root)
    keybind_column.grid(row=1, column=4, padx=(10, 0), pady=(0, 70))

    keybind_column_fields(keybind_column)