from machine import Pin, I2C
from utime import sleep
from lcd1602 import LCD1602

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)


d.display()
sleep(1)

d.clear()
d.print(' Ola')
sleep(1)
d.setCursor(0,1) #linha, coluna (???)
d.print(' Professor')