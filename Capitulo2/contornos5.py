import cv2
import numpy as np

"""
# Primero crearemos una imagen vacia negra de 200x200 y luego colocamos un cuadrado blanco en el medio
img = np.zeros((200,200),dtype=np.uint8)
img[50:150, 50:150] = 255
#cv2.imshow("Ventana", img)
#cv2.waitKey(0)

imgCopia = np.copy(img)
ret, thresh = cv2.threshold(img, 127,255,0)
# Esta linea de contours, hierarchy.. Es la misma siempre que quiera hacer contornos
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Esta funcion findContours tiene tres parametros, primero la imagen, luego un tipo de jerarquia y por ultimo
# un metodo de aproximacion del contorno. Hay que tener aspectos en cuenta como que esta funcion provoca
# una modificacion en la iamgen original, teniendo que hacer de antemano una copia de la misma.
# En segundo lugar el arbol de jerarquias es muy importante, RETR_TREE recupera toda la jerarquia de contornos
# de la imagen, permitiendote establecer relaciones entre contornos. SI por ejemplo solo queremos recuperar los contornos
# externos entonces tendriamos que utilizar RETR_EXTERNAL, esto es particularmente util cuando queremos eliminar contornos
# que estan completamente contenido dentro de otros contornos, por ejemplo nosotros no queremos o no necesitamos detectar
# un objeto dentro de otro objeto con la misma forma

# Paso a blanco y negro la imagen, la copia, pues findContours produce cambios en la imagen original
color = cv2.cvtColor(imgCopia, cv2.COLOR_GRAY2BGR)

# linea que sirve para dibujar los contornos sobre una imagen
# dentro de los parametros de drawContours poner el -1 para que se vean todos los contornos,
#( si luego quiero el 4to contorno entonces en vez de un -1 tendre que poner un 3 luego viene el color que
# sea el contorno y por ultimo el ancho que quiero que se vea el contorno
cv2.drawContours(color,contours, -1, (0,0,255), 2)
cv2.imshow("contours", color)
cv2.waitKey(0)
"""


"""
Ya visto un poco de teoria y lo que son los contornos vamos a hacer ejemplo de verdad
"""



"""
...........................
Aqui haremos un cuadrado (verde) que detecte el objeto, lo construiremos con el contorno mas grande, si lo hacemos con
los pequenos solo saldran puntos.
...........................
"""
img = cv2.pyrDown(cv2.imread("imagenes/figura.jpg", cv2.IMREAD_UNCHANGED))
imgCopia2 = np.copy(img)
ret, thresh = cv2.threshold(cv2.cvtColor(np.copy(img),cv2.COLOR_BGR2GRAY),127, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

"""
PRUEBAAAAAAAAAAAAAAAAAAAAAAAAAAAA
cv2.drawContours(img, contours, -1, (0,255,0), 2)
cv2.imshow("Contornos", img)
cv2.waitKey(0)
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(imgCopia2, (x,y), (x+w, y+h),(0,255,0),2)
ae = cv2.contourArea(contours[0])
rect = cv2.minAreaRect(contours[0])
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
cv2.drawContours(imgCopia2, [box], 0, (0,0,255), 2)
cv2.imshow("rectangulo", imgCopia2)
cv2.waitKey(0)
print (contours[10])
print(ae)
print (rect)
print (box)
cv2.imshow("rectangulo girado", imgCopia2)
cv2.waitKey(0)
"""
for c in contours:
 #rectangulo recto
 x, y, w, h = cv2.boundingRect(c)
 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
 #rectangulo girado
 rect = cv2.minAreaRect(c)
 box = cv2.boxPoints(rect)
 box = np.int0(box)
 cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
 """
 En este caso la imagen es muy sencilla, pero lo mejor seria calcular el contorno con el area mas grande
 """

 #Circulos
 (x,y), radius = cv2.minEnclosingCircle(c)
 center = (int(x), int(y))
 radius = int(radius)
 cv2.circle(img, center, radius, (0,255,0), 2)
 #elipse, pero saldra error porque el numero de puntos tiene que ser mayor o igual a 5
 #ellipse = cv2.fitEllipse(contours[10])
 #cv2.ellipse(img, ellipse, (0,0,255), 2)



cv2.drawContours(img, contours, -1, (255,0,0),1)
cv2.imshow("contornos", img)
cv2.waitKey(0)








"""
PARA UNA MEJOR EXACTITUD UTILIZAMOS IMAGENES BINARIAS, POR TANTO ANTES DE ENCONTRAR CONTORNOS PRIMERO APLICAMOS
UN UMBRAL (COMO EN LA LINEA 52, A PARTIR DE AHORA UTILIZAREMOS ESE UMBRAL PARA DETECTAR CONTORNOS) O HACEMOS UNA
DETECCION DE BORDES MEDIANTE CANNY (PERO PREFERIREMOS EL UMBRAL POR SER MAS SEGURO

TENER CUIDADO CON FINDCONTOURS PORQUE MODIFICA LAS IMAGENES ORIGINALES, MEJOR INTRODUCIRLES COPIAS O LUEGO UTILIZAR
UNA COPIA

EN OPENCV, ENCONTRAR CONTORNOS IS COMO ENCONTRAR UN OBJETO BLANCO DE UN FONDO NEGRO, POR TANTO RECORDAR QUE UN OBJETO
PARA SER ENCONTRADO DEBE SER BLANCO Y EL FONDO DEBE SER NEGRO.

SIEMPRE USAR COLORES EN BLANCO Y NEGRO, NO EN COLOR, POR TANTO
LEER IMAGEN -> PASARLO A BLANCO Y NEGRO SI ES NECESARIO -> UMBRAL (DE LA LINEA 52) -> DETECCION DE CONTORNOS

contours (lo que obtenemos de la funcion findContours), es una lista de todos los contornos de la imagen, cada contorno
individual es un array numpy de coordenadas x,y de los puntos del borde del objeto, por tanto, un cortorno (de los mas
que hay) es un array formado por coordenadas x,y que definen ese contorno
"""


