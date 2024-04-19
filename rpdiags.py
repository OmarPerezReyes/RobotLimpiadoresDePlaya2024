import RPi.GPIO as GPIO
import time 

out1 = 16 

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(out1, GPIO.OUT)

    #GPIO.output(out1, GPIO.HIGH)  # Enciende el pin

    time.sleep(4)  # Espera 20 segundos

    
finally:
	GPIO.output(out1, GPIO.LOW)  # Apaga el pin
	time.sleep(1)
	GPIO.cleanup()  # Limpia los pines GPIO al salir del programa, incluso si ocurre un error
