import RPi.GPIO as GPIO
import time
import sys
import cv2
import numpy as np

# Definición de pines para motor 1
IN1 = 18  # Pin de dirección motor 1
IN2 = 27  # Pin de dirección motor 1

# Definición de pines para motor 2
IN3 = 23  # Pin de dirección motor 2
IN4 = 24  # Pin de dirección motor 2
out1 = 16 

# Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(out1, GPIO.OUT)

# Función para mover ambos motores hacia adelante
def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Función para mover ambos motores hacia atrás
def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# Función para girar a la izquierda
def left():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# Función para girar a la derecha
def right():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Función para detener
def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    
# Función para detectar la tonalidad azul-celeste y negra en una imagen
def detectar_tonalidad(imagen):
    # Convertir la imagen de BGR a HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    
    # Definir el rango de tonalidades azules-celestes en HSV
    lower_azul_celeste = np.array([85, 100, 100])
    upper_azul_celeste = np.array([110, 255, 255])
    
    # Definir el rango de tonalidades negras en HSV
    lower_negro = np.array([0, 0, 0])
    upper_negro = np.array([180, 255, 20])
    
    # Aplicar la máscara para encontrar los píxeles en el rango de azul-celeste
    mask_azul_celeste = cv2.inRange(hsv, lower_azul_celeste, upper_azul_celeste)
    # Aplicar la máscara para encontrar los píxeles en el rango de negro
    mask_negro = cv2.inRange(hsv, lower_negro, upper_negro)
    
    # Calcular el porcentaje de píxeles azul-celestes y negros
    total_pixeles = np.prod(imagen.shape[:2])
    pixeles_azul_celeste = cv2.countNonZero(mask_azul_celeste)
    porcentaje_azul_celeste = (pixeles_azul_celeste / total_pixeles) * 100

    pixeles_negro = cv2.countNonZero(mask_negro)
    porcentaje_negro = (pixeles_negro / total_pixeles) * 100
    
    return porcentaje_azul_celeste, porcentaje_negro

# Inicializar la cámara web
cam = cv2.VideoCapture(0)

# Inicializar el contador
contador = 0

# Lógica principal del programa
try:
    while True:
        forward()
        time.sleep(0.5);
        GPIO.output(out1, GPIO.LOW)  # Apaga el pin
        # Capturar imagen de la cámara
        ret, frame = cam.read()
        
        # Incrementar el contador
        contador += 1
        
        # Revisar la tonalidad cada 10 frames
        if contador == 30:
            # Llamar a la función para detectar la tonalidad azul-celeste y negra
            porcentaje_azul_celeste, porcentaje_negro = detectar_tonalidad(frame)

            # Mostrar el porcentaje de tonalidad azul-celeste y negra
            #print("Porcentaje de tonalidad azul-celeste en el imagen:", porcentaje_azul_celeste)
            #print("Porcentaje de tonalidad negra en la imagen:", porcentaje_negro)
            
            if porcentaje_azul_celeste > 50:
                #print("AGUA")
                stop()
                time.sleep(1)
                backward()
                time.sleep(2.5)
                right()
                time.sleep(2)
                forward()
                
            if porcentaje_negro > 40:
                #print("LATA")
                stop()
                time.sleep(0.5);
                backward()
                time.sleep(1.5);
                GPIO.output(out1, GPIO.HIGH)  # Enciende el pin
                forward()
                GPIO.output(out1, GPIO.LOW)  # Apaga el pin
                time.sleep(3.5);
                GPIO.output(out1, GPIO.LOW)  # Apaga el pin
            
            # Reiniciar el contador
            contador = 0

        # Mostrar la imagen
        cv2.imshow('Frame', frame)
        
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    stop()  # Detiene los motores al presionar Ctrl+C

finally:
    GPIO.cleanup()  # Limpia los pines GPIO al salir del programa

