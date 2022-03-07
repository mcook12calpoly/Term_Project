class Controller:
    
    def __init__ (self, motor_theta, encoder_theta, motor_r, encoder_r):
        
        self.motor_theta = motor_theta
        self.encoder_theta = encoder_theta
        
        self.motor_r = motor_r
        self.encoder_r = encoder_r
        
    def moveto (self, target_theta, speed_theta, theta_threshold, target_r, speed_r, r_threshold):
        
        if (abs(target_theta - encoder_theta) > theta_threshold):
            if (encoder_theta > target_theta):
                self.motor_theta.set_duty_cycle(speed_theta)
            else:
                self.motor_theta.set_duty_cycle(-speed_theta)
        
        if (abs(target_r - encoder_r) > r_threshold):
            if (encoder_r > target_r):
                self.motor_r.set_duty_cycle(speed_r)
            else:
                self.motor_r.set_duty_cycle(-speed_r)
        
if __name__ == "__main__":

    enc_wheel = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc_screw = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    motor_wheel = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    motor_screw = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    
    