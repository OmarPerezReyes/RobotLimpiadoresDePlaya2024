from gpiozero import AngularServo
from time import sleep

# Conecta el servo motor a la GPIO 17
servo_pin = 12

# Crea un objeto AngularServo para controlar el servo
servo = AngularServo(servo_pin, min_angle=0, max_angle=180)

# Mueve el servo a la posición central
servo.angle = 90
sleep(1)

# Mueve el servo a la posición máxima hacia la izquierda
servo.angle = 0
sleep(1)

# Mueve el servo a la posición máxima hacia la derecha
servo.angle = 180
sleep(1)

# Mueve el servo a través de un rango completo en pasos de 2 grados
for angle in range(0, 181, 2):
    servo.angle = angle
    sleep(0.1)

# Mueve el servo de regreso a la posición central
servo.angle = 90
sleep(1)

# Detén el servo
servo.detach()

