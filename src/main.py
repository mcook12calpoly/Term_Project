import gc
import pyb
import cotask
import task_share
import time
from switch import Switch
from encoder import Encoder
from motordriver import MotorDriver
from home import Home
from controller import Controller


def task_encoder_update():
    while True:
        enc_wheel.update()
        enc_screw.update()
        
        s_enc_wheel.put(-enc_wheel.read())    
        s_enc_screw.put(enc_screw.read())

        print("Wheel:", s_enc_wheel.get(), "Screw:", s_enc_screw.get())
        print("stuck in encoder")
        yield (0)
        
def task_move():
    
    setpoint_theta = 0
    setpoint_r = 0
    
    while True:
        print("Theta setpoint:", setpoint_theta, "R setpoint:", setpoint_r)
        print("done flag:", s_done.get())
        
        if s_done.get() == 0:
            
            print("stuck beginning if")
            # target theta, theta speed, target r, r speed, theta threshold, r threshold
            controller.moveto(setpoint_theta, 50, setpoint_r, 75)
            print("stuck end if")
        
        else:
            if q_setpoints_theta.any():
                setpoint_theta = q_setpoints_theta.get()
                setpoint_r = q_setpoints_r.get()
                s_done.put(0)
                
            else:
                controller.moveto(setpoint_theta, 50, setpoint_r, 75)

        yield (0)
        
# def task_setpoints():
#     while True:
#         if s_done.get() == 1:
#             q_setpoints_theta.get()
#             
#             
#         s_done.put(0)
            
        
        
        

if __name__ == "__main__":
    
    # creating shares
    s_enc_screw = task_share.Share ('i', thread_protect = False, name = "screw encoder")
    
    s_enc_wheel = task_share.Share ('i', thread_protect = False, name = "wheel encoder")
    
    s_done = task_share.Share ('i', thread_protect = False, name = "done flag")
    
    q_setpoints_theta = task_share.Queue ('f', 100, thread_protect = False, overwrite = False, name = "theta setpoints")
    
    q_setpoints_r = task_share.Queue ('f', 100, thread_protect = False, overwrite = False, name = "r setpoints")
    
    q_setpoints_theta.put(140)
    q_setpoints_theta.put(90)
    q_setpoints_theta.put(140)
    q_setpoints_theta.put(90)
    
    q_setpoints_r.put(2)
    q_setpoints_r.put(1)
    q_setpoints_r.put(2)
    q_setpoints_r.put(1)
    
    # creating encoder objects
    enc_wheel = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc_screw = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    # creating motor objects
    motor_wheel = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    motor_screw = MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    
    # creating switch objects
    switch_wheel = Switch(pyb.Pin.board.PB8)
    switch_screw = Switch(pyb.Pin.board.PC2)
    
    # creating controller objects
    controller = Controller(motor_wheel, s_enc_wheel, motor_screw, s_enc_screw, s_done)
    
    home = Home()
    home.goHome(motor_screw, enc_screw, switch_screw, 0, 75)
    home.goHome(motor_wheel, enc_wheel, switch_wheel, 1, 50)
    
    del enc_screw
    del enc_wheel
    
    time.sleep_ms(500)
    
    enc_wheel = Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc_screw = Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)


    #q0 = task_share.Queue ('L', 16, thread_protect = False, overwrite = False,
    #                       name = "Queue 0")

    task1 = cotask.Task (task_encoder_update, name = 'update encoder', priority = 1, 
                         period = 50, profile = True, trace = False)

    task2 = cotask.Task (task_move, name = 'move', priority = 2, 
                         period = 50, profile = True, trace = False)
    
    cotask.task_list.append (task1)
    cotask.task_list.append (task2)

    gc.collect ()

    while (True):
        cotask.task_list.pri_sched ()
        





