#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 10:44:49 2021

@author: luis
"""

# ax² + bx + c = 0
# Fórmula general
# -b +- raiz(b² -4ac) / 2a

def formula_general(a, b, c):
    
    x1 = (-b + (b**2 -4*a*c)**(1/2))/2*a
    x2 = (-b - (b**2 -4*a*c)**(1/2))/2*a
    
    return x1, x2

#SI  solo queremos soluciones reales, entonces el discriminante
# debe ser mayor a cero

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    
    print("No se tienen raices reales")

else: 
    
    x1,x2 = formula_general(a, b, c)
    
    print("La primera solución: ", x1)
    print("La segunda solución:", x2)

# x² - 1 = 0 entonces x = +- 1
