'''! @file      switch.py
                This program includes functions for initializing a switch, and determining the current state of the switch depending on input values.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 1, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import pyb
import time

class Switch:
    '''! 
    This class implements a Switch object to determine the current state of a limit switch. 
    '''
    
    def __init__ (self, inpin):
        '''! 
        '''
        self.pinSwitch = pyb.Pin (inpin, pyb.Pin.IN, pyb.Pin.PULL_UP)
        
    def state (self):
        '''!
        This method sets the state of the switch by reading the digital input
        and determining if it is open or closed. 
        '''
        if(self.pinSwitch.value()==1):
            print(1)
            return 1
        elif(self.pinSwitch.value()==0):
            print(0)
            return 0

if __name__ == "__main__":
    while(1):
        switch = Switch(pyb.Pin.board.PB8)
        switch.state()
        time.sleep_ms(10)
        