import pyb

class Switch:
    
    def __init__ (self, inpin):
        pinSwitch = pyb.Pin (inpin, pyb.Pin.IN, pyb.Pin.PULL_UP)
        self.adc = pyb.ADC(pinSwitch)
        
    def state (self):
        print(self.adc.read())
        if(self.adc.read() < 500):
            print(1)
            return 1
        elif(self.adc.read() >= 500):
            print(0)
            return 0

if __name__ == "__main__":
    switch = Switch(pyb.Pin.board.PC0)
    switch.state()