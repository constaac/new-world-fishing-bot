from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def keybind_column_fields(keybind_column):
    keybind_column_movement_header = Label(keybind_column, text = "Movement")
    keybind_column_movement_header.grid(row=0, column=0)

    movement_container = LabelFrame(keybind_column)
    movement_container.grid(row=1, column=0, padx=(10))

    keybind_column_movement_container = Label(movement_container, height=1)
    keybind_column_movement_container.grid(row=0, column=0, padx=(20,19))

    keybind_column_movement_forward_text = Label(keybind_column_movement_container, text="Forward: ")
    keybind_column_movement_forward_text.grid(row=0, column=0, pady=(10, 0))
    keybind_column_movement_forward_entry = Entry(keybind_column_movement_container, width=6, textvariable=dict['keybinds']['forward'])
    keybind_column_movement_forward_entry.grid(row=0, column=1, pady=(10, 0))

    keybind_column_movement_backward_text = Label(keybind_column_movement_container, text="Backward: ")
    keybind_column_movement_backward_text.grid(row=1, column=0, pady=(10, 0))
    keybind_column_movement_backward_entry = Entry(keybind_column_movement_container, width=6, textvariable=dict['keybinds']['backward'])
    keybind_column_movement_backward_entry.grid(row=1, column=1, pady=(10, 0))

    keybind_column_movement_strafe_left_text = Label(keybind_column_movement_container, text="Strafe Left: ")
    keybind_column_movement_strafe_left_text.grid(row=2, column=0, pady=(10, 0))
    keybind_column_movement_strafe_left_entry = Entry(keybind_column_movement_container, width=6, textvariable=dict['keybinds']['strafe_left'])
    keybind_column_movement_strafe_left_entry.grid(row=2, column=1, pady=(10, 0))

    keybind_column_movement_strafe_right_text = Label(keybind_column_movement_container, text="Strafe Right: ")
    keybind_column_movement_strafe_right_text.grid(row=3, column=0, pady=(10, 0))
    keybind_column_movement_strafe_right_entry = Entry(keybind_column_movement_container, width=6, textvariable=dict['keybinds']['strafe_right'])
    keybind_column_movement_strafe_right_entry.grid(row=3, column=1, pady=(10, 0))

    keybind_column_movement_jump_text = Label(keybind_column_movement_container, text="Jump: ")
    keybind_column_movement_jump_text.grid(row=4, column=0, pady=(10, 10))
    keybind_column_movement_jump_entry = Entry(keybind_column_movement_container, width=6, textvariable=dict['keybinds']['jump'])
    keybind_column_movement_jump_entry.grid(row=4, column=1, pady=(10, 10))


    keybind_column_interface_header = Label(keybind_column, text = "Interface")
    keybind_column_interface_header.grid(row=0, column=1)

    interface_container = LabelFrame(keybind_column)
    interface_container.grid(row=1, column=1, padx=(10))

    keybind_column_interface_container = Label(interface_container, height=1)
    keybind_column_interface_container.grid(row=0, column=0, padx=(20,19))

    keybind_column_interface_free_look_text = Label(keybind_column_interface_container, text="Free Look: ")
    keybind_column_interface_free_look_text.grid(row=0, column=0, pady=(10, 0))
    keybind_column_interface_free_look_entry = Entry(keybind_column_interface_container, width=6, textvariable=dict['keybinds']['free_look'])
    keybind_column_interface_free_look_entry.grid(row=0, column=1, pady=(10, 0))

    keybind_column_interface_interact_text = Label(keybind_column_interface_container, text="Interact: ")
    keybind_column_interface_interact_text.grid(row=1, column=0, pady=(10, 0))
    keybind_column_interface_interact_entry = Entry(keybind_column_interface_container, width=6, textvariable=dict['keybinds']['interact'])
    keybind_column_interface_interact_entry.grid(row=1, column=1, pady=(10, 0))

    keybind_column_interface_arm_disarm_fishing_rod_text = Label(keybind_column_interface_container, text="Arm/Disarm Rod: ")
    keybind_column_interface_arm_disarm_fishing_rod_text.grid(row=2, column=0, pady=(10, 0))
    keybind_column_interface_arm_disarm_fishing_rod_entry = Entry(keybind_column_interface_container, width=6, textvariable=dict['keybinds']['arm_disarm_fishing_rod'])
    keybind_column_interface_arm_disarm_fishing_rod_entry.grid(row=2, column=1, pady=(10, 0))

    keybind_column_interface_open_inventory_text = Label(keybind_column_interface_container, text="Open Inventory: ")
    keybind_column_interface_open_inventory_text.grid(row=3, column=0, pady=(10, 0))
    keybind_column_interface_open_inventory_entry = Entry(keybind_column_interface_container, width=6, textvariable=dict['keybinds']['open_inventory'])
    keybind_column_interface_open_inventory_entry.grid(row=3, column=1, pady=(10, 0))

    keybind_column_interface_jump_text = Label(keybind_column_interface_container, text="Bait: ")
    keybind_column_interface_jump_text.grid(row=4, column=0, pady=(10, 10))
    keybind_column_interface_jump_entry = Entry(keybind_column_interface_container, width=6, textvariable=dict['keybinds']['bait'])
    keybind_column_interface_jump_entry.grid(row=4, column=1, pady=(10, 10))
