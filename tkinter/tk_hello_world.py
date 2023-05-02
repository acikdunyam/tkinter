import tkinter as tk
from tkinter import ttk

# create window
root = tk.Tk()

# create widget 
label = ttk.Label(
    root,
    text='Hello World'
)
label.pack()

root.mainloop()