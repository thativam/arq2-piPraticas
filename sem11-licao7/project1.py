from machine import ADC,Pin, PWM
from utime import sleep

led = PWM(Pin(18))
SENSOR_PIN = ADC(0)

led.freq(500)

while True:
    val = SENSOR_PIN.read_u16()
    led.duty_u16(val)
    