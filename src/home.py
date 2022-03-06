import pyb
import time
from motordriver import MotorDriver
from switch import Switch

class Home:
    def __init__ (self, en_pin, in1pin, in2pin, timer):
        self.motor = MotorDriver(en_pin, in1pin, in2pin, timer)
        self.switch = Switch(pyb.Pin.board.PC0)
    
    def goHome (self):
        while (self.switch.state() == 1):
            self.motor.set_duty_cycle(55)
        self.motor.set_duty_cycle(0)
        print("duty set to 0")
        
if __name__ == "__main__":
    home = Home(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    home.goHome()
