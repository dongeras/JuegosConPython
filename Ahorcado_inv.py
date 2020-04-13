import random
IMAGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def cuentaLetras(): #Se pregunta el número de letras de la palabra secreta
    while True: # El ciclo se repetirá hasta que el input sea un número 
        print('¿Cuántas letras tiene tu palabra secreta?')
        numeroLetras = input()
        
        if numeroLetras in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            break# Si numeroLetras es un número se rompe el ciclo.
    
    secreto = list() #Se crea una lista con tantos elementos como letras en la palabra secreta
    for i in range(int(numeroLetras)):
        secreto.append('*') #Se llena la lista secreto con asteriscos.
    return secreto

def pantallaInfo(IMAGENES, secret, errores): # Muestra en pantalla el estado actual del juego
    print(IMAGENES[len(errores)])
    print('')
    
    print('Los intentos fallidos son: ', end='')
    for i in range(0, len(errores)):
        print(errores[i], end=' ')
    print('')
    
    print('La palabra secreta es: ', end = ' ' )
    for i in range(0, len(secret)):
        print(secret[i], end = ' ')
    
def eligeLetra(vocales, consonantes):       # Se elige una letra al azar
    if len(vocales) > 0:                    # Se verifica que vocales no este vacía
        eligeAzar = random.randint(1, 3)    # La eleccion entre vocales y consonantes es al azar
        if eligeAzar < 3:                   # Elegir una vocal tiene más peso.
            intento = random.choice(vocales)
            vocales.remove(intento)
        else:
            intento = random.choice(consonantes)
            consonantes.remove(intento)
    else:                                   # Si ya no hay vocales que elegir no hay de otra
        intento = random.choice(consonantes)
        consonantes.remove(intento)
        
    return intento                          # Se regresa un intento

def intentar(intento, secret):      # Se pregunta si el intento es correcto
    posiciones = []
    print('¿ ' + intento + ' está en la palabra secreta? (si o no)')
    if input().lower().startswith('s'):
        print('¿Cuantas veces aparece?') #Se pregunta cuantas veces aparece la letra
        repeticiones = int(input())
        for i in range(repeticiones):
            print(str(i+1)+'a posición:') #Se preguntan las posiciones del intento en la palabra
            posiciones.append(int(input()))
        for i in range(0, len(posiciones)):
            secret[posiciones[i]-1] = intento #Se remplaza la palabra correcta en la pos. indicada
    else:
        print('¡Me quiero volver chango!') #El intento falló
    return secret


            
        
     

