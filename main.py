import cv2
import time
import datetime
eye_classifier=cv2.CascadeClassifier("haarcascade_eye.xml")
video=cv2.VideoCapture(0)
import os
import playsound as p
c=1
asd=0
initial=time.time()
while True:
    #capture the first frame
    check,frame=video.read()
    frame = cv2.resize(frame, (600,400))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes=eye_classifier.detectMultiScale(gray,1.3,5)
    #print(len(eyes))
    cv2.imshow('img',frame)
    a = cv2.waitKey(1)
    if(len(eyes)<=1):
        asd=1
        if asd==1:
            timer=int(time.time()-initial+1)
            print(timer)
            if timer>=3:
                print("no eyes")
                with open('eyess.mp3'):
                    p.playsound('eyess.mp3')
                    timer=0
    else:
        initial=time.time()
    if(a==ord('q')):
        break
video.release()
cv2.destroyAllWindows()
