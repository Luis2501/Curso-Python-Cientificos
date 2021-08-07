#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:03:31 2021

@author: luis
"""

#from Calculadora import sumar, restar
#import Calculadora as cal
from Calculadora.Calculadora import *
from Calculadora.Stats import promedio

print(sumar(2,2))
print(restar(2,2))

print(potencia(2,2))

Datos = [1,2,3,4,5]

print(promedio(Datos))