import RPi.GPIO as GPIO
import time

# Definir el número de pin GPIO que estás utilizando para el LED
PIN_LED = 12

# Configurar el modo de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

def check_pin(pin):
    GPIO.setup(pin, GPIO.IN)
    value = GPIO.input(pin)
    return value

try:
    # Encender el LED
    GPIO.output(PIN_LED, GPIO.HIGH)
    print("LED encendido")

except KeyboardInterrupt:
    # En caso de interrupción, limpiar los pines GPIO
    GPIO.cleanup()
