import numpy as np
import cv2 as cv

# Cargar clasificadores en cascada
rostro_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
ojo_cascade = cv.CascadeClassifier(r'C:\Users\Balta\Desktop\grafi\haarcascade_eye.xml')  # Asegúrate de la ruta
boca_cascade = cv.CascadeClassifier(r'C:\Users\Balta\Desktop\grafi\haarcascade_smile.xml')  # Asegúrate de la ruta

cap = cv.VideoCapture(0)

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
        ojos = ojo_cascade.detectMultiScale(gray[y:y + h, x:x + w])
        for (ex, ey, ew, eh) in ojos:
            # Dibujar un círculo para representar el filtro de ojo
            cv.circle(frame, (x + ex + ew // 2, y + ey + eh // 2), min(ew, eh) // 2, (255, 0, 0), -1)

        # Detectar boca dentro del rostro
        bocas = boca_cascade.detectMultiScale(gray[y:y + h, x:x + w])
        for (bx, by, bw, bh) in bocas:
            # Dibujar un rectángulo para representar el filtro de boca
            cv.rectangle(frame, (x + bx, y + by), (x + bx + bw, y + by + bh), (0, 0, 255), -1)

    cv.imshow('rostros', frame)

    k = cv.waitKey(1)
    if k == 27:  # Presiona ESC para salir
        break

cap.release()
cv.destroyAllWindows()
