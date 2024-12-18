
#DESCRIPCION DEL PROGRAMA:
# el punto izquierdo rotara el pinito
# el punto derecho trasladara el pinito
# al separarse los dos puntitos se escalara el pinito de navidad 



import cv2
import numpy as np

# variables globales
gris_anterior = None # guardamos escala de grises para flujo optico
puntos_previos = np.array([[800, 500], [1000, 500]], dtype=np.float32).reshape(-1, 1, 2)  # puntos iniciales
vector_movimiento = np.zeros(2) #utilizamos las dos dimensiones las cuales son X y Y 
factor_escala = 1.0
angulo = 0  # angulo para rotar el pinitooo
centro = (800, 500)  # centro inicial del pino

def dibujar_pino(frame, centro, escala, angulo):
    """Dibuja un pino de Navidad transformado en el frame."""
    x, y = centro
    escala = max(0.5, escala)  # escala minima

    # Coordenadas del pino antes de aplicar transformaciones
    tronco = np.array([[x - 10, y + 50], [x + 10, y + 50], [x + 10, y + 70], [x - 10, y + 70]], dtype=np.float32)
    pino = np.array([[x, y], [x - 30, y + 50], [x + 30, y + 50]], dtype=np.float32)

    # Calcular el centro geométrico del triángulo (pino)
    centro_pino = np.mean(pino, axis=0)

    # rotarr 
    def rotar_puntos(puntos, cx, cy, theta):
        puntos_rotados = []
        for px, py in puntos:
            nuevo_x = (px - cx) * np.cos(np.radians(theta)) - (py - cy) * np.sin(np.radians(theta)) + cx
            nuevo_y = (px - cx) * np.sin(np.radians(theta)) + (py - cy) * np.cos(np.radians(theta)) + cy
            puntos_rotados.append([nuevo_x, nuevo_y])
        return np.array(puntos_rotados, dtype=np.float32)

    # Aplicar escalado y rotación al pino y al tronco
    tronco = (tronco - centro_pino) * escala + centro_pino
    pino = (pino - centro_pino) * escala + centro_pino
    tronco_rotado = rotar_puntos(tronco, *centro_pino, angulo)
    pino_rotado = rotar_puntos(pino, *centro_pino, angulo)

    # Dibujar el pino en el frame
    cv2.fillPoly(frame, [pino_rotado.astype(np.int32)], (1, 200, 60))  # triagulo del pinito
    cv2.fillPoly(frame, [tronco_rotado.astype(np.int32)], (1, 70, 100))  # Rectangulo para el troco del pinito



def procesar_flujo_optico(frame_gris):
    """Procesa el flujo optico para los puntos definidos manualmente."""
    global gris_anterior, puntos_previos, vector_movimiento, factor_escala, angulo, centro

    if gris_anterior is None:
        gris_anterior = frame_gris
        return

    # calculo del flujo optico para los puntos
    puntos_siguientes, estado, _ = cv2.calcOpticalFlowPyrLK(gris_anterior, frame_gris, puntos_previos, None,
                                                            winSize=(15, 15), maxLevel=3,
                                                            criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))




    if puntos_siguientes is not None and len(puntos_siguientes) == 2:
        p1, p2 = puntos_siguientes.reshape(2, 2)  # los dos puntos actuales
        prev_p1, prev_p2 = puntos_previos.reshape(2, 2)  # los dos puntos anteriores

        # traslacion basada en el movimiento del punto derecho
        vector_movimiento = p2 - prev_p2
        centro = (
            max(50, min(1500, int(centro[0] + vector_movimiento[0]))),
            max(50, min(1000, int(centro[1] + vector_movimiento[1])))
        )

        # rotacion basada en el movimiento del punto izquierdo
        delta_rotacion = p1 - prev_p1
        if np.linalg.norm(delta_rotacion) > 2:
            angulo += delta_rotacion[1] * 0.9  # Cambiar el ángulo según el movimiento en Y 

        # escalamiento basado en la distancia entre los dos puntos
        distancia_nueva = np.linalg.norm(p1 - p2)
        distancia_vieja = np.linalg.norm(prev_p1 - prev_p2)
        if distancia_vieja > 0:
            factor_escala *= (distancia_nueva / distancia_vieja)

        puntos_previos = puntos_siguientes.copy()  # actualizar puntos previos

    gris_anterior = frame_gris

def principal():
    global gris_anterior

    camara = cv2.VideoCapture(0)
    if not camara.isOpened():
        print("No se pudo abrir la cámara.")
        return

    while True:
        ret, frame = camara.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # dibujar puntos  en la pantalla
        for punto in puntos_previos.reshape(-1, 2):
            cv2.circle(frame, tuple(punto.astype(int)), 5, (0, 0, 255), -1)

        # procesar el flujo optico
        procesar_flujo_optico(frame_gris)

        # dibujar el pinitoo en el frame
        dibujar_pino(frame, centro, factor_escala, angulo)

        # mostrar el frame
        cv2.imshow("Flujo optico con Puntos Manuales", frame)

        # le puse que le presionaran q para salir rapidamente
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camara.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    principal()
