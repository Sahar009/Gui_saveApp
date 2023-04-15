import tkinter
import customtkinter
from pytube import YouTube
#  library for downloadeing

def Download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print('link invalid')
    print('download complete')


customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# app frame

app = customtkinter.CTk()
app.geometry('750x480')
app.title('All Video Downloader')


#  adding UI Element 
title = customtkinter.CTkLabel(app, text='Insert a youtube Link')
title.pack(padx=10, pady=10)

# link input 2
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350,height=50, textvariable=url_var ,text_color='red',placeholder_text='insert link',placeholder_text_color='black')

link.pack()


# download

download =customtkinter.CTkButton(app, text='Download now', command=Download)

download.pack(padx= 10, pady=10)
# run app
app.mainloop()
