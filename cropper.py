import numpy as np
import cv2
import imutils
import os

face_cascade = cv2.CascadeClassifier('C:/opencv/haarcascade_frontalface_default.xml')
image_path='C:\\Users\\HP\\Desktop\\MEDIA\\pictures\\photo.jpg'
img = cv2.imread(image_path,0)

img = imutils.resize(img, width=1000)
faces = face_cascade.detectMultiScale(img, 1.22,3)
i=0
for (x,y,w,h) in faces:
    gray = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    crop_image = gray[y:y+h, x:x+w]
    fname,ext =os.path.splitext(image_path)
    cv2.imwrite(fname+"_crop_"+str(i)+ext,crop_image)
    i=i+1
cv2.imshow('img',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
print("Done")
