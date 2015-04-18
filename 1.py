# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:00:43 2015

@author: GABRIEL
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:37:08 2015

@author: GABRIEL
"""
import random

p = 0
p2 = 0
s = 0
while s != "sim":
    read = False
    stop = False
    while not read:
        p1 = str(input("Qual sua jogada?\n papel \n tesoura \n pedra \n spock \n lagarto\n\n"))
        if p1 in ["pedra", "papel", "tesoura", "spock", "lagarto"]:
        
            read = True 
        
    pcpick = random.randint(0,4)
    
    if p1 == "papel":
        p1 = 1
        
    if p1 == "tesoura":
        p1 = 0
        
    if p1 == "pedra":
        p1 = 2
        
    if p1 == "spock":
        p1 = 4
        
    if p1 == "lagarto":
        p1 = 3
      
    
    
    x = p1 + 1
    y = p1 + 3
    if x > 4:
       x = x % 5 
    
    if y > 4:
       y = y % 5   
    
    if p1 == pcpick:
        print("Empate")
        
    if pcpick == x or pcpick == y:
        print("Você ganhou esta jogada")  
        p += 1
    if pcpick != p1 and pcpick != x and pcpick != y:
        print("Você perdeu esta jogada\n")    
        p2 += 1
        
    if p == 3:
        print("Você derrotou o computador")
        
    if p == - 3:
        print("O Conputador te derrotou")
     
    while not stop:
         s = str(input("Quer para de jogar?\n\n sim \n ou \n nao\n\n"))
         if s in ["sim", "nao"]: 
             stop = True
             
    print("Pontos player:", p)
    print("Pontos computador", p2)    
