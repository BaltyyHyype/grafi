import numpy as np
import cv2 as cv

# Cargar clasificadores en cascada
rostro_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
ojo_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
boca_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

print("Captura iniciada")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo recibir el cuadro.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in rostros:
        # Dibujar el rectángulo alrededor del rostro
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Detectar ojos dentro del rostro
        ojos = ojo_cascade.detectMultiScale(gray[y:y + h, x:x + w], 1.1, 10)
        for (ex, ey, ew, eh) in ojos:
            # Dibujar un óvalo alrededor de los ojos
            center = (x + ex + ew // 2, y + ey + eh // 2)
            axes = (ew // 2, eh // 3)  # Tamaño del óvalo
            cv.ellipse(frame, center, axes, 0, 0, 360, (255, 0, 0), 3)  # Borde más grueso y color azul
            cv.GaussianBlur(frame[y+ey:y+ey+eh, x+ex:x+ex+ew], (15, 15), 0)  # Suavizar la zona del ojo

        # Detectar boca dentro del rostro
        bocas = boca_cascade.detectMultiScale(gray[y + h//2:y + h, x:x + w], 1.7, 20)
        for (bx, by, bw, bh) in bocas:
            # Dibujar un óvalo alrededor de la boca
            center = (x + bx + bw // 2, y + h//2 + by + bh // 2)
            axes = (bw // 2, bh // 3)  # Tamaño del óvalo
            cv.ellipse(frame, center, axes, 0, 0, 360, (0, 0, 255), 3)  # Borde más grueso y color rojo
            cv.GaussianBlur(frame[y+h//2+by:y+h//2+by+bh, x+bx:x+bx+bw], (15, 15), 0)  # Suavizar la zona de la boca

    cv.imshow('rostros', frame)

    if cv.waitKey(30) & 0xFF == 27:  # Presiona ESC para salir
        break

cap.release()
cv.destroyAllWindows()
