#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 09:40:03 2021

@author: luis
"""

def ln(N, x):
    
    suma = 0
    
    for n in range(1, N+1): 
        
        suma += ((-1)**(n+1) / n )* ( (x - 1)**n ) 
        
    return suma

Resultado = 0.40546511

resultado = 0

N = 1

"""

while N <= 100: 
    
    resultado = ln(N, 1.5)
    
    if abs(Resultado-resultado) < 10**(-5):
        
        print("El criterio se cumple si N =", N)
        
        break
    
    N += 1
"""

while abs(Resultado-resultado) > 10**(-5):
    
    resultado = ln(N, 1.5)
    
    N+=1
  
print("El criterio se cumple si N =", N)

    
    