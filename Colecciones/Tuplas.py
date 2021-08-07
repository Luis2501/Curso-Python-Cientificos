#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:42:03 2021

@author: luis
"""

Tuplas = (1, "Hola", True)

print(Tuplas)

print(Tuplas[1])

Tupla_2 = 2, 4, 6                   #Empaquetar

print(Tupla_2) 

print(type(Tupla_2))

#Transoformar a lista

print(Nueva := list(Tuplas))


Lista = [True, False, 3, "FCFM"]

print(tuple(Lista))

#Desempaquetar

x, y, z = Tuplas

print(x,y,z)

print(Tuplas + Tupla_2)

