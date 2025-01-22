from machine import ADC
from utime import sleep


SENSOR_PIN = ADC(0)

while True:
    print(SENSOR_PIN.read_u16())
    sleep(1)