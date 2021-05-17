from tkinter import *
from tkinter import filedialog
import cv2
import random

# let's create a display window with tkinter

root = Tk()
root.geometry('1500x900')
root.resizable(0, 0)
blank_space = " "  # empty space
root.title("Face Detection App")
root.configure(bg='grey')


def webcam_detection():
    # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Choose an image to detect faces in
    # img = cv2.imread('HRTS.webp') # this is for image face detection

    # to capture face from webcam
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # iterate forever over frames
    on = True
    while on:
        # read the current frame
        successful_frame_read, frame = webcam.read()

        # Must convert this image to greyscale
        greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in vid
        face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

        d = 0
        # draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 6)
            d += 1

        if d < 1:
            Label(root, text=' No faces detected ', font='helvetica 40', bg='light blue', fg='red').place(
                  x=530, y=500)
        elif d == 1:
            Label(root, text='One face detected', font='helvetica 40', bg='light blue', fg='red').place(
                  x=543, y=500)
        else:
            Label(root, text=f"  {d} faces detected!  ", font='helvetica 40', bg='light blue', fg='red').place(
                  x=530, y=500)

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
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("All files",
                                                      "*.*"),
                                                     ("Text files",
                                                      "*.txt*")))

    # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Choose an image to detect faces in
    img = cv2.imread(filename)  # this is for image face detection

    # This is to detect faces in photo
    greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect the faces
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

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
        Label(root, text=' No faces detected ', font='helvetica 40', bg='light blue', fg='red').place(
            x=530, y=500)
    elif f == 1:
        Label(root, text='One face detected', font='helvetica 40', bg='light blue', fg='red').place(
            x=543, y=500)
    else:
        Label(root, text=f"  {f} faces detected!  ", font='helvetica 40', bg='light blue', fg='red').place(
            x=530, y=500)

    # wait until key is pressed to close window
    cv2.imshow('Photo', img)
    cv2.waitKey()


title_label = Label(root, text='Face Detection AI', font='helvetica 40 bold', bg='grey', fg='light blue').pack()

webcam_btn = Button(root, text='Webcam Face Detection', font='helvetica 20', bg='light green', fg='red', padx=1,
                    command=webcam_detection).place(x=600, y=210)

img_btn = Button(root, text='  Image Face Detection  ', font='helvetica 20', bg='light green', fg='red', padx=1,
                 command=img_detection).place(x=600, y=300)

blank_label = Label(root, text='                                    ')

root.mainloop()
