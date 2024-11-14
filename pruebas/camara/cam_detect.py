import cv2
import mediapipe as mp

# Inicializar MediaPipe para detección de poses
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Iniciar captura de video
cap = cv2.VideoCapture(0)

# Crear una única ventana de OpenCV
cv2.namedWindow('Detección de Cuerpo', cv2.WINDOW_NORMAL)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("No se pudo recibir el cuadro (fin de la transmisión).")
            break

        # Convertir la imagen de BGR a RGB para MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Realizar la detección de la pose
        results = pose.process(rgb_frame)

        # Volver a BGR para mostrarlo con OpenCV
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

        # Dibujar las conexiones y puntos de la pose detectada
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Mostrar el cuadro en la ventana creada
        cv2.imshow('Detección de Cuerpo', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) == ord('q'):
            break

# Liberar la cámara y cerrar la ventana al final
cap.release()
cv2.destroyAllWindows()
