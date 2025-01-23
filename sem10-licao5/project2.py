from machine import Pin
from utime import sleep

led = Pin(16, Pin.OUT)
button = Pin(18,Pin.IN)

val=0
while True:
    print("val" + str(val) + " button" + str(button.value()))
    if button.value() == 1:
        val = val +1
        
    elif val > 1:
        val = 0
    
    led.value(val)
    sleep(0.5)