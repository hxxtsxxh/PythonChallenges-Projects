# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def widgets():
    link_label = Label(root,
                       text="YouTube link  :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_Link)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2,
                              column=1,
                              pady=5,
                              padx=5)

    browse_b = Button(root,
                      text="Browse",
                      command=browse,
                      width=10,
                      bg="#05E8E0")
    browse_b.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)

    download_b = Button(root,
                        text="Download",
                        command=download,
                        width=20,
                        bg="#05E8E0")
    download_b.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)


# Defining Browse() to select a
# destination folder to save the video

def browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_directory)


# Defining Download() to download the video
def download():
    # getting user-input Youtube Link
    youtube_link = video_Link.get()

    # select the optimal location for
    # saving file's
    download_folder = download_Path.get()

    # Creating object of YouTube()
    getvideo = YouTube(youtube_link)

    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videostream = getvideo.streams.first()

    # Downloading the video to destination
    # directory
    videostream.download(download_folder)

    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_folder)


# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("600x120")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the widgets() function
widgets()

# Defining infinite loop to run
# application
root.mainloop()
