import tkinter as tk
from tkinter import ttk, messagebox

# create window
root = tk.Tk()

# change window title
root.title(string='Tkinter Window - Center')

# window width/height - window.geometry('width x height (+/-)X (+/-)Y')
width  = 300
height  = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - width  / 2)
center_y = int(screen_height / 2 - height  / 2)

# set the position of the window to the center of the screen
root.geometry(f'{width }x{height }+{center_x}+{center_y}')

# window resizable behavior - window.resizable(width,height)
root.resizable(False,False)

# Changing the default icon
root.iconbitmap('./assets/icon.ico')

#  window transparency - 0.0 (fully transparent) to 1.0 (fully opaque)
root.attributes('-alpha',1.0)

# Window stacking order
root.attributes('-topmost', 1)

root.mainloop()