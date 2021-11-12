import math
def problema1(numero):
    while numero%2 == 0: numero//=2
    cont = 3
    while cont*cont <= numero:
        if numero % cont == 0:
            numero//= cont
        else:
            cont+=2
    Respuesta = 2 if numero== 1 else numero
    print("Problema 1 respuesta",Respuesta)

def problema2(numero):
    x = sum([int(c) for c in str(numero)])
    print("Problema 2 respuesta", x)


def primo(numero):
    if numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(numero)) + 1, 2):
            if numero % i == 0:
                return False
    return True

def problema3(numero):
    Respuesta = 0
    for i in range(2, numero):
        if primo(i):
            Respuesta += i
    print("Problema 3 respuesta",Respuesta)

problema1(600851475143)
problema2(21000)
problema3(2000000)