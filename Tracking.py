import cv2
import time
import numpy as np
import HModule as htm
import math
from cvzone.SerialModule import SerialObject
from time import sleep
arduino = SerialObject()


#
wcam, hcam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)

detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList)!=0:
        # print(lmList[4], lmList[8])

        x1,y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1),15,(255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1),(x2,y2),(255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        print("Actual")
        print(length)
        normalize = (((length-20)/(250-25))*1000)
        print(normalize)
        print("\n")

        if(normalize>0 and normalize<999):
            arduino.sendData([normalize])



    cv2.imshow("Result",img)
    cv2.waitKey(1)
