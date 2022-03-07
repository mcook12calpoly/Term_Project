import pyb
import time
from encoder import Encoder
from motordriver import MotorDriver
from switch import Switch

class Home:
    def __init__ (self):
        #self.switch = Switch(pyb.Pin.board.PC2)
        self.switch = Switch(pyb.Pin.board.PB8)
    
    def goHome (self, motor, encoder, state):
        while (self.switch.state() == state):
            motor.set_duty_cycle(50)
            time.sleep_ms(10)
        motor.set_duty_cycle(0)
        print("duty set to 0")
        encoder.zero()
        
if __name__ == "__main__":
    home = Home()
    #motor = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    #encoder = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    #home.goHome(motor, encoder, 0)
    motor2 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    encoder2 = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    home.goHome(motor2, encoder2, 1)
