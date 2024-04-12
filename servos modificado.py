import RPi.GPIO as GPIO
import time
import keyboard

# Configuración de la Raspberry Pi
GPIO.setmode(GPIO.BCM)

# Configuración de los servomotores
servo_pins = [18, 19, 20, 21]
duty_cycles = [0, 0, 0, 0]

for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)
    duty_cycles[servo_pins.index(pin)] = 0

# Posiciones iniciales y finales para los servomotores
initial_positions = [0, 0, 0, 0]
final_positions = [150, 150, 0, 0]
intermediate_positions = [75, 75]

# Funciones para mover los servomotores
def move_servo(servo_index, position):
    duty_cycle = (position / 18) + 2
    duty_cycles[servo_index] = duty_cycle
    pwm.ChangeDutyCycle(duty_cycle)

def reset_servo(servo_index):
    move_servo(servo_index, initial_positions[servo_index])
    time.sleep(1)

# Funciones para controlar los pares de servomotores
def move_pair(pair_index, position):
    if pair_index == 0:
        move_servo(2 * pair_index, position)
        move_servo(2 * pair_index + 1, position)
    elif pair_index == 1:
        move_servo(2 * pair_index, position)
        move_servo(2 * pair_index + 1, intermediate_positions[pair_index - 1])
        move_servo(2 * pair_index + 1, position)

def reset_pair(pair_index):
    if pair_index == 0:
        reset_servo(2 * pair_index)
        reset_servo(2 * pair_index + 1)
    elif pair_index == 1:
        reset_servo(2 * pair_index)
        reset_servo(2 * pair_index + 1)

# Control de teclas
def key_press(key):
    if key == '1':
        move_pair(0, final_positions[0])
    elif key == '2':
        move_pair(1, final_positions[2])
    elif key == '3':
        reset_pair(0)
    elif key == '4':
        reset_pair(1)

keyboard.on_press(key_press)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    # Detener PWM y limpiar configuraciones de GPIO al presionar Ctrl+C
    for pin in servo_pins:
        pwm.stop()
        GPIO.cleanup(pin)