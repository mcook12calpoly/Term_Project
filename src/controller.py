class Controller:
    
    def __init__ (self, motor_theta, encoder_theta, motor_r, encoder_r, done_flag):
        
        self.motor_theta = motor_theta
        self.encoder_theta = encoder_theta
        
        self.motor_r = motor_r
        self.encoder_r = encoder_r
        
        self.done_flag = done_flag
        
    def moveto (self, target_theta, speed_theta, target_r, speed_r, theta_threshold = 350, r_threshold = 500):
        
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

        
if __name__ == "__main__":

    enc_wheel = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc_screw = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    motor_wheel = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    motor_screw = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    
    
