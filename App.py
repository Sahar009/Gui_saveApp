import tkinter
import customtkinter
from pytube import YouTube
#  library for downloadeing

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# app frame

app = customtkinter.CTk()
app.geometry('750 x 480')
app.title('All Video Downloader')


#  adding UI Element 
title = customtkinter.CTkLabel(app, text='Insert a youtube Link')
title.pack(padx=10, pady=10)

# link input 
link = customtkinter.CTkEntry(app, width=350,height=50)

link.pack()
# run app
app.mainloop()
