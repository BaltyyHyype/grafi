import numpy as np
import cv2 as cv

# Crea una imagen de 300x500 píxeles con 3 canales (color), todos inicializados con color blanco (255, 255, 255)
img = np.ones((300, 500, 3), dtype=np.uint8) * 255

# Color azul marino en formato BGR
azul_marino = (128, 0, 0)

# Dibujar la camioneta pixel por pixel con color azul marino

# Techo de la camioneta (más grande)
img[50:80, 150:350] = azul_marino  # Techo de la camioneta

# Cuerpo de la camioneta
img[80:160, 120:380] = azul_marino  # Cuerpo de la camioneta

# Ventanas (color gris claro)
ventana_color = (200, 200, 200)
img[90:130, 170:220] = ventana_color  # Ventana izquierda
img[90:130, 280:330] = ventana_color  # Ventana derecha

# Ruedas (círculos negros)
cv.circle(img, (180, 160), 30, (0, 0, 0), -1)  # Rueda izquierda
cv.circle(img, (320, 160), 30, (0, 0, 0), -1)  # Rueda derecha

# Mostrar la imagen con OpenCV
cv.imshow('Camioneta Pixel Art Azul Marino', img)

# Espera a que el usuario presione cualquier tecla
cv.waitKey()

# Cierra todas las ventanas creadas por OpenCV
cv.destroyAllWindows()
