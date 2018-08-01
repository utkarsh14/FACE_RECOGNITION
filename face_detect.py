import numpy as np
import cv2
import imutils
face_cascade = cv2.CascadeClassifier('C:/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/opencv-master/data/haarcascades/haarcascade_eye.xml')

img = cv2.imread('C:\\Users\\Utkarsh\\Desktop\\New folder\\photo5.jpg')

img = imutils.resize(img, width=1000)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.22,3)
for (x,y,w,h) in faces:
    gray = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
k = cv2.waitKey(0)
print("yo")
cv2.destroyAllWindows()
print("Done")
