#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:58:59 2021

@author: luis
"""

x = 1
y = 1

try:
    
    print(x/y)
    
except ZeroDivisionError:
    
    print("No puedes dividir entre cero")
    
print(1/0)    
    
letra = "H"    

try: 
    
    print(letra + 10)

except TypeError:
    
    print("No puedes sumar letras con números")

    
print("Programa Terminado!")