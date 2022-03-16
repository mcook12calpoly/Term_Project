'''! @file      home.py
                This program includes functions for initializing a home class, and sending the motors to their home positions.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 1, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import pyb
import time
from encoder import Encoder
from motordriver import MotorDriver
from switch import Switch

class Home:
    '''! 
    This class implements a Home object to interface with the motors. 
    '''
    def __init__ (self):
        pass
    
    def goHome (self, motor, encoder, switch, state, speed):
        '''!
        This method drives the motors until their corresponding limit switch is pressed,
        indicating that the home position is reached, then stopping the motors.
        @param motor Motor to home
        @param encoder Encoder associated with motor
        @param switch Switch associated with motor
        @param state Switch state
        @param speed Speed to home at
        '''
        while (switch.state() == state):
            #move the motor at the specified speed
            motor.set_duty_cycle(speed)
            time.sleep_ms(10)
        #stop the motor once the switch is pressed
        motor.set_duty_cycle(0)
        #set the encoder's position to 0
        encoder.zero()
        
if __name__ == "__main__":
    home = Home()
    motor = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    encoder = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    switch_screw = Switch(pyb.Pin.board.PC2)
    home.goHome(motor, encoder, switch_screw, 0, 75)
    motor2 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    encoder2 = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    switch_wheel = Switch(pyb.Pin.board.PB8)
    home.goHome(motor2, encoder2, switch_wheel, 1, 50)
