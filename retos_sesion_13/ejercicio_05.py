#Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
filas = 8
columnas = 8

for fila in range(filas):
    linea = ''
    for columna in range(columnas):
        if (fila + columna) % 2 == 0:
            linea += '#'
        else:
            linea += '*'
    print(linea)