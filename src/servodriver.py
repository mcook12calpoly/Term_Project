'''! @file      servodriver.py
                This program includes functions for the servo.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 15, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import pyb
import time

class ServoDriver:
    '''! 
    This class implements a servo driver for an 3-wire hobby servo. 
    '''

    def __init__ (self, inpin, timer):
        '''! 
        Creates a servo driver by initializing GPIO
        pins 
        @param inpin IN pin 
        @param timer Timer pin for PWM
        '''
        
        ## Reference for pin object for B3
        self.pinPB3 = pyb.Pin (inpin, pyb.Pin.OUT_PP)
        
        ## Reference for timer object tim2
        self.tim2 = pyb.Timer(timer, freq=50)
        
        ## Reference for timer 2 channel 2
        self.IN1 = self.tim2.channel(2, pyb.Timer.PWM, pin=self.pinPB3)
        
        #print ('Creating a servo driver')

    def set_duty_cycle (self, level):
        '''!
        This method sets the duty cycle to be sent
        to the servo to the given level. A 1ms pulse moves the servo
        to 0 degrees while a 2ms pulse sets it to 180 degrees.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        
        ##Convert 0-100 PWM values to 1-2ms pulse widths
        OldRange = (100 - 0)
        NewRange = (10 - 5)
        position = (((level - 0) * NewRange) / OldRange) + 5
        
        # 
        self.IN1.pulse_width_percent(abs(position))
            
        print ('Setting duty cycle to ' + str (level))



if __name__ == "__main__":
    driver = ServoDriver(pyb.Pin.board.PB3, 2)
    driver.set_duty_cycle(0)
    time.sleep_ms(1000)
    driver.set_duty_cycle(50)
    time.sleep_ms(2000)
    driver.set_duty_cycle(0)



