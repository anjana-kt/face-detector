import cv2
import dlib
import time

def detect_a_face ():
        t1,t2=0,0     
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)


        while True :
                _, img = cap.read()

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                for (x, y, w, h) in faces:
                        #cv2.ellipse(img, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
                        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                if len(faces) !=0 : 
                        t1 = time.time()
                        return True

                        
                cv2.imshow('img', img)

                cap.release()

print(detect_a_face())
