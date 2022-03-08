import math

if __name__ == "__main__":
        with open('gcode.csv.ngc') as gcode:
            gcomm=[0,0,0,0,0,0]
            for line in gcode:
                line = line.strip()
                for x in line:
                    if(x != 'G'):
                        break
                    else:
                        list=line.strip('(Penetrate)(All units in mm').split(' ')
                    if(len(list)!=0):
                        if(len(list) < 3):
                            gcomm[0]=list[0].strip('GXYZF')
                            if(len(list)>1):
                                for y in list[1]:
                                    for x in y:
                                        if(x=='Y'):
                                            gcomm[2]=list[1].strip('GXYZIJ')
                                        elif(x=='X'):
                                            gcomm[1]=list[1].strip('GXYZIJ')
                                        elif(x=='Z'):
                                            gcomm[3]=list[1].strip('GXYZIJ')
                                        elif(x=='I'):
                                            gcomm[4]=list[1].strip('GXYZIJ')
                                        elif(x=='I'):
                                            gcomm[5]=list[1].strip('GXYZIJ')
                        elif(len(list)>=3):
                            temp=0
                            gcomm[0]=list[0].strip('GXYZF')
                            for x in list:
                                for y in x:
                                    if(y=='X'):
                                        gcomm[1]=list[temp].strip('GXYZFIJ')
                                    elif(y=='Y'):
                                        gcomm[2]=list[temp].strip('GXYZFIJ')
                                    elif(y=='Z'):
                                        gcomm[3]=list[temp].strip('GXYZFIJ')
                                    elif(y=='I'):
                                        gcomm[4]=list[temp].strip('GXYZFIJ')
                                    elif(y=='J'):
                                        gcomm[5]=list[temp].strip('GXYZFIJ')
                                temp+=1
                        print(gcomm)
#                         xprev=0
#                         yprev=0
#                         if(gcomm[0]=='21'):
#                             print('units=mm')
#                         elif(gcomm[0]=='00'):
#                             x = float(gcomm[1])
#                             y = float(gcomm[2])
#                             setpts=[(x,y,0)]
#                             xprev = x
#                             yprev = y
#                             print('move',setpts)
#                             
#                         elif(gcomm[0]=='01'):
#                             setpts=[]
#                             x = float(gcomm[1])
#                             y = float(gcomm[2])
#                             z = float(gcomm[3])
#                             div = 10
#                             xdif = (x-xprev)
#                             ydif = (y-yprev)
#                             i=0
#                             xinc = xdif/div
#                             yinc = ydif/div
#                             while(i < div):
#                                 xout = xinc + (xinc * i)
#                                 yout = yinc + (yinc * i)
#                                 r=math.sqrt((xout*xout)+(yout*yout))
#                                 theta=math.atan(yout/xout)*(180/math.pi)
#                                 if(z > 0):
#                                     setpts.append((xout,yout,0))
#                                 else:
#                                     setpts.append((xout,yout,1))
#                                 i+=1
#                             xprev = x
#                             yprev = y
#                             print('linear',setpts)
#                             
#                             
#                         elif(gcomm[0]=='02'):
#                             print('circular cw')
#                             x = gcomm[1]
#                             y = gcomm[2]
#                             z = gcomm[3]
#                             i = gcomm[4]
#                             j = gcomm[5]
#                             
#                         elif(gcomm[0]=='03'):
#                             print('circular ccw')
#                             x = gcomm[1]
#                             y = gcomm[2]
#                             z = gcomm[3]
#                             i = gcomm[4]
#                             j = gcomm[5]
#                             
#                 
#                         
#             