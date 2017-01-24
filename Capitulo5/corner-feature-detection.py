import cv2
import numpy as np

# En este codigo escribiremos un simple algoritmo para la deteccion de esquinas en una imagen a partir
# de la funcion CornerHarris

img = cv2.imread("imagenes/ajedrez.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 23, 0.04)
img[dst>0.01 * dst.max()] = [0,0,255]
while (True):
    cv2.imshow("corners", img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()