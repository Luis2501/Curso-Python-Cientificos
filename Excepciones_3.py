#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:04:50 2021

@author: luis
"""

x = "Python"

#Si el tipo de dato de x no es entero, entonces
#Si objeto no es esto

if not type(x) is int:
    
    raise TypeError("x no es de tipo entero")
    
print("Programa terminado")