"""

This is a basic program that detects face in webcam and then displays detection on screen

"""

import cv2
import random

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('HRTS.webp') # this is for image face detection

# to capture face from webcam
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# iterate forever over frames
while True:
    # read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert this image to greyscale
    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in vid
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

    # draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (random.randint(175, 255), random.randint(175, 255),
                                                      random.randint(175, 255)), 6)

    # this shows our webcam on the screen
    # key = cv2... is for waiting until a key is pressed to quit the program
    # if the key == 27 or 'esc', quit the program
    cv2.imshow('Face Detection AI', frame)
    key = cv2.waitKey(1)

    if key == 27:
        quit()

# """

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
# trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('HRTS.webp') # this is for image face detection
# This is to detect faces in photo

# # detect the faces
# face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)
#
# # draw rectangles around the faces
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (random.randint(175, 255), random.randint(175, 255),
#                                                 random.randint(175, 255)), 6)
#
# print(face_coordinates)
# # Draw rectangles around the faces
#
# # wait until key is pressed to close window
# cv2.imshow('Photo', img)
# cv2.waitKey()


# """
