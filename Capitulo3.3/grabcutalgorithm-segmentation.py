import cv2
import numpy as np
from matplotlib import pyplot as plt

# Para hacer segmentacion de objetos aplicaremos el algotirmo de Grabcut (Agarrar y cortar). SEGMENTACION
"""
1. UN rectangulo incluyendo el objeto de la imagen es definido
2. EL area que quede fuera del rectangulo automaticamente es definido como fondo
3. Los datos contenidos en el fondo (background) es usado como una referencia para distinguie de el area de fondo de
las areas de primer plano dentro del rectangulo definido anteriormente
4. Un GMM (Gaussians MIxture Model) modela el fondo y el primer plano, y nivela los pixeles no definidos como posibles
fondo o posible primer plano
5. Cada pixel en la imagen esta practicamente conectado con los pixeles de su alrededor a traves de bordes virtuales,
y cada borde da una probabilidad de ser fondo o primer plano, basado en cuan similar es en color con los pixeles de
alrededor
6. Cada pixel (o nodo como esta conceptualizado en el algoritmo) esta conectado tanto con el nodo de fondo como con el
nodo de primer plano
7. Despues que los nodos han sido conectado con ambos terminales (fondo y primer plano), los bordes entre nodos
pertenecientes a diferentes terminales son cortadas (este es la famosa parte del corte del algoritmo), lo cual permite
la separacion de las partes de la imagen.
"""
img = cv2.imread("imagenes/estatua.jpg")
# Creamos una mascara con ceros que tenga la mis aforma que la imagen que hemos cargado
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)
# rectangulo en el que definimos la imagen que queremos obtener
rect = (100,50,421,378)
# El numero 5 es el numero de iteraciones
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Despues nuestra mask tendra ahora valores entre 0 y 3. Los valores 0 y 2 se convertiran en 0 y el 1-3 en 1, y estos
# seran guardados en mask2 y hacemos uso de un "filtro" que teóricamente dejara el primer plano que queremos intacto,
# aunque vemos que aun asi hay fallos en la segmentacion de la imagen
mask2 = np.where((mask==2) | (mask==0), 0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.subplot(121), plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread('imagenes/estatua.jpg'), cv2.COLOR_BGR2RGB))
plt.title("original"), plt.xticks([]), plt.yticks([])
plt.show()