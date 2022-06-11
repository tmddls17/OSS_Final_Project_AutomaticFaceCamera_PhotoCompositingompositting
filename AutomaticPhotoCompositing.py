
import cv2
import time
 
font = cv2.FONT_ITALIC
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "./haarcascade_frontalface_default.xml")

def faceDetect():
    eye_detect = False
 
    try:
        cam = cv2.VideoCapture(0)
    except:
        print("camera loading error")
        return
 
    while True:
        ret, frame = cam.read()
        if not ret:
            break
 
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3, 5)
        
        for(x,y, w,h) in faces:
            roi = frame[y+15:y+h-5, x+20:x+w-20]
            cv2.imwrite('face.jpg',roi)
            cam.release()
            cv2.destroyAllWindows()
            return
            
        cv2.imshow("frame", frame)
        
        k=cv2.waitKey(30)
        if(k == 27):
            exit()
    
    
def combine():
    src1 = cv2.imread('face.jpg')
    src2 = cv2.imread('background.jpg')
    
    cv2.imshow('source 1',src1)
    cv2.imshow('source 2',src2)
    
    gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3, 5)
    
    height, width, channel = src1.shape
    
    x1, y1 = 0, 0    
    for(x,y,w,h) in faces:
        cv2.rectangle(src2, (x,y), (x+width, y+height), (0,0,0), -1)
        src2[y:y+height, x:x+width] = src1
        x1, y1 = x, y
        
    cv2.imshow('result',src2)
    
    while True:
        input = cv2.waitKey(30)

        if(input == 27):
            cv2.imwrite('result.jpg',src2)
            cv2.destroyAllWindows()
            exit()
        elif(input == 117):
            src2 = cv2.imread('background.jpg')
            src1 = cv2.resize(src1, None, fx=1.05, fy=1.05)
            height, width, channel = src1.shape
            src2[y1:y1+height, x1:x1+width] = src1
        elif(input == 100):
            src2 = cv2.imread('background.jpg')
            src1 = cv2.resize(src1, None, fx=0.95, fy=0.95)
            height, width, channel = src1.shape
            src2[y1:y1+height, x1:x1+width] = src1
        elif(input == 114):
            faceDetect()
            src1 = cv2.imread('face.jpg')
            src2 = cv2.imread('background.jpg')
            height, width, channel = src1.shape
            src2[y1:y1+height, x1:x1+width] = src1
        elif(input == 106):
            src2 = cv2.imread('background.jpg')
            height, width, channel = src1.shape
            x1 = x1 - 2
            src2[y1:y1+height, x1:x1+width] = src1
        elif(input == 108):
            src2 = cv2.imread('background.jpg')
            x1 = x1 + 2
            height, width, channel = src1.shape
            src2[y1:y1+height, x1:x1+width] = src1
        elif(input == 105):
            src2 = cv2.imread('background.jpg')
            y1 = y1 - 2
            height, width, channel = src1.shape
            src2[y1:y1+height, x1:x1+width] = src1
        elif(input == 107):
            src2 = cv2.imread('background.jpg')
            y1 = y1 + 2
            height, width, channel = src1.shape
            src2[y1:y1+height, x1:x1+width] = src1
        cv2.imshow('result',src2)
        

faceDetect()
combine()
