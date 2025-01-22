from machine import ADC,Pin
from utime import sleep

led = Pin(16, Pin.OUT)
SENSOR_PIN = ADC(0)

while True:
    print(SENSOR_PIN.read_u16())
    if(SENSOR_PIN.read_u16() > 20000):
        led.value(1)
    else:
        led.value(0)
    sleep(1)