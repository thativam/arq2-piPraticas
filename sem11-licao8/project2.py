

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

def END(time=1):
    buzzer.duty_u16(0)
    sleep(time)
    
melodyPiratasCaribe = [
    (MI, 0.4), (SOL, 0.4), (LA, 0.2), (SOL, 0.2),
    (MI, 0.4), (SOL, 0.4), (LA, 0.2), (SI, 0.6),
    (DO, 0.4), (SI, 0.2), (LA, 0.4), (SOL, 0.2),
    (MI, 0.6), (SOL, 0.6), (LA, 0.4), (SOL, 0.2),
    (MI, 0.4), (SOL, 0.4), (LA, 0.2), (SI, 0.6),
    (DO, 0.4), (SI, 0.2), (LA, 0.4), (SOL, 0.2),
    (MI, 0.6), (SOL, 0.6), (MI, 0.6)
]

musicaExercicio8 = [(DO,0.25), (RE,0.25), (MI,0.25),
                    (DO,0.25), (END,0.01),(DO,0.25),
                    (RE,0.25), (MI,0.25),(DO,0.25),
                    (MI,0.25), (FA,0.25), (SOL,0.5),
                    (MI,0.25), (FA,0.25), (SOL,0.5),
                    (END,0.01),(SOL,0.125), (LA,0.125), 
                    (SOL,0.125), (FA,0.125), (MI,0.25),
                    (DO,0.25),(SOL,0.125), (LA,0.125), 
                    (SOL,0.125), (FA,0.125), (MI,0.25),
                    (DO,0.25), (RE,0.25),(SOL,0.25),
                    (DO,0.5), (END,0.01),(RE,0.25),(SOL,0.25),
                    (DO,0.5)]



def playMusic(melody):
    for i in melody:
        i[0](time=i[1])
        
while True:
    playMusic(musicaExercicio8)


