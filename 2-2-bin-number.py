import RPi.GPIO as GPIO
import time 
from random import randint 

def bin(x):
    n = ""
 
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    
    while len(n) < 8:
        n = '0' + n
    
    b = [None for i in range(len(n))]
    for i in range(len(b)):
        b[i] = int(n[i])
    return b

def ten(n):
    res = 1

    for i in range(len(n)):
        res += n[-i - 1] * (2 ** i)
    
    return res

GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
#number = [i % 2 for i in range(len(dac))]

GPIO.setup(dac, GPIO.OUT)

number = [randint(0,1) for i in range(len(dac))]

GPIO.output(dac, number)
print(ten(number))

time.sleep(5)

izm = [255, 127, 64, 32, 5, 0, 255]
zero = [0 for i in range(8)]
for i in range(len(izm)):
    GPIO.output(dac, bin(izm[i]))
    print(izm[i])
    time.sleep(5)
    GPIO.output(dac, zero)
    

GPIO.cleanup()