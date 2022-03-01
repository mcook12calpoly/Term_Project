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

    def pos (self, pos):
        '''!
        This method sets the position of the pen
        to up or down by sending corresponding PWM signals
        to the servo.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        
        ##Create a servo driver
        s1 = ServoDriver(pyb.Pin.board.PB3, 2)
        
        #determine the corresponding PWM signal
        if (pos=="up"):
            s1.set_duty_cycle(50)
        elif(pos=="down"):
            s1.set_duty_cycle(0)



if __name__ == "__main__":
    p1=Pen()
    p1.pos("up")
    time.sleep_ms(1000)
    p1.pos("down")
    
    




