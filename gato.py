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

    return ((tablero[7] == le and tablero[8] == le and tablero[9] == le) or
            
             (tablero[4] == le and tablero[5] == le and tablero[6] == le) or
             
             (tablero[1] == le and tablero[2] == le and tablero[3] == le) or
             
             (tablero[7] == le and tablero[4] == le and tablero[1] == le) or
             
             (tablero[8] == le and tablero[5] == le and tablero[2] == le) or
             
             (tablero[9] == le and tablero[6] == le and tablero[3] == le) or 
             
             (tablero[7] == le and tablero[5] == le and tablero[3] == le) or 
             
             (tablero[9] == le and tablero[5] == le and tablero[1] == le))
    
    
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

def espacioVacio(tablero, pos): #Regresa Verdadero si el espacio está vacío

    return tablero[pos] == ' '

def movimientoUsuario(tablero, letraUsuario):
    
    movimiento = ''
    
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not espacioVacio(tablero, int(movimiento)):
        print('¿Cuál es tu movimento? (1, 2, 3, 4, 5, 6, 7, 8, 9)')
        movimiento = input()
        
    tablero[int(movimiento)] = letraUsuario
    
def jugadaAzar(tablero, listaPosiciones):
    
    posiblesSitios = []
    
    for i in listaPosiciones:
        if espacioVacio(tablero, i):
            posiblesSitios.append(i)
            
    if len(posiblesSitios) !=0:
        return random.choice(posiblesSitios)
    else:
        return None
    
    #La siguiente función regresa la jugada de la PC
def jugadaComputadora(tablero, letraPC, letraUsuario):
    
    espaciosVacios = []
    
    #1.- ¿Hay jugada ganadora?
    for j in range(1, len(tablero)):
        if tablero[j] == ' ':
            espaciosVacios.append(j)
    
    
    
    for i in espaciosVacios:
        copiaTablero = duplicandoTablero(tablero)
        jugada(copiaTablero, i, letraPC)
        if tableroganador(copiaTablero, letraPC):
            return i
        
    #2.- Bloquear jugadas ganadoras del contrario    
    for i in espaciosVacios:
        copiaTablero = duplicandoTablero(tablero)
        jugada(copiaTablero, i, letraUsuario)
        if tableroganador(copiaTablero, letraUsuario):
            return i
    
    # 3.- Tratar de jugar en una esquina
    listaEsquinas = [1, 3, 7, 9]
    movimiento = jugadaAzar(tablero, listaEsquinas)
    
    if movimiento != None:
        return movimiento
    
    # 4.- Tratar de jugar en el centro
    if espacioVacio(tablero, 5):
        return 5
    
    # 5. Elegir entre los lados
    
    listaLados = [2, 4, 6, 8]
    return jugadaAzar(tablero, listaLados)


  
        
        
        
        
        
volverAJugar = True

while volverAJugar:    
    print('¡Bienvenido al Gato!')

    letraJugador, letraCom = preguntarLetra()
    primerTurn = volado(letraJugador, letraCom)
    tab = [' '] * 10

    if primerTurn == letraJugador:
        turno = 'El Usuario'
    else:
        turno = 'La Computadora'
    
    print( turno + ' tirará primero.' )

    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El Usuario':
            muestraTablero(tab)
        
            movimientoUsuario(tab, letraJugador)
        
            if tableroganador(tab, letraJugador):
                print('¡Ganaste!')
                juegoEnCurso = False
                break
            if empate(tab):
                juegoEnCurso = False
                break
        
            turno = 'La Computadora'
        
        if turno == 'La Computadora':
            jugadaPC = jugadaComputadora(tab, letraCom, letraJugador)
       
            if jugadaPC in range(1, 10):
                jugada(tab, jugadaPC, letraCom)
       
            if tableroganador(tab, letraCom):
                print('¡Perdiste!')
                juegoEnCurso = False
                break
            if empate(tab):
                juegoEnCurso = False
                break
     
            turno = 'El Usuario'
        
    print('¿quieres volver a jugar? (Sí o No)')
    volverAJugar = input().lower().startswith('s')
    
       
    
       


