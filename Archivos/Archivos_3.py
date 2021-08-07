#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:32:55 2021

@author: luis
"""

#Datos = [1,2,3,4,5,6,7,8,9,10]

#1
#2
#3

Datos = list(range(1,11))

try:

    archivo = open("Datos.txt", "w")
    
    for i in Datos:
        
        archivo.write(f"{i} \n")
    

finally:

    archivo.close()
    
    
try: 
    
    archivo = open("Datos.txt", "r")
    
    Lista = archivo.readlines()
    
    datos = []
    
    for i in Lista:
        
        datos.append(float(i))
    
finally:

    archivo.close()
    
print(datos)