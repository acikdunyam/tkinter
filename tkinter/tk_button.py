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

# callback
def callback():
    messagebox.showinfo(
        title='Bilgi',
        message='Butona tıklandı ..'
    )

demo_button = ttk.Button(
    root,
    text='Button',
    command=callback,
)
demo_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# exit
exit_icon = tk.PhotoImage(file='./assets/exit.png')

exit_button = ttk.Button(
    root,
    text='Exit',
    image=exit_icon,
    compound=tk.LEFT,
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# download button
def download_clicked():
    messagebox.showinfo(
        title='İnformation',
        message='Download button clicked!'
    )

download_icon = tk.PhotoImage(file='./assets/download.png')

download_button = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)
download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
