#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:33:05 2021

@author: luis
"""

while True: 
    
    edad = int(input("Digita tu edad: "))
    
    if edad >= 0 and edad >= 18:
        
        print("Acceso a la página")
        
        break 
    
    else:
    
        print("NO tienes acceso")
        print("Eres menor de edad")
        
        