import time

# Dibujo de las torres.
def dibujar():
    for fila in torres:
        for col in fila:
            if col == 0:
                print('                          ', end='')
            elif col == 1:
                print('        [Disco 1 ]        ', end='')
            elif col == 2:
                print('        [Disco 2 ]        ', end='')
            elif col == 3:
                print('        [Disco 3 ]        ', end='')
            elif col == 4:
                print('        [Disco 4 ]        ', end='')
            elif col == 5:
                print('        [Disco 5 ]        ', end='')
            elif col == 6:
                print('        [Disco 6 ]        ', end='')
            elif col == 7:
                print('        [Disco 7 ]        ', end='')
            elif col == 8:
                print('        [Disco 8 ]        ', end='')
            elif col == 9:
                print('        [Disco 9 ]        ', end='')
            elif col == 10:
                print('        [Disco 10]        ', end='')
        print()
    print("-" * 80)
    print("            1                        2                           3         ")
    time.sleep(t)


# Disco superior
def buscador_discos(col):
    fila = 0
    for i in range(discos + 1):
        if torres[fila][col] == 0:
            fila += 1
    if fila <= discos:
        return torres[fila][col]
    else:
        return 0

# Buscador de espacios
def buscador_espacios(col):
    fila = 0
    for i in range(discos + 1):
        if torres[fila][col] == 0:
            fila += 1
    return fila - 1

# Eliminar discos superior
def eliminar(col):
    fila = 0
    for i in range(discos + 1):
        if torres[fila][col] == 0:
            fila += 1
    if fila <= discos:
        torres[fila][col] = 0

# Suma del contador
def suma(X):
    A = 0
    for i in X:
        A += i
    return A

# Gráfico
def hanoi(n, partida=1, pivote=2, llegada=3):
    if 0 < n:
        hanoi(n - 1, partida, llegada, pivote)
        disco = buscador_discos(partida - 1)
        eliminar(partida - 1)
        X.append(1)
        torres[buscador_espacios(llegada - 1)][llegada - 1] = disco
        dibujar()
        print('Paso', sum(X))
        hanoi(n - 1, pivote, partida, llegada)

# Menu
def menu():
    print('Torres de Hanoi')
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
        X = []
        discos = int(input('Numero de discos: '))
        t = int(input('Tiempo entre movimientos: '))
        print('Desea ver la simulación: \n 1. Si\n 2. No')
        simular = int(input(''))
        if simular == 2:
            print('El minimo numero de paso es: ', 2 ** discos - 1)
        else:
            if 2 < discos and discos < 11:
                if discos == 3:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]]
                elif discos == 4:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0]]
                elif discos == 5:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0]]
                elif discos == 6:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0]]
                elif discos == 7:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0]]
                elif discos == 8:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0],
                              [8, 0, 0]]
                elif discos == 9:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0],
                              [8, 0, 0], [9, 0, 0]]
                elif discos == 10:
                    torres = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0],
                              [8, 0, 0], [9, 0, 0], [10, 0, 0]]
                dibujar()
                print('Posicion Inicial')
                hanoi(discos)
            print('\nEl minimo numero de paso es: ', 2 ** discos - 1)
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