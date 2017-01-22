import numpy as np
import cv2

# Vemos que es muy importante el kernel, cuando mas grande sea el kernel menos nitido se vera la imagen
# PODEMOS DECIR QUE UN FILTRO BASADO EN KERNEL TAMBIEN PUEDE SER LLAMADO UN FILTRO DE CONVOLUCION
# Vamos a crear una matriz de convolucion
# usaremos la funcion de opencv filter2D() que aplica cualquier kernel o matriz de convolucion que le especifiquemos
# utilizaremos un kernel con un 9 en el medio y -1 alrededor, lo que significara que si el pixel de interes es un poco
# diferente de sus vecinos, esta diferencia de intensificara

img = cv2.imread("imagenes/images4_21.jpg")
kernel = np.array([[-1,-1,-1], [-1, 8, -1], [-1, -1, -1]])
# Ver que la diferencia entre el centro del kernel y la suma de los vecinos es 1. Este deberia ser el caso cuando
# nosotros queremos dejar el brillo de la imagen intacto. Pero si la suma da 0 (intercambiar el 9 por un 8) entonces
# nos sale los bordes
# Lo ideal seria pasarlo a blanco y negro y luego blurearlo (hacerlo mas borroso)
img = cv2.medianBlur(img, 3)
imgcopia = np.copy(img)
filtro = cv2.filter2D(img, -1, kernel)
# UN valor negativo en el segundo parametro de filter2D()significa que la imagen final tiene la misma profuncidad
# que la imagen originial
cv2.imshow("Originial", imgcopia)
cv2.imshow("Filtrado", filtro)
cv2.waitKey(0)
# ESte filtrado (filter2D()) funciona tanto para imagenes a color como para en blanco y negro

""""
# AQUI TENEMOS OTRO METODO PARA DETECTAR BORDES, HACIENDO QUE LA SUMA DE LOS ELEMENTOS DEL KERNEL O MATRIZ DE
# CONVOLUCION SEA 0, PERO LOS BORDES SALEN MUY TENUES
Vemos que con esta ultima funcion de openCV podemos meter un kernel que nosotros hayamos desarrollado
AL median blur no le hace falta introducir ningun kernel creado, solo la dimension del kernel que de fabrica
va a usar
"""
# CURIOSITY
# Nuestro refinamiento (filter2D()), deteccion de bordes (anteriormente encontrados) y los filtros blur usan kernels
# que son altamente simetricos. ALgunas veces kernels con menos simetria oriduce un efecto interesante. Vamos a considerar
# una kernel que blurea en un lado (con numeros poitivos) y que refina (parecido a filter2D()) en otro lado (con numeros
# negativos. ESto creara como un efecto en relieve.
imgcopia2 = np.copy(img)
kernel2 = np.array([[-2, -1, 0],[-1, 1, 1],[ 0, 1, 2]])
embossed = cv2.filter2D(img, -1, kernel2)
cv2.imshow("Original", imgcopia2)
cv2.imshow("Embossed", embossed)
cv2.waitKey(0)
# Este efecto mola, Y MUCHO

# vamos a hacer un experimento con la camara del portatil, a ver que tal sale
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.medianBlur(frame,3)
    # NO METERLE UN KERNEL MUY GRANDE PORQUE SI NO LAS IMAGENES VAN LENTo
    # COmo mucho vamos a meterle un 3, porque con un 5 los videos que no son de camara van lentos
    # Our operations on the frame come here
    # Las imagenes las cambio de color a blanco y negro


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #frame = cv2.Laplacian(frame,cv2.CV_8U, frame, 5)


    # y aqui es donde puedo jugar, el kernel que esta metido ahora tiene diferencia 0 en sus elementos, por lo que
    # me daran los contornos. Puedo cambiar a kernel2 que mas arriba pone las caracteristicas del kernel para embossed
    embossed2 = cv2.filter2D(frame, -1, kernel2)


    # Display the resulting frame
    cv2.imshow('frame',embossed2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Y ASI ES COMO SE HACE UN VIDEO CON EMBOSSED y con lo que quieras

