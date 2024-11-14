import cv2
import mediapipe as mp
import time

# Inicializar MediaPipe para detección de poses
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Configurar captura de video a baja resolución (por ejemplo, 640x480)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Crear una ventana de OpenCV
cv2.namedWindow('Detección de Cuerpo', cv2.WINDOW_NORMAL)

# Variables para controlar el procesamiento de cuadros
frame_interval = 2  # Procesar cada 2 cuadros
frame_count = 0

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("No se pudo recibir el cuadro (fin de la transmisión).")
            break

        # Solo procesar uno de cada 'frame_interval' cuadros
        frame_count += 1
        if frame_count % frame_interval != 0:
            continue

        # Convertir a RGB para MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Realizar detección de pose
        results = pose.process(rgb_frame)

        # Volver a BGR para mostrarlo con OpenCV
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

        # Dibujar solo si se detectan los puntos de referencia de la pose
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Mostrar el cuadro en la ventana
        cv2.imshow('Detección de Cuerpo', frame)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) == ord('q'):
            break

# Liberar la cámara y cerrar ventana
cap.release()
cv2.destroyAllWindows()
