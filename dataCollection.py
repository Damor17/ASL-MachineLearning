import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300


folder = 'Data/M'
counter = 0




while True:
    success, img = cap.read()

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)

    if key == ord('s'):
        counter += 1 
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', img)
        print(counter)
