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

# Entry
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    messagebox.showinfo(
        title='Information',
        message=msg
    )

# Sign in frame
signin = ttk.Frame(root)
signin.pack(
    padx=10,
    pady=10,
    fill='x',
    expand=True
)

# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()