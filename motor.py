import RPi.GPIO as GPIO
import time

# Definición de pines del BTS7960
in1 = 17
in2 = 18
pwm_pin = 22  # Cambia este pin por el que desees utilizar

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)  # PWM con frecuencia de 100 Hz
pwm.start(0)

def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    pwm.ChangeDutyCycle(100)  # Velocidad máxima

def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    pwm.ChangeDutyCycle(100)  # Velocidad máxima

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        command = input("Presione 'r' para girar a la derecha, 'l' para girar a la izquierda, 's' para detener: ")
        if command == 'r':
            print("Girando a la derecha")
            forward()
        elif command == 'l':
            print("Girando a la izquierda")
            backward()
        elif command == 's':
            print("Deteniendo")
            stop()
        else:
            print("Comando no reconocido")
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario")
finally:
    GPIO.cleanup()
