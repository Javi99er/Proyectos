import string
secret_word = 'estupefacto'
print('I am thinking of a word that is {} letters long'.format(len(secret_word)))

Vidas = 6
Vocal = ['a', 'e', 'i', 'o', 'u']
Letra = input('Por favor ingrese una letra: ').lower()

if Letra in Vocal:
    Vidas -= 2
else:
    Vidas += 1

print(Vidas)
print('-'*40)


Abecedario = string.ascii_lowercase
print(Abecedario)

def longitud(secret_word):
    Tamaño = []
    for i in secret_word:
        Tamaño.append(str(i))
    print(len(set(Tamaño)))

longitud(secret_word)

print(' =========||\n     |    ||\n          ||\n          ||\n          ||\n          ||\n          || ')
print(' =========||\n     |    ||\n          ||\n          ||\n          ||\n          ||\n          ||')
print(' =========||\n     |    ||\n     0    ||\n          ||\n          ||\n          ||\n          ||')
print(' =========||\n     |    ||\n     0    ||\n     |    ||\n          ||\n          ||\n          ||')
print(' =========||\n     |    ||\n     0    ||\n    /|    ||\n          ||\n          ||\n          ||')
print(' =========||\n     |    ||\n     0    ||\n    /|\   ||\n          ||\n          ||\n          ||')
print(' =========||\n     |    ||\n     0    ||\n    /|\   ||\n    /     ||\n          ||\n          ||')
print(' =========||\n     |    ||\n     0    ||\n    /|\   ||\n    / \   ||\n          ||\n          ||')

