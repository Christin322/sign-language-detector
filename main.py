import cv2
import numpy as np # used for working with arrays and structuring datasets
import os
from matplotlib import pyplot as plt # for visualising images
import time # used to take time for each frame
import mediapipe as mp # detecting motion using points

# using openCV to access the webcam
# setup a video capture then looping through the frame -> video

# accessing the webcam and = cap
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Webcam not found or cannot be opened.")
    
    
while cap.isOpened(): # while the video source is opened
    # read feed
    # frame: image of the webcam
    ret, frame = cap.read()
    
    # showing it to the user
    # OpenCV feed is the name of frame
    cv2.imshow('OpenCV Feed', frame)
    
    # if a key is pressed and its q then exit 
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() # releasing the webcam 
cv2.destroyAllWindows() # close down the frame

# using mediapipe for detection
