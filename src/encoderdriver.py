import pyb
import time

class ServoDriver:
    '''! 
    This class implements a motor driver for an ME405 kit. 
    '''

    def __init__ (self, inpin, timer):
        '''! 
        Creates a motor driver by initializing GPIO
        pins 
        @param in1pin IN1 pin 
        @param timer Timer pin for PWM
        '''
        
        ## Reference for pin object for B10
        self.pinPB3 = pyb.Pin (inpin, pyb.Pin.OUT_PP)
        
        ## Reference for timer object tim2
        self.tim2 = pyb.Timer(timer, freq=50)
        
        ## Reference for timer 2 channel 1
        self.IN1 = self.tim2.channel(2, pyb.Timer.PWM, pin=self.pinPB3)
        
        #print ('Creating a servo driver')

    def set_duty_cycle (self, level):
        '''!
        This method sets the duty cycle to be sent
        to the servo to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        
        
        OldRange = (100 - 0)
        NewRange = (10 - 5)
        position = (((level - 0) * NewRange) / OldRange) + 5
        
        # 
        self.IN1.pulse_width_percent(abs(position))
            
        print ('Setting duty cycle to ' + str (level))



if __name__ == "__main__":
    driver = ServoDriver(pyb.Pin.board.PB3, 2)
    driver.set_duty_cycle(0)
    #time.sleep_ms(1000)
    #driver.set_duty_cycle(100)
    #time.sleep_ms(1000)
    #driver.set_duty_cycle(50)



