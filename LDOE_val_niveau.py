# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:48:18 2021

@author: theom
"""

#lvl=15
#val_niv=355


val_min=330

list_lvl=[15,16,17,18,19]
list_lvl=[18]

list_lvl_val_niv=[]

def Print_Pour(txt,pourc):
    print("---------------------------") 
    print('Niveau :',{len(Palier_point)},'A modifier')       
    print(txt,'-1:',(pourc-1),'% =',(pourc-1)*val_niv/100)
    #print('pourc-0.5:',(pourc-0.5),'% =',(pourc-0.5)*val_niv/100)
    print(txt,'__:',(pourc),'% =',(pourc)*val_niv/100)
    #print('pourc+0.5:',(pourc+0.5),'% =',(pourc+0.5)*val_niv/100)
    print(txt,'+1:',(pourc+1),'% =',(pourc+1)*val_niv/100)
    print("---------------------------")
    
    

for lvl in list_lvl:
    
    #if(lvl==16):
        #break
    
    val_niv=val_min
    tab_possible=[]
    tab_depart=[]
    Au_dessus=0
    
    if(lvl==11):
        [P1, Palier_point, Palier_pourc]=6,[32,28,24,18,22,56,24,20],[19,30,40,47,56,78,88,96]
    elif(lvl==12):
        [P1, Palier_point, Palier_pourc]=6,[24,48,20,90,14,46],[15,32,39,71,76,93]
    elif(lvl==13):
        [P1, Palier_point, Palier_pourc]=1,[48,50,72,126],[17,33,56,97]
    elif(lvl==14):
        [P1, Palier_point, Palier_pourc]=1,[102,122,94],[31,69,99]
        raise Exception
    elif(lvl==15):
        [P1, Palier_point, Palier_pourc]=7,[148,154],[49,92]
    elif(lvl==16):
        [P1, Palier_point, Palier_pourc]=6,[114,216,32],[35,90,98]
    elif(lvl==17):
        [P1, Palier_point, Palier_pourc]=6,[216,148,64],[52,84,99]
    elif(lvl==18):
        [P1, Palier_point, Palier_pourc]=36,[84,113,48,46,20,6],[53,73,83,92,96,97]
    elif(lvl==19):
        [P1, Palier_point, Palier_pourc]=5,[60,22,16,16,16,16,16,12,20,14],[16,20,23,26,29,32,35,37,41,43]
        
    list_lvl_val_niv.append(lvl)
    sous_list_lvl_val_niv=[]
    
    while(tab_possible==tab_depart) and (Au_dessus!=1):
        tab_possible=[]
        tab_depart=[]
        if(val_niv>2*val_min):
            print('Stop : 2*val_min')
            break
        
        val_niv=val_niv+1
    
        #print('val_niv :',val_niv)
        #print("---------------------------")
            
        
        if(len(Palier_point)!=len(Palier_pourc)):
            raise Exception
        else:
            nb_possible=0
            
            while((P1+1)*val_niv/100>(P1-1)*val_niv/100+nb_possible):
                nb_possible+=1
                if(nb_possible>20) or ((P1+1)*val_niv/100<(P1-1)*val_niv/100+nb_possible):
                    break
                else:
                    tab_possible.append(int((P1-1)*val_niv/100+nb_possible))
            
            tab_depart=tab_possible.copy()
            tab_faux=[]
        
            for i in range (len(tab_possible)):
                for l in range(len(Palier_point)):
                    
                    tab_possible[i]+=Palier_point[l]
                    
                    if(tab_possible[i]<=(Palier_pourc[l]-1)*val_niv/100) or (tab_possible[i]>=(Palier_pourc[l]+1)*val_niv/100):
                        tab_faux.append(tab_possible[i])
                        tab_possible[i]=tab_depart[i]
                        break
                    
            pourc=Palier_pourc[len(Palier_point)-1]
            
            
    while(tab_possible!=tab_depart):
        tab_possible=[]
        tab_depart=[]
        
        sous_list_lvl_val_niv.append(val_niv)
        
        if(val_niv>2*val_min):
            print('Stop : 2*val_min')
            break
        
        val_niv=val_niv+1
    
        #print('val_niv :',val_niv)   
        
        if(len(Palier_point)!=len(Palier_pourc)):
            raise Exception
        else:
            #Print_Pour('P1',P1)
            
            nb_possible=0
            
            while((P1+1)*val_niv/100>(P1-1)*val_niv/100+nb_possible):
                nb_possible+=1
                if(nb_possible>20) or ((P1+1)*val_niv/100<(P1-1)*val_niv/100+nb_possible):
                    break
                else:
                    tab_possible.append(int((P1-1)*val_niv/100+nb_possible))
            #print(tab_possible)
            
            tab_depart=tab_possible.copy()
            tab_faux=[]
        
            for i in range (len(tab_possible)):
                for l in range(len(Palier_point)):
                    
                    tab_possible[i]+=Palier_point[l]
                    
                    if(tab_possible[i]<=(Palier_pourc[l]-1)*val_niv/100) or (tab_possible[i]>=(Palier_pourc[l]+1)*val_niv/100):
                        #print(tab_depart[i],': Faux au niveau',l+1)
                        tab_faux.append(tab_possible[i])
                        tab_possible[i]=tab_depart[i]
                        break
                    
            pourc=Palier_pourc[len(Palier_point)-1]
            
            #Print_Pour('pourc',pourc)
            
            #if(len(tab_depart)==len(tab_faux)):
                #print('Faux :',tab_faux)
            
            #print(tab_possible)
            
        Au_dessus=1
    
    list_lvl_val_niv.append(min(sous_list_lvl_val_niv))
    list_lvl_val_niv.append(max(sous_list_lvl_val_niv))

print(list_lvl_val_niv)
    
