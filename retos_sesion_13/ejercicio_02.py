
# Imprimir los 20 primeros números que sean múltiplos de 2 y 5 (es decir, múltiplos de 10)
contador = 0
numero = 1

while contador < 20:
    if numero % 2 == 0 and numero % 5 == 0:
        print(numero)
        contador += 1
    numero += 1