import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# Palabra al azar
def choose_word(wordlist):
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    for i in list(secret_word):
        if i in letters_guessed:
            return True
        else:
            return False

def get_guessed_word(secret_word, letters_guessed):
    palabra = []
    for i in list(secret_word):
        if i in letters_guessed:
            palabra += i
        else:
            palabra.append('_')
    X = ' '.join(palabra)
    return X

def get_available_letters(letters_guessed):
    Abecedario = string.ascii_lowercase
    letras_disponibles = ''
    for i in Abecedario:
        if not (i in letters_guessed):
            letras_disponibles += i
    return letras_disponibles

# Dibujo del neneco
def neneco(vidas):
    if vidas == 6:
        print(' =========||\n     |    ||\n          ||\n          ||\n          ||\n          ||\n          ||')
    elif vidas == 5:
        print(' =========||\n     |    ||\n     0    ||\n          ||\n          ||\n          ||\n          ||')
    elif vidas == 4:
        print(' =========||\n     |    ||\n     0    ||\n     |    ||\n          ||\n          ||\n          ||')
    elif vidas == 3:
        print(' =========||\n     |    ||\n     0    ||\n    /|    ||\n          ||\n          ||\n          ||')
    elif vidas == 2:
        print(' =========||\n     |    ||\n     0    ||\n    /|\   ||\n          ||\n          ||\n          ||')
    elif vidas == 1:
        print(' =========||\n     |    ||\n     0    ||\n    /|\   ||\n    /     ||\n          ||\n          ||')
    elif vidas <= 0:
        print(' =========||\n     |    ||\n     0    ||\n    /|\   ||\n    / \   ||\n          ||\n          ||')

# Funcion principal
def hangman(secret_word):
    print('-'*40)
    print('Sea bienvenido')
    print('='*40)
    print('La palabra ha adivinar consta de', len(secret_word), 'letras las cuales', len(set(secret_word)), 'son distintas' )
    Vocal = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    vidas = 6
    Advertencias = 3
    print(secret_word)
    while vidas > 0:
        neneco(vidas)
        print('Cuenta con ', vidas, 'Vidas disponibles')
        print('Cuenta con ', Advertencias, 'Advertencias disponibles')
        print('Letras disponibles: ', get_available_letters(letters_guessed))
        Letra = str(input('Por favor ingrese una letra: ')).lower()
        if Letra in list(secret_word):
            if Letra in letters_guessed:
                print('Esta letra esta repetida \n Has cometido una Falta', get_guessed_word(secret_word, letters_guessed))
                if Advertencias > 0:
                    Advertencias -= 1
                elif Advertencias == 0:
                    print('Has excedido el minimo permitido de Advertencias \nPierdes una vida')
                    vidas -= 1
            else:
                letters_guessed.append(Letra)
                print('Buena esa vaquero: ', get_guessed_word(secret_word, letters_guessed))
        else:
            if Letra in letters_guessed:
                print('Esta letra esta repetida \n Has cometido una Falta', get_guessed_word(secret_word, letters_guessed))
                if Advertencias > 0:
                    Advertencias -= 1
                elif Advertencias == 0:
                    print('Has excedido el minimo permitido de Advertencias \nPierdes una vida')
                    vidas -= 1
            elif not Letra in string.ascii_lowercase:
                print('Este caracter no esta permitido,\n pierdes una advertencia', get_guessed_word(secret_word, letters_guessed))
                if Advertencias > 0:
                    Advertencias -= 1
                elif Advertencias == 0:
                    print('Has excedido el minimo permitido de Advertencias \nPierdes una vida')
                    vidas -= 1
            else:
                letters_guessed.append(Letra)
                if Letra in Vocal:
                    vidas -= 2
                    print('Golpe crítico \n Has perdido 2 vidas', get_guessed_word(secret_word, letters_guessed))
                else:
                    vidas -= 1
                    print('Golpe leve \n Has perdido 1 vida', get_guessed_word(secret_word, letters_guessed))
        print('-' * 40)
        Z = get_guessed_word(secret_word, letters_guessed).count('_')
        if Z == 0:
            neneco(vidas)
            print('En hora buena, habeis ganado')
            Puntaje = vidas * len(set(secret_word))
            print('Tuvo un puntaje de: \n', Puntaje, 'puntos')
            print('='*40)
            break
    while vidas <= 0:
        neneco(vidas)
        print('Lo has matado \nHabeis perdido')
        print('La palabra era:', secret_word)
        print('=' * 40)
        break

# Menu
def menu():
    print('Juego del Ahorcado')
    print('=' * 16)
    opc = int(input('Desea jugar: \n' +
                    '1. Si \n' +
                    '2. No \n' +
                    '3. Salir \n'))
    return opc

# Implementación del menú
opcion = 0
while opcion != 3:
    opcion = menu()
    if opcion == 1:
        wordlist = load_words()
        secret_word ='Programacion'.lower()
        '''
        secret_word = choose_word(wordlist).lower()
        '''
        hangman(secret_word)
        print('\n \n Desea regresar al menu: \n' +
                    '5. Si \n' +
                    '6. No')
        salir = int(input(''))
        if salir == 6:
            print('Vuelva Pronto')
            break

    if opcion == 2:
        print('Gracias por Participar')

    if opcion == 3:
        print("Vuelva Pronto")
    print('-' * 80)

