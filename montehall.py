# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:44:44 2023

@author: User
"""
import random

doors=[0]*3
goatdoor=[0]*2
dnt_swap=0
swap=0  #respective wins
j=0
while j<10:
    x=random.randint(0,2)   #bmw
    doors[x]="bmw"

    for i in range (0,3):
        if( i==x ):
            continue
        
        else:
            doors[i]="goat"
            goatdoor.append(i)
            
    choice=int(input("Enter your choice: "))
    door_open=random.choice(goatdoor)  #open a door that comprises of goat
    while(door_open == choice):     #door_open!=choice made by the participant
        door_open=random.choice(goatdoor)
        
    ch=input("Do you want to swap? y/n ")
    if(ch=='y'):
        if(doors[choice]=='goat'):
            print("Player wins")
            swap+=1
            
        else:
            print("Player lost")
            
    else:
        if(doors[choice]=='goat'):
            print("Player lost")
           
        else:
            print("Player wins")
            dnt_swap+=1
    j+=1
    

        
print(swap)
print(dnt_swap)
       
    

