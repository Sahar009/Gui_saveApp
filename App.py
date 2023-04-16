import tkinter
import customtkinter
from pytube import YouTube

#  library for downloadeing

def Download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color='blue')
        finishlabel.configure(text='')
        video.download()
        finishlabel.configure(text='download complete!')
    except:
        finishlabel.configure(text='invalid tTube link', text_color ='red')
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_complete = bytes_downloaded / total_size * 100
    # print(percentage_complete)
    per = str(int(percentage_complete))
    progress_per.configure(text=per + '% ')
    progress_per.update()

    # progressbar update
    progress_bar.set(float(percentage_complete)/ 100)


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

# finish downloading
finishlabel = customtkinter.CTkLabel(app, text='')
finishlabel.pack()

# progress bar
progress_per = customtkinter.CTkLabel(app, text = '0%')
progress_per.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=350)
progress_bar.set(0)
progress_bar.pack(padx=10,pady=10)

# run app
app.mainloop()
