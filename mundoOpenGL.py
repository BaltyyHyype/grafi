import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Variables globales de cámara
camera_position = [0, 1, 5]
camera_target = [0, 1, 0]
camera_up = [0, 1, 0]

# Clase Muñeco de Nieve
class Snowman:
    def __init__(self, position):
        self.position = position

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        
        # Parte inferior (esfera más grande)
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)  # Color blanco
        glTranslatef(0, -0.75, 0)
        gluSphere(gluNewQuadric(), 0.5, 32, 32)
        glPopMatrix()
        
        # Parte del medio
        glPushMatrix()
        glTranslatef(0, 0, 0)
        gluSphere(gluNewQuadric(), 0.35, 32, 32)
        glPopMatrix()

        # Cabeza
        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        gluSphere(gluNewQuadric(), 0.25, 32, 32)
        glPopMatrix()
        
        glPopMatrix()

# Clase Árbol
class Tree:
    def __init__(self, position):
        self.position = position
        self.rotation_angle = 0

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glRotatef(self.rotation_angle, 0, 1, 0)
        
        # Tronco (cilindro)
        glPushMatrix()
        glColor3f(0.55, 0.27, 0.07)  # Color marrón
        glTranslatef(0, -0.5, 0)
        gluCylinder(gluNewQuadric(), 0.1, 0.1, 0.5, 32, 32)
        glPopMatrix()

        # Hojas (cono)
        glColor3f(0.0, 0.8, 0.0)  # Verde para el follaje
        glPushMatrix()
        glTranslatef(0, 0.1, 0)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.3, 0.0, 0.8, 32, 32)
        glPopMatrix()
        
        glPopMatrix()

    def update(self):
        self.rotation_angle += 0.5  # Rotación constante en Y

# Inicializar GLFW y ventana
def init_window():
    if not glfw.init():
        return None
    window = glfw.create_window(800, 600, "Mundo 3D en OpenGL", None, None)
    if not window:
        glfw.terminate()
        return None
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Color azul claro para simular el cielo
    return window

# Configurar cámara
def update_camera():
    glLoadIdentity()
    gluLookAt(*camera_position, *camera_target, *camera_up)

# Configurar iluminación y materiales
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light_pos = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])

# Procesamiento de entradas para mover la cámara
def key_callback(window, key, scancode, action, mods):
    global camera_position, camera_target
    if action != glfw.PRESS:
        return
    if key == glfw.KEY_W:   # Adelante
        camera_position[2] -= 0.2
        camera_target[2] -= 0.2
    elif key == glfw.KEY_S: # Atrás
        camera_position[2] += 0.2
        camera_target[2] += 0.2
    elif key == glfw.KEY_A: # Izquierda
        camera_position[0] -= 0.2
        camera_target[0] -= 0.2
    elif key == glfw.KEY_D: # Derecha
        camera_position[0] += 0.2
        camera_target[0] += 0.2
    elif key == glfw.KEY_Q: # Arriba
        camera_position[1] += 0.2
        camera_target[1] += 0.2
    elif key == glfw.KEY_E: # Abajo
        camera_position[1] -= 0.2
        camera_target[1] -= 0.2

# Dibujar el suelo
def draw_ground():
    glPushMatrix()
    glColor3f(0.3, 0.8, 0.3)  # Color verde claro
    glBegin(GL_QUADS)
    glVertex3f(-5, -1, -5)
    glVertex3f(-5, -1, 5)
    glVertex3f(5, -1, 5)
    glVertex3f(5, -1, -5)
    glEnd()
    glPopMatrix()

# Bucle principal de dibujo
def main():
    window = init_window()
    if not window:
        print("Error al crear la ventana.")
        return
    
    glfw.set_key_callback(window, key_callback)
    setup_lighting()

    # Instancias de objetos en el mundo
    snowman = Snowman([1, -0.5, -3])
    tree = Tree([-1, -0.5, -4])

    # Bucle principal
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Actualizar y dibujar la cámara
        update_camera()

        # Dibujar el suelo
        draw_ground()

        # Dibujar objetos
        glPushMatrix()
        snowman.draw()
        tree.draw()
        glPopMatrix()
        
        # Actualizar el estado de los objetos
        tree.update()

        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
