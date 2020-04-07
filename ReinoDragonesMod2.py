#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:31:59 2020

@author: gerardo
"""

import random
import time

def Introduccion():
    print('Te encuentras en el reino de los dragones.')
    print('Has sido contratado para cazar un dragón.')
    print('')
    print('Te acercas a la guarida del dragón...')
    time.sleep(2)
    
    print('El dragón se da cuenta de tu presencia y')
    print('comienza la batalla...')
    
    HPdragon = 100
    HPusuario = 100
    
    return HPdragon, HPusuario

def Batalla(pvDragon, pvUsuario):
    respuesta = ''
    while respuesta != 'A' and respuesta != 'D':
        print('¿Deseas atacar (A) o defender (D)')
        respuesta = input()
    
    accionDragon = random.choice(['A', 'D'])
    print(accionDragon)
    if respuesta == 'A'  and accionDragon == 'A':
        print('El dragón también decició atacar.')
        dañoUsuario = random.randint(1, 10)
        dañoDragon = random.randint(1,10)
        
        pvUsuario = pvUsuario - dañoUsuario
        pvDragon = pvDragon - dañoDragon
    elif respuesta == 'A'  and accionDragon == 'D':
        print('El dragón decidió defender.')
        dañoDragon = random.randint(0, 5)
        
        pvDragon = pvDragon - dañoDragon
    elif respuesta == 'D'  and accionDragon == 'A':
        print('el dragón decidió atacar.')
        dañoUsuario = random.randint(0, 5)
        
        pvUsuario = pvUsuario - dañoUsuario
    else:
        print('nadie ataco. Aprovechen a curarse')
        curaUsuario = 10
        curaDragon = 10
        
        pvUsuario = pvUsuario + curaUsuario
        pvDragon = pvDragon + curaDragon
    
    return pvDragon, pvUsuario


volver = 's'
while volver == 's':

    hpDragon, hpUsuario = Introduccion()

    while hpDragon > 0 and hpUsuario > 0:
        hpDragon, hpUsuario = Batalla(hpDragon, hpUsuario)
        
        print('Tus puntos de vida son ' + str(hpUsuario))
        print('')
        
        print('Los puntos de vida del dragón son ' + str(hpDragon))
        print('')

    if hpDragon < 0:
        print('¡Felicidades, derrotaste al dragón!')
    if hpUsuario <0:
        print('El dragón te ha derrotado.')
    

    print('¿quieres volver a jugar?')
    volver = input()
    
    





















    