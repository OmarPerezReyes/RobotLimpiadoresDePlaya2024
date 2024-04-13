import cv2

# Ruta al archivo XML del clasificador pre-entrenado
cascPath = 'haarcascade_frontalface_default.xml'

# Cargar el clasificador pre-entrenado para detección de caras
faceCascade = cv2.CascadeClassifier(cascPath)

# Función para capturar video desde la cámara y detectar objetos
def detect_objects():
    # Instanciar el objeto VideoCapture para acceder a la cámara
    cap = cv2.VideoCapture(0)  # El argumento 0 indica que se usará la primera cámara disponible
    
    # Verificar si la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return
    
    # Ciclo para capturar y detectar objetos en el video en vivo
    while True:
        # Capturar frame por frame
        ret, frame = cap.read()
        
        # Convertir el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detectar caras en el frame
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Dibujar un rectángulo alrededor de las caras detectadas
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Mostrar el frame con las caras detectadas en una ventana
        cv2.imshow('Face Detection', frame)
        
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar la cámara y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para detectar objetos
detect_objects()

