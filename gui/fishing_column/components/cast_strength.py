from tkinter import *
from utils.config import dict

def fishing_column_cast_strength(fishing_column):
    fishing_column_cast_strength_header = Label(fishing_column, text = "Cast Distance")
    fishing_column_cast_strength_header.grid(row=5, column=0, pady=(10, 0),)
    fishing_column_cast_strength_container = LabelFrame(fishing_column)
    fishing_column_cast_strength_container.grid(row=6, column=0, padx=(10))

    values = {"Minimum" : "1",
            "Shallow" : "2",
            "Deep" : "3",
            "Maxiumum" : "4"}
    for (text, value) in values.items():
        Radiobutton(fishing_column_cast_strength_container, text = text, variable = dict['fishing']['cast_strength'],
            value = value).pack(side = TOP, ipady = 5)