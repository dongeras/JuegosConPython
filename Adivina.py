#Este programa genera un número aleatorio y le pide al usuario
# que lo adivine

import random

numeroIntentos = 0

print("¡Hola! ¿Cómo te llamas?")
nombre = input()

numero = random.randint(1,100)

print("Bienvenido, " + nombre + ". Estoy pensando en un número entre 1 y 100.")

for numeroIntentos in range(6):
    print("Adivina ¿en qué número estoy pensando?")
    intento = input()
    intento = int(intento)

    if intento < numero:
        print("Tu intento es muy pequeño.")

    if intento > numero:
        print("Tu intento es muy grande.")

    if intento == numero:
        break

if intento == numero:
    numeroIntentos = numeroIntentos + 1
    numeroIntentos = str(numeroIntentos)
    print("¡Felicidades, " + nombre + "! Adivinaste el número en " + numeroIntentos + " intentos.")

if intento != numero:
    numero = str(numero)
    print("¡Lástima! El número en el que estaba pensando es " + numero + "." )


    

    
