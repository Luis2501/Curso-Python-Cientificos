#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:27:12 2021

@author: luis
"""

N = int(input("Dame el número que deseas: "))

i = 1 

#Operación módulo %   a%b

while i <= N:
    
    if i%2 == 0:
        
        print(f"{i} es un número par")
        
    else:
        
        print(f"{i} es un número impar")
        
    i += 1