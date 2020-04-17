#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:04:47 2020

@author: gerardo
"""
import random

def preguntarLetra(): #Regresa la letra del jugador y de la computadora
    while True:
        print('¿Con qué letra quieres jugar? (X ó O)')
        letraJ = input().upper()
        if letraJ == 'X':
            letraPC = 'O'
            return letraJ, letraPC
        if letraJ == 'O':
            letraPC = 'X'
            return letraJ, letraPC
        
def volado(letraJ, letraPC): #Regresa el jugador que va primero.
    listaJugadores = [letraJ, letraPC]
    primerTurno = random.choice(listaJugadores)
    
    return primerTurno
        
def muestraTablero(tablero): #Imprime en pantalla el estado actual del tablero
   print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9]) 
   print('-----------') 
   print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6]) 
   print('-----------') 
   print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])

def jugada(tablero, pos, letraTurno):# Actualiza el tablero dada una jugada
    
    tablero[pos] = letraTurno
    
def tableroganador(tablero, le): #Devuelve True si el jugador le tiene un tablero ganador

    return { tablero[7] == le and tablero[8] == le and tablero[9] == le or
            
             tablero[4] == le and tablero[5] == le and tablero[6] == le or
             
             tablero[1] == le and tablero[2] == le and tablero[3] == le or
             
             tablero[7] == le and tablero[4] == le and tablero[1] == le or
             
             tablero[8] == le and tablero[5] == le and tablero[2] == le or
             
             tablero[9] == le and tablero[6] == le and tablero[3] == le or 
             
             tablero[7] == le and tablero[5] == le and tablero[3] == le or 
             
             tablero[9] == le and tablero[5] == le and tablero[1] == le }
    
    
def empate(tablero): #Evalúa si hay un empate
    
    for i in range(1,len(tablero)):
        if tablero[i] == ' ' :
            return False
    print('¡Uy, empatamos!')    
    return True
    
def duplicandoTablero(tablero):
    
    tableroDup = []
    
    for i in tablero:
        tableroDup.append(i)
    
    return tableroDup 

        

    
    


#letraJugador, letraCom = preguntarLetra()

#primerTurn = volado(letraJugador, letraCom)

tab = [' '] * 10



