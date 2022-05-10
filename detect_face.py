import cv2
import dlib
import time

def detect_a_face ():
        t1=0   
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        b=False
        while True :
                _, img = cap.read()
                
                if not _:
                        print("Can't receive frame. Exiting ...")
                        break

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
                for (x, y, w, h) in faces:
                        #cv2.ellipse(img, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
                        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                if len(faces) !=0 : 
                        t1 = time.ctime()
                        print("Face found at time : "+str(t1))
                        b=True
                        return b

                k = cv2.waitKey(30) & 0xff
                if k==27:
                        return b
                        
                cv2.imshow('img', img)

        cap.release()
                
k=(detect_a_face())               
print(str(k))
