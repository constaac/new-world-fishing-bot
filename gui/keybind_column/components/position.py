from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def keybind_column_position(keybind_column):
    keybind_column_position_header = Label(keybind_column, text = "Rectangle position (px)")
    keybind_column_position_header.grid(row=0, column=0)
    keybind_column_position_container = LabelFrame(keybind_column)
    keybind_column_position_container.grid(row=1, column=0, padx=(10))
    keybind_column_position_x_container = Label(keybind_column_position_container, height=1)
    keybind_column_position_x_container.grid(row=0, column=0, padx=(20,19))
    keybind_column_position_x_text = Label(keybind_column_position_x_container, text="X:")
    keybind_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    keybind_column_position_x_scale = Scale(keybind_column_position_x_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['fishing']['x'])
    keybind_column_position_x_scale.grid(row=0, column=1)
    keybind_column_position_x_entry = Entry(keybind_column_position_x_container, width=4, textvariable=dict['fishing']['x'])
    keybind_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    keybind_column_position_y_container = Label(keybind_column_position_container, height=1)
    keybind_column_position_y_container.grid(row=1, column=0)
    keybind_column_position_y_text = Label(keybind_column_position_y_container, text="Y:")
    keybind_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    keybind_column_position_y_scale = Scale(keybind_column_position_y_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['fishing']['y'])
    keybind_column_position_y_scale.grid(row=0, column=1)
    keybind_column_position_y_entry = Entry(keybind_column_position_y_container, width=4, textvariable=dict['fishing']['y'])
    keybind_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))
