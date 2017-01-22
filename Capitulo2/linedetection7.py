import cv2
import numpy as np

# Para le deteccion de lineas utilizaremos una funcion que se llama cv2.HoughLinesP, y esta version probabilistica esta
# muy bien porque sol oanaliza un conjunto de puntos y estima la probabilidad de que esos puntos pertenezcan todas ellas
# a la misma linea. Esta implementacion es una version optimizada de la tranformada estandar de Hough

img = cv2.imread("imagenes/sudoku.jpg")
# SIEMPRE PASARLO A BLANCO Y NEGRO, PARA LOS BORDES NO HACE FALTA EL UMBRAL, PERO EN LOS CONTORNOS SI
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayCopia = np.copy(gray)
# Utilizaremos la mejor tecnica para la deteccion de bordes, y esa es la de canny
# ESTA FUNCION DE CANNY PARA DETECCION DE BORDES (NO DE CONTORNOS) SI QUE DEVUELVE UNA IMAGEN, POR TANTO NO HARA
# FALTA UTILIZAR LA FUNCION CV2.DRAWCONTOUR, PUES CANNY DEVUELVE UNA IMAGEN CON LOS BORDES, NO UN CONTORNO
edges = cv2.Canny(gray,50,150, apertureSize = 3)
# Mejor en el metodo de canny usar numeros bajitos, como por ejemplo 50:120

"""
PRUEBA CON LA FUNCION DE CANNY CON NUMEROS MAS GRANDES Y DE MAYOR DIFERENCIA
edges200300 = cv2.Canny(grayCopia, 200,300)

cv2.imshow("edges50", edges50120)
cv2.imshow("edges200", edges200300)
cv2.waitKey(0)
"""
minLineLength = 100
maxLineGap = 10

# Uso de la funcion cv2.HoughLinesP
# lines sera un array de 4 valores por cada fila
# TAmbien interesante ver la funcion cv2.HoughLines, sin la p del final
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100,minLineLength, maxLineGap)
# A lo mejor se pone el 0 porque seran lineas de una sola dimension
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey(0)

"""
LO importante en esta deteccion de lineas, aparte de la funcion, es la definicion de longitud minima de linea (minimun
line length (lineas mas cortas no son tomadas en cuenta) y el hueco maximo de linea (maximun line gap), el cual es el
tamano maximo del hueco en una linea antes de que dos segmentos empiecen a considerarse como lineas separadas.
VEr que para la deteccion de lineas se ha hecho la funcion de cv2.Canny, esta se usa porque es la mejor en la deteccion
de bordes y esta en una funcion, no es necesario, pero es muy aconsejable y lo iremos viendo en diferentes proyectos

Por tanto los parametros de la funcion cv2.HoughLinesP es:
1. Imagen a procesar (que directamente sera la imagen de Canny, solo con los bordes, habiendo utilizado la funcion de Canny
2. Representaciones geometricas de las lineas, como rho y theta, que normalmente seran 1 y np.pi/180 respectivamente
3. EL umbral, cuanto mas grande sea menos lineas se representaran (EN este caso le hemos puesto 100 que es lo normal
4. Por ultimo el hueco y la longitud que esta explicado anteriormente
"""

