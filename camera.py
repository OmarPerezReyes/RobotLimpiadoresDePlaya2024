import cv2

# Función para capturar video desde la cámara
def capture_video():
    # Instanciar el objeto VideoCapture para acceder a la cámara
    cap = cv2.VideoCapture(0)  # El argumento 0 indica que se usará la primera cámara disponible
    
    # Verificar si la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return
    
    # Ciclo para capturar y mostrar el video en vivo
    while True:
        # Capturar frame por frame
        ret, frame = cap.read()
        
        # Verificar si la captura fue exitosa
        if not ret:
            print("Error: No se pudo capturar el frame.")
            break
        
        # Mostrar el frame en una ventana
        cv2.imshow('Camera', frame)
        
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar la cámara y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para capturar video
capture_video()

