'''! @file      controller.py
                This program includes functions for the motor controller, moving the machine to setpoints.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 15, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

class Controller:
    
    def __init__ (self, motor_theta, encoder_theta, motor_r, encoder_r, pen, done_flag):
        '''! 
        Initializes variables and passes motors, encoders, servo, and shared variable in.
        @param motor_theta Motor that controls theta axis
        @param encoder_theta Encoder for theta axis
        @param motor_r Motor that controls r axis
        @param encoder_r Encoder for r axis
        @param pen Pen object
        @param done_flag Shared variable indicating if last setpoint has been reached
        '''        
        self.motor_theta = motor_theta
        self.encoder_theta = encoder_theta
        
        self.motor_r = motor_r
        self.encoder_r = encoder_r
        
        self.done_flag = done_flag
        
        self.pen = pen
        
    def moveto (self, target_theta, speed_theta, target_r, speed_r, target_pen, theta_threshold = 350, r_threshold = 500):
        '''! 
        Moves motors to setpoint with a certain speed and threshold
        @param target_theta Theta axis setpoint
        @param speed_theta Theta axis speed
        @param target_r r axis setpoint
        @param speed_r r axis speed
        @param target_pen Pen setpoint
        @param theta_threshold Acceptable threshold(error) from setpoint for theta axis
        @param r_threshold Acceptable threshold(error) from setpoint for r axis
        
        '''        
        # thresholds in ticks
        # 4.3125 inches = 112000 ticks
        # 180 degrees = 44000 ticks
        
        target_theta = target_theta * 44000 / 180
        target_r = target_r * 112000 / 4.3125
        
        if (abs(target_theta - self.encoder_theta.get()) < theta_threshold):
            self.motor_theta.set_duty_cycle(0)
            self.done_flag.put(1)
            #print("WITHIN THRESHOLD")
            
        elif (self.encoder_theta.get() > target_theta):
            self.motor_theta.set_duty_cycle(speed_theta)
            #print("still good", self.encoder_r.get())
            
        elif (self.encoder_theta.get() < target_theta):
            self.motor_theta.set_duty_cycle(-speed_theta)
    
        if (abs(target_r - self.encoder_r.get()) < r_threshold):
            self.motor_r.set_duty_cycle(0)
            self.done_flag.put(1)
            #print("WITHIN THRESHOLD")
            
        elif (self.encoder_r.get() > target_r):
            self.motor_r.set_duty_cycle(speed_r)
            #print("still good", self.encoder_r.get())
            
        elif (self.encoder_r.get() < target_r):
            self.motor_r.set_duty_cycle(-speed_r)
            
        if target_pen == 1:
            self.pen.down()
            
        elif target_pen == 0:
            self.pen.up()
            

        
if __name__ == "__main__":

    enc_wheel = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc_screw = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    motor_wheel = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    motor_screw = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    
    
