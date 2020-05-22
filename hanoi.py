#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:08:21 2020

@author: gerardo
"""

def algoritmoHanoi(numDiscos, torreInicial, torreFinal, torreAux):

        
    if numDiscos == 1:
        realizaMovida(configuracionActual, torreInicial, torreFinal)
        print("Mueve el último disco de la torre %s a la torre %s" %(torreInicial+1, torreFinal+1))
        dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
        
    else:
        
        algoritmoHanoi(numDiscos-1, torreInicial, torreAux, torreFinal)    
        
        realizaMovida(configuracionActual, torreInicial, torreFinal)
        print("Mueve el último disco de la torre %s a la torre %s" %(torreInicial+1, torreFinal+1))
        dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
        
        algoritmoHanoi(numDiscos-1, torreAux, torreFinal, torreInicial)
        

def dibujaPostes(discosEnTorres, n):
    #toma la información de en qué postes están los discos
    #y muestra en pantalla el dibujo correspondiente.
    
    print(' '*(n+2) + '1' + ' '*2*(n+2) + '2' + ' '*2*(n+2) + '3' )
    print('')
    for i in range(n):
        print(discosEnTorres[0][i] + discosEnTorres[1][i] + discosEnTorres[2][i])
    print('_' *3*(2*n+5))
    print("|" *3*(2*n+5)  )
        
    
def configuracionInicial(n):
    # Regresa una lista con tres listas
    # Cada una las sub-listas representa el conjunto de discos en una torre
    listaDiscos = [[],[],[]]
    for j in range(n):
        listaDiscos[0].append(j+1)
    return listaDiscos

def colocaDiscos(configuracion, n):
    #Prepara una lista de listas con las cadenas de texto
    # para mostrar el Arte ASCI correspondiente a la 
    #Configuración de discos "configuracion"
    torre = [[], [], []]
    for j in range(3):
        for i in range(n-len(configuracion[j])):
            torre[j].append(" " * (n+2) + "|" + " " * (n+2))
        for i in range(len(configuracion[j])):
            torre[j].append(" " * (n +2 - configuracion[j][i]) + 
                            "_" * configuracion[j][i] +
                            "|" + "_" * configuracion[j][i] +
                            " " *(n + 2 - configuracion[j][i]))
    return torre
        
def jugadaValida(configuracionDiscos, torreInicial, torreFinal):
    #Regresa True si si la jugada es válida
    #y regresa False en caso contrario
    copiaConfiguracion = [[],[],[]] 
    
    #El sig. ciclo copia la configuración
    
    if len(configuracionDiscos[torreInicial]) == 0:
        return False
    
    for i in range(3):
        for disco in configuracionDiscos[i]:
            copiaConfiguracion[i].append(disco)
    
    #Se hace la jugada en la copia de la conf.
    realizaMovida(copiaConfiguracion, torreInicial, torreFinal)
    #Se verigica que la jugada sea válida
    if len(copiaConfiguracion[torreFinal]) > 1:
        if copiaConfiguracion[torreFinal][0] >= copiaConfiguracion[torreFinal][1]:
            return False
    return True

def esGanadora(configuracionDiscos, n):
    #Regresa True si la configuración de discos es la ganadora
    #i.e todos los discos están en la última torre.
    #Regresa False si no es la conf. ganadora
    todosDiscos = [i for i in range(1, n+1)]
    return set(configuracionDiscos[2]) == set(todosDiscos)
    
    
    
               

def movimientoUsuario(configuracionDiscos):
    # Le pide al usuario un movimiento y verifica
    # 1) que elija torres existente (1, 2, 3)
    # 2) que el disco que se mueve es más chiquito que el último de la nueva torre
    
    respuesta = ''
    DIGITOS = '1 2 3'.split()
    while (len(respuesta) != 2 or respuesta[0] == respuesta[1] or  
           (respuesta[0] not in DIGITOS and respuesta[1] not in DIGITOS) or 
           not jugadaValida(configuracionDiscos, int(respuesta[0])-1, int(respuesta[1])-1)):
        print('¿Cuál es tu movimiento (Indica Torre inicial y final)?')
        respuesta = input()
        
    torreInicial = int(respuesta[0]) - 1
    torreFinal = int(respuesta[1]) - 1
        
    return [torreInicial, torreFinal]    
        


def realizaMovida(discosEnTorre, torreInicial, torreFinal):
    #Realiza la "jugada" en la configuración "discosEnTorre"
    discosEnTorre[torreFinal].insert(0, discosEnTorre[torreInicial][0])
    del discosEnTorre[torreInicial][0]

while True:
    
    print('¿Cuántos discos hay en las torres?')
    numeroDeDiscos = int(input()) 
    configuracionActual = configuracionInicial(numeroDeDiscos)
    dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
    respuesta = ''
    while  not respuesta.startswith('j') and not respuesta.startswith('s'):
        print('¿Quieres jugar (j) o ver la solución (s)?')
        respuesta = input().lower()
    
    if respuesta.startswith('j'):
        numPasos = 0
        while not esGanadora(configuracionActual, numeroDeDiscos):
#            dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
            numPasos += 1
            torreInicial, torreFinal = movimientoUsuario(configuracionActual)
            realizaMovida(configuracionActual, torreInicial, torreFinal)
            dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
            dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
            
        print('El juego ha finalizado después de %s pasos.' % (numPasos))
        if numPasos == 2**numeroDeDiscos - 1:
            print('¡Felicidades, lo resolviste en el menor número de pasos!')
    elif respuesta.startswith('s'):
        dibujaPostes(colocaDiscos(configuracionActual, numeroDeDiscos), numeroDeDiscos)
        algoritmoHanoi(numeroDeDiscos, 0, 2, 1)  
    
    print('¿Quieres volver a jugar? (S o N)')
    if input().lower().startswith('n'):
        break
