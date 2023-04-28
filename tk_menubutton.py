import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        # change window title
        self.title(string='Tkinter Widgets')

        # window width/height - window.geometry('width x height (+/-)X (+/-)Y')
        width  = 300
        height  = 200

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - width  / 2)
        center_y = int(screen_height / 2 - height  / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{width }x{height }+{center_x}+{center_y}')

        # window resizable behavior - window.resizable(width,height)
        self.resizable(False,False)

        # Changing the default icon
        self.iconbitmap('./assets/icon.ico')


        # self.geometry('300x250')
        # self.title('Menubutton Demo')

        # Menubutton variable
        self.selected_color = tk.StringVar()
        self.selected_color.trace("w", self.menu_item_selected)

        # create the menu button
        self.create_menu_button()

    def menu_item_selected(self, *args):
        """ handle menu selected event """
        self.config(bg=self.selected_color.get())

    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        colors = ('Red', 'Green', 'Blue')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Renk Seçiniz: ')

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for color in colors:
            menu.add_radiobutton(
                label=color,
                value=color,
                variable=self.selected_color)

        # associate menu with the Menubutton
        menu_button["menu"] = menu

        menu_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
