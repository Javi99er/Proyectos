import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words.copy()


    def build_transpose_dict(self, vowels_permutation):
        Diccionario = dict()
        for indice in range(5):
            Diccionario[VOWELS_LOWER[indice]] = vowels_permutation[indice].lower()
        for indice in range(5):
            Diccionario[VOWELS_UPPER[indice]] = vowels_permutation[indice].upper()
        for consonante in CONSONANTS_LOWER:
            Diccionario[consonante] = consonante
        for consonante in CONSONANTS_UPPER:
            Diccionario[consonante] = consonante
        return Diccionario

    def apply_transpose(self, transpose_dict):
        mensaje = self.get_message_text()
        mensaje_cifrado = ""
        for i in range(len(mensaje)):
            if mensaje[i] in VOWELS_UPPER:
                cambio = mensaje[i]
                mensaje_cifrado += transpose_dict[cambio]
            elif mensaje[i] in VOWELS_LOWER:
                cambio = mensaje[i]
                mensaje_cifrado += transpose_dict[cambio]
            else:
                mensaje_cifrado += mensaje[i]
        return mensaje_cifrado

'''
#Llamo a la clase
mensaje = SubMessage("Hello World! sOy El 1234")
#Letras que seran permutadas
permutacion = "UAeio"
# llamo de la clase a la funcion del constructor
# Me crea un nuevo diccionario
diccionario = mensaje.build_transpose_dict(permutacion)
print("Original message:", mensaje.get_message_text(), "Permutation:", permutacion)
print("Expected encryption:", "Halli Wirld! sIy Al 1234")
Transponer = mensaje.apply_transpose(diccionario)
print("Actual encryption:", Transponer )
'''

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        Listado = self.valid_words
        permutaciones = get_permutations(VOWELS_LOWER)
        for i in permutaciones:
            Contador = 0
            Mensaje = []
            vowels_permutation = i
            Diccionario_transposicion = SubMessage.build_transpose_dict(self, vowels_permutation)
            Mensaje_transpuesto = SubMessage.apply_transpose(self, Diccionario_transposicion)
            Listado_mensaje_transpuesto = Mensaje_transpuesto.split()
            No_palabras_en_mensaje_transpuesto = len(Listado_mensaje_transpuesto)
            for elemento in Listado_mensaje_transpuesto:
                if elemento.isalpha():
                    if is_word(Listado, elemento):
                        Contador += 1
                    else:
                        Mensaje.append(elemento)
                else:
                    Contador += 1
                    Mensaje.append(elemento)
            if Contador >= No_palabras_en_mensaje_transpuesto:
                Salida = ''.join(Mensaje)
                return (Mensaje_transpuesto, i)

'''
# Ejwmploa
mensaje = SubMessage("Hello World! sOy El 1234")
permutacion = "UAeio"
diccionario = mensaje.build_transpose_dict(permutacion)
print("Original message:", mensaje.get_message_text(), "Permutation:", permutacion)
print("Expected encryption:", "Halli Wirld! sIy Al 1234")
x = mensaje.apply_transpose(diccionario)
print("Actual encryption:", x)

citado = EncryptedSubMessage('Halli Wirld! 1234 et e')
y = citado.decrypt_message()
print("Decrypted message:", y)
'''

