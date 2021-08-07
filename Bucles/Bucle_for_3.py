#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 09:14:29 2021

@author: luis
"""

#1+2+3+4+5+6+7+8+...
# Sumar hasta el número 100

n= 1000

suma = 0

for i in range(n+1):
    
    suma += i               #suma = suma + i
    
# SI queremos sumar hasta n, entonces
# suma = n(n+1)/2    
    
print("La suma de los primeros 100 enteros es: ", suma)
print("Con la fórmula se obtiene", n*(n+1)/2)
