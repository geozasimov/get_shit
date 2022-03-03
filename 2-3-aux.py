import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

number = [0 for i in range(len(leds))]
for i in range(len(leds)):
    number[i] = 1
    GPIO.output(leds, number)
    time.sleep(1)

while(True):
    for i in range(len(leds)):
        GPIO.output(leds[i], GPIO.input(aux[i]))
    
GPIO.cleanup()