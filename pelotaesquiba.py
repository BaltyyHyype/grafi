import cv2 as cv
import numpy as np

# tamaño de la ventana para saber dónde va a chocar
ancho_ventana, alto_ventana = 800, 600 

# tamaño de la bola de ping pong (aumentado)
radio_bola1 = 50  # bola de ping pong más grande
radio_bola2 = 20   # tamaño de la segunda bola

# posición inicial de las bolas
posicion_bola1 = [50, 50]  
direccion_bola1 = [8, 12]  # dirección de la bola 1

posicion_bola2 = [400, 300]  # posición inicial de la bola 2
direccion_bola2 = [3, 5]  # dirección de la bola 2

# ventana para la animación
cv.namedWindow('bola pingpong', cv.WINDOW_NORMAL)

while True:
    # imagen en negro de fondo
    cuadro = np.zeros((alto_ventana, ancho_ventana, 3), dtype=np.uint8)

    # dibujar la bola 1 (ping pong)
    cv.circle(cuadro, (posicion_bola1[0], posicion_bola1[1]), radio_bola1, (255, 255, 255), -1)  # color blanco
    # dibujar la bola 2
    cv.circle(cuadro, (posicion_bola2[0], posicion_bola2[1]), radio_bola2, (0, 255, 0), -1)  # color verde

    # mostrar la imagen
    cv.imshow('bola pingpong', cuadro)

    # actualizar la posición de la bola 1
    posicion_bola1[0] += direccion_bola1[0]
    posicion_bola1[1] += direccion_bola1[1]

    # rebotar la bola 1 al tocar los bordes
    if posicion_bola1[0] - radio_bola1 < 0 or posicion_bola1[0] + radio_bola1 > ancho_ventana:
        direccion_bola1[0] *= -1  # se invierte la dirección en x
    if posicion_bola1[1] - radio_bola1 < 0 or posicion_bola1[1] + radio_bola1 > alto_ventana:
        direccion_bola1[1] *= -1  # se invierte la dirección en y

    # actualizar la posición de la bola 2
    posicion_bola2[0] += direccion_bola2[0]
    posicion_bola2[1] += direccion_bola2[1]

    # rebotar la bola 2 al tocar los bordes
    if posicion_bola2[0] - radio_bola2 < 0 or posicion_bola2[0] + radio_bola2 > ancho_ventana:
        direccion_bola2[0] *= -1  # se invierte la dirección en x
    if posicion_bola2[1] - radio_bola2 < 0 or posicion_bola2[1] + radio_bola2 > alto_ventana:
        direccion_bola2[1] *= -1  # se invierte la dirección en y

    # medir la distancia entre las bolas
    distancia = np.linalg.norm(np.array(posicion_bola1) - np.array(posicion_bola2))

    # si la bola 2 está muy cerca de la bola 1, cambiar dirección
    umbral_distancia = (radio_bola1 + radio_bola2)  # distancia segura para el rebote
    if distancia < umbral_distancia:
        # invertir la dirección de la bola 2
        direccion_bola2[0] *= -1  # invertir dirección en x
        direccion_bola2[1] *= -1  # invertir dirección en y

        # ajustar la posición para evitar solapamiento
        overlap = umbral_distancia - distancia
        direccion_bola2[0] += vector_separacion[0] * overlap / norm_vector
        direccion_bola2[1] += vector_separacion[1] * overlap / norm_vector

    # le ponemos un escape con la letra q
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
