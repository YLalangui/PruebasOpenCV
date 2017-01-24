import cv2
import numpy as np

filename = "imagenes/faces.jpg"

def detect(filename):
    # Declaramos una variable face_cascade, el cual es un objeto CascadeClassifier para las caras, y el responsable
    # de la deteccion de caras. El documento haarcascade_... tiene que estar en el mismo lugar que este documento, para
    # asi evitar problemas. Por tanto face_cascade se convierte en un objeto, al cual le podemos aplicar algunas funciones
    # como veremos mas adelante
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    cv2.namedWindow("Faces Detected")
    cv2.imshow("Faces Detected", img)
    cv2.waitKey(0)

detect(filename)