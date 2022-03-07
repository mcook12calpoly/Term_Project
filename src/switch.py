import pyb
import time

class Switch:
    
    def __init__ (self, inpin):
        self.pinSwitch = pyb.Pin (inpin, pyb.Pin.IN, pyb.Pin.PULL_UP)
        #self.adc = pyb.ADC(pinSwitch)
        
    def state (self):
        #print(self.adc.read())
        #if(self.adc.read() < 200):
        if(self.pinSwitch.value()==1):
            print(1)
            return 1
        #elif(self.adc.read() >= 200):
        elif(self.pinSwitch.value()==0):
            print(0)
            return 0

if __name__ == "__main__":
    while(1):
        switch = Switch(pyb.Pin.board.PB8)
        switch.state()
        time.sleep_ms(10)
        