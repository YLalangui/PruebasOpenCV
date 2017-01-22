import cv2
import numpy as np
from matplotlib import pyplot as plt

# Para hacer una buena deteccion de bordes primero hay que suavizar la imagen para evitar que
# se confunda el ruido con nuevos bordes, probamos con medianBlur utilizando una matriz de convolucion
# de 3x3 y de 7x7

imagen = cv2.imread("imagenes/images4_21.jpg")
#imagenborrosa7 = cv2.medianBlur(imagen, 7)
imagenborrosa3 = cv2.medianBlur(imagen,3)
#imagenborrosa15 = cv2.medianBlur(imagen,15)
#cv2.imshow("Imagen", imagen)
#cv2.imshow("Imagen borrosa 7", imagenborrosa7)
#cv2.imshow("Imagen borrosa 3", imagenborrosa3)
#cv2.imshow("Imagen borrosa 15", imagenborrosa15)
cv2.waitKey(0)





# Despues de probar varios kernel lo pasamos a blanco y negro, para intensificar mas los contrastes
# Vemos en los parametros de cvtColor que el codigo es para pasar de BGR a blanco y negro
# Utilizamos el laplaciano para bordes completos, sobelx para resaltar los bordes verticales y solbely
# para resaltar los bordes horizaontales, tener cuidado porque no se que pasa que cuando aplico el
# laplaciano aun asi grayImage se torna a laplaciano. Para evitarnos problemas con el laplaciano y el sobel
# utilizaremos la funcion de numpy copy(), asi hacemos una copia de seguridad de la original, guardada en este
# caso en otra variable que es gray

grayImage = cv2.cvtColor(imagenborrosa3, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Imagen B/N", grayImage)
cv2.waitKey(0)





# Aqui unos ejemplos de la utilizacion del laplaciano para conocer los bordes
gray = np.copy(grayImage)
laplacian = cv2.Laplacian(grayImage,cv2.CV_8U, grayImage, 5)
sobelx = cv2.Sobel(grayImage,cv2.CV_8U,1,0,ksize=5)
sobely = cv2.Sobel(gray,cv2.CV_8U,0,1,ksize=5)

cv2.imshow("Original",gray)
cv2.imshow("Laplaciano", laplacian)
cv2.imshow("Sobel", sobelx)

cv2.waitKey(0)
# EL libro dice que un kernel de 7 para el borroso y un kernel de 5 para el laplaciano esta bien

"""
# YA TENEMOS OTRO METODO PARA DETECTAR BORDES, EL LAPLACIANO Y ESTE NO ESTA NADA MAL
Con estos metodos no nos dejan especificar lso kernel que queremos utilizar
"""




