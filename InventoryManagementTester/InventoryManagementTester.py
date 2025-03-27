from ctypes import alignment
import tkinter as tk
from tkinter import ttk

from available_bays import bay_stack
from inventory_dictionary import inventory_dictionary

empty_bays = bay_stack()
inventory = inventory_dictionary()

#Initialize all bays labels in configuration for option one
for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
    for number in range(1,12):
        empty_bays.add(letter + str(number))
for number in range(1,11):
    empty_bays.add('G' + str(number))

# #TESTING BLOCK
# # FD FZ GY
# inventory.add_to_inventory("FD FZ GY","FG01")
# inventory.add_to_inventory("FD FZ GY","FG02")
# inventory.add_to_inventory("FD FZ GY","FG03")
# inventory.add_to_inventory("FD FZ GY","FG04")
# # FD FZ WW
# inventory.add_to_inventory("FD FZ WW","FG05")
# inventory.add_to_inventory("FD FZ WW","FG06")
# inventory.add_to_inventory("FD FZ WW","FG07")
# inventory.add_to_inventory("FD FZ WW","FG08")
# # FD FF GY
# inventory.add_to_inventory("FD FF GY","FG09")
# inventory.add_to_inventory("FD FF GY","FG10")
# inventory.add_to_inventory("FD FF GY","FG11")
# inventory.add_to_inventory("FD FF GY","FG12")
# # FD FF WW
# inventory.add_to_inventory("FD FF WW","FG13")
# inventory.add_to_inventory("FD FF WW","FG14")
# inventory.add_to_inventory("FD FF WW","FG15")
# inventory.add_to_inventory("FD FF WW","FG16")
# # CD FZ GY
# inventory.add_to_inventory("CD FZ GY","FG17")
# inventory.add_to_inventory("CD FZ GY","FG18")
# inventory.add_to_inventory("CD FZ GY","FG19")
# inventory.add_to_inventory("CD FZ GY","FG20")
# # CD FZ WW
# inventory.add_to_inventory("CD FZ WW","FG21")
# inventory.add_to_inventory("CD FZ WW","FG22")
# inventory.add_to_inventory("CD FZ WW","FG23")
# inventory.add_to_inventory("CD FZ WW","FG24")
# # CD FF GY
# inventory.add_to_inventory("CD FF GY","FG25")
# inventory.add_to_inventory("CD FF GY","FG26")
# inventory.add_to_inventory("CD FF GY","FG27")
# inventory.add_to_inventory("CD FF GY","FG28")
# # CD FF WW
# inventory.add_to_inventory("CD FF WW","FG29")
# inventory.add_to_inventory("CD FF WW","FG30")
# inventory.add_to_inventory("CD FF WW","FG31")
# inventory.add_to_inventory("CD FF WW","FG32")


# print(inventory.get_next("FD FZ GY"))
# print(inventory.get_next("FD FF GY"))
# print(inventory.get_next("FD FZ GY"))
# print(inventory.get_next("FD FZ GY"))
# print(inventory.get_next("FD FZ GY"))
# print(inventory.get_next("FD FZ GY"))

main_window = tk.Tk()
main_window.title('Sheet Warehouse Manager')

label = tk.Label(main_window, text = "Make a selection: ")
view_inv_button = tk.Button(main_window, text = 'View Inventory', height=10, width = 50, command = main_window.destroy)
add_inv_button = tk.Button(main_window, text = 'Add to Inventory', height=10, width = 50, command = main_window.destroy)
pull_inv_button = tk.Button(main_window, text = 'Pull from Inventory',height=10, width = 50, command = main_window.destroy)

label.grid(row = 0, column = 1)
view_inv_button.grid(row=1, column=0)
add_inv_button.grid(row = 1, column = 1)
pull_inv_button.grid(row = 1, column = 2)

main_window.mainloop()