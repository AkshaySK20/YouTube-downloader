import tkinter
import customtkinter
from pytube import YouTube
import threading
import time

def download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Finished Downloading!")

    except:
        finishLabel.configure(text="Error! YouTube link is Invalid.", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded/total_size * 100
    per = str(int(percentage_of_completion))
    progPercentage.configure(text=per +'%')
    progPercentage.update()

    # update progressbar
    progressBar.set(float(percentage_of_completion)/100)


# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link here:")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Bar
progPercentage = customtkinter.CTkLabel(app, text="0%")
progPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=download)
download.pack(padx=10, pady=10)


# Run app
app.mainloop()


