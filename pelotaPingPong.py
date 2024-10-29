import cv2 as cv
import numpy as np

# tamaño de la ventana para saber dónde va a chocar
ancho_ventana, alto_ventana = 800, 600 

# tamaño de la bola
radio_bola = 20

# posición inicial de la bola
posicion_bola = [50, 50]  
direccion_bola = [6, 9]  # se va a mover

# ventana para la animación
cv.namedWindow('bola pingpong', cv.WINDOW_NORMAL)

while True:
    # imagen en negro de fondo
    cuadro = np.zeros((alto_ventana, ancho_ventana, 3), dtype=np.uint8)

    # dibujar la bola en la posición que está ahorita
    cv.circle(cuadro, (posicion_bola[0], posicion_bola[1]), radio_bola, (255, 255, 255), -1)  # color blanco

    # mostrar la imagen
    cv.imshow('bola pingpong', cuadro)

    # actualizar la posición donde está la bola
    posicion_bola[0] += direccion_bola[0]
    posicion_bola[1] += direccion_bola[1]

    # rebotar la bola al tocar los bordes
    if posicion_bola[0] - radio_bola < 0 or posicion_bola[0] + radio_bola > ancho_ventana:
        direccion_bola[0] *= -1  # se invierte la dirección en x
    if posicion_bola[1] - radio_bola < 0 or posicion_bola[1] + radio_bola > alto_ventana:
        direccion_bola[1] *= -1  # se invierte la dirección en y

    # le ponemos un escape con la letra q
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
