#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:43:52 2021

@author: luis
"""

#Módulo de calculadora

def sumar(x, y):
    
    return x+y

def restar(x,y):
    
    return x-y

def multiplicacion(x,y):
    
    return x*y

def division(x,y):
    
    try:
        
        return x/y
    
    except ZeroDivisionError:
        
        print("NO se puede dividir entre cero")
        
#x^n 1/x^n        
        
def potencia(x,n):
    
    if isinstance(n, int):
    
        return x**abs(n)
    
    else:
        
        raise ValueError("La potencia debe ser de un número entero")
    