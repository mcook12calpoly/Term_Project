
if __name__ == "__main__":
    with open('gcode.csv', 'r') as f:   #read csv file
        prev=[0,0,0]
        for line in f:
            list=[]
            for words in line.split(' '):    #seperate values at ','
                for x in words:
                    if(x==";"):
                        break
                    elif(x=="G" or x=="X" or x=="Y"):
                        list.append(words.strip())
            
            if(len(list)!=0):
                if(len(list) < 3):
                    prev[0]=list[0].strip('GXY')
                    for y in list[1]:
                        for x in y:
                            if(x=='Y'):
                                prev[2]=list[1].strip('GXY')
                            elif(x=='X'):
                                prev[1]=list[1].strip('GXY')
                elif(len(list)==3):
                    prev[0]=list[0].strip('GXY')
                    prev[1]=list[1].strip('GXY')
                    prev[2]=list[2].strip('GXY')
            print('GXY:',prev)
                
                        
            