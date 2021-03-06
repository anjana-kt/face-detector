import cv2
import dlib
import time

t1,t2=0,0
l=0
flag=0
idp = 0
data =[]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)


while True:
    _, img = cap.read()

    if not _:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        #cv2.ellipse(img, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if len(faces) !=0 and flag==0: 
            flag=1
            t1 = time.time()

    elif len(faces)==0 and flag!=0:
            idp+=1
            flag=0
            t2=time.time()
            data.append([idp,t2-t1])
            print(data)
            
        
    cv2.imshow('img', img)

 
    k = cv2.waitKey(30) & 0xff
    if k==27:
        l=len(faces)
        break

if l!=0 and flag!=0:
            idp+=1
            t2=time.time()
            data.append([idp,t2-t1])
            print(data)       

cap.release()
