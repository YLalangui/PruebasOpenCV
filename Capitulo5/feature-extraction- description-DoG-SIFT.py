import cv2
import sys
import numpy as np

img = cv2.imread("imagenes/italia.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Creamos un objeto SIFT y calculamos la imagen de blanco y negro
# ESte es un proceso interesante e importante, el objeto SIFT usa DoG (Difference of Gaussians) para detectar puntos
# de interes (keypoints) y calcula un vector caracteristico alrededor de cada region (punto) de interes. Como el nombre
# del metodo claramente lo dice, hay dos operaciones principales que se tienen que llevar a cabo: deteccion y calculo.
# Lo que devuelve esta funcion es una array que contiene informacion de los puntos de interes(keypoints) y el descriptor

sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, flags=4,
                        color=(51,163,236))
cv2.imshow('sift_keypoints', img)
while (True):
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()