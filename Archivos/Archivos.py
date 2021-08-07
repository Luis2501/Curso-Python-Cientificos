#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:40:40 2021

@author: luis
"""

archivo = open("archivo.txt", "w")

texto = "Hola a todos\nEste es mi primer archivo"

archivo.write(texto)

archivo.close()

archivo = open("archivo.txt", "r")

texto = archivo.read()

print(texto)

archivo.close()