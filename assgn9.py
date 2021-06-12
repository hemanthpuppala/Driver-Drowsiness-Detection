
import cv2
import datetime

face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_classifier=cv2.CascadeClassifier("haarcascade_eye.xml")
watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')
car_cascade = cv2.CascadeClassifier('cars.xml')
video=cv2.VideoCapture('object.mp4')
phone_cascade=cv2.CascadeClassifier('Phone_Cascade.xml')
wall_cascade=cv2.CascadeClassifier('classifier WallClock.xml')

while True:
    
    check,frame=video.read()
    frame=cv2.resize(frame, (600,600))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    watches = watch_cascade.detectMultiScale(gray, 1.5, 50)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    phones=phone_cascade.detectMultiScale(gray, 3, 9)
    clock=wall_cascade.detectMultiScale(gray, 3, 9)


    print(watches)

    for (px,py,pw,ph) in phones:
        cv2.rectangle(frame, (px,py), (px+pw, py+ph), (255,0,255), 2)
        cv2.imshow('object detection', frame)

    for (bx,by,bw,bh) in clock:
        cv2.rectangle(frame, (bx,by), (bx+bw, by+bh), (255,10,255), 2)
        cv2.imshow('object detection', frame)
    


    for (ax,ay,aw,ah) in watches:
          cv2.circle(frame, (int(ax+ah/2),int(ay+aw/2)), 30, (0,100,255), 2)
          cv2.imshow('object detection', frame)

    for (cx,cy,cw,ch) in cars:
          cv2.rectangle(frame, (cx,cy),(cx+cw,cy+ch),(0,0,255),2)
          
          cv2.imshow('object detection', frame)     
         
          picname=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
          cv2.imwrite(picname+".jpg",frame)
   
    Key=cv2.waitKey(1)
    if Key==ord('q'):
        #release the camera
        video.release()
        #destroy all windows
        cv2.destroyAllWindows()
        break

