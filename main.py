import cv2

# import cv2
# import numpy as np # used for working with arrays and structuring datasets
# import os
# from matplotlib import pyplot as plt # for visualising images
# import time # used to take time for each frame
import mediapipe as mp # detecting motion using points
print("file is running")


mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# to detect what was in the webcam
# results will give types of landamrks like face, left/right hand
def mediapipe_detection(image, model):
    # recolour the image to rgb
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False 
    results = model.process(image) # making the prediction
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results


# rendering the landmarks to the frame
def draw_landmarks(image, results):
    # mediapipe function that makes it easy to draw landmarks on the image
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

# changing how the landmarks are drawn
# smaller circles, diff colours, line thickness etc
def draw_styled_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                            #   stylising the landmarks
                                mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                            )
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    
# using openCV to access the webcam _______________________ 
# setup a video capture then looping through the frame -> video
# accessing the webcam and = cap
cap = cv2.VideoCapture(0)

# checking if its opened
if not cap.isOpened():
    print("Cannot open camera")
    exit()

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened(): 
        # read feed
        # frame: image of the webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame. Exiting ...")
            break
        
        # print(f"ret: {ret}")

        # make detections
        image, results = mediapipe_detection(frame, holistic)
        # print(results)
        
        # draw landmarks
        draw_styled_landmarks(image, results)
        
        # showing it to the user
        # OpenCV feed is the name of frame
        cv2.imshow('Webcam', image)

        # if a key is pressed and its q then exit 
        if cv2.waitKey(10) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows() # close down the frame



    # using mediapipe for detection __________________
