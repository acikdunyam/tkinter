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

# checkbox
kabul_et = tk.StringVar()

def check_changed():
    messagebox.showinfo(
        title='Sonuç',
        message=kabul_et.get()
    )

checkbox = ttk.Checkbutton(
    root,
    text='Kabul ediyorum.',
    command=check_changed,
    variable=kabul_et,
    onvalue='evet',
    offvalue='hayır'
)
checkbox.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()