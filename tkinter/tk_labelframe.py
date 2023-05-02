import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()

# change window title
root.title(string='Tkinter Widgets')

# window width/height - window.geometry('width x height (+/-)X (+/-)Y')
width = 300
height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - width / 2)
center_y = int(screen_height / 2 - height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{width }x{height }+{center_x}+{center_y}')

# window resizable behavior - window.resizable(width,height)
root.resizable(False, False)

# Changing the default icon
root.iconbitmap('./assets/icon.ico')

# label frame
label_frame = ttk.LabelFrame(root, text='Hizalama')
label_frame.grid(column=0, row=0, padx=20, pady=20)

alignment_var = tk.StringVar()
alignments = ('Sol', 'Orta', 'Sağ')

# create radio buttons and place them on the label frame
grid_column = 0

for alignment in alignments:
    # create a radio button
    radio = ttk.Radiobutton(label_frame, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid column
    grid_column += 1


root.mainloop()