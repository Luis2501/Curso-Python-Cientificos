#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:57:19 2021

@author: luis
"""

try:

    archivo = open("archivo.txt", "a")

    archivo.write("Hemos agregado esta linea\n")
    

finally:

    archivo.close()