import cv2
import numpy as np

planets = cv2.imread("imagenes/planetas1.jpg")
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
# En las imagenes es interesante hacer un emborronado para evitar posibles ruidos en la imagen
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#img_canny = cv2.Canny(img,50,150, apertureSize = 3)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, 120, param1=100, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(planets, (i[0], i[1]), i[2], (0,255,0), 2)
    cv2.circle(planets, (i[0], i[1]), 2, (0,0,255), 3)

cv2.imshow("HoughCircles", planets)
cv2.waitKey(0)

"""
AQUI TENEMOS LA DETECCION DE CIRCULOS MEDIANTE HOUGH, MEJOR NO HACER CANNY, MEJOR COLO UTILIZAR LA IMAGEN EN BLANCO Y
NEGRO:


SI QUEREMOS DETECTAR UNA IMAGEN QUE CONTIENE POLIGONOS, ENTONCES SERA MEJOR DETECTADO USANDO LA COMBINACION DEL USO
DE CV2.FINDCONTOURS Y CV2.APPROXPOLYDP
"""