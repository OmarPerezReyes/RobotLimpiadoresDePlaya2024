import RPi.GPIO as GPIO
import time
import sys

# Definición de pines para motor 1
IN1 = 18  # Pin de dirección motor 1
IN2 = 27  # Pin de dirección motor 1

# Definición de pines para motor 2
IN3 = 23  # Pin de dirección motor 2
IN4 = 24  # Pin de dirección motor 2

# Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

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

# Lógica principal del programa
try:
    while True:
        command = input("Enter command (w: forward, s: backward, a: left, d: right, x: stop, q: quit): ")
        if command == 'w':
            forward()
            print("Forward")
        elif command == 's':
            backward()
            print("Backward")
        elif command == 'a':
            left()
            print("Turn left")
        elif command == 'd':
            right()
            print("Turn right")
        elif command == 'x':
            stop()
            print("Stop")
        elif command == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid command")

except KeyboardInterrupt:
    stop()  # Detiene los motores al presionar Ctrl+C

finally:
    GPIO.cleanup()  # Limpia los pines GPIO al salir del programa

