'''! @file      mainpage.py
                This page describes our software design for a 2.5 axis plotter.
    @author     Michael Cook
    @author     Derick Louie
    @date       February 22, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3

@mainpage Term Project

@section Software_Design Software Design


@subsection Task_Diagram Task Diagram
The figure below shows the task diagram for our plotter.
The user/main task allows the user to input a file to read G-Code from.
The user/main task then sends a single line of G-Code to the "G-Code to Position" task, which converts the G-Code to encoder setpoint values.
These setpoints are then passed to the encoder task, which sends PWM values for the motor based on the encoder value and setpoint.
When the movement has been completed, the encoder task sends a flag to the user/main task to indicate that the next line of G-Code is ready to be processed.
@image html Task_Diagram.png


@subsection User_Task User/Main Task FSM
The figure below shows the FSM diagram for the user/main task.
This task waits for the user to input a file to read G-Code from.
Once a file has been specified, it reads a single line. If share_d is true, this indicates that the previous movement has completed,
and the current line is stored in share variable share_g for use in "G-Code to Position" task.
@image html Main_FSM.png

@subsection G_Code G-Code to Position Task FSM
The figure below shows the FSM diagram for the G-Code to Position Task.
This task takes the data from share_g (1 line of G-Code) and parses it.
Depending on the first 3 characters of the line, different states are entered.
If the command is a movement command, the X and Y coordinates are translated to polar setpoints, and desired setpoint values are passed to the encoder task.
Otherwise, the command is performed and the task returns to state 0, waiting for data.
@image html G_Code_FSM.png

@subsection Encoder Encoder Task FSM
This task takes the position setpoints from the G code task and determines which motors/servo need to move and what PWM value to set each to.
The PWM values are shared to the motor driver via share_e.
The encoder position is read and if the desired setpoint is reached, the task will inform the main task via share_d and the task will wait for the next input.
If the setpoint has not been reached, the task will continue to determine PWM values to follow the inputted command.
@image html Encoder_FSM.png
'''