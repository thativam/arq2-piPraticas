from machine import Pin, I2C, ADC
from utime import sleep

class LCD1602:
    def __init__(self, i2c, addr=0x27):
        self.i2c = i2c
        self.addr = addr
        self._send(0x03)
        self._send(0x03)
        self._send(0x03)
        self._send(0x02)

        self._send(0x28)  # 4-bit mode, 2 lines, 5x8 dots
        self._send(0x0C)  # Display on, no cursor
        self._send(0x06)  # Entry mode set
        self._send(0x01)  # Clear display
        sleep(0.002)

    def _send(self, data, mode=0):
        high = mode | (data & 0xF0) | 0x08
        low = mode | ((data << 4) & 0xF0) | 0x08
        self.i2c.writeto(self.addr, bytes([high, high & ~0x04]))
        self.i2c.writeto(self.addr, bytes([low, low & ~0x04]))

    def print(self, message):
        for char in message:
            self._send(ord(char), 0x01)

    def clear(self):
        self._send(0x01)
        sleep(0.002)

    def set_cursor(self, col, row):
        pos = 0x80 + (0x40 * row) + col
        self._send(pos)


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