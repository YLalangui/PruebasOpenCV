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