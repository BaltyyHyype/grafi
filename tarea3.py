##############################################
# actv 1 rotar 70 grados, escalar a 2, trasladar 20px
##############################################

import cv2 as cv
import numpy as np
import math

# cargar la imagen en escala de grises
img = cv.imread('chevrolet.png', 0)

# obtener el tamaño de la imagen
x, y = img.shape

# definir el angulo de rotacion
angle = 70  # rotar 70 grados
theta = math.radians(angle)

# crear una imagen vacia para la imagen rotada
rotated_img = np.zeros((x * 2, y * 2), dtype=np.uint8)
xx, yy = rotated_img.shape

# calcular el centro de la imagen
cx, cy = int(x // 2), int(y // 2)

##############################################################################

# rotar la imagen 70 grados a la derecha
for i in range(x):
    for j in range(y):
        new_x = int((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx)
        new_y = int((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy)
        if 0 <= new_x < xx and 0 <= new_y < yy:
            rotated_img[new_y, new_x] = img[i, j]

######################################################################

# definir el factor de escala
scale_x, scale_y = 2, 2  # escalar a 2

# crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

######################################################################

# aplicar el escalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < xx and 0 <= orig_y < yy:
            scaled_img[i, j] = rotated_img[orig_x, orig_y]

########################################################################

# crear una imagen vacia para la traslacion
final_img = np.zeros((scaled_img.shape[0], scaled_img.shape[1]), dtype=np.uint8)

# desplazamiento en el eje x y en el eje y
dx, dy = 20, 20  # trasladar 20 pixeles

# trasladar la imagen escalada
for i in range(scaled_img.shape[0]):
    for j in range(scaled_img.shape[1]):
        new_x = i + dy
        new_y = j + dx
        if 0 <= new_x < final_img.shape[0] and 0 <= new_y < final_img.shape[1]:
            final_img[new_x, new_y] = scaled_img[i, j]

########################################################################

# mostrar las imagenes
cv.imshow('imagen original', img)
cv.imshow('imagen rotada 70 grados', rotated_img)
cv.imshow('imagen escalada a 2', scaled_img)
cv.imshow('imagen final trasladada', final_img)
cv.waitKey(0)
cv.destroyAllWindows()
