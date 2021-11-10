import string

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

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story
### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words.copy()

#Crea un diccionario y toma como parametro la variable de corrimiento
    def build_shift_dict(self, shift):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        diccionario = dict()
        for i in range(len(upper)):
            #Letras mayusculas
            diccionario[upper[i]] = upper[(i+shift)% len(upper)].upper()
            #Letras minusculas
            diccionario[lower[i]] = lower[(i+shift)% len(lower)].lower()
        return diccionario

#Devuelve el mensaje con el corrimiento
    def apply_shift(self, shift):
        Nuevas_letras = self.build_shift_dict(shift)
        mensaje = self.get_message_text()
        Mensaje_cifrado = ''
        for i in range(len(mensaje)):
            if mensaje[i] in string.ascii_letters:
                cambio = mensaje[i]
                Mensaje_cifrado += Nuevas_letras[cambio]
            else:
                Mensaje_cifrado += mensaje[i]
        return Mensaje_cifrado

'''
plaintext = Message('HELLO, este es carlos 1234')
print('Expected Output: KHOOR, hvwh hv fduorv 1234')
Diccionario = plaintext.build_shift_dict(3)
x = plaintext.apply_shift(3)
print('ver esto: ', x)
'''

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

'''
plaid = PlaintextMessage('HELLO, este es carlos 1234', 4)
print('Expected Output: KHOOR, hvwh hv fduorv 1234')
y = plaid.get_message_text_encrypted()
print('Actual Output:', y)
'''

class CiphertextMessage(Message):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        Lista = self.get_valid_words()
        Mejor = []
        Prueba = []
        for i in range(26):
            texto = self.apply_shift(i)
            Lista_mensaje = texto.split()
            for palabra in Lista_mensaje:
                if is_word(Lista, palabra):
                    Prueba.append(1)
                else:
                    Prueba.append(0)
            Mejor.append((sum(Prueba), i, texto))
            del Prueba[0:len(Prueba)]
        A = max(Mejor)
        mensaje = A[1:3]
        return mensaje

'''
# Pruebas para cifrar
plaintext = PlaintextMessage('HELLO', 2)
print('Expected Output: JGNNQ')
B = plaintext.get_message_text_encrypted()
print('Actual Output:', B)

# Example test case (PlaintextMessage)
plaintext_test = PlaintextMessage('Mehmet', 4)
print('Expected Output: Qilqix ')
A = plaintext_test.get_message_text_encrypted()
print('Actual Output:', A)

plaintext_test2 = PlaintextMessage('Python', 14)
print('Expected Output: Dmhvcb ')
C = plaintext_test2.get_message_text_encrypted()
print('Actual Output:', C)

# Example test case (CiphertextMessage)
print('ver esto')
ciphertext = CiphertextMessage('aioue')
print('Expected Output:', (24, 'hello'))

#Decifrar ejemplo
ciphertext_test2 = CiphertextMessage(' oqzogg')
print('Expected Output:', (1, 'fire'))
x = ciphertext_test2.decrypt_message()
print('Actual Output:', x)

prueba = CiphertextMessage('xbufs, gjsf')
print('Expected Output:', (1, 'water'))
Z = prueba.decrypt_message()
print('Actual Output:', Z)

Proof = get_story_string()
print(Proof)
Aver = CiphertextMessage(Proof)
H = Aver.decrypt_message()
print('la prueba', H)
'''
