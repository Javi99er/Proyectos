import string
from ps4b import Message
from ps4b import PlaintextMessage
from ps4b import CiphertextMessage
from ps4c import SubMessage
from ps4c import EncryptedSubMessage

#Archivo
def abrir_archivo(x):
    f = open(x, "r")
    abrir = str(f.read())
    f.close()
    return abrir

# Menu
def menu():
    print('Cifrado y decifrado ')
    print('=' * 22)
    opc = int(input('Que desea realizar: \n' +
                    '1. Cifrar un mensaje \n' +
                    '2. Decifrar un mensaje \n'))
    print('-' * 40)
    return opc

# Implementación del menú
opcion = 0
while opcion != 3:
    opcion = menu()
    if opcion == 1:
        #El mensaje que se desea cifrar
        print('Ingrese el archivo que desea cifrar')
        documento = input('Mensaje: ')
        '''
        archivo = abrir_archivo(documento)
        '''
        # Tipo de cifrado
        print('-' * 40)
        print('Que metodo desea utilizar: \n' +
              '1. Cifrado Cesar \n' +
              '2. Cifrado por sustitucion')
        Tipo = int(input(''))
        print('-' * 40)
        # Cifrado Cesar
        if Tipo == 1:
            k = int(input('Ingrese la constante de corrimiento: '))
            llamado1 = PlaintextMessage(documento, k)
            print('Su mensaje es: \n', llamado1.get_message_text_encrypted())
        # Cifrado por sustitucion
        if Tipo == 2:
            llamado2 = SubMessage(documento)
            Permutacion = str(input('Ingrese un nuevo orden para las vocales \n'))
            Vocales = llamado2.build_transpose_dict(Permutacion)
            print('Su mensaje es: \n', llamado2.apply_transpose(Vocales))

    if opcion == 2:
        print('Ingrese el archivo que desea decifrar')
        Documento = input('Mensaje: ')
        Archivo = abrir_archivo(Documento)
        print('-' * 40)

        # Decifrar por Cesar
        llamado3 = CiphertextMessage(Archivo)
        x = llamado3.decrypt_message()

        # Decifrar por sustitucion
        llamado4 = EncryptedSubMessage(Archivo)
        y = llamado4.decrypt_message()

        if y is not None:
            print('El mensaje era: \n', y)
            print('Cifrado de tipo Sustitucion')
        else:
            print('El mensaje era: \n', x)
            print('Cifrado de tipo Cesar')

    print('-' * 80)





