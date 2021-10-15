from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def keybind_column_fields(keybind_column):
    keybind_column_movement_header = Label(keybind_column, text = "Movement")
    keybind_column_movement_header.grid(row=0, column=0)

    movement_container = LabelFrame(keybind_column)
    movement_container.grid(row=1, column=0, padx=(10))

    keybind_column_position_x_container = Label(movement_container, height=1)
    keybind_column_position_x_container.grid(row=0, column=0, padx=(20,19))

    keybind_column_position_x_text = Label(keybind_column_position_x_container, text="Forward:")
    keybind_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    keybind_column_position_x_entry = Entry(keybind_column_position_x_container, width=4, textvariable=dict['keybinds']['forward'])
    keybind_column_position_x_entry.grid(row=0, column=1, pady=(20, 0))
