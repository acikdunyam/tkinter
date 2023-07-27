from tkinter import *
import os, openai, customtkinter, pickle

# Genel ayarlar
root = customtkinter.CTk()
root.title('ChatGPT Bot')
root.geometry('600x480')
root.iconbitmap('./icon/ai_lt.ico')

# Renklendirme Özellikleri
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

# Fonksiyolar
def speak():
    if chat_entry.get():
        file_name = './api/api_key'  
        try:  
            if os.path.isfile(file_name):
                input_file = open(file_name, 'rb')
                api_entry.delete(0,END) 
                api_sifre = pickle.load(input_file)
                #my_text.insert(END, "\nÇalışıyor..")
                openai.api_key= api_sifre
                openai.Model.list()

                cevap = openai.Completion.create(
                    model ="text-davinci-003",
                    prompt = chat_entry.get(),
                    temperature=0,
                    max_tokens=4000,
                    top_p = 1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                my_text.insert(END, (cevap["choices"][0]["text"]).strip())
                my_text.insert(END, "\n")

            else:
                input_file=open(file_name, 'wb')
                input_file.close() 
                my_text.insert(END, "\nApi key almayı unuttun. Lütfen aşağıdaki sayfadan temin et!")
        except Exception as ex:
            my_text.insert(END, f"\nBir hata oluştu: {ex}") 
    else:
        my_text.insert(END, "\nHey dostum soru sormayı unuttun.")

def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)

def key():
    file_name = './api/api_key'  
    try:  
        if os.path.isfile(file_name):
            input_file = open(file_name, 'rb')
            api_entry.delete(0,END) 
            api_sifre = pickle.load(input_file)
            api_entry.insert(END, api_sifre)
        else:
            input_file=open(file_name, 'wb')
            input_file.close() 
    except Exception as ex:
        my_text.insert(END, f"\nBir hata oluştu: {ex}")   
        
    root.geometry('600x580')
    api_frame.pack(pady=10)

def save_key():
    file_name = './api/api_key'
    
    try:
        output_file = open(file_name, 'wb')
        pickle.dump(api_entry.get(), output_file)    
        api_entry.delete(0,END)    
        api_frame.pack_forget()
    except Exception as ex:
        my_text.insert(END, f"\nBir hata oluştu: {ex}")
        
    root.geometry('600x480')

# Text frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

my_text = Text(text_frame, width=65, bd=1, relief='flat', wrap=WORD)#, selectbackground='#1f538d')
my_text.grid(row=0, column=0)

# scrollbar
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0,column=1, sticky='ns')

my_text.configure(yscrollcommand=text_scroll.set)

# Entry
chat_entry = customtkinter.CTkEntry(root, placeholder_text='ChatGPT Bot\'a ne sormak istersiniz?', width=495, height=50, border_width=1)
chat_entry.pack(pady=10)

# Button Frame
button_frame = customtkinter.CTkFrame(root, border_width=0)
button_frame.pack(pady=10)

# Api button
submit_button = customtkinter.CTkButton(button_frame, text='ChatGPT\'ye Sor', command=speak)
submit_button.grid(row=0, column=0, padx=20)

clear_button = customtkinter.CTkButton(button_frame, text='Ekranı Temizle', command=clear)
clear_button.grid(row=0, column=1, padx=20)

api_button = customtkinter.CTkButton(button_frame, text='Api Key güncelle', command=key)
api_button.grid(row=0, column=2, padx=20)

# Api key frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=10)

api_entry = customtkinter.CTkEntry(api_frame, placeholder_text='Yeni api key giriniz!', width=300, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

api_save_button = customtkinter.CTkButton(api_frame, text='Key kaydet', command=save_key)
api_save_button.grid(row=0, column=1, padx=10)


root.mainloop()