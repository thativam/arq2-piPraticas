from machine import Pin
from utime import sleep
led = Pin(16, Pin.OUT)
button = Pin(18,Pin.IN)

val=0
while True:
    if button.value() == 1:
        val = val +1
        sleep(1)
    else:
        val = 0
        sleep(1)
    led.value(val)