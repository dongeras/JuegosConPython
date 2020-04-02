import random


print('Trataré de adivinar tu número que está entre "a" y "b" ')
print('Dime quién es "a".')
a = input()
a = int(a)
print('Dime quién es "b".')
b = input()
b = int(b)

numeroIntentos = 0

for numeroIntentos in range(6):

    intento = int(a + (b-a)/2)

    print('¿El número que pensaste es' + str(intento) + '?')
    print('Si son iguales pon "="; si tu número es menor pon "<"; si es tu número es mayor pon ">".')
    respuesta = input()

    if respuesta == '<':
        a = a
        b = intento
        vicotria = False
    if respuesta == '>':
        a = intento
        b = b
        victoria = False
    if respuesta == '=':
        victoria = True
        break
    
if victoria == True:
    print('¡Yupi, gané!')

if victoria != True:
    print('¡Oh no, perdí!')
        
