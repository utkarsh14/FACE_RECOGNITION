import cv2
import os

def facecrop(image,j):
    facedata = "C:/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml"#cascade location
    cascade = cv2.CascadeClassifier(facedata)
    img = cv2.imread(image,0)
    faces = cascade.detectMultiScale(img)
    i=0
    for f in faces:
       x, y, w, h = [ v for v in f ]
       cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))
       sub_face = img[y:y+h, x:x+w]
       fname,ext= os.path.splitext(image)
       i=i+1
       cv2.imwrite("F:\\SAMPLES\\IMAGES\\"+"photo"+str(i+j)+ext, sub_face) #destination address
       print(i+j)
    return i
def crop_all(path):
    j=0
    for folderName, subfolders, filenames in os.walk(path): #os.walk cycles through each file present in folder
        for filename in filenames:
            k=facecrop(folderName+'\\'+filename,j)
            j=j+k
            
crop_all("F:\\photos\\TOUR") #SOURCE ADDRESS
