#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:26:04 2020

@author: gerardo
"""

import random

def numeroAleatorio():
    unidades = str(random.randint(1, 9))
    decenas = str(random.randint(0, 9))
    centenas = str(random.randint(0, 9))
    
    return centenas + decenas + unidades

def pedirIntento():
    intentoUsuario = ''
    
    while len(intentoUsuario) != 3:
        print('Estoy pensando un número de tres cifras.')
        print('Intenta adivinarlo.')
        print('')
        print('¿Cuál es tu intento?')
    
        intentoUsuario = input()
        
    return intentoUsuario

def pistas(numeroGenerado, intentoJugador):
    listaErrores  = []
    for i in range(0,3):
        if intentoJugador[i] in numeroGenerado:
            if intentoJugador[i] == numeroGenerado[i]:
                print('Fermi')
            else:
                print('Dirac')
        else:
            listaErrores.append(intentoJugador[i])
    if len(listaErrores) == 3:
        print('Panecillo')
        

while True:
    numPC = numeroAleatorio()
    numeroIntentos = 10
    print('P A N E C I L L O S')
    print('')
    print('Pensaré en un número de tres cifras;')
    print('intenta adivinarlo!')
    print('')
    print('PISTAS:')
    print('* Fermi: acertaste un dígito en el lugar correcto;')
    print('* Dirac: acertaste un dígito pero no el lugar correcto;')
    print('* panecillos: no acertaste ningún dígito.')
    
    
    while numeroIntentos > 0:
       
        intentoPL = pedirIntento()
        
        if intentoPL == numPC:
            print('¡Felicidades, ganaste!')
            break
        else:
            pistas(numPC, intentoPL)
        numeroIntentos -= 1
    
    if numeroIntentos == 0:
        print('¡Lo sentimos, has perdido!')
        print('Estaba pensando en ' + numPC)
    
    print('¿Quieres volver a jugar?')
    if not input().lower().startswith('s'):
        break
    
    
        
    
    
    
            
            
        
