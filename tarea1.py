##############################################
# actv 1 rotar=60, trasladar=10px, escala=1/5
##############################################

import cv2 as cv
import numpy as np
import math

# carquekos la imagen en escala de grises
img = cv.imread('chevrolet.png', 0)

# para que obtengamos el amaño de la imagen
x, y = img.shape

# convertirlo a radianes lpos grados de la imagej
angle = 60
theta = math.radians(angle)

# creanios una imagen vacía para poder almacenar la imagen ya rotada
rotated_img = np.zeros((x * 2, y * 2), dtype=np.uint8)
xx, yy = rotated_img.shape

# cceeentro de la imagen
cx, cy = int(x // 2), int(y // 2)

##############################################################################

# rotamos la imagen
for i in range(x):
    for j in range(y):
        new_x = int((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx)
        new_y = int((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy)
        if 0 <= new_x < xx and 0 <= new_y < yy:
            rotated_img[new_y, new_x] = img[i, j]

######################################################################

# escala de 1/5 de act1
scale_x, scale_y = 1/5, 1/5

# creamos nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

#################################################################333
#eeescalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < xx and 0 <= orig_y < yy:
            scaled_img[i, j] = rotated_img[orig_x, orig_y]
########################################################################


# imagen vacía para la traslación
final_img = np.zeros((scaled_img.shape[0], scaled_img.shape[1]), dtype=np.uint8)

# desplazamiento en el ekje x y en el eje y
dx, dy = 10, 10

# trasladar la imagen escalada
for i in range(scaled_img.shape[0]):
    for j in range(scaled_img.shape[1]):
        new_x = i + dy
        new_y = j + dx
        if 0 <= new_x < final_img.shape[0] and 0 <= new_y < final_img.shape[1]:
            final_img[new_x, new_y] = scaled_img[i, j]

# imprimimos la imagen original, rotada, escalada y trasladada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada 60 grados', rotated_img)
cv.imshow('Imagen Escalada 1/5', scaled_img)
cv.imshow('Imagen Final Trasladada', final_img)
cv.waitKey(0)
cv.destroyAllWindows()
