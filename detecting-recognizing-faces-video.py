import cv2
import numpy as np

def detect(filename):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    gray = cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(np.copy(gray), 1.3, 5)

    x1,y1,w1,h1 = 0,0,0,0
    for (x, y, w, h) in faces:
        cv2.rectangle(filename, (x, y), (x + w, y + h), (255, 0, 0), 2)
        x1 = x
        y1 = y
        w1 = w
        h1 = h
    rect = gray[y1:y1+h1, x1:x1+w1]
    eyes = eye_cascade.detectMultiScale(rect, 1.3, 5, 0, (40, 40))

    for(a, b, c, d) in eyes:
       cv2.rectangle(filename, (a+x1, b+y1), (a+x1 + c, b+y1 + d), (0, 255, 0), 2)


    cv2.imshow("Faces Detected", filename)
    #cv2.imshow("Just Face", rect)


cap = cv2.VideoCapture(0)

while (1):
    ret, frame = cap.read()
    # frame = cv2.medianBlur(frame, 3)
    detect(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

