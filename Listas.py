#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:10:32 2021

@author: luis
"""

        #0      1      2     3
Lista = [2, "Python", True, [1,1]]

print(Lista)

#Acceder a un elemento

print(Lista[1])

Lista[2] = 100

print(Lista[2])

#Accerder a varios elementos

print(Lista[:3])

print(Lista[1:3])


x = [1,2,3]                 #x = (1,2,3)

#Matrices
#  1 2
#  3 4

Matriz = [[1,2], 
          [3,4]]

print(Matriz)

Lista_vacia = [ ]

# Método append

Lista_vacia.append(23)
Lista_vacia.append("FCFM")

print(Lista_vacia)

Lista_vacia.extend([False, 56, "Hola"])

print(Lista_vacia, "\n")

print(Lista + Lista_vacia)

# Función sum

Datos = [1,2,3,4,5]

print("La suma de datos es: ", sum(Datos))

def promedio(datos):
    
    return sum(datos)/len(datos)

print("El promedio es:", promedio(Datos))

Lista_2 = [True, "Hola"]                    #No se puede sumar

print(sum(Lista_2))