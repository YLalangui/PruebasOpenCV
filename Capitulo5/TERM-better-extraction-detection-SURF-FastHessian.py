import cv2
import sys
import numpy as np

# LA imagen final se obtiene procesando con un algoritmo SURF usando un umbral Hessiano de 8000
# Tanto el algoritmo de SIFT como el SURF no detectan Keypoint, pero si detecta regiones que se diferencian de su
# alrededor (blobs). EStos son independientes del tamano de la imagen, pero por ejemplo el algoritmo de HArris si
# depende del tamaño de la imagen y ademas detecta esquinas donde antes no habia al cambiar la escala de la imagen
# ESTE CODIGO SE PUEDE EJECUTAR DESDE LA TERMINAL: > python3.5 TERM-better-extraction-detection-SURF-FastHessian
# imagenes/italia.jpg SURF 8000
# CUando mas grande sea el umbral (8000) menos puntos de interes se detectaran
# ES MEJOR EL SURF
imgpath = sys.argv[1]
img = cv2.imread(imgpath)
alg = sys.argv[2]

def fd(algorithm):
    if algorithm == "SIFT":
        return cv2.xfeatures2d.SIFT_create()
    if algorithm == "SURF":
        return cv2.xfeatures2d.SURF_create(float(sys.argv[3]) if len(sys.argv) == 4 else 4000)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fd_alg = fd(alg)
keypoints, descriptor= fd_alg.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, flags=4, color=(51, 163, 236))

cv2.imshow("Keypoints", img)
while (True):
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()
