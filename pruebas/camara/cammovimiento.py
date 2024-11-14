import cv2
import mediapipe as mp

# Inicializar MediaPipe para detección de poses
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Configurar captura de video
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Crear una ventana de OpenCV
cv2.namedWindow('Detección de Cuerpo', cv2.WINDOW_NORMAL)

# Procesar cada 5 cuadros para optimizar el rendimiento
frame_interval = 5
frame_count = 0

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print("No se pudo recibir el cuadro (fin de la transmisión).")
            break

        frame_count += 1
        if frame_count % frame_interval != 0:
            continue

        # Convertir a RGB para MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Realizar detección de pose
        results = pose.process(rgb_frame)

        # Volver a BGR para mostrarlo con OpenCV
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

        # Dibujar las conexiones de la pose y verificar si las manos están levantadas
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Obtener las posiciones de los puntos de los hombros y las manos
            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

            # Verificar si ambas manos están por encima de los hombros
            if left_wrist.y < left_shoulder.y and right_wrist.y < right_shoulder.y:
                cv2.putText(frame, "Manos levantadas!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Mostrar el cuadro en la ventana
        cv2.imshow('Detección de Cuerpo', frame)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) == ord('q'):
            break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
