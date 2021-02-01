import cv2
from PIL import ImageGrab
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    screen = np.array(ImageGrab.grab(bbox=(0,0,1500,1000)))

    # Convert to grayscale
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(screen, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', screen)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()