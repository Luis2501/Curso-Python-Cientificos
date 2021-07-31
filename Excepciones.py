#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:26:54 2021

@author: luis
"""

x = int(input("Digite el primer número: "))
y = int(input("Digite en segundo número: "))

try: 
    
    print(x/y)
    
except:

    print("División entre cero") 

palabra = 2

try:
    
    print(palabra + 10)
    
except:
    
    print("No se pueden sumar")
    
finally:
    
    print("\n Programa terminado!")