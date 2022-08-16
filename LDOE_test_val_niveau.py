# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:49:54 2021

@author: theom
"""


val_niv=400

lvl=16

if(lvl==11):
    [Depart_1, Depart_2, P1, Palier_point, Palier_pourc]=14,16,6,[32,28,24,18,22,56,24,20],[19,30,40,47,56,78,88,96]
if(lvl==12):
    [Depart_1, Depart_2, P1, Palier_point, Palier_pourc]=16,18,6,[24,48,20,90,14,46],[15,32,39,71,76,93]
if(lvl==13):
    [Depart_1, Depart_2, P1, Palier_point, Palier_pourc]=2,4,1,[48,50,72,126],[17,33,56,97]
if(lvl==14):
    [Depart_1, Depart_2, P1, Palier_point, Palier_pourc]=5,0,1,[102,122,94],[31,69,99]
    raise Exception
if(lvl==15):
    [Depart_1, Depart_2, P1, Palier_point, Palier_pourc]=24,26,7,[148,154],[49,92]
if(lvl==16):
    [Depart_1, Depart_2, P1, Palier_point, Palier_pourc]=27,29,6,[114,216,32],[35,90,98]


if(len(Palier_point)!=len(Palier_pourc)):
    raise Exception
else:
    print('P1-1:',(P1-1),'% =',(P1-1)*val_niv/100)
    print('P1__:',(P1),'% =',(P1)*val_niv/100)
    print('P1+1:',(P1+1),'% =',(P1+1)*val_niv/100)
    print("---------------------------")
    
    if(Depart_1<=(P1-1)*val_niv/100) or (Depart_2<=(P1-1)*val_niv/100):
        print(Depart_1,'',(P1-1)*val_niv/100)
        print(Depart_2,'',(P1-1)*val_niv/100)
        print("---------------------------")
        
        if(Depart_1<=(P1-1)*val_niv/100):
            for i in range (len(Palier_point)):
                Depart_2+=Palier_point[i]
                if (Depart_2>val_niv):
                    print('Depart 2 : Faux')
                    break
                else:
                    pourc=Palier_pourc[i]
                    
                    print('pourc-1:',(pourc-1),'% =',(pourc-1)*val_niv/100)
                    print('pourc__:',(pourc),'% =',(pourc)*val_niv/100)
                    print('pourc+1:',(pourc+1),'% =',(pourc+1)*val_niv/100)
                    print("---------------------------")
                    
                    if(Depart_2<=(pourc-1)*val_niv/100):
                        print('Depart_2 petit:',Depart_2,'\n')
                        break
                    elif(Depart_2>=(pourc+1)*val_niv/100):
                        print('Depart_2 grand:',Depart_2,'\n')
                        break
                    else:
                        print('Depart_2:',Depart_2)
                    print("---------------------------")
            
        elif (Depart_2<=(P1-1)*val_niv/100):
            for i in range (len(Palier_point)):
                Depart_1+=Palier_point[i]
                if (Depart_1>val_niv):
                    print('Depart 1 : Faux')
                    break
                else:
                    pourc=Palier_pourc[i]
                    
                    print('pourc-1:',(pourc-1),'% =',(pourc-1)*val_niv/100)
                    print('pourc__:',(pourc),'% =',(pourc)*val_niv/100)
                    print('pourc+1:',(pourc+1),'% =',(pourc+1)*val_niv/100)
                    print("---------------------------")
                    
                    if(Depart_1<=(pourc-1)*val_niv/100):
                        print('Depart_1 petit:',Depart_1,'\n')
                        break
                    elif(Depart_1>=(pourc+1)*val_niv/100):
                        print('Depart_1 grand:',Depart_1,'\n')
                        break
                    else:
                        print('Depart_1:',Depart_1)
                    print("---------------------------")
        
    elif (Depart_1>=(P1+1)*val_niv/100) or (Depart_2>=(P1+1)*val_niv/100):
        print(Depart_1,'',(P1+1)*val_niv/100)
        print(Depart_2,'',(P1+1)*val_niv/100)
        raise Exception
    else:
        for i in range (len(Palier_point)):
            Depart_1+=Palier_point[i]
            Depart_2+=Palier_point[i]
            
            if (Depart_1>val_niv):
                print('Depart 1 : Faux')
                break
            elif (Depart_2>val_niv):
                print('Depart 2 : Faux')
                break
            else:
                pourc=Palier_pourc[i]
                
                print('pourc-1:',(pourc-1),'% =',(pourc-1)*val_niv/100)
                print('pourc__:',(pourc),'% =',(pourc)*val_niv/100)
                print('pourc+1:',(pourc+1),'% =',(pourc+1)*val_niv/100)
                print("---------------------------")
                
                if(Depart_1<=(pourc-1)*val_niv/100) or (Depart_2<=(pourc-1)*val_niv/100):
                    if(Depart_1<=(pourc-1)*val_niv/100):
                        print('Depart_1 petit:',Depart_1,'\n')
                        #break
                    if(Depart_2<=(pourc-1)*val_niv/100):
                        print('Depart_2 petit:',Depart_2,'\n')
                        break
                elif (Depart_1>=(pourc+1)*val_niv/100) or (Depart_2>=(pourc+1)*val_niv/100):
                    if(Depart_2>=(pourc+1)*val_niv/100):
                        print('Depart_2 grand:',Depart_2,'\n')
                        #break
                    if(Depart_1>=(pourc+1)*val_niv/100):
                        print('Depart_1 grand:',Depart_1,'\n')
                        break
        
        
    print('Depart_1:',Depart_1)
    print('Depart_2:',Depart_2)

