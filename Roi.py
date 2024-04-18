import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo TensorFlow Lite
interpreter = tf.lite.Interpreter(model_path="modelo.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Función para detectar objetos en un frame
def detect_objects(frame):
    input_data = np.expand_dims(frame, axis=0)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    boxes = interpreter.get_tensor(output_details[0]['index'])
    return boxes

# Función para verificar si la zona de interés contiene objetos
def check_interest_zone(boxes, width, height):
    for box in boxes[0]:
        ymin, xmin, ymax, xmax = box
        ymin = int(ymin * height)
        xmin = int(xmin * width)
        ymax = int(ymax * height)
        xmax = int(xmax * width)
        # Definir la zona de interés (en este caso, el centro del frame)
        center_x = width // 2
        center_y = height // 2
        if center_x > xmin and center_x < xmax and center_y > ymin and center_y < ymax:
            return True
    return False

# Abrir el video
cap = cv2.VideoCapture("video.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar objetos en el frame
    boxes = detect_objects(frame)

    # Verificar si algún objeto está en la zona de interés
    if check_interest_zone(boxes, frame.shape[1], frame.shape[0]):
        print("¡Encontrado!")

    # Mostrar el frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

