import cv2 as cv
import numpy as np


img = cv.imread('/Users/baltyyhyype/Documents/Graficacion/FotoGrafiPrueba.png', 0)


#allj;



x, y = img.shape


scale_x, scale_y = 0.5, 0.5


scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)


for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < x and 0 <= orig_y < y:
            scaled_img[i, j] = img[orig_x, orig_y]


kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]], dtype=np.float32)


smoothed_img = np.zeros_like(scaled_img)


for i in range(1, scaled_img.shape[0] - 1):
    for j in range(1, scaled_img.shape[1] - 1):
        sum_val = 0.0
        for m in range(-1, 2):
            for n in range(-1, 2):
                sum_val += scaled_img[i + m, j + n] * kernel[m + 1, n + 1]
        smoothed_img[i, j] = int(sum_val)

cv.imshow('Imagen Grises', img)
cv.imshow('Imagen Escalada ', scaled_img)
cv.imshow('Imagen Escalada con covolucion', smoothed_img)
cv.waitKey(0)
cv.destroyAllWindows()
