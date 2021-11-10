# Menu
def menu():
    print('Ahorcado')
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
        print('El numero de letras sin repetir de la palabra es ', longitud(secret_word))
        secret_word = chooseWord(wordlist).lower()
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
