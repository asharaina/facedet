from PIL import Image
from io import BytesIO
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image_path = input("Please enter the path to the image file: ")
cap = cv2.VideoCapture(image_path)
ret, image_path = cap.read()
gray = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(image_path, (x,y), (x+w, y+h), (255, 255, 0), 2)

cv2.imshow('img', image_path)
k = cv2.waitKey(0)

cap.release()

cv2.destroyAllWindows()






