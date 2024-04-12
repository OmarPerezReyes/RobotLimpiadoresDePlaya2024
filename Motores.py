import RPi.GPIO as GPIO
import time

# Definición de pines para el primer motor
motor1_in1 = 17
motor1_in2 = 18
motor1_pwm_pin = 22

# Definición de pines para el segundo motor
motor2_in1 = 23
motor2_in2 = 24
motor2_pwm_pin = 25

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)

# Configuración del primer motor
GPIO.setup(motor1_in1, GPIO.OUT)
GPIO.setup(motor1_in2, GPIO.OUT)
GPIO.setup(motor1_pwm_pin, GPIO.OUT)
pwm_motor1 = GPIO.PWM(motor1_pwm_pin, 100)
pwm_motor1.start(0)

# Configuración del segundo motor
GPIO.setup(motor2_in1, GPIO.OUT)
GPIO.setup(motor2_in2, GPIO.OUT)
GPIO.setup(motor2_pwm_pin, GPIO.OUT)
pwm_motor2 = GPIO.PWM(motor2_pwm_pin, 100)
pwm_motor2.start(0)

# Funciones para controlar el movimiento de los motores
def adelante(motor_pwm):
    motor_pwm.ChangeDutyCycle(100)
    time.sleep(0.1)

def atras(motor_pwm):
    motor_pwm.ChangeDutyCycle(100)
    time.sleep(0.1)

def detener(motor_pwm):
    motor_pwm.ChangeDutyCycle(0)
    time.sleep(0.1)

try:
    while True:
        comando_motor1 = input("Presione 'a' para mover el motor 1 hacia adelante, 'b' para atrás, 'c' para detener: ")
        if comando_motor1 == 'a':
            print("Moviendo motor 1 hacia adelante")
            adelante(pwm_motor1)
        elif comando_motor1 == 'b':
            print("Moviendo motor 1 hacia atrás")
            atras(pwm_motor1)
        elif comando_motor1 == 'c':
            print("Deteniendo motor 1")
            detener(pwm_motor1)
        else:
            print("Comando no reconocido para motor 1")

        comando_motor2 = input("Presione 'd' para mover el motor 2 hacia adelante, 'e' para atrás, 'f' para detener: ")
        if comando_motor2 == 'd':
            print("Moviendo motor 2 hacia adelante")
            adelante(pwm_motor2)
        elif comando_motor2 == 'e':
            print("Moviendo motor 2 hacia atrás")
            atras(pwm_motor2)
        elif comando_motor2 == 'f':
            print("Deteniendo motor 2")
            detener(pwm_motor2)
        else:
            print("Comando no reconocido para motor 2")
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario")
finally:
    GPIO.cleanup()
