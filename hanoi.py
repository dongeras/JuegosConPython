#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:08:21 2020

@author: gerardo
"""
"""
def postes(n):
    #Muestra en pantalla tres postes con n discos cada uno
    #
    torres = [[],[],[]]
        
        
    for j in range(n):
        for i in range(3):
            torres[i].append(" "*((n+1)-j) + "_"*(j+1) + "|" + "_"*(j+1) + " "*((n+1)-j)) 
    
    for i in range(n):
        print(torres[0][i] + torres[1][i] + torres[2][i])

Siento que ya no servirá. La dejamos por si las dudas
"""
def dibujaPostes(discosEnTorres, n):
    #toma la información de en qué postes están los discos
    #y muestra en pantalla el dibujo correspondiente.
    for i in range(n):
        print(discosEnTorres[0][i] + discosEnTorres[1][i] + discosEnTorres[2][i])
        
    
def discos(n):
    # Regresa una lista con los n discos del juego
    listaDiscos = []
    for j in range(n):
        listaDiscos.append(" "*((n+1)-j) + "_"*(j+1) + "|" + "_"*(j+1) + " "*((n+1)-j))
    return listaDiscos

def colocaDiscos(discosEnTorre, n):
    #Coloca, de abajo para arriba, los discos en la lista "discosEnTorre"
    #en una lista "torre"; llena los espacios restantes con diburjos vacíos
    #dicosEnTorre ordenados de mayor a menor
    torre = [" " * (n+2) + "|" + " " * (n+2) ] * n
    for i in range(len(discosEnTorre)):
        torre[(n-1-i)] = discosEnTorre[i]
    return torre
        
def ordenDiscos(discosEnTorre):
    #MODIFICAR!
    #Regresa True si los discos están bien acomodados
    #y regresa False en caso contrario
    for i in range(1,len(discosEnTorre)):
        #recorrer todos los discos en la lista
        for j in range(0,i):
            #recorre los que están por debajo del iésimo
            if len(discosEnTorre[i]) <= len(discosEnTorre[j]):
                return False
    return True
               
discosEnLaTorre = discos(5)
discosEnLaTorre.reverse()
orden = ordenDiscos(discosEnLaTorre)


"""
Ya podemos dibujar una configuración arbitraria de torres y discos.

Falta verificar que los discos en una torre están bien ordenados
"""

