import random 
import time
import os

def adivina():
    
    numeroIntentos = 0

    print("¡Bienvenido a mi guarida! Adivina el entero que estoy pensando")
    print('entre 1 y 50 y te llevaré a la cueva del dragón amistoso.')
    print('Si fracasas, te llevaré con el dragón hambriento.')
    print('Tienes 6 intentos.')
    print()

    numero = random.randint(1,50)


    for numeroIntentos in range(6):
        print("Adivina en qué número estoy pensando?")
        intento = input()
        intento = int(intento)

        if intento < numero:
            print("Tu intento es muy pequeño.")

        if intento > numero:
            print("Tu intento es muy grande.")

        if intento == numero:
            break

    if intento == numero:
    
        print("¡Has sido más astuto que yo, mereces el tesoro!")
       

    if intento != numero:
        numero = str(numero)
        print("¡Lástima! El número en el que estaba pensando es " + numero + "." )
       
    
    return 

def mostrarIntroduccion():
    print()
    print('Estás en una tierra llena de dragones. Frente a ti')
    print('hay tres cuevas: en una de ellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo; en otra, el dragón')
    print('es codicioso y hambriento y te deborará inmediatamente; por ')
    print('último, encontrarás un mago curioso que jugará contigo.')
    print()
    
def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2' and cueva != '3':
        print('¿A qué cueva quieres entrar? (1, 2 ó 3)')
        cueva = input()
    
    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    
    listaCuevas = ["1", "2", "3"]
   
    cuevaMago, cuevaAmigo, cuevaEnemigo = random.sample(listaCuevas, 3)
    
    if cuevaElegida == cuevaMago:
        adivina()
        
    if cuevaElegida == cuevaAmigo:
        print('Te encuentras con el dragón amistoso y comparte su tesoro.')
    
    if cuevaElegida == cuevaEnemigo:
        print('Te encuentras con el dragón hambriento y te debora!')
 
        
JugarDeNuevo = 'si'

while JugarDeNuevo == 'si' or JugarDeNuevo == 's':
    
    os.system('clear')
    mostrarIntroduccion()
    
    numeroDeCueva = elegirCueva()
    
    explorarCueva(numeroDeCueva)
    
    print('¿Quieres jugar de nuevo? (si (s) o no (n))')
    JugarDeNuevo = input()
 
 



