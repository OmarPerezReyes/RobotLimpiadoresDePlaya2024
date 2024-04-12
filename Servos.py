import RPi.GPIO as GPIO
import time

# Configuración de la Raspberry Pi
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)

# Crear objeto PWM para el servo motor
pwm = GPIO.PWM(servo_pin, 50)  # Frecuencia de 50 Hz (estándar para servos)

# Inicializar el servo en la posición de inicio
pwm.start(0)

try:
    while True:
        # Obtener el número del usuario
        choice = int(input("Ingrese 1 para 0° o 2 para 150°: "))
        
        # Ajustar el ángulo según la elección del usuario
        if choice == 1:
            angle = 0
        elif choice == 2:
            angle = 150
        else:
            print("Selección no válida. Intente nuevamente.")
            continue

        # Calcular el ciclo de trabajo correspondiente para el ángulo
        duty_cycle = (angle / 18) + 2

        # Mover el servo a la posición deseada
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)  # Pausa para dar tiempo al servo de llegar a la posición
        
except KeyboardInterrupt:
    # Detener PWM y limpiar configuraciones de GPIO al presionar Ctrl+C
    pwm.stop()
    GPIO.cleanup()
