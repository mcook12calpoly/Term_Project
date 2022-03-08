import math

if __name__ == "__main__":
        with open('gcode.csv.ngc') as gcode:
            gcomm=[0,0,0,0,0,0]
            xprev=0
            yprev=0
            gprev='0'
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
                        if(gcomm[0]=='21'):
                            gprev='21'
                        elif(gcomm[0]=='00'):
                            x = float(gcomm[1])
                            y = float(gcomm[2])
                            xdif=x-xprev
                            ydif=y-yprev
                            if(xdif<=0.0):
                                r=math.sqrt((x*x)+(y*y))
                                if(x==0.0):
                                    theta=0
                                else:
                                    theta=math.atan(y/x)*(180/math.pi)
                            else:
                                r=math.sqrt((xdif*xdif)+(ydif*ydif))
                                theta=math.atan(ydif/xdif)*(180/math.pi)
                            setpts=[(r,theta,0)]
                            xprev = x
                            yprev = y
                            for data in setpts:
                                print(data)
                            gprev='00'
                            
                        elif(gcomm[0]=='01'):
                            setpts=[]
                            x = float(gcomm[1])
                            y = float(gcomm[2])
                            z = float(gcomm[3])
                            div = 10
                            xdif = (x-xprev)
                            ydif = (y-yprev)
                            i=0
                            xinc = xdif/div
                            yinc = ydif/div
                            while(i < div):
                                xout = xinc + (xinc * i)
                                yout = yinc + (yinc * i)
                                if(gprev=='00'):
                                    r=math.sqrt((x*x)+(y*y))
                                    theta=math.atan(y/x)*(180/math.pi)
                                elif(xout==0.0):
                                    r=math.sqrt((xout*xout)+(yout*yout))
                                    theta=math.atan(yout/xprev)*(180/math.pi)
                                else:
                                    r=math.sqrt((xout*xout)+(yout*yout))
                                    theta=math.atan(yout/xout)*(180/math.pi)
                                if(z > 0):
                                    setpts.append((r,theta,0))
                                else:
                                    setpts.append((r,theta,1))
                                i+=1
                            r=math.sqrt((x*x)+(y*y))
                            theta=math.atan(y/x)*(180/math.pi)
                            if(z > 0):
                                setpts.append((r,theta,0))
                            else:
                                setpts.append((r,theta,1))
                            xprev = x
                            yprev = y
                            for data in setpts:
                                print(data)
                            gprev='01'
                            
                            
                        elif(gcomm[0]=='02'):
                            x = float(gcomm[1])
                            y = float(gcomm[2])
                            z = float(gcomm[3])
                            i = float(gcomm[4])
                            j = float(gcomm[5])
                            if(i!=0.0 or j!=0.0):
                                phi=math.atan(j/i)
                            else:
                                phi=0
                            yt=y-(yprev+j)
                            xt=(xprev+i)-x
                            rt=math.sqrt((xt*xt)+(yt*yt))
                            div = 10
                            xdif = x - xprev
                            ydif = y - yprev
                            n=0
                            phiinc = phi/div
                            while(n < div):
                                phidiv = phiinc + (phiinc * n)
                                xout = rt*math.cos(phidiv)
                                yout = rt*math.sin(phidiv)
                        
                                if(gprev=='00'):
                                    r=math.sqrt((x*x)+(y*y))
                                    theta=math.atan(y/x)*(180/math.pi)
                                elif(xout==0.0):
                                    r=math.sqrt((xout*xout)+(yout*yout))
                                    theta=math.atan(yout/xprev)*(180/math.pi)
                                else:
                                    r=math.sqrt((xout*xout)+(yout*yout))
                                    theta=math.atan(yout/xout)*(180/math.pi)
                                if(z > 0):
                                    setpts.append((r,theta,0))
                                else:
                                    setpts.append((r,theta,1))
                                n+=1
                            xprev = x
                            yprev = y
                            for data in setpts:
                                print(data)
                            gprev='02'
                            
                        elif(gcomm[0]=='03'):
                            x = float(gcomm[1])
                            y = float(gcomm[2])
                            z = float(gcomm[3])
                            i = float(gcomm[4])
                            j = float(gcomm[5])
                            if(i!=0.0 or j!=0.0):
                                phi=math.atan(j/i)
                            else:
                                phi=0
                            yt=y-(yprev+j)
                            xt=(xprev+i)-x
                            rt=math.sqrt((xt*xt)+(yt*yt))
                            div = 10
                            xdif = x - xprev
                            ydif = y - yprev
                            n=0
                            phiinc = phi/div
                            while(n < div):
                                phidiv = phiinc + (phiinc * n)
                                xout = rt*math.cos(phidiv)
                                yout = rt*math.sin(phidiv)
                                if(gprev=='00'):
                                    r=math.sqrt((x*x)+(y*y))
                                    theta=math.atan(y/x)*(180/math.pi)
                                elif(xout==0.0):
                                    r=math.sqrt((xout*xout)+(yout*yout))
                                    theta=math.atan(yout/xprev)*(180/math.pi)
                                else:
                                    r=math.sqrt((xout*xout)+(yout*yout))
                                    theta=math.atan(yout/xout)*(180/math.pi)
                                if(z > 0):
                                    setpts.append((r,theta,0))
                                else:
                                    setpts.append((r,theta,1))
                                n+=1
                            xprev = x
                            yprev = y
                            for data in setpts:
                                print(data)
                            gprev='03'
                            
                
                        
            
