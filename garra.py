import RPi.GPIO as GPIO
import time
import sys
import tty
import termios

PIN_SERVO = 12  # El número de pin GPIO que estás usando

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SERVO, GPIO.OUT)

# Crea un objeto PWM (Modulación de Ancho de Pulso) en el pin servo
pwm = GPIO.PWM(PIN_SERVO, 50)  # 50Hz (20ms period)

# Inicializa el PWM con un ciclo de trabajo del 0%
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(PIN_SERVO, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(PIN_SERVO, False)
    pwm.ChangeDutyCycle(0)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

try:
    while True:
        char = getch()
        if char == '1':
            set_angle(30)   # Mueve el servo a 0 grados
        elif char == '2':
            set_angle(140)  # Mueve el servo a 30 grados

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
