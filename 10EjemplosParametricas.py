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
        
        # Mostrar la figura
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

# 3. Limaçon con un bucle
def draw_figura3(img, a, b, k, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = a + b * np.cos(k * t)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (0, 255, 0), 1)
        
        cv2.imshow('Figura 3: Limaçon con un bucle', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura3(img, a=100, b=50, k=2, theta_increment=0.05, max_theta=2 * np.pi)

# 4. Rosa
def draw_figura4(img, n_petals, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = 300 * np.sin(n_petals * t)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (255, 0, 0), 1)
        
        cv2.imshow('Figura 4: Rosa con {} pétalos'.format(n_petals), img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura4(img, n_petals=6, theta_increment=0.05, max_theta=2 * np.pi)

# 5. Espiral
def draw_figura5(img, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    r_increment = 1  # Incremento del radio
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = r_increment * t
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (0, 165, 255), 1)
        
        cv2.imshow('Figura 5: Espiral', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura5(img, theta_increment=0.05, max_theta=10 * np.pi)

# 6. Lemniscata de Bernoulli
def draw_figura6(img, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = 300 * np.sqrt(np.cos(2 * t))
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            cv2.circle(img, (x, y), 1, (255, 165, 0), 1)
        
        cv2.imshow('Figura 6: Lemniscata de Bernoulli', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura6(img, theta_increment=0.05, max_theta=2 * np.pi)

# 7. Hipociclo
def draw_figura7(img, a, b, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            r = a - b
            x = int(center_x + r * np.cos(t) + b * np.cos((a/b - 1) * t))
            y = int(center_y + r * np.sin(t) - b * np.sin((a/b - 1) * t))
            cv2.circle(img, (x, y), 1, (128, 0, 128), 1)
        
        cv2.imshow('Figura 7: Hipociclo', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura7(img, a=150, b=50, theta_increment=0.05, max_theta=2 * np.pi)

# 8. Epicycloid
def draw_figura8(img, a, b, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            x = int(center_x + (a + b) * np.cos(t) - b * np.cos((a/b + 1) * t))
            y = int(center_y + (a + b) * np.sin(t) - b * np.sin((a/b + 1) * t))
            cv2.circle(img, (x, y), 1, (0, 255, 255), 1)
        
        cv2.imshow('Figura 8: Epicíclo', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura8(img, a=150, b=50, theta_increment=0.05, max_theta=2 * np.pi)

# 9. Óvalo
def draw_figura9(img, a, b, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    theta = 0
    
    while True:
        img[:] = 255
        
        for t in np.arange(0, theta, theta_increment):
            x = int(center_x + a * np.cos(t))
            y = int(center_y + b * np.sin(t))
            cv2.circle(img, (x, y), 1, (0, 255, 0), 1)
        
        cv2.imshow('Figura 9: Óvalo', img)
        theta += theta_increment
        
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
        if theta >= max_theta:
            break

draw_figura9(img, a=200, b=100, theta_increment=0.05, max_theta=2 * np.pi)

# 10. Hipérbola
def draw_figura10(img, a, b, theta_increment, max_theta):
    width, height = img.shape[1], img.shape[0]
    center_x, center_y = width // 2, height // 2
    t = -max_theta / 2

    while True:
        img[:] = 255
        
        for _ in np.arange(-10, 10, 0.01):
            x = int(center_x + a * np.cosh(t))
            y = int(center_y + b * np.sinh(t))
            cv2.circle(img, (x, y), 1, (255, 20, 147), 1)
            t += theta_increment
        
        cv2.imshow('Figura 10: Hipérbola', img)
        
        if cv2.waitKey(30) & 0xFF == 27:
            break

draw_figura10(img, a=50, b=30, theta_increment=0.05, max_theta=2 * np.pi)

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
