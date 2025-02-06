from machine import Pin, PWM
from utime import sleep


class Servo:
    def __init__(self, pin):
        self.pin = Pin(pin)
        self.servo = PWM(self.pin)
        self.servo.freq(100)
    
    def set_angle(self, angle):
        if angle < 0:
            angle = 0
        if angle > 180:
            angle = 180
        duty = int(500 + (angle * 20))
        self.servo.duty_u16(duty)

    def turn180(self):
        self.servo.duty_u16(17000)
    def turn90(self):
        self.servo.duty_u16(10500)
    def turn45(self):
        self.servo.duty_u16(7250)
    def turn0(self):
        self.servo.duty_u16(4000)
    def turnAngle(self, val):
        self.servo.duty_u16(int(val/180*13000+4000))


servo = Servo(20)
while True:
    servo.turn180()
    sleep(1)
    servo.turn90()
    sleep(1)
    servo.turn45()
    sleep(1)
    servo.turn0()
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)
    servo.turnAngle(180)
    sleep(1)
    servo.turnAngle(135)
    sleep(1)
    servo.turnAngle(90)
    sleep(1)
    servo.turnAngle(45)
    sleep(1)
    servo.turnAngle(0)
    sleep(1)