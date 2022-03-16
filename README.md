# Term Project - Plotting Machine

For this term project, a 2.5 axis plotting machine was contructed using a pivoting arm driven by a motor attached to a wheel at the end of the arm. Alongside the arm, a lead screw driven by a second motor which will move a pen carrier linearly along the arm. Within the pen carrier is a servo attached to the pen to raise and lower the pen. A small piece wraps around tip of the pen to allow the servo arm to push it upwards. The body of the arm and the base is made of square metal tubing and the pen chassis as well as the coupling piece that connects the arm and carrier to keep the pen carrier upright will be 3D printed. The pivoting mechanism includes a bearing to minimize slop in our rotation. Limit switches are used to signal when the arm is in its home position. The encoders included with the motors are used to track the movement of the arm and determine the pen's location. The code uses kinematic calculations to convert the x,y plot directions to the curvilinear movement of the arm and pen carrier.

---

### Bill of Materials

| Qty. | Part                  | Source                | Est. Cost |
|:----:|:----------------------|:----------------------|:---------:|
|  2   | Pittman Gearmotors    | ME405 Tub             |     -     |
|  1   | Nucleo with Shoe      | ME405 Tub             |     -     |
|  1   | Nucleo Motor Driver   | ME405 Tub             |     -     |
|  5   | Hobby Micro Servo     | Amazon&trade;         |   $8.99   |
|  1   | 400mm Lead Screw      | Amazon&trade;         |   $12.99  |
|  1   | 96" Square Metal Tube | Home Depot&trade;     |   $22.26  |
|  1   | Triplus Fineliner Pen | Already Owned         |   $1.29   |
|  1   | Chassis for servo/pen | 3D Printer            |     -     |
|  1   | Limit Switch          | Already Owned         |     -     |
|  2   | Wheel              | 3D Printer            |     -     |


---
### Hardware Design
The frame for our machine was constructed of aluminum tubing and 3d printed connectors. The central connector had mounting points for the pivot arm's limit switch as well as the hinge for the pivot arm. The pivot arm was also constructed out of alumininum tubing with a 3d printed motor mount and coupler at the end that attached to a 3d printed wheel with rubber bands for grip. Opposite the wheel on the arm is another 3d printed motor mount and coupler that operated the lead screw which is supported by a bearing on the other end placed within the wheel motor's mount. The pen holder was also 3d printed and made to wrap around the pivot arm and move with the lead screw by attaching to the copper nut provided with the lead screw. 

![projectsketch1](/docs/sketch1.png)
![projectsketch2](/docs/sketch2.png)
![projectsketch3](/docs/sketch3.png)


---
### Software Design
The software begins with a custom GCode file that is processed through a script that goes line by line and convcerts each command into polar setpoints of r and theta and a pen state(up or down). This processed list of setpoints is then loaded on the board where it can be read by the main file, with each line placed in a queue. After initially sending both motors (screw and wheel) back to their home positions near the origin, three tasks are created and added to the task list: update encoder, move and read. The update encoder task updates the encoder drivers to get the current position values for both motors, the move task moves the motors (and pen servo if applicable) until their corresponding enocders reach the current setpoint on the top of the queue. The read task adds each line of setpoints to the queue one at a time.

Link to Doxygen: https://mcook12calpoly.github.io/Term_Project/

---
### Results
After some initial testing and reworking of our software, the first successful drawing was of a rectangle. Due to the changes made on how the Gcode processing script determines the resolution of each line drawn, we were able to get much better looking and consistent long lines. The lines of the rectangle did not display any large zigzags as our device had been producing before the changes. However, the lines were not perfectly aligned and created angles that were not 90 degrees in the rectangle. We believe that this issue was due to the home position of our pen holder relative to the expected origin of our axis.

---
### Lessons Learned
The combination of 3d printed parts and aluminum tubing for the frame of the machine made the construction very durable for our testing uses and allowed the mechanical side of the machine to run without issue, leaving more time to focus on software.

We did not initially think to factor in the distance between the pivot(hinge) and the resting home position of the pen in its holder. This would have given us an offset radial value for what should be home or (0,0). This is likely why our rectange did not have straight angles in our testing. In addition, we learned quite a bit about task timing and efficiency. Reducing the period of certain tasks such as our move task and read task greatly improved the resolution of our machine, as it took less time for the next setpoint to be ready. 

If we were to write the code for this machine again, one improvement that we would make would be to implement Bresenham's line drawing algorithm, which would better help us calculate setpoints so that the steps in straight lines are less noticable. In addition to this, we would parse the setpoints and load them into memory before the machine runs, instead of parsing the setpoints each time the read task is called. This would likely improve the performance of our program, allowing us to run at finer setpoint resolutions. Although we didn't experience any issues with sensor resolution, their effect(especially on the wheel) could be noticable with better code performance. A potentiometer could be implemented on the pivot of the arms, which would allow for better accuracy and negate any error from wheel slippage. Also, the implementation of a PID controller could help with line smoothness due to the acceleration and decelleration of both axis.

---
