# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:42:52 2021

@author: theom
"""

list_lvl=[15,16,17,18,19]
list_val_test=[15, 348, 362, 16, 386, 402, 17, 456, 469, 18, 432, 588, 19, 521, 567]


lvl=list_lvl[int(list_val_test.index(15)/3)]
min_lvl=list_val_test[list_val_test.index(15)+1]
    

if(lvl==11):
    [P1, Palier_point, Palier_pourc]=6,[32,28,24,18,22,56,24,20],[19,30,40,47,56,78,88,96]
    next_lvl=28
elif(lvl==12):
    [P1, Palier_point, Palier_pourc]=6,[24,48,20,90,14,46],[15,32,39,71,76,93]
    next_lvl=24
elif(lvl==13):
    [P1, Palier_point, Palier_pourc]=1,[48,50,72,126],[17,33,56,97]
    next_lvl=12
elif(lvl==14):
    [P1, Palier_point, Palier_pourc]=1,[102,122,94],[31,69,99]
    next_lvl=32
    raise Exception
elif(lvl==15):
    [P1, Palier_point, Palier_pourc]=7,[148,154],[49,92]
    next_lvl=56
elif(lvl==16):
    [P1, Palier_point, Palier_pourc]=6,[114,216,32],[35,90,98]
    next_lvl=24
elif(lvl==17):
    [P1, Palier_point, Palier_pourc]=6,[216,148,64],[52,84,99]
    next_lvl=36
elif(lvl==18):
    [P1, Palier_point, Palier_pourc]=36,[84,113,48,46,20,6],[53,73,83,92,96,97]
    next_lvl=14
elif(lvl==19):
    [P1, Palier_point, Palier_pourc]=5,[60,22,16,16,16,16,16,12,20,14],[16,20,23,26,29,32,35,37,41,43]
    next_lvl=0
else:
    raise Exception

tab_possible=[]
tab_depart=[]

val_niv=min_lvl

def Print_Pour(txt,pourc):
    print("---------------------------") 
    print('Niveau :',{len(Palier_point)},'A modifier')       
    print(txt,'-1:',(pourc-1),'% =',(pourc-1)*val_niv/100)
    #print('pourc-0.5:',(pourc-0.5),'% =',(pourc-0.5)*val_niv/100)
    print(txt,'__:',(pourc),'% =',(pourc)*val_niv/100)
    #print('pourc+0.5:',(pourc+0.5),'% =',(pourc+0.5)*val_niv/100)
    print(txt,'+1:',(pourc+1),'% =',(pourc+1)*val_niv/100)
    print("---------------------------")

print('val_niv :',val_niv)   

if(len(Palier_point)!=len(Palier_pourc)):
    raise Exception
else:
    Print_Pour('P1',P1)
    
    nb_possible=0
    
    while((P1+1)*val_niv/100>(P1-1)*val_niv/100+nb_possible):
        nb_possible+=1
        if(nb_possible>20) or ((P1+1)*val_niv/100<(P1-1)*val_niv/100+nb_possible):
            break
        else:
            tab_possible.append(int((P1-1)*val_niv/100+nb_possible))
    print(tab_possible)
    
    tab_depart=tab_possible.copy()
    tab_faux=[]

    for i in range (len(tab_possible)):
        for l in range(len(Palier_point)):
            
            tab_possible[i]+=Palier_point[l]
            
            if(tab_possible[i]<=(Palier_pourc[l]-1)*val_niv/100) or (tab_possible[i]>=(Palier_pourc[l]+1)*val_niv/100):
                print(tab_depart[i],': Faux au niveau',l+1)
                tab_faux.append(tab_possible[i])
                tab_possible[i]=tab_depart[i]
                break
            
    pourc=Palier_pourc[len(Palier_point)-1]
    
    Print_Pour('pourc',pourc)
    
    if(len(tab_depart)==len(tab_faux)):
        print('Faux :',tab_faux)
    
    print(tab_possible)
    
    for i in range(len(tab_possible)):
        if (tab_possible[i]!=tab_depart[i]):
            diff=next_lvl-val_niv+tab_possible[i]
            print(diff)
            
    