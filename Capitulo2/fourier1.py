import cv2
import numpy as np
from scipy import ndimage



# tenemos una funcion en numpy que es "fft2()" que nos permite hacer la DFT en la imagen (Discrete Fourier Transform)

# Veremos ahora el FILTRO PASO ALTO
# Vemos el valor del kernel, que es una matriz de 3x3 que va reocrriendo pixel a pixel la imagen y cuando el kernel cae
# sobre un pixel lo que se hace es multiplicar los valores de la matriz de kernel con los correspondientes a donde
# haya caido, siendo el valor de ese pixel la suma de todas las multiplicaicones (mejor buscar en internet
# matriz de convolucion
# Vemos que al utilizar el ndimage.convolve hace la convolucion con una matriz de convolucion, pero la suma
# de los elementos de las matrices es 0, luego veremos por que, pero vemos que detecta los bordes de la imagen
# ESte filtro alto lo hemos usado con la libreria SCIPY

kernel_3x3 = np.array([[-1, -1, -1],
[-1, 8, -1],
[-1, -1, -1]])
kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
[-1, 1, 2, 1, -1],
[-1, 2, 4, 2, -1],
[-1, 1, 2, 1, -1],
[-1, -1, -1, -1, -1]])

img = cv2.imread("imagenes/images4_21.jpg", 0)
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)
blurred = cv2.GaussianBlur(img, (11,11), 0)
g_hpf = img - blurred
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()


# Ahora haremos un FILTRO PASO BAJO

"""
# YA TENEMOS UN METODO PARA DETECTAR BORDES, USANDO TRANSFORMADAS DE FOURIER, AUNQUE HACE FALTA MEJORARLO
Con este metodo de scipy SI nos deja meter un kernel que nosotros hemos creado, pero no es una funcion de openCV
"""








