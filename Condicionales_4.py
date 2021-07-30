#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:18:15 2021

@author: luis
"""

calificacion = int(input("Digite la calificación: "))


if calificacion < 70 and calificacion >= 0:
    
    print("Calificación deficiente")
    
elif calificacion >= 70 and calificacion < 80:
    
    print("Calificación regular")
    
elif calificacion >= 80 and calificacion < 90:
    
    print("Califación buena")
    
elif calificacion >= 90 and calificacion <= 100:
    
    print("Califación excelente")
    
else:
    
    print("Califación incorrecta")