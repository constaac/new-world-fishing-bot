from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def keybind_column_attributes(keybind_column):
    keybind_column_attributes_header = Label(keybind_column, text = "Rectangle attributes (px)")
    keybind_column_attributes_header.grid(row=2, column=0)
    keybind_column_attributes_container = LabelFrame(keybind_column)
    keybind_column_attributes_container.grid(row=3, column=0, padx=(10))
    keybind_column_attributes_width_container = Label(keybind_column_attributes_container, height=1)
    keybind_column_attributes_width_container.grid(row=0, column=0, padx=(5))
    keybind_column_attributes_width_text = Label(keybind_column_attributes_width_container, text="Width:")
    keybind_column_attributes_width_text.grid(row=0, column=0, pady=(20, 0))
    keybind_column_attributes_width_scale = Scale(keybind_column_attributes_width_container, from_=0, to=dict['resolution']['x'], orient=HORIZONTAL, variable=dict['fishing']['width'])
    keybind_column_attributes_width_scale.grid(row=0, column=1)
    keybind_column_attributes_width_entry = Entry(keybind_column_attributes_width_container, width=4, textvariable=dict['fishing']['width'])
    keybind_column_attributes_width_entry.grid(row=0, column=2, pady=(20, 0))
    keybind_column_attributes_height_container = Label(keybind_column_attributes_container, height=1)
    keybind_column_attributes_height_container.grid(row=1, column=0, padx=(5))
    keybind_column_attributes_height_text = Label(keybind_column_attributes_height_container, text="Height:")
    keybind_column_attributes_height_text.grid(row=0, column=0, pady=(20, 0))
    keybind_column_attributes_height_scale = Scale(keybind_column_attributes_height_container, from_=0, to=dict['resolution']['y'], orient=HORIZONTAL, variable=dict['fishing']['height'])
    keybind_column_attributes_height_scale.grid(row=0, column=1)
    keybind_column_attributes_height_entry = Entry(keybind_column_attributes_height_container, width=4, textvariable=dict['fishing']['height'])
    keybind_column_attributes_height_entry.grid(row=0, column=2, pady=(20, 0))
