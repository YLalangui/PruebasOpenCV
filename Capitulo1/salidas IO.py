import numpy
import cv2
import cv
import os
import numpy as np

"""
img = numpy.zeros((3,3), dtype=numpy.uint8)
print img
"""
# Ahora convertiremos esa matriz (imagen) en BGR

"""
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print img
"""
# Como podemos ver cada pixel esta ahora representado con un array de tres elementos, cada Int corresponde a B,G y R
# Recordar no poner tildes

# Tambien puedo ver propiedad shape, la cual me da las filas, de columnas y el numero de canales, en caso de ser mas de 3
# EL ultimo 3 me sale porque lo tengo en RGB, me salen 3 canales
"""
print img.shape
"""

# podemos cambiar el formato a una imagen, si vemos que nos es dificil trabajar con alguno
# tambien podemos ensenar la imagen en pantalla
# recordar que imread() devuelve un formato BGR, inverso al RGB, con el orden invertido
"""
image = cv2.imread("imagenes/images4_21.jpg")
cv2.imshow("Imagenes", image)
cv2.waitKey(0)
cv2.imwrite("imagenes/images4_21.png", image)

"""

# Tambien lo podemos sabar igualmente las imagenes en blanco y negro
# Imwrite tambien necesita archivos en BGR
"""
grayImage = cv2.imread("imagenes/images4_21.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("imagenes/images4_21.png", grayImage)
cv2.imshow("Imagenes", grayImage)
cv2.waitKey(0)
# Como una imagen es una matriz puedo acceder a los valores de un pixel poniendo nombre_imagen[0,0,0], siendo el primer
# indice la "y" o las filas, el segundo indice la "x" o columnas y el ultimo indice el canal
print grayImage[0,0]
"""

"""
# CREACION DE IMAGENES EN COLOR Y EN BLANCO Y NEGRO ALEATORIAS

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)
# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)
"""

#Forma de cambiar el color a un pixel de una imagen
"""
image = cv2.imread("imagenes/images4_21.jpg")
image[0,0] = [255,255,255]
cv2.imshow("Imagenes", image)
cv2.waitKey(0)
"""

# Hemos obtenido el valor de uno de los canales de un pixel, en este caso como el indice es 0 hemos
# obtenido el del color azul y luego lo hemos cambiado a otro color, esto haciendolo con numpy (item y itemset respectivamente)
"""
image = cv2.imread("imagenes/images4_21.jpg")
print image.item(150, 120, 0)
# imprime el valor del azul en ese pixel, pues como ultimo parametro mira a la matriz ([65,65,65]), siendo este un ejemplo
# y siemdo el primer elemento el azul, el segundo el verde y el ultimo el rojo
image.itemset( (150, 120, 0), 255)
print image.item(150, 120, 0)
cv2.imshow("Imagenes", image)
cv2.waitKey(0)
"""

# Aqui lo que estamos haciendo es evitarnos el usar los loops y hemos cambiado todos los pixeles del indice 1, de los verdes
# a cero, saliendo una imagen un tanto curiosa, sin verdes. Asi tambien podemos quitar o  cambiar todos los pixeles de
# un canal (Azul, verde o rojo) a nuestro antojo
"""
image = cv2.imread("imagenes/images4_21.jpg")
image[:,:,2] = 0
cv2.imshow("Imagenes", image)
cv2.waitKey(0)
"""

# Aqui vamos a hacer un corta y pega de la foto, sabiendo de antemano la parte que queremos copiar y sabiendo los pixeles
# de antemano de esa region que queremos copiar y sabiendo de antemano la region (los pixeles) y los que queremos pegar
# Saldra como resultado una imagen con un chacho de ella misma en otro lado
# ES importante tener en cuenta que las regiones que estamos copiando y pegando tienen que tener las mismas dimensiones
"""
image = cv2.imread("imagenes/images4_21.jpg")
# recordar que aqui no meto canales
my_roi = image[0:100, 0:100]
image[300:400,300:400] = my_roi
cv2.imshow("Ventana", image)
cv2.waitKey(0)
"""


# Como ultimo podemos obtener las caracteristicas de la imagen
# con shape nos devuelve un array con el ancho, largo y el numero de canales si hay mas, en ese orden respectivamente
# ESte shape es bueno para sber si una imagen es en color o en blanco y medio, viendo a ver si me devuelve el tercer
# elemento que sera el numero de canales en caso de que sea a color o no me duvuelve el tercer elemento en caso de
# que sea en blanco y negro
"""
image = cv2.imread("imagenes/images4_21.jpg")
print image.shape
print image.size
print image.dtype

"""

"""
VAMOS CON VIDEOS
"""

# Ensenamos un video en pantalla
"""
cap = cv2.VideoCapture('pelota_roja.avi')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
"""

# FOrma simple de ensenar una imagen por pantalla
"""
image = cv2.imread("imagenes/images4_21.jpg")
cv2.imshow("Imagen", image)
cv2.waitKey()
cv2.destroyAllWindows()
"""

# Otra forma de ensenar un video por pantalla de la camara frontal
"""
clicked = False
def onMouse(event, x, y, flags, param):
 global clicked
 if event == cv2.EVENT_LBUTTONUP:clicked = True
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)
print 'Showing camera feed. Click window or press any key to stop.'
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
 cv2.imshow('MyWindow', frame)
 success, frame = cameraCapture.read()
cv2.destroyWindow('MyWindow')
cameraCapture.release()
"""


