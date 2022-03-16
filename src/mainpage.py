'''! @file      mainpage.py
                This page describes our software design for a 2.5 axis plotter.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 15, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3

@mainpage Term Project

@section Software_Design Software Design


@subsection Task_Diagram Task Diagram
The figure below shows the task diagram for our plotter.
The read task takes values from the setpoint file and stores them in two queues- one for theta and one for r
The move task takes setpoints from the queues and commands the motors to move to those setpoints
The encoder task updates the encoder values and stores them in two shared variables- one for theta and one for r
@image html Task_Diagram.png

@subsection Move Task FSM
The figure below shows the FSM diagram for the move task.
The task begins by waiting for the s_done variable to update. This variable indicates if the previous movement is complete.
If the movement is not complete, then the task continues to move to the last setpoint by running again with the previous setpoints.
If the movement is complete, then new setpoints are loaded and movement begins.
@image html Main_FSM.png

@subsection Encoder Encoder Task FSM
The encoder task updates the encoder values and stores them in shared variables for use in other tasks and functions.
@image html Encoder_FSM.png

@subsection Read Read Task FSM
The read task waits for queue space and places setpoint values into queues for use in move task.
@image html Read_FSM.png

@subsection G_Code G-Code to Position Program FSM
The figure below shows the FSM diagram for the G-Code to Position Task.
This task takes the data from the G-code file and parses it.
Depending on the first 3 characters of the line, different states are entered.
If the command is a movement command, the X and Y coordinates are translated to polar setpoints, and desired setpoint values are stored in a list.
Once the values are stored in a list, the program loops and reads the next line of G-code.
@image html G_Code_FSM.png


'''