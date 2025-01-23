from machine import ADC,Pin, PWM
from utime import sleep

PACE= 250
TIMEOUT = 0.01
led = PWM(Pin(18))

led.freq(500)
val=0
while True:
    while val < 65535:
        val = val + PACE
        sleep(TIMEOUT)
        led.duty_u16(val)
    while val > 0:
        val = val - PACE
        sleep(TIMEOUT)
        led.duty_u16(val)