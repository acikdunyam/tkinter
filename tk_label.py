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

'''
    anchor			When the text and/or image are smaller than the width, the anchor option determines 
                    where to position them tk.W, tk.CENTER or tk.E for left, center, and right alignment respectively.
    background		Set the background color for the label
    borderwidth		Add a border around the label.
    class_			Specify a custom widget class name for changing the label’s appearance.
    compound		Specify how to display both text and image on the Label.
    cursor			Specify the mouse cursor’s appearance when the mouse is over the widget.
    font			Specify the font style for displaying text
    foreground		Specify the color of the text
    image			Specify an image or images to show in addition to text or instead of text.
    justify			If the text contains newline characters, the justify option specifies how each line is positioned horizontally.
                    The valid values are tk.LEFT (left-justify), tk.CENTER (center), and tk.RIGHT (right-justify).
    padding			Add more space around the label.
    relief			Use this option to create an effect for the Label .e.g, flat, raised, sunken, groove, and ridge.
    style			Specify the custom widget style.
    takefocus		is a boolean value that specifies whether the label is visited during focus traversal. It defaults to False which doesn’t get focus.
    text			Specify a string of text to show in the widget
    textvariable	A StringVar instance that holds the text value of the widget. It overrides the text option if both textvariable and text are available.
    underline		Specify the position of the letter that should be underlined e.g, underline = 0 would underline the letter E in the text='Exit'
    width			Specify the number of characters to show
    wraplength		Chop the text into the lines which less than the length specified by the wraplength option.
'''

label = tk.Label(
    root,
    text='This is a label',
    font=("Helvetica", 14)
)
label.pack(
    ipadx=10,
    ipady=10
)

# display an image label
photo = tk.PhotoImage(file='./assets/python.png')

image_label = ttk.Label(
    root,
    image=photo,
    padding=5
)
image_label.pack()

root.mainloop()
