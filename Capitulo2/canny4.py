import cv2
import numpy as np

# Vamos a usar un algoritmo para deteccion de bordes hecha por John F. Canny

img = cv2.imread("imagenes/images4_21.jpg",0)
# tener cuidado con el imread, si directamtente despues del nombre de la imagen le ponemos un 0 este ya sera
# de por si en blanco y negro
# COn el 0 puesto en la funcion imread no hace falta que hagamos un cambio de color a blanco y negro, el propio 0
# de la funcion imread ya hace ese trabajo, codigo que nos ahorramos
cv2.imshow("Ventana", img)
cv2.waitKey(0)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("canny.jpg", cv2.Canny(img, 200,300))
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()

"""
# COmo ensenanza de por vida tenemos que tener en cuenta que siempre que queramos detectar bordes en las imagenes
# tendremos que primero pasarlos a blanco y negro, y esto se puede hacer directamente en la funcion de imread, con el
# 0 o con la funcion de cv2.cvtColor
"""