from tkinter import *  # Source: https://docs.python.org/3/library/tkinter.html
from tkinter import filedialog
import cv2  # Source: https://opencv.org/
import random  # built-in library of python

# defining necessary variables
# Source: https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
path_to_data = 'C:/haarcascade_frontalface_default.xml'  # trained face data we will use
screen_dimensions = '900x700'
screen_bg_color = "#7DCFB6"
button_bg_color = '#D6EDFF'
button_fg_color = '#8B95C9'
title_bg_color = '#7DCFB6'
title_fg_color = '#478978'
label_font = 'helvetica 40'

# creating a display window with tkinter
root = Tk()
root.geometry(screen_dimensions)
root.resizable(0, 0)
blank_space = " "  # empty space
root.title("Face Detection App")
root.configure(bg=screen_bg_color)


def webcam_detection():
    # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier(path_to_data)

    # to capture face from webcam
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # iterate forever over frames
    on = True
    while on:
        # read the current frame
        successful_frame_read, frame = webcam.read()

        # Must convert this image to greyscale
        grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in vid
        face_coordinates = trained_face_data.detectMultiScale(grey_img)

        d = 0

        # draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 6)
            d += 1

        if d < 1:
            Label(root, text=' No faces detected ', font='helvetica 40', bg='#ACD7EC', fg='red', padx=2).place(
                x=230, y=500)
        elif d == 1:
            Label(root, text=' One face detected ', font='helvetica 40', bg='#ACD7EC', fg='red', padx=2).place(
                x=230, y=500)
        else:
            Label(root, text=f"  {d} faces detected!  ", font='helvetica 40', bg='#ACD7EC', fg='red, padx=2').place(
                x=230, y=500)

        # this shows our webcam on the screen
        # key = cv2... is for waiting until a key is pressed to quit the program
        # if the key == 27 or 'esc', quit the program
        cv2.imshow('Face Detection AI', frame)
        key = cv2.waitKey(1)

        if key == 27:
            on = False
            cv2.destroyAllWindows()


def img_detection():
    # this asks what file to open
    filename = filedialog.askopenfilename(initialdir="/Pictures",
                                          title="Select Image File",
                                          filetypes=(("Image files",
                                                      "*.jpg*"),
                                                     ("All files",
                                                      "*.*"),
                                                     ("Text files",
                                                      "*.txt*")))

    # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier(path_to_data)

    # this lets us choose an image to detect faces in
    img = cv2.imread(filename)  # this is for image face detection

    # This is to detect faces in the photo; we need to convert RGB to black/white
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect the faces
    face_coordinates = trained_face_data.detectMultiScale(grey_img)

    # draw rectangles around the faces
    # 'f' variable is for number of faces
    f = 0
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (random.randint(180, 255), random.randint(180, 255),
                                                    random.randint(180, 255)), 6)
        # for each face detected, f is incremented by 1
        f += 1

    # this block of code prints how many faces were detected and displays the result
    if f < 1:
        Label(root, text=' No faces detected! ', font=label_font, bg='#ACD7EC', fg='red', padx=2).place(
            x=230, y=500)
    elif f == 1:
        Label(root, text=' One face detected ', font=label_font, bg='#ACD7EC', fg='red', padx=2).place(
            x=230, y=500)
    else:
        Label(root, text=f"  {f} faces detected!  ", font=label_font, bg='#ACD7EC', fg='red', padx=2).place(
            x=230, y=500)

    # wait until key is pressed to close window
    cv2.imshow('Photo', img)
    cv2.waitKey()


#  the 'on_enter' and 'on_leave' functions for both buttons have the button change colors once hovered over.
def on_enter_webcam(e):
    webcam_btn.config(background=button_fg_color, foreground=button_bg_color)


def on_leave_webcam(e):
    webcam_btn.config(background=button_bg_color, foreground=button_fg_color)


def on_enter_image(e):
    img_btn.config(background=button_fg_color, foreground=button_bg_color)


def on_leave_image(e):
    img_btn.config(background=button_bg_color, foreground=button_fg_color)


title_label = Label(root, text='Face Detection AI', font='Cambria 50 italic bold',
                    bg=title_bg_color, fg=title_fg_color)
title_label.pack()

# when clicked on the webcam button, it initiates the 'webcam_detection' function
webcam_btn = Button(root, text='Webcam Face Detection', font='Arial 20 bold',
                    bg=button_bg_color, fg=button_fg_color, padx=2,
                    pady=2, command=webcam_detection)

webcam_btn.place(x=289, y=210)

webcam_btn.bind('<Enter>', on_enter_webcam)
webcam_btn.bind('<Leave>', on_leave_webcam)

# when clicked on the image button, it initiates the 'img_detection' function
img_btn = Button(root, text='  Image Face Detection  ', font='Arial 20 bold',
                 bg=button_bg_color, fg=button_fg_color, padx=2,
                 pady=2, command=img_detection)

img_btn.place(x=289, y=330)

img_btn.bind('<Enter>', on_enter_image)
img_btn.bind('<Leave>', on_leave_image)

blank_label = Label(root, text='                                   ')

root.mainloop()
# end
