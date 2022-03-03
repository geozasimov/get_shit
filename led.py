import RPi.GPIO as GPIO
from math import abs

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while (True):
    input_value = GPIO.input(4)
    input_value = 1 - input_value
    GPIO.output(3, input_value)


