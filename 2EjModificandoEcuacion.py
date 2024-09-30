import numpy as np
import cv2

# Función para dibujar la figura de Limacon
def draw_figura1(img, a, b, k, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255  # Limpiar la imagen
        
        for t in np.arange(0, theta, theta_increment):
            r = a + b * np.cos(k * t)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (0, 234, 0), 1)
        
        cv2.imshow('Figura 1: Limacon k = {}'.format(k), img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

# Inicializar la ventana
width, height = 1000, 1000
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# 1. Limacon
draw_figura1(img, a=150, b=100, k=10, theta_increment=0.05, max_theta=2 * np.pi)

# 2. Cardioide
def draw_figura2(img, a, b, k, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = a + b * np.cos(k * t)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (0, 0, 255), 1)
        
        cv2.imshow('Figura 2: Cardioide', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura2(img, a=100, b=100, k=1, theta_increment=0.05, max_theta=2 * np.pi)

# 3. Curva con ecuación modificada
def draw_figura3(img, a, b, k, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = a * np.sin(k * t) + b * np.cos(t)  # Ecuación modificada
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (255, 0, 0), 1)
        
        cv2.imshow('Figura 3: Curva Modificada', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura3(img, a=100, b=50, k=3, theta_increment=0.05, max_theta=2 * np.pi)

# 4. Espiral con ecuación diferente
def draw_figura4(img, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    r_increment = 5  # Incremento del radio más grande
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = r_increment * t**2  # Ecuación modificada
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (0, 165, 255), 1)
        
        cv2.imshow('Figura 4: Espiral Modificada', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura4(img, theta_increment=0.05, max_theta=10 * np.pi)

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
