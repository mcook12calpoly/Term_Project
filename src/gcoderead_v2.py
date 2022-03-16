'''! @file      gcoderead_v2.py
                This program opens a stated gcode script, obtains the command and coordiante values from each line and creates a list of setpoints for each motor to move to.
                This program was to work for linear movement gcode commands by finding the r and theta setpoints using the appropriate curvilinear equations.
                The curvilinear setpoints are then exported to a file which is read by the main program.
    @author     Michael Cook
    @author     Derick Louie
    @date       March 7, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import math

def conv_r(x,y):
    '''!
    This method obtains the polar r value from given x,y coordinates 
    '''
    r = math.sqrt(x**2 + y**2)    
    return r

def conv_theta(x,y):
    '''!
    This method obtains the polar theta value from given x,y coordinates 
    '''
    theta = math.atan2(x,y)*180/math.pi
    return theta

if __name__ == "__main__":
        # x_prev = 0
        # y_prev = 0
        res = 0.05
        # results_cartesian = []
        # results_polar = []
        end = []
        with open('gcode.csv.ngc') as gcode:
            gcomm=[0,0,0,0,0,0]
            for line in gcode:
                #read each line of gcode and strip unnecessary values
                line = line.strip()
                for x in line:
                    if(x != 'G'):
                        break
                    else:
                        my_list=line.strip('(Penetrate)(All units in mm').split(' ')
                    if(len(my_list)!=0):
                        if(len(my_list) < 3):
                            gcomm[0]=my_list[0].strip('GXYZF')
                            if(len(my_list)>1):
                                for y in my_list[1]:
                                    for x in y:
                                        #obtain any X,Y,Z,I,J values from line of Gcode
                                        if(x=='Y'):
                                            gcomm[2]=my_list[1].strip('GXYZIJ')
                                        elif(x=='X'):
                                            gcomm[1]=my_list[1].strip('GXYZIJ')
                                        elif(x=='Z'):
                                            gcomm[3]=my_list[1].strip('GXYZIJ')
                                        elif(x=='I'):
                                            gcomm[4]=my_list[1].strip('GXYZIJ')
                                        elif(x=='J'):
                                            gcomm[5]=my_list[1].strip('GXYZIJ')
                        elif(len(my_list)>=3):
                            temp=0
                            gcomm[0]=my_list[0].strip('GXYZF')
                            for x in my_list:
                                for y in x:
                                    #obtain any X,Y,Z,I,J values from line of Gcode
                                    if(y=='X'):
                                        gcomm[1]=my_list[temp].strip('GXYZFIJ')
                                    elif(y=='Y'):
                                        gcomm[2]=my_list[temp].strip('GXYZFIJ')
                                    elif(y=='Z'):
                                        gcomm[3]=my_list[temp].strip('GXYZFIJ')
                                    elif(y=='I'):
                                        gcomm[4]=my_list[temp].strip('GXYZFIJ')
                                    elif(y=='J'):
                                        gcomm[5]=my_list[temp].strip('GXYZFIJ')
                                temp+=1
                        print(gcomm)
                        
                        if (gcomm[0] == '00'):
                            #for move to point commands
                            x = float(gcomm[1])
                            y = float(gcomm[2])
                            z = float(gcomm[3])
                            
                            
                            r_seg = conv_r(x, y)
                            theta_seg = conv_theta(x, y)
                            end.append([r_seg, theta_seg, 0])

                            x_prev = x
                            y_prev = y
                            
                            #print('x_prev:', x_prev,'y_prev:',y_prev)
                        
                        if (gcomm[0] == '01'):
                            #for linear movement commands
                            print("back to start")
                            x = float(gcomm[1])
                            y = float(gcomm[2])
                            z = float(gcomm[3])
                            #divide line into segments for given resolution
                            distance = math.sqrt((x_prev-x)**2 + (y_prev-y)**2)
                            num_segs = distance/res
                            
                            dx = (x_prev - x)
                            dy = (y_prev - y)
                            print('dy',dy)
                            
                            i=0
                            while i < num_segs:
                                if round(dx,10) == 0:
                                    #Find next XY setpoints for vertical line
                                    print('in vertical')
                                    x_seg = x
                                    if (y_prev < y):
                                        y_seg = y_prev + res
                                    elif (y_prev > y):
                                        y_seg = y_prev - res
                                        
                                    r_seg = conv_r(x_seg, y_seg)
                                    theta_seg = conv_theta(x_seg, y_seg)
                                    
                                    #r_seg = x_seg
                                    #theta_seg = y_seg
                                    
                                    end.append([r_seg, theta_seg, 1])
                                    x_prev = x_seg
                                    y_prev = y_seg
                                
                                    print("y:", y, 'y_prev:', y_prev)
                                    
                                elif round(dy, 10) == 0 :
                                    #Find next XY setpoints for horizontal line
                                    print('in horizontal line')
                                    y_seg = y
                                    if (x_prev < x):
                                        x_seg = x_prev + res
                                    elif (x_prev > x):
                                        x_seg = x_prev - res
                                        
                                    #convert XY setpoints to polar setpoints    
                                    r_seg = conv_r(x_seg, y_seg)
                                    theta_seg = conv_theta(x_seg, y_seg)
                                    
                                    
                                    #r_seg = x_seg
                                    #theta_seg = y_seg
                                    
                                    end.append([r_seg, theta_seg, 1])
                                    x_prev = x_seg
                                    y_prev = y_seg
                                else:
                                    # slanted line
                                    #m = dy/dx
                                    pass
                                i += 1
                        
                        print("---------end:",end)
                        
                        f = open('setpoints.txt','w')
                        for k in end:
                            #write all setpoints to text file
                            f.write(str(k))
                            f.write('\n')
                        f.close()
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        # if (gcomm[0] == '00'):
                        #     x = float(gcomm[1])
                        #     y = float(gcomm[2])
                        #     z = float(gcomm[3])
                            
                        #     x_prev = x
                        #     y_prev = y
                            
                        #     x_start = x
                        #     y_start = y
                            
                        #     print('-----x_prev, y_prev', x_prev,y_prev)
                        
                        # if (gcomm[0] == '01'):
                            
                        #     r_seg = []
                        #     theta_seg = []
                        #     #results = []
                        #     # prev is "2"
                        #     x = float(gcomm[1])
                        #     y = float(gcomm[2])
                        #     z = float(gcomm[3])
                            
                        #     distance = math.sqrt((x_prev-x)**2 + (y_prev-y)**2)
                        #     num_segs = distance/res
                            
                        #     dx = (x_prev - x)
                        #     dy = (y_prev - y)
                            
                        #     x_start = x
                        #     y_start = y
                            
                        #     i=0
                        #     while i <= num_segs:
                        #         if dx == 0:
                        #             # vertical line
                        #             x = x_prev
                        #             y = y_start + res*i
                                    
                        #             r_seg.append(conv_r(x,y))
                        #             theta_seg.append(conv_theta(x,y))
                        #             print("y:", y, 'y_prev:', y_prev, 'y_start', y_start)
                        #         elif dy == 0 :
                        #             # horizontal line
                        #             x = x_start + res*i
                        #             y = y_prev
                                    
                        #             r_seg.append(conv_r(x,y))
                        #             theta_seg.append(conv_theta(x,y))
                        #             #print("in horiz")
                        #         else:
                        #             # slanted line
                        #             #m = dy/dx
                        #             pass
                        #         i += 1
                        #         #x_prev = x
                        #         #y_prev = y
                                
                        #     pen = [1]*len(r_seg)
                            

                            
                        #     results_cartesian.extend(list(zip(r_seg, theta_seg, pen)))
                            
                        #     print("results", results_cartesian)
                            
                        #     f = open('setpoints.txt','w')
                        #     for k in results_cartesian:
                        #         f.write(str(k))
                        #         f.write('\n')

                            

                            # print("num_segs", num_segs)
                            # print("distance", distance)
                            #print('x_seg',x_seg)
                            #print('y_seg',y_seg)
