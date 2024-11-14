import cv2

# Iniciar la captura de video (0 es la cámara predeterminada)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

while True:
    # Leer el cuadro de video de la cámara
    ret, frame = cap.read()

    # Verificar si se obtuvo el cuadro correctamente
    if not ret:
        print("No se pudo recibir el cuadro (fin de la transmisión).")
        break

    # Mostrar el cuadro en una ventana llamada 'Hola Mundo'
    cv2.imshow('Hola Mundo', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar el objeto de captura y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
