import pyb
from motordriver import MotorDriver
from switch import Switch

class Home:
    def __init__ (self, motor)
    motor = MotorDriver(motor)
    switch = Switch(PB0)
    while (switch.state() == 0):
        motor.set_duty_cycle(100)
        if (switch.state() == 1):
            motor.set_duty_cycle(0)
            break
        