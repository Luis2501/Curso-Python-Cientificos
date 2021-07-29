#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:37:50 2021

@author: luis
"""

def sumar(x, y):
    
    return x+y

print(sumar("Hola ", "mundo"))              #Sumar cadenas de texto

# input()

x = float(input("Digite un número: "))

#x = int(x)                 Manera de cambiar de tipo de dato a x

print(x)
print(type(x))

y = float(input("Digite otro número: "))

print(sumar(x, y))  

# De número a cadenas de texto : str()

# Función round

suma = sumar(x, y)

print(round(suma, 4))

z = complex(2, 3)

print(z)

parte_real = z.real
parte_img = z.imag

print(parte_real, parte_img)