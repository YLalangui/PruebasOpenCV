import cv2
import cv
import numpy as np

# En esta ocasion en vez de detectar la imagen mediante cuadrados o circulos vamos a aproximar nuestro contorno a
# poligonos, con lineas rectas, pues sera de vital importancia en procesos de vision, pues tendremos formas poligonales
# para representar un solo objeto

img = cv2.imread("imagenes/figura.jpg")
imgCopia1 = np.copy(img)
imgCopia2 = np.copy(img)

ret, thresh = cv2.threshold(cv2.cvtColor(np.copy(img),cv2.COLOR_BGR2GRAY),127, 255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Algoritmo para encontrar el contorno con el area mas grande, primero creamos un array llamado area y hacemos un bucle
# for para que vaya recorriendo cada uno de los contornos y calculando su area y guardarlo en ese array que hemos
# llamado area. Luego obtenemos el indice de la posicion dentro del array area del elemento mas grande (del area mas
# grande) y lo guardamos en la variable indice_max. Luego el contorno especifico que nos interesa es contours[indice_max]
# y a ese unico contorno que es el que nos interesa por tener el area mas grande lo llamaremos cnt_max
area = [cv2.contourArea(c) for c in contours]
indice_max = np.argmax(area)
cnt_max = contours[indice_max]

# Vamos a utilizar una nueva funcion denominada cv2.aproxPolyDP, para aproximar nuestro contorno a un poligono, este
# tiene 3 parametros, lo primero es el contorno a aproximar, luego un epsilon, que es un valor de referencia que
# tendra la funcion para calcular la funcion pologonal, que lo calcularemos en la siguiente linea de codigo y el ultimo
# una bandera booelana significando que el poligono este cerrado.
# Siendo el epsilon un valor de referencia vamos a calcularlo mediante otra funcion que es cv2.arcLength

epsilon = 0.01*cv2.arcLength(cnt_max, True)
approx = cv2.approxPolyDP(cnt_max, epsilon, True)

# POr tanto estamos diciendo a opencv de calcular un poligono aproximado cuyo perimetro puede solo difeir del contorno
# original en un radio epsilon

# Esta ultima funcion es para formar un poligono (no tan recto) que rodee a toda figura
hull = cv2.convexHull(cnt_max)

# La unica forma de anadir contornos a una imagen es mediante la funcion cv2.drawContours, ya que ni hull ni approx
# son imagenes en si, sino que son simplemente pares de puntos que estan dentro de un array
cv2.drawContours(img, [approx], 0, (0,255,0), 2)
cv2.drawContours(img, [hull], 0, (0,0,255), 2)
cv2.drawContours(img, contours, -1, (255,0,0), 2)
cv2.imshow("poligono", img)
cv2.waitKey(0)

