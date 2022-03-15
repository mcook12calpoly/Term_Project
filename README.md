# Term Project - Plotting Machine

For this term project, a 2.5 axis plotting machine will be contructed using a pivoting arm driven by a motor attached to a wheel at the end of the arm. Alongside the arm with the motor will be a lead screw driven by a second motor which will move a pen carrier linearly along the arm. Within the pen carrier will be a servo attached to the pen to raise and lower the pen. A small piece will be added near the tip of the pen to allow the servo arm to push it upwards. To keep tension on the pen as it is in its lower, writing position, a rubber band will be wrapped around the top of it. The body of the arm will be made of square metal tubing and the pen chassis as well as the coupling piece that connects the arm and carrier to keep the pen carrier upright will be 3D printed. The pivoting mechanism for the arm will have a bearing to minimize slop in our rotation. A limit switch will be used to signal when the arm is in its home position. The encoders included with them motors will be used to track the movement of the arm and determine the pen's location. The code will use kinematic calculations to convert the x,y plot directions to the curvilinear movement of the arm and pen carrier.
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
|  1   | Black Sharpie&trade;  | STAPLES&trade;        |   $1.29   |
|  1   | Chassis for servo/pen | 3D Printer            |     -     |
|  1   | Limit Switch          | Already Owned         |     -     |
|  2   | 3" Wheel              | 3D Printer            |     -     |
|  10  | 8x22x7 Wellgo Bearing | Amazon&trade;         |   $9.95   |


---
### Hardware Design
The frame for our machine was constructed of aluminum tubing and 3d printed connectors. The central connector had mounting points for the pivot arm's limit switch as well as the hinge for the pivot arm. The pivot arm was also constructed out of alumninum tubing with a 3d printed motor mount and coupler at the end that attached to a 3d printed wheel with rubber bands for grip. Opposite the wheel on the arm was another 3d printed motor mount and coupler which that and operated the lead screw which was supported by a bearing on the other end placed within the wheel motor's mount. The pen holder was also 3d printed and made to wrap around the pivot arm and move with the lead screw by attaching to the copper nut provided with the lead screw. 

![projectsketch1](/docs/sketch1.png)
![projectsketch2](/docs/sketch2.png)
![projectsketch3](/docs/sketch3.png)


---
### Software Design
The software begins with a custom GCode file that is processed through a script that goes line by line and convcerts each command into polar setpoints of r and theta and a pen state(up or down). This processed list of setpoints is then loaded on the board where it can be read by the main file and each line placed in a queue. After initially sending both motors (screw and wheel) back to their home positions near the origin, three tasks are created and added to the task list: update encoder, move and read. The update encoder task updates the encoder drivers to get the current position values for both motors, the move task moves the motors (and pen servo if applicable) until their corresponding enocders reach the current setpoint on the top of the queue. The read task adds each line of setpoints to the queue one at a time.
Link to Doxygen:

---
### Results
After some initial testing and reworking of our software, the first successful drawing was of a rectangle. Due to the changes made on how the Gcode processing script determines the resolution of each line drawn, which allowed us to get much better looking and consistent long lines, The lines of the rectangle did not display any large zigzags as our device had been producing before the changes. However, the lines were not perfectly aligned and created angles that were not 90 degrees in the rectangle. We believe that this issue was due to the home position of our pen holder relative to the expected origin of our axis.

---
### Lessons Learned
The use of 3d printing for the frame of the machine made the construction very durable for our testing uses and allowed the mechanical side of the machine to run without issue, leaving more time to focus on software.
We did not initially think to factor in the distance between the pivot(hinge) and the resting home position of the pen in its holder. This would have given us an offset radial value for what should be home or (0,0). This is likely why our rectange did not have straight angles in our testing.


---
### etc



---
