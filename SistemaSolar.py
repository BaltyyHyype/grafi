import numpy as np
import cv2

# Definir los parámetros del sistema solar
width, height = 800, 800
sun_radius = 30  # Radio del sol
planet_radii = [50, 100, 150, 200]  # Radios de las órbitas de los planetas
planet_sizes = [10, 15, 12, 18]  # Tamaños de los planetas
num_planets = len(planet_radii)
num_frames = 300  # Número de frames en la animación
speed_factors = [1, 0.5, 0.3, 0.2]  # Velocidades relativas de los planetas

# Colores de los planetas
planet_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0)]  # Rojo, Verde, Azul, Naranja

# Crear una ventana para mostrar la animación
cv2.namedWindow('Sistema Solar', cv2.WINDOW_AUTOSIZE)

# Animar el sistema solar
for frame in range(num_frames):
    # Crear una imagen en blanco
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Dibujar el sol en el centro
    cv2.circle(img, (width // 2, height // 2), sun_radius, (0, 255, 255), -1)  # Color amarillo

    # Dibujar las órbitas y los planetas
    for i in range(num_planets):
        # Dibujar la órbita
        cv2.circle(img, (width // 2, height // 2), planet_radii[i], (200, 200, 200), 1)  # Color gris

        # Calcular la posición del planeta
        t = frame * speed_factors[i]  # Ajustar la velocidad de cada planeta
        x = int((width // 2) + planet_radii[i] * np.cos(t * 0.05))
        y = int((height // 2) + planet_radii[i] * np.sin(t * 0.05))

        # Dibujar el planeta
        cv2.circle(img, (x, y), planet_sizes[i], planet_colors[i], -1)  # Color del planeta
    
    # Mostrar el frame en la ventana
    cv2.imshow('Sistema Solar', img)

    # Esperar un corto tiempo para crear la animación (ajustar velocidad)
    cv2.waitKey(50)

# Cerrar la ventana cuando la animación termine
cv2.destroyAllWindows()
