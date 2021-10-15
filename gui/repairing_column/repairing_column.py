from tkinter.constants import N
from gui.repairing_column.components.enable_repair import *
from gui.repairing_column.components.enable_afk_break import *
from gui.repairing_column.components.every import *
from gui.repairing_column.components.position import *
from gui.repairing_column.components.show_button import *
import utils.global_variables as gv
from tkinter import Label, LabelFrame

def repairing_column():
    repairing_column_header = Label(gv.root, text = "Repairing")
    repairing_column_header.grid(row=0, column=1, pady=(3, 0))
    repairing_column = LabelFrame(gv.root)
    repairing_column.grid(row=1, column=1, padx=(10, 0), pady=(0, 118), sticky=N)
    repairing_column_position_header = Label(repairing_column, text = "Click position (px)")
    repairing_column_position_header.grid(row=0, column=0)

    repairing_column_position(repairing_column)
    repairing_column_every(repairing_column)
    repairing_column_enable_repair(repairing_column)
    repairing_column_enable_afk_break(repairing_column)
    repairing_column_show(repairing_column)
