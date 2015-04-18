-*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:08:31 2015

@author: GABRIEL
"""

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
p22 = 0
s = 0
while s != "sim":
    read = False
    read2 = False
    stop = False
    while not read:
        p1 = str(input("Qual sua jogada player 1?\n papel \n tesoura \n pedra \n spock \n lagarto\n\n"))
        if p1 in ["pedra", "papel", "tesoura", "spock", "lagarto"]:
        
            read = True 
    while not read2:
        p2 = str(input("\n\n\nQual sua jogada player 2?\n papel \n tesoura \n pedra \n spock \n lagarto\n\n"))
        if p1 in ["pedra", "papel", "tesoura", "spock", "lagarto"]:
        
            read2 = True         
        
        
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
      
          
    if p2 == "papel":
        p2 = 1
        
    if p2 == "tesoura":
        p2 = 0
        
    if p2 == "pedra":
        p2 = 2
        
    if p2 == "spock":
        p2 = 4
        
    if p2 == "lagarto":
        p2 = 3
      
    
    
    x = p1 + 1
    y = p1 + 3
    if x > 4:
       x = x % 5 
    
    if y > 4:
       y = y % 5   
    
    if p1 == p2:
        print("Empate")
        
    if p2 == x or p2 == y:
        print("Player 1 ganhou esta jogada")  
        p += 1
    if p2 != p1 and p2 != x and p2 != y:
        print("Player 2 ganhou esta jogada\n")    
        p22 += 1

    while not stop:
         s = str(input("Quer para de jogar?\n\n sim \n ou \n nao\n\n"))
         if s in ["sim", "nao"]: 
             stop = True
  
         
    print("Pontos player:", p)
    print("Pontos player 2:", p22)    
