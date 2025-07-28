#Tres en Raya
tablero = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(fila)

def verificar_ganador():
    # Filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False

def tablero_lleno():
    return all(casilla != " " for fila in tablero for casilla in fila)

def tres_en_raya(jugador, fila, columna):
    if tablero[fila][columna] != " ":
        print("Casilla ocupada. Elige otra.")
        return
    tablero[fila][columna] = jugador
    mostrar_tablero()

    if verificar_ganador():
        print("Ganó", jugador)
        return

    if tablero_lleno():
        print("Empate")
        return

    siguiente = "O" if jugador == "X" else "X"
    print("Juega", siguiente)

# Ejemplo de ejecución
tres_en_raya("X", 0, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 0, 1)
tres_en_raya("O", 1, 0)
tres_en_raya("X", 0, 2)  # Aquí gana X