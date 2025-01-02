"""
This project uses the Gentle AdaBoost frontal face detector (20x20 tree-based) created by Rainer Lienhart,
integrated into the Open Source Computer Vision Library (OpenCV).

Intel License Agreement
For Open Source Computer Vision Library

 Copyright (C) 2000, Intel Corporation, all rights reserved.
"""

import cv2

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('/Users/mani/Documents/Python Greenoly/open cv/Object Detection/haarcascade_frontalface_alt2.xml')  # path to the classifier

# Open the webcam 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using the classifier
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=8, minSize=(40, 40))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.putText(frame, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.putText(frame, 'Press ESC to Exit...', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 200), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if the 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()

