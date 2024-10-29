##############################################
# actv 2 rotar 30° a la derecha, rotar 60° a la izquierda, escalar a 2
##############################################

import cv2 as cv
import numpy as np
import math

# ponemos ala imagen en escala de grises
img = cv.imread('chevrolet.png', 0)

# tamaño de la imagen
x, y = img.shape

# angulos de rotación
angle_right = 30  # Rotar 30 grados a la derecha
angle_left = 60   # Rotar 60 grados a la izquierda
theta_right = math.radians(angle_right)
theta_left = math.radians(angle_left)

# imagen vacía para almacenar la imagen rotada 30 grados
rotated_img_right = np.zeros((x * 2, y * 2), dtype=np.uint8)
xx, yy = rotated_img_right.shape

# centro de la imagen
cx, cy = int(x // 2), int(y // 2)

##############################################################################

# rrrotar 30 grados a la derecha
for i in range(x):
    for j in range(y):
        new_x = int((j - cx) * math.cos(theta_right) - (i - cy) * math.sin(theta_right) + cx)
        new_y = int((j - cx) * math.sin(theta_right) + (i - cy) * math.cos(theta_right) + cy)
        if 0 <= new_x < xx and 0 <= new_y < yy:
            rotated_img_right[new_y, new_x] = img[i, j]

######################################################################

# imagen vacía para almacenar la imagen rotada 60 grados a la izquierda
rotated_img_left = np.zeros((x * 2, y * 2), dtype=np.uint8)
xx, yy = rotated_img_left.shape

# rotarimagen 60 grados a la izquierda
for i in range(x):
    for j in range(y):
        new_x = int((j - cx) * math.cos(-theta_left) - (i - cy) * math.sin(-theta_left) + cx)
        new_y = int((j - cx) * math.sin(-theta_left) + (i - cy) * math.cos(-theta_left) + cy)
        if 0 <= new_x < xx and 0 <= new_y < yy:
            rotated_img_left[new_y, new_x] = rotated_img_right[i, j]

######################################################################

# definir el numero qiue escalarelmos la imagen
scale_x, scale_y = 2, 2  # Escalar a 2

# nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

######################################################################

# aplicar el escalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < xx and 0 <= orig_y < yy:
            scaled_img[i, j] = rotated_img_left[orig_x, orig_y]

########################################################################

# aostramos todas las imagenes incliuyendo la original 
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada 30° a la Derecha', rotated_img_right)
cv.imshow('Imagen Rotada 60° a la Izquierda', rotated_img_left)
cv.imshow('Imagen Escalada a 2', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()
