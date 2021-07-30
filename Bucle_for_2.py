#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:38:21 2021

@author: luis
"""

Numeros = [1,2,3,4,5,6, 7, 8,9]

for i in Numeros:
    
    print(i)
    
print("\n")    
    
# range(Inicio, Final, Salto)

for i in range(7, 12, 2):
    
    print(i)
    
print("\n", range(11))    #list ---- #tuple

x = list(range(1, 101))

print(x)

H = "Hola mundo, estamos aprendiendo bucles"

for letra in H:
    
    #print(letra, end="")
    print(f"La letra es: {letra}")


for k in range(11):

    print(f"El número es {k}")    
    
print(f"La primera lista del program es {Numeros}")
