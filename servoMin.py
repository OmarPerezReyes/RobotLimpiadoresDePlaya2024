from gpiozero import Servo
from time import sleep

servo = Servo(14)

servo.min()
sleep(1)
servo.mid()
sleep(1)
servo.max()