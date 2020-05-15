#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:08:21 2020

@author: gerardo
"""

def postes(n):
    torres = [[],[],[]]
        
        
    for j in range(n):
        for i in range(3):
            torres[i].append(" "*((n+1)-j) + "_"*(j+1) + "|" + "_"*(j+1) + " "*((n+1)-j)) 
    
    for i in range(n):
        print(torres[0][i] + torres[1][i] + torres[2][i])

#torres = [[" "*(4-1) + "_"*1+"|" + "_" + " "*(4-1), 
#           " "*(4-2) + "_"*2 + "|" + "_"*2 + " "*(4-2),
#           " "*(4-3) + "_"*3 + "|" + "_"*3 + " "*(4-3), 
#           " "*(4-4) + "_"*4 + "|" + "_"*4 + " "*(4-4)],[],[]]

"""
Ya está el tablero inicial. 

Falta ver como dibujar un número arbitrario de discos en un poste
"""