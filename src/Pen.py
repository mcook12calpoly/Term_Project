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
        This method sets the position of the pen to up
        by sending corresponding PWM signal to the servo.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        
        ##Create a servo driver
        s1 = ServoDriver(pyb.Pin.board.PB3, 2)
        
        #
        s1.set_duty_cycle(0)
            
    def up (self):
        '''!
        This method sets the position of the pen to down
        by sending corresponding PWM signal to the servo.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        
        ##Create a servo driver
        s1 = ServoDriver(pyb.Pin.board.PB3, 2)
        
        #
        s1.set_duty_cycle(70)
    



if __name__ == "__main__":
    p1=Pen()
    p1.up()
    time.sleep_ms(1000)
    p1.down()
    
    




