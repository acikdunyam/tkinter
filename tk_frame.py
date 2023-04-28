import tkinter as tk
from tkinter import ttk, TclError

'''
    borderwidth	Çerçevenin kenarlık genişliğini belirtin. Varsayılan olarak sıfırdır
    class_	    Widget sınıfı adını ayarla
    cursor	    Fare imleci çerçevenin üzerindeyken imleç görünümünü değiştirin
    height	    Çerçevenin yüksekliğini ayarlayın.
    padding	    Çerçevenin içinde ve içerilen pencere öğelerinin dışında dolgu oluşturmak için.
    relief	    Kenarlık için kabartma stilini belirtin. Etkili hale getirmek için ayrıca borderwidth.
    style	    Özel widget özel stil adını belirtin
    takefocus	Bir boole değeri, odak geçişi sırasında çerçevenin ziyaret edilip edilmediğini belirtir. 
                Varsayılan olarak, False. Bu nedenle, çerçeve widget'ı odağı kabul etmez.
    width	    Çerçevenin genişliğini ayarlayın.
'''


def create_input_frame(root):
    frame = ttk.Frame(root)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(
        frame,
        text='Find what:'
    ).grid(column=0, row=0, sticky=tk.W)

    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(
        column=1,
        row=0,
        sticky=tk.W
    )

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print('{0} -> {1}'.format('Match case', match_case.get()))
    )
    match_case_check.grid(
        column=0,
        row=2,
        sticky=tk.W
    )

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print('{0} -> {1}'.format('Wrap around', wrap_around.get()))
    )
    wrap_around_check.grid(
        column=0,
        row=3,
        sticky=tk.W
    )

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_button_frame(root):
    frame = ttk.Frame(root)
    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def create_main_window():
    
    root = tk.Tk()
    root.title(string='Replace')
    
    width = 450
    height = 150

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{width }x{height }+{center_x}+{center_y}')

    # Changing the default icon
    root.iconbitmap('./assets/replace.ico')
    
    try:
        # windows only (remove the minimize/maximize button)
        # root.attributes('-toolwindow', True)
        pass
    except TclError:
        print('Not supported on your platform')
    
    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    # window resizable behavior - window.resizable(width,height)
    # root.resizable(False, False)
    
    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()
    
if __name__ == '__main__':
    create_main_window()