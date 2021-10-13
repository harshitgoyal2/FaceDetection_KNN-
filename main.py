import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier

cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()
    if ret:
        cv2.imshow("My Camera",image)
    key = cv2.waitKey(50)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("myimage.png", image)

