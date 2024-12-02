import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluNewQuadric, gluSphere, gluPerspective
import sys

# Variables globales para el ángulo de rotación y posición de la esfera
window = None
rotation_angle = 0.0  # Ángulo de rotación de la esfera
position_x = 0.0  # Posición en el eje X de la esfera
position_y = 0.0  # Posición en el eje Y de la esfera
speed_x = 0.01  # Velocidad de movimiento en el eje X
speed_y = 0.02  # Velocidad de movimiento en el eje Y
radius = 0.5  # Radio de la esfera

# Dimensiones de la ventana
window_width = 500
window_height = 500

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glEnable(GL_DEPTH_TEST)            # Activar prueba de profundidad
    glEnable(GL_LIGHTING)              # Activar iluminación
    glEnable(GL_LIGHT0)                # Activar la luz 0

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, window_width / window_height, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Configuración de la luz
    light_pos = [1.0, 1.0, 1.0, 0.0]  # Posición de la luz
    light_color = [1.0, 1.0, 1.0, 1.0]  # Color de la luz blanca
    ambient_light = [0.2, 0.2, 0.2, 1.0]  # Luz ambiental

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)

    # Configuración de las propiedades de material
    material_diffuse = [1, 0.2, 1.0, 0.0]  # Color difuso (azul claro)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)

def draw_sphere():
    global rotation_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(position_x, position_y, -5)  # Posición de la esfera
    glRotatef(rotation_angle, 0, 1, 0)  # Rotar la esfera sobre su eje Y

    quadric = gluNewQuadric()
    gluSphere(quadric, radius, 32, 32)  # Dibujar la esfera

    glfw.swap_buffers(window)

def update_motion():
    global rotation_angle, position_x, position_y
    global speed_x, speed_y

    # Actualizar el ángulo de rotación
    rotation_angle += 1
    if rotation_angle >= 360:
        rotation_angle = 0  # Reiniciar el ángulo después de una vuelta completa

    # Actualizar la posición de la esfera
    position_x += speed_x
    position_y += speed_y

    # Rebotar en los bordes de la ventana considerando el radio de la esfera
    if position_x + radius > 2.0:  # Límite derecho
        speed_x = -abs(speed_x)  # Invertir la dirección en X a la izquierda
    elif position_x - radius < -2.0:  # Límite izquierdo
        speed_x = abs(speed_x)  # Invertir la dirección en X a la derecha

    if position_y + radius > 2.0:  # Límite superior
        speed_y = -abs(speed_y)  # Invertir la dirección en Y hacia abajo
    elif position_y - radius < -2.0:  # Límite inferior
        speed_y = abs(speed_y)  # Invertir la dirección en Y hacia arriba

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    window = glfw.create_window(window_width, window_height, "Esfera rebotando en los bordes", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, window_width, window_height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_sphere()
        update_motion()  # Actualizar el movimiento y rotación
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
