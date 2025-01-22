from machine import Pin

led = Pin(16, Pin.OUT)
button = Pin(18,Pin.IN)

while True:
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0)