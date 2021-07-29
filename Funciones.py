#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:15:19 2021

@author: luis
"""

#Las variables en Python son objetos, las funciones en una clase se llaman "métodos"

def mostrar_mensaje():
    
    print("Hola a todos, esta es mi primera función")
    
mostrar_mensaje() 

def mensaje():

    print("\nHola a todos")
    print("Hoy estamos aprendiendo funciones")
    print("Python es muy divertido")

# f(x) = x²

def f(x): 
    
    resultado = x**2
    
    return resultado

print(f(10))

# f(x) = x³ + exp(x) + sen(x) ; función lambda 

def sumar(x, y): 

    return x + y
    
print(sumar(2,3))

x = sumar(10,10)

print("La suma es: ", x)

def sumar_multiplicar(x, y):
    
    return x+y, x*y

suma, multiplicacion = sumar_multiplicar(1,1)

print(suma, multiplicacion) 
