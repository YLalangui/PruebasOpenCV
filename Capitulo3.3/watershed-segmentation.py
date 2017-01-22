import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("imagenes/hoja.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Vamos a usar otro algoritmo que permite tambien segmentar una parte de la imagen de interes
# Vamos a separar las hojas del fondo
# Como hicimos en trabajos anteriores vamos a aplicar un umbral

ret, thresh = cv2.threshold(gray, 0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Para eliminar ruido utilizamos una nueva funcion que es morphologyEx transformation

kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Podemos obtener areas de primer plano aplicando distanceTransform.

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255,0)

sure_fg =  np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)

markers = markers +1
markers[unknown==255] = 0

markers = cv2.watershed(img, markers)
img[markers==-1] = [255,0,0]
plt.imshow(img)
plt.show()