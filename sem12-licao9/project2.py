from machine import Pin, I2C, ADC
from utime import sleep
from lcd1602 import LCD1602

SENSOR_ANGULAR = ADC(0)
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)


d.display()


while True:
    sleep(1)
    d.clear()
    d.setCursor(0,0) #linha, coluna

    d.print(str(SENSOR_ANGULAR.read_u16()))
    sleep(1)