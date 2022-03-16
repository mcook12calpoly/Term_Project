'''! @file      Pen.py
                This program includes functions for initializing a Pen state controller, and setting a servo driver to one of two positions.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 1, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import pyb
import time
from servodriver import ServoDriver

class Pen:
    '''! 
    This class implements a Pen object to interface with the servo. 
    '''

    def __init__ (self):
        '''! 
        '''
        #print ('Creating a pen')

    def down (self):
        '''!
        This method sets the position of the pen to down
        by sending corresponding PWM signal to the servo. 
        '''
        
        #Create a servo driver
        s1 = ServoDriver(pyb.Pin.board.PB3, 2)
        
        #Set the servo to its end position
        s1.set_duty_cycle(0)
            
    def up (self):
        '''!
        This method sets the position of the pen to up
        by sending corresponding PWM signal to the servo.
        '''
        
        ##Create a servo driver
        s1 = ServoDriver(pyb.Pin.board.PB3, 2)
        
        #Set the servo to its middle position
        s1.set_duty_cycle(70)
    



if __name__ == "__main__":
    p1=Pen()
    p1.up()
    time.sleep_ms(1000)
    p1.down()
    
    




