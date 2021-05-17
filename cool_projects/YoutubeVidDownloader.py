from tkinter import *
from pytube import YouTube
from tkinter import filedialog

# create a display window with tkinter
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
blank_space = " "  # One empty space
root.title(45 * blank_space + "Youtube Video Downloader")  # Easier to add the blank space
root.configure(bg='navy blue')

Label(root, text='Youtube Video Downloader', font='arial 20 bold', bg='navy blue', fg='white').pack()

# enter link
link = StringVar()
Label(root, text='Paste Link Here: ', font='arial 15 bold', bg='navy blue', fg='light pink').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link,
                   fg='blue', highlightcolor='red', highlightbackground='black',
                   highlightthickness='2').place(x=32, y=100)


# download video function
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    Label(root, text='Title: ' + url.title + f' ({url.length} sec)', font='arial 10 bold', bg='navy blue',
          fg='yellow').place(x=0, y=270)

    path = filedialog.askdirectory()
    if len(path) < 1:
        Label(root, text='File is Unsaved!', font='arial 23 bold', bg='navy blue', fg='red').place(x=127, y=210)
    else:
        video.download(path)
        Label(root, text='Saved!', font='arial 23 bold', bg='navy blue', fg='light green').place(x=185, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='black', fg='red', padx=1, command=downloader).place(x=174,
                                                                                                            y=150)
root.mainloop()

