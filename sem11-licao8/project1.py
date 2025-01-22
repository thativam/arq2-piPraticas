from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(27))



def DO(time=1, volume=1000):
    buzzer.freq(1046)
    buzzer.duty_u16(volume)
    sleep(time)

def RE(time=1, volume=1000):
    buzzer.freq(1175)
    buzzer.duty_u16(volume)
    sleep(time)

def MI(time=1, volume=1000):
    buzzer.freq(1318)
    buzzer.duty_u16(volume)
    sleep(time)

def FA(time=1, volume=1000):
    buzzer.freq(1397)
    buzzer.duty_u16(volume)
    sleep(time)

def SOL(time=1, volume=1000):
    buzzer.freq(1568)
    buzzer.duty_u16(volume)
    sleep(time)

def LA(time=1, volume=1000):
    buzzer.freq(1760)
    buzzer.duty_u16(volume)
    sleep(time)

def SI(time=1, volume=1000):
    buzzer.freq(1967)
    buzzer.duty_u16(volume)
    sleep(time)

def END():
    buzzer.duty_u16(0)
    


while True:
    DO()
    RE()
    MI()
    FA()
    SOL()
    LA()
    SI()
    END()
    